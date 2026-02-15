from PIL import Image

def encode_lsb(image_path, data: bytes, output_path):
    img = Image.open(image_path)
    pixels = img.load()

    binary = ''.join(format(byte, '08b') for byte in data) + '1111111111111110'

    w, h = img.size
    idx = 0

    for y in range(h):
        for x in range(w):
            if idx >= len(binary):
                img.save(output_path)
                return

            r, g, b = pixels[x, y]
            r = (r & ~1) | int(binary[idx])
            idx += 1

            pixels[x, y] = (r, g, b)

def decode_lsb(image_path):
    img = Image.open(image_path)
    pixels = img.load()

    bits = ""
    w, h = img.size

    for y in range(h):
        for x in range(w):
            r, g, b = pixels[x, y]
            bits += str(r & 1)

    bytes_out = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if byte == '11111110':
            break
        bytes_out.append(int(byte, 2))

    return bytes(bytes_out)
