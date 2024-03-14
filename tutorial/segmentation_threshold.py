from PIL import Image, ImageFilter

def erode(cycles, image):
    for _ in range(cycles):
        image = image.filter(ImageFilter.MinFilter(3))
    
    return image

def dilate(cycles, image):
    for _ in range(cycles):
        image = image.filter(ImageFilter.MaxFilter(3))

    return image

filename = "russell-westbrook-on-the-floor-of-the-grizzlies-court-v0-9h3200wqlzqa1.webp"
with Image.open(filename) as img:
    img.load()

img_to_split = img
red, green, blue = img_to_split.split()
threshold = 150
img_threshold = blue.point(
    lambda x: 255 if x < threshold else 0
)
img_threshold = img_threshold.convert('1') # only black and white wihtout gray
img_threshold.show()

step_1 = dilate(20, img_threshold)
step_1.show()

step_2 = erode(20, step_1)
step_2.show()

img_mask = dilate(5, step_2)
img_mask.show()

img_mask = img_mask.convert('L')
img_mask = img_mask.filter(ImageFilter.BoxBlur(20))
img_mask.show()

blank = img.point(lambda _: 0)
img_segmented = Image.composite(img, blank, img_mask)
# for the russel westbrook image the court is now balck and see only the players now
img_segmented.show()

filename_brick = "brick_wall.jpg"
with Image.open(filename_brick) as img_brick:
    img_brick.load()

img_brick.paste(
    img.resize((img.width//2, img.height//2)),
    (200, 100),
    img_mask.resize((img_mask.width//2, img_mask.height//2))
)

img_brick.show()