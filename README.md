# DemandAI – Intelligent Demand Forecasting & Prediction System

## Project Overview

DemandAI is an end-to-end Data Analytics and Machine Learning project designed to analyze historical sales data, identify business trends, and estimate next-day product demand.

The project combines Python-based data analysis, machine learning, and an interactive Streamlit dashboard.

## Objectives

- Analyze historical sales data.
- Identify sales trends across stores and products.
- Understand monthly sales performance.
- Build a machine learning model for demand estimation.
- Present insights through an interactive dashboard.

## Key Features

- Exploratory Data Analysis (EDA)
- Data cleaning and preprocessing
- Date-based feature engineering
- Lag features and rolling averages
- Store-wise sales analysis
- Product-wise sales analysis
- Monthly sales visualization
- Random Forest Regression
- Model evaluation using MAE and RMSE
- Interactive next-day demand prediction

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit
- Joblib
- Jupyter Notebook

## Machine Learning Model

**Algorithm:** Random Forest Regressor

**Features used:**
- Store
- Product
- Year
- Month
- Day
- Day of week
- Previous day's sales
- Sales from seven observations earlier
- Seven-observation rolling average

**Model Evaluation:**

| Metric | Result |
|---|---:|
| MAE | 1.94 |
| RMSE | 2.43 |

## Business Insights

The analysis identified:

- Store 5 recorded the highest total sales.
- Product 10 recorded the highest total sales.
- March 2025 had the highest monthly sales.
- Historical weekly sales patterns were important for model predictions.

## Dashboard

The Streamlit dashboard provides:
- Overall sales metrics
- Store performance charts
- Product performance charts
- Monthly sales trends
- Interactive next-day demand estimation

## Project Structure

```text
DemandAI/
├── app.py
├── DemandAI.ipynb
├── demandai_sales_dataset.csv
├── requirements.txt
├── .gitignore
└── README.md
```

The trained model file is managed separately because it exceeds GitHub's standard file size limit.

## How to Run

1. Clone this repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

2. Navigate to the project folder:

```bash
cd DemandAI
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Place `demandai_model.pkl` in the project folder.

5. Start the application:

```bash
streamlit run app.py
```

## Limitations

- Predictions depend on historical sales patterns.
- The current model estimates demand one day ahead.
- Model evaluation uses a rolling one-step-ahead approach with previous actual sales observations.

## Future Improvements

- Compare different machine learning algorithms.
- Improve multi-day forecasting.
- Add interactive filters and visualizations.
- Deploy the dashboard online.

## Author

**Rakesh R**

GitHub:(https://github.com/rajanalarakesh1)

LinkedIn: www.linkedin.com/in/rajunala-rakesh-2b1741334

---

*DemandAI – Turning Historical Sales Data into Actionable Insights.*