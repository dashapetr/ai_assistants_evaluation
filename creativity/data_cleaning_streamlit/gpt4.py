# Create a streamlit app for data uploading and cleaning

import streamlit as st
import pandas as pd


def main():
    st.title("Data Uploading and Cleaning App")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write("### First 5 rows of the dataset")
        st.write(data.head())

        # Handling missing values
        if data.isnull().sum().sum() > 0:
            st.write("### Missing Values")
            st.write(data.isnull().sum())

            option = st.selectbox("How to handle missing values?",
                                  ["Remove", "Fill with Mean", "Fill with Median", "Fill with Mode"])
            if option == "Remove":
                data = data.dropna()
                st.write("### Missing values removed!")
            elif option == "Fill with Mean":
                data = data.fillna(data.mean())
                st.write("### Missing values filled with mean!")
            elif option == "Fill with Median":
                data = data.fillna(data.median())
                st.write("### Missing values filled with median!")
            elif option == "Fill with Mode":
                for column in data.columns:
                    data[column].fillna(data[column].mode()[0], inplace=True)
                st.write("### Missing values filled with mode!")

        # Convert columns to appropriate data types
        st.write("### Convert Data Types")
        columns = data.columns.tolist()
        column_types = st.multiselect("Which columns to convert to 'category' data type?", columns)
        for col in column_types:
            data[col] = data[col].astype('category')
        if column_types:
            st.write(f"Columns {column_types} converted to 'category' data type!")


if __name__ == "__main__":
    main()
