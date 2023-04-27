#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_row',100)


# In[2]:


df = pd.read_csv('transaction.csv',sep=';')


# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


df['CostPerTransaction'] = df['NumberOfItemsPurchased'] * df['CostPerItem']
df['SalesPerTransaction'] = df['NumberOfItemsPurchased'] * df['SellingPricePerItem']
df['ProfitPerTransaction'] = df['SalesPerTransaction'] - df['CostPerTransaction']
df['Markup'] = (df['ProfitPerTransaction'])/df['CostPerTransaction']


# In[6]:


df.head()


# In[7]:


df['Markup'] = round(df['Markup'],2)


# In[8]:


df.head()


# In[9]:


day = df['Day'].astype(str)
year = df['Year'].astype(str)
df['Date'] = day+'-'+df['Month']+'-'+year


# In[10]:


df.head()


# In[11]:


round(df.isnull().mean()*100,2)


# In[12]:


new_col = df['ClientKeywords'].str.split(',',expand=True)


# In[13]:


df['ClientAge'] = new_col[0]
df['ClientType'] = new_col[1]
df['ContractLength'] = new_col[2]


# In[14]:


df.head()


# In[15]:


df['ClientAge'] = df['ClientAge'].str.replace('[','')
df['ContractLength'] = df['ContractLength'].str.replace(']','')


# In[16]:


df['ContractLength']


# In[17]:


df['ItemDescription'] = df['ItemDescription'].str.capitalize()


# In[18]:


df.head()


# In[19]:


seasons = pd.read_csv('value_inc_seasons.csv',sep=';')


# In[20]:


seasons.info()


# In[21]:


final_df = pd.merge(df,seasons,on='Month')


# In[22]:


final_df.head()


# In[23]:


final_df = final_df.drop(['Year','Month','Day','ClientKeywords'],axis=1)


# In[24]:


final_df.head()


# In[25]:


round(final_df.isnull().mean()*100,2)


# In[26]:


final_df['ItemDescription'].value_counts(dropna=False).head()


# In[27]:


final_df['ItemDescription'].isnull().sum()


# In[28]:


mode_rep = final_df['ItemDescription'].mode()[0]
final_df['ItemDescription'] = final_df['ItemDescription'].fillna(mode_rep)


# In[29]:


final_df['ItemDescription'].isnull().sum()


# In[30]:


sns.boxplot(data=final_df,x='Markup')


# In[31]:


mean_rep = final_df['Markup'].mean()
final_df['Markup'] =  final_df['Markup'].fillna(mean_rep)


# In[32]:


final_df['Markup'].isnull().sum()


# In[39]:


final_df['ClientAge'] = final_df['ClientAge'].str.replace("'","")
final_df['ClientType'] = final_df['ClientType'].str.replace("'","")
final_df['ContractLength'] = final_df['ContractLength'].str.replace("'","")


# In[40]:


final_df.head()


# In[41]:


final_df.to_csv('ValueInc_Cleaned.csv',index=False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




