from skimage import data, io, filters

image = data.coins()
# ... or any other NumPy array!
edges = filters.sobel(image)

io.imshow(image)
io.show()

io.imshow(edges)
io.show()
