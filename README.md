# 🏠 House Price Prediction using Machine Learning

A complete end-to-end Machine Learning project that predicts house prices based on property features. This project includes data preprocessing, model training, evaluation, a Scikit-learn pipeline, and a Streamlit web application for predictions.

---

## 📌 Project Overview

This project predicts the selling price of a house using property information such as:

- Bedrooms
- Bathrooms
- Living Area
- Lot Area
- Floors
- Waterfront
- View Rating
- Condition
- Above Ground Area
- Basement Area
- Year Built
- Year Renovated
- City

The model is trained using Linear Regression and deployed through a Streamlit web application.

---

## 🚀 Features

- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Linear Regression Model
- Scikit-learn Pipeline
- Model Serialization using Joblib
- Streamlit Web Application
- Input Validation
- House Price Prediction

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Streamlit
- Git
- GitHub

---

## 📂 Project Structure

```
house-price-prediction/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── Housing.csv
│
├── models/
│   └── house_price_pipeline.pkl
│
├── notebooks/
│   └── exploration.ipynb
│
├── src/
│   ├── __init__.py
│   ├── constants.py
│   ├── predict.py
│   ├── train.py
│   └── utils.py
```

---

## 📊 Dataset

The dataset contains information about residential properties, including:

- Property dimensions
- Number of rooms
- Construction details
- Location
- Selling price

Target Variable:

```
price
```

---

## 🤖 Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Engineering
5. Train-Test Split
6. Model Training
7. Model Evaluation
8. Pipeline Creation
9. Model Saving
10. Streamlit Deployment

---

## 📈 Model Performance

| Metric | Value |
|--------|-------:|
| MAE | 146,232 |
| RMSE | 238,736 |
| R² Score | 0.617 |

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/eMohan07/house-price-prediction.git
```

Move into the project

```bash
cd house-price-prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---


## 👨‍💻 Author

**Mohan E**

GitHub:
https://github.com/eMohan07

LinkedIn:
https://www.linkedin.com/in/emohan/

---

## ⭐ If you like this project

Please consider giving the repository a ⭐.