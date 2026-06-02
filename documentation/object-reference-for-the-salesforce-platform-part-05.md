`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

### BuyerGroupRelatedObject is availble only if the org is Market Enabled ( Commerce.orgHasCommerceMarketEnabled ).

Fields

**Field** **Details**

```
BuyerGroupId

LastReferencedDate

LastViewedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. ID of the buyer group this record is associated with.

This field is a relationship field.

**Relationship Name**
### BuyerGroup

**Relationship Type**
Lookup

**Refers To**
### BuyerGroup

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a list view or related record.

**Type**
dateTime


Standard Objects BuyerGroupRelatedObject

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
and `LastReferenceDate` is not null, the user accessed this record or list view indirectly..

```
Name

ObjectType

ObjectValues

```

Usage

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of this record.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. The names displayed in the picklist showing the ObjectValues - currency and
ship-to countries.

Possible values are:

**•** `DefaultCurrency`  - Default Currency

**•** `SupportedShipToCountries`  - Supported Ship-to Countries

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Optional. Values for ObjectType. The actual currency and supported ship-to countries. Possible
values are:

**•** Three-letter ISO currency code associated with the buyer account or a supported locale.

**•** ISO country code for supported ship-to countries.

BuyerGroupRelatedObject is related to objects that enable a localized buyer experience. Together, these objects provide buyers with
dynamic access to the qualifiers (entitlements, price books, and promotions) associated with their buyer group when they browse and
shop in webstores with localized languages and currencies. The related objects are as follows:

**•** BuyerGroup - stores keys that link member entitlements, price books, promotions, and shipping methods to either a single currency
and language or to multiple currencies and languages.


### Standard Objects CalcProcStepRelationship

**•** BuyerCriteria - represents locales (languages and currencies) that are enabled for BuyerGroup members when they shop in webstores
with localized currencies and languages.

**•** BuyerGroupBuyerCriteria - associates a buyer group that is enabled for webstores with multiple languages and currencies with
BuyerCriteria that define those languages and currencies.

**•** BuyerGroupRelatedObject - allows BuyerGroup qualifiers (entitlements, price books, and promotions) to be available in multiple
languages and currencies without duplicating the qualifiers for each language and currency.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**BuyerGroupRelatedObjectChangeEvent on page 68**
Change events are available for the object.

**BuyerGroupRelatedObjectFeed on page 55**
Feed tracking is available for the object.

**BuyerGroupRelatedObjectHistory on page 63**
History is available for tracked fields of the object.

### CalcProcStepRelationship

Defines a parent-child relationship between two Expression Set Steps in an Expression Set Version. The label for this object is Expression
Set Step Relationship. This object is available in API version 53.0 and later.

Note: This object has been deprecated as of API version 55.0. In API version 55.0 and later, use the new Expression Set objects in
Business Rules Engine instead.

Parent-child step relationships collectively determine the step order.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Access to Expression Sets requires OmniStudio licenses.

Fields

**Field** **Details**

```
CalcProcStepId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects CalcProcStepRelationship

**Field** **Details**

**Description**
The ID of the child Expression Set Step.

This is a relationship field.

**Relationship Name**
CalcProcStep

**Relationship Type**
Lookup

**Refers To**
CalculationProcedureStep

```
CalcProcVersionId

Name

ParentCalcProcStepId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the related Expression Set Version.

This is a relationship field.

**Relationship Name**
CalcProcVersion

**Relationship Type**
Lookup

**Refers To**
CalculationProcedureVersion

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The Expression Set Step Relationship name.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the parent Expression Set Step.

This is a relationship field.

**Relationship Name**
ParentCalcProcStep


### Standard Objects CalculatedInsightRangeBound

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
CalculationProcedureStep

```
RelationshipType

```

Associated Objects

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of relationship between the parent and child steps.

Possible values are:

**•** `Bypass` —The parent is a condition step. If the condition is false, the child is the next
step.

**•** `ParentChild` —The child is the next step after the parent.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CalcProcStepRelationshipFeed on page 55**
Feed tracking is available for the object.

**CalcProcStepRelationshipHistory on page 63**
History is available for tracked fields of the object.

### CalculatedInsightRangeBound

Stores the information required to calculate a range-bound data insight. This object is available in API version 59.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available only if a B2B Commerce or D2C Commerce license is enabled.


Standard Objects CalculatedInsightRangeBound

Fields

**Field** **Details**

```
InsightName

LastReferencedDate

LastViewedDate

LowerBoundRange

Name

Operator

```

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Name of the calculated insight.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate) but not
viewed it.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The lower limit of the calculated insight.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The autogenerated name of the insight.

**Type**
picklist


Standard Objects CalculatedInsightRangeBound

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Operation used to calculate the insight based on the upper bound range and lower bound
range.

Possible values are:

**•** `EQUAL_TO`

**•** `GREATER_THAN`

**•** `GREATER_THAN_EQUAL_TO`

**•** `LESS_THAN`

**•** `LESS_THAN_EQUAL_TO`

```
OwnerId

SalesStoreId

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the contact who owns the insight.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the webstore associated with the insight benchmarks.

This field is a relationship field.

**Relationship Name**
SalesStore

**Relationship Type**
Lookup

**Refers To**
WebStore


### Standard Objects CalculationMatrix

**Field** **Details**

```
UpperBoundRange

```

Associated Objects

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The upper limit of the calculated insight.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CalculatedInsightRangeBoundOwnerSharingRule on page 65**
Sharing rules are available for the object.

**CalculatedInsightRangeBoundShare on page 67**
Sharing is available for the object.

### CalculationMatrix

Matches input values to a table row and returns the row's output values. The label for this object is Decision Matrix. This object is available
in API version 53.0 and later.

Decision Matrices are useful for implementing complex rules in a systematic, readable way. There are two types: Standard and Grouped.
A Grouped Decision Matrix groups rows in different versions by one or two keys such as geographic region or product code.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search(), undelete()`, `update()`, `upsert()`

Special Access Rules

Access to Decision Matrices requires Omnistudio licenses.

Fields

**Field** **Details**

```
DecisionMatrixDefinitionId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort


Standard Objects CalculationMatrix

**Field** **Details**

**Description**
The decision matrix definition record associated with this calculation matrix.

This field is a polymorphic relationship field.

**Relationship Name**
DecisionMatrixDefinition

**Relationship Type**
Lookup

**Refers To**
DecisionMatrixDefinition, DecisionTable

```
DecisionMatrixType

Description

GroupKey

LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the type of lookup table.

Possible values are:

**•** `DecisionMatrix`

**•** `DecisionTable`

The default value is `DecisionMatrix` .

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A text description of the Decision Matrix.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A key for grouping matrix rows in different versions, such as geographic region or product
code.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects CalculationMatrix

**Field** **Details**

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

```
LastViewedDate

MigrationStatus

Name

OwnerId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it's possible the user only accessed this record or list view ( `LastReferencedDate` ) but
didn't view it.

**Type**
textarea

**Properties**
Nillable

**Description**
The status of migrating the data from the Calculation Matrix object to the Decision Matrix
Definition object.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The Decision Matrix name.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who currently owns this matrix. Default value is the user logged in to the
API to perform the create action.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


Standard Objects CalculationMatrix

**Field** **Details**

```
SubGroupKey

Type

UniqueName

UsageType

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A subkey for grouping matrix rows in different versions, such as geographic region or product
code. For example, if the `GroupKey` is `Country`, the `SubGroupKey` can be `State`
or `Province` .

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The Decision Matrix type. A Standard Decision Matrix has no special features. A Grouped
Decision Matrix groups rows by one or two keys ( `GroupKey` and `SubGroupKey` ) such
as geographic region or product code.

Possible values are:

**•** `Grouped`

**•** `Standard`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique identifier of the record, which is sourced from the value in the Name field of
CalculationMatrix (decision matrix). For example, if the name of the calculation matrix is
sample matrix, its UniqueName would be sample_matrix.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
A decision matrix’s usage type.

Available in API version 59.0 and later.

Possible value is:

**•** `Bre` -Default


### Standard Objects CalculationMatrixColumn

**Field** **Details**

When Business Rules Engine is enabled on your Salesforce org, the default value is Bre. Other
usage types may be available to you depending on your industry solution and permission
sets.

Usage

Expression Sets, OmniScripts, and Integration Procedures can call Decision Matrices.

### CalculationMatrixColumn

Defines a column in a Decision Matrix. The label for this object is Decision Matrix Column. This object is available in API version 53.0 and
later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Access to Decision Matrices requires Omnistudio licenses.

Fields

**Field** **Details**

```
ApiName

CalculationMatrixId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The API name of the column.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Decision Matrix to which this column belongs.

This is a relationship field.


Standard Objects CalculationMatrixColumn

**Field** **Details**

**Relationship Name**
CalculationMatrix

**Relationship Type**
Lookup

**Refers To**
CalculationMatrix

```
ColumnType

DataType

DisplaySequence

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies whether the column matches matrix input or is returned as output.

Possible values are:

**•** `Input`

**•** `Output`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of data in the column.

Possible values are:

**•** `Boolean`

**•** `Currency`

**•** `Number`

**•** `NumberRange`

**•** `Percent`

**•** `Text`

**•** `TextRange`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The position of this column in the column order.


### Standard Objects CalculationMatrixRow

**Field** **Details**

```
IsWildcardColumn

Name

RangeValues

WildcardColumnValue

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies that this column can contain a wildcard value such as `ALL` .

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The column name.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A list of values that define range boundaries.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The value that indicates a wildcard, for example `ALL` . Applicable if `IsWildcardColumn`
is `true` .

### CalculationMatrixRow

Defines a row in a Decision Matrix. The label for this object is Decision Matrix Row. This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects CalculationMatrixRow

Special Access Rules

Access to Decision Matrices requires Omnistudio licenses.

Fields

**Field** **Details**

```
CalculationMatrixVersionId

EndDateTime

InputData

IsVersionEnabled

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the Decision Matrix Version to which this row belongs.

This is a relationship field.

**Relationship Name**
CalculationMatrixVersion

**Relationship Type**
Lookup

**Refers To**
CalculationMatrixVersion

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The last date on which this row version is active. Applicable if `IsVersionEnabled` is
`true` .

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The input columns and associated values for this row of the matrix.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


### Standard Objects CalculationMatrixVersion

**Field** **Details**

**Description**
Specifies whether the associated matrix version is active. Derived from the associated Decision
Matrix Version (CalculationMatrixVersion object).

The default value is `false` .

```
Name

OutputData

StartDateTime

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The row name.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The output columns and associated values for this row of the matrix.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The first date on which this row version is active. Applicable if `IsVersionEnabled` is
`true` .

### CalculationMatrixVersion

Defines a version of a Decision Matrix. The label for this object is Decision Matrix Version. This object is available in API version 53.0 and
later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Access to Decision Matrices requires Omnistudio licenses.


Standard Objects CalculationMatrixVersion

Fields

**Field** **Details**

```
ApiName

CalculationMatrixId

DecisionMatrixDefinitionVerId

DscnModelNoteExportStatus

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The API name of the decision matrix version. This field is available in API version 56.0 and
later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Decision Matrix to which this version belongs.

This is a relationship field.

**Relationship Name**
CalculationMatrix

**Relationship Type**
Lookup

**Refers To**
CalculationMatrix

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The decision matrix definition version associated with this calculation matrix version.

This field is a relationship field.

**Relationship Name**
DecisionMatrixDefinitionVer

**Relationship Type**
Lookup

**Refers To**
DecisionMatrixDefinitionVersion

**Type**
reference


Standard Objects CalculationMatrixVersion

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Indicates the export status of a decision matrix version in the Decision Model and Notation
(DMN) format.

Possible values are:

**•** `Initiated`

**•** `InProgress`

**•** `Complete`

**•** `Failed`

```
EndDateTime

GroupKey

GroupKeyValue

IsEnabled

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The last date on which this matrix version is active.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A key for grouping matrix rows in different versions, such as geographic region or product
code. Derived from the associated Decision Matrix (CalculationMatrix object).

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The value of the `GroupKey` for this version. For example, if the `GroupKey` is `Country`,
the `GroupKeyValue` can be `United States` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether this version is active.

The default value is `false` .


Standard Objects CalculationMatrixVersion

**Field** **Details**

```
LoadProcessStatus

MatrixType

Name

Rank

StartDateTime

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of a data upload from a `.csv` file.

Possible values are:

**•** `Completed`

**•** `CompletedWithErrors`

**•** `Failed`

**•** `InProgress`

**•** `Pending`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The matrix type, either `Standard` or `Grouped` . A Grouped Decision Matrix groups rows
in different Decision Matrix Versions by one or two keys such as geographic region or product
code. Derived from the associated Decision Matrix (CalculationMatrix object).

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The matrix version name.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
When the invocation time of a matrix call is between the `StartDateTime` and
`EndDateTime` of more than one enabled matrix version, the version with the highest
`Rank` is chosen.

**Type**
dateTime


### Standard Objects CalculationProcedure

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The first date on which this matrix version is active.

```
SubGroupKey

SubGroupKeyValue

VersionNumber

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A subkey for grouping matrix rows in different versions, such as geographic region or product
code. For example, if the `GroupKey` is `Country`, the `SubGroupKey` can be `State`
`or Province` . Derived from the associated Decision Matrix (CalculationMatrix object).

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The value of the `SubGroupKey` for this version. For example, if the `SubGroupKey` is
`State or Province`, the `SubGroupKeyValue` can be `California` .

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The version number.

### CalculationProcedure

Performs a series of calculations using matrix lookups and user-defined variables and constants. The label for this object is Expression
Set. This object is available in API version 53.0 and later.

Note: This object has been deprecated as of API version 55.0. In API version 55.0 and later, use the new Expression Set objects in
Business Rules Engine instead.

Expression Sets accept input variables and return output variables, both in JSON format. Expression Sets are especially useful for determining
prices, rates, and quotes.


Standard Objects CalculationProcedure

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Access to Expression Sets requires OmniStudio licenses.

Fields

**Field** **Details**

```
Description

InputVariablesMetadata

LastReferencedDate

LastViewedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A text description of the Expression Set.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Metadata for the Expression Set's input variables.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it's possible the user only accessed this record or list view ( `LastReferencedDate` ) but
didn't view it.


### Standard Objects CalculationProcedureStep

**Field** **Details**

```
Name

OutputVariablesMetadata

OwnerId

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The Expression Set name.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Metadata for the Expression Set's output variables.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who currently owns this Expression Set. Default value is the user logged
in to the API to perform the create action.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

OmniScripts and Integration Procedures can call Expression Sets. Expression Sets can call Decision Matrices.

### CalculationProcedureStep

Defines a step in an Expression Set. The label for this object is Expression Set Step. This object is available in API version 53.0 and later.

Note: This object has been deprecated as of API version 55.0. In API version 55.0 and later, use the new Expression Set objects in
Business Rules Engine instead.


Standard Objects CalculationProcedureStep

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Access to Expression Sets requires OmniStudio licenses.

Fields

**Field** **Details**

```
CalculationMatrixId

CalculationMatrixType

CalculationProcedure

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Decision Matrix this step calls. Applicable only if the `StepType` is
`MatrixLookup` or `GroupMatrixLookup` .

This is a relationship field.

**Relationship Name**
CalculationMatrix

**Relationship Type**
Lookup

**Refers To**
CalculationMatrix

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of the Decision Matrix this step calls. Applicable only if this step calls a Decision
Matrix. If the `StepType` is `MatrixLookup`, the value of this field is `Standard` . If the
`StepType` is `GroupMatrixLookup`, the value of this field is `Grouped` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Expression Set to which this step belongs.


Standard Objects CalculationProcedureStep

**Field** **Details**

```
CalculationProcedureVersionId

ConditionsConvertedText

ConditionsExpressionText

ConditionsUiFormattedText

Description

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Expression Set Version to which this step belongs.

This is a relationship field.

**Relationship Name**
CalculationProcedureVersion

**Relationship Type**
Lookup

**Refers To**
CalculationProcedureVersion

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The condition expression converted to postfix notation. Applicable only if the `StepType`
is `Condition` .

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The condition expression as the user entered it. Applicable only if the `StepType` is
`Condition` .

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The condition expression converted to JSON format for UI display. Applicable only if the
`StepType` is `Condition` .

**Type**
string


Standard Objects CalculationProcedureStep

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A text description of the Expression Set Step.

```
FormulaConvertedText

FormulaExpressionText

FormulaUiFormattedText

InputVariablesFormatText

IsConditionalStep

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The formula expression converted to postfix notation. Applicable only if the `StepType` is
`Calculation` .

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The formula expression as the user entered it. Applicable only if the `StepType` is
`Calculation` .

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The formula expression converted to JSON format for UI display. Applicable only if the
`StepType` is `Calculation` .

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A list of the input matrix columns or procedure variables applicable to the step.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies that this step is conditional.


Standard Objects CalculationProcedureStep

**Field** **Details**

The default value is `false` .

```
IsResultIncluded

Name

OutputVariablesFormatText

OutputVariablesMappingText

ReferenceProcedureId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies that the result of this step is included in the Expression Set output.

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The step name.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A list of the output matrix columns or procedure variables applicable to the step. Applicable
only if the `StepType` is `MatrixLookup`, `GroupMatrixLookup`, or
`ReferenceProcedure` .

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Maps Decision Matrix output variables to Expression Set variables. Applicable only if the
`StepType` is `MatrixLookup` or `GroupMatrixLookup` .

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the child Expression Set this step calls. Applicable only if the `StepType` is
`ReferenceProcedure` .

This is a relationship field.


Standard Objects CalculationProcedureStep

**Field** **Details**

**Relationship Name**
ReferenceProcedure

**Relationship Type**
Lookup

**Refers To**
CalculationProcedure

```
ReturnMessageValueSet

Stage

StageStepSequence

StepType

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A set of messages to return based on the result of a step with a `StepType` of `Condition` .

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The stage of Expression Set invocation. The `Aggregation` stage applies only to steps
with a `StepType` of `Aggregation` .

Possible values are:

**•** `Aggregation`

**•** `Calculation`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Sequence order of the step within the Expression Set. Used only for Expression Sets migrated
from a Salesforce Industries package. New Expression Sets use Expression Set Step Relationship
objects to order their steps.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of action this step performs.

Possible values are:


### Standard Objects CalculationProcedureVariable

**Field** **Details**

**•** `Aggregation` —Returns an average, maximum, minimum, or sum of a list of values.

### • Calculation —Performs a mathematical operation, which can include variables and

constants.

**•** `Condition` —Defines a condition that determines whether other steps are invoked.

**•** `GroupMatrixLookup` —Calls a Grouped Decision Matrix.

**•** `MatrixLookup` —Calls a Standard Decision Matrix.

**•** `ReferenceProcedure` —Calls a child Expression Set.

### CalculationProcedureVariable

Defines a variable in an Expression Set. The label for this object is Expression Set Variable. This object is available in API version 53.0 and
later.

Note: This object has been deprecated as of API version 55.0. In API version 55.0 and later, use the new Expression Set objects in
Business Rules Engine instead.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Access to Expression Sets requires OmniStudio licenses.

Fields

**Field** **Details**

```
ApiName

CalculationMatrixName

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The API name of this variable.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects CalculationProcedureVariable

**Field** **Details**

**Description**
The name of the Decision Matrix to which this variable belongs. Applicable only if this variable
references a Decision Matrix column.

```
CalculationProcedureVersionId

DataType

DefaultValue

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Expression Set Version to which this variable belongs.

This is a relationship field.

**Relationship Name**
CalculationProcedureVersion

**Relationship Type**
Lookup

**Refers To**
CalculationProcedureVersion

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The data type of this variable.

Possible values are:

**•** `Boolean`

**•** `Currency`

**•** `Date`

**•** `Number`

**•** `Percent`

**•** `Text`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The default value of this variable.


Standard Objects CalculationProcedureVariable

**Field** **Details**

```
DisplayName

IsEditable

IsUserDefined

Name

Precision

UiDisplayOrder

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user-readable name of this variable.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true`, specifies that a variable is NOT auto-imported from a step that calls a Decision
Matrix or a child Expression Set.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether a variable is defined by the user.

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of this variable.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of decimal places. Applicable if the `DataType` is Currency, Number, or Percent.

**Type**
int


### Standard Objects CalculationProcedureVersion

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The display order of the variable in the UI.

### CalculationProcedureVersion

Defines a version of an Expression Set. The label for this object is Expression Set Version. This object is available in API version 53.0 and
later.

Note: This object has been deprecated as of API version 55.0. In API version 55.0 and later, use the new Expression Set objects in
Business Rules Engine instead.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Access to Expression Sets requires OmniStudio licenses.

Fields

**Field** **Details**

```
CalculationProcedureId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Expression Set to which this version belongs.

This is a relationship field.

**Relationship Name**
### CalculationProcedure

**Relationship Type**
Lookup

**Refers To**
### CalculationProcedure


Standard Objects CalculationProcedureVersion

**Field** **Details**

```
Constants

Description

EndDateTime

IsEnabled

IsLoopingEnabled

LastSimulatedVariablesInput

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A serialized JSON object containing information about each constant. This information
includes the name, data type, alias, and precision.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A text description of the Expression Set Version.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The last date on which this Expression Set Version is active.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether this Expression Set Version is active.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether looping is enabled in this Expression Set Version.

The default value is `false` .

**Type**
textarea


Standard Objects CalculationProcedureVersion

**Field** **Details**

**Properties**
Create, Nillable, Update

**Description**
The input variables and results of the most recent simulation.

```
LoopEnd

LoopIncrement

LoopStart

Name

Rank

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the end variable for looping.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the interval variable for looping.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the start variable for looping.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The version name.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
When more than one enabled version matches an Expression Set call, and the
`StartDateTime` to `EndDateTime` spans overlap, the version with the highest `Rank`
is chosen.


### Standard Objects Calendar

**Field** **Details**

```
StartDateTime

VersionNumber

### Calendar

```

**Type**
dateTime

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
The first date on which this Expression Set Version is active.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The version number.

Represents a calendar. This can be a default user calendar, public calendar, resource calendar, or holiday calendar. This object is available
in API version 45.0 and later.

Newly created users are assigned a default calendar automatically. Similarly, holiday calendars are created automatically for each
organization.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`, `search()`

Special Access Rules

Users with "View Setup and Configuration" user permissions can create, edit, and delete public and resource calendars in the user
interface. All users, even those without the “View Setup and Configuration” user permission, can view calendars via the API.

Fields

All fields are readable only.

**Field** **Details**

```
IsActive

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


### Standard Objects CalendarView

**Field** **Details**

**Description**
This field indicates whether a user can save events to the calendar.

```
Name

Type

UserId

### CalendarView

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
A user provided name that identifies the calendar. It is text-indexed for searchability. Note
that this is not an enumerated field; it can be any string to a maximum length of 80 characters.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of the calendar. Possible values are:

**•** `Holiday` (Holiday Calendar)

**•** `Public` (Public Calendar)

**•** `Resource` (Resource Calendar)

**•** `User` (User Calendar)

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user that owns that calendar record. If Type=User, there’s a UserID associated
(foreign key reference to the user). Otherwise, the user field is null.

These calendars can be created and assigned to users other than the creator. Available calendars include object, shared, public, resource,
and user list calendars. Object calendars represent a calendar based on a Salesforce object, either standard or custom. This object is
available in API version 51.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`


Standard Objects CalendarView

Special Access Rules

All fields and entities referenced by field values must be accessible by the CalendarView creator even if the creator isn’t the CalendarView
owner.

Fields

**Field** **Details**

```
Color

CurrencyIsoCode

DateHandlingType

DisplayField

EndField

```

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Represents the color used in the background for records displayed in a user’s calendar view
within the user interface.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for organizations with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Determined by the data type of the `StartField` . Valid values include:

**•** `Date`

**•** `Datetime`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Represents the `SobjectType` field used as the subject for records displayed in a user’s
calendar view within the user interface.

**Type**
string


Standard Objects CalendarView

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An optional field that represents the sObjectType field used as the end time for records
displayed in a user’s calendar view within the user interface. Must be a date or dateTime field
that matches the type in `StartField` .

```
FillPattern

IsDisplayed

ListViewFilterId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the pattern displayed as the background for records displayed in a user’s calendar
view within the user interface. Valid values include:

**•** `verticalStripes`

**•** `ascDiagonalStripes`

**•** `descDiagonalStripes`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Defines whether users can see a calendar’s records in their calendar view in the user interface.
When `true`, records are visible in the user’s calendar view. When `false`, records are
hidden from the user’s calendar view. The default is `true` . `IsDisplayed` can be `true`
for up to 50 calendars.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
References the ListView used to filter records represented by the CalendarView. ListView
must have the same sObjectType. If no `ListViewFilterId` is defined, the calendar
displays only records with the same owner as the CalendarView.

This is a relationship field.

**Relationship Name**
ListViewFilter

**Relationship Type**
Lookup


Standard Objects CalendarView

**Field** **Details**

**Refers To**
ListView

```
Name

OwnerId

PublisherId

SobjectType

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
A user-provided name that identifies the calendar. This isn’t an enumerated field; it can be
any string to a maximum length of 80 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Represents the owner of the CalendarView.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Represents the user, user list, public, or resource calendar from where event data is populated.

This is a polymorphic relationship field.

**Relationship Name**
Publisher

**Relationship Type**
Lookup

**Refers To**
Calendar, ListView, User

**Type**
picklist


Standard Objects CalendarView

**Field** **Details**

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of standard or custom Salesforce object that is used to create records for the
CalendarView. Use the API name of the desired `SobjectType` .

```
StartField

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Represents the `SobjectType` field used as the start time for records displayed in a user’s
calendar view within the user interface. Must be a date or dateTime field type.

To distribute a CalendarView to multiple users, IDs can be pulled from a group, user list, or profile. For this example, a CalendarView
based on opportunity close dates is being distributed to a sales team in a public group, Sales Group:

```
Group userGroup = [SELECT Id FROM Group WHERE Name = 'Sales Group' LIMIT 1];

List<Id> groupId = new List<Id>();

groupId.add(userGroup.id);

List<GroupMember> groupMembers = [SELECT UserOrGroupId FROM GroupMember

  WHERE GroupId IN: groupId];

List<CalendarView> calendarViews = new List<CalendarView>();

for (GroupMember groupMember : groupMembers) {

  CalendarView calendarView = new CalendarView(name = 'Opportunity Close Dates’,

   SobjectType = 'Opportunity', StartField = 'CloseDate', DisplayField =

   'Name', OwnerId = groupMember.UserOrGroupId);

  calendarViews.add(calendarView);

}

insert calendarViews;

```

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CalendarViewChangeEvent (API version 62.0)**
Change events are available for the object.


### Standard Objects CallCenter CallCenter

Represents a call center, which is a logical representation of a single computer-telephony integration (CTI) system instance in an
organization.

Supported Calls

`create()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Customer Portal users can't access this object.

Fields

**Field** **Details**

```
AdapterUrl

CustomSettings

Id

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

An optional field that specifies the location of where the CTI adapter is hosted. For example,
`http://localhost:11000` .

This field is available in API version 23.0 or later.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort

**Description**

Specifies settings in the call center definition file, such as whether the call center uses the
Open CTI, and SoftPhone properties, such as height in pixels.

This field is available for Open CTI and in API version 25.0 or later.

**Type**
ID

**Properties**
Defaulted on create, Filter

**Description**
System field that uniquely identifies this call center. Label is **Call Center ID** . This ID is created
automatically when the call center is created.


### Standard Objects CallCenterRoutingMap

**Field** **Details**

```
InternalName

Name

Version

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**

The internal name of the call center.

Limit is 80 characters.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort

**Description**

The name of the call center.

Limit is 80 characters.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort

**Description**
The version of the CTI Toolkit used to create the call center (for versions 2.0 and later).

This field is available in API version 18.0 and later.

Create a call center or query an existing call center.

### CallCenterRoutingMap

Stores a mapping between a user or queue in a Salesforce org to a user or queue in an external system’s call center. This object is available
in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Access to standard objects requires Salesforce admin privileges or the Customize Application permission.


Standard Objects CallCenterRoutingMap

Access to call center routing map records requires Salesforce Voice Contact Center Admin, Salesforce Voice Contact Center Admin
(Partner Telephony), Salesforce Voice Contact Center Supervisor, or Manage Call Centers permission.

Fields

**Field** **Details**

```
CallCenterId

DeveloperName

ExternalId

Language

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Reference to a call center.

This is a relationship field.

**Relationship Name**
CallCenter

**Relationship Type**
Lookup

**Refers To**
CallCenter

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The developer name is a combination of the Salesforce user ID or queue name, and the call
center ID, with an underscore between these two values.

**•** `[SALESFORCE_USER_ID]_[CALL_CENTER_ID]`

**•** `[SALESFORCE_QUEUE_NAME]_[CALL_CENTER_ID]`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Unique identifier for the external system’s user or queue.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


### Standard Objects CallCoachingMediaProvider

**Field** **Details**

**Description**
The language of the MasterLabel.

```
MasterLabel

QuickConnect

ReferenceRecordId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The master label of the CallCenterRoutingMap.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Amazon Connect QuickConnectId ARN used to determine agent availability for
Omni-Channel call transfers. Available in API version 56.0 and later.

This is a polymorphic relationship field.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Lookup field to a Salesforce user or queue.

This is a polymorphic relationship field.

**Relationship Name**
ReferenceRecord

**Relationship Type**
Lookup

**Refers To**
Group, User

### CallCoachingMediaProvider

Represents the media provider for call recordings. This object is available in API version 49.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


### Standard Objects CallCtrAgentFavTrfrDest

Fields

**Field** **Details**

```
IsActive

ProviderDescription

ProviderName

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Whether the connection with the provider is active or not.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the media provider.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort

**Description**
The name of the media provider.

### CallCtrAgentFavTrfrDest

Represents a transfer destination that has been marked (starred) as a favorite in the Omni-Channel softphone by a contact center agent
for voice call transfers. This object is available in API version 55.0 and later.

To see a list of transfer destinations that have been marked as favorites in the Omni-Channel softphone, add a participant to the call,
click the Phone tab, and select **Favorite** from the Filter dropdown menu. Examples of transfer destination types include agents, contacts,
directories, flows, and queues.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`


Standard Objects CallCtrAgentFavTrfrDest

Fields

**Field** **Details**

```
AgentId

CallCenterId

Name

OwnerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique ID of the contact center agent who marked the transfer destination as a favorite.

This field is a relationship field.

**Relationship Name**
Agent

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique ID of the contact center from where the agent starred the transfer destination
as a favorite.

This field is a relationship field.

**Relationship Name**
CallCenter

**Relationship Type**
Lookup

**Refers To**
CallCenter

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the transfer destination record that’s marked as a favorite.

**Type**
reference


### Standard Objects CallCtrAgentFavTrfrDestShare

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The unique ID of the user who owns this object.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
TransferDestination

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique ID of the transfer destination that’s marked as a favorite. This is an external ID.

### CallCtrAgentFavTrfrDestShare

Represents a sharing entry on a favorite transfer destination in the Omni-Channel softphone for voice call transfers. This object is available
in API version 55.0 and later.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AccessLevel

```

**Type**
picklist


Standard Objects CallCtrAgentFavTrfrDestShare

**Field** **Details**

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The level of access the User or Group has to the transfer destination that’s marked as a favorite.
Possible values are:

**•** `All`                   - Owner

**•** `Edit`                   - Read/Write

**•** `Read`                   - Read Only

```
ParentId

RowCause

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique ID of the parent object.

This field is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
CallCtrAgentFavTrfrDest

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only permitted
value is `Manual` . If no value is specified, the field defaults to `Manual` . All other `RowCause`
values are read-only. After the sharing entry is created, this field can’t be edited.

Possible values are:

**•** `CompliantDataSharing`  - Compliant Data Sharing

**•** `GuestParentImplicit`  - Associated guest user sharing

**•** `GuestPersonImplicit`  - Associated Guest User Sharing

**•** `GuestRule`  - Guest User Sharing Rule

**•** `ImplicitChild`  - Account Sharing

**•** `ImplicitParent`  - Associated record owner or sharing

**•** `ImplicitPerson`  - Person Contact

**•** `LearningAssignment`  - Learning Assignment Share


### Standard Objects CallDisposition

**Field** **Details**

**•** `LearningAssignmentImplicit`                   - Learning Assignment Implicit Share

**•** `LearningItemAssignment`                   - Learning Item Assignment Share

**•** `Manual`                   - Manual Sharing

**•** `MfgTargetShare`                   - Manufacturing Target Sharing Rule

**•** `Owner`

**•** `Rule`                   - Sharing Rule

**•** `SharingRecordCollection`                   - Record Collection

**•** `SurveyShare`                   - Survey Sharing Rule

**•** `Team`                   - Sales Team

**•** `Territory`                   - Territory Assignment Rule

**•** `Territory2AssociationManual`                   - Territory Manual

**•** `Territory2Forecast`                   - Territory assignment for forecasting and reporting

**•** `TerritoryManual`                   - Territory Manual

**•** `TerritoryRule`                   - Territory Sharing Rule

```
UserOrGroupId

### CallDisposition

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique ID of the User or Group that has been given access to the favorite transfer
destination.

This field is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User

Represents a call result value that sales reps select when logging a call. This object is available in API version 47.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


### Standard Objects CallDispositionCategory

Special Access Rules

As of Spring ’20 and later, only your Salesforce org's internal users can access this object.

Fields

**Field** **Details**

```
Disposition

