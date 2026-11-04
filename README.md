# DemandAI – Sales Forecasting & Analytics

A machine learning-powered sales analytics application that explores historical retail sales, visualizes business trends, and generates next-day demand estimates using Random Forest Regression.

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Streamlit-Application-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/Scikit--learn-Machine%20Learning-F7931E?logo=scikitlearn&logoColor=white" alt="Scikit-learn" />
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white" alt="Pandas" />
</p>

## Overview

DemandAI turns historical store-level and product-level sales data into interactive visualizations and demand predictions.

The application combines exploratory data analysis, time-based feature engineering, and a trained Random Forest model to estimate the next day's sales for a selected store and product.

## Features

- **Sales Analytics** – Explore overall, store-wise, and product-wise sales.
- **Trend Visualization** – Analyse monthly sales patterns and performance.
- **Feature Engineering** – Generate calendar features, lag variables, and rolling averages.
- **Demand Prediction** – Estimate next-day sales using a trained Random Forest model.
- **Interactive Dashboard** – Explore results through a Streamlit interface.

## How It Works

```text
Historical Sales Data
         |
         v
Data Preparation & EDA
         |
         v
Feature Engineering
         |
         v
Random Forest Regression
         |
         v
Model Evaluation
         |
         v
Streamlit Dashboard
         |
         v
Next-Day Demand Estimate
```

## Model Performance

The Random Forest Regressor was evaluated using a time-based train/test split and a rolling one-step-ahead evaluation approach.

| Metric | Random Forest |
|:-------|--------------:|
| MAE    | 1.94 |
| RMSE   | 2.43 |

The model achieved a lower MAE than the 7-day seasonal baseline (2.49) on the test period.

**Note:** The evaluation uses previous actual sales observations when constructing lag features. Results therefore represent rolling one-step-ahead predictions, not independent multi-day forecasting.

## Tech Stack

| Category | Tools |
|:---------|:------|
| Language | Python |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib |
| Machine Learning | Scikit-learn |
| Web Application | Streamlit |
| Model Persistence | Joblib |
| Version Control | Git, GitHub, Git LFS |

## Getting Started

### Prerequisites

- Python 3.12
- Git
- Git LFS

### Installation

**1. Clone the repository**

```bash
git lfs install
git clone https://github.com/rajanalarakesh1/DemandAI.git
cd DemandAI
```

**2. Create a virtual environment**

Windows:

```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**3. Install dependencies**

```bash
python -m pip install -r requirements.txt
```

**4. Run the application**

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal (usually `http://localhost:8501`).

> The trained model is stored using Git LFS. Git LFS must be installed before cloning so the actual model file is downloaded rather than only its pointer.

## Repository Structure

```text
DemandAI/
├── app.py
├── demandai_sales_dataset.csv
├── demandai_model.pkl
├── requirements.txt
├── README.md
├── .gitignore
└── .gitattributes
```

## Notes & Limitations

- The project uses the historical dataset included in the repository; it is not connected to a live retail system.
- The current application estimates demand for one day ahead of the latest available observations.
- Multi-day forecasting and deployment are potential future improvements.

## Author

**Rakesh R**

[GitHub](https://github.com/rajanalarakesh1) · [LinkedIn](https://linkedin.com/in/rajunala-rakesh-2b1741334)
