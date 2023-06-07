#!/usr/bin/env python
# coding: utf-8

# # Reading in Files using Pandas

# In[19]:


import pandas as pd


# Below is a demonstration of how to read a csv in python using Pandas

# In[7]:


pd.read_csv(r"C:\Users\natee\OneDrive\Desktop\Tableau Materials\csv files\bq-results-20230422-202038-1682194885305.csv")


# You can also change the names of the header colum using the process below

# In[11]:


pd.read_csv(r"C:\Users\natee\OneDrive\Desktop\Tableau Materials\csv files\bq-results-20230422-202038-1682194885305.csv", header = None, names = ['Country', 'Pop', 'Date', 'Max Infection Count', '% Pop Infected'], low_memory=False)


# It can be useful to save .csv files as dataframes to make them easier to use and call

# In[12]:


df = pd.read_csv(r"C:\Users\natee\OneDrive\Desktop\Tableau Materials\csv files\bq-results-20230422-202038-1682194885305.csv")
df


# In[43]:


pd.read_csv(r"C:\Users\natee\OneDrive\Desktop\Tableau Materials\csv files\Tableau Table 3.csv")


# Pandas can be used to read other file types, incluing .Json flies

# In[34]:


df = pd.read_json(r"C:\Users\natee\Downloads\sample-json-file.json", typ="series")
df


# Or .xslx files

# In[44]:


df = pd.read_excel(r"C:\Users\natee\OneDrive\Desktop\PowerBI Tutorial Materials\Apocolypse Food Prep.xlsx")
df


# In[42]:


pd.set_option('display.max.rows', 25)

