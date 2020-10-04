#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf


# In[9]:


frase = tf.constant('Hello World!')


# In[10]:


# with tf.Session() as sess:
#     rodar = sess.run(frase)


# In[13]:


print(tf.Session().run(frase))


# In[14]:


print(frase)  # tensorflow só exibe o valor da variável quando criado uma sessão

