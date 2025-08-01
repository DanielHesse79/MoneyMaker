"""Entry point for SmartTradeAI."""
from pathlib import Path

from src.ingest_market_data import download_historical, fetch_latest, update_historical
from src.ingest_news_data import fetch_news
from src.train_price_model import train
from src.trading_agent import decide, reasoning
from src.trade_execution import execute_trade
from src.utils import load_config


def run() -> None:
    config = load_config()
    stocks = config['stocks']
    download_historical(stocks)
    update_historical(stocks)
    price_df = fetch_latest(stocks)
    news_df = fetch_news(stocks)

    # train using one stock's history as an example
    model_path = train(Path('data/historical_prices/AAPL.csv'))
    latest_price_csv = Path('data/historical_prices/AAPL.csv')
    news_text = ' '.join(news_df['title'].tolist())
    result = reasoning(model_path, latest_price_csv, news_text)
    execute_trade('AAPL', result['action'], shares=1)
    print(result['reason'])


if __name__ == '__main__':
    run()
