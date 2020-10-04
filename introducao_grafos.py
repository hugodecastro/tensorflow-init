#!/usr/bin/env python
# coding: utf-8

# ### Grafos

# In[1]:


import tensorflow as tf


# In[9]:


a = tf.constant(5)
b = tf.constant(3)
c = tf.constant(2)

d = tf.multiply(a,b)
e = tf.add(b,c)
f = tf.subtract(d,e)

sess = tf.Session()
saida = sess.run(f)
sess.close()


# In[10]:


print(saida)


# In[6]:


print(f)

