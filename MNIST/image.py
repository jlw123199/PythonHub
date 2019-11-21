import os

import matplotlib.pyplot as plt

import dbreader

from MNIST.dbreader import load_mnist
from TensorFlow.learn1 import y_train

X_train, labels = dbreader.load_mnist(os.curdir)

fig, ax = plt.subplots(
    nrows=2,
    ncols=5,
    sharex=True,
    sharey=True, )

ax = ax.flatten()

for i in range(10):
    # img = X_train[y_train == i][0].reshape(28, 28)
    img = X_train[y_train == i][0].reshape(28, 28)
    ax[i].imshow(img, cmap='Greys', interpolation='nearest')

ax[0].set_xticks([])
ax[0].set_yticks([])
plt.tight_layout()
plt.show()
