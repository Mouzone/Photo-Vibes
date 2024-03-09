from PIL import Image

file = "wakin_chau.jpeg"

with Image.open(file) as img:
    img.load()

cmyk_img = img.convert("CMYK") # best for printing output
gray_img = img.convert("L")

cmyk_img.show()
gray_img.show()

print(img.getbands())
print(cmyk_img.getbands())
print(gray_img.getbands())

red, green, blue = img.split()
print(red)
print(red.mode) # output is L meaning we need the proper format to see image in any color
# it is just luminance or how much light for each pixel

# abscence or small values is represented by black in RGB
# don't need lambda fubnction but can you use math equations to modify each pixel based on a property
# can just do red.point(0)
# we use red here bc we don't ened to guess or check the array we would need to create
zeroed_band = red.point(lambda _:0)
red_merge = Image.merge(
    "RGB", (red, zeroed_band, zeroed_band)
)
green_merge = Image.merge(
    "RGB", (zeroed_band, green, zeroed_band)
)
blue_merge = Image.merge(
    "RGB", (zeroed_band, zeroed_band, blue)
)

red_merge.show()
green_merge.show()
blue_mnerge.show()