"""Simulated trade execution."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

from .monitoring_logging import get_logger
from .portfolio_management import update_position
from .utils import load_config

LOG_FILE = Path(__file__).resolve().parents[1] / 'logs' / 'trade_logs.log'
logger = get_logger()


def execute_trade(symbol: str, action: str, shares: float) -> None:
    """Record a simulated trade and update the portfolio."""
    update_position(symbol, shares if action == "BUY" else -shares)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(
            f"{datetime.now().isoformat()} - {action} {shares} of {symbol}\n"
        )
    logger.info("%s %s shares of %s", action, shares, symbol)
