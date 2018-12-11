import pandas as pd
pd.set_option('display.max_columns', 500)


#Read in journal list csv and convert to dataframe
df = pd.read_csv('journal_list.csv', sep=';')

for item in df[df.Type == 'journal']['Title']:
    print(item)

