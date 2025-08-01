"""Fetch recent news headlines for specified stocks using NewsAPI."""
from datetime import datetime
from pathlib import Path
from typing import Iterable, List

import pandas as pd
import requests

from .utils import load_config

DATA_DIR = Path(__file__).resolve().parents[1] / 'data'


def fetch_news(keywords: List[str]) -> pd.DataFrame:
    config = load_config()
    api_key = config['api_keys'].get('news_api', '')
    url = 'https://newsapi.org/v2/everything'

    articles = []
    for keyword in keywords:
        params = {
            'q': keyword,
            'apiKey': api_key,
            'pageSize': 5,
            'sortBy': 'publishedAt',
        }
        resp = requests.get(url, params=params, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            for item in data.get('articles', []):
                articles.append({
                    'keyword': keyword,
                    'title': item['title'],
                    'publishedAt': item['publishedAt'],
                })
    df = pd.DataFrame(articles)
    DATA_DIR.joinpath('news_feeds').mkdir(parents=True, exist_ok=True)
    path = DATA_DIR / 'news_feeds' / f"news_{datetime.now().date()}.csv"
    df.to_csv(path, index=False)
    return df


def fetch_news_since(keywords: Iterable[str], since: str) -> pd.DataFrame:
    """Fetch news since a given ISO date (YYYY-MM-DD)."""
    since_dt = datetime.fromisoformat(since)
    df = fetch_news(list(keywords))
    df['publishedAt'] = pd.to_datetime(df['publishedAt'])
    return df[df['publishedAt'] >= since_dt]