DispositionCategoryId

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The result of a phone call, such as whether a call was connected or the rep left a voicemail.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The related call outcome that is used in reports and branching criteria for cadences.

### CallDispositionCategory

Represents the call outcome of a phone call that is used in reports and branching criteria for cadences. This object is available in API
version 47.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

As of Spring ’20 and later, only your Salesforce org's internal users can access this object.

Fields

**Field** **Details**

```
Category

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort


Standard Objects CallDispositionCategory

**Field** **Details**

**Description**
The name of the call outcome.

```
DeveloperName

Language

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the call category.

Possible values are:

**•** `da` —Danish

**•** `de` —German

**•** `en_US` —English

**•** `es` —Spanish

**•** `es_MX` —Spanish (Mexico)

**•** `fi` —Finnish

**•** `fr` —French

**•** `it` —Italian

**•** `ja` —Japanese

**•** `ko` —Korean

**•** `nl_NL` —Dutch

**•** `no` —Norwegian

**•** `pt_BR` —Portuguese (Brazil)

**•** `ru` —Russian

**•** `sv` —Swedish

**•** `th` —Thai


### Standard Objects CallTemplate

**Field** **Details**

**•** `zh_CN` —Chinese (Simplified)

**•** `zh_TW` —Chinese (Traditional)

```
 MasterLabel

### CallTemplate

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The static name of the call outcome.

Represents a call script for users to read when making calls.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
Description

HtmlBody

LastReferencedDate

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The description of the call script.

**Type**
textarea

**Properties**
Nillable

**Description**
The body content of the call script.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects CallTemplate

**Field** **Details**

**Description**
The time stamp that indicates when the current user last viewed a record that is related to
this CallTemplate.

```
LastViewedDate

Name

OwnerId

TemplateType

TotalCalls

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time stamp that indicates when the current user last viewed this CallTemplate. If this
value is null, this record might have been only referenced ( `LastReferencedDate` ) and
not viewed.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the call script.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user who owns the call script.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of call template.

Possible values are:

**•** `Text`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects CallTemplate

**Field** **Details**

**Description**
The total number of calls that use the CallTemplate.

```
TotalCallsCallBackLater

TotalCallsLeftVoicemail

TotalCallsMeaningfulConnect

TotalCallsNotInterested

TotalCallsUncategorized

TotalCallsUnqualified

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total Call Back Later call results that use the CallTemplate.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total Left Voicemail call results that use the CallTemplate.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total Meaningful Connect call results that use the CallTemplate.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total Not Interested call results that use the CallTemplate.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total uncategorized call results that use the CallTemplate.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects Campaign

**Field** **Details**

**Description**
The total Unqualified call results that use the CallTemplate.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CallTemplateChangeEvent (API version 48.0)**
Change events are available for the object.

### Campaign

Represents and tracks a marketing campaign, such as a direct mail promotion, webinar, or trade show.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`

Special Access Rules

Customer Portal users can't access this object.

Fields

**Field** **Details**

```
ActualCost

AmountAllOpportunities

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount of money spent to run the campaign. Label is Actual Cost in Campaign.

**Type**
currency

**Properties**
Filter, Sort

**Description**
Amount of money in all opportunities associated with the campaign, including closed/won
opportunities. Label is Value Opportunities in Campaign.


Standard Objects Campaign

**Field** **Details**

```
AmountWonOpportunities

BriefId

BudgetedCost

CampaignImageId

CampaignMemberRecordTypeId

```

**Type**
currency

**Properties**
Filter, Sort

**Description**
Amount of money in closed or won opportunities associated with the campaign. Label is
Value Won Opportunities in Campaign.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the brief that's associated with the campaign. A brief contains additional context
about the goals and audience for the campaign. The label is Brief.

**Relationship Name**
Brief

**Relationship Type**
Lookup

**Refers To**
Record

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of money budgeted for the campaign. Label is Budgeted Cost in Campaign.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the campaign image. Available in API version 42.0 and later. Only available to orgs with
Partner Community licenses and Digital Experience enabled or orgs that have installed the
Direct Marketing Managed package.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects Campaign

**Field** **Details**

**Description**
The record type ID for CampaignMember records associated with the campaign.

This is a relationship field.

**Relationship Name**
CampaignMemberRecordType

**Relationship Type**
Lookup

**Refers To**
RecordType

```
CampaignStage

CreatedByID

CurrencyIsoCode

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
This field is available with Marketing Cloud Growth and Advanced editions. The lifecycle
stage of the campaign based on the status of all of its related flows. Possible values are:

**•** In Planning

**•** In Progress

**•** Completed

**•** Error

**•** Canceled

**•** Paused

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who created the campaign.

This is a relationship field.

**Relationship Name**
Creator

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist


Standard Objects Campaign

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for organizations with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

```
Description

EndDate

ExpectedResponse

ExpectedRevenue

HierarchyActualCost

```

**Type**
textarea

**Properties**
Nillable

**Description**
Description of the campaign. Limit: 32 KB. Only the first 255 characters display in reports.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Ending date for the campaign. Responses received after this date are still counted.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
Percentage of responses you expect to receive for the campaign.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of money you expect to generate from the campaign.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Calculated field for the total amount of money spent to run the campaigns in a campaign
hierarchy. Label is Total Actual Cost in Hierarchy.


Standard Objects Campaign

**Field** **Details**

```
HierarchyAmountAllOpportunities

HierarchyAmountWonOpportunities

HierarchyBudgetedCost

HierarchyExpectedRevenue

HierarchyNumberOfContacts

HierarchyNumberOfConvertedLeads

```

**Type**
currency

**Properties**
Filter, Sort

**Description**
Amount of money in all opportunities associated with the campaign in a campaign hierarchy,
including closed/won opportunities. Label is Value Opportunities in Hierarchy.

**Type**
currency

**Properties**
Filter, Sort

**Description**
The amount of money in closed or won opportunities associated with the campaign in a
campaign hierarchy. Label is Value Won Opportunities in Hierarchy.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Calculated field for the total amount of money budgeted for the campaigns in a campaign
hierarchy. Label isTotal Budgeted Cost in Hierarchy.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Calculated field for the total amount of money you expect to generate from the campaign
in a campaign hierarchy. Label is Total Expected Revenue in Hierarchy.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for the number of contacts associated with the campaign hierarchy. Label
is Total Contacts in Hierarchy.

**Type**
currency


Standard Objects Campaign

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
Calculated field for the number of converted leads from the campaign in a campaign
hierarchy. Label is Converted Leads in Hierarchy.

```
HierarchyNumberOfLeads

HierarchyNumberOfOpportunities

HierarchyNumberOfResponses

HierarchyNumberOfWonOpportunities

HierarchyNumberSent

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Calculated field for the number of leads from the campaign in a campaign hierarchy. Label
is Leads in Hierarchy.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Calculated field for the number of opportunities related to the campaign in a campaign
hierarchy. Label is Opportunities in Hierarchy.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Number of contacts and unconverted leads with a Member Status equivalent to “Responded”
for the campaign in a campaign hierarchy. Label is **Responses in Hierarchy** .

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of closed or won opportunities associated with the campaign. Label is Won
Opportunities in Hierarchy.

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects Campaign

**Field** **Details**

**Description**
Calculated field for the total number of individuals targeted by the campaign in a campaign
hierarchy. For example, the number of email messages sent. The label is Num Sent in
Hierarchy.

```
HierarchyTotalEmailsDelivered

HierarchyTotalFormSubmissions

HierarchyTotalFormViews

HierarchyTotalLandingPageFormSubmissions

HierarchyTotalLandingPageViews

```

**Type**
int

**Properties**
Filter

**Description**
Calculated field for emails delivered related to the campaign in a campaign hierarchy. Label
is Total Emails Delivered in Hierarchy. This field is available with Marketing Cloud Account
Engagement.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for form submissions related to the campaign in a campaign hierarchy. Label
is Total Form Submissions in Hierarchy. This field is available with Marketing Cloud Account
Engagement.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for form views related to the campaign in a campaign hierarchy. Label is
Total Form Views in Hierarchy. This field is available with Marketing Cloud Account
Engagement.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for form submissions from a landing page related to the campaign in a
campaign hierarchy. Label is Total Landing Page Form Submissions in Hierarchy. This field
is available with Marketing Cloud Account Engagement.

**Type**
int


Standard Objects Campaign

**Field** **Details**

**Properties**
Filter

**Description**
Calculated field for landing page views related to the campaign in a campaign hierarchy.
Label is Total Landing Page Views in Hierarchy. This field is available with Marketing Cloud
Account Engagement.

```
HierarchyUniqueEmailOpens

HierarchyUniqueEmailTrackedLinkClicks

HierarchyUniqueMarketingLinkClicks

IsActive

```

**Type**
int

**Properties**
Filter

**Description**
Calculated field for email opens related to the campaign in a campaign hierarchy. Excludes
repeat opens. Label is Unique Email Opens in Hierarchy. This field is available with Marketing
Cloud Account Engagement.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for unique email link clicks related to the campaign in a campaign hierarchy.
Excludes repeat clicks. Label is Unique Email Clicks in Hierarchy. This field is available with
Marketing Cloud Account Engagement.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for unique marketing link clicks related to the campaign in a campaign
hierarchy. Excludes repeat clicks. Label is Unique Marketing Link Clicks in Hierarchy. This field
is available with Marketing Cloud Account Engagement.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this campaign is active ( `true` ) or not ( `false` ). The default value is
`false` . The label is **Active** .


Standard Objects Campaign

**Field** **Details**

```
LastActivityDate

LastModifiedById

LastReferencedDate

LastViewedDate

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Value is one of the following, whichever is the most recent:

**•** The due date of the most recent event logged against the record.

**•** The due date of the most recently closed task associated with the record.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who last updated the campaign.

This is a relationship field.

**Relationship Name**
Last Modified

**Relationship Type**
Lookup

**Refers To**
User

**Type**
datetime

**Properties**
Filter, Nillable, Sort,

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
datetime

**Properties**
Filter, Nillable, Sort,

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view ( `LastReferencedDate` ) but
not viewed it.


Standard Objects Campaign

**Field** **Details**

```
Name

NumberOfContacts

NumberOfConvertedLeads

NumberOfLeads

NumberOfOpportunities

NumberOfResponses

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Required. Name of the campaign. Limit: is 80 characters.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Number of contacts associated with the campaign. Label is Total Contacts.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Number of leads that were converted to an account and contact due to the marketing efforts
in the campaign. Label is Converted Leads.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of leads associated with the campaign. Label is Leads in Campaign.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of opportunities associated with the campaign. Label is Opportunities in
Campaign.

**Type**
int

**Properties**
Filter, Group, Sort


Standard Objects Campaign

**Field** **Details**

**Description**
The number of contacts and unconverted leads with a Member Status equivalent to
“Responded” for the campaign. Label is Responses in Campaign.

```
NumberOfWonOpportunities

NumberSent

OwnerId

ParentCampaign

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of closed or won opportunities associated with the campaign. Label is Won
Opportunities in Campaign.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of individuals targeted by the campaign. For example, the number of emails
sent. Label is Num Sent.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who owns this campaign. Default value is the user logging in to the API to
perform the create.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
The campaign above the selected campaign in the campaign hierarchy.


Standard Objects Campaign

**Field** **Details**

```
ParentId

RecordTypeId

StartDate

Status

TenantId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

ID of the parent Campaign record, if any.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Campaign

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the record type assigned to this object.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Starting date for the campaign.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Status of the campaign, for example, Planned, In Progress. Limit: 40 characters.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects Campaign

**Field** **Details**

**Description**
ID of the associated Marketing Cloud Account Engagement business unit. Read-only. Available
with Marketing Cloud Account Engagement in API version 51.0 and later.

This is a relationship field.

**Relationship Name**
Business Unit

**Relationship Type**
Lookup

**Refers To**
PardotTenant

```
TotalAmountAllOpportunities

TotalAmountAllWonOpportunities

TotalEmailsDelivered

TotalFormSubmissions

```

**Type**
currency

**Properties**
Filter

**Description**
Calculated field for total amount of all opportunities associated with the campaign hierarchy,
including closed/won opportunities. Label is Total Value Opportunities in Hierarchy.

**Type**
currency

**Properties**
Filter

**Description**
Calculated field for amount of all closed/won opportunities associated with the campaign
hierarchy. Label is Total Value Won Opportunities in Hierarchy.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for emails delivered related to the campaign. Label is Total Emails Delivered
in Campaign. This field is available with Marketing Cloud Account Engagement.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for form submissions related to the campaign. Label is Total Form Submissions
in Campaign. This field is available with Marketing Cloud Account Engagement.


Standard Objects Campaign

**Field** **Details**

```
TotalFormViews

TotalLandingPageFormSubmissions

TotalLandingPageViews

TotalNumberofLeads

TotalNumberofOpportunities

```

**Type**
int

**Properties**
Filter

**Description**
Calculated field for form views related to the campaign. Label is Total Form Views in Campaign.
This field is available with Marketing Cloud Account Engagement.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for form submissions from a landing page related to the campaign. Label is
Total Landing Page Form Submissions in Campaign. This field is available with Marketing
Cloud Account Engagement.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for landing page views related to the campaign. Label is Total Landing Page
Views in Campaign. This field is available with Marketing Cloud Account Engagement.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for total number of leads associated with the campaign hierarchy. This
number also includes converted leads. Label is Total Leads in Hierarchy.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for the total number of opportunities associated with the campaign hierarchy.
Label is Total Opportunities in Hierarchy.


Standard Objects Campaign

**Field** **Details**

```
TotalNumberofResponses

TotalNumberofWonOpportunities

Type

UniqueEmailOpens

UniqueEmailTrackedLinkClicks

```

**Type**
int

**Properties**
Filter

**Description**
Calculated field for number of contacts and unconverted leads that have a `Member`
`Status` equivalent to “Responded” for the campaign hierarchy. Label is Total Responses
in Hierarchy.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for the total number of won opportunities associated with the campaign
hierarchy. Label is Total Won Opportunities in Hierarchy.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Type of campaign, for example, Direct Mail or Referral Program. Limit: 40 characters.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for email opens related to the campaign. Excludes repeat opens. Label is
Unique Email Opens in Campaign. This field is available with Marketing Cloud Account
Engagement.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for unique email link clicks related to the campaign. Excludes repeat clicks.
Label is Unique Email Clicks in Campaign. This field is available with Marketing Cloud Account
Engagement.


### Standard Objects CampaignInfluence

**Field** **Details**

```
UniqueMarketingLinkClicks

```

Usage

**Type**
int

**Properties**
Filter

**Description**
Calculated field for unique marketing link clicks related to the campaign. Excludes repeat
clicks. Label is Unique Marketing Link Clicks in Campaign. This field is available with Marketing
Cloud Account Engagement.

Client applications can create, update, delete, and query Attachment records associated with a campaign via the API.

The Campaign object is defined only for those organizations that have the marketing feature enabled and valid marketing licenses. In
addition, it is accessible only to those users that are enabled as marketing users. If the organization does not have the marketing feature
or valid marketing licenses, this object does not appear in the `describeGlobal()` call, and you can’t use `describeSObjects()`
or `query()` with the Campaign object.

Note: The main constituent of a campaign is a CampaignMember. You will commonly need to update campaigns with
CampaignMember.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**CampaignChangeEvent (API version 44.0)**
Change events are available for the object.

**CampaignFeed (API version 18.0)**
Feed tracking is available for the object.

**CampaignHistory (API version 40.0)**
History is available for tracked fields of the object.

**CampaignOwnerSharingRule**

Sharing rules are available for the object.

**CampaignShare**

Sharing is available for the object.

SEE ALSO:

Overview of Salesforce Objects and Fields

### CampaignInfluence

Represents the association between a campaign and an opportunity in Customizable Campaign Influence. This object is available in API
version 37.0 and later.


Standard Objects CampaignInfluence

[Note: This information applies only to Customizable Campaign Influence and not to Campaign Influence 1.0 .](https://help.salesforce.com/s/articleView?id=sf.campaigns_influence_original.htm&language=en_US)

[To ingest this object in Data Cloud, set up the Data Cloud Salesforce Connector permission set. See Enable Object and Field Permissions](https://help.salesforce.com/s/articleView?id=data.c360_a_crm_enable_object_and_field_permissions.htm&type=5&language=en_US)
[for CRM Connections.](https://help.salesforce.com/s/articleView?id=data.c360_a_crm_enable_object_and_field_permissions.htm&type=5&language=en_US)

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

To access this object, Customizable Campaign Influence must be enabled. Customer Portal users can’t access this object.

Fields

**Field Name** **Details**

```
CampaignId

CampaignMemberId

ContactId

Influence

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the campaign that’s related to the opportunity.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the campaign member related to the opportunity. Not available in the
UI.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The ID of the contact on the associated opportunity.

**Type**
percent

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update


Standard Objects CampaignInfluence

**Field Name** **Details**

**Description**

The percentage of the Amount field for the related opportunity that’s attributed
to the campaign.

```
ModelId

OpportunityContactRoleId

OpportunityId

RevenueShare

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the campaign influence model that’s related to the record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The opportunity contact role ID of the related opportunity. Not available in the
UI.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the related opportunity.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount of revenue from the related opportunity attributed to the campaign.

Use this object to create campaign influence records for your custom campaign influence models. Don’t create campaign influence
records for the Primary Campaign Source model. Records added to the Primary Campaign Source model via the API are deleted when
the model is recalculated.


### Standard Objects CampaignInfluenceModel CampaignInfluenceModel

This read-only object represents a campaign influence model in Customizable Campaign Influence. Use campaign influence models to
### group CampaignInfluence records created by a specific set of triggers and workflows that you define. The Primary Campaign

Source influence model is the default model. This object is available in API version 37.0 and later.

[Note: This information applies only to Customizable Campaign Influence and not to Campaign Influence 1.0.](https://help.salesforce.com/s/articleView?id=sales.campaigns_influence_customizable.htm&type=5&language=en_US)

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

To access this object, Customizable Campaign Influence must be enabled. Customer Portal users can’t access this object.

Fields

**Field Name** **Details**

```
DeveloperName

IsActive

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The API name of the influence model. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming
conflicts on package installations. With this field, a developer can change the
object’s name in a managed package and the changes are reflected in a
subscriber’s organization.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the model is active. Active models can generate campaign
influence records. Deactivating a model deletes its campaign influence records.
Custom models are always active and this field is ignored.


Standard Objects CampaignInfluenceModel

**Field Name** **Details**

```
IsDefaultModel

IsModelLocked

Language

MasterLabel

ModelDescription

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the model is the default model ( `true` ) or not ( `false` ).
`CampaignInfluence` records associated with the default model appear in
3 locations.

**•** The Campaign Influence related list on opportunities

**•** The Influenced Opportunities related list on campaigns

**•** The Campaign Statistics section on campaigns

The value of `IsDefaultModel` can only be true for 1 model at a time.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the model is locked ( `true` ) or not ( `false` ). Records for locked
models can only be added, updated, or deleted via the API.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the influence model.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label for the influence model.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The description of the influence model.


Standard Objects CampaignInfluenceModel

**Field Name** **Details**

```
ModelType

NamespacePrefix

RecordPreference

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates whether the model is the Primary Campaign Source influence model,
or a custom model. These values are the allowed.

**•** 1: Primary Campaign Source Model

**•** 2: Custom Model

**•** 3: First Touch Model

**•** 4: Last Touch Model

**•** 5: Even Distribution Model

**•** 6: Data-Driven Model

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition
org that creates a managed package has a unique namespace prefix. Limit: 15
characters. You can refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace
prefix of the org for all objects that support it, unless an object is in an installed
managed package. In that case, the object has the namespace prefix of the
installed managed package. This field’s value is the namespace prefix of the
Developer Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set
only for objects that are part of an installed managed package. All other
objects have no namespace prefix.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The value of this field determines when to create campaign influence records.

**•** AllRecords: Creates records regardless of the revenue attribution percentage.


### Standard Objects CampaignMember

**Field Name** **Details**

**•** RecordsWithAttribution: Creates records only when the revenue attribution
is greater than 0%.

### CampaignMember

The CampaignMember object represents the relationship between a campaign and either a lead or a contact. If the Accounts as Campaign
Members setting is enabled in an org, CampaignMember can also represent the relationship between a campaign and an account.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

Customer Portal users can’t access this object.

Fields

**Field** **Details**

```
AccountId

CampaignId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the account related to the campaign. This field is available only if the Accounts as
Campaign Members setting is enabled in the org.

This field is a relationship field.

**Relationship Name**
Related Record ID

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Create, Filter, Group, Sort


Standard Objects CampaignMember

**Field** **Details**

**Description**
Required. The ID of the campaign related to the lead or contact.

This field is a relationship field.

**Relationship Name**
Campaign

**Relationship Type**
Lookup

**Refers To**
Campaign

```
City

CompanyOrAccount

ContactId

CurrencyIsoCode

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The city for the address of the lead or contact. In orgs with the Accounts as Campaign
Members setting enabled, this field can be the city for the account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The company or account of the lead or contact.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Required. The ID of a contact that's related to the campaign.

This field is a relationship field.

**Relationship Name**
Contact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
picklist


Standard Objects CampaignMember

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for organizations with the multicurrency feature enabled. This field contains
the ISO code for any currency allowed by the organization.

```
Country

Description

DoNotCall

Email

Fax

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The country for the address of the lead or contact. In orgs with the Accounts as Campaign
Members setting enabled, this field can be the country for the account.

**Type**
textarea

**Properties**
Nillable

**Description**
The description of the associated lead or contact. In orgs with the Accounts as Campaign
Members setting enabled, this field can be the description of the account.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates that the lead or contact doesn’t want to be called. In orgs with the Accounts as
Campaign Members setting enabled, this field can indicate the account doesn’t want to be
called.

**Type**
email

**Properties**
Filter, Group, Nillable, Sort

**Description**
Email address for the lead or contact. In orgs with the Accounts as Campaign Members
setting enabled, this field can be the email address for the account.

**Type**
phone


Standard Objects CampaignMember

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Fax number for the lead or contact. In orgs with the Accounts as Campaign Members setting
enabled, this field can be the fax number for the account.

```
FirstName

FirstRespondedDate

HasOptedOutOfEmail

HasOptedOutOfFax

HasResponded

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The first name of the lead or contact.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field indicates the date that the campaign member received a status of Responded.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
This field indicates the email opt-out preference for the lead or contact. A value of `false`
indicates that the lead or contact is opted in to emails. A value of `true` indicates that they’re
opted out. In orgs with the Accounts as Campaign Members setting enabled, this field can
be the opt-out preference for the account email address.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
This field indicates the fax opt-out preferences for the lead or contact. A value of false indicates
that the lead or contact is opted in to receiving faxes. A value of true indicates that they’re
opted out. In orgs with the Accounts as Campaign Members setting enabled, this field can
indicate the account has opted out of faxes.

**Type**
boolean


Standard Objects CampaignMember

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
This field indicates whether the campaign member has responded to the campaign ( `true` )
or not ( `false` ). Label is **Responded** .

```
LastName

LeadId

LeadOrContactId

LeadOrContactOwnerId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The last name of the lead or contact. The limit is 80 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Required. The ID of a lead that's related to the campaign.

This field is a relationship field.

**Relationship Name**
Lead

**Relationship Type**
Lookup

**Refers To**
Lead

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The ID of a lead or contact that's related to the campaign. In orgs with the Accounts as
Campaign Members setting enabled, this field also accepts an account ID.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects CampaignMember

**Field** **Details**

**Description**
The ID of the owner of the associated lead or contact owner. In orgs with the Accounts as
Campaign Members setting enabled, this field can be the owner of the account.

This field is a polymorphic relationship field.

**Relationship Name**
LeadOrContactOwner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
LeadSource

MobilePhone

Name

Phone

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
The source where the lead was obtained.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
The mobile phone number of the lead or contact. In orgs with the Accounts as Campaign
Members setting enabled, this field can be the mobile phone number for the account.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The first and last name of the lead or contact that's related to the campaign member.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
The phone number of the lead or contact. In orgs with the Accounts as Campaign Members
setting enabled, this field can be the phone number for the account.


Standard Objects CampaignMember

**Field** **Details**

```
PostalCode

RecordTypeId

Salutation

State

Status

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The postal code for the lead or contact. In orgs with the Accounts as Campaign Members
setting enabled, this field can be the postal code for the account.

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the record type assigned to this object. To change the record type, modify the
`CampaignMemberRecordTypeId` field on the associated Campaign.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
Salutation for the lead or contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The state for the address of the lead or contact. The limit is 80 characters. In orgs with the
Accounts as Campaign Members setting enabled, this field can be the state of the account
address.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Controls the `HasResponded` flag on this object. You can't directly set the
`HasResponded` flag, as it’s read-only. You can set it indirectly by setting this field in a
create or update call. Each predefined value implies a `HasResponded` flag value. Each
time you update this field, you implicitly update the `HasResponded` flag. In the Salesforce
user interface, Marketing users can define valid status values for the `Status` picklist. They


Standard Objects CampaignMember

**Field** **Details**

can choose one status as the default status. For each `Status` field value, they can also
select which values to count as “Responded,” meaning that the `HasResponded` flag is
set to `true` for those values. The limit is 40 characters.

When you create or update campaign members, use the text value for `Status` instead of
the ID from the CampaignMemberStatus object.

```
Street

Title

Type

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The street for the address of the lead or contact. In orgs with the Accounts as Campaign
Members setting enabled, this field can be the street of the account address.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Title for the lead or contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates if the campaign member is a lead or a contact. In orgs with the Accounts as
Campaign Members setting enabled, this field can indicate an account.

Note: If you’re importing CampaignMember data into Salesforce and want to set the value for an audit field, such as
`CreatedDate`, contact Salesforce. Audit fields are automatically updated during API operations unless you request to set these
fields yourself.

Usage

Each record has a unique ID, and must contain either a `ContactId` or a `LeadId`, but can't contain both. Any attempt to create a
single record with both results in a successful insert but only the `ContactId` is inserted. However, you can create two separate records
on a Campaign—one for the Lead and one for the Contact.

In orgs with the Accounts as Campaign Members setting enabled, the unique ID can be an `AccountID` .


### Standard Objects CampaignMemberStatus

Standard fields from a lead or contact are associated with the CampaignMember object, but you can’t query them directly. To include
a `Phone` in your query, for example, query the field from the Lead object.

```
   SELECT Id, (SELECT Phone FROM Lead)

   FROM CampaignMember

```

This object is defined only for orgs that have the marketing feature and valid marketing licenses. If your org doesn’t have the marketing
feature or valid marketing licenses, this object doesn’t appear in the `describeGlobal()` call, and you can't use
`describeSObjects()` or `query()` with this object.

Note: If you want to track lead-based campaign members you convert to contacts, provide both a ContactId and a LeadId.
Otherwise, only use one ID type.

To issue `create()` requests to the API, your account only requires read access to campaigns.

If the record doesn’t exist for the specified `ContactId` or `LeadId`, then a new record is created. If the record exists, an error is
returned and no update is made. To update an existing record, specify the ID of the CampaignMember record to update.

To delete a record, specify the ID of the CampaignMember record.

When creating or updating records, the `Status` field value specified in the call is verified as a valid status for the given Campaign:

**•** If the specified `Status` value is a valid status, the value is updated, and the `HasResponded` field is updated to either `true`
or `false`, depending on the `Status` value association with `HasResponded` .

**•** If the specified `Status` value isn’t a valid status, the API assigns the default status to the `Status` field and updates the
`HasResponded` field with the associated value. However, if the given Campaign doesn’t have a default status, the API assigns
the value specified in the call to the `Status` field, and the `HasResponded` field is set to `false` .

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CampaignMemberChangeEvent (API version 46.0)**
Change events are available for the object.

SEE ALSO:

### Campaign CampaignMemberStatus CampaignMemberStatus

One or more member status values defined for a campaign.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Customer Portal users can't access this object.


Standard Objects CampaignMemberStatus

You can't delete a CampaignMemberStatus if that status is designated as the default status or if the status is currently used in a Campaign.

Fields

**Field** **Details**

```
CampaignId

HasResponded

IsDefault

IsDeleted

Label

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the campaign associated with this member status.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this status is equivalent to “Responded” ( `true` ) or not ( `false` ). Beginning
with API version 39.0, at least one `CampaignMemberStatus` on each campaign must
have a `hasResponded` value of `true` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this status is the default status ( `true` ) or not ( `false` ). Beginning with
API version 39.0, there must be a default CampaignMemberStatus defined for every campaign.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

**Type**
string

**Properties**
Filter, Sort

**Description**
Label for the status in the picklist. Limited to 765 characters.


### Standard Objects CampaignOwnerSharingRule

**Field** **Details**

```
 SortOrder

```

Usage

**Type**
int

**Properties**
Filter, Group, Sort, Update

**Description**
Unique number order where this campaign member status appears in the picklist.

Use this object to create picklist items for the member status in a campaign.

This object is defined only for those organizations that have the marketing feature and valid marketing licenses. In addition, the object
is accessible only to those users that are enabled as marketing users. If the organization does not have the marketing feature or valid
marketing licenses, this object does not appear in a `describeGlobal()` call, and you can't use `describeSObjects()` or
`query()` with the CampaignMember object.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CampaignMemberStatusChangeEvent (API version 46.0)**
Change events are available for the object.

SEE ALSO:

### Campaign

CampaignMember

### CampaignOwnerSharingRule

Represents the rules for sharing a campaign with User records other than the owner or anyone above the owner in the role hierarchy.

Note: To enable access to this object for your org, contact Salesforce customer support. However, we recommend that you
instead use Metadata API to programmatically update owner sharing rules because it triggers automatic sharing rule recalculation.
[The SharingRules Metadata API type is enabled for all orgs.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_sharingrules.htm)

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
upsert()

```


Standard Objects CampaignOwnerSharingRule

Fields

**Field** **Details**

```
CampaignAccessLevel

Description

DeveloperName

GroupId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the type of access granted to the target Group, or UserRole. The
possible values are:

**•** `Read`

**•** `Edit`

**•** `All`

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A description of the sharing rule. Maximum size is 1000 characters. This field is available in
API version 29.0 and later.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization. Corresponds to **Rule Name** in the user interface.

This field is available in API version 24.0 and later.

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance may slow while
Salesforce generates one for each record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects CampaignShare

**Field** **Details**

**Description**
The ID representing the source group. A Campaign owned by a User in the source Group
triggers the rule to give access.

```
Name

UserOrGroupId

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label of the sharing rule as it appears in the user interface. Limited to 80 characters.
Corresponds to **Label** on the user interface.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the User or Group being granted access.

Use this object to manage the sharing rules for campaigns.

SEE ALSO:

_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_sharingrules.htm)_ : SharingRules

### CampaignShare

Represents a sharing entry on a Campaign.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects CampaignShare

Special Access Rules

As of Summer ’20 and later, only users with access to the Campaign object can access this object.

Fields

The properties available for some fields depend on the default organization-wide sharing settings. The properties listed are true for the
default settings of such fields.

**Field** **Details**

```
CampaignId

CampaignAccessLevel

RowCause

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the Campaign associated with this sharing entry. This field can't be updated.

This is a relationship field.

**Relationship Name**
Campaign

**Relationship Type**
Lookup

**Refers To**
Campaign

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Level of access that the User or Group has to the Campaign. The possible values are:

**•** `Read`

**•** `Edit`

**•** `All` (This value is not valid for creating or updating records.)

This field must be set to an access level that is higher than the organization’s default access
level for Campaign.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort


### Standard Objects CampaignTag

**Field** **Details**

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only permitted
value is `Manual` . If no value is specified, the field defaults to `Manual` . All other `RowCause`
values are read-only. After the sharing entry is created, this field can’t be edited.

Valid values:

**•** `Rule` —The User or Group has access via a Campaign sharing rule.

**•** `GuestRule` —The User or Group has access via a Campaign guest user sharing rule.

**•** `Manual` —The User or Group has access because a User with “ `All` ” access manually
shared the Campaign with them.

**•** `Owner` —The User is the owner of the Campaign.

**•** `LpuImplicit` —The User has access to records owned by high-volume Experience
Cloud site users via a share group.

**•** `ARImplicit` —The User, who belongs to a partner or customer account, has access
to the Campaign via an account relationship data sharing rule.

```
 UserOrGroupId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the User or Group that has been given access to the Campaign. This field can't be
updated.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User

This object allows you to determine which users and groups can view or edit Campaign records owned by other users.

### CampaignTag

Associates a word or short phrase with a Campaign.


Standard Objects CampaignTag

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
ItemId

Name

TagDefinitionId

Type

```

**Type**
reference

**Properties**
Create, Filter

**Description**
ID of the tagged item.

**Type**
string

**Properties**
Create, Filter

**Description**
Name of the tag. If this value does not already exist, a new TagDefinition is created and
becomes the parent of this Tag object. Otherwise, a TagDefinition with the same name
becomes the parent of this Tag object. Parent relationships are created automatically.

**Type**
reference

**Properties**
Filter

**Description**
ID of the parent TagDefinition object that owns the tag.

**Type**
picklist

**Properties**
Create, Filter, Restricted picklist

**Description**
Defines the visibility of a tag.

Valid values:

**•** `Public` —The tag can be viewed and manipulated by all users in an organization.

**•** `Personal` —The tag can be viewed or manipulated only by a user with a matching
`OwnerId` .


### Standard Objects CardPaymentMethod

Usage

CampaignTag stores the relationship between its parent TagDefinition and the Campaign being tagged. Tag objects act as metadata,
allowing users to describe and organize their data.

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.

### CardPaymentMethod

