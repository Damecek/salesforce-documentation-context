`contactName` string Contact name for this model card.


Metadata Types DiscoveryGoal

**Field Name** **Field Type** **Description**

`label` string Title for this model card.

`sections` string Sections in the model card.

DiscoveryGoalOutcome

Represents the outcome variable of the model.

**Field Name** **Field Type** **Description**

`field` string Name of the outcome variable.

`fieldLabel` string Label for the outcome variable.

`goal` DiscoveryOutcomeGoal Goal for the outcome variable.

`mappedField` string Mapped field.

DiscoveryOutcomeGoal

Represents the goal for an outcome.

**Field Name** **Field Type** **Description**

`Minimize` string Maximize the outcome.

`Maximize` string Minimize the outcome.

`None` string Reserved for future use.

DiscoveryPredictionType

Represents the prediction type for a model.

**Field Name** **Field Type** **Description**

`Unknown` string Unknown prediction type.

`Regression` string Regression prediction (numeric use case).

`Classification` string Binary classification prediction.

`MulticlassClassification` string Multiclass classification prediction.

DiscoveryPushbackType

Represents the type of writeback field. Must be set to `AiRecordInsight` .


Metadata Types DiscoveryGoal

**Field Name** **Field Type** **Description**

`AiRecordInsight` string Automatic writeback type. Required.

`Direct` string Currently not supported. Reserved for future use.

Declarative Metadata Sample Definitions

Here is a sample DiscoveryGoal:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <DiscoveryGoal xmlns="http://soap.sforce.com/2006/04/metadata"

   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

     <active>true</active>

     <deployedModels>

       <active>true</active>

       <aiModel>Maximize_Tenure</aiModel>

       <fieldMappings>

         <mappedField>Opportunity.Amount</mappedField>

         <modelField>PTO</modelField>

         <sourceType>SalesforceField</sourceType>

       </fieldMappings>

       <fieldMappings>

         <mappedField>Opportunity.ExpectedRevenue</mappedField>

         <modelField>Salary</modelField>

         <sourceType>SalesforceField</sourceType>

       </fieldMappings>

       <fieldMappings>

         <mappedField>Level</mappedField>

         <modelField>Level</modelField>

         <sobjectFieldJoinKey>Opportunity.Name</sobjectFieldJoinKey>

         <source>employees</source>

         <sourceFieldJoinKey>Name</sourceFieldJoinKey>

         <sourceType>AnalyticsDatasetField</sourceType>

       </fieldMappings>

       <fieldMappings>

         <mappedField>Opportunity.StageName</mappedField>

         <modelField>Field</modelField>

         <sourceType>SalesforceField</sourceType>

       </fieldMappings>

       <filters>

         <field>Opportunity.StageName</field>

         <operator>Equal</operator>

         <values>

           <type>Constant</type>

           <value>Qualification</value>

         </values>

       </filters>

       <label>employees</label>

       <name>employees</name>

       <prescribableFields>

         <customDefinitions>

```


Metadata Types DiscoveryGoal

```
          <filters>

            <field>Salary</field>

            <operator>LessThan</operator>

            <type>Number</type>

            <values>

              <type>PlaceHolder</type>

              <value>[value_low]</value>

            </values>

          </filters>

          <template>Increase [field_name] by [diff]</template>

         </customDefinitions>

         <customDefinitions>

           <filters>

            <field>Salary</field>

            <operator>GreaterThan</operator>

            <type>Number</type>

            <values>

               <type>PlaceHolder</type>

               <value>[value_low]</value>

             </values>

           </filters>

           <template xsi:nil="true"/>

         </customDefinitions>

         <name>Salary</name>

       </prescribableFields>

       <prescribableFields>

         <customDefinitions>

           <filters>

             <field>Level</field>

             <operator>LessThan</operator>

             <type>Number</type>

             <values>

               <type>PlaceHolder</type>

               <value>[value_low]</value>

             </values>

           </filters>

           <template xsi:nil="true"/>

         </customDefinitions>

         <customDefinitions>

           <filters>

             <field>Level</field>

             <operator>GreaterThan</operator>

             <type>Number</type>

             <values>

               <type>PlaceHolder</type>

               <value>[value_low]</value>

              </values>

            </filters>

            <template xsi:nil="true"/>

         </customDefinitions>

         <name>Level</name>

       </prescribableFields>

       <prescribableFields>

         <name>Field</name>

```


### Metadata Types DiscoveryStory

```
       </prescribableFields>

     </deployedModels>

     <label>employees_Tenure</label>

     <outcome>

       <field>Tenure</field>

       <fieldLabel>Tenure</fieldLabel>

       <goal>Maximize</goal>

       <mappedField>Opportunity.Amount</mappedField>

     </outcome>

     <predictionType>Regression</predictionType>

     <pushbackField>My_Pushback_Field__c</pushbackField>

     <subscribedEntity>Opportunity</subscribedEntity>

     <terminalStateFilters>

       <field>Opportunity.Amount</field>

       <operator>GreaterThan</operator>

       <values>

         <type>Constant</type>

         <value>5</value>

       </values>

     </terminalStateFilters>

     <terminalStateFilters>

       <field>Opportunity.Amount</field>

       <operator>LessThan</operator>

       <values>

         <type>Constant</type>

         <value>10</value>

       </values>

     </terminalStateFilters>

   </DiscoveryGoal>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### DiscoveryStory

Represents the metadata associated with a story used in Einstein Discovery.

A story defines the data and analytical settings that Einstein Discovery uses to generate insights and build predictive models. Story
settings include the outcome variable, whether to maximize or minimize the outcome variable, the data to analyze in a CRM Analytics
dataset, and other preferences. Story settings tell Einstein Discovery how to conduct the analysis and communicate its results. In Package
Manager, this type is listed as "Discovery Story".

Note: Write operations for DiscoveryStory objects are generally not supported.

Declarative Metadata File Suffix and Directory Location

A DiscoveryStory is stored in the `discovery` folder. DiscoveryStory have two files:

**•** file with `.story` suffix contains the story’s actual data


Metadata Types DiscoveryStory

**•** file named _`ModelName`_ `.story-meta.xml` suffix contains the story’s metadata

Here is a sample `package.xml` file:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Subscriber_Changes</members>

        <name>DiscoveryStory</name>

      </types>

      <version>55.0</version>

   </Package>

```

Version

DiscoveryStorys are available in API version 54.0 and later.

Fields

**Field Name** **Field Type** **Description**

`application` string Required. The CRM Analytics app the story is associated with.

`autopilot` DiscoveryStoryAutopilotStatus Optional. The autopilot status for the story. One of the following
strings:

**•** `Enabled`

**•** `Disabled`

`classificationThreshold` double Optional. The threshold for classification predictions for the story.

`label` string Required. The story label. If you package a story, this label appears
in Package Manager.

`outcome` DiscoveryStoryOutcome Required. The selected outcome of the story.

`sourceContainer` string Required. The source ID for the story.

`sourceType` DiscoveryStorySourceType Required. The source type of the story. One of the following strings:

**•** `AnalyticsDataset`

**•** `LiveDataset`

**•** `Report`

`validationContainder` string Optional. The validation ID for the story.

DiscoveryStoryOutcome

Represents the selected outcome of the generated story.


Metadata Types DiscoveryStory

**Field Name** **Field Type** **Description**

`failureValue` string Optional. The value if the story failed.

`field` string Required. The field configuration for the story.

`goal` DiscoveryStoryOutcomeGoal Required. The story outcome goal. One of the following strings:

**•** `Maximize`

**•** `Minimize`

**•** `None`

`label` string Required. The story outcome label.

`successValue` string Optional. The value if the story succeeded.

`type` DiscoveryStoryOutcomeType Required. The story outcome type. One of the following strings:

**•** `Categorical`

**•** `Count`

**•** `Number`

**•** `Text`

Declarative Metadata Sample Definitions

Here is a sample DiscoveryStory:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <DiscoverStory xmlns="http://soap.sforce.com/2006/04/metadata"

   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

      <application>MyStoryApp</application>

      <autopilot>Enabled</autopilot>

      <classificationThreshold>0.7383</classificationThreshold>

      <label>SubscriberChanges</label>

      <outcome>

        <field>Subscriber</field>

        <goal>Minimize</goal>

        <label>SubscriberChangeOutcome</label>

        <successValue>Success</successValue>

        <type>Numerical</type>

      </outcome>

      <sourceContainer>01X00000000xxxx1AB</sourceContainer>

      <sourceType>AnalyticsDataset</sourceType>

   </DiscoveryStory>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types Document Document

Represents a Document. All documents must be in a document folder, such as `sampleFolder/TestDocument` .

This type extends the MetadataWithContent metadata type and inherits its `content` and `fullName` fields.

Retrieving Documents

You can’t use the wildcard (*) symbol with documents in `package.xml` . To retrieve the list of documents for populating
### package.xml with explicit names, call listMetadata() and pass in DocumentFolder as the type. Note that DocumentFolder

is not returned as a type in `describeMetadata()` . Document is returned from `describeMetadata()` with an associated
attribute of `inFolder` set to true. If that attribute is set to true, you can construct the type by using the component name with the
word Folder, such as DocumentFolder.

The following example shows folders in `package.xml` :

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>MyDBFolder/MyDBName</members>

        <name>Dashboard</name>

      </types>

      <types>

        <members>MyDocumentFolder/MyDocumentName</members>

        <name>Document</name>

      </types>

      <types>

        <members>unfiled$public/MarketingProductInquiryResponse</members>

        <members>unfiled$public/SalesNewCustomerEmail</members>

        <name>EmailTemplate</name>

      </types>

      <types>

        <members>MyReportFolder/MyReportName</members>

        <name>Report</name>

      </types>

      <version>66.0</version>

   </Package>

### For each document an accompanying metadata file named DocumentFilename -meta.xml is created in the document folder.
```

For example, for a document `TestDocument.png` in the sampleFolder folder, there’s a `TestDocument.png-meta.xml` in
the `documents/sampleFolder` of the package.

Version

### Documents are available in API version 10.0 and later.

In API version 17.0 and later, you can delete a folder containing documents moved to the Recycle Bin. When you delete the folder, any
related documents in the Recycle Bin are permanently deleted.

In API version 18.0 and later, documents do not need an extension.


Metadata Types Document

Fields

This metadata type contains the following fields:

**Field Name** **Field Type** **Description**

`content` base64 Content of the document. Base 64-encoded binary data. Prior to making
an API call, client applications must encode the binary attachment data

as base64. Upon receiving a response, client applications must decode
the base64 data to binary. This conversion is usually handled for you by
a SOAP client. This field is inherited from the MetadataWithContent
component.

`description` string A description of the document. Enter a description to distinguish this
document from others.

`fullName` string The name of the document, including the folder name. In version 17.0
and earlier, the `fullName` included the document extension. In version

18.0 and later, the `fullName` does not include the file extension. The
`fullName` can contain only underscores and alphanumeric characters.
It must be unique, begin with a letter, not include spaces, not end with
an underscore, and not contain two consecutive underscores. If this field
contained characters before version 14.0 that are no longer allowed, the
characters were stripped out of this field, and the previous value of the
field was saved in the `name` field. This field is inherited from the
Metadata component.

`internalUseOnly` boolean

Required. Indicates whether the document is confidential ( `true` ) or not
( `false` ). This field and `public` are mutually exclusive; you cannot
set both to `true` .

`keywords` string Contains one or more words that describe the document. A check for
matches to words in this field is performed when doing a search.

`name` string The list of characters allowed in the `fullName` field has been reduced
for versions 14.0 and later. This field contains the value contained in the

`fullName` field before version 14.0. This field is only populated if the
value of the `fullName` field contained characters that are no longer
accepted in that field.

`public` boolean Required. Indicates whether the document is an image available for
HTML email templates and does not require a Salesforce username and

password to view in an email ( `true` ) or not ( `false` ). If the images will
be used as a custom app logo or custom tab icon, both of which require
a Salesforce username and password to view, set this field to `false` .
This field and `internalUseOnly` are mutually exclusive; you cannot
set both to `true` .


### Metadata Types DocumentCategory

Declarative Metadata Sample Definition

The following is the definition of a document:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Document xmlns="http://soap.sforce.com/2006/04/metadata">

      <internalUseOnly>false</internalUseOnly>

      <name>Q2 Campaign Analysis</name>

      <public>false</public>

      <description>Analyze Q2 campaign effectiveness</description>

   </Document>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

Folder

### DocumentCategory

Represents a document category.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### DocumentCategory components have the suffix .documentCategory and are stored in the documentCategory folder.

Version

### DocumentCategory components are available in API version 59.0 and later.

Special Access Rules

Fields

**Field Name** **Description**

```
description

```

**Field Type**
string


### Metadata Types DocumentCategoryDocumentType

**Field Name** **Description**

**Description**
A description of the DocumentCategory.

```
isProtected

masterLabel

```

**Field Type**
boolean

**Description**
An auto-generated value that doesn’t impact the behavior of the metadata type. The
default value is `false` .

**Field Type**
string

**Description**

Required.

The master label of the DocumentCategory. This internal label doesn’t get translated.

Declarative Metadata Sample Definition

The following is an example of a DocumentCategory component.

```
<?xml version="1.0" encoding="UTF-8"?>

<DocumentCategory xmlns="http://soap.sforce.com/2006/04/metadata">

   <masterLabel>Address_Proof</masterLabel>

</DocumentCategory>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>*</members>

     <name>DocumentCategory</name>

   </types>

   <version>59.0</version>

</Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### DocumentCategoryDocumentType

Represents the junction between a DocumentCategory and a DocumentType. Puts a DocumentType in a DocumentCategory.


Metadata Types DocumentCategoryDocumentType

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

DocumentCategoryDocumentType components have the suffix `.documentCategoryDocumentType` and are stored in the
`documentCategoryDocumentTypes` folder.

Version

DocumentCategoryDocumentType components are available in API version 59.0 and later.

Special Access Rules

Fields

**Field Name** **Description**

```
documentCategory

documentType

isProtected

masterLabel

```

**Field Type**
string

**Description**

Required.

The master label of the related DocumentCategory.

**Field Type**
string

**Description**

Required.

The master label of the related DocumentType.

**Field Type**
boolean

**Description**
An auto-generated value that doesn’t impact the behavior of the metadata type. The
default value is `false` .

**Field Type**
string

**Description**

Required.


### Metadata Types DocumentChecklistSettings

**Field Name** **Description**

The master label of the DocumentCategoryDocumentType. This internal label doesn’t
get translated.

Declarative Metadata Sample Definition

The following is an example of a DocumentCategoryDocumentType component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <DocumentCategoryDocumentType xmlns="http://soap.sforce.com/2006/04/metadata">

      <documentCategory>Address_Proof</documentCategory>

      <documentType>Utility_Bill</documentType>

      <masterLabel>junction1</masterLabel>

   </DocumentCategoryDocumentType>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8" standalone="yes"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>DocumentCategory</name>

      </types>

      <types>

        <members>*</members>

        <name>DocumentCategoryDocumentType</name>

      </types>

      <types>

        <members>*</members>

        <name>DocumentType</name>

      </types>

      <version>59.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### DocumentChecklistSettings

Represents an org’s DocumentChecklistItem settings.

This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for more details.


Metadata Types DocumentChecklistSettings

File Suffix and Directory Location

DocumentChecklistSettings components are stored in the `DocumentChecklist.settings` file in the `settings` folder. The
`.settings` files are different from other named components because there’s only one settings file for each settings component.

Version

DocumentChecklistSettings components are available in API versions 55.0 and later.

Fields

**Field Name** **Field Type** **Description**

`dciCustomSharing` boolean

Indicates whether the custom sharing rule for document checklist items
is enabled for your org ( `true` ) or not ( `false` ). The default value is
`false` .

`deleteDCIWithFiles` boolean Indicates whether deletion of document checklist items is enabled for
your org ( `true` ) or not ( `false` ). The default value is `false` .

Declarative Metadata Sample Definition

The following is an example of a DocumentChecklistSettings.settings component.

```
<?xml version="1.0" encoding="UTF-8"?>

<DocumentChecklistSettings

 xmlns="http://soap.sforce.com/2006/04/metadata">

 <dciCustomSharing>true</dciCustomSharing>

 <deleteDCIWithFiles>true</deleteDCIWithFiles>

</DocumentChecklistSettings>

```

Example Package Manifest

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package

 xmlns="http://soap.sforce.com/2006/04/metadata">

 <types>

  <members>DocumentChecklist</members>

  <name>Settings</name>

 </types>

 <version>55.0</version>

</Package>

```


### Metadata Types DocumentType

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### DocumentType

Represents a document type.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### DocumentType components have the suffix .documentType and are stored in the documentTypes folder.

Version

### DocumentType components are available in API version 59.0 and later.

Special Access Rules

Fields

**Field Name** **Description**

```
description

isActive

masterLabel

```

**Field Type**
string

**Description**
A description of the DocumentType.

**Field Type**
boolean

**Description**

Required.

Specifies whether the DocumentType is active.

**Field Type**
string

**Description**

Required.


### Metadata Types DuplicateRule

**Field Name** **Description**

The master label of the DocumentType. This internal label doesn’t get translated.

Declarative Metadata Sample Definition

The following is an example of a DocumentType component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <DocumentType xmlns="http://soap.sforce.com/2006/04/metadata">

      <description>Utility_Bill</description>

      <isActive>true</isActive>

      <masterLabel>Utility_Bill</masterLabel>

   </DocumentType>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8" standalone="yes"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>DocumentType</name>

      </types>

      <version>59.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### DuplicateRule

Represents a rule that specifies how duplicate records in an object are detected. This type extends the Metadata metadata type and
inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### DuplicateRule components have the .duplicateRule  suffix and are stored in the duplicateRules/  directory. The name

of the component file is based on the name of the object associated with the rule. For example, the component file name
`duplicateRules/Account.Standard_Account_Duplicate_Rule.duplicateRule` describes a duplicate rule
component associated with the Account object.

Version

### DuplicateRule components are available in API version 66.0 and later.


Metadata Types DuplicateRule

Fields

**Field Name** **Field Type** **Description**

Required. Determines what the duplicate rule does when users or the
DuplicateRule API try to insert a record that is a duplicate. Valid values
are:

```
Allow
```

For users, if `operationsOnInsert` is set to `alert`, the UI
displays the value of `alertText` in a dialog. The dialog prompts

users to continue or cancel. If the user chooses to continue, the
insertion proceeds. If the user chooses to cancel, the record isn’t
inserted.

The DuplicateRule API returns an error code and a message. To
complete the insertion, the code must set the `allowSave` field
in DuplicateRuleHeader to `true` and reissue the request.

If `operationsOnInsert` isn’t set to `alert`, the UI inserts the
record without issuing an alert. The API inserts the record and doesn’t
return an error code.

```
Block
```

For users, the UI displays an error message and prevents them from
inserting the new record. The DuplicateRule API returns an error and
doesn’t insert the record.

Required. Determines what the duplicate rule does when users or the
DuplicateRule API try to update a record, and the result is a duplicate.
Valid values are:

```
Allow
```

For users, if `operationsOnUpdate` is set to `alert`, the UI
displays the value of `alertText` in a dialog. The dialog prompts

users to continue or cancel. If the user chooses to continue, the
update proceeds. If the user chooses to cancel, the record isn’t
updated.

The DuplicateRule API returns a message. To complete the update,
the code must set the `allowSave` field in DuplicateRuleHeader
to `true` and reissue the request.

If `operationsOnUpdate` isn’t set to `alert`, the UI updates
the record without issuing an alert. The API updates the record and
doesn’t return an error code.

```
Block
```

For users, the UI displays an error message and prevents them from
continuing. The DuplicateRule API returns an error.


```
actionOnInsert

actionOnUpdate

```

DupeActionType
(enumeration of
type string)

DupeActionType
(enumeration of
type string)

Metadata Types DuplicateRule

**Field Name** **Field Type** **Description**

`alertText` string

Text that’s sent when the duplicate rule is triggered. The text is only sent
if `isActive` is `true` . In the UI, the text displays as a message. The
DuplicateRule API returns the message in its response.

You can set a value for `alertText` only when you have
`actionOnInsert` or `actionOnUpdate` (or both) set to `Allow` .

Otherwise, you receive a validation error when you add or update this
component.

`description` string Required. Text that describes the duplicate rule. The value is
customer-supplied, but isn’t visible in the UI.

`duplicateRuleFilter` DuplicateRuleFilter

Required. Criteria that define how to find records to consider when
looking for duplicates. For example, use `duplicateRuleFilter`
to exclude records from the match when looking for duplicates.

`duplicateRuleMatchRules` DuplicateRuleMatchRule[] Required. One or more MatchingRule components for the DuplicateRule.
A `MatchingRule` controls what constitutes a match between records.

`isActive` boolean Required. If `true`, the DuplicateRule detects duplicate records.
Otherwise, the rule has no effect.

`masterLabel` string Required. Label for this DuplicateRule. This value is the internal label for
the rule.

`operationsOnInsert` string[]

`operationsOnUpdate` string[]

Required. Controls the action to take when `actionOnInsert` is set
to `Allow` and the duplicate rule is triggered. Either one or both of
these values can be set in the array:

```
alert
```

If set, the action specified in `actionOnInsert` occurs; otherwise,
the insert proceeds.

```
report
```

If set, the insert operation is added to the report of duplicates.

Required. Controls the action to take when `actionOnUpdate` is set
to `Allow` and the duplicate rule is triggered. Either one or both of
these values can be set in the array:

```
alert
```

If set, the action specified in `actionOnUpdate` occurs; otherwise,
the update proceeds.

```
report
```

If set, the update operation is added to the report of duplicates.

Required. Determines how record sharing rules affect duplicate
management. Valid values are:

```
EnforceSharingRules
```

Sharing rules affect duplicate management. If a duplicate rule is
triggered because an insert or update duplicates an existing record,


```
securityOption

```

DupeSecurityOptionType
(enumeration of
type string)

Metadata Types DuplicateRule

**Field Name** **Field Type** **Description**

but the running user doesn’t have sharing access to that record, the
insert or update proceeds. The sharing rule doesn’t prevent the user
from creating or updating the record because the record is hidden
from the user. No message is issued.

```
                           BypassSharingRules
```

Sharing rules don’t affect duplicate management. If a duplicate rule
is triggered because an insert or update duplicates an existing record,
sharing rules are ignored, but other access restrictions apply.

`sortOrder` int Required. Determines the order in which duplicate rules are applied.

DuplicateRuleMatchRule

Describes the MatchingRule associated with the `DuplicateRule` . The `MatchingRule` identifies duplicate records.

**Field Name** **Field Type** **Description**

`matchRuleSObjectType` string Required. The name of the target object of the matching rule. For
example, if you define a duplicate rule for Contact records, and you want

to match with Lead records, the value of `matchRuleSObjectType`
is Lead.

`matchingRule` string Required. Value that corresponds to the value of `developerName`
in the MatchingRule for this duplicate rule.

`objectMapping` ObjectMapping

DuplicateRuleFilter

Required. Foreign key to an ObjectMapping that maps fields from the
duplicate rule’s object to fields in the target object specified by
`matchRuleSObjectType` .

Specifies filter criteria for a DuplicateRule. Salesforce only applies the DuplicateRule if the record matches the criteria.

**Field Name** **Field Type** **Description**

`booleanFilter` string Required. A string of boolean operators that establishes the filter logic
for the filter items specified in `duplicateRuleFilterItems` .

`duplicateRuleFilterItems` DuplicateRuleFilterItem[] Required. A list of DuplicateRuleFilterItem components.

DuplicateRuleFilterItem

This type extends the FilterItem type and inherits all its fields.

**Field Name** **Field Type** **Description**

`sortOrder` int Required. The order of this item in the duplicate rule filter.


Metadata Types DuplicateRule

**Field Name** **Field Type** **Description**

`table` string

ObjectMapping

Required. The object that has the field specified in the `field` field of
DuplicateRuleFilterItem. See the documentation for FilterItem for the
definition of `field` .

Represents a map of fields in the input object of the DuplicateRule to fields in the output object of DuplicateRule. The input object is
the object associated with the DuplicateRule. The output object can be the same object or a different object with similar fields.

For example, you can have a DuplicateRule that looks for duplicates between the Contact object and the Lead object. In this case, the
input object is Contact, and the output object is Lead.

**Field Name** **Field Type** **Description**

`inputObject` string Required. The input object for the duplicate rule. The DuplicateRule is
associated with this object. For example, if you define a duplicate rule

for Contact records, and you want to match with Lead records, the value
of `inputObject` is Contact.

`mappingFields` ObjectMappingField[] Required. The mapping of source object fields to target object fields for
the duplicate rule.

`outputObject` string Required. The output object for the duplicate rule. This value is the same
as the value of the `matchRuleSObjectType` field in

DuplicateRuleMatchRule. Any duplicate rules that this object has are
ignored when the DuplicateRule API uses the ObjectMapping.

ObjectMappingField

A field name in the input object of the DuplicateRule, and the corresponding field name in the output object.

**Field Name** **Field Type** **Description**

`inputField` string Required. Field in the object specified by the `inputObject` field in
ObjectMapping. This field is mapped to the field in `outputField`,

which is assumed to be a field in the object specified by the
`outputObject` field in ObjectMapping.

`outputField` string Required. Field in the object specified by the `outputObject` field
in ObjectMapping. The field is mapped to the field name in

`inputField`, which is assumed to be a field in the object specified
by the `inputObject` in ObjectMapping.


Metadata Types DuplicateRule

Declarative Metadata Sample Definition

The following is an example of a DuplicateRule component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <DuplicateRule xmlns="http://soap.sforce.com/2006/04/metadata"

   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

      <actionOnInsert>Allow</actionOnInsert>

      <actionOnUpdate>Allow</actionOnUpdate>

      <alertText>You are creating a duplicate record. Use an existing record

   instead.</alertText>

      <description>Detects a contact that duplicates a Lead</description>

      <duplicateRuleFilter>

        <booleanFilter xsi:nil="true"/>

        <duplicateRuleFilterItems>

           <field>Username</field>

           <operation>equals</operation>

           <value>user@example.com</value>

           <sortOrder>1</sortOrder>

           <table>User</table>

        </duplicateRuleFilterItems>

      </duplicateRuleFilter>

      <duplicateRuleMatchRules>

        <matchRuleSObjectType>Lead</matchRuleSObjectType>

        <matchingRule>ContactToLeadDuplicate_matching_rule</matchingRule>

        <objectMapping>

           <inputObject>Contact</inputObject>

           <mappingFields>

             <inputField>FirstName</inputField>

             <outputField>FirstName</outputField>

           </mappingFields>

           <mappingFields>

             <inputField>LastName</inputField>

             <outputField>LastName</outputField>

           </mappingFields>

           <outputObject>Lead</outputObject>

        </objectMapping>

      </duplicateRuleMatchRules>

      <isActive>true</isActive>

      <masterLabel>ContactToLeadDuplicate</masterLabel>

      <operationsOnInsert>Alert</operationsOnInsert>

      <operationsOnInsert>Report</operationsOnInsert>

      <operationsOnUpdate>Alert</operationsOnUpdate>

      <operationsOnUpdate>Report</operationsOnUpdate>

      <securityOption>EnforceSharingRules</securityOption>

      <sortOrder>1</sortOrder>

   </DuplicateRule>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>ContactToLeadDuplicate</members>

        <name>DuplicateRule</name>

```


### Metadata Types EclairGeoData

```
      </types>

      <version>38.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### EclairGeoData

Represents an Analytics custom map chart. Custom maps are user-defined maps that are uploaded to Analytics and are used just as
standard maps are. Custom maps are accessed in Analytics from the list of maps available with the map chart type.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### EclairGeoData components have the suffix geodata and are stored in the eclair folder.

Version

### EclairGeoData components are available in API version 39.0 and later.

Fields

**Field Name** **Field Type** **Description**

`maps` EclairMap[] A list of EclairMap objects. Each EclairMap object specifies the bounding
box (if any) and the map name that appears in the user interface.

`masterLabel` string Required. Label for this object. This display value is the internal label that
is not translated.

EclairMap

**Field Name** **Field Type** **Description**

`boundingBoxBottom` double When bounding-box coordinates are used, this contains the bottom coordinate.

`boundingBoxLeft` double When bounding-box coordinates are used, this contains the left side coordinate.

`boundingBoxRight` double When bounding-box coordinates are used, this contains the right side
coordinate.

`boundingBoxTop` double When bounding-box coordinates are used, this contains the top coordinate.


Metadata Types EclairGeoData

**Field Name** **Field Type** **Description**

`mapLabel` string Required. The user-interface name of the map. This name appears in the maps
list for the map chart in Analytics.

`mapName` string Required. Label for this object. This display value is the internal label that is not
translated.

`projection` string Required. The type of map projection used to create the map. Valid values are:

**•** Equirectangular

**•** Mercator

**•** AlbersUSA

Declarative Metadata Sample Definition

The following is an example of an EclairGeoData component:

```
         <EclairGeoData xmlns="http://soap.sforce.com/2006/04/metadata"

   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

           <content xsi:nil="true"/>

           <maps>

            <boundingBoxBottom>0.0</boundingBoxBottom>

            <boundingBoxLeft>100.0</boundingBoxLeft>

            <boundingBoxRight>100.0</boundingBoxRight>

            <boundingBoxTop>0.0</boundingBoxTop>

            <mapLabel>WorldMap0 Label</mapLabel>

            <mapName>WorldMap0</mapName>

            <projection>Equirectangular</projection>

           </maps>

           <maps>

            <boundingBoxBottom>1.0</boundingBoxBottom>

            <boundingBoxLeft>101.0</boundingBoxLeft>

            <boundingBoxRight>101.0</boundingBoxRight>

            <boundingBoxTop>1.0</boundingBoxTop>

            <mapLabel>WorldMap1 Label</mapLabel>

            <mapName>WorldMap1</mapName>

            <projection>Mercator</projection>

           </maps>

           <masterLabel>WorldMapGeoDataToCreate Label</masterLabel>

         </EclairGeoData>

```

The following is an example `package.xml` that references the previous definition.

```
        <?xml version="1.0" encoding="UTF-8"?>

        <Package xmlns="http://soap.sforce.com/2006/04/metadata">

         <types>

           <members>*</members>

           <name>EclairGeoData</name>

         </types>

```


### Metadata Types EmailServicesFunction

```
         <version>39.0</version>

        </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### EmailServicesFunction

Represents an email service. This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### EmailServicesFunction components have the suffix .xml and are stored in the emailservices folder.

Version

### EmailServicesFunction components are available in API version 42.0 and later.

Fields

**Field Name** **Field Type** **Description**

`apexClass` string Required. The name of the Apex class that the email service uses to
process inbound messages.

```
attachmentOption

```

EmailServicesAttOptions Required. Indicates the types of attachments the email service accepts.
(enumeration of One of the following values:
type string)

**•** `None` —The email service accepts the message but discards any
attachment.

**•** `NoContent` —The attachment metadata (filename, MIME type,
and so on) is provided to the Apex class, but the body is set to `null` .

**•** `TextOnly` —The email service only accepts the following types
of attachments:

**–** Attachments with a Multipurpose Internet Mail Extension (MIME)
type of text.

**–** Attachments with a MIME type of application/octet-stream and
a file name that ends with either a .vcf or .vcs extension. These
are saved as text/x-vcard and text/calendar MIME types,
respectively.

**•** `BinaryOnly` —The email service only accepts binary attachments,
such as image, audio, application, and video files.

**•** `All` —The email service accepts any type of attachment.


Metadata Types EmailServicesFunction

**Field Name** **Field Type** **Description**

Required. Indicates what the email service does with messages that fail
or do not support any of the authentication protocols if the
isAuthenticationRequired field is true.

Required. Indicates what the email service does with messages received
from senders who are not listed in the authorizedSenders field on either
the email service or email service address.

```
authenticationFailureAction

authorizationFailureAction

```

EmailServicesErrorAction
(enumeration of
type string)

EmailServicesErrorAction
(enumeration of
type string)

`authorizedSenders` string Configures the email service to only accept messages from the email
addresses or domains listed in this field. If the email service receives a

message from an unlisted email address or domain, the email service
performs the action specified in the authorizationFailureAction field.
Leave this field blank if you want the email service to receive email from
any email address.

`emailServicesAddresses` EmailServicesAddress A list of EmailServiceAddress records.

`errorRoutingAddress` email The destination email address for error notification email messages when
isErrorRoutingEnabled `is true` .

Required. Indicates what the email service does with messages it receives
when the email service itself is inactive.

One of the following values:

**•** `UseSystemDefault` —The system default is used.

**•** `Bounce` —The email service returns the message to the sender
with a notification that explains why the message was rejected.

**•** `Discard` —The email service deletes the message without
notifying the sender.

**•** `Requeue` —The email service queues the message for processing
in the next 24 hours. If the message is not processed within 24 hours,
the email service returns the message to the sender with a
notification that explains why the message was rejected.

```
functionInactiveAction

```

EmailServicesErrorAction
(enumeration of
type string)

`functionName` string Required. The name of the email service in the API. This name can contain
only underscores and alphanumeric characters and must be unique in

your org. The value in this 64-character field must begin with a letter,
not include spaces, not end with an underscore, and not contain two
consecutive underscores.

In managed packages, this field prevents naming conflicts on package
installations. This field is automatically generated, but you can supply
your own value if you create the record using the API. With this field, a
developer can change the object’s name in a managed package and
the changes are reflected in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique
`functionName` for each record. If no `functionName` is
specified, performance may slow while Salesforce generates one
for each record.


Metadata Types EmailServicesFunction

**Field Name** **Field Type** **Description**

`isActive` boolean Indicates whether this object is active ( `true` ) or not ( `false` ).

`isAuthenticationRequired` boolean Configures the email service to verify the legitimacy of the sending server
before processing a message. The email service uses the SPF, SenderId,

and DomainKeys protocols to verify the sender's legitimacy: If the sending
server passes at least one of these protocols and does not fail any, the
email service accepts the email. If the server fails a protocol or does not
support any of the protocols, the email service performs the action
specified in the authenticationFailureAction field.

`isErrorRoutingEnabled` boolean

When incoming email messages can’t be processed, indicates whether
error notification email messages are routed to a chosen address or to
the senders.

`isTextAttachmentsAsBinary` boolean If `true`, text attachments are supplied to the Apex code as a
`Messaging.BinaryAttachment` instead of as a

`Messaging.TextAttachment` . This means that the body is
supplied as an Apex Blob instead of as an Apex String.

`isTlsRequired` boolean Not currently in use.

Required. Indicates what the email service does with messages if the
total number of messages processed by all email services combined has
reached the daily limit for your organization.

One of the following values:

**•** `UseSystemDefault` —The system default is used.

**•** `Bounce` —The email service returns the message to the sender
with a notification that explains why the message was rejected.

**•** `Discard` —The email service deletes the message without
notifying the sender.

**•** `Requeue` —The email service queues the message for processing
in the next 24 hours. If the message is not processed within 24 hours,
the email service returns the message to the sender with a
notification that explains why the message was rejected.

The system calculates the limit by multiplying the number of user licenses
by 1,000.

```
overLimitAction

```

EmailServicesAddress

EmailServicesErrorAction
(enumeration of
type string)

Each email service has one or more email addresses to which users can send messages for processing. An email service only processes
messages it receives at one of its addresses.

**Field Name** **Field Type** **Description**

`authorizedSenders` string Configures the email service address to only accept messages from the email
addresses or domains listed in this field. If the email service address receives a

message from an unlisted email address or domain, the email service performs


### Metadata Types EmailTemplate

**Field Name** **Field Type** **Description**

the action specified in the authorizationFailureAction field of its associated
email service. Leave this field blank if you want the email service address to
receive email from any email address.

`developerName` string Required. The name of the object in the API. This name can contain only
underscores and alphanumeric characters and must be unique in your org. It

must begin with a letter, not include spaces, not end with an underscore, and
not contain two consecutive underscores. This 25-character field must be
unique among other EmailServicesAddress records under the same
EmailServiceFunction parent.

In managed packages, this field prevents naming conflicts on package
installations. This field is automatically generated, but you can supply your own
value if you create the record using the API. With this field, a developer can
change the object’s name in a managed package and the changes are reflected
in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique
`developerName` for each record. If no `developerName` is
specified, performance might be slow while Salesforce generates one
for each record.

`isActive` boolean Indicates whether this object is active ( `true` ) or not ( `false` ).

`localPart` string

Required. The local-part of the email service address, which is the string that
comes before the @ symbol. For the local-part of a Salesforce email address,
all alphanumeric characters are valid, plus the following special characters:

```
! # $ % & amp; ' * / = ? ^ _ + - ` { | } ~,

```

The dot character (.) is also valid as long as it's not the first or last character.
Email addresses aren’t case sensitive.

`runAsUser` string Required. The username of the user whose permissions the email service
assumes when processing messages sent to this address.

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

### EmailTemplate

Represents a template for an email, mass email, list email, or Sales Engagement email. Supported in first-generation managed packages
only.

This type extends the MetadataWithContent metadata type and inherits its `content` and `fullName` fields.

Note: First-generation packaging only is supported for Lightning email templates.


Metadata Types EmailTemplate

File Suffix and Directory Location

The file suffix is `.email` for the template file. The accompanying metadata file is named _`EmailTemplateName`_ `-meta.xml` .

EmailTemplate components are stored in the `email` folder in the corresponding package directory. For example, for an email template
named SampleTemplate in the sampleFolder folder, there’s a `SampleTemplate-meta.xml` in the `email/sampleFolder`
of the package.

Retrieving Email Templates

You can’t use the wildcard (*) symbol with email templates in `package.xml` . To retrieve the list of email templates for populating
`package.xml` with explicit names, call `listMetadata()` and pass in `EmailTemplate` as the type.

The following example shows folders in `package.xml` :

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>MyDBFolder/MyDBName</members>

        <name>Dashboard</name>

      </types>

      <types>

        <members>MyDocumentFolder/MyDocumentName</members>

        <name>Document</name>

      </types>

      <types>

        <members>unfiled$public/MarketingProductInquiryResponse</members>

        <members>unfiled$public/SalesNewCustomerEmail</members>

        <name>EmailTemplate</name>

      </types>

      <types>

        <members>MyReportFolder/MyReportName</members>

        <name>Report</name>

      </types>

      <version>66.0</version>

   </Package>

```

Version

Email templates are available in API version 12.0 and later.

Fields

This metadata type contains the following fields:

**Field Name** **Field Type** **Description**

`apiVersion` double

The API version if it's a Visualforce email template. Every Visualforce email
template has an API version specified at creation. This field is available in API
version 16.0 and later.


Metadata Types EmailTemplate

**Field Name** **Field Type** **Description**

`attachedDocuments` string[]

A list of references to documents in your organization. These documents are
included as attachments in the email template. Each document is referenced
by its path, for example `MyFolder/MyDocument.txt` .

`attachments` Attachment[] A list of attachments for the email template.

`available` boolean Required. Indicates whether this template is offered to users when sending an
email ( `true` ) or not ( `false` ).

`content` base64Binary Content of the email template. Base 64-encoded binary data. Before making an
API call, client applications must encode the binary attachment data as base64.

Upon receiving a response, client applications must decode the base64 data to
binary. This conversion is handled for you by a SOAP client. This field contains:

**•** Binary content of the email body if `type` is set to `text`

**•** HTML email content if `type` is set to `html`

**•** HTML body if `type` is set to `custom`

**•** Visualforce body if `type` is set to `visualforce`

This field is inherited from the MetadataWithContent component.

`description` string The email template description describes the reason for creating the template.

`encodingKey` Encoding (enumeration
of type string)

Required for Classic email templates. The default encoding setting is Unicode:
`UTF-8` . Change it if your template requires data in a different format.

Valid values include:

**•** `UTF-8` —Unicode (UTF-8)

**•** `ISO-8859-1` —General US & Western Europe (ISO-8859–1, ISO-LATIN-1)

**•** `Shift_JIS` —Japanese (Shift-JIS)

**•** `ISO-2022-JP` —Japanese (JIS)

**•** `EUC-JP` —Japanese (EUC-JP)

**•** `x-SJIS_0213` —Japanese (Shift-JIS_2004)

**•** `ks_c_5601-1987` —Korean (ks_c_5601-1987)

**•** `Big5` —Traditional Chinese (Big5)

**•** `GB2312` —Simplified Chinese (GB2312)

**•** `Big5-HKSCS` —Traditional Chinese Hong Kong (Big5–HKSCS)

Lightning email templates don’t use this field. Instead, the encoding values are
taken directly from the user’s encoding settings.

`fullName` string The email template developer name used as a unique identifier for API access.
The `fullName` can contain only underscores and alphanumeric characters.

It must be unique, begin with a letter, not include spaces, not end with an
underscore, and not contain two consecutive underscores. If this field contained
characters before version 14.0 that are no longer allowed, the characters were
stripped out of this field, and the previous value of the field was saved in the
`name` field. This field is inherited from the Metadata component.


Metadata Types EmailTemplate

**Field Name** **Field Type** **Description**

`letterhead` string The letterhead name associated with this email template. Only available when
`type` is set to `html` .

`name` string

`packageVersions` PackageVersion[]

Required. Email template name. The list of characters allowed in the `fullName`
field has been reduced for versions 14.0 and later. This field contains the value
contained in the `fullName` field before version 14.0.

The list of package versions for any managed packages containing components
that are referenced by this email template. This field is only relevant for Visualforce
email templates.

[For more information about managed packages, see Second-Generation](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_dev2gp.htm)
[Managed Packages in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_dev2gp.htm) _Salesforce DX Developer Guide_ . This field is available in
API version 16.0 and later.

```
relatedEntityType

style

```

Object Name Reserved for future use with Lightning Experience.
(enumeration of type
string)

EmailTemplateStyle
(enumeration of type
string)

Required. The style of the template. This field is only available when type is set
to `html` .

Valid style values include:

**•** `none`

**•** `freeForm`

**•** `formalLetter`

**•** `promotionRight`

**•** `promotionLeft`

**•** `newsletter`

**•** `products`

The email subject.

The limit is 1,000 characters for Lightning email templates and 230 characters
for Classic email templates.

`subject` string

`textOnly` string The text of the email body if type is set to `html` or `custom` .

Required. The email template type.

The valid values are:

**•** `text` - all users can create or change text email templates.

**•** `html` - administrators and users with the “Edit HTML Templates” permission
can create HTML email templates based on a letterhead.

**•** `custom` - administrators and users with the “Edit HTML Templates”
permission can create custom HTML email templates without using a
letterhead. You must either know HTML or obtain the HTML code to insert
in your email template.


```
type

```

EmailTemplateType
(enumeration of type
string)

Metadata Types EmailTemplate

**Field Name** **Field Type** **Description**

**•** `visualforce`                       - administrators and users with the Customize Application
permission can create email templates using Visualforce.

```
UiType

```

Example:

EmailTemplateUiType Indicates the user interface where this template is usable. Valid values are:
(enumeration of type

**•** `Aloha` (Salesforce Classic)

string)

**•** `Aloha` (Salesforce Classic)

**•** `SFX` (Lightning Experience)

**•** `SFX_Sample` (Lightning Experience Sample)

If `UiType` is `SFX`, the `type` must be `custom` .

Packaging is supported for Salesforce Classic email templates only.

```
   <EmailTemplate>

     <available>true</available>

     <description>Notification that user has been added to a community.</description>

     <encodingKey>UTF-8</encodingKey>

     <name>Communities: New Member Welcome Email</name>

     <style>none</style>

     <subject>Welcome to {!Community_Name}</subject>

     <type>custom</type>

     <uiType>Aloha</uiType>

   </EmailTemplate>

```

Attachment

Attachment represents an email attachment.

**Field** **Field Type** **Description**

`content` base64Binary Required. The attachment content. Base 64-encoded binary
data. Before making an API call, client applications must encode

the binary attachment data as base64. Upon receiving a
response, client applications must decode the base64 data to
binary. This conversion is handled for you by a SOAP client.

`name` string Required. The attachment file name.

Declarative Metadata Sample Definition

Here's a sample XML definition of an email template.

```
<?xml version="1.0" encoding="UTF-8"?>

<EmailTemplate xmlns="http://soap.sforce.com/2006/04/metadata">

   <available>true</available>

```


### Metadata Types EmbeddedServiceBranding

```
      <description>Sample Email Template</description>

      <encodingKey>ISO-8859-1</encodingKey>

      <name>Sample Email Template</name>

      <style>none</style>

      <subject>Sample email subject</subject>

      <textOnly>Your case has been resolved.</textOnly>

      <type>custom</type>

   </EmailTemplate>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

Letterhead

### EmbeddedServiceBranding

Represents the branding for each Embedded Service deployment. This type extends the Metadata metadata type and inherits its
`fullName` field.

This object works only with the legacy chat products. For Messaging for In-app and Web, use the BrandingSet object.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### EmbeddedServiceBranding components are stored in the developer_name .EmbeddedServiceBranding file in the EmbeddedServiceBranding folder.

Version

### EmbeddedServiceBranding is available in API version 39.0 and later.

Fields

**Field Name** **Field Type** **Description**

`contrastInvertedColor` string

Accent branding color used in the embedded component, displayed as
a hexadecimal value. Changes made to this field in the API aren’t reflected
in the embedded component.

`contrastPrimaryColor` string Accent branding color used in the embedded component, displayed as
a hexadecimal value.


Metadata Types EmbeddedServiceBranding

**Field Name** **Field Type** **Description**

`embeddedServiceConfig` string Required. The Embedded Service configuration that this branding applies
to.

`font` string Font used in the text of the embedded component.

`height` int Height of the embedded component. Available in API version 43.0 and
later.

`masterLabel` string Required. The name of the Embedded Service configuration node.

`navBarColor` string Color used for the header in the embedded component, displayed as a
hexadecimal value.

`navBarTextColor` string

Color used for the text and icons in the header in the embedded
component, displayed as a hexadecimal value. Available in API version
49.0 and later.

`primaryColor` string Primary branding color used in the embedded component, displayed
as a hexadecimal value.

`secondaryColor` string Secondary branding color used in the embedded component, displayed
as a hexadecimal value.

`secondaryNavBarColor` string Secondary branding color used for the header in the embedded
component, displayed as a hexadecimal value. It applies to the header

in the chat feature when it's trying to reconnect because of lost internet
connection. Available in API version 49.0 and later.

`width` int Width of the embedded component. Available in API version 43.0 and
later.

Declarative Metadata Sample Definition

The following is an example of an EmbeddedServiceBranding file.

```
<?xml version="1.0" encoding="UTF-8"?>

<EmbeddedServiceBranding xmlns="http://soap.sforce.com/2006/04/metadata">

   <contrastInvertedColor>#ffffff</contrastInvertedColor>

   <contrastPrimaryColor>#333333</contrastPrimaryColor>

   <embeddedServiceConfig>EswConfig001</embeddedServiceConfig>

   <font>Salesforce Sans</font>

   <height>498</height>

   <masterLabel>EmbeddedServiceBranding_Parent04IRM000000002a_16033cd2c16</masterLabel>

   <navBarColor>#222222</navBarColor>

   <primaryColor>#222222</primaryColor>

   <secondaryColor>#005290</secondaryColor>

   <width>320</width>

</EmbeddedServiceBranding>

```


### Metadata Types EmbeddedServiceConfig

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

### EmbeddedServiceConfig

Represents a setup node for creating an Embedded Service for Web deployment. This type extends the Metadata metadata type and
inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### EmbeddedServiceConfig components have the suffix .EmbeddedServiceConfig and are stored in the EmbeddedServiceConfig folder.

Version

### EmbeddedServiceConfig is available in API version 37.0 and later.

Fields

**Field Name** **Field Type** **Description**

`areGuestUsersAllowed` boolean Specifies whether a user must be logged in to access an embedded
component. Available in API version 45.0 and later.

```
authMethod

```

EmbeddedServiceAuthMethod Type of login method selected for this Embedded Service deployment.
(enumeration of Valid values are:
type string)

**•** `CommunitiesLogin` –Customers log in using Communities.

**•** `CustomLogin` –Customers log in using your own custom
authentication.

Available in API version 43.0 and later.

`branding` string The branding set that has all of the branding configurations for this
Embedded Service configuration. Available in API version 52.0 and later.

`customMinimizedComponent` string The custom Lightning component that’s used in this Embedded Service
deployment in its minimized state. Available in API version 43.0 to 45.0.


Metadata Types EmbeddedServiceConfig

**Field Name** **Field Type** **Description**

`deploymentFeature` EmbeddedServiceDeploymentFeature(enumeration The conversation type of this Embedded Service deployment. Valid
of type string) values are:

**•** `EmbeddedMessaging` —Messaging for In-App and Messaging
for Web deployments

**•** `Flows`

**•** `FieldService`

**•** `LiveAgent`

**•** `None`

Available in API version 52.0 and later.

```
deploymentType

```

EmbeddedServiceDeploymentType The platform this Embedded Service is deployed to. Valid values are:
(enumeration of

**•** `Mobile` —For future use

type string)

**•** `Mobile` —For future use

**•** `Web`

`embeddedServiceAppointmentSettings` EmbeddedServiceAppointmentSe **t** ings[]

**•** `API`

Available in API version 51.0 and later.

The settings of the Embedded Service deployment whose
`deploymentFeature` is `FieldService` . Available in API version
46.0 and later.

`embeddedServiceCustomComponents` EmbeddedServiceCustomComponent The custom components used in this Embedded Service deployment.
on page 1015[] Available in API version 44.0 and later.

`embeddedServiceCustomLabels` EmbeddedServiceCustomLabel The custom labels used in this Embedded Service deployment. Available
on page 1015[] in API version 44.0 and later.

`embeddedServiceCustomizations` EmbeddedServiceCustomization
on page 1016[]

The customizations used in this Embedded Service deployment. Each
customization is associated with a static resource. Available in API version
50.0 and later.

`embeddedServiceFlowConfig` EmbeddedServiceFlowConfig Represents a setup node for creating an embedded flow. Available in
on page 1020[] API version 45.0 and later.

`embeddedServiceFlows` EmbeddedServiceFlow All of the flows used by this Embedded Service deployment. Available
on page 1019[] in API version 45.0 and later.

`embeddedServiceLayouts` EmbeddedServiceLayout[] The layout of an Appointment Management deployment of an
Embedded Service. Available in API version 44.0 and later.

`isEnabled` boolean Indicates if this Embedded Service deployment is enabled (true).

`isTermsAndConditionsEnabled` boolean Indicates whether Terms and Conditions is displayed. Displaying Terms
and Conditions is supported if the `deploymentFeature` is either

`EmbeddedMesssaging` or `LiveAgent` . The default is `false` .
Available in API version 59.0 and later.

`isTermsAndConditionsRequired` boolean Indicates whether acceptance of the Terms and Conditions is required
before starting a chat. Displaying Terms and Conditions is supported if

the `deploymentFeature` is either `EmbeddedMesssaging`


Metadata Types EmbeddedServiceConfig

**Field Name** **Field Type** **Description**

or `LiveAgent` . The default is `false` . Available in API version 59.0
and later.

`masterLabel` string Required. The name of the Embedded Service configuration node.
Available in API version 37.0 and later.

`shouldHideAuthDialog` boolean Specifies whether the prompt that the customer log in again during a
flow is hidden ( `true` ) or not ( `false` ). When it’s hidden, the customer

is taken directly to your login page. This field is set to `false` by default.
Available in API version 43.0 and later.

`site` string Required. The name of the Experience site or website connected to this
Embedded Service deployment. Available in API version 37.0 and later.

EmbeddedServiceAppointmentSettings

Returns the settings of an Embedded Service deployment whose `deploymentFeature` is `FieldService` . Available in API
version 46.0 and later.

**Field Name** **Description**

```
appointmentConfirmImg

enabled

homeImg

logoImg

shouldShowExistingAppointment

```

**Field Type**
string

**Description**
The URL of the image to display when an appointment is confirmed.

**Field Type**
boolean

**Description**

Required.

Indicates whether this deployment is enabled. The default is `false` .

**Field Type**
string

**Description**
The URL of the image to display on the appointment management widget home
screen.

**Field Type**
string

**Description**
The URL of the logo to display in the appointment management widget.

**Field Type**
boolean


Metadata Types EmbeddedServiceConfig

**Field Name** **Description**

**Description**
Indicates whether existing appointments are displayed in the appointment
management widget. The default is `false` .

```
shouldShowNewAppointment

```

**Field Type**
boolean

**Description**
Indicates whether new appointments are displayed in the appointment management
widget. The default is `false` .

EmbeddedServiceCustomComponent

Returns a custom component that’s associated with an EmbeddedServiceConfig setup.

EmbeddedServiceCustomLabel

Returns a custom label that’s associated with an EmbeddedServiceConfig setup.


Metadata Types EmbeddedServiceConfig

EmbeddedServiceCustomization

Returns the customization associated with the Embedded Service feature. Available in API version 50.0 and later.

EmbeddedServiceForm

Returns the form that’s used for pre-chat. Available in API version 62 and later.


Metadata Types EmbeddedServiceConfig

EmbeddedServiceFormField

Represents an individual field in a prechat form. Available in API version 62 or higher.


Metadata Types EmbeddedServiceConfig

embeddedServiceMessagingChannel

Returns the settings of an Embedded Service deployment whose

```
deploymentFeature

```

is EmbeddedMessaging. Available in API version 62 or higher.


Metadata Types EmbeddedServiceConfig

EmbeddedServiceResource

Returns the static resource associated with the Embedded Service Chat feature customization. Available in API version 50.0 and later.

EmbeddedServiceFlow

Returns an embedded flow that’s associated with an EmbeddedServiceConfig setup.


Metadata Types EmbeddedServiceConfig

EmbeddedServiceFlowConfig

Returns the EmbeddedServiceFlowConfig type.

EmbeddedServiceLayout

Returns the layout of an Embedded Service deployment whose `deploymentFeature` is `FieldService` . Available in API version
44.0 and later.

**Field Name** **FieldDescription**
**Type**

`embeddedServiceLayoutRules` []tRledSrviceLayo **u** Embe **de** The appointment statuses that the layout of the Embedded Service deployment is valid
for.

`layout` string The FlexiPage that represents the layout of this Embedded Service deployment.

```
layoutType

```

SrviceLayoutTypeEmb **ed**
(enumeration
f 

The type of layout applied to the Embedded Service deployment.

Values are:

**•** `FS_AppointmentHome`
type
string)


Metadata Types EmbeddedServiceConfig

EmbeddedServiceLayoutRule

Returns an appointment status for which the Embedded Service layout is valid for. This subtype is for Embedded Service deployments
whose `deploymentFeature` is `FieldService` . Available in API version 44.0 and later.

**Field Name** **Field Type** **Description**

`appointmentStatus` string The service appointment status that the EmbeddedServiceLayout subtype
is valid for.

Declarative Metadata Sample Definition

The following is an example of an EmbeddedServiceConfig file.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <EmbeddedServiceConfig xmlns="http://soap.sforce.com/2006/04/metadata">

      <areGuestUsersAllowed>false</areGuestUsersAllowed>

      <deploymentType>Mobile</deploymentType>

      <deploymentFeature>EmbeddedMessaging</deploymentFeature>

      <masterLabel>ESWOne</masterLabel>

      <shouldHideAuthDialog>false</shouldHideAuthDialog>

      <embeddedServiceMessagingChannel>

        <isEnabled>true</isEnabled>

        <shouldShowTypingIndicators>false</shouldShowTypingIndicators>

        <shouldShowReadReceipts>false</shouldShowReadReceipts>

        <shouldShowDeliveryReceipts>false</shouldShowDeliveryReceipts>

        <shouldShowEmojiSelection>false</shouldShowEmojiSelection>

        <shouldStartNewLineOnEnter>false</shouldStartNewLineOnEnter>

        <messagingChannel>EM1</messagingChannel>

      </embeddedServiceMessagingChannel>

      <embeddedServiceForms>

        <isActive>true</isActive>

        <displayContext>Session</displayContext>

        <embeddedServiceFormFields>

           <displayOrder>0</displayOrder>

           <formField>_FirstName</formField>

           <messagingChannelParameterType>Standard</messagingChannelParameterType>

           <formFieldType>Text</formFieldType>

           <isHidden>false</isHidden>

           <isRequired>true</isRequired>

           <embeddedServiceCustomLabels>

   <customLabel>EM_PreChat_Base_PrechatCustomFieldLabel_133xx0000004GG2_5523048</customLabel>

             <labelKey>EM_PreChat_Base_PrechatCustomFieldLabel</labelKey>

             <feature>EmbeddedMessaging</feature>

           </embeddedServiceCustomLabels>

        </embeddedServiceFormFields>

        <embeddedServiceFormFields>

           <displayOrder>1</displayOrder>

```


### Metadata Types EmbeddedServiceFieldService

```
           <formField>_LastName</formField>

           <messagingChannelParameterType>Standard</messagingChannelParameterType>

           <formFieldType>Text</formFieldType>

           <isHidden>false</isHidden>

           <isRequired>true</isRequired>

           <embeddedServiceCustomLabels>

   <customLabel>EM_PreChat_Base_PrechatCustomFieldLabel_133xx0000004GG2_5523058</customLabel>

             <labelKey>EM_PreChat_Base_PrechatCustomFieldLabel</labelKey>

             <feature>EmbeddedMessaging</feature>

           </embeddedServiceCustomLabels>

        </embeddedServiceFormFields>

        <embeddedServiceFormFields>

           <displayOrder>2</displayOrder>

           <formField>FavoriteFood_name</formField>

           <messagingChannelParameterType>Custom</messagingChannelParameterType>

           <formFieldType>ChoiceList</formFieldType>

           <isHidden>false</isHidden>

           <isRequired>true</isRequired>

           <choiceList>Food</choiceList>

        </embeddedServiceFormFields>

      </embeddedServiceForms>

   </EmbeddedServiceConfig>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

### EmbeddedServiceFieldService

Represents a setup node for creating an embedded Appointment Management deployment. This type extends the Metadata metadata
type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### EmbeddedServiceFieldService components are stored in a developer_name .EmbeddedServiceFieldService file in the EmbeddedServiceFieldService folder.

Version

### EmbeddedServiceFieldService is available in API version 43.0 and later.


Metadata Types EmbeddedServiceFieldService

Fields

**Field Name** **Field Type** **Description**

`appointmentBookingFlowName` string Name of the appointment booking flow for this embedded Appointment
Management (beta) deployment.

`cancelApptBookingFlowName` string Name of the appointment cancellation flow for this embedded
Appointment Management (beta) deployment.

`embeddedServiceConfig` string Required. The name of the Embedded Service configuration node.

`enabled` boolean Required. Indicates whether this embedded Appointment Management
deployment is enabled ( `true` ).

`fieldServiceConfirmCardImg` string URL of the image used for the confirmation card in embedded
Appointment Management (beta).

`fieldServiceHomeImg` string URL of the image used for the home screen in embedded Appointment
Management (beta).

`fieldServiceLogoImg` string URL of the logo used for the home screen in embedded Appointment
Management (beta).

`masterLabel` string Required. Name of the embedded Appointment Management (beta)
deployment.

`modifyApptBookingFlowName` string Name of the appointment modification flow for this embedded
Appointment Management (beta) deployment.

`shouldShowExistingAppointment` boolean

`shouldShowNewAppointment` boolean

Specifies whether to display a button on the home screen for customers
to access their existing appointments ( `true` ) or not ( `false` ). This field
is `false` by default.

Specifies whether to display a button on the home screen for customers
to create a new appointment ( `true` ) or not ( `false` ). This field is
`false` by default.

Declarative Metadata Sample Definition

The following is an example of an EmbeddedServiceFieldService file.

```
<?xml version="1.0" encoding="UTF-8"?>

<EmbeddedServiceFieldService xmlns="http://soap.sforce.com/2006/04/metadata">

   <appointmentBookingFlowName>ESW_FS_BookAppt_Main_Flow</appointmentBookingFlowName>

   <cancelApptBookingFlowName>ESW_FS_CancelAppt_Flow</cancelApptBookingFlowName>

   <embeddedServiceConfig>EswFS</embeddedServiceConfig>

   <enabled>true</enabled>

<fieldServiceConfirmCardImg>https://google.com/AppointmentConfirmationImg.png</fieldServiceConfirmCardImg>

   <fieldServiceHomeImg>https://google.com/HeroImg.png</fieldServiceHomeImg>

   <fieldServiceLogoImg>https://google.com/logo.png</fieldServiceLogoImg>

```


### Metadata Types EmbeddedServiceFlowConfig

```
   <masterLabel>EmbeddedServiceFieldService_Parent04IRM000000007p2AA_162d4270834</masterLabel>

      <modifyApptBookingFlowName>ESW_FS_ModifyAppt_Main_Flow</modifyApptBookingFlowName>

      <shouldShowExistingAppointment>true</shouldShowExistingAppointment>

      <shouldShowNewAppointment>true</shouldShowNewAppointment>

   </EmbeddedServiceFieldService>

```

Usage

Note: Any changes you make to the image fields override what you’ve entered in Setup. We recommend setting your image
URLs in Setup.

### EmbeddedServiceFlowConfig

Represents a setup node for creating an embedded flow. This type extends the Metadata metadata type and inherits its `fullName`
field.

File Suffix and Directory Location

### EmbeddedServiceFlowConfig components are stored in the developer_name .EmbeddedServiceFlowConfig file in the EmbeddedServiceFlowConfig folder.

Version

### EmbeddedServiceFlowConfig is available in API version 45.0 and later.

Fields

**Field Name** **Field Type** **Description**

`enabled` boolean Indicates whether the embedded flow is enabled ( `true` ) or not
( `false` ). Defaults to `false` .

Declarative Metadata Sample Definition

The following is an example of an EmbeddedServiceFlowConfig file.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <EmbeddedServiceFlowConfig xmlns="http://soap.sforce.com/2006/04/metadata">

      <enabled>true</enabled>

   </EmbeddedServiceFlowConfig>

```


### Metadata Types EmbeddedServiceLiveAgent EmbeddedServiceLiveAgent

Represents a setup node for creating an embedded chat deployment. This type extends the Metadata metadata type and inherits its
`fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### EmbeddedServiceLiveAgent components are stored in the developer_name .EmbeddedServiceLiveAgent file in the EmbeddedServiceLiveAgent folder.

Version

### EmbeddedServiceLiveAgent is available in API version 38.0 and later.

Fields

**Field Name** **Field Type** **Description**

`avatarImg` string Avatar image for this embedded chat deployment.

`customPrechatComponent` string The custom Lightning Component that’s used for the pre-chat page in
this embedded chat deployment.

`embeddedServiceConfig` string Required. The name of the embedded service configuration node.

`embeddedServiceQuickActions` EmbeddedServiceQuickAction The quick action used by the pre-chat form.

`enabled` boolean Required. Indicates whether this embedded chat deployment is enabled
( `true` ).

```
fontSize

```

EmbeddedServiceFontSize Required. The font size for the text in the embedded chat window. One
(enumeration of of the following values:
type string)

**•** `Small`

**•** `Medium`

**•** `Large`

`headerBackgroundImg` string Header background image for this embedded chat window. Removed
in API version 49.0.

`isOfflineCaseEnabled` boolean Indicates whether offline support is enabled for this embedded chat
deployment. Available in API version 43.0 and later.

`isQueuePositionEnabled` boolean

Indicates whether queue position (displaying the chat visitor’s place in
line while they wait for an agent) is enabled for this embedded chat
deployment. Available in API version 43.0 and later.

`liveAgentChatUrl` string The rest endpoint for chats.


Metadata Types EmbeddedServiceLiveAgent

**Field Name** **Field Type** **Description**

`liveAgentContentUrl` string The rest endpoint for cChat content.

`liveChatButton` string Required. Reference to a chat button created in Chat setup.

`liveChatDeployment` string Required. Reference to a deployment created in Chat setup.

`masterLabel` string Required. Name of the embedded chat deployment.

`offlineCaseBackgroundImg` string Offline support case form background image for this embedded chat
window. Available in API version 43.0 and later.

`prechatBackgroundImg` string Pre-chat background image for this embedded chat window.

`prechatEnabled` string Required. Indicates whether the embedded chat pre-chat form is enabled
for this deployment.

`prechatJson` string JSON object of all the fields of the selected pre-chat form in Chat setup.

```
scenario

```

EmbeddedServiceScenario Required. The scenario for the embedded chat window that determines
(enumeration of which objects to relate to the chat. One of the following values:
type string)

**•** `Sales`

**•** `Service`

**•** `Basic`

`smallCompanyLogoImg` string Company logo image for this embedded chat window.

`waitingStateBackgroundImg` string Chat waiting image for this embedded chat window.

EmbeddedServiceQuickAction

Returns a quick action that’s associated with an EmbeddedServiceLiveAgent setup. The quick action includes the pre-chat form fields
that the embedded chat window displays and shows the order in which the fields are displayed.

**Field Name** **Field Type** **Description**

`embeddedServiceLiveAgent` string Reference to the embedded chat deployment.

`order` int Order in which this quick action appears in the embedded chat pre-chat form.

`quickActionDefinition` string Reference to a quick action.

```
quickActionType

```

EmbeddedServiceQuickActionType Quick action type. One of the following values:
(enumeration of type

**•** `Prechat` –Pre-chat

string)

**•** `Prechat` –Pre-chat

**•** `OfflineCase` –Offline support (Cases)

Available in API version 43.0 and later.


Metadata Types EmbeddedServiceLiveAgent

Declarative Metadata Sample Definition

The following is an example of an EmbeddedServiceLiveAgent file.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <EmbeddedServiceLiveAgent xmlns="http://soap.sforce.com/2006/04/metadata">

      <avatarImg>https://google.com/avatar.png</avatarImg>

      <customPrechatComponent>auraCustomPrechat</customPrechatComponent>

      <embeddedServiceConfig>EswConfig001</embeddedServiceConfig>

      <embeddedServiceQuickActions>

   <embeddedServiceLiveAgent>EmbeddedServiceLiveAgent_Parent04Ixx0000000001EAA_15ec5bd2971</embeddedServiceLiveAgent>

        <order>1</order>

   <quickActionDefinition>Snapins_Contact_QuickAction_08hRM000000001h</quickActionDefinition>

      </embeddedServiceQuickActions>

      <embeddedServiceQuickActions>

   <embeddedServiceLiveAgent>EmbeddedServiceLiveAgent_Parent04Ixx0000000001EAA_15ec5bd2971</embeddedServiceLiveAgent>

        <order>1</order>

   <quickActionDefinition>Snapins_Case_OfflineCaseQuickAction_08hRM000000001h</quickActionDefinition>

        <quickActionType>OfflineCase</quickActionType>

      </embeddedServiceQuickActions>

      <embeddedServiceQuickActions>

   <embeddedServiceLiveAgent>EmbeddedServiceLiveAgent_Parent04Ixx0000000001EAA_15ec5bd2971</embeddedServiceLiveAgent>

        <order>2</order>

   <quickActionDefinition>Snapins_Case_QuickAction_08hRM000000001h</quickActionDefinition>

      </embeddedServiceQuickActions>

      <enabled>true</enabled>

      <fontSize>Medium</fontSize>

      <headerBackgroundImg>https://google.com/headerBackgroundImg.png</headerBackgroundIm>

      <isOfflineCaseEnabled>true</isOfflineCaseEnabled>

      <isQueuePositionEnabled>true</isQueuePositionEnabled>

      <liveChatButton>chatButton01</liveChatButton>

      <liveChatDeployment>liveAgentDeployment01</liveChatDeployment>

     <masterLabel>EmbeddedServiceLiveAgent_Parent04Ixx0000000001EAA_15ec5bd2971</masterLabel>

   <offlineCaseBackgroundImg>https://google.com/offlineCaseBackgroundImg.png</offlineCaseBackgroundImg>

     <prechatBackgroundImg>https://google.com/prechatBackgroundImg.png</prechatBackgroundImg>

      <prechatEnabled>true</prechatEnabled>

      <scenario>Service</scenario>

      <smallCompanyLogoImg>https://google.com/smallCompanyLogoImg.png</smallCompanyLogoImg>

```


### Metadata Types EmbeddedServiceMenuSettings

```
   <waitingStateBackgroundImg>https://google.com/waitingImage.png</waitingStateBackgroundImg>

   </EmbeddedServiceLiveAgent>

```

Usage

EmbeddedServiceLiveAgent represents a Chat configuration that is added to your web page. The EmbeddedServiceLiveAgent record
contains a unique combination of a chat button and the Chat deployment that the administrator selects during setup.

To create an EmbeddedServiceLiveAgent record:

**1.** Create a Chat Deployment record.

**2.** Create a Chat Button record.

**3.** Create an EmbeddedServiceConfig record.

**4.** Set the fields for the Chat Deployment record, Chat Button record, and EmbeddedServiceConfig record as references on the
EmbeddedServiceLiveAgent record.

Any changes you make to the image fields override what you’ve entered in Setup. We recommend setting your image URLs in Setup.

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

### EmbeddedServiceMenuSettings

Represents a setup node for creating a channel menu deployment. Channel menus list the ways in which customers can contact your
business. This type extends the Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### EmbeddedServiceMenuSettings components are stored in the developer_name.EmbeddedServiceMenuSettings folder.

Version

### EmbeddedServiceMenuSettings components are available in API version 47.0 and later.

Fields

**Field Name** **Field Type** **Description**

`branding` string The developer name of the associated BrandingSet.

`embeddedServiceCustomLabels` EmbeddedServiceCustomLabel[]


Represents a customized label that appears in the
embedded component for a particular channel menu
deployment.

Metadata Types EmbeddedServiceMenuSettings

**Field Name** **Field Type** **Description**

`embeddedServiceCustomizations` EmbeddedServiceCustomization The customizations used in this Embedded Service
on page 1029[] deployment. Each customization is associated with

a static resource. Available in API version 50.0 and
later.

`embeddedServiceMenuItems` EmbeddedServiceMenuItem[] Represents a channel menu item that lists a way in
which customers can contact your business.

`isEnabled` boolean If `true` (default), the deployment is enabled. If
`false`, the deployment is disabled.

`masterLabel` string Required. The name of the channel menu
deployment.

`site` string Required. The name of the Experience site or website
connected to this channel menu deployment.

EmbeddedServiceCustomLabel

Represents the custom labels used in your channel menu deployment.

**Field Name** **Field Type** **Description**

`customLabel` string The customized label that appears in the channel menu.

`feature` EmbeddedServiceFeature The feature using the custom label. For channel menu
(enumeration of type string) deployments, the value is `ChannelMenu` .

`labelKey` EmbeddedServiceLabelKey
(enumeration of type string)

EmbeddedServiceCustomization

The type of label for this embedded component. The value
corresponds to the label within a label group (substate of chat
state or page type).

Returns the customization associated with the Embedded Service feature. Available in API version 50.0 and later.


Metadata Types EmbeddedServiceMenuSettings

EmbeddedServiceResource

Returns the static resource associated with the Embedded Service Chat feature customization. Available in API version 50.0 and later.

EmbeddedServiceMenuItem

Represents an item in a channel menu.

**Field Name** **Field Type** **Description**

`channel` string The ID of the channel type. If `channelType` is
`Phone` or `CustomURL`, this field is `null` .

`channelType` EmbeddedServiceChannelType The type of communication channel. Values are:
(enumeration of type string)

**•** `EmbeddedMessaging`

**•** `EmbeddedServiceConfig`

**•** `MessagingChannel`

**•** `Phone`

**•** `CustomURL`

`customUrl` string

A custom URL that appears in the menu. The
`shouldOpenUrlInSameTab` field determines
where the URL opens.

`displayOrder` int The item’s order in the menu, such as 1 or 2.

`embeddedServiceCustomLabels` EmbeddedServiceCustomLabel[] Represents the custom labels used in your channel
menu item.


Metadata Types EmbeddedServiceMenuSettings

**Field Name** **Field Type** **Description**

`iconUrl` string

The icon URL for the menu item. Icons can be used
only for phone, SMS, custom URL, and chat menu
items.

`isDisplayedOnPageLoad` boolean If `true`, the menu item is displayed on page load.
Available in API version 49.0 and later.

`itemName` string A unique custom name for the menu item, which is
visible in the user interface.

`osOptionsHideInIOS` boolean If `true`, the menu item is hidden in iOS.

`osOptionsHideInLinuxOS` boolean If `true`, the menu item is hidden in Linux operating
system.

`osOptionsHideInMacOS` boolean If `true`, the menu item is hidden in Mac operating
system.

`osOptionsHideInOtherOS` boolean If `true`, the menu item is hidden in any operating
system other than iOS, Linux, Mac, and Windows.

`osOptionsHideInWindowsOS` boolean If `true`, the menu item is hidden in Windows
operating system.

`phoneNumber` string The phone number for menu items whose
`channelType` is `Phone` .

`shouldOpenUrlInSameTab` boolean

Declarative Metadata Sample Definition

The following is an example of an EmbeddedServiceMenuSettings component.

If the menu item’s `channelType` is `CustomURL`,
this field indicates whether the link opens in the same
tab ( `true` ) or a new tab ( `false` ).

```
<?xml version="1.0" encoding="UTF-8"?>

<EmbeddedServiceMenuSettings xmlns="http://soap.sforce.com/2006/04/metadata">

   <embeddedServiceCustomLabels>

<customLabel>CM_Container_Header_Primary_Greeting_3MsRM0000004CB5_6181150</customLabel>

     <labelKey>CM_Container_Header_Primary_Greeting</labelKey>

   </embeddedServiceCustomLabels>

   <embeddedServiceCustomLabels>

<customLabel>CM_Container_Header_Secondary_Greeting_3MsRM0000004CB5_4637097</customLabel>

     <labelKey>CM_Container_Header_Secondary_Greeting</labelKey>

   </embeddedServiceCustomLabels>

   <embeddedServiceMenuItems>

     <channel>Chat</channel>

     <channelType>EmbeddedServiceConfig</channelType>

     <displayOrder>1</displayOrder>

```


Metadata Types EmbeddedServiceMenuSettings

```
        <embeddedServiceCustomLabels>

   <customLabel>CM_Container_MenuItems_WebChatUnavailable_3miRM0000004CuZ_8003848</customLabel>

           <labelKey>CM_Container_MenuItems_WebChatUnavailable</labelKey>

        </embeddedServiceCustomLabels>

        <embeddedServiceCustomLabels>

   <customLabel>CM_Container_MenuItems_WebChatAvailable_3miRM0000004CuZ_5823055</customLabel>

           <labelKey>CM_Container_MenuItems_WebChatAvailable</labelKey>

        </embeddedServiceCustomLabels>

        <itemName>Chat1</itemName>

        <osOptionsHideInIOS>false</osOptionsHideInIOS>

        <osOptionsHideInLinuxOS>true</osOptionsHideInLinuxOS>

        <osOptionsHideInMacOS>false</osOptionsHideInMacOS>

        <osOptionsHideInOtherOS>false</osOptionsHideInOtherOS>

        <osOptionsHideInWindowsOS>true</osOptionsHideInWindowsOS>

        <shouldOpenUrlInSameTab>false</shouldOpenUrlInSameTab>

      </embeddedServiceMenuItems>

      <embeddedServiceMenuItems>

        <channelType>Phone</channelType>

        <displayOrder>2</displayOrder>

        <itemName>Phone1</itemName>

        <osOptionsHideInIOS>true</osOptionsHideInIOS>

        <osOptionsHideInLinuxOS>false</osOptionsHideInLinuxOS>

        <osOptionsHideInMacOS>true</osOptionsHideInMacOS>

        <osOptionsHideInOtherOS>false</osOptionsHideInOtherOS>

        <osOptionsHideInWindowsOS>false</osOptionsHideInWindowsOS>

        <phoneNumber>1234567890</phoneNumber>

        <shouldOpenUrlInSameTab>false</shouldOpenUrlInSameTab>

      </embeddedServiceMenuItems>

      <embeddedServiceMenuItems>

        <channelType>CustomURL</channelType>

        <customUrl>https://google.com</customUrl>

        <displayOrder>3</displayOrder>

        <itemName>url1</itemName>

        <osOptionsHideInIOS>false</osOptionsHideInIOS>

        <osOptionsHideInLinuxOS>false</osOptionsHideInLinuxOS>

        <osOptionsHideInMacOS>false</osOptionsHideInMacOS>

        <osOptionsHideInOtherOS>false</osOptionsHideInOtherOS>

        <osOptionsHideInWindowsOS>false</osOptionsHideInWindowsOS>

        <shouldOpenUrlInSameTab>false</shouldOpenUrlInSameTab>

      </embeddedServiceMenuItems>

      <isEnabled>true</isEnabled>

      <masterLabel>ChannelMenuSettings</masterLabel>

      <site>SnapInCommunity</site>

   </EmbeddedServiceMenuSettings>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types EnablementMeasureDefinition EnablementMeasureDefinition

Represents an Enablement measure, which specifies the job-related activity that a user performs to complete a milestone or outcome
in an Enablement program. A measure identifies a source object and optional related objects, with optional field filters and filter logic,
for tracking the activity. To avoid deployment errors, deploy measures before you deploy programs.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### EnablementMeasureDefinition components have the suffix .enablementMeasureDefinition and are stored in the

`enablementMeasureDefinitions` folder.

Version

### EnablementMeasureDefinition components are available in API version 61.0 and later.

Special Access Rules

To access Enablement measures, the Design and Deliver Enablement Programs permission is required. This permission is available with
the Enablement add-on license.

Fields

**Field Name** **Description**

```
description

developerName

masterLabel

```

**Field Type**
string

**Description**
An internal description for the measure to help Enablement admins understand the
activity that’s tracked.

**Field Type**
string

**Description**

Required. The unique programmatic name for the measure record.

**Field Type**
string


Metadata Types EnablementMeasureDefinition

**Field Name** **Description**

**Description**

Required. A user-friendly name for the measure, which is defined when the measure
is created.

```
sourceMeasureObject

status

```

**Field Type**

EnablementMeasureSourceObjectDefinition

**Description**

Required. The source object that tracks the activity you're measuring.

**Field Type**
EnblProgramMeasureStatus (enumeration of type string)

**Description**

Required. Indicates whether the measure is published for use in Enablement programs.

Values are:

**•** `Draft` —The measure is saved, but not activated for use in programs.

**•** `Published` —The measure is activated for use in programs. In Lightning
Experience, this value is Active.

EnablementMeasureSourceObjectDefinition

Defines the source object, fields, field values, and calculation method for the job-related activity you’re measuring.

**Field Name** **Description**

```
aggregateFieldApiName

aggregateFunction

```

**Field Type**
string

**Description**
The unique programmatic name for the field that the `aggregateFunction` uses
for calculating.

For example, if you’re measuring how much revenue a sales rep has won, the value
of `aggregateFunction` is `Sum` and the value of `aggregateFieldApiName`
is `Amount`, which is the programmatic name of the Amount field on the Opportunity
object.

**Field Type**
EnablementAggregationType (enumeration of type string)

**Description**

Required. The method for calculating progress towards the milestone or outcome
from records that qualify for the measure’s criteria.

Values are:


Metadata Types EnablementMeasureDefinition

**Field Name** **Description**

**•** `Average`

**•** `Count`

**•** `Sum`

For example, if you’re measuring the number of deals won, the function is `Count` .

If the function is `Average` or `Sum`, `aggregateFieldApiName` is required.

```
dateFieldApiName

displayFieldApiName

filterLogic

filters

objectApiName

```

**Field Type**
string

**Description**

Required. The unique programmatic name for the field that defines when users get
credit for the activity you’re measuring. For example, if you’re measuring the number
of deals won, this value can be `ClosedDate`, the programmatic name of the Close
Date field on the Opportunity object.

**Field Type**
string

**Description**

Required. The unique programmatic name for the field that primarily identifies records
that qualify for the activity you’re measuring. For example, if you’re measuring the
number of deals won, you’re tracking the Opportunity object, and maybe you want
to identify opportunities by their name. In this case, this field can be `Name`, the
programmatic name of the Opportunity Name field on the Opportunity object.

**Field Type**
string

**Description**
An expression that determines how to evaluate the optional field filters for the object.

**Field Type**

EnablementMeasureFilterDefinition[]

**Description**
The fields on the object and corresponding field values that further specify criteria for
the activity you’re measuring.

**Field Type**
string

**Description**

Required. The unique programmatic name for the source object that tracks the activity
you’re measuring. For example, if you’re measuring the number of deals won, this
value is `Opportunity`, the programmatic name of the Opportunity object.


Metadata Types EnablementMeasureDefinition

**Field Name** **Description**

```
relatedMeasureObjects

userFieldApiName

```

**Field Type**

EnablementMeasureRelatedObjectDefinition[]

**Description**
The optional related objects that further specify criteria for the activity you’re measuring.
Related objects can also specify additional filters.

**Field Type**
string

**Description**

Required. The unique programmatic name for the field that defines who gets credit
for the activity you’re measuring. For example, if you’re measuring the number of deals
won by a sales rep, this value can be `OwnerId`, the developer name of the
Opportunity Owner field on the Opportunity object.

EnablementMeasureFilterDefinition

Represents the fields on the source object or related objects and the corresponding field values that further specify criteria for the activity
you’re measuring.

**Field Name** **Description**

```
fieldApiName

fieldValue

operator

```

**Field Type**
string

**Description**

Required. The unique programmatic name for the field that you’re filtering by. For
example, if you’re tracking activity on the Opportunity object and want to filter by the
Stage field, this value can be `StageName` .

**Field Type**
string

**Description**

Required. The field value to filter by. For example, if you’re tracking activity on the
Opportunity object and want to filter by the Stage field, this value can be `Closed`

```
  Won.

```

**Field Type**
EnablementFilterOperator (enumeration of type string)

**Description**

Required. The logic for evaluating the specified field and field value.

Values are:

**•** `Contains`


Metadata Types EnablementMeasureDefinition

**Field Name** **Description**

**•** `DoesNotContain`

**•** `DoesNotEqual`

**•** `EndsWith`

**•** `Equals`

**•** `GreaterThan`

**•** `GreaterThanOrEqual`

**•** `In`

**•** `IsNull`

**•** `LessThan`

**•** `LessThanOrEqual`

**•** `NotIn`

**•** `StartsWith`

```
sequenceNumber

```

**Field Type**
int

**Description**

Required. A number that specifies the order of the filter, relative to other filters, starting
at 1.

EnablementMeasureRelatedObjectDefinition

Represents objects related to the source object. Related objects can further specify criteria for the activity you’re measuring. Related
objects can also have additional filters. For example, maybe you’re measuring deals won for a specific product line. In this case, the source
object is Opportunity, the related object is Opportunity Product, and the related object can have a filter for the specific product name.

**Field Name** **Description**

```
filterLogic

filters

idFieldApiName

```

**Field Type**
string

**Description**
An expression that determines how to evaluate the optional field filters for the object.

**Field Type**

EnablementMeasureFilterDefinition[]

**Description**
The fields on the related object and the corresponding field values that further specify
criteria for the activity you’re measuring.

**Field Type**
string


Metadata Types EnablementMeasureDefinition

**Field Name** **Description**

**Description**

Required. The programmatic name of the field that links the related object to the
primary object. For example, if the primary object is Opportunity and the related object
is Opportunity Product, this value is `OpportunityId`, the developer name of the
Opportunity field on the Opportunity Product object.

```
objectApiName

```

**Field Type**
string

**Description**

Required. The unique programmatic name for the related object. For example, if the
related object is Opportunity Product, this value is `OpportunityLineItem` .

Declarative Metadata Sample Definition

The following is an example of an EnablementMeasureDefinition component.

```
<?xml version="1.0" encoding="UTF-8"?>

<EnablementMeasureDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

   <description>Total amount in pipeline measure</description>

   <developerName>TotalAmountInPipeline</developerName>

   <masterLabel>Total Amount in Pipeline</masterLabel>

   <status>Draft</status>

   <sourceMeasureObject>

     <aggregateFieldApiName>Amount</aggregateFieldApiName>

     <aggregateFunction>Sum</aggregateFunction>

     <dateFieldApiName>CreatedDate</dateFieldApiName>

     <displayFieldApiName>Name</displayFieldApiName>

     <objectApiName>Opportunity</objectApiName>

     <userFieldApiName>OwnerId</userFieldApiName>

     <filters>

        <fieldApiName>StageName</fieldApiName>

        <fieldValue>Closed Won</fieldValue>

        <operator>Equals</operator>

        <sequenceNumber>1</sequenceNumber>

     </filters>

     <relatedMeasureObjects>

        <objectApiName>OpportunityLineItem</objectApiName>

        <idFieldApiName>OpportunityId</idFieldApiName>

        <filterLogic>1 OR 2</filterLogic>

        <filters>

          <fieldApiName>UnitPrice</fieldApiName>

          <fieldValue>10000</fieldValue>

          <operator>GreaterThan</operator>

          <sequenceNumber>1</sequenceNumber>

        </filters>

        <filters>

          <fieldApiName>TotalPrice</fieldApiName>

          <fieldValue>10000</fieldValue>

```


### Metadata Types EnablementProgramDefinition

```
             <operator>GreaterThan</operator>

             <sequenceNumber>2</sequenceNumber>

           </filters>

        </relatedMeasureObjects>

      </sourceMeasureObject>

   </EnablementMeasureDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>TotalAmountInPipeline</members>

        <name>EnablementMeasureDefinition</name>

      </types>

      <version>61.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### EnablementProgramDefinition

Represents an Enablement program, which includes exercises and measurable milestones to help users such as sales reps achieve specific
outcomes related to your company’s revenue goals.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### EnablementProgramDefinition components have the suffix .enablementProgramDefinition and are stored in the

`enablementProgramDefinitions` folder.

Version

### EnablementProgramDefinition components are available in API version 61.0 and later.

Special Access Rules

To access Enablement programs, the Design and Deliver Enablement Programs permission is required. This permission is available with
the Enablement add-on license.


Metadata Types EnablementProgramDefinition

[For partner programs in supported Experience Cloud sites, a supported Partner Relationship Management (PRM) add-on license is also](https://help.salesforce.com/s/articleView?id=slack.prm_support_license_template.htm&type=5&language=en_US)
required.

Fields

**Field Name** **Description**

```
description

developerName

doesAllowSelfEnrollment

masterLabel

name

network

sections

```

**Field Type**
string

**Description**

Required. A summary of the program’s goals and content that’s visible to users.

**Field Type**
string

**Description**

Required. The unique programmatic name for the program record.

**Field Type**
boolean

**Description**
Indicates whether users can self-enroll in programs that are shared with them ( `true` )
or take only assigned programs ( `false` ). The default value is `false` .

**Field Type**
string

**Description**

Required. A user-friendly name for the program, which is defined when the program
is created.

**Field Type**
string

**Description**

Required. The name of the program that’s visible to users.

**Field Type**
string

**Description**
The Experience Cloud site where a program is published for partner users.

**Field Type**

EnablementProgramSection[]

**Description**
Groups of milestones and exercises within a program.


Metadata Types EnablementProgramDefinition

**Field Name** **Description**

```
tasks

type

```

**Field Type**

EnablementProgramTask[]

**Description**
The outcome, milestones, and exercises in the program.

**Field Type**
string

**Description**

Required. Indicates whether the program is for sales users in Lightning Experience
( `Enablement` ) or partner users in supported Experience Cloud sites
( `PtnrEnablement` ).

EnablementProgramSection

Represents a logical, trackable group of milestones and exercises within an Enablement program. When users take programs, they can
expand or collapse sections.

**Field Name** **Description**

```
developerName

name

sequenceNumber

tasks

```

**Field Type**
string

**Description**

Required. The unique programmatic name for the section.

**Field Type**
string

**Description**
Required. The title of the section that’s visible to users when they take the program.

**Field Type**
int

**Description**

Required. A number that specifies the order of the section, relative to other sections,
starting at 0.

**Field Type**

EnablementProgramTask[]

**Description**
The milestones and exercises in the section.


Metadata Types EnablementProgramDefinition

EnablementProgramTask

Represents an outcome, milestone, or exercise in an Enablement program. A program task is also known as a program item.

**Field Name** **Description**

```
customSubCategoryName

day

description

developerName

exercise

milestone

```

**Field Type**
string

**Description**

The API name of custom exercise task subcategory. This value determines the type of
the custom exercise and its associated content. Available in API version 63.0 and later.

**Field Type**
int

**Description**

Required. The day of the program when the item is due, relative to the program's start
date. For example, if a user is expected to complete an exercise where they watch a
product demo by day 2, this field’s value is 2. For an outcome, this field specifies the
number of days the full program takes. For example, if your program lasts 60 days, the
value of this field is 60 for the outcome. This field’s value contributes to the program’s
due date that users see when they take the program.

**Field Type**
string

**Description**

Required. A summary of the outcome, milestone, or exercise that’s visible to users
when they take the program.

**Field Type**
string

**Description**

Required. The unique programmatic name for the outcome, milestone, or exercise.

**Field Type**

EnablementProgramTaskExercise

**Description**
The content used with an exercise.

If `taskSubCategory` is `ActionItem`, this field isn’t included when retrieving
metadata.

**Field Type**

EnablementProgramTaskMilestone


Metadata Types EnablementProgramDefinition

**Field Name** **Description**

**Description**
The definition of an outcome or milestone, including the Enablement measures used
and the criteria for completing the goal.

```
name

sequenceNumber

taskCategory

taskSubCategory

```

**Field Type**
string

**Description**

Required. The title of the outcome, milestone, or exercise that’s visible to users when
they take the program.

**Field Type**
int

**Description**

Required. A number that specifies the order of the milestone or exercise, relative to
other milestones or exercises that have the same due date in the program or in the
same section, starting at 0. This number determines the order of items that users see
for that day in the program.

**Field Type**
ProgramTaskDefCategory (enumeration of type string)

**Description**

Required. The type of the program item.

Values are:

**•** `Exercise`

**•** `Milestone`

`Milestone` is used for both the program’s outcome and incremental milestones.

**Field Type**
string

**Description**

Required. The type of exercise. This value determines the content associated with the
exercise. For example, if the field value is `Video`, the exercise must reference video
content from the Enablement workspace in the Digital Experiences app. Possible values
are:

**•** `ActionItem`

**•** `AudioRecording`

**•** `CustomExercise` —Available in API version 62.0 and later.

**•** `Document`

**•** `FeedbackRequest`

**•** `Other`


Metadata Types EnablementProgramDefinition

**Field Name** **Description**

**•** `OtherExercise`

**•** `ScheduledEvent`

**•** `TextLesson`

**•** `Trailhead`

**•** `Video`

When `taskCategory` is `Milestone`, the value of `taskSubCategory` must
be `Other` .

EnablementProgramTaskExercise

Represents the content used with an exercise in an Enablement program.

**Field Name** **Description**

```
cmsContent

customContent

externalContent

feedbackContent

```

**Field Type**

EnablementProgramTaskCmsContent

**Description**

The definition of content managed in the Enablement workspace in the Digital
Experiences app when `taskSubCategory` on EnablementProgramTask is
`AudioRecording`, `Document`, `OtherExercise`, `ScheduledEvent`,
`TextLesson`, or `Video` .

**Field Type**

EnablementProgramTaskCustomContent

**Description**

The definition of content used with a custom exercise type when
`taskSubCategory` on EnablementProgramTask is `CustomExercise` .

**Field Type**

EnablementProgramTaskExternalContent

**Description**
The definition of Trailhead content when `taskSubCategory` on
EnablementProgramTask is `Trailhead` .

**Field Type**

EnablementProgramTaskFeedbackContent

**Description**
The definition of an assessment survey or Einstein prompt template when
`taskSubCategory` on EnablementProgramTask is `FeedbackRequest` .


Metadata Types EnablementProgramDefinition

EnablementProgramTaskCmsContent

Defines content managed in the Enablement workspace in the Digital Experiences app for the Audio Recording, Document, Other,
Scheduled Event, Text Lesson, or Video exercise types.

**Field Name** **Description**

```
apiName

contentKey

```

**Field Type**
string

**Description**

Required in API version 62.0. The unique programmatic ID of the Digital Experiences
content for the exercise. This string’s format is
_**`workspaceType`**_ `/` _**`workspaceApiName`**_ `.` _**`contentFQN`**_ `/` _**`contentApiName`**_,
which matches the `fullName` field value on the corresponding DigitalExperience
metadata type.

For example, a Link content record from the Enablement workspace has this API name:
`enablement/sfdcEnablement_EnablementWorkspace.sfdc_enablement__link/link_API_name` .

**Field Type**
string

**Description**

Required in API version 61.0 only.

EnablementProgramTaskCustomContent

Defines content used with a custom exercise type.

**Field Name** **Description**

```
content

```

**Field Type**
string

**Description**

A serialized string returned by the Apex class that’s specified in the corresponding
LearningItemType metadata type’s `apexSerializerDeserializer` field. This
string identifies the content used with the custom exercise type so the custom exercise
can be recreated in the destination org. This string:

**•** Can’t exceed 250 characters

**•** Must contain only alphanumeric characters

[For details, see Implement Custom Exercise Types for Enablement Programs in the](https://developer.salesforce.com/docs/sales/enablement/guide/enablement-custom-exercises-intro.html)
_Sales Programs and Partner Tracks with Enablement Developer Guide_ .


Metadata Types EnablementProgramDefinition

EnablementProgramTaskExternalContent

Defines Trailhead content for the Trailhead exercise type.

**Field Name** **Description**

```
externalId

providerType

```

**Field Type**
string

**Description**

Required. The API name of the Trailhead module used with the exercise.

**Field Type**
ProgramExtContentDefProvider (enumeration of type string)

**Description**

Required. The supported external content platform or system.

Values are:

**•** `Trailhead`

EnablementProgramTaskFeedbackContent

Defines the assessment survey or Einstein prompt template for the Feedback Request exercise type.

**Field Name** **Description**

```
inviteeCount

promptTemplate

surveyDeveloperName

```

**Field Type**
int

**Description**
The number of peers or managers that the user is required to invite for giving feedback
when `type` is `PeerFeedback` . Each peer or manager receives an invitation to the
assessment survey associated with the Feedback Request exercise.

When `type` is `AIFeedback`, this value is always `1` .

**Field Type**
string

**Description**
The prompt template to use with this exercise when `type` is `AIFeedback` .

**Field Type**
string

**Description**
The unique programmatic name for the assessment survey that’s sent to peers and
managers when `type` is `PeerFeedback` .


Metadata Types EnablementProgramDefinition

**Field Name** **Description**

```
type

```

**Field Type**
string

**Description**

Required. The type of feedback used with the exercise.

Values are:

**•** `AIFeedback` —Users submit a video call, and Einstein generates feedback from
the call’s transcription. With this type, `promptTemplate` is required.

**•** `PeerFeedback` —Users submit a URL to a sample of their work, and select
peers and managers to review their work. Selected peers and managers complete
an assessment survey. With this type, `surveyId` is required.

EnablementProgramTaskMilestone

Defines the requirements for an outcome or milestone, including the Enablement measures used for tracking activity and the criteria
for completing the outcome or milestone.

**Field Name** **Description**

```
compositeMilestoneType

isMilestoneAnOutcome

milestoneMeasures

milestoneTarget

```

**Field Type**
EnblCompositeMilestoneType (enumeration of type string)

**Description**
The type of logic to use for evaluating the activity from two Enablement measures in
a composite milestone.

Values are:

**•** `Addition`

**•** `Division`

**•** `Percentage`

**Field Type**
boolean

**Description**

Required. Indicates whether the program item is the program’s outcome ( `true` ) or
an incremental milestone ( `false` ).

**Field Type**

EnablementProgramTaskMilestoneMeasure[]

**Description**
The Enablement measures used with the outcome or milestone.

**Field Type**
double


Metadata Types EnablementProgramDefinition

**Field Name** **Description**

**Description**
The target value for a user to achieve to get credit for completing the outcome or
milestone. The unit depends on the specific measure used with the outcome or
milestone. For example, if the measure is the dollar amount of all closed opportunities,
then the field value is measured in dollars.

```
minimumSampleSize

```

**Field Type**
int

**Description**
The number of records to evaluate when calculating progress for an outcome or
milestone that uses an average-based measure. Use this field with
`milestoneTarget` . For example, if you want users to achieve an average deal
size of $50,000 after closing 4 deals, then this field’s value is `4` and
`milestoneTarget` is `50000` .

EnablementProgramTaskMilestoneMeasure

Defines the Enablement measure used with an outcome or milestone.

**Field Name** **Description**

```
measureDefinitionDeveloperName

sequenceNumber

```

**Field Type**
string

**Description**
The unique programmatic name of the Enablement measure used with the outcome
or milestone.

**Field Type**
int

**Description**
A number that specifies the order of the Enablement measure when multiple measures
are used with one outcome or milestone, starting at 0. For example, in a composite
milestone that uses the Percentage function, the measure that provides the numerator
value is sequence 0 and the measure that provides the denominator value is sequence
1.

Declarative Metadata Sample Definition

The following is an example of an EnablementProgramDefinition component.

```
<?xml version="1.0" encoding="UTF-8"?>

<EnablementProgramDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

   <description>Get started with sales at Cloud Kicks and close your first

```


Metadata Types EnablementProgramDefinition

```
   deal!</description>

      <developerName>Get_Started_Close_First_Deal_Program</developerName>

      <doesAllowSelfEnrollment>false</doesAllowSelfEnrollment>

      <masterLabel>Welcome to Sales at Cloud Kicks</masterLabel>

      <name>Welcome to Sales at Cloud Kicks</name>

      <sections>

        <developerName>section_0</developerName>

        <name>Learn the Ropes in Your First Week</name>

        <sequenceNumber>0</sequenceNumber>

        <tasks>

           <day>1</day>

           <description>Learn the basics of sales at Cloud Kicks.</description>

           <developerName>task_0</developerName>

           <exercise>

             <externalContent>

               <externalId>sales-rep-training</externalId>

               <providerType>Trailhead</providerType>

             </externalContent>

           </exercise>

           <name>Sales Rep Training</name>

           <sequenceNumber>0</sequenceNumber>

           <taskCategory>Exercise</taskCategory>

           <taskSubCategory>Trailhead</taskSubCategory>

        </tasks>

        <tasks>

           <day>2</day>

           <description>Watch our CEO explain the company vision.</description>

           <developerName>task_1</developerName>

           <exercise>

             <cmsContent>

   <apiName>enablement/sfdcEnablement_EnablementWorkspace.sfdc_enablement__link/company_vision_video</apiName>

             </cmsContent>

           </exercise>

           <name>See Our Company Vision</name>

           <sequenceNumber>1</sequenceNumber>

           <taskCategory>Exercise</taskCategory>

           <taskSubCategory>Video</taskSubCategory>

        </tasks>

        <tasks>

           <day>3</day>

           <description>Action Item</description>

           <developerName>task_2</developerName>

           <name>Action Item</name>

           <sequenceNumber>2</sequenceNumber>

           <taskCategory>Exercise</taskCategory>

           <taskSubCategory>ActionItem</taskSubCategory>

        </tasks>

        <tasks>

           <day>4</day>

           <description>Try out your first sales patch at Cloud Kicks and get feedback

   from our in-house experts.</description>

           <developerName>task_3</developerName>

```


Metadata Types EnablementProgramDefinition

```
           <exercise>

             <feedbackContent>

             <inviteeCount>1</inviteeCount>

             <surveyDeveloperName>discovery_call_assessment</surveyDeveloperName>

           </feedbackContent>

           </exercise>

           <name>Feedback from Peers and Managers</name>

           <sequenceNumber>3</sequenceNumber>

           <taskCategory>Exercise</taskCategory>

           <taskSubCategory>FeedbackRequest</taskSubCategory>

        </tasks>

        <tasks>

           <day>5</day>

           <description>Complete a discovery calls by day 5.</description>

           <developerName>task_4</developerName>

           <isMilestoneAnOutcome>false</isMilestoneAnOutcome>

           <milestone>

             <milestoneMeasures>

   <measureDefinitionDeveloperName>salesforceTemplate_CallsEmails</measureDefinitionDeveloperName>

             </milestoneMeasures>

             <milestoneTarget>1.0</milestoneTarget>

           </milestone>

           <name>Log a Discovery Call by Day 5</name>

           <sequenceNumber>4</sequenceNumber>

           <taskCategory>Milestone</taskCategory>

           <taskSubCategory>Other</taskSubCategory>

        </tasks>

        <tasks>

           <day>6</day>

           <description>Browse our sales leaders blog for more insights.</description>

           <developerName>task_5</developerName>

           <exercise>

             <cmsContent>

   <apiName>enablement/sfdcEnablement_EnablementWorkspace.sfdc_enablement__link/sales_blog</apiName>

             </cmsContent>

           </exercise>

           <name>Review Tips from Sales Leaders</name>

           <sequenceNumber>5</sequenceNumber>

           <taskCategory>Exercise</taskCategory>

           <taskSubCategory>OtherExercise</taskSubCategory>

        </tasks>

        <tasks>

           <day>7</day>

          <description>Follow a screen flow for onboarding to the sales team.</description>

           <developerName>task_6</developerName>

           <exercise>

             <customContent>

               <content>flowDeveloperName=OnboardingFlow</content>

             </customContent>

```


### Metadata Types EnblProgramTaskSubCategory

```
           </exercise>

           <name>Onboarding Flow</name>

           <sequenceNumber>6</sequenceNumber>

           <taskCategory>Exercise</taskCategory>

           <taskSubCategory>CustomExercise</taskSubCategory>

           <customSubCategoryName>ScreenFlowTaskSubCategory</customSubCategoryName>

        </tasks>

      </sections>

      <tasks>

        <day>30</day>

        <description>Close your first opportunity. To make sure it's counted, set the

   opportunity Stage field to Closed Won.</description>

        <developerName>task_enablementProgramOutcomeCard</developerName>

        <isMilestoneAnOutcome>true</isMilestoneAnOutcome>

        <milestone>

           <milestoneMeasures>

   <measureDefinitionDeveloperName>measure_CloseFirstDeal</measureDefinitionDeveloperName>

           </milestoneMeasures>

           <milestoneTarget>1.0</milestoneTarget>

        </milestone>

        <name>outcome</name>

        <sequenceNumber>0</sequenceNumber>

        <taskCategory>Milestone</taskCategory>

        <taskSubCategory>Other</taskSubCategory>

      </tasks>

      <type>Enablement</type>

   </EnablementProgramDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Get_Started_Close_First_Deal_Program</members>

        <name>EnablementProgramDefinition</name>

      </types>

      <version>61.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### EnblProgramTaskSubCategory

Represents a custom exercise type that an Enablement admin adds to an Enablement program in Program Builder. A custom exercise
type also requires a corresponding EnblProgramTaskDefinition record for Program Builder and corresponding LearningItem and
LearningItemType records for when users take the exercise in the Guidance Center.


Metadata Types EnblProgramTaskSubCategory

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

EnblProgramTaskSubCategory components have the suffix `.enblProgramTaskSubCategory` and are stored in the
`enblProgramTaskSubCategories` folder.

Version

EnblProgramTaskSubCategory components are available in API version 62.0 and later.

Special Access Rules

**•** For Enablement admins to create, update, and delete Enablement programs, the Design and Deliver Enablement Programs permission
is required. This permission is enabled by default as part of the Manage Enablement Essentials permission set, which comes with
the Enablement add-on license.

**•** For users who take Enablement programs, the Take Enablement Programs permission is required. This permission is enabled by
default as part of the Use Enablement Programs permission set, which comes with the Enablement add-on license.

Important: Custom exercises aren’t compatible with Partner Enablement programs.

Fields

**Field Name** **Description**

```
developerName

icon

```

**Field Type**
string

**Description**

Required. The unique programmatic name for the EnblProgramTaskSubCategory
record.

**Field Type**
string

**Description**
Required. The icon to use for the custom exercise type in Program Builder.

Use the format _**`iconType`**_ `:` _**`iconName`**_, where the values correspond to icon
[categories and names from the Salesforce Lightning Design System.](https://www.lightningdesignsystem.com/icons/)

**•** _**`iconType`**_ is the type of icon, such as `standard` or `doctype` .

**•** _**`iconName`**_ is the icon name, such as `flow` or `slide` .


Metadata Types EnblProgramTaskSubCategory

**Field Name** **Description**

For example, to use the Standard type Flow icon, this value is `standard:flow` .
[For details, see Implement Custom Exercise Types for Enablement Programs in the](https://developer.salesforce.com/docs/sales/enablement/guide/enablement-custom-exercises-intro.html)
_Sales Programs and Partner Tracks with Enablement Developer Guide_ .

```
learningItemType

masterLabel

```

**Field Type**
string

**Description**

[Required. The programmatic name of the LearningItemType record that represents](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_learningitemtype.htm)
this custom exercise type in the Guidance Center when users take a program.

**Field Type**
string

**Description**

Required. A user-friendly name for the EnblProgramTaskSubCategory, which is defined
when it’s created.

Declarative Metadata Sample Definition

The following is an example of an EnblProgramTaskSubCategory component for a custom exercise type that shows a screen flow.

```
<?xml version="1.0" encoding="UTF-8"?>

<EnblProgramTaskSubCategory xmlns="http://soap.sforce.com/2006/04/metadata">

   <developerName>ScreenFlowTaskSubCategory</developerName>

   <icon>standard:flow</icon>

   <learningItemType>ScreenFlowLearningItemType</learningItemType>

   <masterLabel>Screen Flow Exercise</masterLabel>

</EnblProgramTaskSubCategory>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>ScreenFlowTaskSubCategory</members>

     <name>EnblProgramTaskSubCategory</name>

   </types>

   <version>62.0</version>

</Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types EntitlementProcess EntitlementProcess

Represents the settings for an entitlement process.

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

Entitlement process values are stored in files in the `entitlementProcesses` directory. Each file has the name of a process and
the suffix `.entitlementProcess` . Each file contains one entitlement process or, if entitlement versioning is enabled, one version
of an entitlement process.

The name of the file is the name of the entitlement process with the version appended to the end, if applicable (for example, an entitlement
process named “gold_support” can have the file name “gold_support_v2.entitlementProcess”). This file name corresponds to the
`slaProcess.NameNorm` field exposed through SOAP API. This file name is distinct from the `name` field, which represents what
displays in the user interface and, if versioning is enabled, can be shared among multiple versions of the same entitlement process. The
`slaProcess.NameNorm` field contains the lowercase version of the `name` field shown in the user interface.

Version

Entitlement processes are available in API version 27.0 and later.

Fields

**Field Name** **Field Type** **Description**

`active` boolean Indicates whether the entitlement process is active
( `true` ) or not ( `false` ).

`businessHours` string

The business hours that apply to the entitlement process.

This field is available in API version 30.0 and later.

`description` string The description of the entitlement process.

`entryStartDateField` string

`exitCriteriaBooleanFilter` string

For milestone processes on which a case enters the
process based on a custom date/time field on the case,
specifies which date and time are used. Valid values are:

**•** SlaStartDate (entitlement process start date)

**•** CreatedDate (date case was opened)

**•** ClosedDate (date case was closed)

**•** LastModifiedDate (date case was last modified)

**•** StopStartDate (date case was stopped)

For milestone processes on which a case exits the process
when custom criteria are met, and for which filter logic
is added, specifies that logic.


Metadata Types EntitlementProcess

**Field Name** **Field Type** **Description**

`exitCriteriaFilterItems` FilterItem[] For milestone processes on which a case exits the process
when custom criteria are met, specifies those criteria.

`exitCriteriaFormula` string

`isVersionDefault` boolean

For milestone processes on which a case exits the process
when a custom formula evaluates to true, specifies that
formula.

Indicates whether the entitlement process is the default
version ( `true` ) or not ( `false` ).

This field is available in API version 28.0 and later.

`milestones` EntitlementProcessMilestoneItem[] Represents a milestone on the entitlement process.

`name` string The name of the entitlement process as it displays in the
user interface.

`SObjectType` string Indicates the type of record that the entitlement process
can run on.

`versionMaster` string Identifies the sequence of versions to which this
entitlement process belongs. This field’s contents can be

any value as long as it’s identical among all versions of
the entitlement process.

This field is available in API version 28.0 and later.

`versionNotes` string

`versionNumber` int

EntitlementProcessMilestoneItem

Represents a milestone item on an entitlement process.

Fields

The description of the entitlement process version.

This field is available in API version 28.0 and later.

The version number of the entitlement process. Must be
1 or greater.

This field is available in API version 28.0 and later.

**Field Name** **Field Type** **Description**

`businessHours` string

The business hours that apply to the milestone.

This field is available in API version 30.0 and later.

`criteriaBooleanFilter` string For milestones that apply only when criteria are met
and for which filter logic is added, specifies that logic.


Metadata Types EntitlementProcess

**Field Name** **Field Type** **Description**

`milestoneCompletionCriteria` string

The criteria to be met for the milestone to be marked
complete.

`milestoneCriteriaFilterItems` FilterItem[] For milestones that apply only when criteria are met,
specifies those criteria.

`milestoneCriteriaFormula` string For milestones that apply only when a formula
evaluates to true, specifies that formula.

`milestoneName` string The name of the milestone.

`minutesCustomClass` string

The name of the Apex class that is used to calculate
the trigger time. This field is available in API version
30.0 and later.

`minutesToComplete` int The number of minutes from when the case enters the
entitlement process that the milestone occurs.

`successActions` WorkflowActionReference[] The actions triggered when the milestone is completed.

`timeTriggers` EntitlementProcessMilestoneTimeTrigger[] The time triggers on an entitlement process milestone.

`useCriteriaStartTime` boolean

EntitlementProcessMilestoneTimeTrigger

Represents the time trigger on an entitlement process milestone.

Fields

**Field Name** **Field Type** **Description**

When the milestone starts: when the milestone criteria
are met (true) or when the case enters the entitlement
process (false).

`actions` WorkflowActionReference[] The actions to take when the time trigger is reached, if, at that time,
the milestone isn’t completed.

`timeLength` int The length of time between the time trigger activation and the
milestone target completion date. This length of time can be a

negative or positive value. Negative values indicate that the target
completion date hasn’t yet arrived and correspond to warning time
triggers. Positive values indicate that the target completion date has
passed and correspond to violation time triggers.

```
workflowTimeTriggerUnit

```

MilestoneTimeUnits Specifies the type of unit used to determine when a workflow is
(enumeration of type triggered. Valid values are:
string)

**•** `Minutes`

**•** `Hours`

**•** `Days`


Metadata Types EntitlementProcess

Declarative Metadata Sample Definition

Here’s a sample entitlement process.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <EntitlementProcess xmlns="http://soap.sforce.com/2006/04/metadata">

      <active>true</active>

      <description>eppersone</description>

      <entryStartDateField>SlaStartDate</entryStartDateField>

      <exitCriteriaBooleanFilter>1 OR 2</exitCriteriaBooleanFilter>

      <exitCriteriaFilterItems>

        <field>Case.IsClosed</field>

        <operation>equals</operation>

        <value>true</value>

      </exitCriteriaFilterItems>

      <exitCriteriaFilterItems>

        <field>Case.Description</field>

        <operation>startsWith</operation>

        <value>foo</value>

      </exitCriteriaFilterItems>

      <milestones>

        <milestoneName>m1</milestoneName>

        <minutesToComplete>1</minutesToComplete>

        <successActions>

           <name>emailBob</name>

           <type>Alert</type>

        </successActions>

        <timeTriggers>

           <actions>

             <name>emailAlice</name>

             <type>Alert</type>

           </actions>

           <actions>

             <name>setEscalateToTrue</name>

             <type>FieldUpdate</type>

           </actions>

           <timeLength>1</timeLength>

           <workflowTimeTriggerUnit>Minutes</workflowTimeTriggerUnit>

        </timeTriggers>

        <timeTriggers>

           <actions>

             <name>setStopToTrue</name>

             <type>FieldUpdate</type>

           </actions>

           <timeLength>2</timeLength>

           <workflowTimeTriggerUnit>Minutes</workflowTimeTriggerUnit>

        </timeTriggers>

        <useCriteriaStartTime>false</useCriteriaStartTime>

      </milestones>

      <milestones>

        <milestoneCriteriaFilterItems>

           <field>Case.Priority</field>

           <operation>equals</operation>

           <value>High</value>

        </milestoneCriteriaFilterItems>

```


### Metadata Types EntitlementTemplate

```
        <milestoneName>m2</milestoneName>

        <minutesToComplete>120</minutesToComplete>

        <useCriteriaStartTime>true</useCriteriaStartTime>

        <successActions>

           <name>emailBob</name>

           <type>Alert</type>

        </successActions>

      </milestones>

   </EntitlementProcess>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### EntitlementTemplate

Represents an entitlement template. Entitlement templates are predefined terms of customer support that you can quickly add to
products. For example, you can create entitlement templates for Web or phone support so that users can easily add entitlements to
products offered to customers.

### EntitlementTemplate extends the Metadata metadata type and inherits its fullName field.

Declarative Metadata File Suffix and Directory Location

### EntitlementTemplate components are stored in the entitlementTemplates directory of the corresponding package directory.

The file name matches the unique name of the entitlement template, and the extension is `.entitlementTemplate` .

Version

Lightning Platform EntitlementTemplate components are available in API version 18.0 and higher.

Fields

**Field** **Field Type** **Description**

`businessHours` string The entitlement's supported business hours.

`casesPerEntitlement` int The total number of cases the entitlement supports.

`entitlementProcess` string The entitlement process associated with the entitlement.
Entitlement processes are timelines that include all the steps

(milestones) that your support team must complete to resolve
cases. Each process includes logic to determine how to enforce
the correct service level for your customers.

`isPerIncident` boolean `true` if entitlements created from this template service a
limited number of cases; `false` otherwise.


### Metadata Types EscalationRules

**Field** **Field Type** **Description**

`term` int The number of days the entitlement is in effect.

`type` string The type of entitlement, such as Web or phone support.

Declarative Metadata Sample Definition

A sample XML definition of an entitlement template is shown below.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <EntitlementTemplate xmlns="http://soap.sforce.com/2006/04/metadata">

      <businessHours>AlternateBusinessHours</businessHours>

      <casesPerEntitlement>12</casesPerEntitlement>

      <entitlementProcess>Process1</entitlementProcess>

      <isPerIncident>true</isPerIncident>

      <term>33</term>

      <type>Phone Support</type>

   </EntitlementTemplate>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### EscalationRules

Represents case escalation rules to escalate cases automatically if they aren’t resolved within a certain time. You can access rules metadata
for all applicable objects, for a specific object, or for a specific rule on a specific object.

The `package.xml` syntax for accessing all escalation rules for all objects is:

```
      <types>

        <members>*</members>

        <name>EscalationRules</name>

      </types>

```

All rules for a specific object use a similar syntax without the wildcard. For example, all escalation rules for the Case object would use
this syntax:

```
      <types>

        <members>Case</members>

        <name>EscalationRules</name>

      </types>

```

You can also access specific escalation rules for an object. The following example only accesses the “samplerule” and “newrule” escalation
### rules on the Case object. Notice that for this example the type name syntax is EscalationRule and not EscalationRules .

```
      <types>

        <members>Case.samplerule</members>

        <members>Case.newrule</members>

```


Metadata Types EscalationRules

```
        <name>EscalationRule</name>

      </types>

```

File Suffix and Directory Location

EscalationRules for an object have the suffix `.escalationRules` and are stored in the `escalationRules` folder. For example,
all Case escalation rules are stored in the `Case.escalationRules` file.

Version

EscalationRules components are available in API version 27.0 and later.

Fields

**Field Name** **Field Type** **Description**

`escalationRule` EscalationRule[] on
page 1060

EscalationRule

Represents one escalation rule and specifies whether it’s active or not.
Escalation rules are processed in the order they appear in the
EscalationRules container.

**Field Name** **Field Type** **Description**

`active` boolean Indicates whether the escalation rule is active ( `true` ) or
not ( `false` ).

`fullname` string Inherited from Metadata, this field is defined in the WSDL
for this metadata type. It must be specified when creating,

updating, or deleting. See `createMetadata()` to see
an example of this field specified for a call.

This value can't be `null` .

`ruleEntry` `RuleEntry[]` Contains the definitions of the rule entries in the escalation
rule.

RuleEntry

Represents the fields used by the rule.

**Field Name** **Field Type** **Description**

`booleanFilter` string Advanced filter conditions that were specified for the rule.

`businessHours` string The hours when escalation actions are performed. Specify
only if `businessHoursSource` is set to `Static` .


Metadata Types EscalationRules

**Field Name** **Field Type** **Description**

`businessHoursSource` BusinessHoursSourceType Valid values are:
(enumerations of type string)

**•** `None`

**•** `Case`

**•** `Static`

`criteriaItems` FilterItem The items in the list that define the assignment criteria.

`disableEscalationWhenModified` boolean Indicates whether the escalation is disabled when the
record is modified `true` ) or not ( `false` ).

`escalationAction` EscalationAction[] The actions to perform when the escalation criteria are met.

`escalationStartTime` EscalationStartTimeType Indicates the start time for the escalation. Valid values are:
(enumeration of type string)

**•** `CaseCreation`

**•** `CaseLastModified`

`formula` string

EscalationAction

Describes the action to take for an escalation rule.

The validation formula.

Specify either `formula` or `criteriaItems`, but not
both fields.

**Field Name** **Field Type** **Description**

`assignedTo` string The name of the user or queue the item is assigned to.

`assignedToTemplate` string

Specifies the template to use for the email that is
automatically sent to the new owner specified by the
escalation rule.

Lightning email templates aren’t packageable. We
recommend using a Classic email template.

`assignedToType` AssignToLookupValueType Valid values are:
(enumeration of type string)

**•** `User`

**•** `Queue`

`minutesToEscalation` int The number of minutes until the escalation occurs.

`notifyCaseOwner` boolean Indicates that the owner of the case is notified when the
case is escalated `true` ) or not ( `false` ).

`notifyEmail` string Specifies the email address of the user to notify.

`notifyTo` string Specifies the user to notify.


### Metadata Types EventDelivery

**Field Name** **Field Type** **Description**

`notifyToTemplate` string Specifies the template to user for the notification email.

Declarative Metadata Sample Definition

The following is an example EscalationRules component:

```
   <EscalationRules xmlns="http://soap.sforce.com/2006/04/metadata">

      <escalationRule>

        <fullName>samplerule</fullName>

        <active>false</active>

        <ruleEntry>

           <businessHours>test</businessHours>

           <businessHoursSource>Static</businessHoursSource>

           <criteriaItems>

             <field>Case.Description</field>

             <operation>contains</operation>

             <value>test</value>

           </criteriaItems>

           <escalationAction>

             <assignedTo>someuser@org.com</assignedTo>

             <assignedToTemplate>emailtemplatename</assignedToTemplate>

             <assignedToType>User</assignedToType>

             <minutesToEscalation>1440</minutesToEscalation>

             <notifyCaseOwner>false</notifyCaseOwner>

           </escalationAction>

           <escalationStartTime>CaseLastModified</escalationStartTime>

        </ruleEntry>

      </escalationRule>

   </EscalationRules>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### EventDelivery

Represents how an event instance maps to a target payload. Removed in API version 46.0. This type extends the Metadata metadata
type and inherits its `fullName` field.

File Suffix and Directory Location

Event delivery components have the suffix file path `.delivery`, and are stored in the `eventDeliveries` folder.

Version

Event delivery components are available in API versions 41.0 to 45.0.


Metadata Types EventDelivery

Limits

Your org can have a maximum of 2500 EventDelivery object instances.

Fields

**Field Name** **Field Type** **Description**

`eventParameters` EventParameterMap[] An array of parameters to deliver in addition to the published event’s data.

`eventSubscription` string Required. The ID of the subscription to deliver the data to.

`referenceData` string User-defined non-unique identifier.

Required. Determines what action occurs when the event is delivered to the listeners on
behalf of the subscribers.

Valid values are:

**•** `StartFlow` —When the event occurs, it’s delivered to a flow of type CustomEvent.
Those flows are built through Process Builder.

**•** `ResumeFlow` —Reserved for future use.

```
type

```

EventDeliveryType
(enumeration of type
string)

EventParameterMap

Parameters to deliver in addition to the published event’s data.

If `type` is `StartFlow`, you must include a parameter where `parameterName` is `FlowVersionName` and `parameterValue`
is the name of the flow that you want to start. The flow name must include its version number. For example, `myFlow-3` .

Each event delivery can have up to 10 parameters.

**Field Name** **Field Type** **Description**

`parameterName` string The parameter name.

`parameterValue` string The parameter value.

Declarative Metadata Sample Definition

The following is an example of an event delivery file.

```
<?xml version="1.0" encoding="UTF-8"?>

<EventDelivery xmlns="http://soap.sforce.com/2006/04/metadata">

  <eventParameters>

    <parameterName>FlowVersionName</parameterName>

    <parameterValue>My_Event_Based_Process-1</parameterValue>

  </eventParameters>

  <eventSubscription>MySubscription</eventSubscription>

  <referenceData>My_Event_Based_Process_1</referenceData>

  <type>StartFlow</type>

</EventDelivery>

```


### Metadata Types EventRelayConfig

The following is an example `package.xml` that deploys or retrieves all the available event delivery metadata in your org.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <types>

       <members>EventDelivery</members>

       <name>*</name>

     </types>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### EventRelayConfig

Represents the configuration of an event relay, which relays platform events and change data capture events from Salesforce to Amazon
EventBridge.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### EventRelayConfig components have the suffix .eventRelay and are stored in the eventRelays folder.

Version

### EventRelayConfig components are available in API version 56.0 and later.

Special Access Rules

**•** You must have the Customize Application permission to deploy and retrieve this type.

**•** You can update only the `state` and `relayOption` fields and not `eventChannel` or `destinationResourceName` .

Fields

**Field Name** **Description**

```
destinationResourceName

```

**Field Type**
string


Metadata Types EventRelayConfig

**Field Name** **Description**

**Description**
Required. The developer name of the named credential, which stores the AWS account
information. The `destinationResourceName` value contains the `callout:`
prefix. For example: `callout:MyRelayNamedCredential`

```
eventChannel

label

relayOption

state

```

**Field Type**
string

**Description**
Required. The full name of the event channel used in the event relay. For example:

```
  MyRelayChannel__chn

```

**Field Type**
string

**Description**
The label for the event relay. The label is displayed in the user interface. Make sure you
use a meaningful label that describes your event relay and try to make it unique.

**Field Type**
string

**Description**
A JSON-encoded string that contains an option for resuming an event relay after the
system recovers from an error. This option is used if the event relay can't resume after
the last relayed event. The options available are:

**•** `{\"ReplayRecovery\":\"LATEST\"}` —(Default) Start relaying events
from new events received in the event bus. Use this option if you aren’t interested
in missed events while the relay was down.

**•** `{\"ReplayRecovery\":\"EARLIEST\"}` —Resend all events stored in
the event bus and relay new events thereafter. The event bus stores events for up
to three days. Use this option if you want to reprocess all stored events and catch
up on missed events.

**Field Type**
EventRelayAdminState (enumeration of type string)

**Description**
The execution state of the event relay. Possible values are:

**•** `RUN` —The event relay is running and actively relaying event messages from
Salesforce to Amazon EventBridge.

**•** `PAUSE` —An administrator paused the event relay. No events are relayed to
Amazon EventBridge during this status. All current state information is saved.

**•** `STOP` —(Default) The event relay is stopped and no events are relayed to Amazon
EventBridge. All current state information is deleted.


### Metadata Types EventSubscription

**Field Name** **Description**

The event relay is created with a default state of `STOP` if you don't specify this
field. If you specify this field when creating an event relay, the only valid value you
can set is `STOP` .

**•** `DELETE` —Reserved for future use.

```
usageType

```

**Field Type**
string

**Description**
Reserved for future use.

Declarative Metadata Sample Definition

The following is an example of an EventRelayConfig component with the file name `Carbon_Comparison_Relay.eventRelay` .

```
<?xml version="1.0" encoding="UTF-8"?>

<EventRelayConfig xmlns="http://soap.sforce.com/2006/04/metadata">

   <destinationResourceName>callout:AWS_Account</destinationResourceName>

   <eventChannel>Carbon_Comparison_Channel__chn</eventChannel>

   <label>Carbon Comparison Relay</label>

   <relayOption>{\"ReplayRecovery\":\"LATEST\"}</relayOption>

   <state>STOP</state>

</EventRelayConfig>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>Carbon_Comparison_Relay</members>

     <name>EventRelayConfig</name>

   </types>

   <version>66.0</version>

</Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### EventSubscription

Represents a subscription to an event type. Removed in API version 46.0. This type extends the Metadata metadata type and inherits its
`fullName` field.


Metadata Types EventSubscription

File Suffix and Directory Location

EventSubscription components have the suffix file path `.subscription`, and are stored in the `eventSubscriptions` folder.

Version

Event subscription components are available in API versions 41.0 to 45.0.

Limits

Your org can have a maximum of:

**•** 4,000 total event subscriptions

**•** 2,000 active event subscriptions

Fields

**Field Name** **Field Type** **Description**

`active` boolean If the subscription isn’t active, it never receives any events.

`eventParameters` EventParameterMap[] An array of parameters that must be true for published events.

`eventType` string Required. The name of the platform event.

`referenceData` string Required. If the subscriber is a flow of type CustomEvent, `referenceData` is
_**`flowName`**_ `_` _**`versionNumber`**_ . For example, `Printer_Management_2` .

EventParameterMap

An array of parameters that must be true for published events. For example, subscribe to Vendor Response events only if `Status__c`
is `Shipped` .

Each event subscription can have up to 10 parameters.

**Field Name** **Field Type** **Description**

`parameterName` string Required. The published event’s field name.

`parameterValue` string The value that must be true.

Declarative Metadata Sample Definition

The following is an example of an active event subscription.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <EventSubscription xmlns="http://soap.sforce.com/2006/04/metadata">

      <active>true</active>

      <eventType>Printer_Status__e</eventType>

```


### Metadata Types ExperienceBundle

```
      <referenceData>Printer_Management</referenceData>

   </EventSubscription>

```

The following is an example of an inactive event subscription that sets event parameters.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <EventSubscription xmlns="http://soap.sforce.com/2006/04/metadata">

     <name>MySubscription</name>

     <active>false</active>

     <eventParameters>

       <parameterName>Ink_Status__c</parameterName>

       <parameterValue>low</parameterValue>

     </eventParameters>

     <eventParameters>

       <parameterName>Serial_Number__c</parameterName>

       <parameterValue>00123456789</parameterValue>

     </eventParameters>

     <eventType>Printer_Status__e</eventType>

     <referenceData>My_Event_Based_Process_1</referenceData>

   </EventSubscription>

```

The following is an example `package.xml` that deploys or retrieves all the available event subscription metadata in your org.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <types>

       <members>*</members>

       <name>EventSubscription</name>

     </types>

     <version>41.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### ExperienceBundle

Represents a text-based code structure of the settings and site components, such as pages, branding sets, and themes that make up an
Experience Builder site. Developers can quickly update and deploy Experience Builder sites _programmatically_ using their preferred
development tools. This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ExperienceBundle components have the suffix .json and are stored in the experiences folder when retrieved. Each Experience

Builder site in your org has its own folder. Each of these folders contains other folders for the supported properties.

The ExperienceBundle can contain one or more site definitions under the `experiences` folder. Each site definition has resource
folders for brandingSets, config, routes, themes, variations, and views, each with additional, related configuration information in JSON
files. Here’s an example site definition, showing the resource folders.


Metadata Types ExperienceBundle

Version

ExperienceBundle components are available in API version 46.0 and later.

Special Access Rules

To use the ExperienceBundle metadata type for Aura-based Experience Builder sites, from Setup, enter _`Digital Experiences`_
in the Quick Find box, and then select **Settings** . Select **Enable ExperienceBundle Metadata API**, and save your changes. LWR sites
use ExperienceBundle by default.

Fields

**Field Name** **Field Type** **Description**

`experienceResources` ExperienceResources[]

The list of resources in this ExperienceBundle. Each resource represents an
artifact of a site such as brandingSets, config, routes, themes, variations, and
views.

`label` string Required. Represents the name of the ExperienceBundle.

`type` SiteType (enumeration Required. Identifies the kind of site. Only Experience Builder sites are supported,
of type string) using the value `ChatterNetworkPicasso` .

`urlPathPrefix` string Specify a URL prefix for an Experience Builder site. For example, in the site URL
SitesSubdomainName.force.com/customers, customers is the UrlPathPrefix.

Note: For authenticated LWR sites created before Winter ’23 and Aura
sites, the URL path prefix ends in /s, and the part of the path without
the /s must match the Network metadata type’s URL. For
unauthenticated LWR sites and authenticated LWR sites created after


Metadata Types ExperienceBundle

**Field Name** **Field Type** **Description**

Winter ’23 through Experience Builder or Connect API, this path doesn’t
contain /s, and the path can be anything as long as there’s no conflict.

**Sample meta.xml file**

```
                          <?xml version="1.0" encoding="UTF-8"?>

                          <ExperienceBundle

                          xmlns="http://soap.sforce.com/2006/04/metadata">

                            <label>SampleStarterSite2</label>

                            <type>ChatterNetworkPicasso</type>

                          <urlPathPrefix>SampleStarterSite2/s</urlPathPrefix>

                          </ExperienceBundle>

```

ExperienceResources

Represents a list of sites in the bundle.

**Field Name** **Field Type** **Description**

`experienceResource` ExperienceResource[] The list of resources in this ExperienceBundle. Each resource represents a
property for the site, such as brandingSets, config, routes, themes, and views.

ExperienceResource

Represents specific site information included in the ExperienceBundle.

Each type has a folder in the structure. Each folder contains one or more files providing information about that type and the site. Each
corresponds to a specific folder and file in the ExperienceBundle.

**Field Name** **Field Type** **Description**

`fileName` string Required. Name of resource file.

`format` string Required. Only `JSON` is allowed.

`source` base64 The `JSON` content of each file.

`type` string Required. The type of the resource. Valid values are:

**•** `brandingSets`

**•** `config`

**•** `routes`

**•** `themes`

**•** `views`


Metadata Types ExperienceBundle

Folders and Bundled Definitions

Each ExperienceBundle includes folders and associated data that is contained in JSON files.

brandingSets Folder

This folder contains one JSON file per branding set, named _`brandingSets_name`_ `.json` . Each file has the same structure and
properties.

```
   <brandingSets_name> .json

```

**Property** **Type** **Description**

`brandingSetType` string Required in LWR sites. Not applicable for Aura sites. Represents whether the
color palette stored in the branding set is for the entire site or a specific section.

You can’t change one branding set type to another. Available in API Version
52.0 and later.

Valid values are:

**•** `APP` : The branding set applies to the entire site. There can be only one
branding set of this type.

**•** `SCOPED` : The branding set applies to a specific section.

`definitionName` string

Required. Represents the name for the branding set that is used in grouping
branding sets under a theme. Defined as _`theme`_ :branding- _`theme`_ .

For example, if the site theme is Stella, the `definitionName` would be
`stella:branding-stella` .

In addition, there are several standard templates that have unique naming:

**•** Customer Account Portal uses `cpt:branding-cpt`

**•** Customer Service uses `service:branding-service`

**•** Help Center uses `helpCenter:branding-helpCenter`

**•** Partner Central uses `prm:branding-prm`

**•** Build Your Own uses `starter:branding-starter`

Note: The combination of `definitionName` + `label` must be
unique in your org.

`id` UUID Represents the component’s GUID.

`label` string Represents the name of the branding set.

Note: The combination of `definitionName` + `label` must be
unique in your org.

`type` string Represents the component type. The only supported value is `brandingSet` .


Metadata Types ExperienceBundle

**Property** **Type** **Description**

`values` map Required. Represents a map of branding values that can be applied to a site.

```
   {

     "values" : {

      "HeaderBackgroundColor" : "#FFFFFF",

      "TextTransformStyle" : "none",

      "BorderColor" : "#D4D4D4",

      "DetailTextColor" : "#5A5A5A",

      "HeaderFonts" : "Ek Mukta",

      "CardBackgroundColor" : "rgba(255, 255, 255, 0)",

      "LoginBackgroundColor" : "#F4F4F4",

      "_ActionColorTrans" : "rgba(25, 124, 190, 0.9)",

      "LoginBackgroundImage" :

   "../../../../sfsites/picasso/core/external/salesforceIdentity/images/background.jpg?v=1",

      "PageBackgroundColor" : "#F5F7FA",

      "_HeaderTextColor" : "rgba(34,34,34,.8)",

      "_NavigationMenuHoverColor" : "rgba(255,255,255,.2)",

      "_HeaderInputBackgroundColor" : "rgba(255,255,255,.4)",

      "TextColor" : "#222222",

      "NavigationMenuTextColor" : "#222222",

      "_HeaderPlaceholderTextColor" : "rgba(85,85,85,.8)",

      "_OverlayTextColorShadow" : "#000000",

      "ActionColor" : "#0099DE",

      "CompanyLogo" : "",

      "_LinkColorDarker" : "#135F90",

      "_ActionColorDarker" : "#135F90",

      "_HoverColor" : "rgba(25, 124, 190, 0.05)",

      "ErrorFontColor" : "#ff9e9e",

      "OverlayTextColor" : "#FFFFFF",

      "PrimaryFont" : "Ek Mukta",

      "LinkColor" : "#3558D6"

      },

     "definitionName" : "cpt:branding-cpt",

     "label" : "Customer Account Portal",

     "id" : "283407c3-5938-4a6b-b97f-621cda6968c8",

     "type" : "brandingSet"

    }

```

config Folder

The `config` folder contains several JSON files.

**•** _`sitename`_ `.json`

**•** `languages.json`

**•** `nativeConfig.json`

**•** _`page_name`_ `.json`

Note: One for each single-page application in the site: `loginAppPage.json` and `mainAppPage.json`


Metadata Types ExperienceBundle

_`sitename`_ `.json` **File Properties**

**Property** **Type** **Description**

`authenticationType` string For LWR sites, indicates whether guest users have access to the site.

Note: For Aura sites, use `isAvailableToGuests` instead.

Valid values are:

**•** `AUTHENTICATED` : The site isn’t public. Only authenticated users can
access the site after logging in.

**•** `AUTHENTICATED_WITH_PUBLIC_ACCESS_ENABLED` : The site is
an authenticated site, but the **Public can access the site** checkbox is
enabled in Experience Builder in **Settings**                                   - **General** . Guest users can
access the site.

**•** `UNAUTHENTICATED` : The unauthenticated site is publicly available to
anyone on the web, and doesn’t support login or authentication. Guest
users can access the site. `UNAUTHENTICATED` isn’t supported for LWR
sites created after Winter ’23 through Experience Builder or Connect API.
To allow guest user access, we recommend using
`AUTHENTICATED_WITH_PUBLIC_ACCESS_ENABLED` .

Available in API version 51.0 and later.

`forgotPasswordRouteId` UUID Represents the ID of the route to use when a user forgets their password.

Note: Unsupported if the active Experience Builder template for the
site doesn't support login (such as Help Center).

`isAvailableToGuests` boolean For Aura sites, indicates whether public users have access to the site ( `true` )
or not ( `false` ). The default value is `false` .

Note: For LWR sites, use `authenticationType` instead.

`isFilteredComponentsView` boolean Indicates whether the list of components is filtered based on the current page
type ( `true` ) or not ( `false` ). Some components require specific parameters

from the page and don't work unless you manually configure them. The default
value is `false` .

`isLockerServiceEnabled` boolean

Indicates whether Lightning Locker is enabled ( `true` ) or disabled ( `false` ).
The default value is `true` .

Available in API version 55.0 and later.

`isProgressiveRenderingEnabled` boolean Indicates whether the display order of page components is prioritized ( `true` )
or not ( `false` ). The default value is `false` .

`loginAppPageId` UUID Represents the ID of the login page. Unsupported if the active Experience
Builder template for the site doesn't support login (such as Help Center).

`mainAppPageId` UUID Required. Represents the ID of the main page.


Metadata Types ExperienceBundle

**Property** **Type** **Description**

`preferredDomain` string

`preferredDomainId` string

`selfRegistrationRouteId` UUID

Represents the name of the domain to use for indexing a site’s pages. Improves
search engine results.

Available in API version 48.0 and later.

Represents the domain to use for indexing a site’s pages. Improves search
engine results.

Removed in API version 48.0. Use `preferredDomain` instead.

Represents the ID of the login route to use for self-registration. Unsupported
if the active Experience Builder template for the site doesn't support login (such
as Help Center).

`type` string Represents the component type. The only supported value is `site` .

**trustedSitesForScript container**

When implemented, there’s one `trustedSitesForScript` container in _`sitename`_ `.json` .

**Property** **Type** **Description**

`id` UUID Represents the component's GUID.

`isActive` boolean Indicates if allowlisted item is active ( `true` ) and must be respected or inactive
( `false` ) and must not be treated as an allowlisted source. Default is `false` .

`trustedSiteName` string Name of the allowlisted source as it appears in the UI.

`trustedSiteUrl` string The fully qualified URL of the allowlisted source.

`type` string Represents the component type. The only supported value is
`trustedSitesForScripts` .

```
{

  "isAvailableToGuests" : false,

  "isFilteredComponentsView" : false,

  "mainAppPageId" : "df9907cb-6e68-4ca1-8bb2-51173ca5374e",

  "loginAppPageId" : "58e9939a-84b2-498d-bbc5-7a89d89087fa",

  "selfRegistrationRouteId" : "ad5c8bf1-297f-4ad3-b47c-0e35d85f10ef",

  "forgotPasswordRouteId" : "e3139f6f-44d8-4eec-be9d-3609ce063039",

  "isProgressiveRenderingEnabled" : false,

  "preferredDomain" : "none",

  "selfRegistrationRouteId" : "b8fe8ab1-f266-41e1-a63b-4791165f3c1d",

  "trustedSitesForScript" : [ {

   "id" : "92c489e2-0b7b-4a48-9c88-bef7e8fe6f1b",

   "isActive" : true,

   "trustedSiteName" : "test",

   "trustedSiteUrl" : "https://123.com",

   "type" : "trustedSitesForScripts"

  }, {

```


Metadata Types ExperienceBundle

```
      "id" : "92c489e2-0b7b-4a48-9c88-bef7e8fe6f1c",

      "isActive" : true,

      "trustedSiteName" : "test1",

      "trustedSiteUrl" : "https://1234.com",

      "type" : "trustedSitesForScripts"

     } ],

      "type" : "site"

   }

```

`languages.json` **File Properties**

**Property** **Type** **Description**

`defaultCode` string Required. Represents the base language code plus the country code where
used.

`defaultLabel` string Required. Defines the display label for the language.

`id` UUID Represents the component's GUID.

`type` string Represents the component type. The only supported value is
`languageContainer` .

There’s one section per supported language as a container in `languages.json`

**language container**

**Property** **Type** **Description**

`countryCode` string Represents the country code of the selected language. This string can be empty.
It applies only when the selected language has variations depending on the

country, like Arabic (Algeria) and Arabic (Bahrain). In this case, use
`countryCode` to distinguish between them.

For example: `{ languageCode" : "ar", "CountryCode" :`

```
                        "DZ", "Label" : "Arabic (Algeria) (DZ)",}, { "Code"

                        : "ar", "CountryCode" : "BH", "Label" : "Arabic

                        (Bahrain) (BH)",}

```

`fallbackLanguageId` UUID Represents the language to use when no content is available for the selected
language. For example, if a site visitor chooses **Japanese** from the language

selector, but there’s no content for that page in Japanese, then content is
displayed in the fallback language.

Only one level of fallback is allowed for LWR sites. Here are examples for an
LWR site where English is the default language, and Spanish, French, and Finnish
are available site languages.

**•** Not allowed: Spanish falls back to French, and French falls back to Finnish.
This configuration includes two levels of fallback.

**•** Allowed: Spanish falls back to French, and French falls back to English. This
configuration is allowed because English is the site’s default language.


Metadata Types ExperienceBundle

**Property** **Type** **Description**

**•** Allowed: Spanish falls back to French, and French has no fallback. This
configuration includes only one level of fallback.

`id` UUID Represents the component's GUID.

`isActive` boolean Indicates whether a language is available to site visitors in the language selector
( `true` ) or not ( `false` ). The default value is `true` .

`label` string

Defines the display label for a language. The display label appears in any
language selector components that you add to your site and in the language
selector in Experience Builder.

`languageCode` string Represents the language code for the selected language.

`type` string Represents the component type. The only supported value is `language` .

```
{

   "defaultCode" : "en_US",

   "defaultLabel" : "English (US)",

   "id" : "04597c83-0b9d-4f16-9f4d-4ec28bd553b4",

   "type" : "languageContainer",

   "languages" : [ {

     "languageCode" : "af",

     "countryCode" : "",

     "isActive" : true,

     "label" : "Afrikaans",

     "fallbackLanguageId" : "c6e7fe67-55e0-47b3-ad58-bf49539249f0",

     "id" : "22036d6f-11ce-4f7b-b7f0-f2c409f817ea",

     "type" : "language"

     }

   ]

 }

```

The page file represents single-page applications in the site. One file per page, named _`page_name`_ `.json` .

Note: Each Experience Builder site is actually a single-page application, which is a web app that loads a single `HTML` page.
Single-page applications use multiple views to update the page dynamically as the user interacts with it.

`nativeConfig.json` **File Properties**

**Property** **Type** **Description**

`showHamburgerMenu` boolean Required. Controls whether the hamburger menu is shown.

`mobilePublisherAppUpdateConfig` boolean

Required. Controls whether and which App Version Update message is shown.
To avoid service disruptions, users must be on the app version that supports
enhanced domains.

`id` UUID Represents the component's GUID.


Metadata Types ExperienceBundle

**Property** **Type** **Description**

`type` string Represents the component type. The only supported value is
`nativeConfig` .

```
   {

    "id": "a70a0e5e-0400-4531-94dc-8f587daa5946",

    "nativeMobileNavConfig": {

     "showBackButton": true,

     "showHamburgerMenuWithBackButton": false

    },

    "mobilePublisherAppUpdateConfig": {

     "enableAppUpdate" : true,

     "forceAppUpdate" : true,

     "minVersion" : {

        "ios" : {

          "version" : "10.0"

    },

        "android" : {

            "version" : "10.1"

    }

    }

    },

    "nativeTabMenu": {

     "branding": {

      "iconTintColorUnselected": "#C9C5C5",

      "barTintColor": "#FF00FF",

      "iconTintColor": "#555321"

     },

     "menuItems": [

      {

        "iconAsset": "icon_homepng",

        "targetUrl": "/"

      },

      {

        "name": "Test",

        "iconAsset": "icon_filespng",

        "targetUrl": "/files"

      }

     ]

    },

    "showNavMenu": true,

    "type": "nativeConfig"

   }

```

**nativeMobileNavConfig container**

A required container for the configuration for the Native Navigation Bar component.

**Property** **Type** **Description**

`showBackButton` boolean Controls whether the Back button is shown on iOS devices.


Metadata Types ExperienceBundle

**Property** **Type** **Description**

`showHamburgerMenuWithBackButton` boolean Controls whether the hamburger menu is shown, in addition to
the Back button, on iOS devices.

**mobilePublisherAppUpdateConfig container**

A required container for the configuration of the App Version Update message.

**Property** **Type** **Description**

`enableAppUpdate` boolean

`forceAppUpdate` boolean

`minVersion` string

**nativeTabMenu container**

Controls whether the App Version Update message is shown, to
encourage users to update by giving them a choice of whether
to do so.

Set the properties to `"enableAppUpdate" : true`, and

`"forceAppUpdate" : false` to show the message that
encourages your users to update.

If you don’t want to show an update message, for example if all
your users are on the correct version or your site uses a custom
domain, set the property to `"enableAppUpdate" :`
`false`, and don’t use the `forceAppUpdate` property.

Controls whether the App Version Update message to require
users to update is shown.

Set the properties to `"enableAppUpdate" : true`, and

`"forceAppUpdate" : true` to show the message that
requires your users to update.

Controls the iOS and Android Minimum App Versions. These
property values are currently hard coded to ensure that the app
versions supporting enhanced domains are used.

A required container for the configuration of the hamburger menu and Back button behavior.

**Property** **Type** **Description**

`branding` map Settings for the Native Navigation Bar component branding. Valid keys are:

**•** iconTintColorUnselected

**•** iconTintColor

**•** barTintColor

Supply a valid 6 digit hexadecimal as the value for all properties.

`menuItems` list Items which must be displayed in the Native Navigation Bar component.


Metadata Types ExperienceBundle

**menuItems container**

A container within the nativeTabMenu container that specifies the items displayed in the tab bar of the Native Navigation Bar component.

**Property** **Type** **Description**

`name` string Optional. The label of the tab bar menu item.

`targetUrl` string Required. The relative URL to which the tab bar menu item points.

`iconAsset` string Required. Name of the ContentAsset to use for the tab bar menu item.

_`page_name`_ `.json` **File Properties**

**Property** **Type** **Description**

`cmsSettings` map Settings for the CMS Connect header and footer. Valid values are:

**•** `headerName`

**•** `headerUrl`

**•** `headerPersonalization`

**•** `footerName`

**•** `footerUrl`

**•** `footerPersonalization`

Both source and target org must have the CMSConnect and CMSPersonalization
org perms enabled for settings to be retrieved.

`currentThemeId` UUID

`headMarkup` string

Required. Represents the UUID of the site's current theme. This field is available
for `mainAppPage.json` and `loginAppPage.json` (where
applicable).

Required. Allows the addition of custom markup to the site's main page

`<head>` tag. Similar to using **Experience Builder** - **Setting** - **Advanced** **Head Markup** [See Salesforce Help for markup guidance.](https://help.salesforce.com/articleView?id=community_builder_page_head.htm&type=5&language=en_US)

`id` UUID Required. Represents the component's GUID.

`isRelaxedCSPLevel` boolean

Controls the ability to run scripts and script access to third-party hosts. The
default is `false` . This field is available for `mainAppPage.json` and
`loginAppPage.json` (where applicable).

`label` string Required. Represents the name of the page.

`templateName` string Required. The unique developer name of the template. Allowed values include:

**•** CPT Community Template (which represents the Customer Account Portal
template)

**•** Help Center Template (which represents the Help Center template)

**•** microsite-template-marketing (which represents the Microsite (LWR)
template

**•** PRM Community Template (which represents the Partner Central template)


Metadata Types ExperienceBundle

**Property** **Type** **Description**

**•** Service Community Template (which represents the Customer Service
template)

**•** Starter Template (which represents the Build Your Own (Aura) template)

**•** talon-template-byo (which represents the Build Your Own (LWR) template)

**•** _`Custom_template_name`_ (which is the name of a customized
template that was exported as a Bolt Solution)

Alternatively, you can retrieve a list of allowed template name values using
[Connect REST API. See Experience Builder Templates in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/connect_resources_communities_templates.htm) _Connect REST API_
_Developer Guide_ .

`type` string Required. Represents the component type. The only supported value is
`appPage` .

```
   {

      "headMarkup" : null,

      "isRelaxedCSPLevel" : false,

      "templateName" : "Starter Template",

      "cmsSettings" : { },

      "currentThemeId" : "ff52089c-6ad9-4dd9-b5b5-251d4a117ce3",

      "label" : "main",

      "id" : "df9907cb-6e68-4ca1-8bb2-51173ca5374e",

      "type" : "appPage"

   }

```

routes Folder

The `routes` folder contains one JSON file per page, named _`<page_name>`_ `.json` .

```
   <page_name> .json

```

**Property** **Type** **Description**

`activeViewId` UUID

Required. Represents the default view of the route. Used when there are no
defined audiences or the user doesn’t match any audience.

Available in API version 48.0 and later.

`appPageId` UUID Required. Represents the single page application (SPA) page for the route. It
points to either `main.json` or `login.json` .

`configurationTags` string[] Required. Represents the configuration tags for the route. The only supported
value is `allow-in-static-site` . Available in API Version 51.0 and later.

Note: This is an internal property and must not be edited.

`devName` string[] Required. Represents the unique API name that’s defined when creating a new
route. Available in API version 59.0 and later.


Metadata Types ExperienceBundle

**Property** **Type** **Description**

`id` UUID Required. Represents the component GUID. Inherited from the component.

`label` string Required. Represents the name of the route. Inherited from the component.

`objectApiName` string Required. The name of the custom object API. (Not available for standard
objects.)

`pageAccess` string Required. Identifies the status of a route as public or private. When set to the
default value `UseParent`, the status of the site determines the status of the

route. Not editable from the user interface for routes that are always private.
Valid values are `UseParent`, `Public`, and `RequiresLogin` .

`routeType` string Required. Identifies the type of route. Value is unique among all routes that
share the same SPA page. The value in `viewType` must match.

`type` string Required. Represents the component type. The only supported value is `route` .

`urlPrefix` string Required. Represents the base URL for the route.

```
   {

      "urlPrefix" : "",

      "appPageId" : "b5fe94e2-071f-47b2-b76d-427a624cb407",

      “configurationTags” : “allow-in-static-site”

      "routeType" : "home",

      "pageAccess" : "UseParent",

      "label" : "Home",

      "id" : "c7263124-7bc4-4147-a39a-25fe7e305b98",

      "type" : "route"

   }

```

themes Folder

The `themes` folder contains one JSON file per theme named _`theme_name`_ `.json` .

```
   theme_name .json

```

**Property** **Type** **Description**

`activeBrandingSetId` UUID The id of the branding set currently in use. The branding set's
`definitionName` must match the theme's `brandingSetReference` .

`customCSS` string Custom CSS for pages created in the Experience Builder template.

`developerName` string

Required. The unique developer name of the theme. Most themes derive their
names directly, for example Jepson uses `jespon` for its `developerName` .

Standard templates have unique values:

**•** `cpt` for Customer Account Portal

**•** `service` for Customer Service

**•** `helpCenter` for Help Center


Metadata Types ExperienceBundle

**Property** **Type** **Description**

**•** `prm` for Partner Central

**•** `starter` for Build Your Own

`id` UUID Required. Represents the component's GUID.

`label` string Represents the name of the theme.

`layouts` map Required. Maps `ThemeLayoutType` to UUID, and contains the definition
of the ThemeLayout. Login and Inner theme layouts are always required.

`type` string Required. Represents the component type. The only supported value is `theme` .

```
   {

      "developerName" : "cpt",

      "layouts" : {

        "Login" : "12162c3e-06ac-43a9-adc7-db36ae5140b0",

        "Inner" : "c09d58be-0622-4fc4-806a-ed34174929f9"

      },

      "customCSS" : "",

      "activeBrandingSetId" : "283407c3-5938-4a6b-b97f-621cda6968c8",

      "label" : "Customer Account Portal",

      "id" : "ff52089c-6ad9-4dd9-b5b5-251d4a117ce3",

      "type" : "theme",

      "views" : [ {

        "componentName" : "salesforceIdentity:loginBody2",

        "label" : "Login",

        "id" : "12162c3e-06ac-43a9-adc7-db36ae5140b0",

        "type" : "view",

        "regions" : [ {

           "regionName" : "header",

           "id" : "f8354922-11f2-495d-9d89-0a51943af2b0",

           "type" : "region",

           "components" : [ ]

        } ]

      } ]

   }

```

Note: Views can be children of a theme. These children are structured the same as views in the views folder.

variations Folder

Experience variations let you change the default behavior of the Experience Builder site based on the audience. The `variations`
folder contains one JSON file per experience variation. The file is named _`experienceVariation_name`_ `.json` .

Note:

**•** Experience variations are available in API version 47.0 and later.

**•** The name of your JSON file must match the `developerName` of your variation to avoid issues when deploying a site more
than one time.


Metadata Types ExperienceBundle

Four distinct types of variations are supported: branding sets, page variations, component visibility, and component attributes. The
different variations are indicated through the `componentVariant` container.

For example, you want the site to show a page variation for the home page when a user meets certain audience criteria. To achieve this,
create an audience and then target that audience to your experience variation using `targetId` in the `componentVariant`
container of the experience variation definition file.

```
   experienceVariation_name .json

```

**Property** **Type** **Description**

`componentVariants` list Required. A list of component variants that belong to this experience variation.

Note: Only one component variant per experience variation is allowed.

`developerName` string

Required. The unique developer name of the experience variation. This name
is used in the `targetValue` field of a Personalization API target and can’t
be updated after it’s set.

Note: For more information, see Audience.

`id` UUID Required. Represents the GUID of the component.

`type` string Required. Represents the type of the component. The only supported value is
`experienceVariation` .

When implemented, there’s one container in each _`experienceVariation_name`_ `.json` file describing the variation.

**componentVariant container**

**Property** **Type** **Description**

`id` UUID Required. Represents the GUID of the component.

`propertyOverrides` map

Required. Defines the property overrides for the given theme, route, or
component `targetId` .

For example, if the `targetId` is pointing to a theme, you can override the
`defaultBrandingSet` property of the theme to use a different branding
set for this experience variation.

Supported property overrides:

```
activeBrandingSetId
```

Defines which branding set to use when `targetId` is a theme. Uses the
format:

```
  "activeBrandingSetId" : " ID_of_brandingset "

activeViewId
```

Defines which page variation to use when `targetId` is a route. Uses
the format:

```
  "activeViewId" : " ID_of_view "

```


Metadata Types ExperienceBundle

**Property** **Type** **Description**

```
                        componentAttributes
```

Supported only for CMS Collection components and navigation
components, such as Navigation Menu or Tile Menu. Components can be
placed in header and footer regions, and also in the view body.

**•** Defines which navigation linkset to display when `targetId` is a
navigation component.

The value of the property is a JSON container with a single key-value
pair denoting the attribute and the value of the attribute.

`NavigationMenuEditorRefresh` is the only supported
attribute. Uses the format:

```
                             "componentAttributes" : {

                               "NavigationMenuEditorRefresh" :

                             " linkset_name "

                             }

```

**•** Defines which content collection to display when `targetId` is a
CMS Collection component.

The value of the property is a JSON container with a single key-value
pair denoting the path to the attribute and the value of the attribute.

```
                           config/dataProviderDefinition/attributes/dataProviderInfo/apiName
```

is the only supported attribute. Uses the format:

```
                             "componentAttributes" : {

                               "config/dataProviderDefinition/attributes

                             /dataProviderInfo/apiName":" collection_name "

                             }

                        isVisible
```

Defines whether a component is visible for the audience when `targetId`
is a component. Unsupported for components in header or footer regions.
Uses the format:

```
                            "isVisible": boolean

```

Note:

**•** Only one entry in the map is allowed.

**•** For a component, you can vary either its visibility or attributes but
not both together.

`targetId` UUID Required. The UUID of the item whose properties you’re overriding. Must be
the ID of a theme, route, or component.

`type` string Required. Represents the type of the component. The only supported value is
`experienceVariation` .


Metadata Types ExperienceBundle

**Example of an experience variation for a branding set**

```
   {

     "id": "64e93604-78fa-11e9-8f9e-2a86e4085a59",

     "developerName": "BrandingVariation",

     "type": "experienceVariation",

     "componentVariants": [{

       "id": "4bf0af78-8d73-11e9-bc42-526af7764f64",

       "type": "componentVariant",

       // Theme UUID

       "targetId": "c810858e-78fa-11e9-8f9e-2a86e4085a59",

       "propertyOverrides": {

         // Brandingset UUID

         "activeBrandingSetId": "be9f4760-78fa-11e9-8f9e-2a86e4085a59"

       }

     }]

   }

```

**Example of an experience variation for a page variation**

```
   {

     "id": "64e93604-78fa-11e9-8f9e-2a86e4085a59",

     "developerName": "PageVariation",

     "type": "experienceVariation",

     "componentVariants": [{

       "id": "4bf0af78-8d73-11e9-bc42-526af7764f64",

       "type": "componentVariant",

       // Route UUID

       "targetId": "c810858e-78fa-11e9-8f9e-2a86e4085a59",

       "propertyOverrides": {

         // View UUID

         "activeViewId": "be9f4760-78fa-11e9-8f9e-2a86e4085a59"

       }

     }]

   }

```

**Example of an experience variation for component visibility**

```
   {

     "id": "64e93604-78fa-11e9-8f9e-2a86e4085a59",

     "developerName": "ComponentVisibilityVariation",

     "type": "experienceVariation",

     "componentVariants": [{

       "id": "4bf0af78-8d73-11e9-bc42-526af7764f64",

       "type": "componentVariant",

       // Component UUID

       "targetId": "c810858e-78fa-11e9-8f9e-2a86e4085a59",

       "propertyOverrides": {

         "isVisible": true

       }

     }]

   }

```


Metadata Types ExperienceBundle

**Example of a component variation for a CMS Collection component**

```
   {

     "id" : "6ce1260f-cb01-45a0-8947-f2d85602a3db"

     "developerName": "Home_CMS_Collection_Component_Properties",

     "type": "experienceVariation",

     "componentVariants": [{

       "id" : "3gh1260f-cb01-45a0-8947-f2d92037a4db"

       "type": "componentVariant",

       "targetId": "d77369e6-7230-43e7-9b59-6e91c47b3273",

       "propertyOverrides": {

         "componentAttributes": {

   "config/dataProviderDefinition/attributes/dataProviderInfo/apiName":"SilverCollection"

         }

       },

     }],

   }

```

**Example of a component variation for Navigation Menu component**

```
   {

     "id" : "8cf943b8-525d-4c13-a719-6ebc7d61a81e",

     "developerName" : "Default_Navigation_Menu_Component_Properties",

     "type" : "experienceVariation",

     "componentVariants" : [{

       "id" : "5be1260f-cb01-45a0-8947-f2d85602a4db",

       "type" : "componentVariant",

       "targetId" : "fdf9eb51-ddc5-4e79-9ea8-5b94f5ca8db4",

       "propertyOverrides" : {

         "componentAttributes" : {

           "NavigationMenuEditorRefresh" : "NavMenu1"

         }

       },

     }],

   }

```

views Folder

The `views` folder contains several JSON files that each define a view. Each Experience Builder site is built from single-page applications,
which are web apps that load a single HTML page. Single-page applications consist of multiple views that update the page dynamically
as the user interacts with it.

A _view_ is made up of _regions_ that contain other regions or _components_ in the rendered page for the user. Within the `views` folder
there’s one file per view, named _`view_name`_ `.json` .

Note: Single-page applications in your site are defined in the page files of the `config` folder.

```
   view_name .json

```

**Property** **Type** **Description**

`appPageId` UUID Required. Single page application (SPA) page ID of the view. It points to either
`main.json` or `login.json` .


Metadata Types ExperienceBundle

**Property** **Type** **Description**

`componentName` string

Required. The FQN of the layout component. The component must implement
`forceCommunity:layout` or, for theme layouts,

```
forceCommunity:themeLayout

```

`id` UUID Required. Represents the GUID of the component.

`label` string Required. The name that appears in **Experience Builder** - **Settings** **Theme**                   - **Configure** .

`themeLayoutType` string Theme layout type of the view (exposed only for views).

`type` string Required. Represents the type of the component. The only supported value is
`view` .

`viewType` string Required. Matches `routeType` for the route.

There are one or more regions as a container in each _`<view_name>`_ `.json`

**region container**

**Property** **Type** **Description**

`id` UUID Required. Represents the component GUID.

`regionLabel` string Specifies region labels for tabs.

Note: This property is present only for tab regions that are children of
a component.

`regionName` string Required. Matches the design attribute in the design file of the layout
component.

`type` string Required. Represents the component type. The only supported value is
`region` .

Each _`<view_name>`_ `.json` file contains a hidden region called `sfdcHiddenRegion` . The hidden region contains a component
that represents the SEO assistant component. In Aura sites, the component’s definition is `forceCommunity:seoAssistant`,
and in LWR sites, the component’s definition is `community_builder:seoAssistant` . This component corresponds to the
SEO page properties that you can configure in Experience Builder and isn’t visible on your pages. To improve search engine results, use
the SEO assistant component to set the `customHeadTags`, `description`, and `pageTitle` properties for your public and
custom site pages. You can’t edit the other properties associated with the SEO assistant component. To learn more about what the title,
[description, and custom head tags properties represent and which head tags are allowed, see SEO Page Properties in Experience Builder.](https://help.salesforce.com/s/articleView?id=experience.networks_seo_tags.htm&type=5&language=en_US)

There are one or more components as a container in the region section of each _`<view_name>`_ `.json`

**component container**

**Property** **Type** **Description**

`componentAttributes` HashMap Required. The design attribute values of the component.


Metadata Types ExperienceBundle

**Property** **Type** **Description**

`componentName` string Required. The FQN of the component. Only components that can be used in
the component panel in Experience Builder can be used in this field.

`id` UUID Required. Represents the component GUID.

Note: If you add a component to ExperienceBundle, you can enter any
value because the system automatically generates a UUID for the
component when deployed.

`renderPriority` enums.priority Sets priority value for progressive rendering of the component. Possible Values:
`HIGHEST`, `HIGH`, `NEUTRAL`

Note: Only evaluated if the site has progressive rendering turned on
in **Experience Builder**                                            - **Settings**                                            - **Advanced** .

`renditionMap` HashMap Map of different rendition keys to UUIDs of RenditionComponents.

`scopedBrandingSetID` UUID

Required for LWR sites. Not applicable for Aura sites. Represents the ID of a
branding set for a specific `community_layout:section` component.
Available in API Version 52.0 and later.

`type` string Required. Represents the component type. The only supported value is
`component` .

Each component can have a rendition container in each _`<view_name>`_ `.json`

**rendition container**

**Property** **Type** **Description**

`id` UUID Required. Represents the component GUID.

`renditionValue` map Map of different variations of a component, such as different languages of text.

`type` string Required. Represents the component type. The only supported value is
`renditionComponent` .

```
{

   "themeLayoutType" : "Inner",

   "viewType" : "account-management",

   "appPageId" : "df9907cb-6e68-4ca1-8bb2-51173ca5374e",

   "componentName" : "siteforce:sldsOneColLayout",

   "label" : "Account Management",

   "id" : "9ca8fa47-8e87-4915-a6f7-c2d8d37f3076",

   "type" : "view",

   "regions" : [ {

      "regionName" : "content",

      "id" : "969ada98-7d72-4e45-8a10-7db51fae247c",

      "type" : "region",

      "components" : [ {

```


Metadata Types ExperienceBundle

```
           "componentName" : "forceCommunity:tabset",

           "componentAttributes" : {

             "tabsetConfig" :

   "{\"UUID\":\"4711850e-ffdc-4375-a45e-f716bcdbbb1c\",\"activeTab\":\"tab1\",

   \"useOverflowMenu\":false,\"tabs\":[{\"UUID\":\"bc8fb51f-4783-43d4-9376-60c07677a367\",\"tabName\":\"Members\",

   \"tabKey\":\"tab1\",\"locked\":false,\"allowGuestUser\":false,\"seedComponents\":[{\"fqn\":\"forceCommunity:relatedList\",

   \"attributes\":{\"parentRecordId\":\"{!CurrentUser.accountId}\",\"relatedListName\":\"Users\",\"customTitle\":\"Members\",

   \"showCustomTitle\":\"true\",\"showBreadCrumbs\":\"false\",\"showRowNumbers\":\"false\",\"showManualRefreshButton\":\"false\"}}]},

   {\"UUID\":\"f2793a99-b757-4be4-846f-dc98a13a8139\",\"tabName\":\"Branding\",\"tabKey\":\"tab2\",\"locked\":false,

   \"allowGuestUser\":false,\"seedComponents\":[{\"fqn\":\"forceCommunity:accountBrandRecord\",

             \"attributes\":{\"recordId\":\"{!CurrentUser.accountId}\"}}]}]}",

             "regions" : ""

           },

           "renderPriority" : "NEUTRAL",

           "renditionMap" : { },

           "id" : "4711850e-ffdc-4375-a45e-f716bcdbbb1c",

           "type" : "component",

           "renditions" : [ {

            "renditionValue" : {

              "LumenInstanceAttributes" : {

              "richTextValue" : "<p>new text</p>"

              }

            },

            "id" : "9d8878df-f520-4010-861c-57b930a3daab",

            "type" : "renditionComponent"

           } ]

        } ]

      } ]

   }

```

Declarative Metadata Sample Definition

Here’s an example of an ExperienceBundle declaration. For individual folder and file examples for the bundled code, see brandingSets,
config, routes, themes, variations, and views.

```
   <xsd:complexType name="ExperienceBundle">

      <xsd:complexContent>

        <xsd:extension base="tns:Metadata">

           <xsd:sequence>

             <xsd:element name="experienceResources" minOccurs="0"

   type="tns:ExperienceResources"/>

```


### Metadata Types ExperiencePropertyTypeBundle (Beta)

```
             <xsd:element name="label" type="xsd:string"/>

             <xsd:element name="type" type="tns:SiteType"/>

           </xsd:sequence>

        </xsd:extension>

      </xsd:complexContent>

   </xsd:complexType>

      <xsd:complexType name="ExperienceResources">

        <xsd:sequence>

           <xsd:element name="experienceResource" minOccurs="0" maxOccurs="unbounded"

   type="tns:ExperienceResource"/>

        </xsd:sequence>

      </xsd:complexType>

   <xsd:complexType name="ExperienceResource">

      <xsd:sequence>

        <xsd:element name="fileName" type="xsd:string"/>

        <xsd:element name="format" type="xsd:string"/>

        <xsd:element name="source" minOccurs="0" type="xsd:base64Binary"/>

        <xsd:element name="type" type="xsd:string"/>

      </xsd:sequence>

   </xsd:complexType>

```

Usage

Tip: Before you update the .json files of an Experience Builder site, we recommend making a copy of the site’s folder as a backup.

When you add a component to ExperienceBundle, you can enter any value for the `id`, because the system automatically generates a
UUID for the component when deployed.

When deploying an Experience Builder site with ExperienceBundle, ensure that the SiteDotCom type isn’t included in the manifest file.

ExperienceBundle doesn’t support retrieving and deploying across different API versions. If you’re trying to upgrade ExperienceBundle
metadata from an earlier API version to a later one—for example, from API version 48.0 to 49.0—take the following steps:

**1.** Set the API version in the package.xml manifest file to 48.0 and deploy the package.

**2.** Then, set the API version in package.xml to 49.0.

**3.** To get the latest ExperienceBundle updates, retrieve the package.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

ExperienceBundleSettings

_Developer Guide:_ [ExperienceBundle for Experience Builder Sites](https://developer.salesforce.com/docs/atlas.en-us.262.0.communities_dev.meta/communities_dev/communities_dev_migrate_expbundle.htm)

### ExperiencePropertyTypeBundle (Beta)

Represents a property type. Replaced in Spring ’26 by the updated LightningPropertyType. When you create a custom property type for
a Lightning web component, use LightningPropertyType instead, and deploy that bundle to your org.


Metadata Types ExperiencePropertyTypeBundle (Beta)

Note: This feature is a Beta Service. Customer may opt to try such Beta Service in its sole discretion. Any use of the Beta Service
[is subject to the applicable Beta Services Terms provided at Agreements and Terms.](https://www.salesforce.com/company/legal/agreements/)

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

[To create a custom property type, see LightningPropertyType.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_lightningtypebundle.htm)

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Structure and Directory Location

ExperiencePropertyTypeBundle components are stored in the experiencePropertyTypeBundles folder. Here’s an example of how the
folder is structured.

```
   +--myMetadataPackage

      +--experiencePropertyTypeBundles (1)

        +--addressProperty (2)

           +--schema.json (3)

           +--design.json (4)

```

**•** In the experiencePropertyTypeBundles folder (1) is a folder for each custom property type.

**•** Each custom property type folder is named in the format propertyTypeName. In this example (2), the name is addressProperty.

**•** Each propertyTypeName folder contains a JSON file or files that define the property type.

**–** A `schema.json` file (3), which is a JSON schema that drives the property type validation

**–** An optional `design.json` file (4), which provides the user experience and property editor information for that property type

Version

ExperiencePropertyTypeBundle components are available in API version 58.0 and later.

Special Access Rules

The ExperiencePropertyTypeBundle metadata type is available only for use with Lightning web components on LWR sites.

Fields

**Field Name** **Description**

```
description

```

**Field Type**
string

**Description**
Explanatory text about the property type.


Metadata Types ExperiencePropertyTypeBundle (Beta)

**Field Name** **Description**

```
masterLabel

resources

```

**Field Type**
string

**Description**

Required. A user-friendly name for ExperiencePropertyTypeBundle, which is defined
when the ExperiencePropertyTypeBundle is created.

**Field Type**

ExperiencePropertyTypeBundleResource[]

**Description**
A list of source files in the experiencePropertyTypeBundles folder.

ExperiencePropertyTypeBundleResource

Represents a resource inside ExperiencePropertyTypeBundle.

**Field Name** **Description**

```
fileName

filePath

source

```

**Field Type**
string

**Description**

Required. The file name of the resource.

**Field Type**
string

**Description**

Required. The file path of the resource.

**Field Type**
base64Binary

**Description**

Required. The content of the resource.

Declarative Metadata Sample Definition

This `package.xml` file retrieves all the ExperiencePropertyTypeBundle components in an org.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>*</members>

     <name>ExperiencePropertyTypeBundle</name>

```


Metadata Types ExperiencePropertyTypeBundle (Beta)

```
      </types>

      <version>58.0</version>

   </Package>

```

In the retrieved `.zip` file, each property type is nested under an experiencePropertyTypeBundles folder.

This example shows the directory structure in the `.zip` file of a property type named addressProperty.

```
   experiencePropertyTypeBundles

      addressProperty

        schema.json

        design.json

```

Here are the contents of the files in the addressProperty directory. The addressProperty is a complex type that includes subproperties
for firstName, lastName, address, city, state, and postal code. Each subproperty is a primitive type.

Contents of `schema.json` :

```
   {

    "title": "Simple Address Type",

    "lightning:type": "lightning__objectType",

    "properties": {

     "firstName": {

      "lightning:type": "lightning__textType",

      "title": "First Name"

     },

     "lastName": {

      "lightning:type": "lightning__textType",

      "title": "Last Name"

     },

     "address": {

      "lightning:type": "lightning__textType",

      "title": "Address Line 1"

     },

     "city": {

      "lightning:type": "lightning__textType",

      "title": "City"

     },

     "state": {

      "lightning:type": "lightning__textType",

      "title": "State"

     },

     "postalCode": {

      "lightning:type": "lightning__numberType",

      "title": "Postal Code"

     }

    },

    "required": ["firstName", "lastName"]

   }

```

Contents of `design.json` (an optional file):

```
   {

    "definition": "lightning/tabsetLayout",

    "children": [

     {

      "definition": "lightning/tabLayout",

```


### Metadata Types ExplainabilityMsgTemplate

```
      “attributes”: {

        “label”: “First Tab”

      },

      “children”: [

        {

         "definition": "lightning/propertyLayout",

         "attributes": {

          "property": "aProperty"

         }

        },

        {

         "definition": "lightning/propertyLayout",

         "attributes": {

          "property": "bProperty"

         }

        },

      ]

     },

      {

      "definition": "lightning/tabLayout",

      “attributes”: {

        “label”: “Second Tab”

      },

      “children”: [

        {

         "definition": "lightning/propertyLayout",

         "attributes": {

          "property": "cProperty"

         }

        },

      ]

     },

    ]

   }

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

_External Link_ [: Custom Property Types and Property Editors (Beta)](https://resources.docs.salesforce.com/rel1/doc/en-us/static/pdf/custom_property_types_and_editors.pdf)

### ExplainabilityMsgTemplate

Represents information about the template that contains the decision explanation message for a specified expression set step type.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types ExplainabilityMsgTemplate

File Suffix and Directory Location

ExplainabilityMsgTemplate components have the suffix `.explainabilityMsgTemplate` and are stored in the
`ExplainabilityMsgTemplates` folder.

Version

ExplainabilityMsgTemplate components are available in API version 56.0 and later.

Fields

**Field Name** **Description**

```
evaluationResult

expressionSetStepType

```

**Field Type**
EvaluationResult (enumeration of type string)

**Description**

Required.

The type of result for which the message template can be used. The step type for
which the result is evaluated can be a condition, conditional group, or branch.

Valid values are:

**•** `Failed`

**•** `Passed`

**•** `NoResult`

**Field Type**
ExpressionSetStepType (enumeration of type string)

**Description**

Required.

The step type in an expression set that uses the explainability message template.

Valid values are:

**•** `Aggregation`

**•** `Branch`

**•** `BusinessElement`

**•** `Calculation`

**•** `Condition`

**•** `DecisionTableLookup`

**•** `ListEnabledGroup`

**•** `ListFilter`

**•** `MatrixLookup`

**•** `ReferenceProcedure`


Metadata Types ExplainabilityMsgTemplate

**Field Name** **Description**

```
expsSetProcessType

isDefault

masterLabel

message

```

**Field Type**
ExpsSetProcessType (enumeration of type string)

**Description**

Required.

The type of industry that’s using the expression set.

Valid values are:

**•** `Bre`

**•** `GpaCalculation`

**•** `InsuranceClaimProcessing` —Available in API version 65.0 and later.

**•** `ItServiceManagement` —Available in API version 65.0 and later.

**•** `PlanCostCalculation`

**•** `RatingDiscovery`

**•** `StudentInformationSystem` —Available in API version 65.0 and later.

**•** `StudentSuccess`

When Business Rules Engine is enabled for a Salesforce instance, the default value is
' `Bre` ’. Other process types are available to you depending on your industry solution
and permission sets.

**Field Type**
boolean

**Description**
Indicates whether the decision explainer template for a specified step type is default
(true) or not (false).

**Field Type**
string

**Description**

Required.

Master label the for ExplainabilityMsgTemplate.

**Field Type**
string

**Description**

Required.

The message associated with the template for a specific expression set step type.


### Metadata Types ExpressionSetDefinition

Declarative Metadata Sample Definition

The following is an example of an ExplainabilityMsgTemplate component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ExplainabilityMsgTemplate

    xmlns="http://soap.sforce.com/2006/04/metadata">

    <evaluationResult>Passed</evaluationResult>

    <expressionSetStepType>Condition</expressionSetStepType>

    <expsSetProcessType>ProductQualification</expsSetProcessType>

    <isDefault>false</isDefault>

    <masterLabel>ML EMT testDM</masterLabel>

    <message>EMT Testing</message>

   </ExplainabilityMsgTemplate>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package

    xmlns="http://soap.sforce.com/2006/04/metadata">

    <types>

     <members>*</members>

     <name>ExplainabilityMsgTemplate</name>

    </types>

    <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/file_based.htm)

### ExpressionSetDefinition

Represents an expression set definition.

[Note: Before deploying an expression set or an expression set version to a target org, review these Expression Set Migration](https://help.salesforce.com/s/articleView?id=ind.considerations_for_migrating_expression_sets.htm&type=5&language=en_US)
[Considerations.](https://help.salesforce.com/s/articleView?id=ind.considerations_for_migrating_expression_sets.htm&type=5&language=en_US)

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ExpressionSetDefinition components have the suffix .expressionSetDefinition and are stored in the

`expressionSetDefinition` folder.


Metadata Types ExpressionSetDefinition

Version

ExpressionSetDefinition components are available in API version 55.0 and later.

Fields

**Field Name** **Description**

```
description

executionMode

executionScale

interfaceSourceType

```

**Field Type**
string

**Description**
The description of an expression set definition.

**Field Type**
ExpsSetExecutionMode (enumeration of type string)

**Description**
Specifies the execution mode for the expression set definition.

Valid values are:

**•** `Cloud`

**•** `Local`

**Field Type**
ExpsSetExecutionScale (enumeration of type string)

**Description**
Specifies the scale of the inputs that an expression set processes. The scale determines
where the expression set is executed.

Valid values are:

**•** `High`

**•** `Low`

Available in API version 61.0 and later.

**Field Type**
ExpsSetInterfaceSourceType (enumeration of type string)

**Description**
The interface source type designed by the consuming cloud that's making a customized
expression set builder available to its users.

Valid values are:

**•** `Bre`

**•** `Constraint` (Available in API version 62.0 and later).

**•** `DiscoveryProcedure` (Available in API version 61.0 and later).

**•** `EventOrchestration` (Available in API version 61.0 and later).

**•** `GpaCalculationProcedure` (Available in API version 67.0 and later).


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

**•** `IntelligentDecisionStudio` (Available in API version 67.0 and later).

**•** `ItServiceManagement` (Available in API version 65.0 and later).

**•** `PricingProcedure`

**•** `QualificationProcedure`

**•** `RatingDiscoveryProcedure` (Available in API version 61.0 and later).

**•** `RatingProcedure` (Available in API version 67.0 and later).

**•** `Sample`

Available in API version 59.0 and later.

```
label

processType

resourceInitializationType

```

**Field Type**
string

**Description**
Required.

The UI label of an expression set definition.

**Field Type**
ExpsSetProcessType (enumeration of type string)

**Description**
The process type that uses the expression set rule.

Valid values are:

**•** `Bre`

**•** `GpaCalculation`

**•** `InsuranceClaimProcessing` —Available in API version 65.0 and later.

**•** `ItServiceManagement` —Available in API version 65.0 and later.

**•** `PlanCostCalculation`

**•** `RatingDiscovery`

**•** `StudentInformationSystem` —Available in API version 65.0 and later.

**•** `StudentSuccess`

When Business Rules Engine is enabled for a Salesforce instance, the default value is
`Bre` . Other process types are available to you depending on your industry solution
and permission sets.

**Field Type**
ResourceInitializationType (enumeration of type string)

**Description**
Indicates whether the initial value of expression set variables and context tags is null
or a default value.

Valid values are:

**•** `Default`

**•** `Off`


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

Available in API version 64.0 and later.

```
template

type

usageSubType

versions

```

**Field Type**
boolean

**Description**
Defines whether an expression set is a template or not.

**Field Type**
ExpsSetType (enumeration of type string)

**Description**
The type of the expression set definition.

Valid values are:

**•** `Custom`

**•** `Standard`

**Field Type**
ExpsSetUsageSubType (enumeration of type string)

**Description**
The subtype of the industry that's using the expression set definition. If no value is
specified, the field defaults to null.

**Field Type**

ExpressionSetDefinitionVersion[]

**Description**
Represents an array of expression set version definitions in an expression set.

This array must contain at least one version.

ExpressionSetDefinitionVersion

Represents a definition of an expression set version.

**Field Name** **Description**

```
decimalScale

description

```

**Field Type**
integer

**Description**
Number of decimal places to be used in the results of calculation steps that involve context
variables.

**Field Type**
string


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

**Description**
Describes the version of an expression set definition.

```
endDate

expressionSetDefinition

interfaceSourceType

label

```

**Field Type**
dateTime

**Description**
The date until which the expression set definition is available for use.

**Field Type**
string

**Description**
The full name of an expression set definition.

**Field Type**
ExpsSetInterfaceSourceType (enumeration of type string)

**Description**
The interface source type designed by the consuming cloud that's making a customized
expression set builder available to its users.

Valid values are:

**•** `Bre`

**•** `Constraint`

**•** `DiscoveryProcedure`

**•** `EventOrchestration`

**•** `GpaCalculationProcedure`

**•** `IntelligentDecisionStudio`

**•** `ItServiceManagement`

**•** `PricingProcedure`

**•** `QualificationProcedure`

**•** `RatingDiscoveryProcedure`

**•** `RatingProcedure`

**•** `Sample`

Available in API version 67.0 and later.

**Field Type**
string

**Description**
Required.

The UI label of an expression set definition.


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

```
processType

rank

shouldShowExplExternally

startDate

status

steps

```

**Field Type**
ExpsSetProcessType (enumeration of type string)

**Description**
The process type that uses the expression set rule. Available in API version 67.0 and later.

**Field Type**
int

**Description**
The rank of the `Expression Set Definition Version` . When more than one
enabled version matches an expression set call, and the start date time to end date time
spans overlap, the version with the highest rank is chosen. Available in API version 62.0 and
later.

**Field Type**
boolean

**Description**
Indicates whether the decision explanation is exposed to external users ( `true` ) or not
( `false` ). The default value is `false` . Available in API version 56.0 and later.

**Field Type**
dateTime

**Description**
Required.

The date from when the expression set definition is available for use.

**Field Type**
ExpsSetStatus (enumeration of type string)

**Description**
Required.

The status of an expression set definition.

Valid values are:

**•** `Active`

**•** `Draft`

**•** `Inactive`

**•** `InvalidDraft`

**•** `Obsolete`

**Field Type**

ExpressionSetStep[]

**Description**
Represents an array of steps created in an expression set version.


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

```
uiTier

variables

versionNumber

```

ExpressionSetStep

**Field Type**
boolean

**Description**
Indicates whether the API call originated from the design time builder or a package.

Note: This field is for internal use only.

**Field Type**

ExpressionSetVariable[]

**Description**
Represents an array of variables in an expression set version.

**Field Type**
int

**Description**
Required.

The version number of an expression set definition.

Represents a step in an expression set version.

**Field Name** **Description**

```
actionType

```

**Field Type**
BusinessKnowledgeModel (enumeration of type string)

**Description**
Specifies the type of action this step executes.

Valid values are:

**•** `AiAcceleratorSubscriberChurnPrediction`

**•** `ApexAction`

**•** `ApexListAction` (Available in API version 64.0 and later.)

**•** `AssetDiscovery`

**•** `AssignBadgeToMember`

**•** `AssignParameterValues`

**•** `AssignmentElement`

**•** `AssignmentRuleCustomQueue` (Available in API version 65.0 and later.)

**•** `AssignmentRuleCustomUser` (Available in API version 65.0 and later.)

**•** `AteprlRecordCreator` (Available in API version 65.0 and later.)

**•** `AttributeAdjustmentMatrix`


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

**•** `AttributeDiscount`

**•** `AutomatedClaimsProcessingValidation`

**•** `BaseRate`

**•** `BindingObjectRateAdjustmentResolution` (Available in API version 64.0
and later.)

**•** `BindingObjectRateCardEntryResolution` (Available in API version 64.0
and later.)

**•** `BreAggregator`

**•** `BreAggregatorAssignment`

**•** `BreakdownLineMapping` (Available in API version 64.0 and later.)

**•** `BundleDiscount`

**•** `CalculateQuantity` (Available in API version 64.0 and later.)

**•** `ChangeMemberTier`

**•** `CheckMemberBadgeAssignment`

**•** `CommercePricing` (Available in API version 62.0 and later.)

**•** `CommitmentAdjustment` (Available in API version 65.0 and later.)

**•** `ComplianceCheck`

**•** `ComplianceControlLog` (Available in API version 62.0 and later.)

**•** `Constraint` (Available in API version 64.0 and later.)

**•** `CreditPoints`

**•** `Crud`

**•** `DebitPoints`

**•** `DerivedPricing`

**•** `DiscountDistributionService`

**•** `DiscoverySettings` (Available in API version 64.0 and later.)

**•** `DynamicRulesExecutor` (Available in API version 65.0 and later.)

**•** `EvaluateCategoryDisqualification` (Available in API version 62.0 and
later.)

**•** `EvaluateCategoryQualification` (Available in API version 62.0 and later.)

**•** `EvaluateDisqualification`

**•** `EvaluateQualification`

**•** `FormulaBasedPricing`

**•** `FormulaBasedRating` (Available in API version 62.0 and later.)

**•** `GetCustomerPromotionAttrValue` (Available in API version 64.0 and later.)

**•** `GetMemberAttributesValues`

**•** `GetMemberPartnerLinkageStatus`

**•** `GetMemberPointBalance`

**•** `GetMemberPromotions`

**•** `GetMemberTier`


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

**•** `GetOutputsFromDecisionMatrix`

**•** `GetOutputsFromDecisionTable`

**•** `GetUserData`

**•** `GroupingAndAggregatePricing`

**•** `GroupingAndAggregateRating` (Available in API version 62.0 and later.)

**•** `IncreaseUsageForCumulativePromotion`

**•** `IntegrationOrchestration`

**•** `InterNodeDataCopy`

**•** `IssueExtendedReward` (Available in API version 64.0 and later.)

**•** `IssueVoucher`

**•** `ListGroup`

**•** `ListGroupCalculation`

**•** `ListPrice`

**•** `ManualDiscount`

**•** `ManualRatingDiscount` (Available in API version 62.0 and later.)

**•** `MapProduct`

**•** `MinimumPrice` (Available in API version 62.0 and later.)

**•** `MultiRecipientProductQualification` (Available in API version 64.0 and
later.)

**•** `NegotiatedBaseRate` (Available in API version 64.0 and later.)

**•** `NegotiatedRateCardEntryResolution` (Available in API version 64.0 and
later.)

**•** `NegotiatedTierAdjustment` (Available in API version 64.0 and later.)

**•** `NegotiatedVolumeAdjustment` (Available in API version 64.0 and later.)

**•** `PredictiveAI`

**•** `PriceAdjustmentMatrix`

**•** `PriceGuidance` (Available in API version 64.0 and later.)

**•** `PriceRevision` (Available in API version 65.0 and later.)

**•** `PricingPropagation` (Available in API version 65.0 and later.)

**•** `PricingSettings`

**•** `PromotionExecution` (Available in API version 65.0 and later.)

**•** `PromotionsDiscount`

**•** `Proration`

**•** `RateAdjustmentByAttributeResolution` (Available in API version 62.0
and later.)

**•** `RateAdjustmentByTierResolution` (Available in API version 62.0 and later.)

**•** `RateAdjustmentMatrix` (Available in API version 62.0 and later.)

**•** `RateAssignment` (Available in API version 62.0 and later.)

**•** `RateCardEntryResolution` (Available in API version 62.0 and later.)


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

**•** `RateCardResolution` (Available in API version 62.0 and later.)

**•** `RatingAttributeDiscount`

**•** `RatingBreakdownLineMapping` (Available in API version 65.0 and later.)

**•** `RatingRoundingValues` (Available in API version 62.0 and later.)

**•** `RatingSetting`

**•** `RatingTierDiscount`

**•** `RatingVolumeDiscount`

**•** `RecordAction`

**•** `RecordAlert`

**•** `RedeemVoucher`

**•** `RoundingValues`

**•** `RuleFetch`

**•** `RunFlow`

**•** `RunProgramProcess`

**•** `SampleBusinessElementWithContext`

**•** `SampleCustomElementWithExpressionAndListFilter`

**•** `SampleDynamicCustomElement`

**•** `SampleJavaBasedTaxCalculatorCustomElement`

**•** `SampleTaxCalculatorCustomElement`

**•** `SendMail`

**•** `StopPricing`

**•** `StopRating` (Available in API version 62.0 and later.)

**•** `SubscriptionPricing`

**•** `TermGpaCalculation` (Available in API version 64.0 and later.)

**•** `TermGpaReporting` (Available in API version 64.0 and later.)

**•** `TestCustomElement`

**•** `UpdateCurrentValueForMemberAttribute`

**•** `UpdateCustomerPromotionAttrValue` (Available in API version 64.0 and
later.)

**•** `UpdatePointBalance`

**•** `UpdateUsageForCumulativePromotion`

**•** `UpsertRecord` (Available in API version 64.0 and later.)

**•** `VolumeDiscount`

**•** `VolumeTierDiscount`

```
advancedCondition

```

**Field Type**

ExpressionSetAdvancedCondition

**Description**
Represents an advanced condition step.


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

```
aggregation

assignment

conditionExpression

customElement

decisionTable

description

failedExplainerTemplate

failedMessage

TokenMappings

```

**Field Type**

ExpressionSetAggregation

**Description**
Represents an aggregation step.

**Field Type**

ExpressionSetAssignment

**Description**
Represents an assignment step.

**Field Type**

ExpressionSetConditionExpression

**Description**
Represents a condition step.

**Field Type**

ExpressionSetCustomElement

**Description**
Represents a custom element step that contains the input and output mappings. Available
in API version 56.0 and later.

**Field Type**

ExpressionSetDecisionTable

**Description**
Represents a decision matrix or decision table step.

**Field Type**
string

**Description**
Describes an expression set definition version step.

**Field Type**
string

**Description**

The explainability message template that’s used when the result type of a condition step
in an expression set is Failed.

**Field Type**
ExplainabilityMessageTemplateTokenMapping (enumeration of type string)

**Description**

List of the token resource mappings of the failed explainability message template. Valid
values are:


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

**•** `expressionSetMessageToken`

**•** `resourceReference`

Available in API version 59.0 and later.

```
hasNestedExplainability

label

name

noResult

ExplainerTemplate

noResultMessage

TokenMappings

```

**Field Type**
boolean

**Description**
Indicates whether the step has nested explainability (

```
  true

```

) or not (

```
  false

```

). Available in API version 67.0 and later.

**Field Type**
string

**Description**
Required.

The UI label of an expression set definition version step.

**Field Type**
string

**Description**
Required.

The full name of an expression set definition version step.

**Field Type**
string

**Description**

The explainability message template that’s used when the result type of a condition step
in an expression set is No Result. Available in API version 59.0 and later.

**Field Type**
ExplainabilityMessageTemplateTokenMapping (enumeration of type string)

**Description**

List of the token resource mappings of the no result explainability message template. Valid
values are:

**•** `expressionSetMessageToken`

**•** `resourceReference`

Available in API version 59.0 and later.


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

```
parentStep

passedExplainerTemplate

passedMessage

TokenMappings

resultIncluded

sequenceNumber

shouldExposExecPathMsgOnly

shouldExposeConditionDetails

```

**Field Type**
string

**Description**

The name of the parent step in an expression set definition version that’s associated with
a step.

**Field Type**
string

**Description**

The explainability message template that’s used when the result type of a condition step
in an expression set is Passed.

**Field Type**
ExplainabilityMessageTemplateTokenMapping (enumeration of type string)

**Description**

List of the token resource mappings of the passed explainability message template. Valid
values are:

**•** `expressionSetMessageToken`

**•** `resourceReference`

Available in API version 59.0 and later.

**Field Type**
boolean

**Description**

Indicates whether the step output must be included in the expression result (true) or not
(false).

**Field Type**
int

**Description**
Required.

The sequence number of a step in an expression set definition version.

**Field Type**
boolean

**Description**
Indicates whether the message in the explainability message template is exposed for only
the branch path that was run.

**Field Type**
boolean


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

**Description**
Indicates whether the details of the condition are shown in the decision explanation.

```
shouldShowExplExternally

stepType

subExpression

```

**Field Type**
boolean

**Description**
Indicates whether the decision explanations are shown to external users.

**Field Type**
ExpsSetStepType (enumeration of type string)

**Description**
Required.

Specifies the type of step in an expression set definition version.

Valid values are:

**•** `AdvancedCondition`

**•** `AdvancedListFilter` (Available in API version 67.0 and later).

**•** `Branch`

**•** `BusinessKnowledgeModel`

**•** `Condition`

**•** `DefaultPath`

**•** `ListFilter` (Available in API version 67.0 and later).

**•** `ListGroup` (Available in API version 67.0 and later).

**•** `SubExpression`

**Field Type**

ExpressionSetSubExpression

**Description**
Represents a sub expression step.

ExpressionSetAdvancedCondition

Represents an advanced condition step.

**Field Name** **Description**

```
conditionLogic

```

**Field Type**
string

**Description**
Required.

The condition that’s defined for an advanced condition.


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

```
criteria

errorMessage

resultParameter

successMessage

```

**Field Type**

ExpressionSetConditionCriteria []

**Description**
Represents an array of criteria defined in the advanced condition.

**Field Type**
string

**Description**
An error message for a failed advanced condition.

**Field Type**
string

**Description**
An expression set definition version variable associated with the result of a step.

**Field Type**
string

**Description**
A success message for a successful advanced condition.

ExpressionSetConditionCriteria

Represents a criterion defined in an advanced condition.

**Field Name** **Description**

```
operator

```

**Field Type**
ExpsSetConditionOperator (enumeration of type string)

**Description**
Required.

Specifies the operator for evaluating an expression.

Valid values are:

**•** `Contains`

**•** `DoesNotContain`

**•** `Equals`

**•** `GreaterThan`

**•** `GreaterThanOrEquals`

**•** `IsNull`

**•** `IsNotNull`

**•** `LessThan`


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

**•** `LessThanOrEquals`

**•** `NoEquals`

```
sequenceNumber

sourceFieldName

value

valueType

```

**Field Type**
int

**Description**
Required.

The position of the condition in a step that contains multiple conditions.

**Field Type**
string

**Description**
Required.

The expression set definition version variable associated with the result of a condition
criterion.

**Field Type**
string

**Description**
Specifies the condition of a criterion.

**Field Type**
ExpsSetValueType (enumeration of type string)

**Description**
Specifies the type of value.

Valid values are:

**•** `Formula`

**•** `Literal`

**•** `Lookup`

**•** `Parameter`

**•** `Picklist`

ExpressionSetAggregation

Represents an aggregation step.

**Field Name** **Description**

```
aggregatedParameter

```

**Field Type**
string


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

**Description**
Required.

The expression set definition version variable associated with the result of a condition
criterion.

```
aggregateFunction

expression

```

**Field Type**
ExpsSetAggregationFunction (enumeration of type string)

**Description**
Required.

Specifies the aggregation function used in a step.

Valid values are:

**•** `Avg`

**•** `Max`

**•** `Min`

**•** `Sum`

**Field Type**
string

**Description**
Required.

Specifies the expression of an aggregation.

ExpressionSetAssignment

Represents an assignment step.

**Field Name** **Description**

```
aggregatedParameter

expression

```

**Field Type**
string

**Description**
Required.

The expression set definition version variable associated with a step detail.

**Field Type**
string

**Description**
Required.

The expression that’s defined for a step.


Metadata Types ExpressionSetDefinition

ExpressionSetConditionExpression

Represents a condition in a condition step.

**Field Name** **Description**

```
errorMessage

expression

resultParameter

successMessage

```

**Field Type**
string

**Description**
An error message for a failed condition.

**Field Type**
string

**Description**
Required.

The expression that’s defined for a step.

**Field Type**
string

**Description**
The expression set definition version variable associated with the result of a step.

**Field Type**
string

**Description**
A success message for a successful condition.

ExpressionSetCustomElement

Represents a custom element in an expression set. Available in API version 56.0 and later.

**Field Name** **Description**

```
parameters

```

**Field Type**

ExpressionSetElementParameter[]

**Description**
Represents the list of parameters in the custom element.

ExpressionSetElementParameter

Represents a parameter within a custom element of an expression set. Available in API version 56.0 and later.


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

```
input

name

output

type

value

```

**Field Type**
boolean

**Description**

Required.

Indicates whether the custom element parameter is input ( `true` ) or not ( `false` ).

The default value is `true` .

**Field Type**
string

**Description**

Required.

The name of the custom element parameter.

**Field Type**
boolean

**Description**

Required.

Indicates whether the custom element parameter is output ( `true` ) or not ( `false` ).

The default value is `true` .

**Field Type**
ExpsSetValueType (enumeration of type string)

**Description**
The type of custom element parameter.

Values are:

**•** `Formula`

**•** `Literal`

**•** `Lookup`

**•** `Parameter`

**•** `PickList`

The default value is `Parameter` .

**Field Type**
string

**Description**

Required.

The name of the expression set variable.


Metadata Types ExpressionSetDefinition

ExpressionSetDecisionTable

Represents a decision table or decision matrix in a step.

**Field Name** **Description**

```
decisionTableName

mappings

type

```

**Field Type**
string

**Description**
Required.

The decision matrix or decision table name used in a step.

**Field Type**

ExpressionSetElementParameter[]

**Description**
The mapping information between various parameters in an ExpressionSetDecisionTable.

Available in API version 59.0 and later.

**Field Type**
string

**Description**
Required.

The type in a step. It can be a decision table or decision matrix.

ExpressionSetSubExpression

Represents a sub expression in a step.

**Field Name** **Description**

```
expressionSet

mappings

```

**Field Type**
string

**Description**
Required.

The sub expression name used in a step.

**Field Type**

ExpressionSetElementParameter[]

**Description**
The mapping information between various parameters in an ExpressionSetDecisionTable.

Available in API version 61.0 and later.


Metadata Types ExpressionSetDefinition

ExpressionSetVariable

Represents a definition of an expression set variable.

**Field Name** **Description**

```
collection

dataType

decimalPlaces

description

fields

```

**Field Type**
boolean

**Description**
Indicates whether a variable stores a collection of values ( `true` ) or not ( `false` ).

**Field Type**
ExpsSetDataType (enumeration of type string)

**Description**
Required.

The data type of an expression set variable.

Valid values are:

**•** `ActionOutput`

**•** `Boolean`

**•** `Currency`

**•** `Date`

**•** `DateTime`

**•** `DecisionMatrix`

**•** `DecisionTable`

**•** `Numeric`

**•** `Percent`

**•** `Sobject`

**•** `SubExpression`

**•** `Text`

**Field Type**
int

**Description**
The decimal digits in the currency, number, or percent data type for an expression set
variable.

**Field Type**
string

**Description**
The description of the variable used in an expression set.

**Field Type**

ExpressionSetVariableField []


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

**Description**
Represents an array of fields in an object that's used as a variable in an expression set.

```
input

lookupName

lookupType

name

objectName

output

```

**Field Type**
boolean

**Description**
Indicates whether an expression set variable is used as an input ( `true` ) in an expression
or not ( `false` ).

**Field Type**
string

**Description**
The API name of a decision matrix, a decision table, or a sub expression.

**Field Type**
ExpsSetVariableLookupType (enumeration of type string)

**Description**
The type of the lookup used in an expression set definition.

Valid values are:

**•** `DecisionMatrix`

**•** `DecisionTable`

**•** `SubExpression`

**Field Type**
string

**Description**
Required.

The full name of the variable used in an expression set definition.

**Field Type**
string

**Description**
The name of the sObject.

**Field Type**
boolean

**Description**
Indicates whether an expression set variable is used as an output in an expression( `true` )
or not ( `false` ).


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

```
resultStep

type

value

```

**Field Type**
string

**Description**
The step that produces the expression set variable.

**Field Type**
ExpsSetVariableType (enumeration of type string)

**Description**
Required.

The type of variable in an expression set definition.

Valid values are:

**•** `Constant`

**•** `ContextDynamicAttributeTag` (Available in API version 62.0 and later.)

**•** `ExecutableContextDefinitionTag` (Available in API version 62.0 and later.)

**•** `Formula`

**•** `Variable`

**Field Type**
string

**Description**
Represents a constant value or a formula.

Note: It stores the default value of a variable.

ExpressionSetVariableField

Represents a definition of a field in an object that's used as a variable in an expression set.

**Field Name** **Description**

```
dataType

```

**Field Type**
ExpsSetDataType (enumeration of type string)

**Description**
Required.

Specifies the type of data stored in an expression set variable.

Valid values are:

**•** `ActionOutput`

**•** `Boolean`

**•** `Currency`

**•** `Date`


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

**•** `DateTime`

**•** `DecisionMatrix`

**•** `DecisionTable`

**•** `Numeric`

**•** `Percent`

**•** `Sobject`

**•** `SubExpression`

**•** `Text`

```
decimalPlaces

fields

lookupName

lookupType

name

```

**Field Type**
int

**Description**
The decimal digits in the currency, number, or percent data type for an expression set
variable.

**Field Type**

ExpressionSetVariableField []

**Description**
Represents an array of fields in an object that's used as a variable in an expression set.

**Field Type**
string

**Description**
The API name of a decision matrix, a decision table, or a sub expression.

**Field Type**
ExpsSetVariableLookupType (enumeration of type string)

**Description**
Required.

The type of lookup used in an expression set definition.

Valid values are:

**•** `DecisionMatrix`

**•** `DecisionTable`

**•** `SubExpression`

**Field Type**
string

**Description**
Required.

The full name of the field used in an expression set variable.


Metadata Types ExpressionSetDefinition

**Field Name** **Description**

```
objectName

```

**Field Type**
string

**Description**
The name of the sObject.

Declarative Metadata Sample Definition

The following is an example of an ExpressionSetDefinition component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ExpressionSetDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

   <label>ExpSetWithAllSteps</label>

   <processType>Bre</processType>

   <template>false</template>

   <description></description>

   <interfaceSourceType>Sample</interfaceSourceType>

   <executionScale>Low</executionScale>

   <versions>

     <fullName>ExpSetWithAllSteps_V1</fullName>

     <expressionSetDefinition>ExpSetWithAllSteps</expressionSetDefinition>

     <label>ExpSetWithAllSteps V1</label>

     <shouldShowExplExternally>false</shouldShowExplExternally>

     <startDate>2022-08-09T22:04:56.000Z</startDate>

     <endDate>2023-08-09T22:04:56.000Z</endDate>

     <status>Draft</status>

     <uiTier>false</uiTier>

     <rank>1</rank>

     <description>ExpSetWithAllSteps_V1</description>

     <steps>

        <description>Aggregate</description>

        <actionType>BreAggregator</actionType>

        <aggregation>

          <aggergatedParameter>result</aggergatedParameter>

          <aggregateFunction>Avg</aggregateFunction>

          <expression>AVG ( result )</expression>

        </aggregation>

        <label>Aggregate</label>

        <name>Aggregate</name>

        <resultIncluded>true</resultIncluded>

        <sequenceNumber>5</sequenceNumber>

        <shouldExposExecPathMsgOnly>true</shouldExposExecPathMsgOnly>

        <shouldExposeConditionDetails>false</shouldExposeConditionDetails>

        <shouldShowExplExternally>false</shouldShowExplExternally>

        <stepType>BusinessKnowledgeModel</stepType>

     </steps>

     <steps>

        <label>Branch</label>

        <name>Branch</name>

        <resultIncluded>false</resultIncluded>

        <sequenceNumber>4</sequenceNumber>

```


Metadata Types ExpressionSetDefinition

```
           <shouldExposExecPathMsgOnly>true</shouldExposExecPathMsgOnly>

           <shouldExposeConditionDetails>false</shouldExposeConditionDetails>

           <shouldShowExplExternally>false</shouldShowExplExternally>

           <stepType>Branch</stepType>

        </steps>

        <steps>

           <actionType>AssignParameterValues</actionType>

           <assignment>

             <assignedParameter>b</assignedParameter>

             <expression>SUM ( a, 10 )</expression>

           </assignment>

           <label>Calculation</label>

           <name>Calculation</name>

           <resultIncluded>true</resultIncluded>

           <sequenceNumber>1</sequenceNumber>

           <shouldExposExecPathMsgOnly>true</shouldExposExecPathMsgOnly>

           <shouldExposeConditionDetails>false</shouldExposeConditionDetails>

           <shouldShowExplExternally>false</shouldShowExplExternally>

           <stepType>BusinessKnowledgeModel</stepType>

        </steps>

        <steps>

           <actionType>AssignParameterValues</actionType>

           <assignment>

             <assignedParameter>result</assignedParameter>

             <expression>b * 100</expression>

           </assignment>

           <label>Calculation</label>

           <name>Calculation10</name>

           <parentStep>DefaultLane</parentStep>

           <resultIncluded>false</resultIncluded>

           <sequenceNumber>1</sequenceNumber>

           <shouldExposExecPathMsgOnly>true</shouldExposExecPathMsgOnly>

           <shouldExposeConditionDetails>false</shouldExposeConditionDetails>

           <shouldShowExplExternally>false</shouldShowExplExternally>

           <stepType>BusinessKnowledgeModel</stepType>

        </steps>

        <steps>

           <actionType>AssignParameterValues</actionType>

           <assignment>

             <assignedParameter>result</assignedParameter>

             <expression>b * 1</expression>

           </assignment>

           <label>Calculation</label>

           <name>Calculation3</name>

           <parentStep>Condition</parentStep>

           <resultIncluded>false</resultIncluded>

           <sequenceNumber>1</sequenceNumber>

           <shouldExposExecPathMsgOnly>true</shouldExposExecPathMsgOnly>

           <shouldExposeConditionDetails>false</shouldExposeConditionDetails>

           <shouldShowExplExternally>false</shouldShowExplExternally>

           <stepType>BusinessKnowledgeModel</stepType>

        </steps>

        <steps>

           <actionType>AssignParameterValues</actionType>

```


Metadata Types ExpressionSetDefinition

```
           <assignment>

             <assignedParameter>result</assignedParameter>

             <expression>SUM ( b, 10 )</expression>

           </assignment>

           <label>Calculation</label>

           <name>Calculation5</name>

           <parentStep>Condition4</parentStep>

           <resultIncluded>false</resultIncluded>

           <sequenceNumber>1</sequenceNumber>

           <shouldExposExecPathMsgOnly>true</shouldExposExecPathMsgOnly>

           <shouldExposeConditionDetails>false</shouldExposeConditionDetails>

           <shouldShowExplExternally>false</shouldShowExplExternally>

           <stepType>BusinessKnowledgeModel</stepType>

        </steps>

        <steps>

           <actionType>AssignParameterValues</actionType>

           <assignment>

             <assignedParameter>result</assignedParameter>

             <expression>b * 10</expression>

           </assignment>

           <label>Calculation</label>

           <name>Calculation8</name>

           <parentStep>Condition7</parentStep>

           <resultIncluded>false</resultIncluded>

           <sequenceNumber>1</sequenceNumber>

           <shouldExposExecPathMsgOnly>true</shouldExposExecPathMsgOnly>

           <shouldExposeConditionDetails>false</shouldExposeConditionDetails>

           <shouldShowExplExternally>false</shouldShowExplExternally>

           <stepType>BusinessKnowledgeModel</stepType>

        </steps>

        <steps>

           <conditionExpression>

             <successMessage>success</successMessage>

             <errorMessage>error</errorMessage>

             <expression>IS10 == b</expression>

             <resultParameter>condition_output__1</resultParameter>

           </conditionExpression>

           <label>Condition</label>

           <name>Condition</name>

           <resultIncluded>false</resultIncluded>

           <sequenceNumber>2</sequenceNumber>

           <shouldExposExecPathMsgOnly>true</shouldExposExecPathMsgOnly>

           <shouldExposeConditionDetails>false</shouldExposeConditionDetails>

           <shouldShowExplExternally>false</shouldShowExplExternally>

           <stepType>Condition</stepType>

        </steps>

        <steps>

           <advancedCondition>

             <successMessage>success</successMessage>

             <errorMessage>error</errorMessage>

             <conditionLogic>1</conditionLogic>

             <criteria>

               <operator>Equals</operator>

               <sequenceNumber>1</sequenceNumber>

```


Metadata Types ExpressionSetDefinition

```
               <sourceFieldName>condition_output__1</sourceFieldName>

               <value>true</value>

               <valueType>Literal</valueType>

             </criteria>

             <resultParameter>condition_output__3</resultParameter>

           </advancedCondition>

           <label>Condition</label>

           <name>Condition4</name>

           <resultIncluded>false</resultIncluded>

           <sequenceNumber>3</sequenceNumber>

           <shouldExposExecPathMsgOnly>true</shouldExposExecPathMsgOnly>

           <shouldExposeConditionDetails>false</shouldExposeConditionDetails>

           <shouldShowExplExternally>false</shouldShowExplExternally>

           <stepType>AdvancedCondition</stepType>

        </steps>

        <steps>

           <conditionExpression>

             <expression>IS10 == b</expression>

             <resultParameter>condition_output__2</resultParameter>

           </conditionExpression>

           <label>Condition</label>

           <name>Condition7</name>

           <parentStep>Branch</parentStep>

           <resultIncluded>false</resultIncluded>

           <sequenceNumber>1</sequenceNumber>

           <shouldExposExecPathMsgOnly>true</shouldExposExecPathMsgOnly>

           <shouldExposeConditionDetails>false</shouldExposeConditionDetails>

           <shouldShowExplExternally>false</shouldShowExplExternally>

           <stepType>Condition</stepType>

        </steps>

        <steps>

           <label>Default Lane</label>

           <name>DefaultLane</name>

           <parentStep>Branch</parentStep>

           <resultIncluded>false</resultIncluded>

           <sequenceNumber>2</sequenceNumber>

           <shouldExposExecPathMsgOnly>true</shouldExposExecPathMsgOnly>

           <shouldExposeConditionDetails>false</shouldExposeConditionDetails>

           <shouldShowExplExternally>false</shouldShowExplExternally>

           <stepType>DefaultPath</stepType>

        </steps>

        <steps>

           <actionType>AssignParameterValues</actionType>

           <assignment>

             <assignedParameter>a</assignedParameter>

             <expression>3</expression>

           </assignment>

           <failedExplainerTemplate>CalculationFailure</failedExplainerTemplate>

           <failedMessageTokenMappings>

             <expressionSetMessageToken>y2</expressionSetMessageToken>

             <resourceReference>a</resourceReference>

           </failedMessageTokenMappings>

           <label>CalculationStepWithTokensAndMappings</label>

           <name>CalculationStepWithTokensAndMappings</name>

```


Metadata Types ExpressionSetDefinition

```
           <passedExplainerTemplate>CalculationSuccess</passedExplainerTemplate>

           <passedMessageTokenMappings>

             <expressionSetMessageToken>y1</expressionSetMessageToken>

             <resourceReference>a</resourceReference>

           </passedMessageTokenMappings>

           <resultIncluded>false</resultIncluded>

           <sequenceNumber>1</sequenceNumber>

           <shouldExposExecPathMsgOnly>true</shouldExposExecPathMsgOnly>

           <shouldExposeConditionDetails>false</shouldExposeConditionDetails>

           <shouldShowExplExternally>true</shouldShowExplExternally>

           <stepType>BusinessKnowledgeModel</stepType>

        </steps>

        <variables>

           <collection>false</collection>

           <dataType>Boolean</dataType>

           <description>condition_output__3</description>

           <input>false</input>

           <name>condition_output__3</name>

           <output>false</output>

           <resultStep>Condition4</resultStep>

           <type>Variable</type>

           <value>False</value>

        </variables>

        <variables>

           <collection>false</collection>

           <dataType>Numeric</dataType>

           <decimalPlaces>2</decimalPlaces>

           <description>a</description>

           <input>true</input>

           <name>a</name>

           <output>false</output>

           <type>Variable</type>

           <value>10</value>

        </variables>

        <variables>

           <collection>false</collection>

           <dataType>Boolean</dataType>

           <description>condition_output__1</description>

           <input>false</input>

           <name>condition_output__1</name>

           <output>false</output>

           <resultStep>Condition</resultStep>

           <type>Variable</type>

           <value>False</value>

        </variables>

        <variables>

           <collection>false</collection>

           <dataType>Boolean</dataType>

           <description>condition_output__2</description>

           <input>false</input>

           <name>condition_output__2</name>

           <output>false</output>

           <resultStep>Condition7</resultStep>

           <type>Variable</type>

```


Metadata Types ExpressionSetDefinition

```
           <value>False</value>

        </variables>

        <variables>

           <collection>false</collection>

           <dataType>Numeric</dataType>

           <decimalPlaces>2</decimalPlaces>

           <description>IS10</description>

           <input>false</input>

           <name>IS10</name>

           <output>false</output>

           <type>Constant</type>

           <value>10</value>

        </variables>

        <variables>

           <collection>false</collection>

           <dataType>Numeric</dataType>

           <decimalPlaces>2</decimalPlaces>

           <description>b</description>

           <input>false</input>

           <name>b</name>

           <output>true</output>

           <type>Variable</type>

        </variables>

        <variables>

           <collection>false</collection>

           <dataType>Numeric</dataType>

           <decimalPlaces>2</decimalPlaces>

           <description>result</description>

           <input>false</input>

           <name>result</name>

           <output>true</output>

           <type>Variable</type>

        </variables>

        <versionNumber>1</versionNumber>

      </versions>

   </ExpressionSetDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package

    xmlns="http://soap.sforce.com/2006/04/metadata">

    <types>

     <members>*</members>

     <name>ExpressionSetDefinition</name>

    </types>

    <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/file_based.htm)


### Metadata Types ExpressionSetMessageToken ExpressionSetMessageToken

Represents an interface to retrieve, deploy, create, update, or delete information on Expression Set Message Token.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ExpressionSetMessageToken components have the suffix expressionSetMessageToken and are stored in the ExpressionSetMessageToken folder.

Version

### ExpressionSetMessageToken components are available in API version 59.0 and later.

Special Access Rules

InteractionCalculation.orgHasBREandDESAccess Org permission set license is required for users to access this metadata type.

Fields

**Field Name** **Description**

```
description

developerName

masterLabel

```

**Field Type**
string

**Description**

Required.

Description of the expression set message token.

**Field Type**
string

**Description**

Required.

Developer name of the expression set message token.

**Field Type**
string


### Metadata Types ExpressionSetObjectAlias

**Field Name** **Description**

**Description**

Required.

A user-friendly name for ExpressionSetMessageToken, which is defined when the
ExpressionSetMessageToken is created.

Declarative Metadata Sample Definition

The following is an example of an ExpressionSetMessageToken component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ExpressionSetMessageToken xmlns="http://soap.sforce.com/2006/04/metadata">

      <developerName>token</developerName>

      <description>Description</description>

      <masterLabel>token</masterLabel>

   </ExpressionSetMessageToken>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ExpressionSetMessageToken</name>

      </types>

      <version>59.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### ExpressionSetObjectAlias

Represents information about the alias of the source object that’s used in an expression set.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ExpressionSetObjectAlias components have the suffix .expressionSetObjectAlias and are stored in the

`expressionSetObjectAlias` folder.


Metadata Types ExpressionSetObjectAlias

Version

ExpressionSetObjectAlias components are available in API version 56.0 and later.

Fields

**Field Name** **Description**

```
dataType

mappings

objectApiName

usageType

```

**Field Type**
ExpsSetObjectDataType (enumeration of type string)

**Description**

Required.

The data type of the object alias.

Values are:

**•** `JSON`

**•** `sObject`

**Field Type**

ExpressionSetObjectAliasField[]

**Description**
The mapping between a source field and its corresponding field alias.

**Field Type**
string

**Description**

Required.

The API name of the top-level object, when the data type is sObject. The key of the
top-level object, when the data type is JSON.

**Field Type**
ExpsSetProcessType (enumeration of type string)

**Description**

Required.

The type of application associated with the industry that's using an expression set.
Your Salesforce org admin can define the values.

Valid values are:

**•** `Bre`

**•** `GpaCalculation`

**•** `InsuranceClaimProcessing` —Available in API version 65.0 and later.

**•** `ItServiceManagement` —Available in API version 65.0 and later.

**•** `PlanCostCalculation`


Metadata Types ExpressionSetObjectAlias

**Field Name** **Description**

**•** `RatingDiscovery`

**•** `StudentInformationSystem` —Available in API version 65.0 and later.

**•** `StudentSuccess`

When Business Rules Engine is enabled for a Salesforce instance, the default value is
' `Bre` ’. Other usage types are available to you depending on your industry solution
and permission sets.

ExpressionSetObjectAliasField

The fields associated with the source object for which the object alias is created.

**Field Name** **Description**

```
fieldAlias

sourceFieldName

```

**Field Type**
string

**Description**

Required.

The field alias associated with the source field name.

**Field Type**
string

**Description**

Required.

The name of the source field for which the field alias is created. The source field name
under an object alias must be unique.

Declarative Metadata Sample Definition

The following is an example of an ExpressionSetObjectAlias component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ExpressionSetObjectAlias xmlns="http://soap.sforce.com/2006/04/metadata">

   <dataType>sObject</dataType>

   <mappings>

     <fieldAlias>dum2</fieldAlias>

     <sourceFieldName>CreatedBy.Contact.Name</sourceFieldName>

   </mappings>

   <mappings>

     <fieldAlias>dum3</fieldAlias>

     <sourceFieldName>CreatedBy.Name</sourceFieldName>

   </mappings>

   <mappings>

     <fieldAlias>dum1</fieldAlias>

```


### Metadata Types ExternalAuthIdentityProvider

```
        <sourceFieldName>Owner.Contact.Name</sourceFieldName>

      </mappings>

      <objectApiName>Account</objectApiName>

      <usageType>Bre</usageType>

   </ExpressionSetObjectAlias>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package

    xmlns="http://soap.sforce.com/2006/04/metadata">

    <types>

     <members>*</members>

     <name>ExpressionSetObjectAlias</name>

    </types>

    <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/file_based.htm)

### ExternalAuthIdentityProvider

Represents an external authentication (auth) identity provider. An external auth identity provider links to an external credential and
obtains OAuth tokens for outbound callouts to external systems.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ExternalAuthIdentityProvider components have the suffix .externalAuthIdentityProvider and are stored in the

`externalAuthIdentityProviders` folder.

Version

### ExternalAuthIdentityProvider components are available in API version 62.0 and later.

Special Access Rules

Only users with the Customize Application permission or the Manage Named Credentials permission can access this type.


Metadata Types ExternalAuthIdentityProvider

Fields

**Field Name** **Description**

```
authenticationFlow

authenticationProtocol

description

externalAuthIdentityProviderParameters

label

```

**Field Type**
IdentityProviderAuthFlow (enumeration of type string)

**Description**

Required.

Authentication flow to get tokens to call protected APIs. Values are:

**•** `AuthorizationCode`

**•** `ClientCredentials`

**•** `SalesforceDefined`

**Field Type**
IdentityProviderAuthProtocol (enumeration of type string)

**Description**

Required.

The authentication protocol that’s required to access the external system. Values are:

**•** `OAuth`

**•** `SalesforceDefined`

**Field Type**
string

**Description**
A meaningful description of the external auth identity provider.

**Field Type**

ExternalAuthIdentityProviderParameter[]

**Description**
One or more sets of parameters that further configure the external auth identity
provider.

**Field Type**
string

**Description**

Required.

Name of the external auth identity provider.

ExternalAuthIdentityProviderParameter

Represents the parameters that configure an external auth identity provider.


Metadata Types ExternalAuthIdentityProvider

These parameters are used internally to provide a flexible architecture and are exposed here for packaging reasons.

**Field Name** **Description**

```
description

parameterName

parameterType

parameterValue

```

**Field Type**
string

**Description**
A human-readable description of this external auth identity provider parameter.

**Field Type**
string

**Description**

Required.

The name of the external auth identity provider parameter.

**Field Type**
ExtlIdentityProviderParmType (enumeration of type string)

**Description**

Required.

The type of external auth identity provider parameter. The value of this field drives the
behavior of the parameter. Values are:

**•** `AuthorizeRequestQueryParameter`

**•** `AuthorizeUrl`

**•** `ClientAuthentication`

**•** `CreatedByNamespace`

**•** `IdentityProviderOptions`

**•** `ManagedByComponent`

**•** `ManagedByFeature`

**•** `RefreshRequestBodyParameter`

**•** `RefreshRequestHttpHeader`

**•** `RefreshRequestQueryParameter`

**•** `StandardExternalIdentityProvider`

**•** `TokenRequestBodyParameter`

**•** `TokenRequestHttpHeader`

**•** `TokenRequestQueryParameter`

**•** `TokenUrl`

**•** `UserInfoUrl`

**Field Type**
string


Metadata Types ExternalAuthIdentityProvider

**Field Name** **Description**

**Description**
If the `parameterType` field describes a literal value, then this field stores the literal
value.

```
sequenceNumber

```

**Field Type**
int

**Description**
Specifies the order of parameters to apply when an external auth identity provider has
more than one parameter. Priority is from lower to higher numbers (for example, 1 is
the highest priority).

Declarative Metadata Sample Definition

The following is an example of an ExternalAuthIdentityProvider component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ExternalAuthIdentityProvider xmlns="http://soap.sforce.com/2006/04/metadata">

   <authenticationFlow>AuthorizationCode</authenticationFlow>

   <authenticationProtocol>OAuth</authenticationProtocol>

   <description>OAuth Browser flow for connected app</description>

   <externalAuthIdentityProviderParameter>

     <parameterName>TokenUrl</parameterName>

     <parameterType>TokenUrl</parameterType>

     <parameterValue>https://localhost:6101/services/oauth2/token</parameterValue>

     <sequenceNumber>1</sequenceNumber>

   </externalAuthIdentityProviderParameter>

   <externalAuthIdentityProviderParameter>

     <parameterName>AuthorizeUrl</parameterName>

     <parameterType>AuthorizeUrl</parameterType>

     <parameterValue>https://localhost:6101/services/oauth2/authorize</parameterValue>

     <sequenceNumber>2</sequenceNumber>

   </externalAuthIdentityProviderParameter>

   <label>exampleExtlIdp</label>

</ExternalAuthIdentityProvider>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>*</members>

     <name>ExternalAuthIdentityProvider</name>

   </types>

   <version>62.0</version>

</Package>

```


### Metadata Types ExternalClientApplication

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### ExternalClientApplication

Represents the header file for an external client application configuration.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ExternalClientApplication components have the suffix .eca and are stored in the externalClientApps folder.

Version

### ExternalClientApplication components are available in API version 59.0 and later.

Special Access Rules

Access to the ExternalClientApplication type requires orgs to enable the Opt in to External Client Apps permission in Setup.

Fields

**Field Name** **Description**

```
contactEmail

contactPhone

description

```

**Field Type**
string

**Description**
The email address that Salesforce uses to contact the external client app admin for
the subscriber org.

**Field Type**
string

**Description**
The phone number that Salesforce uses to contact the external client app admin for
the subscriber org.

**Field Type**
string


Metadata Types ExternalClientApplication

**Field Name** **Description**

**Description**
A description for the app.

```
distributionState

iconUrl

infoUrl

isProtected

label

logoUrl

managedType

```

**Field Type**
ExtlClntAppDistState (enumeration of type string)

**Description**
The distribution state of an external client app.

Values are:

**•** `AutoInstalled` . For internal use only.

**•** `Local` .

**•** `Managed` . For internal use only.

**•** `Packaged` .

**Field Type**
string

**Description**
The URL for the icon image.

**Field Type**
string

**Description**
Reserved for future use.

**Field Type**
boolean

**Description**
A package construct that developers use to control the visibility of components in
subscriber orgs. Default is false.

**Field Type**
string

**Description**
The label for the external client app.

**Field Type**
string

**Description**
The URL for the logo image.

**Field Type**
ExtlClntAppManagedType (enumeration of type string)


Metadata Types ExternalClientApplication

**Field Name** **Description**

**Description**
For internal use only.

```
orgScopedExternalApp

```

**Field Type**
string

**Description**
A unique ID consisting of the org ID and the name of this external client app. Either
defined by the developer or auto-generated during the first deployment. The expected
value uses this format: _`[Organization_ID]`_ : _`[External Client App`_
_`Name]`_ .

Declarative Metadata Sample Definition

This example shows an ExternalClientApplication component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ExternalClientApplication xmlns="http://soap.sforce.com/2006/04/metadata">

   <contactEmail>johndoe@example.com</contactEmail>

   <description>Test external client app</description>

   <distributionState>Local</distributionState>

   <iconUrl>https://icon.example.com</iconUrl>

   <infoUrl>https://info.example.com</infoUrl>

   <logoUrl>https://logo.example.com</logoUrl>

   <label>myeca</label>

   <isProtected>false</isProtected>

   <orgScopedExternalApp>Org_ID:External_Client_App_Name</orgScopedExternalApp>

</ExternalClientApplication>

```

This example `package.xml` references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>*</members>

     <name>ExternalClientApplication</name>

   </types>

   <types>

     <members>*</members>

     <name>ExtlClntAppOauthSettings</name>

   </types>

   <types>

     <members>*</members>

     <name>ExtlClntAppGlobalOauthSettings</name>

   </types>

   <types>

     <members>*</members>

     <name>ExtlClntAppOauthConfigurablePolicies</name>

   </types>

```


### Metadata Types ExternalCredential

```
      <types>

        <members>*</members>

        <name>ExtlClntAppConfigurablePolicies</name>

      </types>

      <version>60.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### ExternalCredential

Represents the details of how Salesforce authenticates to the external system.

Note: All credentials stored within this entity are encrypted under a framework that is consistent with other encryption frameworks
on the platform. Salesforce encrypts your credentials by auto-creating org-specific keys. Credentials encrypted using the previous
encryption scheme have been migrated to the new framework.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

### ExternalCredential components have the suffix .externalCredential and are stored in the externalCredentials folder.

Version

### ExternalCredential components are available in API version 56.0 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Description**

```
authenticationProtocol

```

**Field Type**
AuthenticationProtocol (enumeration of type string)

**Description**

Required.


Metadata Types ExternalCredential

**Field Name** **Description**

The authentication protocol that’s required to access the external system. Valid values
are:

**•** `AwsSv4`

**•** `Basic`

**•** `Custom`                     - User-created authentication. Specify the permission set, sequence
number, and authentication parameters. Each authentication parameter requires
a name and value.

**•** `Jwt`                     - Reserved for future use

**•** `JwtExchange`                     - Reserved for future use

**•** `NoAuthentication` —Reserved for future use

**•** `Oauth`

**•** `Password`                     - Reserved for future use

For connections to Amazon Web Services using Signature Version 4, use `AwsSv4` .

For connections using a direct token system, select `Jwt` .

For Simple URL data sources, select `Custom` with no parameters.

For cloud-based Files Connect external systems, select `Oauth` . For on-premises
systems, select `Password` .

```
description

externalCredentialParameters

label

```

**Field Type**
string

**Description**
A meaningful description of the external credential.

**Field Type**

ExternalCredentialParameter[]

**Description**
One or more sets of parameters that further configure the external credential.

**Field Type**
string

**Description**

Required.

Name of the external credential.

ExternalCredentialParameter

Represents the parameters that configure an external credential. External credential parameters are used to configure external credential
callouts through a combination of the type, name, and value and lookup fields. Available in API version 56.0 and later.

These parameters are used internally to provide a flexible architecture and are exposed here for packaging reasons.


Metadata Types ExternalCredential

**Field Name** **Description**

```
authProvider

certificate

description

externalAuthIdentityProvider

parameterGroup

parameterName

```

**Field Type**
string

**Description**
Reference to an authentication provider that the `AuthProvider` component
represents, which defines the service that provides the login process and approves
access to the external system.

**Type**
string

**Description**
If the value of `parameterType` is `SigningCertificate`, then this field
references the certificate.

**Field Type**
string

**Description**
A human-readable description of this external credential parameter.

**Field Type**
string

**Description**
Reference to an external authentication identity provider that the
`externalAuthIdentityProvider` component represents. The
`externalAuthIdentityProvider` defines the service that provides the login
process and approves access to the external system.

To simplify the configuration process for the authentication providers used by your
named credentials, use an `externalAuthIdentityProvider` instead of an
`authProvider` . Link the external auth identity provider to an external credential.

**Field Type**
string

**Description**
Groups a parameter along with its respective principal. For example, with dynamic
scopes, the user can apply a scope `AuthParameter` only when authenticated
against a specific principal with a matching `parameterGroup` value.

If a value for `parameterGroup` isn’t provided, `parameterGroup` defaults to
the `parameterName` value for PER_USER and NAMED_PRINCIPAL. For all other
parameters `parameterGroup` defaults to DEFAULT_GROUP.

**Field Type**
string


Metadata Types ExternalCredential

**Field Name** **Description**

**Description**

Required.

The name of the external credential parameter.

```
parameterType

```

**Field Type**
ExternalCredentialParamType (enumeration of type string)

**Description**

Required.

The type of external credential parameter. The value of this field drives the behavior
of the parameter. Valid values are:

**•** `AdditionalRefreshStatusCode` : Allows the user to specify 4 _`xx`_, 6 _`xx`_,
7 _`xx`_, 8 _`xx`_, and 9 _`xx`_ HTTP status codes that trigger Salesforce to refresh expired
or invalid access tokens, in addition to the standard `401` HTTP status code
response.

**•** `AuthHeader` : Allows the user to specify custom authentication headers to be
added to the callout at run time. When using `AuthHeader`, the
`parameterName` field must be the header name as a string, and
`parameterValue` must be a formula of a header value that is evaluated at
run time. `sequenceNumber` determines the order in which headers are sent
out in the callout. Headers with lower numbers are sent out first.

**•** `AuthParameter` : Allows the user to add additional authentication settings.
`parameterName` defines the parameter to set. For example, `AwsRegion`
sets the AWS Region parameter to apply for an AWS Signature V4 authentication
protocol and `parameterValue` is the value for the AWS Region.

**•** `AuthProtocolVariant` : Used to specify a variant of an authentication
protocol. For example, `Aws Sts` as a variant when the `ParameterName` is
`AwsSv4` and the `ParameterValue` is `AwsSv4_STS` .

**•** `AuthProvider` : Specifies that this parameter configures an authentication
provider referenced by the `authProvider` field.

**•** `AuthProviderUrl` : Specifies the authentication endpoint URL. For example,
if the authentication type is OAuth with JWT Bearer Flow, then
`parameterValue` is an authentication token endpoint.

**•** `AuthProviderUrlQueryParameter` : Allows the user to specify custom
query parameters to be added to the callout to the authentication provider at run
time. Currently, supported only for AWS Signature V4 with STS. The allowed
`AuthProviderUrlQueryParameter` values are `AwsExternalId` and
`AwsDuration`, used with AWS STS.

**•** `AwsStsPrincipal` : Configures AWS Signature V4 along with STS.
`parameterName` is `AwsStsPrincipal` and `parameterValue` isn’t
specified.

**•** `CreatedByNamespace` : Reserved for internal use.

**•** `CustomPrincipal` : Reserved for internal use.


Metadata Types ExternalCredential

**Field Name** **Description**

**•** `ExternalAuthIdentityProvider` : Specifies that this parameter
configures an authentication provider referenced by the
`externalAuthIdentityProvider` field.

**•** `GlobalNamedPrincipal` : Reserved for internal use.

**•** `JwtBodyClaim` : Specifies a JWT (JSON Web Token) body claim, where
`parameterName` is the key and `parameterValue` is the value. For example,
the parameter name for a JWT audience is `aud` .

**•** `JwtHeaderClaim` : Specifies a JWT header claim, where `parameterName`
is the key and `parameterValue` is the value. For example, the parameter
name for a JWT key identifier is `kid` .

**•** `ManagedByComponent` : Reserved for internal use.

**•** `ManagedByFeature` : Reserved for internal use.

**•** `NamedPrincipal` : Specifies that the parameter uses the same set of user
credentials for all users who access the external system.

**•** `PerUserPrincipal` : Provides access control at the individual user level.

**•** `PrincipalIdentityAlias` : Reserved for internal use.

**•** `SfHttpRequestExtensionName` : Reserved for internal use.

**•** `SigningCertificate` : Specifies the certificate used for an authentication
signature. Use the `certificate` field to specify the certificate name. Used for
OAuth with JWT Bearer Flow and AwsSv4 STS with RolesAnywhere authentication.

**•** `SystemUserPrincipal` : Reserved for internal use.

```
parameterValue

principal

sequenceNumber

```

**Field Type**
string

**Description**
If the `parameterType` field describes a literal value then the literal value is stored
in this field.

**Field Type**
string

**Description**
If the value of the `parameterType` field is either `NamedPrincipal` or
`PerUserPrincipal`, this field points to a permission set. That value then
determines the set of users that are allowed to use credentials provided by the
credential provider. The value of the `parameterName` field specifies the name of
this principal.

**First available in API version 56.0, this field is removed in API version 58.0 and**
**later.**

**Field Type**
int


Metadata Types ExternalCredential

**Field Name** **Description**

**Description**
Specifies the order of principals to apply when a user participates in more than one
principal. For example, a user could be part of multiple permission sets that are
applicable for a credential provider. Priority is from lower to higher numbers.

You can set this field only when `parameterType` is `NamedPrincipal` .

Declarative Metadata Sample Definition

The following is an example of an ExternalCredential component.

```
   <ExternalCredential xmlns="http://soap.sforce.com/2006/04/metadata">

      <label>SampleExternalCredential</label>

      <authenticationProtocol>AwsSv4</authenticationProtocol>

      <externalCredentialParameters>

        <parameterName>Principal</parameterName>

        <parameterType>NamedPrincipal</parameterType>

        <sequenceNumber>1</sequenceNumber>

      </externalCredentialParameters>

      <externalCredentialParameters>

        <parameterName>AwsService</parameterName>

        <parameterValue>iam</parameterValue>

        <parameterType>AuthParameter</parameterType>

      </externalCredentialParameters>

      <externalCredentialParameters>

        <parameterName>AwsRegion</parameterName>

        <parameterValue>us-east-1</parameterValue>

        <parameterType>AuthParameter</parameterType>

      </externalCredentialParameters>

   </ExternalCredential>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ExternalCredential</name>

      </types>

      <version>56.0</version>

   </Package>

```


### Metadata Types ExternalAIModel

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/file_based_zip_file.htm)

SEE ALSO:

NamedCredential

_Salesforce Help_ [: Named Credentials](https://help.salesforce.com/s/articleView?id=xcloud.named_credentials_about.htm&type=5&language=en_US)

_Named Credentials Developer Guide_ [: Get Started with Named Credentials](https://developer.salesforce.com/docs/platform/named-credentials/guide/get-started.html)

_[Named Credentials Developer Guide](https://developer.salesforce.com/docs/platform/named-credentials/references/named-credentials-reference/nc-api-links.html)_ : Named Credential API Links

_Apex Developer Guide_ [: Invoking Callouts Using Apex](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_callouts.htm)

_Apex Developer Guide_ [: Named Credentials as Callout Endpoints](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_callouts_named_credentials.htm)

### ExternalAIModel

Represents the state of a given model for an Einstein for Service feature, such as Einstein Reply Recommendations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ExternalAIModel components have the suffix .externalAIModel and are stored in the externalAIModels folder.

Version

### ExternalAIModel components are available in API version 51.0 and later.

Special Access Rules

This type is available only when an org is configured to access the application in the `applicationSourceType` field. For example,
if `applicationSourceType` is set to `ARTICLE_RECOMMENDATION`, this type is available only if Einstein Article
Recommendations is enabled in the org and the Main Services Agreement has been accepted.

Fields

**Field Name** **Field Type** **Description**

```
applicationSourceType

```

ApplicationSourceType Required. The target application for the configuration. Valid values are:
(enumeration of

**•** `REPLY_RECOMMENDATION`        - Einstein Reply

type string)

Recommendations

**•** `ARTICLE_RECOMMENDATION`        - Einstein Article
Recommendations


Metadata Types ExternalAIModel

**Field Name** **Field Type** **Description**

**•** `UTTERANCE_RECOMMENDATION`                           - Einstein Bot utterances

**•** `FAQ`                           - Einstein Bot frequently asked questions

`externalModelKey` string Required. Unique key which identifies external model
corresponding this applicationType

```
externalModelStatus

```

ExternalModelStatus Required. The current state of a given model. Valid values are:
(enumeration of

**•** `DISABLED`

type string)

**•** `DISABLED`

**•** `ENABLED`

**•** `PAUSED`

`name` string Required. A reference to the configuration.

`threshold` double Threshold override value for this model. Nillable.

`trainingJobName` string Training job path corresponding to the given model. Nillable.

Declarative Metadata Sample Definition

The following is an example of an ExternalAIModel component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ExternalAIModel xmlns="http://soap.sforce.com/2006/04/metadata">

   <applicationSourceType>REPLY_RECOMMENDATION</applicationSourceType>

   <externalModelKey>0f16dea6-b886-44df-9cfa-4d96b51d6594</externalModelKey>

   <externalModelStatus>ENABLED</externalModelStatus>

   <name>SR1601228426202</name>

   <threshold>0.9</threshold>

   <trainingJobName>TestJob</trainingJobName>

</ExternalAIModel>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>*</members>

     <name>ExternalAIModel</name>

   </types>

</Package>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types ExternalServiceRegistration ExternalServiceRegistration

Represents the external service configuration for an org.

File Suffix and Directory Location

### ExternalServiceRegistration components have the suffix .externalServiceRegistration and are stored in the

`externalServiceRegistrations` folder.

Version

### ExternalServiceRegistration components are available in API version 39.0 and later.

Fields

**Field Name** **Field Type** **Description**

`catalogedApiVersion` string

A version of an API brought into API Catalog from an external source
and managed for consumption in Salesforce. Available in API version
65.0 and later.

`description` string The external service description defined when the service is created.

`label` string Required. The service name as it appears on the External Services wizard.

`namedCredential` string The reference by name to be used for the service.

`namedCredentialReferenceId` reference

The reference by ID to be used for the named credential. When used,
supersedes `namedCredential` . Available in API version 57.0 and
later.

`operations` ExternalServiceOperation[] Items defined for this operation.

`registrationProvider` string A reference to the registration provider.

**•** If the registrationProviderType is `ExternalConnector`, this
field contains the external connector name.

**•** If the registrationProviderType is `Heroku`, this field contains the
HerokuAppLink ID.

**•** For any other registrationProviderType value, this field is blank and
reserved for future use.

`registrationProviderAsset` string A polymorphic foreign key field that contains the name of the asset
related to the external service registration.

**•** For an external service registration created for a named query, this
field contains the named query API name.

**•** For an external service registration created for an Apex class that has
methods exposed as REST resources or methods that are
Aura-enabled. This field contains the Apex class name.


Metadata Types ExternalServiceRegistration

**Field Name** **Field Type** **Description**

Available in API version 66.0 and later.

```
registrationProviderType

```

ExternalServiceRegistrationProviderType Indicates the source of the API specification registered with the External
(enumeration of Services wizard. Valid values include:
type string)

**•** `AgentActionOutputs` —Reserved for internal use.

**•** `AgentToAgent` —The API specification represents the external
service schemas that enable communication between AI agents.
Available in API version 66.0 and later.

**•** `Anypoint` —The API specification is managed in the MuleSoft
Anypoint Platform. Available in API version 63.0 and later.

**•** `AnypointPublic` —Reserved for internal use.

**•** `ApexRest` —The API specification was created from an Apex REST
class. Available in API version 63.0 and later.

**•** `AuraEnabled` —The API specification was created from an Apex
class that has AuraEnabled methods. Available in API version 65.0
and later.

**•** `CodeExtension` —Reserved for internal use.

**•** `ContextDef` —The API specification used to create dynamic Apex
classes for the related context definition structure. Available in API
version 66.0 and later.

**•** `Custom` —The API specification was manually configured.

**•** `CustomExternalConnector` —The API specification
represents a custom partner-created version of an external
connection. Available in API version 66.0 and later.

**•** `DocumentProcessing` —Reserved for internal use.

**•** `ExternalConnector` —The API specification represents an
external connection.

**•** `Heroku` —The API specification represents a Heroku app.

**•** `MuleSoft` —The API specification was selected from MuleSoft.
Use Anypoint for MuleSoft for Agentforce: API Catalog MuleSoft
sources.

**•** `NamedQuery` —The API specification represents a named query
REST endpoint. Available in API version 64.0 and later.

**•** `SchemaInferred` —The API specification was provided during
the HTTP Callout configuration process. Available in API version 57.0
and later.

**•** `Standard` —The API specification was defined when an external
service was created.

`schema` string The content of the OpenAPI 2.0.x or OpenAPI 3.0.x schema in JSON or
YAML format. Nillable.

`schemaAbsoluteUrl` string The full, absolute URL to the schema. Populated when a user selects
**Absolute URL** during registration.


Metadata Types ExternalServiceRegistration

**Field Name** **Field Type** **Description**

`schemaType` string The schema format. OpenAPI for Open API 2.0.x or Open API 3.0.x. If not
specified, schema type is derived based on the schema content. Nillable.

`schemaUploadFileExtension` string The file’s extension. Populated when a user selects **Upload from local**
during registration.

`schemaUploadFileName` string The file’s name without the file extension. Populated when a user selects
**Upload from local** during registration.

`schemaUrl` string The path must begin with "/" and be relative to the named credential
endpoint.

`serviceBinding` string

`serviceName` string

Used to map non-supported media types for this external service
registration to supported media types. Nillable. Available in API version
53.0 and later.

The name of the cataloged API service that this external service
registration belongs to. Available in API version 63.0 and later. This field
was removed in API version 65.0.

`status` string Required. Indicates service registration status. Valid values include:

**•** `complete` —The API spec is valid and the registration is ready to
use.

**•** `incomplete` —The service registration hasn’t completed.

`systemVersion` int

The internal version of External Services that is used to register the API
specification. Available in API version 55.0 and later. The system versions
are independent of API versions.

**•** `1` —Retired legacy External Services.

**•** `2` —External Services with limitations on object and operation name
length.

**•** `3` —External Services automatically derives developer names fitting
within 80 characters.

**•** `4` —Removed the default character set when making a callout to an
external service. To specify a character set, include it in the OpenAPI
specification, for example: `contentType:`
`application/xml; charset=utf-8` .

**•** `5` —Introduced asynchronous callouts with callbacks from Apex.

**•** `6` —Added support for OpenAPI Specification (OAS) discriminator
mapping.

**•** `7` —Added support for property names that begin with a number.

For input parameters on invocable actions, encodes the keyword
`connection` as `reconnection` .

**•** `8` —Current version.

This field is read-only. You can’t upgrade an external service to a newer
system version. To take advantage of functionality in a newer system


Metadata Types ExternalServiceRegistration

**Field Name** **Field Type** **Description**

version, you must create an external service using the same OpenAPI
spec and then replace any references to the old external service. See
[Register an External Service in Salesforce Help.](https://help.salesforce.com/s/articleView?id=platform.external_services_register.htm&language=en_US)

ExternalServiceOperation

**Field Name** **Field Type** **Description**

`active` boolean Required. Indicates whether the operation is active ( `true` ), or inactive
( `false` ).

`name` string Required. The operation’s name.

Declarative Metadata Sample Definition

The following is an example of an ExternalServiceRegistration component that references an external credit service.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ExternalServiceRegistration xmlns="http://soap.sforce.com/2006/04/metadata">

     <label>BankService</label>

     <namedCredential>Bank</namedCredential>

     <schema>{

     "swagger": "2.0",

     "basePath": "/",

     "info": {

      "version": "1.0",

      "title": "External Service for demo bank",

      "description": "### External Service for demo bank",

      "x-vcap-service-name": "DemoBankRestServices"

     },

     ...

     "paths": {

     "/accounts/{accountName}": {

       ...

      }

     },

     "definitions": {

      "accountDetails": {

       ...

      },

      "errorModel": {

       ...

      }

     }

   }</schema>

     <schemaType>OpenApi</schemaType>

     <schemaUrl>/accounts/schema</schemaUrl>

     <status>Complete</status>

   </ExternalServiceRegistration>

```


### Metadata Types ExtlClntAppCanvasSettings

serviceBinding

The following JSON-encoded string defines the mapping of a non-supported media type to a supported media type for external service
request and response body serialization.

```
   {"compatibleMediaTypes":{

      "application/x-acme-json":"application/json"

   }}

```

The non-supported media type `application/x-acme-json` is mapped to the supported media type `application/json`
for this External Services registration. The External Services runtime considers the non-supported media type for request and response
header processing. It serializes the request and response content by the mapped supported media type.

SEE ALSO:

_Salesforce Help_ [: Media Type Mapping in External Service Registrations](https://help.salesforce.com/s/articleView?id=platform.external_services_mime_type_mapping.htm&type=5&language=en_US)

### ExtlClntAppCanvasSettings

Represents an external client app’s canvas app settings.

Parent Type and Manifest Access

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ExtlClntAppCanvasSettings components have the suffix .ecaCanvas and are stored in the

`extlClntAppCanvasSettings` folder.

Version

### ExtlClntAppCanvasSettings components are available in API version 66.0 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Field Type** **Description**

`accessMethod` AccessMethod (enumeration of type string) Required. Indicates how the canvas app initiates the
OAuth authentication flow. The valid values are:

**•** `Get` —OAuth authentication is used, and the
user is prompted to allow the third-party
application to access their information. When you


Metadata Types ExtlClntAppCanvasSettings

**Field Name** **Field Type** **Description**

use this access method, the canvas app must
initiate the OAuth authentication flow.

**•** `Post` —OAuth authentication is used, but when
the administrator installs the canvas app, they
implicitly allow access for users. Therefore, the
user isn’t prompted to allow the third party to
access their user information. When you use this
access method, the authentication is posted
directly to the canvas app URL.

`canvasLocationOptions` CanvasLocationOptions (enumeration of type string)[] Indicates where the canvas app can appear to the
user. The valid values are:

**•** `Aura` —The canvas app can appear in a custom
Lightning component.

**•** `ChatterFeed` —The canvas app can appear
as a Chatter feed item.

**•** `MobileNav` —The canvas app can appear in a
mobile card in the Salesforce mobile app.

**•** `None` —The canvas app can appear only in the
Canvas App Previewer.

**•** `PageLayout` —The canvas app can appear on
a page layout. When viewed in the Salesforce
mobile app, the canvas app appears in the record
detail page.

**•** `Publisher` —The canvas app can appear as a
global action.

**•** `Visualforce` —The canvas app can appear
on a Visualforce page.

`canvasOptions` CanvasOptions (enumeration of type string)[]

Indicates whether to hide the **Share** button and
header in the publisher for your canvas app. Valid
values are:

**•** `HideShare` —The **Share** button is hidden in
the publisher for the related canvas app.

**•** `HideHeader` —The header is hidden in the
publisher for the related canvas app.

`canvasUrl` string Required. The URL of the third-party app that’s
exposed as a canvas app.

`externalClientApplication` string Required. The name of the associated external client
app.

`label` string The name of the app.

`lifeCycleHandler` string The name of the lifecycle handler Apex class.


Metadata Types ExtlClntAppCanvasSettings

**Field Name** **Field Type** **Description**

`samlInitiationMethod` SamlInitiationMethod (enumeration of type string) If you’re using SAML single sign-on (SSO), indicates
which provider initiates the SSO flow.

**•** `IdpInitiated` —Identity provider initiated.
Salesforce makes the initial request to start the
SSO flow.

**•** `SpInitiated` —Service provider initiated. The
canvas app starts the SSO flow after it’s invoked.

**•** `None` —The canvas app isn’t using SAML SSO.

Declarative Metadata Sample Definition

The following is an example of a ExtlClntAppCanvasSettings component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ExtlClntAppCanvasSettings xmlns="http://soap.sforce.com/2006/04/metadata">

      <accessMethod>Post</accessMethod>

      <canvasUrl>https://www.example.com</canvasUrl>

      <canvasLocationOptions>Aura</canvasLocationOptions>

      <canvasLocationOptions>Visualforce</canvasLocationOptions>

      <canvasOptions>HideHeader</canvasOptions>

      <label>My external client app settings for canvas</label>

      <samlInitiationMethod>None</samlInitiationMethod>

      <externalClientApplication>testCanvasECA</externalClientApplication>

   </ExtlClntAppCanvasSettings>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ExternalClientApplication</name>

      </types>

      <types>

        <members>*</members>

        <name>ExtlClntAppOauthSettings</name>

      </types>

      <types>

        <members>*</members>

        <name>ExtlClntAppCanvasSettings</name>

      </types>

      <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types ExtlClntAppConfigurablePolicies ExtlClntAppConfigurablePolicies

Represents the policies for an external client app to disable or enable plugins.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ExtlClntAppConfigurablePolicies components have the suffix .ecaPlcy and are stored in the extlClntAppPolicies folder.

Version

### ExtlClntAppConfigurablePolicies components are available in API version 60.0 and later.

Special Access Rules

The View all External Client Apps, view their settings, and edit their policies user permission is required for users with admin roles to
configure OAuth policies.

Fields

**Field Name** **Description**

```
externalClientApplication

isEnabled

isCanvasPluginEnabled

```

**Field Type**
string

**Description**

Required.

The name of the external client app associated with the plugins.

**Field Type**
boolean

**Description**

Required.

If `true`, all plugins are enabled unless individually disabled. If `false`, all plugins are
disabled. The default value is `true` . Available in API version 60.0 and later.

**Field Type**
boolean

**Description**
If `true`, the Canvas app plugin is enabled. If `false`, the Canvas app plugin is disabled.
The default value is `true` . Available in API version 66.0 and later.


Metadata Types ExtlClntAppConfigurablePolicies

**Field Name** **Description**

```
isMobilePluginEnabled

isNotificationPluginEnabled

isOauthPluginEnabled

isPushPluginEnabled

isSamlPluginEnabled

label

startPage

```

**Field Type**
boolean

**Description**
If `true`, the Mobile plugin is enabled. If `false`, the Mobile plugin is disabled. The
default value is `true` . Available in API version 63.0 and later.

**Field Type**
boolean

**Description**
If `true`, the Notification plugin is enabled. If `false`, the Notification plugin is
disabled. The default value is `true` . Available in API version 63.0 and later.

**Field Type**
boolean

**Description**
If `true`, the OAuth plugin is enabled. If `false`, the OAuth plugin is disabled. The
default value is `true` . Available in API version 60.0 and later.

**Field Type**
boolean

**Description**
If `true`, the Push Notification plugin is enabled. If `false`, the Push Notification
plugin is disabled. The default value is `true` . Available in API version 63.0 and later.

**Field Type**
boolean

**Description**
If `true`, the SAML plugin is enabled. If `false`, the SAML plugin is disabled. The
default value is `true` . Available in API version 63.0 and later.

**Field Type**
string

**Description**
The OAuth policies name for the external client app.

**Field Type**
ExtlClntAppStartPage (enumeration type of string)

**Description**
Determines which URL to use for the start page.

**•** Custom

**•** None

**•** OAuth


Metadata Types ExtlClntAppConfigurablePolicies

**Field Name** **Description**

Available in API version 63.0 and later.

startUrl

**Field Type**
string

**Description**
The custom URL where users are directed after they authenticate. For example, direct
users to a specific page in the service provider app. Available in API version 63.0 and
later.

Declarative Metadata Sample Definition

This example shows an ExtlClntAppConfigurablePolicies component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ExtlClntAppConfigurablePolicies xmlns="http://soap.sforce.com/2006/04/metadata">

   <externalClientApplication>myeca</externalClientApplication>

   <isEnabled>true</isEnabled>

....<isCanvasPluginEnabled>true</isCanvasPluginEnabled>

   <isMobilePluginEnabled>true</isMobilePluginEnabled>

   <isNotificationPluginEnabled>true</isNotificationPluginEnabled>

   <isOauthPluginEnabled>true</isOauthPluginEnabled>

   <isPushPluginEnabled>true</isPushPluginEnabled>

   <isSamlPluginEnabled>true</isSamlPluginEnabled>

   <label>myecapolicy</label>

   <startPage>OAuth</startPage>

   <startUrl>https://example.org</startUrl>

</ExtlClntAppConfigurablePolicies>

```

This example `package.xml` references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>*</members>

     <name>ExternalClientApplication</name>

   </types>

   <types>

     <members>*</members>

     <name>ExtlClntAppOauthSettings</name>

   </types>

   <types>

     <members>*</members>

     <name>ExtlClntAppGlobalOauthSettings</name>

   </types>

   <types>

     <members>*</members>

     <name>ExtlClntAppOauthConfigurablePolicies</name>

   </types>

   <types>

     <members>*</members>

```


### Metadata Types ExtlClntAppGlobalOauthSettings

```
        <name>ExtlClntAppConfigurablePolicies</name>

      </types>

      <version>60.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### ExtlClntAppGlobalOauthSettings

Represents the global settings for the OAuth plugin in an external client app. These settings include private and sensitive OAuth consumer
information that can’t be packaged and must not be added to source control.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ExtlClntAppGlobalOauthSettings components have the suffix .ecaGlblOauth and are stored in the

`extlClntAppGlobalOauthSets` folder.

Version

### ExtlClntAppGlobalOauthSettings components are available in API version 59.0 and later.

Special Access Rules

Access to the OAuth plugin requires orgs to enable the Allow Access to OAuth Consumer Secrets via Metadata API permission in Setup.
The View External Client Apps Consumer Secrets in Metadata user permission is required for users with developer roles to configure
global OAuth settings.

Fields

**Field Name** **Description**

```
callbackUrl

```

**Field Type**
string

**Description**
The endpoint that Salesforce calls back to your external client app during OAuth. It’s
the OAuth redirect_uri.


Metadata Types ExtlClntAppGlobalOauthSettings

**Field Name** **Description**

```
certificate

consumerKey

consumerSecret

externalClientApplication

idTokenConfig

isClientCredentialsFlowEnabled

isCodeCredFlowEnabled

```

**Field Type**
string

**Description**
If the app uses a certificate, the PEM-encoded certificate string. When provided, it
enables the JWT Bearer flow. Available in API version 60.0 and later.

**Field Type**
string

**Description**
A value used by the consumer for identification to Salesforce. Referred to as client_id
in OAuth 2.0.

**Field Type**
string

**Description**
A value that is combined with the `consumerKey` and used by the consumer for
identification to Salesforce. Referred to as client_secret in OAuth 2.0.

**Field Type**
string

**Description**

Required.

Name of the external client application.

**Field Type**

ExternalAppIdTokenConfig

**Description**
The settings for the ID token.

**Field Type**
boolean

**Description**
If set to `true`, the OAuth 2.0 client credentials flow is enabled. Available in API version
60.0 and later.

**Field Type**
boolean

**Description**
If set to `true`, the external client app can use the Authorization Code and Credentials
Flow and its variations for headless login, passwordless login, and guest user identity
services in an off-platform app. Headless registration isn’t currently supported for
external client apps. The default value is `false` .


Metadata Types ExtlClntAppGlobalOauthSettings

**Field Name** **Description**

To use this field, the Authorization Code and Credentials Flow must be enabled for
your org in OAuth and OpenID Connect settings.

Available in API version 61.0 and later.

```
isCodeCredPostOnly

isConsumerSecretOptional

isDeviceFlowEnabled

isIntrospectAllTokens

isNamedUserJwtEnabled

```

**Field Type**
boolean

**Description**
If set to `true`, for the Authorization Code and Credentials Flow, the external client
app is required to send the user’s credentials to the Salesforce
`services/oauth2/authorize` endpoint in the body of a POST request. If set
to `false`, the app can send a POST or GET request with the user’s credentials in the
request body or in a Basic authorization header. The default value is `false` .

To use this field, the Authorization Code and Credentials Flow must be enabled for
your external client app. Headless registration, a variation of this flow, isn’t currently
supported for external client apps.

Available in API version 61.0 and later.

**Field Type**
boolean

**Description**
If set to `false` (default), the external app’s client secret is required in exchange for
an access token in the OAuth 2.0 web server flow. If set to `true`, the external app’s
client secret is optional.

**Field Type**
boolean

**Description**
If set to `true`, the external client app can use the OAuth 2.0 device flow. Available in
API version 60.0 and later.

**Field Type**
boolean

**Description**
If set to `true`, authorizes the external app to introspect all access and refresh all
tokens. If set to `false` (default), the external client app can introspect its own tokens.

**Field Type**
boolean

**Description**
If set to `true`, the external client app issues JSON Web Token (JWT)-based access
tokens. If set to `false`, it issues opaque access tokens. The default value is `false`

Available in API version 61.0 and later.


Metadata Types ExtlClntAppGlobalOauthSettings

**Field Name** **Description**

```
isPkceRequired

isRefreshTokenRotationEnabled

isSecretRequiredForRefreshToken

isSecretRequiredForTokenExchange

isTokenExchangeEnabled

label

shouldRotateConsumerKey

```

**Field Type**
boolean

**Description**
If set to `true` (default) Proof Key for Code for Exchange (PKCE) is required for OAuth
integration. If set to `false`, PKCE is optional.

**Field Type**
boolean

**Description**
If set to `true`, the refresh token rotation is enabled. Available in API version 60.0 and
later.

**Field Type**
boolean

**Description**
If set to `true` (default), the app’s client secret is required in the authorization request
of a refresh token and hybrid refresh token flow. If set to `false` and an app sends
the client secret in the authorization request, Salesforce still validates it.

**Field Type**
boolean

**Description**
If set to `true`, the app’s client secret is required for token exchange. Available in API
version 60.0 and later.

**Field Type**
boolean

**Description**
If set to `true`, token exchange is enabled. Available in API version 60.0 and later.

**Field Type**
string

**Description**
External Client Application Global OAuth Settings name.

**Field Type**
boolean

**Description**
If set to `true`, the OAuth external client app's consumer key is replaced with a newly
generated key on metadata deploy.. To maintain security, if this field is set to `true`,
you must include the ignore warnings attribute in the deploy command. Default is
`false` .


Metadata Types ExtlClntAppGlobalOauthSettings

**Field Name** **Description**

```
shouldRotateConsumerSecret

```

**Field Type**
boolean

**Description**
If set to `true`, the OAuth external client app’s consumer secret is replaced with a
newly generated secret on metadata deploy. To maintain security, if this field is set to
`true`, you must include the ignore warnings attribute in the deploy command. Default
is `false` .

ExternalAppIdTokenConfig

Represents configurations that determine the ID token attributes.

**Field Name** **Description**

```
idTokenAudience

idTokenIncludeAttributes

idTokenIncludeStandardClaims

idTokenValidityInMinutes

```

**Field Type**
string

**Description**
The audience that this ID token is intended for. The value is an array of case-sensitive
strings. If no audiences are specified, the `client_id` of the relying party is returned
as the default audience. Otherwise, the other audiences are returned with the
`client_id` in the `aud` value.

**Field Type**
boolean

**Description**
Indicates whether attributes are included in the ID token ( `true` ) or not ( `false` ).

**Field Type**
boolean

**Description**
Indicates whether standard claims about the authentication event are included in the
ID token ( `true` ) or not ( `false` ).

**Field Type**
int

**Description**
The length of time that the ID token is valid for after it’s issued. The value can be 1–720
minutes. The default value is 2 minutes.


Metadata Types ExtlClntAppGlobalOauthSettings

Declarative Metadata Sample Definition

This example shows an ExtlClntAppGlobalOauthSettings component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ExtlClntAppGlobalOauthSettings xmlns="http://soap.sforce.com/2006/04/metadata">

      <callbackUrl>https://www.example.com</callbackUrl>

      <externalClientApplication>myeca</externalClientApplication>

      <idTokenConfig>

        <idTokenAudience>SalesforceAudience</idTokenAudience>

        <idTokenIncludeStandardClaims>true</idTokenIncludeStandardClaims>

        <idTokenValidityInMinutes>0</idTokenValidityInMinutes>

      </idTokenConfig>

      <isConsumerSecretOptional>false</isConsumerSecretOptional>

      <isIntrospectAllTokens>false</isIntrospectAllTokens>

      <isPkceRequired>true</isPkceRequired>

      <isSecretRequiredForRefreshToken>false</isSecretRequiredForRefreshToken>

      <label>myecaglobalset</label>

      <shouldRotateConsumerKey>false</shouldRotateConsumerKey>

      <shouldRotateConsumerSecret>false</shouldRotateConsumerSecret>

   </ExtlClntAppGlobalOauthSettings>

```

This example `package.xml` references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ExternalClientApplication</name>

      </types>

      <types>

        <members>*</members>

        <name>ExtlClntAppOauthSettings</name>

      </types>

      <types>

        <members>*</members>

        <name>ExtlClntAppGlobalOauthSettings</name>

      </types>

      <types>

        <members>*</members>

        <name>ExtlClntAppOauthConfigurablePolicies</name>

      </types>

      <types>

        <members>*</members>

        <name>ExtlClntAppConfigurablePolicies</name>

      </types>

      <version>60.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types ExtlClntAppMobileConfigurablePolicies ExtlClntAppMobileConfigurablePolicies

Represents an external client app’s mobile policies configuration.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ExtlClntAppMobileConfigurablePolicies components have the suffix .ecaMobilePlcy and are stored in the

`extlClntAppMobilePolicies` folder.

Version

### ExtlClntAppMobileConfigurablePolicies components are available in API version 64.0 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Field Type** **Description**

externalClientApplication string Required. The name of the associated external client app.

label string Label for the external client app’s mobile policies configuration.

screenLockTimeout

ScreenLockTimeout When `isScreenLockEnabled` is true in the associated
[(enumeration](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_objects_intro.htm#enumeration_title) of ExtlClntAppMobileSettings metadata type, `screenLockTimeout`
type string) represents the amount of time after which the mobile app locks and

requires the app user to reauthenticate. Valid values include:

**•** _`Never`_

**•** _`One`_ (1 minute)

**•** _`Five`_ (5 minutes)

**•** _`Ten`_ (10 minutes)

**•** _`Thirty`_ (30 minutes)

**•** _`Sixty`_ (60 minutes)

**•** _`OneTwenty`_ (120 minutes)

**•** _`OneEighty`_ (180 minutes)

**•** _`TwoForty`_ (240 minutes)


### Metadata Types ExtlClntAppMobileSettings ExtlClntAppMobileSettings

Represents an external client app’s mobile app settings, such as screen lock on a mobile device.

Note: The ExtlClntAppMobileSettings metadata type is a pilot or beta service that is subject to the Beta Services Terms at
[Agreements - Salesforce.com or a written Unified Pilot Agreement if executed by Customer, and applicable terms in the Product](https://www.salesforce.com/company/legal/agreements/)
[Terms Directory. Use of this pilot or beta service is at the Customer's sole discretion.](https://ptd.salesforce.com/)

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ExtlClntAppMobileSettings components have the suffix .ecaMobile and are stored in the extlClntAppMobileSettings

folder.

Version

### ExtlClntAppMobileSettings components are available in API version 64.0 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Field Type** **Description**

externalClientApplication string Required. The name of the associated external client app.

isScreenLockEnabled boolean Required. Indicates whether the mobile app locks the screen after a
specified timeout value.

label string Label for the external client app’s mobile app settings configuration.

### ExtlClntAppNotificationSettings

Represents an external client app’s notification subscriptions for mobile.

Note: The ExtlClntAppNotificationSettings metadata type is a pilot or beta service that is subject to the Beta Services Terms at
[Agreements - Salesforce.com or a written Unified Pilot Agreement if executed by Customer, and applicable terms in the Product](https://www.salesforce.com/company/legal/agreements/)
[Terms Directory. Use of this pilot or beta service is at the Customer's sole discretion.](https://ptd.salesforce.com/)

The ExtlClntAppNotificationSettings metadata type requires the OAuth plugin for External Client Apps. See [OAuth Plugin Enablement](https://help.salesforce.com/s/articleView?id=xcloud.meta_enable_oauth_plugin.htm&type=5&language=en_US)
[with Metadata API](https://help.salesforce.com/s/articleView?id=xcloud.meta_enable_oauth_plugin.htm&type=5&language=en_US) in Salesforce Help.


Metadata Types ExtlClntAppNotificationSettings

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

ExtlClntAppNotificationSettings components have the suffix `.ecaNotifications` and are stored in the
`extlClntAppNotifSettings` folder.

Version

ExtlClntAppNotificationSettings components are available in API version 64.0 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Field Type** **Description**

externalClientApplication string Required. The name of the associated external client app.

label string Label for the external client app’s notification settings configuration.

notificationTypes ExtlClntAppNotificationType[]

ExtlClntAppNotificationType

A list of notification types the external client app is subscribed to. Only
notifications of these types are returned to the associated external client
app via API or sent as push notifications.

Represents a notification type that an external client app is subscribed to. Only custom notification types enabled for the mobile delivery
channel are supported.

Note: You can use Notification Builder in Setup to configure a notification type for the mobile delivery channel. See [Manage](https://help.salesforce.com/s/articleView?id=platform.notif_builder_delivery_settings.htm&type=5&language=en_US)
[Notification Delivery Settings](https://help.salesforce.com/s/articleView?id=platform.notif_builder_delivery_settings.htm&type=5&language=en_US) in Salesforce Help.

**Field Name** **Field Type** **Description**

notificationType string Required. The API name of the notification type.

pushByDefault boolean

Required. Indicates whether the notification type is sent as a push
notification on mobile devices.

To send a notification type as a push notification, you must also configure
the ExtlClntAppPushSettings metadata type.


### Metadata Types ExtlClntAppOauthConfigurablePolicies ExtlClntAppOauthConfigurablePolicies

Represents the policies configured by the admin for an OAuth-enabled external client app.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ExtlClntAppOauthConfigurablePolicies components have the suffix .ecaOauthPlcy and are stored in the

`extlClntAppOauthPolicies` folder.

Version

### ExtlClntAppOauthConfigurablePolicies components are available in API version 59.0 and later.

Special Access Rules

The View all External Client Apps, view their settings, and edit their policies user permission is required for users with admin roles to
configure OAuth policies.

Fields

**Field Name** **Description**

```
apexHandler

clientCredentialsFlowUser

commaSeparatedCustomScopes

```

**Field Type**
string

**Description**
Name of the Apex handler. Available in API version 61.0 and later.

**Field Type**
string

**Description**
The execution user for the OAuth 2.0 client credentials flow. Salesforce returns access
tokens on behalf of this user. This user must have the API Only permission. Available
in API version 60.0 and later.

**Field Type**
string

**Description**
Custom scope names in a comma-separated list. Available in API version 61.0 and later.


Metadata Types ExtlClntAppOauthConfigurablePolicies

**Field Name** **Description**

```
commaSeparatedPermissionSet

commaSeparatedProfile

customAttributes

executeHandlerAs

externalClientApplication

guestJwtTimeout

```

**Field Type**
string

**Description**
Permission set IDs in a comma-separated list. This field or commaSeparatedProfile is
used when permittedUsersPolicyType is set to AdminApprovedPreAuthorized.

**Field Type**
string

**Description**
Profiles in a comma-separated list. This field or commaSeparatedPermissionSet is used
when permittedUsersPolicyType is set to AdminApprovedPreAuthorized.

**Field Type**

ExtlClntAppOauthPoliciesAttribute[]

**Description**
Unique attributes to be included as admin defaults. The maximum number accepted
is 128. Each custom attribute must have a unique key and use an available field.

**Field Type**
string

**Description**
Username of the Apex handler's execution user. Available in API version 61.0 and later.

**Field Type**
string

**Description**

Required.

The name of the external client app associated with this OAuth policies file.

**Field Type**
int

**Description**
If `guestJwtSessionTimeoutType` is set to `Custom`, this field defines the
amount of time before a JWT-based access token issued to a guest user expires. Values
are in minutes.

These values are available in API version 61.0 and later.

**•** `1` —1 Minute

**•** `5` —5 Minutes

**•** `10` —10 Minutes

**•** `15` —15 Minutes

**•** `30` —30 Minutes


Metadata Types ExtlClntAppOauthConfigurablePolicies

**Field Name** **Description**

These values are available in API version 65.0 and later.

**•** `60` —1 Hour

**•** `90` —90 Minutes

**•** `120` —2 Hours

**•** `240` —4 Hours

**•** `480` —8 Hours

**•** `720` —12 Hours

If `guestJwtSessionTimeoutType` is set to `UserSession`, omit this field.

```
guestJwtSessionTimeoutType

ipRelaxationPolicyType

isClientCredentialsFlowEnabled

```

**Field Type**
JWTSessionTimeoutType (enumeration of type string)

**Description**
Specifies how the JWT-based access token timeout is defined for guest users. Valid
values are:

**•** `UserSession` —Salesforce uses the value from the `sessionTimeout` field
[in the ProfileSessionSetting type for the Experience Cloud guest user profile.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_profilesessionsetting.htm)

If there's no profile session timeout for the user, Salesforce uses the
`sessionTimeout` [value from the SessionSettings type.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_securitysettings.htm)

If both are defined, Salesforce defaults to the profile session timeout.

**•** `Custom` —Salesforce uses the value from the `guestJwtTimeout` field.

Available in API version 65.0 and later.

**Field Type**
string

**Description**

The policy that determines IP restrictions.

Values are:

**•** `Enforce`

**•** `Bypass`

**•** `Bypass_2factor`

**•** `Enforce_RelaxRefresh`

**Field Type**
boolean

**Description**
If `true`, the client credentials flow is enabled. The default value is `false` . Available
in API version 60.0 and later.


Metadata Types ExtlClntAppOauthConfigurablePolicies

**Field Name** **Description**

```
isGuestCodeCredFlowEnabled

isNamedUserJwtEnabled

isTokenExchangeFlowEnabled

label

namedUserJwtTimeout

```

**Field Type**
boolean

**Description**
If `true`, the external client app can use the guest user variation of the Authorization
Code and Credentials Flow. To use this flow variation, the external client app must also
be configured to issue JWT-based access tokens. The default value is `false` . Available
in API version 61.0 and later.

**Field Type**
boolean

**Description**
Deprecated.

If `true`, the external client app issues JWT-based access tokens instead of opaque
access tokens. If this field is available, it means that the `isNamedUserJwtEnabled`
field in the ExtlClntAppGlobalOauthSettings type is set to `true` .

The default value is `false` .

**Field Type**
boolean

**Description**
If `true` **true**, the token exchange flow is enabled. The default value is `false` .
Available in API version 60.0 and later.

**Field Type**
string

**Description**
The OAuth policies name for the external client app.

**Field Type**
int

**Description**
If `namedUserJwtSessionTimeoutType` is set to `Custom`, the amount of
time before a JWT-based access token issued to a named user expires. Values are in
minutes.

These values are available in API version 61.0 and later.

**•** `1` —1 Minute

**•** `5` —5 Minutes

**•** `10` —10 Minutes

**•** `15` —15 Minutes

**•** `30` —30 Minutes

These values are available in API version 65.0 and later.


Metadata Types ExtlClntAppOauthConfigurablePolicies

**Field Name** **Description**

**•** `60` —1 Hour

**•** `90` —90 Minutes

**•** `120` —2 Hours

**•** `240` —4 Hours

**•** `480` —8 Hours

**•** `720` —12 Hours

If `namedUserJwtSessionTimeoutType` is set to `UserSession`, omit this
field.

```
namedUserJwtSessionTimeoutType

permittedUsersPolicyType

policyAction

```

**Field Type**
JWTSessionTimeoutType (enumeration of type string)

**Description**
Specifies how the JWT-based access token timeout is defined for named users. Valid
values are:

**•** `UserSession` —Salesforce uses the value from the `sessionTimeout` field
[in the ProfileSessionSetting type for the named user's profile.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_profilesessionsetting.htm)

If there's no profile session timeout for the user, Salesforce uses the
`sessionTimeout` [value from the SessionSettings type.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_securitysettings.htm)

If both are defined, Salesforce defaults to the profile session timeout.

**•** `Custom` —Salesforce uses the value from the `namedUserJwtTimeout` field.

Available in API version 65.0 and later.

**Field Type**
PermittedUsersPolicyType (enumeration of type string)

**Description**
The policy that determines which users are allowed in the external client app.

Values are:

**•** `AdminApprovedPreAuthorized`

**•** `AllSelfAuthorized`

**Field Type**
PolicyAction (enumeration of type string)

**Description**
Requires users to verify their identity with two-factor authentication when they log in
to the external client app. Use `RaiseSessionLevel` along with
`requiredSessionLevel` to determine the security posture.

Values are:

**•** `Block`

**•** `RaiseSessionLevel`


Metadata Types ExtlClntAppOauthConfigurablePolicies

**Field Name** **Description**

```
refreshTokenPolicyType

refreshTokenValidityPeriod

refreshTokenValidityUnit

requiredSessionLevel

sessionTimeoutInMinutes

```

**Field Type**
RefreshTokenPolicyType (enumeration of type string)

**Description**
The type of policy that determines when a token must be refreshed.

Values are:

**•** `Infinite`

**•** `SpecificInactivity`

**•** `SpecificLifetime`

**•** `Zero`

**Field Type**
int

**Description**
The number of units of measure used to specify validity when refresh token policy
type is set to `SpecificInactivity` or `SpecificLifetime` .

**Field Type**
string

**Description**
The unit of measurement that is used to specify validity when refresh token policy
type is set to `SpecificInactivity` or `SpecificLifetime` .

Values are:

**•** `Days`

**•** `Hours`

**•** `Months`

**Field Type**
SessionSecurityLevel (enumeration of type string)

**Description**
Defines the security posture.

Values are:

**•** `HIGH_ASSURANCE`

**•** `LOW`

**•** `STANDARD`

**Field Type**
int

**Description**
Length of time the external client app’s session lasts. This field applies only if the app
issues opaque tokens.


Metadata Types ExtlClntAppOauthConfigurablePolicies

**Field Name** **Description**

```
singleLogoutUrl

startUrl

```

**Field Type**
string

**Description**
URL where Salesforce sends a logout request when users log out of Salesforce.

**Field Type**
string

**Description**
URL where users are directed after they authenticate.

ExtlClntAppOauthPoliciesAttribute

Represents admin-defined attributes that provide personal information to customize the external client app for a specific use case.

**Field Name** **Description**

```
formula

key

```

**Field Type**
string

**Description**

Required.

The existing field that includes the desired information. For example,
`Organization.Country` .

**Field Type**
string

**Description**

Required.

A unique name for the attribute. For example, `country` .

Declarative Metadata Sample Definition

This example shows an ExtlClntAppOauthConfigurablePolicies component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ExtlClntAppOauthConfigurablePolicies xmlns="http://soap.sforce.com/2006/04/metadata">

   <externalClientApplication>myeca</externalClientApplication>

   <label>myecapolicy</label>

   <apexHandler>MyEcaOauthApexHandler</apexHandler>

   <executeHandlerAs>admin@example.org</executeHandlerAs>

   <refreshTokenPolicyType>SpecificLifetime</refreshTokenPolicyType>

   <refreshTokenValidityPeriod>1</refreshTokenValidityPeriod>

   <refreshTokenValidityUnit>Days</refreshTokenValidityUnit>

```


### Metadata Types ExtlClntAppOauthSettings

```
      <ipRelaxationPolicyType>Enforce</ipRelaxationPolicyType>

      <permittedUsersPolicyType>AdminApprovedPreAuthorized</permittedUsersPolicyType>

      <commaSeparatedPermissionSet>PermSetExample</commaSeparatedPermissionSet>

      <commaSeparatedCustomScopes>CustomScopeExample</commaSeparatedCustomScopes>

      <sessionTimeoutInMinutes>1</sessionTimeoutInMinutes>

      <requiredSessionLevel>HIGH_ASSURANCE</requiredSessionLevel>

      <policyAction>RaiseSessionLevel</policyAction>

      <singleLogoutUrl>https://www.example.com</singleLogoutUrl>

      <startUrl>https://www.example.com</startUrl>

      <guestJwtSessionTimeoutType>UserSession</guestJwtSessionTimeoutType>

      <namedUserJwtSessionTimeoutType>Custom</namedUserJwtSessionTimeoutType>

      <namedUserJwtTimeout>10</namedUserJwtSessionTimeout>

   </ExtlClntAppOauthConfigurablePolicies>

```

This example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ExternalClientApplication</name>

      </types>

      <types>

        <members>*</members>

        <name>ExtlClntAppOauthSettings</name>

      </types>

      <types>

        <members>*</members>

        <name>ExtlClntAppGlobalOauthSettings</name>

      </types>

      <types>

        <members>*</members>

        <name>ExtlClntAppOauthConfigurablePolicies</name>

      </types>

      <types>

        <members>*</members>

        <name>ExtlClntAppConfigurablePolicies</name>

      </types>

      <version>60.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### ExtlClntAppOauthSettings

Represents the settings configuration for the external client app’s OAuth plugin.


Metadata Types ExtlClntAppOauthSettings

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

ExtlClntAppOauthSettings components have the suffix `.ecaOauth` and are stored in the `extlClntAppOauthSettings` folder.

Version

ExtlClntAppOauthSettings components are available in API version 59.0 and later.

Special Access Rules

Access to the OAuth plugin requires orgs to enable the Allow Access to OAuth Consumer Secrets via Metadata API permission in Setup.
The View External Client Apps Consumer Secrets in Metadata user permission is required for users with developer roles to configure
OAuth settings.

Fields

**Field Name** **Description**

```
areAttributesIncludedInAssetToken

areCustomPermsIncludedInAssetToken

assetTokenAudiences

```

**Field Type**
boolean

**Description**
Indicates whether custom attributes associated with the external client app are included
in the JSON Web Token (JWT) payload of an asset token issued as a result of the asset
token flow. The default value is `false` .

Available in API version 61.0 and later.

**Field Type**
boolean

**Description**
Indicates whether custom permissions associated with the external client app are
included in the JWT payload of an asset token issued as a result of the asset token flow.
The default value is `false` .

Available in API version 61.0 and later.

**Field Type**
string

**Description**
Required for the OAuth asset token flow. The audience ( `aud` ) claim in the JWT payload
of an asset token issued by the external client app. This claim identifies who the asset
token is intended for. The value must be an array of case-sensitive strings, each


Metadata Types ExtlClntAppOauthSettings

**Field Name** **Description**

containing a `StringOrURI` value. Specify an audience for each intended consumer
of the asset token.

Available in API version 61.0 and later.

```
assetTokenSigningCertificate

assetTokenValidity

clientAssertionCertificate

commaSeparatedOauthScopes

```

**Field Type**
string

**Description**
Required for the asset token flow. The ID of the self-signed certificate used to sign
asset tokens issued by the external client app. The certificate size is limited to 4 KB. If
your certificate is too large, try using a DER-encoded file to reduce the size.

Available in API version 61.0 and later.

**Field Type**
int

**Description**
Required for the asset token flow. The period of time for which the asset token is valid
after it’s issued, expressed as the number of seconds from 1970-01-01T0:0:0Z measured
in UTC. The validity period must be within 3 minutes of the expiration time of the
assertion.

Available in API version 61.0 and later.

**Field Type**
string

**Description**
A certificate that's used to sign a client attestation JSON Web Token (JWT), which is
required for requests to the OAuth 2.0 authorization challenge endpoint for headless
identity flows for first-party apps. To confirm that the app that sent the request is your
first-party app, Salesforce validates the client attestation JWT against this certificate.

**Field Type**
string

**Description**
OAuth scopes for the external client app, written as a comma-separated list.

**•** `Basic` —Allows access to your identity URL service (the same behavior as
deploying `Address`, `Email`, `Phone`, and `Profile` ).

**•** `Api` —Allows access to the logged-in user's account over the APIs.

**•** `Web` —Allows use of the `access_token` on the web. This usage also includes
`visualforce`, allowing access to Visualforce pages.

**•** `Full` —Allows access to all data accessible by the logged-in user.

**•** `Chatter` —Allows access to only the Connect REST API resources.

**•** `CustomApplications` —Provides access to custom applications, such as
those using Visualforce.


Metadata Types ExtlClntAppOauthSettings

**Field Name** **Description**

**•** `RefreshToken` —Allows a refresh token to be returned if you’re eligible to
receive one (the same behavior as deploying `OfflineAccess` ).

**•** `OpenID` —Allows access to the logged-in user's unique identifier for OpenID
Connect apps.

**•** `Profile` —Allows access to the logged-in user's profile (the same behavior as
deploying `Basic` ).

**•** `Email` —Allows access to the logged-in user's email address (the same behavior
as deploying `Basic` ).

**•** `Address` —Allows access to the logged-in user's street address (the same
behavior as deploying `Basic` ).

**•** `Phone` —Allows access to the logged-in user's phone number value (the same
behavior as deploying `Basic` ).

**•** `OfflineAccess` —Allows the app to interact with the user's data while the
user is offline and get a refresh token (the same behavior as deploying
`RefreshToken` ).

**•** `CustomPermissions` —Allows access to the custom permissions in an
organization associated with the external client app and shows whether the current
user has each permission enabled.

**•** `Wave` —Allows access to the Analytics REST API resources.

**•** `Eclair` —Allows access to the Analytics REST API Charts Geodata resource.

**•** `Pardot` —Allows access to Pardot API services on behalf of the user. The full
extent of accessible services is managed by the Pardot account.

**•** `Lightning` —Allows hybrid apps to directly obtain Lightning child sessions
through the OAuth 2.0 hybrid app token flow and hybrid app refresh token flow.

**•** `Content` —Allows hybrid apps to directly obtain content child sessions through
the OAuth 2.0 hybrid app token flow and hybrid app refresh token flow.

**•** `CDPIngest` —Allows access to Data Cloud ingest API services. Customers use
these API services to upload and maintain external datasets in the Data 360.

**•** CDPProfile—Allows access to Data 360 profile.

**•** CDPQuery—Allows access to Data 360 metadata and query data.

**•** `Chatbot` —Allows access to Einstein Bot API services.

**•** CDPSegment—Allows access to Data 360 segments.

**•** CDPIdentityResolution—Allows access to Data 360 identity resolution.

**•** CDPCalculatedInsight—Allows access to Data 360 calculated insights.

**•** SFApiPlatform—Allows access to the Salesforce API Platform.

**•** Interaction—Allows access to Interaction Service API.

**•** EinsteinGPT—Allows access to Einstein Generative AI features in an org.

**•** `PwdlessLogin` —Allows access to Headless Passwordless Login API. Assign
to an internal integration user to get an access token for authenticated requests
to this API.


Metadata Types ExtlClntAppOauthSettings

**Field Name** **Description**

**•** `ForgotPassword` —Allows access to Headless Forgot Password API. Assign
to an internal integration user to get an access token for authenticated requests
to this API.

**•** `UserRegistration` —Allows access to Headless Registration API. Assign to
an internal integration user to get an access token for authenticated requests to
this API.

**•** MCP—Allows access to Model Context Protocol (MCP).

**•** SCRT—Allows access to Service Cloud Real-Time features.

```
customAttributes

externalClientApplication

isFirstPartyAppEnabled

label

oauthLink

singleLogoutUrl

```

**Field Type**

ExtlClntAppOauthSettingsAttribute[]

**Description**
Unique attributes to be included as developer defaults. The maximum number accepted
is 128. Each custom attribute must have a unique key and use an available field.

**Field Type**
string

**Description**

Required.

The external client app associated with this OAuth plugin.

**Field Type**
boolean

**Description**
Determines whether a first-party app can send requests to the OAuth 2.0 authorization
challenge endpoint on this Experience Cloud site. This endpoint support headless
identity flows using the OAuth 2.0 for First-Party Applications draft protocol.

**Field Type**
string

**Description**
Label for the external client app.

**Field Type**
string

**Description**
An auto-generated value that combines the org ID and the OAuth Consumer ID.

**Field Type**
string

**Description**
URL where Salesforce sends a logout request when users log out of Salesforce.


Metadata Types ExtlClntAppOauthSettings

**Field Name** **Description**

```
trustedIpRanges

```

**Field Type**

ExtlClntAppOauthIpRange[]

**Description**
Specifies the ranges of IP addresses that can access the app without requiring the user
to authenticate with the external client app. The maximum number of IP ranges is
128.

ExtlClntAppOauthSettingsAttribute

Represents developer-defined attributes that are used to include additional information in the external client apps. Developers use these
attributes to customize the app for specific use cases.

**Field Name** **Description**

```
formula

key

```

**Field Type**
string

**Description**

Required.

The existing field that includes the desired information. For example,
`Organization.Country` .

**Field Type**
string

**Description**

Required.

A unique name for the attribute. For example, `country` .

ExtlClntAppOauthIpRange

Represents the range of IP addresses that are trusted by the external client app.

**Field Name** **Description**

```
description

endIpAddress

```

**Field Type**
string

**Description**
Identifies the purpose of the range, such as which part of a network corresponds to
this range.

**Field Type**
string


Metadata Types ExtlClntAppOauthSettings

**Field Name** **Description**

**Description**

Required.

Last address in the IP range, inclusive. Required with start address.

```
startIpAddress

```

**Field Type**
string

**Description**

Required.

First address in the IP range, inclusive. Required with end address.

Declarative Metadata Sample Definition

The following is an example of an ExtlClntAppOauthSettings component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ExtlClntAppOauthSettings xmlns="http://soap.sforce.com/2006/04/metadata">

   <externalClientApplication>myeca</externalClientApplication>

   <label>My Oauth Settings</label>

   <trustedIpRanges>

     <startIpAddress>10.55.2.0</startIpAddress>

     <endIpAddress>10.55.2.255</endIpAddress>

     <description>Building 6</description>

   </trustedIpRanges>

   <trustedIpRanges>

     <startIpAddress>10.55.12.0</startIpAddress>

     <endIpAddress>10.55.12.255</endIpAddress>

   </trustedIpRanges>

   <customAttributes>

     <key>userattribute</key>

     <formula>User.Country</formula>

   </customAttributes>

   <commaSeparatedOauthScopes>Basic, Web</commaSeparatedOauthScopes>

</ExtlClntAppOauthSettings>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>*</members>

     <name>ExternalClientApplication</name>

   </types>

   <types>

     <members>*</members>

     <name>ExtlClntAppOauthSettings</name>

   </types>

   <types>

     <members>*</members>

```


### Metadata Types ExtlClntAppPushConfigurablePolicies

```
        <name>ExtlClntAppGlobalOauthSettings</name>

      </types>

      <types>

        <members>*</members>

        <name>ExtlClntAppOauthConfigurablePolicies</name>

      </types>

      <version>59.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### ExtlClntAppPushConfigurablePolicies

Represents an external client app’s push notification policies configuration.

Note: The ExtlClntAppPushConfigurablePolicies metadata type is a pilot or beta service that is subject to the Beta Services Terms
[at Agreements - Salesforce.com or a written Unified Pilot Agreement if executed by Customer, and applicable terms in the Product](https://www.salesforce.com/company/legal/agreements/)
[Terms Directory. Use of this pilot or beta service is at the Customer's sole discretion.](https://ptd.salesforce.com/)

The ExtlClntAppPushConfigurablePolicies metadata type requires the OAuth plugin for External Client Apps. See [OAuth Plugin](https://help.salesforce.com/s/articleView?id=xcloud.meta_enable_oauth_plugin.htm&type=5&language=en_US)
[Enablement with Metadata API](https://help.salesforce.com/s/articleView?id=xcloud.meta_enable_oauth_plugin.htm&type=5&language=en_US) in Salesforce Help.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ExtlClntAppPushConfigurablePolicies components have the suffix .ecaPushPlcy and are stored in the

`extlClntAppPushPolicies` folder.

Version

### ExtlClntAppPushConfigurablePolicies components are available in API version 64.0 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Field Type** **Description**

externalClientApplication string Required. The name of the associated external client app.


### Metadata Types ExtlClntAppPushSettings

**Field Name** **Field Type** **Description**

isFullContent boolean Required. Indicates if push notifications display the full notification title
and body text ( _`true`_ ). When set to _`false`_, standard notifications

display a generic message and custom notifications display only the
notification title.

label string Label for the external client app’s push notification policies configuration.

### ExtlClntAppPushSettings

Represents an external client app’s push notification settings.

[Note: The ExtlClntAppPushSettings metadata type is a pilot or beta service that is subject to the Beta Services Terms at Agreements](https://www.salesforce.com/company/legal/agreements/)

[- Salesforce.com or a written Unified Pilot Agreement if executed by Customer, and applicable terms in the Product Terms Directory.](https://www.salesforce.com/company/legal/agreements/)
Use of this pilot or beta service is at the Customer's sole discretion.

The ExtlClntAppPushSettings metadata type requires the OAuth plugin for External Client Apps. See [OAuth Plugin Enablement](https://help.salesforce.com/s/articleView?id=xcloud.meta_enable_oauth_plugin.htm&type=5&language=en_US)
[with Metadata API](https://help.salesforce.com/s/articleView?id=xcloud.meta_enable_oauth_plugin.htm&type=5&language=en_US) in Salesforce Help.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ExtlClntAppPushSettings components have the suffix .ecaPush and are stored in the extlClntAppPushSettings folder.

Version

### ExtlClntAppPushSettings components are available in API version 64.0 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

Important: You can configure the ExtlClntAppPushSettings metadata type with either `androidPushConfig` or
`applePushConfig`, but not both. You can configure `pushConfigLink` instead to refer to an existing
`androidPushConfig` or `applePushConfig` record.

Of the three push notification configuration options ( `androidPushConfig`, `applePushConfig`, or `pushConfigLink)`,
you must only have one of the options within the same record. If you create a record with `androidPushConfig` or
`applePushConfig`, the `pushConfigLink` is automatically generated and retrievable from the metadata.

If you retrieve the ExtlClntAppPushSettings metadata of an existing packageable external client app to install in another org, delete
the `androidPushConfig` or `applePushConfig` information from the record, if present. To make sure that the destination


Metadata Types ExtlClntAppPushSettings

org refers to the information in the source org, keep the `pushConfigLink` field as the only push notification configuration
in the record.

If the `pushServiceType` is _`Android`_, you must configure `androidPushConfig` or configure a `pushConfigLink`
that refers to an existing `androidPushConfig` record. If the `pushServiceType` is _`Apple`_, you must configure
`applePushConfig` or configure a `pushConfigLink` that refers to an existing `applePushConfig` record.

**Field Name** **Field Type** **Description**

androidPushConfig ExtlClntAppAndroidPushConfig Represents the push notification configuration of an Android mobile
app.

applePushConfig ExtlClntAppApplePushConfig Represents the push notification configuration of an iOS mobile app.

externalClientApplication string Required. The name of the associated external client app.

label string Label for the external client app’s push notifications configuration.

pushConfigLink string Identifies the push notification credentials used by the app. Valid format
is the org ID (for example, _`00D000000000001`_ ) and an

`ExtlClntAppApplePushConfig` or
`ExtlClntAppAndroidPushConfig` record ID (for example,
_`1Dh000000000001`_ ) separated by a colon. For example:

```
                           00D000000000001:1Dh000000000001

```

If you configure `pushConfigLink`, you can’t also have
`androidPushConfig` or `applePushConfig` in the same
record.

pushServiceType

PushServiceType Required. Identifies the mobile operating system of the mobile app. Valid
[(enumeration](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_objects_intro.htm#enumeration_title) of values are:
type string)

**•** _`Apple`_

**•** _`Android`_

ExtlClntAppAndroidPushConfig

Represents the push notification configuration of an Android mobile app.

**Field Name** **Field Type** **Description**

fcmProject string Required. The ID of the Google Firebase project associated with the
mobile app.

serviceAccount string

Required. The Base64-encoded Admin SDK private key for your Google
Firebase service account. You can generate this key from the Service
accounts tab in the Google Firebase console.

The maximum length of the string is 8000 characters.


### Metadata Types ExtlClntAppSamlConfigurablePolicies

ExtlClntAppApplePushConfig

Represents the push notification configuration of an iOS mobile app. To configure the required authentication for iOS push notifications,
you submit either a private key (.p8 file) or a TLS certificate (.p12 file).

To configure push notifications with a private key (.p8 file), complete the `signingKey`, `keyIdentifier`, and `teamIdentifier`
fields.

To configure push notifications with a TLS certificate (.p12 file), complete the `certificate` and `password` fields.

**Field Name** **Field Type** **Description**

applicationBundle string The bundle ID of the iOS mobile app from Apple App Store Connect.

certificate string

The Base64-encoded TLS certificate with Apple Push Notification service
[(APNs) enabled. To generate and export this certificate, see Communicate](https://developer.apple.com/help/account/capabilities/communicate-with-apns-using-a-tls-certificate/)
[with APNs using a TLS certificate in Apple Developer documentation.](https://developer.apple.com/help/account/capabilities/communicate-with-apns-using-a-tls-certificate/)

environment

ApplePushEnvironmentType Required. The Apple Push Notification service environment. Valid values
[(enumeration](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_objects_intro.htm#enumeration_title) of are:
type string)

**•** _`Production`_

**•** _`Sandbox`_

keyIdentifier string The key identifier for the private key entered in the `signingKey` field.
[See Get a key identifier in Apple Developer documentation.](https://developer.apple.com/help/account/keys/get-a-key-identifier/)

password string The password for the TLS certificate entered in the `certificate`
field.

signingKey string

The Base64-encoded private key with Apple Push Notification service
[(APNs) enabled. To generate and download this key, see Create a private](https://developer.apple.com/help/account/keys/create-a-private-key)
[key to access a service in Apple Developer documentation.](https://developer.apple.com/help/account/keys/create-a-private-key)

teamIdentifier string The team ID listed in the membership details of the Apple Developer
account associated with the iOS mobile app.

### ExtlClntAppSamlConfigurablePolicies

Represents SAML configuration policies for an external client app. Use this type to configure Salesforce as an identity provider for SAML
single sign-on (SSO). In this type of SSO configuration, users log in to a third-party service provider, such as Google, using their Salesforce
credentials.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ExtlClntAppSamlConfigurablePolicies components have the suffix .ecaSamlPlcy and are stored in the

`extlClntAppSamlConfigurablePolicies` folder.


Metadata Types ExtlClntAppSamlConfigurablePolicies

Version

ExtlClntAppSamlConfigurablePolicies components are available in API version 63.0 and later.

Special Access Rules

To use the ExtlClntAppSamlConfigurablePolicies type, you must have the View all External Client Apps, view their settings, and edit their
policies user permission.

[This type must be related to a parent ExternalClientApplication. Because external client apps with SAML configurations can't be packaged,](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_externalclientapplication.htm)
the `distributionState` for the parent external client app must be set to `Local` .

[The parent external client app must also have an associated ExtlClntAppConfigurablePolicies metadata type where the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_extlclntappconfigurablepolicies.htm)
`isSamlPluginEnabled` field is set to `true` .

Fields

**Field Name** **Description**

```
acsUrl

certificate

commaSeparatedPermissionSet

commaSeparatedProfile

```

**Field Type**
string

**Description**

Required. The assertion consumer service (ACS) URL from the third-party service
provider. The ACS URL is the endpoint where the service provider receives SAML
responses from Salesforce.

**Field Type**
string

**Description**
A security certificate that the third-party service provider uses to sign SAML requests.
Include this field only if your service provider signs SAML requests and you also want
[to use a service provider-initiated SAML flow.](https://help.salesforce.com/s/articleView?id=xcloud.identity_provider_about.htm&type=5&language=en_US)

If you include a certificate, Salesforce requires that all SAML requests from the service
provider are signed. If you don't include a certificate, Salesforce accepts all SAML
requests, whether or not they're signed.

**Field Type**
string

**Description**
A comma-separated list of permission set IDs that defines the user permissions required
for an end user to use the SAML SSO flow. The permission sets that you specify here
apply to the entire app, not just its SAML configuration.

**Field Type**
string


Metadata Types ExtlClntAppSamlConfigurablePolicies

**Field Name** **Description**

**Description**
A comma-separated list of profile IDs that defines the profiles required for an end user
to use the SAML SSO flow. Like permission sets, profiles define user permissions. The
profiles that you specify here apply to the entire app, not just its SAML configuration.
We recommend that you use permission sets to manage user permissions instead of
profiles.

```
customAttributes

encryptionCertificate

encryptionType

entityUrl

```

**Field Type**

ExtlClntAppSamlConfigurablePoliciesAttribute[]

**Description**
Custom attributes that you can use to send more information about the user in SAML
responses. For example, send information about the user's country. The service provider
can use the information to validate the user's identity.

**Field Type**
string

**Description**
A certificate that's used to encrypt SAML assertions that Salesforce sends to the service
provider. Use an X.509 certificate that's saved in your Certificate and Key Management
settings. To get the certificate, work with a certificate provider. If you include an
`encryptionCertificate`, make sure that your service provider is configured
to decrypt SAML assertions.

**Field Type**
ExtlClntAppSamlEncryptType

**Description**
If you include an `encryptionCertificate` to encrypt SAML assertions, the
`encryptionType` field specifies the encryption method. When the service provider
receives SAML assertions from Salesforce, it detects this method and decrypts it.

These values are valid.

**•** `AES_128` —Advanced Encryption Standard (AES) encryption algorithm with a
128-bit cryptographic key.

**•** `AES_256` —AES encryption algorithm with a 256-bit cryptographic key.

For more information about AES encryption from the National Institute of Standards
and Technology, see
[https://www.nist.gov/publications/advanced-encryption-standard-aes-0.](https://www.nist.gov/publications/advanced-encryption-standard-aes-0)

**Field Type**
string

**Description**

Required. The entity ID from the third-party service provider. The entity ID is a globally
unique ID that Salesforce uses to recognize the service provider.


Metadata Types ExtlClntAppSamlConfigurablePolicies

**Field Name** **Description**

```
externalClientApplication

issuer

label

nameIdFormat

signingAlgorithmType

```

**Field Type**
string

**Description**

Required. The `label` for the parent ExternalClientApplication.

**Field Type**
string

**Description**
Specifies the URI from which Salesforce sends SAML responses. The service provider
uses this value to confirm that the response came from Salesforce. If you don't include
this field, Salesforce uses your My Domain by default. Include this field to specify a
different value, such as an Experience Cloud site URL.

**Field Type**
string

**Description**
A name for your external client app SAML policies configuration.

**Field Type**
ExtlClntAppNameIdFormatType

**Description**
Specifies the format of the user's SSO identifier (dictated by the value of the
`subjectType` field) in SAML messages. So that the service provider can recognize
the user, the name ID format that Salesforce uses for SAML responses must match the
format that the service provider uses. Get this value from your service provider.

These values are valid.

**•** `Unspecified` (default)—No format.

**•** `EmailAddress` —The user's identifier is formatted as an email address.

**•** `Persistent` —The user's identifier is in an opaque format. Only Salesforce and
the service provider can recognize it. The identifier doesn't change based on
context.

**•** `Transient` —Like the `Persistent` identifier, the user's identifier is in an
opaque format. But `Transient` identifiers are temporary values that can change.

**Field Type**
ExtlClntAppSamlSignAlgoType

**Description**
The signing algorithm that Salesforce uses to secure SAML messages. The signing
algorithm generates a signature by hashing the private key that's stored in the
`certificate` . Salesforce includes this signature in the SAML response—in both
the response body and in the SAML assertion. When the service provider receives


Metadata Types ExtlClntAppSamlConfigurablePolicies

**Field Name** **Description**

SAML responses, it validates the signature. Salesforce also applies this algorithm to
single logout requests and responses.

These values are valid.

**•** `SHA1` —Secure Hash Algorithm (SHA) 1 algorithm, which generates a 160-bit
hash value.

**•** `SHA256` —SHA-256 algorithm,which generates a 256-bit hash value.

```
singleLogoutBindingType

singleLogoutUrl

startUrl

subjectCustomAttribute

subjectType

```

**Field Type**
ExtlClntAppSamlBindingType

**Description**
The SAML HTTP binding type that the service provider uses when it initiates single
logout. The binding type determines how the service provider transfers HTTP
information to Salesforce. These values are valid.

**•** `PostBinding` –The service provider uses POST requests for single logout.

**•** `RedirectBinding` —The service provider sends single logout requests through
the browser via GET requests.

**Field Type**
string

**Description**
The SAML single logout endpoint on the service provider. When Salesforce initiates
single logout, it sends logout requests to this endpoint.

**Field Type**
string

**Description**
A URL where users are directed after they authenticate. For example, direct users to a
specific page in the service provider app.

Deprecated. Use the `startUrl` [field on the ExtlClntAppConfigurablePolicies](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_extlclntappconfigurablepolicies.htm)
metadata type instead.

**Field Type**
string

**Description**
If the `subjectType` is `CustomAttribute`, specify which field you want to
use to identify the user. Choose an existing field on the User object, or create a custom
User field.

**Field Type**
ExtlClntAppSamlSubjectType

**Description**
Specifies the user's SSO identifier. These values are valid.


Metadata Types ExtlClntAppSamlConfigurablePolicies

**Field Name** **Description**

**•** `Username` —The user's Salesforce username.

**•** `FederationId` —The user's federation ID, which maps to the
`FederationIdentifier` —A field on the User object. The federation ID can
be any value as long as both Salesforce and the service provider can recognize it.
For example, get a value from the service provider and then specify it in Salesforce.

**•** `UserId` —The user's 15-character Salesforce user ID.

**•** `CustomAttribute` —An identifier that's taken from a custom field value.
Specify the custom field in the `subjectCustomAttribute` field.

**•** `PersistentId` —An opaque identifier that only Salesforce and the service
provider recognize.

ExtlClntAppSamlConfigurablePoliciesAttribute

Represents custom attributes that provide more information about the user. The attributes are included in SAML assertions in SAML
responses that Salesforce sends to the service provider.

**Field Name** **Description**

```
formula

key

```

**Field Type**
string

**Description**

Required.

A field that stores the user information that you want to send. Format the value as
`$<object name>.<field>` .

For example: `$Organization.Country` to indicate the `Country` field on the
Organization object.

**Field Type**
string

**Description**

Required.

A unique name for the attribute to help you and the service provider recognize it in
SAML responses.

Declarative Metadata Sample Definition

The following is an example of an ExtlClntAppSamlConfigurablePolicies component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ExtlClntAppSamlConfigurablePolicies xmlns="http://soap.sforce.com/2006/04/metadata">

   <acsUrl>https://www.<serviceprovideracsurl>.com</acsUrl>

   <entityUrl>https://www.<serviceproviderentityid>.com</entityUrl>

```


### Metadata Types FeatureParameterBoolean

```
      <externalClientApplication>mySamlEca</externalClientApplication>

      <issuer>https://mydomainname.my.salesforce.com</issuer>

      <label>myeca_samlpolicies</label>

      <nameIdFormat>Unspecified</nameIdFormat>

      <singleLogoutUrl>https://www.<serviceprovidersinglelogouturl>.com</singleLogoutUrl>

      <singleLogoutBindingType>RedirectBinding</singleLogoutBindingType>

      <subjectType>CustomAttribute</subjectType>

      <subjectCustomAttribute>MyCustomField</subjectCustomAttribute>

      <certificate>MIIDzDCCArQCCQCFaZKGsGqZ...</certificate>

      <encryptionCertificate>MIIDzDCCArQCCQCFaZKGsGqZ...</encryptionCertificate>

      <encryptionType>AES_128</encryptionType>

      <signingAlgorithmType>SHA1</signingAlgorithmType>

      <customAttributes>

        <key>User Firstname</key>

        <formula>$User.FirstName</formula>

      </customAttributes>

      <customAttributes>

        <key>User Country</key>

        <formula>$User.Country</formula>

      </customAttributes>

   </ExtlClntAppSamlConfigurablePolicies>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ExternalClientApplication</name>

      </types>

      <types>

        <members>*</members>

        <name>ExtlClntAppConfigurablePolicies</name>

      </types>

      <types>

        <members>*</members>

        <name>ExtlClntAppSamlConfigurablePolicies</name>

      </types>

      <version>63.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### FeatureParameterBoolean

Represents a boolean feature parameter in the Feature Management App (FMA). Feature parameters let you drive app behavior and
track activation metrics in subscriber orgs that install your package. This type extends the Metadata metadata type and inherits its
`fullName` field.


Metadata Types FeatureParameterBoolean

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

FeatureParameterBoolean components have the suffix `.featureParameterBoolean` . The components are stored in the
`featureParameters` folder, which contains components for all the feature parameter metadata types.

Version

FeatureParameterBoolean components are available in API version 41.0 and later.

Special Access Rules

[Available to package developers who have access to the Feature Management App (FMA). For details, see Manage Features in the](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/fma_manage_features.htm)
_Second-Generation Managed Packaging Developer Guide_ .

Fields

**Field Name** **Field Type** **Description**

`dataFlowDirection` FeatureParameterDataFlowDirection After a package containing the components is installed,
indicates whether the feature parameter’s value is

editable in your License Management Org (LMO) and
read-only in your customer’s org or the other way around.

`masterLabel` string The feature parameter name that appears in the user
interface.

`value` boolean

FeatureParameterDataFlowDirection

The default value for this feature parameter. You can
reference this value in your code, just like you reference
other values in a subscriber’s org.

Represents the direction of the data flow between your License Management Org (LMO) and the customer’s org.

**Field Name** **Field Type** **Description**

`FeatureParameterDataFlowDirection` string

After a package containing the components is installed,
indicates whether the feature parameter’s value is

editable in your License Management Org (LMO) and
read-only in your customer’s org or the other way around.

**•** `LmoToSubscriber`

**•** `SubscriberToLmo`


### Metadata Types FeatureParameterDate

Declarative Metadata Sample Definition

The following is an example of a FeatureParameterBoolean component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <FeatureParameterBoolean xmlns="http://soap.sforce.com/2006/04/metadata">

      <dataflowDirection>SubscriberToLmo</dataflowDirection>

      <masterLabel>Budget Tracking Enabled</masterLabel>

      <value>false</value>

   </FeatureParameterBoolean>

```

The following is an example `package.xml` that references the previous definition (and the definitions for the other feature parameter
types).

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>FeatureParameterBoolean</name>

      </types>

      <types>

        <members>*</members>

        <name>FeatureParameterDate</name>

      </types>

      <types>

        <members>*</members>

        <name>FeatureParameterInteger</name>

      </types>

      <version>41.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### FeatureParameterDate

Represents a date feature parameter in the Feature Management App (FMA). Feature parameters let you drive app behavior and track
activation metrics in subscriber orgs that install your package. This type extends the Metadata metadata type and inherits its `fullName`
field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### FeatureParameterDate components have the suffix .featureParameterDate . The components are stored in the

`featureParameters` folder, which contains components for all the feature parameter metadata types.


Metadata Types FeatureParameterDate

Version

FeatureParameterDate components are available in API version 41.0 and later.

Special Access Rules

[Available to package developers who have access to the Feature Management App (FMA). For details, see Manage Features in the](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/fma_manage_features.htm)
_Second-Generation Managed Packaging Developer Guide_ .

Fields

**Field Name** **Field Type** **Description**

`dataFlowDirection` FeatureParameterDataFlowDirection After a package containing the components is installed,
indicates whether the feature parameter’s value is

editable in your License Management Org (LMO) and
read-only in your customer’s org or the other way around.

`masterLabel` string The feature parameter name that appears in the user
interface.

`value` date

FeatureParameterDataFlowDirection

The default value for this feature parameter. You can
reference this value in your code, just like you reference
other values in a subscriber’s org.

Represents the direction of the data flow between your License Management Org (LMO) and the customer’s org.

**Field Name** **Field Type** **Description**

`FeatureParameterDataFlowDirection` string

Declarative Metadata Sample Definition

The following is an example of a FeatureParameterDate component.

After a package containing the components is installed,
indicates whether the feature parameter’s value is

editable in your License Management Org (LMO) and
read-only in your customer’s org or the other way around.

**•** `LmoToSubscriber`

**•** `SubscriberToLmo`

```
<?xml version="1.0" encoding="UTF-8"?>

<FeatureParameterDate xmlns="http://soap.sforce.com/2006/04/metadata">

   <dataflowDirection>SubscriberToLmo</dataflowDirection>

   <masterLabel>Activation Date</masterLabel>

```


### Metadata Types FeatureParameterInteger

```
      <value>2017-10-23</value>

   </FeatureParameterDate>

```

The following is an example `package.xml` that references the previous definition (and the definitions for the other feature parameter
types).

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>FeatureParameterBoolean</name>

      </types>

      <types>

        <members>*</members>

        <name>FeatureParameterDate</name>

      </types>

      <types>

        <members>*</members>

        <name>FeatureParameterInteger</name>

      </types>

      <version>41.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### FeatureParameterInteger

Represents an integer feature parameter in the Feature Management App (FMA). Feature parameters let you drive app behavior and
track activation metrics in subscriber orgs that install your package. This type extends the Metadata metadata type and inherits its
`fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### FeatureParameterInteger components have the suffix .featureParameterInteger . The components are stored in the

`featureParameters` folder, which contains components for all the feature parameter metadata types.

Version

### FeatureParameterInteger components are available in API version 41.0 and later.


Metadata Types FeatureParameterInteger

Special Access Rules

[Available to package developers who have access to the Feature Management App (FMA). For details, see Manage Features in the](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/fma_manage_features.htm)
_Second-Generation Managed Packaging Developer Guide_ .

Fields

**Field Name** **Field Type** **Description**

`dataFlowDirection` FeatureParameterDataFlowDirection After a package containing the components is installed,
indicates whether the feature parameter’s value is

editable in your License Management Org (LMO) and
read-only in your customer’s org or the other way around.

`masterLabel` string The feature parameter name that appears in the user
interface.

`value` int

FeatureParameterDataFlowDirection

The default value for this feature parameter. You can
reference this value in your code, just like you reference
other values in a subscriber’s org.

Represents the direction of the data flow between your License Management Org (LMO) and the customer’s org.

**Field Name** **Field Type** **Description**

`FeatureParameterDataFlowDirection` string

Declarative Metadata Sample Definition

The following is an example of a FeatureParameterInteger component.

After a package containing the components is installed,
indicates whether the feature parameter’s value is

editable in your License Management Org (LMO) and
read-only in your customer’s org or the other way around.

**•** `LmoToSubscriber`

**•** `SubscriberToLmo`

```
<?xml version="1.0" encoding="UTF-8"?>

<FeatureParameterInteger xmlns="http://soap.sforce.com/2006/04/metadata">

   <dataflowDirection>SubscriberToLmo</dataflowDirection>

   <masterLabel>Current Project Count</masterLabel>

   <value>42</value>

</FeatureParameterInteger>

```


### Metadata Types FieldMappingConfig

The following is an example `package.xml` that references the previous definition (and the definitions for the other feature parameter
types).

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>FeatureParameterBoolean</name>

      </types>

      <types>

        <members>*</members>

        <name>FeatureParameterDate</name>

      </types>

      <types>

        <members>*</members>

        <name>FeatureParameterInteger</name>

      </types>

      <version>41.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### FieldMappingConfig

Represents the configuration for fields mapped between a source object and one or more destination objects and fields. This object is
available in API version 63.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

This object is available only if the Fundraising Access license is enabled and the Fundraising User system permission is assigned to users.

Fields

### **Field Details**

```
Description

```

**Type**
textarea


Metadata Types FieldMappingConfig

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the field mapping configuration.

```
DeveloperName

Language

MasterLabel

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unqiue name for FieldMappingConfig.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the FieldMappingConfig.

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

**•** `zh_CN` —Chinese (Simplified)

**•** `zh_TW` —Chinese (Traditional)

**Type**
string


Metadata Types FieldMappingConfig

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for the FieldMappingConfig.

```
NamespacePrefix

ProcessType

SourceObjectId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix associated with this object. Each Developer Edition organization that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values:

**•** In Developer Edition organizations, the namespace prefix is set to the namespace prefix
of the organization for all objects that support it. There is an exception if an object is in
an installed managed package. In that case, the object has the namespace prefix of the
installed managed package. This field’s value is the namespace prefix of the Developer
Edition organization of the package developer.

**•** In organizations that are not Developer Edition organizations, `NamespacePrefix`
is only set for objects that are part of an installed managed package. There is no
namespace prefix for all other objects.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the type of process that the field mapping configuration supports.

Possible values are:

**•** `ChangeRequest`

**•** `GiftEntry`

**•** `Incident`

**•** `Problem`

The default value is `GiftEntry` .

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


### Metadata Types FieldRestrictionRule **Field Details**

**Description**
The ID of the source object for all of the fields mapped in the configuration.

Possible values are:

**•** `GiftEntry`

### FieldRestrictionRule

Represents a field visibility rule that controls whether a field is visible to a user, based on the field’s inclusion in a field set. If Enhanced
Personal Information Management setting was enabled before Spring ’22, field visibility is based on the field’s compliance categorization.
This type extends the Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### FieldRestrictionRule components have the suffix .rule and are stored in the fieldRestrictionRules folder.

Version

### FieldRestrictionRule components are available in API version 52.0 and later.

Special Access Rules

**•** To access this type, you must have the Manage Sharing permission.

**•** To create and manage Employee field visibility rules, you must be assigned a Workplace Command Center permission set license
and the Provides access to Workplace Command Center features system permission.

**•** To create and manage User field visibility rules, you must enable Digital Experiences and the Enhanced Personal Information
Management feature.

Fields

**Field Name** **Field Type** **Description**

`active` boolean Indicates whether the rule is active ( `true` ) or not ( `false` ). The default
value is `false` .

`classification` string[] Required. The data classification compliance categorization or field set
that is targeted by the rule. The rule applies to fields that are marked

with this categorization or included in this field set. If you enabled
Enhanced Personal Information Management before Spring ‘22 (API
version 54.0), you can use Salesforce's default compliance categorization
values or values that you add yourself. If you enabled Enhanced Personal


Metadata Types FieldRestrictionRule

**Field Name** **Field Type** **Description**

Information Management after Spring ‘22 (API version 54.0), use the
PersonalInfo_EPIM field set or a field set that you add yourself.

```
classificationType

```

ClassificationType The type of classification method used in your org. If you enabled
(enumeration of Enhanced Personal Information Management before Spring ‘22 (API
type string) version 54.0), use `ComplianceCategory` . If you enabled Enhanced

Personal Information Management after Spring ‘22, use `FieldSet` .

**•** `ComplianceCategory`         

**•** `FieldSet`         

The default value is `ComplianceCategory` . Available in API version
54.0 and later.

`description` string Required. The description of the rule.

```
enforcementType

```

EnforcementType Required. The type of rule. Possible values are:
(enumeration of

**•** `FieldRestrict`

type string)

**•** `FieldRestrict` —Field visibility rule. Only this value is valid.

**•** `Restrict` —Do not use.

**•** `Scoping` —Do not use.

`masterLabel` string Required. The name of the rule.

`recordFilter` string

Required. The criteria that determine which fields are visible to the
specified users. For example, the field can check if the logged-in user
matches the Employee’s ID.

`targetEntity` string Required. The object for which you're creating the rule. Only the
Employee and User objects are supported.

`userCriteria` string Required. The users that this rule applies to, such as all active users or
users with a specified role or profile.

`version` int Required. The rule's version number.

Declarative Metadata Sample Definition

The following is an example of a FieldRestrictionRule component, which uses the ComplianceCategory classification type. The classification
value is one of Salesforce's default compliance categorization values, but you can create a custom compliance categorization value to
use instead.

```
<?xml version="1.0" encoding="UTF-8"?>

<FieldRestrictionRule xmlns="http://soap.sforce.com/2006/04/metadata">

   <active>true</active>

   <classification>PII</classification>

   <classificationType>ComplianceCategory</classificationType>

   <description>Is Owner of Employee</description>

   <enforcementType>FieldRestrict</enforcementType>

   <masterLabel>Is Owner Field Restriction Rule</masterLabel>

   <recordFilter>OwnerId = $User.Id</recordFilter>

   <targetEntity>Employee</targetEntity>

```


### Metadata Types FlexiPage

```
      <userCriteria>$User.IsActive = true</userCriteria>

      <version>1</version>

   </FieldRestrictionRule>

```

The following is an example of a FieldRestrictionRule component, which uses the FieldSet classification type. The classification value is
Salesforce's default field set for personal information, but you can create a field set to use instead.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <FieldRestrictionRule xmlns="http://soap.sforce.com/2006/04/metadata">

      <active>true</active>

      <classification>PersonalInfo_EPIM</classification>

      <classificationType>FieldSet</classificationType>

      <description>Is Owner of Employee</description>

      <enforcementType>FieldRestrict</enforcementType>

      <masterLabel>Is Owner Field Restriction Rule</masterLabel>

      <recordFilter>OwnerId = $User.Id</recordFilter>

      <targetEntity>Employee</targetEntity>

      <userCriteria>$User.IsActive = true</userCriteria>

      <version>1</version>

   </FieldRestrictionRule>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>FieldRestrictionRule</name>

      </types>

      <version>52.0</version>

   </Package>

### FlexiPage

```

Represents the metadata associated with a Lightning page. A Lightning page represents a customizable screen made up of regions
containing Lightning components.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

This type extends the Metadata metadata type and inherits its `fullName` field.

Note: These pages are known as FlexiPages in the API, but are referred to as Lightning pages in the rest of the Salesforce
documentation and UI.

Note: In API version 49.0 and later, arrays in a FlexiPage are represented as `valueList` . Each array element is represented as
`valueListItem`, and the element name is represented as `value` . In API version 48.0 and earlier, arrays are represented as
`value` and array elements are formatted as a comma-separated list. Any FlexiPage retrieved using API version 49.0 or later uses
`valueList` to represent component property array values, regardless of which API version was used to create the FlexiPage.

Lightning pages are used in several places.

**•** In the Salesforce mobile app, a Lightning page is the home page for an app that appears in the navigation menu.

**•** In Lightning Experience, Lightning pages can be used:


Metadata Types FlexiPage

**–** To customize the layout of record pages, the Salesforce Home page, and the Email Application pane in the Outlook and Gmail
integrations.

**–** As the home page for an app.

**–** As the utility bar for a Lightning app.

For more information on Lightning pages, see Salesforce Help.

Note: The namespace prefix is important to help identify the source of items like fields, custom objects, and more. For example,
when working with FlexiPages, we recommend keeping namespaces for object fields, because removing them can cause unexpected
results such as name collisions.

File Suffix and Directory Location

FlexiPage components have the suffix `.flexipage` and are stored in the `flexipages` folder.

Version

FlexiPage components are available in API version 29.0 and later.

Fields

**Field Name** **Field Type** **Description**

`description` string The optional description text of the Lightning page.

events FlexiPageEvent[]

The list of events associated with the Lightning page.

This field is available in API version 53.0 and later.

`flexiPageRegions` FlexiPageRegion[] The list of regions of a page.

`masterLabel` string Required. The label for the Lightning page, which displays in
Setup.

`pageTemplate` string

`parentFlexiPage` string

`platformActionlist` PlatformActionList

Deprecated. Use this field in API versions 33.0 to 38.0 only. In
later versions, use `template` .

Required. The template associated with the Lightning page.

The name of the Lightning page that this page inherits
behavior from.

This field is available in API version 37.0 or later.

The list of all actions, and their order, that display on a
Lightning app page. In the Salesforce mobile app, the actions
appear in the action bar.

This field is available in API version 34.0 and later.

`quickActionList` QuickActionList The list of quick actions associated with the Lightning page.


Metadata Types FlexiPage

**Field Name** **Field Type** **Description**

`sobjectType` string

`template` FlexiPageTemplateInstance

`type` FlexiPageType (enumeration
of type string)


The object the Lightning page is associated with. For Lightning
pages of type `AppPage` or `HomePage`, this field is `null` .

After the value of this field is set, it can’t be changed.

This field is available in API version 37.0 or later.

Required. The template associated with the Lightning page.

This field is available in API version 39.0 and later.

Required. The type of a page. In API versions 32.0 through 36.0,
this field can only have a value of `AppPage` .

Valid values are:

**•** `CdpRecordPage` —A Lightning page that is used to
override a CDPNearCoreObject record page in Lightning
Experience. This value is available in API version 54.0 and
later for orgs that have Data 360 enabled.

**•** `AppPage` —A Lightning page that is used as the home
page for a custom app.

**•** `CommAppPage` —A Lightning page that is used to
represent a custom page, as created in the Experience
Builder. This value is available in API version 37.0 and later.

**•** `CommContractDetailViewPage` —This value is
available in API version 64.0 and later.

**•** `CommCheckoutPage` —A Lightning page that is used
to create a B2B Commerce checkout, as created in the
Experience Builder. This value is available in API version
46.0 and later.

**•** `CommFlowPage` A Lightning page used to override a
flow page, as created in the Experience Builder. This value
is available in API version 45.0 and later.

**•** `CommForgotPasswordPage` —A Lightning page
that’s used to override a forgot-password page, as created
in Experience Builder. This value is available in API version
39.0 and later.

**•** `CommFlowPage` —An out-of-the-box flow page, as
created in Experience Builder. This value is available in API
version 45.0 and later.

**•** `CommGlobalSearchResultPage` A Lightning page
used to override the global search result page, as created
in Experience Builder. This value is available in API version
41.0 and later.

**•** `CommLoginPage` —A Lightning page that’s used to
override the login page, as created in Experience Builder.
This value is available in API version 39.0 and later.

Metadata Types FlexiPage

**Field Name** **Field Type** **Description**

**•** `CommNoSearchResultsPage` —An Experience
Builder site page for B2B searches that return no results.
The URL for this page is `no-results/:term` . The
page starts out empty. You can add any component to it
that accepts parameters to achieve the desired “no results”
experience. For example, you can place an HTML Editor
component or CMS components for recommendations,
banners, help, and support. This value is available in API
version 48.0 and later.

**•** `CommObjectPage` —A Lightning page used to override
an object page, as created in Experience Builder. This value
is available in API version 38.0 and later.

**•** `CommOrderComfirmationPage` —A Lightning
page that is used to create a B2B Commerce order
confirmation page in checkout, as created in the
Experience Builder. This value is available in API version
46.0 and later.

**•** `CommQuickActionCreatePage` —A Lightning
page used to override the create record page, as created
in Experience Builder. This value is available in API version
38.0 and later.

**•** `CommRecordPage` —A Lightning page used to override
a record page, as created in the Experience Builder. This
value is available in API version 38.0 and later.

**•** `CommRelatedListPage` —A Lightning page used
to override a related list page, as created in the Experience
Builder. This value is available in API version 38.0 and later.

**•** `CommSearchResultPage` —A Lightning page used
to override the search result page, as created in Experience
Builder. This value is available in API version 38.0 and later.

**•** `CommSelfRegisterPage` —A Lightning page used
to override the self-registration page, as created in
Experience Builder. This value is available in API version
39.0 and later.

**•** `CommThemeLayoutPage` —A Lightning page used
to override a theme layout page, as created in the
Experience Builder. This value is available in API version
38.0 and later.

**•** `EmbeddedServicePage` This value is available in API
version 45.0 and later.

**•** `EmailContentPage`                              - A page that contains the
builder markup for your email content. When you edit
email content in the builder, the FlexiPage object
remembers where you put the components.


Metadata Types FlexiPage

**Field Name** **Field Type** **Description**

Because they include builder markup, you can't retrieve
or deploy FlexiPages when type is EmailContentPage.

**•** `EmailTemplatePage`                              - A page that contains the
builder markup for your email template. When you edit
an email template in the builder, the FlexiPage object
remembers where you put the components.

Because they include builder markup, you can't retrieve
or deploy FlexiPages when type is EmailTemplatePage or
EmailContentPage.

**•** `ForecastingPage` —A Lightning page that is used
to override the default forecasts page in Lightning
Experience. This value is available in API version 57.0 and
later.

**•** `HomePage` —A Lightning page that is used to override
the Home page in Lightning Experience. This value is
available in API version 37.0 and later.

**•** `MailAppAppPage` —An email application pane used
to override the default layout in the Outlook and Gmail
integrations. This value is available in API version 38.0 and
later.

**•** `OmniSupervisorPageType—` A Lightning page used
to customize the user interface on the Omni-Channel
Supervisor page. This value is available in API version 60.0
and later.

**•** `RecordPage` —A Lightning page used to override an
object record page in Lightning Experience. This value is
available in API version 37.0 and later.

**•** `RecordPreview` A Lightning page used to override
standard lookup previews when hovering over previewable
records in Lightning Experience.This value is available in
API version 45.0 and later.

**•** `UtilityBar` —A Lightning page used as the utility bar
in Lightning Experience apps. This value is available in API
version 38.0 and later.

**•** `VoiceExtension` —A Lightning page used to
customize user interfaces and agent actions in the
Omni-Channel widget for Service Cloud Voice. This value
is available in API version 57.0 and later.

This field is available in API version 32.0 and later.

FlexiPageEvent

An event associated with the Lightning page. Available in API version 53.0 and later.


Metadata Types FlexiPage

**Field Name** **Field Type** **Description**

`sourceName` string

Required. The name of the event source item. If the
source is a custom Lightning web component, this
field is the name of the component.

In API 53.0, a source can be only a Lightning web
component.

`sourceProperties` FlexiPageEventSourceProperty[] The list of properties associated with the event source.

`sourceType` FlexipageEventSourceTypeEnum
(enumeration of type string)

Required. The type of item assigned as the event
source.

In API version 53.0, this field can have only a value of
`Component` .

`targets` FlexiPageEventTarget[] The list of targets associated with the event source.

FlexiPageEventSourceProperty

A property associated with an event. Available in API version 53.0 and later.

**Field Name** **Field Type** **Description**

`name` string Required. In API version 53.0 and later, the value of this
field can be only `eventName` .

`value` string

FlexiPageEventTarget

Required. If the `name` field value is `eventName`, this
field is the name of the event.

If the event source is a Lightning web component, this
value must be the same as the event name defined in
the source component’s `js-meta.xml` file.

A target associated with an event source on the Lightning page. Available in API version 53.0 and later.

**Field Name** **Field Type** **Description**

`mappings` FlexiPageEventPropertyMapping[] A list of key-value pairs for an event’s source-to-target
bindings.

`method` string

`name` string

Required.

The only valid value is `updateProperties` .

Required. The name of the event target.

Valid values are:

**•** `flexipage:componentService`


Metadata Types FlexiPage

**Field Name** **Field Type** **Description**

`properties` FlexiPageEventTargetProperty[] List of properties of the event target.

`type` FlexiPageEventTargetTypeEnum
(enumeration of type string)

FlexiPageEventPropertyMapping

Required. The type of item assigned as the event target.

Valid values are:

**•** `FlexipageServices` —A component on the
Lightning page.

A key-value pair for an event’s source-to-target bindings. Available in API version 53.0 and later.

**Field Name** **Field Type** **Description**

`name` string Required. Name of the target property that changes
when the event is triggered.

`value` string

FlexiPageEventTargetProperty

Value of the target property when the event occurs.

For properties of type string, integer, and boolean, you
can use an expression to define their value. Valid

expression format is
`{!Event.eventPropertyName}` . Event is the
only context supported for expressions in interactions.

A property on the event source’s target represented as a key-value pair. Available in API version 53.0 and later.

**Field Name** **Field Type** **Description**

`name` string Required. In API version 53.0 and later, the value of this
field can be only `componentIdentifier`

`value` string Required. The ComponentInstance `identifier`
value for the component.

FlexiPageRegion

FlexiPage Region represents the properties of a region of a page. A region can contain a record list component or a recent items
component that can be scoped to a set of entities.

Note: A Lightning page region can contain up to 100 components.


Metadata Types FlexiPage

**Field Name** **Field Type** **Description**

`appendable` RegionFlagStatus
(enumeration of type string)

`componentInstances` ComponentInstance[]

`itemInstances` ItemInstance[]

`mode` FlexiPageRegionMode
(enumeration of type string)

This field is available in Digital Experiences in API 45.0 or later,
but is reserved for future use for all other areas.

Valid values are:

**•** `disabled`

**•** `enabled`

This field is assessed in combination with `replaceable`
and `prependable`

**•** If all the properties are set to `enabled`, the region is
unlocked

**•** If all the properties are set to `disabled`, the region is
locked

**•** If none of the properties are specified OR any of these three
properties are missing, the region is unlocked.

This field is available in API version 35.0 or later.

Properties and name of the component instance.

This field was removed in API version 49.0. In API version 49.0
and later, use the `itemInstances` field instead.

Array of item instances, which can contain components and
fields.

This field is available in API version 49.0 or later.

This field is reserved for future use.

Valid values are:

**•** `Append`

**•** `Prepend`

**•** `Replace`

This field is available in API version 35.0 or later.

`name` string Required. Unique name of the FlexiPage region.

`prependable` RegionFlagStatus
(enumeration of type string)


This field is available in Digital Experiences in API 45.0 or later,
but is reserved for future use for all other areas.

Valid values are:

**•** `disabled`

**•** `enabled`

This field is assessed in combination with `appendable` and
`replaceable` .

**•** If all the properties are set to `enabled`, the region is
unlocked

Metadata Types FlexiPage

**Field Name** **Field Type** **Description**

**•** If all the properties are set to `disabled`, the region is
locked

**•** If none of the properties are specified OR any of these three
properties are missing, the region is unlocked.

This field is available in API version 35.0 or later.

`replaceable` RegionFlagStatus
(enumeration of type string)

`type` FlexiPageRegionType
(enumeration of type string)

ItemInstance

This field is available in Digital Experiences in API 45.0 or later,
but is reserved for future use for all other areas.

Valid values are:

**•** `disabled`

**•** `enabled`

This field is assessed in combination with `appendable` and
`prependable` .

**•** If all the properties are set to `enabled`, the region is
unlocked

**•** If all the properties are set to `disabled`, the region is
locked

**•** If none of the properties are specified OR any of these three
properties are missing, the region is unlocked.

This field is available in API version 35.0 or later.

Required. The type of FlexiPage region.

Valid values are:

**•** `Background` —Represents a region for background
utility items, which aren’t visible in the UI. Supported for
utility bars only.

**•** `Facet`

**•** `Region`

This field is available in API version 35.0 or later.

Instance of a component or field on a Lightning page. Available in API version 49.0 or later.

**Field Name** **Field Type** **Description**

`componentInstance` ComponentInstance Properties and name of the component instance.

`fieldInstance` FieldInstance

API name, label, and visibility rule information of the
field component. This field is available only on
Lightning pages that use Dynamic Forms.


Metadata Types FlexiPage

ComponentInstance

Instance of a component in a page, such as a filter list.

**Field Name** **Field Type** **Description**

`componentInstanceProperties` ComponentInstanceProperty[] The value of a single property in a component instance.

`componentName` string Required. The name of a single instance of a
component.

`identifier` string Required. The unique name of the ComponentInstance.
Provides a way to uniquely identify an individual

instance of a component on a Lightning page. This
field has a maximum limit of 120 characters.

This field is available in API version 53.0 and later.

`visibilityRule` UiFormulaRule

ComponentInstanceProperty

A set of one or more filters that define the conditions
under which the component displays on the page.

If the rule evaluates to `true`, the component displays
on the page. If `false`, it doesn't display. If this field
is `null`, the component displays by default.

This field is available in API version 41.0 and later.

Value of a single property in a component instance. ComponentInstanceProperty has a maximum limit of 10,000 characters.

**Field Name** **Field Type** **Description**

`name` string

Name of the property, unique within the component instance.
For Lightning components, this value is the
`<aura:attribute>` as defined in the `.cmp` file.

`type` ComponentInstancePropertyTypeEnum If this field value is `null`, then the
(enumeration of type string) ComponentInstanceProperty values apply to the Lightning

component. If this field value is `decorator`, then the
ComponentInstanceProperty values apply to the _component_
_decorator_ for the Lightning component.

The component decorator is a wrapper around a Lightning
component. The decorator can apply more capabilities to the
component when it renders on a specific page in Lightning
Experience. For example, you can configure a component
decorator around a component on the Lightning Experience
utility bar to set the component’s height or width when
opened. The `UtilityBar` is the only page type that
supports component decorators.

Valid values are:


Metadata Types FlexiPage

**Field Name** **Field Type** **Description**

**•** `decorator`

This field is available in API version 38.0 or later.

`value` string

Reference or value of the property.

When defining a Related List component, to use a parent
record set the `parentFieldApiName` value to

_**`object`**_ `.` _**`field_name`**_ . If you don’t want to use a parent
record, set the value to _**`object`**_ `.Id` .

`valueList` ComponentInstancePropertyList An array of values in a component instance. Available in API
version 49.0 and later.

**Tabs**

When you give a standard label to a tab in a Tabs component—such as Activity, Collaborate, or Details—and when the `name` field is
set to `title`, the `value` field uses a system-defined value instead of the label. Here are some examples of the system-defined values:

**•** `Standard.Tab.activity`

**•** `Standard.Tab.collaborate`

**•** `Standard.Tab.detail`

**•** `Standard.Tab.feed`

**•** `Standard.Tab.preview`

**•** `Standard.Tab.relatedLists`

For example, let’s say you have a Lightning page that contains a tab with the standard label “Activity”. If you query the definition that
page, you see the system-defined name of the tab, not the label, in `value` .

```
<componentInstances>

  <componentInstanceProperties>

   <name>title</name>

   <value>Standard.Tab.activity</value>

  </componentInstanceProperties>

   <componentName>flexipage:tab</componentName>

</componentInstances>

```

**Save Options**

Save options are available on pages of type `RecordPage` only, when users edit an account or when they create, edit, or clone a case
or lead. Save options are configured as a ComponentInstanceProperty under FlexiPageTemplateInstance.

Set the ComponentInstanceProperty `name` to `saveOptions` and use `value` to define the checkbox values. The `value` field in
this case is not a ComponentInstancePropertyList, but instead is a string representation of a JSON array of name and value pairs representing
each checkbox name and its value.

**API Name** **Available** **Available Values** **UI Label**
**Objects**

UseDefaultAssignmentRule Account Evaluate this account against territory

**•** `NONE`
rules on save

**•** `APPLY_OPTION_WITHOUT_CHECKBOX_DISPLAY`


Metadata Types FlexiPage

**API Name** **Available** **Available Values** **UI Label**
**Objects**

**•** `SHOW_CHECKBOX_WITH_DEFAULT_OFF`

**•** `SHOW_CHECKBOX_WITH_DEFAULT_ON`

UseDefaultAssignmentRule Lead Assign using active assignment rule

**•** `NONE`

**•** `SHOW_CHECKBOX_WITH_DEFAULT_OFF`

**•** `SHOW_CHECKBOX_WITH_DEFAULT_ON`

UseDefaultAssignmentRule Case Assign using active assignment rule

**•** `NONE`

**•** `APPLY_OPTION_WITHOUT_CHECKBOX_DISPLAY`

**•** `SHOW_CHECKBOX_WITH_DEFAULT_OFF`

**•** `SHOW_CHECKBOX_WITH_DEFAULT_ON`

triggerOtherEmail Case Send notification email to Contact

**•** `NONE`

**•** `SHOW_CHECKBOX_WITH_DEFAULT_OFF`

**•** `SHOW_CHECKBOX_WITH_DEFAULT_ON`

**Value** **UI Result**

`NONE` Don’t display the checkbox and don’t apply any save
options during save.

`APPLY_OPTION_WITHOUT_CHECKBOX_DISPLAY` Don’t display the checkbox, but apply the save option
value during save.

`SHOW_CHECKBOX_WITH_DEFAULT_OFF` Display the checkbox, unchecked by default.

`SHOW_CHECKBOX_WITH_DEFAULT_ON` Display the checkbox, checked by default.

For example, you can set cases, when saved, to run the **Assign using active assignment rule** without displaying a checkbox, and
display the **Send notification email to Contact** checkbox, checked by default.

```
   saveOptions =

   [{"name":"UseDefaultAssignmentRule","value":"APPLY_OPTION_WITHOUT_CHECKBOX_DISPLAY"},

   {"name":"triggerOtherEmail","value":"SHOW_CHECKBOX_WITH_DEFAULT_ON"}]

```

Note: Set assignment rules, territory rules, and email templates before configuring them as save options.

ComponentInstancePropertyList

Value of an element in an array in a component instance.


Metadata Types FlexiPage

**Field Name** **Field Type** **Description**

`valueListItems` ComponentInstancePropertyListItem[] An array of elements in a component instance.

ComponentInstancePropertyListItem

Name of an element in an array in a component instance.

**Field Name** **Field Type** **Description**

`value` string Name of an element in an array in a component instance.

In API version 49.0 and later, arrays in a FlexiPage are represented as `valueList` . Each array element is represented as
`valueListItem`, and the element name is represented as `value` .

For example, if you have an array of actions with API names `Clone` and `Edit`, the array is represented as `valueList`, with two
`valueListItems` . One `valueListItems` has the `value Clone`, and one `valueListItems` has the `value Edit` .

```
   <componentInstances>

     <componentInstanceProperties>

      <name>actionApiName</name>

      <valueList>

       <valueListItems>

        <value>Clone</value>

       </valueListItems>

       <valueListItems>

        <value>Edit</value>

       </valueListItems>

      </valueList>

     </componentInstanceProperties>

   </componentInstances>

```

UiFormulaRule

A set of one or more filters that define the conditions under which a component displays on a Lightning page. For example, you could
construct a filter that causes a rich text component on an opportunity page to display only when the Amount is greater than $1,000,000.
Available in API version 41.0 and later.

**Field Name** **Field Type** **Description**

`booleanFilter` string Specifies advanced filter conditions such as `1 AND`
`2` .

`criteria` UiFormulaCriterion[] List of one or more filters that, when evaluated,
determine component visibility.

UiFormulaCriterion

A single filter that when evaluated, helps define component visibility on a Lightning page. Available in API version 41.0 and later.


Metadata Types FlexiPage

**Field Name** **Field Type** **Description**

`leftValue` string Required. The field upon which the filter is based. For
example, `AMOUNT` .

`operator` string Required. Defines the operator used to filter the data.
Valid values are:

**•** `CONTAINS`

**•** `EQUAL`

**•** `NE` —not equal

**•** `GT` —greater than

**•** `GE` —greater than or equal

**•** `LE` —less than or equal

**•** `LT` —less than

`rightValue` string The value by which you want to evaluate the
component’s visibility. For example, `1000000` .

You can use these expressions in the `leftValue` field when setting filters for component visibility.

**•** `{!$Client.FormFactor}` —Use this expression to control component visibility based on the device the page is being rendered
on. Valid values are `Small` (phone), `Medium` (tablet), and `Large` (Lightning Experience desktop). Setting the value to `Small`
for record pages is supported only in orgs that are enabled for the new Salesforce mobile app. This expression is supported for app
pages in API version 41.0 and later, and record pages in API version 47.0 and later.

**•** `{!$Permission.CustomPermission.` _**`permissionName`**_ `}` —Use this expression to control component visibility based
on the custom permissions of the user viewing the Lightning page. Supported for app, Home, and record pages only.

**•** `{!$Permission.StandardPermission.` _**`permissionName`**_ `}` —Use this expression to control component visibility
based on the standard permissions of the user viewing the Lightning page. Supported for app, Home, and record pages only.

**•** `{!Record.` _**`field`**_ `}` —Supported for record pages only.

**•** `{!$User.` _**`field`**_ `}` —Supported for app, Home, and record pages only.

For example, to display a component only when it renders on a phone, add this filter: `{!$Client.FormFactor} EQUAL`
`"SMALL"` . Or, to display a component only to the System Administrator, use `{!$User.Profile.Name} EQUAL "System`
`Administrator"` .

Expressions in component visibility rules can span no more than five fields. For example,
`{!Record.Account.Owner.Manager.Manager.Manager.LastName}` has six spans and therefore isn’t supported.

FieldInstance

Represents a single field component that resides on a Lightning page. Available in API version 49.0 and later. This subtype is available
only on Lightning Pages that have enabled Dynamic Forms.

**Field Name** **Field Type** **Description**

`fieldInstanceProperties` FieldInstanceProperty on page 1213[] Properties of the field instance. Contains a name and
value pair for each property associated with the field.


Metadata Types FlexiPage

**Field Name** **Field Type** **Description**

`fieldItem` string The API name of the field, prefixed with its context. For
example, record fields are prefixed with `Record.` .

`identifier` string Required. The unique name of the FieldInstance.
Provides a way to uniquely identify an individual

instance of a field on a Dynamic Forms-enabled
Lightning page. This field has a maximum limit of 120
characters.

This field is available in API version 53.0 and later.

`visibilityRule` UiFormulaRule A set of one or more filters that define the conditions
under which the component displays on the page. If

the rule evaluates to `true`, the component displays
on the page. If `false`, it doesn't display. If this field
is `null`, the component displays by default.

FieldInstanceProperty

Represents a single property of a field instance. Available in API version 49.0 and later. This subtype is available only on Lightning pages
that have enabled Dynamic Forms.

**Field Name** **Field Type** **Description**

`name` string

`value` string

FlexiPageTemplateInstance

Name of the property, unique within the field instance.

Valid values are:

**•** `conditionalFormatRuleset`

Available in API version 62.0 and later.

**•** `uiBehavior`

Available in API version 49.0 and later.

Reference or value of the property.

When the `name` value is `uiBehavior`, valid values
for this field are:

**•** `None`

**•** `Readonly`

**•** `Required`

FlexiPageTemplateInstance represents an instance of a Lightning page template.


Metadata Types FlexiPage

**Field Name** **Field Type** **Description**

`name` string Required. The name of a single instance of a template.

`properties` ComponentInstanceProperty[]

PlatformActionList

The value of a single property in a template instance.

Valid only for:

**•** `CommThemeLayoutPage`

**•** Dynamic Forms-enabled pages of type
`RecordPage` that are associated with account,
case, or lead objects

Contains a name and value pair for each theme layout
property associated with the page template. In
Experience Builder, the theme layout and its properties
appear in the Theme area.

PlatformActionList represents the list of actions, and their order, that display on a Lightning app page. Available in API version 34.0 and
later.

**Field Name** **Field Type** **Description**

```
actionListContext

```

PlatformActionListContext Required. The context of the action list. Valid values are:
(enumeration of

**•** `Assistant`

type string)

**•** `Assistant`

**•** `BannerPhoto`

**•** `Chatter`

**•** `Dockable`

**•** `FeedElement`

**•** `Flexipage`

**•** `Global`

**•** `ListView`

**•** `ListViewDefinition`

**•** `ListViewRecord`

**•** `Lookup`

**•** `MruList`

**•** `MruRow`

**•** `ObjectHomeChart`

**•** `Photo`

**•** `Record`

**•** `RecordEdit`

**•** `RelatedList`

**•** `RelatedListRecord`


Metadata Types FlexiPage

**Field Name** **Field Type** **Description**

`platformActionListItems` PlatformActionListItem[] The actions in the PlatformActionList.

`relatedSourceEntity` string

PlatformActionListItem

When the `ActionListContext` is RelatedList or RelatedListRecord,
this field represents the API name of the related list to which the action
belongs.

PlatformActionListItem represents an action in the PlatformActionList. Available in API version 34.0 and later.

**Field Name** **Field Type** **Description**

`actionName` string Required. The API name for the action in the list.

```
actionType

```

PlatformActionType Required. The type of action. Valid values are:
(enumeration of type

**•** `ActionLink` —An indicator on a feed element that targets an API, a

string)

web page, or a file, represented by a button in the Salesforce Chatter feed
UI.

**•** `CustomButton` —When clicked, opens a URL or a Visualforce page in
a window or executes JavaScript.

**•** `InvocableAction`

**•** `ProductivityAction` —Productivity actions are predefined and
attached to a limited set of objects. Productivity actions include Send Email,
Call, Map, View Website, and Read News. Except for the Call action, you
can’t edit productivity actions.

**•** `QuickAction` —A global or object-specific action.

**•** `StandardButton` —A predefined Salesforce button such as New, Edit,
and Delete.

`sortOrder` int Required. The placement of the action in the list.

`subtype` string The subtype of the action. For quick actions, the subtype is
`QuickActionType` . For custom buttons, the subtype is

`WebLinkTypeEnum` . For action links, subtypes are `Api`, `ApiAsync`,
`Download`, and `Ui` . Standard buttons and productivity actions have no
subtype.

Declarative Metadata Sample Definition

Here’s a sample XML FlexiPage component definition for a custom opportunity record page. It includes a tab set and a rich text component
with visibility rules assigned to it.


Metadata Types FlexiPage

Note: As an Experience Builder site page, three initial regions in the definition show the `header` region as locked, the `content`
region as unlocked, and the `footer` region as unlocked.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <FlexiPage xmlns="http://soap.sforce.com/2006/04/metadata">

      <flexiPageRegions>

        <itemInstances>

           <componentInstance>

             <componentInstanceProperties>

               <name>collapsed</name>

               <value>false</value>

             </componentInstanceProperties>

             <componentInstanceProperties>

               <name>hideChatterActions</name>

               <value>false</value>

             </componentInstanceProperties>

             <componentInstanceProperties>

               <name>numVisibleActions</name>

               <value>3</value>

             </componentInstanceProperties>

             <componentName>force:highlightsPanel</componentName>

           </componentInstance>

        </itemInstances>

        <name>header</name>

        <type>Region</type>

      </flexiPageRegions>

      <flexiPageRegions>

        <itemInstances>

           <componentInstance>

             <componentInstanceProperties>

               <name>hideUpdateButton</name>

               <value>false</value>

             </componentInstanceProperties>

             <componentInstanceProperties>

               <name>variant</name>

               <value>linear</value>

             </componentInstanceProperties>

             <componentName>runtime_sales_pathassistant:pathAssistant</componentName>

           </componentInstance>

        </itemInstances>

        <name>subheader</name>

        <type>Region</type>

      </flexiPageRegions>

      <flexiPageRegions>

        <itemInstances>

           <componentInstance>

             <componentInstanceProperties>

               <name>entityNames</name>

               <valueList>

                  <valueListItems>

                    <value>Opportunity</value>

                  </valueListItems>

               </valueList>

             </componentInstanceProperties>

```


Metadata Types FlexiPage

```
             <componentInstanceProperties>

               <name>maxRecords</name>

               <value>3</value>

             </componentInstanceProperties>

             <componentName>flexipage:recentItems</componentName>

           </componentInstance>

        </itemInstances>

        <name>Facet-afbed70e-277a-41f5-9919-34651ff97773</name>

        <type>Facet</type>

      </flexiPageRegions>

      <flexiPageRegions>

        <itemInstances>

           <componentInstance>

             <componentInstanceProperties>

               <name>relatedListComponentOverride</name>

               <value>NONE</value>

             </componentInstanceProperties>

             <componentName>force:relatedListContainer</componentName>

           </componentInstance>

        </itemInstances>

        <name>facet-77f21b6f-ad73-4d79-838a-79e0df27cc63</name>

        <type>Facet</type>

      </flexiPageRegions>

      <flexiPageRegions>

        <itemInstances>

           <componentInstance>

             <componentName>force:detailPanel</componentName>

           </componentInstance>

        </itemInstances>

        <name>facet-c22fcfa7-d6f2-46ab-ac03-6c92e7398da1</name>

        <type>Facet</type>

      </flexiPageRegions>

      <flexiPageRegions>

        <itemInstances>

           <componentInstance>

             <componentName>runtime_sales_activities:activityPanel</componentName>

           </componentInstance>

        </itemInstances>

        <name>Facet-u9v2x6h8u4k</name>

        <type>Facet</type>

      </flexiPageRegions>

      <flexiPageRegions>

        <itemInstances>

           <componentInstance>

             <componentInstanceProperties>

               <name>body</name>

               <value>Facet-afbed70e-277a-41f5-9919-34651ff97773</value>

             </componentInstanceProperties>

             <componentInstanceProperties>

               <name>title</name>

               <value>Recent Items</value>

             </componentInstanceProperties>

             <componentName>flexipage:tab</componentName>

           </componentInstance>

```


Metadata Types FlexiPage

```
        </itemInstances>

        <itemInstances>

           <componentInstance>

             <componentInstanceProperties>

               <name>active</name>

               <value>true</value>

             </componentInstanceProperties>

             <componentInstanceProperties>

               <name>body</name>

               <value>facet-77f21b6f-ad73-4d79-838a-79e0df27cc63</value>

             </componentInstanceProperties>

             <componentInstanceProperties>

               <name>title</name>

               <value>Standard.Tab.relatedLists</value>

             </componentInstanceProperties>

             <componentName>flexipage:tab</componentName>

           </componentInstance>

        </itemInstances>

        <itemInstances>

           <componentInstance>

             <componentInstanceProperties>

               <name>body</name>

               <value>facet-c22fcfa7-d6f2-46ab-ac03-6c92e7398da1</value>

             </componentInstanceProperties>

             <componentInstanceProperties>

               <name>title</name>

               <value>Standard.Tab.detail</value>

             </componentInstanceProperties>

             <componentName>flexipage:tab</componentName>

           </componentInstance>

        </itemInstances>

        <itemInstances>

           <componentInstance>

             <componentInstanceProperties>

               <name>body</name>

               <value>Facet-u9v2x6h8u4k</value>

             </componentInstanceProperties>

             <componentInstanceProperties>

               <name>title</name>

               <value>Standard.Tab.activity</value>

             </componentInstanceProperties>

             <componentName>flexipage:tab</componentName>

           </componentInstance>

        </itemInstances>

        <name>facet-27334405-c871-463f-bc20-b3713bbb4884</name>

        <type>Facet</type>

      </flexiPageRegions>

      <flexiPageRegions>

        <itemInstances>

           <componentInstance>

             <componentInstanceProperties>

               <name>tabs</name>

               <value>facet-27334405-c871-463f-bc20-b3713bbb4884</value>

             </componentInstanceProperties>

```


Metadata Types FlexiPage

```
             <componentName>flexipage:tabset</componentName>

           </componentInstance>

        </itemInstances>

        <name>main</name>

        <type>Region</type>

      </flexiPageRegions>

      <flexiPageRegions>

        <itemInstances>

           <componentInstance>

             <componentInstanceProperties>

               <name>decorate</name>

               <value>true</value>

             </componentInstanceProperties>

             <componentInstanceProperties>

               <name>richTextValue</name>

               <value>&lt;p style=&quot;text-align: center;&quot;&gt;&lt;span

   style=&quot;background-color: rgb(255, 255, 255); font-size: 18px; color: rgb(11, 11,

   11);&quot;&gt;A million dollar opportunity closed! Oh yeah!&lt;/span&gt;&lt;/p&gt;</value>

             </componentInstanceProperties>

             <componentName>flexipage:richText</componentName>

             <visibilityRule>

               <booleanFilter>1 AND 2</booleanFilter>

               <criteria>

                  <leftValue>{!Record.Amount}</leftValue>

                  <operator>GE</operator>

                  <rightValue>1000000</rightValue>

               </criteria>

               <criteria>

                  <leftValue>{!Record.StageName}</leftValue>

                  <operator>EQUAL</operator>

                  <rightValue>Closed Won</rightValue>

               </criteria>

             </visibilityRule>

           </componentInstance>

        </itemInstances>

        <itemInstances>

           <componentInstance>

             <componentInstanceProperties>

               <name>decorate</name>

               <value>true</value>

             </componentInstanceProperties>

             <componentInstanceProperties>

               <name>richTextValue</name>

               <value>&lt;p style=&quot;text-align: center;&quot;&gt;&lt;span

   style=&quot;background-color: rgb(255, 255, 255); font-size: 16px; color: rgb(244, 0,

   0);&quot;&gt;This component is for mobile users only.&lt;/span&gt;&lt;/p&gt;</value>

             </componentInstanceProperties>

             <componentName>flexipage:richText</componentName>

             <visibilityRule>

               <criteria>

                  <leftValue>{!$Client.formFactor}</leftValue>

                  <operator>EQUAL</operator>

                  <rightValue>Small</rightValue>

```


### Metadata Types Flow

```
               </criteria>

             </visibilityRule>

           </componentInstance>

        </itemInstances>

        <itemInstances>

           <componentInstance>

             <componentName>forceChatter:recordFeedContainer</componentName>

           </componentInstance>

        </itemInstances>

        <name>sidebar</name>

        <type>Region</type>

      </flexiPageRegions>

      <masterLabel>New Opportunity Page</masterLabel>

      <sobjectType>Opportunity</sobjectType>

      <template>

        <name>flexipage:recordHomeWithSubheaderTemplateDesktop</name>

      </template>

      <type>RecordPage</type>

   </FlexiPage>

```

And, here’s the sample `package.xml` file that references the FlexiPage component definition:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <fullName>New Opportunity Page</fullName>

      <types>

        <members>New_Opportunity_Page</members>

        <name>FlexiPage</name>

      </types>

      <version>49.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### Flow

Represents the metadata associated with a flow that encompasses the flow's structure, logic, and run-time behavior. It allows you to
build dynamic applications that guide users through interactive screens, automate processes, and connect with various Salesforce and
external services. This includes managing data operations like creating, updating, or deleting records, handling complex decisions,
looping through collections, and invoking actions like Apex or external services to extend functionality. A flow contains options for API
versioning, various execution environments, and detailed configuration of elements to design powerful automation solutions.

Important: Where possible, we changed non-inclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Here are the limitations related to how you can use Metadata API to work with flows:

**•** You can’t use Metadata API to access a flow installed from a managed package unless the flow is a template.

**•** Spaces in a flow file name can lead to errors when you deploy the flow. You can include spaces at the beginning or end of a name,
but these spaces are removed when you deploy the flow.


Metadata Types Flow

**•** You can deploy changes to an active flow if in a non-production org, such as a scratch or sandbox org. To deploy changes in a
production org, you must enable the **Deploy processes and flows as active** preference. After you deploy changes to an active
flow, the flow’s detail page shows a new flow version that’s active. The new version includes your changes.

**•** You can delete a flow version if it isn’t active and doesn’t have any paused interviews. If the flow version has paused interviews, wait
for those interviews to resume and finish, or delete them.

Warning: Don’t edit the metadata of retrieved Process Builder processes, such as flow components whose processType is
`Workflow` or `InvocableProcess` . If you deploy process metadata that you edited, you can’t open the process in the target
org.

Declarative Metadata File Suffix and Directory Location

Flows are stored in the `Flow` directory of the corresponding package directory. The file name matches the flow’s unique full name,
and the extension is `.flow` .

Version

The flow Metadata API is available in API version 24.0 and later.

Flow

This metadata type represents a valid definition of a flow. This type extends the Metadata metadata type and inherits its `fullName`
field.

**Field Name** **Field Type** **Description**

`actionCalls` FlowActionCall[] An array of nodes that defines calls to action. This field is available
in API version 31.0 and later.

`apexPluginCalls` FlowApexPluginCall[] An array of nodes that defines calls to Apex plug-ins.

`apiVersion` number The API version that defines the execution behavior of the flow.
This field is available in API version 50.0 and later. Flows created

before API version 50.0 show an API version of 0 on the Flows
list view in Setup. To show the correct API version number, create
another version of the flow, and set the API version for running
the flow to 49.0 or later.

`areMetricsLoggedToDataCloud` boolean

Indicates whether the flow's metrics are logged to Data Cloud.
The default value is `false` . This field is available in API version
63.0 and later.

`assignments` FlowAssignment[] An array of assignment nodes.

`choices` FlowChoice[] An array of static choice options.

`collectionFilterCriteria` FlowCollectionFilterCriteria[] Reserved for future use.

`collectionProcessors` FlowCollectionProcessor[] An array of nodes that process collections. This field is available
in API version 50.0 and later.

`constants` FlowConstant[] An array of constants.


Metadata Types Flow

**Field Name** **Field Type** **Description**

`customErrors` FlowCustomError[] An array of custom errors.

`customProperties` FlowCustomProperty[]

An array of custom properties that specify flow properties such
as the option to show a progress indicator in a screen flow. This
field is available in API version 63.0 and later.

`decisions` FlowDecision[] An array of decision nodes.

`description` string Description of the flow.

`dynamicChoiceSets` FlowDynamicChoiceSet[] An array that constructs a set of choice options based on a
database lookup.

`environments` FlowEnvironment (enumeration The environment in which the flow can run. Valid values are:
of type string)

**•** `Default` —The flow can run from a Visualforce
component, Lightning page, flow action, or custom Aura
component.

**•** `Offline` —The flow can run only offline. Flow types that
support offline flows must set this value. This value is
available in API version 62.0 and later.

**•** `Slack` —The flow can run in Slack and the default
environment. You specify the Slack flow environment when
you save the flow.

This field is available in API version 55.0 and later.

`exitRules` FlowExitRule[]

An array of exit rules that determine when to end the flow for
a user in a segment-triggered flow. This field is available in API
version 61.0 and later.

`experiments` FlowExperiment[] An array of experiments. This field is available in API version 61.0
and later.

`formulas` FlowFormula[] An array of formulas.

`groups` FlowNodeGroup[] Reserved for future use.

`fullName` string

Required. Inherited from the Metadata component. Name of
the file in Metadata API.

A unique name for the flow that contains only underscores and
alphanumeric characters. The name must be unique across the

org, begin with a letter, not include spaces, not end with an
underscore, and not contain two consecutive underscores.

To deploy or retrieve a version, you can specify the version
number. For example, `sampleFlow-3` specifies version 3 of
the flow whose unique name is sampleFlow. If you don’t specify
a version number, the flow is the latest version.

In API version 43.0 and earlier, this field included the version
number. In API version 44 and later, this field no longer includes
the version number.


Metadata Types Flow

**Field Name** **Field Type** **Description**

`interviewLabel` string

Label for the interview. This label helps users and administrators
differentiate interviews from the same flow.

In the user interface, this label appears in the Paused Flow
Interviews component on the user’s Home tab and in the list of
paused flow interviews in Setup.

`isAdditionalPermissionRequiredToRun` boolean Override the default behavior and restrict access to enabled
profiles or permission sets by setting this property to `true` .

The default value is `false` . This field is available in API version
47.0 and later.

`isTemplate` boolean Indicates whether the process or flow is a template. The default
value is `false` . When installed from managed packages,

subscribers can’t view or clone processes or flows because of
intellectual property (IP) protection. But when those processes
and flows are templates, subscribers can open them in a builder,
clone them, and customize the clones. This field is available in
API version 45.0 and later.

`label` string Required. Label for the flow.

`loops` FlowLoop[] An array of nodes for iterating through collections. This field is
available in API version 30.0 and later.

`migratedFromWorkflowRuleName` string The name of the workflow rule that the flow was migrated from.
This field is available in API version 54.0 and later.

`orchestratedStages` FlowOrchestratedStage[] An array of stage nodes in an orchestration. This field is available
in API version 53.0 and later.

`processMetadataValues` FlowMetadataValue[]

Metadata values for the flow.

This field is available in API version 31.0 and later.

`processType` FlowProcessType (enumeration The type of the flow, as determined by the active version, or the
of type string) latest version, if there’s no active version. Valid values are:

**•** `ActionableEventManagementFlow` —A flow that
triggers an actionable event orchestration process in the
background and automatically executes different types of
actions based on the event type. This value is available in
API version 62.0 and later.

**•** `ActionCadenceAutolaunchedFlow` —A flow that’s
executed when a user completes a cadence step. This value
is available in API version 56.0 and later.

**•** `ActionCadenceStepFlow` —A screen flow used as
a cadence step. This value is available in API version 56.0
and later.

**•** `ActivityObjectMatchingFlow` —A flow that
launches when Einstein Activity Capture detects and


Metadata Types Flow

**Field Name** **Field Type** **Description**

captures a new activity, such as an email. This type of flow
runs in the background without user interaction. This value
is available with Sync Email as Salesforce Activity in API
version 64.0 and later.

**•** `Appointments` —A flow for Lightning Scheduler. This
value is available in API version 44.0 and later.

**•** `ApprovalWorkflow` —An orchestration that’s used for
an approval process. This value is available in API version
63.0 and later.

**•** `AutoLaunchedFlow` —A flow that doesn’t require user
interaction.

**•** `CheckoutFlow` —A flow used in Lightning B2B
Commerce to create a checkout in a store. This value is
available in API version 48.0 and later.

**•** `ContactRequestFlow` —A flow that lets customers
request to be contacted by customer support. This flow is
used to create contact request records. This value is available
in API version 45.0 and later.

**•** `CustomerLifecycle` —A Salesforce Surveys flow that
lets you associate survey questions with different stages in
customer lifecycles. This value is available in API version 49.0
and later and only when the Customer Lifecycle Designer
license is enabled.

**•** `CustomEvent` —A process that is invoked when it
receives a platform event message. In the UI, it’s an event
process. This value is available in API version 41.0 and later.

**•** `DataCaptureFlow`                             - In the UI, Data Capture flows
configure the Form tab in the Field Service mobile app.
When the Data Capture flow is launched, its Flow metadata
is publicly available in JavaScript format. This value is
available in API version 62.0 and later.

**•** `DcvrFrameworkDataCaptureFlow` —A screen flow
that presents assessment questions from Discovery
Framework. Launches when invoked by a user on a mobile
device. This type of flow collects or displays information,
requires user interaction, and works offline or online. This
value is available in API version 62.0 and later.

**•** `EvaluationFlow` —A flow for evaluating custom entry
and exit conditions in an orchestration. Uses the
`isOrchestrationConditionMet` output variable
and discards values from any other output variables. This
value is available in API version 54.0 and later.

**•** `FieldServiceMobile` —A flow for the Field Service
mobile app. This value is available in API version 39.0 and
later.


Metadata Types Flow

**Field Name** **Field Type** **Description**

**•** `FieldServiceWeb` —A flow for embedded
Appointment Booking. Its UI label is Field Service Embedded
Flow. This value is available in API version 41.0 and later.

**•** `Flow` —A flow that requires user interaction because it
contains one or more screens or local actions, choices, or
dynamic choices. In the UI and Salesforce Help, it’s a screen
flow. Screen flows can be launched from the UI, such as with
a flow action, Lightning page, or web tab.

**•** `FSCLending` —A flow for Financial Services Cloud
Mortgage. This value is available in API version 46.0 and later.

**•** `IdentityUserRegistrationFlow` —A flow to
handle user registration and updates for single sign-on with
the authentication provider framework. Available in API
version 64.0 and later.

**•** `IndicatorResultFlow` —A flow for Outcome
Management that calculates and creates indicator results
for a selected indicator performance period. This value is
available with the Outcome Management license in API
version 60.0 and later.

**•** `IndividualObjectLinkingFlow` —A flow that
associates individuals with interactions such as voice calls,
messaging sessions, or case-related emails. This value is
available in API version 58.0 and later.

**•** `InvocableProcess` —A process that another process
or the Invocable Actions resource in REST API invokes. This
value is available in API version 38.0 and later.

**•** `Journey` —An audience-driven flow for Marketing Cloud.
This value is available in API version 57.0 and later.

**•** `LoginFlow` —A flow for login. This value is available in
API version 51.0 and later.

**•** `LoyaltyManagementFlow` —A flow for the Loyalty
Management app that’s invokable by loyalty program
processes. This value is available in API version 54.0 and later.

**•** `Orchestrator` —An orchestration that organizes flows
into groups of steps contained in a series of stages. This
value is available in API version 53.0 and later.

**•** `PromptFlow` —A flow for Prompt Builder. Pass data
between Prompt Builder and the flow. This value is available
in API version 60.0 and later.

**•** `RecommendationStrategy` —Build
recommendations for your users. A recommendation
launches its assigned flow. This value is available in API
[version 54.0 and later. See Flow Builder Strategies.](https://help.salesforce.com/s/articleView?id=platform.nba_building_flow_builder_strategy.htm&type=5&language=en_US)


Metadata Types Flow

**Field Name** **Field Type** **Description**

**•** `RoutingFlow` —A flow for Salesforce Omni-Channel
routing and other business logic. This value is available in
API version 52.0 and later.

**•** `Survey` —A flow for Salesforce Surveys. From the UI, this
type of flow is created in Survey Builder. This value is
available in API version 42.0 and later.

**•** `SurveyEnrich` —A Salesforce Surveys flow that uses
the Survey Data Mapper. From the UI, this type of flow is
created in the Survey Builder and requires an associated
survey flow type. This value is available in API version 49.0
or later and only when the Customer Lifecycle Designer
license is enabled.

**•** `Workflow` —A process that is invoked when a record is
created or edited. In the UI and Salesforce Help, it’s a record
change process.

Across flow versions, you can change the type only from `Flow`
to `AutoLaunchedFlow` or vice versa. Before you change
the flow type, make sure that the flow contains only the
elements, resources, and functionality that the new flow type
supports.

These values are reserved for future or Salesforce internal use.

**•** `ActionPlan`

**•** `AppProcess`

**•** `ApprovalWorkflow`

**•** `CartAsyncFlow`

**•** `DigitalForm`

**•** `JourneyBuilderIntegration`

**•** `LoginFlow`

**•** `ManagedContentFlow`

**•** `OrchestrationFlow`

**•** `SalesEntryExperienceFlow`

**•** `TransactionSecurityFlow`

**•** `UserProvisioningFlow`

This field is available in API version 31.0 and later.

`recordCreates` FlowRecordCreate[] An array of nodes for creating records in the database.

`recordDeletes` FlowRecordDelete[] An array of nodes for deleting records in the database.

`recordLookups` FlowRecordLookup[] An array of nodes for looking up records in the database.

`recordRollbacks` FlowRecordRollback[] An array of nodes for rolling back transactions in the screen flow.
This field is available in API version 52.0 and later.


Metadata Types Flow

**Field Name** **Field Type** **Description**

`recordUpdates` FlowRecordUpdate[] An array of nodes for updating records in the database.

`runInMode` FlowRunInMode (enumeration The context that the flow runs in. Valid values are:
of type string)

**•** `DefaultMode` —How the flow is launched determines
whether the flow runs in user context or in system context.
In the UI, this value appears as **User or System**
**Context—Depends on How Flow is Launched** .

**•** `SystemModeWithSharing` —The flow respects
org-wide default settings, role hierarchies, sharing rules,
manual sharing, teams, and territories. The flow doesn’t
respect object permissions, field-level access, or other
permissions of the running user. In the UI, this value appears
as **System Context with Sharing—Enforces**
**Record-Level Access** .

**•** `SystemModeWithoutSharing—` The flow can access
all data. In the UI, this value appears as **System Context**
**without Sharing—Access All Data** . This value is available
in API version 49.0 and later.

This field is available in API version 48.0 and later.

`screens` FlowScreen[] An array of screen nodes.

`segment` string Reserved for future use.

`stages` FlowStage[] An array of stage resources that you can use throughout the
flow. This field is available in API version 42.0 and later.

`start` FlowStart[] The flow’s Start element, which specifies how and when the
flow starts. This field is available in API version 47.0 and later.

`startElementReference` string

Specifies which node or element is the starting point in the flow.

This field isn’t used in flows created or saved in Flow Builder in
Winter ’20 and later. Those flows use the `start` field instead
to specify how the flow starts.

`status` FlowVersionStatus (enumeration The activation status of the flow. Valid values are:
of type string)

**•** `Active`

**•** `Draft` —In the UI, this status appears as `Inactive` .

**•** `Obsolete` —In the UI, this status appears as `Inactive` .

**•** `InvalidDraft` —In the UI, this status appears as
`Draft` .

**•** `UnderReview` —In the UI, this status appears as `Under`
`Review` .

`steps` FlowStep[] An array of step nodes.


Metadata Types Flow

**Field Name** **Field Type** **Description**

`subflows` FlowSubflow[] An array of subflows. This field is available in API version 25.0
and later.

`textTemplates` FlowTextTemplate[] An array of text templates.

`timeZoneSidKey` string The ID that defines the time zone in which the flow runs. This
field is available in API version 56.0 and later.

`transforms` FlowTransform[] An array of data transformations. This field is available in API
version 59.0 and later.

`triggerOrder` int The run order of a record-triggered flow, from 1 to 2,000. See
[Guidelines for Defining the Run Order of Record-Triggered Flows](https://help.salesforce.com/s/articleView?id=flow_concepts_trigger_guidelines.htm&type=5&language=en_US)

[for an Object in Salesforce Help. This field is available in API](https://help.salesforce.com/s/articleView?id=flow_concepts_trigger_guidelines.htm&type=5&language=en_US)
version 54.0 and later.

`variables` FlowVariable[] An array of variable definitions.

`waits` FlowWait[] An array of wait nodes. This field is available in API version 32.0
and later.

FlowActionCall

Defines a call to an action from the flow. It extends FlowNode.

This metadata type is available in API version 31.0 and later.

**Field Name** **Field Type** **Description**

`actionCallPaths` ActionCallPath[] Reserved for future use.

`actionName` string Required. Name for the action. Must be unique across
actions with the same `actionType` .

`actionType` InvocableActionType (enumeration of type Required. See InvocableActionType on page 1230.
string)

`connector` FlowConnector Specifies which node to execute after this action call.

`dataTypeMappings` FlowDataTypeMapping[]

An array of data type mappings for input and output values
that have the generic sObject data type. This field is available
in API version 48.0 and later.

`einsteinDecidePath` string Reserved for future use.

`faultConnector` FlowConnector Specifies which node to execute if the action call results in
an error.

`flowTransactionModel` FlowTransactionModel (enumeration of Required. Specifies the transactional model for flows that
type string) execute invocable actions. Valid values are:

**•** `Automatic`                            - Creates a transaction if the invocable
action supports it and there’s pending DML.


Metadata Types Flow

**Field Name** **Field Type** **Description**

**•** `CurrentTransaction`                               - Keeps the invocable
action running in the same transaction.

**•** `NewTransaction`                               - Creates a transaction before
the invocable action is executed.

This field is available in API version 51.0 and later.

`inputParameters` FlowActionCallInputParameter[] An array of input parameters from the flow to the action.

`isWaitUntilCompleted` boolean

Specifies whether to pause the flow until the action is
completed. This field is available in API version 61.0 and
later.

`nameSegment` string Specifies the name of the versioned action. Supported only
when nameSegment is specified. This field is available in

API version 58.0 to 61.0. This field is deprecated in API
version 62.0 and later.

`offset` int

Specify the number of months, days, hours, or minutes to
pause the flow while it waits for the action to be completed.
This field is available in API version 61.0 and later.

`offsetUnit` FlowScheduledPathOffsetUnit Specify the time unit used to wait when the async action
(enumeration of type string) executes. Possible values are:

**•** `Months`

**•** `Days`

**•** `Hours`

**•** `Minutes`

This field is available in API version 61.0 and later.

`outputParameters` FlowActionCallOutputParameter[] An array of output parameters from the action to the flow.

`storeOutputAutomatically` boolean Indicates whether the action’s output parameters are
automatically available in the flow without creating any

variables. When the value is `true`, you can reference an
output parameter by specifying the API name of the Action
element in the flow. The default value is `false` . When the
value is `false`, create variables manually to store output
values from the action.

This field is available in API version 48.0 and later.

`timeoutConnector` FlowConnector

Specifies which node to execute if an async action execution
is timed out. This field is available in API version 62.0 and
later.

`timeoutPathUsage` FlowActionCallTimeoutPath (enumeration Include or exclude a timeout path for an asynchronous
of type string) action in a flow. Valid values are:

**•** `DisableTimeoutPath`

**•** `EnableTimeoutPath`


Metadata Types Flow

**Field Name** **Field Type** **Description**

This field is available in API version 66.0 and later.

`versionSegment` int Specifies the version of the versioned action. By default, the
value is 1. Supported only when versionSegment is specified.

This field is available in API version 58.0 to 61.0. This field is
deprecated in API version 62.0 and later.

`versionString` string Reserved for future use.

InvocableActionType

The valid values in the required `actionType` on FlowActionCall on page 1228.

**Valid Value** **Description**

`activateSessionPermSet` Activates a session-based permission set for the running user.

`activationSchema` Gets the activation schema for the specified activation. This value is available in API version 64.0
and later.

`addMessageToChat` Adds a message to an existing Salesforce Anywhere chat. This value is available in API version
49.0 and later.

`addMessageToQuipChat` Adds a Quip message to an existing chat room. This value is available in API version 46.0 and
later.

`addMessageToQuipDocument` Adds a Quip message to an existing Quip document, spreadsheet, or slide. This value is available
in API version 46.0 and later.

`addQuipDocumentToFolder` Adds an existing Quip document, spreadsheet, or slide to an existing folder. This value is available
in API version 46.0 and later.

`addUsersToChat` Adds users to an existing Salesforce Anywhere chat. This value is available in API version 49.0
and later.

`addUsersToQuipDocument` Adds users, identified by their email addresses, to an existing Quip document, spreadsheet, or
slide. This value is available in API version 46.0 and later.

`addUsersToQuipChat` Adds users, identified by their email addresses, to an existing Quip chat room. This value is
available in API version 46.0 and later.

`adjustPartnerInvShipAndDebit` Adjusts the point of sales record during ship and debit claim pocessing to a different partner
unsold inventory. Available in API version 64.0 and later.

`adjustPartnerUnsoldInventory` Adjusts the partner unsold inventory quantities and prices. Available in API version 64.0 and
later.

`answerQuestionsWithSalesforceDocumentation` Searches Salesforce documentation to provide answer to questions, as well as links to relevant
articles.

`analyticsSendDigestAsSlackMsg` Sends an Analytics digest to a Slack channel. This value is available in API version 64.0 and later.


Metadata Types Flow

**Valid Value** **Description**

`attachQuipDocumentToRecord` Attaches a Quip document, spreadsheet, or slide to a Salesforce record. This value is available
in API version 46.0 and later.

`apex` Invokes an Apex method that has the @invocableMethod annotation.

`archiveKnowledgeArticles` Archives a list of published Knowledge articles. This value is available in API version 45.0 and
later.

```
assignApptForServiceResourceForFieldService

```

Assigns the service appointment selected by the dispatcher to a service resource, in the gap
identified in the service resource’s schedule on a specific date. This value is available in API
version 63.0 and later.

`assignKnowledgeArticles` Mass assigns knowledge articles from article list views. This value is available in API version 44.0
and later.

`automateRefund` Initiate a refund to the customer. This value is available in API version 60.0 and later.

```
buildIdentityVerification

```

Calls an action that builds the identity verification context using the identity verification process
definition specified in IdVerfProcessDefinition and information passed into the flow. Stores the
result in the VerificationContext variable. This value is available in API version 55.0 and later.

`cdpGetDataGraph` Query a data graph in Data Cloud by data graph API name, data space name, and record ID. This
resource is available in API version 61.0 and later.

`cdpGetDataGraphByLookup` Get data of a data graph in Data Cloud by data graph API name, data space name, and lookup
key. This resource is available in API version 63.0 and later.

```
cdpGetDataGraphMetadata

```

Get metadata of a data graph in Data Cloud by data graph API name and data space name. If
the data space name isn't provided, the API uses the default value. This resource is available in
API version 64.0 and later.

`cdpPublishCalculatedInsight` Run the calculated insight in Data Cloud. Available in API version 60.0 and later.

`cdpPublishSegment` Publish a segment in Data Cloud. Available in API version 60.0 and later.

`cdpRefreshDataStream` Refresh a data stream in Data Cloud. Available in API version 60.0 and later.

`cdpRunIdentityResolution` Runs a Data Cloud identity resolution process. This value is available in API version 57.0 and later.

`cdpValidateSegmentMember` Validate a segment in Data Cloud. Available in API version 60.0 and later.

`calcPriceProtectPayoutAmt` Calculates the payout after a price protection adjustment or execution is made. This value is
available in API version 63.0 and later.

`chat` Creates a Salesforce Anywhere chat. This value is available in API version 49.0 and later.

`chatterPost` Posts to Chatter.

`choosePricebook` Selects a price book.

`component` Invokes the Aura component that implements the lightning:availableForFlowActions interface
and that is referenced by actionName. This value is available in API version 43.0 and later.

`computeConsumption` Determines if a consumption threshold has been reached.

`contactRequestAction` Creates a contact request record. This value is available in API version 45.0 and later.


Metadata Types Flow

**Valid Value** **Description**

`contentWorkspaceEnableFolders` Enables folders in a library.

`convertAttributesToJson` Converts the given attributes into a JSON string format. This value is available in API version 64.0
and later.

`copyQuipDocument` Creates a copy of an existing Quip document, spreadsheet, or slide, and gives it a new title. This
value is available in API version 46.0 and later.

`createConsumptionAlert` Creates a consumption alert and sends a notification.

`createDraftFromOnlineKnowledgeArticle` Creates a draft from a published knowledge article. This value is available in API version 45.0 and
later.

`createFieldGnrnPromptTmplResp` Creates a field generation prompt template response. This value is available in API version 62.0
and later.

`createInvoiceFromFulfillmentOrder` Creates an invoice from a purchase order. Available to B2B Commerce. This value is available in
API version 49.0 and later.

`createQuipChat` Creates a Quip chat room. This value is available in API version 46.0 and later.

`createQuipDocument` Creates a Quip document, spreadsheet, or slide. This value is available in API version 46.0 and
later.

`createQuipFolder` Creates a Quip folder. This value is available in API version 46.0 and later.

`customNotificationAction` Sends a custom notification. This value is available in API version 46.0 and later.

`dataCloudIngestionApi` Send data to Data Cloud using Ingestion API. This value is available in API version 61.0 and later.

`deactivateSessionPermSet` Deactivates a session-based permission set for the running user.

`deleteKnowledgeArticle` Deletes a draft version (translation or master-language) or an entire archived knowledge article.
This value is available in API version 46.0 and later.

`dynamicSendSurveyInvitation` Sends customized notifications to users about important events or updates to the records that
they're working on. This value is available in API version 51.0 and later.

`editQuipDocument` Modifies the contents of an existing Quip document, spreadsheet, or slide. This value is available
in API version 46.0 and later.

```
einsteinDecidePath

```

Determines a user's level of email engagement using Einstein Engagement Frequency or Einstein
Engagment Scoring, and route users through the flow based on that engagement. This value
is available in API version 64.0 and later.

`emailAlert` Sends an email by referencing a workflow email alert

`emailSimple` Sends an email by using flow resources. This action isn't available for flows with a processType
of Workflow.

`exploreConversation` Retrieves insights from a conversation. This value is available in API version 61.0 and later.

`externalConnector` Executes a process or method exposed via a connector to an external system. This value is
available in API version 63.0 and later.


Metadata Types Flow

**Valid Value** **Description**

```
externalService

```

Invokes an External Service operation that makes an HTTP request to an external system made
available by an External Service schema registered through Setup. This value is available in API
version 46.0 and later.

`findMatchingIndividuals` Finds contact, lead, or employee records that match a search term.

```
findPastCollaborators

flow

```

Leverages insights from Einstein Activity Capture to identify individuals with past collaborative
ties, aiding in securing introductions to relevant parties in ongoing or future deals. This value is
available in API version 63.0 and later.

Invokes an autolaunched flow. This action type isn't available for flows with a processType of
Flow or AutolaunchedFlow. To invoke an autolaunched flow from one of those types, use
FlowSubflow. This value is available in API version 32.0 and later.

`generateAiAgentResponse` Generates a response from the AI agent based on input and instructions to support intelligent,
conversational experiences. This value is available in API version 63.0 and later.

`generateAnalyticsAssetsContent` Generates Analytics assets content. This value is available in API version 64.0 and later.

`generateVerificationCode` Sends a verification code to the customer's email to verify their identity. This value is available
in API version 63.0 and later.

`getActivitySummary` Gets a summary of activity data associated with a specified record, including emails, calls, and
meetings. This value is available in API version 60.0 and later.

```
getArticleSmartLinkUrl

```

Gets the Smart Link URL of the Salesforce Knowledge article. Smart links go to the right article
and version, even when a new version is published or the URL name changes. This value is
available in API version 54.0 and later.

`getPoliciesByObject` Gets Policy Center policies that contain a given object and returns a list of matching policy
names.

`getPoliciesByPolicyType` Gets Policy Center policies of the type specified in the user input, such as Data Backup or Data
Archive.

`getPolicyDetails` Gets details about a policy in Policy Center, such as the policy type and the objects the policy
targets.

```
getProductPricing

getResourcesForMnlScheduling

getSalesAgreementDetails

```

Gets the pricing information of a product, including relevant historical sale price data from
previous won deals involving the same product. This value is available in API version 63.0 and
later.

Recommends resources to use to manually schedule the start of a care visit or recurring visits.
You must enable Home Health to use this action. This value is available in API version 61.0 and
later.

Retrieves a comprehensive collection of all required data (spread across multiple entities like
SalesAgreement, Product2, SalesAgreementProduct, etc.) for a given Sales Agreement. Available
