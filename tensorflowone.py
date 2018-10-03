#-*- coding:utf-8 -*-

import tensorflow as tf
import os
#设置它的显示等级
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1' #默有认的显示等级，显示所有信息
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' #只显示Error
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' #只显示warning 和 Error
node1 = tf.constant(3.0,dtype = tf.float32)
node2 = tf.constant(4.0,dtype = tf.float32)
node3 = tf.add(node1,node2)
sess = tf.Session()
print(sess.run(node3))