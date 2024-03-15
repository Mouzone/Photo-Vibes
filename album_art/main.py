# make it able to take a file name input or some kind of drag and drop website to proccess
import os
from PIL import Image

def proccess_image(image_path):
    img = Image.open(image_path)
    img.show()

folder_path = "original albums"
files = os.listdir(folder_path)
for file in files:
    image_path = os.path.join(folder_path, file)
    proccess_image(image_path)
# output is the edited image in a rectangular frame with the gap between album image and frame the distrotion