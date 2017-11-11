
# coding: utf-8

# In[377]:


import pandas as pd
import numpy as np



# In[378]:


budgetdata = pd.read_csv("../raw_data/budget_data_combined.csv", low_memory=False)
budgetdata.count()
budgetdata.dropna(how='any')


# In[379]:


# The total number of months included in the dataset
months = budgetdata["Date"].count()
print("Total Months: " + str(months))


# In[380]:


# The total amount of revenue gained over the entire period

revenue = budgetdata["Revenue"].value_counts()
print("Total Revenue: $" + str(revenue))


# In[381]:


# The average change in revenue between months over the entire period
# Three Variables: Month_A, Month_B, Month_Dif
#--- Loop Begin 

i = 0
Month_A = 0.0
Month_B = 0.0
Month_Dif = 0.0
sumtable = 0.0

for i in range(126): 
    Month_A = budgetdata["Revenue"][i]
    Month_B = budgetdata["Revenue"][i+1]
    Month_Dif = Month_B - Month_A
    sumtable = Month_Dif + sumtable 
    

avgchange = sumtable/126
print("Average Change in Revenue is: $" + str(avgchange))


# In[382]:


# The greatest increase in revenue (date and amount) over the entire period
i = 0
Month_A = 0.0
Month_B = 0.0
Month_Dif = 0.0
current_max = 0.0
date = ''

for i in range(126): 
    Month_A = budgetdata["Revenue"][i]
    Month_B = budgetdata["Revenue"][i+1]
    Month_Dif = Month_B - Month_A
    
    if Month_Dif > current_max:
    
        current_max = Month_Dif 
        date = budgetdata["Date"][i+1]
   
great_inc = current_max
print("Greatest Increase in Revenue: $" + str(great_inc) + " - " + date)


# In[383]:


# The greatest decrease in revenue (date and amount) over the entire period


# In[384]:


i = 0
Month_A = 0.0
Month_B = 0.0
Month_Dif = 0.0
current_min = 0.0
date = ''

for i in range(126): 
    Month_A = budgetdata["Revenue"][i]
    Month_B = budgetdata["Revenue"][i+1]
    Month_Dif = Month_B - Month_A
    if Month_Dif < current_min:
    
        current_min = Month_Dif 
        date = budgetdata["Date"][i+1]
    
   
great_dec = current_min
print("Greatest Decrease in Revenue: $" + str(great_dec) + " - " + date)

