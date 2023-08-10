# create a class for data cleaning: input missing values and remove duplicates

class DataCleaning:
    def __init__(self, data):
        self.data = data

    def input_missing_values(self, missing_value):
        self.data.fillna(missing_value, inplace=True)

    def remove_duplicates(self):
        self.data.drop_duplicates(inplace=True)

    def get_data(self):
        return self.data
