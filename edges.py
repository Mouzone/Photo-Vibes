from PIL import Image, ImageFilter

filename = "wakin_chau.jpeg"
with Image.open(filename) as img:
    img.load()

img_gray = img.convert('L')
edges = img_gray.filter(ImageFilter.FIND_EDGES)
edges.show()

img_gray_smooth = img_gray.filter(ImageFilter.SMOOTH) # much better at finding edges after smoothing
# focuses on the main edges instead of just miscellaneous hair
edges_smooth = img_gray_smooth.filter(ImageFilter.FIND_EDGES)
edges_smooth.show()

# makes the edges pop out more while keeping the inner areas smoothed out
edge_enhance = img_gray_smooth.filter(ImageFilter.EDGE_ENHANCE)
edge_enhance.show()

# different edge detection and different output than hte previous white liens on black
emboss = img_gray_smooth.filter(ImageFilter.EMBOSS)
emboss.show()