from PIL import Image, ImageFilter
import numpy as np

filename_left = "houseleft.jpg"
img_house_l = Image.open(filename_left)

filename_right = "houseright.jpg"
img_house_r = Image.open(filename_right)

array_l = np.asarray(img_house_l)
array_r = np.asarray(img_house_r)

difference_array = array_r - array_l

difference = Image.fromarray(difference_array)
difference.show()
# now will show the differences between the two images with the elements that are different the only remaining