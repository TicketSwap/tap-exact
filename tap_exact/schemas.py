"""Schemas for Exact Online streams."""

from singer_sdk.typing import (
    BooleanType,
    DateTimeType,
    IntegerType,
    NumberType,
    PropertiesList,
    Property,
    StringType,
)

transaction_lines_schema = PropertiesList(
    Property("Timestamp", IntegerType),
    Property("Account", StringType),
    Property("AccountCode", StringType),
    Property("AccountName", StringType),
    Property("AmountDC", NumberType),
    Property("AmountFC", NumberType),
    Property("AmountVATBaseFC", NumberType),
    Property("AmountVATFC", NumberType),
    Property("Asset", StringType),
    Property("AssetCode", StringType),
    Property("AssetDescription", StringType),
    Property("CostCenter", StringType),
    Property("CostCenterDescription", StringType),
    Property("CostUnit", StringType),
    Property("CostUnitDescription", StringType),
    Property("Created", DateTimeType),
    Property("Creator", StringType),
    Property("CreatorFullName", StringType),
    Property("Currency", StringType),
    Property("CustomField", StringType),
    Property("Date", DateTimeType),
    Property("Description", StringType),
    Property("Division", IntegerType),
    Property("Document", StringType),
    Property("DocumentNumber", IntegerType),
    Property("DocumentSubject", StringType),
    Property("DueDate", DateTimeType),
    Property("EntryID", StringType),
    Property("EntryNumber", IntegerType),
    Property("ExchangeRate", NumberType),
    Property("ExternalLinkDescription", StringType),
    Property("ExternalLinkReference", StringType),
    Property("ExtraDutyAmountFC", NumberType),
    Property("ExtraDutyPercentage", NumberType),
    Property("FinancialPeriod", IntegerType),
    Property("FinancialYear", IntegerType),
    Property("GLAccount", StringType),
    Property("GLAccountCode", StringType),
    Property("GLAccountDescription", StringType),
    Property("ID", StringType),
    Property("InvoiceNumber", IntegerType),
    Property("Item", StringType),
    Property("ItemCode", StringType),
    Property("ItemDescription", StringType),
    Property("JournalCode", StringType),
    Property("JournalDescription", StringType),
    Property("LineNumber", IntegerType),
    Property("LineType", IntegerType),
    Property("Modified", DateTimeType),
    Property("ModifierFullName", StringType),
    Property("Notes", StringType),
    Property("OffsetID", StringType),
    Property("OrderNumber", IntegerType),
    Property("PaymentDiscountAmount", NumberType),
    Property("PaymentReference", StringType),
    Property("Project", StringType),
    Property("ProjectCode", StringType),
    Property("ProjectDescription", StringType),
    Property("Quantity", NumberType),
    Property("SerialNumber", StringType),
    Property("Status", IntegerType),
    Property("Subscription", StringType),
    Property("SubscriptionDescription", StringType),
    Property("TrackingNumber", StringType),
    Property("TrackingNumberDescription", StringType),
    Property("Type", IntegerType),
    Property("VATCode", StringType),
    Property("VATCodeDescription", StringType),
    Property("VATPercentage", NumberType),
    Property("VATType", StringType),
    Property("YourRef", StringType),
).to_dict()

gl_accounts_schema = PropertiesList(
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

gl_classifications_schema = PropertiesList(
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

gl_account_classification_mappings_schema = PropertiesList(
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

assets_schema = PropertiesList(
    Property("ID", StringType),  # Primary key
    Property("AlreadyDepreciated", IntegerType),  # Asset already depreciated before registering
    Property("AssetFrom", StringType),  # Original asset ID in case of transfer/split
    Property("AssetFromDescription", StringType),  # Description of AssetFrom
    Property("AssetGroup", StringType),  # Asset group for GLAccount transactions
    Property("AssetGroupCode", StringType),  # Code of the asset group
    Property("AssetGroupDescription", StringType),  # Description of the asset group
    Property("CatalogueValue", NumberType),  # The catalogue value of the asset
    Property("Code", StringType),  # Code of the asset
    Property("CommercialBuildingValues", StringType),  # Commercial building values with dates
    Property("Costcenter", StringType),  # Assets can be linked to a cost center
    Property("CostcenterDescription", StringType),  # Description of Costcenter
    Property("Costunit", StringType),  # Assets can be linked to a cost unit
    Property("CostunitDescription", StringType),  # Description of Costunit
    Property("Created", DateTimeType),  # Creation date
    Property("Creator", StringType),  # User ID of creator
    Property("CreatorFullName", StringType),  # Name of creator
    Property("CustomField", StringType),  # Custom field endpoint
    Property("DeductionPercentage", NumberType),  # Belgium legislation investment deduction
    Property("DepreciatedAmount", NumberType),  # Already depreciated amount for existing asset
    Property("DepreciatedPeriods", IntegerType),  # Number of periods already depreciated
    Property("DepreciatedStartDate", DateTimeType),  # StartDate of depreciating
    Property("Description", StringType),  # This is the description of the Asset
    Property("Division", IntegerType),  # Division code
    Property("EndDate", DateTimeType),  # Asset EndDate when Sold or Inactive
    Property("EngineEmission", IntegerType),  # Engine emission for co² report
    Property("EngineType", IntegerType),  # Engine type for co² report
    Property("GLTransactionLine", StringType),  # GL transaction line creating the asset
    Property("GLTransactionLineDescription", StringType),  # Description of GLTransactionLine
    Property("InvestmentAccount", StringType),  # Supplier of the asset
    Property("InvestmentAccountCode", StringType),  # Code of InvestmentAccount
    Property("InvestmentAccountName", StringType),  # Name of InvestmentAccount
    Property("InvestmentAmountDC", NumberType),  # Investment amount in default currency
    Property("InvestmentAmountFC", NumberType),  # Investment value of the asset
    Property("InvestmentCurrency", StringType),  # Currency of the investment amount
    Property("InvestmentCurrencyDescription", StringType),  # Description of InvestmentCurrency
    Property("InvestmentDate", DateTimeType),  # Original date when asset was bought
    Property("InvestmentDeduction", IntegerType),  # Belgian investment deduction functionality
    Property("Modified", DateTimeType),  # Last modified date
    Property("Modifier", StringType),  # User ID of modifier
    Property("ModifierFullName", StringType),  # Name of modifier
    Property("Notes", StringType),  # Extra remarks for the asset
    Property("Parent", StringType),  # Parent asset
    Property("ParentCode", StringType),  # Code of Parent
    Property("ParentDescription", StringType),  # Description of Parent
    Property("Picture", StringType),  # Image for an asset (Binary data as string)
    Property("PictureFileName", StringType),  # Filename of the image
    Property("PrimaryMethod", StringType),  # First method of depreciation
    Property("PrimaryMethodCode", StringType),  # Code of PrimaryMethod
    Property("PrimaryMethodDescription", StringType),  # Description of PrimaryMethod
    Property("ResidualValue", NumberType),  # Residual value at end of depreciation
    Property("StartDate", DateTimeType),  # Asset Depreciation StartDate
    Property("Status", IntegerType),  # Asset status (1=Active, 2=Not validated, etc.)
    Property("TransactionEntryID", StringType),  # Reference to transaction lines
    Property("TransactionEntryNo", IntegerType),  # Entry number of transaction
    Property("Type", StringType),  # Asset type (0=Other Assets, 1=Commercial Building)
).to_dict()
