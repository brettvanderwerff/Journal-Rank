import pandas as pd
import numpy as np
pd.set_option('display.max_columns', 500)


#Read in journal list csv and convert to dataframe
df = pd.read_csv('journal_list.csv', sep=';')
print(df.shape)
df_drop_dup = df.drop_duplicates(['Title'])
print((df_drop_dup.shape))
print(df_drop_dup.head())

print(df_drop_dup.isna().sum())

df_drop_dup = df_drop_dup.dropna(subset=['Publisher'])

print(df_drop_dup.isna().sum())
