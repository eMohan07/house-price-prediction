import pytest
import pandas as pd
from src.utils import validate_house
from src.predict import load_pipeline, predict_price
from src.constants import CITIES


@pytest.fixture
def sample_house_input():
    return pd.DataFrame([{
        "bedrooms": 3,
        "bathrooms": 2.0,
        "sqft_living": 2000,
        "sqft_lot": 5000,
        "floors": 1.0,
        "waterfront": 0,
        "view": 0,
        "condition": 3,
        "sqft_above": 1500,
        "sqft_basement": 500,
        "yr_built": 2000,
        "yr_renovated": 0,
        "city": "Seattle"
    }])


def test_validate_house_valid():
    assert validate_house(sqft_living=2000, sqft_above=1500, sqft_basement=500) is True
    assert validate_house(sqft_living=2000, sqft_above=1000, sqft_basement=500) is True


def test_validate_house_invalid():
    # Above + basement exceeds living
    assert validate_house(sqft_living=2000, sqft_above=1600, sqft_basement=500) is False


def test_model_pipeline_loading():
    pipeline = load_pipeline()
    assert pipeline is not None
    assert hasattr(pipeline, "predict")


def test_predict_price_valid(sample_house_input):
    price = predict_price(sample_house_input)
    assert isinstance(price, (int, float))
    assert price > 0


def test_predict_price_deterministic(sample_house_input):
    price_1 = predict_price(sample_house_input)
    price_2 = predict_price(sample_house_input)
    assert price_1 == price_2


def test_predict_price_different_cities(sample_house_input):
    for city in CITIES[:3]:
        df = sample_house_input.copy()
        df["city"] = city
        price = predict_price(df)
        assert isinstance(price, (int, float))
        assert price > 0
