# Create a streamlit app for data uploading and trying different ML models

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score


def main():
    st.title("Data Uploading and ML App")
    st.write("This app is for uploading and trying different ML models")
    st.write("Upload your data in the sidebar")
    st.write("The data will be displayed below")
    st.write("You can try different ML models in the sidebar")
    st.write("The results of the ML models will be displayed below")
    st.write("The results of the ML models will be saved as a png file")
    st.write("The results of the ML models will be saved in the same directory as this app")
    st.write("The results of the ML models will be saved with the name 'results.png'")

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

        if st.sidebar.checkbox("Try SVM"):
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
            plot_svm(df, x, y, title, xlabel, ylabel, figsize)

        if st.sidebar.checkbox("Try Decision Tree"):
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
            plot_decision_tree(df, x, y, title, xlabel, ylabel, figsize)

        if st.sidebar.checkbox("Try Random Forest"):
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
            plot_random_forest(df, x, y, title, xlabel, ylabel, figsize)

        if st.sidebar.checkbox("Try KNN"):
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
            plot_knn(df, x, y, title, xlabel, ylabel, figsize)

        if st.sidebar.checkbox("Try Logistic Regression"):
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
            plot_logistic_regression(df, x, y, title, xlabel, ylabel, figsize)

        if st.sidebar.checkbox("Try Naive Bayes"):
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
            plot_naive_bayes(df, x, y, title, xlabel, ylabel, figsize)

        if st.sidebar.checkbox("Try XGBoost"):
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
            plot_xgboost(df, x, y, title, xlabel, ylabel, figsize)

        if st.sidebar.checkbox("Try LightGBM"):
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
            plot_lightgbm(df, x, y, title, xlabel, ylabel, figsize)


    elif choice == "EDA":
        st.subheader("Exploratory Data Analysis")
        st.write("This section is under development")
        st.write("Please select another option from the sidebar")

    elif choice == "Data Cleaning":
        st.subheader("Data Cleaning")
        st.write("This section is under development")
        st.write("Please select another option from the sidebar")

    elif choice == "Feature Engineering":
        st.subheader("Feature Engineering")
        st.write("This section is under development")
        st.write("Please select another option from the sidebar")


if __name__ == "__main__":
    main()
