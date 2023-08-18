# visualization class for mixed data types


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Visualization:
    def __init__(self, df):
        self.df = df
        self.df_types = self.df.dtypes
        self.df_types = self.df_types.reset_index()
        self.df_types.columns = ['column', 'type']
        self.df_types = self.df_types.set_index('column')
        self.df_types = self.df_types.drop(['index'], axis=1)
        self.df_types = self.df_types.replace('object', 'str')
        self.df_types = self.df_types.replace('int64', 'int')

    def plot_bar(self, column):
        if self.df_types.loc[column, 'type'] == 'int':
            self.df[column].plot.hist()
        elif self.df_types.loc[column, 'type'] == 'str':
            self.df[column].value_counts().plot.bar()
        else:
            print('invalid data type')
        plt.show()

    def plot_scatter(self, column1, column2):
        if self.df_types.loc[column1, 'type'] == 'int' and self.df_types.loc[column2, 'type'] == 'int':
            self.df.plot.scatter(x=column1, y=column2)
        elif self.df_types.loc[column1, 'type'] == 'str' and self.df_types.loc[column2, 'type'] == 'str':
            self.df[column1].value_counts().plot.bar()
        else:
            print('invalid data type')
        plt.show()

    def plot_box(self, column):
        if self.df_types.loc[column, 'type'] == 'int':
            self.df[column].plot.box()
        elif self.df_types.loc[column, 'type'] == 'str':
            self.df[column].value_counts().plot.bar()
            self.df[column].value_counts().plot.box()
        else:
            print('invalid data type')

        plt.show()

    def plot_pie(self, column):
        if self.df_types.loc[column, 'type'] == 'int':
            self.df[column].value_counts().plot.pie()
            plt.show()

        elif self.df_types.loc[column, 'type'] == 'str':
            self.df[column].value_counts().plot.pie()
            plt.show()

        else:
            print('invalid data type')

    def plot_heatmap(self, column1, column2):
        if self.df_types.loc[column1, 'type'] == 'int' and self.df_types.loc[column2, 'type'] == 'int':
            self.df.corr().style.background_gradient(cmap='coolwarm')
        elif self.df_types.loc[column1, 'type'] == 'str' and self.df_types.loc[column2, 'type'] == 'str':
            self.df[column1].value_counts().plot.bar()
            self.df[column2].value_counts().plot.bar()
            self.df.corr().style.background_gradient(cmap='coolwarm')
        else:
            print('invalid data type')
        plt.show()

    def plot_line(self, column1, column2):
        if self.df_types.loc[column1, 'type'] == 'int' and self.df_types.loc[column2, 'type'] == 'int':
            self.df.plot.line(x=column1, y=column2)
        elif self.df_types.loc[column1, 'type'] == 'str' and self.df_types.loc[column2, 'type'] == 'str':
            self.df[column1].value_counts().plot.bar()
            self.df[column2].value_counts().plot.bar()
            self.df.plot.line(x=column1, y=column2)
        else:
            print('invalid data type')
        plt.show()
