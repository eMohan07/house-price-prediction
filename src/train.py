from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_DIR = BASE_DIR / "models"
MODEL_DIR.mkdir(exist_ok=True)

MODEL_PATH = MODEL_DIR / "house_price_model.pkl"


def save_model(model):
    joblib.dump(model, MODEL_PATH)
    print(f"Model saved to: {MODEL_PATH}")