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


# code after the bug correction (the plot_linear_regression function was missing, however, it
# wasn't fixed by Fix Bug Brush but was suggested by GitHub Copilot):


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


def plot_linear_regression(df, x, y, title, xlabel, ylabel, figsize):
    # create a linear regression object
    lr = LinearRegression()

    # split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        df[x].values.reshape(-1, 1), df[y].values.reshape(-1, 1), test_size=0.2
    )

    # train the model
    lr.fit(X_train, y_train)

    # make predictions on the test data
    y_pred = lr.predict(X_test)

    # plot the predictions as a scatter plot
    plt.figure(figsize=(figsize, figsize))
    plt.scatter(X_test, y_test, color="black")
    plt.plot(X_test, y_pred, color="blue", linewidth=3)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    st.pyplot()
