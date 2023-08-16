# visualization for numerical data

import matplotlib.pyplot as plt
import seaborn as sns


def plot_numerical_data(data, x, y, title, xlabel, ylabel, figsize=(10, 5)):
    plt.figure(figsize=figsize)
    sns.lineplot(data=data, x=x, y=y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
