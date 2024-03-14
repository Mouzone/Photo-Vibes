from PIL import Image, ImageFilter
import numpy as np

square = np.zeros((600, 600)) # 0 means it is black
square[200: 400, 200: 400] = 255 # selects rows [200, 400) and cols [200, 400) and sets it to white

square_img = Image.fromarray(square)
square_img.show()

square_img = square_img.convert('L') # converts from F which is 32 bit (color) to 8 bit (grayscale)
square_img.show()

red = np.zeros((600, 600))
blue = np.zeros((600, 600))
green = np.zeros((600, 600))
# these are the intensity values of each of the color vals 
red[150: 350, 150: 350] = 255 
green[200: 400, 200: 400] = 255
blue[250: 450, 250: 450] = 255

red_img = Image.fromarray(red).convert('L')
green_img = Image.fromarray(green).convert('L')
blue_img = Image.fromarray(blue).convert('L')

# merges them under RGB mode
square_img = Image.merge("RGB", (red_img, green_img, blue_img))
square_img.show()