import joblib
import numpy as np
import pandas as pd
from .utils import preprocess_input

MODEL_PATH = "data/model.pkl"

def load_model():
    return joblib.load(MODEL_PATH)

def predict(model, raw_input):
    df = preprocess_input(raw_input)
    prediction = model.predict(df)
    return int(prediction[0])