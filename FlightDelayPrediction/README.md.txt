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
FlightDelayPrediction/
│
├── data/
│
├── model/
│
├── static/
│
├── templates/
│
├── analysis.py
├── app.py
├── train_model.py
└── README.md
```

## ⚙️ How to Run the Project

Follow these steps to run the Flight Delay Prediction and Analytics System on your local machine.

### Step 1: Open the Project Folder

Open Anaconda Prompt or a terminal and navigate to the project folder that contains `app.py`.

For example:

```bash
cd /path/to/FlightDelayPrediction
```

**Important:** Make sure you are inside the `FlightDelayPrediction` folder containing `app.py` before running the following commands.

### Step 2: Activate the Conda Environment

Activate the existing Conda environment used for this project:

```bash
conda activate tfenv
```

### Step 3: Run the Application

Start the Flask web application:

```bash
python app.py
```

Once the application starts successfully, open the local URL displayed in the terminal in your web browser.

The application is now ready to use.

## 🔄 System Workflow

1. The user accesses the web application.
2. Flight-related information is provided through the interface.
3. The application processes the input data.
4. The trained Random Forest model predicts the flight delay category.
5. The prediction is displayed to the user.
6. The analytics module provides insights into flight delay patterns.

## 🔮 Future Enhancements

- Integrate real-time flight data.
- Improve prediction accuracy through model optimization.
- Compare multiple machine learning algorithms.
- Deploy the application on a cloud platform.
- Enhance data visualization and analytics.

## 👩‍💻 Project Outcome

This project demonstrates how machine learning and web development can be combined to predict flight delays and analyze contributing factors. The Flask application provides an accessible interface for generating predictions and exploring flight delay insights.

## 📜 License

This project is developed for educational and learning purposes.
