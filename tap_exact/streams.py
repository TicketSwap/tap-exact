"""Stream type classes for tap-exact."""

from __future__ import annotations

import typing as t

from tap_exact import schemas
from tap_exact.client import ExactBulkStream, ExactStream, ExactSyncStream


class TransactionLinesStream(ExactBulkStream):
    """Define TransactionLines stream."""

    name = "transaction_lines"
    path = "/bulk/Financial/TransactionLines"
    primary_keys: t.ClassVar[list[str]] = ["ID", "Division"]
    replication_key: t.ClassVar[str] = "Modified"
    schema = schemas.transaction_lines_schema  # pyright: ignore[reportAssignmentType]


class GLAccountsStream(ExactBulkStream):
    """Define GLAccounts stream."""

    name = "gl_accounts"
    path = "/bulk/Financial/GLAccounts"
    primary_keys: t.ClassVar[list[str]] = ["ID", "Division"]
    replication_key: t.ClassVar[str] = "Modified"
    schema = schemas.gl_accounts_schema  # pyright: ignore[reportAssignmentType]


class GLClassificationsStream(ExactBulkStream):
    """Define GLClassifications stream."""

    name = "gl_classifications"
    path = "/bulk/Financial/GLClassifications"
    primary_keys: t.ClassVar[list[str]] = ["ID", "Division"]
    schema = schemas.gl_classifications_schema  # pyright: ignore[reportAssignmentType]


class GLAccountClassificationMappingsStream(ExactStream):
    """Define GLAccountClassificationMappings stream."""

    name = "gl_account_classification_mappings"
    path = "/Financial/GLAccountClassificationMappings"
    primary_keys: t.ClassVar[list[str]] = ["ID", "Division"]
    schema = schemas.gl_account_classification_mappings_schema  # pyright: ignore[reportAssignmentType]


class AssetsStream(ExactStream):
    """Define Assets stream."""

    name = "assets"
    path = "/assets/Assets"
    primary_keys: t.ClassVar[list[str]] = ["ID", "Division"]
    schema = schemas.assets_schema  # pyright: ignore[reportAssignmentType]


class DeletedStream(ExactSyncStream):
    """Define Deleted stream."""

    name = "deleted"
    path = "/sync/Deleted"
    primary_keys: t.ClassVar[list[str]] = ["ID", "Division"]
    replication_key: t.ClassVar[str] = "Timestamp"
    schema = schemas.deleted_schema  # pyright: ignore[reportAssignmentType]
