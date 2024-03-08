import cv2
import matplotlib.pyplot as plt

image = cv2.imread('wakin_chau.jpeg')

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

histogram = cv2.calcHist([image_rgb], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])

plt.figure()
plt.title("RGB Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(histogram)
plt.xlim([0, 256])
plt.show()
