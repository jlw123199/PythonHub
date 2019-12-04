from skimage import data, io, filters
import numpy as np
import os

# imageFilePath = os.path.abspath("D:/JiaLiWei/WorkArea/PythonRD/PythonHub/Scikit/girl.png")
# print (imageFilePath)

image = data.load("girl.png")

# image = data.load(imageFilePath)
io.imshow(image)
io.show()
print (image)

# edges = filters.sobel(image)
# io.imshow(edges)
# io.show()

image = data.camera()
image = data.text()
print(image)
io.imshow(image)
io.show()

edges = filters.sobel(image)
io.imshow(edges)
io.show()


# from skimage.util import img_as_ubyte
# image = np.array([0, 0.5, 1], dtype=float)
# img_as_ubyte(image)
# np.array([  0, 128, 255], dtype=np.uint8)
#
# io.imshow(image)
# io.show()

