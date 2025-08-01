"""Simple rule-based trading agent."""

from __future__ import annotations

from pathlib import Path
from typing import Dict

import pandas as pd

from .predict_prices import predict
from .sentiment_analysis import get_sentiment


def decide(model_path: Path, price_csv: Path, news_text: str) -> str:
    """Return a trading action based on predicted change and sentiment."""
    price_pred = predict(model_path, price_csv)
    last_close = _last_close(price_csv)
    change = price_pred - last_close
    sentiment = get_sentiment(news_text)
    if change > 0 and sentiment > 0:
        return "BUY"
    if change < 0 and sentiment < 0:
        return "SELL"
    return "HOLD"


def reasoning(model_path: Path, price_csv: Path, news_text: str) -> Dict[str, str]:
    """Provide reasoning for a trade decision."""
    price_pred = predict(model_path, price_csv)
    last_close = _last_close(price_csv)
    change = price_pred - last_close
    sentiment = get_sentiment(news_text)
    action = decide(model_path, price_csv, news_text)
    reason = (
        f"Predicted close: {price_pred:.2f} (change {change:+.2f}) "
        f"with sentiment {sentiment:.2f}. Action: {action}."
    )
    return {"action": action, "reason": reason}


def _last_close(price_csv: Path) -> float:
    """Return the most recent closing price from a CSV."""
    df = pd.read_csv(price_csv)
    return float(df["Close"].iloc[-1])
