# create a class for data cleaning: input missing values and remove duplicates

class DataCleaner:

    def __init__(self, data):
        self.data = data

    def remove_duplicates(self):
        self.data = list(dict.fromkeys(self.data))
        return self.data

    def fill_missing(self, fill_value=None):
        if fill_value is None:
            fill_value = 'N/A'  # Default value if none is provided
        self.data = [x if x is not None else fill_value for x in self.data]
        return self.data
