from PIL import Image
from pwn import xor

# Load the two images
img1 = Image.open('../images/lemur_ed66878c338e662d3473f0d98eedbd0d.png')
img2 = Image.open('../images/flag_7ae18c704272532658c10b5faad06d74.png')

img1_rgb = img1.convert('RGB')
img2_rgb = img2.convert('RGB')

img_bytes = img1_rgb.tobytes()
img_bytes2 = img2_rgb.tobytes()

xor_pixels = xor(img_bytes, img_bytes2)

res = Image.frombytes('RGB', img1_rgb.size, xor_pixels)
res.save('../images/xor_image.png')

