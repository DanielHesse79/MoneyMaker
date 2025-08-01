"""Streamlit dashboard for SmartTradeAI."""
import pandas as pd
import streamlit as st
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / 'data'
LOG_FILE = Path(__file__).resolve().parents[1] / 'logs' / 'trade_logs.log'

st.title('SmartTradeAI Dashboard')

portfolio = pd.read_csv(DATA_DIR / 'portfolio.csv')
st.subheader('Portfolio')
st.table(portfolio)

if LOG_FILE.exists():
    logs = LOG_FILE.read_text().splitlines()[-10:]
    st.subheader('Recent Trades')
    for line in logs:
        st.write(line)
