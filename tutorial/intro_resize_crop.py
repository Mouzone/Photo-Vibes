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

# crops by resetting boundaries for left, upper, right, bottom
# sets left 300 pixels from the original left boundary, and right 700 pixels from the original left boundary
# set upper 150 pixels from theo original upper boundary, and the bottom 1000 pixels from original top boundary
# original upper an dleft boundaries start at border of the picture on those sides
# moving 1000 pixels to the right when the picutre is 600 pixels works by adding blackspace to the right until the dimension is met
cropped_img = img.crop((300, 150, 700, 1000))
print(f"size: {cropped_img.size}")
cropped_img.show()

# changes resolution (resizes width and height by a factor)
low_res_img = cropped_img.resize(
    (cropped_img.width//4, cropped_img.height//4)
)
low_res_img.show()

# changes resolution as well by a factor of 4 for both width and height
low_res_img = cropped_img.reduce(4)

cropped_img.save("cropped_img.jpg")
low_res_img.save("low_res_img.jpg")
