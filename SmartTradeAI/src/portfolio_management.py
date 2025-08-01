"""Simple portfolio management utilities."""

from __future__ import annotations

from pathlib import Path
from typing import Dict

import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[1] / 'data'
PORTFOLIO_CSV = DATA_DIR / 'portfolio.csv'


def load_portfolio() -> pd.DataFrame:
    """Return portfolio dataframe."""
    return pd.read_csv(PORTFOLIO_CSV)


def update_position(symbol: str, shares: float) -> None:
    """Update the share count for a symbol."""
    df = load_portfolio()
    df.loc[df["symbol"] == symbol, "shares"] += shares
    df.to_csv(PORTFOLIO_CSV, index=False)


def get_position(symbol: str) -> float:
    """Get the number of shares held for a symbol."""
    df = load_portfolio()
    result = df.loc[df["symbol"] == symbol, "shares"]
    return float(result.values[0]) if not result.empty else 0.0


def portfolio_value(prices: Dict[str, float]) -> float:
    """Compute total portfolio value given current prices."""
    df = load_portfolio()
    total = 0.0
    for _, row in df.iterrows():
        symbol = row["symbol"]
        if symbol == "cash":
            total += row["shares"]
        else:
            price = prices.get(symbol, 0.0)
            total += row["shares"] * price
    return total
