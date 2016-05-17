
# coding: utf-8

# In[2]:

#Import dependencies to use
import re
#Create a new .csv file to store all the ip addresses in 
f = open("tor_node_ip.csv", "w")
#Open up the text file with all the tor node information
for line in open('tor_nodes.txt'):
        #Go through each line to find the IP address
        ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)[:1]
        #Write each IP address it finds to the just created .csv
        f.write(ip[0] + "\n")
        #Print the results to the screen
        print(str(ip))
#Close the created file
f.close()

