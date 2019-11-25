import numpy as np

data = [1,3,3,4,5,6,5,5,5]

categories = np.unique(data,  return_counts=True)

print(categories)

a = np.array([[1, 1], [2, 3]])

print(a)

print( np.unique(a) )