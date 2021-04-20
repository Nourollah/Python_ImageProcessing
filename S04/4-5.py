import cv2
import matplotlib.pyplot as plt
import skimage.filters
import skimage.morphology

plt.gray()

# Read image anc normalized it between 0.0 and 1.0 as float type
img = cv2.imread("Lenna.jpg", cv2.IMREAD_GRAYSCALE)
# Apply salt and pepper noise to image
imgn = skimage.util.random_noise(skimage.util.random_noise(img, 'salt', amount=0.2), 'pepper', amount=0.2)
imgd1 = skimage.filters.median(imgn, skimage.morphology.disk(3))
imgd2 = skimage.filters.median(imgn, skimage.morphology.disk(5))
imgd3 = skimage.filters.median(imgn, skimage.morphology.disk(7))

plt.subplot(131)
plt.imshow(imgd1)
plt.title("3*3 Kernel")
plt.subplot(132)
plt.imshow(imgd2)
plt.title("5*5 Kernel")
plt.subplot(133)
plt.imshow(imgd3)
plt.title("7*7 Kernel")
plt.subplots_adjust(left=0.1, bottom=0.0, right=0.9, top=0.9, wspace=0.6, hspace=0.6)
plt.show()
