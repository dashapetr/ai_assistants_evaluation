# Create a streamlit app for data uploading and trying different ML models

import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def main():
    st.title("Machine Learning Model Testing App")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write("### First 5 rows of the dataset")
        st.write(data.head())

        # Select target variable
        target_column = st.selectbox("Select the target column", data.columns)
        y = data[target_column]

        # Select input features
        feature_columns = st.multiselect("Select the feature columns", data.columns.difference([target_column]))
        X = data[feature_columns]

        # Split data into train and test sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Select a model to train
        model_choice = st.selectbox("Select a machine learning model",
                                    ["Linear Regression", "Decision Tree", "Random Forest"])

        if st.button("Train Model"):
            st.write(f"Training {model_choice}...")

            if model_choice == "Linear Regression":
                model = LinearRegression()
            elif model_choice == "Decision Tree":
                model = DecisionTreeRegressor()
            elif model_choice == "Random Forest":
                model = RandomForestRegressor()

            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

            mae = mean_absolute_error(y_test, y_pred)
            mse = mean_squared_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)

            st.write(f"Mean Absolute Error (MAE): {mae:.2f}")
            st.write(f"Mean Squared Error (MSE): {mse:.2f}")
            st.write(f"R^2 Score: {r2:.2f}")


if __name__ == "__main__":
    main()
