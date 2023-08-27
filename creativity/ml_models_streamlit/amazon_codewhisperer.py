# Create a streamlit app for data uploading and trying different ML models


import streamlit as st
import pandas as pd
import numpy as np

st.title('Data Upload')

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
    st.write(df.shape)
    st.write(df.columns)
    st.write(df.columns)

    st.write('Choose the model')
    model = st.selectbox('Model', ['Linear Regression', 'Random Forest', 'XGBoost'])
    if model == 'Linear Regression':
        st.write('Linear Regression')

        st.write('Choose the features')
        features = st.multiselect('Features', df.columns)
        st.write(features)

        X = df[features]
        y = df['price']

        from sklearn.model_selection import train_test_split

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        from sklearn.linear_model import LinearRegression

        lr = LinearRegression()
        lr.fit(X_train, y_train)
        lr_pred = lr.predict(X_test)
        st.write('R2 score:', lr.score(X_test, y_test))
        st.write('Mean absolute error:', np.mean(np.absolute(lr_pred - y_test)))
        st.write('Mean squared error:', np.mean((lr_pred - y_test) ** 2))

        st.write('Intercept:', lr.intercept_)
        st.write('Coefficient:', lr.coef_)

        st.write('Predictions:')
        st.write(lr_pred)

        st.write('Actual:')
        st.write(y_test)

    elif model == 'Random Forest':
        st.write('Random Forest')

        st.write('Choose the features')
        features = st.multiselect('Features', df.columns)
        st.write(features)

        X = df[features]
        y = df['price']

        from sklearn.model_selection import train_test_split

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        from sklearn.ensemble import RandomForestRegressor

        rf = RandomForestRegressor()
        rf.fit(X_train, y_train)
        rf_pred = rf.predict(X_test)
        st.write('R2 score:', rf.score(X_test, y_test))
        st.write('Mean absolute error:', np.mean(np.absolute(rf_pred - y_test)))
        st.write('Mean squared error:', np.mean((rf_pred - y_test) ** 2))

        st.write('Predictions:')
        st.write(rf_pred)

        st.write('Actual:')
        st.write(y_test)

    elif model == 'XGBoost':
        st.write('XGBoost')

        st.write('Choose the features')
        features = st.multiselect('Features', df.columns)
        st.write(features)

        X = df[features]
        y = df['price']

        from sklearn.model_selection import train_test_split

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        from xgboost import XGBRegressor

        xgb = XGBRegressor()
        xgb.fit(X_train, y_train)
        xgb_pred = xgb.predict(X_test)
        st.write('R2 score:', xgb.score(X_test, y_test))
        st.write('Mean absolute error:', np.mean(np.absolute(xgb_pred - y_test)))
        st.write('Mean squared error:', np.mean((xgb_pred - y_test) ** 2))

        st.write('Predictions:')
        st.write(xgb_pred)

        st.write('Actual:')
        st.write(y_test)
