
# coding: utf-8

# In[108]:


import pandas as pd
import numpy as np


# In[109]:


data_file = "raw_data/election_data_2.csv"


# In[110]:


data_file_pd = pd.read_csv(data_file)
data_file_pd.head()


# In[111]:


print("Election Results")
print("-------------------------")


# In[112]:


# The total number of votes cast

total_votes = data_file_pd["Voter ID"].count()
print("Total Votes: " + str(total_votes))


# In[113]:


# A complete list of candidates who received votes
# The total number of votes each candidate won

candidates = data_file_pd["Candidate"].value_counts(dropna=False) 

print("Distribution of Votes")
print("---------------------")
print(str(candidates))


# In[114]:


# The percentage of votes each candidate won

votes_percent = (candidates/total_votes) * 100
print("Distribution of Votes(%)")
print("------------------------")
print(str(votes_percent))


# In[115]:


# The winner of the election based on popular vote.


# In[117]:


print("------------------------")
print("         Winner         ")
print("------------------------")

i = 0
candidate_1 = 0
candidate_2 = 0
winner = 0


for i in range(4):
    candidate_1 = data_file_pd["Candidate"][i]
    candidate_2 = data_file_pd["Candidate"][i + 1]

    if candidate_2 > candidate_1:
        winner = candidate_2
    else 
        winner = candidate_1
        
print(str(winner))
    

