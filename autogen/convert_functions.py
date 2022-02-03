import os
import re
from common import *

rejects = ""
integer_types = ["u8", "u16", "u32", "u64", "s8", "s16", "s32", "s64", "int"]
number_types = ["f32", "float"]
param_override_build = {}
out_filename = 'src/pc/lua/smlua_functions_autogen.c'
docs_lua_functions = 'docs/lua/functions.md'

###########################################################

template = """/* THIS FILE IS AUTOGENERATED */
/* SHOULD NOT BE MANUALLY CHANGED */

#include "smlua.h"

#include "game/level_update.h"
#include "game/area.h"
#include "game/mario.h"
#include "game/mario_step.h"
#include "game/mario_actions_stationary.h"
#include "audio/external.h"
#include "object_fields.h"
#include "engine/math_util.h"
#include "engine/surface_collision.h"
#include "pc/network/network_utils.h"

$[FUNCTIONS]

void smlua_bind_functions_autogen(void) {
    lua_State* L = gLuaState;
$[BINDS]
}
"""

###########################################################

param_vec3f_before_call = """
    f32* $[IDENTIFIER] = smlua_get_vec3f_from_buffer();
    $[IDENTIFIER][0] = smlua_get_number_field($[INDEX], "x");
    if (!gSmLuaConvertSuccess) { return 0; }
    $[IDENTIFIER][1] = smlua_get_number_field($[INDEX], "y");
    if (!gSmLuaConvertSuccess) { return 0; }
    $[IDENTIFIER][2] = smlua_get_number_field($[INDEX], "z");
"""

param_vec3f_after_call = """
    smlua_push_number_field($[INDEX], "x", $[IDENTIFIER][0]);
    smlua_push_number_field($[INDEX], "y", $[IDENTIFIER][1]);
    smlua_push_number_field($[INDEX], "z", $[IDENTIFIER][2]);
"""

param_override_build['Vec3f'] = {
    'before': param_vec3f_before_call,
    'after': param_vec3f_after_call
}

param_vec3s_before_call = """
    s16* $[IDENTIFIER] = smlua_get_vec3s_from_buffer();
    $[IDENTIFIER][0] = smlua_get_integer_field($[INDEX], "x");
    if (!gSmLuaConvertSuccess) { return 0; }
    $[IDENTIFIER][1] = smlua_get_integer_field($[INDEX], "y");
    if (!gSmLuaConvertSuccess) { return 0; }
    $[IDENTIFIER][2] = smlua_get_integer_field($[INDEX], "z");
"""

param_vec3s_after_call = """
    smlua_push_integer_field($[INDEX], "x", $[IDENTIFIER][0]);
    smlua_push_integer_field($[INDEX], "y", $[IDENTIFIER][1]);
    smlua_push_integer_field($[INDEX], "z", $[IDENTIFIER][2]);
"""

param_override_build['Vec3s'] = {
    'before': param_vec3s_before_call,
    'after': param_vec3s_after_call
}

############################################################################

header_h = ""

def reject_line(line):
    if len(line) == 0:
        return True
    if '(' not in line:
        return True
    if ')' not in line:
        return True
    if ';' not in line:
        return True

def normalize_type(t):
    t = t.strip()
    if ' ' in t:
        parts = t.split(' ', 1)
        t = parts[0] + ' ' + parts[1].replace(' ', '')
    return t

def alter_type(t):
    if t.startswith('enum '):
        return 'int'
    return t


############################################################################

