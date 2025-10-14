# ECB Image Recovery - How It Works

## The Problem

I had an encrypted BMP image file (`aes.bmp.enc`) that was encrypted using AES in ECB mode. The challenge was to recover the image without having the decryption key.

## Why ECB Mode is Vulnerable

ECB (Electronic Codebook) mode has a major weakness - it encrypts identical blocks of data to identical encrypted blocks. This means patterns in the original image are preserved in the encrypted version.

For images, this is bad because:
- Areas with the same color (like a white background) all encrypt to the same encrypted bytes
- The spatial layout stays the same
- You can still see shapes and patterns even though colors are scrambled

## The Solution

Since ECB preserves patterns, I realized I could just treat the encrypted pixel data as if it were normal pixel data. The colors would be wrong, but the image structure would remain visible.

### How the Code Works

1. **Skip the BMP header** - The first 54 bytes are the BMP file header (not encrypted), so I skip those
2. **Extract pixel data** - Everything after byte 54 is the encrypted pixel data
3. **Guess dimensions** - BMP files don't store dimensions in the pixel data, so I need to guess width and height
4. **Reconstruct the image** - Use PIL to arrange the encrypted bytes into an image grid
5. **Flip it** - BMP files store images upside down, so flip it right-side up

### Guessing Image Dimensions

The tricky part was figuring out the image dimensions. I tried common image sizes from https://www.fileformat.info/tip/web/imagesize.htm:

- 640 × 480 (old standard)
- 800 × 600 (common web size)
- 1024 × 768 (old monitor size)
- 512 × 512 (square images)

I run the script with different dimensions until one works:

```bash
python lab6_image.py 640 480
python lab6_image.py 800 600
```

When you get the dimensions right, the image will look correct (wrong colors, but clear patterns). Wrong dimensions make it look like garbage.

### Interesting Finding

Turns out my guessing didn't even need to be that accurate! Both 640×350 and 640×480 displayed the flag text "Tro11d" clearly enough to read. The image was stretched or squashed a bit, but the patterns were still visible. This shows just how forgiving this attack is - you don't need perfect dimensions to extract the information.

## Usage

```bash
python lab6_image.py <width> <height>
```

Example:
```bash
python lab6_image.py 640 480
```

This creates `recovered_flag_w640_h480.bmp` with the recovered image.

## What I Learned

- ECB mode is terrible for encrypting images (or anything with patterns)
- You should always use a mode with an IV like CBC or CTR
- Even without the key, you can recover meaningful information from ECB-encrypted images
- BMP format quirks: 54-byte header, BGR color order, stored upside down
