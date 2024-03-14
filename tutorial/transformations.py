from PIL import Image

file = "wakin_chau.jpeg"

with Image.open(file) as img:
    img.load()

# Image.FLIP_TOP_BOTTOM is the type of transpose to run in img.transpose 
# FLIP_TOP_BOTTOM is across the middle of the top and bottom not the diagonal
converted_img = img.transpose(Image.FLIP_TOP_BOTTOM)
converted_img.show()
# Other options:
# - left to right
# - rotations (90, 180, 270)
# - transpose (across y=-x diagonal)
# - transverse (across y=x diagonal)

# transpose_img = img.transpose(Image.TRANSPOSE)
# transpose_img.show()

# transverse_img = img.transpose(Image.TRANSVERSE)
# transverse_img.show()

# ROTATION HAPPENS AROUND THE CENTER
# this is fitted inside the original border so corners will be cut out
# this is for rotations that aren't multiples of 90 
# positive direction is left, negative direction is towards the right
rotated_img = img.rotate(45)
rotated_img.show()

# expand zooms out 
rotated_img = img.rotate(-47, expand=True)
rotated_img.show()