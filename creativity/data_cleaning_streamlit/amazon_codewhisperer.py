# Create a streamlit app for data uploading and cleaning


import streamlit as st
import pandas as pd
import numpy as np

st.title('Data Cleaning App')

uploaded_file = st.file_uploader('Upload a file', type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
    st.write(df.shape)
    st.write(df.columns)
    st.write(df.dtypes)
    st.write(df.head())
    st.write(df.tail())
    st.write(df.describe())
    st.write(df.info())
    st.write(df.isnull().sum())
    st.write(df.isnull().sum().sum())

    # Cleaning the data
    # Drop the columns that have more than 50% missing values
    df = df.dropna(axis=1, thresh=int(df.shape[0] * 0.5))
    st.write(df.isnull().sum())
    st.write(df.isnull().sum().sum())
    st.write(df.shape)

    # Drop the rows that have more than 50% missing values
    df = df.dropna(axis=0, thresh=int(df.shape[0] * 0.5))
    st.write(df.isnull().sum())
    st.write(df.isnull().sum().sum())
    st.write(df.shape)

    # Convert the data type of the columns
    df['price'] = df['price'].astype('float64')
    df['rating'] = df['rating'].astype('float64')
    df['review_count'] = df['review_count'].astype('float64')
    df['shipping'] = df['shipping'].astype('float64')
    df['category'] = df['category'].astype('category')
    df['brand'] = df['brand'].astype('category')
    df['title'] = df['title'].astype('category')
    df['description'] = df['description'].astype('category')
    df['image'] = df['image'].astype('category')
    df['url'] = df['url'].astype('category')
    df['review_body'] = df['review_body'].astype('category')

    # Create a new column called 'price_per_unit'
    df['price_per_unit'] = df['price'] / df['quantity']
    st.write(df.head())
