import keras
# import pandas

import tensorflow as tf

def main():
    A = tf.constant([[1, 2], [3, 4]])
    B = tf.constant([[5, 6], [7, 8]])
    C = tf.matmul(A, B)
    print(A.shape)
    print(A.numpy())
    C = tf.add(A,B)
    print(C)
    D = tf.multiply(A,B)
    print(D)
    E = tf.matmul(A,B)
    print(E)

def gradientTape():
    # x = tf.Variable(initial_value=3.)
    # with tf.GradientTape() as tape:  # 在 tf.GradientTape() 的上下文内，所有计算步骤都会被记录以用于求导
    #     y = tf.square(x)
    # y_grad = tape.gradient(y, x)  # 计算y关于x的导数
    # print([y])

    X = tf.constant([[1., 2.], [3., 4.]])
    y = tf.constant([[1.], [2.]])
    w = tf.Variable(initial_value=[[1.], [2.]])
    b = tf.Variable(initial_value=1.)
    with tf.GradientTape() as tape:
        L = 0.5 * tf.reduce_sum(tf.square(tf.matmul(X, w) + b - y))
    w_grad, b_grad = tape.gradient(L, [w, b])  # 计算L(w, b)关于w, b的偏导数
    print([L.numpy(), w_grad.numpy(), b_grad.numpy()])

def function():
    import numpy as np

    X_raw = np.array([2013, 2014, 2015, 2016, 2017], dtype=np.float32)
    y_raw = np.array([12000, 14000, 15000, 16500, 17500], dtype=np.float32)

    X = (X_raw - X_raw.min()) / (X_raw.max() - X_raw.min())
    y = (y_raw - y_raw.min()) / (y_raw.max() - y_raw.min())

    print(X)
    print(y)
if __name__ =="__main__":
    # main()
    # gradientTape()
    function()



