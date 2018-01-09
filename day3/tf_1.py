# encoding=utf-8
import tensorflow as tf

w1 = tf.Variable(tf.random_normal([2,3],stddev=1,seed=1))
w2 = tf.Variable(tf.random_normal([3,1],stddev=1,seed=1))

x = tf.placeholder(tf.float32,shape=(3,2),name="input")
#用placeholder 机制 提供输入数据，定义一个位置，数据在运行时指定
#shape 代表输入的x 的维度，可以不加，自动识别，（3，2）代表3条数据，每条数据两个属性

a = tf.matmul(x,w1)
y = tf.matmul(a,w2)

sess = tf.Session()

init_op = tf.initialize_all_variables()
sess.run(init_op)

print sess.run(y,feed_dict={x:[[0.7,0.9],[0.8,0.4],[0.6,1.0]]}) #指定placeholder中的数据