from PIL import Image, ImageDraw, ImageFont

# Extracted from 'bug.pcx' (with final entry corrected to black).
PALETTE_RAW = [
    0x00, 0x00, 0x00, 0xDD, 0xDD, 0xDD, 0xB6, 0xB6, 0xB6, 0x96, 0x96, 0x96,
    0x7C, 0x7C, 0x7C, 0x66, 0x66, 0x66, 0x54, 0x54, 0x54, 0x45, 0x45, 0x45,
    0x39, 0x39, 0x39, 0x2F, 0x2F, 0x2F, 0x27, 0x27, 0x27, 0x20, 0x20, 0x20,
    0x1A, 0x1A, 0x1A, 0x16, 0x16, 0x16, 0x12, 0x12, 0x12, 0x0F, 0x0F, 0x0F,
    0x0C, 0x0C, 0x0C, 0x0A, 0x0A, 0x0A, 0x08, 0x08, 0x08, 0x06, 0x06, 0x06,
    0x05, 0x05, 0x05, 0x04, 0x04, 0x04, 0x03, 0x03, 0x03, 0x7A, 0x84, 0x49,
    0x70, 0x7A, 0x43, 0x65, 0x70, 0x3D, 0x5B, 0x65, 0x36, 0x00, 0x87, 0xFE,
    0x00, 0x7D, 0xF2, 0x00, 0x73, 0xE6, 0x00, 0x69, 0xDA, 0x00, 0x5F, 0xCE,
    0xB1, 0x8C, 0x82, 0xA3, 0x81, 0x78, 0x96, 0x77, 0x6E, 0x88, 0x6C, 0x64,
    0x7B, 0x61, 0x5A, 0x6D, 0x56, 0x50, 0x60, 0x4C, 0x46, 0x52, 0x41, 0x3C,
    0x44, 0x36, 0x32, 0x37, 0x2B, 0x28, 0x29, 0x21, 0x1E, 0x1C, 0x16, 0x14,
    0x0E, 0x0B, 0x0A, 0xA3, 0x02, 0x02, 0x98, 0x02, 0x02, 0x8E, 0x02, 0x02,
    0x83, 0x02, 0x02, 0x78, 0x01, 0x01, 0x6D, 0x01, 0x01, 0x63, 0x01, 0x01,
    0x58, 0x01, 0x01, 0x4D, 0x01, 0x01, 0x38, 0x01, 0x01, 0x22, 0x00, 0x00,
    0x0D, 0x00, 0x00, 0x08, 0x30, 0x15, 0x07, 0x2B, 0x13, 0x06, 0x25, 0x10,
    0x05, 0x20, 0x0E, 0x04, 0x1A, 0x0B, 0x03, 0x15, 0x09, 0x02, 0x0F, 0x06,
    0x8E, 0x6D, 0x43, 0x87, 0x68, 0x3F, 0x81, 0x62, 0x3C, 0x7A, 0x5D, 0x38,
    0x73, 0x57, 0x34, 0x6D, 0x52, 0x31, 0x66, 0x4C, 0x2D, 0x60, 0x47, 0x2A,
    0x57, 0x3F, 0x25, 0x4D, 0x38, 0x20, 0x44, 0x30, 0x1A, 0x3A, 0x29, 0x15,
    0x31, 0x21, 0x10, 0x3E, 0x12, 0x10, 0x3A, 0x11, 0x0F, 0x36, 0x10, 0x0E,
    0x32, 0x0E, 0x0D, 0x2E, 0x0D, 0x0C, 0x2A, 0x0C, 0x0B, 0x26, 0x0B, 0x0A,
    0x22, 0x0A, 0x09, 0x1D, 0x08, 0x07, 0x18, 0x06, 0x06, 0x12, 0x05, 0x04,
    0x0D, 0x03, 0x03, 0x32, 0x1D, 0x46, 0x2D, 0x1A, 0x3F, 0x27, 0x17, 0x36,
    0x20, 0x13, 0x2C, 0x1A, 0x10, 0x23, 0x14, 0x0C, 0x1B, 0x0E, 0x09, 0x12,
    0xEE, 0x9A, 0x47, 0xDE, 0x90, 0x42, 0xCF, 0x86, 0x3E, 0xBF, 0x7C, 0x39,
    0xAF, 0x71, 0x34, 0xA0, 0x67, 0x2F, 0x90, 0x5D, 0x2B, 0x81, 0x53, 0x26,
    0x71, 0x49, 0x22, 0x61, 0x3F, 0x1D, 0x51, 0x35, 0x19, 0x41, 0x2B, 0x14,
    0x31, 0x21, 0x10, 0x31, 0x21, 0x10, 0x2E, 0x1F, 0x0F, 0x2B, 0x1D, 0x0E,
    0x27, 0x1A, 0x0D, 0x24, 0x18, 0x0C, 0x21, 0x16, 0x0B, 0x1E, 0x14, 0x0A,
    0x1B, 0x12, 0x09, 0x17, 0x0F, 0x07, 0x14, 0x0D, 0x06, 0x11, 0x0B, 0x05,
    0x0A, 0x06, 0x03, 0xFF, 0xFF, 0xBD, 0xFF, 0xB5, 0x10, 0xFF, 0xAD, 0x52,
    0xFF, 0xFF, 0x7B, 0xF1, 0xE6, 0x57, 0xE4, 0xCE, 0x34, 0xD6, 0xB5, 0x10,
    0x8C, 0x7B, 0x5A, 0x86, 0x75, 0x55, 0x7F, 0x6E, 0x4F, 0x79, 0x68, 0x4A,
    0x72, 0x61, 0x45, 0x6C, 0x5B, 0x40, 0x65, 0x54, 0x3A, 0x5C, 0x4C, 0x33,
    0x54, 0x43, 0x2C, 0x4B, 0x3B, 0x25, 0x42, 0x32, 0x1E, 0x3A, 0x2A, 0x17,
    0x31, 0x21, 0x10, 0x50, 0x5B, 0x30, 0x4B, 0x55, 0x2D, 0x46, 0x4F, 0x2A,
    0x40, 0x49, 0x27, 0x3B, 0x44, 0x23, 0x36, 0x3E, 0x20, 0x31, 0x38, 0x1D,
    0x2C, 0x32, 0x1A, 0x26, 0x2C, 0x17, 0x21, 0x26, 0x14, 0x1C, 0x20, 0x11,
    0x17, 0x1B, 0x0D, 0xAD, 0x10, 0xB5, 0x9C, 0x29, 0xAD, 0xB5, 0x18, 0x94,
    0x94, 0x00, 0xC6, 0x63, 0x00, 0xAD, 0x4A, 0x00, 0x80, 0x31, 0x00, 0x52,
    0x6D, 0x77, 0x87, 0x66, 0x6F, 0x7E, 0x5F, 0x67, 0x75, 0x57, 0x5F, 0x6C,
    0x50, 0x57, 0x64, 0x49, 0x4F, 0x5A, 0x42, 0x47, 0x52, 0x3B, 0x40, 0x48,
    0x33, 0x37, 0x3E, 0x2B, 0x2E, 0x34, 0x22, 0x25, 0x29, 0x1A, 0x1C, 0x1F,
    0x12, 0x13, 0x15, 0x5A, 0x31, 0x39, 0x54, 0x2E, 0x35, 0x4E, 0x2B, 0x31,
    0x48, 0x27, 0x2E, 0x42, 0x24, 0x2A, 0x3C, 0x21, 0x26, 0x36, 0x1E, 0x22,
    0x31, 0x1B, 0x1F, 0x2B, 0x17, 0x1B, 0x23, 0x13, 0x16, 0x1B, 0x0E, 0x11,
    0x13, 0x0A, 0x0C, 0xE7, 0x18, 0x21, 0xCE, 0x21, 0x18, 0xFF, 0x8C, 0x18,
    0xD9, 0x74, 0x15, 0xB2, 0x5C, 0x12, 0x8C, 0x44, 0x0F, 0x65, 0x2C, 0x0C,
    0x6D, 0x53, 0x70, 0x66, 0x4E, 0x69, 0x5E, 0x47, 0x60, 0x56, 0x41, 0x58,
    0x4D, 0x3B, 0x4E, 0x46, 0x35, 0x46, 0x3D, 0x2E, 0x3D, 0x35, 0x28, 0x35,
    0x2D, 0x22, 0x2D, 0x24, 0x1B, 0x24, 0x1C, 0x15, 0x1C, 0x13, 0x0E, 0x13,
    0x0B, 0x08, 0x0B, 0x9C, 0x4A, 0x4A, 0xA8, 0x61, 0x61, 0xB5, 0x77, 0x77,
    0xC1, 0x8E, 0x8E, 0xCE, 0xA5, 0xA5, 0xDA, 0xBB, 0xBB, 0xE6, 0xD2, 0xD2,
    0xF3, 0xE8, 0xE8, 0xFF, 0xFF, 0xFF, 0x00, 0x55, 0xC2, 0x00, 0x4B, 0xB6,
    0x00, 0x41, 0xA2, 0xB5, 0xBD, 0xFF, 0x8C, 0x8C, 0xE7, 0x9C, 0xAD, 0xEF,
    0x7E, 0x9D, 0xE2, 0x5F, 0x8E, 0xD4, 0x41, 0x7E, 0xC7, 0x22, 0x6E, 0xB9,
    0xDE, 0xD6, 0x84, 0xCF, 0xC8, 0x7B, 0xC1, 0xBA, 0x73, 0xB2, 0xAC, 0x6A,
    0xA4, 0x9E, 0x61, 0x95, 0x90, 0x58, 0x87, 0x82, 0x50, 0x74, 0x6F, 0x44,
    0x60, 0x5C, 0x39, 0x4D, 0x4A, 0x2D, 0x39, 0x37, 0x21, 0x26, 0x24, 0x16,
    0x12, 0x11, 0x0A, 0x74, 0x95, 0x9D, 0x97, 0xB0, 0xB6, 0xBA, 0xCA, 0xCE,
    0xDC, 0xE5, 0xE7, 0xFF, 0xFF, 0xFF, 0x3A, 0x5B, 0x4B, 0x46, 0x6E, 0x57,
    0x53, 0x80, 0x63, 0x5F, 0x93, 0x6F, 0x6B, 0xA5, 0x7B, 0x00, 0x37, 0x8D,
    0x00, 0x2D, 0x79, 0x00, 0x23, 0x64, 0x00, 0x19, 0x50, 0x00, 0x0F, 0x3B,
    0x00, 0x00, 0xFF, 0x00, 0x00, 0xFF, 0xFF, 0x00, 0xFF, 0x00, 0x00, 0x00
    ]


