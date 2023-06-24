// 0x06005D54
static const s16 moneybag_seg6_animvalue_06005D54[] = {
    0x0000, 0x00B4, 0xFF1A, 0x3FFF, 0x3B84, 0x3FFF, 0x5FCF, 0x62B8,
    0x6758, 0x6BA0, 0x6D82, 0x6B5E, 0x66A8, 0x61F3, 0xF6B5, 0xFD63,
    0x0000, 0xFBB1, 0xF323, 0xEAC2, 0xE6FC, 0xEAE5, 0x10B8, 0x0568,
    0x0000, 0x0456, 0x0E78, 0x18B6, 0x1D63, 0x18CC, 0xCB51, 0xD1A7,
    0xD3F8, 0xCF36, 0xC62D, 0xBDA4, 0xBA61, 0xC022, 0x0B33, 0x1144,
    0x13E9, 0x10FC, 0x0A72, 0x03AA, 0x0000, 0x0154, 0xEDCE, 0xE3F3,
    0xDFA7, 0xE4C7, 0xF004, 0xFB28, 0x0000, 0xFA46, 0xCBE1, 0xC320,
    0xBECD, 0xC17F, 0xC8B2, 0xD070, 0xD4C8, 0xD3C1, 0x8001, 0x8001,
    0x5FCF, 0x62B8, 0x6758, 0x6BA0, 0x6D82, 0x6B5E, 0x66A8, 0x61F3,
};

// 0x06005DE4
static const u16 moneybag_seg6_animindex_06005DE4[] = {
    0x0001, 0x0000, 0x0001, 0x0001, 0x0001, 0x0002, 0x0001, 0x0003, 0x0001, 0x0004, 0x0001, 0x0005,
    0x0001, 0x0000, 0x0001, 0x0000, 0x0008, 0x0040,
    0x0001, 0x0000, 0x0001, 0x0000, 0x0001, 0x003F,
    0x0008, 0x000E, 0x0008, 0x0016, 0x0008, 0x001E,
    0x0001, 0x0000, 0x0001, 0x0000, 0x0001, 0x003E,
    0x0008, 0x0026, 0x0008, 0x002E, 0x0008, 0x0036,
    0x0001, 0x0000, 0x0001, 0x0000, 0x0008, 0x0006,
};

// 0x06005E44
static const struct Animation moneybag_seg6_anim_06005E44 = {
    0,
    0,
    0,
    0,
    0x08,
    ANIMINDEX_NUMPARTS(moneybag_seg6_animindex_06005DE4),
    moneybag_seg6_animvalue_06005D54,
    moneybag_seg6_animindex_06005DE4,
    0,
    ANIM_FIELD_LENGTH(moneybag_seg6_animvalue_06005D54),
    ANIM_FIELD_LENGTH(moneybag_seg6_animindex_06005DE4),
};
