#!/usr/bin/env python3
"""
Test script to validate logger_utils functionality.
"""

from typing import List

from logger_utils import (
    get_log_level_from_string,
    log_list_items,
    log_section_header,
    setup_logging,
)


def main() -> None:
    # Test logger setup
    logger = setup_logging(get_log_level_from_string("INFO"), logger_name=__name__)

    # Test section headers
    log_section_header(logger, "🧪 Logger Utility Test")

    # Test different log levels
    logger.info("✅ INFO level message")
    logger.warning("⚠️ WARNING level message")
    logger.error("❌ ERROR level message")
    logger.debug("🔍 DEBUG level message (should not show with INFO level)")

    # Test list logging
    test_channels: List[str] = [
        "festival-operations",
        "tech-support",
        "customer-escalations",
        "venue-coordination",
    ]
    log_list_items(logger, test_channels, "Test Channels")

    # Test long list with truncation
    long_list: List[str] = [f"item-{i}" for i in range(15)]
    log_list_items(logger, long_list, "Long List Test", max_items=5)

    log_section_header(logger, "✅ Logger Test Complete")


if __name__ == "__main__":
    main()
