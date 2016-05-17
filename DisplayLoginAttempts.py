
# coding: utf-8

# In[6]:

#importing all the package dependencies required
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#Setting the style for all our graphs withtin this script
matplotlib.style.use('ggplot')

#Magical expression to create our graphs
get_ipython().magic(u'matplotlib inline')
#Reading in the csv with all login credentials attempted in FindLoginAttempts
loginAttempts = pd.read_csv("login_attempts.csv")
#Inputting the csv into a data frame
df = pd.DataFrame(loginAttempts)
#Name the columns username and password
df.columns = ['username','password']


# In[4]:

#Display the data frame
df


# In[9]:

#Create a new data frame with just the username column 
total_usernames = df[['username']]
#Count the total size of each username used and plot it on the graph
total_usernames.username.value_counts().plot.barh(figsize=(10,10))
plt.title('Number of appearances in dataset')
plt.xlabel('Frequency')
plt.ylabel('Usernames')
#Save the graph to .png image
plt.savefig('username_attempts.png',bbox_inches='tight')

