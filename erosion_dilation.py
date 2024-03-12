from PIL import Image, ImageFilter
filename = "wakin_chau.jpeg"

with Image.open(filename) as img:
    img.load()

# erosion and dilation fills in small holes and remove small objects to make grayscale and finding edges much easier
# can run as many cycles as you want until the objects dissapear or holes are filled
# or even run one after the other, such that you fill in all the holes then shrink back any dilations
# you can also dissapear any objects then grow back any areas that got shrunk
for _ in range(3):
    # MinFilter removes white pixels around borders of images
    # works by looking in the 3x3 grid around each pixel and picking the lowest value
    # this then dilates lighter areas, but erodes darker areas as well
    img = img.filter(ImageFilter.MinFilter(3))

img.show()

for _ in range(10):
    # oposite of MinFilter
    img = img.filter(ImageFilter.MaxFilter(3))

img.show()