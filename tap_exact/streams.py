"""Stream type classes for tap-exact."""

from __future__ import annotations

import typing as t
from pathlib import Path

from singer_sdk.typing import StringType, IntegerType, BooleanType, DateTimeType, PropertiesList, Property, NumberType

from tap_exact.client import ExactStream, ExactSyncStream


class TransactionLinesStream(ExactSyncStream):
    """Define TransactionLines stream."""

    name = "transaction_lines"
    path = "/sync/Financial/TransactionLines"
    primary_keys: t.ClassVar[list[str]] = ["ID"]
    replication_key = "Timestamp"
    schema = PropertiesList(
        Property("Timestamp", IntegerType),
        Property("Account", BooleanType),
        Property("AccountCode", StringType),
        Property("AccountName ", StringType),
        Property("AmountDC", DateTimeType),
        Property("AmountFC", StringType),
        Property("AmountVATBaseFC", StringType),
        Property("AmountVATFC", IntegerType),
        Property("Asset", StringType),
        Property("AssetCode", BooleanType),
        Property("AssetDescription", DateTimeType),
        Property("CostCenter", StringType),
        Property("CostCenterDescription", StringType),
        Property("CostUnit", StringType),
        Property("CostUnitDescription", BooleanType),
        Property("Created", StringType),
        Property("Creator", StringType),
        Property("CreatorFullName", StringType),
        Property("Currency", StringType),
        Property("CustomField", StringType),
        Property("Date", StringType),
        Property("Description", StringType),
        Property("Division", IntegerType),
        Property("Document", StringType),
        Property("DocumentNumber", BooleanType),
        Property("DocumentSubject", DateTimeType),
        Property("DueDate", StringType),
        Property("EntryID", StringType),
        Property("EntryNumber", StringType),
        Property("ExchangeRate", BooleanType),
        Property("ExternalLinkDescription", StringType),
        Property("ExternalLinkReference", StringType),
        Property("ExtraDutyAmountFC", StringType),
        Property("ExtraDutyPercentage", StringType),
        Property("FinancialPeriod", StringType),
        Property("FinancialYear", StringType),
        Property("GLAccount", DateTimeType),
        Property("GLAccountCode", StringType),
        Property("GLAccountDescription", StringType),
        Property("ID", IntegerType),
        Property("InvoiceNumber", StringType),
        Property("Item", BooleanType),
        Property("ItemCode", DateTimeType),
        Property("ItemDescription", StringType),
        Property("JournalCode", StringType),
        Property("LineNumber", StringType),
        Property("LineType", BooleanType),
        Property("Modified", StringType),
        Property("ModifierFullName", StringType),
        Property("Notes", StringType),
        Property("OffsetID", StringType),
        Property("OrderNumber", StringType),
        Property("PaymentDiscountAmount", StringType),
        Property("PaymentReference", StringType),
        Property("Project", IntegerType),
        Property("ProjectCode", StringType),
        Property("ProjectDescription", BooleanType),
        Property("Quantity", DateTimeType),
        Property("SerialNumber", StringType),
        Property("Status", StringType),
        Property("Subscription", StringType),
        Property("SubscriptionDescription", BooleanType),
        Property("TrackingNumber", StringType),
        Property("TrackingNumberDescription", StringType),
        Property("Type", StringType),
        Property("VATCode", StringType),
        Property("VATCodeDescription", StringType),
        Property("VATPercentage", StringType),
        Property("VATType", StringType),
        Property("YourRef", StringType),
    ).to_dict()


class GLAccountsStream(ExactSyncStream):
    """Define GLAccounts stream."""

    name = "gl_accounts"
    path = "/sync/Financial/GLAccounts"
    primary_keys: t.ClassVar[list[str]] = ["ID"]
    replication_key = "Timestamp"
    schema = PropertiesList(
        Property("Timestamp", IntegerType),
        Property("AllowCostsInSales", BooleanType),
        Property("AssimilatedVATBox", IntegerType),
        Property("BalanceSide", StringType),
        Property("BalanceType", StringType),
        Property("BelcotaxType", IntegerType),
        Property("Code", StringType),
        Property("Compress", BooleanType),
        Property("Costcenter", StringType),
        Property("CostcenterDescription", StringType),
        Property("Costunit", StringType),
        Property("CostunitDescription", StringType),
        Property("Created", DateTimeType),
        Property("Creator", StringType),
        Property("CreatorFullName", StringType),
        Property("CustomField", StringType),
        Property("Description", StringType),
        Property("Division", IntegerType),
        Property("ExcludeVATListing", BooleanType),
        Property("ExpenseNonDeductiblePercentage", NumberType),
        Property("ID", StringType),
        Property("IsBlocked", BooleanType),
        Property("Matching", BooleanType),
        Property("Modified", DateTimeType),
        Property("Modifier", StringType),
        Property("ModifierFullName", StringType),
        Property("PrivateGLAccount", StringType),
        Property("PrivatePercentage", NumberType),
        Property("ReportingCode", BooleanType),
        Property("RevalueCurrency", BooleanType),
        Property("SearchCode", StringType),
        Property("Type", IntegerType),
        Property("TypeDescription", StringType),
        Property("UseCostcenter", BooleanType),
        Property("UseCostunit", BooleanType),
        Property("VATCode", StringType),
        Property("VATDescription", StringType),
        Property("VATGLAccountType", StringType),
        Property("VATNonDeductibleGLAccount", StringType),
        Property("VATNonDeductiblePercentage", NumberType),
        Property("VATSystem", StringType),
        Property("YearEndCostGLAccount", StringType),
        Property("YearEndReflectionGLAccount", StringType),
    ).to_dict()


class GLClassificationsStream(ExactSyncStream):
    """Define GLClassifications stream."""

    name = "gl_classifications"
    path = "/sync/Financial/GLClassifications"
    primary_keys: t.ClassVar[list[str]] = ["ID"]
    replication_key = "Timestamp"
    schema = PropertiesList(
        Property("Timestamp", IntegerType),
        Property("Abstract", BooleanType),
        Property("Balance", StringType),
        Property("Code", StringType),
        Property("Created", DateTimeType),
        Property("CreatorFullName", StringType),
        Property("Description", StringType),
        Property("Division", IntegerType),
        Property("ID", StringType),
        Property("IsTupleSubElement", BooleanType),
        Property("Modified", DateTimeType),
        Property("Modifier", StringType),
        Property("ModifierFullName", StringType),
        Property("Name", StringType),
        Property("Nillable", BooleanType),
        Property("Parent", StringType),
        Property("PeriodType", StringType),
        Property("SubstitutionGroup", StringType),
        Property("TaxonomyNamespace", StringType),
        Property("TaxonomyNamespaceDescription", StringType),
        Property("Type", StringType),
    ).to_dict()


class GLAccountClassificationMappingsStream(ExactStream):
    """Define GLAccountClassificationMappings stream."""

    name = "gl_account_classification_mappings"
    path = "/Financial/GLAccountClassificationMappings"
    primary_keys: t.ClassVar[list[str]] = ["ID"]
    schema = PropertiesList(
        Property("ID", StringType),
        Property("Classification", StringType),
        Property("ClassificationCode", StringType),
        Property("ClassificationDescription", StringType),
        Property("Division", IntegerType),
        Property("GLAccount", StringType),
        Property("GLAccountCode", StringType),
        Property("GLAccountDescription", StringType),
        Property("GLSchemeCode", StringType),
        Property("GLSchemeDescription", StringType),
        Property("GLSchemeID", StringType),
    ).to_dict()
