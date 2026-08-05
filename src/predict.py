import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PIPELINE_PATH = BASE_DIR / "models" / "house_price_pipeline.pkl"


def load_pipeline():
    return joblib.load(PIPELINE_PATH)


def predict_price(input_df):
    pipeline = load_pipeline()
    prediction = pipeline.predict(input_df)[0]
    return max(0, round(prediction))