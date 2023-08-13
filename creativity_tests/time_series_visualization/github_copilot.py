# visualization for time series data

import matplotlib.pyplot as plt
import seaborn as sns


def plot_time_series_data(data, x, y, title, xlabel, ylabel, figsize=(10, 5)):
    plt.figure(figsize=figsize)
    sns.lineplot(data=data, x=x, y=y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