def build_param(param, i):
    ptype = alter_type(param['type'])
    pid = param['identifier']

    if ptype in param_override_build:
        return param_override_build[ptype]['before'].replace('$[IDENTIFIER]', str(pid)).replace('$[INDEX]', str(i))
    elif ptype == 'bool':
        return '    %s %s = smlua_to_boolean(L, %d);\n' % (ptype, pid, i)
    elif ptype in integer_types:
        return '    %s %s = smlua_to_integer(L, %d);\n' % (ptype, pid, i)
    elif ptype in number_types:
        return '    %s %s = smlua_to_number(L, %d);\n' % (ptype, pid, i)
    else:
        lot = translate_type_to_lot(ptype)
        s = '  %s %s = (%s)smlua_to_cobject(L, %d, %s);' % (ptype, pid, ptype, i, lot)

        if '???' in lot:
            s = '//' + s + ' <--- UNIMPLEMENTED'
        else:
            s = '  ' + s

        return s + '\n'

def build_param_after(param, i):
    ptype = param['type']
    pid = param['identifier']

    if ptype in param_override_build:
        return param_override_build[ptype]['after'].replace('$[IDENTIFIER]', str(pid)).replace('$[INDEX]', str(i))
    else:
        return ''

def build_call(function):
    ftype = alter_type(function['type'])
    fid = function['identifier']

    ccall = '%s(%s)' % (fid, ', '.join([x['identifier'] for x in function['params']]))

    if ftype == 'void':
        return '    %s;\n' % ccall

    lfunc = 'UNIMPLEMENTED -->'
    if ftype in integer_types:
        lfunc = 'lua_pushinteger'
    elif ftype in number_types:
        lfunc = 'lua_pushnumber'
    elif ftype == 'bool':
        lfunc = 'lua_pushboolean'

    return '    %s(L, %s);\n' % (lfunc, ccall)

def build_function(function, do_extern):
    s = ''

    if len(function['params']) <= 0:
        s = 'int smlua_func_%s(UNUSED lua_State* L) {\n' % function['identifier']
    else:
        s = 'int smlua_func_%s(lua_State* L) {\n' % function['identifier']

    s += '    if(!smlua_functions_valid_param_count(L, %d)) { return 0; }\n\n' % len(function['params'])

    i = 1
    for param in function['params']:
        s += build_param(param, i)
        s += '    if (!gSmLuaConvertSuccess) { return 0; }\n'
        i += 1
    s += '\n'

    if do_extern:
        s += '    extern %s\n' % function['line']

    s += build_call(function)

    i = 1
    for param in function['params']:
        s += build_param_after(param, i)
        i += 1
    s += '\n'

    s += '    return 1;\n}\n'

    function['implemented'] = 'UNIMPLEMENTED' not in s
    if 'UNIMPLEMENTED' in s:
        s = "/*\n" + s + "*/\n"

    return s + "\n"

def build_functions(processed_files):
    s = ''
    for processed_file in processed_files:
        s += gen_comment_header(processed_file['filename'])

        for function in processed_file['functions']:
            s += build_function(function, processed_file['extern'])
    return s

def build_bind(function):
    s = 'smlua_bind_function(L, "%s", smlua_func_%s);' % (function['identifier'], function['identifier'])
    if function['implemented']:
        s = '    ' + s
    else:
        s = '    //' + s + ' <--- UNIMPLEMENTED'
    return s + "\n"

def build_binds(processed_files):
    s = ''
    for processed_file in processed_files:
        s += "\n    // " + processed_file['filename'] + "\n"

        for function in processed_file['functions']:
            s += build_bind(function)
    return s

############################################################################

def process_function(line):
    function = {}

    line = line.strip()
    function['line'] = line

    line = line.replace('UNUSED', '')

    match = re.search('[a-zA-Z0-9_]+\(', line)
    function['type'] = normalize_type(line[0:match.span()[0]])
    function['identifier'] = match.group()[0:-1]

    function['params'] = []
    params_str = line.split('(', 1)[1].rsplit(')', 1)[0].strip()
    if len(params_str) == 0 or params_str == 'void':
        pass
    else:
        param_index = 0
        for param_str in params_str.split(','):
            param = {}
            param_str = param_str.strip()
            if param_str.endswith('*') or ' ' not in param_str:
                param['type'] = normalize_type(param_str)
                param['identifier'] = 'arg%d' % param_index
            else:
                match = re.search('[a-zA-Z0-9_]+$', param_str)
                param['type'] = normalize_type(param_str[0:match.span()[0]])
                param['identifier'] = match.group()
            function['params'].append(param)
            param_index += 1

    return function

