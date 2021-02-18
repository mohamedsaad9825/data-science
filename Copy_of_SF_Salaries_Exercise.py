#!/usr/bin/env python
# coding: utf-8

# ** Import pandas as pd.**

# In[16]:


import pandas as pd


# ** Read Salaries.csv as a dataframe called sal.**

# In[18]:


df=pd.read_csv('Copy of Copy of Salaries.csv - Copy of Copy of Salaries.csv.csv')


# ** Check the head of the DataFrame. **

# In[21]:


df.tail()


# ** Use the .info() method to find out how many entries there are.**

# In[22]:


df.info()


# **What is the average BasePay ?**

# In[24]:


df['BasePay'].mean()


# ** What is the highest amount of OvertimePay in the dataset ? **

# In[26]:


df['OvertimePay'].max()


# ** What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **

# In[33]:


df[df['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle']


# ** How much does JOSEPH DRISCOLL make (including benefits)? **

# In[37]:


df.loc[[24],['TotalPayBenefits']]


# ** What is the name of highest paid person (including benefits)?**

# In[42]:


df[df['TotalPayBenefits']==max(df['TotalPayBenefits'])]


# ** How many unique job titles are there? **

# In[43]:


df['JobTitle'].nunique()


# ** What are the top 5 most common jobs? **

# In[51]:


df['JobTitle'].value_counts().head()


# ** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **

# In[45]:


sum(df[df['Year']==2013]['JobTitle'].value_counts()==1)


# # Great Job!
