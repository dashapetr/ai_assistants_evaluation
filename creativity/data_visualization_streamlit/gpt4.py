# Create a streamlit app for data uploading and visualization

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    st.title("Data Uploading and Visualization App")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write("### First 5 rows of the dataset")
        st.write(data.head())

        column_to_plot = st.selectbox("Select a column to visualize", data.columns)

        # Check data type of the column
        col_type = data[column_to_plot].dtype

        # If column is numeric, provide options for histogram or line plot
        if pd.api.types.is_numeric_dtype(col_type):
            plot_type = st.selectbox("Choose a type of plot", ["Histogram", "Line Plot"])

            if plot_type == "Histogram":
                bins = st.slider("Number of bins", 5, 100, 20)
                plt.figure(figsize=(10, 6))
                plt.hist(data[column_to_plot], bins=bins)
                plt.title(f"Histogram for {column_to_plot}")
                plt.xlabel(column_to_plot)
                plt.ylabel("Frequency")
                st.pyplot(plt)

            elif plot_type == "Line Plot":
                plt.figure(figsize=(10, 6))
                plt.plot(data[column_to_plot])
                plt.title(f"Line Plot for {column_to_plot}")
                plt.xlabel("Index")
                plt.ylabel(column_to_plot)
                st.pyplot(plt)

        # If column is categorical, provide option for bar plot
        elif pd.api.types.is_object_dtype(col_type):
            plt.figure(figsize=(10, 6))
            sns.countplot(data[column_to_plot])
            plt.title(f"Bar Plot for {column_to_plot}")
            plt.xlabel(column_to_plot)
            plt.ylabel("Count")
            plt.xticks(rotation=45)
            st.pyplot(plt)

        else:
            st.write(f"The data type for {column_to_plot} is {col_type}. No visualization available.")


if __name__ == "__main__":
    main()
