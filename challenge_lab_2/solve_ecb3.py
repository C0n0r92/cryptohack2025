#!/usr/bin/env python3
from pathlib import Path
from PIL import Image

BYTES_PER_PIXEL = 3
ROW_ALIGNMENT = 4
BMP_HEADER_SIZE = 54

# BMP rows must be 4-byte aligned
def get_row_size(width):
    return ((width * BYTES_PER_PIXEL + ROW_ALIGNMENT - 1) // ROW_ALIGNMENT) * ROW_ALIGNMENT

def find_dimensions(data_size):
    # common image sizes trying to find the right dimensions
    for width, height in [(640, 480), (800, 600), (1024, 768), (512, 512)]:
        if height * get_row_size(width) == data_size:
            return width, height

def recover_image(encrypted_file, output_file):
    data = Path(encrypted_file).read_bytes()
    pixels = data[BMP_HEADER_SIZE:]
    
    width, height = find_dimensions(len(pixels))
    
    recovered = Image.frombytes('RGB', (width, height), pixels, 'raw', 'BGR')
    recovered = recovered.transpose(Image.FLIP_TOP_BOTTOM)  # was updside down
    recovered.save(output_file, 'BMP')

if __name__ == "__main__":
    recover_image("aes.bmp.enc", "recovered_flag3.bmp")


