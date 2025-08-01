"""Train a simple price prediction model."""
from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from .features import add_sma

MODELS_DIR = Path(__file__).resolve().parents[1] / 'models' / 'price_prediction_model'


def train(csv_path: Path) -> Path:
    """Train a linear regression model and return the saved path."""
    if not csv_path.exists():
        raise FileNotFoundError(csv_path)
    df = pd.read_csv(csv_path)
    df = add_sma(df)
    df = df.dropna()
    X = df[['SMA_14']]
    y = df['Close']
    X_train, X_test, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    model_path = MODELS_DIR / 'linear_model.pkl'
    pd.to_pickle(model, model_path)
    return model_path
