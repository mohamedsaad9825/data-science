#!/usr/bin/env python
# coding: utf-8

# # NumPy Exercises 
# 
# 

# #### Import NumPy as np

# In[1]:


import numpy as np


# #### Create an array of 10 zeros 

# In[2]:


np.zeros(10)


# #### Create an array of 10 ones

# In[3]:


np.ones(10)


# #### Create an array of 10 fives

# In[6]:


x=np.array(5,5,5,5,5,5,5,5,5,5)


# #### Create an array of the integers from 10 to 50

# In[9]:


np.linspace(10,50,41)


# #### Create an array of all the even integers from 10 to 50

# In[10]:


np.arange(10,51,2)


# #### Create a 3x3 matrix with values ranging from 0 to 8

# In[11]:


np.array([[0,1,2],[3,4,5],[6,7,8]])


# #### Create a 3x3 identity matrix

# In[13]:


np.eye(3)


# #### Use NumPy to generate a random number between 0 and 1

# In[14]:


np.random.rand(1)


# #### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

# In[15]:


np.random.randn(5,5)


# #### Create the following matrix:

# In[19]:


np.array([np.arange(0.01,0.11,0.01),np.arange(0.11,0.21,0.01),np.arange(0.21,0.31,0.01),np.arange(0.31,0.41,0.01),np.arange(0.41,0.5,0.01),np.arange(0.51,0.61,0.01),np.arange(0.61,0.71,0.01),np.arange(0.71,0.8,0.01),np.arange(0.81,0.91,0.01),np.arange(0.91,1.01,0.01)])


# In[23]:


x=np.arange(0.01,1.01,0.01)
x


# In[24]:


x.reshape(10,10)


# #### Create an array of 20 linearly spaced points between 0 and 1:

# In[20]:


np.random.rand(20)


# ## Numpy Indexing and Selection
# 
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

# In[28]:


y=np.arange(1,26,1).reshape(5,5)
y


# In[39]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[53]:


a=np.array([y[2,],y[3,],y[4,]])
a=np.delete(a,0,axis=1)
a


# In[29]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[30]:


y[3,4]


# In[30]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[99]:


np.array([y[0,1],y[1,1],y[2,1]]).T


# In[31]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[66]:


y[4]


# In[32]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[69]:


np.array([y[3],y[4]])


# ### Now do the following

# #### Get the sum of all the values in mat

# In[70]:


y.sum()


# #### Get the standard deviation of the values in mat

# In[71]:


y.std()


# #### Get the sum of all the columns in mat

# In[91]:


np.array(y.sum(0))


# In[92]:


y


# In[96]:


y.sum(0)


# In[ ]:




