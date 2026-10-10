# ✈️ Flight Delay Prediction and Analytics System

## 📌 Project Overview

The Flight Delay Prediction and Analytics System is a machine learning-based web application that predicts flight delays and analyzes the factors contributing to them. It uses a Random Forest Classifier and a Flask-based web interface to provide flight delay predictions and analytical insights.

## 🎯 Objectives

- Predict flight delays using machine learning.
- Analyze factors contributing to flight delays.
- Identify patterns in flight delay data.
- Provide an interactive web application for flight delay prediction.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Machine Learning Algorithm:** Random Forest Classifier
- **Web Framework:** Flask
- **Data Processing:** Pandas, NumPy
- **Machine Learning Library:** Scikit-learn
- **Frontend:** HTML, CSS
- **Model Serialization:** Pickle
- **Environment Management:** Anaconda

## ✨ Features

- Flight delay prediction using a trained machine learning model.
- Analysis of flight delay patterns.
- Identification of different delay categories, including Carrier, NAS, and Late Aircraft.
- User-friendly web interface.
- User registration and login functionality.
- Data-driven insights into flight delays.

## 📊 Dataset Information

Due to GitHub's file size limit (100 MB per file), the large dataset file (`DelayedFlights.csv`, ~234 MB) is excluded from this repository via `.gitignore`. 

- **Dataset Name:** Airlines Delay Causes / Flight Delays
- **Source:** Originally sourced from the **U.S. Bureau of Transportation Statistics (BTS)** and commonly hosted on platforms like [Kaggle (e.g., Airlines Delay Dataset)](https://www.kaggle.com/datasets/giovamata/airlinedelaycauses).
- **Usage:** To run data analysis or retrain the model locally, download `DelayedFlights.csv` from Kaggle and place it in the root directory of your project folder.

## 📊 Input Features

The system uses flight-related features such as:

- Month
- Day
- Departure time
- Flight distance
- Airline carrier
- Origin airport
- Destination airport
- Weather-related information, where applicable

## 🧠 Machine Learning Algorithm

The project uses a **Random Forest Classifier**, an ensemble machine learning algorithm that combines multiple decision trees to generate classification predictions.

The model is trained using flight-related data and saved as a pickle file. The trained model is then loaded into the Flask application to generate predictions based on user inputs.

## 📁 Project Structure

```text
Airlines-delay-prediction-machine-learning/
│
├── FlightDelayPrediction/
│   ├── data/
│   ├── model/
│   ├── static/
│   ├── templates/
│   ├── analysis.py
│   ├── app.py
│   └── train_model.py
│
├── .gitignore
├── airlines-delay-and-cancellation-analysis.ipynb
└── README.md
