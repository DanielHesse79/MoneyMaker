"""Utilities for running the price prediction model."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from .features import add_sma


def predict(model_path: Path, price_csv: Path) -> float:
    """Predict the next closing price."""
    model = pd.read_pickle(model_path)
    df = pd.read_csv(price_csv)
    df = add_sma(df)
    df = df.dropna()
    last_row = df.iloc[-1:]
    pred = model.predict(last_row[[f"SMA_14"]])
    return float(pred[0])


def predict_series(model_path: Path, price_csv: Path) -> pd.Series:
    """Return predictions for an entire price series."""
    model = pd.read_pickle(model_path)
    df = pd.read_csv(price_csv)
    df = add_sma(df)
    df = df.dropna()
    preds = model.predict(df[[f"SMA_14"]])
    return pd.Series(preds, index=df["Date"]).astype(float)
