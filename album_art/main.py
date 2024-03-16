# make it able to take a file name input or some kind of drag and drop website to proccess
# output is the edited image in a rectangular frame with the gap between album image and frame the distrotion

from PIL import Image, ImageFilter
import numpy as np
import os

def proccess_image(image_path):
    img = Image.open(image_path)
    img = img.resize((500, 550))
    return img

def create_background(img):
    width = 1278//2 # //2 to scale it to irl phone width and height and accepts only ints
    height = 2778//2
    img = img.filter(ImageFilter.GaussianBlur(30))
    background = img.resize((width, height))
    return background

def create_screen(background, img):
    background_width, background_height = background.size
    img_width, img_height = img.size

    x_offset = (background_width - img_width)//2 
    y_offset = (background_height - img_width)//2 - 50

    background.paste(img, (x_offset, y_offset))
    background.show()

folder_path = "original albums"
files = os.listdir(folder_path)
for file in files:
    image_path = os.path.join(folder_path, file)
    img = proccess_image(image_path)
    background = create_background(img)
    final = create_screen(background, img)
