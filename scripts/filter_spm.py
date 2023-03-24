import pandas as pd

# load the csv file
df = pd.read_csv('data/air-pollution-vs-gdp-per-capita.csv')

# filter rows where Suspended Particulate Matter (SPM) (Fouquet and DPCC (2011)) is not null
df_filtered = df[df['Suspended Particulate Matter (SPM) (Fouquet and DPCC (2011))'].notnull()]

# save the filtered data to a new csv file
df_filtered.to_csv('data/filtered-air-pollution-vs-gdp-per-capita.csv', index=False)
