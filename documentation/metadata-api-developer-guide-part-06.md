**Field Type**
string

**Description**

Required. The name of the field in the reference object used to define stages.

**Field Type**
string

**Description**
The record type of a reference object associated with the stage definition.

**Field Type**

StageTransition[]

**Description**
A collection of fields to set up transitions between two states.

**Field Type**

StageValue[]

**Description**
A collection of fields to set up the field values of an object for which stages are defined.

Represents a collection of fields to set up transitions between two states.


Metadata Types StageDefinition

**Field Name** **Description**

```
criteria

customPermission

fromStageValue

stepGroup

toStageValue

userPermission

```

**Field Type**

StageCriteria[]

**Description**
A collection of fields to set up the criteria for the object stage transition and object
stage change.

**Field Type**
string

**Description**
The custom permission associated with the stage transition. The custom permission
required to initiate a stage change.

**Field Type**
string

**Description**

Required. The `From Stage` that's associated with the referenced object's stage
transition.

**Field Type**

StgFulfillmentStepDefGrp[]

**Description**
A collection of fields to set up the stage fulfillment step definition.

**Field Type**
string

**Description**

Required. The `To Stage` that's associated with the referenced object's stage
transition.

**Field Type**
StageUserPermission (enumeration of type string)

**Description**
Specifies the type of user permission needed to initiate a stage change.

Values are:

**•** `CoordinateClinicalTrials`

**•** `CoordinateClnclTrialExprcUsr`

**•** `ManageClinicalTrials`

**•** `ParticipateClinicalTrials`

**•** `ProcessOrder`


Metadata Types StageDefinition

StageCriteria

Represents a collection of fields to set up the criteria for the object stage transition and object stage change.

**Field Name** **Description**

```
condition

criteriaType

errorMessage

executionType

flowDefinitionName

```

**Field Type**

StageCondition[]

**Description**
A collection of fields to set up the rules in transition criteria and stage change, including
the object state, logic, and values.

**Field Type**
StageCriteriaType (enumeration of type string)

**Description**

Specifies the criteria type used to execute the transition.

Values are:

**•** `AND`

**•** `CUSTOMLOGIC`

**•** `OR`

**Field Type**
string

**Description**

A custom error message that's displayed when stage transition criteria evaluation fails.

Available in API version 64.0 and later.

**Field Type**
StageCriteriaExecType (enumeration of type string)

**Description**

Required. Specifies the type of logic used to execute the criteria.

Values are:

**•** `CONDITION`

**•** `FLOW`

**Field Type**
string

**Description**

Specifies the developer name of the Flow that executes when the criteria execution
type is set to `FLOW` .

Available in API version 63.0 and later.


Metadata Types StageDefinition

**Field Name** **Description**

```
isChildObject

logicalExpression

targetFieldName

targetObject

```

StageCondition

**Field Type**
boolean

**Description**
Indicates whether the target object in the stage criteria represents a child object in a
parent-child relationship ( `true` ) or not ( `false` ).

Available in API version 63.0 and later.

**Field Type**
string

**Description**

Formula to specify custom logic. Compares the Criteria field to the Value field.

**Field Type**
string

**Description**

Specifies the field name on the target object that's used in the stage transition criteria
evaluation.

Available in API version 63.0 and later.

**Field Type**
string

**Description**

Object that's used in a Parent-Child object relationship condition.

Represents a collection of fields to set up the rules in transition criteria and stage change, including the object state, logic, and values.

**Field Name** **Description**

```
operator

```

**Field Type**
StageConditionOperator (enumeration of type string)

**Description**

Required. Specifies the operator used in the transition criteria.

Values are:

**•** `Contains`

**•** `DoesNotContain`

**•** `Equals`

**•** `GreaterOrEqual`


Metadata Types StageDefinition

**Field Name** **Description**

**•** `GreaterThan`

**•** `LessOrEqual`

**•** `LessThan`

**•** `NotEqualTo`

**•** `StartsWith`

```
sequenceNumber

sourceField

value

```

**Field Type**
int

**Description**

Required. Specifies the order of the object state transition condition in a sequence.

**Field Type**
string

**Description**

Required. The object field to define filter conditions.

**Field Type**
string

**Description**

Required. Value of the field used in the transition criteria.

StgFulfillmentStepDefGrp

Represents a collection of fields to set up the stage fulfillment step definition.

**Field Name** **Description**

```
name

step

```

StgFulfillmentStepDef

**Field Type**
string

**Description**

Required. The name of the stage fulfillment step definition group.

**Field Type**

StgFulfillmentStepDef[]

**Description**
A collection of fields to set up fullfillment step definitions for stages and transitions.

Represents a collection of fields to set up fullfillment step definitions for stages and transitions.


Metadata Types StageDefinition

**Field Name** **Description**

```
apiName

assignedToQueue

assignedToUser

dependency

executeOnRule

flowDefinitionName

integrationDefinitionName

name

```

**Field Type**
string

**Description**

Required. The developer name of the stage fulfillment step definition.

**Field Type**
string

**Description**
The queue associated with the stage fulfillment step definition.

**Field Type**
string

**Description**
The user associated with the stage fulfillment step definition.

**Field Type**

StgFulfillmentStepDpndDef[]

**Description**
A collection of fields to set up the stage fulfillment step dependency between two
steps.

**Field Type**
string

**Description**

Specifies the expression set for the fulfillment step. The step is executed only when
the corresponding expression set is set to `true` .

Available in API version 62.0 and later.

**Field Type**
string

**Description**
The name of the flow added to the step definition.

**Field Type**
string

**Description**
The ID associated with the integration provider definition.

**Field Type**
string


Metadata Types StageDefinition

**Field Name** **Description**

**Description**

Required. The name of the stage fulfillment step definition.

```
omniscriptName

runAsUser

stepType

```

**Field Type**
string

**Description**
The name of the Omniscript defined in step definition.

**Field Type**
string

**Description**
The ID of the user associated with the step definition. The user required to execute
the step definition.

**Field Type**
string

**Description**

Required. Specifies the type of fulfillment step.

StgFulfillmentStepDpndDef

Represents a collection of fields to set up the stage fulfillment step dependency between two steps.

**Field Name** **Description**

```
step

```

StageValue

**Field Type**
string

**Description**

Required. The step definition for the fulfillment step.

Represents a collection of fields to set up the field values of an object for which stages are defined.

**Field Name** **Description**

```
criteria

```

**Field Type**

StageCriteria[]

**Description**
A collection of fields to set up the criteria for the object stage transition and object
stage change.


Metadata Types StageDefinition

**Field Name** **Description**

```
stepGroup

value

```

**Field Type**

StgFulfillmentStepDefGrp[]

**Description**
A collection of fields to set up the stage fulfillment step definition.

**Field Type**
string

**Description**

Required. The value of the field used in the transition criteria.

Declarative Metadata Sample Definition

The following is an example of a StageDefinition component.

```
<?xml version="1.0" encoding="UTF-8"?>

<StageDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

   <active>false</active>

   <description>Application form Stage transitions</description>

   <masterLabel>basic</masterLabel>

   <referenceObject>ApplicationForm</referenceObject>

   <referenceObjectField>Stage</referenceObjectField>

   <stageTransition>

     <criteria>

        <condition>

          <operator>Equals</operator>

          <sequenceNumber>1</sequenceNumber>

          <sourceField>ApplicationForm.Name</sourceField>

          <value>test</value>

        </condition>

        <criteriaType>AND</criteriaType>

        <executionType>CONDITION</executionType>

        <logicalExpression>1</logicalExpression>

        <targetObject>ApplicationForm</targetObject>

     </criteria>

     <userPermission>ProcessOrder</userPermission>

     <fromStageValue>Initiated</fromStageValue>

     <toStageValue>On Hold</toStageValue>

     <stepGroup>

        <name>Initiated-On Hold</name>

        <step>

          <apiName>Autotask_step_defn</apiName>

         <flowDefinitionName>disputemanagement__InvokeAsyncAction</flowDefinitionName>

          <name>Autotask step defn</name>

          <runAsUser>testuser@salesforce.com</runAsUser>

          <stepType>AutoTask</stepType>

        </step>

        <step>

```


Metadata Types StageDefinition

```
             <apiName>testScreenFlow</apiName>

             <assignedToUser>testuser@salesforce.com</assignedToUser>

             <flowDefinitionName>cms_orch__CMS_NotifyRequester</flowDefinitionName>

             <name>testScreenFlow</name>

             <stepType>ManualTask</stepType>

             <dependency>

               <step>Autotask_step_defn</step>

             </dependency>

           </step>

        </stepGroup>

      </stageTransition>

      <stageValue>

        <value>Initiated</value>

        <criteria>

           <condition>

             <operator>Equals</operator>

             <sequenceNumber>1</sequenceNumber>

             <sourceField>ApplicationForm.Name</sourceField>

             <value>test</value>

           </condition>

           <criteriaType>AND</criteriaType>

           <executionType>CONDITION</executionType>

           <logicalExpression>1</logicalExpression>

           <targetObject>ApplicationForm</targetObject>

        </criteria>

        <stepGroup>

           <name>Initiated</name>

           <step>

             <apiName>Autotask_step_defn</apiName>

            <flowDefinitionName>disputemanagement__InvokeAsyncAction</flowDefinitionName>

             <name>Autotask step defn</name>

             <runAsUser>testuser@salesforce.com</runAsUser>

             <stepType>AutoTask</stepType>

           </step>

           <step>

             <apiName>testScreenFlow</apiName>

             <assignedToUser>testuser@salesforce.com</assignedToUser>

             <flowDefinitionName>cms_orch__CMS_NotifyRequester</flowDefinitionName>

             <name>testScreenFlow</name>

             <stepType>ManualTask</stepType>

             <dependency>

               <step>Autotask_step_defn</step>

             </dependency>

           </step>

        </stepGroup>

      </stageValue>

      <stageValue>

        <value>On Hold</value>

      </stageValue>

   </StageDefinition>

```


### Metadata Types SustainabilityUom

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>StageDefinition</name>

      </types>

      <version>62.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### SustainabilityUom

Represents the unit of measure (UOM) values for custom fuel types in an org. Track fuel consumption and emission results with the
flexibility to add custom fuel types and UOM values.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### SustainabilityUom components have the suffix .sustainabilityUom and are stored in the sustainabilityUoms folder.

Version

### SustainabilityUom components are available in API version 56.0 and later.

Special Access Rules

The Net Zero Cloud permission set license is required to access this object along with the user access for carbon accounting and org
access for custom fuels and UOMs.

Fields

**Field Name** **Description**

```
description

```

**Field Type**
string

**Description**
The description of the unit of measure.


Metadata Types SustainabilityUom

**Field Name** **Description**

```
isProductUom

isProtected

isStationaryAssetUom

isVehicleAssetUom

masterLabel

unitType

```

**Field Type**
boolean

**Description**

Indicates whether the unit of measure is for a product that the company has procured
in its supply chain operations ( `true` ) or not ( `false` ).

The default value is `false` .

**Field Type**
boolean

**Description**
An auto-generated value that doesn’t impact the behavior of the metadata type.

The default value is `false` .

**Field Type**
boolean

**Description**

Indicates whether the unit of measure is used in the stationary asset calculations
( `true` ) or ( `false` ).

The default value is `false` .

**Field Type**
boolean

**Description**
Indicates whether the unit of measure is used in the vehicle asset calculations ( `true` )
or ( `false` ).

The default value is `false` .

**Field Type**
string

**Description**

Required.

The label assigned to this object.

**Field Type**
UnitType (enumeration of type string)

**Description**

Required.

The type of unit used for conversions or calculations.

Values are:


### Metadata Types SustnUomConversion

**Field Name** **Description**

**•** `Energy`

**•** `Other`

**•** `Volume`

**•** `Weight`

Declarative Metadata Sample Definition

The following is an example of a SustainabilityUom component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <SustainabilityUom xmlns="http://soap.sforce.com/2006/04/metadata">

     <description>Weight in Grams</description>

     <isProductUom>true</isProductUom>

     <isProtected>false</isProtected>

     <isStationaryAssetUom>false</isStationaryAssetUom>

     <isVehicleAssetUom>false</isVehicleAssetUom>

     <masterLabel>Grams</masterLabel>

     <unitType>Weight</unitType>

   </SustainabilityUom>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <fullName>Pkg</fullName>

     <types>

      <members>Grams</members>

      <name>SustainabilityUom</name>

     </types>

     <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### SustnUomConversion

Represents information about the unit of measure (UOM) conversion for the custom fuel types defined by a customer in an org.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types SustnUomConversion

File Suffix and Directory Location

SustnUomConversion components have the suffix `sustnUomConversion` and are stored in the `sustnUomConversions`
folder.

Version

SustnUomConversion components are available in API version 57.0 and later.

Special Access Rules

The Net Zero Cloud permission set license is required to access this object along with the user access for carbon accounting and org
access for custom fuels and UOMs.

Fields

**Field Name** **Description**

```
conversionFactor

fuelType

```

**Field Type**
double

**Description**

Required.

The conversion factor that's used to convert values from one unit of measure to another
for the fuel type.

**Field Type**
string

**Description**
The name of the fuel type.

Possible values are:

**•** `AutogasLPG`

**•** `Biodiesel`

**•** `Biomass`

**•** `CityGas`

**•** `CompressedNaturalGasCNG`

**•** `Cooling`

**•** `Diesel`

**•** `Electricity`

**•** `Ethanol`

**•** `FuelOil`

**•** `Gasoline`

**•** `Heat`


Metadata Types SustnUomConversion

**Field Name** **Description**

**•** `HeavyOil`

**•** `ITElectricity`

**•** `JetFuel`

**•** `Kerosene`

**•** `LightOil`

**•** `LiquidNaturalGasLNG`

**•** `MobileDiesel`

**•** `NaturalGas`

**•** `Propane`

**•** `Refrigerant`

**•** `Steam`

```
isProtected

masterLabel

sourceUom

```

**Field Type**
boolean

**Description**
An auto-generated value that doesn’t impact the behavior of the metadata type.

The default value is `false` .

**Field Type**
string

**Description**
A user-friendly name for SustnUomConversion, which is defined when the
SustnUomConversion is created.

**Field Type**
string

**Description**

Required.

The source unit of measure for the fuel type.

Possible values are:

**•** `1000m3`

**•** `GJ`

**•** `GWh`

**•** `Kiloliters`

**•** `Liters`

**•** `MJ`

**•** `MMBtu`

**•** `MWh`

**•** `Therms`


Metadata Types SustnUomConversion

**Field Name** **Description**

**•** `Tonnes`

**•** `UkGallons`

**•** `UsGallons`

**•** `ccf`

**•** `kG`

**•** `kWh`

**•** `kcal`

**•** `lbs`

**•** `longTons`

**•** `m3`

**•** `shortTons`

```
targetUom

uomsKey

```

**Field Type**
string

**Description**

Required.

The target unit of measure for the fuel type.

**Field Type**
string

**Description**
The key associated with a unit of measure for the fuel type.

Declarative Metadata Sample Definition

The following is an example of a SustnUomConversion component.

```
<?xml version="1.0" encoding="UTF-8"?>

<SustnUomConversion xmlns="http://soap.sforce.com/2006/04/metadata">

   <conversionFactor>0.9</conversionFactor>

   <fuelType>Diesel</fuelType>

   <isProtected>false</isProtected>

   <masterLabel>KG_Liters</masterLabel>

   <sourceUom>KG</sourceUom>

   <targetUom>Liters</targetUom>

   <uomsKey>uomsKey</uomsKey>

</SustnUomConversion>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <fullName>Pkg</fullName>

   <types>

```


### Metadata Types SvcCatalogCategory

```
        <members>US_UK_Gallons</members>

        <members>Therms_kWh</members>

        <members>KG_Liters</members>

        <name>SustnUomConversion</name>

      </types>

      <version>57.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### SvcCatalogCategory

Represents the grouping of individual catalog items in Service Catalog.

File Suffix and Directory Location

### SvcCatalogCategory components have the suffix category and are stored in the svcCatalogCategories folder.

Version

### SvcCatalogCategory components are available in API version 53.0 and later.

Fields

**Field Name** **Description**

```
image

isActive

isProtected

```

**Field Type**
string

**Description**
The developer name of a content document to be displayed in the Service Catalog
for this category.

**Field Type**
boolean

**Description**
Indicates if a catalog category is active.

**Field Type**
boolean

**Description**
An auto-generated value. This value currently has no impact.


### Metadata Types SvcCatalogFulfillmentFlow

**Field Name** **Description**

```
masterLabel

parentCategory

sortOrder

```

**Field Type**
string

**Description**
Required. The primary label for the catalog category record.

**Field Type**
string

**Description**
If provided, the name of another SvcCatalogCategory that this category should appear
under. The parent category in this field can’t have its own parent category. Categories
can’t have more than one level of nesting.

**Field Type**
int

**Description**
Displays a set order for catalog category entities.

Declarative Metadata Sample Definition

The following is an example of a SvcCatalogCategory component.

```
<?xml version="1.0" encoding="UTF-8"?>

<SvcCatalogCategory xmlns="http://soap.sforce.com/2006/04/metadata">

   <image>AdobeStock_287068722</image>

   <isActive>true</isActive>

   <isProtected>false</isProtected>

   <masterLabel>Workplace Services</masterLabel>

   <sortOrder>4</sortOrder>

</SvcCatalogCategory>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### SvcCatalogFulfillmentFlow

Represents the flow associated with a specific catalog item in the Service Catalog.

File Suffix and Directory Location

### SvcCatalogFulfillmentFlow components have the suffix fulfillmentFlow and are stored in the

`svcCatalogFulfillmentFlows` folder.


Metadata Types SvcCatalogFulfillmentFlow

Version

SvcCatalogFulfillmentFlows components are available in API version 53.0 and later.

Fields

**Field Name** **Description**

```
description

flow

icon

isProtected

items

masterLabel

```

**Field Type**
string

**Description**
Required. Free-text description of the fulfillment flow.

**Field Type**
string

**Description**
Required. The name of the flow represented by this SvcCatalogFulfillmentFlow.

**Field Type**
string

**Description**
Represents the details of an icon.

**Field Type**
boolean

**Description**
An auto-generated value. This value currently has no impact.

**Field Type**

SvcCatalogFulfillFlowItem on page 2352[]

**Description**
The list of variables in the flow that can accept a value as input.

**Field Type**
string

**Description**
Required. The primary label for the fulfillment flow record.

SvcCatalogFulfillFlowItem

Represents a variable in a fulfillment flow that can accept input. Describes what type of value it accepts.


Metadata Types SvcCatalogFulfillmentFlow

**Field Name** **Description**

```
catalogInputVariable

displayType

fieldDefinition

fieldLookupDomain

isAdditionalQuestionsInputVariable

```

**Field Type**
string

**Description**

Required.

The FlowVariable the fulfillment flow property represents.

**Field Type**
PropertyDisplayType (enumeration of type string)

**Description**

The display options available.

Values are:

**•** `Checkbox`

**•** `Date` (available in API version 59.0 and later)

**•** `DateTime` (available in API version 59.0 and later)

**•** `Lookup`

**•** `Number`

**•** `Picklist`

**•** `Queue` (available in API version 57.0 and later)

**•** `Text`

**Field Type**
string

**Description**
The name of a field in the object provided in `objectLookupDomain` that specifies
the value for this variable. If `displayType` is `Picklist`, this value must be the
name of a picklist field. If `displayType` is `Lookup` and `fieldLookupDomain`
is `FieldDefinition`, this value must be the name of a relationship field.

**Field Type**
string

**Description**
The name of a standard or custom object that specifies the domain of that lookup or
picklist. This value is relevant only if `displayType` is `Lookup` or `Picklist` .

**Field Type**
boolean

**Description**
Determines if this variable accepts input for all additional questions that were asked
to a user. This value can only be `true` if the `displayType` for this item is `Text` .
Only one item per SvcCatalogFulfillmentFlow component can set this attribute to
`true` .


Metadata Types SvcCatalogFulfillmentFlow

**Field Name** **Description**

```
isRequired

lookupDomainFieldType

masterLabel

objectLookupDomain

```

**Field Type**
boolean

**Description**
Determines if the field is required for the related fulfillment flow to be executed.

**Field Type**
string

**Description**
This value specifies the fields for the object specified by `objectLookupDomain`
that are displayed in the Catalog Builder by type. This value is only relevant if
`displayType` is `Lookup` and `fieldLookupDomain` is
`FieldDefinition` .

**Field Type**
string

**Description**

Required.

The primary label for the fulfillment flow record.

**Field Type**
string

**Description**
The name of a custom or standard object. If `displayType` is `Lookup` or
`Picklist`, this value filters the available options to a specific object.

Declarative Metadata Sample Definition

The following is an example of a SvcCatalogFulfillmentFlow component.

```
<?xml version="1.0" encoding="UTF-8"?>

<SvcCatalogFulfillmentFlow xmlns="http://soap.sforce.com/2006/04/metadata">

   <description>Creates a Case record related to the Contact belonging to the current

User. If this will be used by Users without related Contacts, provide an Account Id below.

 This Account Id will be used instead of a Contact.</description>

   <flow>Create_Case_by_Record_Type</flow>

   <isProtected>false</isProtected>

   <items>

     <catalogInputVariable>Input_RecordTypeApiName</catalogInputVariable>

     <displayType>Text</displayType>

     <isAdditionalQuestionsInputVariable>false</isAdditionalQuestionsInputVariable>

     <isRequired>true</isRequired>

     <masterLabel>Record Type Developer Name</masterLabel>

   </items>

   <items>

```


Metadata Types SvcCatalogFulfillmentFlow

```
        <catalogInputVariable>Input_AccountId</catalogInputVariable>

        <displayType>Lookup</displayType>

        <fieldDefinition>AccountId</fieldDefinition>

        <fieldLookupDomain>Account</fieldLookupDomain>

        <isAdditionalQuestionsInputVariable>false</isAdditionalQuestionsInputVariable>

        <isRequired>false</isRequired>

        <masterLabel>(Optional) Related Account</masterLabel>

        <objectLookupDomain>Contact</objectLookupDomain>

      </items>

      <items>

        <catalogInputVariable>Input_Origin</catalogInputVariable>

        <displayType>Picklist</displayType>

        <fieldDefinition>Origin</fieldDefinition>

        <isAdditionalQuestionsInputVariable>false</isAdditionalQuestionsInputVariable>

        <isRequired>true</isRequired>

        <masterLabel>Case Origin</masterLabel>

        <objectLookupDomain>Case</objectLookupDomain>

      </items>

      <items>

        <catalogInputVariable>Input_Priority</catalogInputVariable>

        <displayType>Picklist</displayType>

        <fieldDefinition>Priority</fieldDefinition>

        <isAdditionalQuestionsInputVariable>false</isAdditionalQuestionsInputVariable>

        <isRequired>false</isRequired>

        <masterLabel>Case Priority</masterLabel>

        <objectLookupDomain>Case</objectLookupDomain>

      </items>

      <items>

        <catalogInputVariable>Input_Status</catalogInputVariable>

        <displayType>Picklist</displayType>

        <fieldDefinition>Status</fieldDefinition>

        <isAdditionalQuestionsInputVariable>false</isAdditionalQuestionsInputVariable>

        <isRequired>true</isRequired>

        <masterLabel>Case Status</masterLabel>

        <objectLookupDomain>Case</objectLookupDomain>

      </items>

      <items>

        <catalogInputVariable>Input_Subject</catalogInputVariable>

        <displayType>Text</displayType>

        <isAdditionalQuestionsInputVariable>false</isAdditionalQuestionsInputVariable>

        <isRequired>true</isRequired>

        <masterLabel>Case Subject</masterLabel>

      </items>

      <items>

        <catalogInputVariable>Input_Description</catalogInputVariable>

        <displayType>Text</displayType>

        <isAdditionalQuestionsInputVariable>true</isAdditionalQuestionsInputVariable>

        <isRequired>false</isRequired>

        <masterLabel>Case Description</masterLabel>

      </items>

      <masterLabel>Create Case by Record Type</masterLabel>

   </SvcCatalogFulfillmentFlow>

```


### Metadata Types SvcCatalogItemDef

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### SvcCatalogItemDef

Represents the entity associated with a specific, individual service available in the Service Catalog.

File Suffix and Directory Location

### SvcCatalogItemDef components have the suffix catalogItem and are stored in the svcCatalogItems folder.

Version

### SvcCatalogItemDef components are available in API version 53.0 and later.

Fields

**Field Name** **Description**

```
apiVersion

catalogFilterCriteria

categories

dataCategories

```

**Field Type**
double

**Description**
The API version in which this catalog item was created. The value for this field updates
based on the value of `fulfillmentFlow` . For catalog items created before version
57.0, the value for this field is `null` . Available in version 57.0 and later.

**Field Type**
### SvcCatalogItemDefFiltrCrit[]

**Description**
The eligibility rule associated with a catalog item. Eligibility rules customize access to
catalog items for different audiences, based on the User object. Available in API version
59.0 and later.

**Field Type**

SvcCatalogCategoryItem[]

**Description**
A list of catalog categories that contain this catalog item.

**Field Type**
### SvcCatalogItemDefDataCategorySelection[]

**Description**
A list of data categories for this catalog item. Available in API version 59.0 and later.


Metadata Types SvcCatalogItemDef

**Field Name** **Description**

```
description

flow

fulfillmentFlow

image

inputs

internalNotes

isAvailableToAllCustomers

```

**Field Type**
string

**Description**
Description of the catalog item.

**Field Type**
string

**Description**
The screen flow associated with the catalog item. Available in API version 53.0 to 58.0.

**Field Type**
string

**Description**
Name of the related `SvcCatalogFulfillmentFlow` on page 2351, which
represents the flow associated with a specific catalog item in the Service Catalog.
Available in API version 56.0 and later.

**Field Type**
string

**Description**
The developer name of a content document to be displayed in the Service Catalog
for this item.

**Field Type**

SvcCatalogItemAttribute[]

**Description**
Represents attributes of a catalog item version. Available in API version 57.0 and later.

**Field Type**
string

**Description**
Intended to describe what the catalog item does and its implementation. That value
is meant for other catalog builders.

**Field Type**
boolean

**Description**
Required. Controls catalog item access for internal users. To share with all internal
users, set the value to `True` . This value corresponds to the **Allow Access for All**
**Users** option for Internal Access in the Catalog Item Builder. Available in API version
61.0 and later.


Metadata Types SvcCatalogItemDef

**Field Name** **Description**

```
isFeatured

isGuestAccessible

isProtected

masterLabel

sharedTo

status

```

**Field Type**
boolean

**Description**
Determines if the catalog item is part of the featured catalog items.

**Field Type**
boolean

**Description**
Required. Controls catalog item access for guest users. To share with guests, set the
value to `True` . This value corresponds to **Guest Visibility** option for External Access
in the Catalog Item Builder. Available in API version 61.0 and later.

**Field Type**
boolean

**Description**
An auto-generated value. This value has no impact.

**Field Type**
string

**Description**
Required. The primary label for the catalog item record.

**Field Type**

SharedTo on page 2292

**Description**
Describes how the catalog item is shared across multiple catalog categories.
SvcCatalogItemDef only supports sharing with groups.

**Field Type**
PublishStatusType (enumeration of type string)

**Description**

Required. Displays the publishing status of a catalog item.

Values are:

**•** `Deprecated`

**•** `Draft`

**•** `PendingChanges`

**•** `Published`


Metadata Types SvcCatalogItemDef

SvcCatalogItemDefFiltrCrit

Represents the association of an eligibility rule with a catalog item. Eligibility rules customize access to catalog items for different
audiences, based on the User object. Available in version 59.0 and later.

**Field Name** **Description**

```
svcCatalogFilterCriteria

```

**Field Type**
string

**Description**
The name of the associated `catalogFilerCriteria` eligibility filter.

