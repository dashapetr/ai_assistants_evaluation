# visualization class for mixed data types

import matplotlib.pyplot as plt
import seaborn as sns


class MixedDataVisualization:
    def __init__(self, data, x, y, title, xlabel, ylabel, figsize=(10, 5)):
        self.data = data
        self.x = x
        self.y = y
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.figsize = figsize

    def plot(self):
        plt.figure(figsize=self.figsize)
        sns.scatterplot(data=self.data, x=self.x, y=self.y)
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.show()