Represents a credit card or debit card payment method, which implements the PaymentMethod object. This object is available in API
version 48.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access Salesforce Payments objects with the API, your org must have one or more of these licenses: Salesforce Payments, Salesforce
Order Management, B2B Commerce, or D2C Commerce. Salesforce Payments objects are available only in Lightning Experience.

Fields

**Field** **Details**

```
AccountId

AuditEmail

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Customer account for the payment method.

This field is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects CardPaymentMethod

**Field** **Details**

**Description**
Email address of the card owner where audit information about payments gets sent.

This field is available in API v49.0 and later. It doesn’t appear in the UI by default for orgs that
upgraded from v48.0. Users must add it to the CardPaymentMethod page layout on their
own.

```
AutoCardType

CardBin

CardCategory

CardHolderFirstName

CardHolderLastName

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Card network type, derived from the card number.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
First six digits of the card number.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Defines whether the card is a credit card or debit card.

Possible values are:

**•** `CreditCard`

**•** `DebitCard`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
First name of the cardholder.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects CardPaymentMethod

**Field** **Details**

**Description**
Last name of the cardholder.

```
CardHolderName

CardLastFour

CardPaymentMethodNumber

CardType

CardTypeCategory

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Full name of the cardholder.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Last four digits of the credit card or debit card.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-defined unique ID for the card payment method.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Identifies the credit card type.

Possible values are:

**•** `American Express`

**•** `Diners Club`

**•** `JCB`

**•** `Maestro`

**•** `Master Card`

**•** `Visa`

**Type**
picklist


Standard Objects CardPaymentMethod

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Further identifies the credit card. Used for internal reference.

Possible values are:

**•** `AmericanExpress`

**•** `DinersClub`

**•** `Discover`

**•** `Jcb`

**•** `Maestro`

**•** `MasterCard`

**•** `UnionPay`

**•** `Visa`

```
Comments

CompanyName

DisplayCardNumber

Email

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Payment admin can add comments to provide additional details about a record. Maximum
of 1000 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Company of the cardholder.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Masked digits for the full credit card number except the last four digits.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects CardPaymentMethod

**Field** **Details**

**Description**
Email address of the payer.

```
ExpiryMonth

ExpiryYear

GatewayDate

GatewayResultCode

GatewayResultCodeDescription

GatewayToken

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The card’s expiration month.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The card’s expiration year.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date that the payment gateway logs a card activity.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The result of the card payment method’s interaction with the payment gateway during a
transaction request.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Additional information about the gateway result code. Descriptions vary between payment
gateway providers.

**Type**
string


Standard Objects CardPaymentMethod

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Unencrypted unique token ID generated by the payment gateway to represent the card
payment method during transactions. `GatewayToken` is for use with APIs earlier than
version 52.0. For version 53.0 and latter, use the GatewayTokenEncrypted field. To secure
the token, use the `GatewayTokenEncrypted` field.

An error message appears if you try to record a `GatewayToken` for a card payment
method that already has a `GatewayToken` or `GatewayTokenEncrypted` value.

```
GatewayTokenDetails

GatewayTokenEncrypted

InputCardNumber

IpAddress

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Additional information about the gateway token.

**Type**
encryptedstring

**Properties**
Create, Nillable, Update

**Description**
Encrypted unique token ID generated by the payment gateway to represent the card payment
method during transactions. Encrypted using Salesforce Classic Encryption.

Available in API version 52.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Used by a payer to enter a credit card number when storing an external-type card payment
method. After entry, the credit card number isn’t saved, so the `InputCardNumber` value
always appears blank. The credit card number appears as a masked value in
`DisplayCardNumber`, which shows only the last four digits.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
IP address of the card payment method holder.


Standard Objects CardPaymentMethod

**Field** **Details**

This field is available in API version 49.0 and later. It doesn’t appear in the UI by default for
Salesforce orgs that upgraded from version 48.0. Users must add it to the CardPaymentMethod
page layout on their own.

```
IsAutoPayEnabled

LastReferencedDate

LastViewedDate

MacAddress

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the payment method can be used for recurring payments ( `True` ) or not
( `False` ). The default value is `False` .

This field is available in API version 55.0 and later. For orgs that upgraded from version 54.0,
you must add this field to the Card Payment Method page layout in the UI. It isn't automatically
added.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record or list view related to this
record, but didn’t access it directly.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it's
possible the user referenced this record but didn’t view it directly.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
MAC address of the card payment method holder.

This field is available in API version 49.0 and later. It doesn’t appear in the UI by default for
Salesforce orgs that upgraded from version 48.0. Users must add it to the CardPaymentMethod
page layout on their own.


Standard Objects CardPaymentMethod

**Field** **Details**

```
NickName

PaymentGatewayId

PaymentMethodAddress

PaymentMethodCity

PaymentMethodCountry

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Payer-defined nickname for the card payment method.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The payment gateway used to create a gateway token. For transactions with a saved payment
method in Salesforce, this field stores the payment gateway ID used in the transaction.

This field is a relationship field.

**Relationship Name**
PaymentGateway

**Relationship Type**
Lookup

**Refers To**
PaymentGateway

**Type**
address

**Properties**
Filter, Nillable

**Description**
Full address associated with the card payment method.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
City of the address for the payment method.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects CardPaymentMethod

**Field** **Details**

**Description**
Country of the address for the payment method.

```
PaymentMethodDetails

PaymentMethodGeocodeAccuracy

PaymentMethodLatitude

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Optional information about the payment method type. This field is available in API version
57.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode for the payment method address. An accuracy level contains
information about the location of a latitude and longitude. For more information about
geolocation fields, see Geolocation Compound Field.

Possible values are:

**•** `Address`

**•** `Block`

**•** `City`

**•** `County`

**•** `ExtendedZip`

**•** `NearAddress`

**•** `Neighborhood`

**•** `State`

**•** `Street`

**•** `Unknown`

**•** `Zip`

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Latitude of the payment method address. Used with the PaymentMethodLongitude to
specify the precise geolocation of the address. For details on geolocation compound fields,
see Compound Field Considerations and Limitations.


Standard Objects CardPaymentMethod

**Field** **Details**

```
PaymentMethodLongitude

PaymentMethodPostalCode

PaymentMethodState

PaymentMethodStreet

PaymentMethodSubType

PaymentMethodType

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Latitude of the payment method address. Used with the PaymentMethodLatitude to specify
the precise geolocation of the address. For details on geolocation compound fields, see
Compound Field Considerations and Limitations.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Postal Code of the address for the payment method.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
State of the address for the payment method.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Street of the address for the payment method.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A payment method that exists as a subtype of a payment method type. For example, Visa,
Mastercard, and American Express exist as subtypes of payment method types such as Apple
Pay and Google Pay. This field is available in API version 57.0 and later.

**Type**
picklist


Standard Objects CardPaymentMethod

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Payment method used for the transaction. This field is available in API version 57.0 and later.

Possible values are:

**•** `AfterpayClearpay`

**•** `AmericanExpress`

**•** `ApplePay`

**•** `BanContact`

**•** `DinersClub`

**•** `Discover`

**•** `EPS`

**•** `GooglePay`

**•** `Jcb`

**•** `Klarna`

**•** `Maestro`

**•** `MasterCard`

**•** `Other`

**•** `PayPal`

**•** `SepaDebit`

**•** `UnionPay`

**•** `Venmo`

**•** `Visa`

**•** `iDeal`

```
Phone

ProcessingMode

```

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number of the payer.

This field is available in API version 49.0 and later. It doesn’t appear in the UI by default for
Salesforce orgs that upgraded from version 48.0. Users must add it to the CardPaymentMethod
page layout on their own.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort


Standard Objects CardPaymentMethod

**Field** **Details**

**Description**
Defines whether the card payment method is used for transactions made by Salesforce
Payments or by an external third-party payment provider.

Possible values are:

**•** `External` —Transactions happened outside of the Salesforce payments platform.

**•** `Salesforce` —Salesforce made and recorded an external call to the payment platform.

This field is available in API version 49.0 and later. It doesn’t appear in the UI by default for
Salesforce orgs that upgraded from version 48.0. Users must add it to the CardPaymentMethod
page layout on their own.

You must enter a value for this field.

```
SavedPaymentMethodId

SfResultCode

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the saved payment method record. This field is available in API version 60.0 and
later.

**Relationship Name**
SavedPaymentMethod

**Relationship Type**
Lookup

**Refers To**
SavedPaymentMethod

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The results of the card payment method’s interaction with the payment gateway.

Possible values are:

**•** `Decline`

**•** `Indeterminate`

**•** `PermanentFail`

**•** `RequiresReview`

**•** `Success`

**•** `SystemError`

**•** `ValidationError`


Standard Objects CardPaymentMethod

**Field** **Details**

```
StartMonth

StartYear

Status

```

Usage

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The month is activated.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The year the card is activated.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the payment method.

Possible values are:

**•** `Active`

**•** `Canceled`

**•** `InActive`

The following fields drop zeroes that appear at the beginning of the field value, and introduce commas for values with four or more
digits:

**•** `CardLastFour`

**•** `CardBin`

**•** `ExpiryYear`

For example, a `CardLastFour` entered value of _`0004112233445566`_ would appear as _`4,112,233,445,566`_ on the record.

As a workaround, create a String-type custom formula field with the same label as the field that you want to replace, then hide the
original field. Here are some examples for replacing `CardLastFour`, `CardBin`, and `ExpiryYear` .

**CardLastFour**

```
  IF(ISBLANK(CardLastFour), NULL,RIGHT("0000" & TEXT(CardLastFour), 4))

```

**CardBin**

```
  IF(ISBLANK(CardBin), NULL,RIGHT("000000" & TEXT(CardBin), 6))

```


### Standard Objects CartCheckoutSession

**ExpiryYear**

```
    IF(ISBLANK(ExpiryYear), NULL,TEXT(ExpiryYear)))

### CartCheckoutSession

```

Represents a checkout session used in Lightning B2B Commerce checkout. This object is available in API version 48.0 and later.

A checkout session is tied to a single web cart, but there can be multiple checkout sessions for a single cart.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
BackgroundOperationId

CurrencyIsoCode

IsArchived

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the in progress background operation.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The currency used for the checkout session. Default value is `USD` .

Possible values are:

**•** `USD` —U.S. Dollar

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects CartCheckoutSession

**Field** **Details**

**Description**
Indicates whether checkout processing is archived ( `true` ) or not ( `false` ). After a session
is archived, it can’t be unarchived. Default value is `false` .

```
IsError

IsProcessing

Name

NextState

OrderId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the session is in error state ( `true` ) or not ( `false` ). Default value is
`false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether checkout processing is in progress ( `true` ) or not ( `false` ). Default
value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the checkout session.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The next state of the checkout session.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of a created order after the checkout session has gone from cart to order.


### Standard Objects CartDeliveryGroup

**Field** **Details**

```
OrderReferenceNumber

State

WebCartId

### CartDeliveryGroup

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Unique reference number the shopper can use to refer to the order. In API version 63.0 and
later, LWR stores don't populate this field upon checkout. Instead, the
`InitialOrderReferenceNumber` field on the WebCart object is populated.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The current state of the checkout session.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the cart that is used to create the checkout session.

Represents shipping information for the delivery of items in an order against a store built with B2B Commerce or D2C Commerce. This
object is available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The CartDeliveryGroup object is available only if the B2B Commerce or D2C Commerce license is enabled.


Standard Objects CartDeliveryGroup

Fields

**Field** **Details**

```
CartId

CompanyName

CurrencyIsoCode

DeliverToAddress

DeliverToCity

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID the `WebCart on page 5858` that’s associated with this delivery group.

This field is a relationship field.

**Relationship Name**
Cart

**Relationship Type**
Lookup

**Refers To**
WebCart

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Company name associated with a delivery. This field is available in API version 59.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ISO code for the currency that’s specified on the buyer’s account. Default value is `USD` .
Possible values are:

**•** `USD` —U.S. Dollar

**Type**
address

**Properties**
Filter, Nillable

**Description**
The address to which a buyer order is delivered.

**Type**
string


Standard Objects CartDeliveryGroup

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city to which a buyer order is delivered.

```
DeliverToCountry

DeliverToFirstName

DeliverToGeocodeAccuracy

DeliverToLastName

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country to which a buyer order is delivered.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The first name of the person set to receive an order. This field is available in API version 57.0
and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The geocode location to which a buyer order is delivered. Possible values are:

**•** `Address`

**•** `Block`

**•** `City`

**•** `County`

**•** `ExtendedZip`

**•** `NearAddress`

**•** `Neighborhood`

**•** `State`

**•** `Street`

**•** `Unknown`

**•** `Zip`

**Type**
string


Standard Objects CartDeliveryGroup

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The last name of the person to whom a buyer order is delivered. This field is available in API
version 57.0 and later.

```
DeliverToLatitude

DeliverToLongitude

DeliverToName

DeliverToPostalCode

DeliverToState

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The latitude of a buyer delivery location.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The longitude of a buyer delivery location.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the person to deliver a buyer order to. This field is set based on the `Name` field
of the `ContactPointAddress` associated with this delivery group.
`ContactPointAddress.Name` is generated by the system using the first and last
names entered by a buyer during checkout.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code to which to deliver a buyer order.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects CartDeliveryGroup

**Field** **Details**

**Description**
The state to which to deliver a buyer order.

```
DeliverToStreet

DeliveryMethodId

DesiredDeliveryDate

GiftMessage

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street to which to deliver a buyer order.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID for the delivery method to use to deliver a buyer order. Populated if the selected
`CartDeliveryGroupMethod` only has the `ShippingFee` populated, but it has
reference to an existing `DeliveryMethodId` which contains the fields `Carrier`,
`ClassOfService`, and `ReferenceNumber` . If not, the
`SelectedDeliveryMethod` field is used.

This field is a relationship field.

This field is deprecated in API version 64.0 and will be removed in API version 66.0. Instead,
use the `DeliveryMethodId` field on the `CartDeliveryGroupMethod` object.

**Relationship Name**
DeliveryMethod

**Relationship Type**
Lookup

**Refers To**
OrderDeliveryMethod

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date that a buyer requests to have an order delivered.

**Type**
textarea

**Properties**
Create, Nillable, Update


Standard Objects CartDeliveryGroup

**Field** **Details**

**Description**
Personalized gift message for the order. This field is available in API version 64.0 and later.

```
GiftToName

GrandTotalAmount

IsDefault

IsGift

Name

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the recipient for a gift order. This field is available in API version 64.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of all cart items’ `TotalAmount`, or `CartDeliveryGroupTotalAmount` plus
`CartDeliveryGroup TotalTaxAmount` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the delivery group is the default. This field is available in API version 59.0 and
later.

The default value is `false` .

B2B and D2C stores create a default delivery group, along with a WebCart, when a customer
adds an item to cart and doesn't have an existing cart. The default cart delivery group is
needed to complete the checkout flow, and can't be replaced by a non-default cart delivery
group. If you customize the standard checkout flow, make sure that you don't delete the
default cart delivery group.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the delivery group is a gift. This field is available in API version 64.0 and later.

The default value is `false` .

**Type**
string


Standard Objects CartDeliveryGroup

**Field** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of this `CartDeliveryGroup` record. `Name` can be up to 255 characters. In
API version 62.0 and later, if `IsDefault` is `true`, the `Name` is `Shipment1`, a localized
string. In prior API versions, the `Name` for a default delivery group was `Cart Delivery`
`Group` . Due to this change, any queries intended to identify default delivery groups should
use the `IsDefault` rather than `Name` field.

```
SelectedDeliveryMethodId

ShipToPhoneNumber

ShippingInstructions

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the selected cart delivery group method. Populated if the selected
`CartDeliveryGroupMethod` has the fields `Carrier`, `ClassOfService`,
`ReferenceNumber`, and `ShippingFee`, but the `DeliveryMethodId` is null. If
not, the `DeliveryMethodId` field is used. This field is available in API version 59.0 or
later.

This field is a relationship field.

**Relationship Name**
SelectedDeliveryMethod

**Relationship Type**
Lookup

**Refers To**
CartDeliveryGroupMethod

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number associated with a delivery. This field is available in API version 59.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Instructions for delivering an order.


Standard Objects CartDeliveryGroup

**Field** **Details**

```
TotalAdjustmentAmount

TotalAdjustmentTaxAmount

TotalAmount

TotalCartItemCount

TotalChargeAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total amount of all promotional adjustments on the cart delivery group. This field is
available in API version 54.0 and later.

For product bundles, this includes the aggregate adjustments of all child components.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total tax amount for all promotional adjustments on the cart delivery group. This field
is available in API version 54.0 and later.

For product bundles, this includes the aggregate of the tax amounts for all child components’
adjustments.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all cart items `TotalPrice`, or `TotalProductAmount` plus
`TotalChargeAmount` .

For product bundles, this includes the aggregate of all child component prices.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of cart items, including their quantities, of the type `PRODUCT` in the delivery
group.

For product bundles, this count includes only the parent component.

If the total quantity of cart items of type `PRODUCT` in the delivery group exceeds the
system-defined maximum (INT_MAX), this field is set to INT_MAX.

**Type**
currency


Standard Objects CartDeliveryGroup

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all the cart items `TotalPrice` for all cart items of type `CHARGE` . Cart items
can be of type Product or Charge.

For product bundles, if a child component includes a cart item of type `CHARGE`, its amount
is aggregated with the parent’s cart item's total charge amount.

```
TotalChargeTaxAmount

TotalProductAmount

TotalProductTaxAmount

TotalTaxAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all the cart items `TotalTaxAmount` for all cart items of type `CHARGE` . Cart
items can be of type Product or Charge.

For product bundles, this includes the aggregate of all tax amounts associated with
bundle-level charges, including the taxes of individual child products.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all the cart items `TotalPrice` for all cart items of type `PRODUCT` . Cart items
can be of type Product or Charge.

For product bundles, this includes the aggregate of all child component prices.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all the cart items `TotalTaxAmount` for all cart items of type `PRODUCT` . Cart
items can be of type Product or Charge.

For product bundles, this includes the aggregate of all child component taxes based on their
individual prices.

**Type**
currency

**Properties**
Filter, Nillable, Sort


### Standard Objects CartDeliveryGroupMethod

**Field** **Details**

**Description**
The sum of all cart items `TotalTaxAmount`, or the combined value of
`TotalProductTaxAmount` plus `TotalChargeTaxAmount` .

For product bundles, this includes the aggregate of all child component taxes based on their
individual prices.

Associated Objects

**CartDeliveryGroupChangeEvent (API version 58.0)**
Change events are available for the object.

### CartDeliveryGroupMethod

Represents the selected delivery method for a cart delivery group used in Lightning B2B Commerce checkout. This object is available in
API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The CartDeliveryGroupMethod object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
AdjustedShippingFee

Carrier

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Shipping fee, including `TotalAdjustmentAmount`, for the delivery method.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects CartDeliveryGroupMethod

**Field** **Details**

**Description**
The carrier that the buyer chose for their delivery method. Values are defined based on the
user’s shipping service. This field is available in API version 59.0 or later.

```
CartCheckoutSessionId

CartDeliveryGroupId

ClassOfService

CurrencyIsoCode

DeliveryMethodId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique ID used to identify your cart checkout session.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the cart delivery group associated with the checkout session.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The carrier class of service that the buyer chose for their delivery method. Values are defined
based on the user’s shipping service. This field is available in API version 59.0 or later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The currency used for your shipping fee. Default value is `USD` .

Possible values are:

**•** `USD` —U.S. Dollar

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the selected order delivery method.


Standard Objects CartDeliveryGroupMethod

**Field** **Details**

```
ExternalProvider

IsActive

Name

ProcessTime

ProcessTimeUnit

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the external shipping method provider. Optional field.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Assign new delivery groups to active delivery methods. The default value is `False` . This
field is available in API version 59.0 or later.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the delivery method.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Merchant-specified process time for the delivery method. Process time includes the time
between when an order is placed and when the shipment is given to the shipping carrier.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Unit of time used to define `ProcessTime` .

Possible values are:

**•** `Days`

**•** `Hours`

**•** `Weeks`


Standard Objects CartDeliveryGroupMethod

**Field** **Details**

```
ProductId

ReferenceNumber

ShippingFee

TotalAdjustmentAmount

TransitTimeMax

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Optional. This product represents a delivery charge order product for a delivery using this
delivery method. For example, you could create a product that represents an overnight
express charge and assign it to an overnight express delivery method. If your store uses
[Salesforce Native Shipping, the](https://help.salesforce.com/s/articleView?id=commerce.comm_set_up_native_shipping.htm&type=5&language=en_US) `ProductId` is selected from a non-variation product with
`Shipping` in its name. The term `Shipping` in a product name isn’t localized. If no
matching product is found, a random non-variation product is used. This field is available in
API version 59.0 or later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Reference number for an external delivery method. This field is available in API version 59.0
or later.

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
Shipping fee associated with the delivery method. Required field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The adjustment amount of a promotion applicable to the delivery method.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects CartDeliveryGroupMethodAdj

**Field** **Details**

**Description**
Maximum estimate of transit time for the delivery method. Transit time includes the time
between when a shipping carrier receives a shipment and when the shipment arrives at the
delivery address.

```
TransitTimeMin

TransitTimeUnit

WebCartId

```

Usage

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Minimum estimate of transit time for the delivery method. Transit time includes the time
between when a shipping carrier receives a shipment and when the shipment arrives at the
delivery address.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Unit of time used to define `TransitTimeMax` and `TransitTimeMin` .

Possible values are:

**•** `Days`

**•** `Hours`

**•** `Weeks`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the WebCart associated with the cart delivery group method. Required field.

Use the CartDeliveryGroupMethod object to give commerce buyers the ability to choose a delivery method for a cart delivery group.
Shipping integrations populate the delivery options that are available for a cart delivery group.

### CartDeliveryGroupMethodAdj

Represents the shipping promotion discount for a shipping method. This object is available in API version 60.0 and later.


Standard Objects CartDeliveryGroupMethodAdj

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The CartDeliveryGroupMethodAdj object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
AdjustmentAmount

AdjustmentBasisReferenceId

AdjustmentType

```

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
Amount subtracted from the price by the shipping promotion discount.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the adjustment basis reference. This is the coupon that causes the adjustment. This
field is a relationship field.

This field is available in API version 62.0 and later.

**Relationship Name**
AdjustmentBasisReference

**Refers To**
Coupon

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Type of shipping promotion discount.

Possible values are:

**•** `AdjustmentAmount`

**•** `AdjustmentPercentage`

**•** `OverrideAmount`


Standard Objects CartDeliveryGroupMethodAdj

**Field** **Details**

```
AdjustmentValue

CartDeliveryGroupMethodId

CurrencyIsoCode

Name

```

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
Number representing the value of the price adjustment. For example, if the
`AdjustmentType` is `AdjustmentPercentage`, a -10 `AdjustmentValue`
means 10 percent off. If the `AdjustmentType` is `AdjustmentAmount`, a -10
`AdjustmentValue` means 10 dollars off.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the cart delivery group method.

This field is a relationship field.

**Relationship Name**
CartDeliveryGroupMethod

**Relationship Type**
Lookup

**Refers To**
CartDeliveryGroupMethod

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Currency ISO code of the cart.

Possible values are:

**•** `USD` —U.S. Dollar

The default value is `USD` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the cart delivery group method adjustment.


### Standard Objects CartItem

**Field** **Details**

```
PriceAdjustmentCauseId

Priority

### CartItem

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the price adjustment cause.

This field is a relationship field.

**Relationship Name**
PriceAdjustmentCause

**Relationship Type**
Lookup

**Refers To**
Promotion

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If there are multiple promotional adjustments, the order in which the shipping promotion
is applied.

Represents an item in a `WebCart` that’s active in a store built with B2B. Cart item can be of type `Product` or `Charge` . This object
is available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The CartItem object is available only if the B2B Commerce license is enabled.


Standard Objects CartItem

Fields

**Field** **Details**

```
AdjustmentAmount

AdjustmentTaxAmount

AssociatedItemPricing

BillingFrequency

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Non-itemized adjustments for this cart item.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The tax that’s calculated on the `AdjustmentAmount` .

**Type**
picklist

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Specifies how a child cart item is priced relative to its parent cart item within a product
bundle. This field is `null` for standalone products that aren't part of a bundle. Available in
API version 65.0 and later.

Possible values are:

**•** `IncludedInBundlePrice` —Indicates that the parent product’s price includes
the aggregated prices of its child components.

**•** `NotIncludedInBundlePrice` —Indicates that the parent product’s price doesn’t
include the aggregated prices of its child components.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies how often a subscription is billed. Available in API version 59.0 and later.

Possible values are:

**•** `Annual`

**•** `MilestonePlan`

**•** `Monthly`

**•** `Quarterly`


Standard Objects CartItem

**Field** **Details**

**•** `Semi-Annual`

```
CartDeliveryGroupId

CartId

ChildProductCount

ConfigureDuringSale

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the `CartDeliveryGroup` that’s associated with a cart item.

This field is a relationship field.

**Relationship Name**
CartDeliveryGroup

**Relationship Type**
Lookup

**Refers To**
CartDeliveryGroup

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the `WebCart` that’s associated with a cart item.

This field is a relationship field.

**Relationship Name**
Cart

**Relationship Type**
Lookup

**Refers To**
WebCart

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of child products associated with this cart item. If a child product is a
bundle, its own `ChildProductCount` is included in this total. For simple products that
don’t have any child products, the `ChildProductCount` value is zero.

**Type**
picklist


Standard Objects CartItem

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Specify whether a product bundle is configurable. Available in API version 65.0 and later.

Possible values are:

**•** `Allowed`

**•** `NotAllowed`

```
CurrencyIsoCode

DistributedAdjustment

Amount

DistributedAdjustment

TaxAmount

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ISO code for the currency that’s specified on the buyer’s account. Default value is `USD` .
Possible values are:

**•** `AED` —UAE Dirham

**•** `AUD` —Australian Dollar

**•** `BRL` —Brazilian Real

**•** `CAD` —Canadian Dollar

**•** `EUR` —Euro

**•** `GBP` —British Pound

**•** `INR` —Indian Rupee

**•** `JPY` —Japanese Yen

**•** `SEK` —Swedish Krona

**•** `USD` —U.S. Dollar

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
A calculated field that determines the amount of a cart-wide promotional adjustment when
distributed across all items in the cart. This field is for display purposes only and is valid only
during checkout. This field is available in API version 52.0 and later.

You receive $10 off, and there are 5 items in the cart. The distributed adjustment is (-$2).

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort


Standard Objects CartItem

**Field** **Details**

**Description**
A calculated field that determines the amount of a cart-wide tax adjustment due to
promotions when distributed across all items in the cart. This field is available in API version
52.0 and later.

EXAMPLE: Your discount causes a cart-wide tax reduction of (-$10), and there are 5 items in
the cart. The distributed tax adjustment is (-$2).

```
EndQuantity

FirstPymtPriceAferAdjustments

FirstPymtTax

GrossAdjustmentAmount

GrossUnitPrice

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the final asset quantity when the subscription is modified or when it ends.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The first term price for term-based subscription products, after price adjustments are applied.
The total amount for a non-subscription product or a non-term based subscription product,
after price adjustments are applied. This is available in API version 60.0 and later.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The tax for the first term price for term-based subscription products. The tax amount for a
non-subscription product or a non-term subscription product. This field is available in API
version 60.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The gross amount of the price adjustment on the cart item (tax inclusive). This is available
in API version 55.0 and later.

**Type**
currency


Standard Objects CartItem

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The gross amount of the unit price for a cart item (tax inclusive). This is available in API version
55.0 and later.

```
IsShippingChargeNot

Applicable

ItemizedAdjustment

Amount

ItemizedAdjustment

TaxAmount

ListPrice

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether shipping charges are applicable ( `true` ) or not ( `false` ) to the cart item.
The default value is `false` .

This field is available in API version 64.0 and later.

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
A calculated field that determines the total amount of promotional adjustments that are
specific to an item. This field is available in API version 52.0 and later.

EXAMPLE: One cart item has one discount code for $10 off. Your itemized adjustment amount
is (-$10) for that item.

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
A calculated field that determines the total amount of promotion-related tax adjustments
that are specific to an item. This field is available in API version 52.0 and later.

EXAMPLE: One cart item has one discount code for $10 off. This reduces the tax on that item
by (-$2). Your itemized adjustment tax amount is (-$2) for that item.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects CartItem

**Field** **Details**

**Description**
The original price of the cart item. Typically shown with a line through it. List price is shown
only when it’s higher than the negotiated price. If the list price is the same or lower, it isn’t
shown to the buyer. This field is available in API version 52.0 and later.

```
Name

NetAdjustmentAmount

NetUnitPrice

NetUnitPriceAfterAdjustments

ParentCartItemId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of this `CartItem` record. `Name` can be up to 255 characters.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The net amount of the price adjustment made on the cart item (tax exclusive). This is available
in API version 55.0 and later.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The net amount of the unit price for the cart item (tax exclusive). This is available in API
version 55.0 and later.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The net unit price for a cart item, after all tier and promotional price adjustments are applied.
This field is available in API version 60.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects CartItem

**Field** **Details**

**Description**
The ID of the cart item's parent `CartItem` . The value is empty if the item is a top-level cart
item.

This field is a relationship field.

**Relationship Name**
CartItem

**Relationship Type**
Lookup

**Refers To**
CartItem

```
PerUnitWeight

PeriodBoundary

PeriodBoundaryDay

PeriodBoundaryStartMonth

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Weight per unit of this cart item, in the unit specified by `WeightUnit` . This field is available
in API version 62.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The. Default value is . Possible values are:

**•** `AlignToCalendar`

**•** `Anniversary`

**•** `DayOfPeriod`

**•** `LastDayOfPeriod`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The .

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects CartItem

**Field** **Details**

**Description**
The. Default value is . Possible values are:

**•** `1` —January

**•** `10` —October

**•** `11` —November

**•** `12` —December

**•** `2` —February

**•** `3` —March

**•** `4` —April

**•** `5` —May

**•** `6` —June

**•** `7` —July

**•** `8` —August

**•** `9` —September

```
PriceBookEntryId

PricingTermCount

Product2Id

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the price book entry for the product. This field is available in API version 60.0 and
later.

This field is a relationship field.

**Relationship Name**
PricebookEntry

**Relationship Type**
Lookup

**Refers To**
PricebookEntry

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A calculated field that indicates the number of pricing terms in the subscription. This field is
available in API version 59.0 and later.

**Type**
reference


Standard Objects CartItem

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of a product type cart item. Cart items can be of type `PRODUCT` or `CHARGE` .

This field is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

```
ProductClass

ProductRelated

ComponentId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The product class of the cart item. Default value is `Simple` . Possible values are:

**•** `Bundle`

**•** `Set`

**•** `Simple`

**•** `Variation`

**•** `VariationParent`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the cart item's `ProductRelatedComponent` . The
`ProductRelatedComponent` represents a product that is included in a product
bundle, a set, or a product and an add-on. The `ProductRelatedComponent` is empty
if the item is a top-level cart item.

This field is a relationship field.

**Relationship Name**
ProductRelatedComponent

**Relationship Type**
Lookup

**Refers To**
ProductRelatedComponent


Standard Objects CartItem

**Field** **Details**

```
ProductSellingModelId

ProductValidationKey

ProductRelationshipTypeId

ProrationPolicyId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the model used to sell a product. This field is available in API version 59.0 or later.

This field is a relationship field.

**Relationship Name**
ProductSellingModel

**Relationship Type**
Lookup

**Refers To**
ProductSellingModel

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product validation key of the cart item.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the product relationship type that defines the relationship between a product
bundle and its child product. Available in API version 65.0 and later.

This field is a relationship field.

**Relationship Name**
ProductRelationshipType

**Relationship Type**
Lookup

**Refers To**

[https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_productrelationshiptype.htmProductRelationshipType](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_productrelationshiptype.htm)

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects CartItem

**Field** **Details**

**Description**
The ID of the proration policy, which defines how prices are calculated for each time period
within a subscription term. This field is available in API version 60.0 and later.

This field is a relationship field.

**Relationship Name**
ProrationPolicy

**Relationship Type**
Lookup

**Refers To**
Proration Policy

```
StartQuantity

Quantity

QuantityScaleMethod

SalesPrice

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the initial asset quantity when the subscription starts.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The number of a given cart item in a cart.

**Type**
picklist

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Determines how a child product's quantity scales when added to a cart or configured within
a product bundle. Available in API version 65.0 and later. Possible values are:

**•** `Constant` —Represents a value that remains fixed relative to the parent bundle.

**•** `Proportional` —Represents a value that varies in proportion to the parent bundle’s
price or quantity.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects CartItem

**Field** **Details**

**Description**
The discounted price of a cart item.

```
SellingModelType

Sku

StockCheckMethod

SubType

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of the product selling model associated with a term-based subscription product.
This field is available in API version 60.0 and later. Possible values are:

**•** `Evergreen`

**•** `OneTime`

**•** `TermDefined`

The default value is `OneTime` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Shelf-Keeping Unit ID of a cart item.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Determines how inventory is assessed for a cart item that’s part of a bundle or set. Possible
values are:

**•** `ChildProducts` —Inventory is assessed based on the child product or products.

**•** `ParentProduct` —Inventory is assessed based on the parent product.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the subtype of the product. Possible values are:

**•** `Bonus` —Bonus product.

**•** `GiftWrap` —Gift wrapped product.


Standard Objects CartItem

**Field** **Details**

This field is available in API version 64.0 and later.

```
SubscriptionTerm

