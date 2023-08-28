# visualization for numerical data

# Numerical data is quantitative and can be discrete (e.g., number of students) or continuous
# (e.g., height of students). There are various visualizations available to depict numerical data effectively:
#
# Histograms: These represent the distribution of a single numerical variable by segmenting data into bins
# and displaying the number of observations in each bin.
#
# Box plots (or Whisker plots): These show the distribution of a numerical variable, capturing the median, quartiles,
# and potential outliers.
#
# Scatter plots: Useful for showing the relationship between two numerical variables.
#
# Line plots: Used to represent a series of data points in order, often displaying data over time.
#
# Density plots: Display the distribution of a numerical variable, similar to histograms but smooth.
#
# Violin plots: Combine aspects of box plots and density plots to show
# the distribution of data across different categories or levels.
#
# Pair plots: Display pairwise relationships in a dataset. By using pair plots, we can immediately see
# the distributions of single variables and relationships between two variables.
#
# Let's visualize a sample numerical dataset using some of these methods using the seaborn library.
# We'll use the tips dataset, focusing on the numerical columns "total_bill" and "tip".

# Load the 'tips' dataset
tips = sns.load_dataset('tips')

# 1. Histogram for 'total_bill'
plt.figure(figsize=(8, 6))
sns.histplot(tips['total_bill'], kde=True)
plt.title('Histogram of Total Bill')
plt.show()

# 2. Box plot for 'total_bill'
plt.figure(figsize=(8, 6))
sns.boxplot(x=tips['total_bill'])
plt.title('Box Plot of Total Bill')
plt.show()

# 3. Scatter plot of 'total_bill' vs 'tip'
plt.figure(figsize=(8, 6))
sns.scatterplot(x='total_bill', y='tip', data=tips)
plt.title('Scatter Plot of Total Bill vs Tip')
plt.show()

# 4. Line plot for 'total_bill' (assuming it's a time series for the sake of visualization)
plt.figure(figsize=(8, 6))
sns.lineplot(data=tips['total_bill'])
plt.title('Line Plot of Total Bill')
plt.show()

# 5. Density plot for 'total_bill'
plt.figure(figsize=(8, 6))
sns.kdeplot(tips['total_bill'], shade=True)
plt.title('Density Plot of Total Bill')
plt.show()

# 6. Violin plot for 'total_bill' based on day
plt.figure(figsize=(8, 6))
sns.violinplot(x='day', y='total_bill', data=tips)
plt.title('Violin Plot of Total Bill by Day')
plt.show()

# 7. Pair plot focusing on 'total_bill' and 'tip'
sns.pairplot(tips[['total_bill', 'tip']])
plt.show()

# It seems I encountered an issue while attempting to fetch the tips dataset from Seaborn's online repository.
# This is likely due to restricted internet access in the current environment.
#
# However, I can still guide you on how to create these visualizations using the tips dataset or any similar
# dataset you have locally.
#
# Here's a brief guideline:

# Histogram:

sns.histplot(data['numerical_column'], kde=True)
plt.title('Histogram of Numerical Column')
plt.show()

# Box Plot:

sns.boxplot(x=data['numerical_column'])
plt.title('Box Plot of Numerical Column')
plt.show()

# Scatter plot:

sns.scatterplot(x='numerical_column1', y='numerical_column2', data=data)
plt.title('Scatter Plot of Column1 vs Column2')
plt.show()

# Line plot:

sns.lineplot(data=data['numerical_column'])
plt.title('Line Plot of Numerical Column')
plt.show()

# Density plot:

sns.kdeplot(data['numerical_column'], shade=True)
plt.title('Density Plot of Numerical Column')
plt.show()

# Violin plot:

sns.violinplot(x='categorical_column', y='numerical_column', data=data)
plt.title('Violin Plot of Numerical Column by Category')
plt.show()

# Pair plot:

sns.pairplot(data[['numerical_column1', 'numerical_column2']])
plt.show()

# Replace data with your DataFrame name and adjust the column names accordingly.
#
# If you provide a sample of your data or a similar dataset,
# I can also generate these plots directly within this environment.
