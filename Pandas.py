
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().magic(u'matplotlib inline')

iplist = pd.read_csv("iplocation.csv")
df = pd.DataFrame(iplist)

df.columns = ['time_stamp', 'ip', 'country', 'city']


# In[5]:

df.head()


# In[6]:

df.tail()


# In[7]:

df_filtered = df[df['country'] !='Ireland']

df_filtered


# In[8]:

df_filtered['ip'].describe()


# In[9]:

df_filtered['time_stamp'].describe()


# In[10]:

df_filtered['country'].describe()


# In[11]:

df_filtered['city'].describe()


# In[12]:

df_filtered.dtypes


# In[13]:

visitors = df_filtered[['ip', 'country']]
visitors.head()


# In[14]:

visitor_group = visitors.groupby('country')
total_visitors = visitor_group.size()
total_visitors


# In[15]:

df_filtered.country.value_counts().plot(kind='barh')
plt.title('Number of appearances in dataset')
plt.xlabel('Frequency')


# In[16]:

df_filtered.country.value_counts().plot(kind='barh', figsize=(10,10))
plt.title('Number of appearances in dataset')
plt.xlabel('Frequency')


# In[17]:

ax12 = plt.subplot2grid((2,2), (0,1))
labels = ["bewarfefvl","easdfgvagfvd","asasdfve.sd",
              "rgdegaf","adfewga","qargw","qaerghrttw","errrrd","ejjjjd"]
ax12.pie( [10,20,30,5,5,6,4,10,10], [0,0,0.0,0.1,0.3,.5,0,0,0], 
                          labels = labels, labeldistance=1.2)


# In[ ]:



