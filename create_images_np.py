from PIL import Image, ImageFilter
import numpy as np

square = np.zeros((600, 600)) # 0 means it is black
square[200: 400, 200: 400] = 255 # selects rows [200, 400) and cols [200, 400) and sets it to white

square_img = Image.fromarray(square)
square_img.show()