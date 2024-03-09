from PIL import Image
filename = "wakin_chau.jpeg"

with Image.open(filename) as img:
    img.load()

print(f"Type: {type(img)}")

print(f"is img an instance of Image.Image? {isinstance(img, Image.Image)}")

img.show()

print(f"format: {img.format}")
print(f"size: {img.size}")
print(f"mode: {img.mode}")