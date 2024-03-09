from PIL import Image
filename = "wakin_chau.jpeg"

with Image.open(filename) as img:
    img.load()

print(f"Type: {type(img)}")

print(f"is img an instance of Image.Image? {isinstance(img, Image.Image)}")
