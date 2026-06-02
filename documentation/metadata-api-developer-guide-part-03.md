`isPrimaryKey` boolean Indicates whether a column name is the primary key ( `true` ) or not ( `false` )
for the Data Cloud CSV file.

`name` string Required. Name of the field. Can be either of the following:

**•** Name of the source field selected in the associated data source object.

**•** Name from a nested lookup object with three child levels.

BatchCalcJobFilter

Represents a collection of fields relating to a filter node in a data processing engine.

Fields

**Field Name** **Field Type** **Description**

`criteria` BatchCalcJobFilter
Criteria[]

Collection of filter criteria in a filter node.

The field is required when `isDynamicFilter` is set to `False` .

`description` string Description of the batch calculation job filter.


Metadata Types BatchCalcJobDefinition

**Field Name** **Field Type** **Description**

`filterCondition` string

Logic that is specified to apply the filter conditions.

The field is required when `isDynamicFilter` is set to `False` .

`filterParameterName` string Name of the parameter of type filter.

`isDynamicFilter` boolean Indicates whether the filter criteria is dynamic. If value is set to `True`, filter
criteria is passed in runtime with `filterParameterName` .

`label` string Required. Label of the filter node.

`name` string Required. Name of the filter node.

`sourceName` string Required. Name of the source node.

BatchCalcJobForecast

Represents a collection of fields relating to a forecast node in a data processing engine. Available in API version 58.0 and later.

Fields

**Field** **Field Type** **Description**
**Name**

`accuracyPercent` BatchCalcJobFrcstAccuracy (enumeration of type string)

The interval percentage to
account for errors in
forecasts.

Possible values are:

**•** `Eighty`

**•** `NinetyFive`

**•** `None`

The default value is `None` .

`aggregationFields` BtchCalcJobFrcstAggrFld[] The list of fields to
forecast.

`dateFieldName` string

Required.

The date field from the
source node used to

forecast values for the
specified forecast length.

`description` string The description of the
forecast node.


Metadata Types BatchCalcJobDefinition

**Field** **Field Type** **Description**
**Name**

`forecastModelType` BatchCalcJobFrcstModel (enumeration of type string)

The model used to
forecast data.

Possible values are:

**•** `Additive`

**•** `Auto`

**•** `Multiplicative`

The default value is `Auto` .

`forecastPeriodCount` int The number of time
periods to generate

forecast data. For example,
if you select Year-Month
as the forecast period
type, and 4 as the forecast
period count, the forecast
results are generated for
the next 4 months.

The minimum and the
default count is 1, and the
maximum is 100.

`forecastPeriodType` BatchCalcJobFrcstPeriodType (enumeration of type string)

Required.

The type of forecast period
to group date field values
in the forecast results.

Possible values are:

**•** `FiscalYear`

**•** `FiscalYearMonth`

**•** `FiscalYearQuarter`

**•** `FiscalYearWeek`

**•** `Year`

**•** `YearMonth`

**•** `YearMonthDay`

**•** `YearQuarter`

**•** `YearWeek`

`groupFields` BatchCalcJobFrcstGrpFld[] The source fields for
grouping the data to be

processed by the forecast
node.


Metadata Types BatchCalcJobDefinition

**Field** **Field Type** **Description**
**Name**

`label` string

`name` string

`periodStartDateName` string

`seasonality` BatchCalcJobFrcstSeasonality (enumeration of type string)


Required.

The name of the forecast
node in the UI.

Required.

A unique name for the
forecast node.

Required.

The start date of the
forecast period.

Represents the periodic
fluctuations that occur

around the same time
every year.

Possible values are:

**•** `Two`

**•** `Three`

**•** `Four`

**•** `Five`

**•** `Six`

**•** `Seven`

**•** `Eight`

**•** `Nine`

**•** `Ten`

**•** `Eleven`

**•** `Twelve`

**•** `Thirteen`

**•** `Fourteen`

**•** `Fifteen`

**•** `Sixteen`

**•** `Seventeen`

**•** `Eighteen`

**•** `Nineteen`

**•** `Twenty`

**•** `TwentyOne`

**•** `TwentyTwo`

**•** `TwentyThree`

Metadata Types BatchCalcJobDefinition

**Field** **Field Type** **Description**
**Name**

**•** `TwentyFour`

**•** `Auto`

**•** `None`

The default value is `None` .

`shouldExcludeLastPeriod` boolean Indicates whether to
ignore the last period in

the source node when it
has incomplete data
( `true` ) or not ( `false` ).

The default value is
`false` .

`sourceName` string

BtchCalcJobFrcstAggrFld

Represents a list of fields to forecast in a forecast node.

**Field Name** **Field Type** **Description**

Required.

The name of the source
node.

A source can be any node
other than the datasink
and register node.

`aggregateFunction` BatchCalcJobAggregateFunction
(enumeration of type string)


Required.

The function of the aggregate field.

Possible values are:

**•** `Avg`

**•** `Count`

**•** `Max`

**•** `Min`

**•** `Std`

**•** `StdP`

**•** `Sum`

**•** `Unique`

**•** `Var`

**•** `VarP`

Metadata Types BatchCalcJobDefinition

**Field Name** **Field Type** **Description**

`aggregationResultLabel` string

`fieldName` string

BatchCalcJobFrcstGrpFld

Required.

The name of the aggregation result generated from
the aggregation function that’s applied to the source
node field.

Required.

The name of the source field.

Represents source fields for grouping the data to be processed by the forecast node.

**Field Name** **Field Type** **Description**

`fieldName` string

`groupBy` string

BatchCalcJobHierarchyPath

Required.

The name of the source field to group the data to be processed by the
forecast node.

A comma-separated list of values to group data by.

Required when the source field type is Date or DateTime.

Possible values are:

**•** `Second`

**•** `Second Epoch`

**•** `Minute`

**•** `Hour`

**•** `Day`

**•** `Day Epoch`

**•** `Week`

**•**

**•** `Month`

**•** `Quarter`

**•** `Year`

Represents a collection of hierarchy path nodes in a data processing engine definition.


Metadata Types BatchCalcJobDefinition

Fields

**Field Name** **Field Type** **Description**

`description` string Description of the hierarchy path node.

`hierarchyFieldName` string Required. Field name that contains the hierarchy path.

`isSelfFieldValueIncluded` boolean Indicates whether the self value is included in the calculated hierarchy path
( `True` ) or not ( `False` ).

`label` string Required. Label of the hierarchy path node.

`name` string Required. Name of the hierarchy path node.

`parentFieldName` string Required. Parent field name to calculate hierarchy path.

`selfFieldName` string Required. Self field name to calculate hierarchy path.

`sourceName` string Required. Name of the source node.

BatchCalcJobFilterCriteria

Represents a collection of fields relating to a filter condition in a filter node in a data processing engine.

Fields

**Field Name** **Field Type** **Description**

`inputVariable` string Name of the input variable used as a filter.

Required. Operator that is specified in the filter condition.

Valid values are:

**•** `Equals`

**•** `NotEquals`

**•** `GreaterThan`

**•** `GreaterThanOrEqual`

**•** `LessThan`

**•** `LessThanOrEqual`

**•** `StartsWith`

**•** `EndsWith`

**•** `Contains`

**•** `DoesNotContain`

**•** `IsNull`

**•** `IsNotNull`

**•** `In`

**•** `NotIn`


```
operator

```

BatchCalcJobFilter
Operator
(enumeration of type
string)

Metadata Types BatchCalcJobDefinition

**Field Name** **Field Type** **Description**

`sequence` integer Required. Sequence number used to refer the criteria in a filter node.

`sourceFieldName` string Required. Name of the field from the source node to apply the filter.

`value` string Value used to filter data from the source node.

BatchCalcJobParameter

Represents a collection of fields relating to an input variable in a data processing engine.

Fields

**Field Name** **Field Type** **Description**

`dataType` BatchCalcJobParameter Required. Data type of the parameter. Valid values are:
DataType

**•** `Date`
(enumeration of type

**•** `DateTime`
string)

**•** `Expression`

**•** `FileIdentifier`

**•** `Filter`

**•** `Numeric`

**•** `Text`

`defaultValue` string Default value of the parameter.

`description` string Description of the batch calculation job parameter.

`isMultiValue` boolean Indicates whether the parameter has different values ( `True` ) or not ( `False` ).
This field is supported only for the `Text` data type.

`label` string Required. Label of the batch calculation job parameter.

`name` string Required. Name of the batch calculation job parameter.

BatchCalcJobSourceJoin

Represents a collection of fields relating to a join node in a data processing engine.

Fields

**Field Name** **Field Type** **Description**

`description` string Description of the join node.


Metadata Types BatchCalcJobDefinition

**Field Name** **Field Type** **Description**

`fields` BatchCalcJobJoin Collection of fields in a join node.
ResultField[]

`joinKeys` BatchCalcJobJoin Collection of mapping of fields from the primary source node and the second
Key[] source node in a join node.

`label` string Required. Label of the join node.

`name` string Required. Name of the join node.

`primarySourceName` string Required. Name associated with the node as the primary source node.

`secondarySourceName` string Required. Name associated with the node as the secondary source node.

```
type

```

BatchCalcJobSource Required. Type of join specified between the primary source node and
JoinType secondary source node. Valid values are:
(enumeration of type

**•** `LeftOuter`

string)

**•** `LeftOuter`

**•** `RightOuter`

**•** `Inner`

**•** `Outer`

**•** `Lookup`

BatchCalcJobJoinKey

Represents a collection of fields relating to a mapping of fields from the first source node and second source node in a join node of a
data processing engine.

Fields

**Field Name** **Field Type** **Description**

`primarySourceFieldName` string Required. Mapped field name of the primary source node.

`secondarySourceFieldName` string Required. Mapped field name of the secondary source node.

BatchCalcJobJoinResultField

Represents a collection of fields relating to a set of resultant fields in a join node of a data processing engine.

Fields

**Field Name** **Field Type** **Description**

`alias` string Required. Name that subsequent nodes within the data processing engine
definition use to refer to the resultant field.


Metadata Types BatchCalcJobDefinition

**Field Name** **Field Type** **Description**

`sourceFieldName` string Required. Name of field from the primary or secondary data source.

`sourceName` string Required. Source node of the primary or secondary data source.

BatchCalcJobTransform

Represents a collection of fields relating to a data transformation in a data processing engine.

Fields

**Field Name** **Field Type** **Description**

`description` string The description of the batch calculation job transform.

`droppedFields` BatchCalcJobTransform The collection of dropped fields in a data transformation. Available when the
DroppedField[] transformation type is `Slice` .

`expressionFields` BatchCalcJobTransform The collection of formula fields in a data transformation. Available when the
AddedField[] transformation type is `Expression` .

`label` string Required. The label of the batch calculation job transform.

`name` string Required. The name of the batch calculation job transform.

`orderBy` BatchCalcJobOrderByField A collection of fields that’s used to sort the records within each partition group.
on page 464[]

`partitionBy` string[] A group of fields that’s used to partition the source data into partition groups.

`sourceName` string Required. Name of the source node.

Required. The type of transformation.

Valid values are:

**•** `ComputeRelative—` This transformation calculates values based on
values of the same partition group.

**•** `Expression` —This transformation calculates values based on existing
values of fields in the same record.

**•** `Slice` —This transformation removes fields from the source node.

```
transformType

```

BatchCalcJobTransform
Type (enumeration of
type string)

BatchCalcJobTransformDroppedField

Represents a collection of fields relating to a dropped field in a data transformation of a data processing engine.


Metadata Types BatchCalcJobDefinition

Fields

**Field Name** **Field Type** **Description**

`sourceFieldName` string Required. Name of the field that is dropped.

BatchCalcJobTransformAddedField

Represents a collection of fields relating to a formula in a data transformation of a data processing engine.

Fields

**Field Name** **Field Type** **Description**

`alias` string Required. Name that subsequent nodes within the data processing engine use
to the transform node.

Required. Data type of the formula.

Valid values are:

**•** `Boolean` —Available in API version 65.0 and later.

**•** `Date`

**•** `DateTime`

**•** `MultiValue`

**•** `Numeric`

**•** `Text`

```
dataType

```

BatchCalcJobDataType
(enumeration of type
string)

`decimalPlaces` integer Number of digits to the right of a decimal point in the value. Required for the
`Numeric` data type.

`expression` string Required. Formula defined by the user.

`length` integer Total length of the value including the decimal places. Required for data types:
`Text` and `Numeric` .

BatchCalcJobOrderByField

Represents a collection of fields that are used to sort the partitioned data.

Fields

**Field Name** **Field Type** **Description**

`name` string Required. Name of the field that is used to sort data.


Metadata Types BatchCalcJobDefinition

**Field Name** **Field Type** **Description**

`orderType` BatchCalcJobOrderType(enumeration
of type string)

BatchCalcJobUnion

Order in which the data is sorted.

Valid values are:

**•** Ascending

**•** Descending

Represents a collection of fields relating to the union of data from two nodes in a data processing engine.

Fields

**Field Name** **Field Type** **Description**

`description` string Description of the batch calculation job union.

`isDisjointedSchema` boolean

Indicates whether the union is of two disjointed datasets ( `true` ) or not
( `false` ). Set to `True` to allow joining of two datasets having no common
fields.

`label` string Required. Label of the batch calculation job union.

`name` string Required. Name of the batch calculation job union.

`sources` string[] Names of the source nodes.

BatchCalcJobWritebackObject

Represents a collection of fields relating to the object in which the results of the data processing engine are written back.

Fields

**Field Name** **Field Type** **Description**

`canWrtbckToNonEditableFields` boolean

Indicates whether the non-editable fields are included in field mapping when
the action type is upsert. The default value is `false` .

Available in API version 64.0 and later.

`description` string Descriptions of the batch calculation job writeback object.

`externalIdFieldName` string

Unique external field ID for the target object name.

Available in API version 60.0 and later.

`fields` BatchCalcJobWriteback Collection of the writeback fields.
Mapping[]


Metadata Types BatchCalcJobDefinition

**Field Name** **Field Type** **Description**

`filterCondition` string

The condition that filters the records from a writeback dataset for a user.
Examples of a filter condition include a user ID, stage name, and a security
policy that returns only the records that a user owns.

Available in API version 57.0 and later.

`folderName` string The folder where the writeback dataset is saved. Available in API version 57.0
and later.

`groupBy` string Reserved for future use.

`isChangedRow` boolean Indicates whether a row in the write back object is changed. Set to `True` to
write back the changed rows.

`isExistingDataset` boolean

Indicates whether a CRM Application (CRMA) dataset or a Data 360 Data Lake
object is present ( `true` ) or will be created ( `false` ). Available in API version
62.0 and later.

`label` string Required. Name of the write back object.

`name` string Required. Name of the batch calculation job write back object.

Type of operation specified.

Valid values are:

**•** `Delete` —This value is available in API version 56.0 and later.

**•** `Insert`

**•** `Overwrite` —Available only when `storageType` is
`DataLakeObject` . This value is available in API version 60.0 and later.

**•** `Update`

**•** `Upsert`

```
operationType

```

BatchCalcJobWriteback
Opn (enumeration of
type string)

`sharingInheritanceObjectName` string The name of the source object from which the row-level sharing inheritance
settings are applied. Available in API version 57.0 and later.

`shouldCreateTargetObject` boolean Indicates whether target Data Lake Object or Salesforce Object is created in
Salesforce ( `true` ) or not ( `false` ). Available in API version 65.0 and later.

`shouldMngRowLockFor` boolean Reserved for future use.

```
GroupedRec

```

`sourceName` string Required. Name of the source node associated with the write back object.

Specifies where you want to use the data stored in the source node. Available
in API version 57.0 and later.

Valid values are:

**•** `Analytics`

**•** `DataLakeObject`

**•** `sObject`

The default value is `sObject` .


```
storageType

```

BatchCalcJobWriteback
Type (enumeration of
type string)

Metadata Types BatchCalcJobDefinition

**Field Name** **Field Type** **Description**

`targetObjectName` string Required. Object that is inserted or upserted by the data processing engine.

`writebackSequence` integer Sequence in which the target object is updated by the data processing engine.

`writebackUser` string ID of the user whose permissions decide which objects and fields of the target
object can be updated.

BatchCalcJobWritebackMapping

Represents a collection of fields relating to the mapping between results and the fields in the target object.

Fields

**Field Name** **Field Type** **Description**

`fieldType` string Target field type on the writeback object. Valid values are:

**•** Primary Key

**•** Qualifier Key

Available in API version 64.0 and later.

isAutogenerated boolean

Indicates whether the target field value on the writeback object is
autogenerated ( `true` ) or not ( `false` ).

Available in API version 64.0 and later.

`parentName` string Name of the lookup object. Required only when the `relationshipName`
field is defined.

`relationshipName` string Name of the lookup relationship.

`runtimeParameter` boolean

Indicates whether the source field from runtime parameter is `true` or `false` .
The default value is `false` .

Available in API version 59.0 and later.

`sourceFieldName` string Required. Name of the field in the source node that is written back.

`targetFieldName` string Name of the sObject field to which the results are written back.

Declarative Metadata Sample Definition

The following is an example of a BatchCalcJobDefinition component.

```
<?xml version="1.0" encoding="UTF-8"?>

<BatchCalcJobDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

   <aggregates>

     <description>Aggregate Description</description>

     <fields>

```


Metadata Types BatchCalcJobDefinition

```
           <aggregateFunction>Count</aggregateFunction>

           <alias>NameCount</alias>

           <sourceFieldName>Name</sourceFieldName>

        </fields>

        <groupBy>ContactId</groupBy>

        <groupBy>Name</groupBy>

        <label>AggregateOpportunities</label>

        <name>AggregateOpportunities</name>

        <sourceName>Opportunity</sourceName>

      </aggregates>

      <forecasts>

        <description>ForecastNode Description</description>

        <label>ContactForecast</label>

        <name>ContactForecast</name>

        <sourceName>Contact</sourceName>

        <dateFieldName>CreatedDate</dateFieldName>

        <forecastPeriodType>YearMonth</forecastPeriodType>

        <shouldExcludeLastPeriod>false</shouldExcludeLastPeriod>

        <forecastPeriodCount>12</forecastPeriodCount>

        <periodStartDateName>CreatedDateYM</periodStartDateName>

        <forecastModelType>Auto</forecastModelType>

        <seasonality>None</seasonality>

        <accuracyPercent>None</accuracyPercent>

        <aggregationFields>

           <aggregateFunction>Count</aggregateFunction>

           <aggregationResultLabel>CountOfLastName</aggregationResultLabel>

           <fieldName>LastName</fieldName>

        </aggregationFields>

        <groupFields>

           <fieldName>LastModifiedDate</fieldName>

           <groupBy>Week</groupBy>

        </groupFields>

      </forecasts>

      <appends>

        <description>Append desc</description>

        <isDisjointedSchema>true</isDisjointedSchema>

        <label>AppendAllAccounts</label>

        <name>AppendAllAccounts</name>

        <sources>AccountsOfManufacturingIndustry</sources>

        <sources>ComputeRelativeManufacturingIndustry</sources>

      </appends>

      <datasources>

        <description>Desc Contact</description>

        <fields>

           <alias>Id</alias>

           <name>Id</name>

           <isPrimaryKey>false</isPrimaryKey>

           <dataType>Text</dataType>

        </fields>

        <fields>

           <alias>LastName</alias>

           <name>LastName</name>

           <isPrimaryKey>false</isPrimaryKey>

           <dataType>Text</dataType>

```


Metadata Types BatchCalcJobDefinition

```
        </fields>

        <fields>

           <alias>CreatedDate</alias>

           <name>CreatedDate</name>

           <isPrimaryKey>false</isPrimaryKey>

           <dataType>Date</dataType>

        </fields>

        <fields>

           <alias>LastModifiedDate</alias>

           <name>LastModifiedDate</name>

           <isPrimaryKey>false</isPrimaryKey>

           <dataType>Date</dataType>

        </fields>

        <label>Contact</label>

        <name>Contact</name>

        <sourceName>Contact</sourceName>

        <type>StandardObject</type>

        <fileSource>ContentManagement</fileSource>

        <fileIdentifier>069xx0000004CAeAAM</fileIdentifier>

        <CSVDelimiter>COMMA</CSVDelimiter>

        <filePath>parentFolder/childFolder</filePath>

      </datasources>

      <datasources>

        <fields>

           <alias>Name</alias>

           <name>Name</name>

           <isPrimaryKey>false</isPrimaryKey>

           <dataType>Text</dataType>

        </fields>

        <fields>

           <alias>ContactId</alias>

           <name>ContactId</name>

           <isPrimaryKey>false</isPrimaryKey>

           <dataType>Text</dataType>

        </fields>

        <label>Opportunity</label>

        <name>Opportunity</name>

        <sourceName>Opportunity</sourceName>

        <type>StandardObject</type>

        <fileSource>ContentManagement</fileSource>

        <fileIdentifier>069xx0000004CAeAAM</fileIdentifier>

        <CSVDelimiter>COMMA</CSVDelimiter>

        <filePath>parentFolder/childFolder</filePath>

      </datasources>

      <description>Calculates and creates transaction journal records based on the orders

   placed by the loyalty program members. The transaction journals are used to accrue points

    to the member.</description>

      <filters>

        <criteria>

           <operator>Equals</operator>

           <sequence>1</sequence>

           <sourceFieldName>LastName</sourceFieldName>

           <value>Salesforce</value>

        </criteria>

```


Metadata Types BatchCalcJobDefinition

```
        <description>Filter Desc</description>

        <filterCondition>1</filterCondition>

        <isDynamicFilter>false</isDynamicFilter>

        <label>AccountsOfManufacturingIndustry</label>

        <name>AccountsOfManufacturingIndustry</name>

        <sourceName>AccountOpportunities</sourceName>

      </filters>

      <hierarchyPaths>

        <description>Hierarchy Path Node</description>

        <hierarchyFieldName>Hierarchy_Path</hierarchyFieldName>

        <isAggregationRequired>true</isAggregationRequired>

        <isSelfFieldValueIncluded>true</isSelfFieldValueIncluded>

        <label>Get Hierarchy</label>

        <name>Get_Hierarchy</name>

        <parentFieldName>ContactId</parentFieldName>

        <selfFieldName>LastName</selfFieldName>

        <sourceName>AppendAllAccounts</sourceName>

        <aggregateFields>

           <aggregateFunction>Count</aggregateFunction>

           <aggregationFieldName>*</aggregationFieldName>

           <aggregateFieldAliasName>CountOfLastName</aggregateFieldAliasName>

        </aggregateFields>

      </hierarchyPaths>

      <isTemplate>false</isTemplate>

      <executionPlatformObjectType>None</executionPlatformObjectType>

      <joins>

        <description>Left Outer Join</description>

        <fields>

           <alias>ContactId</alias>

           <sourceFieldName>Id</sourceFieldName>

           <sourceName>Contact</sourceName>

        </fields>

        <fields>

           <alias>LastName</alias>

           <sourceFieldName>LastName</sourceFieldName>

           <sourceName>Contact</sourceName>

        </fields>

        <fields>

           <alias>NameCount</alias>

           <sourceFieldName>NameCount</sourceFieldName>

           <sourceName>AggregateOpportunities</sourceName>

        </fields>

        <fields>

           <alias>OpportunityName</alias>

           <sourceFieldName>Name</sourceFieldName>

           <sourceName>AggregateOpportunities</sourceName>

        </fields>

        <joinKeys>

           <primarySourceFieldName>Id</primarySourceFieldName>

           <secondarySourceFieldName>ContactId</secondarySourceFieldName>

        </joinKeys>

        <label>AccountOpportunities</label>

        <name>AccountOpportunities</name>

        <primarySourceName>Contact</primarySourceName>

```


Metadata Types BatchCalcJobDefinition

```
        <secondarySourceName>AggregateOpportunities</secondarySourceName>

        <type>LeftOuter</type>

      </joins>

      <label>Create Transaction Journals Based on Orders</label>

      <parameters>

        <dataType>Date</dataType>

        <defaultValue>2020-01-01</defaultValue>

        <description>Desc TextParameter</description>

        <isMultiValue>false</isMultiValue>

        <label>DateParameter</label>

        <name>DateParameter</name>

      </parameters>

      <parameters>

        <dataType>Filter</dataType>

        <defaultValue>{&quot;filterCondition&quot;: &quot;1 AND 2&quot;,

   &quot;criteria&quot;: [{&quot;sourceFieldName&quot;:

   &quot;NameCount&quot;,&quot;operator&quot;: &quot;GreaterThan&quot;,&quot;value&quot;:

   &quot;20&quot;,&quot;sequence&quot;: &quot;1&quot;}, {&quot;sourceFieldName&quot;:

   &quot;Name&quot;,&quot;operator&quot;: &quot;Equals&quot;,&quot;value&quot;:

   &quot;Salesforce&quot;,&quot;sequence&quot;: &quot;2&quot;}]}</defaultValue>

        <isMultiValue>false</isMultiValue>

        <label>FilterParameter</label>

        <name>FilterParameter</name>

      </parameters>

      <parameters>

        <dataType>Numeric</dataType>

        <defaultValue>5000</defaultValue>

        <description>Desc TextParameter</description>

        <isMultiValue>false</isMultiValue>

        <label>NumericParameter</label>

        <name>NumericParameter</name>

      </parameters>

      <parameters>

        <dataType>Text</dataType>

        <defaultValue>@salesforce.com</defaultValue>

        <description>Desc TextParameter</description>

        <isMultiValue>false</isMultiValue>

        <label>TextParameter</label>

        <name>TextParameter</name>

      </parameters>

      <processType>Rebates</processType>

      <definitionRunMode>Batch</definitionRunMode>

      <status>Inactive</status>

      <transforms>

        <description>transforms Desc</description>

        <expressionFields>

           <alias>NewLastName</alias>

           <dataType>Text</dataType>

           <expression>TODAY()</expression>

           <length>80</length>

        </expressionFields>

        <label>ManufacturingIndustry</label>

        <name>ManufacturingIndustry</name>

        <sourceName>AccountsOfManufacturingIndustry</sourceName>

```


Metadata Types BatchCalcJobDefinition

```
        <transformationType>Expression</transformationType>

      </transforms>

      <transforms>

        <droppedFields>

           <sourceFieldName>NewLastName</sourceFieldName>

        </droppedFields>

        <label>MediaIndustry</label>

        <name>MediaIndustry</name>

        <sourceName>ManufacturingIndustry</sourceName>

        <transformationType>Slice</transformationType>

      </transforms>

      <transforms>

        <description>compute relative transforms Desc</description>

        <expressionFields>

           <alias>NewLastName</alias>

           <dataType>Text</dataType>

           <expression>rank()</expression>

           <length>80</length>

        </expressionFields>

        <label>ComputeRelativeManufacturingIndustry</label>

        <name>ComputeRelativeManufacturingIndustry</name>

        <orderBy>

           <name>LastName</name>

           <orderType>Ascending</orderType>

        </orderBy>

        <partitionBy>LastName</partitionBy>

        <sourceName>MediaIndustry</sourceName>

        <transformationType>ComputeRelative</transformationType>

      </transforms>

      <customNodes>

        <name>RebatesCustomNode</name>

        <label>Rebates Custom Node</label>

        <description>customNodes Desc</description>

        <sources>Get_Hierarchy</sources>

        <extensionName>RebatesExpression</extensionName>

        <extensionNamespace>industries_mfg</extensionNamespace>

        <parameters>

           <name>inputColumn</name>

           <value>LastName</value>

        </parameters>

        <parameters>

           <name>isFilterCriteria</name>

           <value>true</value>

        </parameters>

        <parameters>

           <name>outputColumn</name>

           <value>GenName</value>

        </parameters>

      </customNodes>

      <writebacks>

        <fields>

           <sourceFieldName>GenName</sourceFieldName>

           <targetFieldName>LastName</targetFieldName>

        </fields>

```


### Metadata Types BatchProcessJobDefinition

```
        <isChangedRow>false</isChangedRow>

        <label>exportToContact</label>

        <name>exportToContact</name>

        <description>Export To Contact</description>

        <operationType>Insert</operationType>

        <sourceName>RebatesCustomNode</sourceName>

        <targetObjectName>Contact</targetObjectName>

        <writebackSequence>1</writebackSequence>

        <canWrtbckToNonEditableFields>false</canWrtbckToNonEditableFields>

      </writebacks>

      <writebacks>

        <fields>

           <sourceFieldName>CreatedDateYM</sourceFieldName>

           <targetFieldName>CreatedDate</targetFieldName>

        </fields>

        <isChangedRow>false</isChangedRow>

        <isExistingDataset>false</isExistingDataset>

        <label>exportToContactFC</label>

        <name>exportToContactFC</name>

        <description>Export To Contact</description>

        <operationType>Insert</operationType>

        <sourceName>ContactForecast</sourceName>

        <targetObjectName>Contact</targetObjectName>

        <writebackSequence>2</writebackSequence>

        <canWrtbckToNonEditableFields>false</canWrtbckToNonEditableFields>

      </writebacks>

   </BatchCalcJobDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <!-
     ~ Copyright 2020 Salesforce, Inc.

     ~ All Rights Reserved

     ~ Company Confidential

   -->

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <types>

       <members>*</members>

       <name>BatchCalcJobDefinition</name>

     </types>

     <version>60.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### BatchProcessJobDefinition

Represents the details of a Batch Management job definition.


Metadata Types BatchProcessJobDefinition

This type extends the Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

BatchProcessJobDefinition components have the suffix `.batchProcessJobDefinition` and are stored in the
`batchProcessJobDefinitions` folder.

Version

BatchProcessJobDefinition components are available in API version 51.0 and later.

Special Access Rules

To use this metadata type, your Salesforce org must have the Loyalty Management or the Rebate Management license. The Loyalty
Program Process type is only available in orgs that have Loyalty Management enabled.

Fields

**Field Name** **Field Type** **Description**

`batchSize` integer Required. Number of records that each Batch Management job can
process. Flow type Batch Management jobs can process up to 2000

records and Loyalty Program Process type Batch Management jobs can
process up to 250 records.

`dataSource` BatchDataSource Required. Source of information whose records must be processed by
on page 476[] the Batch Management job.

`description` string Description of the Batch Management job, up to 255 characters.

`executionProcessApiName` string API name of process that must be executed by the Batch Management
job. This field is available in API version 55.0 and later.

**•** If the batch job’s type is Flow, enter the API name of an active flow
that the batch job must execute.

**•** If the batch job’s type is Loyalty Program Process, enter:

**–** Transaction_Journals if you want the batch job to process
Transaction Journal records by applying the applicable active
loyalty program process of the type TransactionJournal.

**–** API name of an active loyalty process of the type TierProcessing
if you want the batch job to run the loyalty program process to
assess the tier of eligible members. The API name consists of the
name of the process, the process type, and the name of the
loyalty program separated by two consecutive underscores. For
example, the process API name is `Update Member`
`Tier__TierProcessing__Inner Circle` if the


Metadata Types BatchProcessJobDefinition

**Field Name** **Field Type** **Description**

process name is Update Member Tier, the process type is
TierProcessing, and the loyalty program name is Inner Circle.

You can use database-based APEX classes that let you use flex queues in
the Batch Management job, allowing to place more than 5 jobs in a
queue. This functionality is applicable to all Industry Clouds that use
[managed packages. See Apex Flex Queue.](https://help.salesforce.com/s/articleView?id=platform.code_apex_flex_queue.htm&type=5&language=en_US)

`flowApiName` string

API name of an active flow process that must be executed by the Batch
Management job.

You can either specify the flow API name in the
`executionProcessApiName` field or in the `flowApiName`
field.

`flowInputVariable` string Input variable of associated flow that is used by the batch job to uniquely
identify records.

`masterLabel` string Required. Name of the Batch Management job, up to 80 characters.

`processGroup` string Required. Name of the group for which the Batch Management job
processes records.

`retryCount` integer Required. Number of times this Batch Management job must be rerun
in case it fails. The maximum retry count is 3. Valid values are 1–3.

`retryInterval` integer Required. Number of milliseconds after which the Batch Management
job must be rerun in case it fails. Valid values are 1,000–10,000.

`status` string Indicates the status of the Batch Management job. Valid values are
`Active` and `Inactive` .

`type` string (enumeration The type of process that the Batch Management job must execute. This
of type string) field is available in API version 55.0 and later. Valid values are:

**•** `BulkUpdate`

**•** `Calc` —Data Processing Engine

**•** `ConsumptionOveragesCalculation`

**•** `DecisionTableRefresh`

**•** `DeepCloneSalesAgreement`

**•** `FlattenAccountIOUHierarchyBatchJob`

**•** `Flow`

**•** `EnergyUseRecordCreationBatchJob`

**•** `EntitlementCreationBatchJob`

**•** `HighScaleBreProcess`

**•** `IndustriesLSCommercial`

**•** `InvoiceDTPRunBatchJob`

**•** `InvoiceRecoveryRunBatchJob`


Metadata Types BatchProcessJobDefinition

**Field Name** **Field Type** **Description**

**•** `InvoiceRunBatchJob`

**•** `LifeSciProviderActivityGoalSharingBatchJob`

**•** `LoyaltyProgramProcess`

**•** `NetUnitRateCalculation`

**•** `NextGenCommitmentBatchProcessingJob`

**•** `ManagerProvisioning`

**•** `PbbToOptyConversion`

**•** `ProductCatalogCacheRefresh`

**•** `PromotionChannelPropagationBatchJob`

**•** `RatableSummaryCreation`

**•** `ServiceProcess`

**•** `StoreAssortmentPropagationBatchJob`

**•** `SummaryCreation`

**•** `WorkDotComToHRManagerProvisioning`

BatchDataSource

Represents the source of information whose records must be processed by the Batch Management job.

Fields

**Field Name** **Field Type** **Description**

`condition` string Required. Criteria defined to filter the records.

`criteria` string Type of filter criteria that’s used to filter records for processing.

`dataSourceType` string Type of data source that's used to create the batch job definition. Valid values
are:

**•** SingleSobject

**•** MultiSobject

Available in API version 64.0 and later.

`filters` BatchDataSrcFilterCriteria Filter criterion that decides which records must be processed by the Batch
on page 477[] Management job.

orderFields BatchDataSourceOrderField Fields that are used to order the records before the records are added to a
on page 478 batch in a job.

`sourceObject` string

Required. API name of an object whose records must be processed by the
batch job.

If the batch job type is Loyalty Program Process, the source object must be:


Metadata Types BatchProcessJobDefinition

**Field Name** **Field Type** **Description**

**•** TransactionJournal if the batch job is used to process transaction journals
by applying the applicable loyalty program process.

**•** An object that stores the details of loyalty program members whose tier
must be assessed by the loyalty program process specified in the
executionProcessApiName field.

`sourceObjectField` string

BatchDataSrcFilterCriteria

API name of the source object field that uniquely identifies records for which
the batch job is executed. This field is available in API version 57.0 and later.

This field is only applicable when the batch job’s type is Loyalty Program Process
and a TierProcess type active loyalty program process is specified in the

`executionProcessApiName` field. Specify the API name of a field that
is a lookup to the LoyaltyProgramMember object and uniquely identifies the
members whose tier must be assessed.

Represents the filter conditions that decide which records must be processed by the Batch Management job.

Fields

**Field Name** **Field Type** **Description**

domainObjectName string Name of the object the field is associated with. Available in API version 64.0
and later.

`dynamicValueType` string Data type of the input variable used as a filter.

`fieldName` string Required. Name of the field that must be used to filter records.

`fieldPath` string Stores the path to a field in the object. Available in API version 64.0 and later.

`fieldValue` string Required. Value of the field that must be filtered. Specify the field if
`isDynamicValue` is set to `False` .

`isDynamicValue` boolean Required. Indicates whether the filter criteria is dynamic.

`operator` string (enumeration Required. Operator that is specified in the filter criteria. Valid values are:
of type string)

**•** `equals`

**•** `excludes`

**•** `greaterThan`

**•** `greaterThanOrEqualTo`

**•** `in`

**•** `includes`

**•** `lessThan`

**•** `LessThanOrEqualTo`


Metadata Types BatchProcessJobDefinition

**Field Name** **Field Type** **Description**

**•** `GreaterOrEqual`

**•** `like`

**•** `notEquals`

**•** `notIn`

`sequenceNo` integer Required. Sequence number used to refer the criteria in a filter.

BatchDataSourceOrderField

Represents the fields that are used to group data.

Fields

**Field Name** **Field Type** **Description**

domainObjectName string Required. Name of the object the field is associated with. Available in API version
64.0 and later.

`fieldName` string Required. Name of the field that must be used to filter records. Available in API
version 64.0 and later.

`fieldPath` string Required. Stores the path to a field in the object. Available in API version 64.0
and later.

Declarative Metadata Sample Definition

The following is an example of a BatchProcessJobDefinition component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <BatchProcessJobDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

     <batchSize>10</batchSize>

     <dataSource>

       <condition>1</condition>

       <criteria>all</criteria>

       <filters>

         <dynamicValue>false</dynamicValue>

         <dynamicValueType>string</dynamicValueType>

         <fieldName>Name</fieldName>

         <fieldValue>abcd</fieldValue>

         <operator>equals</operator>

         <sequenceNo>1</sequenceNo>

       </filters>

       <sourceObject>Account</sourceObject>

     </dataSource>

     <flowApiName>Flow1</flowApiName>

     <flowInputVariable>recordId</flowInputVariable>

```


Metadata Types BatchProcessJobDefinition

```
     <masterLabel>BatchJob1</masterLabel>

     <processGroup>Loyalty</processGroup>

     <retryCount>2</retryCount>

     <retryInterval>1000</retryInterval>

     <status>Inactive</status>

     <description>test</description>

     <type>Flow</type>

     <executionProcessApiName>testFlow</executionProcessApiName>

   </BatchProcessJobDefinition>

```

The following is an example of a Flow object used in Metadata API.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <!-
     ~ Copyright 2020 Salesforce, Inc.

     ~ All Rights Reserved

     ~ Company Confidential

   -->

   <Flow xmlns="http://soap.sforce.com/2006/04/metadata">

     <apiVersion>51.0</apiVersion>

     <interviewLabel>Flow1 {!$Flow.CurrentDateTime}</interviewLabel>

     <label>Flow1</label>

     <processMetadataValues>

       <name>BuilderType</name>

       <value>

         <stringValue>LightningFlowBuilder</stringValue>

       </value>

     </processMetadataValues>

     <processMetadataValues>

       <name>OriginBuilderType</name>

       <value>

         <stringValue>LightningFlowBuilder</stringValue>

       </value>

     </processMetadataValues>

     <processType>AutoLaunchedFlow</processType>

     <recordLookups>

       <name>getAcc</name>

       <label>getAcc</label>

       <locationX>614</locationX>

       <locationY>465</locationY>

       <assignNullValuesIfNoRecordsFound>false</assignNullValuesIfNoRecordsFound>

       <filterLogic>and</filterLogic>

       <filters>

         <field>Id</field>

         <operator>EqualTo</operator>

         <value>

           <elementReference>recordId</elementReference>

         </value>

       </filters>

       <getFirstRecordOnly>true</getFirstRecordOnly>

       <object>Account</object>

       <storeOutputAutomatically>true</storeOutputAutomatically>

     </recordLookups>

     <start>

```


### Metadata Types BillingSettings

```
       <locationX>73</locationX>

       <locationY>213</locationY>

       <connector>

         <targetReference>getAcc</targetReference>

       </connector>

     </start>

     <status>Draft</status>

     <variables>

       <name>recordId</name>

       <dataType>String</dataType>

       <isCollection>false</isCollection>

       <isInput>true</isInput>

       <isOutput>false</isOutput>

     </variables>

   </Flow>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <types>

       <members>*</members>

       <name>BatchProcessJobDefinition</name>

     </types>

     <types>

       <members>Flow1</members>

       <name>Flow</name>

     </types>

     <version>51.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### BillingSettings

Represents the settings for Salesforce Billing.

Parent Type and Manifest Access

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

[In the package manifest, all the settings metadata types for the org are accessed using the “Settings” name. See Settings for more details.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_settings.htm)

File Suffix and Directory Location

### The BillingSettings values are stored in the BillingSettings.settings file in the settings folder. The .settings

files are different from other named components, because there’s only one settings file for each settings component.


Metadata Types BillingSettings

Version

BillingSettings components are available in API version 62.0 and later.

Special Access Rules

These settings are available when Billing is enabled.

Fields

**Field Name** **Description**

```
acctRecGlAccount

billingContextDefinition

billingContextSourceMapping

billingIntraCtxtSrcMapping

defaultAPClosureDPEDefnName

defaultApplyCreditMemoFlow

```

**Field Type**
string

**Description**
General ledger account to record the credit amount for unrealized or realized losses
and the debit amount for unrealized or realized gains in transaction journals. Available
in API version 64.0 and later.

**Field Type**
string

**Description**
[Name of the context definition that the Create Billing Schedules for Orders API uses](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_create_billing_schedules.htm)
to understand your order data. Available in API version 64.0 and later.

**Field Type**
string

**Description**
Name of the context mapping that links Order fields to billing transaction context
nodes. Available in API version 64.0 and later.

**Field Type**
string

**Description**
Name of the custom context mapping that maps your custom or standard Order fields
to billing transaction context nodes. Available in API version 64.0 and later.

**Field Type**
string

**Description**
Org-wide default value to specify the Data Processing Engine (DPE) definition to close
legal entity accounting periods. Available in API version 64.0 and later.

**Field Type**
string


Metadata Types BillingSettings

**Field Name** **Description**

**Description**
Default flow that’s used to apply the credit memo to invoices. Available in API version
64.0 and later.

```
defaultBillingTreatment

defaultEmailTemplate

defaultInvPreviewTemplate

defaultInvoiceDocTemplate

defaultLegalEntity

defaultTaxTreatment

enableBillingDisputeManagement

```

**Field Type**
string

**Description**
Org-wide default value to specify the name of the billing treatment. Available in API
version 64.0 and later.

**Field Type**
string

**Description**
Default email template to send the generated invoice PDFs. Available in API version
64.0 and later.

**Field Type**
string

**Description**
Default template to generate PDFs of invoice previews. Available in API version 64.0
and later.

**Field Type**
string

**Description**
Default template to generate PDFs of invoices. Available in API version 64.0 and later.

**Field Type**
string

**Description**
Org-wide default value to specify the name of the legal entity. Available in API version
64.0 and later.

**Field Type**
string

**Description**
Org-wide default value to specify the name of the tax treatment. Available in API
version 64.0 and later.

**Field Type**
boolean


Metadata Types BillingSettings

**Field Name** **Description**

**Description**
Indicates whether to enable Dispute Management ( `true` ) or not ( `false` ). The default
value is `false` . Available in API version 66.0 and later.

```
enableBillingSetup

enableCreditMemoSequenceService

enableCrMemoApplicationToPostedInvoices

enableFailedPaymentsRetry

enableForeignExchangeTrxnJrnlCreation

```

**Field Type**
boolean

**Description**
Indicates whether to enable Billing setting ( `true` ) or not ( `false` ). The default value
is `false` .

**Field Type**
boolean

**Description**
Indicates whether to mandate the application of sequence policy for credit memos
( `true` ) or not ( `false` ). The default value is `false` .

Available in API version 66.0 and later with Revenue Cloud Billing.

**Field Type**
boolean

**Description**

Indicates whether to enable Apply Credits to Posted Invoices setting ( `true` ) or not
( `false` ). The default value is `false` .

This setting automates settlement of invoices through application of credits to posted
invoices. The credit application level determines whether credits are automatically
applied to invoices or invoice lines.

**Field Type**
boolean

**Description**

Indicates whether to retry failed payment schedule items automatically based on the
defined payment retry rules ( `true` ) or not ( `false` ). The default value is `false` .
Available in API version 66.0 and later.

**Field Type**
boolean

**Description**

Indicates whether to create Transaction Journal records for invoices that hold balance
amounts (partially settled and not fully settled posted invoices) to record foreign
exchange unrealized gains or losses during the closure activity of a legal entity
accounting period. The default value is `false` . Available in API version 65.0 and later
with Revenue Cloud Billing.


Metadata Types BillingSettings

**Field Name** **Description**

```
enableInvoiceEmailDelivery

enableInvoicePdfGeneration

enableInvoiceSequenceService

enableNegInvoiceLnConversionToCrMemoLn

enablePaymentSchedulesAndItemsCreation

enableRefundIssuingAndBalanceSettlement

```

**Field Type**
boolean

**Description**
Indicates whether to enable Configure Email Delivery Settings ( `true` ) or not ( `false` ).
The default value is `false` . Available in API version 63.0 and later with Revenue Cloud
Billing.

**Field Type**
boolean

**Description**
Indicates whether to enable Document Generation setting ( `true` ) or not ( `false` ).
The default value is `false` . Available in API version 63.0 and later with Revenue Cloud
Billing.

**Field Type**
boolean

**Description**

Indicates whether to mandate the application of sequence policy for posted invoices
( `true` ) or not ( `false` ). The default value is `false` .

If enabled, each posted invoice is assigned an invoice number. Available in API version
65.0 and later with Revenue Cloud Billing.

**Field Type**
boolean

**Description**
Indicates whether to enable Convert Negative Invoice Lines to Credit Memo Lines
setting ( `true` ) or not ( `false` ). The default value is `false` .

**Field Type**
boolean

**Description**

Indicates whether to create a default payment schedule policy and payment schedule
treatment ( `true` ) or not ( `false` ). The default value is `false` .

If enabled, payment schedules and payment schedule items are created during financial
transactions such as posting of invoices. Available in API version 64.0 and later with
Revenue Cloud Billing.

**Field Type**
boolean

**Description**

Indicates whether to issue refunds and settle balances ( `true` ) or not ( `false` ). The
default value is `false` .


Metadata Types BillingSettings

**Field Name** **Description**

If enabled, refunds are issued and credit memos are applied to any remaining invoice
balance when customers amend or cancel an order. Available in API version 67.0 and
later.

```
enableTransactionJournalCreation

enableTransactionsApplicationToInvoices

```

**Field Type**
boolean

**Description**

Indicates whether to create Transaction Journal records based on the defined general
ledger account assignment rules for the billing entities when billing transaction records
are created or updated ( `true` ) or not ( `false` ). The default value is `false` . Available
in API version 63.0 and later with Revenue Cloud Billing.

Billing transaction records include these transaction types.

**•** Invoice

**•** Invoice Line

**•** Invoice Line Tax

**•** Credit Memo

**•** Credit Memo Line

**•** Credit Memo Line Tax

**•** Payment

**•** Refund

**•** Payment Line Invoice

**•** Payment Line Invoice Line

**•** Credit Memo Inv Application

**•** Credit Memo Line Invoice Line

**Field Type**
boolean

**Description**

Indicates whether to enable Credit Application Level setting ( `true` ) or not ( `false` ).
The default value is `false` .

**Revenue Cloud Advanced**

This setting applies balances of credit memos to invoices or balances of credit memo
lines to invoice lines. For the latter, amounts and balances on the invoices are rolled-up
from the related invoice lines.

**Revenue Cloud Billing**

This setting applies balances of credit memos and payments to invoices or balances
of credit memo lines and payments lines to invoice lines. For the latter, amounts and
balances on the invoices are rolled-up from the related invoice lines.


Metadata Types BillingSettings

**Field Name** **Description**

```
enableTrxnAmountsStorageInCorpCurrency

realisedGainGlAccount

realisedLossGlAccount

ruleBasedCrAndPymtAppln

unrealisedGainGlAccount

unrealisedLossGlAccount

```

**Field Type**
boolean

**Description**

Indicates whether to allow conversion of amounts of the Invoice, Invoice Line, Credit
Memo, and Credit Memo Line records to your corporate currency ( `true` ) or not
( `false` ). The default value is `false` . Available in API version 63.0 and later.

Store the converted amounts in corporate currency-specific amount fields.

**Field Type**
string

**Description**
Name of the general ledger account to record realized gains in transaction journals.
Available in API version 64.0 and later.

**Field Type**
string

**Description**
Name of the general ledger account to record realized losses in transaction journals.
Available in API version 64.0 and later.

**Field Type**
string

**Description**
Automates the settlement of the posted invoices by applying payments and credits
that meet the specified application rules. The rules application level determines whether
payments or credits are applied first to the invoices. The ruleset displays a list of
selectable rules. Available in API version 66.0 and later.

**Field Type**
string

**Description**
Name of the general ledger account to record unrealized gains in transaction journals.
Available in API version 64.0 and later.

**Field Type**
string

**Description**
Name of the general ledger account to record unrealized losses in transaction journals.
Available in API version 64.0 and later.


### Metadata Types BlacklistedConsumer

Declarative Metadata Sample Definition

The following is an example of a BillingSettings component.

```
   <BillingSettings xmlns="http://soap.sforce.com/2006/04/metadata">

      <enableBillingSetup>true</enableBillingSetup>

      <enableForeignExchangeTrxnJrnlCreation>true</enableForeignExchangeTrxnJrnlCreation>

      <enableInvoicePdfGeneration>true</enableInvoicePdfGeneration>

     <enableTransactionsApplicationToInvoices>true</enableTransactionsApplicationToInvoices>

     <enableCrMemoApplicationToPostedInvoices>true</enableCrMemoApplicationToPostedInvoices>

      <enableInvoiceEmailDelivery>true</enableInvoiceEmailDelivery>

      <enableInvoiceSequenceService>true</enableInvoiceSequenceService>

      <enableTransactionJournalCreation>true</enableTransactionJournalCreation>

      <enableTrxnAmountsStorageInCorpCurrency>true</enableTrxnAmountsStorageInCorpCurrency>

      <enablePaymentSchedulesAndItemsCreation>true</enablePaymentSchedulesAndItemsCreation>

   </BillingSettings>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Billing</members>

        <name>Settings</name>

      </types>

      <version> 67.0 </version>

   </Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The wildcard
[applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the manifest](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_settings.htm)
[file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### BlacklistedConsumer

Represents a connected app that is inaccessible to your Salesforce org’s users. This type extends the Metadata metadata type and inherits
its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### BlacklistedConsumer components have the suffix .blacklistedConsumer and are stored in the blacklistedConsumers

folder.


Metadata Types BlacklistedConsumer

Version

BlacklistedConsumer components are available in API version 49.0 and later.

Fields

This metadata type contains the following fields:

**Field Name** **Field Type** **Description**

`blockedByApiWhitelisting` boolean Set to `true` to apply the Permitted Users policy, `Admin approved`
`users are pre-authorized` to all connected apps in the org.

This policy limits access to only users with the associated profile or
permission set assigned to the app. Set to `false` to allow access to
the connected app. False is the default value.

`consumerKey` string

Required. A value used by the consumer for identification of the
connected app to Salesforce. Referred to as `client_id` in OAuth 2.0.

After you define and save the value, it can’t be edited. The value must
be alphanumeric, can’t contain special characters or spaces, and must
be between 8–256 characters. Consumer keys must be globally unique.

`consumerName` string Required. The name of the connected app being blocked.

`masterLabel` string Required. The primary label for the connected app record.

Declarative Metadata Sample Definition

The following is an example of a component.

```
<BlacklistedConsumer xmlns="http://soap.sforce.com/2006/04/metadata">

   <consumerKey>testConsumerKey</consumerKey>

   <consumerName>testName</consumerName>

   <blockedByApiWhitelisting>false</blockedByApiWhitelisting>

   <masterLabel>myTest</masterLabel>

</BlacklistedConsumer>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>*</members>

     <name>BlacklistedConsumer</name>

   </types>

   <version>49.0</version>

</Package>

```


### Metadata Types Bot

Usage

Use this type judiciously for connected apps that you want to make inaccessible to your org’s users. Blocking an app ends all current
user sessions and prevents future sessions. To block malicious attempts to access your org’s data, we recommend using API Access
Control instead. This feature restricts users from accessing your Salesforce APIs unless they are pre-authorized through an approved
connected app.

### Bot

Represents a definition of an Einstein Bot configuration that can have one or more versions. Only one version can be active.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### Bot components have the suffix .bot and are stored in the bots folder.

Version

### Bot components are available in API version 43.0 and later.

Special Access Rules

### Bot is available only if Chat and Einstein Bots are enabled in your org. Bot metadata deployment and retrieval are not supported for Lead Nurturing and Sales Coach Agents.

Fields

**Field Name** **Field Type** **Description**

`agentDSLEnabled` boolean Reserved for internal use.

`agentTemplate` string If this Bot represents an agent, this field represents the name of the agent
template used to create it. Available in API version 64.0 and later.

```
agentType

```

GenAiAgentType
(enumeration of
type string)

`botMlDomain` LocalMlDomain on
page 490

Specifies the agent type for this agent. For example,
`AgentforceServiceAgent` . Available in API version 64.0 and
later.

Represents the Einstein intent set that groups intents, entities, and
variables associated with a bot. All Einstein Bot versions under the same
bot now share an intent set. Available in API version 44.0 and later.

`botUser` string Specifies the username of the user account, not the first and last name
or the user ID. Available in API version 46.0 and later.


Metadata Types Bot

**Field Name** **Field Type** **Description**

`botVersions` BotVersion on page Represents the configuration details for a specific Einstein Bots version,
510 including dialogs, intents, entities, and variables.

`contextVariables` ConversationContextVariable Represents the context variables that enable your bot to gather customer
on page 491 information regardless of channel. Available in API 45.0 and later.

`conversationChannelProviders` ConversationDefintonChannelProvider **i** Represents a list of the conversation channels linked to the bot. Available

[] on page 492 in API version 51.0 and later.

`defaultOutboundFlow` string Specifies a fallback escalation behavior if the primary agent escalation
behavior is not available. For example, Agentforce Service Agents can

route conversations to human service reps. Available in API version 65.0
and later.

`description` string A description of the bot.

`label` string Label that identifies the bot throughout the Salesforce user interface.

`logPrivateConversationData` boolean Specifies whether to log customer inputs as part of conversation data
( `true` ) or not ( `false` ). Available in API version 48.0 and later.

`pageContextVariables` PageContextVariable Provides page-level context variables for the bot. Available in API version
on page 493[] 64.0 and later.

sessionTimeout int Represents the maximum amount of minutes that a bot session can be
idle. Available in API version 58.0 and later.

```
type

```

LocalMlDomain

BotType Required. The default value is `Bot` . This field represents the configuration
(enumeration of type of the bot. Valid values are:
type string)

**•** `Bot`         - Default Einstein Bot configuration.

**•** `ExternalCopilot`         - An external-facing agent. For example,
an Agentforce Service agent.

**•** `InternalCopilot`         - An internal-facing agent. For example,
an Agentforce Employee agent.

An Einstein Intent Set local to the current bot version.

**Field Name** **Field Type** **Description**

`label` string Label that represents an Einstein Intent Set local to the current bot version
throughout the Salesforce user interface.

`mlIntents` MlIntent[] List of intents associated with this local intent set.

`mlSlotClasses` MlSlotClass[] List of entities associated with this local intent set.

`name` string Required. This unique name prevents conflicts with other local Einstein Intent
Sets. This name can contain only underscores and alphanumeric characters


Metadata Types Bot

**Field Name** **Field Type** **Description**

and must be unique in your org. It must begin with a letter, not include spaces,
not end with an underscore, and not contain two consecutive underscores.

ConversationContextVariable

A context variable local to the current bot version. Available in API version 45.0 and later.

**Field Name** **Field Type** **Description**

`contextVariableMappings` ConversationContextVariableMapping Represents the mapping between a context variable, channel type, and sObject
on page 492 field.

```
dataType

```

ConversationDataType Required. Represents the data type of the context variable. Valid values are:
(enumeration of type

**•** `Text`

string)

**•** `Text`

**•** `Number`

**•** `Boolean`

**•** `Object`

**•** `Date`

**•** `DateTime`

**•** `Currency`

**•** `Id`

`description` string A description of this variable. This value may be used by the Agentforce planner
service. Available in API version 63.0 and later.

`developerName` string Required. Represents the name of the context variable. Can contain only
underscores and alphanumeric characters and must be unique in your org. It

must begin with a letter, not include spaces, not end with an underscore, and
not contain two consecutive underscores.

`includeInPrompt` boolean Indicates whether the variable is injected into the prompt sent to the Agentforce
model. If `true`, the variable appears in the **Included Fields** section of the UI.

Note: The default variables `Id`, `EndUserId`, and
`EndUserLanguage` always appear in the **Included Fields** section
of the UI, regardless of their value of `includeInPrompt` . We
recommend that you don't change the value of `includeInPrompt`
for these default variables, as changing the value can prevent your agent
from accessing important session data.

Available in API version 63.0 and later.

`label` string Required. A label that identifies the context variable throughout the Salesforce
user interface.

`SObjectType` string Valid values are:

**•** `BotDefinition`


Metadata Types Bot

**Field Name** **Field Type** **Description**

**•** `Queue`

ConversationContextVariableMapping

Represents the mapping between a context variable, channel type, and sObject field.

**Field Name** **Field Type** **Description**

`fieldName` string Required. The API name of an SObject field to be used as part of the mapping.

```
messageType

```

MessageType Required. Represents the message channel. Valid values are:
(enumeration of type

**•** `Alexa`

string)

**•** `Alexa`

**•** `AppleBusinessChat` —Messages sent in enhanced Apple Messages
for Business channels.

**•** `EmbeddedMessaging` —Messages sent in Messaging for In-App and
Web channels. Available in API version 50.0 and later.

**•** `Facebook`

**•** `GoogleHome`

**•** `InternalCopilot`

**•** `Line`

**•** `Omega`

**•** `Phone`

**•** `Text`

**•** `WeChat`

**•** `WebChat`

**•** `WhatsApp`

`SObjectType` string Required. SObject type for the field property defined as part of the mapping.
Valid values are:

**•** `LiveChatTranscript`

**•** `MessagingEndUser`

**•** `MessagingSession`

ConversationDefinitionChannelProvider

The developer name of a conversation channel linked to the bot. Available in API version 51.0 and later.

Note: To add, edit, or remove a messaging channel, you must use the UI. If you deploy a bot with messaging channel providers,
those providers aren’t visible in Metadata API.


Metadata Types Bot

**Field Name** **Field Type** **Description**

`agentRequired` boolean Specifies whether an agent must be online for the bot to be active ( `true` ) or
not ( `false` ) The default is `false` .

`chatButtonName` string Required. The developer name of a LiveChatButton metadata component.

PageContextVariable

A page-level context variable used by the bot. Available in API version 64.0 and later.

**Field Name** **Field Type** **Description**

`SObjectType` string Specifies the sObject type associated with this page context variable.

```
dataType

```

ConversationDataType Required. Represents the data type of the page context variable. Valid values
(enumeration of type are:
string)

**•** `Text`

**•** `Number`

**•** `Boolean`

**•** `Object`

**•** `Date`

**•** `DateTime`

**•** `Currency`

**•** `Id`

`description` string A description of the page context variable.

`developerName` string Required. Represents the unique API name of the page context variable. Can
contain only underscores and alphanumeric characters and must be unique

in your org. It must begin with a letter, not include spaces, not end with an
underscore, and not contain two consecutive underscores.

`label` string Required. A label that identifies the page context variable throughout the
Salesforce user interface.

Declarative Metadata Sample Definition

The following is an example of a Bot. This example has been trimmed to make it easier to read.

```
<?xml version="1.0" encoding="UTF-8"?>

<Bot xmlns="http://soap.sforce.com/2006/04/metadata">

   <botMlDomain>

     <label>Astros Pizza</label>

     <mlIntents>

        <developerName>New_Order</developerName>

        <label>New Order</label>

        <mlIntentUtterances>

          <utterance>Today is pie day so I want pie</utterance>

```


Metadata Types Bot

```
           </mlIntentUtterances>

        </mlIntents>

        <mlSlotClasses>

           <developerName>Size</developerName>

           <extractionType>Value</extractionType>

           <label>Size</label>

           <mlSlotClassValues>

             <synonymGroup>

               <languages>en_US</languages>

               <terms>Big</terms>

               <terms>Extra Large</terms>

               <terms>X-Large</terms>

               <terms>Grande</terms>

               <terms>Huge</terms>

             </synonymGroup>

             <value>Large</value>

           </mlSlotClassValues>

        </mlSlotClasses>

        <name>Astros_Pizza_ld1</name>

      </botMlDomain>

      <botVersions>

        <fullName>v1</fullName>

        <botDialogGroups>

           <developerName>Order_Management</developerName>

           <label>Order Management</label>

        </botDialogGroups>

        <botDialogs>

           <botDialogGroup>Order_Management</botDialogGroup>

           <botSteps>

             <botMessages>

               <message> ������Pizza Time! ������ </message>

             </botMessages>

             <type>Message</type>

           </botSteps>

           <botSteps>

             <botStepConditions>

               <leftOperandName>Verified_User</leftOperandName>

               <leftOperandType>ConversationVariable</leftOperandType>

               <operatorType>Equals</operatorType>

               <rightOperandValue>false</rightOperandValue>

             </botStepConditions>

             <botSteps>

               <botNavigation>

                  <botNavigationLinks>

                    <targetBotDialog>Customer_Verification</targetBotDialog>

                  </botNavigationLinks>

                  <type>Call</type>

               </botNavigation>

               <type>Navigation</type>

             </botSteps>

             <type>Group</type>

           </botSteps>

           <botSteps>

             <botStepConditions>

```


Metadata Types Bot

```
               <leftOperandName>Location</leftOperandName>

               <leftOperandType>ConversationVariable</leftOperandType>

               <operatorType>IsNotSet</operatorType>

             </botStepConditions>

             <botSteps>

               <botNavigation>

                  <botNavigationLinks>

                    <targetBotDialog>Select_Location</targetBotDialog>

                  </botNavigationLinks>

                  <type>Call</type>

               </botNavigation>

               <type>Navigation</type>

             </botSteps>

             <type>Group</type>

           </botSteps>

           <botSteps>

             <botVariableOperation>

               <botInvocation>

                  <invocationActionName>CreateOrderService</invocationActionName>

                  <invocationActionType>apex</invocationActionType>

                  <invocationMappings>

                    <parameterName>customer</parameterName>

                    <type>Input</type>

                    <variableName>Contact</variableName>

                    <variableType>ConversationVariable</variableType>

                  </invocationMappings>

                  <invocationMappings>

                    <parameterName>location</parameterName>

                    <type>Input</type>

                    <variableName>Location</variableName>

                    <variableType>ConversationVariable</variableType>

                  </invocationMappings>

                  <invocationMappings>

                    <parameterName>output</parameterName>

                    <type>Output</type>

                    <variableName>Pizza_Order</variableName>

                    <variableType>ConversationVariable</variableType>

                  </invocationMappings>

               </botInvocation>

               <type>Set</type>

             </botVariableOperation>

             <type>VariableOperation</type>

           </botSteps>

           <botSteps>

             <botMessages>

              <message>Perfect, let&apos;s work on your order from our {!Location.Name}

    location</message>

             </botMessages>

             <type>Message</type>

           </botSteps>

           <botSteps>

             <botNavigation>

               <botNavigationLinks>

                  <targetBotDialog>Add_Items_to_Order</targetBotDialog>

```


Metadata Types Bot

```
               </botNavigationLinks>

               <type>Redirect</type>

             </botNavigation>

             <type>Navigation</type>

           </botSteps>

           <developerName>New_Order</developerName>

           <label>New Order</label>

           <mlIntent>New_Order</mlIntent>

           <showInFooterMenu>false</showInFooterMenu>

        </botDialogs>

        <conversationVariables>

           <dataType>Object</dataType>

           <developerName>Contact</developerName>

           <label>Contact</label>

        </conversationVariables>

        <conversationVariables>

           <dataType>Text</dataType>

           <developerName>Delivery_Address</developerName>

           <label>Delivery Address</label>

        </conversationVariables>

        <conversationVariables>

           <dataType>Object</dataType>

           <developerName>Pizza_Order</developerName>

           <label>Pizza Order</label>

        </conversationVariables>

        <entryDialog>Welcome</entryDialog>

        <mainMenuDialog>Main_Menu</mainMenuDialog>

      </botVersions>

      <contextVariables>

        <contextVariableMappings>

           <SObjectType>LiveChatTranscript</SObjectType>

           <fieldName>LiveChatTranscript.ChatKey</fieldName>

           <messageType>WebChat</messageType>

        </contextVariableMappings>

        <dataType>Text</dataType>

        <developerName>ChatKey</developerName>

        <label>Chat Key</label>

      </contextVariables>

      <contextVariables>

        <contextVariableMappings>

           <SObjectType>LiveChatTranscript</SObjectType>

           <fieldName>LiveChatTranscript.ContactId</fieldName>

           <messageType>WebChat</messageType>

        </contextVariableMappings>

        <dataType>Id</dataType>

        <developerName>ContactId</developerName>

        <label>Contact Id</label>

      </contextVariables>

      <contextVariables>

        <contextVariableMappings>

           <SObjectType>LiveChatTranscript</SObjectType>

           <fieldName>LiveChatTranscript.LiveChatVisitorId</fieldName>

           <messageType>WebChat</messageType>

        </contextVariableMappings>

```


### Metadata Types BotBlock

```
        <dataType>Id</dataType>

        <developerName>EndUserId</developerName>

        <label>End User Id</label>

      </contextVariables>

      <contextVariables>

        <contextVariableMappings>

           <SObjectType>LiveChatTranscript</SObjectType>

           <fieldName>LiveChatTranscript.Id</fieldName>

           <messageType>WebChat</messageType>

        </contextVariableMappings>

        <dataType>Id</dataType>

        <developerName>RoutableId</developerName>

        <label>Routable Id</label>

      </contextVariables>

   ....<conversationChannelProviders>

        <agentRequired>false</agentRequired>

        <chatButtonName>Chat_Button_For_Bot</chatButtonName>

      </conversationChannelProviders>

      <label>Astro&apos;s Pizza</label>

   </Bot>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Pizza_Bot</members>

        <name>Bot</name>

      </types>

      <version>45.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### BotBlock

Represents the configuration details for a specific Einstein Bot block, including dialogs and variables.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### BotBlock components have the suffix .botBlock and are stored in the botBlocks folder.


Metadata Types BotBlock

Version

BotBlock components are available in API version 58.0 and later.

Special Access Rules

BotBlock is available only if Chat and Einstein Bots are enabled in your org.

Bot metadata deployment and retrieval are not supported for Lead Nurturing and Sales Coach Agents.

Fields

**Field Name** **Description**

```
botBlockVersions

description

masterLabel

richContentEnabled

```

BotBlockVersion

**Field Type**

BotBlockVersion[]

**Description**
The configuration details for specific Einstein Bot block versions, including dialogs and
variables.

**Field Type**
string

**Description**
A description of the bot block.

**Field Type**
string

**Description**

Required.

A user-friendly label for BotBlock, which is defined when the block is created.

**Field Type**
boolean

**Description**
Indicates whether the block is available for enhanced bots ( `true` ) or for only standard
bots ( `false` ). The default is `false` .

Represents the configuration details for an Einstein Bot block version, including dialogs and variables.

**Field Name** **Description**

```
botDialogs

```

**Field Type**

BotDialog[] on page 514


Metadata Types BotBlock

**Field Name** **Description**

**Description**
The list of dialogs in this bot block.

```
conversationGoals

conversationLanguages

conversationVariables

description

mlDomain

permissionSet

status

```

**Field Type**

ConversationDefinitionGoal[] on page 534

**Description**
The list of goals in this bot block. Available in API version 57.0 and later.

**Field Type**
string

**Description**

Required.

Specifies the language of the bot block.

**Field Type**

ConversationVariable[] on page 535

**Description**
A container that stores a specific piece of data collected from the customer. You can
use variables within dialog actions as both inputs and outputs. Available in API version
44.0 and later.

**Field Type**
string

**Description**
A description of the bot block.

**Field Type**

LocalMlDomain on page 490

**Description**

Required.

The Einstein Intent Set that groups intents, entities, and variables associated with a
block.

**Field Type**
string

**Description**
The permission set associated with the bot block. Available in API version 59.0 and
later.

**Field Type**
ConvDefBlockVersionStatus (enumeration of type string)


Metadata Types BotBlock

**Field Name** **Description**

**Description**

Required.

Indicates whether a block is published or is a draft.

Values are:

**•** `Published`

Declarative Metadata Sample Definition

The following is an example of a BotBlock component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <BotBlock xmlns="http://soap.sforce.com/2006/04/metadata">

      <access xsi:nil="true"/>

      <botBlockVersions>

        <fullName>Published</fullName>

        <botDialogs>

           <developerName>Test_Dialog_1646070168572</developerName>

           <label>Test_Dialog_1646070168572</label>

           <showInFooterMenu>false</showInFooterMenu>

        </botDialogs>

        <botDialogs>

           <developerName>Test_Dialog_1646070168926</developerName>

           <label>Test_Dialog_1646070168926</label>

           <showInFooterMenu>false</showInFooterMenu>

        </botDialogs>

        <botDialogs>

           <botSteps>

             <stepIdentifier>s4</stepIdentifier>

             <type>Wait</type>

           </botSteps>

           <developerName>Main_Menu</developerName>

           <label>Main Menu</label>

           <mlIntent>Main_Menu</mlIntent>

           <showInFooterMenu>false</showInFooterMenu>

        </botDialogs>

        <botDialogs>

           <botSteps>

             <botMessages>

               <message>Goodbye! Click the &quot;End Chat&quot; button to end this

   chat</message>

               <messageIdentifier>m2</messageIdentifier>

             </botMessages>

             <stepIdentifier>s6</stepIdentifier>

             <type>Message</type>

           </botSteps>

           <botSteps>

             <stepIdentifier>s7</stepIdentifier>

             <type>Wait</type>

```


Metadata Types BotBlock

```
           </botSteps>

           <developerName>End_Chat</developerName>

           <label>End Chat</label>

           <mlIntent>End_Chat</mlIntent>

           <showInFooterMenu>false</showInFooterMenu>

        </botDialogs>

        <botDialogs>

           <botSteps>

             <botMessages>

               <message>Unfortunately, there are no agents available at the

   moment</message>

               <messageIdentifier>m3</messageIdentifier>

             </botMessages>

             <stepIdentifier>s8</stepIdentifier>

             <type>Message</type>

           </botSteps>

           <botSteps>

             <stepIdentifier>s9</stepIdentifier>

             <type>Wait</type>

           </botSteps>

           <developerName>No_Agent_Available</developerName>

           <label>No Agent</label>

           <showInFooterMenu>false</showInFooterMenu>

        </botDialogs>

        <botDialogs>

           <botSteps>

             <botMessages>

               <message>Hi! I&apos;m your helpful bot.</message>

               <messageIdentifier>m1</messageIdentifier>

             </botMessages>

             <stepIdentifier>s1</stepIdentifier>

             <type>Message</type>

           </botSteps>

           <botSteps>

             <conversationRecordLookup>

               <SObjectType>Account</SObjectType>

               <conditions>

                  <leftOperand>Account.Phone</leftOperand>

                  <operatorType>Equal</operatorType>

                  <rightOperandValue>Value</rightOperandValue>

                  <sortOrder>0</sortOrder>

               </conditions>

               <lookupFields>

                  <fieldName>Account.Phone</fieldName>

               </lookupFields>

               <lookupFields>

                  <fieldName>Account.OwnerId</fieldName>

               </lookupFields>

               <maxLookupResults>1</maxLookupResults>

               <sourceVariableName>_LastCustomerInput</sourceVariableName>

               <sourceVariableType>ConversationVariable</sourceVariableType>

               <targetVariableName>MyCustomVariable</targetVariableName>

             </conversationRecordLookup>

             <stepIdentifier>s2</stepIdentifier>

```


Metadata Types BotBlock

```
             <type>RecordLookup</type>

           </botSteps>

           <botSteps>

             <botNavigation>

               <botNavigationLinks>

                  <targetBotDialog>Main_Menu</targetBotDialog>

                  <targetVariable xsi:nil="true"/>

                  <targetVariableType xsi:nil="true"/>

               </botNavigationLinks>

               <type>Redirect</type>

             </botNavigation>

             <stepIdentifier>s3</stepIdentifier>

             <type>Navigation</type>

           </botSteps>

           <developerName>Welcome</developerName>

           <label>Welcome</label>

           <mlIntent>Welcome</mlIntent>

           <showInFooterMenu>false</showInFooterMenu>

        </botDialogs>

        <conversationLanguages>en_US</conversationLanguages>

        <conversationVariables>

           <dataType>Text</dataType>

           <developerName>TestVariableABC</developerName>

           <label>TestVariableABC</label>

        </conversationVariables>

        <conversationVariables>

           <dataType>Text</dataType>

           <developerName>TestVariableXYZ</developerName>

           <label>TestVariableXYZ</label>

        </conversationVariables>

        <conversationVariables>

           <collectionType>List</collectionType>

           <dataType>Object</dataType>

           <developerName>MyCustomVariable</developerName>

           <label>MyCustomVariable</label>

        </conversationVariables>

        <description>Created for testing.</description>

        <mlDomain>

           <label>vPub</label>

           <mlIntents>

             <developerName>End_Chat</developerName>

             <label>End Chat</label>

             <mlIntentUtterances>

               <language>es</language>

               <utterance>Utterance1</utterance>

             </mlIntentUtterances>

             <mlIntentUtterances>

               <language>es</language>

               <utterance>Utterance2</utterance>

             </mlIntentUtterances>

             <mlIntentUtterances>

               <language>es</language>

               <utterance>Utterance3</utterance>

             </mlIntentUtterances>

```


### Metadata Types BotTemplate

```
           </mlIntents>

           <mlIntents>

             <description>Main Menu Intent</description>

             <developerName>Main_Menu</developerName>

             <label>Main Menu</label>

           </mlIntents>

           <mlIntents>

             <description>Welcome Intent</description>

             <developerName>Welcome</developerName>

             <label>Welcome</label>

           </mlIntents>

           <name>blockDevName0001_vPub</name>

        </mlDomain>

        <status>Published</status>

      </botBlockVersions>

      <description>Collects the user&apos;s first name, last name, email address, phone

   number, and company name.</description>

      <masterLabel>User Info Collection Block</masterLabel>

      <richContentEnabled>true</richContentEnabled>

   </BotBlock>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>AgentTransfer</members>

        <name>BotBlock</name>

      </types>

      <version>58.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### BotTemplate

Represents the configuration details for a specific Einstein Bot template, including dialogs and variables.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### BotTemplate components have the suffix .botTemplate and are stored in the botTemplates folder.


Metadata Types BotTemplate

Version

BotTemplate components are available in API version 55.0 and later.

Special Access Rules

BotTemplate is available only if Chat and Einstein Bots are enabled in your org.

Bot metadata deployment and retrieval are not supported for Lead Nurturing and Sales Coach Agents.

Fields

**Field Name** **Description**

```
botDialogGroups

botDialogs

conversationLanguages

contextVariables

conversationGoals

conversationSystemDialogs

```

**Field Type**

BotDialogGroup[] on page 513

**Description**
The list of dialog groups in this bot template.

**Field Type**

BotDialog[] on page 514

**Description**
The list of dialogs in this bot template.

**Field Type**
string

**Description**

Required.

Specifies the language of the bot template.

**Field Type**

ConversationContextVariable[] on page 491

**Description**
Represents the context variables that enable your bot to gather customer information
regardless of channel.

**Field Type**

ConversationDefinitionGoal[] on page 534

**Description**
The list of goals in this bot template. Available in API version 57.0 and later.

**Field Type**

ConversationSystemDialog[] on page 535

**Description**
A system function assigned to a dialog.


Metadata Types BotTemplate

**Field Name** **Description**

```
conversationVariables

description

entryDialog

icon

mainMenuDialog

masterLabel

mlDomain

```

**Field Type**

ConversationVariable[] on page 535

**Description**
A container that stores a specific piece of data collected from the customer. You can
use variables within dialog actions as both inputs and outputs.

**Field Type**
string

**Description**
A description of the bot template.

**Field Type**
string

**Description**
A reference to the first dialog that the bot presents to your customer. For example,
`Welcome` .

**Field Type**
string

**Description**
The icon used to identify the template.

**Field Type**
string

**Description**
A reference to the dialog identified as the main menu dialog. For example, `Main`
`Menu` .

**Field Type**
string

**Description**

Required.

A user-friendly label for BotTemplate, which is defined when the BotTemplate is created.

**Field Type**

LocalMlDomain on page 490

**Description**

Required.

Represents the Einstein Intent Set that groups intents, entities, and variables associated
with a template.


Metadata Types BotTemplate

**Field Name** **Description**

```
permissionSet

richContentEnabled

type

```

**Field Type**
string

**Description**
The permission set associated with the bot template. Available in API version 59.0 and
later.

**Field Type**
boolean

**Description**
Indicates whether the template is available for enhanced bots ( `true` ) or for standard
bots ( `false` ). The default is `false` .

**Field Type**
BotType (enumeration of type string)

**Description**
This field represents the configuration type of the bot. The default value is `Bot` .

Valid values are:

**•** `Bot` —Default Einstein Bot configuration.

**•** `ExternalCopilot`  - An external-facing agent. For example, an Agentforce
Service agent.

**•** `InternalCopilot`  - An internal-facing agent. For example, an Agentforce
Employee agent.

Declarative Metadata Sample Definition

The following is an example of a BotTemplate component.

```
<?xml version="1.0" encoding="UTF-8"?>

<BotTemplate xmlns="http://soap.sforce.com/2006/04/metadata">

   <botDialogGroups>

     <developerName>dialog_group1</developerName>

     <label>dialog group1</label>

   </botDialogGroups>

   <botDialogs>

     <developerName>Test_Dialog_1</developerName>

     <label>Test_Dialog_1</label>

     <showInFooterMenu>false</showInFooterMenu>

   </botDialogs>

   <botDialogs>

     <developerName>Test_Dialog_2</developerName>

     <label>Test_Dialog_2</label>

     <showInFooterMenu>false</showInFooterMenu>

   </botDialogs>

   <botDialogs>

     <botSteps>

```


Metadata Types BotTemplate

```
           <botMessages>

             <message>Hi! I&apos;m your helpful bot.</message>

             <messageIdentifier>m1</messageIdentifier>

           </botMessages>

           <stepIdentifier>s1</stepIdentifier>

           <type>Message</type>

        </botSteps>

        <botSteps>

          <conversationRecordLookup>

            <SObjectType>Account</SObjectType>

            <conditions>

               <leftOperand>Account.Phone</leftOperand>

               <operatorType>Equal</operatorType>

               <rightOperandValue>Value</rightOperandValue>

               <sortOrder>0</sortOrder>

            </conditions>

            <lookupFields>

               <fieldName>Account.Phone</fieldName>

            </lookupFields>

            <lookupFields>

               <fieldName>Account.OwnerId</fieldName>

            </lookupFields>

            <maxLookupResults>1</maxLookupResults>

            <sourceVariableName>_LastCustomerInput</sourceVariableName>

            <sourceVariableType>ConversationVariable</sourceVariableType>

            <targetVariableName>MyCustomVariable</targetVariableName>

          </conversationRecordLookup>

          <stepIdentifier>s2</stepIdentifier>

          <type>RecordLookup</type>

        </botSteps>

        <botSteps>

           <botNavigation>

             <botNavigationLinks>

               <targetBotDialog>Main_Menu</targetBotDialog>

             </botNavigationLinks>

             <type>Redirect</type>

           </botNavigation>

           <stepIdentifier>s3</stepIdentifier>

           <type>Navigation</type>

        </botSteps>

        <developerName>Welcome</developerName>

        <label>Welcome</label>

        <mlIntent>Welcome</mlIntent>

        <showInFooterMenu>false</showInFooterMenu>

      </botDialogs>

      <botDialogs>

        <botSteps>

           <stepIdentifier>s4</stepIdentifier>

           <type>Wait</type>

        </botSteps>

        <developerName>Main_Menu</developerName>

        <label>Main Menu</label>

        <mlIntent>Main_Menu</mlIntent>

        <showInFooterMenu>false</showInFooterMenu>

```


Metadata Types BotTemplate

```
      </botDialogs>

      <botDialogs>

        <botSteps>

           <botMessages>

             <message>Goodbye! Click the &quot;End Chat&quot; button to end this

   chat</message>

             <messageIdentifier>m2</messageIdentifier>

           </botMessages>

           <stepIdentifier>s6</stepIdentifier>

           <type>Message</type>

        </botSteps>

        <botSteps>

           <stepIdentifier>s7</stepIdentifier>

           <type>Wait</type>

        </botSteps>

        <developerName>End_Chat</developerName>

        <label>End Chat</label>

        <mlIntent>End_Chat</mlIntent>

        <showInFooterMenu>false</showInFooterMenu>

      </botDialogs>

      <botDialogs>

        <botSteps>

           <botMessages>

            <message>Unfortunately, there are no agents available at the moment</message>

             <messageIdentifier>m3</messageIdentifier>

           </botMessages>

           <stepIdentifier>s8</stepIdentifier>

           <type>Message</type>

        </botSteps>

        <botSteps>

           <stepIdentifier>s9</stepIdentifier>

           <type>Wait</type>

        </botSteps>

        <developerName>No_Agent_Available</developerName>

        <label>No Agent</label>

        <showInFooterMenu>false</showInFooterMenu>

      </botDialogs>

      <contextVariables>

        <contextVariableMappings>

           <SObjectType>LiveChatTranscript</SObjectType>

           <fieldName>LiveChatTranscript.ChatKey</fieldName>

           <messageType>WebChat</messageType>

        </contextVariableMappings>

        <dataType>Text</dataType>

        <developerName>ChatKey</developerName>

        <label>Chat Key</label>

      </contextVariables>

      <conversationLanguages>en_US</conversationLanguages>

      <conversationSystemDialogs>

        <dialog>No_Agent_Available</dialog>

        <type>TransferFailed</type>

      </conversationSystemDialogs>

      <conversationSystemDialogs>

```


Metadata Types BotTemplate

```
        <dialog>Test_Dialog_1</dialog>

        <type>ErrorHandling</type>

      </conversationSystemDialogs>

      <conversationVariables>

        <dataType>Text</dataType>

        <developerName>TestVariableXYZ</developerName>

        <label>TestVariableXYZ</label>

      </conversationVariables>

      <conversationVariables>

        <collectionType>List</collectionType>

        <dataType>Object</dataType>

        <developerName>MyCustomVariable</developerName>

        <label>MyCustomVariable</label>

      </conversationVariables>

      <description>Description of BotTemplate</description>

      <entryDialog>Test_Dialog_1</entryDialog>

      <icon>AA8qwqXXXXX</icon>

      <mainMenuDialog>Test_Dialog_2</mainMenuDialog>

      <masterLabel>Astro Bot</masterLabel>

      <mlDomain>

        <label>Astro Bot</label>

        <mlIntents>

           <developerName>End_Chat</developerName>

           <label>End Chat</label>

           <mlIntentUtterances>

             <utterance>Utterance1</utterance>

             <language>es</language>

           </mlIntentUtterances>

           <mlIntentUtterances>

             <utterance>Utterance2</utterance>

             <language>es</language>

           </mlIntentUtterances>

           <mlIntentUtterances>

             <utterance>Utterance3</utterance>

             <language>es</language>

           </mlIntentUtterances>

        </mlIntents>

        <mlIntents>

           <developerName>Main_Menu</developerName>

           <label>Main Menu</label>

           <description>Main Menu Intent</description>

        </mlIntents>

        <mlIntents>

           <developerName>Welcome</developerName>

           <label>Welcome</label>

           <description>Welcome Intent</description>

        </mlIntents>

        <name>Astro_Bot_ld1</name>

      </mlDomain>

      <richContentEnabled>true</richContentEnabled>

   </BotTemplate>

```


### Metadata Types BotVersion

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>BotTemplate</name>

      </types>

      <version>55.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### BotVersion

Represents the configuration details for a specific Einstein Bot version, including dialogs and variables.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### BotVersion components have the suffix .bot and are stored in the bot folder. BotVersion is a top-level child of Bot and shares its

suffix and file directory.

Version

### BotVersion components are available in API version 43.0 and later.

Special Access Rules

### BotVersion is available only if Chat and Einstein Bots are enabled in your org.

Bot metadata deployment and retrieval are not supported for Lead Nurturing and Sales Coach Agents.

Fields

**Field Name** **Description**

```
botDialogGroups

```

**Field Type**

BotDialogGroup[] on page 513

**Description**
The list of dialog groups in this bot version.


Metadata Types BotVersion

**Field Name** **Description**

```
botDialogs

company

conversationGoals

conversationPlanner

conversationSystemDialogs

conversationVariables

copilotPrimaryLangauge

copilotSecondaryLanguages

```

**Field Type**

BotDialog[] on page 514

**Description**
The list of dialogs in this bot version.

**Field Type**
string

**Description**
Reserved for internal use.

**Field Type**

ConversationDefinitionGoal[] on page 534

**Description**
The list of goals in this bot verion. Available in API version 57.0 and later.

**Field Type**

ConversationDefinitionPlanner[] on page 534

**Description**
Represents the API name of the Agent planner service GenAiPlanner on page 1372.

Available in API version 60.0 and later.

**Field Type**

ConversationSystemDialog[] on page 535

**Description**
A system function assigned to a dialog. Available in API version 48.0 and later.

**Field Type**

ConversationVariable[] on page 535

**Description**
A container that stores a specific piece of data collected from the customer. You
can use variables within dialog actions as both inputs and outputs. Available in
API version 44.0 and later.

**Field Type**
Language (enumeration of type string)

**Description**
Represents the primary language of a Copilot or Agent.

**Field Type**
string

**Description**
Reserved for internal use.


Metadata Types BotVersion

**Field Name** **Description**

```
entryDialog

initialIntentDetectionEnabled

intentDisambiguationEnabled

intentThreshold

intentV3Enabled

knowledgeActionEnabled

knowledgeFallbackEnabled

```

**Field Type**
string

**Description**

Required.

A reference to the first dialog that the bot presents to your customer. For example,
`Welcome` .

**Field Type**
boolean

**Description**
Reserved for internal use.

**Field Type**
boolean

**Description**
Reserved for internal use.

**Field Type**
double

**Description**

Specifies how strictly a user message must match with a bot intent.

Valid values are between 1 and 5, where 1 is the least strict and 5 is the most strict.

To turn on this feature, contact Salesforce Customer Support. This field is available
in API version 63.0 and later.

**Field Type**
boolean

**Description**
Reserved for internal use.

**Field Type**
boolean

**Description**
Indicates whether a knowledge action is enabled. The default value is `false` .

**Field Type**
boolean

**Description**
Reserved for internal use.


Metadata Types BotVersion

**Field Name** **Description**

```
mainMenuDialog

nlpProviders

responseDelayMilliseconds

role

surfacesEnabled

toneType

```

BotDialogGroup

The list of dialog groups in this bot version.

**Field Type**
string

**Description**
A reference to the dialog identified as the main menu dialog. For example, `Main`
`Menu` .

**Field Type**

ConversationDefinitionNlpProvider[] on page 537

**Description**
Defines the language provider which is used for a particular language. Available
in API version 49.0 and later.

**Field Type**
int

**Description**
An optional default or custom delay after every bot response to simulate typing.

**Field Type**
string

**Description**
Reserved for internal use.

**Field Type**
boolean

**Description**
Reserved for internal use.

**Field Type**
GenAiBotToneType (enumeration of type string)

**Description**
The tone of the bot. Valid values are:

**•** `Casual`

**•** `Formal`

**•** `Neutral`


Metadata Types BotVersion

**Field Name** **Description**

```
description

developerName

label

```

BotDialog

The list of dialogs in this bot version.

**Field Type**
string

**Description**
A description of the bot dialog group.

**Field Type**
string

**Description**

Required.

This unique name prevents conflicts with other dialog groups associated with the same
bot version. This name can contain only underscores and alphanumeric characters. The
name must begin with a letter, not include spaces, not end with an underscore, and not
contain two consecutive underscores.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Field Type**
string

**Description**

Required.

A label that identifies the dialog group throughout the Salesforce user interface.

**Field Name** **Description**

```
botDialogGroup

botSteps

description

```

**Field Type**
string

**Description**
The bot dialog group that contains this bot dialog.

**Field Type**

BotStep[] on page 516

**Description**
A list of steps that are executed as part of the dialog.

**Field Type**
string


Metadata Types BotVersion

**Field Name** **Description**

**Description**
A description of the bot dialog.

```
developerName

isPlaceholderDialog

label

mlIntent

mlIntentTrainingEnabled

```

**Field Type**
string

**Description**

Required.

This unique name prevents conflicts with other dialogs associated with the same bot version.
This name can contain only underscores and alphanumeric characters. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two consecutive
underscores.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Field Type**
boolean

**Description**
In a bot block, indicates whether a dialog is a placeholder ( `true` ) or not ( `false` ). In a bot
template or bot version not associated with a bot block, this field is read-only and the value
is `false` . Available in API version 58.0 and later.

**Field Type**
string

**Description**

Required.

A label that identifies the dialog throughout the Salesforce user interface.

**Field Type**
string

**Description**

Required.

A label that identifies the dialog throughout the Salesforce user interface. The name of the
intent associated with a dialog.

**Field Type**
boolean

**Description**
Indicates whether Einstein is turned on to train an intent model for the dialog intent ( `true` )
or turned off for the exact match option ( `false` ). The default value is `false` . Available
in API version 46.0 and later.


Metadata Types BotVersion

**Field Name** **Description**

```
showInFooterMenu

```

BotStep

**Field Type**
boolean

**Description**
Indicates whether to show this dialog in the Bot Options menu. The default value is `false` .

A step that is executed as part of the dialog.

**Field Name** **Description**

```
booleanFilter

botInvocation

botMessages

botNavigation

botStepConditions

botSteps

```

**Field Type**
string

**Description**
This field is reserved for future use.

**Field Type**

BotInvocation on page 518

**Description**
Bot Invocation used by a BotStep of type `Invocation` .

**Field Type**

BotMessage[] on page 520

**Description**
List of bot messages used by a BotStep of type `Message` .

**Field Type**

BotNavigation on page 520

**Description**
Bot Navigation used by a BotStep of type `Navigation` .

**Field Type**

BotStepCondition[] on page 522

**Description**
List of BotStep conditions associated with a BotStep of type `Group` .

**Field Type**

BotStep[] on page 516

**Description**
List of BotSteps associated to a Bot Step of type `Group` .


Metadata Types BotVersion

**Field Name** **Description**

```
botVariableOperation

conditionLogicType

conversationRecordLookup

conversationStepGoalMappings

conversationSystemMessage

messageDefinition

stepIdentifier

```

**Field Type**

BotVariableOperation[] on page 523

**Description**
Bot Variable Operation used by a BotStep of type `VariableOperation` .

**Field Type**
ConversationDefinitionLogicalOperatorType (enumeration of type string)

**Description**
Represents the type of conditional logic used by a BotStep. Values are:

**•** `And`

**•** `Or`

Available in API version 58.0 and later.

**Field Type**

ConversationRecordLookup[] on page 528

**Description**
A lookup action to the Conversation record. Available in API version 46.0 and later.

**Field Type**

ConversationDefinitionStepGoalMapping[] on page 532

**Description**
The API name of a goal used by a BotStep of type GoalStep. Available in API version
57.0 and later.

**Field Type**

ConversationSystemMessage[] on page 532

**Description**
System messages that represent an action for a BotStep, such as transferring to an
agent or ending a chat. Available in API version 46.0 and later.

**Field Type**

ConversationDefinitionRichMessage[] on page 533

**Description**
List of configuration details used by a BotStep that references a messaging component.
Available in API version 54.0 and later.

**Field Type**
string

**Description**
A unique key that identifies a step within a dialog. It is used to link translated labels to
labels within the step. This field is recommended for all step records and is required
for translated step labels. Available in API version 53.0 and later.


Metadata Types BotVersion

**Field Name** **Description**

If a step is created via the UI, the `stepIdentifier` is automatically generated. If
a step is created via API, the `stepIdentifier` must be provided. The
`stepIdentifier` can contain letters, numbers, dashes, and underscores, up to
255 characters.

```
type

```

BotInvocation

**Field Type**
BotStepType (enumeration of type string)

**Description**

Required.

Values are:

**•** `GoalStep` (Available in API version 57.0 and later.)

**•** `Group`

**•** `Invocation`

**•** `Message`

**•** `Navigation`

**•** `RecordLookup` (Available in API version 48.0 and later.)

**•** `RichMessage` (Available in API version 54.0 and later.)

**•** `SystemMessage`

**•** `VariableOperation`

**•** `Wait`

Bot Invocation used by a BotStep of type `Invocation` .

**Field Name** **Description**

```
invocationActionName

invocationActionType

```

**Field Type**
string

**Description**
The name of the invocable action used by a Bot Invocation.

**Field Type**
ConversationInvocableTargetType (enumeration of type string)

**Description**
Available dialog action types are:

Values are:

**•** `apex`

**•** `externalService` (Available in API version 53.0 and later.)

**•** `flow`


Metadata Types BotVersion

**Field Name** **Description**

**•** `logFeedback` (Available in API version 51.0 and later.)

**•** `logGoalAchieved` (Deprecated in API version 57.0 and later.)

**•** `standardInvocableAction`

```
invocationMappings

```

BotInvocationMapping

**Field Type**

BotInvocationMapping[] on page 519

**Description**
List of Bot Invocation Mappings for a Bot Invocation.

List of Bot Invocation Mappings for a Bot Invocation.

**Field Name** **Description**

```
parameterName

recordName

type

value

```

**Field Type**
string

**Description**

Required.

Name of an Input/Output parameter of the parent Bot Invocation target.

**Field Type**
string

**Description**
Name of the record that is used as part of an Invocation mapping. Available in API
version 54.0 and later.

**Field Type**
BotInvocationMappingType (enumeration of type string)

**Description**

Required.

Values are:

**•** `Input`

**•** `Output`

**Field Type**
string

**Description**
Literal value to be assigned to the specified parameter.


Metadata Types BotVersion

**Field Name** **Description**

```
variableName

variableType

```

BotMessage

**Field Type**
string

**Description**
Name of the Bot Variable that is used as part of an Invocation mapping.

**Field Type**
ConversationVariableType (enumeration of type string)

**Description**
This field relates to the type of variable used in this invocation mapping.

Values are:

**•** `ContextVariable`

**•** `ConversationVariable`

**•** `PageContextVariable`

A bot message used by a BotStep of type `Message` .

**Field Name** **Description**

```
message

messageIdentifier

```

BotNavigation

**Field Type**
string

**Description**

Required.

Message to display as part of an outgoing message from the bot to the customer.

**Field Type**
string

**Description**
A unique key that identifies a message within a dialog. It is used to link translated labels
to labels within the message. This field is recommended for all message records and
is required for translated message labels. Available in API version 53.0 and later.

If a message is created via the UI, the `messageIdentifier` is automatically
generated. If a message is created via API, the `messageIdentifier` must be
provided. `messageIdentifier` can contain letters, numbers, dashes, and
underscores, up to 255 characters.

Bot navigation used by a BotStep of type `Navigation` .


Metadata Types BotVersion

**Field Name** **Description**

```
botNavigationLinks

type

```

BotNavigationLink

**Field Type**

BotNavigationLink[] on page 521

**Description**
List of Bot Navigation links associated with a Bot Navigation of type `Call` or
`Redirect` .

**Field Type**
BotNavigationType (enumeration of type string)

**Description**

Required.

Values are:

**•** `Call`

**•** `Redirect`

**•** `TransferToAgent`

List of Bot Navigation links associated with a Bot Navigation of type `Call` or `Redirect` .

**Field Name** **Description**

```
label

targetBotDialog

targetVariable

targetVariableType

```

**Field Type**
string

**Description**
Label displayed when more than one Bot Navigation Link is available under a Bot
Navigation of type `Redirect` . The target dialog label is used when no label is
provided.

**Field Type**
string

**Description**
Name of the target dialog to be called as part of this Bot Navigation Link.

**Field Type**
string

**Description**
In the Redirect to Dialog Rule Action, the ID of the target object variable to be called
as part of this Bot Navigation link. Available in API version 57.0 and later.

**Field Type**
ConversationVariableType (enumeration of type string)


Metadata Types BotVersion

**Field Name** **Description**

**Description**
In the Redirect to Dialog Rule Action, the type of variable referred to in
`targetVariable` . Available in API version 57.0 and later.

Values are:

**•** `ContextVariable`

**•** `ConversationVariable`

**•** `PageContextVariable`

BotStepCondition

List of BotStep conditions associated with a BotStep of type `Group` .

**Field Name** **Description**

```
leftOperandName

leftOperandType

operatorType

```

**Field Type**
string

**Description**

Required.

Name of the variable used as the left side of the condition operation.

**Field Type**
ConversationVariableType (enumeration of type string)

**Description**

Required.

Type of the variable used as the left side of the condition operation.

Values are:

**•** `ContextVariable`

**•** `ConversationVariable`

**•** `PageContextVariable`

**Field Type**
BotStepConditionOperatorType (enumeration of type string)

**Description**

Required.

Values are:

**•** `Equals`

**•** `GreaterThan` (Available in API version 47.0 and later.)

**•** `GreaterThanOrEqualTo` (Available in API version 47.0 and later.)

**•** `IsNotSet`


Metadata Types BotVersion

**Field Name** **Description**

**•** `IsSet`

**•** `LessThan` (Available in API version 47.0 and later.)

**•** `LessThanOrEqualTo` (Available in API version 47.0 and later.)

**•** `NotEquals`

```
rightOperandValue

```

BotVariableOperation

**Field Type**
string

**Description**
Value that is used as the right side of the condition operation. This value is ignored
when using `IsSet` and `IsNotSet` operators.

Bot variable operation used by a BotStep of type `VariableOperation` .

**Field Name** **Description**

```
askCollectIfSet

autoSelectIfSingleChoice

botInvocation

```

**Field Type**
boolean

**Description**
If `true`, the bot runs a Bot Variable Operation of type `Collect` regardless of whether
the variable already has a value. When a value exists for a variable, the bot asks the
user for the relevant information, and the bot overwrites the existing value with the
user-provided value. If `false`, the bot skips variables with an existing value and
maintains the existing value. The default is `false` . Available in API version 51.0 and
later.

**Field Type**
boolean

**Description**
If `true`, the bot automatically selects the answer in the conversation flow when only
one button choice is available in a Bot Variable Operation of type `Collect` and a
`quickReplyType` value of `Dynamic` . If `false`, the bot presents the single
button choice and waits for the user’s response. The default is `false` . Available in
API version 51.0 and later.

**Field Type**

BotInvocation on page 518

**Description**
Bot Invocation used to provide Dynamic choices by a Bot Variable Operation of type
`Collect` and `quickReplyType` of `Dynamic` .


Metadata Types BotVersion

**Field Name** **Description**

```
botMessages

botQuickReplyOptions

botVariableOperands

ignoreIntentRecognition

invalidInputBotNavigation

```

messageDefinition

```
optionalCollect

```

**Field Type**

BotMessage[] on page 520

**Description**
List of Bot Messages used as prompt messages by a Bot Variable Operation of type
`Collect` .

**Field Type**

BotQuickReplyOption[] on page 526

**Description**
List of static choice options used by a Bot Variable Operation of type `Collect` and
`quickReplyType` of `Static` .

**Field Type**

BotVariableOperand[] on page 527

**Description**
List of Bot Variable Operands associated with a Bot Variable of type `Set` or `Unset` .

**Field Type**
boolean

**Description**
If `true` the bot requires a response to a Question dialog step. The bot doesn't perform
intent recognition for any user messages that do not fit the entity requirements. The
bot repeats the question until the customer's response fits the entity requirements.
Available in API version 63.0 and later.

**Field Type**

BotNavigation on page 520

**Description**
Bot Navigation used by a Bot Variable Operation of type `Collect` . This navigation
is executed when the associated Bot Invocation doesn’t return any options.

**Field Type**

ConversationDefinitionRichMessage on page 533

**Description**
Configuration details that reference a messaging component. Outputs are used by a
Bot Variable Operation of type `Set` . Available in API version 58.0 and later.

**Field Type**
boolean

**Description**
If `true`, the bot asks the repair attempts once and then moves on to the next dialog
step. The default value is `false` . Available in API version 48.0 and later.


Metadata Types BotVersion

**Field Name** **Description**

```
quickReplyOptionTemplate

quickReplyType

quickReplyWidgetType

retryMessages

sourceVariableName

sourceVariableType

```

**Field Type**
string

**Description**
Formula template used to resolve a label for Dynamic choice options of type `Object` .

**Field Type**
BotQuickReplyType (enumeration of type string)

**Description**

Values are:

**•** `Dynamic`

**•** `Static`

**Field Type**
BotWidgetType (enumeration of type string)

**Description**

Values are:

**•** `Buttons`

**•** `Menu`

**Field Type**

BotMessage[] on page 520

**Description**
[In Conversation Repair, the messages assigned to repair attempts. Available in API](https://help.salesforce.com/articleView?id=bots_service_setup_dialog_question_text.htm&language=en_US)
version 48.0 and later.

**Field Type**
string

**Description**
Name of the source `VariableName` used in the variable operation. Available in
API version 47.0 and later.

**Field Type**
ConversationVariableType (enumeration of type string)

**Description**
This name defines the data type of `VariableName` used in the variable operation.

Values are:

**•** `ContextVariable`

**•** `ConversationVariable`

**•** `PageContextVariable`


Metadata Types BotVersion

**Field Name** **Description**

```
successMessages

type

variableOperationIdentifier

```

BotQuickReplyOption

**Field Type**

BotMessage[] on page 520

**Description**
In a File dialog step, the message displayed to the customer as part of type
`CollectAttachment` to confirm a successful file upload. Available in API version
57.0 and later.

**Field Type**
BotVariableOperationType (enumeration of type string)

**Description**

Required.

Values are:

**•** `Collect`

**•** `CollectAttachment` (Available in API version 57.0 and later.)

**•** `Set`

**•** `SetConversationLanguage` (Available in API version 53.0 and later.)

**•** `Unset`

**Field Type**
string

**Description**
A unique key that identifies a variable operation within a dialog. It is used to link
translated labels to labels within the variable operation. This field is recommended for
all variable operation records and is required for translated variable operation labels.
Available in API version 53.0 and later.

If a variable operation is created via the UI, the
`variableOperationIdentifier` is automatically generated. If a variable
operation is created via API, the `variableOperationIdentifier` must be
provided. `variableOperationIdentifier` can contain letters, numbers,
dashes, and underscores, up to 255 characters.

List of static choice options used by a bot variable operation of type `Collect` and `quickReplyType` of `Static` .

**Field Name** **Description**

```
literalValue

```

**Field Type**
string

**Description**

Required.


Metadata Types BotVersion

**Field Name** **Description**

Value to be displayed as a menu or button choice to your customer.

```
quickReplyOptionIdentifier

```

BotVariableOperand

**Field Type**
string

**Description**
A unique key that identifies a quick reply option within a dialog. It is used to link
translated labels to labels within the quick reply option. This field is recommended for
all quick reply option records and is required for translated quick reply option labels.
Available in API version 53.0 and later.

If a quick reply option is created via the UI, the `quickReplyOptionIdentifier`
is automatically generated. If a message is created via API, the
`quickReplyOptionIdentifier` must be provided.
`quickReplyOptionIdentifier` can contain letters, numbers, dashes, and
underscores, up to 255 characters.

List of bot variable operands associated with a bot variable of type `Set` or `Unset` .

**Field Name** **Description**

```
disableAutoFill

sourceName

sourceType

```

**Field Type**
boolean

**Description**
Disables auto-fill behavior for a bot variable under a bot variable operation of type
`Collect` .

**Field Type**
string

**Description**
Name of the source CustomField or MlSlotClass used in the variable operation.

**Field Type**
ConversationVariableOperandSourceType (enumeration of type string)

**Description**

Values are:

**•** `BotDefinition` (Available in API version 46.0 and later.)

**•** `ContextVariable` (Available in API version 45.0 and later.)

**•** `ConversationVariable`

**•** `FlowDefinition` (Available in API version 52.0 and later.)

**•** `MlSlotClass`

**•** `Queue` (Available in API version 46.0 and later.)


Metadata Types BotVersion

**Field Name** **Description**

**•** `StandardConversationVariable`

**•** `StandardMlSlotClass`

**•** `Value`

```
sourceValue

targetName

targetType

```

**Field Type**
string

**Description**
Literal value used as the source for this variable operation.

**Field Type**
string

**Description**

Required.

Name of the target variable used in the variable operation.

**Field Type**
ConversationVariableType (enumeration of type string)

**Description**

Required.

Type of the target used in the variable operation.

Values are:

**•** `ContextVariable`

**•** `ConversationVariable`

**•** `PageContextVariable`

ConversationRecordLookup

Information related to the linked conversation. Currently only works on Lightning Knowledge. Available in API version 46.0 and later.

**Field Name** **Description**

```
SObjectType

conditions

```

**Field Type**
string

**Description**

Required.

Specifies the SObjectType of the ID stored in a bot variable.

**Field Type**

ConversationRecordLookupCondition[] on page 530


Metadata Types BotVersion

**Field Name** **Description**

**Description**
The conditions associated with this lookup. Available in API version 51.0 and later.

```
filterLogic

lookupFields

maxLookupResults

sortFieldName

sortOrder

sourceVariableName

```

**Field Type**
string

**Description**
The logical operator that connects the conditions.

Values are:

**•** `And`

**•** `Or`

Available in API version 51.0 and later.

**Field Type**

ConversationRecordLookupField[] on page 531

**Description**
Definition of the fields that are used for this lookup.

**Field Type**
int

**Description**

Required.

The maximum number of records to return (1-3).

**Field Type**
string

**Description**
The name of the field used to sort the lookup results. Available in API version 51.0 and
later.

**Field Type**
SortOrder (enumeration of type string)

**Description**
The display order of the lookup results.

Values are:

**•** `Asc`

**•** `Desc`

Available in API version 51.0 and later.

**Field Type**
string


Metadata Types BotVersion

**Field Name** **Description**

**Description**
The input for this lookup operation.

```
sourceVariableType

targetVariableName

```

**Field Type**
ConversationVariableType (enumeration of type string)

**Description**
Type of the target used in the variable operation.

Values are:

**•** `ContextVariable`

**•** `ConversationVariable`

**•** `PageContextVariable`

**Field Type**
string

**Description**

Required.

The variable that holds the results of this lookup.

ConversationRecordLookupCondition

List of conditions associated with a ConversationRecordLookup. Available in API version 51.0 and later.

**Field Name** **Description**

```
leftOperand

operatorType

```

**Field Type**
string

**Description**

Required.

Field on which the condition operation takes place.

**Field Type**
string

**Description**

Required.

The operator applied to the leftOperand.

Values are:

**•** `Equals`

**•** `NotEquals`

**•** `IsSet`


Metadata Types BotVersion

**Field Name** **Description**

**•** `IsNotSet`

**•** `GreaterThan`

**•** `LessThan`

**•** `GreaterThanOrEqualTo`

**•** `LessThanOrEqualTo`

```
rightOperandName

rightOperandType

rightOperandValue

sortOrder

```

**Field Type**
string

**Description**
The name of the variable to compare against.

**Field Type**
ConversationVariableType (enumeration of type string)

**Description**
The type of the variable to compare against.

Values are:

**•** `ContextVariable`

**•** `ConversationVariable`

**•** `PageContextVariable`

**Field Type**
string

**Description**
The custom value to compare against. This value is ignored when using `IsSet` and
`IsNotSet` operators.

**Field Type**
int

**Description**

Required.

Order in which the conditions are applied.

ConversationRecordLookupField

The fields used in a conversation record lookup. Available in API version 46.0 and later.

**Field Name** **Description**

```
fieldName

```

**Field Type**
string


Metadata Types BotVersion

**Field Name** **Description**

**Description**

Required.

Defines the field names used in the Conversation Lookup function.

ConversationDefinitionStepGoalMapping

Represents the association between a goal and a BotStep. A goal can be associated with only one BotStep and one dialog at a time.
Available in API version 57.0 and later.

**Field Name** **Description**

```
goalName

```

**Field Type**
string

**Description**
The API name of the goal.

ConversationSystemMessage

System messages that represent an action for a Bot Step, such as transferring to an agent or ending a chat. Available in API version 46.0
and later.

**Field Name** **Description**

```
systemMessageMappings

type

```

**Field Type**

ConversationSystemMessageMapping on page 532

**Description**
Defines the type of system message to be sent.

**Field Type**
ConversationSystemMessageType (enumeration of type string)

**Description**

Required.

This field defines the values available for a system message.

Values are:

**•** `EndChat`

**•** `Transfer`

ConversationSystemMessageMapping

List of mappings that indicate additional information provided for the system message. Available in API version 46.0 and later.


Metadata Types BotVersion

**Field Name** **Description**

```
mappingType

parameterType

variableName

```

**Field Type**
ConversationMappingType (enumeration of type string)

**Description**

Required.

Defines the type of mapping used in the record.

Values are:

**•** `Input`

**•** `Output`

**Field Type**
ConversationSystemMessageParamType (enumeration of type string)

**Description**

Required.

Defines the type of parameter the value is mapped to.

Values are:

**•** `Transfer`

**Field Type**
string

**Description**

Required.

Name of the variable that contains the value passed to the system message.

ConversationDefinitionRichMessage

Represents the configuration details for referencing a messaging component, such as an enhanced link. Available in API version 54.0
and later.

**Field Name** **Description**

```
messageDefinitionMappings

```

**Field Type**

BotInvocationMapping[] on page 519

**Description**
List of mappings for referencing a messaging component. Includes any input
parameters and their values. Optionally, specifies the conversation variable for storing
any outputs.

Input parameter values can be either static values or references to conversation or
context variables.


Metadata Types BotVersion

**Field Name** **Description**

```
messageDefinitionName

```

**Field Type**
string

**Description**

Required.

The API name of the messaging component referenced by the bot.

ConversationDefinitionGoal

A goal included in the bot version. Available in API version 57.0 and later.

**Field Name** **Description**

```
developerName

label

```

**Field Type**
string

**Description**

Required.

A unique name that prevents conflicts with other goals associated with the same bot
version. This name can contain only underscores and alphanumeric characters. It must
begin with a letter, not include spaces, not end with an underscore, and not contain
two consecutive underscores.

**Field Type**
string

**Description**

Required.

A label that identifies the goal throughout the Salesforce user interface. This label can
contain only underscores and alphanumeric characters. It must begin with a letter,
not include spaces, not end with an underscore, and not contain two consecutive
underscores.

ConversationDefinitionPlanner

Represents the API name for the Agent planner service. Available in API version 60.0 and later.

**Field Name** **Description**

```
genAiPlannerName

```

**Field Type**
string


Metadata Types BotVersion

**Field Name** **Description**

**Description**
The name of an agent planner service that uses a large language model (LLM) and a
reasoning strategy to decompose a given task into smaller subtasks, identify the most
suitable actions for each subtask, and invoke them.

ConversationSystemDialog

A system function assigned to a dialog. Available in API version 48.0 and later.

**Field Name** **Description**

```
dialog

type

```

ConversationVariable

**Field Type**
string

**Description**
The dialog name triggered when this system event fires.

**Field Type**
ConversationSystemDialogType (enumeration of type string)

**Description**
The type of system event. Required. Valid values are:

**•** `Disambiguation` (Reserved for Future Use)

**•** `DisambiguationFailed` (Reserved for Future Use)

**•** `ErrorHandling`

**•** `KnowledgeAction` (Available in API version 60.0.)

**•** `KnowledgeFallback` (Available in API version 51.0.)

**•** `TransferFailed`

A container that stores a specific piece of data collected from the customer. You can use variables within dialog actions as both inputs
and outputs. Available in API version 44.0 and later.

**Field Name** **Description**

```
collectionType

dataType

```

**Field Type**
ConversationVariableCollectionType (enumeration of type string)

**Description**
This field defines whether a variable is designated as a List Variable. Valid value is List.

**Field Type**
ConversationVariableCollectionType (enumeration of type string)


Metadata Types BotVersion

**Field Name** **Description**

**Description**

Required.

Valid values are:

**•** `Boolean`

**•** `Currency`

**•** `Date`

**•** `DateTime`

**•** `Id` (available in API 45.0 and later.)

**•** `Object`

**•** `Number`

**•** `Text`

```
description

developerName

includeInPrompt

```

**Field Type**
string

**Description**

A description of this variable. This value may be used by the Agentforce planner service.
Available in API version 63.0 and later.

**Field Type**
string

**Description**

Required.

This name can contain only underscores and alphanumeric characters and must be unique
in your org. It must begin with a letter, not include spaces, not end with an underscore, and
not contain two consecutive underscores. Only users with View DeveloperName OR View
Setup and Configuration permission can view, group, sort, and filter this field.

**Field Type**
boolean

**Description**
Indicates whether the variable is injected into the prompt sent to the Agentforce model. If
`true`, the variable appears in the **Included Fields** section of the UI.

Note: The default variables `Id`, `EndUserId`, and `EndUserLanguage` always
appear in the **Included Fields** section of the UI, regardless of their value of

`includeInPrompt` . We recommend that you don't change the value of
`includeInPrompt` for these default variables, as changing the value can prevent
your agent from accessing important session data.

Available in API version 63.0 and later.


Metadata Types BotVersion

**Field Name** **Description**

```
label

SObjectType

visibility

```

**Field Type**
string

**Description**

Required.

Label that identifies a variable throughout the Salesforce user interface.

**Field Type**
string

**Description**
Specifies the SObjectType of the ID stored in a bot variable. Valid values are:

**•** `BotDefinition`

**•** `Queue`

**Field Type**
ConversationVariableVisibilityType (enumeration of type string)

**Description**

Required. Determines which components can set this variable. If the visibility is `internal`,
the variable can only be set by action outputs. If the visibility is `external`, the variable
can also be set by the API.

Valid values are:

**•** `internal`

**•** `external`

ConversationDefinitionNlpProvider

Defines the natural language service that is used for the language assigned to a bot version. Available in API version 49.0 and later.

**Field Name** **Description**

```
language

nlpProviderName

```

**Field Type**
Language

**Description**

Required.

The language assigned to a bot version.

**Field Type**
string

**Description**
If nlpProviderType is EinsteinAI, this field is blank. If Apex, this field holds the Apex class
name of the service.


Metadata Types BotVersion

**Field Name** **Description**

```
nlpProviderType

```

**Field Type**
ConversationDefinitionNlpProviderType (enumeration of type string)

**Description**

Required.

Default value is `EinsteinAi` . Valid values are:

**•** `EinsteinAi`

**•** `Apex`

Declarative Metadata Sample Definition

The following is an example of a BotVersion.

```
<?xml version="1.0" encoding="UTF-8"?>

<Bot xmlns="http://soap.sforce.com/2006/04/metadata">

   <botMlDomain>

     <label>Astros Pizza</label>

     <mlIntents>

        <developerName>New_Order</developerName>

        <label>New Order</label>

        <mlIntentUtterances>

          <utterance>Today is pie day so I want pie</utterance>

        </mlIntentUtterances>

     </mlIntents>

     <mlSlotClasses>

        <developerName>Size</developerName>

        <extractionType>Value</extractionType>

        <label>Size</label>

        <mlSlotClassValues>

          <synonymGroup>

            <languages>en_US</languages>

            <terms>Big</terms>

            <terms>Extra Large</terms>

            <terms>X-Large</terms>

            <terms>Grande</terms>

            <terms>Huge</terms>

          </synonymGroup>

          <value>Large</value>

        </mlSlotClassValues>

     </mlSlotClasses>

     <name>Astros_Pizza_ld1</name>

   </botMlDomain>

   <botVersions>

     <fullName>v1</fullName>

     <botDialogGroups>

        <developerName>Order_Management</developerName>

        <label>Order Management</label>

     </botDialogGroups>

     <botDialogs>

```


Metadata Types BotVersion

```
           <botDialogGroup>Order_Management</botDialogGroup>

           <botSteps>

             <botMessages>

               <message> ������Pizza Time! ������ </message>

               <messageIdentifier>Greeting_Message</messageIdentifier>

             </botMessages>

             <stepIdentifier>Greeting</stepIdentifier>

             <type>Message</type>

           </botSteps>

           <botSteps>

             <botStepConditions>

               <leftOperandName>Verified_User</leftOperandName>

               <leftOperandType>ConversationVariable</leftOperandType>

               <operatorType>Equals</operatorType>

               <rightOperandValue>false</rightOperandValue>

             </botStepConditions>

             <botSteps>

               <botNavigation>

                  <botNavigationLinks>

                    <targetBotDialog>Customer_Verification</targetBotDialog>

                  </botNavigationLinks>

                  <type>Call</type>

               </botNavigation>

               <stepIdentifier>Call_Customer_Verification</stepIdentifier>

               <type>Navigation</type>

             </botSteps>

             <stepIdentifier>Verify_User</stepIdentifier>

             <type>Group</type>

           </botSteps>

           <botSteps>

             <botStepConditions>

               <leftOperandName>Location</leftOperandName>

               <leftOperandType>ConversationVariable</leftOperandType>

               <operatorType>IsNotSet</operatorType>

             </botStepConditions>

             <botSteps>

               <botNavigation>

                  <botNavigationLinks>

                    <targetBotDialog>Select_Location</targetBotDialog>

                  </botNavigationLinks>

                  <type>Call</type>

               </botNavigation>

               <stepIdentifier>Call_Select_Location</stepIdentifier>

               <type>Navigation</type>

             </botSteps>

             <stepIdentifier>Set_Location</stepIdentifier>

             <type>Group</type>

           </botSteps>

           <botSteps>

             <botVariableOperation>

               <botInvocation>

                  <invocationActionName>CreateOrderService</invocationActionName>

                  <invocationActionType>apex</invocationActionType>

                  <invocationMappings>

```


Metadata Types BotVersion

```
                    <parameterName>customer</parameterName>

                    <type>Input</type>

                    <variableName>Contact</variableName>

                    <variableType>ConversationVariable</variableType>

                  </invocationMappings>

                  <invocationMappings>

                    <parameterName>location</parameterName>

                    <type>Input</type>

                    <variableName>Location</variableName>

                    <variableType>ConversationVariable</variableType>

                  </invocationMappings>

                  <invocationMappings>

                    <parameterName>output</parameterName>

                    <type>Output</type>

                    <variableName>Pizza_Order</variableName>

                    <variableType>ConversationVariable</variableType>

                  </invocationMappings>

               </botInvocation>

               <type>Set</type>

               <variableOperationIdentifier>Set_Order</variableOperationIdentifier>

             </botVariableOperation>

             <stepIdentifier>Create_Order</stepIdentifier>

             <type>VariableOperation</type>

           </botSteps>

           <botSteps>

             <botMessages>

              <message>Perfect, let&apos;s work on your order from our {!Location.Name}

    location</message>

               <messageIdentifier>Start_Order_Message</messageIdentifier>

             </botMessages>

             <stepIdentifier>Start_Order</stepIdentifier>

             <type>Message</type>

           </botSteps>

           <botSteps>

             <messageDefinition>

               <messageDefinitionName>Astros_Pizza_Menu</messageDefinitionName>

             </messageDefinition>

             <stepIdentifier>36e5a7cb-50c4-4279-aa06-1217eba1bf62</stepIdentifier>

             <type>RichMessage</type>

           </botSteps>

           <botSteps>

             <botNavigation>

               <botNavigationLinks>

                  <targetBotDialog>Add_Items_to_Order</targetBotDialog>

               </botNavigationLinks>

               <type>Redirect</type>

             </botNavigation>

             <stepIdentifier>Proceed_To_Add_Items</stepIdentifier>

             <type>Navigation</type>

           </botSteps>

           <developerName>New_Order</developerName>

           <label>New Order</label>

           <mlIntent>New_Order</mlIntent>

           <showInFooterMenu>false</showInFooterMenu>

```


### Metadata Types BrandingSet

```
        </botDialogs>

        <conversationVariables>

           <dataType>Object</dataType>

           <developerName>Contact</developerName>

           <label>Contact</label>

        </conversationVariables>

        <conversationVariables>

           <dataType>Text</dataType>

           <developerName>Delivery_Address</developerName>

           <label>Delivery Address</label>

        </conversationVariables>

        <conversationVariables>

           <dataType>Object</dataType>

           <developerName>Pizza_Order</developerName>

           <label>Pizza Order</label>

        </conversationVariables>

        <entryDialog>Welcome</entryDialog>

        <mainMenuDialog>Main_Menu</mainMenuDialog>

      </botVersions>

      <label>Astro&apos;s Pizza</label>

   </Bot>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Astros Pizza_Bot.v1</members>

        <name>BotVersion</name>

      </types>

      <version>45.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

### BrandingSet

Represents the definition of a set of branding properties for an Experience Builder site or for your org's Lightning Experience theme.

This type extends the Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### BrandingSet components have the suffix brandingSet and are stored in the brandingSets folder.


Metadata Types BrandingSet

Version

BrandingSet components are available in API version 40.0 and later.

Special Access Rules

The BrandingSet type is available when at least one of the following is enabled in your org: Digital Experiences, Surveys, or Lightning
Experience. All users, including unauthenticated guest users, can access this type.

Fields

**Field Name** **Field Type** **Description**

`brandingSetProperty` BrandingSetProperty[] An array containing the name and value of each branding property, such
as `TextColor:#333` .

`description` string A description of the set of branding properties.

`masterLabel` string Required. The user interface name of the set of branding properties.

`type` string The assigned branding set definition for this BrandingSet.

BrandingSetProperty

Represents the definition of a branding property in the Theme panel in Experience Builder or in the Edit Theme page in Setup.

**Field Name** **Field Type** **Description**

`propertyName` string Required. The name of the branding property, such as `TextColor` .

`propertyValue` string The value of the branding property, such as `#333` .

Branding Properties for Lightning Experience Themes

Use these properties to describe Lightning Experience themes. Each propertyName is case-sensitive and must use all capital letters.
Some properties only apply to either Salesforce Lightning Design System (SLDS) 1 themes or SLDS 2 themes.

**Property** **Description**

```
ACCENT_COLOR_1

```

**Field Type**
string

**Description**
The primary accent color used to highlight active states of the
user interface like navigation, tabs, and hover states. Must be
a valid hex color string in the format #54C254.

Available only for SLDS 2 themes. Available in API version 64.0
and later.


Metadata Types BrandingSet

**Property** **Description**

```
ACCENT_COLOR_2

ACCENT_COLOR_3

ACCENT_CONTAINER_CONTENT_COLOR_1

ACCENT_CONTAINER_CONTENT_COLOR_2

ACCENT_CONTAINER_CONTENT_COLOR_3

```

**Field Type**
string

**Description**
A variant of the primary accent color used to highlight active
states of the user interface like navigation, tabs, and hover
states. Must be a valid hex color string in the format #54C254.

Available only for SLDS 2 themes. Available in API version 64.0
and later.

**Field Type**
string

**Description**
A variant of the primary accent color used to highlight active
states of the user interface, like navigation, tabs, and hover
states. Must be a valid hex color string in the format #54C254.

Available only for SLDS 2 themes. Available in API version 64.0
and later.

**Field Type**
string

**Description**
The primary color used for the icons and text within accent
containers. Must be a valid hex color string in the format
#54C254.

Available only for SLDS 2 themes. Available in API version 65.0
and later.

**Field Type**
string

**Description**
A variant of the primary color used for the icons and text within
accent containers. Must be a valid hex color string in the format
#54C254.

Available only for SLDS 2 themes. Available in API version 65.0
and later.

**Field Type**
string

**Description**
A variant of the primary color used for the icons and text within
accent containers. Must be a valid hex color string in the format
#54C254.


Metadata Types BrandingSet

**Property** **Description**

Available only for SLDS 2 themes. Available in API version 65.0
and later.

```
BANNER_IMAGE

BRAND_COLOR

BRAND_IMAGE

CONTAINER_ACCENT_COLOR_1

CONTAINER_ACCENT_COLOR_2

```

**Field Type**
string

**Description**
The path to the image to display in the background of your
org's pages. Use a JPG, PNG, or GIF that's 1800x360 pixels and
[smaller than 5 MB. Must refer to an asset file that already exists](https://help.salesforce.com/s/articleView?id=experience.admin_files_asset_files.htm&type=5&language=en_US)
within the org.

Available only for SLDS 1 themes.

**Field Type**
string

**Description**
The color to display on your nav bar and other important areas
of Salesforce. Must be a valid hex color string in the format
#54C254.

**Field Type**
string

**Description**
The path to the image to display as your logo. Use a JPG, PNG,
or GIF that’s 600x120 pixels and smaller than 5 MB. Must refer
[to an asset file that already exists within the org.](https://help.salesforce.com/s/articleView?id=experience.admin_files_asset_files.htm&type=5&language=en_US)

**Field Type**
string

**Description**
The primary color used for the background of branded
component containers like the brand button. Container accent
colors are also used for hover states for branded component
containers. Must be a valid hex color string in the format
#54C254.

Available only for SLDS 2 themes. Available in API version 64.0
and later.

**Field Type**
string

**Description**
A variant of the primary color used for the background of
branded component containers. Container accent colors are
also used for hover states for branded component containers.
Must be a valid hex color string in the format #54C254.


Metadata Types BrandingSet

**Property** **Description**

Available only for SLDS 2 themes. Available in API version 64.0
and later.

```
CONTAINER_ACCENT_COLOR_3

GROUP_IMAGE

GROUPS_BANNER_IMAGE

HEADER_BACKGROUND_COLOR

LINK_AS_BACKGROUND

```

**Field Type**
string

**Description**
A variant of the primary color used for the background of
branded component containers. Container accent colors are
also used for hover states for branded component containers.
Must be a valid hex color string in the format #54C254.

Available only for SLDS 2 themes. Available in API version 64.0
and later.

**Field Type**
string

**Description**
The default group avatar image. Use a JPG, PNG, or GIF that's
200x200 pixels and smaller than 5 MB. Group owners can
[change their avatar image. Must refer to an asset file that](https://help.salesforce.com/s/articleView?id=experience.admin_files_asset_files.htm&type=5&language=en_US)
already exists within the org.

**Field Type**
string

**Description**
The default banner image for group pages. Use a JPG, PNG, or
GIF that’s 1800x360 pixels and smaller than 5 MB. Group owners
[can change their banner image. Must refer to an asset file that](https://help.salesforce.com/s/articleView?id=experience.admin_files_asset_files.htm&type=5&language=en_US)
already exists within the org.

**Field Type**
string

**Description**
The color to display at the top of your org pages. Your logo,
global search, and global actions appear on top of the global
header background. Must be a valid hex color string in the
format #54C254.

Available only for SLDS 1 themes.

**Field Type**
boolean

**Description**
Indicates whether you want links in your org to use your
selected brand color ( `true` ) or not ( `false` ). The default value
is `true` .


Metadata Types BrandingSet

**Property** **Description**

Available only for SLDS 1 themes.

```
OVERRIDE_A11Y_COLOR

OVERRIDE_LOADING_PAGE

PAGE_BACKGROUND_COLOR

PROFILE_BANNER_IMAGE

USER_IMAGE

```

**Field Type**
string

**Description**
When you select a value for `BRAND_COLOR`, a color palette
that complements your brand color and is WCAG 2.0 compliant
is automatically generated. In places where your selected brand
color isn’t accessible, an accessible color is used instead. If you
provide a value for `OVERRIDE_A11Y_COLOR`, your value
is used in the instances described in place of an automatically
generated color.

Overriding the accessible brand color only updates the first tile
in your brand-based color palette, which affects colors like links
and buttons. Overriding the accessibility brand color can make
text harder to read.

Must be a valid hex color string in the format #54C254.

Available only for SLDS 1 themes.

**Field Type**
boolean

**Description**
Indicates whether your provided brand logo displays while a
Lighting Experience page loads or refreshes ( `true` ) or not
( `false` ). The default value is `false` .

**Field Type**
string

**Description**
The color used for page backgrounds. Must be a valid hex color
string in the format #54C254.

Available only for SLDS 1 themes.

**Field Type**
string

**Description**
The default banner image for user profiles. Use a JPG, PNG, or
GIF that's 1800x360 pixels and smaller than 5 MB. Users can
[change their profile banner image. Must refer to an asset file](https://help.salesforce.com/s/articleView?id=experience.admin_files_asset_files.htm&type=5&language=en_US)
that already exists within the org.

**Field Type**
string


Metadata Types BrandingSet

**Property** **Description**

**Description**
The default avatar image for user profiles. Use a JPG, PNG, or
GIF that's 200x200 pixels and smaller than 5 MB. Users can
[change their profile avatar image. Must refer to an asset file](https://help.salesforce.com/s/articleView?id=experience.admin_files_asset_files.htm&type=5&language=en_US)
that already exists within the org.

Declarative Metadata Sample Definition

The following is an example of a BrandingSet component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <BrandingSet xmlns="http://soap.sforce.com/2006/04/metadata">

      <brandingSetProperty>

        <propertyName>TextTransformStyle</propertyName>

        <propertyValue>uppercase</propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>DetailTextColor</propertyName>

        <propertyValue>#696969</propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>BorderColor</propertyName>

        <propertyValue>#D4D4D4</propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>HeaderImage</propertyName>

        <propertyValue></propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>HeaderFonts</propertyName>

        <propertyValue>Montserrat</propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>CardBackgroundColor</propertyName>

        <propertyValue>rgba(255, 255, 255, 0)</propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>LoginBackgroundColor</propertyName>

        <propertyValue>#F4F4F4</propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>ActionColor</propertyName>

        <propertyValue>#2574A9</propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>_ActionColorTrans</propertyName>

        <propertyValue>rgba(25, 124, 190, 0.9)</propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>CompanyLogo</propertyName>

```


Metadata Types BrandingSet

```
        <propertyValue></propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>LoginBackgroundImage</propertyName>

        <propertyValue>../../../../sfsites/picasso/core/external/

           salesforceIdentity/images/background.jpg?v=1</propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>_LinkColorDarker</propertyName>

        <propertyValue>#135F90</propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>_ActionColorDarker</propertyName>

        <propertyValue>#135F90</propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>_HoverColor</propertyName>

        <propertyValue>rgba(25, 124, 190, 0.1)</propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>ErrorFontColor</propertyName>

        <propertyValue>#ff9e9e</propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>TextColor</propertyName>

        <propertyValue>#333</propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>OverlayTextColor</propertyName>

        <propertyValue>#FFFFFF</propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>PrimaryFont</propertyName>

        <propertyValue>Lato</propertyValue>

      </brandingSetProperty>

      <brandingSetProperty>

        <propertyName>LinkColor</propertyName>

        <propertyValue>#2574A9</propertyValue>

      </brandingSetProperty>

      <masterLabel>ex</masterLabel>

      <type>napili:branding-napili-merged</type>

   </BrandingSet>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>MyBrandingSet</members>

        <name>BrandingSet</name>

      </types>

      <version>40.0</version>

   </Package>

```


### Metadata Types BriefcaseDefinition

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### BriefcaseDefinition

Represents a briefcase definition. A briefcase makes selected records available for specific users and groups to view when they’re offline
in the Salesforce Field Service mobile app for iOS and Android. This type extends the Metadata metadata type and inherits its `fullName`
field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### BriefcaseDefinition components have the suffix .briefcaseDefinition and are stored in the briefcaseDefinitions

folder.

Version

### BriefcaseDefinition components are available in API version 50.0 and later.

Fields

**Field Name** **Field Type** **Description**

`briefcaseRules` BriefcaseRule[] A list of rules that specify which records are included in the briefcase.

`description` string Description of the briefcase.

`isActive` boolean

Required. Indicates whether the briefcase is active by default ( `true` ) or
inactive ( `false` ). Activate a briefcase to make the selected records
available to assignees.

`masterLabel` string Required. Label for the briefcase name that appears in the Salesforce
user interface.

`type` BriefcaseType Applies if multiple briefcase types are available in your org. Enum values
include:

**•** `Standard` : Standard briefcase that can be used with priming APIs.

**•** `HighVolume` : Increased capacity briefcase that’s used with
performance priming in the Salesforce Field Service mobile app.

**•** `MobileAppSync` : Automatically generated briefcase that’s used
for performance priming in the Salesforce Field Service mobile app.


Metadata Types BriefcaseDefinition

BriefcaseRule

Represents a rule that specifies records to be included in the BriefcaseDefinition.

**Field Name** **Field Type** **Description**

`briefcaseRuleFilters` BriefcaseRuleFilter[] A list of filters on a rule.

`filterLogic` string The filter logic for record selection, for example, `1 AND 2` where 1 and 2
correspond to filter 1 and filter 2. Filter logic operators include `AND` and `OR` .

`isAscendingOrder` boolean Indicates whether the records should be sorted in ascending order ( `true` ) or
descending order ( `false` ).

`isRelatedFilesRule` boolean

Indicates whether the briefcase rule is part of a hierarchical set of rules that
configure the offline priming of file attachments. Available only for the Offline
App (Salesforce Mobile App Plus).

To configure the offline priming of file attachments, create a set of four
hierarchical briefcase rules:

**•** A rule with `targetEntity` set to the object with the file attachments
at the first level

**•** A rule with `targetEntity` set to `ContentDocumentLink` at the
second level

**•** A rule with `targetEntity` set to `ContentDocument` at the third
level

**•** A rule with `targetEntity` set to `ContentVersion` at the fourth
level

See the Declarative Metadata Sample Definition section for an example briefcase
definition that configures the offline priming of file attachments.

The `ContentDocumentLink`, `ContentDocument`, and
`ContentVersion` rules must all have `isRelatedFilesRule` set to
`true` . To delete a briefcase configuration for file attachments, you must delete
the `ContentDocumentLink` rule and all of its nested rules. You can’t
delete a single rule within the hierarchy of `ContentDocumentLink`,
`ContentDocument`, and `ContentVersion` rules.

When `isRelatedFilesRule` is set to true, you must use the
`recordLimit` field to limit the number of file attachments returned by a
briefcase rule. Apply the same `recordLimit` value across the
`ContentDocumentLink`, `ContentDocument`, and
`ContentVersion` rules. You can optionally filter file attachments by file
size and file type through Briefcase Builder in Setup.

After you set a value for `isRelatedFilesRule`, you can no longer modify
the field. The value that you set persists for the life of the rule.

`orderBy` string The field to order the records by, which determines how the records can be
sorted. For example, Account Name or Created By.


Metadata Types BriefcaseDefinition

**Field Name** **Field Type** **Description**

```
queryScope

```

`FilterScope` A group of records to restrict the scope of this rule. Valid values include:
(enumeration of type

**•** `Everything`

string)

**•** `Everything`

**•** `AssignedToMe`

**•** `Mine`

The `AssignedToMe` scope is supported for the ServiceAppointment object
only.

`recordLimit` int The maximum number of records for an object on the briefcase rule. The
maximum is 50,000 records that meet the criteria. However, the records returned

by one briefcase rule must fit within the maximum limit of 50,000 records
across active briefcases. If there are more records that match the criteria than
the record limit allows, the `orderBy` field determines which records are
returned.

`relatedRules` BriefcaseRule[] A list of rules that are related to the current rule.

`relationshipField` string Required for `relatedRules` . Defines the Salesforce object field that relates
the `relatedRules` field to another `relatedRules` field or the

`briefcaseRules` field on the BriefcaseDefinition metadata type that it's
nested in. For example, an Account object rule can be related to a Contact
object rule using the Account ID object field. In this example, the value for the
related rule's `relationshipField` is `AccountID` .

```
relationshipType

```

`BriefcaseRuleRelationshipType` Required for `relatedRules` . Defines the relationship between the
(enumeration of type `relatedRules` field and another `relatedRules` field or the
string) `briefcaseRules` field on the BriefcaseDefinition metadata type that it's

nested in. Valid values include:

**•** `ParentToChild`

**•** `ChildToParent`

`targetEntity` string

BriefcaseRuleFilter

Specifies filter criteria for a BriefcaseRule.

Required. The API name of the standard object, custom object, or custom
metadata type that the briefcase rule selects records from.

If the `targetEntity` is a custom metadata type, the briefcase rule can’t
include any other fields. You can add only one briefcase rule for the same

custom metadata type in a briefcase. Custom metadata types are supported
as the `targetEntity` for top-level rules only–you can’t create a related
rule with `targetEntity` as a custom metadata type.


Metadata Types BriefcaseDefinition

**Field Name** **Field Type** **Description**

```
filterOperator

```

```
BriefcaseFilterOperator
```

(enumeration of type
string)

Required. The comparison operator for this rule filter. Capitalization matters
with date filter operators. Be sure to specify date literals in uppercase. Some
valid date literals include TODAY, YESTERDAY and TOMORROW.

Valid values include:

**•** `d` —Ends with

**•** `e` —Equals

**•** `g` —Greater than

**•** `h` —Greater than or equal

**•** `l` —Less than

**•** `m` —Less than or equal

**•** `n` —Not equals. This value is applicable only when `filterValue` is
empty.

**•** `s` —Starts with

`filterSeqNumber` int Required. The filter number. When you apply multiple filters, the filters are
numbered sequentially, 1, 2, 3, and so on.

`filterValue` string

The value that the field and criteria evaluate. For example, `true` or `false`
for a boolean field whose criteria or filter operator is Equals.

Be sure to specify date literals in uppercase. Some valid date literals include
TODAY, YESTERDAY and TOMORROW.

For `targetEntityField` values that accept a user ID, such as `OwnerId`
or `CreatedById`, enter `$User.Id` to pass the ID of the user making the
request.

To evaluate `targetEntityField` by whether the field is empty or not
empty, leave `filterValue` blank and set `filterOperator` to `e`
(equals) or `n` (not equals).

`targetEntityField` string Required. The API name of the field to filter by. This field is from the
`targetEntity` on BriefcaseRule. Compound fields aren't supported. Fields

encrypted with deterministic encryption can be used in filters with equals and
not equals operators.

Declarative Metadata Sample Definition

The following is an example of a BriefcaseDefinition component for account records.

The following is an example definition of a briefcase definition. If you include a rule filter, you must include a filter logic.

```
<?xml version="1.0" encoding="UTF-8"?>

<BriefcaseDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

   <briefcaseRules>

     <briefcaseRuleFilters>

       <filterOperator>g</filterOperator>

       <filterSeqNumber>1</filterSeqNumber>

```


Metadata Types BriefcaseDefinition

```
          <filterValue>50000.00</filterValue>

          <targetEntityField>AnnualRevenue</targetEntityField>

        </briefcaseRuleFilters>

        <briefcaseRuleFilters>

           <filterOperator>l</filterOperator>

           <filterSeqNumber>2</filterSeqNumber>

           <filterValue>50</filterValue>

           <targetEntityField>NumberOfEmployees</targetEntityField>

        </briefcaseRuleFilters>

        <filterLogic>1 AND 2</filterLogic>

        <isAscendingOrder>false</isAscendingOrder>

        <orderBy>NumberOfEmployees</orderBy>

        <queryScope>Everything</queryScope>

        <recordLimit>1000</recordLimit>

        <targetEntity>Account</targetEntity>

      </briefcaseRules>

      <description>Account Briefcase</description>

      <isActive>true</isActive>

      <masterLabel>Account With Standard Fields</masterLabel>

   </BriefcaseDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>AccountWithCustomFields</members>

        <name>BriefcaseDefinition</name>

      </types>

      <version>49.0</version>

   </Package>

```

This example briefcase definition configures the offline priming of file attachments for the WorkOrder object. Files Priming is available
only for the Offline App (Salesforce Mobile App Plus).

```
   <?xml version="1.0" encoding="UTF-8"?>

   <BriefcaseDefinition xmlns="http://soap.sforce.com/2006/04/metadata"

   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

     <briefcaseRules>

        <isAscendingOrder>false</isAscendingOrder>

        <orderBy>SystemModstamp</orderBy>

        <queryScope>Everything</queryScope>

        <recordLimit>25</recordLimit>

        <targetEntity>WorkOrder</targetEntity>

        <relatedRules>

          <targetEntity>ContentDocumentLink</targetEntity>

          <relationshipField>LinkedEntityId</relationshipField>

          <relationshipType>ParentToChild</relationshipType>

          <isAscendingOrder>false</isAscendingOrder>

          <isRelatedFilesRule>true</isRelatedFilesRule>

          <queryScope>Everything</queryScope>

          <recordLimit>2</recordLimit>

          <relatedRules>

            <targetEntity>ContentDocument</targetEntity>

            <relationshipField>ContentDocumentId</relationshipField>

```


### Metadata Types BusinessProcessGroup

```
            <relationshipType>ChildToParent</relationshipType>

            <isAscendingOrder>false</isAscendingOrder>

            <isRelatedFilesRule>true</isRelatedFilesRule>

            <queryScope>Everything</queryScope>

            <recordLimit>2</recordLimit>

            <relatedRules>

               <targetEntity>ContentVersion</targetEntity>

               <relationshipField>ContentDocumentId</relationshipField>

               <relationshipType>ParentToChild</relationshipType>

               <isAscendingOrder>false</isAscendingOrder>

               <isRelatedFilesRule>true</isRelatedFilesRule>

               <queryScope>Everything</queryScope>

               <recordLimit>2</recordLimit>

            </relatedRules>

          </relatedRules>

        </relatedRules>

     </briefcaseRules>

     <description xsi:nil="true"/>

     <isActive>true</isActive>

     <masterLabel>WorkOrder with Related Files</masterLabel>

   </BriefcaseDefinition>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

Usage

Briefcase objects are available in orgs that have Briefcase Builder and Field Service enabled.

### BusinessProcessGroup

Represents the surveys used to track customers’ experiences across different stages in their lifecycle. This type extends the Metadata
metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### BusinessProcessGroup components have the suffix .businessProcessGroup and are stored in the businessProcessGroups

folder.

Version

### BusinessProcessGroup components are available in API version 49.0 and later.


Metadata Types BusinessProcessGroup

Special Access Rules

This metadata type is available in orgs with Surveys enabled with the Customer Lifecycle Designer license.

Fields

**Field Name** **Field Type** **Description**

`businessProcessDefinitions` BusinessProcessDefinition A list that defines stages in a customer lifecycle map.
on page 556[]

`customerSatisfactionMetric` SurveyQuestionType(enumeration
of type string)

Required. Types of questions that can be associated with stages in a
customer lifecycle map.

Valid values are:

**•** `Attachment`

**•** `Boolean`

**•** `CSAT`

**•** `Currency`

**•** `Date`

**•** `DateTime`

**•** `FreeText`

**•** `Image`

**•** `NPS`

**•** `Matrix`

**•** `MultiChoice`

**•** `MultiSelectPicklist`

**•** `NPS`

**•** `Number`

**•** `Picklist`

**•** `Rating`

**•** `ShortText`

**•** `Slider`

**•** `StackRank`

**•** `Toggle`

`description` string A description of the customer lifecycle map.

`masterLabel` string Required. The name of the customer lifecycle map.


Metadata Types BusinessProcessGroup

BusinessProcessDefinition

**Field Name** **Field Type** **Description**

`businessProcessFeedbacks` BusinessProcessFeedback A list of stages in a customer lifecycle map.
on page 556[]

`description` string A description of a stage in the customer lifecycle map.

`developerName` string

Required. The API name of a stage in the customer lifecycle map.

Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

`masterLabel` string Required. The name of a stage in the customer lifecycle map.

`sequenceNumber` int Required. The position of a stage in the customer lifecycle map.

BusinessProcessFeedback

**Field Name** **Field Type** **Description**

`actionName` string Required. The name of the survey used to collect feedback

`actionParam` string Required. The name of the survey question used to collect feedback.

`actionType` ExpFeedbackCo **l** Type(enumeration Required. The mode of feedback collection. Valid values are:
of type string)

**•** `PHONE_CALL`

**•** `SURVEY`

Declarative Metadata Sample Definition

The following is an example of a BusinessProcessGroup component.

```
<?xml version="1.0" encoding="UTF-8"?>

<BusinessProcessGroup xmlns="http://soap.sforce.com/2006/04/metadata">

   <businessProcessDefinitions>

     <developerName>Customer_Onboarding</developerName>

     <masterLabel>Customer Onboarding</masterLabel>

     <description>A stage in a customer's lifecycle.</description>

     <sequenceNumber>0</sequenceNumber>

     <businessProcessFeedbacks>

        <actionType>Survey</actionType>

        <actionName>New Customer CSAT</actionName>

        <actionParam>How would you rate our service?</actionParam>

     </businessProcessFeedbacks>

   </businessProcessDefinitions>

   <customerSatisfactionMetric>NPS</customerSatisfactionMetric>

   <masterLabel>Customer Lifecycle</masterLabel>

   <description>This map tracks the feedback provided by customers' at different stages

```


### Metadata Types CallCenter

```
   during their lifecycle.</description>

   </BusinessProcessGroup>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>policyholder</members>

        <name>BusinessProcessGroup</name>

      </types>

      <version>49.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### CallCenter

Represents the Call Center definition used to integrate Salesforce with a third-party computer-telephony integration (CTI) system, a
partner telephony system, or partner Contact Center as a Service (CCaaS) system.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### CallCenter components have the suffix .callCenter and are stored in the callCenters folder.

Version

### CallCenter components are available in API version 27.0 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Description**

```
adapterUrl

```

**Field Type**
string


Metadata Types CallCenter

**Field Name** **Description**

**Description**
Optional field. A URL that points to an adapter.

```
contactCenterChannels

displayName

displayNameLabel

internalNameLabel

sections

version

```

**Field Type**

ContactCenterChannel[]

**Description**
Relates Bring Your Own Channel for Contact Center as a Service (CCaaS) messaging
channels to a CallCenter and represents the routing details for a voicemail configuration.

**Field Type**
string

**Description**

Required.

The display name of this call center.

**Field Type**
string

**Description**

Required.

The label of the `displayName` field in Call Center setup page.

**Field Type**
string

**Description**

Required.

The label of the `internalName` field in Call Center setup page.

**Field Type**

CallCenterSection[]

**Description**
Custom setup items defined for this call center.

**Field Type**
string

**Description**
The version of this call center.


Metadata Types CallCenter

CallCenterSection

**Field Name** **Description**

```
items

label

name

```

CallCenterItem

**Field Type**

CallCenterItem[]

**Description**
Contains the label, name, and value that describe the sections.

**Field Type**
string

**Description**

Required.

The label of the section.

**Field Type**
string

**Description**

Required.

The name of the section.

**Field Name** **Description**

```
label

name

value

```

**Field Type**
string

**Description**

Required.

The label of the custom setup item.

**Field Type**
string

**Description**

Required.

The name of the custom setup item.

**Field Type**
string

**Description**

Required.


Metadata Types CallCenter

**Field Name** **Description**

The value of the custom setup item.

ContactCenterChannel

Represents a junction subtype that relates a Bring Your Own Channel for Contact Center as a Service (CCaaS) messaging channel to a
CallCenter type for Bring Your Own Channel for CCaaS. This subtype also represents the routing details for a voicemail configuration and
routing information for callback requests. This subtype is available in API version 56.0 and later.

**Field Name** **Description**

```
channel

contactCenter

omniCallbackFallbackQueue

omniCallbackHandler

```

**Field Type**
string

**Description**

Required.

For Bring Your Own Channel for CCaaS, this field represents the unique ID of the Bring
Your Own Channel messaging channel (MessagingChannel) that’s associated with the
contact center (CallCenterId). Available in API version 60.0 and later.

**Field Type**
string

**Description**

Required.

For Bring Your Own Channel for CCaaS, this field represents the unique ID of the contact
center (CallCenterId) that’s associated with the Bring Your Own Channel messaging
channel (MessagingChannel). Available in API version 60.0 and later.

**Field Type**
string

**Description**
If callbacks are configured for the contact center and the contact center uses
Omni-Channel Unified Routing, this field represents the unique ID of the fallback queue
to use if contact request routing through an Omni-Channel flow fails. Don't change
the value in this field. Instead, configure contact request routing in Lightning Experience.
Available in API version 65.0 and later.

**Field Type**
string

**Description**
If callbacks are configured for the contact center and the contact center uses
Omni-Channel Unified Routing, this field represents the unique ID of the flow or queue
used to route contact requests. Don't change the value in this field. Instead, configure
contact request routing in Lightning Experience. Available in API version 65.0 and later.


Metadata Types CallCenter

**Field Name** **Description**

```
voiceMailFallbackQueue

voiceMailHandler

```

**Field Type**
string

**Description**
If voicemail routing is configured for the contact center, this field represents the unique
ID of the fallback queue to use if voicemail routing fails. Don't change the value in this
field. Instead, configure voicemail routing in Lightning Experience.

**Field Type**
string

**Description**
If voicemail routing is configured for the contact center, this field represents the unique
ID of the flow used to route voicemails. Don't change the value in this field. Instead,
configure voicemail routing in Lightning Experience.

Declarative Metadata Sample Definition

The following is an example of a CallCenter component:

```
<?xml version="1.0" encoding="UTF-8"?>

<CallCenter xmlns="http://soap.sforce.com/2006/04/metadata">

   <adapterUrl>http://localhost:11000</adapterUrl>

   <displayName>Demo Call Center Adapter</displayName>

   <displayNameLabel>Display Name</displayNameLabel>

   <internalNameLabel>Internal Name</internalNameLabel>

   <sections>

     <items>

        <label>Description</label>

        <name>reqDescription</name>

        <value>Demo Call Center Adapter</value>

     </items>

     <items>

        <label>CTI Connector ProgId</label>

        <name>reqProgId</name>

        <value>DemoAdapter.DemoAdapter.1</value>

     </items>

     <items>

        <label>Version</label>

        <name>reqVersion</name>

        <value>3.0</value>

     </items>

     <items>

        <label>CTI Adapter URL</label>

        <name>reqAdapterUrl</name>

        <value>http://localhost:11000</value>

     </items>

     <label>General Information</label>

     <name>reqGeneralInfo</name>

   </sections>

```


### Metadata Types CallCenterRoutingMap

```
      <sections>

        <items>

           <label>Outside Prefix</label>

           <name>reqOutsidePrefix</name>

           <value>1</value>

        </items>

        <items>

           <label>Long Distance Prefix</label>

           <name>reqLongDistPrefix</name>

           <value>1</value>

        </items>

        <items>

           <label>International Prefix</label>

           <name>reqInternationalPrefix</name>

           <value>01</value>

        </items>

        <label>Dialing Options</label>

        <name>reqDialingOptions</name>

      </sections>

      <version>4</version>

   </CallCenter>

```

[For information about the CallCenter definition file, see Call Center Definition Files.](https://developer.salesforce.com/docs/atlas.en-us.210.0.api_cti.meta/api_cti/sforce_api_cti_call_def_file.htm)

### CallCenterRoutingMap

Represents the mapping between a user or queue in a Salesforce org to a user or queue in an external system’s call center.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### CallCenterRoutingMap components have the suffix .callCenterRoutingMap and are stored in the

`callCenterRoutingMaps` folder.

Version

### CallCenterRoutingMap components are available in API version 52.0 and later.

Special Access Rules

This type requires Contact Center Admin, Contact Center Admin (Partner Telephony), Contact Center Supervisor, or Manage Call Centers
permission.


Metadata Types CallCenterRoutingMap

Fields

**Field Name** **Description**

```
callCenter

developerName

externalId

masterLabel

quickConnect

referenceRecord

```

**Field Type**
string

**Description**

Required.

Reference to a call center.

**Field Type**
string

**Description**

Required.

The developer name is a combination of the Salesforce user ID or queue name, and
the `callCenter` value, with an underscore between these two values.

**•** `[SALESFORCE_USER_ID]_[CALL_CENTER]`

**•** `[SALESFORCE_QUEUE_NAME]_[CALL_CENTER]`

**Field Type**
string

**Description**

Required.

Unique identifier for the external system’s user or queue.

**Field Type**
string

**Description**

Required.

The master label of the CallCenterRoutingMap.

**Field Type**
string

**Description**
The Amazon Connect QuickConnectId ARN used to determine agent availability for
Omni-Channel call transfers. Available in API version 56.0 and later.

**Field Type**
string

**Description**

Required.


### Metadata Types CallCoachingMediaProvider

**Field Name** **Description**

Lookup field to a Salesforce user or queue.

Declarative Metadata Sample Definition

The following is an example of a CallCenterRoutingMap component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CallCenterRoutingMap xmlns="http://soap.sforce.com/2006/04/metadata">

      <callCenter>ExampleCallCenter</callCenter>

   <developerName>User_001ABC00000FjYIIA0_04vZ6000000Cagl</developerName>

   <externalId>arn:aws:connect:ap-northeast-1:484907484500:instance/examplestring-9c18-4aa5-b5fe-cda6f34d99a0/agent/a69f7afe-5b04-4aa8-b5ee-108a84d0f504</externalId>

      <masterLabel>001ABC00000FjYIIA0</masterLabel>

      <referenceRecord>example.d2b87b8182fa@salesforce.com</referenceRecord>

   </CallCenterRoutingMap>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>User_001ABC00000FjYIIA0_04vZ6000000Cagl</members>

        <name>CallCenterRoutingMap</name>

      </types>

      <version>64.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### CallCoachingMediaProvider

Represents the CallCoachingMediaProvider configuration. Use CallCoachingMediaProvider to configure which providers of voice recordings
that Einstein Conversation Insights can use. For example, Sales Dialer can provide voice recordings. Einstein Conversation Insights then
stores and analyzes call recordings to surface insights and trends in customer conversations.This type extends the Metadata metadata
type and inherits its `fullName` field.

File Suffix and Directory Location

### CallCoachingMediaProvider components have the suffix .callCoachingMediaProvider and are stored in the CallCoachingMediaProvider folder.

Version

### CallCoachingMediaProvider components are available in API version 49.0 and later.


### Metadata Types CampaignInfluenceModel

Special Access Rules

You must be a Sales Engagement customer to access this metadata type.

Fields

**Field Name** **Field Type** **Description**

`isActive` boolean

Indicates whether the media provider can upload voice recordings ( `true` ) or
not ( `false` ).

Default value is `false` .

`providerDescription` string Description of the media provider.

`providerName` string Name of the media provider.

Declarative Metadata Sample Definition

The following is an example of a CallCoachingMediaProvider component.

```
<?xml version="1.0" encoding="UTF-8"?>

<CallCoachingMediaProvider xmlns="http://soap.sforce.com/2006/04/metadata">

   <isActive>true</isActive>

   <providerDescription>Salesforce telephony provider</providerDescription>

   <providerName>Dialer</providerName>

</CallCoachingMediaProvider>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>*</members>

     <name>CallCoachingMediaProvider</name>

   </types>

   <version>49.0</version>

</Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### CampaignInfluenceModel

Represents a campaign influence model used by Customizable Campaign Influence. You can’t configure Customizable Campaign
Influence via the Metadata API, but you can add a campaign influence model.

This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types CampaignInfluenceModel

[Note: This information applies only to Customizable Campaign Influence and not to Campaign Influence 1.0 .](https://help.salesforce.com/s/articleView?id=sf.campaigns_influence_original.htm&language=en_US)

File Suffix and Directory Location

CampaignInfluenceModel values are stored in the `campaignInfluenceModels` directory of the corresponding package directory.
The file name matches the model name, and the extension is `.campaignInfluenceModel` .

Version

CampaignInfluenceModel components are available in API version 38.0 and later.

Fields

**Field Name** **Field Type** **Description**

`isActive` boolean Indicates whether the model is active. Active models can generate
campaign influence records. Deactivating a model deletes its campaign

influence records. Custom models are always active and this field is
ignored. This field is available beginning with API version 40.0.

`isDefaultModel` boolean Required. Indicates if the model is the default model or not. Only
campaign influence records associated with the default model appear

on campaigns and opportunities. You can only have one default model
at a time. A model must be active to become the default model.

Activating or deactivating custom models does not automatically
generate or delete campaign influence records.

`isModelLocked` boolean Required. Indicates if the model is locked or not. Campaign Influence
records for locked models can be manipulated only via the API.

`modelDescription` string A description of the influence model.

`name` string Required. A unique name for the model.

`recordPreference` picklist The value of this field determines when to create campaign influence
records.

**•** `AllRecords` : Creates records regardless of the revenue attribution
percentage.

**•** `RecordsWithAttribution` : Creates records only when the
revenue attribution is greater than 0%.

This field is available In API version 41.0 and later.

Declarative Metadata Sample Definition

The following is an example of a CampaignInfluenceModel component that represents the default Salesforce campaign influence
attribution model. The default `isDefaultModel` value of `true` can be changed if another model is created and set as the default


### Metadata Types CaseSubjectParticle

model. The `isModelLocked` value of `true` means that Campaign Influence records for this model can be seen in the UI, but not
created, updated, or deleted.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CampaignInfluenceModel xmlns="http://soap.sforce.com/2006/04/metadata">

      <isActive>true</isActive>

      <isDefaultModel>true</isDefaultModel>

     <isModelLocked>true</isModelLocked> <recordPreference>AllRecords</recordPreference>

      <modelDescription>Primary Campaign gets 100% of the revenue share</modelDescription>

      <name>Salesforce Model</name>

   </CampaignInfluenceModel>

```

The following is an example of a CampaignInfluenceModel component that creates an influence model called Last Touch, which will
not be the default model.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CampaignInfluenceModel xmlns="http://soap.sforce.com/2006/04/metadata">

      <isActive>true</isActive>

      <isDefaultModel>false</isDefaultModel>

      <isModelLocked>true</isModelLocked>

      <modelDescription>This model gives 100% influence attribution to the last campaign

   that touched the contact.</modelDescription>

      <name>Last Touch</name>

      <recordPreference>RecordsWithAttribution</recordPreference>

   </CampaignInfluenceModel>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### CaseSubjectParticle

Represents the Social Business Rules custom format for the **Case Subject** field on cases created from inbound social posts.

File Suffix and Directory Location

### CaseSubjectParticle components have the suffix .CaseSubjectParticle and are stored in the CaseSubjectParticles

folder.

Version

### CaseSubjectParticle is available in API version 41.0 and later.


Metadata Types CaseSubjectParticle

Fields

**Field Name** **Field Type** **Description**

`index` int Required. The order in which the custom **Case Subject** is
generated, meaning if the social network is 0 and the social

message is 1, then the subject generates as `Twitter |`
`Tweet` .

`textField` string Specifies inbound social content added to **Case Subject** in
case records.

Required. Specifies the custom **Case Subject** format from
which inbound social content appears in case records. Valid
values are:

**•** `ProvidedString`

**•** `Source`

**•** `MessageType`

**•** `SocialHandle`

**•** `SocialNetwork`

**•** `Sentiment`

**•** `RealName`

**•** `Content`

**•** `PipeSeparator`

**•** `ColonSeparator`

**•** `HyphenSeparator`

```
type

```

CaseSubjectParticleType
(enumeration of type
string)

Declarative Metadata Sample Definition

This is a sample of a `.CaseSubjectParticle` file.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns=http://soap.sforce.com/2006/04/metadata"">

   <types>

     <members>*</members>

     <name>CaseSubjectParticle</name>

   </types>

   <version>41.0</version>

</Package>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types CareBenefitVerifySettings CareBenefitVerifySettings

Represents the configuration settings for benefit verification requests.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

### CareBenefitVerifySettings components have the suffix .careBenefitVerifySettings and are stored in the

`careBenefitVerifySettings` folder.

Version

### CareBenefitVerifySettings components are available in API version 52.0 and later.

Fields

**Field Name** **Description**

```
codeSetType

defaultNpi

generalPlanServiceTypeCode

isDefault

```

**Field Type**
string

**Description**
Specifies the code set type for the benefits verification service type codes.

**Field Type**
string

**Description**
Default National Provider Identifier to be used in the benefits verification request.

**Field Type**
string

**Description**
Service type code for the plan benefits as a whole.

**Field Type**
boolean

**Description**
Indicates whether this record is the default verification service `(true)` or not
`(false)` .


Metadata Types CareBenefitVerifySettings

**Field Name** **Description**

```
masterLabel

organizationName

serviceApexClass

serviceNamedCredential

serviceTypeSourceSystem

uriPath

```

**Field Type**
string

**Description**

Required.

Name of the benefits verification service.

**Field Type**
string

**Description**
Specifies the organization name for the benefits verification request service.

**Field Type**
string

**Description**
Apex class used to access the benefits verification service.

**Field Type**
string

**Description**
Credential used to access the benefits verification service.

**Field Type**
string

**Description**
Service type code for the plan benefits as a whole.

**Field Type**
string

**Description**
Link to payer endpoint.

Declarative Metadata Sample Definition

This is an example of a CareBenefitVerifySettings component.

```
<?xml version="1.0" encoding="UTF-8"?>

<CareBenefitVerifySettings xmlns="http://soap.sforce.com/2006/04/metadata">

   <generalPlanServiceTypeCode>abc</generalPlanServiceTypeCode>

   <isDefault>true</isDefault>

   <masterLabel>test</masterLabel>

   <serviceApexClass>TestApexClass</serviceApexClass>

   <serviceNamedCredential>test</serviceNamedCredential>

   <uriPath>efgh</uriPath>

```


### Metadata Types CareLimitType

```
      <serviceTypeSourceSystem>Lorem ipsum dolor</serviceTypeSourceSystem>

      <codeSetType>Code set</codeSetType>

      <defaultNpi>Npi info</defaultNpi>

      <organizationName>Organization name</organizationName>

   </CareBenefitVerifySettings>

```

This is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>CareBenefitVerifySettings</name>

      </types>

      <types>

        <members>*</members>

        <name>ApexClass</name>

      </types>

      <types>

        <members>*</members>

        <name>NamedCredential</name>

      </types>

      <version>52.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### CareLimitType

Defines the characteristics of limits on benefit provision.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

### CareLimitType components have the suffix .careLimitType and are stored in the careLimitTypes folder.

Version

### CareLimitType components are available in API version 52.0 and later.


Metadata Types CareLimitType

Fields

**Field Name** **Description**

```
isProtected

limitType

masterLabel

metricType

```

**Field Type**
boolean

**Description**
An auto-generated value that doesn’t impact the behavior of the metadata type.

**Field Type**
string

**Description**
Source of limit on benefit provision, such as a co-insurance requirement.

**Field Type**
string

**Description**

Required.

Name of the limit type.

**Field Type**
CareLimitTypeMetricType (enumeration of type string)

**Description**
Metric to be used for calculating and displaying the benefit limit, such as number of
visits, amount spent, or percentage of allowed expenditure.

Valid values are:

**•** `Amount`

**•** `Money`

**•** `Percentage`

**•** `Text`

Declarative Metadata Sample Definition

This is an example of a CareLimitType component.

```
<?xml version="1.0" encoding="UTF-8"?>

<CareLimitType xmlns="http://soap.sforce.com/2006/04/metadata">

   <limitType>test</limitType>

   <masterLabel>test</masterLabel>

   <metricType>Money</metricType>

   <isProtected>false</isProtected>

</CareLimitType>

```


### Metadata Types CareSystemFieldMapping

This is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>CareLimitType</name>

      </types>

      <version>52.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### CareSystemFieldMapping

Represents a mapping from source system fields to Salesforce objects and fields. This type extends the Metadata metadata type and
inherits its `fullName` field.

[other]: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### CareSystemFieldMapping components have the suffix .careSystemFieldMapping and are stored in the

`careSystemFieldMappings` folder.

Version

### CareSystemFieldMapping components are available in API version 49.0 and later.

Special Access Rules

To use this metadata type, your Salesforce org must have the Health Cloud or Life Sciences Cloud license and the user must have the
Health Cloud Foundation (for Health Cloud) or Health Cloud Starter (for Life Sciences Cloud) permission set.

Fields

**Field Name** **Field Type** **Description**

`externalIdField` string The ID of the field in the external system.

`isActive` boolean Indicates whether this field mapping is active ( `true` ) or not ( `false` ).
The default value is False.


Metadata Types CareSystemFieldMapping

**Field Name** **Field Type** **Description**

`isProtected` boolean An auto-generated value that doesn’t currently impact the behavior of
the metadata type.

`masterLabel` string Required. The name of the care system field mapping.

```
role

```

SourceSystemFieldRole Required. The role the field represents. Valid values are:
(enumeration of

**•** `Patient` —When the `role` field is set to `Patient`, the

type string)

Enrollment API uses the value of `externalIdField` as the
patient ID. This role can be used when `targetObject` is set to
`Account` .

**•** `RemoteMonitoringDevice` —Indicates which
`externalIdField` on the Asset object maps to the `Device`
field in the CareObservation object. This role can be used when
targetObject is set to Asset.

**•** `RemoteMonitoringPatient` —Indicates which
`externalIdField` on the Account object maps to the
`ObservedSubject` field in the Care Observation object. This
role is used when targetObject is set to Account.

**•** `ServiceProvider` —The Enrollment API uses the value of
`externalIdField` as the provider ID. This role is used when
`targetObject` is set to `Account` .

**•** `NotApplicable` —This role is used when `targetObject` is
set to `CareProgram` or `Product`, which means that there is
no applicable role.

`sourceSystem` string The system where the record originated.

`targetObject` string The name of the Salesforce object to which the external system field is
mapped.

Declarative Metadata Sample Definition

The following is an example of a CareSystemFieldMapping component.

```
<?xml version="1.0" encoding="UTF-8"?>

<CareSystemFieldMapping xmlns="http://soap.sforce.com/2006/04/metadata">

   <externalIdField>AccountNumber</externalIdField>

   <isActive>true</isActive>

   <isProtected>false</isProtected>

   <masterLabel>Map1</masterLabel>

   <role>Patient</role>

   <sourceSystem>Epic</sourceSystem>

   <targetObject>Account</targetObject>

</CareSystemFieldMapping>

```


### Metadata Types CareProviderSearchConfig

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>patient</members>

        <name>CareSystemFieldMapping</name>

      </types>

      <version>49.0</version>

   </Package>

### CareProviderSearchConfig

```

Represents the information about the fields that appear in care provider search results. This type extends the Metadata metadata type
and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### CareProviderSearchConfig components have the suffix .careProviderSearchConfig and are stored in the

`careProviderSearchConfigs` folder.

Version

### CareProviderSearchConfig components are available in API version 48.0 and later.

Fields

**Field Name** **Field Type** **Description**

`isActive` boolean Indicates whether this configuration is active ( `true` ) or not ( `false` ).

`isProtected` boolean An auto-generated value that doesn’t currently impact the behavior of
the metadata type.

Required. Indicates mapped objects.

Possible values are;

**•** HealthCarePractitionerFacility

**•** HealthCareProvider

```
mappedObject

```

ProviderSearch
ObjectMapping
(enumeration of
type string)

`masterLabel` string Required. Name of the care provider.

`sourceField` string API name of the field that is copied to the target object.

`targetField` string API name of the field to copy the data to.


### Metadata Types CareRequestConfiguration

Declarative Metadata Sample Definition

The following is an example of a CareProviderSearchConfig component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CareProviderSearchConfig xmlns="http://soap.sforce.com/2006/04/metadata">

      <sourceField>Test1__c</sourceField>

      <targetField>Test1__c</targetField>

      <mappedObject>HealthcareProvider</mappedObject>

      <isProtected>false</isProtected>

      <isActive>true</isActive>

      <masterLabel>testlabel</masterLabel>

   </CareProviderSearchConfig>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>HealthcareProvider.Test1__c</members>

        <name>CustomField</name>

      </types>

      <types>

        <members>CareProviderSearchableField.Test1__c</members>

        <name>CustomField</name>

      </types>

      <types>

        <members>Test</members>

        <name>CareProviderSearchConfig</name>

      </types>

      <version>48.0</version>

   </Package>

### CareRequestConfiguration

```

Represents the details for a record type such as service request, drug request, or admission request. One or more record types can be
associated with a care request.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

### CareRequestConfiguration components have the suffix .careRequestConfiguration and are stored in the

`careRequestConfigurations` folder.


Metadata Types CareRequestConfiguration

Version

CareRequestConfiguration components are available in API version 44.0 and later.

Fields

**Field Name** **Description**

```
careRequestRecordType

careRequestRecords

careRequestType

isActive

```

**Field Type**
string

**Description**

Required.

The record type for the care request.

**Field Type**

CareRequestRecords[]

**Description**
The list of objects you can select to configure the care request.

**Field Type**
string

**Description**

Required.

The type of care request. For example, an appeal, a service request, or an admission.

**Field Type**
boolean

**Description**
Indicates whether the care request is active ( `true` ) or not ( `false` ).

**Field Type**
boolean

**Description**
Indicates whether the record type of the care request is default ( `true` ) or not ( `false` ).

**Field Type**
string

**Description**

Required.

A user-friendly name for CareRequestConfiguration, which is defined when the
CareRequestConfiguration is created.


Metadata Types CareRequestConfiguration

CareRequestRecords

Displays a list of objects to customize the care request.

**Field Name** **Description**

```
careRequestRecord

```

**Field Type**
string

**Description**

Required.

The object selected to configure the care request.

Declarative Metadata Sample Definition

This is an example of a CareRequestConfiguration component.

```
<?xml version="1.0" encoding="UTF-8"?>

<CareRequestConfiguration xmlns="http://soap.sforce.com/2006/04/metadata">

   <careRequestRecordType>DrugRequest</careRequestRecordType>

   <careRequestRecords>

     <careRequestRecord>CareRequestItem</careRequestRecord>

   </careRequestRecords>

   <careRequestRecords>

     <careRequestRecord>CareRequestDrug</careRequestRecord>

   </careRequestRecords>

   <careRequestType>Drug Request</careRequestType>

   <isActive>false</isActive>

   <isDefaultRecordType>false</isDefaultRecordType>

   <masterLabel>DrugRequest</masterLabel>

</CareRequestConfiguration>

```

This is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>Case.DrugRequest</members>

     <name>BusinessProcess</name>

   </types>

   <types>

     <members>*</members>

     <name>CareRequestConfiguration</name>

   </types>

   <types>

     <members>CareRequest.DrugRequest</members>

     <members>CareRequestDrug.DrugRequest</members>

     <members>CareRequestItem.DrugRequest</members>

     <members>Case.DrugRequest</members>

     <name>RecordType</name>

   </types>

```


### Metadata Types CatalogedApi

```
      <version>44.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### CatalogedApi

Represents an API brought into API Catalog for Salesforce from an external source.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### CatalogedApi components have the suffix .catalogedApi and are stored in the catalogedApis folder.

Version

### CatalogedApi components are available in API version 65.0 and later.

Fields

**Field Name** **Field Type** **Description**

`description` string The description defined when the API is cataloged.

`descriptor` string The content of the API schema in JSON format.

`externalSourceIdentifier` string The ID of the API in the external source that it's imported from.

### instances CatalogedApiInstance[] Reference to the cataloged API that this instance is specific to.

`label` string
Required. The API name as it appears in API Catalog.

Required. Indicates the source of the API specification registered with
API Catalog.

API Catalog supports the value `Anypoint` for deployment and
supports other values for enumeration. See information about the values
[in the registrationProviderType field.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_externalserviceregistration.htm)

Required. Specifies the API type. If not specified, the API type is derived
based on the descriptor content. Nillable.


```
providerType

type

```

ExternalServiceRegistrationProviderType
(enumeration of
type string)

APIType
(enumeration of
type string)

Metadata Types CatalogedApi

**Field Name** **Field Type** **Description**

Values are:

**•** `GraphQL`

**•** `gRPC`

**•** `REST`

CatalogedApiInstance

Represents a MuleSoft API instance brought into API Catalog for Salesforce from Anypoint Platform.

**Field Name** **Field Type** **Description**

```
accessStatus

```

APIInstanceAccessStatus
Required. The access status for the API instance.
(enumeration of

Values are:

type string)

**•** `Approved`

**•** `Deleted`

**•** `NoStatus`

**•** `NotAccessible`

**•** `Pending`

**•** `Rejected`

**•** `Revoked`

`apiInstanceDescriptor` string The content of the API schema in JSON format.

```
approvalType

endpointType

```

AP **I** nstanceApprovalType
Required. The approval type for access in Anypoint Platform.
(enumeration of

Values are:

type string)

**•** `AutoApproval`

**•** `ManualApproval`

**•** `NoApproval`

AP **I** nstanceEndpointType
(enumeration of
type string)

The endpoint type to invoke the instance. Available in API version 66.0
and later.

Values are:

**•** `Callout`

**•** `Discovery`

`label` string
Required. The instance name as it appears in API Catalog.

`serviceRegistration` string

Required. The service registration in external services related to this API
instance.


### Metadata Types CatalogedApiArtifactVersionInfo

**Field Name** **Field Type** **Description**

`uri` string
Required. The uniform resource identifier (URI) for the instance.

Declarative Metadata Sample Definition

This XML is an example of a CatalogedApi component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CatalogedApi xmlns="http://soap.sforce.com/2006/04/metadata">

   <externalSourceIdentifier>urn:ms:03ff2c74-d0ea-4eba-a536-36dfd2d0fdbb:api-project::petstore-engineering</externalSourceIdentifier>

      <instances>

        <accessStatus>NoStatus</accessStatus>

   <apiInstanceDescriptor>{&quot;@type&quot;:&quot;anypointAPIInstanceDescriptor&quot;,&quot;environmentType&quot;:&quot;SANDBOX&quot;,&quot;environmentName&quot;:&quot;Sandbox&quot;,&quot;environmentId&quot;:&quot;79305d19-1d89-413f-88ec-d7a8dbd1e29d&quot;,&quot;instanceId&quot;:&quot;4051358&quot;,&quot;authenticationMethod&quot;:&quot;NO_AUTH&quot;,&quot;componentType&quot;:&quot;apiInstance&quot;,&quot;instanceOrigin&quot;:&quot;MANUAL&quot;}</apiInstanceDescriptor>

        <approvalType>NoApproval</approvalType>

        <label>petstore-engineering</label>

        <serviceRegistration>PetstoreEngineeringv109C60C7C</serviceRegistration>

        <uri>https://google.com</uri>

      </instances>

      <label>petstore-engineering</label>

      <providerType>Anypoint</providerType>

      <type>REST</type>

   </CatalogedApi>

### CatalogedApiArtifactVersionInfo

```

Represents API version information in API Catalog that’s referenced by other entities.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### CatalogedApiArtifactVersionInfo components have the suffix .catalogedApiArtifactVersionInfo and are stored in the

`catalogedApiArtifactVersionInfos` folder.

Version

### CatalogedApiArtifactVersionInfo components are available in API version 65.0 and later.


### Metadata Types CatalogedApiVersion

Fields

**Field Name** **Field Type** **Description**

`releaseNotes` string The API release notes.

`revision` int The API revision.

`type` string Required. The API type.

`version` string Required. The API version.

Declarative Metadata Sample Definition

This XML is an example of a CatalogedApiArtifactVersionInfo component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CatalogedApiArtifactVersionInfo xmlns="http://soap.sforce.com/2006/04/metadata">

      <revision>1</revision>

      <type>API</type>

      <version>v1</version>

   </CatalogedApiArtifactVersionInfo>

### CatalogedApiVersion

```

Represents a version of an API that is consumable in Salesforce using API Catalog.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### CatalogedApiVersion components have the suffix .catalogedApiVersion and are stored in the catalogedApiVersions

folder.

Version

### CatalogedApiVersion components are available in API version 65.0 and later.


### Metadata Types Certificate

Special Access Rules

Fields

**Field Name** **Field Type** **Description**

`catalogedApi` string Required. An API managed for consumption in Salesforce using API
Catalog.

`description` string The description defined when the API is cataloged.

`externalSourceIdentifier` string The ID of the API in the external source that it's imported from.

`label` string
Required. The API name as it appears in API Catalog.

`version` string Required. The ID of the API version information.

Declarative Metadata Sample Definition

This XML is an example of a CatalogedApiVersion component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CatalogedApiVersion xmlns="http://soap.sforce.com/2006/04/metadata">

      <catalogedApi>PetstoreEngineeringv109C60C7C</catalogedApi>

   <externalSourceIdentifier>urn:ms:03ff2c74-d0ea-4eba-a536-36dfd2d0fdbb:api-project::petstore-engineering/v1</externalSourceIdentifier>

      <label>petstore-engineering</label>

      <version>v1lwWZmDFyJYIFValk</version>

   </CatalogedApiVersion>

### Certificate

```

Represents a certificate used for digital signatures that verify that requests are coming from your org. Certificates are used for either
authenticated single sign-on with an external website, or when using your org as an identity provider. This type extends the Metadata
With Content metadata type and inherits its `content` and `fullName` fields.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### Certificate components have the suffix .crt and are stored in the certs folder.

Version

### Certificate components are available in API version 36.0 and later.


Metadata Types Certificate

Fields

**Field Name** **Field Type** **Description**

`caSigned` boolean Required. Indicates whether this certificate is signed by the issuer (true)
or not (false).

`encryptedWithPlatformEncryption` boolean Indicates whether this certificate is encrypted with Platform Encryption.

`expirationDate` dateTime The date that this certificate expires and is no longer usable. For
self-signed certificates, if `keySize` is 2048 bits, the expiration date is

automatically 1 year after you create the certificate. If `keySize` is 4096
bits, the expiration date is automatically 2 years after you create the
certificate. For CA-signed certificates, `expirationDate` is
automatically updated to the signed certificate’s expiration date when
a signed certificate chain is uploaded. The date format is YYYY-MM-DD.

`keySize` int Certificate keys can be either 2048 bits or 4096 bits. A certificate with
4096-bit keys lasts 2 years, and a certificate with 2048-bit keys lasts 1

year. Certificates with 2048-bit keys are faster than certificates with
4096-bit keys. If `keySize` isn’t specified when you create a certificate,
the key size defaults to 2048 bits.

`masterLabel` string

`privateKeyExportable` boolean

Usage

Required. A user-friendly name for the certificate that appears in the
Salesforce user interface, such as in Certificate and Key Management.
Limit: 64 characters.

Indicates whether this certificate’s private key is exportable. If
`privateKeyExportable` isn’t specified when you create a
certificate, its default value is `true` .

The Metadata API can be used to create a self-signed or a CA-signed certificate. The .crt file’s contents are the certificate chain, which
can be updated when you renew or update the intermediate certificate chain of a CA-signed certificate. After creating a CA-signed
[certificate, the .crt file contains a certificate signing request (CSR). For details, see About Salesforce Certificates and Keys in Salesforce](https://help.salesforce.com/apex/HTViewHelpDoc?id=security_keys_about.htm&language=en_US)
Help.

To copy an existing certificate’s X.509 parameter data to a new certificate, upload the existing certificate. You can also use this procedure
to renew a certificate. A new private+public key pair is created with a new certificate. Salesforce doesn’t allow the import or export of
the private key via the API.

Using the Metadata API, you can download a CSR. After it’s CA-signed, you can upload it back to Salesforce.

After the signed certificate chain is uploaded via the Metadata API, the CSR of that certificate can’t be downloaded via the API anymore.
The content of the `.crt` file is the signed certificate chain. However, the CSR can still be downloaded via the UI.

**•** Downloading a CSR—The CSR is downloadable after a CA-signed cert is created. If a signed certificate hasn’t been uploaded to that
certificate, the content of the downloaded .crt file is the CSR.

**•** Uploading a CA-Signed Certificate—To upload the signed certificate chain back to Salesforce, save the signed certificate chain as
the content of the .crt file and update it via the Metadata API.


### Metadata Types ChatterExtension

Declarative Metadata Sample Definition

The following is an example of a Certificate component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Certificate xmlns="http://soap.sforce.com/2006/04/metadata">

      <caSigned>true</caSigned>

      <encryptedWithPlatformEncryption>true</encryptedWithPlatformEncryption>

      <expirationDate>2017-03-19</expirationDate>

      <keySize>4096</keySize>

      <masterLabel>My Certificate Name</masterLabel>

      <privateKeyExportable>true</privateKeyExportable>

   </Certificate>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### ChatterExtension

Represents the metadata used to describe a Rich Publisher App that’s integrated with the Chatter publisher.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Retrieving ChatterExtension

Using an API tool, you can get extension information from `package.xml` using this code.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

    <types>

     <members>xw1</members>

     <name>ChatterExtension</name>

    </types>

    <version>41.0</version>

   </Package>

```

Use the `<members>` tag to name a specific extension (in this example, _`xw1`_ ), or use the wildcard (*) symbol to retrieve all your
extensions.

Here’s an example of retrieved information.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ChatterExtension xmlns="http://soap.sforce.com/2006/04/metadata">

     <compositionComponent>xwComp</compositionComponent>

     <description>des</description>

     <extensionName>xw1</extensionName>

     <headerText>h1</headerText>

     <hoverText>h2</hoverText>

     <icon>tiger</icon>

```


Metadata Types ChatterExtension

```
     <masterLabel>primary</masterLabel>

     <renderComponent>xwRend</renderComponent>

     <type>Lightning</type>

   </ChatterExtension>

```

Version

ChatterExtension is a new feature in API version 41.0.

Fields

**Field** **Field Type** **Description**

`compositionComponent` string Required. The composition component of the Rich Publisher
App that you provide. It’s comprised of the

```
                              lightning:availableForChatterExtensionComposer
```

interface.

`description` string Required. The description of your custom Rich Publisher App.

`extensionName` string Required. The name of your extension. That is, your Rich
Publisher App.

`headerText` string

`hoverText` string

The text to show in the header of your app composer. Header
text is required for Lightning type extensions. This text can be
localized.

The text to show when a user mouses over your extension’s
icon. Mouse-over text is required for Lightning type extensions.
This text can be localized.

`icon` string Required. The icon to show in the Chatter publisher. Use an
existing file asset id from your org.

`isProtected` boolean An auto-generated value. It currently has no impact.

`masterLabel` string Required. Label for the ChatterExtension object.

`renderComponent` string Required. The rendering component of the Rich Publisher App
that you provide. It’s comprised of the

```
                           lightning:availableForChatterExtensionRenderer
```

interface.

`type` ChatterExtensionType
(enumeration of type string)


Required. Describes the type of the extension. Currently, the
only value supported is _`Lightning`_ . Included to allow for
other possible types in the future.

### Metadata Types ChoiceList

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

[Integrate Your Custom Apps into the Chatter Publisher](https://developer.salesforce.com/docs/atlas.en-us.262.0.lightning.meta/lightning/components_integrate_customapps_to_publisher.htm)

### ChoiceList

Represents the `Choicelist` dropdown field that’s used for pre-chat.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ChoiceList components have the suffix .ChoiceList and are stored in the ChoiceList folder.

Version

### ChoiceList components are available in API version 62 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Description**

```
choiceListValue

description

```

**Field Type**
### ChoiceListValue[]

**Description**
A list of choices to display in the choice list.

**Field Type**
string

**Description**
A description of the choice list.


Metadata Types ChoiceList

**Field Name** **Description**

```
masterLabel

```

ChoiceListValue

**Field Type**
string

**Description**

Required. The label for the choice list.

Represents a choice list value in the pre-chat dropdown. ChoiceListValue is available in API version 62 or later.

**Field Name** **Description**

```
embeddedServiceCustomLabels

isDefaultValue

order

valueName

```

**Field Type**

EmbeddedServiceCustomLabel[] on page 1012

**Description**
Custom labels for the choicelist value.

**Field Type**
boolean

**Description**

Required. Indicates whether the choicelist value should be selected by default.

**Field Type**
int

**Description**

Required. The order of the choicelist value in the choicelist dropdown field.

**Field Type**
string

**Description**

Required. The value of the choicelist.

Declarative Metadata Sample Definition

The following is an example of a Choicelist component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ChoiceList xmlns="http://soap.sforce.com/2006/04/metadata">

   <choiceListValue>

     <embeddedServiceCustomLabels>

<customLabel>EM_PreChat_ChoiceList_PrechatCustomFieldLabel_133xx0000004GG1_7741637</customLabel>

```


### Metadata Types ClaimFinancialSettings

```
           <labelKey>EM_PreChat_ChoiceList_PrechatCustomFieldLabel</labelKey>

           <feature>EmbeddedMessaging</feature>

        </embeddedServiceCustomLabels>

        <isDefaultValue>true</isDefaultValue>

        <order>0</order>

        <valueName>Pizza</valueName>

      </choiceListValue>

      <choiceListValue>

        <embeddedServiceCustomLabels>

   <customLabel>EM_PreChat_ChoiceList_PrechatCustomFieldLabel_133xx0000004GG2_5523047</customLabel>

           <labelKey>EM_PreChat_ChoiceList_PrechatCustomFieldLabel</labelKey>

           <feature>EmbeddedMessaging</feature>

        </embeddedServiceCustomLabels>

        <isDefaultValue>false</isDefaultValue>

        <order>1</order>

        <valueName>Burger</valueName>

      </choiceListValue>

      <masterLabel>Food</masterLabel>

      <description>Food Choice List</description>

   </ChoiceList>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ChoiceList</name>

      </types>

      <version>62.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### ClaimFinancialSettings

Represents the configuration settings for Insurance Claim Financial Services.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types ClaimFinancialSettings

File Suffix and Directory Location

ClaimFinancialSettings components have the suffix `claimFinancialSettings` and are stored in the
`ClaimFinancialSettings` folder.

Version

ClaimFinancialSettings components are available in API version 57.0 and later.

Special Access Rules

To access this metadata type, you require access to either InsurancePolicyAdminAccess or InsuranceClaimMgmtAccess add-on license.

Fields

**Field Name** **Description**

```
claimCovPendingAuthStatus

claimPendingAuthorityStatus

clmCovPymtDtlPendAuthSts

masterLabel

```

**Field Type**
string

**Description**

Required.

The status of pending financial authority for claim coverage.

**Field Type**
string

**Description**

Required.

The status of pending financial authority for claim.

**Field Type**
string

**Description**

Required.

The status of pending financial authority for claim coverage payment detail.

**Field Type**
string

**Description**

Required.

The unique label that identifies the claim financial settings throughout the Salesforce
user interface.


### Metadata Types ClauseCatgConfiguration

Declarative Metadata Sample Definition

The following is an example of a ClaimFinancialSettings component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ClaimFinancialSettings xmlns="http://soap.sforce.com/2006/04/metadata">

      <claimCovPendingAuthStatus>Pending Authority</claimCovPendingAuthStatus>

      <claimPendingAuthorityStatus>Pending Authority</claimPendingAuthorityStatus>

      <clmCovPymtDtlPendAuthSts>Pending Authority</clmCovPymtDtlPendAuthSts>

      <masterLabel>Claim Financial Settings</masterLabel>

   </ClaimFinancialSettings>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?><!-
     ~ Copyright 2022 salesforce.com, inc.

     ~ All Rights Reserved

     ~ Company Confidential

     -->

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ClaimFinancialSettings</name>

      </types>

      <version>57.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### ClauseCatgConfiguration

Represents the configuration about the clause category that can be used to categorize your disclosure and compliance reports from
standardized disclosure templates in a response document.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

### ClauseCatgConfiguration components have the suffix .clauseCatgConfiguration and are stored in the

`clauseCatgConfigurations` folder.

Version

### ClauseCatgConfiguration components are available in API version 57.0 and later.


Metadata Types ClauseCatgConfiguration

Special Access Rules

The ClauseManagementAddOn license is required to access this object along with user access for the Clause Designer User permission
set license.

Fields

**Field Name** **Description**

```
description

isProtected

masterLabel

usageType

```

**Field Type**
string

**Description**
The description about the clause category configuration.

**Field Type**
boolean

**Description**
An auto-generated value that doesn’t impact the behavior of the metadata type. The
default is `false` .

**Field Type**
string

**Description**

Required.

A user-friendly name for ClauseCatgConfiguration, which is defined when the
ClauseCatgConfiguration is created.

**Field Type**
ClmCategoryUsageType

**Description**

Required.

The usage type of the clause category configuration.

Possible values are:

**•** `ContractClauseCategory`

**•** `DisclosureCategory`

Declarative Metadata Sample Definition

The following is an example of a ClauseCatgConfiguration component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ClauseCatgConfiguration

```


### Metadata Types CleanDataService

```
    xmlns="http://soap.sforce.com/2006/04/metadata">

    <description>This is to add description for Contract Clause Category.</description>

    <usageType>ContractClauseCategory</usageType>

    <isProtected>false</isProtected>

    <masterLabel>Contract Clause Cat</masterLabel>

   </ClauseCatgConfiguration>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package

    xmlns="http://soap.sforce.com/2006/04/metadata">

    <fullName>Pkg</fullName>

    <types>

     <name>ClauseCatgConfiguration</name>

    </types>

    <version>57.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### CleanDataService

Represents a data service that adds and updates data in standard objects.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### CleanDataService components have the .cleanDataService suffix and are stored in the cleanDataServices directory.

The name of the component file is based on the name of the object associated with the data service. For example, the component file
name `cleanDataServices/DataCloudCompanyMatch.cleanDataService` describes a data service component
called DataCloudCompanyMatch that's associated with the company name in account objects.

Version

### CleanDataService components are available in API version 66.0 and later.

Fields

**Field Name** **Field Type** **Description**

`cleanRules` CleanRule[] Required. A list of data integration rules


Metadata Types CleanDataService

**Field Name** **Field Type** **Description**

`description` string Required. A description of the data service

`masterLabel` string Required. Label for this data service. Although this value is displayed, it’s
an internal label for the data service and isn’t translated.

`matchEngine` string Required. A key that maps to the internal data service identifier.

CleanRule

Represents information that controls how the data service adds and updates data in an org.

**Field Name** **Field Type** **Description**

`bulkEnabled` boolean Required. If this field is set to `true`, Salesforce applies the data integration
rule to existing records whenever the rule is updated or saved.

`bypassTriggers` boolean Required. If this field is set to `true`, Salesforce bypasses triggers when it applies
the rule; otherwise, it applies triggers after it applies the rule.

`bypassWorkflow` boolean

Required. If this field is set to `true`, Salesforce bypasses workflow rules when
it applies the data integration rule; otherwise, it applies workflow rules after it
applies the rule.

`description` string Required. User-friendly text that describes the data integration rule.

`developerName` string Required. This name can contain only underscores and alphanumeric characters,
and must be unique in your org. It must begin with a letter, not include spaces,

not end with an underscore, and not contain two consecutive underscores.
This unique name prevents conflicts with rules from other packages that have
the same `masterLabel` .

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

`fieldMappings` FieldMapping[] Required. A list of FieldMapping entries for the rule.

`masterLabel` string Required. Label for this object. This display value is the internal label that is not
translated.

`matchRule` string Required. An internal label for a matching rule in the data service that’s
associated with the CleanRule.

`sourceSobjectType` string Required. A virtual object in the data service that is associated with the
CleanRule. Specifying a non-existent object causes an error.

`status` string Required. Status of the data integration rule. Valid values are `Active` and
`Inactive` .

`targetSobjectType` string

Required. A standard object that’s the target of additions and updates specified
by this CleanRule. Specifying an object that the data service does not support
causes an error.


Metadata Types CleanDataService

FieldMapping

Represents a mapping between fields in the data service and fields in an object in the org.

**Field Name** **Field Type** **Description**

`developerName` string Required. This name can contain only underscores and alphanumeric characters,
and must be unique in your org. It must begin with a letter, not include spaces,

not end with an underscore, and not contain two consecutive underscores.
This unique name prevents conflicts with field mappings from other packages
that have the same `masterLabel` .

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

`fieldMappingRows` FieldMappingRow[] Required. A list of FieldMappingRow entries. Each entry represents a field in a
standard object that maps to a field in the data service.

`masterLabel` string Required. Label for this object. This display value is the internal label that is not
translated.

`SObjectType` string Required. The standard object associated with this FieldMapping. Specifying
an object that the data service does not support causes an error.

FieldMappingRow

Represents the status of a CleanRule.

**Field Name** **Field Type** **Description**

`fieldName` string The display name for the field represented by the FieldMappingRow.

`fieldMappingFields` FieldMappingField[] Required. A list of FieldMappingField entries. Each entry is a field in a standard
object that maps to a field in the data service.

`mappingOperation` string The comparison operation the data service applies when it compares the value
of this FieldMappingRow to the mapped field in the object specified in

SObjectType. The value of this field is `AutoFill`, which indicates that the
data service only adds data if the object field is blank.

`SObjectType` string The standard object for the field mapped to the FieldMappingRow. Specifying
an object that the data service does not support causes an error.

FieldMappingField

Represents a field in a standard object. A FieldMappingField maps to a FieldMappingRow entry in a data service.

**Field Name** **Field Type** **Description**

`dataServiceField` string Required. A field in the data service that is mapped to this field.


Metadata Types CleanDataService

**Field Name** **Field Type** **Description**

`dataServiceObjectName` string

Required. An object in the data service that contains the FieldMappingRow
associated with this FieldMappingField. Specifying a non-existent object causes
an error.

`priority` int Required. Represents the priority that the data service uses when it updates
the field, relative to other update rules for the same field. Valid values are 1-100.

Declarative Metadata Sample Definition

The following is an example of a CleanDataService component for the lead standard object.

```
<?xml version="1.0" encoding="UTF-8"?>

<CleanDataService xmlns="http://soap.sforce.com/2006/04/metadata">

   <cleanRules>

     <bulkEnabled>false</bulkEnabled>

     <bypassTriggers>false</bypassTriggers>

     <bypassWorkflow>false</bypassWorkflow>

     <description>Adds data info to leads</description>

     <developerName>DataService_Leads_Enrichment</developerName>

     <fieldMappings>

        <SObjectType>DataServiceCompanyObject</SObjectType>

        <developerName>DataService_Leads_Enrichment_InputMapping</developerName>

        <fieldMappingRows>

          <SObjectType>DataServiceCompanyObject</SObjectType>

          <fieldMappingFields>

            <dataServiceField>Email</dataServiceField>

            <dataServiceObjectName>Lead</dataServiceObjectName>

            <priority>1</priority>

          </fieldMappingFields>

          <fieldName>Email</fieldName>

          <mappingOperation>Autofill</mappingOperation>

        </fieldMappingRows>

        <fieldMappingRows>

          <SObjectType>DataServiceCompanyObject</SObjectType>

          <fieldMappingFields>

            <dataServiceField>Company</dataServiceField>

            <dataServiceObjectName>Lead</dataServiceObjectName>

            <priority>1</priority>

          </fieldMappingFields>

          <fieldName>Name</fieldName>

          <mappingOperation>Autofill</mappingOperation>

        </fieldMappingRows>

        <masterLabel>DataServiceInputMapping</masterLabel>

     </fieldMappings>

     <fieldMappings>

        <SObjectType>Lead</SObjectType>

        <developerName>DataService_Leads_Enrichment_OutputMapping</developerName>

        <fieldMappingRows>

          <SObjectType>Lead</SObjectType>

          <fieldMappingFields>

            <dataServiceField>EmployeesTotal</dataServiceField>

```


Metadata Types CleanDataService

```
              <dataServiceObjectName>DataServiceCompanyObject</dataServiceObjectName>

               <priority>1</priority>

             </fieldMappingFields>

             <fieldName>NumberOfEmployees</fieldName>

             <mappingOperation>Autofill</mappingOperation>

           </fieldMappingRows>

           <fieldMappingRows>

             <SObjectType>Lead</SObjectType>

             <fieldMappingFields>

               <dataServiceField>Revenue</dataServiceField>

              <dataServiceObjectName>DataServiceCompanyObject</dataServiceObjectName>

               <priority>1</priority>

             </fieldMappingFields>

             <fieldName>AnnualRevenue</fieldName>

             <mappingOperation>Autofill</mappingOperation>

           </fieldMappingRows>

           <fieldMappingRows>

             <SObjectType>Lead</SObjectType>

             <fieldMappingFields>

               <dataServiceField>Industry</dataServiceField>

              <dataServiceObjectName>DataServiceCompanyObject</dataServiceObjectName>

               <priority>1</priority>

             </fieldMappingFields>

             <fieldName>Industry</fieldName>

             <mappingOperation>Autofill</mappingOperation>

           </fieldMappingRows>

           <masterLabel>DataServiceOutputMapping</masterLabel>

        </fieldMappings>

        <masterLabel>Data Service Company Info for Leads</masterLabel>

        <matchRule>DataServiceLeadAppendMatchRule</matchRule>

        <sourceSobjectType>DataServiceCompanyObject</sourceSobjectType>

        <status>Active</status>

        <targetSobjectType>Lead</targetSobjectType>

      </cleanRules>

      <description>Data Service Companies for Leads</description>

      <masterLabel>Data Service Companies for Leads</masterLabel>

      <matchEngine>LeadEnrichmentMatchEngine</matchEngine>

   </CleanDataService>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>DataService_Leads_Enrichment</members>

        <name>CleanDataService</name>

      </types>

      <version>38.0</version>

   </Package>

```


### Metadata Types CMSConnectSource

Usage

Use CleanDataService to retrieve all the metadata that describes a data enrichment service. To configure the service in a new org, deploy
the metadata you retrieved. Avoid using CRUD-Based Calls with CleanDataService.

To make small modifications to the CleanDataService component, use the Tooling API.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### CMSConnectSource

Represents the connection information for external content management systems that feed content to Experience Builder sites. This
type extends the Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Note: For use with Change Sets, CMSConnectSource is a dependent of **Network** and **Community** .

File Suffix and Directory Location

### CMSConnectSource components have the suffix .cmsConnectSource and are stored in the cmsConnectSource folder. In

that folder, separate files exist for each network (for example, _`networkname`_ `.` _`sourcedevelopername`_ `.cmsConnectSource` ).
Each file represents a CMS connection.

Version

### CMSConnectSource components are available in API version 43.0 and later.

Special Access Rules

The **CMS Connect org** permission must be enabled.

Fields

**Field Name** **Field Type** **Description**

`cmsConnectAsset` CMSConnectAsset on Represents CSS or JavaScript defined for the connection.
page 600[]

**•** 0–10 for CSS

**•** 0–10 for JavaScript

`cmsConnectLanguage` CMSConnectLanguage 0 to more. Represents language mappings defined for the connection.
on page 600[]


Metadata Types CMSConnectSource

**Field Name** **Field Type** **Description**

`cmsConnectPersonalization` CMSConnectPersonalization[] 0 or 1. Represents personalization defined for the connection. Only
on page 601 for use when `type` is `AEM` .

`cmsConnectResourceType` CMSConnectResourceType 0–5. Represents JSON definitions defined for the connection.
on page 601[]

`connectionType` CMSSourceConnectionType(enumeration Required. Type of authentication being used with outside system.
of type string) Valid values are:

**•** `Public`

**•** `Authenticated`

`cssScope` string The class name used to prefix and scope the CSS rules.

`developerName` string Required. API name of the CMSConnectSource entity.

`languageEnabled` string Required. Valid values are:

**•** `Y` to enable language mapping for connection.

**•** `N` if no language mapping is needed.

`masterLabel` string Required. Connection name

`namedCredential` string

Required when the `connectionType` is `Authenticated` .
API name of `namedCredential` . Before deploying
`namedCredential`, it must exist on the destination org.

`personalizationEnabled` string Required. Valid values are:

**•** `Y` to enable personalization mapping for connection.

**•** Otherwise `N` .

`rootPath` string Required. Root path.

`sortOrder` int Required. Defines the load order of the connection when multiple
connections defined on page. The load order begins with 1.

`status` CMSConnectionStatus(enumeration Required. Status of connection. Valid values are:
of type string)

**•** `ACTIVE`

**•** `INACTIVE`

`type` CMSConnectionSourceType(enumeration Required. The identification of the source connection system. Valid
of type string) values are:

**•** `AEM`

**•** `Drupal`

**•** `WordPress`

**•** `SDL`

**•** `Sitecore`

**•** `Other`


Metadata Types CMSConnectSource

**Field Name** **Field Type** **Description**

`websiteUrl` string Required if `connectionType` is `Public`

Note: Because there can be existing connections when a package comes in, there’s some INSERT or UPDATE logic to consider:

**•** If you find `developerName` in the destination, then update the existing collection with all details form source.

**•** `namedCredential` is handled through `developerName` . If you don’t find `namedCredential` with
`developerName`, then an error is generated.

**•** If the destination isn’t `sortOrder` from the source, then insert or update with the source `sortOrder` .

**•** If `sortOrder` from the source is already in the destination, then increase the source `sortOrder` by 1 for connections
such that the destination `sortOrder`          - `sortOrder` from the source.

CMSConnectAsset

CMSConnectAsset defines the location, types, and order of assets necessary to support the incoming content, such as JavaScript and
CSS files.

Note: Because there can be existing connections when a package comes in, there’s some INSERT or UPDATE logic to consider:

**•** If `assetPath` exists in the destination, then update the existing record, else the new `assetPath` is inserted.

**•** Always keep the `sortOrder` from the source and adjust the destination accordingly.

**Field Name** **Field Type** **Description**

`assetPath` string Relative path of the asset.

`assetType` string

When used in Apex, this value can be sent as an enum, otherwise, this field
has a type of string.

Allowed values as string

**•** `CSS`

**•** `Javascript`

Allowed values as enum

**•** `CSS`

**•** `Javascript`

`sortOrder` int Loading sequence on the page.

CMSConnectLanguage

CMSConnectLanguage components determine the presented language of the content.

**Field Name** **Field Type** **Description**

`cmsLanguage` string When a language placeholder is in the URL path, this value is used to replace
it.


Metadata Types CMSConnectSource

**Field Name** **Field Type** **Description**

`language` string

CMSConnectPersonalization

Salesforce supported language.

For information see
[https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_translations.htm](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_translations.htm)

CMSConnectPersonalization is used only with Adobe Experience Manager (AEM).

Note: Because there can be existing connections when a package comes in, there’s some INSERT or UPDATE logic to consider. If
personalization isn’t enabled in the source system, but is enabled in the destination, the destination is disabled. The record for the
connection is deleted from the table.

**Field Name** **Field Type** **Description**

`connectorPage` string The path to the JSP file that you created and installed in AEM.

`connectorPageAsset` string The path to your Javascript file. Providing this path allows you to run scripts
dynamically.

CMSConnectResourceType

CMSConnectResourceType is for use only to define JSON connections.

Note: Because there can be existing connections when a package comes in, there’s some INSERT or UPDATE logic to consider. If
you find the developer name in the destination, then update the existing record with all details from the source.

**Field Name** **Field Type** **Description**

`cmsConnectResourceDefinition` cmsConnectResourceDefinition 0–10 allowed per CMSConnectResourceType.
on page 601[]

`developerName` string API name of CMSConnectResourceType.

`masterLabel` string Content type name.

`resourceType` string The only allowed value is `JSON` .

CMSConnectResourceDefinition

cmsConnectResourceDefinition is used to define JSON connections.

Note: Because there can be existing connections when a package comes in, there’s some INSERT or UPDATE logic to consider:

**•** If you find developerName in the destination, then the existing record is updated with all details from the new source, else
the new value is inserted.

**•** If the current source is DETAIL and the destination has DETAIL with a different name, then the destination is updated to LIST
and the source is inserted as DETAIL.


Metadata Types CMSConnectSource

**Field Name** **Field Type** **Description**

`developerName` string Required. API name of CMSConnectResourceDefinition.

`masterLabel` string Required. developerName of Content Item or Content List.

`options` int

Required. Identifies whether the content from the external source is a single
item or a list.

0 for Content List

1 for Content Item

`payloadType` string Required. The only valid value is `JSON` .

`resourceIdPath` string Relative path to ID. Required for Content Item.

`resourceNamePath` string Relative path to resource name. Required for Content Item.

`resourcePath` string Required. JSON resource path.

`rootNodePath` string Only for Content List and collection. Defines the initial starting path for a
collection or list.

Declarative Metadata Sample Definition

The following is an example of a CMSConnectSource definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<CMSConnectSource xmlns="http://soap.sforce.com/2006/04/metadata">

   <cmsConnectAsset>

     <assetPath>etc/designs/capricorn/app-prefixed.min.css</assetPath>

     <assetType>CSS</assetType>

     <sortOrder>1</sortOrder>

   </cmsConnectAsset>

   <cmsConnectAsset>

     <assetPath>etc/designs/capricorn/w3data.js</assetPath>

     <assetType>Javascript</assetType>

     <sortOrder>1</sortOrder>

   </cmsConnectAsset>

   <cmsConnectLanguage>

     <cmsLanguage>en</cmsLanguage>

     <language>en_US</language>

   </cmsConnectLanguage>

   <cmsConnectLanguage>

     <cmsLanguage>fr</cmsLanguage>

     <language>fr</language>

   </cmsConnectLanguage>

   <cmsConnectPersonalization>

     <connectorPage>content/salesforceConnector.js</connectorPage>

     <connectorPageAsset>content/js/capricorn/assets.js</connectorPageAsset>

   </cmsConnectPersonalization>

   <cmsConnectResourceType>

     <cmsConnectResourceDefinition>

        <developerName>Details</developerName>

```


Metadata Types CMSConnectSource

```
           <masterLabel>Details</masterLabel>

           <options>0</options>

           <payloadType>JSON</payloadType>

           <resourceIdPath>ID</resourceIdPath>

           <resourceNamePath>title</resourceNamePath>

   <resourcePath>rest/v1.1/sites/cmstry.wordpress.com/posts/{component}</resourcePath>

        </cmsConnectResourceDefinition>

        <cmsConnectResourceDefinition>

           <developerName>List</developerName>

           <masterLabel>List</masterLabel>

           <options>1</options>

           <payloadType>JSON</payloadType>

   <resourcePath>rest/v1.1/sites/cmstry.blog.wordpress.com/posts?number={itemsPerPage}&amp;page={pageNumber}</resourcePath>

        </cmsConnectResourceDefinition>

        <developerName>Posts</developerName>

        <masterLabel>Posts</masterLabel>

        <resourceType>JSON</resourceType>

      </cmsConnectResourceType>

      <connectionType>Public</connectionType>

      <cssScope>capricorn</cssScope>

      <developerName>Capricorn</developerName>

      <languageEnabled>Y</languageEnabled>

      <masterLabel>Capricorn</masterLabel>

      <personalizationEnabled>Y</personalizationEnabled>

      <rootPath>content/capricorn/{language}</rootPath>

      <sortOrder>11</sortOrder>

      <status>ACTIVE</status>

      <type>AEM</type>

      <websiteUrl>https://public-api.wordpress.com</websiteUrl>

   </CMSConnectSource>

```

The following is an example `package.xml` .

```
   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>NetworkA.*</members>

        <name>CMSConnectSource</name>

      </types>

      <version>43.0</version>

   </Package>

```

To retrieve a specific connection:

```
   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>NetworkA. DeveloperName </members>

        <name>CMSConnectSource</name>

      </types>

      <version>43.0</version>

   </Package>

```


Metadata Types CMSConnectSource

Usage

The INSERT or UPDATE logic for the incoming information is always UPSERT. If data isn’t in the entity, then it’s inserted, otherwise the
current data is updated.

Before doing upsert, the content from the package is validated against the maximum limits for the following:

**•** CSS assets <= 10

**•** JavaScript assets <= 10

**•** Resource types < =5

**•** Resource definitions for each type <=10

For example

**1.** The validation on a new connection totals only the elements in the incoming package.

**2.** Validation of existing connections totals the existing assets and new elements to assess validity. For example, if a connection on the
destination org already has six CSS definitions, and the incoming package has defined seven CSS definitions (four new + three
existing), the new total is the six current from the database. The total ignores the three repeated in the package and adds four new
definitions from the incoming package. This totals 10 definitions, which number is at or below the 10 asset threshold, and it passes
validation.

Refer to the following content for more details for how each entity how is handled while saving the details from package to destination
org:


### Metadata Types Community (Zone)

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

[Select Components for an Outbound Change Set](https://help.salesforce.com/articleView?id=changesets_outbound_components_select.htm&type=5&language=en_US)

[View and Add Dependent Components to a Change Set](https://help.salesforce.com/articleView?id=changesets_outbound_dependencies.htm&type=5&language=en_US)

[Developer Guide: Deploying and Retrieving Metadata](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/file_based.htm)

[Salesforce Help: Use Personalized Content in CMS Connect](https://help.salesforce.com/articleView?id=communities_cms_connect_personalization.htm&type=5&language=en_US)

[Developer Guide: Translations](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_translations.htm)

### Community (Zone)

Represents a zone that contains Ideas or Chatter Answers objects. Zones are shared by the Ideas, Answers, and Chatter Answers features,
allowing you to view and create zones from those locations.This type extends the Metadata metadata type and inherits its `fullName`
field.

Note: Starting with the Summer ’13 release, Chatter Answers and Ideas “communities” have been renamed to “zones.” In API
### version 28, the API object label has changed to Zone, but the API type is still Community .

File Suffix and Directory Location

Zones have the suffix `community` and are stored in the `communities` folder.

Version

### Community (Zone) components are available in API version 27.0 and later.

Fields

Note: When `enableChatterAnswers` is set to `false`, values specified for the following fields are ignored and not saved:
`communityFeedPage`, `emailFooterDocument`, `emailHeaderDocument`, `enablePrivateQuestions`,
`emailNotificationUrl`, and `site` .


Metadata Types Community (Zone)

**Field Name** **Field Type** **Description**

`active` boolean Indicates whether the zone is active ( `true` ) or not ( `false` ).

`chatterAnswersFacebookSsoUrl` string (Read only) The Facebook sign-on URL, which is based on the Facebook
authentication provider selected in your Chatter Answers settings. This

field is available only if Chatter Answers and Facebook Single Sign-On
for Chatter Answers are enabled.

`communityFeedPage` string The Visualforce page that hosts the zone’s feeds. This field is available
when Chatter Answers is enabled in the organization.

`description` string The description of the zone.

`emailFooterDocument` string

`emailHeaderDocument` string

`emailNotificationUrl` string

`enableChatterAnswers` boolean

`enablePrivateQuestions` boolean

The text or HTML file that incorporates your organization’s branding into
the footer of email notifications. This field is available when Chatter
Answers is enabled in the organization.

The text or HTML file that incorporates your organization’s branding into
the header of email notifications. This field is available when Chatter
Answers is enabled in the organization.

The URL that’s included in email notifications. This field is available when
Chatter Answers is enabled in the organization. This field replaces
`portalEmailNotificationUrl` in API version 28.0 and later.

Indicates whether the zone has Chatter Answers enabled ( `true` ) or not
( `false` ). This field is available when Chatter Answers is enabled in the
organization.

Indicates whether Chatter Answers questions can be escalated to cases
( `true` ) or not ( `false` ). This field is available when Chatter Answers is
enabled in the organization.

`expertsGroup` string The name of the public group that act as experts in the zone. This field
is available when eitherIdeas or Answers are enabled in the organization.

`portal` string The name of the portal in which to display the zone.

`portalEmailNotificationUrl` string

The portal URL that’s included in email notifications. This field is available
when Chatter Answers is enabled in the organization. This field has been
replaced by `emailNotificationUrl` in API version 28.0 and later.

`reputationLevels` ReputationLevels The fields that define the points and name of each reputation level you
define. You can create up to 25 reputation levels per zone.

`showInPortal` boolean Indicates whether the zone is available to all portals ( `true` ) or not
available to any portals ( `false` ).

`site` string The name of the site for the zone. This field is available when Chatter
Answers is enabled in the organization.


Metadata Types Community (Zone)

ReputationLevels

Represents the points and reputation label that displays on hover over a user’s photo in the feed.

**Field Name** **Field Type** **Description**

`chatterAnswersReputationLevels` ChatterAnswersReputationLevel

[]

Contains the name and value pair that describes the
reputation level for Chatter Answers. Available in API version
28.0 and later.

`ideaReputationLevels` IdeaReputationLevel Contains the name and value pair that describes the
reputation for Ideas. Available in API version 28.0 and later.

ChatterAnswersReputationLevel

Represents the reputation name and the number of points for that level for Chatter Answers.

**Field Name** **Field Type** **Description**

`name` string The name of the reputation level, for example, “Expert.”

`value` int The minimum number of points for the reputation level.

IdeaReputationLevel

Represents the reputation name and the number of points for that level for Ideas. Available in API version 28.0 and later.

**Field Name** **Field Type** **Description**

`name` string The name of the reputation level, for example, “Expert.”

`value` int The minimum number of points for the reputation level.

Declarative Metadata Sample Definition

The following is the definition of a community (zone) component:

```
<?xml version="1.0" encoding="UTF-8"?>

<Community xmlns="http://soap.sforce.com/2006/04/metadata">

   <active>true</active>

   <communityFeedPage>communityWithHeaderAndFooter_main</communityFeedPage>

   <description>Metadata Test</description>

   <emailFooterDocument>sampleFolder/emailFooter.html</emailFooterDocument>

   <emailHeaderDocument>sampleFolder/emailHeader.html</emailHeaderDocument>

   <enableChatterAnswers>true</enableChatterAnswers>

   <enablePrivateQuestions>true</enablePrivateQuestions>

   <expertsGroup>CommunityExperts</expertsGroup>

   <portal>Customer Portal</portal>

   <emailNotificationUrl>http://yourURL</emailNotificationUrl>

<reputationLevels>

     <chatterAnswersReputationLevels>

```


### Metadata Types CommerceSettings

```
           <name>Newbie</name>

           <value>0</value>

        </chatterAnswersReputationLevels>

        <chatterAnswersReputationLevels>

           <name>Smartie</name>

           <value>500</value>

        </chatterAnswersReputationLevels>

        <chatterAnswersReputationLevels>

           <name>Pro</name>

           <value>2000</value>

        </chatterAnswersReputationLevels>

        <chatterAnswersReputationLevels>

           <name>All Star</name>

           <value>5000</value>

        </chatterAnswersReputationLevels>

        <ideaReputationLevels>

           <name>Observer</name>

           <value>0</value>

        </ideaReputationLevels>

        <ideaReputationLevels>

           <name>Contributor</name>

           <value>100</value>

        </ideaReputationLevels>

        <ideaReputationLevels>

           <name>Influencer</name>

           <value>400</value>

        </ideaReputationLevels>

        <ideaReputationLevels>

           <name>Thought Leader</name>

           <value>1500</value>

        </ideaReputationLevels>

      </reputationLevels>

      <showInPortal>true</showInPortal>

      <site>ChatterAnswersSite</site>

   </Community>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### CommerceSettings

Represents settings for various Commerce features.

Parent Type and Manifest Access

This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all the settings metadata types for the org are accessed using the “Settings” name. See Settings for more details.


Metadata Types CommerceSettings

File Suffix and Directory Location

CommerceSettings values are stored in the `Commerce.settings` file in the `settings` folder. The `.settings` files are different
from other named components, because there’s only one settings file for each settings component.

Version

Commerce Settings are available in API version 50.0 and later.

Special Access Rules

A B2B Commerce or D2C Commerce license and access to Commerce objects is required.

Fields

**Field Name** **Description**

```
buyerGroupExtensibility

commerceAnalyticsEnabled

commerceAppEnabled

commerceConciergeEnabled

commerceCopilotEcomEnabled

commerceDCSegmentEnabled

```

**Field Type**
boolean

**Description**
Indicates whether Buyer Group Extensibility is enabled ( `true` ) or not ( `false` ).
Available in API version 64.0 and later.

**Field Type**
boolean

**Description**
Indicates whether Commerce Analytics is enabled ( `true` ) or not ( `false` ).

**Field Type**
boolean

**Description**
Indicates whether Commerce App is enabled ( `true` ) or not ( `false` ).

**Field Type**
boolean

**Description**
Indicates whether Commerce Concierge bots are enabled ( `true` ) or not ( `false` ).

**Field Type**
boolean

**Description**
Indicates whether Commerce Copilot is enabled ( `true` ) or not ( `false` ).

**Field Type**
boolean


Metadata Types CommerceSettings

**Field Name** **Description**

**Description**
Indicates whether the Data 360 segment integration is enabled ( `true` ) or not ( `false` ).

```
commerceDiscoveryExpansion

commerceEnabled

commerceNGPEnabled

commerceRLMSubs

generateInvPerSubscription

lowestUnitPriceTracking

messagingEngagementDataKit

```

**Field Type**
boolean

**Description**
Indicates whether the Commerce Discovery Expansion service is enabled ( `true` ) or
not ( `false` ).

**Field Type**
boolean

**Description**
Indicates whether Commerce is enabled ( `true` ) or not ( `false` ).

**Field Type**
boolean

**Description**
Indicates whether NGP (“Salesforce”) Pricing is enabled ( `true` ) or not ( `false` ).

**Field Type**
boolean

**Description**
Indicates whether Commerce Revenue Lifecycle Management Subscriptions is enabled
( `true` ) or not ( `false` ).

**Field Type**
boolean

**Description**
Indicates whether a separate invoice is generated per subscription ( `true` ) or not
( `false` ). Available in API version 64.0 and later.

**Field Type**
boolean

**Description**
Indicates whether lowest unit price tracking (for EU customers) is enabled ( `true` ) or
not ( `false` ).

**Field Type**
boolean

**Description**
Indicates whether Message Engagement data kit is enabled ( `true` ) or not ( `false` ).
Message Engagement data kit is a Data 360 data model object (DMO) for a user’s
engagement with a marketing message.


### Metadata Types CommunityTemplateDefinition

Declarative Metadata Sample Definition

The following is an example of a CommerceSettings component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CommerceSettings xmlns="http://soap.sforce.com/2006/04/metadata">

    <buyerGroupExtensibility>false</buyerGroupExtensibility>

    <commerceAnalyticsEnabled>false</commerceAnalyticsEnabled>

    <commerceAppEnabled>false</commerceAppEnabled>

    <commerceConciergeEnabled>false</commerceConciergeEnabled>

    <commerceCopilotEcomEnabled>false</commerceCopilotEcomEnabled>

    <commerceDCSegmentEnabled>false</commerceDCSegmentEnabled>

    <commerceDiscoveryExpansion>false</commerceDiscoveryExpansion>

    <commerceEnabled>false</commerceEnabled>

    <commerceNGPEnabled>false</commerceNGPEnabled>

    <commerceRLMSubs>false</commerceRLMSubs>

    <generateInvPerSubscription>false</generateInvPerSubscription>

    <lowestUnitPriceTracking>false</lowestUnitPriceTracking>

    <messagingEngagementDataKit>false</messagingEngagementDataKit>

   </CommerceSettings>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Commerce</members>

        <name>Settings</name>

      </types>

      <version>64.0</version>

   </Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The wildcard
applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the manifest
file, see Deploying and Retrieving Metadata with the Zip File.

### CommunityTemplateDefinition

Represents the definition of an Experience Builder site template. This type extends the Metadata metadata type and inherits its `fullName`
field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### CommunityTemplateDefinition components have the suffix .communityTemplateDefinition and are stored in the

`communityTemplateDefinitions` folder.


Metadata Types CommunityTemplateDefinition

Version

CommunityTemplateDefinition components are available in API version 38.0 and later.

Special Access Rules

This type is available only if Salesforce Digital Experiences is enabled in your org.

Fields

**Field Name** **Field Type** **Description**

Denotes that this CommunityTemplateDefinition was created in API
version 41.0 or later. The only valid value is `c` . This field is available in
API 41.0 and later.

```
baseTemplate

```

CommunityBase
Template
(enumeration of
type string)

`bundlesInfo` CommunityTemplateBundleInfo[] The list of preview images and feature highlights of this
CommunityTemplateDefinition.

```
category

```

CommunityTemplate Required. The optimized use case of this CommunityTemplateDefinition.
Category Valid values are:
(enumeration of

**•** `Commerce`

type string)

**•** `Commerce`

**•** `IT`

`defaultBrandingSet` string

**•** `Marketing`

**•** `Sales`

**•** `Service`

The set of branding properties associated with this
CommunityTemplateDefinition, as defined in the Theme panel in
Experience Builder. Available in API version 40.0 and later.

In API version 44.0 and later, this field is read-only and can be
implemented in CommunityThemeDefinition on page 618.

`defaultThemeDefinition` string Required. The assigned theme definition for this
CommunityTemplateDefinition.

`description` string The optional description text of this CommunityTemplateDefinition.

`enableExtendedCleanUp` boolean False by default. Determines if deleting this
`OnDelete` CommunityTemplateDefinition attempts to delete other directly or
indirectly referenced objects automatically, for example,
CommunityThemeDefinition on page 618, Flexipage on page 1199, or
StaticResource on page 2360. Values are true or false.

`masterLabel` string Required. The label for this CommunityTemplateDefinition, which displays
in Setup.


Metadata Types CommunityTemplateDefinition

**Field Name** **Field Type** **Description**

`navigationLinkSet` NavigationLinkSet The navigation menu associated with this CommunityTemplateDefinition.
A navigation menu consists of items that users can click to go to other

parts of the site. Available in API versions 37.0 to 46.0. In API versions
47.0 and later, use NavigationMenu.

`pageSetting` CommunityTemplatePageSe **t** ing[] The list of FlexiPage of this CommunityTemplateDefinition.

`publisher` string

CommunityTemplateBundleInfo

Defines the name of the publisher as seen in the Change Theme wizard.
If no name is provided, the name of the org from which the package
was originally exported is used.

This field is available in API version 45.0 and later.

**Field Name** **Field Type** **Description**

`description` string The optional description text of its CommunityTemplateBundleInfo.

`image` string Required only when the `type` is `PreviewImage`, otherwise this field is
optional. A preview image for this CommunityTemplateDefinition.

`order` int Required. An integer specifying the position of this
CommunityTemplateBundleInfo relative to others of the same `type` within

its CommunityTemplateDefinition. `1` is the first position, `3` is the maximum
position for `PreviewImage` type, and `4` is the maximum position for the
`Highlight` type.

`title` string Required. The title of this CommunityTemplateBundleInfo to use in code.

Required. Stores descriptive information about the template that’s included in
the export. The template powers the interface of the Experience Creation
Wizard. Valid values are:

**•** `Highlight` —This CommunityTemplateBundleInfo is used as a
highlighted feature. Up to 4 are supported.

**•** `PreviewImage` —This CommunityTemplateBundleInfo is used as a
preview image. Up to 3 are supported.

```
type

```

CommunityTemplate
BundleInfoType
(enumeration of type
string)

CommunityTemplatePageSetting

**Field Name** **Field Type** **Description**

`page` string Required. The list of FlexiPage of this CommunityTemplateDefinition.

`themeLayout` string

Required. The name of the FlexiPage for the theme layout.

This field is available in API version 39.0 and later.


Metadata Types CommunityTemplateDefinition

Declarative Metadata Sample Definition

The following is an example of a CommunityTemplateDefinition component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CommunityTemplateDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

      <baseTemplate>c</baseTemplate>

      <bundlesInfo>

        <description>Feature Description</description>

        <order>1</order>

        <title>Feature Heading</title>

        <type>Highlight</type>

      </bundlesInfo>

      <bundlesInfo>

        <image>siteAsset_2dbe594eb6794173af78da264cd6a4a7</image>

        <order>1</order>

        <title>Preview Image</title>

        <type>PreviewImage</type>

      </bundlesInfo>

      <category>Sales</category>

      <defaultThemeDefinition>communityTemplate</defaultThemeDefinition>

      <description>This is an Experience Builder template</description>

      <enableExtendedCleanUpOnDelete>true</enableExtendedCleanUpOnDelete>

      <masterLabel>communityTemplate</masterLabel>

      <navigationLinkSet>

        <navigationMenuItem>

           <label>Topics</label>

           <position>0</position>

           <publiclyAvailable>true</publiclyAvailable>

           <target>ShowMoreTopics</target>

           <type>NavigationalTopic</type>

        </navigationMenuItem>

      </navigationLinkSet>

      <pageSetting>

        <page>communityTemplate_Report_List</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Topic_Catalog</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Check_Password</page>

        <themeLayout>communityTemplate_themeLayout_Login</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Error</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_User_Settings</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Login</page>

```


Metadata Types CommunityTemplateDefinition

```
        <themeLayout>communityTemplate_themeLayout_Login</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Stream_List</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Sfdc_Page</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Group_Detail</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Report_Related_List</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Register</page>

        <themeLayout>communityTemplate_themeLayout_Login</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_User_Profile</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Case_Detail</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Stream_Related_List</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Dashboard_Detail</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Group_List</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Canvasapp_Page</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Login_Error</page>

        <themeLayout>communityTemplate_themeLayout_Login</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Create_Record</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

```


Metadata Types CommunityTemplateDefinition

```
      <pageSetting>

        <page>communityTemplate_Group_Related_List</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Search</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_File_Detail</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Case_List</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_User_List</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_File_List</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Question_Detail</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Dashboard_List</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Related_Record_List</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_File_Related_List</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Record_List</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Forgot_Password</page>

        <themeLayout>communityTemplate_themeLayout_Login</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Home</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Dashboard_Related_List</page>

```


Metadata Types CommunityTemplateDefinition

```
        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Account_Management</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Case_Related_List</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_User_Related_List</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Stream_Detail</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Topic_Detail</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Messages</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Report_Detail</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Record_Detail</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Feed_Detail</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

      <pageSetting>

        <page>communityTemplate_Contact_Support</page>

        <themeLayout>communityTemplate_themeLayout_Default</themeLayout>

      </pageSetting>

   </CommunityTemplateDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>MyTemplate</members>

        <name>CommunityTemplateDefinition</name>

      </types>

      <version>66.0</version>

   </Package>

```


### Metadata Types CommunityThemeDefinition

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### CommunityThemeDefinition

Represents the definition of a theme for an Experience Builder site. This type extends the Metadata metadata type and inherits its
`fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### CommunityThemeDefinition components have the suffix .communityThemeDefinition and are stored in the

`communityThemeDefinitions` folder.

Version

### CommunityThemeDefinition components are available in API version 38.0 and later.

Special Access Rules

This type is available only if Salesforce Digital Experiences is enabled in your org.

Fields

**Field Name** **Field Type** **Description**

`bundlesInfo` CommunityThemeBundleInfo[]

If specified, at least one preview image and one highlight are required.
Up to 3 preview images and 4 highlights are supported. Available in API
version 44.0 and later

`customThemeLayoutType` CommunityCustomThemeLayoutType[] The list of custom theme layout types available to the theme layout.

`defaultBrandingSet` string

The set of branding properties associated with this
### CommunityThemeDefinition, as defined in the Theme panel in Experience

Builder. Available in API version 44.0 and later.

`description` string The optional description text of this CommunityThemeDefinition.

`enableExtendedCleanUp` boolean

```
OnDelete

```

False by default. Determines if deleting this CommunityThemeDefinition
attempts to delete other directly or indirectly referenced objects
automatically, for example, FlexiPage. Values are true or false.

`masterLabel` string Required. The label for this CommunityThemeDefinition, which displays
in Setup.


Metadata Types CommunityThemeDefinition

**Field Name** **Field Type** **Description**

`publisher` string

Defines the name of the publisher as seen in the wizard for creating
Experience Builder sites. If no name is provided, the name of the org
from which the package was originally exported is used.

This field is available in API version 45.0 and later.

`themeRouteOverride` CommunityThemeRouteOve **r** ide[] List of theme layout type overrides for flexipages (currently only for
home). Available in API version 44.0 and later.

`themeSetting` CommunityTheme Required. The list of settings for this CommunityThemeDefinition.
Setting []

CommunityThemeBundleInfo

**Field Name** **Field Type** **Description**

`description` string The optional description text of its CommunityThemeBundleInfo.

`image` string Required only when the `type` is `PreviewImage`, otherwise this field is
optional. A preview image for this CommunityThemeDefinition.

`order` int Required. An integer specifying the position of this
CommunityThemeBundleInfo relative to others of the same `type` within its

CommunityThemeDefinition. `1` is the first position, `3` is the maximum position
for `PreviewImage` type, and `4` is the maximum position for the
`Highlight` type.

`title` string Required. The title of this CommunityThemeBundleInfo to use in code.

```
type

```

CommunityTemplate Required. Stores descriptive information about the theme that is included in
BundleInfoType the export. Valid values are:
(enumeration of type

**•** `Highlight` —This CommunityThemeBundleInfo is used as a highlighted

string)

feature. Up to 4 are supported.

**•** `PreviewImage` —This CommunityThemeBundleInfo is used as a preview
image. Up to 3 are supported.

CommunityCustomThemeLayoutType

**Field Name** **Field Type** **Description**

`description` string The description of the custom theme layout type.

`label` string Required. The name of the custom theme layout type. The values `Inner`,
`Home`, and `Login` are reserved.


Metadata Types CommunityThemeDefinition

CommunityThemeRouteOverride

**Field Name** **Field Type** **Description**

`customThemeLayoutType` string

Required when `themeLayoutType` isn’t specified. Provides the custom
theme layout type associated with the theme layout. This field and
`themeLayoutType` are mutually exclusive; you can’t specify both.

`pageAttributes` string Required. Specifies the attributes of the site page for which the default theme
layout type is overridden. The only valid value is `{"PageName":"Home"}` .

`pageType` string

Required. Specifies the type of the site page for which the default theme layout
type is overridden. The only valid value is `comm__standardPage` .

```
themeLayoutType

```

CommunityTheme Required if `customThemeLayoutType` isn’t specified. Provides the default
LayoutType theme layout type associated with the theme layout. Valid values are `Inner`,
(enumeration of type `Home`, or `Login` . This field and `customThemeLayoutType` are mutually
string) exclusive; you can’t specify both.

CommunityTheme Setting

**Field Name** **Field Type** **Description**

`customThemeLayoutType` string

Required when `themeLayoutType` isn’t specified. The custom theme
layout type associated with the theme layout. This field and
`themeLayoutType` are mutually exclusive; you can’t specify both.

`themeLayout` string Required. The configuration and layout for this theme.

```
themeLayoutType

```

CommunityTheme Required when `customThemeLayoutType` isn’t specified. The default
LayoutType theme layout type associated with the theme layout. Valid values are `Inner`,
(enumeration of type `Home`, or `Login` . This field and `customThemeLayoutType` are mutually
string) exclusive; you can’t specify both.

Declarative Metadata Sample Definition

The following is an example of a CommunityThemeDefinition component.

```
<?xml version="1.0" encoding="UTF-8"?>

<CommunityThemeDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

   <bundlesInfo>

     <description>Batman Feature1 description</description>

     <order>1</order>

     <title>Batman Feature1</title>

     <type>Highlight</type>

   </bundlesInfo>

   <bundlesInfo>

     <image>siteAsset_d90e2d5ce4cf4d8899e233c051091246</image>

     <order>1</order>

     <title>siteAsset_d90e2d5ce4cf4d8899e233c051091246</title>

```


Metadata Types CommunityThemeDefinition

```
        <type>PreviewImage</type>

      </bundlesInfo>

      <defaultBrandingSet>Batman</defaultBrandingSet>

      <description>Batman theme</description>

      <enableExtendedCleanUpOnDelete>true</enableExtendedCleanUpOnDelete>

      <masterLabel>Batman</masterLabel>

      <themeRouteOverride>

        <pageAttributes>{&quot;PageName&quot;:&quot;Home&quot;}</pageAttributes>

        <pageType>comm__standardPage</pageType>

        <themeLayoutType>Home</themeLayoutType>

      </themeRouteOverride>

      <themeSetting>

        <themeLayout>Batman_themeLayout_Login</themeLayout>

        <themeLayoutType>Login</themeLayoutType>

      </themeSetting>

      <themeSetting>

        <themeLayout>Batman_themeLayout_Home</themeLayout>

        <themeLayoutType>Home</themeLayoutType>

      </themeSetting>

      <themeSetting>

        <themeLayout>Batman_themeLayout_Default</themeLayout>

        <themeLayoutType>Inner</themeLayoutType>

      </themeSetting>

   </CommunityThemeDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Batman</members>

        <name>BrandingSet</name>

      </types>

      <types>

        <members>Batman</members>

        <name>CommunityThemeDefinition</name>

      </types>

      <types>

        <members>Batman_themeLayout_Default</members>

        <members>Batman_themeLayout_Home</members>

        <members>Batman_themeLayout_Login</members>

        <name>FlexiPage</name>

      </types>

      <types>

        <members>siteAsset_d90e2d5ce4cf4d8899e233c051091246</members>

        <name>StaticResource</name>

      </types>

      <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types ConnectedApp ConnectedApp

Represents a connected app configuration. A connected app enables an external application to integrate with Salesforce using APIs and
standard protocols, such as SAML, OAuth, and OpenID Connect. Connected apps use these protocols to authenticate, authorize, and
provide single sign-on (SSO) for external apps. The external apps that are integrated with Salesforce can run on the customer success
platform, other platforms, devices, or SaaS subscriptions.

This type extends the Metadata metadata type and inherits its `fullName` field.

Important: Connected apps creation is restricted as of Spring ‘26. You can use existing connected apps during and after Spring
[‘26. However, we recommend using external client apps instead. If you must continue creating connected apps, contact Salesforce](https://help.salesforce.com/s/articleView?id=xcloud.external_client_apps.htm&language=en_US)
Support.

[See New connected apps can no longer be created in Spring ‘26 for more details.](https://help.salesforce.com/s/articleView?id=005228017&type=1&language=en_US)

File Suffix and Directory Location

### ConnectedApp components have the suffix .connectedApp and are stored in the connectedApps folder.

Version

### ConnectedApp components are available in API version 29.0 and later.

Fields

**Field Name** **Field Type** **Description**

`attributes` `canvasConfig` A custom attribute of the connected app.

AppCanvasConfig The configuration options of the connected app if it's exposed as a
canvas app.

`contactEmail` string Required. The email address that Salesforce uses to contact you or
your support team.

`contactPhone` string The phone number for Salesforce to use to contact you.

`description` string An optional description for your app.

`iconUrl` string Reserved for future use.

`infoUrl` string An optional URL for a web page with more information about your
app.

### ipRanges ConnectedAppIpRange[] Specifies the ranges of IP addresses that can access the app without

requiring the user to authenticate with the connected app.

`label` string Required. The name of the app.

`logoUrl` string An optional logo for the app. The logo appears with the app’s entry
in the list of apps and on the consent page the user sees when


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

authenticating. The URL must use HTTPS, and the logo can't be larger
than 125 pixels high or 200 pixels wide. The default logo is a cloud.

`mobileStartUrl` string Users are directed to this URL after they've authenticated when the
app is accessed from a mobile device. If you don't give a URL, the user

is sent to the app’s default start page after authentication completes.
If the connected app that you’re creating is a canvas app, then you
can leave this field blank. The Canvas App URL field contains the URL
that gets called for the connected app.

`oauthConfig` connectedAppOauthConfig Specifies how your app communicates with Salesforce.

`oauthPolicy` ConnectedAppOauthPolicy Specifies OAuth access policies associated with your connected app.
Available in API version 49.0 and later.

`permissionSetName` string

`plugin` string

Specifies the permissions required to perform different functions with
the connected app. Available in API version 46.0 and later.

You can assign multiple permission sets to the connected app, but
you must enter each permission set name on a separate line. You can’t

enter the same permission set name more than one time for each
connected app.

You can also change a permission set by replacing the current
permission set with a new permission set. Make sure that each
permission set name assigned to the connected app is unique.

You can delete individual permission sets or remove all permission
sets from a connected app by entering an empty
`permissionSetName` string on deployment of the connected
app: ( `<permissionSetName></permissionSetName>` ).

To use this field, the `isAdminApproved` field on the
ConnectedAppOauthConfig subtype must be set to `true` .

The name of a custom Apex class that extends
`Auth.ConnectedAppPlugin` to customize the behavior of the
app.

`pluginExecutionUser` string Specifies the user to run the plugin as. If the user isn’t authorized to
use the connected app, use the `authorize` method. See the

`ConnectedAppPlugin` [class in the Apex Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_namespace_Auth.htm)
Available in API version 46.0 and later.

Enter a user that is part of your org. Otherwise, the user is removed
from this field when you deploy the connected app. If you don’t want
to specify a user, you can leave this field empty.

To use this field in an org, the ConAppPluginExecuteAsUser setting
must be enabled.


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

`profileName` string[]

Specifies the profile (base-level user permissions) required to perform
different functions with the connected app. Available in API version
46.0 and later.

You can assign multiple profiles to the connected app, but you must
enter each profile name on a separate line. You can’t enter the same
profile name more than one time for each connected app.

You can also change profiles by replacing the current profiles with
new profiles. Make sure that each profile name assigned to the
connected app is unique.

You can also delete individual profiles or remove all profiles from a
connected app by entering an empty `profileName` string on
deployment of the connected app:
( `<profileName></profileName>` ).

To use this field, the `isAdminApproved` field on the
ConnectedAppOauthConfig subtype must be set to `true` .

`samlConfig` ConnectedAppSamlConfig Controls how the app uses single sign-on.

`sessionPolicy` ConnectedAppSessionPolicy Specifies a connected app’s session policies. Available in API version
49.0 and later.

`startUrl` string If the app isn’t accessed from a mobile device, users are directed to
this URL after they've authenticated. If you don't give a URL, the user

is sent to the app’s default start page after authentication completes.
Whether you give a URL or not, the start URL can be updated later by
managing the connected app. If the app is accessed from a mobile
device, see `mobileStartUrl` . If the connected app that you’re
creating is a canvas app, then you can leave this field empty. The
Canvas App URL field contains the URL that gets called for the
connected app.

ConnectedAppAttribute

Represents the field names that make up a custom attribute when using SAML with a ConnectedApp. Customize these values to a
specific service provider.

**Field Name** **Field Type** **Description**

`formula` string Required. The value of the attribute.

`key` string Required. The attribute's identifier.

ConnectedAppCanvasConfig

Represents the configuration options of the connected app if it's exposed as a canvas app.


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

`accessMethod` AccessMethod (enumeration of Required. Indicates how the canvas app initiates the OAuth
type string) authentication flow. The valid values are:

**•** `Get` —OAuth authentication is used, and the user is prompted to
allow the third-party application to access their information. When
you use this access method, the canvas app must initiate the OAuth
authentication flow.

**•** `Post` —OAuth authentication is used, but when the administrator
installs the canvas app, they implicitly allow access for users.
Therefore, the user isn’t prompted to allow the third party to access
their user information. When you use this access method, the
authentication is posted directly to the canvas app URL.

`canvasUrl` string Required. The URL of the third-party app that's exposed as a canvas
app.

`lifecycleClass` string

The name of the `Canvas.CanvasLifecycleHandler` Apex
class, if you've implemented this class for custom parameters.

Available in API version 31.0 and later.

`locations` CanvasLocationOptions Indicates where the canvas app can appear to the user. The valid values
(enumeration of type string)[] are:

**•** `Aura` —The canvas app can appear in a custom Lightning
component.

**•** `AppLauncher` —Reserved for future use.

**•** `Chatter` —The canvas app can appear in the app navigation
list on the Chatter tab in Salesforce Classic.

**•** `ChatterFeed` —The canvas app can appear as a Chatter feed
item.

**•** `MobileNav` —The canvas app can appear in a mobile card in
the Salesforce mobile app. Available in API version 31.0 and later.

**•** `None` —The canvas app can appear only in the Canvas App
Previewer.

**•** `OpenCTI` —The canvas app can appear in the call control tool
in Salesforce Classic.

**•** `PageLayout` —The canvas app can appear on a page layout.
When viewed in the Salesforce mobile app, the canvas app appears
in the record detail page. Available in API version 31.0 and later.

**•** `Publisher` —The canvas app can appear as a global action.

**•** `ServiceDesk` —The canvas app can appear in the footer or
sidebars of a console in Salesforce Classic.

**•** `UserProfile` —Reserved for future use.

**•** `Visualforce` —The canvas app can appear on a Visualforce
page.


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

`options` CanvasOptions (enumeration of
type string)[]

Indicates whether to hide the **Share** button and header in the publisher
for your canvas app and whether the app is a canvas personal app.
Valid values are:

**•** `HideShare` —The **Share** button is hidden in the publisher for
the related canvas app. Available in API version 30.0 and later.

**•** `HideHeader` —The header is hidden in the publisher for the
related canvas app. Available in API version 30.0 and later.

**•** `PersonalEnabled` —End users can install the app as a canvas
personal app. Available in API version 32.0 and later.

`samlInitiationMethod` SamlInitiationMethod If you're using SAML single sign-on (SSO), indicates which provider
(enumeration of type string) initiates the SSO flow.

**•** `IdpInitiated` —Identity provider initiated. Salesforce makes
the initial request to start the SSO flow.

**•** `SpInitiated` —Service provider initiated. The canvas app starts
the SSO flow after it's invoked.

**•** `None` —The canvas app isn't using SAML SSO. Available in API
version 31.0 and later.

ConnectedAppIpRange

Represents the list of IP addresses that can access the app without requiring the user to authenticate.

**Field Name** **Field Type** **Description**

`description` string Identifies the purpose of the range, such as which part of a network
corresponds to this range. Available in API version 31.0 and later.

`end` string Required. The last address in the IP range, inclusive.

`start` string Required. The first address in the IP range, inclusive.

ConnectedAppOauthConfig

Represents the field names that configure how your connected app communicates with Salesforce.

**Field Name** **Field Type** **Description**

`assetTokenConfig` connectedAppOauthAssetToken The OAuth asset token configuration for the connected app OAuth
settings. Available in API version 49.0 and later.

`callbackUrl` string Required. The endpoint that Salesforce calls back to your connected
app during OAuth. It’s the OAuth `redirect_uri` .

`certificate` string The PEM-encoded certificate string, if the app uses a certificate.


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

`consumerKey` string

A value used by the consumer for identification to Salesforce. Referred
to as `client_id` in OAuth 2.0.

In API version 32.0 and later, you can set this field’s value only during
creation. After you define and save the value, it can’t be edited. The

value must be alphanumeric, can’t contain special characters or spaces,
and must be between 8–256 characters. Consumer keys must be
globally unique.

`consumerSecret` string A value that is combined with the `consumerKey` and used by the
consumer for identification to Salesforce. Referred to as

`client_secret` in OAuth 2.0. Typically, Salesforce generates this
value when you create the connected app. However, you can customize
the shared secret value during creation. After you save the value, it
can’t be edited. When set, the value isn’t returned in Metadata API
requests.

The value must be alphanumeric (no special characters and no spaces)
and a minimum of 8 characters (maximum of 256 characters). If you
specify a secret already in use for another connected app in the
organization, an error occurs.

Available in API version 32.0 and later.

`idTokenConfig` ConnectedAppOauthIdToken Specifies the ID token configuration for the connected app OAuth
settings. Available in API version 43.0 and later.

`isAdminApproved` boolean

`isClientCredentialEnabled` boolean

If set to `false` (default), anyone in the org can authorize the app.
Users must approve the app the first time they access it.

If set to `true`, only users with the appropriate profile or permission
set can access the app. These users don’t have to approve the app

before they can access it. Manage profiles for the app by editing each
profile’s Connected App Access list. Manage permission sets for the
app by editing each permission set’s Assigned Connected App list. This
setting isn’t available in Group Edition. Available in API version 46.0
and later.

Connected app consumers can edit this setting when deploying a
connected app in their org.

If set to `true`, the connected app can use the OAuth 2.0 client
credentials flow. To use the client credentials flow, you must also specify
a user for `oauthClientCredentialUser` .

If set to `false` (default), the connected app can’t use the client
credentials flow.

Available in API version 56.0 and later.

`isCodeCredentialEnabled` boolean Determines whether the app can use the Authorization Code and
Credentials Flow to provide identity services to headless, off-platform

apps. The Authorization Code and Credentials Flow is the foundation


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

of headless login, headless registration, headless passwordless login,
and headless guest identity.

If set to `true`, the connected app can use the Authorization Code and
Credentials Flow and all associated Headless Identity features. The
default value is `false` .

This field is available in API version 57.0 and later.

`isCodeCredentialPostOnly` boolean For the Authorization Code and Credentials Flow, determines whether
the user’s credentials must be sent in the body of the initial HTTPS POST

request to the Salesforce authorization endpoint. Requiring the
credentials in the POST body instead of in the header improves security.

If set to `true`, the user’s credentials must be included in the POST
body. The default value is `false` .

This field is available in API version 57.0 and later.

`isConsumerSecretOptional` boolean

`isIntrospectAllTokens` boolean

`isNamedUserJwtEnabled` boolean

If set to `false` (default), the connected app’s client secret is required
in exchange for an access token in the OAuth 2.0 web server flow.

If the client app can’t keep the client secret confidential and it must
use the web server flow, set to `true` . A client secret is still generated

for the connected app, but this setting instructs the web server flow
not to require the `client_secret` parameter in the access token
request. We recommend the user agent flow as a more secure option
than web server flow without the secret. Available in API version 49.0
and later.

If set to `true`, authorizes the connected app to introspect all access
and refresh tokens within the entire org.

If set to `false` (default), the connected app can introspect its own
tokens. In addition, an OAuth client that directly registers OAuth 2.0

connected apps through the dynamic client registration endpoint can
check the tokens for itself and its registered apps. Available in API
version 49.0 and later.

If set to `true`, the connected app is enabled to issue JSON Web Token
(JWT)-based access tokens.

This field is generally available in API version 59.0 and later.

`isPkceRequired` boolean Determines whether the Proof Key for Code Exchange (PKCE) extension
is required for variations of the OAuth 2.0 authorization code flow

configured for the connected app, including the web server flow and
Authorization Code and Credentials Flow. For public client apps that
can’t keep the consumer secret confidential, such as mobile apps, the
PKCE extension helps ensure that the client that initiates an
authorization flow is the same client that completes it. For this reason,


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

we always recommend implementing PKCE for public clients. We also
strongly recommend that you implement PKCE for private clients.

If set to `true`, the PKCE extension is required and any authorization
code flow variations that don’t implement it fail. If set to `false`, you
can still implement PKCE but it isn’t required. The default value is
`false` .

This field is available in API version 59.0 and later.

`isRefreshTokenRotationEnabled` boolean If set to `true`, the connected app issues a new refresh token each
time the OAuth refresh token flow is invoked. The old refresh token is

automatically invalidated. If a user tries to use a previous refresh token
that’s been invalidated, the current refresh token and its associated
access tokens get deleted. If set to `false`, the refresh token can be
used to obtain multiple access tokens.

This field is available in API version 60.0 and later.

`isSecretRequiredForRefreshToken` boolean If set to `true` (default), the app’s client secret is required in the
authorization request of a refresh token and hybrid refresh token flow.

If set to `false` and an app sends the client secret in the authorization
request, Salesforce still validates it.

Select this option for web-server based apps that can protect client
secrets. For apps that can’t protect client secrets, such as mobile apps
or apps installed on a user’s computer, we recommend against selecting
this option. Available in API version 51.0 and later.

`isSecretRequiredForTokenExchange` boolean If set to `true`, the connected app must include its consumer secret
( `client_secret` ) in the token request during the OAuth 2.0 token

exchange flow. For security, set this field to `true` only if your app has
a private client backend where it can keep the secret safe. For public
client apps, such as single-page apps and mobile apps, set this field to
`false` and don’t include the consumer secret.

This field is available in API version 60.0 and later.

`isTokenExchangeEnabled` boolean

`oauthClientCredentialUser` string

If set to `true`, the connected app can use the OAuth 2.0 token
exchange flow to exchange tokens from an external identity provider
for Salesforce tokens.

This field is available in API version 60.0 and later.

The execution user for the OAuth 2.0 client credentials flow. Salesforce
returns access tokens on behalf of this user. This user must have the
API Only permission.

To use this field, set `isClientCredentialEnabled` to `true`
and specify a `consumerKey` .

Available in API version 56.0 and later.


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

`scopes` ConnectedAppOauthAccessScope The permissions given by the user running the connected app. When
(enumeration of type string)[] deploying metadata, valid values are:

**•** `Basic` —Allows access to your identity URL service (the same
behavior as deploying `Address`, `Email`, `Phone`, and
`Profile` ).

**•** `Api` —Allows access to the logged-in user's account over the APIs.

**•** `Web` —Allows use of the `access_token` on the web. This
usage also includes `visualforce`, allowing access to Visualforce
pages.

**•** `Full` —Allows access to all data accessible by the logged-in user.

**•** `Chatter` —Allows access to only the Connect REST API resources.

**•** `CustomApplications` —Provides access to custom
applications, such as those using Visualforce.

**•** `RefreshToken` —Allows a refresh token to be returned if you’re
eligible to receive one (the same behavior as deploying
`OfflineAccess` ).

**•** `OpenID` —Allows access to the logged-in user's unique identifier
for OpenID Connect apps.

**•** `Profile` —Allows access to the logged-in user's profile (the
same behavior as deploying `Basic` ).

**•** `Email` —Allows access to the logged-in user's email address (the
same behavior as deploying `Basic` ).

**•** `Address` —Allows access to the logged-in user's street address
(the same behavior as deploying `Basic` ).

**•** `Phone` —Allows access to the logged-in user's phone number
value (the same behavior as deploying `Basic` ).

**•** `OfflineAccess` —Allows the app to interact with the user's
data while the user is offline and get a refresh token (the same
behavior as deploying `RefreshToken` ).

**•** `CustomPermissions` —Allows access to the custom
permissions in an organization associated with the connected app
and shows whether the current user has each permission enabled.

**•** `Wave` —Allows access to the Analytics REST API resources. Available
in API version 35.0 and later.

**•** `Eclair` —Allows access to the Analytics REST API Charts Geodata
resource. Available in API version 35.0 and later.

**•** `Pardot` —Allows access to Pardot API services on behalf of the
user. The full extent of accessible services is managed by the Pardot
account. Available in API version 49.0 and later.

**•** `Lightning` —Allows hybrid apps to directly obtain Lightning
child sessions through the OAuth 2.0 hybrid app token flow and
hybrid app refresh token flow. Available in API version 51.0 and
later.


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

**•** `Content` —Allows hybrid apps to directly obtain content child
sessions through the OAuth 2.0 hybrid app token flow and hybrid
app refresh token flow. Available in API version 51.0 and later.

**•** `CDPIngest` —Allows access to Data Cloud ingest API services.
Customers use these API services to upload and maintain external
datasets in the Data 360. Available in API version 52.0 and later.

**•** `Chatbot` —Allows access to Einstein Bot API services. Available
in API version 54.0 and later.

**•** `ForgotPassword` —Allows access to Headless Forgot Password
API. Assign to an internal integration user to get an access token
for authenticated requests to this API. Available in API version 57.0
and later.

**•** `UserRegistration` —Allows access to Headless Registration
API. Assign to an internal integration user to get an access token
for authenticated requests to this API. Available in API version 58.0
and later.

**•** `PwdlessLogin` —Allows access to Headless Passwordless Login
API. Assign to an internal integration user to get an access token
for authenticated requests to this API. Available in API version 59.0
and later.

When retrieving metadata, valid values are:

**•** `Api` —Allows access to the logged-in user’s account over the APIs.

**•** `Basic` —Allows access to the user’s identity URL service, and
includes `Address`, `Email`, `Phone`, and `Profile` .

**•** `Chatter` —Allows access to only the Connect REST API resources.

**•** `CustomApplications` —Allows access to custom
applications, such as those using Visualforce.

**•** `Full` —Allows access to all data accessible by the logged-in user.

**•** `OpenID` —Allows access to the logged-in user's unique identifier
for OpenID Connect apps.

**•** `CDPIngest` —Allows access to Data Cloud ingest API services.
Customers use these API services to upload and maintain external
datasets in the Data 360. Available in API version 52.0 and later.

**•** `Pardot` —Allows access to Pardot API services on behalf of the
user. The full extent of accessible services is managed by the Pardot
account. Available in API version 49.0 and later.

**•** `Lightning` —Allows hybrid apps to directly obtain Lightning
child sessions through the OAuth 2.0 hybrid app token flow and
hybrid app refresh token flow. Available in API version 51.0 and
later.

**•** `Content` —Allows hybrid apps to directly obtain content child
sessions through the OAuth 2.0 hybrid app token flow and hybrid
app refresh token flow. Available in API version 51.0 and later.


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

**•** `RefreshToken` —Allows a refresh token to be returned if you’re
eligible to receive one and is synonymous with allowing
`OfflineAccess` .

**•** `Wave` —Allows access to the Analytics REST API resources. Available
in API version 35.0 and later.

**•** `Eclair` —Allows access to the Analytics REST API Charts Geodata
resource. Available in API version 35.0 and later.

**•** `Web` —Allows usage of the `access_token` on the web. This
usage also includes `visualforce`, allowing access to Visualforce
pages.

**•** `Chatbot` —Allows access to Einstein Bot API services. Available
in API version 54.0 and later.

**•** `ForgotPassword` —Allows access to Headless Forgot Password
API. Assign to an internal integration user to get an access token
for authenticated requests to this API. Available in API version 57.0
and later.

**•** `UserRegistration` —Allows access to Headless Registration
API. Assign to an internal integration user to get an access token
for authenticated requests to this API. Available in API version 58.0
and later.

**•** `PwdlessLogin` —Allows access to Headless Passwordless Login
API. Assign to an internal integration user to get an access token
for authenticated requests to this API. Available in API version 59.0
and later.

`singleLogoutUrl` string The single logout endpoint. This URL is the endpoint where Salesforce
sends a logout request when users log out of Salesforce.

ConnectedAppOauthAssetToken

Specifies an OAuth asset token configuration for the connected app OAuth settings. Available in API version 49.0 and later.

**Field Name** **Field Type** **Description**

`assetAudiences` string Required. The audience claim associated with the asset token payload.
This claim identifies who the JWT is intended for. Value is an array of

case-sensitive strings, each containing a `StringOrURI` value. An
audience is specified for each intended consumer of the asset token.

`assetIncludeAttributes` boolean

`assetIncludeCustomPerms` boolean

Required. If set to `true` (default), custom attributes associated with
the connected app are included in the asset token payload. If set to
`false`, these attributes aren’t included.

Required. If set to `true` (default), custom permissions associated with
the connected app are included in the asset token payload. If set to
`false`, these permissions aren’t included.


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

`assetSigningCertId` string

`assetValidityPeriod` int

ConnectedAppOauthIdToken

Required. The ID of the JWT certificate’s signing secret. The certificate
size can’t exceed 4 KB. If it does, try using a DER encoded file to reduce
the size.

Required. The asset token’s validity period. The validity must be the
expiration time of the assertion within 3 minutes, expressed as the
number of seconds from 1970-01-01T0:0:0Z measured in UTC.

Specifies the ID token configuration for the connected app OAuth settings. Available in API version 43.0 and later.

**Field Name** **Field Type** **Description**

`idTokenAudience` string The audiences that this ID token is intended for. The value is an array
of case-sensitive strings. If no audiences are specified, the OAuth

2.0 `client_id` of the relying party is returned as the default
audience. Otherwise, the other audiences are returned with the
`client_id` in the `aud` value.

`idTokenIncludeAttributes` boolean Indicates whether attributes are included in the ID token.

`idTokenIncludeCustomPerms` boolean Indicates whether custom permissions are included in the ID token.

`idTokenIncludeStandardClaims` boolean Indicates whether standard claims about the authentication event are
included in the ID token.

`idTokenValidity` int The length of time that the ID token is valid for after it’s issued. The
value can be from 1 to 720 minutes. The default is 2 minutes.

ConnectedAppOauthPolicy

Specifies OAuth access policies for the connected app. Available in API version 49.0 and later.

**Field Name** **Field Type** **Description**

`ipRelaxation` string Required. Specifies whether a user’s access to the connected app is
restricted by IP ranges. Valid options are:

**•** `ENFORCE` (default)—Enforces the IP restrictions configured for
the org, such as the IP ranges assigned to a user profile.

**•** `BYPASS_2FACTOR` —Allows a user running the app to bypass
the org’s IP restrictions when either of these conditions is true.

**–** The app has a list of allowed IP ranges and is using the web
server OAuth authorization flow. Requests coming from only
these IPs are allowed.

**–** The app doesn’t have a list of allowed IP ranges, but it uses the
web server authentication flow. And the user successfully


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

completes identity verification if accessing Salesforce from a
new browser or device.

**•** `BYPASS` —Allows a user to run this app without org IP restrictions.

**•** `ENFORCE_RELAXREFRESH` —Enforces the IP restrictions
configured for the org, such as the IP ranges assigned to a user
profile. However, this option bypasses these restrictions when the
connected app uses refresh tokens to get access tokens.

`refreshTokenPolicy` string

Required. Specifies how long a refresh token is valid for.

If refresh tokens are provided, users can continue to access the
OAuth-enabled connected app without having to reauthorize when

the access token expires, as defined by the session timeout value. The
connected app exchanges the refresh token with an access token to
start a new session. The Refresh Token policy is evaluated only during
usage of the issued refresh token and doesn’t affect a user’s current
session. Refresh tokens are required only when a user’s session has
expired or isn’t available. For example, you set a refresh token policy
to expire the token after 1 hour. If a user uses the app for 2 hours, the
user isn’t forced to reauthenticate after 1 hour. However, the user is
required to authenticate again when the session expires and the client
attempts to exchange its refresh token for a new session.

Valid options are:

**•** `zero` —The refresh token is invalid immediately. The user can use
the current session (access token) already issued, but can’t obtain
a new session when the access token expires.

**•** `infinite` —The refresh token is used indefinitely, unless revoked
by the user or Salesforce admin. Default setting.

**•** `specific_lifetime:` _**`number`**_ `:` _**`HOURS, DAYS,`**_
_**`MONTHS`**_ —The refresh token is valid for a fixed amount of time.
For example, if the policy states
`specific_lifetime:1:DAYS`, the user can obtain new
sessions for only 24 hours.

**•** `specific_inactivity:` _**`number`**_ `:` _**`HOURS, DAYS,`**_
_**`MONTHS`**_ —The refresh token is valid as long as it’s been used
within the specified amount of time. For example, if set to
`specific_inactivity:7:DAYS`, and the refresh token
isn’t exchanged for a new session within seven days, the next
attempt to use the token fails. The expired token can’t generate
new sessions. If the refresh token is exchanged within seven days,
the token is valid for another seven days. The monitoring period
of inactivity also resets.

`singleLogoutUrl` string If single logout is enabled, specify the single logout URL. Salesforce
sends logout requests to this URL when users log out of Salesforce.


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

The single logout URL must be an absolute URL starting with
`https://` .

ConnectedAppSamlConfig

Specifies how an app uses single sign-on.

**Field Name** **Field Type** **Description**

`acsUrl` string Required. The assertion consumer service URL from the service provider.

`certificate` string The PEM-encoded certificate string, if the app uses a certificate.

`encryptionCertificate` string The name of the certificate to use for encrypting SAML assertions to
the service provider. This certificate is saved in the organization's

Certificate and Key Management list. Available in API version 30.0 and
later.

```
encryptionType

```

When Salesforce is the identity provider, the SAML configuration can
SamlEncryptionType
specify the encryption method used for encrypting SAML assertions

(enumeration of type string)

to the service provider. The service provider detects the encryption
method in the SAML assertion for decryption. Valid values are:

**•** `AES_128` —128–bit key

**•** `AES_256` —256–bit key

Available in API version 30.0 and later.

`entityUrl` string Required. The entity ID from your service provider.

`issuer` string

A URI that sends the SAML response. A service provider can use this
URI to determine which identity provider sent the response. Available
in API version 29.0 and later.

`samlIdpSLOBindingEnum` SamlIdpSLOBinding (enumeration The SAML HTTP binding type from the service provider used for single
of type string) logout. Available in API version 40.0 and later. Valid values are:

**•** `PostBinding`

**•** `RedirectBinding`

`samlNameIdFormat` SamlNameIdFormatType
(enumeration of type string)

Indicates the format the service provider (SP) requires for the user's
single sign-on identifier. Available in API version 29.0 and later. Valid
values are:

**•** `Unspecified` (default)—No format given.

**•** `EmailAddress` —Used if the subject type is the user's name
or a federation ID (an ID internal to the SP).

**•** `Persistent` —Used with the user ID and persistent ID subject
types.

**•** `Transient` —Used when the subject type is a custom attribute
and can change every time the user logs in.


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

`samlSigningAlgoType` SamlSigningAlgoType Indicates the signing algorithm applied to SAML requests and responses
(enumeration of type string) when Salesforce is the identity provider. The selected signing algorithm

is applied to both single sign-on and single logout responses from your
org. Available in API version 50.0 and later. Valid values are:

**•** `SHA1`

**•** `SHA256`

`samlSloUrl` string The SAML single-logout endpoint of the connected app service provider
(SP). This endpoint is where SAML LogoutRequests and

LogoutResponses are sent when users log out of Salesforce. The SP
provides this endpoint. Available in API version 40.0 and later.

`samlSubjectCustomAttr` string

If the `samlSubjectType` is `CustomAttr`, include that custom
value here; otherwise, leave empty. Available in API version 29.0 and
later.

`samlSubjectType` SamlSubjectType (enumeration of Required. The single sign-on identifier for the user. Valid values are:
type string)

**•** `Username` —The user's Salesforce name.

**•** `FederationId` —The user's identifier at the service provider.
Get this value from the service provider.

**•** `UserId` —The user's 15-character Salesforce identifier.

**•** `PersistentID` —A persistent opaque identifier that is specific
to the identity provider and a service provider.

**•** `CustomAttr` —The identifier is taken from a custom field value
in `samlSubjectCustomAttr` .

ConnectedAppSessionPolicy

Specifies the configuration options for a connected app’s session policies. Use these policies to define how long a user’s session can last
before reauthenticating, to block user access to the connected app, or to require multi-factor authentication (MFA) to access the app.
Available in API version 49.0 and later.

**Field Name** **Field Type** **Description**

`policyAction` string If the High Assurance session security level is applied to the connected
app, specify associated high assurance action. Valid values are:

**•** `Block` —Makes the connected app inaccessible to your org’s
users. Blocking an app ends all current user sessions with the
connected app and prevents all new sessions.

**•** `RaiseSessionLevel` —Requires users to verify their identity
with multi-factor authentication when they log in to the connected
app. This setting applies to authorization flows that include a user
approval step for API logins. These flows are the OAuth 2.0 refresh
token flow, web server flow, and user-agent flow. All other flows,
such as the JSON Web Token (JWT) bearer token flow, don’t include


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

a user approval step. For flows without a user approval step, API
logins with the High Assurance session security level are blocked.

`sessionLevel` string

Applies the High Assurance session security level to the connected
app. This session level requires users to verify their identity with
multi-factor authentication when they log in to the connected app.

`sessionTimeout` int The length of time the connected app’s session lasts. If you don’t set
a value, Salesforce uses the timeout value in the connected app user’s

profile. If the user’s profile doesn’t specify a timeout value, Salesforce
uses the timeout value in the org’s Session Settings.

Declarative Metadata Sample Definition

The following is an example of a ConnectedApp component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ConnectedApp xmlns="http://soap.sforce.com/2006/04/metadata">

   <attributes>

     <formula>$Api.Enterprise_Server_URL_100</formula>

     <key>test</key>

   </attributes>

   <attributes>

     <formula>$Api.Partner_Server_URL_60</formula>

     <key>test1</key>

   </attributes>

  <canvasConfig>

     <accessMethod>Get</accessMethod>

     <canvasUrl>https://salesforce.com</canvasUrl>

     <lifecycleClass>MyCanvasListener</lifecycleClass>

     <locations>Chatter</locations>

     <locations>Visualforce</locations>

     <locations>Aura</locations>

     <locations>Publisher</locations>

     <locations>ChatterFeed</locations>

     <locations>OpenCTI</locations>

     <locations>MobileNav</locations>

     <locations>PageLayout</locations>

     <options>HideShare</options>

     <options>HideHeader</options>

     <options>PersonalEnabled</options>

     <samlInitiationMethod>None</samlInitiationMethod>

   </canvasConfig>

   <canvas>

   <locationOptions>NONE</locationOptions>

   <samlInitiationMethod>None</samlInitiationMethod>

   <accessMethod>Get</accessMethod>

   <canvasOptions>PE</canvasOptions>

   <lifecycleClass>MyCanvasListener</lifecycleClass>

   <canvasUrl>https://salesforce.com</canvasUrl>

 </canvas>

```


Metadata Types ConnectedApp

```
      <contactEmail>example@salesforce.com</contactEmail>

      <contactPhone>1231231234</contactPhone>

      <description>Test App</description>

   <iconUrl>https://c1.sfdcstatic.com/content/dam/sfdc-docs/www/logos/salesforce-logo-cloud.png</iconUrl>

   <infoUrl>https://c1.sfdcstatic.com/content/dam/sfdc-docs/www/logos/salesforce-logo-cloud.png</infoUrl>

      <startUrl>https://www.salesforce.com</startUrl>

      <ipRanges>

        <end>000.0.0.1</end>

        <start>000.0.0.2</start>

    <description>Test</description>

      </ipRanges>

      <ipRanges>

        <end>000.0.0.1</end>

        <start>000.0.0.2</start>

    <description>Test1</description>

      </ipRanges>

      <label>TestApp</label>

   <logoUrl>https://c1.sfdcstatic.com/content/dam/sfdc-docs/www/logos/salesforce-logo-cloud.png</logoUrl>

      <profileName>Test</profileName>

      <permissionSetName>TestPermission</permissionSetName>

      <mobileStartUrl>http://www.mobile.com</mobileStartUrl>

      <mobileAppConfig>

        <applicationBinaryFile></applicationBinaryFile>

        <applicationBinaryFileName>test</applicationBinaryFileName>

        <applicationBundleIdentifier>testtest</applicationBundleIdentifier>

        <applicationIconFileName>test</applicationIconFileName>

    <applicationIconFile>test</applicationIconFile>

    <applicationFileLength>5</applicationFileLength>

        <applicationInstallUrl>https://salesforce.com</applicationInstallUrl>

        <devicePlatform>ios</devicePlatform>

        <deviceType>minitablet</deviceType>

        <minimumOsVersion>2</minimumOsVersion>

        <privateApp>true</privateApp>

        <version>2</version>

      </mobileAppConfig>

      <oauthConfig>

        <assetTokenConfig>

           <assetAudiences>http://asset.audience.com</assetAudiences>

           <assetIncludeAttributes>true</assetIncludeAttributes>

           <assetIncludeCustomPerms>true</assetIncludeCustomPerms>

           <assetSigningCertId>${cert.id}</assetSigningCertId>

           <assetValidityPeriod>1440</assetValidityPeriod>

        </assetTokenConfig>

        <callbackUrl>https://www.callback.com</callbackUrl>

        <!-- NOTE, TEST.orgId will get replaced with the org ID of the context org, so

   we will have a unique consumer key in every scratch org. -->

        <consumerKey>3MVG9AOp4kbriZOcnmoLmTrguy9ryzcLbBjoNY...${TEST.orgId}</consumerKey>

```


Metadata Types ConnectedApp

```
     <consumerSecret>3MVG9AOp4k...</consumerSecret>

     <certificate>3MVG9AOp4kbriZOInmoLmTrguy9ryzcLbBjoNY...</certificate>

        <scopes>Basic</scopes>

        <scopes>Chatter</scopes>

        <scopes>OpenID</scopes>

        <scopes>CustomPermissions</scopes>

     <singleLogoutUrl>https://www.logout.com</singleLogoutUrl>

        <isAdminApproved>false</isAdminApproved>

        <isConsumerSecretOptional>false</isConsumerSecretOptional>

        <isIntrospectAllTokens>false</isIntrospectAllTokens>

     <idTokenConfig>

     <idTokenAudience>https://idtoken.audience.com</idTokenAudience>

     <idTokenIncludeAttributes>true</idTokenIncludeAttributes>

     <idTokenIncludeCustomPerms>true</idTokenIncludeCustomPerms>

     <idTokenIncludeStandardClaims>true</idTokenIncludeStandardClaims>

     <idTokenValidity>20</idTokenValidity>

     </idTokenConfig>

      </oauthConfig>

      <oauthPolicy>

        <ipRelaxation>ENFORCE</ipRelaxation>

        <refreshTokenPolicy>infinite</refreshTokenPolicy>

        <singleLogoutUrl>https://www.logout.com</singleLogoutUrl>

      </oauthPolicy>

      <plugin>ConnectedAppPluginTest</plugin>

      <pluginExecutionUser>testuser@salesforce.com</pluginExecutionUser>

      <samlConfig>

        <acsUrl>http://www.acs.com</acsUrl>

        <encryptionType>AES_128</encryptionType>

    <encryptionCertificate>3MVG9AOp4kbriZOInmoLmTrguy9ryzcLbBjoNY...</encryptionCertificate>

    <certificate>3MVG9AOp4kbriZOInmoLmTrguy9ryzcLbBjoNY...</certificate>

    <samlSubjectCustomAttr>test</samlSubjectCustomAttr>

        <entityUrl>http://www.entity.com</entityUrl>

        <issuer>https://salesforce.com</issuer>

        <samlIdpSLOBindingEnum>RedirectBinding</samlIdpSLOBindingEnum>

        <samlNameIdFormat>Unspecified</samlNameIdFormat>

        <samlSloUrl>https://www.salesforce.com</samlSloUrl>

        <samlSubjectType>CustomAttribute</samlSubjectType>

      </samlConfig>

      <sessionPolicy>

        <policyAction>RaiseSessionLevel</policyAction>

        <sessionLevel>HIGH_ASSURANCE</sessionLevel>

        <sessionTimeout>720</sessionTimeout>

      </sessionPolicy>

   </ConnectedApp>

```

You can enter multiple callback URL values. At run time, Salesforce validates the callback URL specified by the app by matching it with
one of the values. You must separate each callback URL with line breaks. To enter a new line programmatically, use the `\r` line break
character.

Here's an example of a ConnectedApp component with multiple callback URLs.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ConnectedApp xmlns="http://soap.sforce.com/2006/04/metadata">

    <contactEmail>example@salesforce.com</contactEmail>

```


Metadata Types ConnectedApp

```
    <label>MyConnectedApp</label>

    <oauthConfig>

    <callbackUrl>https://example.com/callback1

   https://example.com/callback2

   https://example.com/callback3</callbackUrl>

    <consumerKey>3MVG9AOp4kbriZOcnmoLmTrguy9ryzcLbBjoNY...</consumerKey>

    <isAdminApproved>false</isAdminApproved>

    <isConsumerSecretOptional>false</isConsumerSecretOptional>

    <isIntrospectAllTokens>false</isIntrospectAllTokens>

    <isSecretRequiredForRefreshToken>true</isSecretRequiredForRefreshToken>

    <scopes>Full</scopes>

    <scopes>RefreshToken</scopes>

    </oauthConfig>

    <oauthPolicy>

    <ipRelaxation>ENFORCE</ipRelaxation>

    <refreshTokenPolicy>infinite</refreshTokenPolicy>

    </oauthPolicy>

   </ConnectedApp>

```

The following is an example package manifest used to deploy or retrieve the ConnectedApp metadata for an organization.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>PortalTestApp</members>

        <name>ConnectedApp</name>

      </types>

      <version>29.0</version>

   </Package>

```

Usage

If you're constructing a SAML-enabled connected app using Metadata API, and must set the `IdP-Initiated Login URL` for
your service provider, you have two options:

You can use the service provider app ID with the `app` parameter in the following format. This value is displayed in the Salesforce user
interface. From Setup, enter _`Connected Apps`_ in the Quick Find box, then select **Connected Apps**, then click the name of the
connected app to see its detail page.

```
   https:// <Salesforce_base_URL> /idp/login?app= <app_id>

```

Or, if you're configuring the connected app using Metadata API only, you can use the `apiName` parameter of the service provider app
in the following format. The `apiName` parameter is the `fullName` inherited from the Metadata type.

```
   https:// <Salesforce_base_URL> /idp/login?apiName= <fullName>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types ContentAsset ContentAsset

Represents the metadata for creating an asset file. Asset files enable a Salesforce file to be used for org setup and configuration purposes.
This type extends the MetadataWithContent metadata type and inherits its `content` and `fullName` fields.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### ContentAsset components have the suffix .asset and are stored in the contentassets folder.

Version

### ContentAsset components are available in API version 38.0 and later.

Special Access Rules

The system prevents metadata retrieval if the total size of the asset’s file content exceeds 30 MB. All pre-existing limits for packaging
apply to asset files.

Fields

**Field Name** **Field Type** **Description**

```
format

```

### ContentAssetFormat Describes the format of the asset file. Valid values are:

(enumeration of

**•** `Original` —A single asset file version.

type string)

**•** `Original` —A single asset file version.

**•** `ZippedVersions` —Contains multiple versions of the asset file.

`isVisibleByExternalUsers` boolean

Indicates whether unauthenticated users can see the asset file ( `true` )
or not ( `false` ). If not specified, the default value is `false` . This field
is available in API version 44.0 and later.

`language` string Required. The language of the asset file label.

`masterLabel` string Required. The label for the asset file record, which displays in Setup.

`originNetwork` string For deploys, the name of the Experience Cloud site the file is assigned
upon creation. For retrievals, the name of the Experience Cloud site the

file is assigned to appears in the field value. If `null`, the file wasn’t
assigned to an Experience Cloud site.

### relationships ContentAssetRelationships The list of ContentAssetLinks that describe whether the asset file can be

shared with the org.

### versions ContentAssetVersions Required. Captures basic information about the file version included the

asset metadata. Typically the file has only one version.


Metadata Types ContentAsset

ContentAssetRelationships

Represents the relationships between an asset file and the locations it's linked with.

**Field Name** **Field Type** **Description**

`emailTemplate` ContentAsset[] An array of email templates the content asset is related to. This field is available
in API version 51.0 and later.

`insightsApplication` ContentAsset[] An array of the insights applications that use the content asset. This field is
available in API version 39.0 and later.

`network` ContentAsset[] An array of networks that use the content asset. This field is available in API
version 39.0 and later.

`organization` ContentAsset[] Stores information about sharing the asset file with the org. Maps to
ContentDocumentLink. This field is available in API version 39.0 and later.

`workspace` ContentAsset[] An array of workspaces and libraries that own or share the content asset. This
field is available in API version 39.0 and later.

ContentAssetLink

Represents a relationship link for an asset file, and includes details about the level of access for the link.

**Field Name** **Field Type** **Description**

```
access

```

ContentAssetAccess Required. The permission granted to the user of the shared file, determined by
(enumeration of type the permission the user already has. Valid values are:
string)

**•** `VIEWER`

**•** `COLLABORATOR`

**•** `INFERRED`

`isManagingWorkspace` boolean

Indicates whether the content asset resides in the workspace or not. When
`true`, the content asset resides in the workspace. If not specified, the default
value is `false` . This field is available in API version 39.0 and later.

`name` string Reserved for future use.

ContentAssetVersions

Represents information about all file versions included in the asset metadata.

**Field Name** **Field Type** **Description**

`version` ContentAssetVersion[] A list of file versions for the asset.


Metadata Types ContentAsset

ContentAssetVersion

Represents information about one file version included in the asset metadata.

**Field Name** **Field Type** **Description**

`number` string Required. The version number. This field is based on, or sets, the ContentVersion.

`pathOnClient` string

`zipEntry` string

Required. Describes the original filename of the file. This field maps to
ContentVersion.PathOnClient. It provides the data for the ContentVersion Title
field.

If the asset file has more than one version, `format` is `ZippedVersions` .
In this case, `zipEntry` is the name of the file within the zip. If the asset file
has only one version, this field is empty.

Declarative Metadata Sample Definition

The following is an example of a ContentAsset component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ContentAsset xmlns="http://soap.sforce.com/2006/04/metadata">

   <masterLabel>some asset</masterLabel>

   <relationships>

     <organization>

        <access>VIEWER</access>

     </organization>

   </relationships>

   <versions>

     <version>

        <number>1</number>

        <pathOnClient>some asset.txt</pathOnClient>

     </version>

   </versions>

</ContentAsset>

```

For assets that include just one version, the format field can be omitted or specified with the value as `Original` . File assets with more
than one version have versions wrapped in a zip file.

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>MyAsset</members>

     <name>ContentAsset</name>

   </types>

   <version>66.0</version>

</Package>

```


### Metadata Types ContentTypeBundle

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### ContentTypeBundle

Represents the definition of enhanced custom content types for use with enhanced CMS workspaces. When you create an enhanced
custom content type, deploy this bundle to your org. Enhanced custom content types are displayed as forms with defined fields. When
deployed, enhanced custom content types are available for use with enhanced LWR site channels. To use enhanced custom content
types with Aura and non-enhanced LWR site channels, use enhanced CMS workspaces resources.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata type and inherits its `fullName` field.

### ContentTypeBundle Structure and Directory Location ContentTypeBundle components are stored in the contentTypes folder. Here’s an example of how the folder is structured.

```
   +--myMetadataPackage

      +--contentTypes (1)

        +--bbHost (2)

          +--schema.json (3)

```

**•** The contentTypes folder (1) contains a folder for each enhanced custom content type.

**•** Each enhanced custom content type folder is named in the format _`contentTypeName`_ . In this example (2), the name is _`bbHost`_ .

**•** Each contentTypeName folder contains a JSON file, `schema.json` (3), that defines the enhanced custom content type. The JSON
file contains a title and one or more Lightning property types. Use this file to edit the properties of the enhanced custom content
type on your local machine or scratch org and then deploy it.

Version

### ContentTypeBundle components are available in version 64.0 and later.

Special Access Rules

### ContentTypeBundle is available only when Salesforce CMS and digital experiences are enabled for your org.


Metadata Types ContentTypeBundle

Fields

**Name** **Description**

```
description

masterLabel

resources

```

**Type**
string

**Description**
Explanatory text about the content type.

**Type**
string

**Description**
Required.

A name for ContentTypeBundle, which is defined when the ContentTypeBundle is
created.

**Type**

ContentTypeBundleResource[]

**Description**
A list of source files in the ContentTypeBundle folder.

ContentTypeBundleResource

Represents the resource file inside the ContentTypeBundle.

**Name** **Description**

```
fileName

filePath

source

```

**Type**
string

**Description**
Required.

The name of the resource file.

**Type**
string

**Description**
Required.

The path to the resource.

**Type**
base64Binary

**Description**
Required.


Metadata Types ContentTypeBundle

**Name** **Description**

The content of the resource.

Declarative Metadata Sample Definition

This `package.xml` retrieves all of the ContentTypeBundle components in an org.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ContentTypeBundle</name>

      </types>

      <version>64.0</version>

   </Package>

```

In the retrieved `.zip` file, each enhanced custom content type is nested under a contentTypes folder.

This example shows the directory structure in the `.zip` file of an enhanced custom content type. The enhaced custom content type
is named bbHost and in this example it represents the profile of a bed and breakfast host.

```
   contentTypes

      bbHost

        schema.json

```

Here are the example contents of the `schema.json` file in the contentTypes directory. The bbHost is a complex type that includes
subproperties for `fullName`, `aboutMe`, `interests`, `profilePicture`, `dateOfBirth`, `lastModified`,
`personalWebsite`, `hostIdentityVerified`, `hostingExperienceInYears`, `rating`, `residenceCountry`,
and `preferredModeOfContact` . Each subproperty is a primitive type. The subproperty types included in the `schema.json`
file are completely configurable and must include a `lightning:type` for each property.

```
   {

     "title": "Bed & Breakfast Host",

     "description": "Schema for capturing B&B host details",

     "lightning:type": "lightning__objectType",

     "lightning:mixinTypes": {

      "sfdc_cms:metadataContent": {}

     },

     "properties": {

      "fullName": {

       "title": "Full Name",

       "lightning:type": "lightning__textType",

       "lightning:textIndexed": true,

       "minLength": 5,

       "maxLength": 50,

       "lightning:uiOptions": {

        "placeholderText": "Enter your full name (e.g., John Doe)"

       },

       "lightning:localizable": false

      },

      "aboutMe": {

       "title": "About Me",

```


Metadata Types ContentTypeBundle

```
       "lightning:type": "lightning__richTextType",

       "minLength": 10,

       "maxLength": 3000,

       "lightning:textIndexed": false,

       "lightning:uiOptions": {

        "placeholderText": "Write something about yourself"

       },

       "lightning:localizable": true

      },

      "interests": {

       "title": "Interests and Hobbies",

       "lightning:type": "lightning__multilineTextType",

       "lightning:textIndexed": true,

       "minLength": 10,

       "maxLength": 500,

       "lightning:uiOptions": {

        "placeholderText": "Summarize your interests and hobbies in a few lines"

       },

       "lightning:localizable": true

      },

      "profilePicture": {

       "title": "Profile Picture",

       "lightning:type": "lightning__imageType",

       "lightning:uiOptions": {

        "placeholderText": "Upload a professional headshot"

       },

       "lightning:localizable": false

      },

      "dateOfBirth": {

       "title": "Date of Birth",

       "lightning:type": "lightning__dateType",

       "lightning:localizable": true,

       "lightning:uiOptions": {

        "placeholderText": "Select your date of birth"

       }

      },

      "lastModified": {

       "title": "Last Profile Update",

       "lightning:type": "lightning__dateTimeType",

       "lightning:localizable": false,

       "lightning:uiOptions": {

        "placeholderText": "Auto-filled on profile update"

       }

      },

      "personalWebsite": {

       "title": "Personal Website",

       "lightning:type": "lightning__urlType",

       "lightning:localizable": false,

       "lightning:uiOptions": {

        "placeholderText": "https://yourwebsite.com"

       }

      },

      "hostIdentityVerified": {

       "title": "Host Identity Verified",

```


Metadata Types ContentTypeBundle

```
       "lightning:type": "lightning__booleanType",

       "lightning:uiOptions": {

        "placeholderText": "Check if host identity is verified"

       }

      },

      "hostingExperienceInYears": {

       "title": "Years of Experience hosting B&B",

       "lightning:type": "lightning__integerType",

       "minimum": 0,

       "maximum": 50,

       "lightning:localizable": false,

       "lightning:uiOptions": {

        "placeholderText": "Enter total years of experience being a B&B host"

       }

      },

      "rating": {

       "title": "Rating",

       "lightning:type": "lightning__numberType",

       "minimum": 0.0,

       "maximum": 5.0,

       "lightning:localizable": false,

       "lightning:uiOptions": {

        "placeholderText": "e.g., 4.5"

       }

      },

      "residenceCountry": {

       "title": "Country of Residence",

       "lightning:type": "lightning__textType",

       "const": ["India"]

      },

      "preferredModeOfContact": {

       "title": "Preferred Mode of Contact",

       "lightning:type": "lightning__textType",

       "enum": ["email", "SMS", "phone"],

       "lightning:uiOptions": {

        "placeholderText": "Choose your preferred mode of contact"

       }

      }

     },

     "required": ["fullName", "hostIdentityVerified"]

```

Usage

For each custom content type that you create, you must also create a CMS content page created in the enhanced LWR, LWR, or Aura
[site that displays the content. Each content page serves as the detail page for all content of a single content type. See Create Custom](https://help.salesforce.com/articleView?id=community_builder_create_page.htm&language=en_US)
[Site Pages with Experience Builder.](https://help.salesforce.com/articleView?id=community_builder_create_page.htm&language=en_US)

To use enhanced custom content types with Aura and non-enhanced LWR site channels, use the enhanced CMS workspaces resources
[for CMS Delivery Contents](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/connect_resources_cms_delivery_contents.htm) [and CMS Delivery Content.](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/connect_resources_cms_delivery_content.htm)


### Metadata Types ContextDefinition

Wildcard Support in the Manifest

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving with the Zip .

### ContextDefinition

Represents the details of a context definition that describe the relationship between the node structures within a context.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

### ContextDefinition components have the suffix .contextDefinition and are stored in the contextDefinitions folder.

Version

### ContextDefinition components are available in API version 59.0 and later.

Special Access Rules

Enable the organization preference ContextDefinitionsEnabled to access the ContextDefinition metadata type.

Fields

**Field Name** **Description**

```
canBeReferenceDefinition

clonedFrom

```

**Field Type**
boolean

**Description**
Indicates whether the context definition can be referred by other context definitions
( `true` ) or not ( `false` ). Available in API version 63.0 and later.

The default value is `false` .

**Field Type**
string

**Description**
The name of the context definition that's used to clone the current context definition.


Metadata Types ContextDefinition

**Field Name** **Description**

```
contextDefinitionReferences

contextDefinitionVersions

contextTtl

description

hasSystemTags

inheritedFrom

inheritedFromVersion

```

**Field Type**

ContextDefinitionReference[]

**Description**
References of the context definition.

**Field Type**

ContextDefinitionVersion[]

**Description**
Version of the context definition.

**Field Type**
int

**Description**

Duration to persist the data, which is loaded in the run-time context instances created
by this context definition, in the cache.

The default value is 10 minutes.

**Field Type**
string

**Description**
Description of the context definition.

**Field Type**
boolean

**Description**
Indicates whether the context definition has system tags ( `true` ) or not ( `false` ).
Available in API version 63.0 and later.

The default value is `false` .

**Field Type**
string

**Description**
Name of the parent context definition that's used to derive the current context
definition.

**Field Type**
string

**Description**
Version number of the parent definition that's used to derive the current context
definition.


Metadata Types ContextDefinition

**Field Name** **Description**

```
isProtected

masterLabel

title

```

**Field Type**
boolean

**Description**
Auto-generated value that doesn’t impact the behavior of the metadata type.

**Field Type**
string

**Description**

Required.

User-friendly name for the context definition, which is defined when the context
definition is created.

**Field Type**
string

**Description**

Required.

Name of the context definition.

ContextDefinitionReference

Represents details about the context definition reference.

**Field Name** **Description**

```
inheritedFrom

referenceContextDefinition

```

**Field Type**
string

**Description**
ID of the parent context definition reference that's used to derive the current context
definition reference.

**Field Type**
string

**Description**

Required.

ID or name of the referred context definition.

ContextDefinitionVersion

Represents details about the context definition version. Only one version can be active at a time.


Metadata Types ContextDefinition

**Field Name** **Description**

```
contextMappings

contextNodes

endDate

isActive

startDate

versionNumber

```

ContextMapping

**Field Type**

ContextMapping[]

**Description**
Mapping of attributes and nodes to related objects.

**Field Type**

ContextNode[]

**Description**
Details of the structure of the nodes within the context.

**Field Type**
string

**Description**
Date and time when the context definition version becomes inactive.

**Field Type**
boolean

**Description**
Indicates whether the context definition version is active ( `true` ) or not ( `false` ).

The default value is `false` .

**Field Type**
string

**Description**

Required.

Date and time when the context definition version becomes active.

**Field Type**
int

**Description**

Required.

Version number of the context definition.

Represents the mapping of attributes and nodes to related objects.

**Field Name** **Description**

```
contextMappingIntents

```

**Field Type**

ContextMappingIntent[]


Metadata Types ContextDefinition

**Field Name** **Description**

**Description**
Purpose associated to a context mapping.

```
contextNodeMappings

default

description

inheritedFrom

title

```

ContextMappingIntent

**Field Type**

ContextNodeMapping[]

**Description**
Mapping of the node in the context and values in the input schema.

**Field Type**
boolean

**Description**
Indicates whether the mapping for a context definition version is default ( `true` ) or
not ( `false` ).

The default value is `false` .

**Field Type**
string

**Description**
Description of the context mapping.

**Field Type**
string

**Description**
Name of the parent mapping that's used to derive the current mapping.

**Field Type**
string

**Description**

Required.

Name of the context mapping.

Represents the purpose associated to a context mapping.

**Field Name** **Description**

```
mappingIntent

```

**Field Type**
ContextMappingIntentType (enumeration of type string)

**Description**

Required.


Metadata Types ContextDefinition

**Field Name** **Description**

Specifies the purpose that's used to identify the type of context mapping required.

Valid values are:

**•** `hydration`

**•** `association`

**•** `persistence`

**•** `translation`

ContextNodeMapping

Represents the relationship between the node in the context and values in the input schema.

**Field Name** **Description**

```
contextAttributeMappings

contextNode

contextNodeAttrDictionaries

inheritedFrom

mappedContextDefinition

object

```

**Field Type**

ContextAttributeMapping[]

**Description**
Mapping of the attribute defined in the context and the values in the related objects.

**Field Type**
string

**Description**
Context node record associated with the context node mapping.

**Field Type**

ContextNodeAttrDictionary[]

**Description**
Facilitates relationships between context node mapping and context dictionary.
Additionally, it records the relationship between context node and context dictionary.

**Field Type**
string

**Description**
Name of the parent context node mapping that's used to derive the current context
node mapping.

**Field Type**
string

**Description**
API name of the context definition for existing context-to-context mappings.

**Field Type**
string


Metadata Types ContextDefinition

**Field Name** **Description**

**Description**
Name of the object used for the mapping.

ContextAttributeMapping

Represents the relationship between the attributes defined in the context and the values in the related objects.

**Field Name** **Description**

```
contextAttrHydrationDetails

contextAttribute

contextInputAttributeName

ctxAttrHydrationCtxs

inheritedFrom

```

**Field Type**

ContextAttrHydrationDetail[]

**Description**
Details of the SOQL (database) queries that fetch data for a chosen attribute from the
input schema.

**Field Type**
string

**Description**
Context attribute record associated with the context attribute mapping.

**Field Type**
string

**Description**

Required.

Name of the input attribute.

**Field Type**

CtxAttrHydrationCtx[]

**Description**
Query that fetches data for a chosen attribute from the input schema for
context-to-context mapping.

**Field Type**
string

**Description**
Name of the parent context attribute mapping that's used to derive the current context
attribute mapping.

ContextAttrHydrationDetail

Represents the SOQL (database) queries that fetch data for a chosen attribute from the input schema.


Metadata Types ContextDefinition

**Field Name** **Description**

```
contextAttrHydrationDetails

inheritedFrom

objectName

queryAttribute

```

CtxAttrHydrationCtx

**Field Type**

ContextAttrHydrationDetail[]

**Description**
Details of the query that fetches the data for the specific query attribute.

**Field Type**
string

**Description**
Name of the parent context attribute hydration detail that's used to derive the current
context attribute hydration detail.

**Field Type**
string

**Description**

Required.

Name of the object used for the attribute hydration detail.

**Field Type**
string

**Description**

Required.

The SOQL query that is the source of the hydration.

Represents the queries that fetch data for a chosen attribute from the input schema for context-to-context mapping.

**Field Name** **Description**

```
contextQueryAttribute

inheritedFrom

```

**Field Type**
string

**Description**

Required.

Attribute in context definition that's the source of context hydration.

**Field Type**
string

**Description**
Name of the parent context attribute hydration detail that's used to derive the current
context attribute.


Metadata Types ContextDefinition

ContextNodeAttrDictionary

Represents the relationship between a context node and the context attribute dictionary.

**Field Name** **Description**

```
contextAttrDictIdentifier

contextNodeTagPrefix

```

ContextNode

**Field Type**
string

**Description**

Required.

Developer name of the context attribute dictionary.

**Field Type**
string

**Description**

Required.

Tag prefix of the context node that's used to create the unique identifier of the parent
context node.

Represents details of the structure of the nodes within the context. Each node can have other nodes related to them and attributes to
describe the object. You can also define a hierarchy for the nodes.

**Field Name** **Description**

```
canonicalNode

contextAttributes

contextNodeAttrDictionaries

contextTags

```

**Field Type**
string

**Description**
Canonical node that's associated with the context node.

**Field Type**

ContextAttribute[]

**Description**
Details of the attribute used to describe the context node.

**Field Type**

ContextNodeAttrDictionary[]

**Description**
Facilitates relationships between context node and context dictionary. Additionally,
it records the relationship between context node and context dictionary.

**Field Type**

ContextTag[]


Metadata Types ContextDefinition

**Field Name** **Description**

**Description**
Unique identifier of the attribute or node.

```
displayName

inheritedFrom

title

transposable

```

ContextAttribute

**Field Type**
string

**Description**
Display name of the context node.

**Field Type**
string

**Description**
Name of the parent context node that's used to derive the current context node.

**Field Type**
string

**Description**

Required.

Name of the context node.

**Field Type**
boolean

**Description**
Indicates whether the data in the Context Node record can be converted to field names
( `true` ) or not ( `false` ).

The default value is `false` .

Represents details of an attribute used to describe a context node. Each node can have one or many associated attributes.

**Field Name** **Description**

```
contextTags

dataType

```

**Field Type**

ContextTag[]

**Description**
Shortened name of the attribute or node.

**Field Type**
ContextAttributeDataType (enumeration of type string)

**Description**

Required.


Metadata Types ContextDefinition

**Field Name** **Description**

Type of data that's stored in the context attribute.

Valid values are:

**•** `boolean`

**•** `currency`

**•** `date`

**•** `datetime`

**•** `number`

**•** `percent`

**•** `picklist`

**•** `reference`

**•** `string`

**•** `selfreference` —Available in API version 63.0 and later.

```
description

displayName

domainSet

fieldType

```

**Field Type**
string

**Description**
Description of the context attribute.

**Field Type**
string

**Description**
Display name of the context attribute.

**Field Type**
string

**Description**
List of node references to show the parent-child relationship between the nodes in a
definition.

**Field Type**
ContextAttributeFieldType (enumeration of type string)

**Description**

Required.

List of node references to depict the parent-child relation between the nodes in a
definition.

Valid values are:

**•** `aggregate`

**•** `input`

**•** `inputoutput`

**•** `output`


Metadata Types ContextDefinition

**Field Name** **Description**

```
inheritedFrom

key

title

transient

value

```

ContextTag

**Field Type**
string

**Description**
Name of the parent attribute that's used to derive the current attribute.

**Field Type**
boolean

**Description**
Indicates whether the attribute is a key attribute in the node ( `true` ) or not ( `false` ).

The default value is `false` .

**Field Type**
string

**Description**

Required.

Name of the context attribute.

**Field Type**
boolean

**Description**
Indicates if an attribute is skipped in context persistence ( `true` ) or not ( `false` ).
Available in API version 63.0 and later.

The default value is `false` .

**Field Type**
boolean

**Description**
Indicates whether the attribute identifies as a value in a node ( `true` ) or not ( `false` ).

The default value is `false` .

Represents a unique identifier of an attribute or node instead of a fully qualified tag structure name.

**Field Name** **Description**

```
title

```

**Field Type**
string

**Description**

Required.


Metadata Types ContextDefinition

**Field Name** **Description**

Name of the context tag.

```
inheritedFrom

```

**Field Type**
string

**Description**
Name of the parent context tag that's used to derive the current context tag.

Declarative Metadata Sample Definition

The following is an example of a ContextDefinition component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ContextDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

   <fullName>Test</fullName>

   <contextDefinitionVersions>

     <contextMappings>

        <contextNodeMappings>

          <contextNodeAttrDictionaries>

            <contextAttrDictIdentifier>Context Attribute Dictionary

Name</contextAttrDictIdentifier>

            <contextNodeTagPrefix>Context Node Tag Prefix</contextNodeTagPrefix>

          </contextNodeAttrDictionaries>

          <contextAttributeMappings>

            <contextAttrHydrationDetails>

               <objectName>CustomAccount__c</objectName>

               <queryAttribute>Name</queryAttribute>

<inheritedFrom>StandardDefinition/version/CustomAccountMapping/Praneeth/AccountName/hydrationInfo-1</inheritedFrom>

            </contextAttrHydrationDetails>

            <ctxAttrHydrationCtxs>

               <contextQueryAttribute>StandardDefinition</contextQueryAttribute>

<inheritedFrom>StandardDefinition/version/AccountMapping/Praneeth/AccountName/ctxToCtxhydrationInfo-1</inheritedFrom>

            </ctxAttrHydrationCtxs>

            <contextAttribute>AccountName</contextAttribute>

            <contextInputAttributeName>AccountName</contextInputAttributeName>

<inheritedFrom>StandardDefinition/version/CustomAccountMapping/Praneeth/AccountName</inheritedFrom>

          </contextAttributeMappings>

          <contextAttributeMappings>

            <contextAttrHydrationDetails>

               <objectName>CustomAccount__c</objectName>

               <queryAttribute>CustomAccountName__c</queryAttribute>

<inheritedFrom>StandardDefinition/version/CustomAccountMapping/Praneeth/CustomAccountName/hydrationInfo-1</inheritedFrom>

```


Metadata Types ContextDefinition

```
               </contextAttrHydrationDetails>

               <ctxAttrHydrationCtxs>

                  <contextQueryAttribute>StandardDefinition</contextQueryAttribute>

   <inheritedFrom>StandardDefinition/version/AccountMapping/Praneeth/AccountName/ctxToCtxhydrationInfo-1</inheritedFrom>

               </ctxAttrHydrationCtxs>

               <contextAttribute>CustomAccountName</contextAttribute>

             <contextInputAttributeName>CustomAccountName</contextInputAttributeName>

   <inheritedFrom>StandardDefinition/version/CustomAccountMapping/Praneeth/CustomAccountName</inheritedFrom>

             </contextAttributeMappings>

             <contextNode>Praneeth</contextNode>

             <object>CustomAccount__c</object>

   <inheritedFrom>StandardDefinition/version/CustomAccountMapping/Praneeth</inheritedFrom>

            <mappedContextDefinition>CustomContextDefinition</mappedContextDefinition>

           </contextNodeMappings>

           <contextMappingIntents>

             <mappingIntent>hydration</mappingIntent>

           </contextMappingIntents>

           <default>true</default>

           <title>CustomAccountMapping</title>

          <inheritedFrom>StandardDefinition/version/CustomAccountMapping</inheritedFrom>

        </contextMappings>

        <contextMappings>

           <contextNodeMappings>

             <contextNodeAttrDictionaries>

               <contextAttrDictIdentifier>Context Attribute Dictionary

   Name</contextAttrDictIdentifier>

               <contextNodeTagPrefix>Context Node Tag Prefix</contextNodeTagPrefix>

             </contextNodeAttrDictionaries>

             <contextAttributeMappings>

               <contextAttrHydrationDetails>

                  <objectName>Account</objectName>

                  <queryAttribute>Name</queryAttribute>

   <inheritedFrom>StandardDefinition/version/AccountMapping/Praneeth/CustomAccountName/AccountName/hydrationInfo-1</inheritedFrom>

               </contextAttrHydrationDetails>

               <ctxAttrHydrationCtxs>

                  <contextQueryAttribute>StandardDefinition</contextQueryAttribute>

   <inheritedFrom>StandardDefinition/version/AccountMapping/Praneeth/AccountName/ctxToCtxhydrationInfo-1</inheritedFrom>

               </ctxAttrHydrationCtxs>

               <contextAttribute>AccountName</contextAttribute>

               <contextInputAttributeName>AccountName</contextInputAttributeName>

```


Metadata Types ContextDefinition

```
   <inheritedFrom>StandardDefinition/version/AccountMapping/Praneeth/CustomAccountName/AccountName</inheritedFrom>

             </contextAttributeMappings>

             <contextAttributeMappings>

               <contextAttrHydrationDetails>

                  <objectName>Account</objectName>

                  <queryAttribute>CustomAccountName__c</queryAttribute>

   <inheritedFrom>StandardDefinition/version/AccountMapping/Praneeth/CustomAccountName/hydrationInfo-1</inheritedFrom>

               </contextAttrHydrationDetails>

               <ctxAttrHydrationCtxs>

                  <contextQueryAttribute>StandardDefinition</contextQueryAttribute>

   <inheritedFrom>StandardDefinition/version/AccountMapping/Praneeth/AccountName/ctxToCtxhydrationInfo-1</inheritedFrom>

               </ctxAttrHydrationCtxs>

               <contextAttribute>CustomAccountName</contextAttribute>

             <contextInputAttributeName>CustomAccountName</contextInputAttributeName>

   <inheritedFrom>StandardDefinition/version/AccountMapping/Praneeth/CustomAccountName</inheritedFrom>

             </contextAttributeMappings>

             <contextNode>Praneeth</contextNode>

             <object>Account</object>

   <inheritedFrom>StandardDefinition/version/AccountMapping/Praneeth</inheritedFrom>

            <mappedContextDefinition>CustomContextDefinition</mappedContextDefinition>

           </contextNodeMappings>

           <contextMappingIntents>

             <mappingIntent>persistence</mappingIntent>

           </contextMappingIntents>

           <description>Account Mapping</description>

           <default>false</default>

           <title>AccountMapping</title>

           <inheritedFrom>StandardDefinition/version/AccountMapping</inheritedFrom>

        </contextMappings>

        <contextNodes>

           <contextNodeAttrDictionaries>

             <contextAttrDictIdentifier>Context Attribute Dictionary

   Name</contextAttrDictIdentifier>

             <contextNodeTagPrefix>Context Node Tag Prefix</contextNodeTagPrefix>

           </contextNodeAttrDictionaries>

           <contextAttributes>

             <contextTags>

               <title>AccountName</title>

   <inheritedFrom>StandardDefinition/version/Praneeth/AccountName/AccountName</inheritedFrom>

             </contextTags>

```


Metadata Types ContextDefinition

```
             <dataType>string</dataType>

             <fieldType>inputoutput</fieldType>

             <key>false</key>

             <title>AccountName</title>

             <displayName>AccountName</displayName>

             <description>Test Description</description>

             <value>false</value>

   <inheritedFrom>StandardDefinition/version/Praneeth/AccountName</inheritedFrom>

           </contextAttributes>

           <contextAttributes>

             <dataType>string</dataType>

             <fieldType>inputoutput</fieldType>

             <key>false</key>

             <title>CustomAccountName</title>

             <value>false</value>

             <displayName>CustomAccountName</displayName>

             <description>Test Description</description>

   <inheritedFrom>StandardDefinition/version/Praneeth/CustomAccountName</inheritedFrom>

           </contextAttributes>

           <contextTags>

             <title>Praneeth</title>

            <inheritedFrom>StandardDefinition/version/Praneeth/Praneeth</inheritedFrom>

           </contextTags>

           <title>Praneeth</title>

           <transposable>false</transposable>

           <inheritedFrom>StandardDefinition/version/Praneeth</inheritedFrom>

           <canonicalNode></canonicalNode>

           <displayName>Praneeth</displayName>

        </contextNodes>

        <endDate>2097-05-10 00:00:00</endDate>

        <startDate>2023-05-10 00:00:00</startDate>

        <versionNumber>1</versionNumber>

        <isActive>true</isActive>

      </contextDefinitionVersions>

      <description>Test Description</description>

      <contextTtl>10</contextTtl>

      <inheritedFrom>StandardDefinition</inheritedFrom>

      <inheritedFromVersion>1.0</inheritedFromVersion>

      <clonedFrom>OriginalDefinition</clonedFrom>

      <isProtected>false</isProtected>

      <masterLabel>Test Label</masterLabel>

      <title>TestTitle</title>

      <displayName>TestTitle</displayName>

   </ContextDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Test</members>

        <name>ContextDefinition</name>

      </types>

```


### Metadata Types ConversationMessageDefinition

```
      <types>

        <members>Account.CustomAccountName__c</members>

        <name>CustomField</name>

      </types>

      <types>

        <members>CustomAccount__c</members>

        <name>CustomObject</name>

      </types>

      <version>64.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### ConversationMessageDefinition

Represents a messaging component in an Enhanced Messaging channel or Messaging for In-App and Web session.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

### ConversationMessageDefinition components have the suffix .conversationMessageDefinition and are

stored in the `conversationMessageDefinitions` folder.

Version

### ConversationMessageDefinition is supported for use in enhanced Messaging channels and Messaging for In-App and

Web, and is available in API version 59.0 and later.

Fields

**Field Name** **Description**

```
constants

```

contentCategory

**Field Type**

ConversationMessageConstant[]

**Description**
An array of constants that defines the messaging components. Constants support
multiple data types, including text, URL, and image.

**Field Type**
ConversationMessageContentCategory (enumeration of type string)


Metadata Types ConversationMessageDefinition

**Field Name** **Description**

**Description**
Specifies the business intent of the Conversation Message Definition. Valid values are:

**•** `AccountUpdate`

**•** `Authentication`

**•** `Feedback`

**•** `OrderUpdate`

**•** `PromotionalOutreach`

**•** `Reminder`

**•** `Response`

```
description

label

language

messageHandlers

messageLayouts

optionsParameter

```

**Field Type**
string

**Description**
The description of the conversation message definition.

**Field Type**
string

**Description**
A user-friendly name for `ConversationMessageDefinition`, which is defined
when `ConversationMessageDefinition` is created.

**Field Type**
string

**Description**
The language of the conversation message definition.

**Field Type**

ConversationMessageHandler[]

**Description**
An array of message handlers.

**Field Type**

ConversationMessageLayout[]

**Description**
An array of message layouts.

**Field Type**

ConversationMessageOptionsParameter[]

**Description**
An array of options parameter of the `ConversationMessageDefinition` .


Metadata Types ConversationMessageDefinition

**Field Name** **Description**

```
parameters

type

```

**Field Type**

ConversationMessageParameter[]

**Description**
An array of parameters.

**Field Type**
ConversationMessageDefinitionType (enumeration of type string)

**Description**

Required. The type of the conversation message definition. Valid values are:

**•** `Action`

**•** `ApexForm`

**•** `AuthenticationRequest`

**•** `AutoResponse`

**•** `Link`

**•** `Notification`

**•** `PaymentRequest`

**•** `Picklist`

**•** `RecordPicker`

**•** `RecordView`

**•** `TimePicker`

ConversationMessageConstant

Represents a constant value on the messaging component. When a messaging component is created in the UI, the text and images
entered during creation are saved as standard constants. Custom constants can also be added.

**Field Name** **Description**

```
compositeValues

constantType

```

**Field Type**

ConversationMessageConstantCompositeValue[]

**Description**
An array of composite values of `ConversationMessageConstant` .

**Field Type**
ConversationMessageConstantType (enumeration of type string)

**Description**

Required. The conversation message constant type. Valid values are:

**•** `Custom`

**•** `Image`


Metadata Types ConversationMessageDefinition

**Field Name** **Description**

**•** `Options`

**•** `SubTitle`

**•** `Title`

**•** `Url`

```
label

name

primitiveValues

valueType

```

**Field Type**
string

**Description**
The UI label of the conversation message constant.

**Field Type**
string

**Description**
The name of the conversation message constant.

**Field Type**

ConversationMessageConstantPrimitiveValue (enumeration of type string)

**Description**
An array of primitive values of `ConversationMessageConstant` .

**Field Type**
ConversationMessageValueType (enumeration of type string)

**Description**

The type of the conversation message constant value. Valid values are:

**•** `Boolean`

**•** `Date`

**•** `DateTime`

**•** `Double`

**•** `ImageId`

**•** `Integer`

**•** `RecordId`

**•** `Text`

**•** `Url`

ConversationMessageConstantCompositeValue

Represents the composite values of the ConversationMessageConstant.


Metadata Types ConversationMessageDefinition

**Field Name** **Description**

```
constantItems

identifier

```

**Field Type**

ConversationMessageConstant[]

**Description**
An array of constant items.

**Field Type**
string

**Description**
Required. The client identifier.

ConversationMessageConstantPrimitiveValue

Represents the primitive values of the ConversationMessageConstant.

**Field Name** **Description**

```
contentAssetName

textValue

type

urlValue

```

**Field Type**
string

**Description**
Represents the value for type = ImageAsset

**Field Type**
string

**Description**
Represents the value for type = Text

**Field Type**
ConversationMessageConstantValueType (enumeration of type string)

**Description**

Required. The type of the conversation message constant primitive value. Valid values
are:

**•** `FileAsset`

**•** `ImageAsset`

**•** `Text`

**•** `Url`

**Field Type**
string

**Description**
Represents the value for type = Url


Metadata Types ConversationMessageDefinition

ConversationMessageHandler

Represents the conversation message handler.

**Field Name** **Description**

```
activeRequestDurationMinutes

handlerName

handlerType

```

**Field Type**
int

**Description**
Required. The duration of an active request in minutes.

**Field Type**
string

**Description**
Required. The name of the message handler.

**Field Type**
ConversationMessageHandlerType (enumeration of type string)

**Description**

Required. The type of message handler. Valid values are:

**•** `ApexFormProvider` . Available in API version 65.0 and later.

**•** `AuthProvider`

**•** `PaymentProvider`

**•** `QuickAction`

**•** `Survey` . Available in API version 65.0 and later.

ConversationMessageLayout

Represents the conversation message layout.

**Field Name** **Description**

```
externalTemplates

formatType

```

**Field Type**

ConvMsgExternalTemplateVersion[]

**Description**
The external template version of the `ConversationMessageLayout` .

**Field Type**
ConversationMessageFormatType (enumeration of type string)

**Description**

Required. The format type of the conversation message layout. Valid values are:

**•** `Application`

**•** `Buttons`


Metadata Types ConversationMessageDefinition

**Field Name** **Description**

**•** `Carousel`

**•** `EncryptedOAuthToken`

**•** `ExternalTemplate`

**•** `Flow`

**•** `Inputs`

**•** `ListPicker`

**•** `Media`

**•** `Payment`

**•** `QuickReplies`

**•** `RichLink`

**•** `Text`

**•** `TimePicker`

**•** `WebView`

```
layoutItems

messageType

```

**Field Type**

ConversationMessageLayoutItem[]

**Description**
An array of layout items.

**Field Type**
ConversationMessageType (enumeration of type string)

**Description**

Required. The conversation message type. Valid values are:

**•** `AuthenticationRequest`

**•** `Choices`

**•** `Form`

**•** `PaymentRequest`

**•** `StaticContent`

ConvMsgExternalTemplateVersion

Represents the external template version of the conversation message layout.

**Field Name** **Description**

```
accountIdentifier

```

**Field Type**
string

**Description**
Required. The account identifier. For WhatsApp channels, this is the WABA ID.


Metadata Types ConversationMessageDefinition

**Field Name** **Description**

```
accountName

language

status

templateName

templateVersionIdentifier

```

**Field Type**
string

**Description**
Required. The account name.

**Field Type**
string

**Description**
Required. The language of the conversation message external template.

**Field Type**
ConvMsgExternalTemplateVersionStatus (enumeration of type string)

**Description**

Required. The status of the conversation message external template. Valid values are:

**•** `Approved` . The template version is approved.

**•** `Blocked` . The template version is blocked. Available in API version 65.0 and later.

**•** `Deleted` . The template version is deleted. Available in API version 65.0 and later.

**•** `Disabled` . The template version is disabled because of recurring negative
customer feedback.

**•** `InAppeal` . The rejected template version is being appealed. Available in API
version 65.0 and later.

**•** `LimitExceeded` . Available in API version 65.0 and later.

**•** `OutOfSync` . The template versions in the messaging service and Salesforce are
out of sync. Available in API version 65.0 and later.

**•** `Paused` . The template version is paused because of recurring negative customer
feedback or low read rates.

**•** `Pending` . The template version awaits Meta's approval.

**•** `PendingDeletion` . The template version is pending deletion. Available in
API version 65.0 and later.

**•** `Rejected` . The template version was rejected during Meta’s review process.

**Field Type**
string

**Description**
Required. The name of the conversation message external template.

**Field Type**
string

**Description**
Required. The template version identifier.


Metadata Types ConversationMessageDefinition

ConversationMessageLayoutItem

Represents the conversation message layout item.

**Field Name** **Description**

```
collectionType

compositeValues

name

primitiveValues

```

**Field Type**
ConversationMessageCollectionType (enumeration of type string)

**Description**

Required. The type of conversation message collection. Valid values are:

**•** `DynamicList`

**•** `None`

**•** `StaticList`

**Field Type**

ConversationMessageLayoutCompositeValue[]

**Description**
An array of composite values of the `ConversationMessageLayoutItem` .

**Field Type**
string

**Description**
The name of the conversation message layout item.

**Field Type**

ConversationMessageLayoutPrimitiveValue[]

**Description**
An array of primitive values of the `ConversationMessageLayoutItem` .

ConversationMessageLayoutCompositeValue

Represents the composite value of the ConversationMessageLayoutItem.

**Field Name** **Description**

```
compositeTypeName

layoutItems

```

**Field Type**
string

**Description**
Required. The name of the conversation message layout composite value type.

**Field Type**

ConversationMessageLayoutItem[]

**Description**
An array of layout items.


Metadata Types ConversationMessageDefinition

**Field Name** **Description**

```
valueSourceReference

```

**Field Type**
string

**Description**
The source of the conversation message layout composite value.

ConversationMessageLayoutPrimitiveValue

Represents the primitive value of the ConversationMessageLayoutItem.

**Field Name** **Description**

```
contentAssetName

fieldName

formulaTemplate

literalValue

mergeFields

type

```

**Field Type**
string

**Description**
The content asset name.

**Field Type**
string

**Description**
The name of the conversation message layout primitive value field.

**Field Type**
string

**Description**
The formula template defines the content for each entry in the list.

**Field Type**
string

**Description**
The literal primitive value of the conversation message layout.

**Field Type**

ConversationMessageMergeField[]

**Description**
Inserts multiple values to a list.

**Field Type**
ConversationMessageLayoutValueType (enumeration of type string)

**Description**

Required. The type of the conversation message layout primitive value. Valid values
are:


Metadata Types ConversationMessageDefinition

**Field Name** **Description**

**•** `FormulaTemplate`

**•** `Literal`

**•** `MediaAsset`

**•** `SourcePrimitiveValue`

**•** `SourceSobjectField`

**•** `SourceSobjectFieldValue`

**•** `SourceSobjectFormula`

```
valueFormula

valueSourceReference

```

**Field Type**
string

**Description**
The formula of the conversation message layout primitive value.

**Field Type**
string

**Description**
The source of the conversation message layout primitive value.

ConversationMessageMergeField

Merge field is used to insert multiple values to a list.

**Field Name** **Description**

```
formulaTemplate

mergeFieldType

name

valueSourceReference

```

**Field Type**
string

**Description**
Required. The formula template of the conversation message merge field.

**Field Type**
ConversationMessageMergeFieldType (enumeration of type string)

**Description**
Required. The type of the conversation message merge field. Valid value is ListTemplate.

**Field Type**
string

**Description**
Required. The name of the conversation message merge field.

**Field Type**
string


Metadata Types ConversationMessageDefinition

**Field Name** **Description**

**Description**
Required. The source of the conversation message merge field value.

ConversationMessageOptionsParameter

Represents a conversation message options parameter.

**Field Name** **Description**

```
compositeTypeDetails

optionsParameterType

primitiveTypeDetails

```

**Field Type**

ConversationMessageParameterCompositeDetails[]

**Description**
An array of composite details of `ConversationMessageOptionsParameter` .

**Field Type**
ConversationMessageOptionsParameterType (enumeration of type string)

**Description**

Required. The type of conversation message options parameter. Valid values are:

**•** `CustomCompositeOptions`

**•** `CustomPrimitiveOptions`

**•** `RecordIdOptions`

**•** `TimeSlotOptions`

**Field Type**
ConversationMessageParameterPrimitiveDetails

**Description**
The primitive type details of conversation message options parameter.

ConversationMessageParameterCompositeDetails

Represents the composite details of a conversation message parameter.

**Field Name** **Description**

```
compositeChildItems

isList

```

**Field Type**
ConversationMessageParameterCompositeDetails[]

**Description**
The composite child items of the conversation message parameter.

**Field Type**
boolean


Metadata Types ConversationMessageDefinition

**Field Name** **Description**

**Description**
Indicates whether the conversation message parameter composite details field is a
list item ( `true` ) or not ( `false` ). The default value is false.

```
isRequired

label

maxListItems

name

primitiveChildItems

```

**Field Type**
boolean

**Description**
Indicates whether the conversation message parameter is required ( `true` ) or not
( `false` ). The default value is false.

**Field Type**
string

**Description**
The UI label of the conversation message parameter composite details field.

**Field Type**
int

**Description**
The maximum number of list items in the conversation message parameter composite
details field.

**Field Type**
string

**Description**
The name of the conversation message parameter composite details field.

**Field Type**

ConversationMessageParameterPrimitiveDetails[]

**Description**
An array of primitive child items.

ConversationMessageParameterPrimitiveDetails

Represents the primitive details of the conversation message parameter.

**Field Name** **Description**

```
isList

```

**Field Type**
boolean

**Description**
Indicates whether the conversation message parameter primitive details field is a list
item ( `true` ) or not ( `false` ). The default value is false.


Metadata Types ConversationMessageDefinition

**Field Name** **Description**

```
isRequired

label

maxListItems

name

sobjectType

valueType

```

**Field Type**
boolean

**Description**
Indicates whether the conversation message parameter primitive details field is required
( `true` ) or not ( `false` ). The default value is false.

**Field Type**
string

**Description**
The UI label of the conversation message parameter primitive details field.

**Field Type**
int

**Description**
The maximum number of list items that are allowed in the conversation message
parameter primitive details field.

**Field Type**
string

**Description**
The name of the conversation message parameter primitive details field.

**Field Type**
string

**Description**
The sObject type.

**Field Type**
ConversationMessageValueType (enumeration of type string)

**Description**

The type of the conversation message parameter value. Valid values are:

**•** `Boolean`

**•** `Date`

**•** `DateTime`

**•** `Double`

**•** `ImageId`

**•** `Integer`

**•** `RecordId`

**•** `Text`

**•** `Url`


Metadata Types ConversationMessageDefinition

ConversationMessageParameter

Represents a conversation message parameter.

**Field Name** **Description**

```
compositeTypeDetails

parameterType

primitiveTypeDetails

```

**Field Type**

ConversationMessageParameterCompositeDetails

**Description**
An array of composite type details.

**Field Type**
ConversationMessageParameterType (enumeration of type string)

**Description**

Required. The type of conversation message parameter. Valid values are:

**•** `CustomComposite`

**•** `CustomPrimitive`

**•** `RecordIds`

**Field Type**

ConversationMessageParameterPrimitiveDetails

**Description**
An array of primitive type details.

Declarative Metadata Sample Definition

The following is an example of a `ConversationMessageDefinition` component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ConversationMessageDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

   <constants>

     <constantType>Custom</constantType>

     <label>imageAsset</label>

     <name>imageAsset</name>

     <primitiveValues>

        <contentAssetName>Screenshot_20240402_at_32437PM</contentAssetName>

        <type>ImageAsset</type>

     </primitiveValues>

     <valueType>ImageId</valueType>

   </constants>

   <constants>

     <constantType>Custom</constantType>

     <label>message</label>

     <name>message</name>

     <primitiveValues>

        <textValue>Favourite Season</textValue>

        <type>Text</type>

     </primitiveValues>

```


Metadata Types ConversationMessageDefinition

```
        <valueType>Text</valueType>

      </constants>

      <constants>

        <constantType>Custom</constantType>

        <label>Prompt1</label>

        <name>Prompt1</name>

        <primitiveValues>

           <textValue>Choose one option</textValue>

           <type>Text</type>

        </primitiveValues>

        <valueType>Text</valueType>

      </constants>

      <constants>

        <compositeValues>

           <constantItems>

             <constantType>Image</constantType>

             <primitiveValues>

               <contentAssetName>Screenshot_20240321_at_53957PM3</contentAssetName>

               <type>ImageAsset</type>

             </primitiveValues>

           </constantItems>

           <constantItems>

             <constantType>SubTitle</constantType>

             <primitiveValues>

               <textValue>January</textValue>

               <type>Text</type>

             </primitiveValues>

           </constantItems>

           <constantItems>

             <constantType>Title</constantType>

             <primitiveValues>

               <textValue>Jan</textValue>

               <type>Text</type>

             </primitiveValues>

           </constantItems>

           <identifier>1c6f8c4d-7bce-1649-fa45-db587bcfbb29</identifier>

        </compositeValues>

        <compositeValues>

           <constantItems>

             <constantType>Image</constantType>

             <primitiveValues>

               <contentAssetName>Screenshot_20240321_at_53957PM4</contentAssetName>

               <type>ImageAsset</type>

             </primitiveValues>

           </constantItems>

           <constantItems>

             <constantType>SubTitle</constantType>

             <primitiveValues>

               <textValue>December</textValue>

               <type>Text</type>

             </primitiveValues>

           </constantItems>

           <constantItems>

             <constantType>Title</constantType>

```


Metadata Types ConversationMessageDefinition

```
             <primitiveValues>

               <textValue>Dec</textValue>

               <type>Text</type>

             </primitiveValues>

           </constantItems>

           <identifier>fb8bb328-7bc7-2830-6194-2ae7ece055ad</identifier>

        </compositeValues>

        <compositeValues>

           <constantItems>

             <constantType>Image</constantType>

             <primitiveValues>

               <contentAssetName>Screenshot_20240321_at_53912PM1</contentAssetName>

               <type>ImageAsset</type>

             </primitiveValues>

           </constantItems>

           <constantItems>

             <constantType>SubTitle</constantType>

             <primitiveValues>

               <textValue>March</textValue>

               <type>Text</type>

             </primitiveValues>

           </constantItems>

           <constantItems>

             <constantType>Title</constantType>

             <primitiveValues>

               <textValue>March</textValue>

               <type>Text</type>

             </primitiveValues>

           </constantItems>

           <identifier>570baa88-fa4d-4b31-0e84-92f87b35af0a</identifier>

        </compositeValues>

        <constantType>Options</constantType>

      </constants>

      <constants>

        <constantType>Title</constantType>

        <primitiveValues>

           <textValue>What is your favourite month?</textValue>

           <type>Text</type>

        </primitiveValues>

      </constants>

      <label>Favourite Month</label>

      <language>en_US</language>

      <messageLayouts>

        <formatType>Buttons</formatType>

        <layoutItems>

           <collectionType>DynamicList</collectionType>

           <compositeValues>

             <compositeTypeName>TitleOptionItem</compositeTypeName>

             <layoutItems>

               <collectionType>None</collectionType>

               <compositeValues>

                  <compositeTypeName>TitleItem</compositeTypeName>

                  <layoutItems>

                    <collectionType>None</collectionType>

```


Metadata Types ConversationMessageDefinition

```
                    <name>title</name>

                    <primitiveValues>

                       <type>SourcePrimitiveValue</type>

   <valueSourceReference>Constants.Options.ListItem.SubTitle</valueSourceReference>

                    </primitiveValues>

                  </layoutItems>

               </compositeValues>

               <name>titleItem</name>

             </layoutItems>

             <valueSourceReference>Constants.Options</valueSourceReference>

           </compositeValues>

           <name>optionItems</name>

        </layoutItems>

        <layoutItems>

           <collectionType>None</collectionType>

           <name>text</name>

           <primitiveValues>

             <type>SourcePrimitiveValue</type>

             <valueSourceReference>Constants.Title</valueSourceReference>

           </primitiveValues>

        </layoutItems>

        <messageType>Choices</messageType>

      </messageLayouts>

      <messageLayouts>

        <formatType>ListPicker</formatType>

        <layoutItems>

           <collectionType>None</collectionType>

           <compositeValues>

             <compositeTypeName>TitleImageItem</compositeTypeName>

             <layoutItems>

               <collectionType>None</collectionType>

               <name>imageId</name>

               <primitiveValues>

                  <type>SourcePrimitiveValue</type>

                  <valueSourceReference>Constants.imageAsset</valueSourceReference>

               </primitiveValues>

             </layoutItems>

             <layoutItems>

               <collectionType>None</collectionType>

               <name>title</name>

               <primitiveValues>

                  <type>SourcePrimitiveValue</type>

                  <valueSourceReference>Constants.Title</valueSourceReference>

               </primitiveValues>

             </layoutItems>

           </compositeValues>

           <name>message</name>

        </layoutItems>

        <layoutItems>

           <collectionType>DynamicList</collectionType>

           <compositeValues>

             <compositeTypeName>TitleOptionItem</compositeTypeName>

```


Metadata Types ConversationMessageDefinition

```
             <layoutItems>

               <collectionType>None</collectionType>

               <compositeValues>

                  <compositeTypeName>TitleImageItem</compositeTypeName>

                  <layoutItems>

                    <collectionType>None</collectionType>

                    <name>imageId</name>

                    <primitiveValues>

                       <type>SourcePrimitiveValue</type>

   <valueSourceReference>Constants.Options.ListItem.Image</valueSourceReference>

                    </primitiveValues>

                  </layoutItems>

                  <layoutItems>

                    <collectionType>None</collectionType>

                    <name>title</name>

                    <primitiveValues>

                       <type>SourcePrimitiveValue</type>

   <valueSourceReference>Constants.Options.ListItem.Title</valueSourceReference>

                    </primitiveValues>

                  </layoutItems>

               </compositeValues>

               <name>titleItem</name>

             </layoutItems>

             <valueSourceReference>Constants.Options</valueSourceReference>

           </compositeValues>

           <name>optionItems</name>

        </layoutItems>

        <layoutItems>

           <collectionType>None</collectionType>

           <compositeValues>

             <compositeTypeName>TitleImageItem</compositeTypeName>

             <layoutItems>

               <collectionType>None</collectionType>

               <name>imageId</name>

               <primitiveValues>

                  <type>SourcePrimitiveValue</type>

                  <valueSourceReference>Constants.imageAsset</valueSourceReference>

               </primitiveValues>

             </layoutItems>

             <layoutItems>

               <collectionType>None</collectionType>

               <name>title</name>

               <primitiveValues>

                  <type>SourcePrimitiveValue</type>

                  <valueSourceReference>Constants.message</valueSourceReference>

               </primitiveValues>

             </layoutItems>

           </compositeValues>

           <name>reply</name>

        </layoutItems>

        <layoutItems>

```


Metadata Types ConversationMessageDefinition

```
           <collectionType>None</collectionType>

           <name>title</name>

           <primitiveValues>

             <type>SourcePrimitiveValue</type>

             <valueSourceReference>Constants.Title</valueSourceReference>

           </primitiveValues>

        </layoutItems>

        <messageType>Choices</messageType>

      </messageLayouts>

      <messageLayouts>

        <formatType>Carousel</formatType>

        <layoutItems>

           <collectionType>DynamicList</collectionType>

           <compositeValues>

             <compositeTypeName>TitleItemWithInteractions</compositeTypeName>

             <layoutItems>

               <collectionType>StaticList</collectionType>

               <compositeValues>

                  <compositeTypeName>TitleOptionItem</compositeTypeName>

                  <layoutItems>

                    <collectionType>None</collectionType>

                    <compositeValues>

                       <compositeTypeName>TitleItem</compositeTypeName>

                       <layoutItems>

                         <collectionType>None</collectionType>

                         <name>title</name>

                         <primitiveValues>

                           <literalValue>Select One</literalValue>

                           <type>Literal</type>

                         </primitiveValues>

                       </layoutItems>

                    </compositeValues>

                    <name>titleItem</name>

                  </layoutItems>

               </compositeValues>

               <name>interactionItems</name>

             </layoutItems>

             <layoutItems>

               <collectionType>None</collectionType>

               <compositeValues>

                  <compositeTypeName>TitleImageItem</compositeTypeName>

                  <layoutItems>

                    <collectionType>None</collectionType>

                    <name>imageId</name>

                    <primitiveValues>

                       <type>SourcePrimitiveValue</type>

   <valueSourceReference>Constants.Options.ListItem.Image</valueSourceReference>

                    </primitiveValues>

                  </layoutItems>

                  <layoutItems>

                    <collectionType>None</collectionType>

                    <name>subTitle</name>

                    <primitiveValues>

```


Metadata Types ConversationMessageDefinition

```
                       <type>SourcePrimitiveValue</type>

   <valueSourceReference>Constants.Options.ListItem.SubTitle</valueSourceReference>

                    </primitiveValues>

                  </layoutItems>

                  <layoutItems>

                    <collectionType>None</collectionType>

                    <name>title</name>

                    <primitiveValues>

                       <type>SourcePrimitiveValue</type>

                     <valueSourceReference>Constants.Title</valueSourceReference>

                    </primitiveValues>

                  </layoutItems>

               </compositeValues>

               <name>titleItem</name>

             </layoutItems>

             <valueSourceReference>Constants.Options</valueSourceReference>

           </compositeValues>

           <name>items</name>

        </layoutItems>

        <messageType>Choices</messageType>

      </messageLayouts>

      <messageLayouts>

        <formatType>Text</formatType>

        <layoutItems>

           <collectionType>None</collectionType>

           <name>text</name>

           <primitiveValues>

             <formulaTemplate>{!$Constants.Title}

   {!$Constants.Prompt1}:

   {!$ListTemplates.OptionsList}</formulaTemplate>

             <mergeFields>

               <formulaTemplate>{!$ListItem.Index}.

   {!$ListItem.Value.Title}{!BR()}</formulaTemplate>

               <mergeFieldType>ListTemplate</mergeFieldType>

               <name>OptionsList</name>

               <valueSourceReference>Constants.Options</valueSourceReference>

             </mergeFields>

             <type>FormulaTemplate</type>

           </primitiveValues>

        </layoutItems>

        <messageType>StaticContent</messageType>

      </messageLayouts>

      <type>Picklist</type>

   </ConversationMessageDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Favourite_Month</members>

        <name>ConversationMessageDefinition</name>

      </types>

```


### Metadata Types ConversationMessageDefinitionTranslation

```
      <version>61.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### ConversationMessageDefinitionTranslation

Represents translated labels and constant values for conversation message definitions in Enhanced Messaging and Messaging for In-App
and Web.

Note: This complex type is used as a nested element within the ConversationMessageDefinition metadata type and is not deployed
as a standalone metadata component. It enables multilingual support by allowing constant values and labels to be translated into
different languages for customer-facing messaging.

Parent Type

This type is used as a nested complex type within the ConversationMessageDefinition on page 665 metadata type.

Version

### ConversationMessageDefinitionTranslation is available in API version 61.0 and later.

Fields


Metadata Types ConversationMessageDefinitionTranslation

ConversationMessageConstantValueTranslation

Represents a translated constant value for conversation message definitions. Available in API version 61.0 and later.

Usage Example

This complex type is used within ConversationMessageDefinition to provide translations. Here's an example context:

```
<?xml version="1.0" encoding="UTF-8"?>

<ConversationMessageDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

   <fullName>Welcome_Message</fullName>

   <label>Welcome Message</label>

   <conversationMessageDefinitionTranslations>

     <constantValueTranslations>

        <name>greeting_text</name>

        <value>Bienvenido</value>

     </constantValueTranslations>

     <label>Mensaje de Bienvenida</label>

     <name>Welcome_Message</name>

   </conversationMessageDefinitionTranslations>

</ConversationMessageDefinition>

```


### Metadata Types ConversationVendorInfo ConversationVendorInfo

Represents the connection between the partner vendor system and the Service Cloud feature. For example, for Service Cloud Voice, this
type contains information about the partner telephony system or Contact Center as a Service (CCaaS) system. For Bring Your Own
Channel for Messaging or Bring Your Own Channel for CCaaS, this type contains information about the partner messaging system or
CCaaS system.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ConversationVendorInfo components have the suffix .ConversationVendorInformation and are stored in the ConversationVendorInformation folder.

Version

### ConversationVendorInfo components are available in API version 52.0 and later.

Special Access Rules

This type requires an add-on license for Service Cloud Voice for Partner Telephony or Digital Engagement.

Fields

The fields in the ConversationVendorInfo type apply to all Service Cloud features unless otherwise stated in the field description. For
example, if a field applies to just one Service Cloud Voice telephony model setup or is applied differently by different partner systems,
this is stated in the field description.

**Field Name** **Description**

```
agentSSOSupported

```

**Field Type**
boolean

**Description**
If set to `true`, agents can single sign-on (SSO) into their contact center using Salesforce
as the identity provider (IdP). Behind the scenes, Salesforce is used as the SAML IdP in
the Single Sign-On external client app for the contact center. If set to `false`, an IdP
other than Salesforce is used or an IdP isn’t used at all. The default value is `false` .

If this value is set to `false` and you want to use Salesforce as the IdP for your contact
center, set this value and the `namedCredentialSupported` value to `true`
and configure the `service_cloud_voice.PartnerSSO` interface in your
Apex integration class.


Metadata Types ConversationVendorInfo

**Field Name** **Description**

Available in API version 53.0 and later.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

**•** Bring Your Own Channel for CCaaS

```
awsAccountKey

awsRootEmail

awsTenantVersion

bridgeComponent

```

**Field Type**
string

**Description**
The 12-digit AWS subaccount ID that’s automatically provisioned for you when Service
Cloud Voice was turned on. Available in API version 55.0 and later.

Applies to the following implementation:

**•** Service Cloud Voice with Amazon Connect

**Field Type**
string

**Description**
The email address used by Salesforce to create the root user for the provisioned AWS
subaccount when Service Cloud Voice was turned on. Available in API version 55.0
and later.

Applies to the following implementation:

**•** Service Cloud Voice with Amazon Connect

**Field Type**
double

**Description**
The version number of the SVCTenantStack AWS CloudFormation stack that’s deployed.
The stack is deployed in AWS region "us-east-1". Available in API version 55.0 and later.

Applies to the following implementation:

**•** Service Cloud Voice with Amazon Connect

**Field Type**
string

**Description**
The Lightning component used to communicate between the telephony or messaging
system and other Lightning components.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

**•** Bring Your Own Channel for CCaaS


Metadata Types ConversationVendorInfo

**Field Name** **Description**

```
clientAuthMode

connectorUrl

customConfig

customIcon

```

**Field Type**
ClientAuthMode (enumeration of type string)

**Description**
The client authentication mode.

Values are:

**•** `Custom`

**•** `Mixed`

**•** `SSO`

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

**Field Type**
string

**Description**
The URL that hosts your Service Cloud Voice or Bring Your Own Channel for CCaaS
connector. This value could be a Visualforce page or a public URL.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

**•** Bring Your Own Channel for CCaaS

**Field Type**
string

**Description**
The foreign key to the CustomEntityDefinition, which contains partner-specific custom
settings. Available in API version 53.0 and later.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

**•** Bring Your Own Channel for CCaaS

**Field Type**
string

**Description**
ID of the static resource used to identify the contact center integration, such as a
Contact Center as a Service (CCaaS) provider logo. The static resource must be in SVG
format. This field is optional. Available in API version 62.0 and later.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony


Metadata Types ConversationVendorInfo

**Field Name** **Description**

**•** Bring Your Own Channel for CCaaS

```
customLoginUrl

developerName

einsteinConversationInsightsSupported

integrationClass

integrationClassName

```

**Field Type**
string

**Description**
The URL that hosts your telephony system or CCaaS system login page.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

**•** Bring Your Own Channel for CCaaS

**Field Type**
string

**Description**
The unique name of the type in the API.

**Field Type**
boolean

**Description**
If set to `true`, Einstein Conversation Insights is turned on. The default value is `false` .
Available in API version 53.0 and later.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

**Field Type**
string

**Description**
The foreign key to the partner Apex class implementing supported interfaces. Available
in API version 53.0 and later.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

**•** Bring Your Own Channel for CCaaS

**Field Type**
string

**Description**
Deprecated in API version 53.0. Don't set this field. Instead, use
`integrationClass` .

Applies to the following implementations:


Metadata Types ConversationVendorInfo

**Field Name** **Description**

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

```
intelligenceSupported

isTaxCompliant

keyProvisioningSupported

masterLabel

```

**Field Type**
boolean

**Description**
If set to `true`, Salesforce ingests real-time signals sent from a partner telephony
system. If set to `false`, Salesforce won't ingest real-time intelligence signals from a
partner telephony system. The default value is `false` . Available in API version 59.0
and later.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**Field Type**
boolean

**Description**
Indicates whether the Amazon tax settings for the AWS subaccount provisioned for
Service Cloud Voice have been confirmed ( `true` ). The default value is `false` .
Available in API version 55.0 and later.

Applies to the following implementation:

**•** Service Cloud Voice with Amazon Connect

**Field Type**
boolean

**Description**
If set to `true`, key provisioning and renewal are automated. The default value is
`false` . Available in API version 54.0 and later.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

**Field Type**
string

**Description**
The partner vendor's display name as it appears in the UI. This name appears in several
places in the UI, so include the partner vendor name for easy identification. For Service
Cloud Voice, this label also represents the telephony provider name in the contact
center record.

For Service Cloud Voice with Amazon Connect, this field is always set to `Service`
`Cloud Voice` .


Metadata Types ConversationVendorInfo

**Field Name** **Description**

```
namedCredential

namedCredentialSupported

partnerContactCenterListSupported

partnerPhoneNumbersSupported

```

**Field Type**
string

**Description**
A sample-named credential that can be used for Apex callouts to the partner system.
Available in API version 53.0 and later.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

**•** Bring Your Own Channel for CCaaS

**Field Type**
boolean

**Description**
A sample-named credential that can be used for Apex callouts to the partner system.
Available in API version 53.0 and later.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

**•** Bring Your Own Channel for CCaaS

**Field Type**
boolean

**Description**
If set to `true`, enables the customer to select one contact center from a list of multiple
contact centers to connect with Salesforce. The default value is `false` . Available in
API version 53.0 and later.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

**•** Bring Your Own Channel for CCaaS

**Field Type**
boolean

**Description**
If set to `true`, displays a list of phone numbers used to create contact center channels.
The default value is `false` . Available in API version 54.0 and later.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect


Metadata Types ConversationVendorInfo

**Field Name** **Description**

```
partnerTransferDestinationsSupported

queueManagementSupported

serverAuthMode

telephonySettingsComponent

```

**Field Type**
boolean

**Description**
If set to `true`, allows Salesforce to fetch contact center queues so that Salesforce and
contact center queues can be mapped. The default value is `false` . Available in API
version 53.0 and later.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

**•** Bring Your Own Channel for CCaaS

**Field Type**
boolean

**Description**
If set to `true`, support queue management. The default value is `false` . Available
in API version 56.0 and later.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

**•** Bring Your Own Channel for CCaaS

**Field Type**
ServerAuthMode (enumeration of type string)

**Description**
Deprecated in API 53.0. Server authentication mode. Set this value to `None` .

Values are:

**•** `None`

**•** `OAuth`

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

**Field Type**
string

**Description**
The name of the Lightning Web Component (LWC) that is used to display additional
agent settings in the Omni-Channel widget. This value is in the format
`mynamespace:componentName`, where `mynamespace` is the namespace
associated with the Service Cloud Voice package that was created, and
`componentName` is the FQDN of the Lightning component.


Metadata Types ConversationVendorInfo

**Field Name** **Description**

Available in API version 54.0 and later.

Applies to the following implementation:

**•** Service Cloud Voice with Partner Telephony

```
unifiedRoutingSupported

(Beta)

universalCallRecordingAccessSupported

userSyncingSupported

vendorType

```

**Field Type**
boolean

**Description**
Indicates whether unified routing is supported ( `true` ) or not supported ( `false` ) for
voice calls in voice channels. The default value is `false` . Once this value is set to
`true`, it can’t be changed to `false` .

Available in API version 63.0 and later.

Applies to the following implementation:

**•** Service Cloud Voice with Partner Telephony

**Field Type**
boolean

**Description**
If set to `true`, Universal Call Recording Access is turned on. The default value is
`false` .

If this value is set to `false` and you want to turn on Universal Call Recording, set
this value to `true` and configure the service_cloud_voice.RecordingMediaProvider
interface in your Apex integration class.

Available in API version 54.0 and later.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

**Field Type**
boolean

**Description**
If set to `true`, supports automated user syncing whenever a user is added to or
removed from a contact center. The default value is `false` . Available in API version
53.0 and later.

Applies to the following implementations:

**•** Service Cloud Voice with Partner Telephony

**•** Service Cloud Voice with Partner Telephony from Amazon Connect

**•** Bring Your Own Channel for CCaaS

**Field Type**
ConversationVendorType (enumeration of type string)


Metadata Types ConversationVendorInfo

**Field Name** **Description**

**Description**
The Service Cloud feature the partner vendor supports.

Possible values are:

**•** `Amazon_Connect`                     - For Service Cloud Voice with Amazon Connect.

**•** `BringYourOwnChannelPartner`                     - For Bring Your Own Channel for
Messaging. Available in API version 60.0 and later.

**•** `BringYourOwnContactCenter`                     - For Bring Your Own Channel for Contact
Center as a Service (CCaaS). Available in API version 60.0 and later.

**•** `ServiceCloudVoicePartner`                     - For Service Cloud Voice with Partner
Telephony or Service Cloud Voice with Partner Telephony from Amazon Connect.

Available in API version 53.0 and later.

Declarative Metadata Sample Definition

The following is an example of a ConversationVendorInfo component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ConversationVendorInfo xmlns="http://soap.sforce.com/2006/04/metadata"

   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

      <einsteinConversationInsightsSupported>true</einsteinConversationInsightsSupported>

      <partnerContactCenterListSupported>true</partnerContactCenterListSupported>

      <namedCredentialSupported>true</namedCredentialSupported>

      <partnerTransferDestinationsSupported>true</partnerTransferDestinationsSupported>

      <agentSSOSupported>true</agentSSOSupported>

      <keyProvisioningSupported>true</keyProvisioningSupported>

      <universalCallRecordingAccessSupported>true</universalCallRecordingAccessSupported>

      <partnerPhoneNumbersSupported>true</partnerPhoneNumbersSupported>

      <queueManagementSupported>true</queueManagementSupported>

      <clientAuthMode>SSO</clientAuthMode>

      <connectorUrl>https://exampleconnectorurl.com</connectorUrl>

      <customConfig>exampleCustomConfig__c</customConfig>

      <customLoginUrl>testurl</customLoginUrl>

      <integrationClass>ExampleIntegrationImpl</integrationClass>

      <masterLabel>Example Partner Name</masterLabel>

      <developerName>exampledevname</developerName>

      <namedCredential>exampleNamedCredential</namedCredential>

      <userSyncingSupported>true</userSyncingSupported>

      <vendorType>BringYourOwnContactCenter</vendorType>

   </ConversationVendorInfo>

```

The following is an example `package.xml` that references the previous definition.

```
   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ConversationVendorInfo</name>

      </types>

```


### Metadata Types ConvIntelligenceSignalRule

```
      <version>59.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### ConvIntelligenceSignalRule

Represents the conversation intelligence signal rule. The rule triggers actions based on real-time intelligence signals from your telephony
system or keywords mentioned by support reps or customers. The rule contains a set of conditions (subrules) and the filter logic used
to evaluate those conditions to determine whether to trigger actions.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ConvIntelligenceSignalRule components have the suffix .ConvIntelligenceSignalRule and are stored in the ConvIntelligenceSignalRule folder.

Version

### ConvIntelligenceSignalRule components are available in API version 62.0 and later.

Special Access Rules

This type requires an add-on license for Service Cloud Voice for Amazon Connect, Service Cloud Voice for Partner Telephony with Amazon
Connect, Service Cloud Voice for Partner Telephony, or Digital Engagement.

Fields

**Field Name** **Description**

```
actionType

```

**Field Type**
ConvIntelligenceActionType (enumeration of type string)

**Description**

Required. The conversation intelligence signal type. Values are:

**•** `AlertSupervisor` –Sends an alert to the supervisor.

**•** `AlertSupervisorAndAgent` –Sends an alert to the rep and supervisor.

**•** `LaunchFlow` –Triggers an auto-launched flow. If set, also set `ActionValue` .


Metadata Types ConvIntelligenceSignalRule

**Field Name** **Description**

**•** `LaunchNBA` –Recommends the next best action to the rep.

```
actionValue

active

channelAddressIdentifier

channelType

criteria

```

**Field Type**
string

**Description**

Action to perform based on the `actionType` specified.

If `actionType` is set to LaunchFlow, this value is the `developerName` of the
flow to be launched. For example, EmailAlert.

For all other `actionType` values, don’t set this parameter.

**Field Type**
boolean

**Description**
Required. Indicates whether the conversation intelligence signal rule is active ( `true` )
or inactive ( `false` ). The default value is `false` .

**Field Type**
string

**Description**

Required. ID ( `ChannelAddressIdentifier` ) of the Messaging channel or name
( `InternalName` ) of the Voice channel.

**Field Type**
string

**Description**

Required. Channel type.

For Messaging, possible values are:

**•** `AppleBusinessChat` —Represents Apple Messages for Business.

**•** `Custom` —Represents Bring Your Own Channel for Messaging or Bring Your Own
Channel for CCaaS.

**•** `EmbeddedMessaging` —Represents Messaging for In-App and Web.

**•** `Facebook`

**•** `Text`

**•** `WhatsApp`

For Voice, set this parameter to `Phone` .

**Field Type**
string


Metadata Types ConvIntelligenceSignalRule

**Field Name** **Description**

**Description**
Required. Filter logic applied to the rule conditions (subrules). For example, ((1 AND
2) OR 3). The numbers in the formula are derived from the
`ConvIntelligenceSignalSubRule.order` value plus 1. For example, filter
logic (1 AND 2) is calculated by adding the first condition ( `order` =0) with the second
condition ( `order` =1).

```
developerName

participantRole

ruleName

service

subrule

```

**Field Type**
string

**Description**
Required. API name of the conversation intelligence signal rule.

**Field Type**
ConvParticipantRole (enumeration of type string)

**Description**
If `service` is set to KeywordMatch, this value determines whether the rule applies
to utterances made by reps, customers, or both roles. Possible values are:

Possible values are:

**•** `Agent`

**•** `AgentOrCustomer`

**•** `Customer`

If `Service` is not set to KeywordMatch, don’t set this parameter.

**Field Type**
string

**Description**
Required. Name of the conversation intelligence signal rule.

**Field Type**
ConvIntelligenceService (enumeration of type string)

**Description**

Required. Salesforce- or partner-provided intelligence source.

For Salesforce-provided intelligence sources, set this parameter to `KeywordMatch` .

For partner-provided intelligence sources, possible values are:

**•** `KeywordMatch`

**•** `AmazonConnectContactLens`

If none of the options apply to you, contact your Salesforce representative for the
service name.

**Field Type**

ConvIntelligenceSignalSubRule[]


Metadata Types ConvIntelligenceSignalRule

**Field Name** **Description**

**Description**
A set of intelligence rules used to measure an agent or customer’s sentiment during
a voice call.

ConvIntelligenceSignalSubRule

Represents a condition (subrule) within a conversation intelligence signal rule.

**Field Name** **Description**

```
operandValue

operator

order

type

```

**Field Type**
string

**Description**

Required. Value of the signal type used to determine if the rule condition is met.

**Field Type**
ConvIntelligenceOperator (enumeration of type string)

**Description**
Required. Filter logic operator used to determine if the rule condition is met. Possible
values are:

**•** `Equals`

**•** `GreaterThan`

**•** `In`

**•** `LessThan`

**•** `NotEquals`

**Field Type**
int

**Description**

Required. Order the condition appears in relation to the other conditions in the list,
with zero (0) being the first condition listed. If `type` is set to Keyword, the maximum
value is 24. For all other `type` values, the maximum value is 4. This value is used when
applying filter logic to the rule.

**Field Type**
ConvIntelligenceType (enumeration of type string)

**Description**

Required. Type of conversation intelligence signal used by the rule to determine
whether to trigger an action. This value depends on the
`ConvIntelligenceSignalRule.channelType` and
`ConvIntelligenceSignalRule.service` values.


Metadata Types ConvIntelligenceSignalRule

**Field Name** **Description**

If `service` is set to KeywordMatch, possible values are:

**•** `Keyword` –A word or group of words spoken or typed.

If `service` is set to `AmazonConnectContactLens`, possible values are:

**•** `Category` –Category name defined in your telephony system.

If `service` is set to another value, contact your Salesforce representative for the
conversation intelligence signal types available for your intelligence source.

Declarative Metadata Sample Definition

The following is an example of a ConvIntelligenceSignalRule component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ConvIntelligenceSignalRule xmlns="http://soap.sforce.com/2006/04/metadata">

      <actionType>AlertSupervisor</actionType>

      <active>true</active>

   <channelAddressIdentifier>a12bc345-1303-44c2-866c-f30d546b58de</channelAddressIdentifier>

      <channelType>Phone</channelType>

      <criteria>1 OR 2</criteria>

      <developerName>ConvIntelligenceRuleAPIName</developerName>

      <participantRole>AgentOrCustomer</participantRole>

      <ruleName>ConvIntelligenceRuleName</ruleName>

      <service>KeywordMatch</service>

      <subrule>

        <operandValue>escalate_level_1</operandValue>

        <operator>Equals</operator>

        <order>0</order>

        <type>Keyword</type>

      </subrule>

      <subrule>

        <operandValue>escalate_level_2</operandValue>

        <operator>Equals</operator>

        <order>1</order>

        <type>Keyword</type>

      </subrule>

   </ConvIntelligenceSignalRule>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ConversationIntelligenceSignalRule</name>

      </types>

      <version>62.0</version>

   </Package>

```


### Metadata Types CorsWhitelistOrigin

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### CorsWhitelistOrigin

Represents an origin in the CORS allowlist.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this metadata type’s name.

File Suffix and Directory Location

### CorsWhitelistOrigin components have the suffix .corswhitelistorigin and are stored in the corswhitelistorigins

folder.

Version

### CorsWhitelistOrigin components are available in API version 32.0 and later.

Fields

**Field Name** **Field Type** **Description**

`urlPattern` String

A URL pattern for the origin.

The origin URL pattern must include the HTTPS protocol and a domain
name, and can include a port. The wildcard character (*) is supported

and must be in front of a second-level domain name. For example,
`https://*.example.com` adds all subdomains of
`example.com` to the allowlist.

Google Chrome [™] and Mozilla [®] Firefox [®] browser extensions are also
allowed as resources in API version 53 and later. Chrome extensions
must use the prefix `chrome-extension://` and 32 characters
without digits or capital letters, for example
`chrome-extension://abdkkegmcbiomijcbdaodaflgehfffed` .
Firefox extensions must use the prefix `moz-extension://` and
an 8-4-4-4-12 format of small alphanumeric characters, for example
`moz-extension://1234ab56-78c9-1df2-3efg-4567891hi1j2` .

The origin URL pattern can be an IP address. But an IP address and a
domain that resolve to the same address aren’t the same origin, and
you must add them to the CORS allowlist as separate entries.


### Metadata Types CspTrustedSite

Declarative Metadata Sample Definition

Here’s an example package manifest used to deploy or retrieve the CorsWhitelistOrigin metadata for an organization.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>CorsWhitelistOrigin</name>

      </types>

      <version>32.0</version>

   </Package>

```

Here’s an example of a CorsWhitelistOrigin component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CorsWhitelistOrigin xmlns="http://soap.sforce.com/2006/04/metadata">

      <developerName>CorsWhitelistEntry1</developerName>

      <urlPattern>https://*.example.com</urlPattern>

   </CorsWhitelistOrigin>

```

Usage

[CORS (cross-origin resource sharing) is a W3C recommendation that enables Web browsers to request resources from origins other than](http://www.w3.org/TR/cors/)
their own. For example, using CORS, a JavaScript script at `https://www.example.com` could request a resource from
`https://www.salesforce.com` .

If a browser that supports CORS makes a request to an origin in your allowlist, Salesforce returns the origin in the
`Access-Control-Allow-Origin` HTTP header, along with any additional CORS HTTP headers. If the origin isn’t allow listed,
Salesforce returns HTTP status code 404.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### CspTrustedSite

Represents a trusted URL. For each CspTrustedSite component, you can specify Content Security Policy (CSP) directives and permissions
policy directives. Each CSP directive allows Lightning components, third-party APIs, and WebSocket connections to access a resource
type from the trusted URL. If the Permissions-Policy HTTP header is enabled, each permissions policy directive grants the trusted URL
access to a browser feature. In API version 58.0 and earlier, CspTrustedSite components included only CSP directives and were referred
to as CSP Trusted Sites.

This type extends the Metadata metadata type and inherits its `fullName` field.

Declarative Metadata File Suffix and Directory Location

### CspTrustedSite components are stored in the cspTrustedSites directory of the corresponding package directory. The file name

matches the unique name of the trusted site, and the extension is `.cspTrustedSite` .


Metadata Types CspTrustedSite

Tip: Some infrastructure limits the maximum size of HTTP headers. If you allow multiple domains to frame content served by your
org, keep the size of the CSP header under 12 KB. Salesforce customers report issues when the header size approaches 16 KB, and
third parties often add to the header during processing.

Version

CspTrustedSite components are available in API version 39.0 and later.

Fields

**Field** **Field Type** **Description**

`canAccessCamera` boolean

`canAccessMicrophone` boolean

Indicates whether this CspTrustedSite can access the user’s
camera ( `true` ) or not ( `false` ). The default value is `false` .

This field takes effect only when the
`enablePermissionsPolicy` field equals `true` and

the `grantCameraAccess` field equals `TrustedUrls`
in the SecuritySettings metadata API type.

This field is available in API version 59.0 and later.

Indicates whether this CspTrustedSite can access the user’s
microphone ( `true` ) or not ( `false` ). The default value is
`false` .

This field takes effect only when the
`enablePermissionsPolicy` field equals `true` and

the `grantMicrophoneAccess` field equals
`TrustedUrls` in the SecuritySettings metadata API type.

This field is available in API version 59.0 and later.

`context` CspTrustedSiteContext Declares the scope of the CSP directives for this trusted URL.
(enumeration of type string)

**•** `All` —Apply the CSP directives to all supported context
types.

**•** `Communities` —Apply the CSP directives to Experience
Builder sites only.

**•** `FieldServiceMobileExtension` —Apply the CSP
directives to the Field Service Mobile Extensions only. This
value is available in API version 47.0 and later.

**•** `LEX` —Apply the CSP directives to Lightning Experience
pages only.

**•** `LightningOut` —Reserved for future use. Available in
API version 64.0 and later

**•** `VisualForce` —Apply the CSP directives to custom
Visualforce pages only. This value is available in API version
55.0 and later.


Metadata Types CspTrustedSite

**Field** **Field Type** **Description**

For custom Visualforce pages, content is restricted to trusted
URLs only if the page’s `cspHeader` attribute is set to `true` .

This field is available in API version 44.0 and later.

`description` string The description of this trusted URL.

`endpointUrl` string

Required. The URL for this CspTrustedSite.

This field must include a domain name and can include a port.
For example, `https://example.com` or
`https://example.com:8080` .

To reduce repetition, you can use the wildcard character `*`
(asterisk). For example, `*.example.com` . For a third-party
API, the URL must begin with https://. For example,
`https://example.com` . For a WebSocket connection,
the URL must begin with wss://. For example,
`wss://example.com` .

Otherwise, the URL cannot be malformed. Examples of
malformed URLs that fail a syntax check are
`malformed^url.example.com`, and
`https://{subdomain}.example.com` .

Before February 2025, it was possible to save a malformed URL.
Malformed URLs are excluded from generated CSP HTTP headers.
To keep your Trusted URLs list accurate, remove any malformed
entries. You can use an Apex class to find all malformed URLs.
[See the knowledge article, Identify Malformed Trusted URLs.](https://help.salesforce.com/s/articleView?id=005317938&type=1&language=en_US)

To add an `EndpointUrl` based on parameters, build the
URL before you add it to this Metadata Type.

`isActive` boolean Required. Indicates whether this CspTrustedSite is active ( `true` )
or not ( `false` ). The default value is `true` .

`isApplicableToConnectSrc` boolean Indicates whether Lightning components, third-party APIs, and
WebSocket connections can load URLs using script interfaces

from this trusted URL ( `true` ) or not ( `false` ). This field has a
default value of `false` .

This field is available in API version 48.0 and later.

`isApplicableToFontSrc` boolean

Indicates whether Lightning components, third-party APIs, and
WebSocket connections can load fonts from this trusted URL
( `true` ) or not ( `false` ). This field has a default value of `false` .

This field is available in API version 48.0 and later.

`isApplicableToFrameSrc` boolean Indicates whether Lightning components, third-party APIs, and
WebSocket connections can load resources contained in

`<iframe>` elements from this trusted URL ( `true` ) or not


Metadata Types CspTrustedSite

**Field** **Field Type** **Description**

( `false` ). This field has a default value of `false` .This field is
available in API version 48.0 and later.

`isApplicableToImgSrc` boolean Indicates whether Lightning components, third-party APIs, and
WebSocket connections can load images from this trusted URL

( `true` ) or not ( `false` ). This field has a default value of `false` .
This field is available in API version 48.0 and later.

`isApplicableToMediaSrc` boolean Indicates whether Lightning components, third-party APIs, and
WebSocket connections can load audio and video from this

trusted URL ( `true` ) or not ( `false` ). This field has a default
value of `false` .

In API version 59.0 and later, for each trusted URL, at least one
CSPTrustedSite starting with `isApplicable` or
`canAccess` must be set to `true.`

In API version 50.0 to 58.0, if all `isApplicable` fields are
`false`, the `isApplicableToImgSrc` field is set to
`true` . In API version 49.0 and earlier, if all `isApplicable`
fields are `false`, these fields all default to `true` .

This field is available in API version 48.0 and later.

`isApplicableToStyleSrc` boolean Indicates whether Lightning components, third-party APIs, and
WebSocket connections can load style sheets from this trusted

URL ( `true` ) or not ( `false` ). This field has a default value of
`false` . This field is available in API version 48.0 and later.

`mobileExtension` string Reserved for future use.

Declarative Metadata Sample Definition

A sample XML definition of a trusted site is shown below.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CspTrustedSite xmlns="http://soap.sforce.com/2006/04/metadata">

      <canAccessCamera>false</canAccessCamera>

      <canAccessMicrophone>true</canAccessMicrophone>

      <description>Used for Lightning component callout to mapping web service</description>

      <context>LEX</context>

      <endpointUrl>https://www.maptestsite.net/</endpointUrl>

      <isActive>true</isActive>

      <isApplicableToConnectSrc>true</isApplicableToConnectSrc>

      <isApplicableToFontSrc>true</isApplicableToFontSrc>

      <isApplicableToFrameSrc>false</isApplicableToFrameSrc>

      <isApplicableToImgSrc>true</isApplicableToImgSrc>

      <isApplicableToMediaSrc>false</isApplicableToMediaSrc>

      <isApplicableToStyleSrc>true</isApplicableToStyleSrc>

   </CspTrustedSite>

```


### Metadata Types CustomApplication

Usage

For each CSPTrustedSite component, at least one field starting with `grantAccess` or `isApplicableTo` must be set to `true.`

In API versions 50.0 to 58.0, if all `isApplicable` fields are `false`, the `isApplicableToImgSrc` field is set to `true` . In API
version 49.0 and earlier, if all `isApplicable` fields are `false`, those fields all default to `true` .

To ensure smooth integration across Salesforce products, Salesforce includes URLs in each of the CSP directives that correspond to the
`isApplicable` fields, even though those URLs aren’t defined as CspTrustedSite components. Salesforce regularly updates those
URLs based on the latest requirements.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### CustomApplication CustomApplication represents a custom or standard application. In API version 29.0 and earlier, CustomApplication represents only a

custom application. An application is a list of tab references, with a description and a logo. This type extends the Metadata metadata
type and inherits its `fullName` field.

File Suffix and Directory Location

Custom and standard applications have the suffix `.app` and are stored in the `applications` folder.

Note: Retrieving a component of this metadata type in a project makes the component appear in any Profile and PermissionSet
components that are retrieved in the same package.

Version

Custom applications are available in API version 10.0 and later. Standard applications are available in API version 30.0 and later.

Fields

**Field Name** **Field Type** **Description**

`actionOverrides` AppActionOverride[] Represents an action override for an application. Use it
to create, update, edit, or delete action overrides.This

field is available for Lightning Experience in API version
38.0 and later.

`brand` AppBrand

The color scheme and logo used for the app.This field is
available for Lightning Experience in API version 38.0 and
later.

`consoleConfig` ServiceCloudConsoleConfig Represents configuration settings for a Salesforce console
app.This field is available in API version 42.0 and later.


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

`defaultLandingTab` string The fullName of a standard tab or custom tab that opens
when this application is selected.

`description` string The optional description text of the application.

`formFactors` FormFactor (enumeration of type Indicates the form factors for which the app is visible for
string) Lightning Experience. Valid values are:

**•** `Null` (no value)—For a desktop using Salesforce
Classic

**•** `Small` —For a mobile device using the Salesforce
mobile app

**•** `Medium` —Reserved for future use

**•** `Large` —For a desktop using Lightning Experience

This field is available in API version 38.0 and later.

As of API version 38.0, `formFactors` is set to `Large`
for existing Salesforce Classic apps, except for Salesforce
Classic consoles. Salesforce Classic apps installed from
packages created before API version 38.0 also have
`formFactors` set to `Large` . For Salesforce Classic
apps in packages created with API 38.0 or later, you must
set `formFactors` to `Large` for Salesforce Classic
apps to appear in the Lightning Experience desktop.

As of API version 47.0, the `Small` value is supported
for Lightning apps. The `formFactors` field can be
set to `Small` or `Large` for Lightning apps, and it can
be set to `Null` or `Large` for Salesforce Classic apps.

`isNavAutoTempTabsDisabled` boolean Indicates whether the navigation automatically creates
temporary tabs settings. Applies only to Lightning apps

with standard navigation. Available in API version 43.0
and later.

`isNavPersonalizationDisabled` boolean

Indicates whether navigation personalization is disabled.
Applies only to Lightning apps. Available in API version
43.0 and later.

`isNavTabPersistenceDisabled` boolean Indicates whether workspace tabs are cleared for each
new console session ( `true` ) or not ( `false` ). Applies

only to Lightning apps with console navigation. Available
in API version 54.0 and later.

`isServiceCloudConsole` boolean

Indicates if the application is a Salesforce Classic console
app. For Lightning Experience console apps, this field is
`null` and the `navType` field is set to `Console` .

`label` string The name of the application.


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

`logo` string The optional reference to the image document for a
Salesforce app or Salesforce console app.

`navType` NavType (enumeration of type string) Not updateable. Indicates the type of navigation the app
uses. The value `Standard` is for a Lightning app with

standard navigation. The value `Console` is for a
Lightning app with console navigation.

This field is available in API version 38.0 and later.

`preferences` AppPreferences

Represents the preferences for a Salesforce Classic
console app. All of the AppPreferences fields are
required.This field is available in API version 42.0 and later.

`profileActionOverrides` AppProfileActionOverride[] A list of the Lightning Experience record page
ProfileActionOverrides that are assigned to this custom

app. When a user invokes the custom app, a matching
ProfileActionOverride assignment takes precedence over
existing overrides for the record page specified in
ActionOverride. You can override a record page for the
custom app by record type and profile.

In API version 45.0 and later, you can override a home
page for the custom app by profile.

`setupExperience` string The type of Setup experience associated with the app.
Valid values are:

**•** `all` —Represents the full Setup tree.

**•** `essentials` —Represents the Essentials Setup
tree, which contains a subset of Setup items
configured for Essentials edition.

**•** `service` —Represents the Service Setup tree,
which contains a subset of Setup items configured
for Service Console.

A `null` value is equivalent to `all` .

Previous valid values `AllSetup`, `ServiceSetup`,
and `EssentialsSetup` have been deprecated.

This field is available in API version 39.0 and later.

`subscriberTabs` string[]

Represents the list of tabs appended by a subscriber to
a Lightning app installed from a managed package.
Records in a subscriber tab always open as primary tabs.

This field is available in API version 41.0 and later.

`tabs` string[] The list of tabs included in this application. In API version
12.0, the `fullName` for built-in tabs like Home,

Account, and Reports, is the name of the tab (Home, for


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

example). In API version 13.0 and later, built-in tabs are
prefixed with `standard-` . For example, to reference
the Account tab you would use `standard-Account` .

In API version 42.0, this field was renamed from `tab` to
`tabs` .

`uiType` UiType (enumeration of type string) Not updateable. Identifies the type of custom app. The
value is:

**•** `Aloha` for Salesforce Classic

**•** `Lightning` for Lightning Experience

This field is available in API version 38.0 and later.

`utilityBar` string

The developer name of the utility bar associated with
this app.

We recommend assigning a utility bar to only one
Lightning App, because utility bars are shared. Sharing

means that if you change the utility bar in one app, it
automatically changes in all apps associated with it.

This field is available in API version 38.0 and later.

`workspaceConfig` AppWorkspaceConfig isServiceCloudConsole `is true` . `Represents how`

```
                              records open in a Salesforce console
```

`app. Required if workspaceConfig` from
`workspaceMappings` .

AppActionOverride

Represents an action override for an application. Use it to create, update, edit, or delete action overrides. AppActionOverride inherits
from ActionOverride and extends it by one field, `pageOrSobjectType` . Available for Lightning Experience in API version 38.0 and
later.

**Field Name** **Field Type** **Description**

`actionName` string The only valid value is `view` for API version 43.0 and earlier. The value
`tab` is supported for API version 44.0 and later.

`comment` string Any comments you want associated with the override.

`content` string

`formFactor` FormFactor(enumeration
of type string)

Set this field if `type` is set to `flexipage` . It refers to the name of the
page to use as the override. To reference installed components, use the
format of _**`Component_namespace`**_ `__` _**`Component_name`**_ .

The size of the page being overridden.

If the `type` field is set to `flexipage`, set this field to `Large` to
override the View action with a Lightning page in Lightning Experience.


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

The `Large` value represents the Lightning Experience desktop
environment and is valid only for the `flexipage` and
`lightningcomponent` types. The `Small` value represents the
Salesforce mobile app on a phone or tablet. The `Medium` value is
reserved for future use. The `null` value (which is the same as specifying
no value) represents Salesforce Classic.

This field is available in API version 37.0 and later and is part of the feature
for creating and editing record pages in Lightning Experience.

Lightning component overrides return different `FormFactor` values
depending on the API version used.

**•** In API version 41.0 and earlier, Lightning component overrides return
only the `null` value (no value), representing the Salesforce Classic
environment.

**•** In API version 42.0, if you specify different Lightning component
overrides for Lightning Experience and mobile, one component is
selected randomly for both overrides and its `FormFactor` value
is returned. If there’s a conflict between Lightning components, and
a Visualforce page override is also specified for Salesforce Classic, the
Visualforce page takes precedence.

**•** In API version 43.0 and later, a Lightning component override for
Lightning Experience returns the `Large` value and a Lightning
component override for mobile returns the `Small` value, as
expected.

`pageOrSobjectType` string

The name of the sObject type being overridden. Valid values are
`standard` and `custom` .

This value must be `standard-home` when actionName is `tab` .

`skipRecordTypeSelect` boolean Set this field to `true` if you prefer that any new records created by this
action override aren’t forwarded to the record type selection page. This

field is only valid if the `actionName` is a “create” type (like `new` ), and
`type` is set to `visualforce` .

Required. Represents the type of action override. The valid values are
`Flexipage` and `Default` .

A `Flexipage` AppActionOverride set to App Default can’t be deleted
via Metadata API. Instead, remove the override using the page assignment
wizard in the Lightning App Builder UI.

```
type

```

AppBrand

ActionOverrideType
(enumeration of type
string)

The color scheme and logo used for the app. Available for Lightning apps in API version 38.0 and later.


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

`footerColor` string Optional. Specify the color with a hexadecimal code, such as #0000FF
for blue.Determines the footer color in the app.

`headerColor` string Optional. Specify the color with a hexadecimal code, such as #0000FF
for blue.Determines the header color in the app.

`logo` string The optional reference to the image document for the application.

`logoVersion` int An optional version number for the logo.

`shouldOverrideOrgTheme` boolean Indicates whether to override the global theme for the org. When `true`,
the color scheme and logo that the user has set are used. When `false`,

the global theme for the org is used, even if the user has set a color
scheme and logo.

AppComponentList

Represents custom console components (Visualforce pages) assigned to a Salesforce console app. In API version 42.0, this type was
renamed from CustomApplicationComponents to AppComponentList.

**Field Name** **Field Type** **Description**

`alignment` string Required. Determines how custom console components are aligned in
the footer of a Salesforce console app.

`components` string[]

AppPreferences

The name of a custom console component assigned to a Salesforce
console app. In API version 42.0, this field was renamed from
`customApplicationComponent` to `components` .

Represents the preferences for a Salesforce Classic console app. All of the AppPreferences fields are required. Available in API version
42.0 and later.

**Field Name** **Field Type** **Description**

`enableCustomizeMyTabs` boolean

Indicates if a Salesforce Classic console app has Customize My Tabs
enabled. If enabled, users can hide, display, and organize items in the
navigation tab.

`enableKeyboardShortcuts` boolean Indicates if a Salesforce Classic console app has keyboard shortcuts
enabled. Shortcuts let users perform actions by pressing a combination

of keys instead of having to use a mouse. After keyboard shortcuts are
enabled, several default shortcuts are available for customization. Before
you can create custom shortcuts, a developer must define the shortcut’s
action with the `addEventListener()` method in the Salesforce
Console Integration Toolkit. You can’t create keyboard shortcuts for
actions performed outside of the console. This field is required if
isServiceCloudConsole `is true` .


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

`enableListViewHover` boolean Indicates if a Salesforce Classic console app has list view hovers enabled.
If set to `true`, summary information is displayed about a record in a

responsive list when the user hovers over a record name. For cases, hover
over the subject field.

`enableListViewReskin` boolean Indicates if Salesforce Classic console apps use responsive list views
instead of Salesforce Classic lists views.

`enableMultiMonitorComponents` boolean Indicates if a Salesforce Classic console app has multi-monitor
components enabled, which lets users move portions of a console from

their browsers to locations on their screens. This field is required if
isServiceCloudConsole `is true` .

`enablePinTabs` boolean Indicates if a Salesforce Classic console app has pinned tabs enabled,
which lets users pin primary tabs to the tab bar for quick access.

`enableTabHover` boolean

`enableTabLimits` boolean

Indicates if a Salesforce Classic console app has tab hover enabled. If
enabled, summary information is displayed about a record in an overlay
when the user hovers over a tab.

Indicates whether limits are enabled on the number of primary tabs and
subtabs that can be opened in a Salesforce Classic console session. When
`true`, values for `tabLimitConfig` are required

`saveUserSessions` boolean Indicates if a Salesforce Classic console app saves user sessions
automatically. If enabled, when console users close their browsers or log

out of Salesforce, any previously open tabs display when users log in
again. Required if isServiceCloudConsole `is true` .

AppProfileActionOverride

Represents a ProfileActionOverride for a custom app. This type inherits from ProfileActionOverride on page 1774 and extends it by one
field, `profile` . Available for Lightning Experience in API version 39.0 and later. In API version 45.0 and later, you can override a home
page for the custom app by profile.

**Field Name** **Field Type** **Description**

`actionName` string

Required. The name of the action. The only valid values are `Tab` and
`View` .

If `pageOrSobjectType` is `record-home`, this field must be
`View` . The `View` action is supported only when ProfileActionOverride
is being specified as part of a CustomApplication.

In API version 45.0 and later, this action is supported only when
ProfileActionOverride is being specified as part of a CustomApplication,
`pageOrSobjectType` is `standard-home`, and this field is `Tab` .

`content` string Read-only. Represents the name of the Lightning page being used as
the override.


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

```
formFactor

```

FormFactor Required. The size of the page being overridden. The `Large` value
(enumeration of type represents the Lightning Experience desktop environment.
string)

`pageOrSobjectType` string

Required. The name of the page being overridden. The only valid values
are `record-home` and `standard-home` . If the `actionName`
is `Tab`, this field must be `standard-home`

`profile` string The profile associated with the ProfileActionOverride.

`recordType` string

The record type associated with the override. If `pageOrSobjectType`
is `standard-home`, this field must be `null` . This field is required
when `actionName` is set to `View` .

```
type

```

ActionOverrideType Required. Read-only. The type of action override. The only valid value is
(enumeration of type `flexipage` .
string)

AppWorkspaceConfig

