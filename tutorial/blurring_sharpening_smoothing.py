from PIL import Image, ImageFilter

filename = "wakin_chau.jpeg"
with Image.open(filename) as img:
    img.load()

# blur_img uses a matrix frame and places it with the cell at the center. All cells inside the frame are added and averaged based
# on the value (0 to 255) then sets the cell in the new image to that value and moves on
# this is a convulution kernel approach for BoxBlur

blur_img = img.filter(ImageFilter.BLUR)
blur_img.show()

# img.crop((300, 300, 500, 500)).show()
# blur_img.crop((300, 300, 500, 500)).show()

# the number dictates the number of pixels from the center
# img.filter(ImageFilter.BoxBlur(5)).sbow()
# img.filter(ImageFilter.BoxBlur(20)).show() # way more intense than 5
# guassian blur is a lot more intense and blurs the center more than the outer edge of the kernel
img.filter(ImageFilter.GaussianBlur(20)).show()

sharp_img = img.filter(ImageFilter.SHARPEN)
img.crop((300, 300, 500, 500)).show()
sharp_img.crop((300, 300, 500, 500)).show()

smooth_img = img.filter(ImageFilter.SMOOTH)
img.crop((300, 300, 500, 500)).show()
smooth_img.crop((300, 300, 500, 500)).show()