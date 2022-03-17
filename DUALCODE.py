#!/usr/bin/env python
# coding: utf-8

# In[1]:


G = Matrix(GF(2), [[1,0,0,0,0,1,1],[0,1,0,0,1,0,1],[0,0,1,0,1,1,0],[0,0,0,1,1,1,1]])
C = LinearCode(G)
C


# In[2]:


C.generator_matrix()


# In[3]:


C.parity_check_matrix()


# In[4]:


D=C.dual_code()
D


# In[5]:


cH=D.parity_check_matrix()
cH


# In[6]:


cG=D.generator_matrix()
cG


# In[7]:


c=LinearCode(cG)
c


# In[8]:


E=D.dual_code()
E


# In[9]:


E==C


# In[ ]:




