"""Utility functions for configuration handling."""

from pathlib import Path
import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def load_config(path: Path | None = None) -> dict:
    """Load YAML configuration file."""
    if path is None:
        path = PROJECT_ROOT / 'config.yaml'
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def save_config(cfg: dict, path: Path | None = None) -> None:
    """Write configuration dictionary to YAML."""
    if path is None:
        path = PROJECT_ROOT / 'config.yaml'
    with open(path, 'w', encoding='utf-8') as f:
        yaml.safe_dump(cfg, f)
