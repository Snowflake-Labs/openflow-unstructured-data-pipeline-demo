#!/usr/bin/env python3
"""
Logging utilities for Festival Operations Demo scripts.
Provides consistent logging configuration across all scripts.
"""

import logging
import sys
from typing import Dict, List, Optional, Sequence, Union


def setup_logging(
    log_level: int = logging.INFO,
    logger_name: Optional[str] = None,
    suppress_external: bool = True,
) -> logging.Logger:
    """
    Configure logging with consistent format for all scripts.

    Args:
        log_level: Logging level (logging.DEBUG, INFO, WARNING, ERROR)
        logger_name: Name for the logger (defaults to calling module)
        suppress_external: Suppress noisy external library logs

    Returns:
        Configured logger instance
    """
    # Create formatter with timestamp and consistent format
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(message)s", datefmt="%H:%M:%S"
    )

    # Create console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    # Configure root logger
    root_logger = logging.getLogger()

    # Clear any existing handlers to avoid duplicates
    root_logger.handlers.clear()

    root_logger.setLevel(log_level)
    root_logger.addHandler(console_handler)

    # Suppress noisy external library logs unless in DEBUG mode
    if suppress_external and log_level != logging.DEBUG:
        external_libraries = ["slack_sdk", "urllib3", "requests", "httpx"]
        for lib in external_libraries:
            logging.getLogger(lib).setLevel(logging.WARNING)

    # Return named logger for the calling script
    if logger_name:
        return logging.getLogger(logger_name)
    else:
        return logging.getLogger(__name__)


def get_log_level_from_string(level_str: str) -> int:
    """Convert string log level to logging constant."""
    level_map = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL,
    }
    return level_map.get(level_str.upper(), logging.INFO)


def log_separator(logger: logging.Logger, char: str = "=", length: int = 50) -> None:
    """Log a separator line for visual organization."""
    logger.info(char * length)


def log_section_header(logger: logging.Logger, title: str, char: str = "=") -> None:
    """Log a section header with separators."""
    log_separator(logger, char)
    logger.info(title)
    log_separator(logger, char)


def log_list_items(
    logger: logging.Logger,
    items: Sequence[Union[str, int, float]],
    title: Optional[str] = None,
    max_items: Optional[int] = None,
) -> None:
    """
    Log a list of items in a formatted way.

    Args:
        logger: Logger instance
        items: List of items to log
        title: Optional title for the list
        max_items: Limit number of items shown (with "and X more..." suffix)
    """
    if not items:
        if title:
            logger.info(f"{title}: None found")
        return

    display_items = items[:max_items] if max_items else items

    if title:
        logger.info(f"{title}: {', '.join(str(item) for item in display_items)}")
        if max_items and len(items) > max_items:
            remaining = len(items) - max_items
            logger.info(f"   ... and {remaining} more")
    else:
        logger.info(", ".join(str(item) for item in display_items))
        if max_items and len(items) > max_items:
            remaining = len(items) - max_items
            logger.info(f"... and {remaining} more")


# Pre-configured logger levels as constants
LOG_LEVELS: Dict[str, int] = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
}

LOG_LEVEL_CHOICES: List[str] = list(LOG_LEVELS.keys())
