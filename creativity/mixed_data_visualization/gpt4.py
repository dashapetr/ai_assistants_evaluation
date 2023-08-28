# visualization class for mixed data types

# Visualizing datasets with mixed data types (numerical, categorical, boolean, etc.) can be a bit challenging
# due to the inherent differences in these data types.
# A common approach is to utilize multiple visualization techniques and combine them in a coherent manner.
#
# Let's create a visualization class for mixed data types using Python's matplotlib and seaborn libraries.
# This class will:
#
# Automatically detect the data type of each column.
# Provide appropriate visualizations for each data type.
# Offer a combined view of the data.
# We'll consider three primary data types for this example:
#
# Numerical: Displayed using histograms or box plots.
# Categorical: Displayed using bar charts or count plots.
# Boolean: Displayed using pie charts.
# Here's a basic implementation of such a class:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class MixedDataVisualizer:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def _plot_numerical(self, col_name):
        sns.histplot(self.data[col_name], kde=True)
        plt.title(f'Histogram for {col_name}')
        plt.show()

    def _plot_categorical(self, col_name):
        sns.countplot(data=self.data, x=col_name)
        plt.title(f'Count plot for {col_name}')
        plt.show()

    def _plot_boolean(self, col_name):
        self.data[col_name].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
        plt.title(f'Pie chart for {col_name}')
        plt.ylabel('')  # Hide y-axis label for cleaner appearance
        plt.show()

    def plot(self):
        for col_name in self.data.columns:
            col_data = self.data[col_name]

            # Determine column type
            if np.issubdtype(col_data.dtype, np.number):
                self._plot_numerical(col_name)
            elif np.issubdtype(col_data.dtype, np.bool_):
                self._plot_boolean(col_name)
            else:  # Assume it's categorical
                self._plot_categorical(col_name)

# Sample data
data = pd.DataFrame({
    'Age': [25, 30, 35, 40, 45],
    'Gender': ['Male', 'Female', 'Male', 'Male', 'Female'],
    'Subscribed': [True, False, True, False, True]
})

# Use the class to visualize the data
visualizer = MixedDataVisualizer(data)
visualizer.plot()

# Here's the visualization for the mixed data types in the sample dataset:
#
# Age (Numerical): Displayed using a histogram that shows the distribution of ages.
# Gender (Categorical): Displayed using a count plot that shows the frequency of each gender.
# Subscribed (Boolean): Displayed using a pie chart that shows the proportion of True and False values.
# The MixedDataVisualizer class detects the data type of each column and then visualizes it accordingly.
# You can further extend this class to handle other data types or to customize the visualizations as needed.
