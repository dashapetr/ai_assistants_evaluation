import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


def main():
    st.title("Data Uploading and ML App")

    # upload data
    st.sidebar.title("Upload Data")
    uploaded_file = st.sidebar.file_uploader(
        label="Upload your CSV or Excel file here", type=["csv", "xlsx"]
    )
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
        except Exception as e:
            print(e)
            df = pd.read_excel(uploaded_file)
        st.write(df)

    # try different ML models
    st.sidebar.title("Try Different ML Models")
    if uploaded_file is not None:
        if st.sidebar.checkbox("Try Linear Regression"):
            x = st.sidebar.selectbox(
                label="Select the column for x axis", options=df.columns
            )
            y = st.sidebar.selectbox(
                label="Select the column for y axis", options=df.columns
            )
            title = st.sidebar.text_input(label="Enter the title of the plot")
            xlabel = st.sidebar.text_input(label="Enter the label for x axis")
            ylabel = st.sidebar.text_input(label="Enter the label for y axis")
            figsize = st.sidebar.slider(
                label="Select the size of the plot",
                min_value=1,
                max_value=100,
                value=10,
            )
            plot_linear_regression(df, x, y, title, xlabel, ylabel, figsize)


# fix the bug in the code above

def plot_linear_regression(df, x, y, title, xlabel, ylabel, figsize):
    # Split the data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(df[x].values.reshape(-1, 1), df[y])

    # Apply linear regression
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    y_pred = lr.predict(X_test)

    # Calculate metrics
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Create the plot
    plt.figure(figsize=(figsize, figsize))
    sns.scatterplot(df[x], df[y], label='Data Points')
    plt.plot(X_test, y_pred, color='red', label=f'Linear Regression\nMSE: {mse:.2f}, R2: {r2:.2f}')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    st.pyplot(plt)
    plt.close()


# Placeholder for the main function (for demonstration purposes only)
def main_placeholder():
    pass


# Assuming the main function would be called to initiate the Streamlit app
main_placeholder()
