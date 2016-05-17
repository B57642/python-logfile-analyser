
# coding: utf-8

# In[2]:

#importing all the package dependencies required
import re
#importing the current working directory
import os

#Open file to write the results
f = open("login_attempts.csv", "w")
#Directory to the Apache log file
logfile = "ApacheLogFile2.log"
#Current working directory 
filepath = os.getcwd()
#Open the Apache log file 
with open(logfile) as logfile,(f) as output:
    #Get a list of matches on the line for username and password attempts 
    attempts = re.findall(r'pma_username=(.*)&pma_password=(.*)\sHTTP', logfile.read())
    #When we get a list of each of the usernames and passwords we print and write them to the csv
    for attempt in attempts:
        #Print the username and password attempts side by side
        print(attempt[0] + ',' + attempt[1])
        #Output the attempts made to the .csv created 
        output.write(attempt[0] + ',' + attempt[1] + '\n') 
#close the file
output.close()

