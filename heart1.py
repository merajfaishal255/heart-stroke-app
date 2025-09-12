import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

st.title("❤️ Heart Stroke Prediction (Faishal Meraj)")

# Small sample data (normally you'd use a CSV dataset)
data = pd.DataFrame({
    'age': [25, 45, 65, 35, 50],
    'hypertension': [0, 1, 1, 0, 1],
    'heart_disease': [0, 1, 0, 0, 1],
    'avg_glucose_level': [85, 120, 180, 90, 160],
    'bmi': [22, 28, 31, 24, 29],
    'stroke': [0, 1, 1, 0, 1]
})

X = data.drop('stroke', axis=1)
y = data['stroke']

# Train simple model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Sidebar inputs
st.sidebar.header("Enter Patient Details")
age = st.sidebar.slider("Age", 1, 100, 30)
hypertension = st.sidebar.selectbox("Hypertension", [0, 1])
heart_disease = st.sidebar.selectbox("Heart Disease", [0, 1])
avg_glucose_level = st.sidebar.number_input("Glucose Level", 50, 300, 100)
bmi = st.sidebar.number_input("BMI", 10, 50, 22)

# Predict
if st.sidebar.button("Predict"):
    input_data = pd.DataFrame([[age, hypertension, heart_disease, avg_glucose_level, bmi]],
                              columns=X.columns)
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("⚠️ High Risk of Stroke!")
    else:
        st.success("✅ Low Risk of Stroke")