SvcCatalogCategoryItem

Represents the assignment of this service to a category within the Service Catalog.

**Field Name** **Description**

```
isPrimaryCategory

sortOrder

svcCatalogCategory

```

**Field Type**
boolean

**Description**
Determines if the catalog category ( `svcCatalogCategory` ) is the primary category
for this catalog item. Exactly one category per SvcCatalogItemDef component must
set this attribute to true.

**Field Type**
int

**Description**
The position of the catalog item relative to other catalog items in the catalog category.

**Field Type**
string

**Description**

Required. The catalog category the catalog item is assigned to.

SvcCatalogItemDefDataCategorySelection

Represents a list of data categories for this catalog item. This subtype is available in API version 59.0 and later.

**Field Name** **Description**

```
category

```

**Field Type**
string


Metadata Types SvcCatalogItemDef

**Field Name** **Description**

**Description**

API name of a data category.

```
categoryGroup

```

SvcCatalogItemAttribute

**Field Type**
string

**Description**

API Name of a data category group.

Represents an attribute of a catalog item version. It can be a static input filled by the catalog builder user or additional questions that
end users answer at runtime. Available in API version 57.0 and later.

**Field Name** **Description**

```
field

inputType

```

**Field Type**
string

**Description**

Applicable when the display type is Lookup/Reference.

**Field Type**
SvcCatalogItemAttrDataType (enumeration of type string)

**Description**

Required.

Values are:

**•** `Attachment`

**•** `Checkbox`

**•** `Currency`

**•** `Date`

**•** `Datetime`

**•** `DisplayText`

**•** `Email`

**•** `IPAddress`

**•** `Integer`

**•** `ListOfAttachment` (available in API version 65.0 and later)

**•** `ListOfBoolean`

**•** `ListOfDouble`

**•** `ListOfInteger`

**•** `ListOfMaps`


Metadata Types SvcCatalogItemDef

**Field Name** **Description**

**•** `ListOfString`

**•** `Lookup`

**•** `Map`

**•** `MultilineText`

**•** `MultiSelectPicklist` (available in API version 65.0 and later)

**•** `Number`

**•** `NumericScale`

**•** `Password` (available in API version 65.0 and later)

**•** `Percentage`

**•** `Picklist`

**•** `Queue`

**•** `RadioButton` (available in API version 65.0 and later)

**•** `SingleCheckbox` (available in API version 59.0 and later)

**•** `SinglelineText`

**•** `Text`

**•** `Toggle` (available in API version 59.0 and later)

**•** `Url`

```
inputVariable

isRequired

label

maxValue

```

**Field Type**
string

**Description**

References the input variable to which the attribute value is forwarded.

**Field Type**
boolean

**Description**

Determines if an answer is required for this question.

**Field Type**
string

**Description**

A translatable label for rendering the attribute to users.

**Field Type**
double

**Description**

Applicable when the display type is slider.


Metadata Types SvcCatalogItemDef

**Field Name** **Description**

```
minValue

name

object

options

type

value

```

**Field Type**
double

**Description**

Applicable when the display type is slider.

**Field Type**
string

**Description**

Required. Applicable when the display type is Lookup/Reference.

**Field Type**
string

**Description**
A picklist object’s custom API Name. Applies when `inputType` is set to `Picklist` .

**Field Type**
SvcCatalogItemAttrDetail

**Description**
The values attached to an attribute of an item version.

**Field Type**
SvcCatalogItemAttrType (enumeration of type string)

**Description**

Required. Type of the attribute; used to determine if it's a pre-filled input or questions
to ask users.

Values are:

**•** `FulfillmentInput`

**•** `UserQuestion`

**Field Type**
string

**Description**

Attribute value defined by the catalog builder.

SvcCatalogItemAttrDetail

Represents the details for an attribute of an item version. Used for options displayed in picklist or checkbox groups.


Metadata Types SvcCatalogItemDef

**Field Name** **Description**

```
isDefault

label

value

```

**Field Type**
boolean

**Description**

Required. Marks the attribute detail as the default. Applicable when the input display
type is picklist or checkbox.

**Field Type**
string

**Description**

Required. Picklist option label when the input type is picklist or checkbox.

**Field Type**
string

**Description**

Attribute value defined by the catalog builder.

Declarative Metadata Sample Definition

The following is an example of a SvcCatalogItemDef component.

```
<SvcCatalogItemDef xmlns="http://soap.sforce.com/2006/04/metadata">

   <apiVersion>57.0</apiVersion>

   <categories>

     <isPrimaryCategory>true</isPrimaryCategory>

     <sortOrder>3</sortOrder>

     <svcCatalogCategory>Category1</svcCatalogCategory>

   </categories>

   <dataCategories>

     <category>France</category>

     <categoryGroup>World</categoryGroup>

   </dataCategories>

   <masterLabel>Item Draft Update</masterLabel>

   <description>Item with a Draft state</description>

   <fulfillmentFlow>TestQuestions</fulfillmentFlow>

   <isFeatured>false</isFeatured>

   <isProtected>false</isProtected>

   <status>Published</status>

   <inputs>

     <name>Input1</name>

     <type>FulfillmentInput</type>

     <inputVariable>input1</inputVariable>

     <label>Input Static</label>

     <inputType>Text</inputType>

     <isRequired>false</isRequired>

   </inputs>

   <inputs>

```


### Metadata Types SynonymDictionary

```
        <type>UserQuestion</type>

        <inputType>Picklist</inputType>

        <isRequired>false</isRequired>

        <label>My First Question</label>

        <name>first_question</name>

        <options>

           <label>Option 1</label>

           <value>option_1</value>

           <isDefault>true</isDefault>

        </options>

        <options>

           <label>Option 2</label>

           <value>option_2</value>

           <isDefault>false</isDefault>

        </options>

        <options>

           <label>Option 3</label>

           <value>option_3</value>

           <isDefault>false</isDefault>

        </options>

      </inputs>

   </SvcCatalogItemDef>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### SynonymDictionary

Represents a set of synonym groups, which are groups of words or phrases that are treated as equivalent in users’ searches. You can
define synonym groups to optimize search results for acronyms, variations of product names, and other terminology unique to your
organization.

Synonyms are available in Service Cloud features such as Salesforce Knowledge. This type extends the Metadata metadata type and
inherits its `fullName` field.

File Suffix and Directory Location

### SynonymDictionary components have the suffix .synonymDictionary and are stored in the synonymDictionaries folder.

Version

### SynonymDictionary components are available in API version 29.0 and later.

Special Access Rules

Synonyms must be enabled in your organization. Only users with the “Manage Synonyms” permission can access this object.


Metadata Types SynonymDictionary

Fields

**Field Name** **Field Type** **Description**

`groups` SynonymGroup The synonym groups defined in this dictionary.

`isProtected` boolean

Indicates whether this component is protected ( `true` ) or not ( `false` ).
Protected components cannot be linked to or referenced by components
created in the installing organization.

`label` string Required. Specifies the display name of the synonym dictionary.

SynonymGroup

Represents a group of synonymous words or phrases.

**Field Name** **Field Type** **Description**

`languages` Language on page Required. Specifies the languages the synonym group applies to. If synonyms
2390 are specific to a single language, specify only that language. If the synonyms

apply to multiple languages, specify multiple languages for one synonym
group.

`terms` string

Required. A word or phrase synonymous with other terms in the group.
Maximum of 50 characters. Minimum of two `terms` per group.

Synonym groups are symmetric, which means that if oranges and apples are
defined in a synonym group, a search for _`oranges`_ will return a match for
_`apples`_, and vice versa for a search for _`apples`_ .

Declarative Metadata Sample Definition

The following is an example of a SynonymDictionary component:

```
<?xml version="1.0" encoding="UTF-8"?>

<SynonymDictionary xmlns="http://soap.sforce.com/2006/04/metadata">

   <groups>

     <languages>en_US</languages>

     <terms>Salesforce</terms>

     <terms>salesforce.com</terms>

     <terms>The Customer Company</terms>

     <terms>SFDC</terms>

   </groups>

   <groups>

     <languages>fr</languages>

     <terms>renault</terms>

     <terms>clio</terms>

   </groups>

   <label>Sample Dictionary</label>

</SynonymDictionary>

```


### Metadata Types Territory

The following is an example `package.xml` that references the SynonymDictionary component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Sample Dictionary</members>

        <name>SynonymDictionary</name>

      </types>

      <version>66.0</version>

   </Package>

```

Usage

If you have existing synonym groups defined before API version 29.0, your existing groups are associated with a default dictionary called
`_Default` .

If you have a set of synonyms that require frequent updates, we recommend assigning the synonym group or groups to a dedicated
dictionary with a small number of groups. Each time you deploy an existing dictionary, all of its synonym groups are overwritten. We
don’t support deploying updates to only a single synonym group within a dictionary.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### Territory

Represents a territory.

Declarative Metadata File Suffix and Directory Location

The file suffix for territory components is `.territory` and components are stored in the `territories` directory of the
corresponding package directory.

Version

### Territory components are available in API version 24.0 and later.

Fields

This metadata type extends to subtype RoleOrTerritory.

**Field Name** **Field Type** **Description**

`accountAccessLevel` string Specifies whether users in this territory can access accounts that are
assigned to this territory and are otherwise inaccessible. Valid values are:

**•** `Read`

**•** `Edit`


### Metadata Types Territory2

**Field Name** **Field Type** **Description**

**•** `All`

If your organization’s sharing model for accounts is Public Read/Write,
valid values are only `Edit` and `All` .

If no value is set for this field, this field value uses the default access level
that is specified in the Manage Territory page in Setup.

This field is available in API version 31.0 and later.

`fullName` string The unique identifier for API access. The `fullName` can contain only
underscores and alphanumeric characters. It must be unique, begin with

a letter, not include spaces, not end with an underscore, and not contain
two consecutive underscores. This field is inherited from the Metadata
component. Corresponds to **Territory Name** in the user interface.

`parentTerritory` string The territory above this territory in the territory hierarchy.

Declarative Metadata Sample Definition

The following is the definition of a territory.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Territory xmlns="http://soap.sforce.com/2006/04/metadata">

      <accountAccessLevel>Edit</accountAccessLevel>

      <caseAccessLevel>Edit</caseAccessLevel>

      <contactAccessLevel>Edit</contactAccessLevel>

      <description>Sample Territory</description>

      <mayForecastManagerShare>false</mayForecastManagerShare>

      <name>T22name</name>

      <opportunityAccessLevel>Read</opportunityAccessLevel>

   </Territory>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### Territory2

Represents the metadata associated with a sales territory. This type extends the Metadata metadata type and inherits its `fullName`
field. Available if Sales Territories has been enabled.

File Suffix and Directory Location

### Territory2 components have the suffix territory2 and are stored in the territories folder under the folder for the corresponding Territory2Model.


Metadata Types Territory2

Version

Territory2 components are available in API version 32.0 and later.

Special Access Rules

The Territory2Model object has a `State` field in the SOAP API. States include `Planning`, `Active`, `Archived`, and several other
states, such as `Cloning`, that indicate that a process is underway. Users who do not have the Manage Territories permission can access
territories that belong to the model in `Active` state. The Manage Territories permission is required for `deploy()` calls for all territory
management entities. Using `retrieve()` without the Manage Territories permission returns only entities that belong to a
Territory2Model in `Active` state. We recommend against retrieving without the Manage Territories permission because the call
retrieves only partial data.

Fields

**Field Name** **Field Type** **Description**

`accountAccessLevel` string

`caseAccessLevel` string

`contactAccessLevel` string

Specifies whether users in this territory can access accounts that are
assigned to this territory and are otherwise inaccessible. Valid values
are:

**•** `Read`

**•** `Edit`

**•** `All`

If your organization’s sharing model for accounts is Public Read/Write,
valid values are only `Edit` and `All` . If no value is set for this field,
this field value uses the default access level that is specified in
Territory2Settings as permitted by the organization’s sharing settings.

Specifies whether users in this territory can access cases that are
assigned to this territory and are otherwise inaccessible. Valid values
are:

**•** `None`

**•** `Read`

**•** `Edit`

Specify no value if your organization’s sharing model for
cases/opportunities is Public Read/Write. If no value is set for this field,
this field value uses the default access level that is specified in
Territory2Settings as permitted by the organization’s sharing settings.

Specifies whether users in this territory can access contacts that are
assigned to this territory and are otherwise inaccessible. Valid values
are:

**•** `None`

**•** `Read`

**•** `Edit`


Metadata Types Territory2

**Field Name** **Field Type** **Description**

Specify no value if your organization’s sharing model for contacts is
Public Read/Write or Controlled By Parent.

`customFields` FieldValue

Values for custom fields defined on the Territory2 object and used by
this territory. Their metadata is captured separately in CustomObject.
Note the following:

**•** Territory2 and Territory2Model objects do not handle values for
Text Area (Long), Text Area (Rich), and text-encrypted custom fields.

**•** Fields are referenced using their API names. Compound field types
like Location appear as their constituent column fields. For example,
`nnn_Latitude__s`, `nnn_Longitude__s` where “nnn” is
the field name and the suffixes are the geolocation components.

**•** Values of required custom fields are enforced during the
`deploy()` operation.

`description` string A description of the territory.

`name` string Required. The user interface label for the territory.

`objectAccessLevels` Territory2AccessLevel Represents the user access levels of an object associated to a territory.
Available in API version 57.0 and later.

`opportunityAccessLevel` string

Specifies whether users in this territory can access opportunities that
are assigned to this territory and are otherwise inaccessible. Valid values
are:

**•** `None`

**•** `Read`

**•** `Edit`

Specify no value if your organization’s sharing model for
cases/opportunities is Public Read/Write. If no value is set for this field,
this field value uses the default access level that is specified in
Territory2Settings as permitted by the organization’s sharing settings.

`parentTerritory` string The name of the territory’s parent. When you specify the parent territory,
use the developer name. Do not use the “fully qualified” name. Custom

fields with no values are retrieved with values of type: `<value`
`xsi:nil="true"/>` . You can also use `<value`
`xsi:nil="true"/>` syntax to remove existing values in custom
fields.

`ruleAssociations` Territory2RuleAssociation[] Represents an object assignment rule and its association to a territory.
Use the developer name of the rule.

`territory2Type` string Required. The territory type that the territory belongs to.

FieldValue

Represents the values of custom fields on the Territory2 object. Available in API version 32.0 and later.


Metadata Types Territory2

**Field Name** **Field Type** **Description**

`name` string Required. The user interface label for the territory.

`value` any type The value of the field, which can also be `null` . The field type is specified in
the XML and depends on the field value.

Territory2AccessLevel

Represents the association of an object access level to a territory. Available in API version 57.0 and later.

**Field Name** **Field Type** **Description**

`accessLevel` string Required. Valid values are:

**•** `Read`

**•** `Edit`

**•** `Transfer`

**•** `All`

If your organization’s sharing model for accounts is Public Read/Write, valid
values are only `Edit` and `All` . If no value is set for this field, this field value
uses the default access level that is specified in Territory2Settings as permitted
by the organization’s sharing settings.

`objectType` string Required. The type of object associated to the territory. For example, Lead.

Territory2RuleAssociation

Represents the association of an object assignment rule to a territory. Available in API version 32.0 and later.

**Field Name** **Field Type** **Description**

`inherited` boolean

`ruleName` string

Required. Indicates whether the rule is inherited from a parent territory ( `true` )
or local to the current territory ( `false` ).

Rule inheritance flows from the parent territory where the rule is created to
the rule’s descendent territories, if any, in the territory model hierarchy. A local
rule is created within a single territory and affects that territory only.

Required. The name of a rule associated with the territory. It isn’t necessary to
fully qualify `ruleName` because Metadata API assumes that the rule belongs
to the same model as the territory.

Declarative Metadata Sample Definition

The following example shows the definition of a Territory2 component.

```
<?xml version="1.0" encoding="UTF-8"?>

<Territory2 xmlns="http://soap.sforce.com/2006/04/metadata"

```


Metadata Types Territory2

```
   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

   xmlns:xsd="http://www.w3.org/2001/XMLSchema">

      <name>USA</name>

      <description>United States sales</description>

      <accountAccessLevel>Edit</accountAccessLevel>

      <opportunityAccessLevel>Read</opportunityAccessLevel>

      <caseAccessLevel>Edit</caseAccessLevel>

      <contactAccessLevel>Edit</contactAccessLevel>

      <parentTerritory>Worldwide_Sales</parentTerritory>

      <territory2Type>Geo</territory2Type>

      <objectAccessLevels>

        <accessLevel>All</accessLevel>

        <objectType>Lead</objectType>

      </objectAccessLevels>

      <ruleAssociations>

        <ruleName>AccRule1</name>

        <inherited>True</inherited>

      </ruleAssociations>

      <ruleAssociations>

        <ruleName>AccRule2</name>

        <inherited>False</inherited>

      </ruleAssociations>

      <customFields>

        <name>Activation_DateTime__c</name>

        <value xsi:type="xsd:dateTime">2014-07-16T05:05:00.000Z</value>

      </customFields>

      <customFields>

        <name>AutoNumber__c</name>

        <value xsi:type="xsd:string">T# 000001</value>

      </customFields>

      <customFields>

        <name>DeactivationDate__c</name>

        <value xsi:type="xsd:date">2016-07-12</value>

      </customFields>

      <customFields>

        <name>External_Id__c</name>

        <value xsi:type="xsd:string">AB2345</value>

      </customFields>

      <customFields>

        <name>ManagersPhone__c</name>

        <value xsi:nil="true"/>

      </customFields>

   </Territory2>

```

The following is a `package.xml` sample. _`FY13`_ and _`FY14`_ represent the names of territory models and demonstrate that rules
can have identical developer names within different models. A wildcard character (*) in place of the model name can be used to retrieve
all rules in all models in an organization.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>FY13</members>

        <members>FY14</members>

        <name>Territory2Model</name>

```


### Metadata Types Territory2Model

```
      </types>

      <types>

        <members>FY13.USA</members>

        <members>FY13.Worldwide_Sales</members>

        <members>FY14.APAC</members>

        <members>FY14.USA</members>

        <name>Territory2</name>

      </types>

      <version>66.0</version>

   </Package>

```

Usage

**•** Triggers defined on Territory2 do _not_ fire during a `deploy()` operation unless there is a deployment failure. For example, when
a child territory references a parent and deploys before the parent territory, the failed components try to deploy again one at a time,
allowing triggers to run.

**•** Sales Territories components don’t support packaging or change sets and aren’t supported in CRUD calls.

### • For unlocked packaging, Territory2 requires packages without a namespace.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### Territory2Model

Represents the metadata associated with a territory model in Sales Territories.This type extends the Metadata metadata type and inherits
its `fullName` field. Available if Sales Territories has been enabled.

File Suffix and Directory Location

### Territory2Model components have the suffix territory2Model and are stored in the territory2Models folder.

Version

### Territory2Model components are available in API version 32.0 and later.

Special Access Rules

The Territory2Model object has a `State` field in the SOAP API. States include `Planning`, `Active`, `Archived`, and several other
states, such as `Cloning`, that indicate that a process is underway. Users who do not have the Manage Territories permission can access
models in `Active` state. The Manage Territories permission is required for `deploy()` calls for all territory management entities.
Using `retrieve()` without the Manage Territories permission returns only entities that belong to a Territory2Model in `Active`
state. We recommend against retrieving without the Manage Territories permission because the call retrieves only partial data.


Metadata Types Territory2Model

Fields

**Field Name** **Field Type** **Description**

`customFields` FieldValue Custom fields defined on the Territory2Model object and used by this
model. Their metadata is captured separately.

**•** Territory2 and Territory2Model objects do not handle values for Text
Area (Long), Text Area (Rich), and text-encrypted custom fields.

**•** Fields are referenced using their API names. Compound field types
like Location appear as their constituent column fields. For example,
`nnn_Latitude__s`, `nnn_Longitude__s` where “nnn” is
the field name and the suffixes are the geolocation components.

**•** Values of required custom fields are enforced during the
`deploy()` operation.

`description` string A description for the territory model.

`name` string Required. The user interface label for the territory model.

Declarative Metadata Sample Definition

The following example shows the definition of a Territory2Model component.

```
   <?xml version="1.0" encoding="UTF-8"?>

      <Territory2Model xmlns="http://soap.sforce.com/2006/04/metadata"

   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

   xmlns:xsd="http://www.w3.org/2001/XMLSchema">

      <name>FY13</name>

      <description>Geographic allocation</description>

      <customFields>

        <name>Activation_DateTime__c</name>

        <value xsi:type="xsd:dateTime">2014-07-16T05:05:00.000Z</value>

      </customFields>

      <customFields>

        <name>AutoNumber__c</name>

        <value xsi:type="xsd:string">M# 000001</value>

      </customFields>

      <customFields>

        <name>DeactivationDate__c</name>

        <value xsi:type="xsd:date">2016-07-12</value>

      </customFields>

      <customFields>

        <name>External_Id__c</name>

        <value xsi:nil="true"/>

      </customFields>

   </Territory2Model>

```


### Metadata Types Territory2Rule

Usage

**•** The `retrieve()` call _does not_ return models in these four states: `Cloning`, `Cloning Failed`, `Deleting`, and `Deletion`
`Failed` .

**•** Whenever a model is created, its initial state is `Planning` . You can only do a `deploy()` operation for models in `Planning`
or `Active` state. The same requirement applies to territories and rules associated with those models. For example, sometimes
you can have a model in `Planning` state on a sandbox org, and a model with the same developer name in `Archived` state
on your production org. The `deploy()` operation on production fails because that model’s state is `Archived` and that state
prevents changes to the model.

**•** Because of the state restrictions, if you have territory models in different orgs with identical developer names and you attempt a
`deploy()` operation, Metadata API attempts to create new models. However, that operation fails because of the developer name
conflict. For example, sometimes you can have a model in `Planning` state on a sandbox org, and a model with the same developer
name in `Archived` state on your production org. The `deploy()` operation on production fails because that model’s state is
`Archived` and that state prevents changes to the model.

**•** If you try to delete a model that has territories, then the `delete()` call changes the model’s state to `Deleting` and cascade
deletes all territories, rules, and user associations in the model. Deleting can take some time depending on the number of territories
in the model.

**•** Whenever a model is created, its initial state is `Planning` . If a model with the same developer name already exists, it already has
a state, so we do not include the `State` field in Territory2.

**•** Sales Territories components don’t support packaging or change sets and aren’t supported in CRUD calls.

**•** Namespaces aren’t supported for unlocked packages.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### Territory2Rule

Represents the metadata associated with a territory assignment rule associated with an object, such as Account. Available if Sales
Territories has been enabled.

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### Territory2Rule components have the suffix territory2Rule and are stored in the rules folder under the folder for the

corresponding Territory2Model.

Version

### Territory2Rule components are available in API version 32.0 and later.


Metadata Types Territory2Rule

Special Access

The Territory2Model object has a `State` field in SOAP API. States include `Planning`, `Active`, `Archived`, and several other
states, such as `Cloning`, that indicate that a process is underway. Users who don’t have the Manage Territories permission can access
rules that belong to the model in `Active` state. The Manage Territories permission is required for `deploy()` calls for all territory
management entities, in addition to the permissions required by Metadata API. Using `retrieve()` without the Manage Territories
permission returns only entities that belong to a Territory2Model in `Active` state. We recommend against retrieving without the
Manage Territories permission because the call retrieves only partial data.

The SOAP API and the user interface require that a user attempting to create or edit a rule has field-level security access to the fields
referenced in the rule item. This restriction is relaxed for Metadata API `deploy()` operations, as they require both Manage Territories
and either the Modify Metadata Through Metadata API Functions or Modify All Data permissions.

Fields

**Field Name** **Field Type** **Description**

`active` boolean Required. Indicates whether the rule is active ( `true` ) or inactive
( `false` ). Via the API, active rules run automatically when object records

are created and edited. The exception is when the value of the
`IsExcludedFromRealign` field on an object record is `true`,
which prevents record assignment rules from evaluating that record.

`booleanFilter` string An advanced filter condition. For example: `(1 AND 2) OR 3` .
Numbering must start at 1 and must be contiguous.

`name` string Required. The user interface label for the rule.

`objectType` string Required. The object that the rule is defined for. For API version 32.0, the
only available object is Account.

`ruleItems` Territory2RuleItem The items that define a rule’s the selection criteria, such as `Billing`
on page 2375 `State equals California` .

Territory2RuleItem

Represents the association of a rule item to a rule. Available in API version 32.0 and later.

**Field Name** **Field Type** **Description**

`field` string The standard or custom object field that the rule item operates on.

```
operation

```

FilterOperation The criterion to apply for the rule item. For example: _`equals`_ or _`starts`_
(enumeration of type _`with`_ . Valid values are:
string)

**•** `equals`

**•** `notEqual`

**•** `lessThan`

**•** `greaterThan`

**•** `lessOrEqual`


Metadata Types Territory2Rule

**Field Name** **Field Type** **Description**

**•** `greaterOrEqual`

**•** `contains`

**•** `notContain`

**•** `startsWith`

**•** `includes`

**•** `excludes`

**•** `within` ( `DISTANCE` criteria only)

`value` string The field value or values to evaluate. For example: if the field is `Billing`
`ZIP/Postal Code`, a value could be `94105` .

Declarative Metadata Sample Definition

The following example shows the definition of a Territory2RuleItem component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Territory2Rule xmlns="http://soap.sforce.com/2006/04/metadata">

      <label>Northern CA</label>

      <description>To capture northern CA based accounts</description>

      <objectType>Account</objectType>

      <active>True</active>

      <ruleItems>

        <field>BillingZip</field>

        <operation>contains</operation>

        <value><94105,94404,94536/value>

      </ruleItems>

      <ruleItems>

        <field>Industry</field>

        <operation>equals</operation>

        <value>IT</value>

      </ruleItems>

      <ruleItems>

        <field>someCustomField__c</field>

        <operation>greater_than</operation>

        <value>50000</value>

      </ruleItems>

      <booleanFilter>(1 OR 2) AND 3</booleanFilter>

   </Territory2Rule>

```

The following is a `package.xml` sample. _`FY13`_ and _`FY14`_ represent names of territory models and demonstrate that rules can
have _identical_ developer names within _different_ models. A wildcard character (*) in place of the model name can be used to retrieve all
rules in all models in an org.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

        <types>

           <members>FY13</members>

```


### Metadata Types Territory2Type

```
           <members>FY14</members>

           <name>Territory2Model</name>

        </types>

        <types>

           <members>FY13.AccRule1</members>

           <members>FY14.AccRule1</members>

           <name>Territory2Rule</name>

        </types>

        <version>66.0</version>

   </Package>

```

Usage

**•** A territory rule can have up to 10 rule items.

**•** The sort order of rule items is implicitly derived from the position of the rule items in the XML

**•** Rules can’t be run via Metadata API.

**•** Territory Management 2.0 components don’t support packaging or change sets and aren’t supported in CRUD calls.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### Territory2Type

Represents the metadata for a category of territories in Sales Territories. Every Territory2 must have a Territory2Type. This type extends
the Metadata metadata type and inherits its `fullName` field. Available if Sales Territories has been enabled.

File Suffix and Directory Location

### Territory2Type components have the suffix territory2Type and are stored in the territory2Types folder.

Version

### Territory2Type components are available in API version 32.0 and later.

Special Access Rules

The Manage Territories permission is required for the `deploy()` operation, but not `retrieve()` . The `retrieve()` operation
retrieves all the Territory2Type components in the org.


### Metadata Types TimelineObjectDefinition

Fields

**Field Name** **Field Type** **Description**

`description` string A description of the territory type.

`name` string Required. The user interface label for the territory type.

`priority` int Required. Used for Filter-Based Opportunity Territory Assignment
(Pilot in Spring ’15 / Metadata API version 33). Lets you specify a

priority for a territory type. For opportunity assignments, the filter
examines all territories assigned to the account that the opportunity
is assigned to. The account-assigned territory whose territory type
priority is highest is then assigned to the opportunity. The
`priority` field value on each territory type must be unique.
Further, if there are multiple territories with the same territory type,
and therefore the same priority, assigned to the account, no territory
is not assigned to the opportunity.

Declarative Metadata Sample Definition

The following example shows the definition of a Territory2Type component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Territory2Type xmlns="http://soap.sforce.com/2006/04/metadata">

      <name>Geo</name>

      <description>Geographic allocation</description>

   </Territory2Type>

```

