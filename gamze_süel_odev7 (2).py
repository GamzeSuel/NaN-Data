# -*- coding: utf-8 -*-
"""GAMZE_SÜEL_ODEV7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ci4VyrDwsSDN-vV8jDMn8q51Kc5ncQC4
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("MOCK_DATA (2).csv")
df

df.info()

num_col = df.select_dtypes(include='number')
num_col

df.describe().T

cat_col = df.select_dtypes(include='object')
cat_col

cat_col.isnull().sum()

100*df.isnull().sum() / len(df)

def percent_missing(df):
    percent_nan = 100*df.isnull().sum() / len(df)
    percent_nan = percent_nan[percent_nan>0].sort_values()
    return percent_nan

percent_nan = percent_missing(df)

plt.figure(figsize=(12,10))

sns.barplot(x=percent_nan.index,y=percent_nan, palette="rocket_r")
plt.xticks(rotation=90);
plt.show()

100/len(df)

df[df['last_name'].isnull()]

percent_nan = percent_missing(df)

plt.figure(figsize=(12,10))

sns.barplot(x=percent_nan.index,y=percent_nan, palette="rocket_r")
plt.xticks(rotation=90);
plt.show()

df["last_name"]=df['last_name'].fillna('None')
df["gender"]=df['gender'].fillna('None')
df

percent_nan = percent_missing(df)

plt.figure(figsize=(12,10))

sns.barplot(x=percent_nan.index,y=percent_nan, palette="rocket_r")
plt.xticks(rotation=90);
plt.show()

df.info()

df["email"]=df['email'].fillna('None')
df["ip_address"]=df['ip_address'].fillna('None')
df

percent_nan = percent_missing(df)

plt.figure(figsize=(12,10))

sns.barplot(x=percent_nan.index,y=percent_nan, palette="rocket_r")
plt.xticks(rotation=90);
plt.show()

df["number"]=df['number'].fillna(0)
df

percent_nan = percent_missing(df)

plt.figure(figsize=(12,10))

sns.barplot(x=percent_nan.index,y=percent_nan, palette="rocket_r")
plt.xticks(rotation=90);
plt.show()

df['first_name']=df['first_name'].fillna('None')
df

percent_nan = percent_missing(df)

plt.figure(figsize=(12,10))

sns.barplot(x=percent_nan.index,y=percent_nan, palette="rocket_r")
plt.xticks(rotation=90);
plt.show()

percent_nan

df.to_csv("MOCK_DATA (3)", index=False)