TaxTreatmentId

TotalAdjustmentAmount

TotalAmount

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of terms (years or months, for example) in the subscription. This field is available
in API version 59.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the related tax treatment for the cart item.

This field is available in API version 63.0 and later. This field is available with Subscription
Management.

This field is a relationship field.

**Relationship Name**
TaxTreatment

**Relationship Type**
Lookup

**Refers To**
TaxTreatment

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The total amount of all promotional adjustments on the item, both distributed and itemized.
This field is available in API version 52.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total cost of this cart item, including taxes and adjustments.


Standard Objects CartItem

**Field** **Details**

```
TotalFirstPymtAdjAmount

TotalFirstPymtListPrice

TotalFirstPymtPrice

TotalLineAmount

TotalLineFirstPymtAmount

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The total adjustment amount for the first payment of a term-based susbcription product.
The TotalAdjustmentAmount for non-subscription products and non-term based subscription
products. This field is available in API version 63.0 and later.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The first-payment amount for a term-based subscription product, based on the product's
ListPrice. This is the same value as TotalListPrice for non-subscription products or non-term
based subscription products. This price is only for comparison, and not the price at which
the buyer purchases a product. This field is available in API version 63.0 and later.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The first term price for term-based subscription products. The price of a line item for
non-subscription products and non-term based subscription products. This price includes
price adjustments and excludes taxes. This field is available in API version 63.0 and later.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Total amount for this cart item, based on sales price and quantity.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The first term price for term-based subscripiton products, calculated based on the sales price
and quantity, before any price adjustments are made. This is the same value as


Standard Objects CartItem

**Field** **Details**

TotalLineAmount for non-subscription products and non-term based subscription products.
This field is available in API version 63.0 and later.

```
TotalLineFirstPymtTaxAmount

TotalLineGrossAmount

TotalLineNetAmount

TotalLineTaxAmount

TotalListPrice

```

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
The tax on the first payment amount, after price adjustments, for term-based subscription
products. The tax on the price of the product for non-subscription products and non-term
based subscription products. Taxes are also calculated on the delivery charge items. This
field is a calculated field. This field is available in API version 63.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total gross amount of the line item (tax inclusive). This is available in API version 55.0
and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total net amount of the line item (tax exclusive). This is available in API version 55.0 and
later.

**Type**
currency

**Properties**
Defaulted on create, Filter, Nillable, Sort

**Description**
Total tax amount for `TotalLineAmount` .

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects CartItem

**Field** **Details**

**Description**
Total amount for this cart item, based on `ListPrice` . We provide this value for comparison.
It's not the price that the buyer is paying.

```
TotalPrice

TotalPriceAfterAll

Adjustments

TotalPriceTaxAmount

TotalPromo

AdjustmentAmount

TotalPromoAdjustment

TaxAmount

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Total amount for this cart item, including adjustments but excluding taxes.

[Note: Although this field is Nillable, if you want to use Commerce Webstore Cart](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_cart_promotions.htm)
[Promotions, this field is required.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_cart_promotions.htm)

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Total price after all price adjustments are applied. This field is available in API version 52.0
and later.

[Note: Although this field is Nillable, if you want to use Commerce Webstore Cart](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_cart_promotions.htm)
[Promotions, this field is required.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_cart_promotions.htm)

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total tax amount for a cart item before promotional adjustments, including quantity-based
adjustments. This field is available in API version 56.0 and later.

**Type**
currency

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Total itemized and distributed adjustment amount in cart (only for promotions). This field is
available in API version 52.0 and later.

**Type**
currency


Standard Objects CartItem

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
Total itemized and distributed adjustment tax amount in cart (only for promotions). This
field is available in API version 52.0 and later.

```
TotalTaxAmount

TotalWeight

Type

UnitAdjustedPrice

UnitAdjustedPrice

WithItemAdj

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total tax amount for this cart item. This value includes taxes for both `TotalLineAmount`
and `AdjustmentAmount` .

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Total weight of this cart item, in the unit specified by `WeightUnit` . This field is available
in API version 62.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The `CartItem` type. Possible values are:

**•** `Product`

**•** `Charge`

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Price per quantity unit after a tier discount or surcharge is applied. This field is available in
API version 50.0 and later.

**Type**
currency


Standard Objects CartItem

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Unit price, including both tier and item level discounts, for the item.

```
UnitAdjustmentAmount

UnitItemAdjustment

Amount

UnitPriceAfterAdjustments

WeightUnit

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Tier discount or surcharge to apply to a quantity unit. This amount is added to the
`SalesPrice` to get the `UnitAdjustedPrice` . This field is available in API version
50.0 and later.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Item level adjustments made to the unit price for the item.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The unit price for a cart item, after tier and promotional price adjustments are applied. This
field is available in API version 60.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Unit of measurement for the weight of the cart item. This field is available in API version 62.0
and later.

Possible values are:

**•** `Grams`

**•** `Kilograms`

**•** `Ounces`

**•** `Pounds`


### Standard Objects CartItemAttribute

Associated Objects

This object has the following associated objects. Unless it’s noted, associated objects are available in the same API version as this object.

**CartItemChangeEvent (API version 58.0)**
Change events are available for the object.

SEE ALSO:

[Commerce Webstore Cart Promotions](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_cart_promotions.htm)

[Commerce Webstore Promotions, Associate Action](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_promotions_actions_associate.htm)

[Commerce Webstore Promotions, Execute Action](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/connect_resources_commerce_webstore_promotions_actions_execute.htm)

CartDeliveryGroup

WebCart

### CartItemAttribute

Represents the attributes associated with a cart item, stored as key-value pairs. These attributes are derived from the product and carried
forward to the order during checkout. This object is available in API version 66.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

The CartItemAttribute object is available:only if the B2B Commerce license, the Salesforce CPQ feature, and Commerce Dynamic Bundles
are enabled in your Salesforce org.

Fields

**Field** **Details**

```
AttributeDefinitionId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the attribute definition associated with the cart item attribute.

This field is a relationship field.

**Relationship Name**
AttributeDefinition

**Relationship Type**
Lookup


Standard Objects CartItemAttribute

**Field** **Details**

**Refers To**

[AttributeDefinition](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_attributedefinition.htm)

```
AttributeName

AttributePicklistValueId

AttributeValue

CartItemId

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The name of the cart item attribute.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the picklist value associated with the cart item attribute.

This field is a relationship field.

**Relationship Name**
AttributePicklistValue

**Relationship Type**
Lookup

**Refers To**

[AttributePicklistValue](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_attributepicklistvalue.htm)

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The value of the cart item attribute, such as Blue or Large.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the cart item to which this attribute is assigned.

This field is a relationship field.

**Relationship Name**
CartItem


Standard Objects CartItemAttribute

**Field** **Details**

**Relationship Type**
Master-detail

**Refers To**

[CartItem (the master object)](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_cartitem.htm)

```
ExternalId

IsPriceImpacting

UnitOfMeasure

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An auto-generated ID for the attribute record that's stored in an external system, such as the
HBase database.

**Type**
boolean

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates whether the attribute affects cart pricing ( `true` ) or not ( `false` ). This field
determines whether the Commerce Pricing API calls must be triggered to update the price.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the unit of measure associated with the cart item attribute.

This field is available only if the AttributeUomPilot Org perm is enabled. Contact Salesforce
support for assistance.

This field is a relationship field.

**Relationship Name**
UnitOfMeasure

**Relationship Type**
Lookup

**Refers To**

[UnitOfMeasure](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_unitofmeasure.htm)

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


### Standard Objects CartItemPriceAdjustment

**CartItemAttributeChangeEvent on page 68**
Change events are available for the object.

**CartItemAttributeFeed on page 55**
Feed tracking is available for the object.

**CartItemAttributeHistory on page 63**
History is available for tracked fields of the object.

**CartItemAttributeOwnerSharingRule on page 65**
Sharing rules are available for the object.

**CartItemAttributeShare on page 67**
Sharing is available for the object.

### CartItemPriceAdjustment

Price adjustment for a cart item. This object is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The CartItemPriceAdjustment object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
AdjustmentAmountScope

AdjustmentBasisReferenceId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Scope of the adjustment amount for a promotion.

Possible values are:

**•** `Total` —The amount off the total price.

This field is available in API version 54.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects CartItemPriceAdjustment

**Field** **Details**

**Description**
Coupon code of the coupon associated with a promotion. This field is available in API version
54.0 and later.

This is a relationship field.

**Relationship Name**
AdjustmentBasisReference

**Relationship Type**
Lookup

**Refers To**
Coupon

```
AdjustmentSource

AdjustmentTargetType

AdjustmentType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Price adjustment type.

Possible values are:

**•** `Discretionary`

**•** `Promotion`

**•** `System`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Target for the price adjustment (the cart itself or individual items).

Possible values are:

**•** `Cart`

**•** `Item`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates if the price adjustment is applied as percentage or an absolute amount.

Possible values are:

**•** `AdjustmentAmount`


Standard Objects CartItemPriceAdjustment

**Field** **Details**

**•** `AdjustmentPercentage`

```
AdjustmentValue

CartId

CartItemId

CurrencyIsoCode

```

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
Numeric value of the adjustment (for example, 10 if the price adjustment is either 10% off
or $10 off).

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the WebCart that’s associated with a cart item. This field is available in API version
55.0 and later.

This is a relationship field.

**Relationship Name**
Cart

**Relationship Type**
Lookup

**Refers To**
WebCart

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the parent cart item to which this adjustment belongs.

This is a relationship field.

**Relationship Name**
CartItem

**Relationship Type**
Lookup

**Refers To**
CartItem

**Type**
picklist


Standard Objects CartItemPriceAdjustment

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ISO code for the currency that’s specified on the buyer’s account. Default value is `USD` .

Possible values are:

**•** `EUR` —Euro

**•** `USD` —U.S. Dollar

```
Description

Name

PriceAdjustmentCauseId

Priority

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the price adjustment.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the price adjustment.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Nillable, Update

**Description**
ID of entity that caused this adjustment (for example, a promotion ID). If unspecified, then
`Description` populates the display name.

This is a relationship field.

**Relationship Name**
PriceAdjustmentCause

**Relationship Type**
Lookup

**Refers To**
Promotion

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects CartItemPriceAdjustment

**Field** **Details**

**Description**
If there are multiple price adjustments, sequence in which the price adjustments are applied.

```
TotalAmount

TotalGrossAmount

TotalNetAmount

TotalTax

WebCartAdjustmentGroupId

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Total price after applying price adjustments.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total gross amount (tax inclusive) after applying price adjustments. This field is available
in API version 55.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total net amount (tax exclusive) after applying price adjustments. This field is available
in API version 55.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the total adjusted price.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the cart’s adjustment group.

This is a relationship field.


### Standard Objects CartTax

**Field** **Details**

**Relationship Name**
WebCartAdjustmentGroup

**Relationship Type**
Lookup

**Refers To**
WebCartAdjustmentGroup

Associated Objects

This object has the following associated objects. Unless it’s noted, associated objects are available in the same API version as this object.

**CartItemPriceAdjustmentChangeEvent (API version 58.0)**
Change events are available for the object.

### CartTax

Represents taxes for a line item in a `WebCart` that’s active in a store built with B2B Commerce or D2C Commerce. This object is available
in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The CartTax object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
AdjustmentTargetType

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Target for the price adjustment (the cart itself or individual items). This field is available in
API version 52.0 and later.

Possible values are:

### • Cart


Standard Objects CartTax

**Field** **Details**

**•** `Item`

```
Amount

CartId

CartItemId

CartItemPriceAdjustmentId

CurrencyIsoCode

```

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
Calculated tax amount.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the `WebCart` being taxed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of a cart item being taxed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of a price adjustment for a cart item being taxed. (This field is available in API version
52.0 and later.)

**Refers To**
CartItemPriceAdjustment

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ISO code for the currency that’s specified on the buyer’s account. Default value is `USD` .
Valid values include:

**•** `USD` —U.S. Dollar


Standard Objects CartTax

**Field** **Details**

```
Description

Name

TaxCalculationDate

TaxRate

TaxType

```

Associated Objects

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the tax. Enter up to 2000 characters.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of this `CartTax` record. `Name` can be up to 255 characters.

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The date this tax was calculated.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The applied tax rate for this line of tax.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of tax for this line of tax. Possible values are:

**•** `Actual`

**•** `Estimated`

This object has the following associated objects. Unless it’s noted, associated objects are available in the same API version as this object.


### Standard Objects CartValidationOutput

**CartTaxChangeEvent (API version 58.0)**
Change events are available for the object.

SEE ALSO:

WebCart

### CartValidationOutput

Associate errors to cart entities, such as cart line items, delivery groups, and the like, in a store built with B2B Commerce or D2C Commerce.
An example error is “Out of stock.” Available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout() describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The CartValidationOutput object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
BackgroundOperationId

CartId

CurrencyIsoCode

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the background operation that ran the validation.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the related `WebCart` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects CartValidationOutput

**Field** **Details**

**Description**
The ISO code for the currency that’s specified on the buyer’s account. Default value is
`USD` .Possible values are:

**•** `EUR` —Euro

**•** `USD` —U.S. Dollar

```
IsDismissed

Level

Message

Name

RelatedEntityId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the validation process is finished. Default value is `false` .

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Describes the type of output resulting from the validation process. Possible values are:

**•** 0 ( `Info` )

**•** 1 ( `Error` )

**•** 2 ( `Warning` )

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Defines the message to show in the log when validation is complete. Message can be up to
255 characters.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of this `CartValidationOutput` record. `Name` can be up to 255 characters.

**Type**
reference


Standard Objects CartValidationOutput

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Foreign key to `WebCart`, `CartItem`, and `CartDeliveryGroup` .

```
RelatedEntityPrefix

Type

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Three-character prefix for the related entity.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The `CartValidationOutput` type. Possible values are:

**•** `CartSave`  - Available in API version 64.0 and later.

**•** `Entitlement`

**•** `Inventory`

**•** `Other`

**•** `Pricing`

**•** `Promotions`

**•** `Shipping`

**•** `ShippingPromotions`

**•** `SystemError`

**•** `Taxes`

This object has the following associated objects. Unless it’s noted, associated objects are available in the same API version as this object.

**CartValidationOutputChangeEvent (API version 58.0)**
Change events are available for the object.

SEE ALSO:

WebCart

CartItem

CartDeliveryGroup


### Standard Objects Case Case

Represents a case, which is a customer issue or problem.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AccountId

AssetWarrantyID

BusinessHoursId

Comments

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the account associated with this case.

This is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Asset associated with the warranty. Must be a valid asset warranty ID.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the business hours associated with this case.

**Type**
textarea


Standard Objects Case

**Field** **Details**

**Properties**
Create, Delete, Layout, Nillable, Query, Retrieve, Search, Sort, Undelete, Update

**Description**
Used to insert a new CaseComment. Email textarea has a length of 4000 chars.

```
CaseNumber

ClosedDate

CommunityId

ConnectionReceivedId

ConnectionSentId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Assigned automatically when each case is inserted. It can't be set directly, and it can't be
modified after the case is created.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the case was closed.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the zone associated with this case.

This field is available in API version 24.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the PartnerNetworkConnection that shared this record with your organization. This
field is available if you enabled Salesforce to Salesforce.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects Case

**Field** **Details**

**Description**
ID of the PartnerNetworkConnection that you shared this record with. This field is available
if you enabled Salesforce to Salesforce. This field is supported using API versions earlier than
15.0. In all other API versions, this field’s value is null. You can use the new
PartnerNetworkRecordConnection object to forward records to connections.

```
ContactEmail

ContactFax

ContactId

ContactMobile

```

**Type**
email

**Properties**
Filter, Group, Nillable, Sort

**Description**
Email address for the contact. The Case.ContactEmail field displays the Email field on the
contact on page 1380 that is referenced by Case.ContactId. Label is `Contact Email` . This
field is available in API version 38.0 and later.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
Fax number for the contact. Label is `Contact Fax` . This field is available in API version
38.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the associated contact.

This is a relationship field.

**Relationship Name**
Contact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort


Standard Objects Case

**Field** **Details**

**Description**
Mobile telephone number for the contact. Label is `Contact Mobile` . This field is available
in API version 38.0 and later.

```
ContactPhone

CreatorFullPhotoUrl

CreatorName

CreatorSmallPhotoUrl

Description

```

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
Telephone number for the contact. Label is `Contact Phone` . This field is available in API
version 38.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL of the user’s profile photo from the feed. Chatter Answers must be enabled to view this
field. This field is available in API version 26.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Name of the user who posted the question or reply. Only the first name of internal users
(agents) appears to portal users in the feed. Chatter Answers must be enabled to view this
field. This field is available in API version 26.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL of the user’s thumbnail photo from the feed. Chatter Answers must be enabled to view
this field. This field is available in API version 26.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update


Standard Objects Case

**Field** **Details**

**Description**
A text description of the case. Limit: 32 KB.

```
FeedItemId

HasCommentsUnreadByOwner

HasSelfServiceComments

IsClosed

IsClosedOnCreate

```

**Type**
reference

**Properties**
Create, Group, Nillable, Sort

**Description**
ID of the question in Chatter associated with the case. This field is available in API version
33.0 and later, and is only accessible in organizations where Question-to-Case is enabled.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a case contains comments that the case owner hasn’t read ( `true` ) or not
( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a case has comments added by a Self-Service user ( `true` ) or not ( `false` ).
Only visible when Customer Portal is enabled.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the case is closed ( `true` ) or open ( `false` ). This field is controlled by the
`Status` field; it can't be set directly. Label is `Closed` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects Case

**Field** **Details**

**Description**
Indicates whether the case was closed at the same time that it was created ( `true` ) or not
( `false` ). This flag is read-only and is automatically set when a record is created. It can't be
set to `true` unless the `IsClosed` flag is also `true` .

```
IsDeleted

IsEscalated

IsSelfServiceClosed

IsStopped

IsVisibleInSelfService

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is `Deleted` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the case has been escalated ( `true` ) or not. A case's escalated state does
not affect how you can use a case, or whether you can query, delete, or update it. You can
set this flag via the API. Label is `Escalated` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the case is closed for Self-Service users ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether an entitlement process on a case is stopped ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects Case

**Field** **Details**

**Description**
Indicates whether the case can be viewed in the Customer Service Portal, Partner Service
Portal, and Self-Service Portal ( `true` ) or not ( `false` ). This field is applied for case visibility
in the Partner Relationship Management, Customer Service Portal, and the earlier version of
Self Service Portal. The field does not alter sharing and will not prevent usage of a direct URL
to a case if a portal user has read or write access.

```
Language

LastReferencedDate

LastViewedDate

MasterRecordId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the case. The Language field is available when you enable Einstein Case
Classification in Enterprise, Performance, and Unlimited edition orgs with Service Cloud. By
default, only Einstein classification apps use this field.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view ( `LastReferencedDate` ) but
not viewed it.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
If this object was deleted as the result of a merge, this field contains the ID of the record that
was kept. If this object was deleted for any other reason, or has not been deleted, the value
is `null` .

This is a relationship field.


Standard Objects Case

**Field** **Details**

**Relationship Name**
MasterRecord

**Relationship Type**
Lookup

**Refers To**
Case

```
Origin

OwnerId

ParentId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable,Sort, Update

**Description**
The source of the case, such as `Email`, `Phone`, or `Web` . Label is `Case Origin` .

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the contact who owns the case.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the parent case in the hierarchy. The label is `Parent Case` .

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Case


Standard Objects Case

**Field** **Details**

```
Priority

QuestionId

Reason

RecordTypeId

ServiceContractId

SlaStartDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The importance or urgency of the case, such as `High`, `Medium`, or `Low` .

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The question in the answers zone that is associated with the case. This field does not appear
if you don't have an answers zone enabled.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The reason why the case was created, such as `Instructions not clear`, or `User`
`didn’t attend training` .

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the record type assigned to this object.

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
Required. ID of the ServiceContract associated with the entitlement. Must be a valid ID.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects Case

**Field** **Details**

**Description**
Shows the time that the case entered an entitlement process. If you have the Edit permission
on cases, you can update or reset the time.

This field is available in API version 18.0 and later.

```
SourceId

Status

StopStartDate

Subject

SuppliedCompany

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the social post source.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The status of the case, such as New, Closed, or Escalated. This field directly controls the
`IsClosed` flag. Each predefined `Status` value implies an `IsClosed` flag value. For
more information, see CaseStatus.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time an entitlement process was stopped on the case.

This field is available in API version 18.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The subject of the case. Limit: 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Case

**Field** **Details**

**Description**
The company name that was entered when the case was created. Label is `Company` .

```
SuppliedEmail

SuppliedName

SuppliedPhone

Type

```

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The email address that was entered when the case was created. Label is `Email` .

If your organization has an active auto-response rule, `SuppliedEmail` is required when
creating a case via the API. Auto-response rules use the email in the contact specified by
`ContactId` . If no email address is in the contact record, the email specified here is used.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name that was entered when the case was created. Label is `Name` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The phone number that was entered when the case was created. Label is `Phone` .

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of case, such as `Feature Request` or `Question` .

Note: If you are importing Case data and need to set the value for an audit field, such as `CreatedDate`, contact Salesforce.
Audit fields are automatically updated during API operations unless you request to set these fields yourself.

Usage

Use the Case object to manage cases for your organization. Client applications can query, update, and delete Attachment records
associated with a case via the API.


Standard Objects Case

Assignment Rules

When you query or update a case, your client application can have the case automatically assigned to one or more User records based
on assignment rules that have been configured in the user interface. To use this feature, your client application must set either of the
following options (but not both) in the AssignmentRuleHeader used in the create or update:

**Field** **Field Type** **Details**

`assignmentRuleId` reference ID of the assignment rule to use. Can be an inactive assignment
rule. If unspecified and `useDefaultRule` is `true`, then the

default assignment rule is used. To find the ID for a given
assignment rule, query the AssignmentRule object (specifying
`RuleType="caseAssignment"` ), iterate through the
returned AssignmentRule objects, find the one you want to use,
retrieve its ID, and then specify its ID in this field in the
AssignmentRuleHeader.

`useDefaultRule` boolean

Specifies whether to use the default rule for rule-based assignment
( `true` ) or not ( `false` ). The default rule is assigned by users in
the Salesforce user interface.

For a code example that shows setting the AssignmentRuleHeader for a Lead (which is similar to setting the AssignmentRuleHeader for
a Case), see Lead.

Separating Accounts from Contacts in Cases

In releases before 8.0, the `AccountId` could not be specified, it was derived from the contact’s account. This behavior will continue
to be supported in future releases, but you can also now specify an `AccountId` . If you do not specify the `AccountId` during the
creation of a case, the value will default to the contact’s `AccountId` .

Note: When a record is updated, if the `ContactId` has not changed, then the `AccountId` is not regenerated. This prevents
the API from overwriting a value previously changed in the Salesforce user interface. However, if an API call changes the ContactId
and the `AccountId` field is empty, then the `AccountId` is generated using the contact’s account.

Using **`_case`** with Java

Depending on the development tool you use, you might need to write your application using `_case` instead of `Case`, because `case`
is a reserved word in Java.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CaseChangeEvent (API version 44.0)**
Change events are available for the object.

**CaseFeed (API version 18.0)**
Feed tracking is available for the object.


### Standard Objects CaseArticle

**CaseHistory**

History is available for tracked fields of the object.

**CaseOwnerSharingRule**

Sharing rules are available for the object.

**CaseShare**

Sharing is available for the object.

SEE ALSO:

Account

CaseMilestone

### CaseArticle

Represents the association between a Case and a KnowledgeArticle. This object is available in API version 20.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Access to this object is controlled by the parent Case and KnowledgeArticle. However, when querying, access is only controlled by the
parent Case.

Customer Portal users can't access this object.

Fields

**Field** **Details**

```
ArticleLanguage

ArticleVersionNumber

```

**Type**
picklist

**Properties**
Filter, Restricted picklist

**Description**
The language of the article associated with the case.

**Type**
int

**Properties**
Create, Group, Nillable

**Description**
The number assigned to a version of an article. This field is available in API version 24.0 and
later.


### Standard Objects CaseComment

**Field** **Details**

```
CaseId

IsSharedByEmail

KnowledgeArticleId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the Case associated with the KnowledgeArticle.

**Type**
int

**Properties**
Create, Group, Nillable

**Description**
Indicates that the article has been shared with the customer through an email.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the KnowledgeArticle associated with the Case.

This object represents the association of a knowledge article with a Case. An article is associated with a case when it’s relevant to a
specific issue, when it helps an agent solve the case, or when the agent sends the article to a customer.

You can use this object to include case-article associations in Apex and Visualforce.

You can't update this object via the API. If you attempt to create a record that matches an existing record, the create request simply
returns the existing record.

SEE ALSO:

### Case

KnowledgeArticle

### CaseComment

Represents a comment that provides additional information about the associated Case.


Standard Objects CaseComment

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CommentBody

ConnectionReceivedId

ConnectionSentId

CreatorFullPhotoUrl

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Text of the CaseComment. The maximum size of the comment body is 4,000 bytes. Label is
**Body** .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the PartnerNetworkConnection that shared this record with your organization. This
field is available if you enabled Salesforce to Salesforce.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the PartnerNetworkConnection that you shared this record with. This field is available
if you enabled Salesforce to Salesforce. This field is supported using API versions earlier than
15.0. In all other API versions, this field’s value is null. You can use the new
PartnerNetworkRecordConnection object to forward records to connections.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL of the user’s profile photo from the feed. Chatter Answers must be enabled to view this
field. This field is available in API version 26.0 and later.


Standard Objects CaseComment

**Field** **Details**

```
CreatorName

CreatorSmallPhotoUrl

IsDeleted

IsNotificationSelected

IsPublished

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Name of the user who posted the question or reply. Only the first name of internal users
(agents) appears to portal users in the feed. Chatter Answers must be enabled to view this
field. This field is available in API version 26.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL of the user’s thumbnail photo from the feed. Chatter Answers must be enabled to view
this field. This field is available in API version 26.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

**Type**
boolean

**Properties**
Create, Defaulted on create, Update

**Description**
Indicates whether an email notification is sent to the case contact when a CaseComment is
created or updated. When this field is queried, it always returns null.

This field is available only when the `Enable Case Comment Notification to`
`Contacts` setting is enabled on the Support Settings page in Setup. To send email
notifications for CaseComment, you must use the `EmailHeader triggerUserEmail` .

Available in API version 43.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


### Standard Objects CaseContactRole

**Field** **Details**

**Description**
Indicates whether the CaseComment is visible to customers in the Self-Service portal ( `true` )
or not ( `false` ). Label is **Published** . This is the only CaseComment field that can be updated
via the API.

```
ParentId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort,

**Description**
Required. ID of the parent Case of the CaseComment.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
### Case

Note: If you're importing CaseComment data and must set the value for an audit field, such as `CreatedDate`, contact Salesforce.
Record id's can't delete CaseComments entities when calling the Database.delete() Apex method or its analogous SOAP API. Audit
fields are automatically updated during API operations unless you request to set these fields yourself.

Usage

In the Salesforce user interface, comments are entered by a User working on a Case. All users have access to create and view CaseComment
in the Salesforce user interface and when using the API. In the API, CaseComment records can't be modified after insertion unless the
user has the “Modify All Records” object-level permission for Cases or the “Modify All Data” permission. If not, users can only update the
`IsPublished` field, and can't delete CaseComment.

SEE ALSO:

Overview of Salesforce Objects and Fields

### CaseContactRole

Represents the role that a given Contact plays on a Case.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`


Standard Objects CaseContactRole

Fields

**Field** **Details**

```
CasesId

ContactId

IsDeleted

Role

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the cases associated with this contact.

This is a relationship field.

**Relationship Name**
Cases

**Relationship Type**
Lookup

**Refers To**
Case

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. ID of the contact.

This is a relationship field.

**Relationship Name**
Contact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

**Type**
picklist


### Standard Objects CaseHistory

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the role played by the contact on this case, such as Technical Contact, Business
Contact, Decision Maker, and so on. Must be unique—there can't be multiple records in
which the `CaseId`, `ContactId`, and `Role` values are identical. Different contacts can
play the same role on the same case. A contact can play different roles on the same case.

Usage

Use this object to define the role that a given Case plays on a given Contact. For example, you can use this object to be able to see all
contacts who are associated to a case, or, given a contact, be able to query all cases that they are associated with, even if they are not
the primary contact on the case.

### CaseHistory

Represents historical information about changes that have been made to the associated Case.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Special Access Rules

This object is always read-only.

Fields

**Field** **Details**

```
CaseId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the Case associated with this record.

This is a relationship field.

**Relationship Name**
### Case


Standard Objects CaseHistory

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Case

```
DataType

Field

IsDeleted

NewValue

OldValue

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Data type of the field that was changed.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Name of the case field that was modified, or a special value to indicate some other
modification to the case. The possible values, in addition to the case field names, are:

**•** **ownerAssignment** —The owner of the case was changed.

**•** **ownerAccepted** —A user took ownership of a case from a queue.

**•** **ownerEscalated** —The owner of the case was changed due to case escalation.

**•** **external** —A user made the case visible to customers in the Customer Self-Service Portal.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
New value of the modified case field. Maximum of 255 characters.

**Type**
anyType


### Standard Objects CaseHistory2

**Field** **Details**

**Properties**
Nillable, Sort

**Description**
Previous value of the modified case field. Maximum of 255 characters.

Usage

Case history entries are indirectly created each time a case is modified.

Two rows are added to this record when foreign key fields change. One row contains the foreign key object names that display in the
online application. For example, `Jane Doe` is recorded as the name of a Contact. The other row contains the actual foreign key ID
that is only returned to and visible from the API.

This object respects field level security on the parent object.

SEE ALSO:

Overview of Salesforce Objects and Fields

### CaseHistory2

Represents historical information about owner and status changes that have been made to the associated Case. This object is available
in API version 59.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

This object is always read-only.

Fields

**Field** **Details**

```
CaseId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the Case associated with this record.

This is a relationship field.


Standard Objects CaseHistory2

**Field** **Details**

**Relationship Name**
Case

**Relationship Type**
Lookup

**Refers To**
Case

```
IsDeleted

OwnerId

PreviousUpdate

Status

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is `Deleted` .

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the contact who owns the case.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the case was last updated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects CaseMilestone

**Field** **Details**

**Description**
The status of the case, such as `New`, `Closed`, or `Escalated` .

Usage

CaseHistory2 entries are intended for case history reports.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CaseHistory2ChangeEvent on page 68**
Change events are available for the object in API version 60.0 or later.

### CaseMilestone

Represents a milestone (required step in a customer support process) on a Case. This object is available in API version 18.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`

Fields

**Field** **Details**

```
BusinessHoursId

CaseId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the BusinessHours associated with the CaseMilestone.

**Type**
reference

**Properties**
Filter

**Description**
ID of the case.


Standard Objects CaseMilestone

**Field** **Details**

```
CompletionDate

ElapsedTimeInDays

ElapsedTimeInHrs

ElapsedTimeInMins

IsCompleted

IsViolated

```

**Type**
dateTime

**Properties**
Filter, Nillable, Update

**Description**
The date and time the milestone was completed.

**Type**
double

**Properties**
Filter, Nillable

**Description**
The time required to complete a milestone in days.

**Type**
double

**Properties**
Filter, Nillable

**Description**
The time required to complete a milestone in hours.

**Type**
int

**Properties**
Filter, Nillable

**Description**
The time required to complete a milestone in minutes.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the milestone is completed ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the milestone is violated ( `true` ) or not ( `false` ).


Standard Objects CaseMilestone

**Field** **Details**

```
MilestoneTypeId

StartDate

TargetDate

TargetResponseInDays

TargetResponseInHrs

TargetResponseInMins

```

**Type**
reference

**Properties**
Filter, Nillable

**Description**
The ID of the milestone on the case.

**Type**
dateTime

**Properties**
Filter, Nillable, Update

**Description**
The date and time the milestone started on the case.

**Type**
dateTime

**Properties**
Filter

**Description**
The date and time the milestone must be completed.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time to complete the milestone in days.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The time to complete the milestone in hours.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The time to complete the milestone in minutes.


Standard Objects CaseMilestone

**Field** **Details**

```
TimeRemainingInDays

TimeRemainingInHrs

TimeRemainingInMins

TimeSinceTargetInDays

TimeSinceTargetInHrs

TimeSinceTargetInMins

```

**Type**
double

**Properties**
Group, Nillable, Sort

**Description**
Time remaining to reach the milestone target, measured in days.

**Type**
text

**Properties**
Nillable

**Description**
Time remaining to reach the milestone target, measured in hours.

**Type**
text

**Properties**
Group, Nillable, Sort

**Description**
Time remaining to reach the milestone target. The format is minutes and seconds.

**Type**
double

**Properties**
Nillable, Sort

**Description**
The time elapsed since the milestone target, measured in days.

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
The time elapsed since the milestone target, measured in hours.

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
The time elapsed since the milestone target. The format is minutes and seconds.


### Standard Objects CaseOwnerSharingRule

Usage

This object lets you view a milestone on a case. It also lets you view if the milestone was completed and when it must be completed.

SEE ALSO:

### Case

MilestoneType

SlaProcess

### CaseOwnerSharingRule

Represents the rules for sharing a case with users other than the owner.

Note: To enable access to this object for your org, contact Salesforce customer support. However, we recommend that you
instead use Metadata API to programmatically update owner sharing rules because it triggers automatic sharing rule recalculation.
[The SharingRules Metadata API type is enabled for all orgs.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_sharingrules.htm)

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

Customer Portal users can’t access this object.

Fields

**Field** **Details**

```
CaseAccessLevel

