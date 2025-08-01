"""Preprocess market and news data."""

from __future__ import annotations

from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[1] / 'data'


def clean_price_data(df: pd.DataFrame) -> pd.DataFrame:
    """Drop duplicates and fill missing prices."""
    df = df.drop_duplicates(subset="Date")
    df = df.sort_values("Date")
    df = df.fillna(method="ffill")
    return df


def clean_news_data(df: pd.DataFrame) -> pd.DataFrame:
    """Drop duplicated news items."""
    return df.drop_duplicates(subset="title")


def merge_price_news(price_df: pd.DataFrame, news_df: pd.DataFrame) -> pd.DataFrame:
    """Simple merge of price and news on date."""
    news_df["date"] = pd.to_datetime(news_df["publishedAt"]).dt.date
    price_df["date"] = pd.to_datetime(price_df["Date"]).dt.date
    merged = pd.merge(price_df, news_df, on="date", how="left")
    return merged
