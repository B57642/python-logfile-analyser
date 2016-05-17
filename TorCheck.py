
# coding: utf-8

# In[14]:

#Implement the Pandas software library
import pandas as pd
#Read in the iplocation.csv so we can assign it to a dataframe
iplist = pd.read_csv("iplocation.csv")
#Create the data frame and implement the csv
df = pd.DataFrame(iplist)
#Assign names to the columns
df.columns = ['time_stamp', 'ip', 'country', 'city']
#Display the first five rows for the data frame
df.head()


# In[15]:

#Create a data frame with only the ip addresses from our access.log files
access_log = df[['ip']]
access_log.columns = ['ip']
access_log.head()


# In[16]:

#Read in the tor_node_ip.csv created in GetTorNodeIp script 
tor_nodes = pd.read_csv("tor_node_ip.csv")
#Create a data frame from the tor_node_ip.csv with the full list of Tor node IP's
tor_nodes_df = pd.DataFrame(tor_nodes)
#Set the column name 
tor_nodes_df.columns = ['ip']
tor_nodes_df.head()


# In[17]:

#Merge the two date frames on the column IP and include only the values that are in both
tor_node_ip_matches = pd.merge(tor_nodes_df, access_log, on=['ip'], how='inner')
tor_node_ip_matches


# In[18]:

#Display the IP address details from our original data frame
node_one_ip_details = df[df['ip'] == '107.181.174.84']
node_one_ip_details


# In[19]:

#Display the IP address details from our original data frame
node_two_ip_details = df[df['ip'] == '64.113.32.29']
node_two_ip_details

