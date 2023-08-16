# Create a streamlit app for data uploading and visualization

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    st.title("Data Uploading and Visualization App")
    st.write("This app is for uploading and visualizing data")
    st.write("Upload your data in the sidebar")
    st.write("The data will be displayed below")
    st.write("You can visualize the data in the sidebar")
    st.write("The visualization will be displayed below")
    st.write("The visualization will be saved as a png file")
    st.write("The visualization will be saved in the same directory as this app")
    st.write("The visualization will be saved with the name 'visualization.png'")

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

    # visualize data
    st.sidebar.title("Visualize Data")
    if uploaded_file is not None:
        if st.sidebar.checkbox("Visualize Geography Data"):
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
            plot_geography_data(df, x, y, title, xlabel, ylabel, figsize)

        if st.sidebar.checkbox("Visualize Categorical Data"):
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
            plot_categorical_data(df, x, y, title, xlabel, ylabel, figsize)

        if st.sidebar.checkbox("Visualize Numerical Data"):
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
            plot_numerical_data(df, x, y, title, xlabel, ylabel, figsize)

        if st.sidebar.checkbox("Visualize Time Series Data"):
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
            plot_time_series_data(df, x, y, title, xlabel, ylabel, figsize)

        if st.sidebar.checkbox("Visualize Correlation Data"):
            title = st.sidebar.text_input(label="Enter the title of the plot")
            figsize = st.sidebar.slider(
                label="Select the size of the plot",
                min_value=1,
                max_value=100,
                value=10,
            )
            plot_correlation_data(df, title, figsize)


def plot_geography_data(data, x, y, title, xlabel, ylabel, figsize=(10, 5)):
    plt.figure(figsize=figsize)
    sns.barplot(data=data, x=x, y=y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    save_visualization_as_png(plt)
    st.pyplot()


def plot_categorical_data(data, x, y, title, xlabel, ylabel, figsize=(10, 5)):
    plt.figure(figsize=figsize)
    sns.barplot(data=data, x=x, y=y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    save_visualization_as_png(plt)
    st.pyplot()


def plot_numerical_data(data, x, y, title, xlabel, ylabel, figsize=(10, 5)):
    plt.figure(figsize=figsize)
    sns.barplot(data=data, x=x, y=y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    save_visualization_as_png(plt)
    st.pyplot()


def plot_time_series_data(data, x, y, title, xlabel, ylabel, figsize=(10, 5)):
    plt.figure(figsize=figsize)
    sns.barplot(data=data, x=x, y=y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    save_visualization_as_png(plt)
    st.pyplot()


def plot_correlation_data(data, title, figsize=(10, 5)):
    plt.figure(figsize=figsize)
    sns.heatmap(data.corr(), annot=True)
    plt.title(title)
    plt.show()
    save_visualization_as_png(plt)
    st.pyplot()


def save_visualization_as_png(plt):
    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    return img


if __name__ == "__main__":
    main()
