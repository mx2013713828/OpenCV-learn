# coding:utf-8
#select 和 greater 函数的使用 ~
import tensorflow as tf
v1 = tf.constant([1.0,2.0,3.0,4.0])
v2 = tf.constant([4.0,3.0,2.0,1.0])

sess = tf.InteractiveSession()

#greater 函数 ，比较两个张量每一个元素的大小，并返回比较结果。
print tf.greater(v1,v2).eval()

#select 函数 3个参数，第一个是选择条件布尔值，True，选第二个参数值，False 选择第三个参数的值
print tf.select(tf.greater(v1,v2),v1,v2).eval()

sess.close()