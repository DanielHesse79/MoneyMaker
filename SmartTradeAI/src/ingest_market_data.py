"""Fetch historical and real-time market data using yfinance."""
from datetime import datetime, timedelta
from pathlib import Path
from typing import List

import pandas as pd
import yfinance as yf

from .utils import load_config


DATA_DIR = Path(__file__).resolve().parents[1] / 'data'


def download_historical(stocks: List[str], start: str = '2020-01-01') -> None:
    """Download historical price data to CSV files."""
    DATA_DIR.joinpath('historical_prices').mkdir(parents=True, exist_ok=True)
    for symbol in stocks:
        df = yf.download(symbol, start=start)
        df.reset_index(inplace=True)
        path = DATA_DIR / 'historical_prices' / f"{symbol}.csv"
        df.to_csv(path, index=False)


def update_historical(stocks: List[str]) -> None:
    """Update existing historical CSVs with the latest data."""
    for symbol in stocks:
        path = DATA_DIR / 'historical_prices' / f"{symbol}.csv"
        if path.exists():
            existing = pd.read_csv(path, parse_dates=['Date'])
            last_date = pd.to_datetime(existing['Date']).max()
            next_day = last_date + timedelta(days=1)
            new_data = yf.download(symbol, start=str(next_day.date()))
            new_data.reset_index(inplace=True)
            if not new_data.empty:
                updated = pd.concat([existing, new_data])
                updated.to_csv(path, index=False)


def fetch_latest(stocks: List[str]) -> pd.DataFrame:
    """Fetch latest price data for the given stocks."""
    prices = {}
    for symbol in stocks:
        ticker = yf.Ticker(symbol)
        info = ticker.history(period='1d')
        prices[symbol] = info['Close'].iloc[-1]
    df = pd.DataFrame(list(prices.items()), columns=['symbol', 'price'])
    path = DATA_DIR / 'real_time_data' / f"prices_{datetime.now().date()}.csv"
    DATA_DIR.joinpath('real_time_data').mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    return df