def process_functions(file_str):
    functions = []
    for line in file_str.splitlines():
        if reject_line(line):
            global rejects
            rejects += line + '\n'
            continue
        functions.append(process_function(line))

    functions = sorted(functions, key=lambda d: d['identifier']) 
    return functions

def process_file(fname):
    processed_file = {}
    processed_file['filename'] = fname.replace('\\', '/').split('/')[-1]
    processed_file['extern'] = fname.endswith('.c')

    with open(fname) as file:
        processed_file['functions'] = process_functions(file.read())

    return processed_file

def process_files():
    processed_files = []
    dir_path = os.path.dirname(os.path.realpath(__file__)) + '/lua_functions/'
    files = sorted(os.listdir(dir_path))
    for f in files:
        processed_files.append(process_file(dir_path + f))
    return processed_files

############################################################################

def doc_function_index(processed_files):
    s = '# Supported Functions\n'
    for processed_file in processed_files:
        s += '- %s\n' % processed_file['filename']
        for function in processed_file['functions']:
            s += '   - [%s](#%s)\n' % (function['identifier'], function['identifier'])
        s += '\n<br />\n\n'
    return s

def doc_function(function):
    if not function['implemented']:
        return ''

    fid = function['identifier']
    s = '\n## [%s](#%s)\n' % (fid, fid)

    rtype, rlink = translate_type_to_lua(function['type'])
    param_str = ', '.join([x['identifier'] for x in function['params']])

    s += "\n### Lua Example\n"
    if rtype != None:
        s += "`local %sValue = %s(%s)`\n" % (rtype, fid, param_str)
    else:
        s += "`%s(%s)`\n" % (fid, param_str)

    s += '\n### Parameters\n'
    if len(function['params']) > 0:
        s += '| Field | Type |\n'
        s += '| ----- | ---- |\n'
        for param in function['params']:
            pid = param['identifier']
            ptype = param['type']
            ptype, plink = translate_type_to_lua(ptype)

            if plink:
                s += '| %s | [%s](structs.md#%s) |\n'  % (pid, ptype, ptype)
                continue

            s += '| %s | %s |\n'  % (pid, ptype)

    else:
        s += '- None\n'

    s += '\n### Returns\n'
    if rtype != None:
        if rlink:
            s += '[%s](structs.md#%s)\n' % (rtype, rtype)
        else:
            s += '- %s\n' % rtype
    else:
        s += '- None\n'


    s += '\n### C Prototype\n'
    s += '`%s`\n' % function['line'].strip()

    s += '\n[:arrow_up_small:](#)\n\n<br />\n'

    return s

def doc_functions(functions):
    s = ''
    for function in functions:
        s += doc_function(function)
    return s

def doc_files(processed_files):
    s = '## [:rewind: Lua Reference](lua.md)\n\n'
    s += doc_function_index(processed_files)
    for processed_file in processed_files:
        s += '\n---'
        s += '\n# functions from %s\n\n<br />\n\n' % processed_file['filename']
        s += doc_functions(processed_file['functions'])

    with open(get_path(docs_lua_functions), 'w') as out:
        out.write(s)

############################################################################

def main():
    processed_files = process_files()

    built_functions = build_functions(processed_files)
    built_binds = build_binds(processed_files)

    filename = get_path(out_filename)
    with open(filename, 'w') as out:
        out.write(template.replace("$[FUNCTIONS]", built_functions).replace("$[BINDS]", built_binds))
    print('REJECTS:')
    print(rejects)
    doc_files(processed_files)

if __name__ == '__main__':
   main()