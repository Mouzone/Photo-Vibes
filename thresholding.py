from PIL import Image

filename = "wakin_chau.jpeg"
with Image.open(filename) as img:
    img.load()

# img = img.crop((200, 100, 450, 300))
# img.show()

img_gray = img.convert('L')
img_gray.show()
threshold = 100
# transforms every point to max or min based on the threshold val
# easier if grayscale
img_threshold = img_gray.point(
    lambda x: 255 if x > threshold else 0
)
img_threshold.show()

# split based on the object you want to segment from the background
# if background are colors wiht higher channels than the obejct then we should use that channel to split by
red, green, blue = img.split()
red.show()
green.show()
blue.show()

# the goal is to get the target white and the background black
threshold = 150
img_threshold = red.point(
    lambda x: 255 if x > threshold else 0
)
img_threshold = img_threshold.convert('1')
img_threshold.show()