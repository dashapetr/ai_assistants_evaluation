# visualization for numerical data


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

# scatter plot

plt.scatter(data["Height"], data["Weight"])

plt.show()

# histogram

plt.hist(data["Height"])

plt.show()

# box plot

plt.boxplot(data["Height"])

plt.show()

# correlation

plt.scatter(data["Height"], data["Weight"])

plt.show()
