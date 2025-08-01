"""Utilities for computing news sentiment."""

from __future__ import annotations

from typing import Iterable, List

from textblob import TextBlob


def get_sentiment(text: str) -> float:
    """Return polarity score in the range [-1, 1]."""
    analysis = TextBlob(text)
    return analysis.sentiment.polarity


def aggregate_sentiment(texts: Iterable[str]) -> float:
    """Average sentiment over multiple texts."""
    scores: List[float] = [get_sentiment(t) for t in texts]
    if not scores:
        return 0.0
    return sum(scores) / len(scores)
