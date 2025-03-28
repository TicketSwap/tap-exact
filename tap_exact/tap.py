"""Exact tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk.typing import ArrayType, DateTimeType, PropertiesList, Property, StringType

from tap_exact import streams


class TapExact(Tap):
    """Exact tap class."""

    name = "tap-exact"

    config_jsonschema = PropertiesList(
        Property("start_date", DateTimeType),
        Property("client_id", StringType, secret=True, required=True),
        Property("client_secret", StringType, secret=True, required=True),
        Property("tokens_s3_bucket", StringType, required=True),
        Property("tokens_s3_key", StringType, required=True),
        Property("divisions", ArrayType(StringType), required=True),
    ).to_dict()

    def discover_streams(self) -> list[streams.ExactStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.GLAccountsStream(self),
            streams.GLClassificationsStream(self),
            streams.GLAccountClassificationMappingsStream(self),
            streams.TransactionLinesStream(self),
        ]


if __name__ == "__main__":
    TapExact.cli()
