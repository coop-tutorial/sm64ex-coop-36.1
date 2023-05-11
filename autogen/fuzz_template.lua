-- $[STRUCTS]

--------

function FuzzVec3s(struct)
    struct.x = 0
    struct.y = 0
    struct.z = 0
end

function FuzzVec3f(struct)
    struct.x = 0
    struct.y = 0
    struct.z = 0
end

function FuzzVec4s(struct)
    struct.x = 0
    struct.y = 0
    struct.z = 0
    struct.w = 0
end

function FuzzVec4f(struct)
    struct.x = 0
    struct.y = 0
    struct.z = 0
    struct.w = 0
end

function FuzzMat4(struct)
    struct.a = 0
    struct.b = 0
    struct.c = 0
    struct.d = 0
    struct.e = 0
    struct.f = 0
    struct.g = 0
    struct.h = 0
    struct.i = 0
    struct.j = 0
    struct.k = 0
    struct.l = 0
    struct.m = 0
    struct.n = 0
    struct.o = 0
    struct.p = 0
end

--------

function rnd_string()
    t = { 0, "test", "this is a very long string this is a very long string this is a very long string this is a very long string this is a very long string this is a very long string this is a very long string this is a very long string this is a very long string this is a very long string this is a very long string this is a very long string this is a very long string" }
    return t[math.random(#t)]
end

function rnd_integer()
    t = { 0, math.random(1, 10), math.random(-2147483648, 2147483647) }
    return t[math.random(#t)]
end

function rnd_number()
    t = { 0, math.random(), (math.random() - 0.5) * 2 * 4294967296 }
    return t[math.random(#t)]
end

function rnd_Vec3s()
    t = { nil, { x = rnd_integer(), y = rnd_integer(), z = rnd_integer() } }
    return t[math.random(#t)]
end

function rnd_Vec3f()
    t = { nil, { x = rnd_number(), y = rnd_number(), z = rnd_number() } }
    return t[math.random(#t)]
end

function rnd_Vec4s()
    t = { nil, { x = rnd_integer(), y = rnd_integer(), z = rnd_integer(), w = rnd_integer() } }
    return t[math.random(#t)]
end

function rnd_Vec4f()
    t = { nil, { x = rnd_number(), y = rnd_number(), z = rnd_number(), w = rnd_number() } }
    return t[math.random(#t)]
end

function rnd_Mat4()
    t = { nil, { a = rnd_integer(), b = rnd_integer(), c = rnd_integer(), d = rnd_integer(), e = rnd_integer(), f = rnd_integer(), g = rnd_integer(), h = rnd_integer(), i = rnd_integer(), j = rnd_integer(), k = rnd_integer(), l = rnd_integer(), m = rnd_integer(), n = rnd_integer(), o = rnd_integer(), p = rnd_integer() } }
    return t[math.random(#t)]
end

function rnd_Object()
    t = { nil, gMarioStates[0].marioObj, gMarioStates[1].marioObj }
    return t[math.random(#t)]
end

function rnd_MarioState()
    t = { nil, gMarioStates[math.random(0, MAX_PLAYERS)] }
    return t[math.random(#t)]
end

function rnd_NetworkPlayer()
    t = { nil, gNetworkPlayers[math.random(0, MAX_PLAYERS)] }
    return t[math.random(#t)]
end

function rnd_SpawnParticlesInfo()
    t = { nil, obj_get_temp_spawn_particles_info(math.random(0, E_MODEL_MAX)) }
    return t[math.random(#t)]
end

function rnd_BehaviorScript()
    t = { nil, get_behavior_from_id(math.random(0, id_bhv_max_count)) }
    return t[math.random(#t)]
end

function rnd_Camera()
    t = { nil, gMarioStates[0].area.camera }
    return t[math.random(#t)]
end

function rnd_PlayerGeometry()
    t = { nil, {} }
    return t[math.random(#t)]
end

--------

function fuzz_functions()
-- $[FUNCS]
end

--------

function fuzz_structs()
end

hook_chat_command('fuzz-funcs', 'funcs', fuzz_functions)
hook_chat_command('fuzz-structs', 'structs', fuzz_structs)
fuzz_functions()
print('!')