from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "house_price_model.pkl"


def load_model():
    return joblib.load(MODEL_PATH)


def predict_price(input_data):
    model = load_model()
    prediction = model.predict(input_data)
    return prediction[0]