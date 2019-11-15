
import sys
sys.path.append("..") # 引入上层目录

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2

import utility
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


# tf.enable_eager_execution()

def Test():
    x = np.arange(0, 5, 0.1)
    utility.PrintSplit()
    print("X: ", x)
    y = x ** 3 - 4 * x ** 2 - 2 * x + 2
    utility.PrintSplit()
    print ( "y: ", y)
    noise = np.random.normal(0, 1.5, size=(len(x),));
    utility.PrintSplit()
    print ( "noise: ", noise)
    y_noise = y + noise
    utility.PrintSplit()
    print ( "y_noise: ", y_noise)
    plt.plot(y_noise)


    y_noise_removed = y_noise - noise
    utility.PrintSplit()
    print("y_noise_removed: ", y_noise_removed)

    plt.show()
class Model(object):
    def __init__(self):
        self.w = tf.Variable(np.random.normal([4])) # The 4 parameters
    def f(self, x):
        return self.w[0] * x ** 3 + self.w[1] * x ** 2 + self.w[2] * x + self.w[3]

def Loss(model, x, y):
    err = model.f(x) - y
    return tf.reduce_mean(tf.square(err))

def Calc():
    x = np.arange(0, 5, 0.1)
    y = x ** 3 - 4 * x ** 2 - 2 * x + 2
    noise = np.random.normal(0, 1.5, size=(len(x),));

    model = Model();

    data = Loss(model,x,y)
    # plt.plot(data)
    # plt.show()


if __name__ == "__main__":
    # Test()
    utility.PrintSplit()
    Calc()