def make_palette():
    pal = []
    for i in range(0, len(PALETTE_RAW), 3):
        pal.append(tuple(PALETTE_RAW[i:i+3]))        
    return pal

def palette_image(pal, *,
        size=8,
        cols=10,
        split=True,
        spacing=2,
        border=4,
        background=(96, 96, 96)):
    fnt = ImageFont.load_default()
    count = len(pal)
    textw, texth = 0, 0
    for index in range(count):
        text = str(index)
        (w, h) = fnt.getsize(text)
        textw = max(textw, w)
        texth = max(texth, h)
    size = max(size, texth)
    rows = (count+cols-1)//cols
    rowsize = max(size, texth)
    width = cols*size + (cols-1)*spacing + 2*border + (border if split else 0) + textw+spacing
    height = rows*rowsize + (rows-1)*spacing + 2*border
    im = Image.new('RGB', (width, height), background)
    draw = ImageDraw.Draw(im)
    cx0 = border+textw+spacing
    cx, cy, col, index = cx0, border, 0, 0
    splitcol = (cols//2 if split else -1)
    for color in pal:
        if col==0:
            text = str(index)
            (tw, th) = fnt.getsize(text)
            draw.text((cx-tw-spacing, cy+(rowsize-th)//2), text, font=fnt, fill=(0,0,0))
        im.paste(color, (cx,cy,cx+size,cy+size))
        cx += size+spacing
        index += 1
        col += 1
        if split and col==splitcol:
            cx += border+spacing
        if col==cols:
            cx = cx0
            cy += rowsize+spacing
            col = 0
    return im

def main():
    pal = make_palette()
    im = palette_image(pal, cols=16)
    im.save('particles16x16.png')
    im = palette_image(pal, cols=10)
    im.save('particles10x25.png')
    im = palette_image(pal, cols=16, background=(255,255,255))
    im.save('particles16x16w.png')
    im = palette_image(pal, cols=10, background=(255,255,255))
    im.save('particles10x25w.png')

if __name__=='__main__':
    main()
