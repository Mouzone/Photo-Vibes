from PIL import Image, ImageFilter
import numpy as np 

# we basically generate a 100 frames then it animates
square_animation = []
for offset in range(0, 100, 2):
    red = np.zeros((600, 600))
    green = np.zeros((600, 600))
    blue = np.zeros((600, 600))

    # as it iterates red moves closer to center from top left and blue does too but from bottom right
    red[101+offset: 301+offset, 101+offset: 301+offset,] = 255
    green[200: 400, 200: 400] = 255
    blue[299-offset: 499-offset, 299-offset: 499-offset] = 255

    red_img = Image.fromarray(red).convert('L')
    blue_img = Image.fromarray(blue).convert('L')
    green_img = Image.fromarray(green).convert('L')

    square_animation.append(
        Image.merge(
            "RGB",
            (red_img, green_img, blue_img)
        )
    )

# animate from image 0
square_animation[0].save(
    "animation.gif", save_all=True, append_images=square_animation[1:]
)