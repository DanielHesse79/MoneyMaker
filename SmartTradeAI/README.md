# SmartTradeAI

SmartTradeAI is an experimental autonomous trading agent that integrates market
data, news sentiment, machine learning predictions, and LLM-driven decision
making.

## Features
- Fetches historical and real-time price data using `yfinance`.
- Collects recent news headlines from NewsAPI.
- Computes technical indicators such as SMA, EMA and RSI using `pandas`.
- Trains a lightweight model for short-term price prediction.
- Generates trade signals based on model output and sentiment scores.
- Logs actions and provides a Streamlit dashboard for monitoring.

This project is intended for research purposes only and **not** financial advice.

## Installation
```bash
python -m pip install -r requirements.txt
```

## Usage
Edit `config.yaml` with your API keys. Then run:
```bash
python main.py
```

The dashboard can be started with:
```bash
streamlit run ui/dashboard_app.py
```

The project ships a minimal demo dataset so you can try the workflow offline.
If `yfinance` fails to download data due to missing symbols, ensure your system
time is correct or adjust the date range in `ingest_market_data.py`.
