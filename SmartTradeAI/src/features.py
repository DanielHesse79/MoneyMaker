"""Feature engineering utilities for price data."""

from __future__ import annotations

import pandas as pd


def add_sma(df: pd.DataFrame, window: int = 14) -> pd.DataFrame:
    """Append a simple moving average column."""
    df[f"SMA_{window}"] = df["Close"].rolling(window=window).mean()
    return df


def add_ema(df: pd.DataFrame, window: int = 14) -> pd.DataFrame:
    """Append an exponential moving average column."""
    df[f"EMA_{window}"] = df["Close"].ewm(span=window, adjust=False).mean()
    return df


def add_rsi(df: pd.DataFrame, window: int = 14) -> pd.DataFrame:
    """Compute the Relative Strength Index."""
    delta = df["Close"].diff()
    gain = delta.where(delta > 0, 0.0)
    loss = -delta.where(delta < 0, 0.0)
    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()
    rs = avg_gain / avg_loss.replace(0, 1)
    df[f"RSI_{window}"] = 100 - (100 / (1 + rs))
    return df


def add_returns(df: pd.DataFrame) -> pd.DataFrame:
    """Add daily percentage returns."""
    df["returns"] = df["Close"].pct_change()
    return df
