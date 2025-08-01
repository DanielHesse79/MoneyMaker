"""Basic logging setup for SmartTradeAI."""

import logging
from pathlib import Path

LOG_FILE = Path(__file__).resolve().parents[1] / 'logs' / 'trade_logs.log'


def get_logger(name: str = 'smarttrade') -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
        handler = logging.FileHandler(LOG_FILE)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger


def log_trade(logger: logging.Logger, symbol: str, action: str, shares: float) -> None:
    """Log executed trade using provided logger."""
    logger.info("%s %s shares of %s", action, shares, symbol)
