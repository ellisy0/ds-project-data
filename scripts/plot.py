import pandas as pd
import matplotlib.pyplot as plt

# load data into a pandas dataframe
df = pd.read_csv('data/london-spm.csv')

# extract year and SPM columns
year = df['Year']
spm = df['Suspended Particulate Matter (SPM) (Fouquet and DPCC (2011))']

# plot the data
plt.plot(year, spm)

# set chart title and axis labels
plt.title('London Suspended Particulate Matter (SPM) over Time')
plt.xlabel('Year')
plt.ylabel('SPM')

# display the chart
plt.show()
