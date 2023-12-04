"""Exact tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk.typing import DateTimeType, StringType, Property, PropertiesList

# TODO: Import your custom stream types here:
from tap_exact import streams


class TapExact(Tap):
    """Exact tap class."""

    name = "tap-exact"

    config_jsonschema = PropertiesList(
        Property("start_date", DateTimeType),
        Property("client_id", StringType),
        Property("client_secret", StringType),
        Property("tokens_s3_bucket", StringType),
        Property("tokens_s3_key", StringType),
        Property("division", StringType),
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
