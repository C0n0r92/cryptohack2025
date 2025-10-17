#!/usr/bin/env python3
from pathlib import Path
from PIL import Image
import sys

BMP_HEADER_SIZE = 54

def recover_image(encrypted_file, output_file, width, height):

    data = Path(encrypted_file).read_bytes()
    pixels = data[BMP_HEADER_SIZE:]

    recovered = Image.frombytes('RGB', (width, height), pixels)
    recovered = recovered.transpose(Image.FLIP_TOP_BOTTOM)  # BMP stores upside down
    recovered.save(output_file, 'BMP')
    print(f"Recovered image saved to: {output_file}")


if __name__ == "__main__":

    width = int(sys.argv[1])
    height = int(sys.argv[2])

    recover_image("aes.bmp.enc", f"recovered_flag_w{width}_h{height}.bmp", width, height)