Description

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the type of sharing being allowed. The possible values are:

**•** `Read`

**•** `Edit`

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects CaseOwnerSharingRule

**Field** **Details**

**Description**
A description of the sharing rule. Maximum size is 1000 characters. This field is available
in API version 29.0 and later.

```
DeveloperName

GroupId

Name

UserOrGroupId

```

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with a
letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming conflicts
on package installations. With this field, a developer can change the object’s name
in a managed package and the changes are reflected in a subscriber’s organization.
Corresponds to **Rule Name** in the user interface.

This field is available in API version 24.0 and later.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is specified,
performance may slow while Salesforce generates one for each record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the source group. Cases owned by users in the source group
trigger the rule to give access.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label of the sharing rule as it appears in the user interface. Limited to 80 characters.
Corresponds to **Label** on the user interface.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects CaseParticipant

**Field** **Details**

**Description**
The ID representing the target user or group. Target users or groups are given access.

Usage

Use this object to manage the sharing rules for cases. General sharing and territory management-related sharing use this object.

SEE ALSO:

### Case

CaseShare

_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_sharingrules.htm)_ : SharingRules

### CaseParticipant

Represents a junction between a case, and an account or a contact. This object stores the details of the participant associated with a
case. This participant could be the applicant, co-applicant, a household, or even a business account. This object is available in API version
54.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Fields and values added in API version 58.0 are available if the add-on license for Financial Services Cloud is enabled.

Fields

**Field** **Details**

```
AuthorizationProof

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
How the participant communicated their consent. This field is available in API version 58.0
and later.

Possible values are:

**•** `Email Consent`


Standard Objects CaseParticipant

**Field** **Details**

**•** `Joint Ownership`

**•** `Power of Attorney`

**•** `Verbal Consent`

```
CaseId

LastReferencedDate

LastViewedDate

Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The case associated with the case participant record.

This field is a relationship field.

**Relationship Name**
Case

**Relationship Type**
Lookup

**Refers To**
Case

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
possibly the user only accessed this record or list view ( `LastReferencedDate` ) but
didn't view it.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the case participant record.


Standard Objects CaseParticipant

**Field** **Details**

```
ParticipantId

PreferredCallTimeFrom

PreferredCallTimeTo

PreferredCommunicationMode

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The participant associated with the case participant record.

This field is a polymorphic relationship field.

**Relationship Name**
Participant

**Relationship Type**
Lookup

**Refers To**
Account, Contact

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The start of the preferred time window for contacting the participant. This field is available
in API version 58.0 and later.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The end of the preferred time window for contacting the participant. This field is available
in API version 58.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
How the participant prefers to receive messages. This field is available in API version 58.0
and later.

Possible values are:

**•** `Email`

**•** `Phone`

**•** `SMS`


Standard Objects CaseParticipant

**Field** **Details**

```
Role

Status

```

Associated Objects

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The role of the case participant.

Possible values are:

**•** `Applicant`

**•** `Complainant Representative` (Available in API version 58.0 and later.)

**•** `Inspection Officer`

**•** `Lawyer`

**•** `Observer`

**•** `Perpetrator`

**•** `Primary Caretaker`

**•** `Victim`

The default value is `Applicant` .

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the case participant.

Possible values are:

**•** `Active`

**•** `Inactive`

**•** `In Review` (Available in API version 58.0 and later.)

**•** `Pending` (Available in API version 58.0 and later.)

**•** `Submitted` (Available in API version 58.0 and later.)

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CaseParticipantFeed on page 55**
Feed tracking is available for the object.

**CaseParticipantHistory on page 63**
History is available for tracked fields of the object.


### Standard Objects CaseRelatedIssue CaseRelatedIssue

This object acts as a junction between a customer issue (Case) and the Incident or Problem that represents an associated service failure.
This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CaseId

Name

RelatedEntityType

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
A relationship field that represents the case you're linking a Problem or Incident to.

**Relationship Name**
### Case

**Relationship Type**
Lookup

**Refers To**
### Case

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
A brief description of the related case.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Shows what type of object the related entity is.

Possible values are:

**•** `Incident`

**•** `Problem`


Standard Objects CaseRelatedIssue

**Field** **Details**

```
RelatedIssueId

RelationshipType

UniqueKeyIndex

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
A polymorphic relationship field that represents a related Problem or Incident.

**Relationship Name**
RelatedIssue

**Relationship Type**
Lookup

**Refers To**
Incident, Problem

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Shows how two records relate to each other.

Possible values are:

**•** `Root Cause`

**•** `Similar`

The default value is 'Root Cause'.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
This field is unique within your organization.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CaseRelatedIssueChangeEvent on page 68 (API version 59.0)**
Change events are available for the object.

**CaseRelatedIssueFeed on page 55**
Feed tracking is available for the object.


### Standard Objects CaseShare

**CaseRelatedIssueHistory on page 63**
History is available for tracked fields of the object.

### CaseShare

Represents a sharing entry on a Case.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`describeSObjects()`, `create()`, `delete()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Summer ’20 and later, only users with access to the Case object can access this object.

Fields

The properties available for some fields depend on the default organization-wide sharing settings. The properties listed are true for the
default settings of such fields.

**Field** **Details**

```
CaseAccessLevel

CaseId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Level of access that the User or Group has to the Case. The possible values are:

**•** `Read`

**•** `Edit`

**•** `All` This value isn’t valid for creating or deleting records.

This field must be set to an access level that is higher than the organization’s default access
level for cases.

**Type**
reference


Standard Objects CaseShare

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the Case associated with this sharing entry. This field can't be updated.

This is a relationship field.

**Relationship Name**
Case

**Relationship Type**
Lookup

**Refers To**
Case

```
IsDeleted

RowCause

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only permitted
value is `Manual` . If no value is specified, the field defaults to `Manual` . All other `RowCause`
values are read-only. After the sharing entry is created, this field can’t be edited.

Valid values include:

**•** `Manual` —The User or Group has access because a user with “All” access manually
shared the Case with them.

**•** `Owner` —The User is the owner of the Case.

**•** `ImplicitChild` —The User or Group has access to the Case on the Account
associated with this Case. After faster account sharing recalculation is enabled for your
org, sharing entries with this value aren’t returned in queries. Instead of storing implicit
child shares, record access is determined dynamically.

**•** `RelatedPortalUser` —The portal user is the contact on the Case.

**•** `Rule` —The User or Group has access via a Case sharing rule.

**•** `GuestRule` —The User or Group has access via a Case guest user sharing rule.

**•** `Team` —The User or Group has team access.


### Standard Objects CaseSolution

**Field** **Details**

**•** `LpuImplicit` —The User has access to records owned by high-volume Experience
Cloud site users via a share group.

**•** `ARImplicit` —The User, who belongs to a partner or customer account, has access
to the Case via an account relationship data sharing rule.

```
UserOrGroupId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the User or Group that has been given access to the Case. This field can't be updated.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User

This object allows you to determine which users and groups can view and edit Case records owned by other users. If you attempt to
create a record that matches an existing record, request updates any modified fields and returns the existing record.

Note: After faster account sharing recalculation is enabled for your org, we no longer store implicit share records between accounts
and their child case records. Sharing entries that have a value of `ImplicitChild` in the `RowCause` field aren’t returned
when you query this object. Instead, the system dynamically determines whether users can access child case records when they
try to access them. This change speeds up ownership and sharing recalculation for accounts.

