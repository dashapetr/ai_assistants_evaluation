# visualization for time series data


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# read data


df = pd.read_csv('data.csv')
df.head()

# plot data

plt.plot(df['value'])

# save plot

plt.savefig('plot.png')

# show plot

plt.show()

# close plot

plt.close()

# save plot as pdf

plt.savefig('plot.pdf')
