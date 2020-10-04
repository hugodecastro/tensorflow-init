#!/usr/bin/env python
# coding: utf-8

# ### Tensores

# In[1]:


import tensorflow as tf


# In[2]:


a = tf.constant(2)
b = tf.constant([3,1,5,8,6])  # 1xn
c = tf.constant([[2,0,4], [3,5,7]])  #nxn

sess = tf.Session()
saida = sess.run(c)
sess.close()


# In[4]:


import numpy as np


# In[5]:


a1 = np.array(2)
b1 = np.array([3,1,5,8,6])
c1 = np.array([[2,0,4], [3,5,7]])


# In[6]:


print(a.shape)  # imprime a dimensão


# In[7]:


print(a1.shape)


# In[8]:


print(b.shape)


# In[9]:


print(b1.shape)


# In[11]:


print(c.shape)


# In[12]:


print(c1.shape)


# In[13]:


const = tf.constant(4.0)


# In[14]:


print(const)

