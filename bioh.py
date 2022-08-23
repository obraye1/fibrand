#!/usr/bin/env python
# coding: utf-8

# # -----------------------------------------------------------------------------------------
# 
# 

# In[1]:


import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import plotly.express as px 
import os 
import psycopg2
import sqlalchemy as sa
from datacleaner import autoclean


# # -----------------------------------------------------------------------------------------
# 
# 

# -------------------------------------------------------------------------------------------------------------------
# 

# ## Questions to answer
# 1.      Which color of shirt is the mean color?
# 2.      Which color is mostly worn throughout the week?
# 3.      Which color is the median?
# 4.      BONUS Get the variance of the colors
# 5.      -BONUS if a colour is chosen at random, what is the probability that the color is red?
# 6.      Save the colours and their frequencies in postgresql database
# 7.      BONUS write a recursive searching algorithm to search for a number entered by user in a list of numbers.
# 8.      Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10.
# 9.      Write a program to sum the first 50 fibonacci sequence.
# 

# -------------------------------------------------------------------------------------------------------------------
# 

# In[5]:


df = pd.read_csv('table.csv', delimiter =',')


# In[6]:


df.head()


# -------------------------------------------------------------------------------------------------------------------
# 

# In[7]:


df.COLOURS.nunique()


# In[8]:


Days = ['MONDAY' 'TUESDAY WEDNESDAY', 'THURSDAY', 'FRIDAY']


# In[9]:


clrs2 = df['COLOURS'].str.split(',', expand = True)
# clrs2


# -------------------------------------------------------------------------------------------------------------------
# 

# In[10]:


clrs2.loc[1].value_counts()


# In[15]:


clrs2.loc[1].value_counts().plot(color = 'm')
plt.xlabel('Colors')
plt.ylabel('Frequceny')


# -------------------------------------------------------------------------------------------------------------------
# 

# ###  Daily REVIEW

# # -----------------------------------------------------------------------------------------
# 

# In[17]:


monday = clrs2.loc[0]
tuesday = clrs2.loc[1]
wednesday = clrs2.loc[2]
thursday = clrs2.loc[3]
friday = clrs2.loc[4]


# In[18]:


monn = monday.value_counts().to_dict()
# type(frii)
mon_s = []
mon_s.append(monn)


# In[19]:


df1 = pd.DataFrame(monn,index=['MONDAY'])
# df1


#  -----------------------------------------------------------------------------------------

# In[20]:


tuee = tuesday.value_counts().to_dict()
# type(frii)
tue_s = []
tue_s.append(tuee)


# In[21]:


df2 = pd.DataFrame(tue_s,index=['TUESDAY'])
# df2


#  -----------------------------------------------------------------------------------------

# In[22]:


wedd = wednesday.value_counts().to_dict()
# type(frii)
wed_s = []
wed_s.append(wedd)


# In[23]:


df3 = pd.DataFrame(wed_s,index=['WEDNESDAY'])


# thurr = thursday.value_counts().to_dict()
# thur_s = []
# thur_s.append(thurr)
# 

#  -----------------------------------------------------------------------------------------

# In[25]:


df4 = pd.DataFrame(thur_s,index=["THURSDAY"])
# df4


# In[26]:


frii = friday.value_counts().to_dict()
# type(frii)
fri_s = []
fri_s.append(frii)


# In[27]:


df5 = pd.DataFrame(fri_s,index=['FRIDAY'])
# df5


#  -----------------------------------------------------------------------------------------

# In[28]:


frames = [df1, df2, df3, df4, df5]
result = pd.concat(frames)
result


# # Frequencey Table
# 

# #  -----------------------------------------------------------------------------------------

# In[134]:


freq_table = result.sum()
# freq_table
df_freq = pd.Series(freq_table)
fin = pd.to_numeric(df_freq)
fin.describe().plot()


# #  -----------------------------------------------------------------------------------------

# ## Which color of shirt is the mean color?
# 

# In[133]:


fin.mean()


# ### BLUE
# 

#  # -----------------------------------------------------------------------------------------

# ## Which color is mostly worn throughout the week?

# In[38]:


mon = monday.value_counts()
mon_stats = monday.describe()
mon_stats


# In[40]:


tues = tuesday.value_counts()
tues_stats = tuesday.describe() 
tues_stats


# In[132]:


wed = wednesday.value_counts()
wed_stats = wednesday.describe()
wed_stats


# In[131]:


thurs = thursday.value_counts()
thurs_stats = thursday.describe()
thurs_stats


# In[139]:


fri = friday.value_counts()
fri_stats = friday.describe()
fri_stats


# #  -----------------------------------------------------------------------------------------

#  # -----------------------------------------------------------------------------------------

# ### BLUE is worn mostly throughout the week

#  -----------------------------------------------------------------------------------------

# ## Which color is the median?

# #### The Median Color is Blue

# ## BONUS Get the variance of the colors

# ### variance of the color - 58.950549

# In[145]:


dg.var()


# In[125]:


top = {}
top["mon"] = mon_stats.top
top["tues"] =tues_stats.top
top["wed"] = wed_stats.top 
top["thurs"] =thurs_stats.top
top["fri"] = fri_stats.top


# In[127]:


finn = pd.DataFrame(fin)
fin3 = autoclean(finn)
fin3.shape


# In[63]:


dg = pd.DataFrame(freq_table)
dg


# # TOP colour of each day
# 

# # -----------------------------------------------------------------------------------------
#     - Database Connection 
# # -----------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------

# In[147]:


# !pip install pymysql


# In[91]:



# import pymysql
# connection = pymysql.connect(host='localhost',
#                              user='username',
#                              password='password',
#                              db='database')


# In[117]:


# cursor = connection.cursor()
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# sql ='''CREATE TABLE Frequnecy(
#    Colors CHAR(20) NOT NULL,
#    Frequncy INT
# )'''
# cursor.execute(sql)
# # 


# In[118]:


# .style.to_sql('Frequnecy', connection, if_exists='append')


# In[119]:


# # creating column list for insertion 
# cols = "','".join([str(i) for i in dg.columns.tolist()])
# # Insert DataFrame records one by one. 
# for i,row in dg.iterrows():
#     sql = "INSERT INTO 'Frequnecy' ('" +cols + "') VALUES (" + "%s,"*(len(row)-1) + "%s) "
#     cursor.execute(sql, tuple(row)) 
# # the connection is not autocommitted by default, so we must commit to save our # changes 
# #     connection.commit()


# In[121]:


# connection.close()


# # -----------------------------------------------------------------------------------------

# In[109]:



dg.style


# # -----------------------------------------------------------------------------------------

# # -----------------------------------------------------------------------------------------

# In[ ]:




