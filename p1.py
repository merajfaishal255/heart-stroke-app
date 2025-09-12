import streamlit as st
import joblib  
import numpy as np
import pandas as pd


st.title("❤️ Heart Stroke Risk Predictor        (Faishal Meraj)")
st.markdown("**Important:** This is an educational demo — not medical advice.")

# Load model
model = joblib.load("stroke_model.pkl")  # the pipeline saved by train_model.py