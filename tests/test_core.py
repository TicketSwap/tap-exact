"""Tests standard tap features using the built-in SDK tests library."""

import os
from datetime import datetime, timedelta, timezone

import pytest
from singer_sdk.testing import get_tap_test_class

from tap_exact.tap import TapExact

SAMPLE_CONFIG = {
    "start_date": (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y-%m-%d"),
    "client_id": os.getenv("TAP_EXACT_CLIENT_ID", ""),
    "client_secret": os.getenv("TAP_EXACT_CLIENT_SECRET", ""),
    "tokens_s3_bucket": os.getenv("TAP_EXACT_TOKENS_S3_BUCKET", ""),
    "tokens_s3_key": os.getenv("TAP_EXACT_TOKENS_S3_KEY", ""),
    "divisions": ["3490573"],
}

pytestmark = pytest.mark.skipif(
    not SAMPLE_CONFIG["client_id"],
    reason="needs TAP_EXACT_* credentials, and every run rotates the OAuth tokens stored in S3",
)

TestTapExact = get_tap_test_class(
    tap_class=TapExact,
    config=SAMPLE_CONFIG,
)
