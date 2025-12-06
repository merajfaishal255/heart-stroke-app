❤️ Heart Stroke Prediction App

A simple and interactive Streamlit Machine Learning Web App created by Faishal Meraj.
This project predicts whether a person is at high risk of stroke based on their health details.                                                               

🚀 Project Overview

This project uses:                   

Python   

Streamlit (for web app UI)

Pandas (for data handling)

Scikit-Learn (for ML model)

Random Forest Classifier (machine learning algorithm)

The app lets users enter Age, Hypertension, Heart Disease, Glucose Level, and BMI — and predicts stroke risk instantly.

🧠 How It Works

A small sample dataset is created inside the code.

Features (age, hypertension, etc.) and target (stroke) are separated.

The Random Forest model is trained using train_test_split.

Using the sidebar, the user enters patient details.

The model predicts:

⚠️ High Risk of Stroke

✅ Low Risk of Stroke

📸 App Preview

✔ Sidebar for patient input
✔ Instant prediction
✔ Clean UI using Streamlit
✔ Error/Success message output

📁 Project Structure
📦 Heart-Stroke-Prediction
│
├── app.py            # Main Streamlit app
├── README.md         # Project documentation
└── requirements.txt  # (Optional) Required packages

🧩 Code Explanation 
1. Import Libraries
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

2. Create Sample Data

A mini dataset is used for demo purposes.

3. Train ML Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

4. Build Streamlit UI

User inputs are taken from sidebar sliders, number inputs, and dropdowns.

5. Make Prediction

If user clicks Predict, the app runs:

model.predict(input_data)


🎯 Features

Uses Random Forest ML model

Works with small sample dataset

Interactive UI

Instant predictions

🔮 Future Improvements

Use a real healthcare dataset

Improve accuracy with feature engineering

Add visualizations

Deploy on Streamlit Cloud / HuggingFace

👨‍💻 Author

Faishal Meraj
✨ Passionate about Python, ML, and building interactive apps
