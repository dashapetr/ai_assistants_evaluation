# visualization for categorical data

import matplotlib.pyplot as plt
import seaborn as sns


def plot_categorical_data(data, x, y, title, xlabel, ylabel, figsize=(10, 5)):
    plt.figure(figsize=figsize)
    sns.barplot(data=data, x=x, y=y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

