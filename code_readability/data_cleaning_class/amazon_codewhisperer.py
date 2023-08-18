# create a class for data cleaning: input missing values and remove duplicates


import pandas as pd
import numpy as np
import os


class Data_Cleaning:
    def __init__(self, data):
        self.data = data

    def missing_values(self):
        # check for missing values
        print(self.data.isnull().sum())

        # replace missing values with mean
        self.data.fillna(self.data.mean(), inplace=True)

        # check for missing values again
        print(self.data.isnull().sum())

    def remove_duplicates(self):
        # remove duplicates
        self.data.drop_duplicates(inplace=True)

        # check for duplicates
        print(self.data.duplicated().sum())

    def save_data(self):
        # save data
        self.data.to_csv(os.path.join(os.getcwd(), 'data', 'cleaned_data.csv'), index=False)
        print('Data saved')
        return self.data

    def load_data(self):
        # load data
        self.data = pd.read_csv(os.path.join(os.getcwd(), 'data', 'cleaned_data.csv'))
        print('Data loaded')
