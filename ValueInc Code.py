#!/usr/bin/env python
# coding: utf-8
# importing the necessary libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_row',100)

# Reading the dataset

df = pd.read_csv('transaction.csv',sep=';')
df.head()

# Getting the summary of the dataset

df.info()

# Creating new columns to better understand the dataset
df['CostPerTransaction'] = df['NumberOfItemsPurchased'] * df['CostPerItem']
df['SalesPerTransaction'] = df['NumberOfItemsPurchased'] * df['SellingPricePerItem']
df['ProfitPerTransaction'] = df['SalesPerTransaction'] - df['CostPerTransaction']
df['Markup'] = (df['ProfitPerTransaction'])/df['CostPerTransaction']


df.head()


# Rounding up the markup value to 2 decimal places

df['Markup'] = round(df['Markup'],2)


df.head()

# Changing dtype of the date Columns to create a combined date

day = df['Day'].astype(str)
year = df['Year'].astype(str)
df['Date'] = day+'-'+df['Month']+'-'+year


df.head()

# Splitting the Client Columns to get independent values

new_col = df['ClientKeywords'].str.split(',',expand=True)


df['ClientAge'] = new_col[0]
df['ClientType'] = new_col[1]
df['ContractLength'] = new_col[2]

df.head()

# Replacing unwanted values with nothing

df['ClientAge'] = df['ClientAge'].str.replace('[','')
df['ContractLength'] = df['ContractLength'].str.replace(']','')


df['ContractLength']

df['ItemDescription'] = df['ItemDescription'].str.capitalize()


df.head()


# Reading the seasons csv

seasons = pd.read_csv('value_inc_seasons.csv',sep=';')
seasons.info()

# merging both the dataset on month column to create a final dataset

final_df = pd.merge(df,seasons,on='Month')


final_df.head()


# Dropping unwanted Columns

final_df = final_df.drop(['Year','Month','Day','ClientKeywords'],axis=1)


final_df.head()

# Finding Out the missing values in the dataset

round(final_df.isnull().mean()*100,2)


final_df['ItemDescription'].value_counts(dropna=False).head()


final_df['ItemDescription'].isnull().sum()

# Replacing the missing values with the most occurring of ItemDescription

mode_rep = final_df['ItemDescription'].mode()[0]
final_df['ItemDescription'] = final_df['ItemDescription'].fillna(mode_rep)


final_df['ItemDescription'].isnull().sum()

# Using Boxplot the detect outliers in the column

sns.boxplot(data=final_df,x='Markup')


# Filling the missing value with mean since there are no outliers

mean_rep = final_df['Markup'].mean()
final_df['Markup'] =  final_df['Markup'].fillna(mean_rep)



final_df['Markup'].isnull().sum()

# Replacing unwanted items in columns with nothing

final_df['ClientAge'] = final_df['ClientAge'].str.replace("'","")
final_df['ClientType'] = final_df['ClientType'].str.replace("'","")
final_df['ContractLength'] = final_df['ContractLength'].str.replace("'","")


final_df.head()


final_df.to_csv('ValueInc_Cleaned.csv',index=False)


