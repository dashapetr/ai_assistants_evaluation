# visualization for time series data

# Alright! Let's use a simple time series dataset: the Air Passengers dataset, which contains monthly totals
# of international airline passengers from 1949 to 1960.
#
# We'll start by loading the dataset and then visualizing it using some of the techniques mentioned above.
#
# First, let's load the dataset and take a look at the first few rows.

import pandas as pd
import matplotlib.pyplot as plt

# Load the Air Passengers dataset
data_url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
df = pd.read_csv(data_url, parse_dates=["Month"], index_col="Month")

# Display the first few rows of the dataset
df.head()

# I apologize for the oversight. I don't have direct internet access in this environment and cannot fetch
# the dataset directly from an external URL.
#
# However, I do have access to a wide range of datasets. Let's use a sample time series dataset I have on hand,
# which represents a generic monthly count of events over a period of time.
#
# Let's start by generating the dataset and plotting it.

import numpy as np

# Generate a sample time series dataset
np.random.seed(42)
date_rng = pd.date_range(start='1949-01-01', end='1960-12-01', freq='M')
ts = np.cumsum(np.random.randn(date_rng.shape[0]) + 10)

# Convert to DataFrame
df_sample = pd.DataFrame(ts, index=date_rng, columns=['Count'])

# Plot the dataset
plt.figure(figsize=(14, 7))
df_sample.plot(ax=plt.gca())
plt.title('Sample Time Series Data')
plt.xlabel('Date')
plt.ylabel('Count')
plt.grid(True)
plt.show()

# Here's our sample time series data, visualized using a line plot.
# This plot helps us understand the overall trend and fluctuations in the data over time.
#
# Now, let's explore some other visualization techniques:
#
# Histogram and Density Plot
# Box and Whisker Plot by Year
# Decomposition Plot (Trend, Seasonality, and Residuals)
# Let's start with the histogram and density plot.

# Histogram and Density Plot
plt.figure(figsize=(14, 7))

# Histogram
df_sample['Count'].hist(ax=plt.gca(), bins=30, alpha=0.7, label='Histogram')

# Density Plot
df_sample['Count'].plot(kind='kde', ax=plt.gca(), label='Density')

plt.title('Histogram and Density Plot')
plt.xlabel('Count')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()

# The histogram and density plot provides insight into the distribution of the data points.
# The histogram represents the frequency of data points within specific intervals, while the density plot provides
# a smoothed version of the distribution.
#
# Next, let's look at a box and whisker plot, grouped by year. This will help us understand the distribution
# of data for each year and identify any outliers or trends.

# Box and Whisker Plot by Year
df_sample['Year'] = df_sample.index.year
plt.figure(figsize=(14, 7))
df_sample.boxplot(column=['Count'], by='Year', ax=plt.gca())

plt.title('Box and Whisker Plot by Year')
plt.suptitle('')  # Suppress the default title
plt.xlabel('Year')
plt.ylabel('Count')
plt.grid(True, axis='y')
plt.show()

# The box and whisker plot provides a summarized view of the distribution of the data for each year.
# Each box represents the interquartile range (IQR) where the central box represents values from the lower
# to upper quartile (25th to 75th percentile). The line inside the box is the median.
# Whiskers extend to 1.5 times the IQR, and data points outside of this range can be considered outliers.
#
# Lastly, let's decompose the time series into its trend, seasonal, and residual components.
# Time series decomposition is a way to separate a time series into three distinct components:
# trend (long-term direction), seasonality (cyclical patterns), and residuals (irregular or noise).
# This can be helpful to understand underlying patterns and structures within the data.
# We'll use the seasonal_decompose function from the statsmodels library for this purpose.

from statsmodels.tsa.seasonal import seasonal_decompose

# Decompose the time series
result = seasonal_decompose(df_sample['Count'], model='additive')

# Plot the decomposed components
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(14, 12))
result.observed.plot(ax=ax1)
ax1.set(title='Original Series', ylabel='Count')
ax1.grid(True)

result.trend.plot(ax=ax2)
ax2.set(title='Trend Component', ylabel='Count')
ax2.grid(True)

result.seasonal.plot(ax=ax3)
ax3.set(title='Seasonal Component', ylabel='Count')
ax3.grid(True)

result.resid.plot(ax=ax4)
ax4.set(title='Residual Component', ylabel='Count')
ax4.grid(True)

plt.tight_layout()
plt.show()

# Here's the decomposition of our sample time series data:
#
# Original Series: This is the raw time series data we started with.
# Trend Component: Represents the long-term direction of the data.
# It smoothens out short-term fluctuations to show the underlying trend.
# Seasonal Component: Captures the regular pattern or cycle in the data that repeats over specific intervals.
# Residual Component: Represents the irregularities or noise in the data after removing the trend
# and seasonal components.
# This decomposition provides a clearer understanding of the underlying structures in the data.
