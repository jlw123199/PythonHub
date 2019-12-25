import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
# 下面方法二选一
# 直接 API下载
import tensorflow.examples.tutorials.mnist as input_data

# 文件路径下获取
# import input_data
# print ("packs loaded.")
print ("download and extract mnist dataset...")
# 独热编码（One-Hot Encoding）
mnist = input_data.read_data_sets('data/', one_hot = True)
print
print ("type of mnist is %s" % (type(mnist)))
print ("number of train data is %d" % (mnist.train.num_examples))
print ("number of test data is %d" % (mnist.test.num_examples))