Usage

Sales Territories components don’t support packaging or change sets and aren’t supported in CRUD calls.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### TimelineObjectDefinition

Represents the container that stores the details of a timeline configuration. You can use this resource with Salesforce objects to see their
records' related events in a linear time-sorted view.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.


Metadata Types TimelineObjectDefinition

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

TimelineObjectDefinition components have the suffix `.timelineObjectDefinition` and are stored in the
`timelineObjectDefinitions` folder.

Version

TimelineObjectDefinition components are available in API version 55.0 and later.

Special Access Rules

TimelineObjectDefinition is available in any org that has the Timeline org preference enabled.

Fields

**Field Name** **Description**

```
baseObject

definition

isActive

masterLabel

```

**Field Type**
string

**Description**
Required.

The object on which a timeline is based. Information displayed in a timeline comes
from objects that are related to the base object. The base object can be a Salesforce
object or custom object.

**Field Type**
string

**Description**
Required.

The timeline definition in JSON format.

**Field Type**
boolean

**Description**
Indicates whether the timeline is active ( `true` ) or not ( `false` ).

**Field Type**
string

**Description**
Required.


Metadata Types TimelineObjectDefinition

**Field Name** **Description**

The user interface label of the timeline object definition record.

Declarative Metadata Sample Definition

The following is an example of a TimelineObjectDefinition component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <TimelineObjectDefinition

    xmlns="http://soap.sforce.com/2006/04/metadata">

    <baseObject>Account</baseObject>

   <definition>{&quot;timeline&quot;:{&quot;anchorObject&quot;:{&quot;object&quot;:{&quot;entity&quot;:&quot;Account&quot;,&quot;label&quot;:&quot;Account&quot;,&quot;source&quot;:&quot;&quot;,&quot;icon&quot;:&quot;&quot;}},&quot;age&quot;:{&quot;field&quot;:&quot;EffectiveDate&quot;,&quot;label&quot;:&quot;Effective

   Date&quot;,&quot;type&quot;:&quot;DateTime&quot;},&quot;events&quot;:[{&quot;oneToMany&quot;:{&quot;eventObject&quot;:{&quot;name&quot;:&quot;Case&quot;,&quot;label&quot;:&quot;Case&quot;,&quot;recordTypes&quot;:[],&quot;fieldsToDisplay&quot;:[{&quot;field&quot;:&quot;Description&quot;,&quot;label&quot;:&quot;Description&quot;,&quot;type&quot;:&quot;StringPlusClob&quot;},{&quot;field&quot;:&quot;Priority&quot;,&quot;label&quot;:&quot;Priority&quot;,&quot;type&quot;:&quot;DynamicEnum&quot;},{&quot;field&quot;:&quot;Status&quot;,&quot;label&quot;:&quot;Status&quot;,&quot;type&quot;:&quot;DynamicEnum&quot;},{&quot;field&quot;:&quot;Subject&quot;,&quot;label&quot;:&quot;Subject&quot;,&quot;type&quot;:&quot;Text&quot;}],&quot;relatedlistsToDisplay&quot;:[{&quot;entity&quot;:&quot;CaseCo m ents&quot;,&quot;label&quot;:&quot;Case

   Comments&quot;},{&quot;entity&quot;:&quot;CombinedAttachments&quot;,&quot;label&quot;:&quot;Attachments&quot;},{&quot;entity&quot;:&quot;AttachedContentDocuments&quot;,&quot;label&quot;:&quot;Files&quot;}],&quot;title&quot;:{&quot;field&quot;:&quot;CaseNumber&quot;,&quot;label&quot;:&quot;Case

   Number&quot;,&quot;type&quot;:&quot;AutoNumber&quot;},&quot;subTitle&quot;:{&quot;field&quot;:&quot;Comments&quot;,&quot;label&quot;:&quot;Internal

   Comments&quot;,&quot;type&quot;:&quot;MultiLineText&quot;}},&quot;filters&quot;:[{&quot;field&quot;:{&quot;field&quot;:&quot;Status&quot;,&quot;label&quot;:&quot;Status&quot;,&quot;type&quot;:&quot;DynamicEnum&quot;},&quot;operator&quot;:&quot;EQ&quot;,&quot;values&quot;:[&quot;New&quot;],&quot;order&quot;:1}],&quot;sort&quot;:{&quot;field&quot;:&quot;CreatedDate&quot;,&quot;label&quot;:&quot;Created

   Date&quot;,&quot;type&quot;:&quot;DateTime&quot;},&quot;anchorReferenceField&quot;:{&quot;field&quot;:&quot;AccountId&quot;,&quot;label&quot;:&quot;Account

   ID&quot;,&quot;type&quot;:&quot;EntityId&quot;}}},{&quot;oneToMany&quot;:{&quot;eventObject&quot;:{&quot;name&quot;:&quot;Event&quot;,&quot;label&quot;:&quot;Event&quot;,&quot;recordTypes&quot;:[],&quot;fieldsToDisplay&quot;:[{&quot;field&quot;:&quot;ActivityDate&quot;,&quot;label&quot;:&quot;Due

    Date

   Only&quot;,&quot;type&quot;:&quot;DueDate&quot;},{&quot;field&quot;:&quot;A t end e s&quot;,&quot;label&quot;:&quot;A t end e s&quot;,&quot;type&quot;:&quot;StringPlusClob&quot;}],&quot;relatedlistsToDisplay&quot;:[],&quot;title&quot;:{&quot;field&quot;:&quot;Description&quot;,&quot;label&quot;:&quot;Description&quot;,&quot;type&quot;:&quot;StringPlusClob&quot;},&quot;subTitle&quot;:{&quot;field&quot;:&quot;Location&quot;,&quot;label&quot;:&quot;Location&quot;,&quot;type&quot;:&quot;Text&quot; },&quot;filters&quot;:[],&quot;sort&quot;:{&quot;field&quot;:&quot;ActivityDate&quot;,&quot;label&quot;:&quot;Due

    Date

   Only&quot;,&quot;type&quot;:&quot;DueDate&quot;},&quot;anchorReferenceField&quot;:{&quot;field&quot;:&quot;WhatId&quot;,&quot;label&quot;:&quot;Related

    To

   ID&quot;,&quot;type&quot;:&quot;EntityId&quot;}}},{&quot;oneToMany&quot;:{&quot;eventObject&quot;:{&quot;name&quot;:&quot;Task&quot;,&quot;label&quot;:&quot;Task&quot;,&quot;recordTypes&quot;:[],&quot;fieldsToDisplay&quot;:[{&quot;field&quot;:&quot;CallDisposition&quot;,&quot;label&quot;:&quot;Call

   Result&quot;,&quot;type&quot;:&quot;Text&quot;},{&quot;field&quot;:&quot;CallObject&quot;,&quot;label&quot;:&quot;Call

    Object

   Identifier&quot;,&quot;type&quot;:&quot;Text&quot;},{&quot;field&quot;:&quot;CallType&quot;,&quot;label&quot;:&quot;Call

   Type&quot;,&quot;type&quot;:&quot;StaticEnum&quot;}],&quot;relatedlistsToDisplay&quot;:[],&quot;title&quot;:{&quot;field&quot;:&quot;Description&quot;,&quot;label&quot;:&quot;Description&quot;,&quot;type&quot;:&quot;StringPlusClob&quot;},&quot;subTitle&quot;:{&quot;field&quot;:&quot;Priority&quot;,&quot;label&quot;:&quot;Priority&quot;,&quot;type&quot;:&quot;DynamicEnum&quot;}},&quot;filters&quot;:[],&quot;sort&quot;:{&quot;field&quot;:&quot;ActivityDate&quot;,&quot;label&quot;:&quot;Due

    Date

   Only&quot;,&quot;type&quot;:&quot;DueDate&quot;},&quot;anchorReferenceField&quot;:{&quot;field&quot;:&quot;WhatId&quot;,&quot;label&quot;:&quot;Related

    To ID&quot;,&quot;type&quot;:&quot;EntityId&quot;}}}]}}</definition>

    <isActive>true</isActive>

    <masterLabel>HealthTimeline</masterLabel>

   </TimelineObjectDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package

    xmlns="http://soap.sforce.com/2006/04/metadata">

    <types>

     <members>*</members>

```


### Metadata Types TimeSheetTemplate

```
     <name>TimelineObjectDefinition</name>

    </types>

    <version>55.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### TimeSheetTemplate

Represents a template for creating time sheets in Field Service. This type extends the Metadata metadata type and inherits its `fullName`
field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### TimeSheetTemplate components have the suffix timeSheetTemplate and are stored in the timeSheetTemplates folder.

Version

### TimeSheetTemplate components are available in API version 46.0 and later.

Special Access Rules

Field Service must be enabled. Users must have the Customize Application and Time Sheet Template permissions.

Fields

**Field Name** **Field Type** **Description**

`active` boolean Required. Indicates whether the time sheet template is active ( `true` )
or not ( `false` ).

`description` string The time sheet template's description.

```
frequency

```

TimeSheetFrequency Required. Defines the frequency of the time sheet creation period. One
(enumeration of of the following values:
type string)

**•** `Daily`

**•** `Weekly`

**•** `EveryTwoWeeks`

**•** `TwiceAMonth`

**•** `Monthly`


Metadata Types TimeSheetTemplate

**Field Name** **Field Type** **Description**

`masterLabel` string Required. The name of the time sheet template.

`startDate` date Required. The date when the time sheet takes effect.

`timeSheetTemplateAssignments` TimeSheetTemplateAssignment A list of profiles that the template is assigned to.

```
workWeekEndDay

workWeekStartDay

```

DaysOfWeek Required. The end day of the template's work week. One of the following
(enumeration of values:
type string)

**•** `Monday`

**•** `Tuesday`

**•** `Wednesday`

**•** `Thursday`

**•** `Friday`

**•** `Saturday`

**•** `Sunday`

DaysOfWeek Required. The start day of the template's work week. One of the following
(enumeration of values:
type string)

**•** `Monday`

**•** `Tuesday`

**•** `Wednesday`

**•** `Thursday`

**•** `Friday`

**•** `Saturday`

**•** `Sunday`

TimeSheetTemplateAssignment

Returns a quick action that’s associated with an EmbeddedServiceLiveAgent setup. The quick action includes the pre-chat form fields
that the embedded chat window displays and shows the order in which the fields are displayed.

**Field Name** **Field Type** **Description**

`assignedTo` string The IDs of the user profiles that a time sheet template is assigned to.

Declarative Metadata Sample Definition

The following is an example of a TimeSheetTemplate file.

```
<?xml version=“1.0” encoding=“UTF-8"?>

<TimeSheetTemplate xmlns=“http://soap.sforce.com/2006/04/metadata“>

  <active>true</active>

  <description>Time Sheet Template description</description>

  <frequency>Daily</frequency>

```


### Metadata Types TopicsForObjects

```
     <masterLabel>label</masterLabel>

     <startDate>2018-10-18</startDate>

     <timeSheetTemplateAssignments>

        <assignedTo>admin</assignedTo>

     </timeSheetTemplateAssignments>

     <timeSheetTemplateAssignments>

        <assignedTo>standard</assignedTo>

     </timeSheetTemplateAssignments>

     <workWeekEndDay>Tuesday</workWeekEndDay>

     <workWeekStartDay>Monday</workWeekStartDay>

   </TimeSheetTemplate>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version=“1.0” encoding=“UTF-8"?>

   <Package xmlns=“http://soap.sforce.com/2006/04/metadata“>

     <types>

        <members>*</members>

        <name>TimeSheetTemplate</name>

     </types>

     <version>46.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### TopicsForObjects

Represents the ability to assign topics to objects or to remove topic assignments.

File Suffix and Directory Location

### TopicsForObjects components have the suffix .topicsForObjects and are stored in the topicsForObjects folder of the

corresponding package directory.

Version

### TopicsForObjects components are available in API version 41.0 and later.


Metadata Types TopicsForObjects

Fields

**Field Name** **Field Type** **Description**

`enableTopics` boolean

Required. When true, indicates whether users can assign topics or remove
topic assignments. When false, users can’t assign or remove topics.

Upon org creation, this value is true for the following objects:

**•** Account

**•** Asset

**•** Campaign

**•** Case

**•** Contact

**•** Content Document

**•** Contract

**•** Event

**•** Lead

**•** Opportunity

**•** Order

**•** Solution

**•** Task

For all remaining standard objects and custom objects, the default is
false.

`entityApiName` string Required. Indicates the object’s API name for enabling topics.

Declarative Metadata Sample Definition

The following is an example of a TopicsForObjects component.

```
<?xml version="1.0" encoding="UTF-8"?>

<TopicsForObjects xmlns="http://soap.sforce.com/2006/04/metadata">

     <enableTopics>false</enableTopics>

     <entityApiName>Account</entityApiName>

</TopicsForObjects>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

<types>

<members>*</members>

<name>TopicsForObjects</name>

</types>

<version>41.0</version>

</Package>

```


### Metadata Types TransactionSecurityPolicy

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### TransactionSecurityPolicy

Represents a transaction security policy definition. Transaction security policies give you a way to look through events in your organization
and specify actions to take when certain combinations occur.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### TransactionSecurityPolicy components have the suffix .transactionSecurityPolicy and are stored in the

`transactionSecurityPolicies` folder.

Version

### TransactionSecurityPolicy components are available in API version 35.0 and later.

Fields

**Field Name** **Field Type** **Description**

`action` TransactionSecurityAction Required. Describes the action to take when the matching
Transaction Security policy is triggered.

`active` boolean Required. If `true`, the policy is enabled and actively monitors its
event.

`apexClass` string Required for Apex-based policies, and optional for all other policies.
The name of the class that implements the

`TxnSecurity.PolicyCondition` or
`TxnSecurity.EventCondition` interface for this policy.
Available in API version 46.0 and later.

`blockMessage` string The custom message sent to a user when a policy blocks their
action. Used in Real-Time Event Monitoring only. Maximum of 1000

characters. This field is null when the default message option is
selected in the UI. Available only when `eventName` is set to
`ApiEvent`, `ListViewEvent`,
`BulkApiResultEventStore`, or `ReportEvent` . Available
in API version 49.0 and later.

Include org- or policy-specific information in your custom message,
such as the name of the responsible administrator or the business


Metadata Types TransactionSecurityPolicy

**Field Name** **Field Type** **Description**

unit. Be careful about what you include. Too much information on
how the policy was designed. can aid a malicious user.

Two-factor authentication (2FA) isn’t supported in Lightning
Experience, so events like `ListView` and `ReportEvent` are
upgraded to Block in Lightning.

Custom messages aren’t translatable.

`customEmailContent` string The administrator-created custom email content sent when a policy
is triggered. Used in Real-Time Event Monitoring only. Maximum

of 1333 characters. This field is null when the Custom Email Content
setting is selected in the UI but no message content is entered.
Available in API version 54.0 and later.

Custom messages aren’t translatable.

`description` string A description of the policy.

`developerName` string This unique name prevents conflicts with other policies that have
the same `masterLabel` . This name can contain only

underscores and alphanumeric characters, and must be unique in
your org. It must begin with a letter, not include spaces, not end
with an underscore, and not contain two consecutive underscores.

Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

`eventName` TransactionSecurityEventName
(enumeration of type string)

Used in Real-Time Event Monitoring only. Indicates the name of
the event the policy monitors. This field is available in API 45.0 and
later. Valid values are:

**•** `ApiEvent` —Tracks these user-initiated read-only API calls:
`query()`, `queryMore()`, and `count()` . Captures API
requests through SOAP API and Bulk API for the Enterprise and
Partner WSDLs. Tooling API calls and API calls originating from
a Salesforce mobile app aren’t captured.

**•** `ApiAnomalyEventStore` —Tracks anomalies in how
users make API calls. ApiAnomalyEventStore is an object that
stores the event data of ApiAnomalyEvent. This object is
available in API version 50.0 and later.

**•** `BulkApiResultEventStore` —Tracks when a user
downloads the results of a Bulk API request.
BulkApiResultEventStore is a big object that stores the event
data of BulkApiResultEvent. This object is available in API
version 50.0 and later.

**•** `CredentialStuffingEventStore` —Tracks when a
user successfully logs into Salesforce during an identified
credential stuffing attack. Credential stuffing refers to


Metadata Types TransactionSecurityPolicy

**Field Name** **Field Type** **Description**

large-scale automated login requests using stolen user
credentials.This value is available in API version 49.0 and later.

**•** `FileEventStore` (beta)—Tracks when a user downloads,
previews, or uploads a file. FileEventStore is a big object that
stores the event data of FileEvent. This object is available in
API version 57.0 and later.

**•** `GuestUserAnomalyEventStore` —Tracks data access
anomalies that are caused by guest user permission
misconfiguration. This object is available in API version 60.0
and later.

**•** `ListViewEvent` —Tracks when users access data with list
views using Lightning Experience, Salesforce Classic, or the
API. It doesn’t track list views of Setup entities.

**•** `LoginAsEvent` —Tracks the login activity of admins who
log in to Salesforce as other users. This object is available in
API version 46.0 and later.

**•** `LoginEvent` —LoginEvent tracks the login activity of users
who log in to Salesforce.

**•** `PermissionSetEventStore` —Tracks changes to
permission sets and permission set groups.

**•** `ReportAnomalyEventStore` —Tracks anomalies in
how users run or export reports, including unsaved reports.
This value is available in API version 49.0 and later.

**•** `ReportEvent` —Tracks when reports are run in your org.

**•** `SessionHijackingEventStore` —Tracks when
unauthorized users gain ownership of a Salesforce user’s
session with a stolen session identifier. To detect such an event,
Salesforce evaluates how significantly a user’s current browser
fingerprint diverges from the previously known fingerprint
using a probabilistically inferred significance of change.
Available in API version 49.0 and later.

`eventType` MonitoredEvents (enumeration
of type string)

Used in Legacy Transaction Security only. Required for Apex-based
policies, and optional for all other policies. Indicates which type of
event is being monitored. Valid values are:

**•** `AccessResource` —Notifies you when the selected
resource has been accessed.

**•** `AuditTrail` —Reserved for future use.

**•** `DataExport` —Notifies you when the selected object type
has been exported using the Data Loader API client.

**•** `Entity` —Notifies you on use of an object type such as an
authentication provider or Chatter comment.

**•** `Login` —Notifies you when a user logs in.


Metadata Types TransactionSecurityPolicy

**Field Name** **Field Type** **Description**

As of Summer '20, Legacy Transaction Security is a retired feature
in all Salesforce orgs.

`executionUser` string

Used in Legacy Transaction Security only. The name or ID of an
active user who is assigned the Modify All Data and View Setup
user permissions.

As of Summer '20, Legacy Transaction Security is a retired feature
in all Salesforce orgs.

`flowId` string Required only for policies of type
`CustomConditionBuilderPolicy` . The ID of the Flow

object that contains the logic the Condition Builder transaction
security policy. Available in API version 46.0 and later.

`masterLabel` string

The label for this object. This display value is the internal label that
is’t translated.

Where possible, we changed noninclusive terms to align with our
company value of Equality. We maintained certain terms to avoid
any effect on customer implementations.

`resourceName` string Used in Legacy Transaction Security only. Required for Apex-based
policies, and optional for all other policies. A resource used to

narrow down the conditions under which the policy triggers. For
example, with a `DataExport` event, you can select a resource
Lead to specifically monitor export activity occurring on your Lead
entities. The resources available depend on the `Event Type`
field. The following valid resources are grouped by event type.

**•** AccessResource—ConnectedApplication, Reports

**•** DataExport—Account, Case, Contact, Lead, Opportunity

**•** Entity—AuthProvider, ChatterMessage, FeedComment,
FeedItem, Idea, Question

**•** Login—LoginHistory

As of Summer '20, Legacy Transaction Security is a retired feature
in all Salesforce orgs.

`type` TxnSecurityPolicyType The type of validation that the policy uses. The valid values are:
(enumeration of type string)

**•** `CustomApexPolicy`                         - Created with Apex editor.

**•** `CustomConditionBuilderPolicy`                         - Created with
Condition Builder.

The default value is `CustomApexPolicy` .

TransactionSecurityAction

Describes the action to take when the matching Transaction Security policy is triggered.


Metadata Types TransactionSecurityPolicy

**Field Name** **Field Type** **Description**

`block` boolean If `true`, the requested operation is blocked. This action only
applies to Login and AccessResource events.

`endSession` boolean

`freezeUser` boolean

Used in Legacy Transaction Security only. If `true`, a current session
must be closed before a new session can be started. This action
only applies to Login events.

As of Summer '20, Legacy Transaction Security is a retired feature
in all Salesforce orgs.

Used in Legacy Transaction Security only. If `true`, the user that
triggered the policy is frozen. This action only applies to Chatter
resources for Entity events.

As of Summer '20, Legacy Transaction Security is a retired feature
in all Salesforce orgs.

`notifications` TransactionSecurityNotification[] Specifies how to notify the Salesforce administrator when the
action is triggered. There can be none, one, or multiple notifications.

`twoFactorAuthentication` boolean

TransactionSecurityNotification

If `true`, multi-factor authentication (MFA) is required for a higher
level of access before the requested operation can continue. This
action only applies to Login and AccessResource events.

Multi-factor authentication was formerly called two-factor
authentication.

Describes who to notify and how to notify them when the matching Transaction Security policy is triggered.

**Field Name** **Field Type** **Description**

`inApp` boolean True if an in-app notification is selected.

`sendEmail` boolean True if an email notification is selected.

`user` string The user to receive the notification.

Declarative Metadata Sample Definition

The following is an example of a Real-Time Event Monitoring TransactionSecurityPolicy component.

```
<?xml version="1.0" encoding="UTF-8"?>

<TransactionSecurityPolicy xmlns="http://soap.sforce.com/2006/04/metadata">

   <action>

     <block>true</block>

     <notifications>

        <inApp>true</inApp>

        <sendEmail>true</sendEmail>

```


### Metadata Types Translations

```
           <user>user@your.org</user>

        </notifications>

        <twoFactorAuthentication>false</twoFactorAuthentication>

      </action>

      <active>true</active>

      <apexClass>TxnSecMDApiPolicyEventCondition</apexClass>

      <blockMessage>You cannot view this report.</blockMessage>

      <developerName>TxnSecPolicyMDApi</developerName>

      <eventName>ReportEvent</eventName>

      <masterLabel>Txn Sec MD Api Policy</masterLabel>

      <type>CustomApexPolicy</type>

   </TransactionSecurityPolicy>

```

The following is an example package manifest used to deploy or retrieve the transaction security metadata for an organization.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>MySecurityPolicy</members>

        <name>TransactionSecurityPolicy</name>

      </types>

      <version>35.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### Translations

Metadata type that enables work with translations for various supported languages. The ability to translate component labels is part of
the Translation Workbench.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

This type extends the Metadata metadata type and inherits its `fullName` field.

Language

A two-character language code identifies each language, such as `en` . A five-character code is used for languages that differ depending
on location. For example, en_AU.

Note: Setting a default language is different from setting a default locale. For more information, see Select Your Language, Locale,
and Currency in Salesforce Help.

Salesforce offers full support for these languages.

**•** Chinese (Simplified): `zh_CN`

**•** Chinese (Traditional): `zh_TW`

**•** Danish: `da`


Metadata Types Translations

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

**•** Spanish (Mexico): `es_MX` Spanish (Mexico) defaults to Spanish for customer-defined translations.

**•** Swedish: `sv`

**•** Thai: `th` The Salesforce user interface is fully translated to Thai, but Help is in English.

End-user languages are useful if you have a multilingual organization or partners who speak languages other than your company’s
default language. For end-user languages, Salesforce provides translated labels for standard objects and pages, except admin pages,
Setup, and Help. Some clouds and features support a subset of these languages in the UI. For details, see User Interface Language Support
in Salesforce Help. When you select an end-user language, labels that aren’t translated and Salesforce Help appear in English. End-user
languages are intended only for personal use by end users. Don’t use end-user languages as corporate languages. Salesforce doesn’t
provide customer support in end-user languages.

End-user languages include:

**•** Arabic: `ar`

**•** Bulgarian: `bg`

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

Important: Before enabling end-user languages Arabic and Hebrew, review the right-to-left language support limitations.


Metadata Types Translations

In situations where Salesforce doesn’t provide default translations, use platform-only languages to localize apps and custom functionality
that you build on the Salesforce Platform. You can translate items such as custom labels, custom objects, and field names. You can also
rename most standard objects, labels, and fields. Informational text and non-field label text aren’t translatable.

Platform-only languages are available in all places where you can select a language in the application. However, when you select a
platform-only language, all standard Salesforce labels default to English or, in select cases, to an end-user or fully supported language.

Note: Language support is closely tied to the API version. For example, we introduced support for Belgian Dutch (nl_BE) in API
version 40.0. To take advantage of this language, you must use API version 40.0 or later. In general, we recommend using the most
recent version of the API to make the most of our language features.

Platform-only languages include:

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


Metadata Types Translations

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


Metadata Types Translations

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


Metadata Types Translations

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

Important: Before enabling Urdu as a platform-only language, review the right-to-left language support limitations.

Declarative Metadata File Suffix and Directory Location

Local translations are stored in a file with a format of _`localeCode`_ `.translation`, where _`localeCode`_ is the locale code of
the translation language. For example, the file name for German translations is `de.translation` . Packaged translations are stored
in a file with a format of _`pkgNamespace`_ `_ _` _`localeCode`_ `.translation` . For example, if the package namespace is Acme,
the file name for German translations installed by the package is `Acme_ _de.translation` . The supported locale codes are listed
in Language.

Custom object translations are stored in the `objectTranslations` folder in the corresponding package directory.

Version

Translations components are available in API version 14.0 and later.

Fields

**Field** **Field Type** **Description**

`aiCoachAgentScnrDefs` AiCoachAgentScnrDefTranslation[] A list of AI Coach agent scenario definition translations.
Available in API version 64.0 and later.

`botBlocks` BotBlockTranslation[] A list of bot block translations. Available in API version
59.0 and later.

`botTemplates` BotTemplateTranslation[] A list of bot template translations. Available in API version
59.0 and later.

`bots` BotTranslation[] A list of bot translations. Available in API version 53.0 and
later.

`conversationMessageDefinitions` ConversationMessageDefinitionTranslation[] A list of conversation message definition translations.
Available in API version 61.0 and later.


Metadata Types Translations

**Field** **Field Type** **Description**

`customApplications` CustomApplicationTranslation[] A list of custom application translations.

`customLabels` CustomLabelTranslation[] A list of custom label translations.

`customPageWebLinks` CustomPageWebLinkTranslation[] A list of translations for web links defined in a home page
component.

`customTabs` CustomTabTranslation[] A list of custom tab translations.

`dataConnectors` DataConnectorTranslation[] A list of data connector translations. Available in API
version 64.0 and later.

`desFieldTemplateMessages` ExplainabilityMsgTemplateFieldTranslation[] A list of admin-configured explainability message
templates.

`flowDefinitions` FlowDefinitionTranslation[]

A list of flow translations.

Only Flow and AutolaunchedFlow types are supported
for translation.

This field is available in API version 41.0 and later.

`identityVerificationCustomFieldLabels` IdentityVerificationFieldTranslation
A list of identity verification translation fields.

This field is available in API version 54.0 and later.

`fullName` string

`globalPicklists` GlobalPicklistTranslation[]

`pipelineInspMetricConfigs` PipelineInspMetricConfigTranslation

Required. The language code. For example, `de` for
German.

Inherited from Metadata, this field is defined in the WSDL
for this metadata type. It must be specified when

creating, updating, or deleting. For an example of this
field specified for a call, see `createMetadata()` .

A list of global picklist translations. A global picklist’s
value set is inherited by all the custom picklist fields that
are based on it.

This field is available in API version 37.0 only and is
removed from later versions.

A list of translations of Pipeline Inspection forecast
category metric settings. This field is available in API
version 57.0 and later.

`productSpecificationTypes` ProductSpecificationTypeTranslation A list of product specification type translations. This field
is available in API version 66.0 and later.

`prompts` PromptTranslation A list of In-App Guidance prompt translations. This field
is available in API version 48.0 and later.

`quickActions` GlobalQuickActionTranslation[] A list of global rather than object-specific quick actions.

`recordAlertCategories` RecordAlertCategoryTranslation[] A list of record alert category translations. Available in
API version 66.0 and later.


Metadata Types Translations

**Field** **Field Type** **Description**

`recordAlertTemplates` RecordAlertTemplateTranslation[] A list of record alert template translations. Available in
API version 66.0 and later.

`reportTypes` ReportTypeTranslation[] A list of report type translations.

`scontrols` ScontrolTranslation[] A list of s-control translations.

`svcCatalogItemAttributes` ServiceProcessAttributeTranslation[] A list of service catalog item attribute translations.
Available in API version 64.0 and later.

`svcCatalogItemGroups` ServiceProcessItemGroupTranslation[] A list of service catalog item group translations. Available
in API version 64.0 and later.

`timelineObjectDefinitions` TimelineObjectDefinitionTranslation[] A list of timeline object definition translations. Available
in API version 66.0 and later.

AiCoachAgentScnrDefTranslation

AiCoachAgentScnrDefTranslation contains details for the translation of Agentforce Sales Coach scenarios. Available in API version 64.0
and later.

**Field** **Field Type** **Description**

`description` string The description of the coaching scenario.

`label` string The title of the coaching scenario.

`name` string Required. Name of the coaching scenario.

`infoMessage` string The instructions that the rep has to follow before starting the
coaching session.

BotBlockTranslation

BotBlockTranslation contains details for a translation of a bot block. Available in API version 59.0 and later.

**Field** **Field Type** **Description**

`botBlockVersions` BotBlockVersionTranslation[] A list of bot block version translations.

`fullName` string Required. The name of the bot block.

BotBlockVersionTranslation

BotBlockVersionTranslation contains details for a translation of a bot block version. Available in API version 59.0 and later.

**Field** **Field Type** **Description**

`botDialogs` BotDialogTranslation[] A list of bot dialog translations for the bot block version.


Metadata Types Translations

**Field** **Field Type** **Description**

`fullName` string Required. The name of the bot block version.

BotTemplateTranslation

BotTemplateTranslation contains details for a translation of a bot template. Available in API version 59.0 and later.

**Field** **Field Type** **Description**

`botDialogs` BotDialogTranslation[] A list of bot dialog translations for the bot template.

`fullName` string Required. The name of the bot template.

BotTranslation

BotTranslation contains details for a translation of a bot. Available in API version 53.0 and later.

**Field** **Field Type** **Description**

`botVersions` BotVersionTranslation[] A list of bot version translations.

`fullName` string

BotVersionTranslation

Required. Name of the bot.

The `fullName` for the translation must match the `fullName`
inherited by the original Bot type.

BotVersionTranslation contains details for a translation of a bot version. Available in API version 53.0 and later.

**Field** **Field Type** **Description**

`botDialogs` BotDialogTranslation[] A translated list of dialogs in this bot version.

`fullName` string

BotDialogTranslation

Required. Name of a bot version.

The `fullName` for the translation must match the
`fullName` inherited by the original BotVersion type.

BotDialogTranslation contains details for a translation of a bot dialog. Available in API version 53.0 and later.

**Field** **Field Type** **Description**

`botSteps` BotStepTranslation[] A translated list of steps that are executed as part of the dialog.


Metadata Types Translations

**Field** **Field Type** **Description**

`developerName` string

Required. This unique name prevents conflicts with other dialogs
associated with the same bot version.

The `developerName` for the translation must match the
`developerName` on the original BotDialog subtype of
BotVersion.

`label` string A translated label that identifies the dialog throughout the
Salesforce user interface.

Note: In Metadata Deployment of Translations, it's expected that blank values cannot be used to delete existing translations. If a
translation label is left blank, it's skipped during deployment, and no error will be shown.

BotStepTranslation

BotStepTranslation contains details for a translation of a bot step. Available in API version 53.0 and later.

**Field** **Field Type** **Description**

`botMessages` BotMessageTranslation[] A translated list of bot messages used by a BotStep of type
`Message` .

`botSteps` BotStepTranslation[] A translated list of bot steps associated with a BotStep of type
`Group` .

`botVariableOperation` BotVariableOperationTranslation A translated bot variable operation used by a BotStep of type
`VariableOperation` .

`stepIdentifier` string Required. A unique key that identifies a step within a dialog. This
key is used to link translated labels to labels within the step. This

field is recommended for all step records and is required for
translated step labels.

The `stepIdentifier` for the translation must match the
`stepIdentifier` on the original BotStep subtype of
BotVersion.

`type` BotStepType (enumeration of Required. Valid values are:
type string)

**•** `Navigation`

**•** `Invocation`

**•** `VariableOperation`

**•** `Message`

**•** `Wait`

**•** `Group`

**•** `RecordLookup` (Available in API version 48.0 and later.)

The `type` for the translation must match the `type` on the
original BotStep subtype of BotVersion.


Metadata Types Translations

BotMessageTranslation

BotMessageTranslation contains details for a translation of a bot message step. Available in API version 53.0 and later.

**Field** **Field Type** **Description**

`message` string A translated message to display as part of an outgoing message
from the bot to the customer.

`messageIdentifier` string Required. A unique key that identifies a message within a dialog.
This key is used to link translated labels to labels within the

message. This field is recommended for all message records and
is required for translated message labels.

The `messageIdentifier` for the translation must match
the `messageIdentifier` on the original BotMessage
subtype of BotVersion.

BotVariableOperationTranslation

BotVariableOperationTranslation contains details for a translation of a bot variable operation (question) step. Available in API version
53.0 and later.

**Field** **Field Type** **Description**

`botMessages` BotMessageTranslation on page A translated list of bot messages used as prompt messages by
2400[] a BotVariableOperation of type `Collect` .

`botQuickReplyOptions` BotQuickReplyOptionTranslation
on page 2401[]

A translated list of static choice options used by a
BotVariableOperation of type `Collect` and
`quickReplyType` of `Static` .

`quickReplyOptionTemplate` string A translated formula template used to resolve a label for
Dynamic choice options of type `Object` .

`retryMessages` BotMessageTranslation on page [In Conversation Repair, the translated messages assigned to](https://help.salesforce.com/s/articleView?id=service.bots_service_setup_dialog_question_text.htm&type=5&language=en_US)
2400[] repair attempts.

`successMessages` BotMessageTranslation on page
2400[]

In a File dialog step, the translated message displayed to the
customer as part of type CollectAttachment to confirm a
successful file upload. Available in API version 57.0 and later.

`type` BotVariableOperationType Required. Valid values are:
(enumeration of type string)

**•** `Set`

**•** `Unset`

**•** `Collect`

**•** `SetConversationLanguage`

`variableOperationIdentifier` string Required. A unique key that identifies a variable operation within
a dialog. This key is used to link translated labels to labels within

the variable operation. This field is recommended for all variable


Metadata Types Translations

**Field** **Field Type** **Description**

operation records and is required for translated variable
operation labels.

The `variableOperationIdentifier` for the
translation must match the
`variableOperationIdentifier` on the original
BotVariableOperation subtype of BotVersion.

BotQuickReplyOptionTranslation

BotQuickReplyOptionTranslation contains details for a translation of a bot quick reply option within a bot variable operation (question)
step. Available in API version 53.0 and later.

**Field** **Field Type** **Description**

`literalValue` string A translated value to be displayed as a menu or button choice
to your customer.

`quickReplyOptionIdentifier` string Required. A unique key that identifies a quick reply option within
a dialog. This key is used to link translated labels to labels within

the quick reply option. This field is recommended for all quick
reply option records and is required for translated quick reply
option labels.

The `quickReplyOptionIdentifier` for the translation
must match the `quickReplyOptionIdentifier` on
the original BotQuickReplyOption subtype of BotVersion.

CustomApplicationTranslation

CustomApplicationTranslation contains details for a custom application translation. For more details, see CustomApplication.

**Field** **Field Type** **Description**

`description` string Description text for the application translation.

`label` string The translated custom application name. Maximum of 765
characters.

`name` string Required. The name of the custom application.

CustomLabelTranslation

CustomLabelTranslation contains details for a custom label translation. For more details, see CustomLabels.


Metadata Types Translations

**Field** **Field Type** **Description**

`label` string Required. The translated custom label name. Maximum of 765
characters.

`name` string Required. The custom label name.

CustomPageWebLinkTranslation

CustomPageWebLinkTranslation contains details for a translation of a web link defined in a home page component. For more details,
see CustomPageWebLink.

**Field** **Field Type** **Description**

`label` string Required. The translated web link.

`name` string Required. The name of the web link.

CustomTabTranslation

CustomTabTranslation contains details for a translation of a custom tab. For more details, see CustomTab.

**Field** **Field Type** **Description**

`label` string Required. The translated custom tab name.

`name` string Required. The custom tab name.

ExplainabilityMsgTemplateFieldTranslation

Represents the template that contains the decision explanation message for a specified step element type.

**Field Name** **Field Type** **Description**

`description` string The explainability message field description.

`label` string A user-friendly name for
ExplainabilityMsgTemplateFieldTranslation.

`name` string
Required.

The name of the decision explanation message for a specified
step element type.

`templateMessage` string The message associated with the template for a specific
expression set step type.


Metadata Types Translations

Declarative Metadata Sample Definition

This is an example of an ExplainabilityMsgTemplateFieldTranslation component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Translations xmlns="http://soap.sforce.com/2006/04/metadata">

      <desFieldTemplateMessages>

        <description>Calc Blitz Message</description>

        <label>CALBLITZ</label>

        <name>CALBLITZ</name>

        <templateMessage>CALBLITZ</templateMessage>

      </desFieldTemplateMessages>

   </Translations>

```

FlowDefinitionTranslation

FlowDefinitionTranslation contains details for a translation of a flow definition. For more details, see FlowDefinition.

Available in API version 41.0 and later.

**Field** **Field Type** **Description**

`flows` FlowTranslation[] A list of flow version translations for the flow definition.

`fullName` string Required. The API name for the flow definition.

`label` string

FlowTranslation

A translated label for the flow definition.

By default, flow definitions inherit the label of the active flow
version. If you provide a label here, the definition label no longer
inherits changes to the active version label.

FlowTranslation contains details for a translation of a flow version. For more details, see Flow.

Available in API version 41.0 and later.

**Field** **Field Type** **Description**

`choices` FlowChoiceTranslation[] A list of choice translations for the flow version.

`fullName` string

The API name for the flow version.

A unique name for the flow that contains only underscores and
alphanumeric characters. The name must be unique across the

org, begin with a letter, not include spaces, not end with an
underscore, and not contain two consecutive underscores.

To deploy or retrieve a version, you can specify the version
number. For example, `sampleFlow-3` specifies version 3 of
the flow whose unique name is sampleFlow. If you don't specify
a version number, the flow is the latest version.


Metadata Types Translations

**Field** **Field Type** **Description**

In API version 43.0 and earlier, this field included the version
number. In API version 44 and later, this field no longer includes
the version number.

`label` string A translated label for the flow version.

`orchestrationStages` FlowOrchestrationStageTranslation A list of orchestration stage translations for the flow version.
on page 2405 Available in API version 63.0 and later.

`orchestrationSteps` FlowOrchestrationStepTranslation A list of orchestration step translations for the flow version.
on page 2405 Available in API version 63.0 and later.

`screens` FlowScreenTranslation[] A list of screen translations for the flow version.

`stages` FlowStageTranslation on page A list of stage translations for the flow version. Available in API
2407[] version 43.0 and later.

FlowChoiceTranslation

FlowChoiceTranslation contains details for a translation of a choice in a flow version. For more details, see FlowChoice in Flow.

Available in API version 41.0 and later.

**Field** **Field Type** **Description**

`choiceText` string A translated label for the choice.

`name` string Required. A unique name for the choice.

`userInput` FlowChoiceUserInputTranslation A translated choice input for the choice.

FlowChoiceUserInputTranslation

FlowChoiceUserInputTranslation contains details for a translation of a choice input. For more details, see FlowChoiceUserInput in Flow.

Available in API version 41.0 and later.

**Field** **Field Type** **Description**

`promptText` string A translated label for the choice input.

`validationRule` FlowInputValidationRuleTranslation A translated validation rule for the choice input.

FlowInputValidationRuleTranslation

FlowInputValidationRuleTranslation contains details for a translation of a validation rule. For more details, see FlowInputValidationRule
in Flow.

Available in API version 41.0 and later.


Metadata Types Translations

**Field** **Field Type** **Description**

`errorMessage` string A translated error message for the validation rule.

FlowOrchestrationStageTranslation

FlowOrchestrationStageTranslation contains details for a translation of an orchestration stage in an orchestration version. For more
details, see FlowOrchestratedStage in Flow.

Available in API version 64.0 and later.

**Field** **Field Type** **Description**

`name` string Required. The unique name of the orchestration stage
translation.

`stageLabel` string A translated label for the orchestration stage.

FlowOrchestrationStepTranslation

FlowOrchestrationStepTranslation contains details for a translation of an orchestration step in an orchestration version. For more details,
see FlowStageStep in Flow.

Available in API version 63.0 and later.

**Field** **Field Type** **Description**

`name` string Required. The unique name of the orchestration step translation.

`stepLabel` string A translated label for the orchestration step.

FlowScreenTranslation

FlowScreenTranslation contains details for a translation of a screen. For more details, see FlowScreen in Flow.

Available in API version 41.0 and later.

**Field** **Field Type** **Description**

`backButtonLabel` string A translated label for the Back button. Available in API version
54.0 and later.

`fields` FlowScreenFieldTranslation[] A list of screen component translations for the screen.

`helpText` string Translated help text for the screen.

`name` string Required. An API name for the screen.

`nextOrFinishButtonLabel` string A translated label for the Next or Finish button. Available in API
version 54.0 and later.

`pauseButtonLabel` string A translated label for the Pause button. Available in API version
54.0 and later.


Metadata Types Translations

**Field** **Field Type** **Description**

`pausedText` string A translated pause confirmation message for the screen.

FlowScreenFieldTranslation

FlowScreenFieldTranslation contains details for a translation of a screen component. For more details, see FlowScreenField in Flow.

Available in API version 41.0 and later.

Note: Translation isn’t supported for screen components that require Lightning runtime.

**Field** **Field Type** **Description**

`fieldText` string A translated label for the screen component.

`helpText` string Translated help text for the screen component.

`inputParameters` FlowInputParameterTranslation Reserved for internal use.

`name` string Required. An API name for the screen component.

`validationRule` FlowInputValidationRuleTranslation Translated validation rule for the screen component.

FlowInputParameterTranslation

FlowInputParameterTranslation is reserved for internal use.

**Field** **Field Type** **Description**

`name` string Reserved for internal use.

`value` FlowFerovTranslation Reserved for internal use.

FlowFerovTranslation

FlowFerovTranslation is reserved for internal use.

**Field** **Field Type** **Description**

`complexValues` FlowComplexLiteralTranslation Reserved for internal use.

`stringValues` string Reserved for internal use.

FlowComplexLiteralTranslation

FlowComplexLiteralTranslation is reserved for internal use.


Metadata Types Translations

**Field** **Field Type** **Description**

`customAspectKey` string Reserved for internal use.

`value` string Reserved for internal use.

FlowStageTranslation

FlowStageTranslation contains details for a translation of a stage in a flow version. For more details, see FlowStage in Flow.

Available in API version 43.0 and later.

**Field** **Field Type** **Description**

`label` string A translated label for the stage.

`name` string Required. An API name for the stage.

FlowTextTemplateTranslation

FlowTextTemplateTranslation is available only in flows created via Salesforce Surveys and represents the translation details for the text
on all the pages of a survey.

Available in API version 45.0 and later.

**Field** **Field Type** **Description**

`name` string Required. Unique name for the text template.

`text` string Translated text for the text template.

IdentityVerificationFieldTranslation

Translates the UI components associated with identity verification fields.

Available in API version 54.0 and later.

**Field** **Field Type** **Description**

`customFieldLabel` string The custom label for the field that contains the verification data.

`description` string The identity verification field description.

`label` string A user-friendly name for IdentityVerificationFieldTranslation.

`name` string Required. The name of the identity verification field.

TimelineObjectDefinitionTranslation

Contains details for a translation of a timeline object definition. Available in API version 66.0 and later.


Metadata Types Translations

**Field** **Field Type** **Description**

`label` string Translated label for the timeline object definition.

`name` string Required. Name of the timeline object definition.

Declarative Metadata Sample Definition

This is an example of an IdentityVerificationFieldTranslation component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Translations

      xmlns="http://soap.sforce.com/2006/04/metadata">

      <identityVerificationCustomFieldLabels>

        <description>Telefono Numero</description>

        <label>Telefono Numero</label>

        <name>Sample93Phone</name>

      </identityVerificationCustomFieldLabels>

      <identityVerificationCustomFieldLabels>

        <description>Nombre de la Cuenta</description>

        <label>Nombre de la Cuenta</label>

        <name>Sample93Account</name>

      </identityVerificationCustomFieldLabels>

      <identityVerificationCustomFieldLabels>

        <name>Sample93PostalCode</name>

      </identityVerificationCustomFieldLabels>

      <identityVerificationCustomFieldLabels>

        <name>Sample93AccountName</name>

        <description>Nombre</description>

        <label>Nombre</label>

      </identityVerificationCustomFieldLabels>

   </Translations>

```

GlobalPicklistTranslation

Note: GlobalPicklistTranslation is available in API version 37.0 only and is removed from later versions.

GlobalPicklistTranslation contains details for a global picklist translation.

Translations are stored in a file with a format of _`globalPicklistName__e`_ `-` _`lang`_ `.objectTranslation`, where
_`globalPicklistName__e`_ is the global picklist name and _`lang`_ is the translation language. To reference a global picklist
translation value, use _`globalPicklistName__e.value1`_, where _`value1`_ is the translated value for the user interface.

Here’s what translations look like for a global picklist.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Translations xmlns="http://soap.sforce.com/2006/04/metadata">

   <globalPicklists>

      <name>transpicklist</name>

      <picklistValues>

        <masterLabel>Three</masterLabel>

        <translation>Trois</translation>

      </picklistValues>

```


Metadata Types Translations

```
      <picklistValues>

        <masterLabel>Four</masterLabel>

        <translation>Quatre</translation>

      </picklistValues>

   </globalPicklists>

   </Translations>

```

**Field** **Field Type** **Description**

`name` string Required. Represents the name of a global picklist to be
translated.

`picklistValues` PicklistValueTranslation[] A list of picklist values from global picklists to be translated.

GlobalQuickActionTranslation

GlobalQuickActionTranslation contains details for the global translation of a quick action. For more information, see QuickAction.

**Field** **Field Type** **Description**

`aspect` string Identifies which quick action label the translated text belongs
to. Use this field only when you want to use different strings for

the quick action’s field label and informational message. Valid
values are `Master` and `InfoMessage` . Available in API
version 53.0 and later.

`label` string Required. The translated quick action name, globally.

`name` string Required. The quick action name.

PipelineInspMetricConfigTranslation

PipelineInspMetricConfigTranslation contains details for the translation of Pipeline Inspection forecast category metric settings. Available
in API version 57.0 and later.

**Field** **Field Type** **Description**

`label` string Required. The translated Pipeline Inspection metric
configuration name.

`name` string Required. The name of the Pipeline Inspection metric
configuration.

ProductSpecificationTypeTranslation

ProductSpecificationTypeTranslation contains details for a translation of a product specification type. For more details, see
[ProductSpecificationType. Available in API version 66.0 and later.](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/meta_productspecificationtype.htm)


Metadata Types Translations

**Field** **Field Type** **Description**

`description` string The translated product specification type description.

`label` string The translated product specification type name.

`name` string Required. The name of the product specification type.

PromptTranslation

PromptTranslation contains metadata for the translation of a prompt, which is part of In-App Guidance. Available in API Version 48.0
and later.

**Field** **Field Type** **Description**

`description` string The prompt description.

`label` string The translated prompt name.

`name` string Required. The name of the prompt.

`promptVersions` PromptVersionTranslation A list of the prompt version translations.

PromptVersionTranslation

PromptVersionTranslation contains details for translation of a prompt, which is part of In-App Guidance. Available in API Version 48.0
and later.

**Field** **Field Type** **Description**

`actionButtonLabel` string The label for the prompt’s action button.

`actionButtonLink` string The URL for the prompt’s action button.

`body` string The body text of the prompt.

`description` string The prompt description.

`dismissButtonLabel` string The label for the floating prompt’s dismiss button.

`header` string The header for the docked prompt.

`imageAltText` string The alt text for a prompt’s image. Available in API version 53.0
and later.

`imageLink` string The URL for a prompt’s image. Available in API version 53.0 and
later.

`label` string The translated prompt name.

`name` string Required. The name of the prompt.

`title` string The title of the prompt.

`videoLink` string The URL for the docked prompt’s video.


Metadata Types Translations

ReportTypeTranslation

ReportTypeTranslation contains details for a translation of a custom report type. For more details, see ReportType.

**Field** **Field Type** **Description**

`description` string The translated report type description.

`label` string The translated report type name.

`name` string Required. The name of the report type.

`sections` ReportTypeSectionTranslation[] A list of report type section translations.

ReportTypeSectionTranslation

ReportTypeSectionTranslation contains details for a report type section translation.

**Field** **Field Type** **Description**

`columns` ReportTypeColumnTranslation[] A list of report type column translations.

`label` string The translated report type section name.

`name` string Required. The name of the report type section.

ReportTypeColumnTranslation

ReportTypeColumnTranslation contains details for a report type column translation.

**Field** **Field Type** **Description**

`label` string Required. The translated report type column name.

`name` string Required. The report type column name.

ScontrolTranslation

Important: Visualforce pages supersede s-controls. Organizations that haven't previously used s-controls can’t create them.
Existing s-controls are unaffected and can still be edited.

ScontrolTranslation contains details for a translation of an s-control. For more information, see “About S-Controls” in Salesforce Help.

**Field** **Field Type** **Description**

`label` string Required. The translated s-control name.

`name` string Required. The name of the s-control.


Metadata Types Translations

ConversationMessageDefinitionTranslation

ConversationMessageDefinitionTranslation contains details for a translation of a conversation message definition. Available in API version
61.0 and later.

**Field** **Field Type** **Description**

`constantValueTranslations` ConversationMessageConstantValueTranslation[] A list of conversation message constant value translations.

`label` string Required. The translated label for the conversation message
definition.

`name` string Required. The name of the conversation message definition.

ConversationMessageConstantValueTranslation

ConversationMessageConstantValueTranslation contains details for a translation of a conversation message constant value. Available in
API version 61.0 and later.

**Field** **Field Type** **Description**

`name` string Required. The name of the conversation message constant value.

`value` string Required. The translated constant value.

DataConnectorTranslation

DataConnectorTranslation contains details for a translation of a data connector. Available in API version 64.0 and later.

**Field** **Field Type** **Description**

`attributes` DataConnectorAttributeTranslation[] A list of data connector attribute translations.

`description` string The translated description for the data connector.

`errors` DataConnectorErrorTranslation[] A list of data connector error translations.

`help` string The translated help text for the data connector.

`label` string The translated label for the data connector.

`language` string The language for the data connector translation.

`name` string The name of the data connector.

DataConnectorAttributeTranslation

DataConnectorAttributeTranslation contains details for a translation of a data connector attribute. Available in API version 64.0 and later.

**Field** **Field Type** **Description**

`errorMessage` string The translated error message for the attribute.


Metadata Types Translations

**Field** **Field Type** **Description**

`infoMessage` string The translated info message for the attribute.

`inputLabel` string The translated input label for the attribute.

`label` string Required. The translated label for the attribute.

`name` string Required. The name of the attribute.

`options` DataConnectorAttributeOptTranslation[] A list of data connector attribute option translations.

DataConnectorAttributeOptTranslation

DataConnectorAttributeOptTranslation contains details for a translation of a data connector attribute option. Available in API version
64.0 and later.

**Field** **Field Type** **Description**

`label` string Required. The translated label for the attribute option.

`name` string Required. The name of the attribute option.

DataConnectorErrorTranslation

DataConnectorErrorTranslation contains details for a translation of a data connector error. Available in API version 64.0 and later.

**Field** **Field Type** **Description**

`label` string Required. The translated label for the error.

`name` string Required. The name of the error.

RecordAlertCategoryTranslation

RecordAlertCategoryTranslation contains details for a translation of a record alert category. Available in API version 66.0 and later.

**Field** **Field Type** **Description**

`description` string The translated description for the record alert category.

`label` string Required. The translated label for the record alert category.

`name` string Required. The name of the record alert category.

RecordAlertTemplateTranslation

RecordAlertTemplateTranslation contains details for a translation of a record alert template. Available in API version 66.0 and later.


Metadata Types Translations

**Field** **Field Type** **Description**

`description` string The translated description for the record alert template.

`label` string The translated label for the record alert template.

`name` string Required. The name of the record alert template.

`subject` string The translated subject for the record alert template.

ServiceProcessAttributeTranslation

ServiceProcessAttributeTranslation contains details for a translation of a service process attribute. Available in API version 64.0 and later.

**Field** **Field Type** **Description**

`label` string Required. The translated label for the service process attribute.

`name` string Required. The name of the service process attribute.

`serviceProcessName` string Required. The name of the service process.

ServiceProcessItemGroupTranslation

ServiceProcessItemGroupTranslation contains details for a translation of a service process item group. Available in API version 64.0 and
later.

**Field** **Field Type** **Description**

`groupName` string Required. The name of the service process item group.

`name` string Required. The name of the service process item group
translation.

`serviceProcessName` string Required. The name of the service process.

Declarative Metadata Sample Definition

This sample XML definition shows a translations component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Translations xmlns="http://soap.sforce.com/2006/04/metadata">

      <customApplications>

      <label>Angebot-Manager</label>

        <name>Quote Manager</name>

      </customApplications>

      <customLabels>

      <label>Dieses ist ein manuelles Angebot</label>

        <name>quoteManual</name>

      </customLabels>

   </Translations>

```


Metadata Types Translations

Usage

When you use the `retrieve()` call to get translations, the files returned in the `.translations` folder only include translations
for the other metadata types referenced in `package.xml` . For example, this `package.xml` file contains `types` elements that
match all custom applications, custom labels, web links defined in home page components, custom tabs, report types, and s-controls.
Translations for all these metadata types are returned because each metadata type is explicitly listed in `package.xml` .

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>CustomApplication</name>

      </types>

      <types>

        <members>*</members>

        <name>CustomLabels</name>

      </types>

      <types>

        <members>*</members>

        <name>CustomPageWebLink</name>

      </types>

      <types>

        <members>*</members>

        <name>CustomTab</name>

      </types>

      <types>

        <members>*</members>

        <name>ReportType</name>

      </types>

      <types>

        <members>*</members>

        <name>Scontrol</name>

      </types>

      <types>

        <members>*</members>

        <name>Translations</name>

      </types>

      <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

CustomLabels


### Metadata Types UiFormatSpecificationSet UiFormatSpecificationSet

Represents a set of rules that define the style and visibility of conditional field formatting on Dynamic Forms-enabled Lightning page
field instances.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

Note: A UiFormatSpecificationSet is referred to as a conditional formatting ruleset in the rest of the Salesforce documentation
and UI.

File Suffix and Directory Location

### UiFormatSpecificationSet components have the suffix .uiFormatSpecificationSet and are stored in the

`uiFormatSpecificationSets` folder.

Version

### UiFormatSpecificationSet components are available in API version 62.0 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Description**

```
field

formatType

```

**Field Type**
string

**Description**

Required. The object field that the conditional formatting is associated with.

**Field Type**
FormatType (enumeration of type string)

**Description**

Required. The type of conditional formatting associated with the field.

Values are:

**•** `ICON`


Metadata Types UiFormatSpecificationSet

**Field Name** **Description**

```
masterLabel

sobjectType

uiFormatSpecifications

```

UiFormatSpecification

A single rule in the ruleset.

**Field Type**
string

**Description**

Required. The label for the conditional formatting ruleset, which displays in Setup.

**Field Type**
string

**Description**

Required. The object the ruleset is associated with.

**Field Type**

UiFormatSpecification[]

**Description**
The list of rules contained in the ruleset.

**Field Name** **Description**

```
formatProperties

formatType

order

```

**Field Type**
string

**Description**

Required. The properties for a given `formatType` in JSON format.

**Field Type**
FormatType (enumeration of type string)

**Description**

Required. The type of conditional formatting associated with the field when the rule
evaluates to `true` .

Values are:

**•** `ICON`

**Field Type**
int

**Description**

Required. A numerical value representing the conditional formatting rule’s position in
the evaluation order.


Metadata Types UiFormatSpecificationSet

**Field Name** **Description**

```
visibilityRule

```

UiFormulaRule

**Field Type**

UiFormulaRule

**Description**
A set of one or more filters that define the conditions under which the conditional
formatting appears on the field.

If the visibility rule evaluates to `true`, the formatting displays on the field. If `false`,
it doesn’t display. If this field is `null`, the formatting displays by default.

A set of one or more filters that define the conditions under which conditional field formatting displays on a Dynamic Forms-enabled
Lightning page field instance. For example, you could construct a filter that causes conditional formatting to display only when the
Amount field is greater than $1,000,000.

**Field Name** **Description**

```
booleanFilter

criteria

```

UiFormulaCriterion

**Field Type**
string

**Description**
Specifies advanced filter conditions such as `1 AND 2` .

**Field Type**

UiFormulaCriterion[]

**Description**
List of one or more filters that, when evaluated, determine conditional field formatting
visibility.

A single filter that when evaluated, helps define conditional formatting visibility on a Dynamic Forms-enabled Lightning page field
instance.

**Field Name** **Description**

```
leftValue

operator

```

**Field Type**
string

**Description**
Required. The field upon which the filter is based. For example, `AMOUNT` .

**Field Type**
string


Metadata Types UiFormatSpecificationSet

**Field Name** **Description**

**Description**
Required. Defines the operator used to filter the data. Valid values are:

**•** `CONTAINS`

**•** `EQUAL`

**•** `NE` —not equal

**•** `GT` —greater than

**•** `GE` —greater than or equal

**•** `LE` —less than or equal

**•** `LT` —less than

```
rightValue

```

**Field Type**
string

**Description**
The value by which you want to evaluate the formatting visibility. For example,
`1000000` .

Declarative Metadata Sample Definition

The following is an example of an UiFormatSpecificationSet component.

```
<?xml version="1.0" encoding="UTF-8"?>

<UiFormatSpecificationSet xmlns="http://soap.sforce.com/2006/04/metadata">

   <field>Contact.Customer_Sentiment__c</field>

   <formatType>ICON</formatType>

   <masterLabel>Sentiment Score</masterLabel>

   <sobjectType>Contact</sobjectType>

   <uiFormatSpecifications>

     <formatProperties>{&quot;icon&quot;:&quot;happy_face&quot;,

&quot;iconColor&quot;:&quot;green&quot;}</formatProperties>

     <formatType>ICON</formatType>

     <order>1</order>

     <visibilityRule>

        <criteria>

          <leftValue>{!Record.Customer_Sentiment__c}</leftValue>

          <operator>EQUAL</operator>

          <rightValue>Happy</rightValue>

        </criteria>

     </visibilityRule>

   </uiFormatSpecifications>

   <uiFormatSpecifications>

     <formatProperties>{&quot;icon&quot;:&quot;neutral_face&quot;,

&quot;iconColor&quot;:&quot;gray&quot;}</formatProperties>

     <formatType>ICON</formatType>

     <order>2</order>

     <visibilityRule>

        <criteria>

```


### Metadata Types UIObjectRelationConfig

```
             <leftValue>{!Record.Customer_Sentiment__c}</leftValue>

             <operator>EQUAL</operator>

             <rightValue>Neutral</rightValue>

           </criteria>

        </visibilityRule>

      </uiFormatSpecifications>

      <uiFormatSpecifications>

        <formatProperties>{&quot;icon&quot;:&quot;sad_face&quot;,

   &quot;iconColor&quot;:&quot;red&quot;}</formatProperties>

        <formatType>ICON</formatType>

        <order>3</order>

        <visibilityRule>

           <criteria>

             <leftValue>{!Record.Customer_Sentiment__c}</leftValue>

             <operator>EQUAL</operator>

             <rightValue>Unhappy</rightValue>

           </criteria>

        </visibilityRule>

      </uiFormatSpecifications>

   </UiFormatSpecificationSet>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Sentiment_Score</members>

        <name>UiFormatSpecificationSet</name>

      </types>

      <version>62.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### UIObjectRelationConfig

Represents the admin-created configuration of the object relation UI component.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.


Metadata Types UIObjectRelationConfig

File Suffix and Directory Location

UIObjectRelationConfig components have the suffix `.uiObjectRelationConfig` and are stored in the
`uiObjectRelationConfigs` folder.

Version

UIObjectRelationConfig components are available in API version 54.0 and later.

Special Access Rules

You must be a Health Cloud or Life Sciences Cloud customer to use this metadata type

Fields

**Field Name** **Description**

```
contextObject

contextObjectRecordType

directRelationshipField

indirectObjectContextField

indirectObjectRelatedField

```

**Field Type**
string

**Description**

Required.

The object that provides the context for this object relation configuration.

**Field Type**
string

**Description**
The record type of the context object for this configuration, if applicable.

**Field Type**
string

**Description**
For direct relationships, the child relationship field on the related object that matches
the context object.

**Field Type**
string

**Description**
For indirect relationships, the field on the junction object that matches the context
object.

**Field Type**
string


Metadata Types UIObjectRelationConfig

**Field Name** **Description**

**Description**
For indirect relationships, the field on the junction object that matches the related
object.

```
indirectRelationshipObject

isActive

masterLabel

relatedObject

relatedObjectRecordType

relationshipType

```

**Field Type**
string

**Description**
For indirect relationships, the junction object representing the relationship between
the related object and its context object.

**Field Type**
boolean

**Description**
Indicates whether the configuration is active ( `true` ) or not ( `false` ).

**Field Type**
string

**Description**

Required.

Label for the UIObjectRelationConfig. In the UI, this field is UI Object Relation Config.

**Field Type**
string

**Description**

Required.

The object containing the data that this object relation configuration displays.

**Field Type**
string

**Description**
The record type of the related object for this configuration.

**Field Type**
ObjectRelationshipType (enumeration of type string)

**Description**

Required.

A string indicating the type of relationship between the related object and context
object.

Valid values are:

**•** `Direct`


Metadata Types UIObjectRelationConfig

**Field Name** **Description**

**•** `Indirect`

**•** `InverseDirect`

**•** `Self`

```
UIObjectRelationFieldConfigs

```

**Field Type**

UIObjectRelationFieldConfig[]

**Description**
Provides a configuration for an object relation field on a specific row of content.

UIObjectRelationFieldConfig

Represents a configuration for a single row of content on a specific object relation configuration.

**Field Name** **Description**

```
displayLabel

queryText

rowOrder

```

**Field Type**
string

**Description**

Required.

A string containing the user-defined label for this field, to be displayed on each object
relation of this type.

**Field Type**
string

**Description**

Required.

A case-insensitive template query for generating the content in this field.

**Field Type**
int

**Description**

Required.

Determines the top-to-bottom display order of this field on the object relation UI.

Declarative Metadata Sample Definition

This is an example of a UIObjectRelationConfig component.

```
 <?xml version="1.0" encoding="UTF-8"?>

 <UIObjectRelationConfig xmlns="http://soap.sforce.com/2006/04/metadata">

   <UIObjectRelationFieldConfigs>

```


Metadata Types UIObjectRelationConfig

```
         <displayLabel>Address:</displayLabel>

         <queryText>{

      "startNode": {

         "initialObject": "RelatedObject"

      },

      "traversalNodes": [],

      "fieldNode": {

         "fieldEnumOrId": "ShippingAddress"

      }

    }</queryText>

         <rowOrder>1</rowOrder>

      </UIObjectRelationFieldConfigs>

      <UIObjectRelationFieldConfigs>

         <displayLabel>Phone:</displayLabel>

         <queryText>{

      "startNode": {

         "initialObject": "RelatedObject"

      },

      "traversalNodes": [],

      "fieldNode": {

         "fieldEnumOrId": "Phone"

      }

    }</queryText>

         <rowOrder>2</rowOrder>

      </UIObjectRelationFieldConfigs>

      <UIObjectRelationFieldConfigs>

         <displayLabel>Fax:</displayLabel>

         <queryText>{

      "startNode": {

         "initialObject": "RelatedObject"

      },

      "traversalNodes": [],

      "fieldNode": {

         "fieldEnumOrId": "Fax"

      }

    }</queryText>

         <rowOrder>3</rowOrder>

      </UIObjectRelationFieldConfigs>

      <UIObjectRelationFieldConfigs>

         <displayLabel>Parent Organization:</displayLabel>

         <queryText>{

      "startNode": {

         "initialObject": "RelatedObject"

      },

      "traversalNodes": [

         {

           "destinationObjectEnumOrId": "Account",

           "fieldEnumOrId": "ParentId",

           "traversalDirection": "parent"

         }

      ],

      "fieldNode": {

         "fieldEnumOrId": "Name"

      }

```


### Metadata Types UiPreviewMessageTabDef

```
    }</queryText>

         <rowOrder>4</rowOrder>

      </UIObjectRelationFieldConfigs>

      <contextObject>Contact</contextObject>

      <directRelationshipField>AccountId</directRelationshipField>

      <isActive>true</isActive>

      <masterLabel>Sample Primary Account Configuration</masterLabel>

      <relatedObject>Account</relatedObject>

      <relationshipType>Direct</relationshipType>

      <indirectObjectRelatedField></indirectObjectRelatedField>

      <indirectObjectContextField></indirectObjectContextField>

      <contextObjectRecordType></contextObjectRecordType>

      <indirectRelationshipObject></indirectRelationshipObject>

      <relatedObjectRecordType></relatedObjectRecordType>

    </UIObjectRelationConfig>

```

This is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <types>

       <members>*</members>

       <name>UIObjectRelationConfig</name>

     </types>

      <version>54.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### UiPreviewMessageTabDef

Represents the registration of a custom Marketing Cloud Preview and Test modal tab, created using custom Lightning web components.
You can register and show multiple tabs in the Preview and Test experience.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

### UiPreviewMessageTabDef components have the suffix .uiPreviewMessageTabDef and are stored in the

`uiPreviewMessageTabDef` folder.


Metadata Types UiPreviewMessageTabDef

Version

UiPreviewMessageTabDef components are available in API version 63.0 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Description**

```
isActive

isProtected

label

lightningComponentDef

supportedChannel

```

**Field Type**
boolean

**Description**

Required.

Indicates whether the tab is enabled and is customer controlled ( `true` ) or not
( `false` ).

**Field Type**
boolean

**Description**
Indicates whether the configuration is protected ( `true` ) or not ( `false` ).

**Field Type**
string

**Description**

Required.

Label for the tab.

**Field Type**
string

**Description**

Required.

The customer-created Lightning web component that displays in the Preview and
Test tabs.

**Field Type**
SupportedChannel (enumeration of type string)

**Description**

Required.

A string indicating the type of channel.


Metadata Types UiPreviewMessageTabDef

**Field Name** **Description**

Values are:

**•** `Email`

**•** `Sms`

**•** `WhatsApp`

```
tabName

```

**Field Type**
string

**Description**

Required.

The case-sensitive, user-defined label displayed as the name of the tab. Maximum
length is 255 characters.

Declarative Metadata Sample Definition

This example is a custom Lightning web component’s HTML file.

```
<template>

   <div>A custom tab</div>

   <div>Preview data</div>

   <div>{previewData}</div>

</template>

```

Here’s the component’s JavaScript file.

```
import { LightningElement, api } from "lwc";

export default class CustomTab extends LightningElement {

   @api previewData;

}

```

Here’s the component’s configuration file.

```
<?xml version="1.0" encoding="UTF-8"?>

<LightningComponentBundle xmlns="http://soap.sforce.com/2006/04/metadata">

   <apiVersion>63.0</apiVersion>

   <isExposed>true</isExposed>

   <capabilities>

     <capability>lightning__dynamicComponent</capability>

   </capabilities>

</LightningComponentBundle>

```

This example `package.xml` references the component’s definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<UiPreviewMessageTabDef xmlns="http://soap.sforce.com/2006/04/metadata">

   <isActive>true</isActive>

   <label>TestUiPreviewMessageTab</label>

   <lightningComponentDef>customTab</lightningComponentDef>

```


### Metadata Types UserAccessPolicy

```
      <supportedChannel>Email</supportedChannel>

      <tabName>My Tab</tabName>

      <isProtected>false</isProtected>

   </UiPreviewMessageTabDef>

### UserAccessPolicy

```

Represents a user access policy.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### UserAccessPolicy components have the suffix .useraccesspolicy and are stored in the useraccesspolicies folder.

Version

### UserAccessPolicy components are available in API version 57.0 and later.

Special Access Rules

To create or modify user access policies, users must have the Manage User Access Policies permission.

Fields

**Field Name** **Description**

```
booleanFilter

description

```

**Field Type**
string

**Description**
Required. The logic that determines how your user criteria filters are applied in the
user access policy. For example, if you have two user access policy filters with the
`sortOrder` equal to `1` and `2`, respectively, the `booleanFilter` can be `1`
`AND 2` or `1 OR 2` .

**Field Type**
string

**Description**
Description of the user access policy.


Metadata Types UserAccessPolicy

**Field Name** **Description**

```
isProtected

masterLabel

order

status

triggerType

```

**Field Type**
boolean

**Description**
An auto-generated value that doesn’t impact the behavior of the metadata type. The
default value is `false` .

**Field Type**
string

**Description**

Required. A user-friendly name for the user access policy, which is defined when the
user access policy is created.

**Field Type**
int

**Description**
Indicates the order for which active policy is applied when a user meets the criteria
for multiple policies. Must be an integer from 0 to 10,000. Only the active policy with
the lowest `order` value is applied. This field is required only if the `status` field is
set to `Active` .

Available in API version 61.0 and later.

**Field Type**
UserAccessPolicyStatus (enumeration of type string)

**Description**

Required. The status of the user access policy.

Values are:

**•** `Active`

**•** `Completed`

**•** `Design`

**•** `Failed`

**•** `Migrate`

**•** `Testing`

**•** `Updating`

If you deploy a policy with a status of `Active`, the status is changed to `Design` . A
Salesforce admin can then set the status to `Active` by automating the policy in
Setup.

**Field Type**
UserAccessPolicyTriggerType (enumeration of type string)


Metadata Types UserAccessPolicy

**Field Name** **Description**

**Description**

The type of user record trigger for which this user access policy runs.

Values are:

**•** `Create` —The user access policy runs when a user who matches the policy criteria
is created.

**•** `CreateAndUpdate` —The user access policy runs when a user who matches
the policy criteria is either created or updated.

**•** `Update` —The user access policy runs when a user who matches the policy criteria
is updated.

```
userAccessPolicyActions

userAccessPolicyFilters

```

UserAccessPolicyAction

**Field Type**

UserAccessPolicyAction[]

**Description**
The actions applied by the user access policy to grant access to or revoke access from
an access mechanism.

**Field Type**

UserAccessPolicyFilter[]

**Description**
The filters used to define the users that the user access policy is applied to.

Represents an action applied by a user access policy.

**Field Name** **Description**

```
action

target

```

**Field Type**
UserAccessPolicyActionType (enumeration of type string)

**Description**

Required. Indicates whether the user access policy grants or revokes the target access
mechanism.

Values are:

**•** `Grant`

**•** `Revoke`

**Field Type**
string

**Description**

Required. Developer name of the access mechanism that the user access policy applies.


Metadata Types UserAccessPolicy

**Field Name** **Description**

```
type

```

UserAccessPolicyFilter

**Field Type**
UserAccessPolicyActionTargetType (enumeration of type string)

**Description**

Required. The type of access mechanism that the user access policy applies.

Values are:

**•** `Group`

**•** `PackageLicense`

**•** `PermissionSet`

**•** `PermissionSetGroup`

**•** `PermissionSetLicense`

**•** `Queue`

Represents a user criteria filter for a user access policy.

**Field Name** **Description**

```
columnName

operation

sortOrder

```

**Field Type**
string

**Description**
If `type` is set to `User`, this is the user field that your user criteria filter is based on.
If you set `type` to any value other than `User`, then this field isn’t used.

**Field Type**
UserAccessPolicyFilterOperation (enumeration of type string)

**Description**

Required. The operator of the user criteria filter.

Values are:

**•** `equals`

**•** `equalsIgnoreCase` —Available in API version 59.0 and later.

**•** `in`  - Available in API version 58.0 and later.

**•** `includes` —Available in API version 59.0 and later.

**•** `notEquals`

Select `in` if you want to reference multiple profiles or roles in the same user criteria
filter via the `target` field.

**Field Type**
int


Metadata Types UserAccessPolicy

**Field Name** **Description**

**Description**

Required. The numeric reference used to identify the specific user criteria filter.

```
target

type

value

```

**Field Type**
string

**Description**

Required. If `type` is set to `User`, then set this field to `User` as well. If `type` is set
to any other value, then set this field to the developer name of the specific resource
used in the user criteria filter.

**Field Type**
UserAccessPolicyFilterTargetType (enumeration of type string)

**Description**

Required. The type of resource that the user criteria filter is based on.

Values are:

**•** `Group`

**•** `PackageLicense`

**•** `PermissionSet`

**•** `PermissionSetGroup`

**•** `PermissionSetLicense`

**•** `Profile`

**•** `Queue`

**•** `User`

**•** `UserRole`

**Field Type**
string

**Description**
If `type` is set to `User`, this field is the value of the user field specified in
`columnName` that your user filter is operating on. If you set `type` to any value other
than `User`, then this field isn’t used.

Declarative Metadata Sample Definition

The following is an example of a UserAccessPolicy component.

```
<?xml version="1.0" encoding="UTF-8"?>

<UserAccessPolicy xmlns="http://soap.sforce.com/2006/04/metadata">

   <booleanFilter>1 AND 2</booleanFilter>

   <description>Policy to assign Sales Rep PSG to active Sales Reps.</description>

   <masterLabel>Sales Rep Migration</masterLabel>

```


Metadata Types UserAccessPolicy

```
      <order>3</order>

      <status>Design</status>

      <triggerType>CreateAndUpdate</triggerType>

      <userAccessPolicyActions>

        <action>Grant</action>

        <target>SalesRepPSG</target>

        <type>PermissionSetGroup</type>

      </userAccessPolicyActions>

      <userAccessPolicyFilters>

        <operation>equals</operation>

        <sortOrder>1</sortOrder>

        <target>SalesRepCustomProfile</target>

        <type>Profile</type>

      </userAccessPolicyFilters>

      <userAccessPolicyFilters>

        <columnName>IsActive</columnName>

        <operation>equals</operation>

        <sortOrder>2</sortOrder>

        <target>User</target>

        <type>User</type>

        <value>true</value>

      </userAccessPolicyFilters>

   </UserAccessPolicy>

```

To reference multiple profiles or roles, in UserAccessPolicyFilter, set the `operator` field to `in` . Then, reference the resources’ developer
names in the `target` field, separated by commas.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <UserAccessPolicy xmlns="http://soap.sforce.com/2006/04/metadata">

      <booleanFilter>1</booleanFilter>

      <description>Policy to remove AMER Sales group from employees with one of two

   roles</description>

      <masterLabel>Remove AMER Sales Group</masterLabel>

      <status>Design</status>

      <userAccessPolicyActions>

        <action>Revoke</action>

        <target>AMERSalesPublicGroup</target>

        <type>Group</type>

      </userAccessPolicyActions>

      <userAccessPolicyFilters>

        <operation>in</operation>

        <sortOrder>1</sortOrder>

        <target>SalesOps,InsideSalesRep</target>

        <type>UserRole</type>

      </userAccessPolicyFilters>

   </UserAccessPolicy>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>UserAccessPolicy</name>

      </types>

```


### Metadata Types UserAuthCertificate

```
      <version>61.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### UserAuthCertificate

Represents a PEM-encoded user certificate. These certificates are associated with a user, and externally uploaded. The uploaded certificate
is used to authenticate the user.

This type extends the Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### UserAuthCertificate components have the suffix .userAuthCertificate and are stored in the userAuthCertificates

folder.

Version

### UserAuthCertificate components are available in API version 50.0 and later.

Fields

**Field Name** **Field Type** **Description**

`developerName` string Required: The name of the certificate with an underscore between words.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this
field.

`expirationDate` dateTime Required. The date on which the certificate expires.

`masterLabel` string Required. A user-friendly name that you create for the certificate. Limited
to 64 characters.

`serialNumber` string Required. The serial number for the certificate.

`user` string Required: The user’s name.


### Metadata Types UserCriteria

Declarative Metadata Sample Definition

The following is an example of a UserAuthCertificate component.

```
   <UserAuthCertificate xmlns="http://soap.sforce.com/2006/04/metadata"

   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

      <content xsi:nil="true"/>

      <developerName>ND_user_cert</developerName>

      <expirationDate>2030-10-01T08:30:00.000Z</expirationDate>

      <masterLabel>ND user cert</masterLabel>

      <serialNumber>1401</serialNumber>

      <user>005RM000001Zn1E</user>

   </UserAuthCertificate>

```

The following is an example `package.xml` that references the previous definition.

```
   Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>UserAuthCertificate</name>

      </types>

      <version>50.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### UserCriteria

Represents the member criteria to use in Experience Cloud site moderation rules. This type extends the Metadata metadata type and
inherits its `fullName` field..

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### UserCriteria components have the suffix site_name.user_criteria_developer_name.userCriteria and are stored in the UserCriteria folder.

Version

### UserCriteria components are available in API version 39.0 and later.

Special Access Rules

To view, create, edit, and delete moderation rules, you need the Manage Experiences or Create and Set Up Experiences permission. As
of Spring ’20 and later, only users with permission to edit moderation rules can access this object.


### Metadata Types UserProfileSearchScope

Fields

**Field Name** **Field Type** **Description**

`creationAgeInSeconds` int If specified, includes only users that were created within a specific time
frame.

`description` string The description of the user criteria.

`lastChatterActivityAgeInSeconds` int If specified, includes only members that have posted or commented in
the Experience Cloud site within a specific time frame.

`masterLabel` string Name of the user criteria.

```
userTypes

```

NetworkUserType The member type to use in moderation rules. Valid values are:
enumeration ( of

**•** Internal

type string)

**•** Internal

**•** Customer

**•** Partner

Declarative Metadata Sample Definition

The following is an example of a UserCriteria component.

```
<?xml version="1.0" encoding="UTF-8"?>

<UserCriteria xmlns="http://soap.sforce.com/2006/04/metadata">

   <masterLabel>Customer and Partner Members</masterLabel>

   <description>Member criteria matches customer and partner member</description>

   <userTypes>Partner</userTypes>

   <userTypes>Customer</userTypes>

</UserCriteria>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### UserProfileSearchScope

Reserved for internal use.

### UserProvisioningConfig

Represents information to use during a user provisioning request flow, such as the attributes for an update.This type extends the Metadata
metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.


Metadata Types UserProvisioningConfig

File Suffix and Directory Location

UserProvisioningConfig components have the suffix `.userProvisioningConfig` and are stored in the
`UserProvisioningConfigs` directory.

Version

UserProvisioningConfig components are available in API version 49.0 and later.

Fields

**Field Name** **Field Type** **Description**

`approvalRequired` string Indicates whether approvals are required for provisioning users for the
associated connected app. If the value is null, no approval is required.

`connectedApp` string The ID of the connected app for which users are being provisioned.

`enabled` boolean Indicates whether user provisioning is enabled for the associated
connected app ( `true` ) or not ( `false` ). Default setting is `false` .

`enabledOperations` string

`flow` string

Lists the operations, as comma-separated values, that create a user
provisioning request for the associated connected app. Allowed values
are:

**•** `Create`

**•** `Update`

**•** `EnableAndDisable` (activation and deactivation)

**•** `SuspendAndRestore` (freeze and unfreeze)

User Provisioning flow type which includes a reference to the Apex
`UserProvisioningPlugin` class. The flow calls the third-party
service’s API to manage user account provisioning on that system.

`masterLabel` string The primary label for this object. This value is the internal label that
doesn’t get translated.

`namedCredential` string

`notes` string

The Salesforce ID of the named credential that’s used for a request. The
named credential identifies the third-party system and the third-party
authentication settings.

Serves as a place for admins to add any additional information about
the configuration. This field is for internal reference only, and is not used
by any process.

`onUpdateAttributes` string Lists the user attributes, as comma-separated values, that generate a
user provisioning request during an update.

`reconFilter` string When collecting and analyzing users on a third-party system, the plug-in
uses this filter to limit the scope of the collection.


### Metadata Types VirtualVisitConfig

**Field Name** **Field Type** **Description**

`userAccountMapping` string

Stores the attributes used to link the Salesforce user to the account on
the third-party system, in JSON format. For example:

```
{"linkingSalesforceUserAttribute":"Username",

"linkingTargetUserAttribute":"Email"}

```

Declarative Metadata Sample Definition

The following is an example of a UserProvisioningConfig component.

```
<?xml version="1.0" encoding="UTF-8"?>

<UserProvisioningConfig xmlns="http://soap.sforce.com/2006/04/metadata">

   <approvalRequired>True</approvalRequired>

   <enabled>true</enabled>

   <enabledOperations>NA</enabledOperations>

   <connectedApp>ExampleApp</connectedApp>

   <masterLabel>label</masterLabel>

   <notes>note</notes>

   <onUpdateAttributes>attri</onUpdateAttributes>

   <reconFilter>filter</reconFilter>

   <userAccountMapping>mapping</userAccountMapping>

</UserProvisioningConfig>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>UPC</members>

     <name>UserProvisioningConfig</name>

   </types>

   <version>49.0</version>

</Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### VirtualVisitConfig

Represents an external video provider configuration, which relays events from Salesforce to the provider.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.


Metadata Types VirtualVisitConfig

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

VirtualVisitConfig components have the suffix `.virtualVisitConfig` and are stored in the `VirtualVisitConfigs` folder.

Version

VirtualVisitConfig components are available in API version 54.0 and later.

Special Access Rules

Access to this metadata type requires at least one of these preferences:

**•** Video Calls: Org Pref (VideoVisits) Org preference

**•** Industries Einstein: Intelligent Form Reader (EinsteinDocReader)

**•** Industries Einstein: Sentiment Insights Account (IESentimentAnalysis)

**•** Natural Language Processing: Key phrase extraction and entity detection (NLPServiceEnabled) Org Preference and the NLP: Key
phrase extraction (KeyPhrasePrefEnabled) Org Preference

**•** Natural Language Processing (NLPServicePrefEnabled) Org Preference

Fields

**Field Name** **Description**

```
comprehendServiceType

developerName

```

**Field Type**
VirtualVisitComprehendServiceType (enumeration of type string)

**Description**
Specifies the type of service used to convert speech into text or to analyze the converted
speech text.

Valid values are:

**•** `ComprehendMedicalService`

**•** `ComprehendService`

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with a
letter, not include spaces, not end with an underscore, and not contain two consecutive
underscores. In managed packages, this field prevents naming conflicts on package


Metadata Types VirtualVisitConfig

**Field Name** **Description**

installations. With this field, a developer can change the object’s name in a managed
package and the changes are reflected in a subscriber’s organization. Label is Record
Type Name. This field is automatically generated, but you can supply your own value
if you create the record using the API.

```
experienceCloudSiteUrl

externalMsgServiceIdentifier

externalRoleIdentifier

externalUserIdentifier

fullName

isProtected

```

**Field Type**
string

**Description**
The URL of the Digital Experience site where the Video Call component is available to
portal or guest users.

**Field Type**
string

**Description**
For internal use only.

**Field Type**
string

**Description**
The ID of the role that's used to allow users to join a video call and to grant them
temporary access to certain functions needed to participate in the call.

**Field Type**
string

**Description**
For internal use only.

**Type**
string

**Properties**
Create, Group, Nillable

**Description**
The full name of the VirtualVisitConfig type in Metadata API. The full name can include
a namespace prefix. Query this field only if the query result contains no more than one
record. Otherwise, an error is returned. If more than one record exists, use multiple
queries to retrieve the records. This limit protects performance.

**Field Type**
boolean

**Description**
An auto-generated value that doesn’t currently impact the behavior of the metadata
type.


Metadata Types VirtualVisitConfig

**Field Name** **Description**

```
masterLabel

messagingRegion

namedCredential

storageBucketName

usageType

videoCallApptTypeValue

```

**Field Type**
string

**Description**

Required.

A user-friendly name for VirtualVisitConfig, which is defined when the VirtualVisitConfig
is created.

**Field Type**
string

**Description**
The region where the waiting room and messaging channel data is processed and
stored. Available in API version 57.0 and later.

**Field Type**
string

**Description**
The named credential record used to authenticate and authorize a video call vendor’s
account.

**Field Type**
string

**Description**
The name of the storage bucket that stores the meeting transcript.

**Field Type**
VirtualVisitUsageType (enumeration of type string)

**Description**
The name of the Salesforce feature for which the video call configuration record is
created.

Valid values are:

**•** `CHIME`

**•** `ENTITY_DETECTION`

**•** `INTELLIGENT_FORM_READER`

**•** `KEY_PHRASE_EXTRACTION`

**•** `SENTIMENT_ANALYSIS`

**Field Type**
string

**Description**
The default Appointment Type picklist values from the Service Appointment object
that represent a video appointment type. Use semicolons to separate multiple values.


Metadata Types VirtualVisitConfig

**Field Name** **Description**

```
videoControlRegion

visitRegion

```

**Field Type**
string

**Description**
The region where API calls related to Video Calls are made. Available in API version
57.0 and later.

**Field Type**
VirtualVisitVisitRegion (enumeration of type string)

**Description**
The region where the Video Call audio and video data is processed.

Valid values are:

**•** `af-south-1`

**•** `ap-east-1`

**•** `ap-northeast-1`

**•** `ap-northeast-2`

**•** `ap-northeast-3`

**•** `ap-south-1`

**•** `ap-southeast-1`

**•** `ap-southeast-2`

**•** `ca-central-1`

**•** `eu-central-1`

**•** `eu-north-1`

**•** `eu-south-1`

**•** `eu-west-1`

**•** `eu-west-2`

**•** `eu-west-3`

**•** `me-south-1`

**•** `sa-east-1`

**•** `us-east-1`

**•** `us-east-2`

**•** `us-west-1`

**•** `us-west-2`

Declarative Metadata Sample Definition

This is an example of a VirtualVisitConfig component.

```
<?xml version="1.0" encoding="UTF-8"?>

 <VirtualVisitConfig xmlns="http://soap.sforce.com/2006/04/metadata">

   <usageType>CHIME</usageType>

```


### Metadata Types WaveAnalyticAssetCollection

```
      <visitRegion>us-east-1</visitRegion>

      <masterLabel>vvconfig1</masterLabel>

      <experienceCloudSiteUrl>videocall_c@testcloudurl.com</experienceCloudSiteUrl>

      <namedCredential>SampleNamedCredential</namedCredential>

      <comprehendServiceType>ComprehendService</comprehendServiceType>

      <storageBucketName>comprehendbucket</storageBucketName>

      <isProtected>false</isProtected>

    </VirtualVisitConfig>

```

This is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

    <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <namespacePrefix>[namespacePrefix]</namespacePrefix>

      <fullName>deployPackage</fullName>

      <types>

         <members>*</members>

         <name>VirtualVisitConfig</name>

      </types>

      <types>

         <members>*</members>

         <name>NamedCredential</name>

      </types>

      <version>55.0</version>

    </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### WaveAnalyticAssetCollection

Represents a collection of Analytics assets. This type extends the Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

WaveAnalyticsAssetCollection components have the suffix `.collection` and are stored in the `wave` folder.

Version

WaveAnalyticsAssetCollection components are available in API version 58.0 and later.


Metadata Types WaveAnalyticAssetCollection

Fields

**Field Name** **Field Type** **Description**

`collectionType` string The collection type.

`color` string The display color for the collection.

`description` string The description that appears in the user interface.

`folder` string The internal API name of the folder or application.

`items` WaveAnalayticAssestCo **l** ectionItem A list of Analytics asset items.

`label` string The label for the collection.

`shares` FolderShare The folder sharing rules.

Declarative Metadata Sample Definition

The following is an example of a WaveAnalyticsAssetCollection component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <WaveAnalyticsAssetCollection xmlns="http://soap.sforce.com/2006/04/metadata">

     <collectionType>static</collectionType>

     <color>#1b96ff</color>

     <description>A collection of my Dashboards</description>

     <folder>Shared</folder>

     <label>My Dashboard Collection</label>

     <items>

      <item>

        <asset>Dashboard One</asset>

        <assetType>dashboard</assetType>

        <sortOrder>1</sortOrder>

      </item>

      <item>

        <asset>Dashboard Two</asset>

        <assetType>dashboard</assetType>

        <sortOrder>2</sortOrder>

      </item>

     </items>

     <shares>

      <accessLevel>EditAllContents</accessLevel>

      <sharedTo>shareswith@org.ee</sharedTo>

      <sharedToType>User</sharedToType>

     </shares>

   </WaveAnalyticsAssetCollection>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types WaveApplication

WaveAnalyticAssestCollectionItem

WaveAnalyticAssestCollectionItem represents an Analytics asset item.

**Field** **Field Type** **Description**

`asset` string The asset name.

`assetType` string The asset type.

`sortOrder` int The sort order for the asset.

### WaveApplication

Represents the Analytics application. This type extends the Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### WaveApplication components have the suffix .wapp and are stored in the wave folder.

Version

### WaveApplication components are available in API version 37.0 and later.

Fields

**Field Name** **Field Type** **Description**

`assetIcon` string The icon that represents the Analytics application.

`description` string The description that appears in the user interface.

`folder` string The internal api name of the folder or application.

`masterLabel` string The user interface label name of the folder or application.

`shares` FolderShare The folder sharing rules.

`templateOrigin` string

`templateVersion` string

The internal (unique) name of the template used to create the
application. This field is blank if the application wasn’t created from a
template.

The version assigned to the application template by the template's
creator. This field is blank if the application wasn’t created from a
template.


### Metadata Types WaveComponent

Declarative Metadata Sample Definition

The following is an example of a WaveApplication component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <WaveApplication xmlns="http://soap.sforce.com/2006/04/metadata">

     <assetIcon>/analytics/wave/web/proto/images/app/icons/11.png</assetIcon>

     <description>Application that shows my sales</description>

     <folder>edit</folder>

     <masterLabel>Sales Application</masterLabel>

     <shares>

     <accessLevel>EditAllContents</accessLevel>

     <sharedTo>shareswith@org.ee</sharedTo>

     <sharedToType>User</sharedToType>

     </shares>

   </WaveApplication>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### WaveComponent

Represents the WaveComponent object in the Analytics application. This type extends the MetadataWithContent metadata type and
inherits its `content` and `fullName` fields.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

When using Metadata API to work with Analytics components, consider that:

**•** Modifications to the `.wcomp` component are unsupported.

File Suffix and Directory Location

### WaveComponent components have the suffix .wcomp and are stored in the wave folder.

Version

### WaveComponent components are available in API version 51.0 and later.

Fields

**Field Name** **Field Type** **Description**

`application` string Required. The internal name of the application.

`description` string The component description that appears in the user interface.

`masterLabel` string Required. The component name that appears in the user interface.


### Metadata Types WaveDataflow

**Field Name** **Field Type** **Description**

`templateAssetSourceName` string Links the component to the template used to create it. Null for assets
not created from a template.

Declarative Metadata Sample Definition

The following is an example of a WaveComponent component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <WaveComponent xmlns="http://soap.sforce.com/2006/04/metadata"

   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

      <content xsi:nil="true"/>

      <application>dev__app</application>

      <masterLabel>Component1</masterLabel>

      <description>Component description</description>

   </WaveComponent>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### WaveDataflow

Represents the WaveDataflow object in the Analytics application. This type extends the MetadataWithContent metadata type and inherits
its `content` and `fullName` fields.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### WaveDataflow components have the suffix .wdf and are stored in the wave folder.

Version

### WaveDataflow components are available in API version 37.0 and later.

Fields

**Field Name** **Field Type** **Description**

`application` string The name of the Analytics application the dataflow is connected to. This
field is available in API version 48.0 and later.


### Metadata Types WaveDashboard

**Field Name** **Field Type** **Description**

`dataflowType` string

The type of the dataflow. Supported types are `User` and `Prepared` .
The default value is `User` This field is available in API version 41.0 and
later.

`description` string The dataflow description that appears in the user interface.

`masterLabel` string Required. The dataflow name that appears in the user interface.

Declarative Metadata Sample Definition

The following is an example of a WaveDataflow component.

```
<?xml version="1.0" encoding="UTF-8"?>

<WaveDataflow xmlns="http://soap.sforce.com/2006/04/metadata"

xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"> <content xsi:nil="true"/>

   <description>flow1</description>

   <masterLabel>flow1</masterLabel>

</WaveDataflow>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### WaveDashboard

Represents the WaveDashboard object in the Analytics application. This type extends the MetadataWithContent metadata type and
inherits its `content` and `fullName` fields.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

When using Metadata API to work with Analytics dashboards, consider that:

**•** Modifications to the `.wdash` component are unsupported.

**•** Modifying or removing conditional formatting from the source org or `.wdash` component doesn’t cause issues while deploying.

**•** Removing steps from the `.wdash` component causes deployment to the destination org to fail because the source dashboard
fails validation.

File Suffix and Directory Location

### WaveDashboard components have the suffix .wdash and are stored in the wave folder.

Version

### WaveDashboard components are available in API version 37.0 and later.


### Metadata Types WaveDataset

Fields

**Field Name** **Field Type** **Description**

`application` string Required. The internal name of the application.

`dateVersion` integer The date version for the dashboard. Only available in v55.0 and above.

`description` string The dashboard description that appears in the user interface.

`masterLabel` string Required. The dashboard name that appears in the user interface.

`templateAssetSourceName` string Links the dashboard to the template used to create it. Null for assets not
created from a template.

Declarative Metadata Sample Definition

The following is an example of a WaveDashboard component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <WaveDashboard xmlns="http://soap.sforce.com/2006/04/metadata"

   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

     <content xsi:nil="true"/>

     <application>dev__app</application>

     <masterLabel>Dashboard1</masterLabel>

     <description>somedesc</description>

   </WaveDashboard>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### WaveDataset

Represents the WaveDataset object in the Analytics application.This type extends the Metadata metadata type and inherits its `fullName`
field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### WaveDataset components have the suffix .wds and are stored in the wave folder.

Version

### WaveDataset components are available in API version 37.0 and later.


### Metadata Types WaveLens

Fields

**Field Name** **Field Type** **Description**

`application` string Required. The internal name of the application.

`description` string The dataset description that appears in the user interface.

`masterLabel` string Required. The user interface label name of the dataset.

`templateAssetSourceName` string Links the dataset to the template used to create it. Null for assets not
created from a template.

`type` string The type of the dataset. Dataset types include `Default`,
`Live`, `StagedData`, and `Trended` .

Declarative Metadata Sample Definition

The following is an example of a WaveDataset component.

```
   <WaveDataset>

      <application>SharedApp</application>

      <description>description</description>

      <masterLabel>datasetLabel</masterLabel>

      <type>Default</type>

   </WaveDataset>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### WaveLens

Represents the WaveLens object in the Analytics application.

This type extends to MetadataWithContent metadata type and inherits its `content` and `fullName` fields.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### WaveLens components have the suffix .wlens and are stored in the wave folder.

Version

### WaveLens components are available in API version 37.0 and later.


Metadata Types WaveLens

Fields

**Field Name** **Field Type** **Description**

`application` string Required. The internal name of the application.

`datasets` string A reference to the dataset used to create this lens.

`dateVersion` int The date version used for this lens.

`description` string The dashboard description that appears in the user interface.

`masterLabel` string Required. The user interface label name of the dashboard.

`templateAssetSourceName` string Links the lens to the template used to create it. Null for assets not created
from a template.

`visualizationType` string Required. The visualization type to be used for this lens. Valid values are:

**•** `calheatmap` —Calendar heat map

**•** `comparisontable` —Comparison table

**•** `heatmap` —Heat map

**•** `hbar` —Horizontal bar

**•** `hbarhdot` —Horizontal dot plot

**•** `matrix` —Matrix

**•** `parallelcoords` —Parallel coordinates

**•** `pie` —Donut

**•** `pivottable` —Pivot table

**•** `scatter` —Scatter plot

**•** `stackhbar` —Stacked horizontal bar

**•** `stackvbar` —Stacked vertical bar

**•** `time` —Time line

**•** `valuestable` —Values table

**•** `vbar` —Vertical bar

**•** `vdot` —Vertical dot plot

Declarative Metadata Sample Definition

The following is an example of a WaveLens component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <WaveLens xmlns="http://soap.sforce.com/2006/04/metadata"

   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

     <content xsi:nil="true"/>

     <application>dev__app</application>

     <datasets>dev__abc</datasets>

     <masterLabel>lens1</masterLabel>

     <description>lens in shared app</description>

```


### Metadata Types WaveRecipe

```
     <visualizationType>hbar</visualizationType>

   </WaveLens>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### WaveRecipe

Represents the WaveRecipe type in an Analytics application. A recipe is a saved set of steps to perform on a specific source dataset or
connected data. This type extends the MetadataWithContent metadata type and inherits its `content` and `fullName` fields.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### WaveRecipe components have the suffix .wdpr and are stored in the wave folder.

Version

### WaveRecipe components are available in API version 41.0 and later.

Fields

**Field Name** **Field Type** **Description**

`application` string The internal name of the application.

`dataflow` string Required. The dataflow ID for the Analytics recipe.

`format` string The format of the current recipe definition. Valid values are:

**•** `R2`                          - recipes created with Data Prep

**•** `R3`                          - recipes created with Data Prep (API version 49.0)

`masterLabel` string Required. The recipe name that appears in the user interface.

`securityPredicate` string A filter condition that defines row-level access to records in a recipe.

`targetDatasetAlias` string The name of the dataset the recipe saves data results into.

`templateAssetSourceName` string Links the recipe to the template used to create it. Null for assets not
created from a template.


### Metadata Types WaveTemplateBundle

Declarative Metadata Sample Definition

The following is an example of a WaveRecipe component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <WaveRecipe xmlns="http://soap.sforce.com/2006/04/metadata"

   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"> <content xsi:nil="true"/>

      <dataflow>02KB0000000b5c7MAA</dataflow>

      <format>R3</format>

      <masterLabel>recipe1</masterLabel>

      <securityPredicate>'UserId' == "$User.Id"</securityPredicate>

      <targetDatasetAlias>Dataset One</targetDatasetAlias>

   </WaveRecipe>

```

Deleting a WaveRecipe Component

Use a simple destructiveChanges.xml file with only the WaveRecipe component declared. This deletes the WaveRecipe and any related
WaveDataflow components. For more information, see Delete Components from an Organization. on page 74

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

Note: Use of the wildcard character doesn’t return the recipe’s associated dataflows.

### WaveTemplateBundle

Represents an Analytics template bundle, which can be used to create Analytics apps. A bundle contains an Analytics template definition
and all its related resources.This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

An Analytics template bundle is a folder that contains definition files for a template. Unlike other metadata components, a
### WaveTemplateBundle component isn’t represented by a single component file, but instead by a collection of JSON and CSV definition

files. Each definition file represents a resource in a template, such as lenses, dashboards, dataflows, and comma-separated values. For
example, this directory structure shows the hierarchy of the folders and files for one Analytics Template definition, template1.

```
   waveTemplates

      template1

        template-info.json

        variables.json

        ui.json

        extFiles

           PostalCodes.csv

```

Analytics template bundles must be under a top-level folder that’s named `waveTemplates` . Each bundle must have its own subfolder
under the `waveTemplates` folder and be named with the template's fully qualified API name. The bundle folder must contain a
template-info.json file to specify the metadata about the template and the references to other definition files. An entire bundle doesn’t
have a suffix and definition files can have one of the following suffixes.


### Metadata Types WaveXmd

Version

WaveTemplateBundle components are available in API version 35.0 and later.

Special Access Rules

Definitions can be created in both managed and unmanaged packages.

Fields

**Field Name** **Field Type** **Description**

`assetIcon` string The icon to use by default for new Analytics apps based on this template.
Valid values are `1.png` through `20.png` .

`description` string The specification of the template.

`label` string Required. The label of the template.

`templateType` string Required. The type of the template. Valid values are:

**•** `App`

**•** `Dashboard`

**•** `Lens`

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### WaveXmd

Represents the WaveXmd object in the Analytics application.This type extends the Metadata metadata type and inherits its `fullName`
field.

File Suffix and Directory Location

### WaveXmd components have the suffix .xmd and are stored in the wave folder.


Metadata Types WaveXmd

Version

WaveXmd components are available in API version 39.0 and later.

Fields

**Field Name** **Field Type** **Description**

`application` string The name of the Analytics application the XMD is associated with.
Available in API version 43.0 and later.

`dataset` string Required. Specifies the dataset associated with this XMD.

`datasetConnector` string The name of the connector source for the dataset.

`datasetFullyQualifiedName` string Specifies the fully qualified name of the dataset version associated with
this XMD.

`dates` WaveXmdDate List of dates, with formatting information.

`dimensions` WaveXmdDimension List of dimensions, with formatting information.

`measures` WaveXmdMeasure List of measures, with formatting information.

`organizations` WaveXmdOrganization List of organizations, for multi-organization support.

`origin` string The origin of the dataset version.

`type` string The XMD type. Valid values are:

**•** `System`

**•** `User`

**•** `Main`

**•** `Asset`

Available in API version 43.0 and later.

`waveVisualization` string The visualization behavior for Analytics assets. Valid values are:

**•** `dashboard`

**•** `lens`

Available in API version 43.0 and later.

WaveXmdDate

WaveXmdDate represents a date.

**Field** **Field Type** **Description**

`alias` string Required. Alias of the Date column.

`compact` boolean Indicates whether the date is displayed in compact form ( `true` )
or not ( `false` ).


Metadata Types WaveXmd

**Field** **Field Type** **Description**

`dateFieldDay` string The day field.

`dateFieldEpochDay` string The epoch day field.

`dateFieldEpochSecond` string The epoch second field.

`dateFieldFiscalMonth` string The fiscal month field.

`dateFieldFiscalQuarter` string The fiscal quarter field.

`dateFieldFiscalWeek` string The fiscal week field.

`dateFieldFiscalYear` string The fiscal year field.

`dateFieldFullYear` string The full year field.

`dateFieldHour` string The hour field.

`dateFieldMinute` string The minute field.

`dateFieldMonth` string The month field.

`dateFieldQuarter` string The quarter field.

`dateFieldSecond` string The second field.

`dateFieldWeek` string The week field.

`dateFieldYear` string The year field.

`description` string The description of the date column.

`firstDayOfWeek` int Required. Represents the first day of the week.

`fiscalMonthOffset` int Required. Offset number of months for the fiscal year in relation
to the calendar year.

`isYearEndFiscalYear` boolean Indicates whether the year end is the fiscal year ( `true` ) or not
( `false` ).

`label` string The label of the date column.

`showInExplorer` boolean Indicates whether the date is displayed in the explorer ( `true` )
or not ( `false` ).

`sortIndex` int Required. The index value the system assigns to indicate where
the item appears in a list.

`type` string Required. The type of date. Valid values are:

**•** `Date` —A legacy date type. Available when the time zone
isn’t enabled.

**•** `DateOnly` —A date type without an associated time.
Available when the time zone is enabled.

**•** `DateTime` —A date type that contains both date and time
parts. Available when the time zone is enabled.


Metadata Types WaveXmd

WaveXmdDimension

WaveXmdDimension represents a dimension.

**Field** **Field Type** **Description**

`conditionalFormatting` WaveXmdFormattingProperty The conditional formatting property for the dimension. Available
in API version 43.0 and later.

`customActions` WaveXmdDimensionCustomAction Custom actions linked to this dimension.

`customActionsEnabled` boolean Indicates whether the dimension has custom actions enabled
( `true` ) or not ( `false` ).

`dateFormat` string The format used for a date that is a dimension.

`defaultAction` string The default action assigned to a dimension. An action for a
dimension can be `openSfdcRecord`,

`openActionsMenu`, `none`, or a valid API name with dot
notation like `Global.LogACall` or `FeedItem.Post` .

`description` string The description of the dimension.

`field` string Required. The field name of the dimension (used in queries).

`fullyQualifiedName` string The fully qualified name of the dimension.

`imageTemplate` string The image template.

`isDerived` boolean Required. Indicates whether the dimension is derived ( `true` )
or not ( `false` ).

`isMultiValue` boolean Indicates whether the dimension is multi-value ( `true` ) or not
( `false` ).

`label` string The label for the dimension.

`linkTemplate` string The template for formatting a link.

`linkTemplateEnabled` boolean Indicates whether the dimension has link templates enabled
( `true` ) or not ( `false` ).

`linkTooltip` string The tooltip to be displayed for links.

`members` WaveXmdDimensionMember The member overrides for a dimension.

`origin` string The origin of this dimension.

`recordDisplayFields` WaveXmdRecordDisplayLookup Ordered list of dimensions. The list defines the default order in
which to display the dimensions in the user interface.

`recordIdField` string The record ID for this dimension.

`recordOrganizationIdField` string The record organization ID for this dimension.

`salesforceActions` WaveXmdDimensionSalesforceAction Salesforce actions linked to this dimension.


Metadata Types WaveXmd

**Field** **Field Type** **Description**

`salesforceActionsEnabled` boolean Indicates whether the dimension has Salesforce actions enabled
( `true` ) or not ( `false` ).

`showDetailsDefaultFieldIndex` int Default order in which to show the dimensions in the user
interface.

`showInExplorer` boolean Indicates whether the dimension is displayed in the explorer
( `true` ) or not ( `false` ).

`sortIndex` int Required. The index value the system assigns to indicate where
the item appears in a list.

WaveXmdFormattingProperty

WaveXmdFormattingProperty represents an XMD formatting property for conditional formatting.

**Field** **Field Type** **Description**

`formattingBins` WaveXmdFormattingBin The formatting bins for this property.

`formattingPredicates` WaveXmdFormattingPredicate The formatting predicates for this property.

`property` string Required. The property name.

`referenceField` string Required. The reference field for this property.

`sortIndex` int Required. The index value the system assigns to indicate where
the item appears in a list.

`type` string Required. The property type.

WaveXmdFormattingBin

WaveXmdFormatttingBin represents an XMD formatting bin for conditional formatting.

**Field** **Field Type** **Description**

`bin` string Required. The formatting bin.

`formatValue` string Required. The format value for the bin.

`label` string Required. The label for the bin.

`sortIndex` int Required. The index value the system assigns to indicate where
the item appears in a list.

WaveXmdFormattingPredicate

WaveXmdFormattingPredicate represents an XMD formatting predicate for conditional formatting.


Metadata Types WaveXmd

**Field** **Field Type** **Description**

`formatValue` string Required. The format value for the predicate.

`operator` string Required. The operator for the predicate.

`sortIndex` int Required. The index value the system assigns to indicate where
the item appears in a list.

`value` string Required. The value for the predicate.

WaveXmdDimensionCustomAction

WaveXmdDimensionCustomAction represents a custom action in a dimension.

**Field** **Field Type** **Description**

`customActionName` string Required. The name of this custom action.

`enabled` boolean Required. Indicates whether the action is enabled for a specific
dimension ( `true` ) or not ( `false` ).

`icon` string The icon for the action.

`method` string The method for the action.

`sortIndex` int Required. The index value the system assigns to indicate where
the item appears in a list.

`target` string The target for the action.

`tooltip` string The tooltip for the action.

`url` string The URL for the action.

WaveXmdDimensionMember

WaveXmdDimensionMember represents a dimension.

**Field** **Field Type** **Description**

`color` string The color for the member.

`label` string The label for the member.

Note: Multi-line text isn't supported

`member` string Required. The member value.

`sortIndex` int Required. The index value the system assigns to indicate where
the item appears in a list.


Metadata Types WaveXmd

WaveXmdRecordDisplayLookup

WaveXmdDimensionRecordDisplayLookup represents a record display field.

**Field** **Field Type** **Description**

`recordDisplayField` string Required. The field to display.

`sortIndex` int Required. The index value the system assigns to indicate where
the item appears in a list.

WaveXmdDimensionSalesforceAction

WaveXmdDimensionSalesforceAction represents an action in a dimension.

**Field** **Field Type** **Description**

`enabled` boolean Required. Indicates whether the action is enabled for a specific
dimension ( `true` ) or not ( `false` ).

`salesforceActionName` string Required. The name of the action.

`sortIndex` int Required. The index value the system assigns to indicate where
the item appears in a list.

WaveXmdMeasure

WaveXmdMeasure represents a measure.

**Field** **Field Type** **Description**

`conditionalFormatting` WaveXmdFormattingProperty The conditional formatting for the measure. Available in API
version 43.0 and later.

`currencies` WaveXmdMeasure[] The list of currency formats for multiple currencies. Use this field
to set the format for each currency used in the dataset.

`currencyCode` String The default currency code for the dataset.

`dateFormat` string The format used for a date that is a measure.

`description` string The description of the measure.

`field` string Required. The field name of the measure (used in queries).

`formatCustomFormat` string The original (XMD 1.1) format array as a single string.

`formatDecimalDigits` int The number of digits displayed after the decimal place.

`formatDecimalSeparator` string The custom separator for the decimal place. Available in API
version 48.0 and later.

`formatIsNegativeParens` boolean Indicates whether to display negative numbers with parentheses,
rather than a minus sign ( `true` ) or not ( `false` ).


Metadata Types WaveXmd

**Field** **Field Type** **Description**

`formatPrefix` string The prefix placed before the field value.

`formatSuffix` string The suffix placed after the field value.

`formatThousandsSeparator` string The custom separator for the thousands place. Available in API
version 48.0 and later.

`formatUnit` string The unit string for the measure. For example, ' `cm` '.

`formatUnitMultiplier` double The multiplier for the unit.

`fullyQualifiedName` string The fully qualified name of the measure.

`isDerived` boolean Required. Indicates whether the measure is derived ( `true` ) or
not ( `false` ).

`isMultiCurrency` boolean Indicates whether multiple currencies are available for this
dataset ( `true` ) or not ( `false` ).

`label` string The label for the measure.

`origin` string The origin of the measure.

`showDetailsDefaultFieldIndex` int Default order in which to show the measures in the user
interface.

`showInExplorer` boolean Indicates whether the measure is displayed in the explorer
( `true` ) or not ( `false` ).

`sortIndex` int Required. The index value the system assigns to indicate where
the item appears in a list.

WaveXmdOrganization

WaveXmdOrganization represents a Salesforce organization.

**Field** **Field Type** **Description**

`instanceUrl` string Required. The instance URL for the organization.

`label` string Required. The label for the organization.

`organizationIdentifier` string Required. The ID of the organization.

`sortIndex` int Required. The index value the system assigns to indicate where
the item appears in a list.

Declarative Metadata Sample Definition

The following is an example of a WaveXmd component for an Asset XMD belonging to a dashboard.

```
   <WaveXmd>

      <dataset xsi:nil="true"/>

```


Metadata Types WaveXmd

```
      <dimesions>

        <conditionalFormatting>

           <formattingBins>

             <bin>*</bin>

             <formatValue>#FFFFFF</formatValue>

             <label xsi:nil="true"/>

             <sortIndex>0</sortIndex>

           </formattingBins>

           <formattingBins>

             <bin>0</bin>

             <formatValue>#000000</formatValue>

             <label xsi:nil="true"/>

             <sortIndex>1</sortIndex>

           </formattingBins>

           <property>chartColor</property>

           <referenceField>count</referenceField>

           <sortIndex xsi:nil="true"/>

           <type>multiple</type>

        </conditionalFormatting>

        <field>all_1.ALL</field>

        <isDerived>false</isDerived>

        <sortIndex>0</sortIndex>

      </dimensions>

      <measures>

        <conditionalFormatting>

           <formattingBins>

             <bin>*</bin>

             <formatValue>#FFFFFF</formatValue>

             <label xsi:nil="true"/>

             <sortIndex>0</sortIndex>

           </formattingBins>

           <formattingBins>

             <bin>0</bin>

             <formatValue>#000000</formatValue>

             <label xsi:nil="true"/>

             <sortIndex>1</sortIndex>

           </formattingBins>

           <property>chartColor</property>

           <referenceField>count</referenceField>

           <sortIndex xsi:nil="true"/>

           <type>multiple</type>

        </conditionalFormatting>

        <field>all_1.count</field>

        <formatCustomFormat>[&quot;#,###.##%&quot;,1]</formatCustomFormat>

        <isDerived>false</isDerived>

        <sortIndex>0</sortIndex>

      </measures>

      <type>Asset</type>

      <waveVisualization>dashboard</waveVisualization>

   </WaveXmd>

```


### Metadata Types WebStoreBundle WebStoreBundle

For internal use only.

### WebStoreTemplate

Represents a configuration for creating commerce stores.

This type extends the Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### WebStoreTemplate components have the suffix .webstoretemplate and are stored in the webstoretemplate folder.

Version

### WebStoreTemplate components are available in API version 49.0 and later.

Special Access Rules

A B2B Commerce or D2C Commerce license and access to Commerce objects is required.

Fields

**Field Name** **Field Type** **Description**

`autoFacetingEnabled` boolean Indicates whether auto faceting is enabled ( `true` ) or not ( `false` ). If
enabled (True), the most relevant search facets are automatically

returned, in addition to the configured search facets, in the product
search results. If disabled (False), only the configured search facets are
returned. The default is `False` [. See Add Product Search Filters (Facets)](https://help.salesforce.com/s/articleView?id=commerce.comm_search_add_filters.htm&type=5&language=en_US)
for more information. This field is available in API version 50.0 or later.

`cartAsyncProcessingEnabled` boolean

`cartCalculateEnabled` boolean

`cartToOrderAutoCustomFieldMapping` boolean

Indicates whether add-to-cart requests are processed asynchronously
( `True` ) or not ( `False` ). The default value is `True` . This field is available
in API version 59.0 or later.

Indicates whether the cart calculate extension is enabled ( `True` ) or not
( `False` ). The default value is `False` . This field is available in API version
59.0 or later.

Indicates whether custom field mapping for cart and order objects is
enabled ( `True` ) or not ( `False` ). The default value is `True` . This field
is available in API version 57.0 or later.


Metadata Types WebStoreTemplate

**Field Name** **Field Type** **Description**

`checkoutTimeToLive` int Amount of time in minutes that a checkout stays active and doesn’t
expire. This field is available in API version 52.0 and later.

`checkoutValidAfterDate` dateTime

A timestamp in the default server timezone (GMT). All checkouts that
start before this date are considered expired. This field is available in API
version 52.0 and later.

`commerceEinsteinActivitiesTracked` boolean Indicates whether Commerce Einstein activities tracking is enabled
( `true` ) or not ( `false` ).

`commerceEinsteinDeployed` boolean Indicates whether Commerce Einstein is deployed ( `true` ) or not
( `false` ).

`country` string

Two-digit ISO code of the store's country. Purchases can be shipped only
to the country assigned to the store. Valid for only D2C stores. This field
is available in API version 56.0 and later.

`defaultCurrency` string The template’s default currency setting for new records.

`defaultLanguage` string Required. The template’s default language setting for new records.

```
defaultTaxLocaleType

```

TaxLocaleType Required. The template’s default tax type for your webstore. Possible
(enumeration of values include:
type string)

**•** `Automatic`

**•** `Gross`

**•** `Net`

`description` string The description of the template.

`duplicateCartItemsEnabled` boolean

Indicates whether a cart can include multiple items with the same
product ID ( `True` ) or not ( `False` ). The default value is `False` . This
field is available in API version 59.0 or later.

`guestBrowsingEnabled` boolean Indicates whether guest browsing is enabled for this store. Set the option
to `True` to allow guest buyers access to products in the store.

`guestCartEnabled` boolean

`guestCheckoutEnabled` boolean

Required. Indicates whether guest cart access is enabled for a store
created with an LWR template. Set the option to `True` to allow guest
buyers access to products in the store.

This field is available in API version 58.0 and later.

Required. Indicates whether guest checkout access is enabled for a store
created with an LWR template. Set the option to `True` to allow guest
buyers access to products in the store.

This field is available in API version 58.0 and later.

`masterLabel` string Required. The original (untranslated) name of a label. Each translated
label is paired with its original untranslated version.

`maxValuesPerFacet` int Maximum number of values that can be added to a facet.


Metadata Types WebStoreTemplate

**Field Name** **Field Type** **Description**

`orderActivationStatus` string Status of the order. Possible values include:

**•** `Activated`

**•** `Draft`

This field is available in API version 55.0 and later.

```
orderLifeCycleType

```

OrderLifeCycleType The order life cycle type. Possible values include:
(enumeration of

**•** `MANAGED`

type string)

**•** `MANAGED`

**•** `UNMANAGED`

This field is available in API version 55.0 and later.

`paginationSize` int Number of results displayed per search results page.

`preserveGuestCartEnabled` boolean

Required. Indicates whether cart contents are preserved when a guest
logs in to the store. Set the option to `True` to preserve guest carts.

This field is available in API version 60.0 and later.

```
pricingStrategy

productGrouping

```

PricingStrategy Required. The price selected to display to buyers. Possible values include:
(enumeration of

**•** `LowestPrice`

type string)

ProductGrouping
(enumeration of
type string)

**•** `LowestPrice`

**•** `Priority`

The default value is `LowestPrice` .

Determines whether product variations are listed individually in search
results or are represented by the parent product, which links to its
children. Possible values are:

**•** `NoGrouping` —Variations are listed individually in search results.

**•** `VariationParent` —The parent product is returned in search
results with a link to its children.

The default value is `VariationParent` . This field is available in API
version 52.0 and later.

`skipAdditionalEntitlementCheckForSearch` boolean By default, user entitlement checks are run as part of a search index
rebuild and again when product search results are returned. Skips the

second check to promote faster search performance. Set the option to
`True` to skip additional entitlement checks on a search. This field is
available in API version 52.0 and later.

`skuDetectionEnabled` boolean Indicates whether SKU detection is enabled ( `true` ) or not ( `false` ).

`splitShipmentEnabled` boolean Required. Indicates whether split shipments are enabled ( `true` ) or not
( `false` ).

`supportedCurrencies` string Currencies supported for store template.

`supportedLanguages` string Required. Languages supported for store template.

`supportedShipToCountries` string Countries that a store created from the template can ship to.


Metadata Types WebStoreTemplate

**Field Name** **Field Type** **Description**

```
type

```

WebStoreType Required. The type of store configuration, `B2C`, `B2B`, `or B2CE` . Default
(enumeration of is B2B.
type string)

Declarative Metadata Sample Definition

The following is an example of a web store template component.

```
<?xml version="1.0" encoding="UTF-8"?>

<WebStoreTemplate xmlns="http://soap.sforce.com/2006/04/metadata">

   <autoFacetingEnabled>true</autoFacetingEnabled>

   <cartAsyncProcessingEnabled>true</cartAsyncProcessingEnabled>

   <cartCalculateEnabled>false</cartCalculateEnabled>

   <cartToOrderAutoCustomFieldMapping>true</cartToOrderAutoCustomFieldMapping>

   <checkoutTimeToLive>10</checkoutTimeToLive>

   <checkoutValidAfterDate>2020-08-10T09:26:50</checkoutValidAfterDate>

   <commerceEinsteinActivitiesTracked>false</commerceEinsteinActivitiesTracked>

   <commerceEinsteinDeployed>false</commerceEinsteinDeployed>

   <country>US</country>

   <defaultCurrency>USD</defaultCurrency>

   <defaultLanguage>ENGLISH</defaultLanguage>

   <defaultTaxLocaleType>Net</defaultTaxLocaleType>

   <description>WebStore description</description>

   <duplicateCartItemsEnabled>false</duplicateCartItemsEnabled>

   <guestBrowsingEnabled>true</guestBrowsingEnabled>

   <guestCartEnabled>false</guestCartEnabled>

   <guestCartTimeToLive>10</guestCartTimeToLive>

   <guestCheckoutEnabled>false</guestCheckoutEnabled>

   <masterLabel>WebStore</masterLabel>

   <maxValuesPerFacet>99</maxValuesPerFacet>

   <orderActivationStatus>Activated</orderActivationStatus>

   <orderLifeCycleType>MANAGED</orderLifeCycleType>

   <paginationSize>9</paginationSize>

   <preserveGuestCartEnabled>false</preserveGuestCartEnabled>

   <pricingStrategy>Priority</pricingStrategy>

   <productGrouping>VariationParent</productGrouping>

  <skipAdditionalEntitlementCheckForSearch>true</skipAdditionalEntitlementCheckForSearch>

   <skuDetectionEnabled>false</skuDetectionEnabled>

   <supportedCurrencies>USD</supportedCurrencies>

   <supportedLanguages>en_us</supportedLanguages>

   <supportedShipToCountries>CA;US</supportedShipToCountries>

   <splitShipmentEnabled>false</splitShipmentEnabled>

   <type>B2B</type>

</WebStoreTemplate>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

```


### Metadata Types Workflow

```
        <members>*</members>

        <name>WebStoreTemplate</name>

      </types>

      <version>60.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### Workflow

Represents the metadata associated with a workflow rule. A workflow rule sets workflow actions into motion when its designated
conditions are met. You can configure workflow actions to execute immediately when a record meets the conditions in your workflow
rule, or set time triggers that execute the workflow actions on a specific day. Use this metadata type to create, update, or delete workflow
rule definitions.

For more information, see Workflow in Salesforce Help. This type extends the Metadata metadata type and inherits its `fullName` field.

When using a manifest file, retrieve all workflow components using this code.

```
   <types>

      <members>*</members>

      <name>Workflow</name>

   </types>

```

Declarative Metadata File Suffix and Directory Location

### Workflow files have the suffix .workflow . There’s one file per standard or custom object that has workflow. These files are stored in

the `workflows` directory of the corresponding package.

Version

### Workflow rules are available in API version 13.0 and later. Workflow

This metadata type represents the valid types of workflow rules and actions associated with a standard or custom object.

**Field Name** **Field Type** **Description**

### alerts WorkflowAlert[] An array of all alerts for the object associated with the workflow. fieldUpdates WorkflowFieldUpdate[] An array of all field updates for the object associated with the

workflow.


Metadata Types Workflow

**Field Name** **Field Type** **Description**

`flowActions` WorkflowFlowAction[]

An array of flow triggers for the object associated with the
workflow. Available in API version 30.0 and later.

The pilot program for flow trigger workflow actions is closed. If
you already enabled the pilot in your org, you can continue to

create and edit flow trigger workflow actions. If you didn’t enable
the pilot, use Flow Builder to create a record-triggered flow, or
use Process Builder to launch a flow from a process.

`fullName` string The developer name used as a unique identifier for API access.
The `fullName` can contain only underscores and

alphanumeric characters. It must be unique, begin with a letter,
not include spaces, not end with an underscore, and not contain
two consecutive underscores. This field is inherited from the
Metadata component.

`knowledgePublishes` WorkflowKnowledgePublish[] An array of Salesforce Knowledge Workflow Publishes associated
with the workflow. Available in API version 27.0 and later.

`outboundMessages` WorkflowOutboundMessage[] An array of all the outbound messages for the object associated
with the workflow.

`rules` WorkflowRule[] An array of all the objects associated with the workflow.

`tasks` WorkflowTask[] An array of all the tasks for the object associated with the
workflow.

WorkflowActionReference

WorkflowActionReference represents one of the workflow actions.

**Field Name** **Field Type** **Description**

`name` string Required. The name of the workflow action.

`type` WorkflowActionType Required. Available types of workflow actions:
(enumeration of type string)

**•** `Alert`

**•** `FieldUpdate`

**•** `FlowAction` —Available in API version 30.0 and later

**•** `OutboundMessage`

**•** `Task`

The pilot program for flow trigger workflow actions is closed. If you
already enabled the pilot in your org, you can continue to create
and edit flow trigger workflow actions. If you didn't enable the pilot,
use Flow Builder to create a record-triggered flow, or use Process
Builder to launch a flow from a process.


Metadata Types Workflow

WorkflowAlert

WorkflowAlert represents an email alert associated with a workflow rule.

**Field Name** **Field Type** **Description**

`ccEmails` string[]

Additional email addresses. This field is similar to the CC field
in email clients.

For the email to be sent successfully, set a value for
`ccEmails` or `recipients` . You can set values for both

fields. The value of `ccEmails` can include up to 5 different
email addresses.

`description` string Required. A description of the email alert. Available in API
version 16.0 and later.

`fullName` string Required. The developer name used as a unique identifier for
API access. The `fullName` can contain only underscores

and alphanumeric characters. It must be unique, begin with
a letter, not include spaces, not end with an underscore, and
not contain two consecutive underscores. This field is inherited
from the Metadata component.

`protected` boolean Required. Indicates whether this component is protected
( `true` ) or not ( `false` ). Protected components can’t be linked

to or referenced by components created in the installing
organization.

`recipients` WorkflowEmailRecipient[]

The recipients for the email.

For the email to be sent successfully, set a value for
`ccEmails` or `recipients` . You can set values for both
fields.

`senderAddress` string The address in the From field for the email alert. With this
address, you can use a standard global email address for your

organization, such as `support@company.com`, instead
of the default From field, which is the email address of the
person who updates the record. You can only specify a value
in this field if the `senderType` is set to
`OrgWideEmailAddress` . See Organization-Wide Email
Addresses in Salesforce Help.

`senderType` ActionEmailSenderType The email used as the sender’s From and Reply-To addresses.
(enumeration of type string) These values are valid.

**•** `CurrentUser` —The email address of the person
updating the record. This value is the default setting.

**•** `DefaultWorkflowUser` —The email address of the
default workflow user. If the email alert is installed from a
package, this field value is changed to `CurrentUser` .


Metadata Types Workflow

**Field Name** **Field Type** **Description**

**•** `OrgWideEmailAddress` —A verified global email
address for your organization, such as
`support@company.com` .

`template` string

WorkflowEmailRecipient

Required. Named reference to an EmailTemplate. This email
template isn’t required to exist in the zip file, but it must exist
in Metadata API.

Lightning email templates aren’t packageable. We recommend
using a Classic email template.

WorkflowEmailRecipient represents a recipient for an email alert associated with a workflow rule.

**Field Name** **Field Type** **Description**

`field` string Name of the field referenced in `type` . The field named is of
the type specified in `type` .

`recipient` string The recipients for the email. Depending on the type selected,
this field is required.

`type` ActionEmailRecipientTypes Named reference to an EmailTemplate component. Valid values
(enumeration of type string) are:

**•** `accountOwner` —The email is sent to the record’s
account owner. For example, the Account owner for an
Opportunity.

**•** `accountTeam` —Only applicable on the Account object.
The email is sent to everyone on that Account’s account
team.

**•** `campaignMemberDerivedOwner` —Emails are sent
to lead and contact owners when contacts are added to a
campaign or in response to a campaign.

**•** `contactLookup` —The email is sent to a contact whose
value is looked up from a field on the record. For this value,
the `field` field must reference a Contact.

**•** `creator` —The email is sent to the record’s creator.

**•** `customerPortalOwner` —The email is sent to a
specific self-service portal user. For this value, the recipient
field must reference a self-service portal user by their
username.

**•** `email` —The email is sent to an email address whose value
is looked up from a field on the record. For this value, the
`field` field must reference an email field.


Metadata Types Workflow

**Field Name** **Field Type** **Description**

**•** `group` —The email is sent to all users in a group. For this
value, the recipient field must reference a group by group
name.

**•** `opportunityTeam` —Only applicable on the
Opportunity object. The email is sent to everyone on that
Opportunity’s opportunity team.

**•** `owner` —The email is sent to the record’s owner.

**•** `partnerUser` —The email is sent to a specific partner
user. For this value, the recipient field must reference a
partner user by username.

**•** `portalRole`                             - Like `role`, but for portal roles only.

**•** `portalRoleSubordinates`                             - Like
`roleSubordinates`, but for portal roles only.

**•** `role` —The email is sent to all users in a role. For this value,
the recipient field must reference a role name in the role
hierarchy.

**•** `roleSubordinates` —The email is sent to all users in
a role subordinate. For this value, the recipient field must
reference a role.

**•** `roleSubordinatesInternal` —Like
`roleSubordinates`, but for internal portal roles only.

**•** `user` —The email is sent to a specific user. For this value,
the recipient field must reference a user by username.

**•** `userLookup` —The email is sent to a user whose value
is looked up from a field on the record. For this value, the
`field` field must reference a user foreign key field.

WorkflowFieldUpdate

WorkflowFieldUpdate represents a workflow field update. With field updates, you can automatically update a field value to one that you
specify when a workflow rule is triggered.

**Field Name** **Field Type** **Description**

`description` string The description of the field update. This information is useful to
track the reasoning for initially configuring the field update.

`field` string Required. The field on the object for the workflow to be updated.

`formula` string If the `operation` field value is `Formula`, the formula used
to compute the new field value.

`fullName` string Required. The developer name used as a unique identifier for API
access. The `fullName` can contain only underscores and

alphanumeric characters. It must be unique, begin with a letter,


Metadata Types Workflow

**Field Name** **Field Type** **Description**

not include spaces, not end with an underscore, and not contain
two consecutive underscores. This field is inherited from the
Metadata component.

`literalValue` string If the `operation` field value is `Literal`, the literal value for
the field.

`lookupValue` string If the `operation` field value is `lookupValue`, the lookup
value that is referenced.

`lookupValueType` LookupValueType The type of object that the `lookupValue` field value is
(enumeration of type string) referencing. The valid values are:

**•** `Queue`

**•** `RecordType`

**•** `User`

`name` string Required. A name for the component. Available in version API
16.0 and later.

`notifyAssignee` boolean Required. Notify the assignee when the field is updated.

`operation` FieldUpdateOperation Required. The operation that computes the value with which to
(enumeration of type string) update the field. Valid values are:

**•** `Formula` —Indicates the field is set to a formula. If set, the
formula must be a valid formula.

**•** `Literal` —Indicates the field is set to a literal value. If set,
the literalValue must be a valid literal value for this field.

**•** `LookupValue` —Similar to Literal, but for an object
reference, such as a contact, user, or account. If set, the
`lookupValue` element must be set. Only User is supported
in the current API.

**•** `NextValue` —Indicates that the field will be set to its next
value. Only allowed when the field update references a picklist.

**•** `Null` —Indicates that the field is set to null.

**•** `PreviousValue` —Indicates that the field is set to its
previous value. Only allowed when the field update references
a picklist.

`protected` boolean

Required. Indicates whether this component is protected ( `true` )
or not ( `false` ). Protected components can’t be linked to or
referenced by components created in the installing organization.

`reevaluateOnChange` boolean When set to `true`, if the field update changes the field’s value,
all workflow rules on the associated object are reevaluated. Any

workflow rules whose criteria are met as a result of the field value
change are triggered.


Metadata Types Workflow

**Field Name** **Field Type** **Description**

If any of the triggered workflow rules result in another field update
that’s also enabled for workflow rule reevaluation, a domino effect
occurs, and more workflow rules can be reevaluated as a result of
the newly triggered field update. This cascade of workflow rule
reevaluation and triggering can happen up to 5 times after the
initial field update that started it.

`targetObject` string Object set if the change is detected on a child record. If set, the
object points to the foreign key reference on the child object that

points to the parent. For example, if `EmailMessage` child
record is changed, `EmailMessage.ParentId` points to
the `Case` parent. This field is named `sourceField` before
version 14.0. The field name change is automatically handled
between versions and doesn’t require any manual editing of
existing XML component files.

WorkflowFlowAction

Represents a flow trigger, which is a workflow action that launches a flow. Available in API version 30.0 and later. For more information,
see these topics in Salesforce Help.

**•** Define a Flow Trigger for Workflow (Pilot)

**•** Flow Trigger Considerations (Pilot)

Note:

**•** The pilot program for flow trigger workflow actions is closed. If you already enabled the pilot in your org, you can continue to
create and edit flow trigger workflow actions. If you didn’t enable the pilot, use Flow Builder to create a record-triggered flow,
or use Process Builder to launch a flow from a process.

**•** Test mode for flow triggers isn’t supported in the Metadata API. If you want a flow trigger to run the latest flow version when
an administrator causes the workflow rule to fire, enable test mode via the user interface after deployment.

**Field Name** **Field Type** **Description**

`description` string Describes the flow trigger.

`flow` string Required. API name of the flow that this workflow action launches.

`flowInputs` WorkflowFlowActionParameter[] An array of values to pass into flow variables when launching the
flow.

`label` string Required. Name of the flow trigger.

`language` string Reserved for future use.

`protected` boolean Reserved for future use.


Metadata Types Workflow

WorkflowFlowActionParameter

Represents a value specified in the flow trigger that is passed into a variable when launching the flow.

Note: The pilot program for flow trigger workflow actions is closed. If you already enabled the pilot in your org, you can continue
to create and edit flow trigger workflow actions. If you didn’t enable the pilot, use Flow Builder to create a record-triggered flow,
or use Process Builder to launch a flow from a process.

**Field Name** **Field Type** **Description**

`name` string

`value` string

Required. API name of the flow variable.

The flow variable must have `isInput` set to `True` .

Required. Value to assign to the flow variable when launching the flow.

If the variable's data type is sObject, `value` must be a merge field that identifies a record—or a
lookup relationship field that references a record—of the same object type as the variable. For example:

**•** _`{!this}`_ —Identifies the record that fired the workflow rule.

**•** _`{!Contact}`_ —Identifies the contact associated with the record that fired the workflow rule.

**•** _`{!Asset.Account}`_ —Identifies the account associated with the asset that is associated with
the record that fired the workflow rule.

**•** _`{!SomeObject__r}`_ —Uses a lookup relationship field to identify a custom object record
associated with the record that fired the workflow rule.

For variables of other data types, you can enter a merge field or a literal value. Manually enter a literal
value when the variable requires the same value every time the flow is launched, regardless of which
record fired the workflow rule. For example, you can enter _`true`_ or _`false`_ for a variable of type
Boolean.

Supported merge fields identify a global variable or a field of the same data type as the flow variable.
For example:

**•** _`{!Id}`_ —ID of the record that fired the workflow rule.

**•** _`{!Account.Owner.Email}`_ —Email address of the account owner for the account associated
with the record that fired the workflow rule.

**•** _`{!$Organization.Country}`_ —Country of the organization.

WorkflowKnowledgePublish

WorkflowKnowledgePublish represents Salesforce Knowledge article publishing actions and information. Available in API version 27.0
and later.

**Field Name** **Field Type** **Description**

`action` KnowledgeWorkflowAction Required. The article publishing actions available when
(enumeration of type string) this rule fires. Valid values are:

**•** `PublishAsNew` —Publishes the article as a new
article.


Metadata Types Workflow

**Field Name** **Field Type** **Description**

**•** `Publish` —Publishes the article as a version of a
previously published article.

`description` string A brief article description.

`label` string

Required. Label that represents the article throughout the
Salesforce user interface.

`language` string The language of the article.

`protected` boolean Required. Indicates whether this component is protected
( `true` ) or not ( `false` ). Protected components can’t be

linked to or referenced by components created in the
installing organization.

WorkflowOutboundMessage

WorkflowOutboundMessage represents an outbound message associated with a workflow rule. Outbound messages are workflow and
approval actions that send the information you specify to an endpoint you designate, such as an external service. An outbound message
sends the data in the specified fields in the form of a SOAP message to the endpoint. For more information, see Outbound Message
Actions in Salesforce Help.

**Field Name** **Field Type** **Description**

`apiVersion` double

Required. The API version of the outbound message. Automatically set
to the current API version when the outbound message is created. Valid
API versions for outbound messages are 8.0 and 18.0 or later.

This API version is used in API calls back to Salesforce using the enterprise
or partner WSDLs. The `API Version` can only be modified by using

Metadata API. It can’t be modified using the Salesforce user interface.
This field is available in API version 18.0 and later.

If you change the `apiVersion` to a version that doesn’t support one
of the `fields` configured for the outbound message, the messages
fail until you update your outbound message listener to consume the
updated WSDL.

To monitor the status of outbound messages, from Setup, in the Quick
Find box, enter _`Outbound Messages`_, and then select **Outbound**
**Messages** inSalesforce.

`description` string Describes the outbound message.

`endpointUrl` string Required. The endpoint URL to which the outbound message is sent.

`fields` string[] The named references to the fields to be sent.

`fullName` string Required. The developer name used as a unique identifier for API access.
The `fullName` can contain only underscores and alphanumeric

characters. It must be unique, begin with a letter, not include spaces, not


Metadata Types Workflow

**Field Name** **Field Type** **Description**

end with an underscore, and not contain two consecutive underscores.
This field is inherited from the Metadata component.

`includeSessionId` boolean

Required. Set if you want the Salesforce _session ID_ included in the
outbound message. Useful if you intend to make API calls and you don’t
want to include a username and password.

`integrationUser` string Required. The named reference to the user under which this message is
sent.

`name` string Required. A name for the component. Available in version API 16.0 and
later.

`protected` boolean

`useDeadLetterQueue` boolean

WorkflowRule

Required. Indicates whether this component is protected ( `true` ) or not
( `false` ). Protected components can’t be linked to or referenced by
components created in the installing organization.

This field is only available for organizations with dead letter queue
permissions turned on. If set, this outbound message uses the dead letter
queue if normal delivery fails.

This metadata type represents a workflow rule. This type extends the Metadata metadata type and inherits its `fullName` field.

**Field Name** **Field Type** **Description**

`actions` WorkflowActionReference[] An array of references for the actions that
happen when this rule fires.

`active` boolean Required. Determines if this rule is active.

`booleanFilter` string

For advanced criteria filter, the boolean
formula. For example, `(1 AND 2) OR`
`3` .

`criteriaItems` FilterItem[] An array of the boolean criteria (conditions)
under which this rule fires. Either

`criteriaItems` or `formula` must
be set.

`description` string The description of the workflow rule.

`failedMigrationToolVersion` string The API version in which a migration fails.
Used as a reference to admins to retry the

migration when the next version is
released.

Available in API version 54.0 and later.


Metadata Types Workflow

**Field Name** **Field Type** **Description**

`formula` string

The formula condition under which this
rule first must be set, either `formula` or
`criteriaItems` .

`fullName` string The developer name used as a unique
identifier for API access. The `fullName`

can contain only underscores and
alphanumeric characters. It must be
unique, begin with a letter, not include
spaces, not end with an underscore, and
not contain two consecutive underscores.
This field is inherited from the Metadata
component.

`triggerType` WorkflowTriggerTypes (enumeration of type string) Under what conditions the trigger fires.
Valid values are:

**•** `onAllChanges` —The workflow
rule is considered on all changes.

**•** `onCreateOnly` —The workflow
rule is considered only on create.

**•** `onCreateOrTriggeringUpdate` —The
workflow rule is considered on create
and triggering updates.

`workflowTimeTriggers` WorkflowTimeTrigger Represents a set of Workflow actions,
including Field Updates, Email Alerts,

Outbound Messages, and Tasks, that
executes before or after a specified interval
of time.

WorkflowTask

This metadata type references an assigned workflow task.

**Field Name** **Field Type** **Description**

`assignedTo` string Specifies the user, role, or team to which the workflow rule
or action is assigned. The field corresponding to the value

specified here must be the same as the specified
`assignedToType` .

`assignedToType` ActionTaskAssignedToTypes Valid string values for this type are:
(enumeration of type string)

**•** `accountCreator` —When set, the task is assigned
to the record’s account's creator.

**•** `accountOwner` —When set, the task is assigned to
the record’s account owner (Opportunity).


Metadata Types Workflow

**Field Name** **Field Type** **Description**

**•** `accountTeam` —Same as WorkflowAlert type

**•** `creator` —When set, the task is assigned to the
record’s creator.

**•** `opportunityTeam` —Same as WorkflowAlert type

**•** `owner` —When set, the task is assigned to the record’s
owner.

**•** `partnerUser` —When set, the `assignedTo` field
references a partner user by username.

**•** `portalRole` —When set, the `assignedTo` field
references a Role by role name, a portal role.

**•** `role` —When set, the `assignedTo` field references
a Role by role name.

**•** `user` —When set, the `assignedTo` field references
a User by username.

`description` string The description of this workflow task.

`dueDateOffset` int Required. The offset, in days, from either the trigger date,
or the date specified in the (optional)

`offsetFromField` . The offset can be a negative
number.

`fullName` string Required. The developer name used as a unique identifier
for API access. The `fullName` can contain only

underscores and alphanumeric characters. It must be
unique, begin with a letter, not include spaces, not end
with an underscore, and not contain two consecutive
underscores. This field is inherited from the Metadata
component.

`notifyAssignee` boolean Required. Set to send an email notification when the task
is assigned.

`offsetFromField` string Optional field reference of the date field from which the
`dueDate` is computed.

`priority` string Required. The priority to assign the created task.

`protected` boolean Required. Indicates whether this component is protected
( `true` ) or not ( `false` ). Protected components can’t be

linked to or referenced by components created in the
installing organization.

`status` string Required. The status to assign the created task.

`subject` string

Required. A subject for the workflow task that’s used if an
email notification is sent when the task is assigned. Available
in API version 16.0 and later.


Metadata Types Workflow

WorkflowTimeTrigger

Represents a set of Workflow actions, including Field Updates, Email Alerts, Outbound Messages, and Tasks, that execute before or after
a specified interval of time.

**Field Name** **Field Type** **Description**

`actions` WorkflowActionReference[] An array of references for the actions that happen when this trigger
fires.

`offsetFromField` string The date type field name that the time-based workflow triggers
from, such as `Created Date`, `Last Modified Date`,

`Rule Trigger Date`, or a custom date field on the object
for which the workflow rule is defined.

`timeLength` string The numeric value of the time after or before the workflow triggers.
A negative value represents the time length before the trigger fires.

The `timeLength` is measured in either hours or days, as specified
by `workflowTimeTriggerUnit` .

`workflowTimeTriggerUnit` WorkflowTimeUnits The unit of time before or after which the time-based workflow
(enumeration of type string) triggers. Valid string values are:

**•** `Hours`

**•** `Days`

Declarative Metadata Sample Definition

Here’s the definition of a workflow rule.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Workflow xmlns="http://soap.sforce.com/2006/04/metadata">

      <alerts>

        <fullName>Another_alert</fullName>

        <description>Another alert</description>

        <protected>false</protected>

        <recipients>

           <type>accountOwner</type>

        </recipients>

        <recipients>

           <field>Contact__c</field>

           <type>contactLookup</type>

        </recipients>

        <recipients>

           <field>Email__c</field>

           <type>email</type>

        </recipients>

        <template>TestEmail/Email Test</template>

      </alerts>

      <fieldUpdates>

        <fullName>Enum_Field_Update</fullName>

        <description>Blah</description>

        <field>EnumField__c</field>

```


Metadata Types Workflow

```
        <name>Enum Field Update</name>

        <notifyAssignee>true</notifyAssignee>

        <operation>NextValue</operation>

        <protected>false</protected>

      </fieldUpdates>

      <fieldUpdates>

        <fullName>Enum_Field_Update2</fullName>

        <description>Blah</description>

        <field>EnumField__c</field>

        <literalValue>PLX2</literalValue>

        <name>Enum Field Update2</name>

        <notifyAssignee>true</notifyAssignee>

        <operation>Literal</operation>

        <protected>false</protected>

      </fieldUpdates>

      <fieldUpdates>

        <fullName>Field_Update</fullName>

        <description>TestField update desc</description>

        <field>Name</field>

        <formula>Name &amp; &quot;Updated&quot;</formula>

        <name>Field Update</name>

        <notifyAssignee>false</notifyAssignee>

        <operation>Formula</operation>

        <protected>false</protected>

      </fieldUpdates>

      <fieldUpdates>

        <fullName>Lookup_On_Contact</fullName>

        <field>RealOwner__c</field>

        <lookupValue>admin@acme.com</lookupValue>

        <name>Lookup On Contact</name>

        <notifyAssignee>false</notifyAssignee>

        <operation>LookupValue</operation>

        <protected>false</protected>

      </fieldUpdates>

      <outboundMessages>

        <fullName>Another_Outbound_message</fullName>

        <description>Another Random outbound.</description>

        <endpointUrl>http://www.test.com</endpointUrl>

        <fields>Email__c</fields>

        <fields>Id</fields>

        <fields>Name</fields>

        <includeSessionId>true</includeSessionId>

        <integrationUser>admin@acme.com</integrationUser>

        <name>Another Outbound message</name>

        <protected>false</protected>

      </outboundMessages>

      <rules>

        <fullName>BooleanFilter</fullName>

        <active>false</active>

        <booleanFilter>1 AND 2 OR 3</booleanFilter>

        <criteriaItems>

           <field>CustomObjectForWorkflow__c.CreatedById</field>

           <operation>notEqual</operation>

        </criteriaItems>

```


Metadata Types Workflow

```
        <criteriaItems>

           <field>CustomObjectForWorkflow__c.CreatedById</field>

           <operation>notEqual</operation>

           <value>abc</value>

        </criteriaItems>

        <criteriaItems>

           <field>CustomObjectForWorkflow__c.CreatedById</field>

           <operation>equals</operation>

           <value>xyz</value>

        </criteriaItems>

        <triggerType>onCreateOrTriggeringUpdate</triggerType>

      </rules>

      <rules>

        <fullName>Custom Rule1</fullName>

        <actions>

           <name>Another_alert</name>

           <type>Alert</type>

        </actions>

        <actions>

           <name>Enum_Field_Update2</name>

           <type>FieldUpdate</type>

        </actions>

        <actions>

           <fullName>Field_Update</name>

             <type>FieldUpdate</type>

        </actions>

        <actions>

           <name>Another_Outbound_message</name>

           <type>OutboundMessage</type>

        </actions>

        <actions>

           <name>Role_task_was_completed</name>

           <type>Task</type>

        </actions>

        <active>true</active>

        <criteriaItems>

           <field>CustomObjectForWorkflow__c.Name</field>

           <operation>startsWith</operation>

           <value>ABC</value>

        </criteriaItems>

        <description>Custom Rule1 desc</description>

        <triggerType>onCreateOrTriggeringUpdate</triggerType>

      </rules>

      <rules>

        <fullName>IsChangedFunctionRule</fullName>

        <active>true</active>

        <description>IsChangedDesc</description>

        <formula>ISCHANGED(Name)</formula>

        <triggerType>onAllChanges</triggerType>

      </rules>

      <tasks>

        <fullName>Another_task_was_completed</fullName>

        <assignedToType>owner</assignedToType>

        <description>Random Comment</description>

```


### Metadata Types WorkSkillRouting

```
        <dueDateOffset>20</dueDateOffset>

        <notifyAssignee>true</notifyAssignee>

        <priority>High</priority>

        <protected>false</protected>

        <status>Completed</status>

        <subject>Another task was completed</subject>

      </tasks>

      <tasks>

        <fullName>Role_task_was_completed</fullName>

        <assignedTo>R11</assignedTo>

        <assignedToType>role</assignedToType>

        <dueDateOffset>-2</dueDateOffset>

        <notifyAssignee>true</notifyAssignee>

        <offsetFromField>CustomObjectForWorkflow__c.CreatedDate</offsetFromField>

        <priority>High</priority>

        <protected>false</protected>

        <status>Completed</status>

        <subject>Role task was completed</subject>

      </tasks>

      <tasks>

        <fullName>User_task_was_completed</fullName>

        <assignedTo>admin@acme.com</assignedTo>

        <assignedToType>user</assignedToType>

        <dueDateOffset>-2</dueDateOffset>

        <notifyAssignee>true</notifyAssignee>

        <offsetFromField>User.CreatedDate</offsetFromField>

        <priority>High</priority>

        <protected>false</protected>

        <status>Completed</status>

        <subject>User task was completed</subject>

      </tasks>

   </Workflow>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### WorkSkillRouting

Represents a setup object that stores a set of WorkSkillRoutingAttribute objects. These objects are used to route a work item to an agent
who has the skills necessary to take the work. This type extends the Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### WorkSkillRouting components have the suffix workSkillRouting and are stored in the workSkillRoutings folder.


Metadata Types WorkSkillRouting

Version

WorkSkillRouting components are available in API version 46.0 and later.

Fields

**Field Name** **Field Type** **Description**

`isActive` boolean Required. Indicates whether assignment rules are active and can be
evaluated.

`masterLabel` string Required. The label for this object. This display value is the internal label
that is not translated.

`relatedEntity` string Required. Type of Salesforce object that the attributes are associated
with.

`workSkillRoutingAttributes` WorkSki **l** RoutingAttribute[] A set of mappings between work-item field values and skills. Create one
attribute mapping set for each object.

WorkSkillRoutingAttribute

Represents the routing assignments between object attributes and skills. Attributes are used to route a work item to an agent who has
the skills necessary to take the work.

Fields

**Field Name** **Field Type** **Description**

`field` string Required. Field that this attribute applies to.

`isAdditionalSkill` boolean

After a designated timeout period, additional skills are dropped from
Omni-Channel routing. The case is then routed to the best-matched
agent even if they don’t have all the skills.

`skill` string Required. Skill used to route the work item when the attribute maps to
the value selected.

`skillLevel` int Level of the skill required. This value can range from 0 to 10.

`skillPriority` int For additional skills, specify the order in which a skill is dropped if after
the Drop Additional Skills Timeout on the routing configuration, no agent

with that skill is available. Skills with a lower priority rank (9 or 10) are
dropped first. Skills with a higher priority rank (0 or 1) are dropped last.
Skills with the same priority value are dropped as a group. You can set
skill priority using attribute setup for skills-based routing or Apex code.
Available in API version 49.0 and later.

`value` string Attribute value that is assigned to the selected skill.


Metadata Types WorkSkillRouting

Declarative Metadata Sample Definition

The following is an example of a WorkSkillRouting component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <WorkSkillRouting xmlns="http://soap.sforce.com/2006/04/metadata">

     <isActive>true</isActive>

     <masterLabel>Attribute setup for skills-based routing for Case object</masterLabel>

     <relatedEntity>Case</relatedEntity>

     <workSkillRoutingAttributes>

      <field>Case.Origin</field>

      <isAdditionalSkill>false</isAdditionalSkill>

      <skill>Technical_Skill</skill>

      <skillLevel>3</skillLevel>

      <skillPriority>2</skillPriority>

      <value>Web</value>

     </workSkillRoutingAttributes>

   </WorkSkillRouting>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


## CHAPTER 14 Headers

Use headers in Metadata API calls to set options for each call.

### AllOrNoneHeader

Indicates whether to roll back all metadata changes when some of the records in a call result in failures.

CallOptions
Specifies the API client identifier.

DebuggingHeader
Specifies that the deployment result contains the debug log output, and specifies the level of detail included in the log. The debug
log contains the output of Apex tests that are executed as part of a deployment.

SessionHeader
Specifies the session ID that the login call returns. This session ID is used to authenticate all subsequent Metadata API calls.

### **`AllOrNoneHeader`**

Indicates whether to roll back all metadata changes when some of the records in a call result in failures.

Version

This header is available in API version 34.0 and later.

Supported Calls

createMetadata(), updateMetadata(), upsertMetadata(), deleteMetadata()

Usage

If this header isn’t used in API version 34.0 and later, by default a call can save a partial set of records (equivalent to
### AllOrNoneHeader=false )—the records that are processed successfully are saved and records that have failures aren’t saved.

Fields


Headers AllOrNoneHeader

Sample Code—Java

Add the `AllOrNoneHeader` to the metadata connection before you perform a call as follows:

```
   metadataConnection.setAllOrNoneHeader(true);

```

This next example shows how to use the `AllOrNoneHeader` when creating two custom objects. Because the second custom object
doesn’t have the required `Name` field, the `create()` call can’t create this custom object and rolls back the first custom object. The
output is shown after this code sample.

```
   import com.sforce.soap.metadata.*;

   import com.sforce.soap.metadata.Error;

   import com.sforce.ws.ConnectionException;

   public class CallWithHeader {

      MetadataConnection metadataConnection = null;

      public static void main(String[] args) throws ConnectionException {

      CallWithHeader samples = new CallWithHeader();

        samples.createWithHeader();

      }

      public CallWithHeader() throws ConnectionException {

        metadataConnection = MetadataLoginUtil.login();

      }

      public void createWithHeader() throws ConnectionException {

        // Define two custom objects to be inserted.

        CustomObject co1 = new CustomObject();

        String name1 = "MyCustomObject1";

        co1.setFullName(name1 + "__c");

        co1.setDeploymentStatus(DeploymentStatus.Deployed);

        co1.setDescription("Created by the Metadata API");

        co1.setEnableActivities(true);

        co1.setLabel(name1 + " Object");

        co1.setPluralLabel(co1.getLabel() + "s");

        co1.setSharingModel(SharingModel.ReadWrite);

        CustomField nf = new CustomField();

        nf.setType(FieldType.Text);

        nf.setLabel(co1.getFullName() + " Name");

        co1.setNameField(nf);

        // The second custom object doesn't have a Name field

        CustomObject co2 = new CustomObject();

        String name2 = "MyCustomObject2";

        co2.setFullName(name2 + "__c");

```


### Headers CallOptions

```
        co2.setDeploymentStatus(DeploymentStatus.Deployed);

        co2.setDescription("Created by the Metadata API");

        co2.setEnableActivities(true);

        co2.setLabel(name2 + " Object");

        co2.setPluralLabel(co2.getLabel() + "s");

        co2.setSharingModel(SharingModel.ReadWrite);

        // Setting the allOrNone header to true to cause

        // the call to not commit any record if one or more

        // records in this call have failures.

        metadataConnection.setAllOrNoneHeader(true);

        // Now that the header has been set, make the create call.

        SaveResult[] results = metadataConnection

             .createMetadata(new Metadata[] { co1, co2 });

        // Iterate through the call results

        for (SaveResult r : results) {

           if (r.isSuccess()) {

             System.out.println("Created component: " + r.getFullName());

           } else {

             System.out

                  .println("Errors were encountered while creating "

                       + r.getFullName());

             for (Error e : r.getErrors()) {

               System.out.println("Error message: " + e.getMessage());

               System.out.println("Status code: " + e.getStatusCode());

             }

           }

        }

      }

   }

```

This is the output that the sample returns. The first record is rolled back and the second has a failure.

```
   Errors were encountered while creating MyCustomObject1__c

   Error message: Record rolled back because not all records were valid and the request was

   using AllOrNone header

   Status code: ALL_OR_NONE_OPERATION_ROLLED_BACK

   Errors were encountered while creating MyCustomObject2__c

   Error message: Must specify a nameField of type Text or AutoNumber

   Status code: FIELD_INTEGRITY_EXCEPTION

### CallOptions

```

Specifies the API client identifier.

Version

This call is available in all API versions.


### Headers DebuggingHeader

Supported Calls

All Metadata API calls.

Fields

Sample Code—Java

To change the API client ID, add the `CallOptions` header to the metadata connection before you perform a call as follows:

```
   metadataConnection.setCallOptions("client ID");

### **`DebuggingHeader`**

```

Specifies that the deployment result contains the debug log output, and specifies the level of detail included in the log. The debug log
contains the output of Apex tests that are executed as part of a deployment.

Version

This header is available in all API versions.

Supported Calls

```
   deploy()

```

Fields


Headers DebuggingHeader

LogInfo

Specifies the type and amount of information to be returned in the debug log. The `categories` field takes a list of these objects.
LogInfo is a mapping of `category` to `level` .

**Element Name** **Type** **Description**

`category` LogCategory Specify the type of information returned in the debug log. Valid values are:

**•** `Db`

**•** `Workflow`

**•** `Validation`

**•** `Callout`

**•** `Apex_code`

**•** `Apex_profiling`

**•** `Visualforce`

**•** `System`

**•** `All`

`level` LogCategoryLevel

Sample Code—Java

Specifies the level of detail returned in the debug log.

Valid log levels are (listed from lowest to highest):

**•** `NONE`

**•** `ERROR`

**•** `WARN`

**•** `INFO`

**•** `DEBUG`

**•** `FINE`

**•** `FINER`

**•** `FINEST`

Add the `DebuggingHeader` to the metadata connection before you perform the `deploy()` call as follows.

```
LogInfo[] logs = new LogInfo[1];

logs[0] = new LogInfo();

```


### Headers SessionHeader

```
   logs[0].setCategory(LogCategory.Apex_code);

   logs[0].setLevel(LogCategoryLevel.Fine);

   metadataConnection.setDebuggingHeader(logs);

```

The result of the `deploy()` call is obtained by calling `checkDeployStatus()` . After the deployment finishes, and if tests were
run, the response of `checkDeployStatus()` contains the debug log output in the `debugLog` field of a `DebuggingInfo`
output header.

### SessionHeader

Specifies the session ID that the login call returns. This session ID is used to authenticate all subsequent Metadata API calls.

Version

This header is available in all API versions.

Supported Calls

All Metadata API calls.

Fields

Sample Code—Java

### Add the SessionHeader to the metadata connection before you perform a call as follows:

```
   metadataConnection.setSessionHeader("<session_ID>");

```


APPENDICES

## APPENDIX A CustomObjectTranslation Language Support: Fully

Supported Languages

Not every language supports all the possible values for the fields in CustomObjectTranslation. Use this appendix to determine which
field values a language supports.

Note: Salesforce offers three levels of language support: fully supported languages, end-user languages, and platform-only
languages. This appendix provides information only for fully supported languages.

Chinese (Simplified)

```
plural

  false

```

Chinese (Traditional)

```
plural

  false

```

Danish

```
article

  None

  Definite

  Indefinite

gender

  Feminine

  Neuter

plural

  true

  false

```

Dutch

```
gender

  Feminine

```


CustomObjectTranslation Language Support: Fully Supported
Languages

```
    Neuter

   plural

    true

    false

```

Finnish

```
   caseType

    Ablative

    Adessive

    Allative

    Elative

    Essive

    Genitive

    Illative

    Inessive

    Nominative

    Partitive

    Translative

   plural

    true

    false

   possessive

    None

    First

    Second

```

French

```
   gender

    Masculine

    Feminine

   startsWith

    Consonant

    Vowel

   plural

    true

    false

```


CustomObjectTranslation Language Support: Fully Supported
Languages

German

```
   caseType

    Accusative

    Dative

    Genitive

    Nominative

   gender

    Masculine

    Feminine

    Neuter

   plural

    true

    false

```

Italian

```
   gender

    Masculine

    Feminine

   startsWith

    Consonant

    Special

    Vowel

   plural

    true

    false

```

Japanese

```
   plural

    false

```

Korean

```
   plural

    false

```


CustomObjectTranslation Language Support: Fully Supported
Languages

Norwegian

```
   article

    Definite

    Indefinite

    None

   gender

    Masculine

    Feminine

    Neuter

   plural

    true

    false

```

Portuguese (Brazil)

```
   gender

    Masculine

    Feminine

   plural

    true

    false

```

Russian

```
   caseType

    Accusative

    Dative

    Genitive

    Instrumental

    Nominative

    Prepositional

   gender

    Masculine

    Feminine

    Neuter

    AnimateMasculine

   plural

    true

```


CustomObjectTranslation Language Support: Fully Supported
Languages

```
    false

```

Spanish

```
   gender

    Masculine

    Feminine

   plural

    true

    false

```

Spanish (Mexico)

```
   gender

    Masculine

    Feminine

   plural

    true

    false

```

Swedish

```
   article

    None

    Definite

    Indefinite

   gender

    Feminine

    Neuter

   plural

    true

    false

```

Thai

```
   plural

    false

```


## APPENDIX B CustomObjectTranslation Language Support:

End-User Languages

Not every language supports all the possible values for the fields in CustomObjectTranslation. Use this appendix to determine which
field values a language supports.

Note: Salesforce offers three levels of language support: fully supported languages, end-user languages, and platform-only
languages. This appendix provides information only for end-user languages.

Arabic

```
article

  Definite

  None

gender

  Masculine

  Feminine

plural

  true

  false

possessive

  None

  First

  Second

```

Bulgarian

```
gender

  Masculine

  Feminine

  Neuter

plural

  true

  false

```


CustomObjectTranslation Language Support: End-User
Languages

Croatian

```
   caseType

    Accusative

    Dative

    Genitive

    Instrumental

    Locative

    Nominative

   gender

    Feminine

    Masculine

    Neuter

   plural

    true

    false

```

Czech

```
   caseType

    Accusative

    Dative

    Genitive

    Instrumental

    Locative

    Nominative

   gender

    Masculine

    Feminine

    Neuter

    AnimateMasculine

   plural

    true

    false

```

English (UK)

```
   plural

    false

```


CustomObjectTranslation Language Support: End-User
Languages

```
    true

   startsWith

    Consonant

    Vowel

```

Greek

```
   caseType

    Accusative

    Genitive

    Nominative

   gender

    Masculine

    Feminine

    Neuter

   plural

    true

    false

```

Hebrew

```
   article

    Definite

    None

   gender

    Masculine

    Feminine

   plural

    true

    false

```

Hungarian

```
   caseType

    Ablative

    Accusative

    Allative

    Causalfinal

    Dative

    Delative

```


CustomObjectTranslation Language Support: End-User
Languages

```
    Distributive

    Elative

    Essiveformal

    Illative

    Inessive

    Instrumental

    Nominative

    Sublative

    Termanative

    Translative

    Superessive

   plural

    true

    false

   possessive

    None

    First

    Second

   startsWith

    Consonant

    Vowel

```

Indonesian

```
   plural

    false

    true

```

Polish

```
   caseType

    Nominative

    Accusative

    Dative

    Genitive

    Instrumental

    Locative

   gender

    Masculine

```


CustomObjectTranslation Language Support: End-User
Languages

```
    Feminine

    Neuter

    AnimateMasculine

   plural

    true

    false

```

Portuguese (Portugal)

```
   gender

    Feminine

    Masculine

   plural

    true

    false

```

Romanian

```
   article

    Definite

    None

   gender

    Masculine

    Feminine

    Neuter

   plural

    true

    false

```

Slovak

```
   caseType

    Accusative

    Dative

    Genitive

    Instrumental

    Nominative

    Locative

   gender

    Feminine

```


CustomObjectTranslation Language Support: End-User
Languages

```
    Masculine

    Neuter

    AnimateMasculine

   plural

    true

    false

```

Slovenian

```
   caseType

    Accusative

    Dative

    Genitive

    Instrumental

    Nominative

    Locative

   gender

    Feminine

    Masculine

    Neuter

    AnimateMasculine

   plural

    true

    false

```

Turkish

```
   caseType

    Ablative

    Accusative

    Dative

    Genitive

    Nominative

    Locative

   possessive

    None

    First

    Second

```


CustomObjectTranslation Language Support: End-User
Languages

```
   plural

    true

    false

```

Ukrainian

```
   caseType

    Accusative

    Dative

    Genitive

    Instrumental

    Nominative

    Locative

   gender

    Masculine

    Feminine

    Neuter

    AnimateMasculine

   plural

    true

    false

```

Vietnamese

```
   plural

    true

    false

```


## APPENDIX C StandardValueSet Names and Standard Picklist

Fields

In API version 38.0 and later, standard picklists are represented by the StandardValueSet type. In previous versions, standard picklists are
represented by the CustomField type. This table lists the names of standard picklists as standard value sets and their corresponding field
names.

Note: The names of standard value sets and picklist fields are case-sensitive.


StandardValueSet Names and Standard Picklist Fields


StandardValueSet Names and Standard Picklist Fields


StandardValueSet Names and Standard Picklist Fields


StandardValueSet Names and Standard Picklist Fields


StandardValueSet Names and Standard Picklist Fields


StandardValueSet Names and Standard Picklist Fields


StandardValueSet Names and Standard Picklist Fields


StandardValueSet Names and Standard Picklist Fields


StandardValueSet Names and Standard Picklist Fields


StandardValueSet Names and Standard Picklist Fields


StandardValueSet Names and Standard Picklist Fields


StandardValueSet Names and Standard Picklist Fields


StandardValueSet Names and Standard Picklist Fields


StandardValueSet Names and Standard Picklist Fields


StandardValueSet Names and Standard Picklist Fields


StandardValueSet Names and Standard Picklist Fields


StandardValueSet Names and Standard Picklist Fields


StandardValueSet Names and Standard Picklist Fields


StandardValueSet Names and Standard Picklist Fields


StandardValueSet Names and Standard Picklist Fields


StandardValueSet Names and Standard Picklist Fields

1Part of Salesforce Health Cloud.

2You can only update the label in this standard value set or picklist field. You can’t insert or delete picklist values.

3You can’t read or update this standard value set or picklist field.

4Part of Salesforce Net Zero Cloud.


StandardValueSet Names and Standard Picklist Fields

5Part of Public Sector Solutions.

6Part of Digital Lending Solutions.

[For values used in Loyalty Management, see StandardValueSet Names and Standard Picklist Fields for Loyalty Management.](https://developer.salesforce.com/docs/atlas.en-us.260.0.loyalty.meta/loyalty/loyalty_standardvalueset_names.htm)


INDEX

C

ChatterEmailsMDSettings component 1995
Components
ChatterEmailsMDSettings 1995

P

Prompt component 1750

U

UserEngagementSettings component 2274

