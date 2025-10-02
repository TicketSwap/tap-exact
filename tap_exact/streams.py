"""Stream type classes for tap-exact."""

from __future__ import annotations

import typing as t

from tap_exact.client import ExactStream, ExactSyncStream
from tap_exact.schemas import (
    assets_schema,
    gl_account_classification_mappings_schema,
    gl_accounts_schema,
    gl_classifications_schema,
    transaction_lines_schema,
)


class TransactionLinesStream(ExactSyncStream):
    """Define TransactionLines stream."""

    name = "transaction_lines"
    path = "/sync/Financial/TransactionLines"
    primary_keys: t.ClassVar[list[str]] = ["ID", "Division"]
    replication_key: t.ClassVar[str] = "Timestamp"
    schema = transaction_lines_schema  # pyright: ignore[reportAssignmentType]


class GLAccountsStream(ExactSyncStream):
    """Define GLAccounts stream."""

    name = "gl_accounts"
    path = "/sync/Financial/GLAccounts"
    primary_keys: t.ClassVar[list[str]] = ["ID", "Division"]
    replication_key: t.ClassVar[str] = "Timestamp"
    schema = gl_accounts_schema  # pyright: ignore[reportAssignmentType]


class GLClassificationsStream(ExactSyncStream):
    """Define GLClassifications stream."""

    name = "gl_classifications"
    path = "/sync/Financial/GLClassifications"
    primary_keys: t.ClassVar[list[str]] = ["ID", "Division"]
    replication_key: t.ClassVar[str] = "Timestamp"
    schema = gl_classifications_schema  # pyright: ignore[reportAssignmentType]


class GLAccountClassificationMappingsStream(ExactStream):
    """Define GLAccountClassificationMappings stream."""

    name = "gl_account_classification_mappings"
    path = "/Financial/GLAccountClassificationMappings"
    primary_keys: t.ClassVar[list[str]] = ["ID", "Division"]
    schema = gl_account_classification_mappings_schema  # pyright: ignore[reportAssignmentType]


class AssetsStream(ExactStream):
    """Define Assets stream."""

    name = "assets"
    path = "/assets/Assets"
    primary_keys: t.ClassVar[list[str]] = ["ID", "Division"]
    schema = assets_schema  # pyright: ignore[reportAssignmentType]
