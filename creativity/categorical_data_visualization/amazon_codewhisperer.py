# visualization for categorical data


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv('data.csv')

data.plot(kind='bar')

plt.show()

data.plot(kind='hist')

plt.show()

data.plot(kind='box')

plt.show()