[For more information, see the Faster Account Sharing Recalculation knowledge article.](https://help.salesforce.com/s/articleView?id=000394638&type=1&language=en_US)

SEE ALSO:

AccountShare

LeadShare

OpportunityShare

### CaseSolution

Represents the association between a Case and a Solution.


Standard Objects CaseSolution

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
CaseId

IsDeleted

SolutionId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the Case associated with the Solution.

This is a relationship field.

**Relationship Name**
Case

**Relationship Type**
Lookup

**Refers To**
Case

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the Solution associated with the case.

This is a relationship field.

**Relationship Name**
Solution

**Relationship Type**
Lookup

**Refers To**
Solution


### Standard Objects CaseStatus

Usage

You can't update this object via the API. If you attempt to create a record that matches an existing record, the request simply returns
the existing record.

SEE ALSO:

CaseShare

SolutionStatus

### CaseStatus

Represents the status of a Case, such as New, On Hold, or In Process.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ApiName

IsClosed

IsDefault

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Uniquely identifies a picklist value so it can be retrieved without using an id or primary label.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this case status value represents a closed Case ( `true` ) or not ( `false` ).
Multiple case status values can represent a closed Case.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


### Standard Objects CaseSubjectParticle

**Field** **Details**

**Description**
Indicates whether this is the default case status value ( `true` ) or not ( `false` ) in the picklist.

```
 MasterLabel

 SortOrder

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Label for this case status value. This display value is the internal label that does not get
translated.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number used to sort this value in the case status picklist. These numbers are not guaranteed
to be sequential, as some previous case status values might have been deleted.

This object represents a value in the case status picklist. The case status picklist provides additional information about the status of a
Case, such as whether a given `Status` value represents an open or closed case. Query the CaseStatus object to retrieve the set of
values in the case status picklist, and then use that information while processing Case records to determine more information about a
given case. For example, the application could test whether a given case is open or closed based on its `Status` value and the value
of the `IsClosed` property in the associated CaseStatus object.

SEE ALSO:

Overview of Salesforce Objects and Fields

### CaseSubjectParticle

Represents the Social Business Rules custom format for the **Case Subject** field on cases created from inbound social posts. This object
is available in API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects CaseSubjectParticle

Fields

**Field** **Details**

```
DeveloperName

Index

Language

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name for the CaseSubjectParticle object.

This name can contain only underscores and alphanumeric characters, and must be unique
in your org. It must begin with a letter, not include spaces, not end with an underscore, and
not contain two consecutive underscores. This field is automatically generated, but you can
supply your own value if you create the record using the API.

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance may slow while
Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
int

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. The order in which the custom **Case Subject** is generated, meaning if the social
network is 0 and the social message is 1, then the subject generates as `Twitter |`
`Tweet` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the case subject field.

Possible values are:

**•** `ar` —Arabic

**•** `da` —Danish

**•** `de` —German

**•** `en_US` —English

**•** `es` —Spanish

**•** `es_MX` —Spanish (Mexico)


Standard Objects CaseSubjectParticle

**Field** **Details**

**•** `fi` —Finnish

**•** `fr` —French

**•** `it` —Italian

**•** `iw` —Hebrew

**•** `ja` —Japanese

**•** `ko` —Korean

**•** `nl_NL` —Dutch

**•** `no` —Norwegian

**•** `pt_BR` —Portuguese (Brazil)

**•** `ru` —Russian

**•** `sv` —Swedish

**•** `th` —Thai

**•** `zh_CN` —Chinese (Simplified)

**•** `zh_TW` —Chinese (Traditional)

```
MasterLabel

TextField

Type

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for the case subject field.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies inbound social content added to **Case Subject** in case records.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. Specifies the custom **Case Subject** format from which inbound social content
appears in case records.

Possible values are:

**•** `ColonSeparator`

**•** `Content` —Message

**•** `HyphenSeparator`


### Standard Objects CaseTag

**Field** **Details**

**•** `MessageType`

**•** `PipeSeparator`

**•** `ProvidedString`

**•** `RealName`

**•** `Sentiment`

**•** `SocialHandle`

**•** `SocialNetwork`

**•** `Source`

Usage

In the Salesforce UI, case subjects are brief descriptions of cases. They are what agents see on cases first. Social Business Rules specify
the brief descriptions of cases created from social posts. Using CaseSubjectParticle objects you can build your own case subject format,
where each object represents a social post's component. For example, combining CaseSubjectParticle objects with components for
types `MessageType`, `RealName`, and `SocialNetwork` results in "Tweet Customer123 Twitter".

### CaseTag

Associates a word or short phrase with a Case

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
ItemId

Name

```

**Type**
reference

**Properties**
Create, Filter

**Description**
ID of the tagged item.

**Type**
string

**Properties**
Create, Filter


### Standard Objects CaseTeamMember

**Field Name** **Details**

**Description**
Name of the tag. If this value does not already exist, a new TagDefinition is created and
becomes the parent of this Tag object. Otherwise, a TagDefinition with the same name
becomes the parent of this Tag object. Parent relationships are created automatically.

```
TagDefinitionId

Type

```

Usage

**Type**
reference

**Properties**
Filter

**Description**
ID of the parent TagDefinition object that owns the tag.

**Type**
picklist

**Properties**
Create, Filter, Restricted picklist

**Description**
Defines the visibility of a tag.

Valid values:

**•** `Public` —The tag can be viewed and manipulated by all users in an organization.

**•** `Personal` —The tag can be viewed or manipulated only by a user with a matching
`OwnerId` .

CaseTag stores the relationship between its parent TagDefinition and the Case being tagged. Tag objects act as metadata, allowing users
to describe and organize their data.

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.

### CaseTeamMember

Represents a case team member, who works with a team of other users to help resolve a case.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
upsert()

```


Standard Objects CaseTeamMember

Special Access Rules

As of Spring ’20 and later, only users with read access to the Case object can access this object.

When accessing from Apex code, use the `WITH USER_MODE` clause to enable field-level and object-level security permissions checking
for `SOQL SELECT` [queries, including subqueries and cross-object relationships. See Enforce User Mode for Database Operations.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_classes_enforce_usermode.htm)

Fields

**Field** **Details**

```
MemberId

ParentId

TeamRoleId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the user or contact who is a member on a case team.

This is a polymorphic relationship field.

**Relationship Name**
Member

**Relationship Type**
Lookup

**Refers To**
Contact, User

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the case with which the case team member is associated.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Case

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects CaseTeamMember

**Field** **Details**

**Description**
The ID of the case team role with which the case team member is associated.

This is a relationship field.

**Relationship Name**
TeamRole

**Relationship Type**
Lookup

**Refers To**
CaseTeamRole

```
TeamTemplateId

TeamTemplateMemberId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the predefined team with which the case team member is associated.

This is a relationship field.

**Relationship Name**
TeamTemplate

**Relationship Type**
Lookup

**Refers To**
CaseTeamTemplate

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the team member included in a predefined case team.

This is a relationship field.

**Relationship Name**
TeamTemplateMember

**Relationship Type**
Lookup

**Refers To**
CaseTeamTemplateMember


### Standard Objects CaseTeamRole CaseTeamRole

Represents a case team role. Every case team member has a role on a case, such as “Customer Contact” or “Case Manager.”

Supported Calls

`create()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Spring ’20 and later, only users with read access to the Case object can access this object.

Fields

**Field** **Details**

```
AccessLevel

Name

PreferencesVisibleInCSP

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the type of access granted to the target Group for cases. The possible
values are:

**•** `None`

**•** `Read`

**•** `Edit`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the case team role.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether or not the case team role is visible to Customer Portal users.


### Standard Objects CaseTeamTemplate CaseTeamTemplate

Represents a predefined case team, which is a group of users that helps resolve a case.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

As of Spring ’20 and later, only users with read access to the Case object can access this object.

Fields

**Field** **Details**

```
Description

Name

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A text description of the predefined case team.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the predefined case team.

### CaseTeamTemplateMember

Represents a member on a predefined case team, which is a group of users that helps resolve cases.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
upsert()

```

Special Access Rules

As of Spring ’20 and later, only users with read access to the Case object can access this object.


### Standard Objects CaseTeamTemplateRecord

Fields

**Field** **Details**

```
MemberId

TeamRoleId

TeamTemplateId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the user or contact who is a team member on a predefined case team.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the predefined case team member's case team role.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the predefined case team's template.

### CaseTeamTemplateRecord

The CaseTeamTemplateRecord object is a linking object between the Case and CaseTeamTemplate objects. To assign a predefined case
team to a case (customer inquiry), create a CaseTeamTemplateRecord record and point the `ParentId` to the case and the
`TeamTemplateId` to the predefined case team.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

As of Spring ’20 and later, only users with read access to the Case object can access this object.


### Standard Objects CategoryData

Fields

**Field** **Details**

```
ParentId

TeamTemplateId

### CategoryData

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the case with which the case team template record is associated.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Case

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the predefined case team with which the case team template record is associated.

This is a relationship field.

**Relationship Name**
TeamTemplate

**Relationship Type**
Lookup

**Refers To**
CaseTeamTemplate

Represents a logical grouping of Solution records.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
upsert()

```


Standard Objects CategoryData

Special Access Rules

Customer Portal users can't access this object.

Fields

**Field** **Details**

```
 CategoryNodeId

 IsDeleted

 RelatedSobjectId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the CategoryNode associated with the solution.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the solution related to the category.

This object allows you to assign one or more categories to a Solution. It is an intermediate data table with two foreign keys that defines
the relationship between a CategoryNode and a Solution record.

CategoryData has two foreign keys:

**•** The first foreign key, `CategoryNodeId`, refers to the ID of a CategoryNode.

**•** The other foreign key, `RelatedSobjectId`, refers to a Solution ID.

This is a many-to-many relationship, so there can be multiple rows returned with a `CategoryNodeId` . A Solution can be associated
with multiple categories.

SEE ALSO:

Overview of Salesforce Objects and Fields


### Standard Objects CategoryNode CategoryNode

Represents a tree of Solution categories.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

**•** Customer Portal users can't access this object.

**•** Attempting to delete a CategoryNode that has children (referred by CategoryNode.Parent), or is referred to elsewhere, causes a
failure.

Fields

**Field** **Details**

```
MasterLabel

ParentId

SortOrder

SortStyle

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for the category node.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the parent of this node, if any.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the sort order of child CategoryNode objects.

**Type**
picklist


### Standard Objects CategoryNodeLocalization

**Field** **Details**

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates whether the sort order is alphabetical or custom.

Usage

A CategoryNode defines a category of solutions. In the user interface, you can edit category definitions from Setup by entering _`Solution`_
_`Categories`_ in the `Quick Find` box, then selecting **Solution Categories** .

SEE ALSO:

CategoryData

Solution

### CategoryNodeLocalization

When the Translation Workbench is enabled for your organization, the CategoryNodeLocalization object provides the translation of the
label of a solution category.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

**•** Your organization must be using Professional, Enterprise, Developer, Unlimited, or Performance Edition and be enabled for the
Translation Workbench.

**•** To view this object, you must have the “View Setup and Configuration” permission.

Fields

**Field** **Details**

```
CategoryNodeId

```

**Type**
reference

**Properties**
Create, Filter, Nillable

**Description**
The ID of the solution CategoryNode that is being translated.


Standard Objects CategoryNodeLocalization

**Field** **Details**

```
LanguageLocaleKey

Language

```

**Type**
picklist

**Properties**
Create, Filter, Nillable, Restricted picklist

**Description**

This field is available in API version 16.0 and earlier. It is the same as the `Language`
field.

**Type**
picklist

**Properties**
Create, Filter, Nillable, Restricted picklist

**Description**

This field is available in API version 17.0 and later. The combined language and locale
ISO code, which controls the language for labels displayed in an application.

This picklist contains the following fully-supported languages:

**•** Chinese (Simplified): `zh_CN`

**•** Chinese (Traditional): `zh_TW`

**•** Danish: `da`

**•** Dutch: `nl_NL`

**•** English: `en_US`

**•** Finnish: `fi`

**•** French: `fr`

**•** German: `de`

**•** Italian: `it`

**•** Japanese: `ja`

**•** Korean: `ko`

**•** Norwegian: `no`

**•** Portuguese (Brazil): `pt_BR`

**•** Russian: `ru`

**•** Spanish: `es`

**•** Spanish (Mexico): `es_MX` Spanish (Mexico) defaults to Spanish for
customer-defined translations.

**•** Swedish: `sv`

**•** Thai: `th` The Salesforce user interface is fully translated to Thai, but Help is in
English.

The following end-user only languages are available.

**•** Arabic: `ar`

**•** Bulgarian: `bg`


Standard Objects CategoryNodeLocalization

**Field** **Details**

**•** Croatian: `hr`

**•** Czech: `cs`

**•** English (UK): `en_GB`

**•** Greek: `el`

**•** Hebrew: `iw`

**•** Hungarian: `hu`

**•** Indonesian: `in`

**•** Polish: `pl`

**•** Portuguese (European): `pt_PT`

**•** Romanian: `ro`

**•** Slovak: `sk`

**•** Slovenian: `sl`

**•** Turkish: `tr`

**•** Ukrainian: `uk`

**•** Vietnamese: `vi`

The following platform languages are available for organizations that use Salesforce
exclusively as a platform.

**•** Albanian: `sq`

**•** Afrikaans: `af`

**•** Amharic: `am`

**•** Arabic (Algeria): `ar_DZ`

**•** Arabic (Bahrain): `ar_BH`

**•** Arabic (Egypt): `ar_EG`

**•** Arabic (Iraq): `ar_IQ`

**•** Arabic (Jordan): `ar_JO`

**•** Arabic (Kuwait): `ar_KW`

**•** Arabic (Lebanon): `ar_LB`

**•** Arabic (Libya): `ar_LY`

**•** Arabic (Morocco): `ar_MA`

**•** Arabic (Oman): `ar_OM`

**•** Arabic (Qatar): `ar_QA`

**•** Arabic (Saudi Arabia): `ar_SA`

**•** Arabic (Sudan): `ar_SD`

**•** Arabic (Syria): `ar_SY`

**•** Arabic (Tunisia): `ar_TN`

**•** Arabic (United Arab Emirates): `ar_AE`

**•** Arabic (Yemen): `ar_YE`

**•** Armenian: `hy`


Standard Objects CategoryNodeLocalization

**Field** **Details**

**•** Basque: `eu`

**•** Bosnian: `bs`

**•** Bengali: `bn`

**•** Burmese: `my`

**•** Catalan: `ca`

**•** Chinese (Hong Kong): `zh_HK`

**•** Chinese (Singapore): `zh_SG`

**•** Chinese (Malaysia): `zh_MY`

**•** Dutch (Belgium): `nl_BE`

**•** English (Australia): `en_AU`

**•** English (Belgium): `en_BE`

**•** English (Canada): `en_CA`

**•** English (Cyprus): `en_CY`

**•** English (Germany): `en_DE`

**•** English (Hong Kong): `en_HK`

**•** English (India): `en_IN`

**•** English (Ireland): `en_IE`

**•** English (Israel): `en_IL`

**•** English (Malaysia): `en_MY`

**•** English (Malta): `en_MT`

**•** English (Netherlands): `en_NL`

**•** English (New Zealand): `en_NZ`

**•** English (Philippines): `en_PH`

**•** English (Singapore): `en_SG`

**•** English (South Africa): `en_ZA`

**•** English (United Arab Emirates): `en_AE`

**•** Estonian: `et`

**•** Farsi: `fa`

**•** French (Belgium): `fr_BE`

**•** French (Canada): `fr_CA`

**•** French (Luxembourg): `fr_LU`

**•** French (Morocco): `fr_MA`

**•** French (Switzerland): `fr_CH`

**•** Georgian: `ka`

**•** German (Austria): `de_AT`

**•** German (Belgium): `de_BE`

**•** German (Luxembourg): `de_LU`

**•** German (Switzerland): `de_CH`


Standard Objects CategoryNodeLocalization

**Field** **Details**

**•** Greek (Cyprus): `el_CY`

**•** Greenlandic: `kl`

**•** Gujarati: `gu`

**•** Hawaiian: `haw`

**•** Haitian Creole: `ht`

**•** Hindi: `hi`

**•** Hmong: `hmn`

**•** Icelandic: `is`

**•** Irish: `ga`

**•** Italian (Switzerland): `it_CH`

**•** Kannada: `kn`

**•** Kazakh: `kk`

**•** Khmer: `km`

**•** Latvian: `lv`

**•** Lithuanian: `lt`

**•** Luxembourgish: `lb`

**•** Macedonian: `mk`

**•** Malay: `ms`

**•** Malayalam: `ml`

**•** Maltese: `mt`

**•** Marathi: `mr`

**•** Montenegrin: `sh_ME`

**•** Punjabi: `pa`

**•** Romanian (Moldova): `ro_MD`

**•** Romansh: `rm`

**•** Russian (Armenia): `ru_AM`

**•** Russian (Belarus): `ru_BY`

**•** Russian (Kazakhstan): `ru_KZ`

**•** Russian (Kyrgyzstan): `ru_KG`

**•** Russian (Lithuania): `ru_LT`

**•** Russian (Moldova): `ru_MD`

**•** Russian (Poland): `ru_PL`

**•** Russian (Ukraine): `ru_UA`

**•** Samoan: `sm`

**•** Serbian (Cyrillic): `sr`

**•** Serbian (Latin): `sh`

**•** Spanish (Argentina): `es_AR`

**•** Spanish (Bolivia): `es_BO`


Standard Objects CategoryNodeLocalization

**Field** **Details**

**•** Spanish (Chile): `es_CL`

**•** Spanish (Colombia): `es_CO`

**•** Spanish (Costa Rica): `es_CR`

**•** Spanish (Dominican Republic): `es_DO`

**•** Spanish (Ecuador): `es_EC`

**•** Spanish (El Salvador): `es_SV`

**•** Spanish (Guatemala): `es_GT`

**•** Spanish (Honduras): `es_HN`

**•** Spanish (Nicaragua): `es_NI`

**•** Spanish (Panama): `es_PA`

**•** Spanish (Paraguay): `es_PY`

**•** Spanish (Peru): `es_PE`

**•** Spanish (Puerto Rico): `es_PR`

**•** Spanish (United States): `es_US`

**•** Spanish (Uruguay): `es_UY`

**•** Spanish (Venezuela): `es_VE`

**•** Swahili: `sw`

**•** Tagalog: `tl`

**•** Tamil: `ta`

**•** Te reo: `mi`

**•** Telugu: `te`

**•** Urdu: `ur`

**•** Welsh: `cy`

**•** Xhosa: `xh`

**•** Yiddish: `ji`

**•** Zulu: `zu`

The values in this field are not related to the default locale selection.

```
NamespacePrefix

```

**Type**
string

**Properties**
Filter, Nillable

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org
that creates a managed package has a unique namespace prefix. Limit: 15 characters.
You can refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values.


### Standard Objects ChangeRequest

**Field** **Details**

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix
of the org for all objects that support it, unless an object is in an installed managed
package. In that case, the object has the namespace prefix of the installed
managed package. This field’s value is the namespace prefix of the Developer
Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only
for objects that are part of an installed managed package. All other objects have
no namespace prefix.

```
 Value

```

Usage

**Type**
string

**Properties**
Create, Filter, Nillable, Update

**Description**
The actual translated label for the solution category. Label is **Translation** .

Use this object to translate the labels of your solution categories into a supported language. Users with the Translation Workbench
enabled can view category node translations, but either the “Customize Application,” “Manage Translation,” or “Manage Categories”
permission is required to create or update category node translations.

SEE ALSO:

ScontrolLocalization

WebLinkLocalization

### ChangeRequest

Represents a decision to implement a formal request for a change (RFC). This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
BusinessJustification

```

**Type**
textarea


Standard Objects ChangeRequest

**Field** **Details**

**Properties**
Create, Nillable, Update

**Description**
A description of the business reason to implement the change. This field can store up to 32
KB of data, but only the first 255 characters display in reports.

```
BusinessReason

Category

ChangeRequestNumber

ChangeType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The core reason for creating the change request.

Possible values are:

**•** `t2`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of change request. Administrators set field values.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique, system-generated change request number.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of change request. Administrators set field values.

Possible values are:

**•** `Emergency`

**•** `Major`

**•** `Normal`

**•** `Standard`


Standard Objects ChangeRequest

**Field** **Details**

```
Description

EstimatedEndTime

EstimatedStartTime

FinalReviewDateTime

FinalReviewNotes

Impact

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the change request. This field can store up to 32 KB of data, but only the
first 255 characters display in reports.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time (in UTC) when the change request is estimated to be implemented.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The estimated date and time (in UTC) when the change request is implemented.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time (in UTC) when the change request was reviewed.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Notes left by the change request reviewer. This field can store up to 32 KB of data, but only
the first 255 characters display in reports.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects ChangeRequest

**Field** **Details**

**Description**
Shows the impact of a requested change.

Possible values are:

**•** `High`

**•** `Low`

**•** `Medium`

The default value is 'High'.

```
LastReferencedDate

LastViewedDate

OwnerId

Priority

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view ( `LastReferencedDate` ) but
not viewed it.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
A polymorphic relationship field that represents the user or group assigned as the change
reviewer.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist


Standard Objects ChangeRequest

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The impact and urgency of a requested change.

Possible values are:

**•** `Critical`

**•** `High`

**•** `Low`

**•** `Moderate`

The default value is 'Critical'.

```
RemediationPlan

ReviewerId

RiskImpactAnalysis

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the steps required to resolve the incident. This field can store up to 32 KB
of data, but only the first 255 characters display in reports.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the user who reviewed the change request.

This is a relationship field.

**Relationship Name**
Reviewer

**Relationship Type**
Lookup

**Refers To**
User

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
An assessment of the risk involved with the implementation of the change request.
Administrators set field values, and each value can have up to 20 characters.


Standard Objects ChangeRequest

**Field** **Details**

```
RiskLevel

Status

StatusCode

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The risk level associated with adopting the requested change.

Possible values are:

**•** `High`

**•** `Low`

**•** `Medium`

The default value is 'High'.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Represents any custom or granular stages a customer may want to track. This will be a
dependent picklist.

Possible values are:

**•** `Approved`

**•** `Canceled`

**•** `Closed`

**•** `Implementing`

**•** `New`

**•** `Open`

**•** `Planning`

**•** `Rejected`

**•** `Reviewed`

**•** `Scheduled`

The default value is 'New'.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the change.

Possible values are:


### Standard Objects ChangeRequestRelatedIssue

**Field** **Details**

**•** `Approved`

**•** `Canceled`

**•** `Closed`

**•** `Implementing`

**•** `New`

**•** `Open`

**•** `Planning`

**•** `Rejected`

**•** `Reviewed`

**•** `Scheduled`

The default value is 'New'.

```
Subject

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A brief description of the requested change.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ChangeRequestChangeEvent on page 68 (API version 59.0)**
Change events are available for the object.

**ChangeRequestFeed on page 55**
Feed tracking is available for the object.

**ChangeRequestHistory on page 63**
History is available for tracked fields of the object.

**ChangeRequestOwnerSharingRule on page 65**
Sharing rules are available for the object.

**ChangeRequestShare on page 67**
Sharing is available for the object.

### ChangeRequestRelatedIssue

Represents a junction object that relates a ChangeRequest to an Incident or Problem due to a service failure. This object is available in
API version 53.0 and later.


Standard Objects ChangeRequestRelatedIssue

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ChangeRequestId

Name

RelatedEntityType

RelatedIssueId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ChangeRequest ID that's linked to the Problem or Incident.

**Relationship Name**
ChangeRequest

**Relationship Type**
Lookup

**Refers To**
ChangeRequest

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
A description of the change request as it relates to the problem or incident.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The name of the related object type.

Possible values are:

**•** `Incident`

**•** `Problem`

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects ChangeRequestRelatedItem

**Field** **Details**

**Description**
A polymorphic relationship field that represents the related Problem or Incident.

**Relationship Name**
RelatedIssue

**Relationship Type**
Lookup

**Refers To**
Incident, Problem

```
RelationshipType

```

Associated Objects

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Shows how the ChangeRequest and Incident or Problem records relate to each other.

Possible values are:

**•** `Caused By`

**•** `Fixed By`

The default value is 'Caused By'.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ChangeRequestRelatedIssueChangeEvent on page 68**
Change events are available for the object.

**ChangeRequestRelatedIssueFeed on page 55**
Feed tracking is available for the object.

**ChangeRequestRelatedIssueHistory on page 63**
History is available for tracked fields of the object.

### ChangeRequestRelatedItem

Represents a junction object that relates a ChangeRequest to an Asset. This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`


Standard Objects ChangeRequestRelatedItem

Fields

**Field** **Details**

```
AssetId

ChangeRequestId

Comment

ImpactLevel

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The Asset ID that’s linked to the ChangeRequest.

This field is a relationship field.

**Relationship Name**
Asset

**Relationship Type**
Lookup

**Refers To**
Asset

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ChangeRequest ID that’s linked to the Asset.

This field is a relationship field.

**Relationship Name**
ChangeRequest

**Relationship Type**
Lookup

**Refers To**
ChangeRequest

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the change request as it relates to the item.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update


Standard Objects ChangeRequestRelatedItem

**Field** **Details**

**Description**
The related item's impact on the change request.

Possible values are:

**•** `High`

**•** `Low`

**•** `Medium`

The default value is `High` .

```
Name

RelationshipType

```

Associated Objects

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated ID of the item that's related to the change request.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Shows how the ChangeRequest and Asset records relate to each other.

Possible values are:

**•** `Broke Item`

**•** `Fixed Item`

The default value is `Broke Item` .

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ChangeRequestRelatedItemChangeEvent on page 68**
Change events are available for the object.

**ChangeRequestRelatedItemFeed on page 55**
Feed tracking is available for the object.

**ChangeRequestRelatedItemHistory on page 63**
History is available for tracked fields of the object.


### Standard Objects ChangeSetOperationEventLog ChangeSetOperationEventLog

Change Set Operation events contain information from change set migrations. This object is available in API version 65.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ChangeSetName

ClientIp

CpuTime

LoginKey

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the change set.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ChangeSetOperationEventLog

**Field** **Details**

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring.

```
OperationType

RequestIdentifier

RunTime

SessionKey

TargetOrganizationIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operation that’s being performed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same REQUEST_ID.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The amount of time that the request took in milliseconds.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the organization that’s receiving the change set.


### Standard Objects ChannelObjectLinkingRule

**Field** **Details**

```
Timestamp

Uri

UserIdentifier

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp at which the log event was generated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URI of the page receiving the request.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.
For example: `00530000009M943` .

### ChannelObjectLinkingRule

Represents a rule for linking a channel interaction with an object (such as Lead or Contact). This object is available in API version 47.0
and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ActionForNoRecordFound

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects ChannelObjectLinkingRule

**Field** **Details**

**Description**
Action to take when no matching records are found.

Possible values are:

**•** `CreateNewRecordAndLink` —Create Record and Link (Recommended)

**•** `PromptAgent` —Prompt Agent

```
ActionForSingleRecordFound

ChannelType

Description

DeveloperName

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Action to take when one matching record is found.

Possible values are:

**•** `AutoLink` —Auto-Link Record (Recommended)

**•** `PromptAgent` —Prompt Agent

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of channel used for this rule.

Possible values are:

**•** `FacebookMessenger`

**•** `Phone`

**•** `Text`

**•** `WeChat`

**•** `WhatsApp`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description for this linking rule.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects ChannelObjectLinkingRule

**Field** **Details**

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance may slow while
Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

```
IsLinkedRecordOpenedAsSubTab

IsRuleActive

Language

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether to open the linked record as a subtab when the link is established.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the rule is active.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language for this linking rule.

Possible values are:

**•** `ar` —Arabic

**•** `bg` —Bulgarian

**•** `cs` —Czech

**•** `da` —Danish

**•** `de` —German

**•** `el` —Greek

**•** `en_GB` —English (UK)


Standard Objects ChannelObjectLinkingRule

**Field** **Details**

**•** `en_US` —English

**•** `es` —Spanish

**•** `es_MX` —Spanish (Mexico)

**•** `fi` —Finnish

**•** `fr` —French

**•** `hr` —Croatian

**•** `hu` —Hungarian

**•** `in` —Indonesian

**•** `it` —Italian

**•** `iw` —Hebrew

**•** `ja` —Japanese

**•** `ko` —Korean

**•** `nl_NL` —Dutch

**•** `no` —Norwegian

**•** `pl` —Polish

**•** `pt_BR` —Portuguese (Brazil)

**•** `pt_PT` —Portuguese (European)

**•** `ro` —Romanian

**•** `ru` —Russian

**•** `sk` —Slovak

**•** `sl` —Slovene

**•** `sv` —Swedish

**•** `th` —Thai

**•** `tr` —Turkish

**•** `uk` —Ukrainian

**•** `vi` —Vietnamese

**•** `zh_CN` —Chinese (Simplified)

**•** `zh_TW` —Chinese (Traditional)

```
MasterLabel

ObjectToLink

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique label name for this rule.

**Type**
picklist


### Standard Objects ChannelProgram

**Field** **Details**

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of object to link to the channel interaction.

Possible values are:

**•** `Contact`

```
 RuleName

### ChannelProgram

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Name of the rule as it appears in the UI. Maximum length is 80 characters.

Represents a channel program that vendors use to market and sell their products through channel partners. This object is available in
API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
Category

Description

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Category of the channel program. Categories group channel programs by type.
For example, a reseller category would include all the different regional reseller
channel programs.

**Type**
textarea


Standard Objects ChannelProgram

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the channel program.

```
IsActive

LastReferencedDate

LastViewedDate

Name

OwnerId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the channel program is active. New channel programs are
inactive by default.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related
to this record, or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, the user might have only accessed this record or list view
( `LastReferencedDate` ) but not viewed it.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Name of the channel program.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


### Standard Objects ChannelProgramLevel

**Field Name** **Details**

**Description**
ID of the owner of the channel program.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ChannelProgramFeed**

Feed tracking is available for the object.

**ChannelProgramHistory**

History is available for tracked fields of the object.

**ChannelProgramOwnerSharingRule**

Sharing rules are available for the object.

**ChannelProgramShare**

Sharing is available for the object.

### ChannelProgramLevel

Represents a level, based on member experience, in a channel program. This object is available in API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
Description

LastReferencedDate

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the channel program level.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects ChannelProgramLevel

**Field Name** **Details**

**Description**
The timestamp when the current user last accessed this record, a record related
to this record, or a list view.

```
LastViewedDate

Name

OwnerId

ProgramId

Rank

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, the user might have only accessed this record or list view
( `LastReferencedDate` ) but not viewed it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the channel program level.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. ID of the user who is the owner of the record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the channel program.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An integer associated with the level. For example, 1 represents the lowest level,
2 the next level up, etc.


### Standard Objects ChannelProgramMember

**Field Name** **Details**

```
RecordTypeId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the record type assigned to this object.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ChannelProgramLevelFeed**

Feed tracking is available for the object.

**ChannelProgramLevelHistory**

History is available for tracked fields of the object.

**ChannelProgramLevelOwnerSharingRule**

Sharing rules are available for the object.

**ChannelProgramLevelShare (API version 43.0)**
Sharing is available for the object.

### ChannelProgramMember

Represents a partner who is a member of a channel program. This object is available in API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
LastReferencedDate

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Most recent date referenced. This field is available in API version 45.0 and later.


Standard Objects ChannelProgramMember

**Field Name** **Details**

```
LastViewedDate

LevelId

Name

OwnerId

PartnerId

ProgramId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Most recent date viewed. This field is available in API version 45.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the channel program level.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the channel program member.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. ID of the user who is the owner of the record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the partner.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the channel program.


### Standard Objects ChatterActivity

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ChannelProgramMemberFeed (API version 46.0)**
Feed tracking is available for the object.

**ChannelProgramMemberHistory (API version 46.0)**
History is available for tracked fields of the object.

**ChannelProgramMemberOwnerSharingRule**

Sharing rules are available for the object.

**ChannelProgramMemberShare (API version 43.0)**
Sharing is available for the object.

### ChatterActivity ChatterActivity represents the number of posts and comments made by a user and the number of comments and likes on posts and

comments received by the same user. This object is available in API version 23.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
CommentCount

CommentReceivedCount

InfluenceRawRank

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of FeedComments made by the ParentId.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of FeedComments received by the ParentId.

**Type**
int

**Properties**
Filter, Group, Sort


Standard Objects ChatterActivity

**Field Name** **Details**

**Description**
Number indicating the ParentId’s Chatter influence rank, which is calculated based
on the ParentId’s ChatterActivity statistics, relative to the other users in the
organization. This field is available in API version 26.0 and later.

```
LikeReceivedCount

NetworkId

ParentId

PostCount

```

Usage

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of FeedLikes received by the ParentId.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Experience Cloud site to which the ChatterActivity belongs. This field is
available only if digital experiences is enabled in your org. This field is available in API
version 26.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the object type to which the ChatterActivity is related. In API version 66.0, the
`ParentId` must be a `UserId` or SelfServiceUser ID.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of FeedItems made by the ParentId.

**•** Use this object to reference the Chatter activity statistics, which include the number of posts and comments made by a user and
the number of comments and likes on posts and comments received by the same user.


### Standard Objects ChatterAnswersActivity

**•** You can directly query for ChatterActivity.

```
     SELECT Id, PostCount, LikeReceivedCount

     FROM ChatterActivity

     WHERE ParentId = UserId

```

Note: To query ChatterActivity, you must provide the `ParentId` . In API version 66.0, the `ParentId` must be a `UserId`
or SelfServiceUser ID.

**•** A ChatterActivity record is created for users the first time they post or comment. Users who have never posted or commented don’t
have ChatterActivity records. If users make only one post and then delete it, they do have ChatterActivity records. In both cases, the
user interface displays zeros for their Chatter activity.

**•** Use the `InfluenceRawRank` field to reference a user’s Chatter influence rank. This field is available in API version 26.0 and later.

SEE ALSO:

FeedItem

FeedComment

FeedLike

### ChatterAnswersActivity

Represents the reputation of a User in Chatter Answers zones.This object is available in API version 25.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
BestAnswerReceivedCount

BestAnswerSelectedCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of best answers the User has received from other users.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of best answers the User has selected.


Standard Objects ChatterAnswersActivity

**Field Name** **Details**

```
QuestionsCount

QuestionSubscrCount

QuestionSubscrReceivedCount

QuestionUpVotesCount

QuestionUpVotesReceivedCount

RepliesCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of Question records posted by the User.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of Question records the User has selected to follow.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of users following Question records posted by the User.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of up votes the User has marked on Question records posted by
other users.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of up votes the User has received from other users on the Question
records he or she has posted.

**Type**
int


Standard Objects ChatterAnswersActivity

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of Reply records posted by the User.

```
ReplyDownVotesCount

ReplyDownVotesReceivedCount

ReplyUpVotesCount

ReplyUpVotesReceivedCount

ReportAbuseOnQuestionsCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of down votes the User has marked on Reply records posted by
other users.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of down votes the User has received from other users on the Reply
records he or she has posted.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of up votes the User has marked on the Reply records posted by
other users.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of up votes the User has received from other users on the Reply
records he or she has posted.

**Type**
int


Standard Objects ChatterAnswersActivity

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of abuses that the User has reported on Question records posted
by other users.

```
ReportAbuseOnRepliesCount

ReportAbuseReceivedOnQnCount

ReportAbuseReceivedOnReCount

UserId

CommunityId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of abuses that the User has reported on Reply records posted by
other users.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of abuses reported by other users on the Question records posted
by the User.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

the number of abuses reported by other users on the Reply records posted by
the User.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The User ID associated with this reputation.

**Type**
reference


### Standard Objects ChatterAnswersReputationLevel

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**

The ID for the zone associated with this reputation.

Usage

Use this object to view metrics on User activity in Chatter Answers. For example, you can use the ChatterAnswersActivity object to view
the number of Question records a user is following in Chatter Answers zones.

SEE ALSO:

Question

Reply

User

### ChatterAnswersReputationLevel

Represents a reputation level within a Chatter Answers zone. This object is available in API version 26.0 and later.

Note: With the Spring ’18 release, Salesforce no longer supports Chatter Answers. Users of Chatter Answers can post, answer,
comment, or view existing Chatter Answers data, but support and updates are scheduled to end. We recommend transitioning
[to Chatter Questions. For more information, see End of Support for Chatter Answers in Spring ’18.](https://help.salesforce.com/apex/HTViewSolution?urlname=Chatter-Answers-to-Retire-in-Spring-18)

Supported Calls

`create()`, `delete()`, `query()`, `retrieve()`, `update()`

Fields

**Field** **Details**

```
CommunityID

Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

ID of the zone for which you’re creating the reputation level.

**Type**
string


### Standard Objects ChatterConversation

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**

Name of the reputation level.

```
Value

```

Usage

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**

Minimum number of points for this level.

Use to create or edit reputation levels for the zone.

### ChatterConversation

Represents a private conversation in Chatter, consisting of messages that conversation members have sent or received. This object is
available in API version 23.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
Id

```

**Type**
ID

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
ID of the conversation.


### Standard Objects ChatterConversationMember

Usage

Use this object to identify private conversations in Chatter. Users can access this object if they have the Manage Chatter Messages and
Direct Messages permission. This object is read-only via the API and is provided only to allow administrators to view users' Chatter
messages; for example, for compliance purposes.

SEE ALSO:

### ChatterConversationMember

ChatterMessage

### ChatterConversationMember

Represents a member of a private conversation in Chatter. A member has either sent messages to or received messages from other
conversation participants. This object is available in API version 23.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
ConversationId

MemberId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the associated ChatterConversation.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the conversation member.


### Standard Objects ChatterExtension

Usage

Use this object to view members of private conversations in Chatter. Users can access this object if they have the Manage Chatter
Messages and Direct Messages permission. This object is read-only via the API and is provided only to allow administrators to view users'
Chatter messages; for example, for compliance purposes.

SEE ALSO:

ChatterConversation

ChatterMessage

### ChatterExtension

Represents a Rich Publisher App that’s integrated with the Chatter publisher. This object is available in API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CompositionComponentEnumOrId

Description

DeveloperName

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ID of the composition component for the Rich Publisher App. This field requires a value.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The description of your custom Rich Publisher App. This field requires a value.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the developer who is responsible for the app.


Standard Objects ChatterExtension

**Field** **Details**

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

```
ExtensionName

HeaderText

HoverText

IconId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of your extension. This field requires a value.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The text to show in the header of your app composer. Header text is required for Lightning
type extensions.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The text to show when a user mouses over your extension’s icon. Mouse-over text is required
for Lightning type extensions.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The icon to show in the Chatter publisher. Use an existing file asset ID from your org. This
field requires a value.

This is a relationship field.

**Relationship Name**
Icon

**Relationship Type**
Lookup

**Refers To**
ContentAsset


Standard Objects ChatterExtension

**Field** **Details**

```
IsProtected

Language

MasterLabel

NamespacePrefix

RenderComponentEnumOrId

Type

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
An auto-generated value. It currently has no impact.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language used for this instance of the `ChatterExtension` . This field requires a
value.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The master label for the `ChatterExtension` object. This field requires a value.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The prefix to use for the extension’s namespace.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The rendering component of the Rich Publisher App that you provide. It’s comprised of the
`lightning:availableForChatterExtensionRenderer` interface. This field
requires a value.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


### Standard Objects ChatterExtensionConfig

**Field** **Details**

**Description**
Describes the type of the extension. Currently, the only value supported is _`Lightning`_ .
Included to allow for other possible types in the future.

### ChatterExtensionConfig

Configuration for the Chatter extension for Experience Cloud sites. This object is available in API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CanCreate

CanRead

ChatterExtensionId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
### Determines whether the ChatterExtension can create an instance that appears by

rendering.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
### Determines whether the ChatterExtension can be viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
### The ID of the ChatterExtension .

This is a relationship field.

**Relationship Name**
### ChatterExtension


### Standard Objects ChatterMessage

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
ChatterExtension

```
NetworkId

Position

### ChatterMessage

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Experience Cloud site where the `ChatterExtension` is deployed.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The position of the `ChatterExtension` icon in the Chatter publisher.

Represents a message sent as part of a private conversation in Chatter. This object is available in API version 23.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`

Fields

**Field Name** **Details**

```
Body

ConversationId

```

**Type**
textarea

**Properties**
Update

**Description**
Text of the message.

**Type**
reference


Standard Objects ChatterMessage

**Field Name** **Details**

**Properties**
Filter, Group, Sort

**Description**
ID of the conversation that the message is associated with.

```
SenderId

SenderNetworkId

SentDate

```

Usage

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the sender.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Experience Cloud site from which the message was sent. This field is
available only if digital experiences is enabled in your org.

This field is available in API version 32.0 and later.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
Date the message was sent.

Use this object to view and delete messages sent or received via private conversations in Chatter. Users can access this object if they
have the Manage Chatter Messages and Direct Messages permission. Users with the Moderate Experiences Chatter Messages permission
can access this object in Experience Cloud sites they’re a member of, only if the message has been flagged as inappropriate. This object
is provided to allow administrators to view and delete users’ Chatter messages, for example, for compliance purposes.

Messages are hard deleted. That is, they’re removed completely without a trip to the Recycle Bin.

Deleting a message that resulted from sharing a file with someone doesn’t also delete the file.

SEE ALSO:

ChatterConversation

ChatterConversationMember


### Standard Objects ClientBrowser ClientBrowser

Represents a cookie added to the browser upon login, and also includes information about the browser application where the cookie
was inserted. This object is available in version 28.0 and later.

Supported Calls

`describeSObjects()`, `delete()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
FullUserAgent

LastUpdate

ProxyInfo

UsersId

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Detailed information about the client (browser). For example, `Mozilla/5.0`

```
  (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.1)

  Gecko/2008070208 Firefox/3.0.1

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Represents the last time the cookie was changed.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The browser’s current proxy information.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user associated with this item.

This is a relationship field.


### Standard Objects CollaborationGroup

**Field** **Details**

**Relationship Name**
Users

**Relationship Type**
Lookup

**Refers To**
User

Usage

At every login, the device the login request is from is checked against the known devices using ClientBrowser. A match means a cookie
was found on the browser that matches an entry in the ClientBrowser table, so the device is known. No match means that no matching
cookie was found, so the device is unknown, and the user is asked to confirm their identity.

### CollaborationGroup

Represents a Chatter group. This object is available in API version 19.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `search()`, `update()`,

```
   upsert()

```

Special Access Rules

The visibility of information in groups depends on the type of group and the user’s permissions.

**•** **Members** : Any user with the Create and Own New Chatter Groups permission can create public, private, and unlisted groups,
including in any Experience Cloud sites they belong to.

**•** **Owners and managers** : Users can modify group details for any group they own or manage. Owners can also delete groups they
own.

**•** **Nonmembers** : These user permissions allow group access regardless of group membership.

**–** View All Data—Allows users to view all public and private groups across their org and its Experience Cloud sites. Users with this
permission can’t view unlisted group information, unless they have the Modify Unlisted Groups permission as well.

**–** Modify All Data—Allows users to view, modify, and delete all public and private groups across their org and its Experience Cloud
sites. Users with this permission can’t view or modify unlisted group information, unless they have the Manage Unlisted Groups
permission as well.

**–** Create and Set Up Experiences—Allows users to view, modify, and delete all public and private groups in Experience Cloud sites.

**–** Manage Unlisted Groups—Allows users to search for, access, and modify any unlisted group in an org and its Experience Cloud
sites.

**–** Data Export—Allows users to export any data from Salesforce, including private and unlisted group data from an org and its
Experience Cloud sites.


Standard Objects CollaborationGroup

**•** **Apex and Visualforce** : Apex code runs in system mode, which means that the permissions of the current user aren’t taken into
account.

**–** Visualforce pages that display groups might expose unlisted or private group data to users who aren’t members.

**–** Because system mode disregards the user’s permissions, all users who are accessing a Visualforce page that’s showing a group
can act as an owner of that group.

**–** AppExchange apps that are written in Apex and that access all groups will expose unlisted groups to users who aren’t members.

To limit and manage access to the unlisted and private groups in your org:

**•** Explicitly filter out unlisted and private group information from SOQL queries in all Apex code.

**•** Use permission sets, profile-level permissions, and sharing checks in your code to further limit group access.

**•** Use Apex triggers on the CollaborationGroup object to monitor and manage the creation of groups. In Setup, enter _`Group`_
_`Triggers`_ in the `Quick Find` box, then select **Group Triggers** to add triggers.

Fields

**Field** **Details**

```
AnnouncementId

BannerPhotoUrl

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Contains the ID of the Announcement last associated with the group. This field is available
in API version 30.0 and later.

This is a relationship field.

**Relationship Name**
Announcement

**Relationship Type**
Lookup

**Refers To**
Announcement

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL for the group's banner photo.

The URL is updated every time a photo is uploaded and reflects the most recent photo. If a
newer photo has been uploaded, the URL returned for an older photo is not guaranteed to
return a photo. Query this field for the URL of the most recent photo.

This field is available in API version 36.0 and later.


Standard Objects CollaborationGroup

**Field** **Details**

```
CanHaveGuests

CollaborationType

Description

FullPhotoUrl

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If set to `true`, indicates that a group allows customers. Chatter customers are people outside
your company's email domains. Customers can see only the groups they're invited to. They
can interact only with members of those groups. Customers can’t see any Salesforce
information.

This field is available starting in API version 23.0, but groups that allow customers are
accessible from earlier API versions. However, when accessed from earlier API versions, groups
that allow customers aren't distinguishable from private groups. We strongly recommend
that you upgrade to the latest API version. If you must use an earlier version, name groups
that allow customers to indicate that they include customers.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of Chatter group. Available values are:

**•** `Public` —Anyone can see and post updates. Anyone can join a public group.

**•** `Private` —Only members can see the group feed and post updates. Non-members
can only see the group name and a few other details in list views, search, and on the
group page. The group's owner or managers must add members who request to join
the group.

**•** `Unlisted` —Only members and users with the Manage Unlisted Groups permission
can see the group and post updates. Other users can’t access the group or see it in lists,
search, and feeds.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the group.

**Type**
url

**Properties**
Filter, Nillable, Sort


Standard Objects CollaborationGroup

**Field** **Details**

**Description**
The URL for the group's profile photo.

The URL is updated every time a photo is uploaded and reflects the most recent photo. If a
newer photo has been uploaded, the URL returned for an older photo is not guaranteed to
return a photo. Query this field for the URL of the most recent photo.

This field is available in API version 20.0 and later.

```
GroupEmail

HasPrivateFieldsAccess

InformationBody

InformationTitle

```

**Type**
email

**Properties**
Nillable, Sort

**Description**
The email address for posting to the group. For private groups, only visible to members and
users with Modify All Data or View All Data permissions.

This field is available in API version 29.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If set to `true`, indicates that a user can see the `InformationBody` and
`InformationTitle` fields in a private group. This field is set to `true` for members of
a private group and users with Modify All Data or View All Data permissions.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The text of the Information section. For private groups, only visible to members and users
with Modify All Data or View All Data permissions.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The title of the Information section. For private groups, only visible to members and users
with Modify All Data or View All Data permissions.


Standard Objects CollaborationGroup

**Field** **Details**

```
IsArchived

IsAutoArchiveDisabled

IsBroadcast

LastFeedModifiedDate

LastReferencedDate

LastViewedDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the group is archived ( `true` ) or not ( `false` ).

This field is available in API version 28.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether automatic archiving is disabled for the group ( `true` ) or not ( `false` ).

This field is available in API version 29.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the group is a broadcast group ( `true` ) or not ( `false` ).

This field is available in API version 36.0 and later.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date of the last post or comment on the group.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
datetime


Standard Objects CollaborationGroup

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced ( `LastReferencedDate` ) and not viewed.

```
MediumPhotoUrl

MemberCount

Name

NetworkId

OwnerId

```

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL for the larger, cropped photo size.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of members in the group.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the group. Group names must be unique across public and private groups. Unlisted
groups don’t require unique names.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the Experience Cloud site that this group is part of. This field is available only if digital
experiences is enabled in your org.

You can only add a `NetworkId` when creating a group. You can’t change or add a
`NetworkId` for an existing group. This field is available in API version 26.0 and later.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects CollaborationGroup

**Field** **Details**

**Description**
ID of the owner of the group. Only the current group owner or people with the Modify All
Data permission can update the `OwnerId` .

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

```
SmallPhotoUrl

```

Usage

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
The URL for a thumbnail of the group's profile photo.

The URL is updated every time a photo is uploaded and reflects the most recent photo. If a
newer photo has been uploaded, the URL returned for an older photo is not guaranteed to
return a photo. Query this field for the URL of the most recent photo.

This field is available in API version 20.0 and later.

Use this object to create, edit, or delete groups in an org or Experience Cloud site. Deleting a group permanently deletes all posts and
comments to the group. It also deletes all files and links posted to the group and removes the files from other locations where they were
shared.

As a Chatter group member, you can post to the group using the CollaborationGroupFeed object. As a Chatter group owner or manager,
you can add or remove group members using the CollaborationGroupMember object, post announcements to the group using the
Announcement object, and accept or decline requests to join private groups using the CollaborationGroupMemberRequest object.
Additionally, the group owner, manager, or your Salesforce system administrator can invite people to join the group using the
CollaborationInvitation object.

The Salesforce system administrator doesn’t need to be a member of the group in order to send invitations using the API.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.


### Standard Objects CollaborationGroupMember

**CollaborationGroupFeed**

Feed tracking is available for the object.

SEE ALSO:

### CollaborationGroupMember CollaborationGroupMemberRequest CollaborationGroupMember

Represents a member of a Chatter group. This object is available in API version 19.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `describeLayout()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CollaborationGroupId

CollaborationRole

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the associated CollaborationGroup.

This is a relationship field.

**Relationship Name**
### CollaborationGroup

**Relationship Type**
Lookup

**Refers To**
### CollaborationGroup

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The role of a group member. Group owners and managers can change roles for members
of their groups. The valid values are:


Standard Objects CollaborationGroupMember

**Field** **Details**

**•** `Standard` —Indicates that a user is a group member. Members can post and comment
in the group.

**•** `Admin` —Indicates that a user is a group manager. Managers can post and comment,
change member roles, edit group settings, add and remove members, delete posts and
comments, and edit the group information field.

Note: To change the group owner, use the `OwnerId` field on the
CollaborationGroup object.

```
LastFeedAccessDate

MemberId

NotificationFrequency

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when a group member last accessed the group’s feed. The value is only
updated when a member explicitly consumes the group’s feed, not when the member sees
group posts in other feeds, like the profile feed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the group member.

This is a relationship field.

**Relationship Name**
Member

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Required. The frequency at which Salesforce sends Chatter group email digests to this
member. Can only be set by the member or users with the “Modify All Data” permission.
The valid values are:

**•** `D` —Daily

**•** `W` —Weekly


### Standard Objects CollaborationGroupMemberRequest

**Field** **Details**

**•** `N` —Never

**•** `P` —On every post

The default value is specified by the member in their Chatter email settings. In communities,
the `Email on every post` option is disabled once more than 10,000 members
choose this setting for the group. All members who had this option selected are automatically
switched to `Daily digests` .

Usage

Use this object to view, create, and delete Chatter group members. You must be a group owner or manager to create members for
private Chatter groups.

SEE ALSO:

### CollaborationGroup CollaborationGroupMemberRequest CollaborationGroupMemberRequest

Represents a request to join a private Chatter group. This object is available in API version 21.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CollaborationGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the private Chatter group.

This is a relationship field.

**Relationship Name**
### CollaborationGroup

**Relationship Type**
Lookup


Standard Objects CollaborationGroupMemberRequest

**Field** **Details**

**Refers To**
CollaborationGroup

```
RequesterId

ResponseMessage

Status

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the user requesting to join the group; must be the ID of the context user.

This is a relationship field.

**Relationship Name**
Requester

**Relationship Type**
Lookup

**Refers To**
User

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Optional message to be included in the notification email when `Status` is `Declined` .

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the request. Available values are:

**•** `Accepted`

**•** `Declined`

**•** `Pending`

This object represents a request to join a private Chatter group, and can be used to accept or decline requests to join private groups you
own or manage. On create, an email is sent to the owner and managers of the private group to be accepted or declined. When the
`Status` is `Accepted` or `Declined`, an email is sent to notify the requester. When the `Status` is `Declined`, a
`ResponseMessage` is optionally included to provide additional details.


### Standard Objects CollaborationGroupRecord

Note the following when working with requests:

**•** Users with the “Modify All Data” or “View All Data” permission can view records for all groups, regardless of membership.

**•** A user can be a member of 300 groups. Requests to join groups count against this limit.

**•** `Status` can't be specified on create.

**•** You can only update a request when the `Status` is `Pending` .

**•** You can't delete or update a request with a `Status` of `Accepted` or `Declined` .

SEE ALSO:

### CollaborationGroup

CollaborationGroupMember

### CollaborationGroupRecord

Represents the records associated with Chatter groups.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CollaborationGroupId

NetworkId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the Chatter group.

This is a relationship field.

**Relationship Name**
### CollaborationGroup

**Relationship Type**
Lookup

**Refers To**
### CollaborationGroup

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects CollaborationInvitation

**Field** **Details**

**Description**
Optional. The ID of the Experience Cloud site that the group belongs to. Available from API
version 34.0.

```
RecordId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The ID of the record associated with the Chatter group.

This is a polymorphic relationship field.

**Relationship Name**
Record

**Relationship Type**
Lookup

**Refers To**
Account, Campaign, Case, Contact, Contract, Lead, Opportunity

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CollaborationGroupRecordChangeEvent (API version 62.0)**
Change events are available for the object.

### CollaborationInvitation

Represents an invitation to join Chatter, either directly or through a group. This object is available in API version 21.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Invitations are available if “Allow Invitations” is enabled for your organization.

Invitations are limited to your allowed domain(s) unless the invite is sent from a private group that allows customers. Allowed domains
are set by the administrator.

Invitations to customers are available if “Allow Customer Invitations” is enabled for your organization. Users must have the “Invite
Customers to Chatter” permission to send invitations to people outside their Chatter domain.


Standard Objects CollaborationInvitation

Fields

**Field** **Details**

```
InvitedUserEmail

InvitedUserEmailNormalized

InviterId

OptionalMessage

ParentId

SharedEntityId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The email address for the user invited to join Chatter. Label is `Invited Email` .

**Type**
email

**Properties**
Filter, Group, Sort

**Description**
A normalized version of the `InvitedUserEmail` entered. Label is `Invited Email`
`(Normalized)` .

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The person that initiated the invitation.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
An optional message from the person sending the invitation to the person receiving it.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Used when the email address on the invitation is different than the one entered when the
invitee accepts the invitation.

**Type**
reference


Standard Objects CollaborationInvitation

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the user or group associated with this invitation.

**•** If the invitation is to join Chatter, the `SharedEntityId` is the ID of the User that
created the invitation. The invitee will auto-follow the inviter.

**•** If the invitation is to join a group within Chatter, the `SharedEntityId` is the ID of
the Chatter CollaborationGroup.

**•** To invite a customer, set `SharedEntityId` to the ID of the private
CollaborationGroup with Allow Customers turned on.

```
Status

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the invitation. Possible values are:

**•** `Sent`

**•** `Accepted`

**•** `Canceled`

Use this object to create or delete (cancel) invitations to join Chatter. You can either invite a user to join Chatter directly or as part of a
CollaborationGroup.

Note: To invite someone to join a CollaborationGroup, you must be either the owner or a manager of the group or a Salesforce
system administrator.

The Salesforce system administrator doesn’t need to be a member of the group in order to send invitations using the API.

When the person accepts your CollaborationGroup invitation, they join the CollaborationGroup and Chatter as well.

Note: You can't send invitations to users of the organization the invite was sent from.

Invited users can view profiles, post on their feed, and join groups, but they can't see your Salesforce data or records.

If your organization allows groups with customers, owners and managers of private groups with the “Allow Customers” setting, as well
as system administrators, can use this object to invite customers.

Java Samples

The following example shows how to send an invitation to join Chatter:

```
public void invitePeople(String inviterUserId, String invitedEmail) throws Exception {

   CollaborationInvitation invitation = new CollaborationInvitation();

```


### Standard Objects CollaborationRoom

```
      invitation.setSharedEntityId(inviterUserId);//pass the userId of the inviter

      invitation.setInvitedUserEmail(invitedEmail);//email of the invited user

      insert(invitation);

   }

```

The following example shows how to send an invitation to a customer user from a group that allows customers:

```
   public void inviteToGroup(String GroupName, String invitedEmail) throws Exception {

      QueryResult qr = query("select id from collaborationgroup where name = '" +

        GroupName); //pass the group name

      String groupId = qr.getRecords()[0].getId();

      CollaborationInvitation invitation = new CollaborationInvitation();

      invitation.setSharedEntityId(groupId);//pass the groupId

      invitation.setInvitedUserEmail(invitedEmail);//email of the invited user

      insert(invitation);

   }

```

Apex Samples

```
   String emailAddress = 'bob@external.com';

   CollaborationGroup chatterGroup = [SELECT Id

       FROM CollaborationGroup

       WHERE Name='All acme.com'

       LIMIT 1];

   CollaborationInvitation inv = New CollaborationInvitation();

   inv.SharedEntityId = chatterGroup.id;

   inv.InvitedUserEmail = emailAddress;

   try {

     Insert inv;

   } catch(DMLException e){

     System.debug('There was an error with the invite: '+e);

   }

### CollaborationRoom

```

Represents a collaboration room, which links Salesforce to a Slack channel used by applications with specific use cases, such as swarming
or reporting. This object is available in API version 55.0 and later.

Supported Calls

`create()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `update()`, `upsert()`

Special Access Rules

To access this object, enable the Slack Terms of Service and one of:

**•** Sales Cloud for Slack App

**•** Service Cloud for Slack App


Standard Objects CollaborationRoom

**•** CRM Analytics for Slack App

**•** Industries Cloud for Slack App

**•** Health Cloud for Slack App

Fields

**Field** **Details**

```
IsArchived

IsAutoJoin

IsExternal

LastReferencedDate

LastViewedDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the collaboration room is archived ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether new users automatically join the collaboration room. Used for Sales Cloud
for Slack App.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether external users are members of the Slack channel ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime


### Standard Objects CollabDocumentMetric

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when the current user last viewed this record or list view. If this value is null, the
user might have only accessed this record or list view ( `LastReferencedDate` ) but not
viewed it.

```
Name

PlatformKey

TeamKey

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of collaboration room.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the Slack channel.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the Slack workspace.

### CollabDocumentMetric

Represents the engagement metrics for a Quip thread (document or spreadsheet) that’s linked to a Salesforce record. This object is
available in API version 50.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects CollabDocumentMetric

Fields

**Field** **Details**

```
Document

Site

SourceTemplate

DocumentTitle

MetricDate

MetricDateOnly

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The Quip thread ID.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Quip site in which the thread is located.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the template (if any) on which a Quip thread is based.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The title of the thread.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the metric was gathered in your local time zone.

**Type**
date

**Properties**
Filter, Nillable, Sort


Standard Objects CollabDocumentMetric

**Field** **Details**

**Description**
The date that the metric was gathered in UTC. Available in API version 55.0 and later.

```
LastUpdatedDate

LastUpdatedDateOnly

ViewerCount

UpdateCount

EditorCount

CommenterCount

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the thread was created, last edited, or last shared in your local time zone.

**Type**
date

**Properties**
Filter, Nillable, Sort

**Description**
The date that the thread was created, last edited, or last shared in UTC. Available in API version
55.0 and later.

**Type**
int

**Properties**
Filter, Nillable, Sort

**Description**
The number of thread views by user for the specified MetricDate.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of edits made on the thread on a given day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
For the specified MetricDate, the number of users who edited the Quip thread.

**Type**
int


### Standard Objects CollabDocumentMetricRecord

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
For the specified MetricDate, the number of users who commented on the Quip thread.

### CollabDocumentMetricRecord

Represents an association between a CollabDocumentMetric and a Salesforce record.It tracks which Salesforce record, such as an Account
or Contact, is linked to a Quip thread for which metrics were gathered using CollabDocumentMetric. CollabDocumentMetricRecord is
available in API version 50.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ParentRecord

QuipDocumentMetric

MetricDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Salesforce record.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the CollabDocumentMetric record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the metric was gathered in your local time zone.


### Standard Objects CollabTemplateMetric

**Field** **Details**

```
MetricDateOnly

EntityType

```

**Type**
date

**Properties**
Filter, Nillable, Sort

**Description**
The date that the metric was gathered in UTC. Available in API version 55.0 and later.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The object type of the Salesforce record, such as Account or Contact.

### CollabTemplateMetric

Represents the engagement metrics for a Quip template.This object is available in API version 50.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
Template

TemplateTitle

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the template.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The title of the template.


Standard Objects CollabTemplateMetric

**Field** **Details**

```
Site

MetricDate

MetricDateOnly

LastUpdatedDate

LastUpdatedDateOnly

TotalDocumentCount

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Quip site on which the template is available.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the metric was gathered in your local time zone.

**Type**
date

**Properties**
Filter, Nillable, Sort

**Description**
The date that the metric was gathered in UTC. Available in API version 55.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the thread was created, last edited, or last shared in your local time zone.

**Type**
date

**Properties**
Filter, Nillable, Sort

**Description**
The date that the thread was created, last edited, or last shared in UTC. Available in API version
55.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects CollabTemplateMetricRecord

**Field** **Details**

**Description**
The number of documents created based on the template.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CollabTemplateMetricChangeEvent (API version 62.0)**
Change events are available for the object.

### CollabTemplateMetricRecord

Represents an association between a CollabTemplateMetric and a Salesforce record.It tracks which Salesforce record, such as an Account
or Contact, is linked to a Quip template for which metrics were gathered using CollabTemplateMetric. CollabTemplateMetricRecord is
available in API version 50.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ParentRecord

QuipDocumentMetric

MetricDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Salesforce record.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the CollabTemplateMetric record.

**Type**
dateTime


### Standard Objects CollabUserEngagementMetric

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date that the metric was gathered in your local time zone.

```
MetricDateOnly

EntityType

```

**Type**
date

**Properties**
Filter, Nillable, Sort

**Description**
The date that the metric was gathered in UTC. Available in API version 55.0 and later.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The object type of the Salesforce record, such as Account or Contact.

### CollabUserEngagementMetric

Represents the user engagement metrics for a Quip thread in a Quip template or document. This object is available in API version 50.0
and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
CommentCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of comments by the user for the specified `MetricDate` .


Standard Objects CollabUserEngagementMetric

**Field** **Details**

```
EditCount

MetricDate

MetricDateOnly

Name

QuipThread

QuipThreadTitle

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of edits by the user for the specified `MetricDate` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the metric was gathered in your local time zone.

**Type**
date

**Properties**
Filter, Nillable, Sort

**Description**
The date that the metric was gathered in UTC. Available in API version 55.0 and later.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique name of the CollabUserEngagementMetric object.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The Quip thread ID.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The title of the Quip document, sheet, slide, and so forth.


Standard Objects CollabUserEngagementMetric

**Field** **Details**

```
QuipThreadType

QuipUser

SalesforceUserId

Site

SourceTemplate

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of Quip thread. The possible values are:

**•** `CHAT`

**•** `DOCUMENT`

**•** `SHEET`

**•** `SLIDE`

**•** `TEMPLATE`

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the Quip user.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Salesforce user.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Quip site.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The ID of the source template.


### Standard Objects CollabUserEngmtRecordLink

**Field** **Details**

```
ViewCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of views by the user for the specified `MetricDate` .

### CollabUserEngmtRecordLink

Represents an association between a CollabUserEngagementMetric and a Salesforce record. It tracks which Salesforce record, such as
an Account or Contact, is associated with the user engagement metric. This object is available in API version 50.0 and later.

Note: The CollabUserEngmtRecordLink object is now deprecated. You can still access user engagement metrics for metric dates
before August 12, 2021. To obtain user engagement metric for dates starting from August 12, 2021, follow the instructions in the
[Quip Engagement Metrics documentation.](https://help.salesforce.com/articleView?id=xcloud.quip_template_metrics.htm&type=5&language=en_US)

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
MetricDate

Name

ObjectType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date of the gathered metric.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique name of the CollabUserEngmtRecordLink object.

**Type**
string


### Standard Objects ColorDefinition

**Field** **Details**

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The object type of the Salesforce record, such as Account or Contact.

```
ParentRecordId

UserEngagementMetricId

### ColorDefinition

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Salesforce record.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the CollabUserEngagementMetric record.

Represents the color-related metadata for a custom tab. This object is available in API version 43.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Fields

**Field Name** **Details**

### `Color`

```
Context

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The color described in web color RGB format—for example, “00FF00”.

**Type**
string


### Standard Objects ContCalloutSummaryEventLog

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**

The color context, which determines whether the color is the main color (or
primary) for the tab.

```
DurableId

TabDefinitionId

Theme

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

A unique virtual Salesforce ID for the color.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

The `TabDefinition` ID.

This is a relationship field.

**Relationship Name**
TabDefinition

**Relationship Type**
Lookup

**Refers To**
TabDefinition

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The icon’s theme.

### ContCalloutSummaryEventLog

Continuation Callout Summary events contain information about all of the asynchronous callouts performed during a transaction, their
response status codes, execution times, and URL endpoint destinations. This object is available in API version 65.0 and later.


Standard Objects ContCalloutSummaryEventLog

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
ContinuationIdentifier

Duration

IsSuccess

OriginRequestIdentifier

RequestFormSize

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A unique ID identifying a sequence of events within a request.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Total duration of continuation, in milliseconds.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the continuation was successful or not.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the request that initiated a callout.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ContCalloutSummaryEventLog

**Field** **Details**

**Description**
Continuation request form size, in bytes. Depending on how many HTTP requests were used
in a continuation, this field can contain up to three space-separated values.

```
RequestIdentifier

ResponseSize

StatusCode

Timestamp

Url

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same REQUEST_ID.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The size of the callout response, in bytes. Depending on how many HTTP requests were used
in a continuation, this field can contain up to three space-separated values.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The HTTP status or internal code returned by the remote endpoint. A status code of 200
indicates that the request was successful. Other status code values indicate the type of
problem that was encountered. Depending on how many HTTP requests were used in a
continuation, this field can contain up to three space-separated values.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example, `20130715233322.670` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects CombinedAttachment

**Field** **Details**

**Description**
The callout endpoint URL. Depending on how many HTTP requests were used in a
continuation, this field can contain up to three space-separated values.

```
UserIdentifier

VisualforceControllerSize

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.
For example: `00530000009M943` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Continuation Visualforce controller size, in bytes. Depending on how many HTTP requests
were used in a continuation, this field can contain up to three space-separated values.

### CombinedAttachment

This read-only object contains all notes, attachments, Google Docs, documents uploaded to libraries in Salesforce CRM content, and
files added to Chatter that are associated with a record.

Supported Calls

```
describeSObjects()

```

Fields

**Field Name** **Details**

```
ContentSize

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The size of the document in bytes for documents smaller than 2 GB.


Standard Objects CombinedAttachment

**Field Name** **Details**

In API version 66.0 and later, we recommend that you use the
`ContentSizeLong` field even for documents smaller than 2 GB.

```
ContentSizeLong

ContentUrl

ExternalDataSourceName

ExternalDataSourceType

FileExtension

```

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**

The size of the document in bytes up to 10 GB.

This field is available in API version 66.0 and later.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL for links and Google Docs. This field is set only for links and Google Docs,
and is one of the fields that determine the `FileType` .

This field is available in API version 31.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the external data source in which the document is stored. This field
is set only for external documents that are connected to Salesforce.

This field is available in API version 32.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Type of external data source in which the document is stored. This field is set
only for external documents that are connected to Salesforce.

This field is available in API version 35.0 and later.

**Type**
string


Standard Objects CombinedAttachment

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**

File extension of the document.

This field is available in API version 31.0 and later.

```
FileType

ParentId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Type of document, which is determined by the file extension.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

The ID of the parent object.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, ActivationTarget, ActivationTrgtIntOrgAccess,
ApiAnomalyEventStore, AssessmentIndicatorDefinition, AssessmentTask,
AssessmentTaskContentDocument, AssessmentTaskDefinition,
AssessmentTaskIndDefinition, AssessmentTaskOrder, Asset, AssetRelationship,
AssignedResource, Award, BoardCertification, BusinessLicense, BusinessMilestone,
BusinessProfile, Campaign, CareBarrier, CareBarrierDeterminant, CareBarrierType,
CareDeterminant, CareDeterminantType, CareDiagnosis, CareInterventionType,
CareMetricTarget, CareObservation, CareObservationComponent,
CarePgmProvHealthcareProvider, CarePreauth, CarePreauthItem, CareProgram,
CareProgramCampaign, CareProgramEligibilityRule, CareProgramEnrollee,
CareProgramEnrolleeProduct, CareProgramEnrollmentCard, CareProgramGoal,
CareProgramProduct, CareProgramProvider, CareProgramTeamMember,
CareProviderAdverseAction, CareProviderFacilitySpecialty,
CareProviderSearchableField, CareRegisteredDevice, CareRequest,
CareRequestDrug, CareRequestExtension, CareRequestItem, CareSpecialty,
CareSpecialtyTaxonomy, CareTaxonomy, Case, CodeSet, CollaborationGroup,
CommSubscription, CommSubscriptionChannelType, CommSubscriptionConsent,


Standard Objects CombinedAttachment

**Field Name** **Details**

CommSubscriptionTiming, ConsumptionSchedule, Contact, ContactEncounter,
ContactEncounterParticipant, ContentWorkspace, Contract, ConversationEntry,
CoverageBenefit, CoverageBenefitItem, CredentialStuffingEventStore, CreditMemo,
CreditMemoLine, Dashboard, DashboardComponent, DataStream,
DelegatedAccount, DocumentChecklistItem, EmailMessage, EmailTemplate,
EngagementChannelType, EnhancedLetterhead, EnrollmentEligibilityCriteria,
Event, HealthcareFacility, HealthcareFacilityNetwork, HealthcarePayerNetwork,
HealthcarePractitionerFacility, HealthcareProvider, HealthcareProviderNpi,
HealthcareProviderSpecialty, HealthcareProviderTaxonomy, Identifier,
IdentityDocument, Image, IndividualApplication, Invoice, InvoiceLine, Lead,
ListEmail, Location, MarketSegment, MarketSegmentActivation, MemberPlan,
MessagingSession, MktCalculatedInsight, OperatingHours, Opportunity, Order,
OrderItem, Organization, OtherComponentTask, PartyConsent, PersonEducation,
PersonLanguage, PersonLifeEvent, PersonName, PlanBenefit, PlanBenefitItem,
Product2, ProductFulfillmentLocation, ProductItem, ProductItemTransaction,
ProductRequest, ProductRequestLineItem, ProductRequired, ProductTransfer,
ProfileSkill, ProfileSkillEndorsement, ProfileSkillUser, ProviderSearchSyncLog,
PurchaserPlan, PurchaserPlanAssn, ReceivedDocument, Report,
ReportAnomalyEventStore, ResourceAbsence, ResourcePreference, ReturnOrder,
ReturnOrderLineItem, ServiceAppointment, ServiceResource, ServiceResourceSkill,
ServiceTerritory, ServiceTerritoryMember, ServiceTerritoryWorkType,
SessionHijackingEventStore, Shift, Shipment, ShipmentItem, Site, SkillRequirement,
SocialPost, Solution, Task, ThreatDetectionFeedback, User, Visit, VisitedParty,
Visitor, VoiceCall, VolunteerProject, WorkBadgeDefinition, WorkOrder,
WorkOrderLineItem, WorkType, WorkTypeGroup, WorkTypeGroupMember

```
RecordType

SharingOption

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The parent object type.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Controls whether sharing is frozen for a file. Only Salesforce admins and file
owners with Collaborator access to the file can modify this field. The default is
`Allowed`, which means that new shares are allowed. When set to
`Restricted`, new shares are prevented without affecting existing shares.

This field is available in API versions 35.0 and later.


### Standard Objects CommerceEntitlementBuyerGroup

**Field Name** **Details**

```
Title

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Title of the attached file.

Use this object to list all notes, attachments, documents uploaded to libraries in Salesforce CRM content, and files added to Chatter for
a record, such as a related list on a detail page.

To determine if an object supports the CombinedAttachment object, call `describeSObject()` on the object. For example,
`describeSObject('Account')` returns all the child relationships of the Account object, including `CombinedAttachment` .
You can then query the CombinedAttachment child relationship.

```
SELECT Name, (SELECT Title FROM CombinedAttachments)

FROM Account

```

You can’t directly query CombinedAttachment.

### CommerceEntitlementBuyerGroup

Represents the entitlement policy for a buyer group. This object is available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`

Special Access Rules

The CommerceEntitlementBuyerGroup object is available when you meet these requirements. The B2B Commerce license is enabled.
The Commerce Buyer and Entitlements Integrator permission is granted.

Fields

**Field** **Details**

```
BuyerGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort


### Standard Objects CommerceEntitlementPolicy

**Field** **Details**

**Description**
The unique ID for the buyer group.

```
CurrencyIsoCode

Name

PolicyId

```

Associated Objects

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The standard code for the currency.

Possible values are:

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the entitlement buyer group.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique ID for the entitlement policy.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CommerceEntitlementBuyerGroupChangeEvent on page 68**
Change events are available for the object.

### CommerceEntitlementPolicy

Represents an entitlement policy, which determines what products and prices a user can see. This object is available in API version 49.0
and later.


Standard Objects CommerceEntitlementPolicy

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The CommerceEntitlementPolicy object is available only if the B2B Commerce license is enabled.

Fields

**Field** **Details**

```
CanViewPrice

CanViewProduct

CurrencyIsoCode

Description

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether a user can view the price of a product ( `true` ) or not ( `false` ). Default
value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether a user can view the product ( `true` ) or not ( `false` ). Default value is
`false` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The standard code for the currency.

Possible values are:

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects CommerceEntitlementPolicy

**Field** **Details**

**Description**
The entitlement policy description.

```
IsActive

LastReferencedDate

LastViewedDate

Name

OwnerId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines if the entitlement policy is active ( `true` ) or inactive ( `false` ). Default value is
`false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it can
mean that the record was only referenced ( `LastReferencedDate` ) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the entitlement policy.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The unique ID for the entitlement policy owner.


### Standard Objects CommerceEntitlementPolicyShare

Associated Objects

This object has the following associated objects. Except where noted, these objects are available in the same API version as
CommerceEntitlementPolicy.

**CommerceEntitlementPolicyChangeEvent on page 68**
Change events are available for the object.

**CommerceEntitlementPolicyOwnerFeed on page 55**
Feed tracking is available for the object.

**CommerceEntitlementPolicyHistory on page 63**
History is available for tracked fields of the object.

**CommerceEntitlementPolicyOwnerSharingRule**

Sharing rules are available for this object.

### CommerceEntitlementPolicyShare

Represents the entitlement rule for sharing products and prices with users other than the owner. This object is available in API version
49.0 and later.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

The CommerceEntitlementPolicyShare object is available only if the B2B Commerce license is enabled.

Fields

**Field** **Details**

```
AccessLevel

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Possible values are:

**•** `All` —Owner


Standard Objects CommerceEntitlementPolicyShare

**Field** **Details**

**•** `Edit` —Read/Write

**•** `Read` —Read Only

```
ParentId

RowCause

UserOrGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique ID of the parent entitlement policy.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only permitted
value is `Manual` . If no value is specified, the field defaults to `Manual` . All other `RowCause`
values are read-only. After the sharing entry is created, this field can’t be edited.

Possible values are:

**•** `CompliantCollaboration` —Compliant Data Sharing

**•** `GuestParentImplicit` —Associated guest user sharing

**•** `GuestPersonImplicit` —Associated Guest User Sharing

**•** `GuestRule` —Guest User Sharing Rule

**•** `ImplicitChild` —Account Sharing

**•** `ImplicitParent` —Associated record owner or sharing

**•** `ImplicitPerson` —Person Contact

**•** `Manual` —Manual Sharing

**•** `Owner`

**•** `Rule` —Sharing Rule

**•** `SurveyShare` —Survey Sharing Rule

**•** `Team` —Sales Team

**•** `Territory` —Territory Assignment Rule

**•** `Territory2AssociationManual` —Territory Manual

**•** `Territory2Forecast` —Territory assignment for forecasting and reporting

**•** `TerritoryManual` —Territory Manual

**•** `TerritoryRule` —Territory Sharing Rule

**Type**
reference


### Standard Objects CommerceEntitlementProduct

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The unique ID of the associated user or buyer group.

### CommerceEntitlementProduct

Represents the entitlement policy for a product. This object is available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`

Special Access Rules

The CommerceEntitlementProduct object is available when you meet these requirements. The B2B Commerce license is enabled. The
Commerce Buyer and Entitlements Integrator permission is granted.

Fields

**Field** **Details**

```
CurrencyIsoCode

Name

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The standard code for the currency.

Possible values are:

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The product entitlement policy name.


### Standard Objects CommissionSchedule

**Field** **Details**

```
PolicyId

ProductId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique ID for the product entitlement policy.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique ID for the product referenced in the entitlement policy.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CommerceEntitlementProductChangeEvent on page 68**
Change events are available for the object.

### CommissionSchedule

Represents a commission calculation and rate definition. Calculates commission values for a commissionable event.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ApplicableObject

```

**Type**
multipicklist

**Properties**
Create, Filter, Nillable, Restricted picklist, Update

**Description**
The object for which this Commission Schedule calculates commissions.


Standard Objects CommissionSchedule

**Field** **Details**

Possible values are:

**•** `Contract`

**•** `InsurancePolicy`

**•** `Producer`

**•** `Quote`

```
CalcProcessInputMapping

CalcProcessOutput

CalcProcessOutputConvNotation

CalculationProcessName

CalculationType

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The input mappings from the object fields to the variables used in the commission calculation.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The formula applied to this Commission Schedule’s process output that calculates the final
commission amount.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
An optimized version of the CalcProcessOutput formula that calculates the commission. Not
user-editable.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the Integration Procedure, Calculation Matrix, or Calculation Procedure this
Commission Schedule uses for calculations.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


Standard Objects CommissionSchedule

**Field** **Details**

**Description**
The type of calculation or process used when this Commission Schedule is used.

Possible values are:

**•** `Amount`

**•** `CalculationMatrix`

**•** `CalculationProcedure`

**•** `IntegrationProcedure`

**•** `Rate`

```
CommissionAmount

CommissionRate

CommissionStructureType

EffectiveEndDate

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The commission amount for the Commission Schedule when the process type is Amount.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The commission percentage for the Commission Schedule when the process type is Rate.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether the commission calculation is Flat or Tiered when the process type is
Matrix.

Possible values are:

**•** `Flat`

**•** `Tiered`

The default value is `Flat` .

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects CommissionSchedule

**Field** **Details**

**Description**
The effective end date of the Commission Schedule.

```
EffectiveStartDate

IsActive

LastReferencedDate

LastViewedDate

Name

OwnerId

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The effective start date of the Commission Schedule.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Commission Schedule is active.

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the Commission Schedule.

**Type**
reference


### Standard Objects CommissionScheduleAssignment

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the record owner.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
TierDefinition

```

Associated Objects

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Internal-only. Applies when the CalculationType is CalculationMatrix.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CommissionScheduleChangeEvent on page 68**
Change events are available for the object in API version 62.0 and later.

**CommissionScheduleFeed**

Feed tracking is available for the object.

**CommissionScheduleHistory**

History is available for tracked fields of the object.

**CommissionScheduleOwnerSharingRule**

Sharing rules are available for the object.

**CommissionScheduleShare**

Sharing is available for the object.

### CommissionScheduleAssignment

Represents the commission calculation applicable to a specific product or producer for one or multiple commissionable events.


Standard Objects CommissionScheduleAssignment

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CommissionableEventType

CommissionScheduleId

EffectiveEndDate

```

**Type**
multipicklist

**Properties**
Create, Filter, Nillable, Restricted picklist, Update

**Description**
The event that results in the commission calculation.

Possible values are:

**•** `Contracting`

**•** `Endorsement`

**•** `Issue Policy`

**•** `Policy Issuance`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the associated Commission Schedule, which is the commission calculation tied to
the product or producer.

This is a relationship field.

**Relationship Name**
CommissionSchedule

**Relationship Type**
Lookup

**Refers To**
CommissionSchedule

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The last date when the Commission Schedule is in effect for the product or producer.


Standard Objects CommissionScheduleAssignment

**Field** **Details**

```
EffectiveStartDate

LastReferencedDate

LastViewedDate

MaxCommissionAmount

MaxCommissionRate

MinCommissionAmount

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The first date when the Commission Schedule is in effect for the product or producer.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced (LastReferencedDate) and not viewed.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The maximum commission calculated for the product or producer for a commissionable
event. Constrains the output from the Commission Schedule.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The maximum commission rate that a producer receives for a commissionable event.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects CommissionScheduleAssignment

**Field** **Details**

**Description**
The minimum commission calculated for the product or producer for a commissionable
event. Constrains the output from the Commission Schedule.

```
MinCommissionRate

Name

ProducerId

Product2Id

```

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The minimum commission rate that a producer receives for a commissionable event.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the Commission Schedule Assignment.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The producer, broker, brokerage, or other user who receives the commission.

This is a relationship field.

**Relationship Name**
Producer

**Relationship Type**
Lookup

**Refers To**
Producer

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product for which commissions are calculated.

This is a relationship field.

**Relationship Name**
Product2


### Standard Objects CommSubscription

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Product2

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CommissionScheduleAssignmentChangeEvent on page 68**
Change events are available for the object in API version 62.0 and later.

**CommissionScheduleAssignmentFeed**

Feed tracking is available for the object.

**CommissionScheduleAssignmentHistory**

History is available for tracked fields of the object.

**CommissionScheduleAssignmentOwnerSharingRule on page 65**
Sharing rules are available for the object.

**CommissionScheduleAssignmentShare on page 67**
Sharing is available for the object.

### CommSubscription

Represents the subscription options for a specific communication. This object is available in API version 48.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
DataUsePurposeId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the data use purpose record associated with the communication subscription.


Standard Objects CommSubscription

**Field** **Details**

```
IsDefault

LastReferencedDate

LastViewedDate

Name

OwnerId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if this communication subscription is the default ( `true` ) or not ( `false` ). This field
has a default value of `false` . Only one communication subscription record can be the
default.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced ( `LastReferencedDate` ) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of the communication subscription record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the account owner associated with this customer.

This is a polymorphic relationship field.

**Relationship Name**
Owner


### Standard Objects CommSubscriptionChannelType

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Group, User

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**CommSubscriptionChangeEvent (API version 61.0)**
Change events are available for the object.

**CommSubscriptionFeed**

Feed tracking is available for the object.

**CommSubscriptionHistory**

History is available for tracked fields of the object.

**CommSubscriptionOwnerSharingRule**

Sharing rules are available for the object.

**CommSubscriptionShare**

Sharing is available for the object.

### CommSubscriptionChannelType

Represents the engagement channel through which you can reach a customer for a communication subscription. This object is available
in API version 48.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CommunicationSubscriptionId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the associated communication subscription record.

This is a relationship field.


Standard Objects CommSubscriptionChannelType

**Field** **Details**

**Relationship Name**
CommunicationSubscription

**Relationship Type**
Lookup

**Refers To**
CommSubscription

```
EngagementChannelTypeId

LastReferencedDate

LastViewedDate

MessagingChannelUsageId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the associated engagement channel type record.

This is a relationship field.

**Relationship Name**
EngagementChannelType

**Relationship Type**
Lookup

**Refers To**
EngagementChannelType

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced ( `LastReferencedDate` ) and not viewed.

**Type**
reference

**Properties**
Filter, Group, Sort


Standard Objects CommSubscriptionChannelType

**Field** **Details**

**Description**
The ID of the associated Messaging channel usage record, which is in turn associated with
a messaging channel.

This is a relationship field.

**Relationship Name**
MessagingChannelUsage

**Relationship Type**
Lookup

**Refers To**
MessagingChannelUsage

```
 Name

 OwnerId

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of the communication subscription channel type record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID account owner associated with this customer.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**CommSubscriptionChannelTypeChangeEvent (API version 61.0)**
Change events are available for the object.

**CommSubscriptionChannelTypeFeed**

Feed tracking is available for the object.


### Standard Objects CommSubscriptionConsent

**CommSubscriptionChannelTypeHistory**

History is available for tracked fields of the object.

**CommSubscriptionChannelTypeOwnerSharingRule**

Sharing rules are available for the object.

**CommSubscriptionChannelTypeShare**

Sharing is available for the object.

### CommSubscriptionConsent

Represents a customer’s consent to a communication subscription. This object is available in API version 48.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

With certain page layout and field-level security settings, some fields aren't visible or editable.

**Field** **Details**

```
BusinessBrandId

CommSubscriptionChannelTypeId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Business Brand that the individual has given consent to for a communication
subscription. This is a relationship field. This field is available in API version 53.0 and later.

**Relationship Name**
BusinessBrand

**Relationship Type**
Lookup

**Refers To**
BusinessBrand

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the associated communication subscription channel type record.

This is a relationship field.


Standard Objects CommSubscriptionConsent

**Field** **Details**

**Relationship Name**
CommSubscriptionChannelType

**Relationship Type**
Lookup

**Refers To**
CommSubscriptionChannelType

```
ConsentCapturedDateTime

ConsentCapturedSource

ConsentGiverId

ContactPointId

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Required. Date when the customer’s consent was captured.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. Source through which consent was captured. For example, user@example.com
or www.example.com.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the person who gave consent to the communication subscription on behalf of the
contact point.

Note: If the contact point gave consent, don't use `ConsentGiverId` .

This is a polymorphic relationship field.

**Relationship Name**
ConsentGiver

**Relationship Type**
Lookup

**Refers To**
Account, Contact, Individual, User

**Type**
reference


Standard Objects CommSubscriptionConsent

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the contact point, such as an Individual or person account, associated with the
communication subscription consent.

This is a polymorphic relationship field.

**Relationship Name**
ContactPoint

**Relationship Type**
Lookup

**Refers To**
ContactPointAddress, ContactPointEmail, ContactPointPhone

```
DataUsePurposeId

EffectiveFromDate

EffectiveToDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the record for data use purpose that you want to associate this consent with.
This field is available in API version 57.0 and later.

This is a relationship field.

**Relationship Name**
DataUsePurpose

**Relationship Type**
Lookup

**Refers To**
DataUsePurpose

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Date when consent starts.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date when consent ends. This field is restricted by field-level security.


Standard Objects CommSubscriptionConsent

**Field** **Details**

```
EngagementChannelTypeId

LastReferencedDate

LastViewedDate

Name

OwnerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the contact method you want to apply consent to. This field is available in API
version 57.0 and later.

This is a relationship field.

**Relationship Name**
EngagementChannelType

**Relationship Type**
Lookup

**Refers To**
EngagementChannelType

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced ( `LastReferencedDate` ) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of the communication subscription consent record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects CommSubscriptionConsent

**Field** **Details**

**Description**
The ID of the account owner associated with this customer.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
PartyId

PartyRoleId

PrivacyConsentStatus

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the record based on the Individual object that you want to associate consent
with. This field is available in API version 57.0 and later.

This is a relationship field.

**Relationship Name**
Party

**Relationship Type**
Lookup

**Refers To**
Individual

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Party Role for the individual you want to associate consent with. This is a
polymorphic relationship field. This field is available in API version 53.0 and later.

**Relationship Name**
PartyRole

**Relationship Type**
Lookup

**Refers To**
Customer, Seller

**Type**
picklist


### Standard Objects CommSubscriptionTiming

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Identifies whether the individual or person account associated with this record agrees to
this form of contact.

Possible values are:

**•** `NotSeen`

**•** `OptIn`

**•** `OptInPending` —Available in API version 58.0 and later.

**•** `OptOut`

**•** `OptOutPending` —Available in API version 58.0 and later.

**•** `Seen`

The default value is `NotSeen` . This field is available in API version 57.0 and later.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CommSubscriptionConsentChangeEvent (API version 49.0)**
Change events are available for the object.

**CommSubscriptionConsentFeed**

Feed tracking is available for the object.

**CommSubscriptionConsentHistory**

History is available for tracked fields of the object.

**CommSubscriptionConsentOwnerSharingRule**

Sharing rules are available for the object.

**CommSubscriptionConsentShare**

Sharing is available for the object.

### CommSubscriptionTiming

Represents a customer's timing preferences for receiving a communication subscription. This object is available in API version 48.0 and
later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects CommSubscriptionTiming

Fields

**Field** **Details**

```
CommSubscriptionConsentId

LastReferencedDate

LastViewedDate

Name

Offset

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the associated communication subscription consent record.

This is a relationship field.

**Relationship Name**
CommSubscriptionConsent

**Relationship Type**
Lookup

**Refers To**
CommSubscriptionConsent

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced ( `LastReferencedDate` ) and not viewed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Required. Name of the communication subscription timing record.

**Type**
double


Standard Objects CommSubscriptionTiming

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The amount of time before or after an event or the specific day of the week to communicate
with the contact point. Set the unit of time in the `Unit` field.

For example, if you set `Unit` as _`Week`_ and `Offset` as _`-4`_, communicate with the contact
point four weeks before the event. If you set `Offset` as _`4`_, communicate with the contact
point four weeks after the event.

```
PreferredTimeEnd

PreferredTimeStart

PreferredTimeZone

Unit

```

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
End of the preferred time span in which to reach the customer.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Start of the preferred time span in which to reach the customer.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Time zone of the preferred time span.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The unit of time that works with the `Offset` field to determine the communication timing.

Possible values are:

**•** `Day`

**•** `DayOfWeek`

**•** `Hour`

**•** `Month`


### Standard Objects Community (Zone)

**Field** **Details**

**•** `Week`

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**CommSubscriptionTimingChangeEvent (API version 62.0)**
Change events are available for the object.

**CommSubscriptionTimingFeed**

Feed tracking is available for the object.

**CommSubscriptionTimingHistory**

History is available for tracked fields of the object.

### Community (Zone)

Represents a zone that contains Idea or Question objects.

Note: Starting with the Summer ’13 release, Chatter Answers and Ideas communities were renamed to zones. In API version 28,
### the API object label has changed to Zone, but the API type is still Community .

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
CanCreateCase

DataCategoryName

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether users can ask private questions in the zone using Chatter Answers.

**Type**
string

**Properties**
Filter, Nillable, Group, Sort

**Description**
The data category associated with the zone.


Standard Objects Community (Zone)

**Field** **Details**

```
Description

HasChatterService

IsActive

IsPublished

Name

NetworkId

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
Text description of the zone.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether Chatter Answers is available in the zone.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the zone is active or inactive. An idea or question can only be posted to
an active zone.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the zone is available in portals.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the zone.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects ConcurApexLimitEventLog

**Field** **Details**

**Description**
ID of the Experience Cloud site that this zone is associated with. This field is available only if
digital experiences is enabled in your org. This field is available in API version 66.0 and later.

Usage

Use this object to create a zone in Ideas, Chatter Answers, or Answers. Zones help organize ideas and questions into logical groups and
are shared by the Ideas, Answers, and Chatter Answers.

### ConcurApexLimitEventLog

Concurrent Apex Limit event logs contain information about long-running concurrent Apex requests in your org that Salesforce terminated
after reaching your org’s concurrency limit. Requests with an established Apex context that execute for 5 seconds are counted towards
your org’s limit of concurrent long-running requests. (Asynchronous requests don’t count towards the limit.) When the long-running
requests exceed the org default limit, additional long-running requests are denied. This object is available in API version 61.0 and later.

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
RequestCount

RequestIdentifier

```

**Type**
int

**Properties**
Filter, Nillable, Sort

**Description**
Count of requests with an established Apex context executing for longer than 5 seconds in
your org.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ConcurApexLimitEventLog

**Field** **Details**

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `RequestIdentifier` . For example:
`3nWgxWbDKWWDIk0FKfF5DV` .

```
RequestLimit

RequestUri

Timestamp

UserIdentifier

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Maximum count of requests with an established Apex context that can execute for longer
than 5 seconds. When `RequestCount` reaches this limit, then additional long-running
Apex requests are terminated. (Asynchronous requests don’t count towards the limit.) See
_Apex Developer Guide_ [: Lightning Platform Apex Limits. For example:](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_gov_limits.htm#in_topic_non_transactional_gov_limits_section) `10` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the long-running Apex request that Salesforce terminated. For example:
`/apex/ApexClassName` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example,
`2020-01-20T19:12:26.965Z` . Milliseconds are the most granular setting.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.
For example: `00530000009M943` .


### Standard Objects ConnectedApplication ConnectedApplication

Represents a connected app and its details; all fields are read-only.

Connected apps link client applications, third-party services, other Salesforce organizations, apps, and resources to your organization.
The connected app configuration specifies authorization and security settings for these resources. This object exposes the settings for
a specified connected app.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
MobileSessionTimeout

MobileStartUrl

Name

NamedUserUvidTimeout

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**

Length of time after which the system logs out inactive mobile users.

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**

Users are directed to this URL after they’ve authenticated when the app is accessed
from a mobile device.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**

The unique name for this object.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects ConnectedApplication

**Field Name** **Details**

**Description**

The timeout value for a JSON Web Token (JWT)-based access token that's issued
to a named user. This field defines the timeout only if the app is configured to
have an app-specific timeout. If the app uses the user's session timeout, the
timeout value is defined based on the user's profile or the org session settings.
For more information about defining JWT-based access token timeout, see
[Configure a Connected App to Issue JWT-Based Access Tokens.](https://help.salesforce.com/s/articleView?id=xcloud.jwt_connectedapp_enable.htm&language=en_US)

These values are available in API version 59.0 and later.

**•** `1` —1 Minute

**•** `5` —5 Minutes

**•** `10` —10 Minutes

**•** `15` —15 Minutes

**•** `30` —30 Minutes

These values are available in API version 65.0 and later.

**•** `60` —1 Hour

**•** `90` —90 Minutes

**•** `120` —2 Hours

**•** `240` —4 Hours

**•** `480` —8 Hours

**•** `720` —12 Hours

This field is available in API version 59.0 and later.

```
OptionsAllowAdminApprovedUsersOnly

```

**Type**
boolean

**Properties**
Filter

**Description**

Indicates whether access is limited to users granted approval to use the connected
app by an administrator. Manage profiles for the app by editing each profile’s
Access list.

`OptionsCodeCredentialGuestEnabled` Reserved for future use.

`OptionsFullContentPushNotifications` For internal use only.

```
OptionsHasSessionLevelPolicy

```

**Type**
boolean

**Properties**
Filter

**Description**

Specifies whether the connected app requires a High Assurance level session.


Standard Objects ConnectedApplication

**Field Name** **Details**

`OptionsIsInternal` For internal use only.

```
OptionsRefreshTokenValidityMetric

OptionsTokenExchangeManageBitEnabled

PinLength

RefreshTokenValidityPeriod

StartUrl

```

**Type**
boolean

**Properties**
Filter

**Description**

Specifies whether the refresh token validity is based on duration or inactivity. If
`true`, the token validity is measured based on the last use of the token;
otherwise, it’s based on the token duration.

**Type**
boolean

**Properties**
Filter

**Description**

If `true`, the OAuth 2.0 token exchange flow is enabled.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

For mobile apps, this field is the PIN length requirement for users of the connected
app. Valid values are `4`, `5`, `6`, `7`, or `8` .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The duration of an authorization token until it expires in hours, months, or days
as set in the connected app management page.

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**

If the app isn’t accessed from a mobile device, users are directed to this URL after
they’ve authenticated.


### Standard Objects ConferenceNumber

**Field Name** **Details**

```
UvidTimeout

### ConferenceNumber

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The timeout value for a JWT-based access token that's issued to an unknown
user as a result of the guest user variation of the Authorization Code and
Credentials Flow. JWT-based access tokens issued during this flow variation
always contain a UVID.

This field defines the timeout only if the app is configured to have an app-specific
timeout. If the app uses the user's session timeout, the timeout value is defined
based on the user's profile or the org session settings. For more information about
[defining JWT-based access token timeout, see Configure a Connected App to](https://help.salesforce.com/s/articleView?id=xcloud.jwt_connectedapp_enable.htm&language=en_US)
[Issue JWT-Based Access Tokens.](https://help.salesforce.com/s/articleView?id=xcloud.jwt_connectedapp_enable.htm&language=en_US)

These values are available in API version 59.0 and later.

**•** `1` —1 Minute

**•** `5` —5 Minutes

**•** `10` —10 Minutes

**•** `15` —15 Minutes

**•** `30` —30 Minutes

These values are available in API version 65.0 and later.

**•** `60` —1 Hour

**•** `90` —90 Minutes

**•** `120` —2 Hours

**•** `240` —4 Hours

**•** `480` —8 Hours

**•** `720` —12 Hours

This field is available in API version 59.0 and later.

Holds the telephone number for an external event shown in the Salesforce Today feature in the Salesforce mobile app. This object is
available in API version 35.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`


Standard Objects ConferenceNumber

Special Access Rules

The Salesforce Today app is available in Salesforce for Android and Salesforce for iOS. It’s not available in the Salesforce desktop site.
Access to Today is available only if you grant Calendar permission to the Salesforce mobile app.

Fields

**Field** **Details**

```
AccessCode

ExternalEventId

IsLocked

Label

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the access code to enter in order to validate identity and join the call.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the external event associated with the conference number.

This field is a relationship field.

**Relationship Name**
ExternalEvent

**Refers To**
ExternalEvent

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Returns `true` if the conference number is locked, or `false` if it’s not.

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the conference number.


### Standard Objects Consumption Rate

**Field** **Details**

```
MayEdit

Name

Number

Vendor

```

Associated Objects

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

Indicates whether the conference number can be edited ( `true` ) or not ( `false` ).

The default value is `false` .

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the conference call’s organizer.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The phone number used to connect to the conference call.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The vendor or company associated with the conference number.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ConferenceNumberChangeEvent**

### Consumption Rate

Consumption rates describe the billing rate for a range of usage within a consumption schedule. All consumption schedules require at
least one consumption rate in order to rate usage on a usage product. This object is available in API version 45.0 and later.

The consumption rate sets a quantity-based boundary for usage and defines how much your product costs when its usage falls within
that boundary. Consumption rates price usage at a per-unit fee or a flat fee across the entire range of usage.


Standard Objects Consumption Rate

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ConsumptionScheduleId

CurrencyIsoCode

Description

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The consumption schedule that contains the consumption rate.

This is a relationship field.

**Relationship Name**
ConsumptionSchedule

**Relationship Type**
Lookup

**Refers To**
ConsumptionSchedule

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled.

Possible values are:

**•** `AUD` —Australian Dollar

**•** `CAD` —Canadian Dollar

**•** `GBP` —British Pound

**•** `JPY` —Japanese Yen

**•** `USD` —U.S. Dollar

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the consumption rate.


Standard Objects Consumption Rate

**Field** **Details**

```
LowerBound

Name

Price

PricingMethod

ProcessingOrder

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The lowest quantity of usage for the consumption rate.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Required. Default name of this record. Label is **Product Name** .

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
The price for usage that falls within the consumption rate’s bounds.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
How Salesforce applies the consumption rate’s price to the total quantity of usage within a
usage summary.

Possible values are:

**•** `FlatFee` —Salesforce applies the rate’s price to the entire quantity of usage.

**•** `PerUnit` —Salesforce applies the rate’s price to each individual quantity of usage
within the usage summary.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The order for processing the usage rate across multiple rates. Consumption rates are evaluated
beginning with the lowest processing order.


### Standard Objects Consumption Schedule

**Field** **Details**

```
UpperBound

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The highest quantity of usage for the consumption rate.

### Consumption Schedule

A consumption schedule organizes a set of consumption rates by which usage-based products are quoted and billed. This object is
available in API version 45.0 and later.

Salesforce uses consumption schedules to group consumption rates. Your consumption schedule defines the unit of measurement and
rating method for the schedule's rates. It also defines the billing frequency that Salesforce Billing uses to invoice a usage product.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
BillingTerm

BillingTermUnit

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The number used with the billing term unit to determine billing frequency.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The unit used with the billing term to determine billing frequency

Possible values are:

**•** `Month`  

**•** `Quarter`  

**•** `Year`  


Standard Objects Consumption Schedule

**Field** **Details**

```
CurrencyIsoCode

Description

IsActive

LastReferencedDate

LastViewedDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled.

Possible values are:

**•** `AUD` —Australian Dollar

**•** `CAD` —Canadian Dollar

**•** `GBP` —British Pound

**•** `JPY` —Japanese Yen

**•** `USD` —U.S. Dollar

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the consumption schedule.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this record is active ( `true` ) or not ( `false` ). Label is **Active** .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects Consumption Schedule

**Field** **Details**

**Description**

The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view ( `LastReferencedDate` ) but
not viewed it.

```
MatchingAttribute

Name

NumberOfRates

OwnerId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Salesforce Billing matches usage with a consumption schedule if the records share Matching
Attribute value.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Default name of this record. Label is **Product Name** .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of consumption rates in this consumption schedule.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The user who owns a consumption schedule record.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


Standard Objects Consumption Schedule

**Field** **Details**

```
RatingMethod

SBQQ__Category__c

Type

UnitOfMeasure

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A specific use case to rate usage against the schedule. This field is the controlling picklist for
the Type field.

Possible values are:

**•** `Tier`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
This field is available only with Salesforce CPQ.

You can define custom categories to organize consumption schedules in separate tabs on
sales rep UI. If you do this, make sure to create a field set for each category.

Possible values are:

**•** `Rates`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines how rate tiers are calculated.

Possible values are:

**•** `Range` —The schedule prices only using the tier that applies to the usage quantity.

**•** `Slab` —Usage within a given bound receives pricing equal to its tier’s value.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A unit of measure defines how you quantify instances of usage for your usage products. For
example, if your usage product is a cloud storage subscription, you could provide a value of
GB for your unit of measure.


### Standard Objects Contact

**Field** **Details**

```
 blng__BillingRule__c

 blng__RevenueRecognitionRule__c

 blng__TaxRule__c

### Contact

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
This field is available only with Salesforce Billing.

Salesforce Billing invoices usage summaries based off their related consumption schedule's
billing rule.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
This field is available only with Salesforce Billing.

Salesforce Billing recognizes usage summary revenue based off the summary's related revenue
recognition rule.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
This field is available only with Salesforce Billing.

Salesforce Billing taxes usage summary invoice lines based off the summary's related tax
rule.

Represents a contact, which is a person associated with an account.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `merge()`,
`query()`, `retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects Contact

Special Access Rules

Customer Portal users can access only portal-enabled contacts.

Fields

**Field** **Details**

```
AccountId

ActionCadenceAssigneeId

ActionCadenceId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the account that’s the parent of this contact.

We recommend that you update up to 50 contacts simultaneously when changing the
accounts on contacts enabled for a Customer Portal or partner portal. We also recommend
that you make this update after business hours.

This is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the sales rep designated to work the lead through their assigned cadence. This
field is available in API version 48.0 and later when the Sales Engagement license is enabled.
To see this field, the user also needs the Sales Engagement User or Sales Engagement Quick
Cadence Creator user permission set.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the lead’s assigned cadence. This field is available in API version 48.0 and later when
the Sales Engagement license is enabled. To see this field, the user also needs the Sales
Engagement User or Sales Engagement Quick Cadence Creator user permission set.


Standard Objects Contact

**Field** **Details**

```
ActionCadenceState

ActiveTrackerCount

ActivityMetricId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The state of the current action cadence tracker. This field is available in API version 50.0 and
later when the Sales Engagement license is enabled. To see this field, the user also needs
the Sales Engagement User or Sales Engagement Quick Cadence Creator user permission
set.

Possible values are:

**•** `Complete`

**•** `Error`

**•** `Initializing`

**•** `Paused`

**•** `Processing`

**•** `Running`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of cadences that are actively running on this contact. This field is available in
API version 57.0 and later when the Sales Engagement license is enabled. To see this field,
the user also needs the Sales Engagement User or Sales Engagement Quick Cadence Creator
user permission set.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
When Einstein Activity Capture with Activity Metrics is enabled, the ID of the related activity
metric.

This field is a relationship field.

This field is available in API version 41.0 and later.

**Relationship Name**
ActivityMetric

**Refers To**
ActivityMetric


Standard Objects Contact

**Field** **Details**

```
ActivityMetricRollupId

AssistantName

AssistantPhone

Birthdate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
When Einstein Activity Capture with Activity Metrics is enabled, the ID of the related activity
metric rollup.

This field is a relationship field.

This field is available in API version 41.0 and later.

**Relationship Name**
ActivityMetricRollup

**Refers To**
ActivityMetricRollup

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The assistant’s name.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The assistant’s phone number. Label is **Asst. Phone** .

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The contact’s birthdate.

Filter criteria for report filters, list view filters, and SOQL queries ignore the year portion of
the `Birthdate` field. For example, this SOQL query returns contacts with birthdays later
in the year than today:

```
  SELECT Name, Birthdate

  FROM Contact

  WHERE Birthdate > TODAY

```


Standard Objects Contact

**Field** **Details**

```
BuyerAttributes

CanAllowPortalSelfReg

CleanStatus

```

**Type**
multipicklist

**Properties**
Create, Filter, Nillable, Restricted picklist, Update

**Description**
If Automatic Contact Enhancements or Buyer Relationship Map is enabled, this field contains
the role of the contact in the opportunity or account. Possible values are:

**•** `BusinessUser` —For example, an end user. Key value.

**•** `Buyer` —Key value

**•** `Champion` —Key value

**•** `DecisionMaker` —Shown in green on a contact in the buyer relationship map UI.
Key value.

**•** `Detractor` —Shown in red on a contact in the buyer relationship map UI. Key value.

**•** `Evaluator`

**•** `ExecutiveSponsor` —Key value

**•** `TechnicalExpert`

Key values represent key contacts on an opportunity or account. If a buyer relationship map
doesn’t have contacts with key values, then Salesforce prompts you to add them. Having all
key values represented on the map provides a full view of the deal or account, increasing
sales success.

Warning: To ensure that the buyer relationship map feature works as expected,
don't modify field values. For example, if you change `Detractor` to `Detract`,
the value isn’t shown in red in a buyer relationship map.

This field is available with all profiles except custom and minimum-access. To provide access,
use field-level security in Object Manager.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this contact can self-register for your Customer Portal ( `true` ) or not
( `false` ).

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects Contact

**Field** **Details**

**Description**
Indicates the record’s clean status as compared with Data.com. Values include: `Matched`,
`Different`, `Acknowledged`, `NotFound`, `Inactive`, `Pending`, `SelectMatch`,
or `Skipped` .

Several values for `CleanStatus` appear with different labels on the contact record.

**•** `Matched` appears as `In Sync`

**•** `Acknowledged` appears as `Reviewed`

**•** `Pending` appears as `Not Compared`

```
CommerceCustomerReference

CommerceGroupReference

CommerceOrganizationReference

ConnectionReceivedId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The external Commerce ID of the individual. To update or create field values, you need the
Manage Shopper Profile Sync System Fields user permission. Available in API version 67.0
and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The external name of the Commerce customer group. To update or create field values, you
need the Manage Shopper Profile Sync System Fields user permission. Available in API version
67.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The external organization ID of the Commerce instance. To update or create field values, you
need the Manage Shopper Profile Sync System Fields user permission. Available in API version
67.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects Contact

**Field** **Details**

**Description**
ID of the PartnerNetworkConnection that shared this record with your organization. This
field is available if you enabled Salesforce to Salesforce.

```
ConnectionSentId

ContactSource

Department

DepartmentGroup

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the PartnerNetworkConnection that you shared this record with. This field is available
if you enabled Salesforce to Salesforce. This field is supported using API versions earlier than
15.0. In all other API versions, this field’s value is null. You can use the new
PartnerNetworkRecordConnection object to forward records to connections.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If Automatic Contact Creation is enabled, this field indicates whether the contact was created
automatically and identifies the source. Possible values are:

**•** `Auto Create`

**•** `Email Message`

**•** `Meeting Digest`

**•** `Seller Home`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The contact’s department.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If Automatic Contact Enhancements or Buyer Relationship Map is enabled, this field contains
the business unit, function, or department that the contact belongs to in the organization.
Possible values are:

**•** `chiefExecutive` —Key value


Standard Objects Contact

**Field** **Details**

**•** `customerSuccess` —For example, wealth management, consumer banking, subject
matter experts, or healthcare research experts.

**•** `finance` —Includes pricing and procurement. Key value.

**•** `humanResources`

**•** `legal` —Key value

**•** `marketing`

**•** `other`

**•** `sales`

**•** `support` —For example, tech support or customer support.

**•** `tech` —For example, IT or engineering. Key value.

Key values represent key contacts on an opportunity or account. If a buyer relationship map
doesn’t have contacts with key values, then Salesforce prompts you to add them. Having all
key values represented on the map provides a full view of the deal or account, increasing
sales success. This field is available with all profiles except custom and minimum-access. To
provide access, use field-level security in Object Manager.

```
Description

DoNotCall

Email

EmailBouncedDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the contact. Label is **Contact Description** up to 32 KB.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates that the contact doesn’t want to receive calls.

**Type**
email

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The contact’s email address.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects Contact

**Field** **Details**

**Description**
If bounce management is activated and an email sent to the contact results in a hard bounce,
the date and time of the bounce.

Note: Email bounce functionality isn't triggered by record updates, including updates
to this field.

```
EmailBouncedReason

Fax

FirstCallDateTime

FirstEmailDateTime

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If bounce management is activated and an email sent to the contact results in a hard bounce,
the reason for the bounce.

Note: Email bounce functionality isn't triggered by record updates, including updates
to this field.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The contact’s fax number. Label is **Business Fax** .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time of the first call placed to the contact. This field is available in API version
48.0 and later when the Sales Engagement license is enabled. To see this field, the user also
needs the Sales Engagement User or Sales Engagement Quick Cadence Creator user
permission set.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time of the first email sent to the contact. This field is available in API version
48.0 and later when the Sales Engagement license is enabled. To see this field, the user also
needs the Sales Engagement User or Sales Engagement Quick Cadence Creator user
permission set.


Standard Objects Contact

**Field** **Details**

```
FirstName

GenderIdentity

HasOptedOutOfEmail

HasOptedOutOfFax

HomePhone

IndividualId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The contact’s first name up to 40 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The contact’s internal experience of their gender, which may or may not correspond to their
designated sex at birth.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the contact doesn’t want to receive email from Salesforce ( `true` ) or does
( `false` ). Label is **Email Opt Out** .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the contact prohibits receiving faxes.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The contact’s home phone number. Label is **Home Phone** .

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Contact

**Field** **Details**

**Description**
ID of the data privacy record associated with this contact. This field is available if Data
Protection and Privacy is enabled.

This is a relationship field.

**Relationship Name**
Individual

**Relationship Type**
Lookup

**Refers To**
Individual

```
IsDeleted

IsEmailBounced

IsPersonAccount

IsPriorityRecord

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If bounce management is activated and an email is sent to a contact, indicates whether the
email results in a soft or hard bounce ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read only. Indicates whether this account has a record type of Person Account ( `true` ) or
not ( `false` ). Label is **Is Person Account** .

**Type**
boolean

**Properties**
Defaulted on create, Group

**Description**
Shows whether the user has marked the contact as important ( _`True`_ ) or not ( _`False`_ ). The
default value is `false` . Available in API version 59.0 and later.


Standard Objects Contact

**Field** **Details**

```
Jigsaw

JigsawContactId

LastActivityDate

LastName

LastReferencedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
References the company’s ID in Data.com. If an account has a value in this field, it means
that the account was imported from Data.com. If the field value is `null`, the account wasn’t
imported from Data.com. Maximum size is 20 characters. Available in API version 22.0 and
later. Label is **Data.com Key** .

Important: The `Jigsaw` field is exposed in the API to support troubleshooting for
import errors and reimporting of corrected data. Do not modify this value.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the contact in reference to `Jigsaw` .

Important: The `Jigsaw` field is exposed in the API to support troubleshooting for
import errors and reimporting of corrected data. Don’t modify the value in the
`Jigsaw` field.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Value is the most recent of either:

**•** Due date of the most recent event logged against the record.

**•** Due date of the most recently closed task associated with the record.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Last name of the contact up to 80 characters.

**Type**
dateTime


Standard Objects Contact

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

```
LastViewedDate

LeadSource

MailingAddress

MailingCity

MailingCountry

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view ( `LastReferencedDate` ) but
not viewed it.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The source of the lead that was converted to this contact.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the mailing address. Read-only. For details on compound address
fields, see Address Compound Fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Mailing address details.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Contact

**Field** **Details**

**Description**
Mailing address details.

```
MailingCountryCode

MailingGeocodeAccuracy

MailingLatitude

MailingLongitude

MailingPostalCode

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO codes for the mailing address’s state and country.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update, Query, Restricted picklist, Nillable

**Description**
Accuracy level of the geocode for the mailing address. For details on geolocation compound
field, see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `MailingLongitude` to specify the precise geolocation of a mailing address.
Acceptable values are numbers between –90 and 90 up to 15 decimal places. For details on
geolocation compound fields, see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `MailingLatitude` to specify the precise geolocation of a mailing address.
Acceptable values are numbers between –180 and 180 up to 15 decimal places. For details
on geolocation compound fields, see Compound Field Considerations and Limitations.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Mailing address details.


Standard Objects Contact

**Field** **Details**

```
MailingState

MailingStateCode

MailingStreet

MasterRecordId

MiddleName

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Mailing address details.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO codes for the mailing address’s state and country.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Street address for mailing address.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
If this record was deleted as the result of a merge, this field contains the ID of the record that
remains. If this record was deleted for any other reason, or hasn’t been deleted, the value is
`null` .

This is a relationship field.

**Relationship Name**
MasterRecord

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Contact

**Field** **Details**

**Description**
The contact’s middle name. Maximum size is 40 characters.

```
MobilePhone

Name

OtherAddress

OtherCity

OtherCountry

OtherCountryCode

```

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Contact’s mobile phone number. Label is **Mobile Phone** .

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Concatenation of `FirstName`, `MiddleName`, `LastName`, and `Suffix` up to 203
characters, including whitespaces.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the other address. Read-only. For details on compound address fields,
see Address Compound Fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Alternate address details.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Alternate address details.

**Type**
picklist


Standard Objects Contact

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO codes for the alternate address’s state and country.

```
OtherGeocodeAccuracy

OtherLatitude

OtherLongitude

OtherPhone

OtherPostalCode

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode for the other address. For details on geolocation compound
fields, see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `OtherLongitude` to specify the precise geolocation of an alternate address.
Acceptable values are numbers between –90 and 90 up to 15 decimal places. For details on
geolocation compound fields, see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `OtherLatitude` to specify the precise geolocation of an alternate address.
Acceptable values are numbers between –180 and 180 up to 15 decimal places. For details
on geolocation compound fields, see Compound Field Considerations and Limitations.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone for alternate address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Contact

**Field** **Details**

**Description**
Alternate address details.

```
OtherState

OtherStateCode

OtherStreet

OwnerId

Phone

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Alternate address details.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO codes for the alternate address’s state and country.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Street for alternate address.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the account associated with this contact.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
phone


Standard Objects Contact

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number for the contact. Label is **Business Phone** .

```
PhotoUrl

Pronouns

RecordTypeId

```

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**

Path to be combined with the URL of a Salesforce instance ( _Example:_
https:// _`yourInstance`_ .salesforce.com/) to generate a URL to request the social network
profile image associated with the contact. Generated URL returns an HTTP redirect (code
302) to the social network profile image for the contact.

Empty if Social Accounts and Contacts isn't enabled or if Social Accounts and Contacts is
disabled for the requesting user.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The contact’s personal pronouns, reflecting their gender identity. Others can use these
pronouns to refer to the contact in the third person. The entry is selected from a picklist of
available values, which the administrator sets. Maximum 40 characters.

Possible values are:

**•** `He/Him`

**•** `He/They`

**•** `Not Listed`

**•** `She/Her`

**•** `She/They`

**•** `They/Them`

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the record type assigned to this object.


Standard Objects Contact

**Field** **Details**

```
ReportsToId

Salutation

ScheduledResumeDateTime

Suffix

Title

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the contact that this contact reports to.

This is a relationship field.

**Relationship Name**
ReportsTo

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Honorific abbreviation, word, or phrase to be used in front of name in greetings, such as Dr.
or Mrs.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the action cadence tracker is going to resume after it’s paused or
on a wait step. This field is available in API version 54.0 and later when the Sales Engagement
license is enabled. To see this field, the user also needs the Sales Engagement User or Sales
Engagement Quick Cadence Creator user permission set.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name suffix of the contact. Maximum size is 40 characters.

**Type**
string


Standard Objects Contact

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Title of the contact, such as CEO or Vice President.

```
TitleType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If Automatic Contact Enhancements or Buyer Relationship Map is enabled, this field contains
the hierarchical position that the contact holds in the organization. In the UI, this field is
shown as Seniority Level. Possible values are:

**•** `ceo` —Key value

**•** `directorOrManager` —Key value

**•** `executive` —Key value

**•** `individualContributor`

**•** `vp` —VP or Head of Department. Key value.

Key values represent key contacts on an opportunity or account. If a buyer relationship map
doesn’t show contacts with key values, then Salesforce prompts you to add them. Having
all key values represented on the map provides a complete picture of the deal or account,
increasing sales success. This field is available with all profiles except custom and
minimum-access. To provide access, use field-level security in Object Manager.

Note: When importing contact data, users need the Set Audit Fields upon Record Creation permission to assign values to audit
fields such as `CreatedDate` . Audit fields are automatically updated during API operations unless you set these fields yourself.

Usage

Use this object to manage individual people who are associated with an account. You can create, query, delete, or update any attachment
associated with a contact.

Create or update contacts by converting a lead with the `convertLead()` call.

Associated Objects

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**AccountChangeEvent (API version 44.0)**
Change events are available for the object.

**ContactFeed (API version 18.0)**
Feed tracking is available for the object.


### Standard Objects ContactCenterChannel

**ContactHistory (API version 11.0)**
History is available for tracked fields of the object.

**ContactOwnerSharingRule**

Sharing rules are available for the object.

**ContactShare**

Sharing is available for the object.

SEE ALSO:

Overview of Salesforce Objects and Fields

### ContactCenterChannel

Represents a junction object that relates a Bring Your Own Channel for Contact Center as a Service (CCaaS) messaging channel to a
CallCenter object for Bring Your Own Channel for CCaaS. This object also represents the routing details for a voicemail configuration and
routing information for callback requests. This object is available in API version 56.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To access this object, Salesforce Voice with Amazon Connect, Salesforce Voice with Partner Telephony, Salesforce Voice with Partner
Telephony from Amazon Connect, or Bring Your Own Channel for Contact Center as a Service (CCaaS) must be enabled. To access this
object, you must be a SysAdmin user or have ViewSetup user permissions.

Fields

**Field** **Details**

```
ChannelId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
For Bring Your Own Channel for CCaaS, this field represents the unique ID of the Bring Your
Own Channel messaging channel (MessagingChannel) that’s associated with the contact
center (CallCenterId). Available in API version 60.0 and later.

This field is a relationship field.

**Relationship Name**
Channel

**Refers To**
MessagingChannel


Standard Objects ContactCenterChannel

**Field** **Details**

```
ContactCenterId

OmniCallbackFallbackQueueId

OmniCallbackHandler

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
This field is a relationship field. For Bring Your Own Channel for CCaaS, this field represents
the unique ID of the contact center (CallCenterId) that’s associated with the Bring Your Own
Channel messaging channel (MessagingChannel). Available in API version 60.0 and later.

This field is a relationship field.

**Relationship Name**
ContactCenter

**Relationship Type**
Master-detail

**Refers To**
CallCenter (the master object)

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If callbacks are configured for the contact center and the contact center uses Omni-Channel
Unified Routing, this field represents the unique ID of the fallback queue to use if contact
request routing through an Omni-Channel flow fails. Don't change the value in this field.
Instead, configure contact request routing in Lightning Experience.

Available in API version 65.0 and later.

This field is a relationship field.

**Relationship Name**
OmniCallbackFallbackQueue

**Refers To**
Group

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If callbacks are configured for the contact center and the contact center uses Omni-Channel
Unified Routing, this field represents the unique ID of the flow or queue used to route contact
requests. Don't change the value in this field. Instead, configure contact request routing in
Lightning Experience.


### Standard Objects ContactCleanInfo

**Field** **Details**

Available in API version 65.0 and later.

```
UserId

VoicemailFallbackQueueId

VoicemailHandler

### ContactCleanInfo

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Available in API version 63.0 only. For internal use.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If voicemail routing is configured for the contact center, this field represents the unique ID
of the fallback queue to use if voicemail routing fails. Don't change the value in this field.
Instead, configure voicemail routing in Lightning Experience.

This field is a relationship field.

**Relationship Name**
VoicemailFallbackQueue

**Refers To**
Group

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If voicemail routing is configured for the contact center, this field represents the unique ID
of the flow used to route voicemails. Don't change the value in this field. Instead, configure
voicemail routing in Lightning Experience.

Stores the metadata Data.com Clean uses to determine a contact record’s clean status. Helps you automate the cleaning or related
processing of contact records. ContactCleanInfo includes a number of bit vector fields. This object is removed in API version 67.0

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields will be removed
from your org.

To support customers’ needs around compliance and to remain a leader in trust and privacy, Salesforce removed all contact data
from the Data.com service on February 1, 2021.


Standard Objects ContactCleanInfo

[For more information, see Data.com Prospector and Clean Retirement.](https://help.salesforce.com/articleView?id=000270376&language=en_US&type=1)

Contact Clean Info provides a snapshot of the data in your Salesforce contact record and its matched Data.com record at the time the
Salesforce record was cleaned.

Contact Clean Info includes a number of bit vector fields, whose component fields each correspond to individual object fields and provide
related data or status information about those fields. For example, the bit vector field `IsDifferent` has an `IsDifferentEmail`
field. If the `IsDifferentEmail` field’s value is `False`, that means the `Email` field value is _the same_ on the Salesforce contact
record and its matched Data.com record.

ContactCleanInfo bit vector fields include:

**•** `CleanedBy` indicates who (a user) or what (a Clean job) cleaned the contact record.

**•** `IsDifferent` indicates whether or not a field on the contact record has a value that differs from the corresponding field on the
matched Data.com record.

**•** `IsFlaggedWrong` indicates whether or not a field on the contact record has a value that is flagged as wrong to Data.com.

**•** `IsReviewed` indicates whether or not a field on the contact record is in a `Reviewed` state, which means that the value was
reviewed but not accepted.

Fields

**Field Name** **Details**

```
Address

City

CleanedByJob

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the address. Read-only. See Address Compound Fields
for details on compound address fields.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Details for the billing address of the contact.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact record was cleaned by a Data.com Clean job ( `true` )
or not ( `false` ).


Standard Objects ContactCleanInfo

**Field Name** **Details**

```
CleanedByUser

ContactId

ContactStatusDataDotCom

Country

DataDotComID

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact record was cleaned by a Salesforce user ( `true` )
or not ( `false` ).

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique, system-generated ID assigned when the contact record was created.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
The status of the contact per Data.com. Values are: `Contact is Active`
`per Data.com`, `Phone is Wrong per Data.com`, `Email is`
`Wrong per Data.com`, `Phone and Email are Wrong per`
`Data.com`, `Contact Not at Company per Data.com`, `Contact`
`is Inactive per Data.com`, `Company this contact`
`belongs to is out of business per Data.com`, `Company`

```
  this contact belongs to never existed per Data.com
```

or `Email address is invalid per Data.com` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Details for the billing address of the contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID Data.com maintains for the contact.


Standard Objects ContactCleanInfo

**Field Name** **Details**

```
Email

FirstName

IsDifferentCity

IsDifferentCountry

IsDifferentCountryCode

IsDifferentEmail

```

**Type**
email

**Properties**
Filter, Group, Nillable, Sort

**Description**
The email address for the contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The contact’s first name.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `City` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `Country` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `Country Code` field value is different from
the corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter


Standard Objects ContactCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the contact’s `Email` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

```
IsDifferentFirstName

IsDifferentLastName

IsDifferentPhone

IsDifferentPostalCode

IsDifferentState

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `First Name` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `Last Name` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `Phone` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `Postal Code` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter


Standard Objects ContactCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the contact’s `State` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

```
IsDifferentStateCode

IsDifferentStreet

IsDifferentTitle

IsFlaggedWrongAddress

IsFlaggedWrongEmail

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `State Code` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `Street` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the contact’s `Title` field value is different from the
corresponding value on its matched Data.com record ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the contact’s `Address` field value is flagged as wrong to
Data.com ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update


Standard Objects ContactCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the contact’s `Email` field value is flagged as wrong to
Data.com ( `true` ) or not ( `false` ).

```
IsFlaggedWrongName

IsFlaggedWrongPhone

IsFlaggedWrongTitle

IsInactive

IsReviewedAddress

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the contact’s `Name` field value is flagged as wrong to Data.com
( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the contact’s `Phone` field value is flagged as wrong to
Data.com ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the contact’s `Title` field value is flagged as wrong to
Data.com ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the contact has been reported to Data.com as _`Inactive`_
( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update


Standard Objects ContactCleanInfo

**Field Name** **Details**

**Description**
Indicates whether the contact’s `Address` field value is in a `Reviewed` state
( `true` ) or not ( `false` ).

```
IsReviewedEmail

IsReviewedName

IsReviewedPhone

IsReviewedTitle

LastMatchedDate

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the contact’s `Email` field value is in a `Reviewed` state
( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the contact’s `Name` field value is in a `Reviewed` state
( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the contact’s `Phone` field value is in a `Reviewed` state
( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether the contact’s `Title` field value is in a `Reviewed` state
( `true` ) or not ( `false` ).

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date the contact record was last matched and linked to a Data.com record.


Standard Objects ContactCleanInfo

**Field Name** **Details**

```
LastName

LastStatusChangedById

LastStatusChangedDate

Latitude

