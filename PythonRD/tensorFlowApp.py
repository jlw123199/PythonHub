
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2

import tensorflow as tf
import numpy as np

# tf.enable_eager_execution()
tf.executing_eagerly()

def run():
    x = [[2.]]
    m = tf.matmul(x, x)
    print (tf.add(1, 2))
    tf.print(m)


if __name__ == '__main__':
    print ('greet')
    run()



