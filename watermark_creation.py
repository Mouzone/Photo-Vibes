from PIL import Image, ImageFilter

background_filename = "reksai.jpeg"
with Image.open(background_filename) as img_b:
    img_b.load()

logo_filename = "watermark.webp"
with Image.open(logo_filename) as img_l:
    img_l.load()

img_l = img_l.convert('L') # convert to gray scale
threshold = 50
img_l = img_l.point(lambda x: 255 if x > threshold else 0) # turn it into only black and white, with higher intensity being white
img_l = img_l.resize(
    (img_l.width//10, img_l.height//10)
)
img_l = img_l.filter(ImageFilter.CONTOUR) # leaves only edges and rest makes it white

img_l = img_l.point(lambda x: 0 if x == 255 else 255) # reverses the contoured image such that edges are now white and everything is filled black
img_l.show()

# first image is the image to paste, the third image is the mask to use
## this decides what parts of img_l to paste, but since it is the same it will paste all of img_l
# the coordinates is for top left
img_b.paste(img_l, (25, 25), img_l)
img_b.show()