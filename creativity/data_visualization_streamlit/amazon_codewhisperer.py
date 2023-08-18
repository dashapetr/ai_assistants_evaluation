# Create a streamlit app for data uploading and visualization


import streamlit as st
import pandas as pd
import numpy as np

st.title("Data Upload")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
    st.write(df.shape)
    st.write(df.columns)
    st.write(df.dtypes)
    st.write(df.head())


    st.title("Visualization")
    st.write(df.describe())
    st.write(df.corr())
    st.write(df.info())
    st.write(df.isnull().sum())

    st.line_chart(df)
    st.bar_chart(df)
    st.area_chart(df)
    st.scatter_chart(df)
    st.map(df)
