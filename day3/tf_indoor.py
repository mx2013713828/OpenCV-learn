# encoding=utf-8
#p55-60 随机生成一个权重矩阵，测试 给出 x1，x2后，所得到的结果，一个简单的前向传播！
import tensorflow as tf

w1 = tf.Variable(tf.random_normal([2,3],stddev=1,seed=1))
w2 = tf.Variable(tf.random_normal([3,1],stddev=1,seed=1))

x = tf.constant([[0.7,0.9]])

a=tf.matmul(x,w1)
y= tf.matmul(a,w2)
sess=tf.Session()
# sess.run(w1.initializer)
# sess.run(w2.initializer)
init_op=tf.initialize_all_variables() #初始化辩论  赋值

sess.run(init_op)
print sess.run(y)
sess.close()