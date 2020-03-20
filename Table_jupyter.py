#!/usr/bin/env python
# coding: utf-8

# In[1]:


import urllib.request
import pandas as pd


# In[2]:


url="https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"
post_list_html=urllib.request.urlopen(url).read()


# In[3]:


postal=pd.read_html(post_list_html)


# In[4]:


print(postal)


# In[5]:


from bs4 import BeautifulSoup
soup=BeautifulSoup(post_list_html,'lxml')


# In[6]:


soup.text


# In[7]:


soup.prettify()


# In[8]:


len(postal)


# In[9]:


print(postal[0])


# In[10]:


postal[0].columns


# In[11]:


postal[0].index


# In[12]:


import numpy as np
postal_array=np.array(postal[0])
code_postal=pd.DataFrame(postal_array,index=postal[0].index,columns=postal[0].columns)


# In[13]:


code_postal.head()


# In[14]:


code_postal.tail()


# In[15]:


code_postalr=code_postal[code_postal["Borough"]!="Not assigned"]


# In[16]:


print(code_postalr.head(10))


# In[17]:


code_postalm=code_postalr.copy()


# In[18]:


print(code_postalm.columns)


# In[33]:


code_postalr.Neighbourhood[code_postalm.Neighbourhood=="Not assigned"]= code_postalm.loc[code_postalm.Neighbourhood=="Not assigned",'Borough']


# In[20]:


code_postalr.head(10)


# In[21]:


mask=code_postalr.Postcode.duplicated(keep=False)


# In[22]:


code_postalr[mask]


# In[23]:


code_postalrw=code_postalr[~mask]


# In[24]:


code_postalrw.head(10)


# In[25]:


coder=code_postalr[mask]


# In[26]:


coder.index


# In[27]:


coder.Postcode


# In[28]:


coderw=coder.drop_duplicates(subset="Postcode",keep="first")


# In[29]:


coderw


# In[30]:


f=lambda x: ','.join(z for z in coder.loc[coder.Postcode==x,'Neighbourhood']) 


# In[31]:


for x in coderw.index:
    coderw.Neighbourhood[x]=f(coderw.Postcode[x])


# In[32]:


coderw


# In[43]:


code_full = pd.concat([code_postalrw,coderw], ignore_index='True')


# In[44]:


code_full


# In[ ]:




