
import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(
    page_title="DemandAI",
    page_icon="📊",
    layout="wide"
)

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("demandai_sales_dataset.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df

# Load trained model
@st.cache_resource
def load_model():
    return joblib.load("demandai_model.pkl")


df = load_data()
model = load_model()

# Dashboard title
st.title("📊 DemandAI")
st.subheader("Intelligent Demand Forecasting & Prediction System")

st.write(
    "Analyze historical sales, explore business trends, "
    "and estimate next-day product demand using machine learning."
)

# Key metrics
total_sales = df["sales"].sum()
total_stores = df["store"].nunique()
total_items = df["item"].nunique()

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"{total_sales:,.0f}")
col2.metric("Total Stores", total_stores)
col3.metric("Total Products", total_items)

st.divider()

# Store performance
st.header("Store Performance")

store_sales = df.groupby("store")["sales"].sum().sort_index()
st.bar_chart(store_sales)

# Product performance
st.header("Product Performance")

item_sales = df.groupby("item")["sales"].sum().sort_index()
st.bar_chart(item_sales)

# Monthly sales trend
st.header("Monthly Sales Trend")

monthly_sales = (
    df.set_index("date")["sales"]
    .resample("ME")
    .sum()
)

st.line_chart(monthly_sales)

st.divider()

# Machine learning model information
st.header("Machine Learning Model")

st.write("Model: Random Forest Regressor")
st.write("Mean Absolute Error (MAE): 1.94")
st.write("Root Mean Squared Error (RMSE): 2.43")

st.divider()

# Interactive demand prediction
st.header("🔮 Next-Day Demand Prediction")

st.write(
    "Select a store and product to estimate its demand "
    "for the day after the latest available sales date."
)

store_choice = st.selectbox(
    "Select Store",
    sorted(df["store"].unique())
)

item_choice = st.selectbox(
    "Select Product",
    sorted(df["item"].unique())
)

history = df[
    (df["store"] == store_choice) &
    (df["item"] == item_choice)
].sort_values("date")

if len(history) >= 7:

    latest_date = history["date"].max()
    next_date = latest_date + pd.Timedelta(days=1)

    last_7_sales = history["sales"].tail(7)

    lag_1 = last_7_sales.iloc[-1]
    lag_7 = last_7_sales.iloc[0]
    rolling_mean_7 = last_7_sales.mean()

    input_data = pd.DataFrame([{
        "store": store_choice,
        "item": item_choice,
        "year": next_date.year,
        "month": next_date.month,
        "day": next_date.day,
        "day_of_week": next_date.dayofweek,
        "lag_1": lag_1,
        "lag_7": lag_7,
        "rolling_mean_7": rolling_mean_7
    }])

    if st.button("Predict Next-Day Demand"):

        prediction = model.predict(input_data)[0]

        st.success(
            f"Predicted demand: {prediction:.2f} units"
        )

        st.caption(
            f"Prediction date: {next_date.strftime('%d %B %Y')}"
        )

        st.info(
            "This is a one-day-ahead estimate based on the "
            "latest seven available sales observations."
        )

else:
    st.warning("Not enough historical data for prediction.")

st.divider()

st.caption("DemandAI | Sales Analysis and Machine Learning Project")
