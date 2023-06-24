// 0x0800AF80
static const s16 chuckya_seg8_animvalue_0800AF80[] = {
    0x0000, 0x0001, 0x3FFF, 0xFBBB, 0xFA1D, 0xF73F, 0xF620, 0xF81B,
    0xFB8D, 0xFEEB, 0x00AA, 0xFFB2, 0xFD07, 0xFA55, 0xF944, 0xFAF2,
    0xFE49, 0x019D, 0x0348, 0x0259, 0xFFE3, 0xFD3E, 0xFBC4, 0x071C,
    0xF225, 0x784B, 0xFD83, 0x05D9, 0x683E, 0x02A3, 0x0334, 0x0466,
    0x0579, 0x05AC, 0x04C3, 0x033C, 0x016D, 0xFFB0, 0xFE57, 0xFDBC,
    0xFE43, 0xFFBA, 0x0196, 0x034F, 0x045B, 0x0469, 0x03D5, 0x0317,
    0x02A6, 0xC001, 0x8001, 0xE35C, 0x3FFF, 0x8001, 0xE35C, 0xD516,
    0xDDDC, 0xF58F, 0x9655, 0x614E, 0x76A6, 0x6078, 0x3FFF, 0xDF87,
    0x9F88, 0xC001, 0xDF87, 0xBF0E, 0x5347, 0xC04A, 0x3FFF, 0x3FE4,
    0x3FA6, 0x3F5E, 0x3F27, 0x3F1C, 0x3F3D, 0x3F77, 0x3FC0, 0x4011,
    0x4061, 0x40A9, 0x40E0, 0x40FF, 0x40F8, 0x40CE, 0x4090, 0x404F,
    0x401A, 0x4000,
};

// 0x0800B034
static const u16 chuckya_seg8_animindex_0800B034[] = {
    0x0001, 0x0000, 0x0001, 0x0000, 0x0001, 0x0001, 0x0001, 0x0000, 0x0001, 0x0002, 0x0001, 0x0000,
    0x0001, 0x0000, 0x0001, 0x0000, 0x0014, 0x0046,
    0x0001, 0x0000, 0x0001, 0x0000, 0x0001, 0x0045,
    0x0001, 0x0000, 0x0001, 0x0000, 0x0001, 0x0044,
    0x0001, 0x0000, 0x0001, 0x0000, 0x0001, 0x0000,
    0x0001, 0x0000, 0x0001, 0x0000, 0x0001, 0x0043,
    0x0001, 0x0000, 0x0001, 0x0000, 0x0014, 0x001D,
    0x0001, 0x0000, 0x0001, 0x0000, 0x0014, 0x0003,
    0x0001, 0x0000, 0x0001, 0x0000, 0x0001, 0x0000,
    0x0001, 0x0000, 0x0001, 0x0000, 0x0001, 0x0000,
    0x0001, 0x0000, 0x0001, 0x0000, 0x0001, 0x0000,
    0x0001, 0x0000, 0x0001, 0x0000, 0x0001, 0x0000,
    0x0001, 0x0000, 0x0001, 0x0000, 0x0001, 0x0000,
    0x0001, 0x0040, 0x0001, 0x0041, 0x0001, 0x0042,
    0x0001, 0x0037, 0x0001, 0x0038, 0x0001, 0x0039,
    0x0001, 0x0000, 0x0001, 0x0000, 0x0001, 0x0000,
    0x0001, 0x0000, 0x0001, 0x0000, 0x0001, 0x0000,
    0x0001, 0x0031, 0x0001, 0x0032, 0x0001, 0x0033,
    0x0001, 0x0017, 0x0001, 0x0018, 0x0001, 0x0019,
    0x0001, 0x0000, 0x0001, 0x0000, 0x0001, 0x0000,
    0x0001, 0x0000, 0x0001, 0x0000, 0x0001, 0x0000,
    0x0001, 0x003D, 0x0001, 0x003E, 0x0001, 0x003F,
    0x0001, 0x003A, 0x0001, 0x003B, 0x0001, 0x003C,
    0x0001, 0x0000, 0x0001, 0x0000, 0x0001, 0x0000,
    0x0001, 0x0000, 0x0001, 0x0000, 0x0001, 0x0000,
    0x0001, 0x0034, 0x0001, 0x0035, 0x0001, 0x0036,
    0x0001, 0x001A, 0x0001, 0x001B, 0x0001, 0x001C,
    0x0001, 0x0000, 0x0001, 0x0000, 0x0001, 0x0000,
    0x0001, 0x0000, 0x0001, 0x0000, 0x0001, 0x0000,
    0x0001, 0x0000, 0x0001, 0x0000, 0x0001, 0x0000,
};

// 0x0800B1A8
static const struct Animation chuckya_seg8_anim_0800B1A8 = {
    0,
    0,
    0,
    0,
    0x14,
    ANIMINDEX_NUMPARTS(chuckya_seg8_animindex_0800B034),
    chuckya_seg8_animvalue_0800AF80,
    chuckya_seg8_animindex_0800B034,
    0,
    ANIM_FIELD_LENGTH(chuckya_seg8_animvalue_0800AF80),
    ANIM_FIELD_LENGTH(chuckya_seg8_animindex_0800B034),
};
