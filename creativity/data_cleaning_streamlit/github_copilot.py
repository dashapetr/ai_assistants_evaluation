# Create a streamlit app for data uploading and cleaning

import streamlit as st
import pandas as pd
import numpy as np


def main():
    st.title("Data Uploading and Cleaning App")
    st.write("This app is for uploading and cleaning data")
    st.write("Upload your data in the sidebar")
    st.write("The data will be displayed below")
    st.write("You can clean the data in the sidebar")
    st.write("The cleaned data will be displayed below")
    st.write("The cleaned data will be saved as a csv file")
    st.write("The cleaned data will be saved in the same directory as this app")
    st.write("The cleaned data will be saved with the name 'cleaned_data.csv'")

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

    # clean data
    st.sidebar.title("Clean Data")
    if uploaded_file is not None:
        if st.sidebar.checkbox("Drop NA"):
            df = df.dropna()
        if st.sidebar.checkbox("Drop Duplicates"):
            df = df.drop_duplicates()
        if st.sidebar.checkbox("Fill NA with 0"):
            df = df.fillna(0)
        if st.sidebar.checkbox("Fill NA with Mean"):
            df = df.fillna(df.mean())
        if st.sidebar.checkbox("Fill NA with Median"):
            df = df.fillna(df.median())
        if st.sidebar.checkbox("Fill NA with Mode"):
            df = df.fillna(df.mode())
        if st.sidebar.checkbox("Fill NA with Forward Fill"):
            df = df.fillna(method="ffill")
        if st.sidebar.checkbox("Fill NA with Backward Fill"):
            df = df.fillna(method="bfill")
        if st.sidebar.checkbox("Drop Columns"):
            columns = st.sidebar.multiselect(
                label="Select the columns you want to drop",
                options=df.columns,
            )
            df = df.drop(columns=columns)
        if st.sidebar.checkbox("Drop Rows"):
            rows = st.sidebar.multiselect(
                label="Select the rows you want to drop",
                options=df.index,
            )
            df = df.drop(index=rows)
        if st.sidebar.checkbox("Replace Values"):
            columns = st.sidebar.multiselect(
                label="Select the columns you want to replace values in",
                options=df.columns,
            )
            old_value = st.sidebar.text_input("Enter the value you want to replace")
            new_value = st.sidebar.text_input("Enter the new value")
            df = df.replace(to_replace=old_value, value=new_value)
        if st.sidebar.checkbox("Rename Columns"):
            columns = st.sidebar.multiselect(
                label="Select the columns you want to rename",
                options=df.columns,
            )
            new_names = st.sidebar.text_input(
                "Enter the new names for the selected columns separated by commas"
            )
            new_names = new_names.split(",")
            df = df.rename(columns=dict(zip(columns, new_names)))
        if st.sidebar.checkbox("Rename Rows"):
            rows = st.sidebar.multiselect(
                label="Select the rows you want to rename",
                options=df.index,
            )
            new_names = st.sidebar.text_input(
                "Enter the new names for the selected rows separated by commas"
            )
            new_names = new_names.split(",")
            df = df.rename(index=dict(zip(rows, new_names)))
        if st.sidebar.checkbox("Convert to Numeric"):
            columns = st.sidebar.multiselect(
                label="Select the columns you want to convert to numeric",
                options=df.columns,
            )
            df[columns] = df[columns].apply(pd.to_numeric)
        if st.sidebar.checkbox("Convert to Datetime"):
            columns = st.sidebar.multiselect(
                label="Select the columns you want to convert to datetime",
                options=df.columns,
            )
            df[columns] = df[columns].apply(pd.to_datetime)
        if st.sidebar.checkbox("Convert to Categorical"):
            columns = st.sidebar.multiselect(
                label="Select the columns you want to convert to categorical",
                options=df.columns,
            )
            df[columns] = df[columns].apply(pd.to_categorical)
        if st.sidebar.checkbox("Convert to String"):
            columns = st.sidebar.multiselect(
                label="Select the columns you want to convert to string",
                options=df.columns,
            )
            df[columns] = df[columns].apply(pd.to_string)
        if st.sidebar.checkbox("Convert to List"):
            columns = st.sidebar.multiselect(
                label="Select the columns you want to convert to list",
                options=df.columns,
            )
            df[columns] = df[columns].apply(pd.to_list)
        if st.sidebar.checkbox("Convert to Array"):
            columns = st.sidebar.multiselect(
                label="Select the columns you want to convert to array",
                options=df.columns,
            )
            df[columns] = df[columns].apply(pd.to_array)
        if st.sidebar.checkbox("Convert to Sparse"):
            columns = st.sidebar.multiselect(
                label="Select the columns you want to convert to sparse",
                options=df.columns,
            )
            df[columns] = df[columns].apply(pd.to_sparse)

    # display cleaned data
    if uploaded_file is not None:
        st.write(df)
        df.to_csv("cleaned_data.csv", index=False)


if __name__ == "__main__":
    main()

