Represents the ReferencedDashboard object in CRM Analytics. A referenced dashboard stores information about an externally
referenced dashboard.

RelatedRecordAssocCriteria
Represents criteria for automatically linking records like accounts, leads, opportunities, and cases with the branches that work with
them.

RelationshipGraphDefinition
Represents a definition of a graph that you can configure in your organization to traverse object hierarchies and record details, giving
you a glimpse of how your business works.

RemoteSiteSetting
Represents a remote site setting. Before any Visualforce page, Apex callout, or JavaScript code using XmlHttpRequest in an s-control
or custom button can call an external site, that site must be registered in the Remote Site Settings page, or the call fails.

Report
Represents a custom report. This metadata type only supports custom reports; standard reports aren’t supported.

ReportType
Represents the metadata associated with a custom report type. Custom report types allow you to build a framework from which
users can create and customize reports.

RestrictionRule
Represents a restriction rule or a scoping rule. A restriction rule has `enforcementType` set to `Restrict` and controls the
access that specified users have to designated records. A scoping rule has `enforcementType` set to `Scoping` and controls
the default records that your users see without restricting access. This type extends the Metadata metadata type and inherits its
`fullName` field.

RetrievalSummaryDefinition
Represents a metadata type that stores the header information of a retrieval definition. It enables the configuration of data retrieval
patterns for summarizing related records across object relationships.

Role
Represents a role in your organization.

RoleOrTerritory
Represents the common base type and valid values for role or territory.

RpaRobotPoolMetadata
Reserved for future use.

SalesWorkQueueSettings
Represents settings used to customize work queue options for third-party scoring. In Sales Engagement, you can add a custom
number field on person accounts, contacts, or leads. Then, use the custom number field to sort the work queue. This type extends
the Metadata metadata type and inherits its `fullName` field.

SamlSsoConfig
Represents a SAML Single Sign-On configuration. This type extends the Metadata metadata type and inherits its `fullName` field.
Single sign-on (SSO) is an authentication method that enables users to access multiple applications with one login and one set of
credentials. For example, after users log in to your org, they can automatically access all apps from the App Launcher. You can set
up your Salesforce org to trust a third-party identity provider to authenticate users. Or you can configure a third-party app to rely on
your org for authentication.


Metadata Types

SchedulingObjective
Represents a scheduling objective in Workforce Engagement. Scheduling objectives define business goals that the scheduling tools
consider when identifying agents for shifts.

SchedulingRule
Represents a scheduling rule in Workforce Engagement Management. Scheduling rules determine when agents are assigned to
shifts.

Scontrol
Deprecated. Represents an Scontrol component, corresponding to an s-control in the Salesforce user interface.

SearchCustomization
Represents the configuration of search settings created in Search Manager. The configuration includes the search channel, searchable
objects and fields, and rules to filter search results.

SearchOrgWideObjectConfig
Represents an object in the search index. The search index contains org-wide search settings created in Search Manager. Each object
in the search index includes searchable fields and fields protected by field-level security in search.

ServiceAISetupDefinition
Represents settings for an Einstein for Service feature such as Einstein Article Recommendations. This type extends the Metadata
metadata type and inherits its `fullName` field.

ServiceAISetupField
Represents a field on cases or knowledge articles that Einstein uses to identify relevant articles in Einstein Article Recommendations.
This type extends the Metadata metadata type and inherits its `fullName` field.

ServiceChannel
Represents a channel of work items that are received from your organization—for example, cases, chats, or leads.

ServicePresenceStatus
Represents a presence status that can be assigned to a service channel. This type extends the Metadata metadata type and inherits
its `fullName` field.

ServiceProcess
Represents a process created in Service Process Studio and its associated attributes.

Settings
Represents the organization settings related to a feature. For example, your password policies, session settings and network access
controls are all available in the SecuritySettings component type.

SharedTo
SharedTo defines the sharing access for a list view or a folder. It can be used to specify the target and source for owner-based sharing
rules.

SharingBaseRule
Represents sharing rule settings such as access level and to whom access is granted.

SharingRules
Represents the base container for sharing rules, which can be criteria-based, ownership-based, territory-based, or for guest user
access. SharingRules enables you to share records with a set of users, using rules that specify the access level for the target user
group.

SharingSet
Represents a sharing set. A sharing set defines an access mapping that grants portal or community users access to objects that are
associated with their accounts or contacts.


Metadata Types

SiteDotCom
Represents a site for deployment.

Skill
Represents the settings for a skill used for field service or to route chats to agents in Chat, such as the name of the skill and which
agents the skills are assigned to.

StandardValueSet
Represents the set of values in a standard picklist field. This type extends the Metadata metadata type and inherits its `fullName`
field.

StandardValueSetTranslation
Contains details for a standard picklist translation. It returns a translated standard value set.This type extends the Metadata metadata
type and inherits its `fullName` field.

StaticResource
Represents a static resource file, often a code library in a ZIP file. Static resources allow you to upload content that you can reference
in a Visualforce page, including archives (such as .zip and .jar files), images, style sheets, JavaScript, and other files. Static resources
can be used only within your Salesforce org, so you can’t host content here for other apps or websites.

StageAssignment
Represents a collection of fields to automatically assign stage definitions to records based on rule criteria.

StageDefinition
Represents a collection of fields to set up the states and transitions for Stage Management.

SustainabilityUom
Represents the unit of measure (UOM) values for custom fuel types in an org. Track fuel consumption and emission results with the
flexibility to add custom fuel types and UOM values.

SustnUomConversion
Represents information about the unit of measure (UOM) conversion for the custom fuel types defined by a customer in an org.

SvcCatalogCategory
Represents the grouping of individual catalog items in Service Catalog.

SvcCatalogFulfillmentFlow
Represents the flow associated with a specific catalog item in the Service Catalog.

SvcCatalogItemDef
Represents the entity associated with a specific, individual service available in the Service Catalog.

SynonymDictionary
Represents a set of synonym groups, which are groups of words or phrases that are treated as equivalent in users’ searches. You can
define synonym groups to optimize search results for acronyms, variations of product names, and other terminology unique to your
organization.

Tag
Reserved for future use.

TagSet
Reserved for future use.

Territory
Represents a territory.


Metadata Types

Territory2
Represents the metadata associated with a sales territory. This type extends the Metadata metadata type and inherits its `fullName`
field. Available if Sales Territories has been enabled.

Territory2Model
Represents the metadata associated with a territory model in Sales Territories. This type extends the Metadata metadata type and
inherits its `fullName` field. Available if Sales Territories has been enabled.

Territory2Rule
Represents the metadata associated with a territory assignment rule associated with an object, such as Account. Available if Sales
Territories has been enabled.

Territory2Type
Represents the metadata for a category of territories in Sales Territories. Every Territory2 must have a Territory2Type. This type extends
the Metadata metadata type and inherits its `fullName` field. Available if Sales Territories has been enabled.

TimelineObjectDefinition
Represents the container that stores the details of a timeline configuration. You can use this resource with Salesforce objects to see
their records' related events in a linear time-sorted view.

TimeSheetTemplate
Represents a template for creating time sheets in Field Service. This type extends the Metadata metadata type and inherits its
`fullName` field.

TopicsForObjects
Represents the ability to assign topics to objects or to remove topic assignments.

TransactionSecurityPolicy
Represents a transaction security policy definition. Transaction security policies give you a way to look through events in your
organization and specify actions to take when certain combinations occur.

Translations
Metadata type that enables work with translations for various supported languages. The ability to translate component labels is part
of the Translation Workbench.

UIBundle (Beta)
Represents a Salesforce Multi-Framework app, such as a React app.

UiFormatSpecificationSet
Represents a set of rules that define the style and visibility of conditional field formatting on Dynamic Forms-enabled Lightning page
field instances.

UIObjectRelationConfig
Represents the admin-created configuration of the object relation UI component.

UiPreviewMessageTabDef
Represents the registration of a custom Marketing Cloud Preview and Test modal tab, created using custom Lightning web components.
You can register and show multiple tabs in the Preview and Test experience.

UserAccessPolicy
Represents a user access policy.

UserAuthCertificate
Represents a PEM-encoded user certificate. These certificates are associated with a user, and externally uploaded. The uploaded
certificate is used to authenticate the user.


Metadata Types

UserCriteria
Represents the member criteria to use in Experience Cloud site moderation rules. This type extends the Metadata metadata type
and inherits its `fullName` field..

UserProfileSearchScope
Reserved for internal use.

UserProvisioningConfig
Represents information to use during a user provisioning request flow, such as the attributes for an update. This type extends the
Metadata metadata type and inherits its `fullName` field.

VirtualVisitConfig
Represents an external video provider configuration, which relays events from Salesforce to the provider.

WaveAnalyticAssetCollection
Represents a collection of Analytics assets. This type extends the Metadata metadata type and inherits its `fullName` field.

WaveApplication
Represents the Analytics application. This type extends the Metadata metadata type and inherits its `fullName` field.

WaveComponent
Represents the WaveComponent object in the Analytics application. This type extends the MetadataWithContent metadata type
and inherits its `content` and `fullName` fields.

WaveDataflow
Represents the WaveDataflow object in the Analytics application. This type extends the MetadataWithContent metadata type and
inherits its `content` and `fullName` fields.

WaveDashboard
Represents the WaveDashboard object in the Analytics application. This type extends the MetadataWithContent metadata type and
inherits its `content` and `fullName` fields.

WaveDataset
Represents the WaveDataset object in the Analytics application. This type extends the Metadata metadata type and inherits its
`fullName` field.

WaveLens
Represents the WaveLens object in the Analytics application.

WaveRecipe
Represents the WaveRecipe type in an Analytics application. A recipe is a saved set of steps to perform on a specific source dataset
or connected data. This type extends the MetadataWithContent metadata type and inherits its `content` and `fullName` fields.

WaveTemplateBundle
Represents an Analytics template bundle, which can be used to create Analytics apps. A bundle contains an Analytics template
definition and all its related resources.This type extends the Metadata metadata type and inherits its `fullName` field.

WaveXmd
Represents the WaveXmd object in the Analytics application. This type extends the Metadata metadata type and inherits its
`fullName` field.

WebStoreBundle
For internal use only.

WebStoreTemplate
Represents a configuration for creating commerce stores.


### Metadata Types Metadata Components and Types

Workflow
Represents the metadata associated with a workflow rule. A workflow rule sets workflow actions into motion when its designated
conditions are met. You can configure workflow actions to execute immediately when a record meets the conditions in your workflow
rule, or set time triggers that execute the workflow actions on a specific day. Use this metadata type to create, update, or delete
workflow rule definitions.

WorkSkillRouting
Represents a setup object that stores a set of WorkSkillRoutingAttribute objects. These objects are used to route a work item to an
agent who has the skills necessary to take the work. This type extends the Metadata metadata type and inherits its `fullName`
field.

### Metadata Components and Types

Metadata components are not based on sObjects, like objects in the API. Instead, they are based on metadata types, such as ApexClass
and CustomObject, which extend Metadata, the base class for all metadata types. A component is an instance of a metadata type.

For example, `CustomObject` is a metadata type for custom objects, and the `MyCustomObject__c` component is an instance
of a custom object.

A metadata type can be identified in the metadata WSDL as any complexType that extends the Metadata complexType. A complexType
that is a metadata type includes the following element in its WSDL definition:

```
   <xsd:extension base="tns:Metadata">

```

CustomObject and BusinessProcess extend Metadata so they are metadata types; ActionOverride doesn't extend Metadata so it's not a
metadata type.

You can individually deploy or retrieve a component for a metadata type. For example, you can retrieve an individual BusinessProcess
component, but you can't retrieve an individual ActionOverride component. You can only retrieve an ActionOverride component by
retrieving its encompassing CustomObject component.

Metadata components can be manipulated by asynchronous Metadata API calls or declarative (or file-based) Metadata API calls.

Most of the components can be accessed using Salesforce Extensions for Visual Studio Code. Exceptions are noted in the description of
the object.

Field Data Types

Each component field has a specific field type. These field types can correspond to other components defined in the WSDL, or primitive
data types, like `string`, that are commonly used in strongly typed programming languages.

These field data types are used in the messages that are exchanged between your client application and the API. When writing your
client application, follow the data typing rules defined for your programming language and development environment. Your development
tool handles the mapping of typed data in your programming language with these data types.

[For more information, see Primitive Data Types in the Salesforce Object Reference.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/primitive_data_types.htm)

Enumeration Fields

Some component fields have a data type that is an enumeration. An enumeration is the API equivalent of a picklist. The valid values of
the field are restricted to a strict set of possible values, all having the same data type. These values are listed in the field description


### Metadata Types Metadata Coverage Report

column for each enumeration field. See `sortBy` for an example of an enumeration field of type string. The XML below shows a sample
definition of an enumeration of type string in the WSDL.

```
   <xsd:simpleType name="DashboardComponentFilter">

      <xsd:restriction base="xsd:string">

        <xsd:enumeration value="RowLabelAscending"/>

        <xsd:enumeration value="RowLabelDescending"/>

        <xsd:enumeration value="RowValueAscending"/>

        <xsd:enumeration value="RowValueDescending"/>

      </xsd:restriction>

   </xsd:simpleType>

```

Supported Calls

All of the metadata types are supported by the main calls, unless it is stated otherwise in the individual component sections. The main
Metadata API calls are:

**•** CRUD calls, such as createMetadata() and deleteMetadata()

**•** File-based calls, such as deploy() and retrieve()

**•** Utility calls, such as listMetadata() and describeMetadata()

### Metadata Coverage Report

Launch the Metadata Coverage report to determine supported metadata components. The Metadata Coverage report is the ultimate
source of truth for metadata coverage across several channels. These channels include Metadata API, scratch org source tracking, unlocked
packages, second-generation managed packages, classic managed packages, and more.

[To view the Metadata Coverage report, you don’t have to be logged into an org.](https://developer.salesforce.com/docs/success/metadata-coverage-report/references/coverage-report/metadata-coverage-report.html)

### Unsupported Metadata Types

Some Salesforce features have metadata types that aren’t available in Metadata API. These metadata types can’t be retrieved or deployed
with Metadata API. To make changes to these types, you must do it manually in each of your organizations.

Some metadata types may also be unsupported in source tracking, packaging, and change sets.

[For a complete list of metadata types and where they’re supported, see Metadata Coverage.](https://developer.salesforce.com/docs/metadata-coverage)

SEE ALSO:

_Salesforce Developers_ [: Metadata Coverage](https://developer.salesforce.com/docs/metadata-coverage)

_Salesforce DX Developer Guide_ [: Track Changes Between Your Project and Org](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_source_tracking.htm)

_[Second-Generation Managed Packaging Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp.htm)_ : Second-Generation Managed Packages

_[Sandboxes: Staging Environments for Customizing and Testing](https://help.salesforce.com/s/articleView?id=platform.changesets.htm&type=5&language=en_US)_ : Change Sets

### Special Behavior in Metadata API Deployments

Important considerations for specific types and contents of a deployment.

Use the information here to determine what to include in your deployment and how the changes appear in the destination.


### Metadata Types Metadata Type Limits

[Special Behavior in Deployments](https://help.salesforce.com/s/articleView?id=platform.deploy_special_behavior.htm&type=5&language=en_US)

### Metadata Type Limits

Certain metadata types have deploy and retrieve limits. Limits apply to each individual deploy or retrieve transaction, and there are daily
limits for specific metadata types.

The individual deploy and retrieve limits represent the maximum count that a metadata type may be deployed or retrieved in a single
package zip. Daily deploy and retrieve limits apply to individual org usage within a 24-hour period.

Metadata Deploy Limits

**•** Individual Metadata Deploy: 50

**•** Daily Metadata Deploys: 100

Metadata Retrieve Limits

**•** Individual Metadata Retrieve: 100

**•** Daily Metadata Retrievals: 200

Deploy and Retrieve Metadata Limits apply to:

**•** AIAuthoringBundle

**•** AnalyticsDashboard

**•** AnalyticsVisualization

**•** AnalyticsWorkspace

### Data 360 Metadata Types

Check out the metadata types that are used for development in Data 360.

ActivationPlatform
Represents the ActivationPlatform configuration, such as platform name, delivery schedule, output format, and destination folder.

ActivationPlatformActvAttr
Represents the information about activation attributes. Reserved for future use.

ActivationPlatformField
Represents the information about the fields used in ActivationPlatform.

ActvPfrmDataConnectorS3
Represents the Amazon S3 bucket name and export directory.

ActvPlatformAdncIdentifier
Represents the information about the identifiers to be activated, such as Email, Phone, Mobile Advertiser (MAID) ID, and Over-the-top
(OTT) ID.

ActvPlatformFieldValue
Represents the field values for the ActivationPlatformFields.

AiPluginUtteranceDef
Represents an utterance that can be used to pick a topic during runtime.


Metadata Types Data 360 Metadata Types

CustomerDataPlatformSettings
Represents an org's Data 360 settings.

DataConnector
Represents the white-labeled metadata configuration for an external connector in Data 360.

DataConnectorIngestApi
Represents the connection information specific to Ingestion API.

DataConnectorS3
Represents the connection information specific to Amazon S3.

DataKitObjectTemplate
Represents the object in Data Kit Object Template. These object templates are added inside the data kit.

DataKitObjectDependency
Represents the dependency between two data kit objects. The object templates are added inside the data kit.

DataObjectBuildOrgTemplate
Represents the derived object template used to define the structure and configuration of data objects in a build organization. The
object templates are added inside the data kit to deploy metadata.

DataPackageKitDefinition
Represents the top-level data kit container definition. Content objects can be added after the data kit is defined.

DataPackageKitObject
Represents the object in Data Kit Content Object. These objects are added inside the data kit.

DataSource
Used to represent the system where the data was sourced. This object is always needed when creating a Data Stream Definition.

DataSourceBundleDefinition
Represents the bundle of streams that a user adds to a data kit.

DataSourceField
Represents the details of a data source field.

DataSourceObject
Represents the object from where the data was sourced.

DataSourceTenant
For internal use only.

DataSrcDataModelFieldMap
Represents the mappings between source data lake object (DLO) fields and target data model object (DMO) fields.

DataStreamDefinition
Contains data ingestion information such as connection, API, and file retrieval settings.

DataStreamTemplate
Represents the data stream that a user adds to a data kit.

ExternalDataConnector
Used to represent the object where the data was sourced.

ExternalDataSource
Represents the metadata associated with an external data source. Create external data sources to manage connection details for
integration with data and content that are stored outside your Salesforce org.


#### Metadata Types ActivationPlatform

ExternalDataTransportFieldTemplate
For internal use only.

ExternalDataTranObject
Represents a definition of a Data 360 schema object. This type extends the Metadata metadata type and inherits its `fullName`
field.

ExternalDataTransportObjectTemplate
For internal use only.

FieldSrcTrgtRelationship
Stores the relationships between a data model object (DMO) and its fields. For example, the `Individual.Id` field has a
one-to-many relationship (1:M) with the `ContactPointEmail.PartyId` field.

InternalDataConnector
For internal use only.

MarketSegmentDefinition
Represents the field values for MarketSegmentDefinition. MarketSegmentDefinition is used to store the exportable metadata of a
segment, such as segment criteria and other attributes. Developers can create segment definition packages, pass segment definition
in the form of data build tool (DBT), and publish it on AppExchange for subscriber organizations to install and instantiate these
segments.

MktCalcInsightObjectDef
Represents Calculated Insight definition such as expression.

MktDataTranObject
An entity that is used to deliver (aka transport) information from the source to a target (target will be called a landing entity).This
can be the schema of a file, API, Event, or other means of transporting data, such as SubscriberFile1.csv, or SubscriberCDCEvent.

ObjectSourceTargetMap
Contains the object-level mappings between the source and the target objects. The source and target objects can be an
MktDataLakeObject or an MktDataModelObject. For example, an Email source object can be mapped to the ContactPointEmail
object.

StreamingAppDataConnector
Represents the connection information specific to Web and Mobile Connectors.

SEE ALSO:

_[Developer Center](https://developer.salesforce.com/developer-centers/data-cloud)_ : Data Cloud

#### ActivationPlatform

Represents the ActivationPlatform configuration, such as platform name, delivery schedule, output format, and destination folder.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types ActivationPlatform

File Suffix and Directory Location

ActivationPlatform components have the suffix `.activationPlatform` and are stored in the `activationPlatforms` folder.

Version

ActivationPlatform components are available in API version 54.0 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Description**

```
activationPlatformConnectorType

activationPlatformAdditionalMetadata

dataConnector

description

enabled

```

**Field Type**
ActivationPlatformConnectorType (enumeration of type string)

**Description**
Reserved for future use.

**Field Type**
string

**Description**
Provides additional details about the activation platform, including subscriber override
options, partner supported IDs, and file output properties such as maximum file size,
compression settings, and the maximum number of records per file.

**Field Type**
string

**Description**
Reference to the ActvPfrmDataConnectorS3 metadata type, which contains S3 bucket
and export directory information into which Data 360 writes data.

**Field Type**
string

**Description**

Required.

The description for ActivationPlatform.

**Field Type**
boolean

**Description**

Required.


Metadata Types ActivationPlatform

**Field Name** **Description**

Indicates if ActivationPlatform is enabled ( `true` ) or not ( `false` ). The default is false.

```
includeSegmentNames

logoUrl

masterLabel

notes

outputFormat

outputGrouping

```

**Field Type**
boolean

**Description**
Indicates whether to include the segment name in metadata ( `true` ) or not ( `false` ).

**Field Type**
string

**Description**
URL of the logo for the activation channel destination.

**Field Type**
string

**Description**

Required.

The name for the activation channel destination.

**Field Type**
string

**Description**
Notes for this ActivationPlartform.

**Field Type**
ActivationPlatformFileOutputFormat (enumeration of type string)

**Description**

Required.

The output format of the file.

Valid values are:

**•** `CSV`

**•** `JSON`

**•** `PARQUET`

**Field Type**
ActivationPlatformFileOutputGrouping (enumeration of type string)

**Description**

Required.

The grouping of the output.

Valid values are:

**•** `PER_ACCOUNT`


Metadata Types ActivationPlatform

**Field Name** **Description**

**•** `PER_SEGMENT`

```
periodicRefreshFrequecy

platformType

refreshFrequency

refreshMode

```

**Field Type**
ActivationPlatformPeriodicFullRefresh (enumeration of type string)

**Description**
The frequency (in days) for periodic full refreshes when using incremental refresh
mode.

Valid values are:

**•** `REFRESH_30`

**•** `REFRESH_60`

**Field Type**
ActivationPlatformType (enumeration of type string)

**Description**

Required.

The type of the Activation Platform.

Valid values are:

**•** `Advertising`

**•** `Analytics`

**•** `Marketing`

**•** `Publishing`

**•** `Technology`

**Field Type**
ActivationPlatformRefreshFrequency (enumeration of type string)

**Description**

Required.

Indicates how often the activation platform accepts data delivery.

Valid value is:

**•** `TWENTY_FOUR`

**Field Type**
ActivationPlatformRefreshMode (enumeration of type string)

**Description**

Required.

Defines how the refresh method handles refreshing files.

Valid values are:

**•** `FULL`


Metadata Types ActivationPlatform

**Field Name** **Description**

**•** `INCREMENTAL`

Declarative Metadata Sample Definition

The following is an example of an ActivationPlatform component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ActivationPlatform xmlns="http://soap.sforce.com/2006/04/metadata">

      <dataConnector>S3Connector</dataConnector>

      <description>Activation Platform Description</description>

      <enabled>false</enabled>

      <includeSegmentNames>false</includeSegmentNames>

      <logoUrl>link to logo</logoUrl>

      <masterLabel>MyExternalPlatform</masterLabel>

      <notes>Notes about this Platform</notes>

      <outputFormat>CSV</outputFormat>

      <outputGrouping>PER_ACCOUNT</outputGrouping>

      <refreshMode>FULL</refreshMode>

      <refreshFrequency>TWENTY_FOUR</refreshFrequency>

      <periodicRefreshFrequecy>NEVER</periodicRefreshFrequecy>

      <platformType>Advertising</platformType>

   </ActivationPlatform>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <fullName>MyActivationPlatform</fullName>

      <types>

        <members>APlatform</members>

        <name>ActivationPlatform</name>

      </types>

      <types>

        <members>AccountIdField</members>

        <name>ActivationPlatformField</name>

      </types>

      <types>

        <members>S3Connector</members>

        <name>ActvPfrmDataConnectorS3</name>

      </types>

      <types>

        <members>EmailIdentifier</members>

        <name>ActvPlatformAdncIdentifier</name>

      </types>

      <types>

        <members>AccountIdFieldValue</members>

        <name>ActvPlatformFieldValue</name>

      </types>

      <version>54.0</version>

   </Package>

```


#### Metadata Types ActivationPlatformActvAttr

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### ActivationPlatformActvAttr

Represents the information about activation attributes. Reserved for future use.

#### ActivationPlatformField

Represents the information about the fields used in ActivationPlatform.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

#### ActivationPlatformField components have the suffix .activationPlatformField and are stored in the

`activationPlatformFields` folder.

Version

#### ActivationPlatformField components are available in API version 54.0 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Description**

```
activationPlatform

helpText

```

**Field Type**
string

**Description**

Required.

Reference to the ActivationPlatform metadata type.

**Field Type**
string


Metadata Types ActivationPlatformField

**Field Name** **Description**

**Description**
Information about ActivationPlatformField.

```
isHidden

isRequired

masterLabel

type

```

**Field Type**
boolean

**Description**

Required.

Indicates whether ActivationPlatformField can be overridden by marketer ( `false` )
or not ( `true` ). The default is false. Field can’t be overridden by marketer when set to
`true` .

**Field Type**
boolean

**Description**

Required.

Indicates whether this ActivationPlatformField is required ( `true` ) or not ( `false` ).
The default is false.

**Field Type**
string

**Description**

Required.

The name of the ActivationPlaformField.

**Field Type**
ActivationPlatformFieldDataType (enumeration of type string)

**Description**
Represents the datatype of the field.

Valid value is:

**•** `Text`

Declarative Metadata Sample Definition

The following is an example of an ActivationPlatformField component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ActivationPlatformField xmlns="http://soap.sforce.com/2006/04/metadata">

   <activationPlatform>APlatform</activationPlatform>

   <isHidden>false</isHidden>

   <isRequired>true</isRequired>

   <masterLabel>AccountId</masterLabel>

</ActivationPlatformField>

```


#### Metadata Types ActvPfrmDataConnectorS3

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <fullName>MyActivationPlatform</fullName>

      <types>

        <members>APlatform</members>

        <name>ActivationPlatform</name>

      </types>

      <types>

        <members>AccountIdField</members>

        <name>ActivationPlatformField</name>

      </types>

      <version>54.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### ActvPfrmDataConnectorS3

Represents the Amazon S3 bucket name and export directory.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

#### ActvPfrmDataConnectorS3 components have the suffix .actvPfrmDataConnectorS3 and are stored in the

`actvPfrmDataConnectorS3s` folder.

Version

#### ActvPfrmDataConnectorS3 components are available in API version 54.0 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.


Metadata Types ActvPfrmDataConnectorS3

Fields

**Field Name** **Description**

```
bucketName

exportDirectory

masterLabel

```

**Field Type**
string

**Description**

Required.

The Amazon S3 bucket name.

**Field Type**
string

**Description**
This is an optional field that is reserved for internal use.

**Field Type**
string

**Description**

Required.

The display name of ActvPfrmDataConnectorS3.

Declarative Metadata Sample Definition

The following is an example of an ActvPfrmDataConnectorS3 component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ActvPfrmDataConnectorS3 xmlns="http://soap.sforce.com/2006/04/metadata">

   <bucketName>MyS3Bucket</bucketName>

   <exportDirectory>Output</exportDirectory>

   <masterLabel>S3Connector</masterLabel>

</ActvPfrmDataConnectorS3>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <fullName>MyActivationPlatform</fullName>

   <types>

     <members>APlatform</members>

     <name>ActivationPlatform</name>

   </types>

   <types>

     <members>S3Connector</members>

     <name>ActvPfrmDataConnectorS3</name>

   </types>

   <version>54.0</version>

</Package>

```


#### Metadata Types ActvPlatformAdncIdentifier

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### ActvPlatformAdncIdentifier

Represents the information about the identifiers to be activated, such as Email, Phone, Mobile Advertiser (MAID) ID, and Over-the-top
(OTT) ID.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

#### ActvPlatformAdncIdentifier components have the suffix .actvPlatformAdncIdentifier and are stored in the

`actvPlatformAdncIdentifiers` folder.

Version

#### ActvPlatformAdncIdentifier components are available in API version 54.0 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Description**

```
activationPlatform

identifierHashMethod

```

**Field Type**
string

**Description**

Required.

Reference to the ActivationPlatform metadata type.Reference to ActivationPlatform.

**Field Type**
ActivationPlatformIdentifierHashMethod (enumeration of type string)

**Description**
The hash method of the identifier type. The supported hash method for Email and
Phone is `SHA256` . The supported hash method for MAID and OTT is `NONE` .


Metadata Types ActvPlatformAdncIdentifier

**Field Name** **Description**

```
identifierType

masterLabel

```

**Field Type**
ActivationPlatformIdentifierType (enumeration of type string)

**Description**

Required.

The type of identifier to be activated.

Valid values are:

**•** `EMAIL`

**•** `MAID`

**•** `OTT`

**•** `PHONE`

**Field Type**
string

**Description**

Required.

The name of the identifier.

Declarative Metadata Sample Definition

The following is an example of an ActvPlatformAdncIdentifier component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ActvPlatformAdncIdentifier xmlns="http://soap.sforce.com/2006/04/metadata">

   <activationPlatform>APlatform</activationPlatform>

   <identifierHashMethod>SHA256</identifierHashMethod>

   <identifierType>EMAIL</identifierType>

   <masterLabel>EmailIdentifier</masterLabel>

</ActvPlatformAdncIdentifier>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <fullName>MyActivationPlatform</fullName>

   <types>

     <members>APlatform</members>

     <name>ActivationPlatform</name>

   </types>

   <types>

     <members>EmailIdentifier</members>

     <name>ActvPlatformAdncIdentifier</name>

   </types>

   <version>54.0</version>

</Package>

```


#### Metadata Types ActvPlatformFieldValue

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### ActvPlatformFieldValue

Represents the field values for the ActivationPlatformFields.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

#### ActvPlatformFieldValue components have the suffix .actvPlatformFieldValue and are stored in the

`actvPlatformFieldValues` folder.

Version

#### ActvPlatformFieldValue components are available in API version 54.0 and later.

Special Access Rules

Fields

**Field Name** **Description**

```
activationPlatformField

isDefault

```

**Field Type**
string

**Description**

Required.

Reference to the ActivationPlatform metadata type.

**Field Type**
boolean

**Description**

Required.

Indicates whether the value is default ( `true` ) or not ( `false` ). The default is false.
Picklist isn’t supported in API version 54.0


Metadata Types ActvPlatformFieldValue

**Field Name** **Description**

```
masterLabel

value

```

**Field Type**
string

**Description**

Required.

The name of the field.

**Field Type**
string

**Description**
The value of `activationPlatformField` .

Declarative Metadata Sample Definition

The following is an example of an ActvPlatformFieldValue component.

Field with no value:

```
<ActvPlatformFieldValue xmlns="http://soap.sforce.com/2006/04/metadata">

   <activationPlatformField>AccountIdField</activationPlatformField>

   <isDefault>true</isDefault>

   <masterLabel>AccountIdValue</masterLabel>

   <value>null</value>

</ActvPlatformFieldValue>

```

Field with value:

```
<ActvPlatformFieldValue xmlns="http://soap.sforce.com/2006/04/metadata">

   <activationPlatformField>AccountIdField</activationPlatformField>

   <isDefault>true</isDefault>

   <masterLabel>AccountIdValue</masterLabel>

   <value>1234</value>

</ActvPlatformFieldValue>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <fullName>MyActivationPlatform</fullName>

   <types>

     <members>APlatform</members>

     <name>ActivationPlatform</name>

   </types>

   <types>

     <members>AccountIdField</members>

     <name>ActivationPlatformField</name>

   </types>

   <types>

     <members>AccountIdValue</members>

     <name>ActvPlatformFieldValue</name>

```


#### Metadata Types AiPluginUtteranceDef

```
      </types>

      <version>54.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### AiPluginUtteranceDef

Represents an utterance that can be used to pick a topic during runtime.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

#### AiPluginUtteranceDef components are part of other components, such as GenAiPlugin, and aren't used separately.

Version

#### AiPluginUtteranceDef components are available in API version 63.0 and later.

Special Access Rules

#### AiPluginUtteranceDef is available only if Agents is enabled in your org.

Fields

**Field Name** **Description**

```
developerName

language

```

**Field Type**
string

**Description**

Required.

Represents the API name of the utterance. Can contain only underscores and
alphanumeric characters and must be unique in your org. It must begin with a letter,
not include spaces, not end with an underscore, and not contain two consecutive
underscores.

**Field Type**
string


#### Metadata Types CustomerDataPlatformSettings

**Field Name** **Description**

**Description**

Required.

The language of the utterance.

```
masterLabel

utterance

```

**Field Type**
string

**Description**

Required.

The master label for the utterance.

**Field Type**
string

**Description**

Required.

The utterance.

Declarative Metadata Sample Definition

See GenAiPlugin on page 1391.

#### CustomerDataPlatformSettings

Represents an org's Data 360 settings.

Parent Type and Manifest Access

This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all the settings metadata types for the org are accessed using the “Settings” name. See Settings for more details.

File Suffix and Directory Location

#### CustomerDataPlatformSettings values are stored in the CustomerDataPlatformSettings.settings file in

the `settings` folder. The `.settings` files are different from other named components, because there is only one settings file for
each settings component.

Version

#### CustomerDataPlatformSettings components are available in API version 48.0 and later.


#### Metadata Types DataConnector

Special Access Rules

Fields

**Field Name** **Description**

```
enableCustomerDataPlatform

```

**Field Type**
boolean

**Description**
Indicates whether an org has Data 360 enabled ( `true` ) or not ( `false` ).

Declarative Metadata Sample Definition

The following is an example of a CustomerDataPlatformSettings component.

```
<?xml version="1.0" encoding="UTF-8"?>

<CustomerDataPlatformSettings xmlns=“http://soap.sforce.com/2006/04/metadata">

  <enableCustomerDataPlatform>true</enableCustomerDataPlatform>

</CustomerDataPlatformSettings>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns=“http://soap.sforce.com/2006/04/metadata">

  <types>

   <members>CustomerDataPlatform</members>

   <name>Settings</name>

  </types>

  <version>55.0</version>

</Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The wildcard
applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the manifest
file, see Deploying and Retrieving Metadata with the Zip File.

#### DataConnector

Represents the white-labeled metadata configuration for an external connector in Data 360.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types DataConnector

File Suffix and Directory Location

DataConnector components have the suffix `.dataconnector` and are stored in the `dataconnectors` folder.

Version

DataConnector components are available in API version 64.0 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Description**

```
attributes

description

errors

features

icon

```

**Field Type**

DataConnectorAttribute[]

**Description**
A list of configurable attributes for the data connector.

**Field Type**
string

**Description**

Required.

The description of the data connector.

**Field Type**

DataConnectorError[]

**Description**
A list of error messages or codes related to the connector’s behavior or configuration
validation.

**Field Type**
DataConnectorFeature[] (enumeration of type string)

**Description**
A list of features supported by the data connector.

Values are:

```
  Override

```

**Field Type**
string


Metadata Types DataConnector

**Field Name** **Description**

**Description**
A static resource in SVG format with dimensions of 100x100 pixels and a file size not
exceeding 100 KB.

```
licenseAgreement

masterLabel

ownerLocation

ownerLogo

ownerName

parentConnector

releaseLevel

```

**Field Type**
string

**Description**
Text of the license agreement associated with the data connector.

**Field Type**
string

**Description**

Required.

The display label of the connector used in user interface (UI).

**Field Type**
string

**Description**
A description or URL that specifies where the connector is maintained or hosted.

**Field Type**
string

**Description**
A static resource in SVG format with dimensions of 100x100 pixels and a file size not
exceeding 100 KB.

**Field Type**
string

**Description**
The name of the organization that owns the connector.

**Field Type**
string

**Description**
The API name of the connector. For example, AwsS3, SNOWFLAKE, ICEBERG, and so
on.

**Field Type**
DataConnectorReleaseLevel (enumeration of type string)

**Description**

Required.


Metadata Types DataConnector

**Field Name** **Description**

Indicates the connector’s lifecycle stage.

Values are:

**•** `BETA`

**•** `GA`

**•** `IN_DEV`

**•** `PILOT`

```
supportEmail

supportMessage

supportPhone

translations

```

DataConnectorAttribute

**Field Type**
string

**Description**
The support email address users can contact for help with the connector.

**Field Type**
string

**Description**
A support-related message or instruction displayed.

**Field Type**
string

**Description**
The support phone number users can call for help with the connector.

**Field Type**
LocalizedValue[]

**Description**
A list of localized labels and descriptions to support multiple languages in the UI.

**Field Name** **Description**

```
capabilities

```

**Field Type**
DataConnectorCapability[] (enumeration of type string)

**Description**
A list of supported capabilities for the data connector.

Values are:

**•** `DataIn`

**•** `DataInDelete`

**•** `DataInHeader`

**•** `DataInIncremental`


Metadata Types DataConnector

**Field Name** **Description**

**•** `DataInSelector`

**•** `DataInStructured`

**•** `DataInUnstructured`

**•** `DataOut`

**•** `Hidden`

**•** `UniqueGroup`

**•** `ZeroCopyIn`

```
command

commandAttributes

dataType

```

**Field Type**
string

**Description**
The command string executed during data operations, such as import or sync.

**Field Type**
string

**Description**
A list of attributes passed with the command.

**Field Type**
DataConnectorDataType (enumeration of type string)

**Description**

Required.

Specifies the type of data input expected.

Values are:

**•** `CHECKBOX`

**•** `COMBOBOX`

**•** `DATE`

**•** `DATETIME`

**•** `EMAIL`

**•** `IDP`

**•** `NAMED_CREDENTIAL`

**•** `NUMBER`

**•** `PASSWORD`

**•** `PASSWORD_FILE`

**•** `PRIVATE_NETWORK_ROUTE`

**•** `RADIO`

**•** `RADIO_BUTTONS`

**•** `TEXT`

**•** `TEXTAREA`


Metadata Types DataConnector

**Field Name** **Description**

**•** `TIME`

**•** `TOGGLE`

```
defaultValue

editable

externalName

masterLabel

max

min

options

```

**Field Type**
string

**Description**
The default value assigned to the field if no user input is provided.

**Field Type**
boolean

**Description**
Indicates whether the field value can be modified by the user.

**Field Type**
string

**Description**

Required.

The unique name used to reference the connector externally, such as in API calls.

**Field Type**
string

**Description**

Required.

The label used for display in the UI.

**Field Type**
string

**Description**
The maximum allowable value or length for the field.

**Field Type**
string

**Description**
The minimum allowable value or length for the field.

**Field Type**

DataConnectorAttributeOpt[]

**Description**
A list of selectable options available for the field.


Metadata Types DataConnector

**Field Name** **Description**

```
order

pattern

placeholder

readonly

required

secure

tooltip

translations

```

**Field Type**
int

**Description**

Required.

The display order or evaluation order of the field.

**Field Type**
string

**Description**
The validation pattern used to ensure input follows a defined format.

**Field Type**
string

**Description**
The placeholder text displayed in the input field when empty.

**Field Type**
boolean

**Description**
Indicates whether the field is read-only.

**Field Type**
boolean

**Description**
Indicates whether the field must have a value.

**Field Type**
boolean

**Description**
Indicates whether the field contains sensitive data and should be masked.

**Field Type**
string

**Description**
The tooltip text shown to users for additional guidance.

**Field Type**
LocalizedValue[]

**Description**
A list of localized labels and descriptions for use in different languages.


Metadata Types DataConnector

**Field Name** **Description**

```
validationMessageError

```

DataConnectorAttributeOpt

**Field Type**
string

**Description**
The error message shown when input validation fails for this field.

**Field Name** **Description**

```
capabilities

conditionAttributes

externalName

masterLabel

```

**Field Type**
DataConnectorCapability[] (enumeration of type string)

**Description**
A list of capabilities supported by the data connector.

Values are:

**•** `DataIn`

**•** `DataInDelete`

**•** `DataInHeader`

**•** `DataInIncremental`

**•** `DataInSelector`

**•** `DataInStructured`

**•** `DataInUnstructured`

**•** `DataOut`

**•** `Hidden`

**•** `UniqueGroup`

**•** `ZeroCopyIn`

**Field Type**
string

**Description**
A list of attributes used to define conditions in the connector configuration.

**Field Type**
string

**Description**

Required.

The unique name used to reference the connector externally, such as in API calls.

**Field Type**
string


Metadata Types DataConnector

**Field Name** **Description**

**Description**

Required.

The display label for the connector used in the UI.

```
order

translations

```

DataConnectorError

**Field Type**
int

**Description**

Required.

The order or priority of the connector in processing context.

**Field Type**
LocalizedValue[]

**Description**
A list of localized labels and descriptions for use in different languages.

**Field Name** **Description**

```
externalName

masterLabel

translations

```

**Field Type**
string

**Description**

Required.

The unique name used to reference the object externally, such as in API calls. Must be
unique across the namespace.

**Field Type**
string

**Description**

Required.

The label displayed in the UI.

**Field Type**
LocalizedValue[]

**Description**
A list of localized labels and descriptions for use in different languages.


Metadata Types DataConnector

Declarative Metadata Sample Definition

The following is an example of a DataConnector component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <DataConnector xmlns="http://soap.sforce.com/2006/04/metadata">

      <masterLabel>Iceberg Override</masterLabel>

      <icon>Salesforce</icon>

      <parentConnector>ICEBERG</parentConnector>

      <releaseLevel>BETA</releaseLevel>

      <description>Connect to Apache Iceberg tables</description>

      <features>Override</features>

      <ownerName>Slack</ownerName>

      <ownerLogo>Salesforce</ownerLogo>

      <ownerLocation>Settle, USA</ownerLocation>

      <supportMessage>Click download logs before reachout</supportMessage>

      <supportPhone>+15788467513</supportPhone>

      <licenseAgreement>https://www.salesforce.com/company/legal</licenseAgreement>

      <attributes>

        <fullName>IcebergOverride_storageSourceType</fullName>

        <externalName>storageSourceType</externalName>

        <masterLabel>Storage Type</masterLabel>

        <dataType>COMBOBOX</dataType>

        <defaultValue>CATALOG_PROVIDED</defaultValue>

        <capabilities>DataIn</capabilities>

        <capabilities>Hidden</capabilities>

        <order>20</order>

        <editable>true</editable>

        <required>true</required>

        <secure>true</secure>

      </attributes>

   </DataConnector>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>DataConnector</name>

      </types>

      <types>

        <members>*</members>

        <name>StaticResource</name>

      </types>

      <version>64.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


#### Metadata Types DataConnectorIngestApi DataConnectorIngestApi

Represents the connection information specific to Ingestion API.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

#### DataConnectorIngestApi components have the suffix .dataConnectorIngestApi and are stored in the

`dataConnectorIngestApis` folder.

Version

#### DataConnectorIngestApi components are available in API version 54.0 and later.

Special Access Rules

You must have the CustomizeApplication user permissions to access the DataConnectorIngestApi type.

Fields

**Field Name** **Description**

```
masterLabel

sourceName

```

**Field Type**
string

**Description**

Required.

UI label of the Ingestion API Connector.

**Field Type**
string

**Description**

Required.

Name of the Ingestion API Connector.


#### Metadata Types DataConnectorS3

Declarative Metadata Sample Definition

The following is an example of a DataConnectorIngestApi component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <DataConnectorIngestApi xmlns="http://soap.sforce.com/2006/04/metadata">

      <sourceName>CONNECTOR NAME</sourceName>

      <masterLabel>CONNECTOR NAME</masterLabel>

   </DataConnectorIngestApi>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <DataConnectorIngestApi xmlns="http://soap.sforce.com/2006/04/metadata">

      <sourceName>MyConnector</sourceName>

      <masterLabel>MyConnector</masterLabel>

   </DataConnectorIngestApi>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### DataConnectorS3

Represents the connection information specific to Amazon S3.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

#### DataConnectorS3 components have the suffix s3DataConnector and are stored in the s3DataConnectors folder.

Version

#### DataConnectorS3 components are available in API version 50.0 and later.

Special Access Rules

You need the Salesforce CustomizeApplication permission to access this object.

Fields

**Field Name** **Field Type** **Description**

`fileNameWildcard` string Optional. File or Wildcard (*) to be used when finding files.

`importFromDirectory` string Required. Path from the directory to where files are located.

`masterLabel` string Required. The UI name for the S3 data connector.


#### Metadata Types DataKitObjectTemplate

**Field Name** **Field Type** **Description**

`s3BucketName` string Optional. The Amazon S3 Name of the Bucket.

Declarative Metadata Sample Definition

The following is an example of a DataConnectorS3 component.

```
      <?xml version="1.0" encoding="UTF-8"?>

      <DataConnectorS3 xmlns="http://soap.sforce.com/2006/04/metadata">

      <fileNameWildcard>*.csv</fileNameWildcard>

      <importFromDirectory>c360-subset-lheader/</importFromDirectory>

      <masterLabel>Person</masterLabel>

      <s3BucketName>bucketeer-aa32faea-8431-4635-8a1d-b323a2d66c7c</s3BucketName>

      </DataConnectorS3>

#### DataKitObjectTemplate

```

Represents the object in Data Kit Object Template. These object templates are added inside the data kit.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this metadata type’s name.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

#### DataKitObjectTemplate components have the suffix .DataKitObjectTemplate and are stored in the DataKitObjectTemplate folder.

Version

#### DataKitObjectTemplate components are available in API version 63.0 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Description**

```
developerName

```

**Field Type**
string


Metadata Types DataKitObjectTemplate

**Field Name** **Description**

**Description**
Required. Name of the data kit object template. This can contain only underscores and
alphanumeric characters and must be unique in your org. It must begin with a letter,
not include spaces, not end with an underscore, and not contain two consecutive
underscores.

```
entityPayload

masterLabel

parentDataPackageKitDefinitionName

sourceObject

sourceObjectType

```

**Field Type**
string

**Description**
A string-based JSON payload containing the metadata of a data kit component. The
payload is templatized to enable variable substitution during the deployment process.

**Field Type**
string

**Description**
Required. The label of the data kit object template.

**Field Type**
string

**Description**
Required. The linked data kit package definition in the data kit.

**Field Type**
string

**Description**
The developer name of the source object for the data kit object template.

**Field Type**
string

**Description**
Required. The object type of the metadata component in the data kit. Valid values are:

**•** `MKT_DATA_TRANSFORM`

**•** `MKT_DATA_CONNECTION`

**•** `IDENTITY_RESOLUTION`

**•** `DATA_GRAPH`

**•** `EXT_DATA_SHARE`

**•** `SEMANTIC_SEARCH`

**•** `DATA_ACTION`

**•** `DATA_ACTION_TARGET`

**•** `MARKET_SEGMENT`

**•** `DATA_SPACE_MEMBER`


Metadata Types DataKitObjectTemplate

**Field Name** **Description**

**•** `INTERNAL_DATA_CONNECTOR`

**•** `MARKET_SEGMENT_ACTIVATION`

**•** `STREAMING_APP_AND_INGESTION_CONNECTOR`

**•** `ML_CONFIGURED_MODEL`

**•** `ACTIVATION_TARGET`

**•** `SEMANTIC_MODEL`

**•** `PERSONALIZATION_RECOMMENDER`

**•** `PERSONALIZATION_POINT`

**•** `PERSONALIZATION_SCHEMA`

**•** `PERSONALIZATION_OBJECTIVE`

**•** `ENGAGEMENT_SIGNAL`

**•** `PERSONALIZATION_BATCH_DECISION`

**•** `MC_CONNECTOR`

**•** `ML_PREDICTION_JOB`

**•** `ML_RETRIEVER`

**•** `TUA_TEMPLATED_OBJECT`

**•** `IR_RELATED_LIST_ENRICHMENT`

**•** `TAG_METADATA`

**•** `DATA_CLEAN_ROOM_PROVIDER`

**•** `IDP_CONFIGURATION`

**•** `COPY_FIELD_ENRICHMENT`

**•** `DATA_CUSTOM_CODE`

**•** `ANALYTICS_VISUALIZATION`

**•** `ANALYTICS_DASHBOARD`

**•** `ANALYTICS_WORKSPACE`

**•** `SECONDARY_INDEX`

**•** `POLICY_RULE_DEFINITION_METADATA`

**•** `POLICY_RULE_DEFINITION_SET_METADATA`

```
templateVersion

```

**Field Type**
string

**Description**
The version number of the template.


#### Metadata Types DataKitObjectDependency

Declarative Metadata Sample Definition

The following is an example of a DataKitObjectTemplate component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <DataKitObjectTemplate xmlns="http://soap.sforce.com/2006/04/metadata">

     <developerName xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>

     <entityPayload>

       {

         "dataSpaceName": "default",

         "type": "DLO",

         "developerName": "DLO_StaticCurrencyRates_Home"

       }

     </entityPayload>

     <masterLabel>StaticCurrencyRates_Home__dll</masterLabel>

     <parentDataPackageKitDefinitionName xsi:nil="true"

   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>

     <sourceObject>0viSB00000JzG05YAF</sourceObject>

     <sourceObjectType>DataSpaceMember</sourceObjectType>

     <templateVersion>1</templateVersion>

   </DataKitObjectTemplate>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>StaticCurrencyRates_Home</members>

        <members>StaticCurrencyRates_Home1</members>

        <name>DataKitObjectTemplate</name>

      </types>

      <version>64.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### DataKitObjectDependency

Represents the dependency between two data kit objects. The object templates are added inside the data kit.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this metadata type’s name.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types DataKitObjectDependency

File Suffix and Directory Location

`DataKitObjectDependency` components have the suffix `.DataKitObjectDependency` and are stored in the
`DataKitObjectDependency` folder.

Version

DataKitObjectDependency components are available in API version 65.0 and later.

Special Access Rules

You need the Salesforce CustomizeApplication permission to access this object.

Fields

**Field Name** **Description**

```
dataPackageKitDef

developerName

masterLabel

sourceObject

sourceObjectType

```

**Field Type**
string

**Description**
Required. The ID of the linked `DataPackageKitDefinition.`

**Field Type**
string

**Description**
Required. The name of the `DataKitObjectDependency` . This name can contain
only underscores and alphanumeric characters and must be unique in your org. It
must begin with a letter, not include spaces, not end with an underscore, and not
contain two consecutive underscores.

**Field Type**
string

**Description**
Required. Label that identifies the data kit object dependency.

**Field Type**
string

**Description**
The source data kit object template that the target object depends on.

**Field Type**
string

**Description**
Required. The type of the source object referenced in the data kit. Valid values are:

**•** `DataKitObjectTemplate`


#### Metadata Types DataObjectBuildOrgTemplate

**Field Name** **Description**

**•** `DataSourceObject`

**•** `DataStreamTemplate`

**•** `DataSourceBundleDefinition`

**•** `MKtDataModelObject`

```
targetObject

```

**Field Type**
string

**Description**
Required. The target data kit object template that depends on the source object.

#### DataObjectBuildOrgTemplate

Represents the derived object template used to define the structure and configuration of data objects in a build organization. The object
templates are added inside the data kit to deploy metadata.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this metadata type’s name.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

#### DataObjectBuildOrgTemplate components have the suffix .DataObjectBuildOrgTemplate and are stored in the DataObjectBuildOrgTemplate folder.

Version

#### DataObjectBuildOrgTemplate components are available in API version 63.0 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Description**

```
developerName

```

**Field Type**
string


Metadata Types DataObjectBuildOrgTemplate

**Field Name** **Description**

**Description**
Required. Name of the data object build org template. This name can contain only
underscores and alphanumeric characters and must be unique in your org.

```
masterLabel

objectDevName

objectPayload

objectType

templateObject

templateVersion

```

**Field Type**
string

**Description**
Required. The label of the data object build org template.

**Field Type**
string

**Description**
Required. The developer name of the object created from the `objectPayload`
entity in the build org.

**Field Type**
string

**Description**
Required. The serialized metadata for the entity. The build organization deserializes
this payload to create the underlying metadata components.

**Field Type**
string

**Description**
Required. The type of metadata entity associated with the template. Valid values are:

**•** `DataGraph`

**•** `MktCalculatedInsightObject`

**•** `MktDataModelObject`

**•** `MktDataLakeObject`

**Field Type**
string

**Description**
Required. The name of the template associated with the data object build org template.

**Field Type**
string

**Description**
The version number of the data object build org template.


#### Metadata Types DataPackageKitDefinition

Declarative Metadata Sample Definition

The following is an example of a DataObjectBuildOrgTemplate component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <DataKitObjectTemplate xmlns="http://soap.sforce.com/2006/04/metadata">

     <developerName xsi:nil="true" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>

     <entityPayload>

       {

         "dataSpaceName": "default",

         "type": "DLO",

         "developerName": "DLO_StaticCurrencyRates_Home"

       }

     </entityPayload>

     <masterLabel>StaticCurrencyRates_Home__dll</masterLabel>

     <parentDataPackageKitDefinitionName xsi:nil="true"

   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"/>

     <sourceObject>0viSB00000JzG05YAF</sourceObject>

     <sourceObjectType>DataSpaceMember</sourceObjectType>

     <templateVersion>1</templateVersion>

   </DataKitObjectTemplate>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>StaticCurrencyRates_Home</members>

        <members>StaticCurrencyRates_Home1</members>

        <name>DataKitObjectTemplate</name>

      </types>

      <version>64.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### DataPackageKitDefinition

Represents the top-level data kit container definition. Content objects can be added after the data kit is defined.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this metadata type’s name.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types DataPackageKitDefinition

File Suffix and Directory Location

`DataPackageKitDefinition` components have the suffix `.dataPackageKitDefinition` and are stored in the
`dataPackageKitDefinitions` folder.

Version

DataPackageKitDefinition components are available in API version 53.0 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Description**

```
dataKitType

dataKitSource

description

developerName

isDeployed

```

**Field Type**
string

**Description**
The type of data kit created. Available in API version 63.0 and later. Valid values are:

**•** Default

**•** Sandbox

**Field Type**
string

**Description**
The data source in the updated data kit. Available in API version 63.0 and later.

**Field Type**
string

**Description**
The description of the data kit.

**Field Type**
string

**Description**
Required. The name of the application. This name contain only underscores and
alphanumeric characters and must be unique in your org. It must begin with a letter,
not include spaces, not end with an underscore, and not contain two consecutive
underscores.

**Field Type**
boolean


Metadata Types DataPackageKitDefinition

**Field Name** **Description**

**Description**
Indicates whether the data kit content is deployed.

```
isEnabled

masterLabel

useDeterministicNaming

versionNumber

dataSpaceDefinitionDevName

deploymentOrder

```

**Field Type**
boolean

**Description**
Indicates whether the data kit is enabled.

**Field Type**
string

**Description**
Required. Label that identifies the AI application throughout the Salesforce user
interface.

**Field Type**
boolean

**Description**
Required. Indicates whether the data kit should use the deterministic naming feature.
Available in API version 65.0 and later. Valid values are:

**•** True

**•** False

**Field Type**
double

**Description**
Auto incremented version number.

**Field Type**
string

**Description**
Data space name used to create the data kit. Available in API version 61.0 and later.

**Field Type**
string

**Description**
Deployment order of components that are added to the data kit. Available in API
version 61.0 and later.


#### Metadata Types DataPackageKitObject

Declarative Metadata Sample Definition

The following is an example of a DataPackageKitDefinition component.

```
   <DataPackageKitDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

      <developerName>SalesforceCRM</developerName>

      <isDeployed>false</isDeployed>

      <isEnabled>false</isEnabled>

      <masterLabel>SalesforceCRM</masterLabel>

      <versionNumber>1.0</versionNumber>

   </DataPackageKitDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <fullName>SalesforceDataKit</fullName>

      <types>

        <members>SalesforceCRM</members>

        <name>DataPackageKitDefinition</name>

      </types>

      <types>

        <members>Admin</members>

        <name>Profile</name>

      </types>

      <version>53.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### DataPackageKitObject

Represents the object in Data Kit Content Object. These objects are added inside the data kit.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this metadata type’s name.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

#### DataPackageKitObject components have the suffix .DataPackageKitObject and are stored in the DataPackageKitObjects folder.

Version

DataPackageKitDefinition components are available in API version 53.0 and later.


Metadata Types DataPackageKitObject

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Description**

```
masterLabel

parentDataPackageKitDefinitionName

referenceObjectName

referenceObjectType

```

**Field Type**
string

**Description**
Required. Label that identifies the AI application throughout the Salesforce user
interface.

**Field Type**
string

**Description**
Required. Name of the data kit definition

**Field Type**
string

**Description**
Required. The name of the data kit content.

**Field Type**
string

**Description**
Required. The type of the content object in the data kit.

Declarative Metadata Sample Definition

The following is an example of a DataPackageKitDefinition component.

```
<?xml version="1.0" encoding="UTF-8"?>

<DataPackageKitObject xmlns="http://soap.sforce.com/2006/04/metadata">

   <masterLabel>CRM</masterLabel>

   <parentDataPackageKitDefinitionName>CRM</parentDataPackageKitDefinitionName>

   <referenceObjectName>CRM</referenceObjectName>

   <referenceObjectType>DLO</referenceObjectType>

</DataPackageKitObject>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <fullName>SalesforceDataKit</fullName>

   <types>

     <members>CRM</members>

```


#### Metadata Types DataSource

```
        <name>DataPackageKitObject</name>

      </types>

      <types>

        <members>Admin</members>

        <name>Profile</name>

      </types>

      <version>53.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### DataSource

Used to represent the system where the data was sourced. This object is always needed when creating a Data Stream Definition.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

#### DataSource components have the suffix dataSource and are stored in the mktDataSources folder.

Version

#### DataSource components are available in API version 50.0 and later.

Special Access Rules

You need the Salesforce CustomizeApplication permission to access this object.

Fields

**Field Name** **Field Type** **Description**

`masterLabel` string Required. The UI name for the Data Source.

`prefix` string Required. Prefix for the Data Source to make Data Source Object records
unique.

#### DataSourceBundleDefinition

Represents the bundle of streams that a user adds to a data kit.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.


Metadata Types DataSourceBundleDefinition

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

`DataSourceBundleDefinition` components have the suffix `.dataSourceBundleDefinition` and are stored in the
`dataSourceBundleDefinitions` folder.

Version

DataSourceBundleDefinition components are available in API version 52.0 and later.

Special Access Rules

You need Data 360 permission to access this object.

Fields

**Field Name** **Description**

```
dataPlatform

description

icon

isMultiDeploymentSupported

masterLabel

```

**Field Type**
string

**Description**
Required. Indicates the connector type that the streams in the bundle belong to.

**Field Type**
string

**Description**
A description of the associated data source bundle. This field is available in API version
53.0 and later.

**Field Type**
string

**Description**
The icon used in the deployment flow. This field is available in API version 53.0 and
later.

**Field Type**
boolean

**Description**
Indicates if the bundle can be deployed multiple times or not. Default value is `false` .

**Field Type**
string


#### Metadata Types DataSourceField

**Field Name** **Description**

**Description**
Required. Indicates the name of the bundle.

```
bundleVersion

```

**Field Type**
int

**Description**
Indicates the version of the bundle. This field is available in API version 63.0 and later.

Declarative Metadata Sample Definition

The following is an example of a DataSourceBundleDefinition component.

```
<?xml version="1.0" encoding="UTF-8"?>

<DataSourceBundleDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

   <dataPlatform>Salesforce_Sales_and_Service_Cloud</dataPlatform>

   <isMultiDeploymentSupported>true</isMultiDeploymentSupported>

   <bundleVersion>1</bundleVersion>

   <masterLabel>b2</masterLabel>

</DataSourceBundleDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
<types>

    <members>b2</members>

    <name>DataSourceBundleDefinition</name>

</types>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/file_based_zip_file.htm)

#### DataSourceField

Represents the details of a data source field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

#### DataSourceField components have the suffix .dataSourceField and are stored in the dataSourceFields folder.


Metadata Types DataSourceField

Version

DataSourceField components are available in API version 52.0 and later.

Special Access Rules

You need the Salesforce Customize Application permission to access this metadata type.

Fields

**Field Name** **Field Type** **Description**

`datatype` string Required. Indicates the data type of the field: text, number, or date.

`dateFormat` string The date format of date, time, date/time fields.

```
definitionCreationType

```

DefinitionCreationType Describes whether this object was added by the user or as part of a standard
(enumeration of type taxonomy. Available in API version 62.0 and later. Valid values are:
string)

**•** `Activation_Audience` (Reserved for internal use only)

**•** `ADG`

**•** Activation_Audience. Available in API version 63.0 and later.

**•** `Bridge`

**•** `Calculated_Insight`

**•** `CG_Audience`

**•** `Chunk`

**•** `Curated`

**•** `Custom`

**•** `Derived`

**•** `Directory_Table`

**•** `External`

**•** `Ml_Prediction`

**•** `Segment_Membership`

**•** `Semantic`

**•** `Standard`

**•** `System`

**•** `Transform`

**•** `Vector_Embedding`

`externalDataType` string The type of data in the external system. Available in API version 63.0 and later.

`externalName` string Required. Name of the object in the external system. This is different from the
developer name.

`fieldFormula` string Used for formulas.

`isDataRequired` boolean If `true`, data is required. Default value is `false` .


Metadata Types DataSourceField

**Field Name** **Field Type** **Description**

`isEventDate` boolean If `true`, an event date is required. Default value is `false` . Available in API
version 63.0 and later.

`isFormula` boolean If `true`, a formula is required. Default value is `false` .

`isRecordModified` boolean If `true`, the system tracks the modification date of the record. Default value
is `false` . Available in API version 63.0 and later.

`keyQualifierName` string

Contains the developer name of the `keyQualifier` field. Available in API
version 62.0 and later.

`length` int Length of a string column.

`masterLabel` string Required. Field label.

`precision` int The total number of digits in a number including decimal points. Used for
currency and for numeric accuracy.

`primaryIndexOrder` int

If supplied, indicates that this field is part of the primary key. The number value
indicates the order of attributes if it’s a compound primary key. A missing value
means that this field isn’t part of the primary key.

`scale` int The number of digits to the right of the decimal point. Used for currency and
for numeric accuracy.

`sequence` int Required. The sequence of this source schema.

`srcKeyQualifier` string

Contains a reference to the source key qualifier record. The source key is the
MktDataLakeSrcKeyQualifer metadata type. Available in API version 55.0 and
later.

Indicates if the field is a key qualifier field. Available in API version 55.0 and later.

Values are:

**•** `KEY_QUALIFIER` —The field is used as a key qualifier field.

**•** `NONE` —The field isn’t used as a key qualifier field.

```
usageTag

```

usageTag
(enumeration of type
string)

`versionNumber` double Required. The version of the data source object.

Declarative Metadata Sample Definition

This is an example of a DataSourceObject component and its fields. You can retrieve the DataSourceField component only through its
parent object, DataSourceObject.

```
<DataSourceObject xmlns="http://soap.sforce.com/2006/04/metadata"

xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

   <dataSource>test1108</dataSource>

   <dataSourceFields>

     <fullName>DOB</fullName>

     <datatype>D</datatype>

     <externalName>DOB</externalName>

     <isDataRequired>false</isDataRequired>

```


#### Metadata Types DataSourceObject

```
        <masterLabel>DOB</masterLabel>

        <sequence xsi:nil="true"/>

        <versionNumber xsi:nil="true"/>

      </dataSourceFields>

      <externalRecordIdentifier>individuals_20200125_000000_csv</externalRecordIdentifier>

      <masterLabel>test1108</masterLabel>

      <objectType>Object</objectType>

   </DataSourceObject>

```

The following is an example `package.xml` that references the previous definition.

```
   <types>

        <members>test1108</members>

        <name>DataSource</name>

      </types>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### DataSourceObject

Represents the object from where the data was sourced.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

#### DataSourceObject components have the suffix dataSourceObject and are stored in the mktDataSourceObjects folder.

Version

#### DataSourceObject components are available in API version 50.0 and later.

Special Access Rules

You need the Salesforce Customize Application permission to access this metadata type.


Metadata Types DataSourceObject

Fields

**Field Name** **Field Type** **Description**

```
accelerationEnabled

```

AccelerationEnabled Acceleration of data stream processing. Available in API version 63.0
(enumeration and later. Possible values are:
of type

**•** `Yes`

string)

**•** `Yes`

**•** `No`

`additionalDLOInfoJson` string Additional information about the Directory Table data lake object
(DLO), such as the directory path and file pattern.

`creationType` string Indicates whether this object was added by the user or as part of a
standard taxonomy.

`dataConnection` string The source data connector for the Directory Table DLO.

`dataSource` string Required. The system where the data was sourced.

`dataSourceFields` DataSourceField[] An array of data source fields.
on page 215

`dmoDeveloperName` string The developer name of the Directory Table data model object (DMO).

`dmoLabel` string The UI name of the Directory Table DMO.

`externalDatabaseName` string The name of the external database for the data source object. Available
in API version 63.0 and later.

`externalObjectName` string The external data source object. Available in API version 63.0 and later.

`externalRecordIdentifier` string The identifier for the data source.

`externalSchemaName` string The name of the schema within the external database. Available in
API version 63.0 and later.

`masterLabel` string Required. The UI name for the data source object.

`objectCategory` string The category of the data source object.

`objectType` DataObjectType The object type. Possible values are:
(enumeration

**•** API
of type

**•** Object
string)

**•** Table

`sourceObject` string The developer name of the source object for the data source object.

```
storageType

```

StorageType The type of storage used for data source object. Available in API version
(enumeration 63.0 and later. Possible values are:
of type

**•** External

string)

**•** External

**•** Local

`templateVersion` int The version number of the data source object.


#### Metadata Types DataSourceTenant DataSourceTenant

For internal use only.

#### DataSrcDataModelFieldMap

Represents the mappings between source data lake object (DLO) fields and target data model object (DMO) fields.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

#### DataSrcDataModelFieldMap components have the suffix .dataSrcDataModelFieldMap and are stored in the

`dataSrcDataModelFieldMaps` folder.

Version

#### DataSrcDataModelFieldMap components are available in API version 53.0 and later.

Special Access Rules

You need Data 360 permissions to access this object.

Fields

**Field Name** **Description**

```
filterApplied

filterOperationType

filterValue

```

**Field Type**
boolean

**Description**
Indicates whether a filter is applied to a DLO-to-DMO field mapping ( `true` ) or not
( `false` ). Available in API version 60.0 and later.

**Field Type**
string

**Description**
Required when filterApplied is true. The comparison operator used when filtering the
DLO-to-DMO field mapping. Available in API version 60.0 and later.

**Field Type**
string


Metadata Types DataSrcDataModelFieldMap

**Field Name** **Description**

**Description**
Required when filterApplied is true. The value used for filtering the DLO-to-DMO field
mapping. Available in API version 60.0 and later.

```
masterLabel

sourceField

targetField

templateVersion

versionNumber

```

**Field Type**
string

**Description**
Required. A user-friendly name for DataSrcDataModelFieldMap, which is defined when
the DataSrcDataModelFieldMap is created.

**Field Type**
string

**Description**
Required. The developer name of the DLO field.

**Field Type**
string

**Description**
Required. The developer name of the DMO field.

**Field Type**
int

**Description**
The version number of the field mapping template. Available in API version 61.0 and
later.

**Field Type**
double

**Description**
Required. The version number of the DataSrcDataModelFieldMap.

Declarative Metadata Sample Definition

The following is an example of a DataSrcDataModelFieldMap component.

```
<?xml version="1.0" encoding="UTF-8"?>

<DataSrcDataModelFieldMap xmlns="http://soap.sforce.com/2006/04/metadata">

   <filterApplied>true</filterApplied>

   <filterOperationType>equals</filterOperationType>

   <filterValue>Active</filtervalue>

   <masterLabel>DataSrcDataModel26</masterLabel>

   <sourceField>Account1.LastModifiedDate__c</sourceField>

   <targetField>ssot__Account__dlm.ssot__LastModifiedDate__c</targetField>

   <tepmlateVersion>2</templateVersion>

```


#### Metadata Types DataStreamDefinition

```
      <versionNumber>1.0</versionNumber>

   </DataSrcDataModelFieldMap>

```

The following is an example `package.xml` that references the previous definition.

```
   <types>

        <members>DataSrcDataModel26</members>

        <name>DataSrcDataModelFieldMap</name>

   </types>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/file_based_zip_file.htm)

#### DataStreamDefinition

Contains data ingestion information such as connection, API, and file retrieval settings.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

#### DataStreamDefinition components have the suffix dataStreamDefinition and are stored in the dataStreamDefinitions

folder.

Version

#### DataStreamDefinition components are available in API version 50.0 and later.

Special Access Rules

You need the Salesforce CustomizeApplication permission to access this object.

Fields

**Field Name** **Field Type** **Description**

`areHeadersIncludedInFile` boolean If true, headers are included in the file if this is a single file stream.

`bulkIngest` boolean If true, files are aggregated before data is ingested if the file names
contain a wildcard. For example, `profiles*.csv` .

`definitionCreationType` string Required. Enum tracks the source of an object or field creation. Valid
values are:

**•** `Custom`

**•** `Standard`

Valid values available in API version 62.0 and later are:


Metadata Types DataStreamDefinition

**Field Name** **Field Type** **Description**

**•** `ADG`

**•** `Calculated_Insight`

**•** `CG_Audience`

**•** `Chunk`

**•** `Directory_Table`

**•** `External`

**•** `Semantic`

**•** `Transform`

**•** `Vector_Embedding`

`dataConnector` string Required. Describe whether this data stream definition was created by
a customer or by an internal system.

```
dataConnectorType

```

DataConnectorType The ingestion data source. Valid values are:
(enumeration of

**•** `ACCOUNTENGAGEMENT`

type string)

**•** `ACCOUNTENGAGEMENT`

**•** `AwsS3`

**•** `AzureBlob`

**•** `BIG_QUERY`

**•** `CuratedEntity`

**•** `DataCloud`

**•** `ExternalPlatform`

**•** `GoogleCloudStorage`

**•** `IngestApi`

**•** `REDSHIFT`

**•** `SalesforceCommerceCloud`

**•** `SalesforceDotCom`

**•** `SalesforceInteractionStudio`

**•** `SalesforceMarketingCloud`

**•** `SFTP`

**•** `Snowflake`

**•** `StreamingApp`

**•** `UPLOAD`

`dataExtensionIdentifier` string For a Marketing Cloud data extension, the unique identifier.

`dataExtractField` string Name of the transport field that’s used when the extract method is CDC.

```
dataExtractMethods

```

DataImportDataExtractMethods Describes how to identify the data to be extracted. Valid values include:
(enumeration of

**•** `DATETIME_CDC`

type string)

**•** `FULL_REFRESH`

**•** `NUMERIC_CDC`


#### Metadata Types DataStreamTemplate

**Field Name** **Field Type** **Description**

**•** `BINARY_CDC` (reserved for future use)

`dataPlatDataSetBundle` string Identifies which data set bundle this definition was created from. Useful
in cases where the same item can be configured across data connections.

`dataPlatformDataSet` string The description is provided by the developer.

`dataPlatformDataSetItemName` string Name of the Data Platform Set Item.

`dataSource` string Required. A reference to the data source from which the data originated.
This is usually the API name or a unique system identifier, such as the

enterprise ID (EID) of the customer in the format `MC_<EID>` . Example:
`MCEnterprise` or `MC_12345` .

`description` string Required. A description of the data stream definition.

`fileNameWildcard` string File or wildcard (*) used when finding files.

`internalOrganization` string The name of the internal organization.

`isLimitedToNewFiles` boolean If true, file retrieval is limited to new files.

`isMissingFileFailure` boolean If true, treat the case of missing files as a failure.

`masterLabel` string Required. UI label for this data stream definition.

`mktDataLakeObject` string Required. Reference to the landing entity (target) where data will be
stored.

`mktDataTranObject` string Reference to the object that’s used to transport information from the
source to a landing entity (target).

#### DataStreamTemplate

Represents the data stream that a user adds to a data kit.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

#### DataStreamTemplate components have the suffix .dataStreamTemplate and are stored in the dataStreamTemplates

folder.

Version

#### DataStreamTemplate components are available in API version 53.0 and later.


Metadata Types DataStreamTemplate

Special Access Rules

You need the Salesforce Customize Application permission to access this metadata type.

Fields

**Field Name** **Description**

```
dataConnectionSourceParameters

dataSourceBundleDefinition

dataSourceObject

filterCriteria

masterLabel

objectCategory

refreshDayOfMonth

```

**Field Type**
DataConnectionParamTmpl[]

**Description**
Input representation for the data connection source parameters.

**Field Type**
string

**Description**
Required. Reference to the bundle to which this template belongs.

**Field Type**
string

**Description**
Required. Reference to the Data Source Objects (DSOs). A DSO represents the object
from where the data was sourced.

**Field Type**
string

**Description**
Filter applied to the data stream before the information is sent to Data Cloud.

**Field Type**
string

**Description**
Required. Name assigned to the data stream template.

**Field Type**
string

**Description**
Required. Category of the Data Model Object (DMO).

**Field Type**
int

**Description**
The duration of the day of the month after which the data stream must be refreshed.


Metadata Types DataStreamTemplate

**Field Name** **Description**

```
refreshDayOfWeek

refreshFrequency

refreshHours

refreshMode

```

**Field Type**
int

**Description**
The duration of the day of the week after which the data stream must be refreshed.

**Field Type**
DataImportRefreshFrequency (enumeration of type string)

**Description**
The frequency with which the datastream must be refreshed. Possible values are:

**•** `Batch`

**•** `NONE`

**•** `MINUTES_15`

**•** `MINUTES_30`

**•** `MINUTES_5`

**•** `HOURLY`

**•** `DAILY`

**•** `WEEKLY`

**•** `MONTHLY`

**•** `NOT_APPLICABLE`

**•** `STREAMING`

Possible values available in API version 64.0 and later are:

**•** EVERY_12_HOURS

**•** EVERY_4_HOURS

**Field Type**
string

**Description**
The duration after which the datastream must be refreshed.

**Field Type**
DataImportRefreshMode (enumeration of type string)

**Description**
The mode of refresh. Possible values are:

**•** `FULL_REFRESH`

**•** `UPSERT`

**•** `INCREMENTAL`

**•** `REPLACE`

**•** `NEAR_REAL_TIME_INCREMENTAL`

**•** `NOT_APPLICABLE`


Metadata Types DataStreamTemplate

**Field Name** **Description**

**•** `PARTIAL_UPDATE`

**•** `STREAMING`

```
refreshStartDate

sourceObjectName

streamType

streamingAppDataConnectorType

templateVersion

```

**Field Type**
date

**Description**
The date to retrieve data based on the refresh frequency data. Available in API version
62.0 and later.

**Field Type**
string

**Description**
The name of the source object from which data is streamed. Available in API version
62.0 and later.

**Field Type**
StreamType (enumeration of type string)

**Description**
The type of data stream. Available in API version 62.0 and later. Possible values are:

**•** `DIRECT_ACCESS`

**•** `DIRECT_ACCESS_ACCELERATED`

**•** `INGEST`

**Field Type**
streamingAppDataConnectorType (enumeration of type string)

**Description**
The connector app for data streaming. Available in API version 63.0 and later. Possible
values are:

**•** `MobileApp`

**•** `WebApp`

**Field Type**
int

**Description**
The version number of the template. Available in API version 62.0 and later.

Declarative Metadata Sample Definition

The following is an example of a DataStreamTemplate component.

```
<DataStreamTemplate xmlns="http://soap.sforce.com/2006/04/metadata">

   <dataSourceBundleDefinition>b2</dataSourceBundleDefinition>

```


#### Metadata Types ExternalDataConnector

```
      <dataSourceObject>sd3ds</dataSourceObject>

      <masterLabel>b2</masterLabel>

      <objectCategory>Profile</objectCategory>

   </DataStreamTemplate>

```

The following is an example `package.xml` that references the previous definition.

```
    <types>

        <members>ssd3s</members>

        <name>DataStreamTemplate</name>

      </types>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
[using the manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/file_based_zip_file.htm)

#### ExternalDataConnector

Used to represent the object where the data was sourced.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

#### ExternalDataConnector components have the suffix externalDataConnector and are stored in the externalDataConnectors folder.

Version

#### ExternalDataConnector components are available in API version 50.0 and later.

Special Access Rules

You need the Salesforce CustomizeApplication permission to access this object.

Fields

**Field Name** **Field Type** **Description**

```
dataConnectionStatus

```

DataConnectionStatus Indicates whether you’re connected to a data source. Valid values are:
(enumeration of

**•** `Connected`

type string)

**•** `Connected`

**•** `Disconnected`

**•** `Failed`

`dataConnectorConfiguration` string Reference to the Data Connector Configuration that is used to retrieve
or receive data such as DataConnectorS3.


#### Metadata Types ExternalDataSource

**Field Name** **Field Type** **Description**

```
dataConnectorType

```

DataConnectorType Type of connection such as AmazonS3. Valid values are:
(enumeration of

**•** `ACCOUNTENGAGEMENT`

type string)

**•** `ACCOUNTENGAGEMENT`

**•** `AmazonS3`

**•** `CuratedEntity`

**•** `DataCloud`

**•** `ExternalPlatform`

**•** `GoogleCloudStorage`

**•** `IngestApi`

**•** `SalesforceCommerceCloud`

**•** `SalesforceDotCom`

**•** `SalesforceInteractionStudio`

**•** `SalesforceMarketingCloud`

**•** `SFTP`

**•** `StreamingApp`

**•** `UPLOAD`

`dataPlatform` string Reference to the Data Platform that provides or uses this data, such as
Amazon_S3.

`externalDataTranObjects` [ExternalDataTranObject](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_externaldatatranobject.htm) Stores the schema objects related to the data connector. Available in
API version 56.0 and later.

`masterLabel` string Required. The UI name for the ExternalDataConnector.

Declarative Metadata Sample Definition

The following is an example of a ExternalDataConnector component.

```
     <?xml version="1.0" encoding="UTF-8"?>

     <ExternalDataConnector xmlns="http://soap.sforce.com/2006/04/metadata">

     <dataConnectionStatus>Connected</dataConnectionStatus>

     <dataConnectorConfiguration>Person</dataConnectorConfiguration>

     <dataConnectorType>AmazonS3</dataConnectorType>

     <dataPlatform>Amazon_S3</dataPlatform>

     <masterLabel>AmazonS3</masterLabel>

     </ExternalDataConnector>

#### ExternalDataSource

```

Represents the metadata associated with an external data source. Create external data sources to manage connection details for
integration with data and content that are stored outside your Salesforce org.


Metadata Types ExternalDataSource

Note: All credentials stored within this entity are encrypted under a framework that is consistent with other encryption frameworks
on the platform. Salesforce encrypts your credentials by auto-creating org-specific keys. Credentials encrypted using the previous
encryption scheme are migrated to the new framework.

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

ExternalDataSource components are stored in the `dataSources` directory of the corresponding package directory. ExternalDataSource
components have the suffix `.dataSource`, and the prefix is the name of the external data source.

Version

ExternalDataSource components are available in API version 28.0 and later.

Special Access Rules

As of Spring ’20 and later, only authenticated internal and external users can access this type.

Fields

**Field Name** **Field Type** **Description**

`authProvider` string The authentication provider represented by the AuthProvider
component.

`certificate` string If you specify a certificate, your Salesforce org supplies it when
establishing each two-way SSL connection with the external system.

The certificate is used for digital signatures, which verify that
requests are coming from your Salesforce org.

Tip: For best performance, verify that your remote HTTPS
encrypted sites have OCSP (Online Certificate Status Protocol)
stapling turned on.

`customConfiguration` string A string of configuration parameters that are specific to the external
data source’s `type` .

**•** customConfiguration for Salesforce Connect—Cross-Org
Adapter

**•** customConfiguration for Salesforce Connect—OData 2.0 or 4.0
Adapter

**•** customConfiguration for Salesforce Connect—Custom Adapter

`customHttpHeaders` CustomHttpHeaders[] Represents custom HTTP headers used with OData 2.0 or OData 4.0
connectors. Available in API version 43.0 or later.


Metadata Types ExternalDataSource

**Field Name** **Field Type** **Description**

`endpoint` string

The URL of the external system, or if that URL is defined in a named
credential, the named credential URL. Corresponds to the `URL` in
the user interface.

A named credential URL contains the scheme `callout:`, the
name of the named credential, and an optional path. For example:
`callout:` _`My_Named_Credential`_ `/` _`some_path`_ .

You can append a query string to a named credential URL. Use a
question mark (?) as the separator between the named credential
URL and the query string. For example:
`callout:` _`My_Named_Credential`_ `/` _`some_path`_ `?format=json` .

`externalDataSrcDescriptors` ExternalDataSrcDescriptors[] Represents schema descriptors for an external data source used
with the Salesforce Connect adapter for Amazon DynamoDB

(available in API version 55.0 or later) or Amazon Athena (available
in API version 56.0 or later).

`isWritable` boolean

`label` string

`namedCredential` string

Allows the Lightning Platform and users in this org to create, update,
and delete records for external objects associated with the external

data source. The external object data is stored outside the org. By
default, external objects are read-only. Corresponds to `Writable`
`External Objects` in the user interface.

Available in API version 35.0 and later. However, with the cross-org
adapter for Salesforce Connect, you can set this field to `true` only
in API version 39.0 and later.

A name for the external data source. The label is displayed in the
Salesforce user interface, such as in list views.

Examples include Acme Team Marketing Site or Acme SharePoint.

Represents the definition of the referenced named credential for
an external data source of the type Amazon DynamoDB or Amazon
Athena.

`oauthRefreshToken` string The OAuth refresh token. Used to obtain a new access token for an
end user when a token expires.

`oauthScope` string Specifies the scope of permissions to request for the access token.
Corresponds to the `Scope` in the user interface.

`oauthToken` string The access token issued by the external system.

`password` string The password your org uses to access the external system. Make
sure that the credentials you use have adequate privileges to access

the external system, perform searches, return data, and return
information about the external system’s metadata.


Metadata Types ExternalDataSource

**Field Name** **Field Type** **Description**

```
principalType

protocol

```

```
External

PrincipalType
```

(enumeration of type string)

`Authentication` The authentication protocol that’s required to access the external
`Protocol` (enumeration system. The valid values are:
of type string)

**•** `NoAuthentication`

Determines whether you're using one set or multiple sets of
credentials to access the external system. Corresponds to
`Identity Type` in the user interface. The valid values are:

**•** `Anonymous`

**•** `PerUser`

**•** `NamedUser`

**•** `Oauth`

**•** `Password`

For cloud-based Files Connect external systems, select **Oauth 2.0** .
For on-premises systems, select **Password Authentication** .

For Simple URL data sources, select **No Authentication** .

`repository` string Used for SharePoint Online. If metadata isn't accessible, use this
field to create tables and default table fields.

`type` `ExternalDataSourceType` Required. For Salesforce Connect, specifies the adapter that connects
(enumeration of type string) to the external system. The valid values are:

**•** `AmazonAthena` —Amazon Athena

**•** `AmazonDynamoDB` —Amazon DynamoDB

**•** `OData` —OData 2.0 adapter

**•** `OData4` —OData 4.0 adapter

**•** `SfdcOrg` —cross-org adapter

**•** _`ApexClassId`_                         - `DataSource.Provider` class that
defines the custom adapter created via the Apex Connector
Framework

For Files Connect, specifies the data source type. The valid values
are:

**•** `ContentHubSharepoint` —SharePoint 2010 or 2013

**•** `ContentHubSharepointOffice365` —SharePoint
Online

**•** `ContentHubSharepointOneDrive` —OneDrive for
Business

**•** `ContentHubGDrive` —Google Drive

**•** `ContenHubIsotope` —Isotope

If Chatter is enabled, you can also specify `SimpleURL` to access
data hosted on a web server that doesn’t require authentication.


Metadata Types ExternalDataSource

**Field Name** **Field Type** **Description**

**•** `outgoingemail` —A data source used for sending an email
through a quick action.

For Digital Lending Configurator, the valid value is:

**•** `AFPPAttribute` —The data source name for the Application
Form Product Proposal Attribute virtual object.

For the federated search external data source type, the valid value
is:

**•** `OpenSearch`

For Transaction Management in Revenue Cloud, the valid values
are:

**•** `ASPAttribute` —The data source name for the Asset State
Period Attribute virtual object. Available in API version 63.0 and
later.

**•** `OIAttribute` —The data source name for the Order Item
Attribute virtual object. Available in API version 63.0 and later.

**•** `QLIAttribute` —The data source name for the Quote Line
Item Attribute virtual object. Available in API version 63.0 and
later.

For SalesAgreement in Manufacturing Cloud, the valid values are:

**•** `SAPAttribute` —The data source name for the
SalesAgreement Product Attribute virtual object. Available in
API version 60.0 and later.

These values are reserved for internal use:

**•** `AssetAttribute`

**•** `ClaimAttributeDS`

**•** `ClaimItemAttributeDS`

**•** `CryptoTrEnvChgLogSnp`

**•** `CtrtGrpPlnAttr`

**•** `CtrtGrpPlnGrpClsAttr`

**•** `FAAttribute`

**•** `FLAttribute`

**•** `IAItemProdtAttr`

**•** `Identity`

**•** `InsPolicyAttribute`

**•** `IPAAttribute`

**•** `IPCAttribute`

**•** `IPCvrBnftAttribute`

**•** `IPPAttribute`

**•** `SdbOvenPODataSource`


Metadata Types ExternalDataSource

**Field Name** **Field Type** **Description**

**•** `Wrapper`

`username` string The user name that your org uses to access the external system.
Make sure that the credentials you use have adequate privileges to

access the external system, perform searches, return data, and return
information about the external system’s metadata.

`version` string Reserved for future use.

CustomHttpHeaders

Represents a custom HTTP header used with OData 2.0 or OData 4.0 connectors. Available in API version 43.0 or later.

**Field Name** **Field Type** **Description**

`description` string A text description of the header field’s purpose.

`headerFieldName` string

`headerFieldValue` string

Required. Name of the header field. The name must contain at least one
alphanumeric character or underscore. It can also include these
characters: `! # $ % & ' * + - . ^ _ ` | ~` .

Required. A formula that resolves to the value for the header. The values
in the formula must evaluate to a string. If the formula resolves to null
and an empty string, the header isn’t sent.

`isActive` boolean Indicates whether the custom HTTP header is available to use ( `true` )
or unavailable ( `false` ).

**`customConfiguration`** for Salesforce Connect—Cross-Org Adapter

This sample JSON-encoded configuration string defines parameters that apply when the external data source’s `type` is set to `SfdcOrg` .

```
{"apiVersion":"32.0","environment":"CUSTOM",

"searchEnabled":"true","timeout":"120"}

```

The parameters correspond to these fields in the user interface:

**•** `apiVersion` - `API Version`

**•** `environment` - `Connect to`

**•** `searchEnabled` - `Enable Search`

**•** `timeout` - `Connection Timeout`

**`customConfiguration`** for Salesforce Connect—OData 2.0 or 4.0 Adapter

This JSON-encoded configuration string defines parameters that apply when the external data source’s `type` is set to `OData` or
`OData4` .

```
{"inlineCountEnabled":"true","csrfTokenName":"X-CSRF-Token",

"requestCompression":"false","pagination":"CLIENT",

```


Metadata Types ExternalDataSource

```
   "noIdMapping":"false","format":"ATOM",

   "searchFunc":"","compatibility":"DEFAULT",

   "csrfTokenEnabled":"true","timeout":"120",

   "searchEnabled":"true"}

```

The parameters correspond to these fields in the user interface.

**•** `compatibility`   - `Special Compatibility`

**•** `csrfTokenEnabled`   - `Cross-Site Request Forgery (CSRF) Protection`

**•** `csrfTokenName`   - `Anti-CSRF Token Name`

**•** `format`   - `Format`

**•** `inlineCountEnabled`   - `Request Row Counts`

**•** `noIdMapping`   - `High Data Volume`

**•** `pagination`   - `Server Driven Pagination`

**•** `requestCompression`   - `Compress Requests`

**•** `searchEnabled`   - `Enable Search`

**•** `searchFunc`   - `Custom Query Option for Salesforce Search`

**•** `timeout`   - `Connection Timeout`

Declarative Metadata Sample Definition: OData 2.0 or 4.0

The following is the definition of an external data source for Salesforce Connect—OData 2.0 or 4.0 adapter.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ExternalDataSource xmlns="http://soap.sforce.com/2006/04/metadata">

      <authProvider>FacebookAuth</authProvider>

      <customConfiguration>{"compatibility":"DEFAULT",

      "noIdMapping":"false","inlineCountEnabled":"true",

      "searchEnabled":"true","format":"ATOM",

      "requestCompression":"false","pagination":"SERVER",

      "timeout":"120"}</customConfiguration>

      <customHttpHeaders>

        <headerFieldName>X-User</headerFieldName>

        <headerFieldValue>$User.Username</headerFieldValue>

      </customHttpHeaders>

      <endpoint>http://myappname.herokuapp.com/DataHub.svc</endpoint>

      <label>DataHub</label>

      <principalType>NamedUser</principalType>

      <protocol>Oauth</protocol>

      <type>OData</type>

   </ExternalDataSource>

```

**`customConfiguration`** for Salesforce Connect—Custom Adapter

This sample JSON-encoded configuration string defines the parameter that applies when the external data source’s `type` is set to the
ID of a `DataSource.Provider` class.

```
   {"noIdMapping":"false"}

```

The `noIdMapping` parameter corresponds to the `High Data Volume` field in the user interface.


Metadata Types ExternalDataSource

**`ExternalDataSrcDescriptors`** for Salesforce Connect Adapter for Amazon
DynamoDB and for Amazon Athena

Represents schema descriptors for an external data source used with the Salesforce Connect adapter. The schema descriptors are for
Amazon DynamoDB (available in API version 55.0 or later) or Amazon Athena (available in API version 56.0 or later).

**Field Name** **Field Type** **Description**

`customObject` string If set, the external object associated with the descriptor.

`descriptor` string Required. The descriptor document that contains the metadata
information.

`descriptorVersion` string If the external system supports schema versioning for the data source,
the optional descriptor document version tracks the external system's

schema version. Several descriptors with different document versions
can be active.

`developerName` string Required. The unique name of the child-level setup entity.

`externalDataSource` string Required. The name of the external data source associated with the
descriptor.

Required. The subtype of the descriptor.

Values are:

**•** `SchemaTableMetadata` - Used to cache information about
the external system.

**•** `SchemaTableQualifiers` - Used to customize the data
retrieval query to the external system.

```
subtype

```

ExternalDataSrcDescSubtype
(enumeration of
type string)

`systemVersion` int Required. The version that defines the descriptor format and provides
compatibility with descriptor formats between Salesforce releases.

Required. The type of the descriptor.

Valid value:

**•** `Schema`

```
type

```

ExternalDataSrcDescType
(enumeration of
type string)

Declarative Metadata Sample Definition: Amazon DynamoDB

The following is an example of an external data source for the Salesforce Connect adapter for Amazon DynamoDB that uses
`ExternalDataSrcDescriptor` component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ExternalDataSource xmlns="http://soap.sforce.com/2006/04/metadata">

   <customConfiguration>{"timeout":"120"}</customConfiguration>

   <externalDataSrcDescriptors>

     <fullName>MyQualifierName</fullName>

     <customObject>MyExternalObject__x</customObject>

     <descriptor>

     {

      "tableName": "MyDynamoDBTable",

```


Metadata Types ExternalDataSource

```
         "columns": {

           "MyField": {"presence": "exists"}

         }

        }

        </descriptor>

        <developerName>MyQualifierName</developerName>

        <externalDataSource>MyDataSource</externalDataSource>

        <subtype>SchemaTableQualifiers</subtype>

        <systemVersion>0</systemVersion>

        <type>Schema</type>

      </externalDataSrcDescriptors>

      <isWritable>true</isWritable>

      <label>MyDataSource</label>

      <namedCredential>MyNamedCredential</namedCredential>

      <principalType>Anonymous</principalType>

      <protocol>NoAuthentication</protocol>

      <type>AmazonDynamoDb</type>

   </ExternalDataSource>

```

Declarative Metadata Sample Definition: Amazon Athena

The following is an example of an external data source for the Salesforce Connect adapter for Amazon Athena that uses
`ExternalDataSrcDescriptor` component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ExternalDataSource xmlns="http://soap.sforce.com/2006/04/metadata">

      <customConfiguration>

      {

       "DataCatalog": "AwsDataCatalog",

       "timeout": "120"

      }

      </customConfiguration>

      <externalDataSrcDescriptors>

        <fullName>MyAthenaQualifierName</fullName>

        <customObject>MyAthenaExternalObject__x</customObject>

        <descriptor>

        {

         "tableName": "myathenadatabase.myathenatable",

         "extendedQualifiers": {"workgroup": "primary"},

         "keyColumns": ["ExternalIdComponent", "OtherExternalIdComponent"]

        }

        </descriptor>

        <developerName>MyAthenaQualifierName</developerName>

        <externalDataSource>MyAthenaDataSource</externalDataSource>

        <subtype>SchemaTableQualifiers</subtype>

        <systemVersion>0</systemVersion>

        <type>Schema</type>

      </externalDataSrcDescriptors>

      <isWritable>false</isWritable>

      <label>MyAthenaDataSource</label>

      <namedCredential>MyAthenaNamedCredential</namedCredential>

      <principalType>Anonymous</principalType>

      <protocol>NoAuthentication</protocol>

      <type>AmazonAthena</type>

   </ExternalDataSource>

```


#### Metadata Types ExternalDataTransportFieldTemplate

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### ExternalDataTransportFieldTemplate

For internal use only.

#### ExternalDataTranObject

Represents a definition of a Data 360 schema object. This type extends the Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

#### ExternalDataTranObject components have the suffix .externalDataTranObject and are stored in the

`externalDataTranObjects` folder.

Version

#### ExternalDataTranObject components are available in API version 55.0 and later.

Special Access Rules

#### ExternalDataTranObject is available only if Data 360 is provisioned.

Fields

**Field Name** **Description**

```
availabilityStatus

creationType

```

**Field Type**
AvailabilityStatus (enumeration of type string)

**Description**

Required.

Represents the availability of the object. Valid values are:

**•** `Available`

**•** `In_Use`

**Field Type**
DefinitionCreationType (enumeration of type string)

**Description**

Required.


Metadata Types ExternalDataTranObject

**Field Name** **Description**

Describes whether this object was added by the Customer or as part of a Standard
Taxonomy or by the System. Valid values are:

**•** `Segment_Membership`

**•** `Activation_Audience` (Reserved for internal use only)

**•** `Custom`

**•** `Standard`

**•** `System`

**•** `Derived`

**•** `Bridge`

**•** `Curated`

**•** `Standard`

Valid values available in API version 62.0 and later are:

**•** `ADG`

**•** `Calculated_Insight`

**•** `CG_Audience`

**•** `Chunk`

**•** `Directory_Table`

**•** `External`

**•** `Semantic`

**•** `Transform`

**•** `Vector_Embedding`

```
extDataTranObjectTemplate

externalDataTranFields

masterLabel

```

**Field Type**
string

**Description**
Reserved for internal use and read-only. Reference to the associated
ExtDataTranObjectTemplate data kit object. The system populates this field when
a data kit that contains a data stream is deployed.

**Field Type**

ExternalDataTranField

**Description**

Optional.

Stores the fields related to that schema object.

**Field Type**
string

**Description**

Required.


Metadata Types ExternalDataTranObject

**Field Name** **Description**

The UI name for the object.

```
mktDataTranObject

objectCategory

```

ExternalDataTranField

**Field Type**

MktDataTranObject

**Description**

Optional.

An entity that is used to transport information from the source to a target.

**Field Type**
string

**Description**

Required.

Reference to the Object Category. For Transport, they're Profile, Engagement, or
Other.

Stores the fields related to ExternalDataTranObject schema.

**Field Name** **Description**

```
creationType

datatype

```

**Field Type**
DefinitionCreationType (enumeration of type string).

**Description**

Required.

Describes whether this object was added by the Customer or as part of a Standard Taxonomy
or by the System. Valid values are:

**•** `Segment_Membership`

**•** `Custom`

**•** `Standard`

**•** `System`

**•** `Derived`

**•** `Bridge`

**•** `Curated`

**Field Type**
string

**Description**

Required.


Metadata Types ExternalDataTranObject

**Field Name** **Description**

Phone, currency, number, or other assigned type.

```
dateFormat

extDataTranFieldTemplate

externalName

isCurrencyIsoCode

isDataRequired

length

```

**Field Type**
string

**Description**

Optional.

The Date format of date, time, date/time fields in this Transport field.

**Field Type**
string

**Description**
Reserved for internal use and read-only. Reference to the associated
ExtDataTranFieldTemplate data kit object. The system populates this field when a data kit
that contains a data stream is deployed.

**Field Type**
string

**Description**

Optional.

Name of the object in the external system (different from Developer Name).

**Field Type**
boolean

**Description**

Optional.

If true, this field is a currency ISO code.

**Field Type**
boolean

**Description**

Optional.

If true, data is required for this field.

**Field Type**
int

**Description**

Optional.

Length of a string column.

`masterLabel` Optional. Field label.


Metadata Types ExternalDataTranObject

**Field Name** **Description**

```
mktDataTranField

precision

primaryIndexOrder

scale

sequence

```

MktDataTranField

**Field Type**

mktDataTranFieldType on page 242

**Description**

Optional.

**Field Type**
int

**Description**

Optional.

Used for currency and numeric accuracy.

**Field Type**
int

**Description**

Optional.

If supplied, indicates this field is part of the primary key where the number value (starting
at 1) indicates the order of attributes if it's a compound primary key. Missing value means
this field isn’t part of the primary key.

**Field Type**
int

**Description**

Optional.

Used for currency and numbers.

**Field Type**
int

**Description**

Optional.

The sequence of this source schema.

Stores fields related to MktDataTranObject.

**Field Name** **Description**

```
creationType

```

**Field Type**
DefinitionCreationType (enumeration of type string).


Metadata Types ExternalDataTranObject

**Field Name** **Description**

**Description**

Required.

Describes whether this object was added by the Customer or as part of a Standard Taxonomy
or by the System. Valid values are:

**•** `Segment_Membership`

**•** `Custom`

**•** `Standard`

**•** `System`

**•** `Derived`

**•** `Bridge`

**•** `Curated`

**•** Valid values available in API version 62.0 and later are:

**–** `ADG`

**–** `Calculated_Insight`

**–** `CG_Audience`

**–** `Chunk`

**–** `Directory_Table`

**–** `External`

**–** `Semantic`

**–** `Transform`

**–** `Vector_Embedding`

```
datatype

dateFormat

externalName

```

**Field Type**
string

**Description**

Required.

Phone, currency, number, or other assigned type.

**Field Type**
string

**Description**

Optional.

The Date format of date, time, date/time fields in this Transport field.

**Field Type**
string

**Description**

Optional.


Metadata Types ExternalDataTranObject

**Field Name** **Description**

Name of the object in the external system (different from Developer Name).

```
isDataRequired

length

```

**Field Type**
boolean

**Description**

Optional.

If true, data is required for this field.

**Field Type**
int

**Description**

Optional.

Length of a string column.

`masterLabel` Optional. Field label.

```
precision

primaryIndexOrder

scale

sequence

```

**Field Type**
int

**Description**

Optional.

Used for currency and numeric accuracy.

**Field Type**
int

**Description**

Optional.

If supplied, indicates this field is part of the primary key where the number value (starting
at 1) indicates the order of attributes if it's a compound primary key. Missing value means
this field isn’t part of the primary key.

**Field Type**
int

**Description**

Optional.

Used for currency and numbers.

**Field Type**
int

**Description**

Optional.


#### Metadata Types ExternalDataTransportObjectTemplate

**Field Name** **Description**

The sequence of this source schema.

Declarative Metadata Sample Definition

The following is an example of a ExternalDataTranObject component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ExternalDataTranObject xmlns="http://soap.sforce.com/2006/04/metadata">

        <fullName>PlatformTraces</fullName>

        <availabilityStatus>Available</availabilityStatus>

        <creationType>Custom</creationType>

        <masterLabel>PlatformTraces</masterLabel>

        <objectCategory>Salesforce_SFDCReferenceModel_0_93.Engagement</objectCategory>

   </ExternalDataTranObject>

```

The following is an example `package.xml` that references the previous definition.

```
   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ExternalDataTranObject</name>

      </types>

      <version>55.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/file_based_zip_file.htm)

#### ExternalDataTransportObjectTemplate

For internal use only.

#### FieldSrcTrgtRelationship

Stores the relationships between a data model object (DMO) and its fields. For example, the `Individual.Id` field has a one-to-many
relationship (1:M) with the `ContactPointEmail.PartyId` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types FieldSrcTrgtRelationship

File Suffix and Directory Location

FieldSrcTrgtRelationship components have the suffix `.fieldSrcTrgtRelationship` and are stored in the
`fieldSrcTrgtRelationships` folder.

Version

FieldSrcTrgtRelationship components are available in API version 51.0 and later.

Special Access Rules

To access this metadata type, you must have the Customize Application user permission.

Fields

**Field Name** **Field Type** **Description**

Required. Describes whether this object was added by the user or as
part of a standard taxonomy.

Values are:

**•** `ADG`

**•** `Activation_Audience`

**•** `Bridge`

**•** `Calculated_Insight`

**•** `Chunk`

**•** `Curated`

**•** `Custom`

**•** `Derived`

**•** `Directory_Table`

**•** `External`

**•** `Ml_Prediction`

**•** `Segment_Membership`

**•** `Semantic`

**•** `Standard`

**•** `System`

**•** `Transform`

**•** `Vector_Embedding`

```
definitionCreationType

```

DefinitionCreationType
(enumeration of
type string)

`lookupFieldName` string Reference to the DMO lookup field.

`masterLabel` string Required. The UI name for the field relationship.

Optional. The type of relationship that exists between the source and
the target.

Values are:


```
owner

```

FieldSrcTrgtRelationshipOwner
(enumeration of
type string)

#### Metadata Types InternalDataConnector

**Field Name** **Field Type** **Description**

**•** `SObject`                          - The source of the relationship is a DMO and the target
is a standard or custom SObject.

**•** `DataCloud`                          - Both the source and the target of the relationship
are DMOs.

The field is needed only when the target is an SObject. The system can
infer the value when the target is a DMO.

Required. Cardinality of the relationship between the source and target
fields.

Values are:

**•** `ManyToOne`

**•** `OneToOne`

```
relationshipCardinality

```

RelationshipCardinality
(enumeration of
type string)

`sourceFieldName` string Required. Name of the field that represents the source side of the
relationship.

`targetEntity` string Optional. Name of the entity that represents the target side of the
relationship. The target entity can be a DMO or a standard or custom

SObject. The field is needed only when the target entity is an SObject.
The system can infer the value when the target entity is a DMO.

`targetFieldName` string Required. Name of the field that represents the target side of the
relationship.

#### InternalDataConnector

For internal use only.

#### MarketSegmentDefinition

Represents the field values for MarketSegmentDefinition. MarketSegmentDefinition is used to store the exportable metadata of a segment,
such as segment criteria and other attributes. Developers can create segment definition packages, pass segment definition in the form
of data build tool (DBT), and publish it on AppExchange for subscriber organizations to install and instantiate these segments.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata type and inherits its `fullName` field.

File Suffix and Directory Location

#### MarketSegmentDefinition components have the suffix .marketSegmentDefinition and are stored in the

`marketSegmentDefinitions` folder.


Metadata Types MarketSegmentDefinition

Version

MarketSegmentDefinition components are available in API version 55.0 and later.

Fields

**Field Name** **Description**

```
additionalMetadata

excludeCriteria

includeCriteria

masterLabel

segmentOn

segmentType

```

**Field Type**
string

**Description**
An XML clob to hold name value pairs for storing additional metadata. Not applicable
for DBT type segment.

**Field Type**
string

**Description**
Holds the JSON exclude criteria for UI based segments. Not applicable for DBT or
Lookalike segments.

**Field Type**
string

**Description**
An XML wrapped in a CDATA section that captures DBT definition. Only single model
DBT is supported.

**Field Type**
string

**Description**

Required. Display name of the field value.

**Field Type**
string

**Description**
Required when `segmentType` is `UI` . Points to relevant MktDataModelObject entity
instance. Must be a valid developerName for an MktDataModelObject instance of
Profile type.

**Field Type**
MarketSegmentType (enumeration of type string)

**Description**

Required. Type of the segment to be created. Only DBT is supported via API.

Values are:

**•** `DBT`


Metadata Types MarketSegmentDefinition

**Field Name** **Description**

**•** `Lookalike`

**•** `UI`

**•** `EinsteinGPTSegmentsUI`

Declarative Metadata Sample Definition

The following is an example of a MarketSegmentDefinition component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <MarketSegmentDefinition>

      <segmentType>DBT</segmentType>

      <includeCriteria>

      <![CDATA[

        <DbtPipeline>

           <models>

             <model>

               <name>m1</name>

               <sql>select ssot__Individual__dlm.ssot__Id__c from

   ssot__Individual__dlm</sql>

             </model>

           </models>

        </DbtPipeline>

        ]]>

      </includeCriteria>

      <masterLabel>msd2_simple</masterLabel>

   </MarketSegmentDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8" standalone="yes"?>

   <ns2:Package xmlns:ns2="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>MarketSegmentDefinition</name>

      </types>

      <version>55.0</version>

   </ns2:Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
[wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_settings.htm)
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/file_based_zip_file.htm)


#### Metadata Types MktCalcInsightObjectDef MktCalcInsightObjectDef

Represents Calculated Insight definition such as expression.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

#### MktCalcInsightObjectDef components have the suffix mktCalcInsightObjectDef and are stored in the mktCalcInsightObjectDefs folder.

Version

#### MktCalcInsightObjectDef components are available in API version 52.0 and later.

Special Access Rules

You need the Salesforce CustomizeApplication permission to access this object.

Fields

**Field Name** **Field Type** **Description**

`builderExpression` string Reserved for internal use.

`creationType` [CalculatedInsightCreationType(enumeration](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_objects_intro.htm#enumeration_title) Required. Describes whether this Calculated Insight Object Definition
of type string) was added was added by the customer. Valid values include: Custom.

`description` string The description for this Calculated Insight Object Definition.

`expression` string Required when the Calculated Insight Object Definition is for internal
insight type. This is the SQL query to generate the calculated insight.

`masterLabel` string Required. App name for this Calculated Insight Object Definition.

`system` string

Required. Indicates how this calculated insight object definition was
added, by the customer or by the system. Valid values are:

**•** Custom

**•** System (API version 61.0 and later)


#### Metadata Types MktDataTranObject

Declarative Metadata Sample Definition

The following is an example of a MktCalcInsightObjectDef component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <MktCalcInsightObjectDef xmlns="http://soap.sforce.com/2006/04/metadata">

      <creationType>Custom</creationType>

      <description>InsightName description</description>

      <expression>SELECT COUNT(ssot__Individual__dlm.ssot__Id__c) as count__c FROM

   ssot__Individual__dlm</expression>

   </MktCalcInsightObjectDef>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### MktDataTranObject

An entity that is used to deliver (aka transport) information from the source to a target (target will be called a landing entity).This can
be the schema of a file, API, Event, or other means of transporting data, such as SubscriberFile1.csv, or SubscriberCDCEvent.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

#### MktDataTranObject components have the suffix mktDataTranObject and are stored in the mktDataTranObjects folder.

Version

#### MktDataTranObject components are available in API version 50.0 and later.

Special Access Rules

You need the Salesforce CustomizeApplication permission to access this object.

Fields

**Field Name** **Field Type** **Description**

`connector` string Required. Data 360 connector name that allows you to connect the data
source to Data 360.

`creationType` DefinitionCreationType Required. Describe whether this object was added as the result of the
Customer or as part of a Standard Taxonomy.

**•** Valid values available in API version 62.0 and later are:

**–** `ADG`

**–** `Calculated_Insight`


Metadata Types MktDataTranObject

**Field Name** **Field Type** **Description**

**–** `CG_Audience`

**–** `Chunk`

**–** `Directory_Table`

**–** `External`

**–** `Semantic`

**–** `Transform`

**–** `Vector_Embedding`

`dataSource` string

Required. Your reference to the data source from which the data
originated (source of that data such as the name of a CRM Org. Example:
MC Enterprise.

`dataSourceObject` string Required. Represents the object name from where the data is sourced.
Example: ecommerce-OrderItem.

`masterLabel` string Required. The UI name for the Data Transport Object.

`objectCategory` string Required. Reference to the Object Category. For Transport, these are
Profile, Engagement, or Other.

MktDataTranField

This is a sub-type to MktDataTranObject.

**Field Name** **Field Type** **Description**

`creationType` DefinitionCreationType Optional: Was this object added as a result of the Customer, part of a Standard
Taxonomy.

**•** Valid values available in API version 62.0 and later are:

**–** `ADG`

**–** `Calculated_Insight`

**–** `CG_Audience`

**–** `Chunk`

**–** `Directory_Table`

**–** `External`

**–** `Semantic`

**–** `Transform`

**–** `Vector_Embedding`

`datatype` string Required. Phone, currency, number, or other assigned type.

`dateFormat` string Optional: The Date format of date, time, date/time fields in this Transport field.


#### Metadata Types ObjectSourceTargetMap

**Field Name** **Field Type** **Description**

`externalName` string Optional. Name of the object in the external system (different from Developer
Name).

`isDataRequired` boolean Optional. If true, data is required for this field.

`length` int Optional. Length of a string column

`masterLabel` string Optional? Field label.

`precision` int Optional. Used for currency and numeric accuracy.

`primaryIndexOrder` int Optional. If supplied, indicates this field is part of the primary key where the
number value (starting at 1) indicates the order of attributes if this happens to

be a compound primary key. Missing value means this field is not part of the
primary key.

`scale` int Optional. Used for currency and numeric accuracy.

`sequence` int Optional. The sequence of this source schema.

#### ObjectSourceTargetMap

Contains the object-level mappings between the source and the target objects. The source and target objects can be an MktDataLakeObject
or an MktDataModelObject. For example, an Email source object can be mapped to the ContactPointEmail object.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

#### ObjectSourceTargetMap components have the suffix .objectSourceTargetMap and are stored in the

`objectSourceTargetMaps` folder.

Version

#### ObjectSourceTargetMap components are available in API version 51.0 and later.

Special Access Rules

To access this metadata type, you must have the Customize Application user permission.


Metadata Types ObjectSourceTargetMap

Fields

**Field Name** **Field Type** **Description**

```
creationType

```

DefinitionCreationType Describes whether this object was added by the user or as part of a
(enumeration of standard taxonomy. Valid values are:
type string)

**•** `ADG`

**•** `Activation_Audience`

**•** `Bridge`

**•** `Calculated_Insight`

**•** `CG_Audience` (Available in API version 62.0 and later)

**•** `Chunk`

**•** `Curated`

**•** `Custom`

**•** `Derived`

**•** `Directory_Table`

**•** `External`

**•** `Ml_Prediction`

**•** `Segment_Membership`

**•** `Semantic`

**•** `Standard`

**•** `System`

**•** `Transform`

**•** `Vector_Embedding`

`fieldSourceTargetMaps` FieldSourceTargetMap[] Contains the field-level mappings associated with this object mapping.

`masterLabel` string Required. The UI name for the target map.

`sequenceNbr` int

Use this field to display multiple mappings between the same two
objects, for a consistent customer experience when presenting the
mappings.

`sourceObjectName` string Required. Name of the source object that’s mapped, such as Email, or
SfmcEnt1_Subscriber.

`targetObjectName` string Required. Name of the target object that’s mapped, such as
ContactPointEmail or Individual.

FieldSourceTargetMap

Contains the field-level mappings between the source and the target objects.

The source and target can be MktDataLakeField or MktDataModelField.

For example, you can map a Person source object’s field called emailAddress to an Individual target object's field called emailAddress.


Metadata Types ObjectSourceTargetMap

**Field Name** **Field Type** **Description**

Describes whether this object was added by the user or as part of a standard
taxonomy.

Values are:

**•** `ADG`

**•** `Activation_Audience`

**•** `Bridge`

**•** `Calculated_Insight`

**•** `Chunk`

**•** `Curated`

**•** `Custom`

**•** `Derived`

**•** `Directory_Table`

**•** `External`

**•** `Ml_Prediction`

**•** `Segment_Membership`

**•** `Semantic`

**•** `Standard`

**•** `System`

**•** `Transform`

**•** `Vector_Embedding`

```
creationType

```

DefinitionCreationType
(enumeration of type
string)

`filterApplied` boolean Specifies whether the field-level mapping is an event type filter ( `true` ) or not
( `false` ).

`filterOperationType` string

If the field-level mapping is an event type filter, specifies the filtering operator.

Value is:

**•** `Equal`

`filterValue` string If the field-level mapping is an event type filter, specifies the object that contains
the event type field.

`isSourceFormula` boolean Specifies whether the source field is a formula ( `true` ) or not ( `false` ). If `true`,
you must include the sourceFormula value.

`sourceField` string Required. The source object field that’s mapped, such as `EmailAddr` or
`SfmcEnt1_Subscriber.FName` .

`sourceFormula` string A formula, such as concatenation, date function, or constant value.

`targetField` string Required. The target object field that’s mapped, such as
`SfmcEnt1_Email.EmailAddr` or `Individual.FirstName` .


#### Metadata Types StreamingAppDataConnector StreamingAppDataConnector

Represents the connection information specific to Web and Mobile Connectors.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

#### StreamingAppDataConnector components have the suffix .streamingAppDataConnector and are stored in the

`streamingAppDataConnectors` folder.

Version

#### StreamingAppDataConnector components are available in API version 55.0 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Description**

```
appIdentifier

dataConnectorType

isProtected

```

**Field Type**
string

**Description**

Required.

The unique app identifier (UUID).

**Field Type**
DataConnectorType (enumeration of type string)

**Description**

Required.

The value of the field is restricted to `SteamingApp` .

Possible values are:

**•** `DataCloud`

#### • StreamingApp

**Field Type**
boolean


Metadata Types StreamingAppDataConnector

**Field Name** **Description**

**Description**
An auto-generated value that doesn’t impact the behavior of the metadata type.

```
masterLabel

streamingAppDataConnectorType

```

**Field Type**
string

**Description**

Required.

The display name of the connector.

**Field Type**
StreamingAppDataConnectorType (enumeration of type string)

**Description**

Required.

The type of connector.

Possible values are:

**•** `MobileApp`

**•** `WebApp`

Declarative Metadata Sample Definition

The following is an example of a StreamingAppDataConnector component.

```
<?xml version="1.0" encoding="UTF-8"?>

<StreamingAppDataConnector xmlns="http://soap.sforce.com/2006/04/metadata">

   <appIdentifier>61826b62-6b90-49ff-8259</appIdentifier>

   <dataConnectorType>StreamingApp</dataConnectorType>

   <masterLabel>My Web Application</masterLabel>

   <streamingAppDataConnectorType>WebApp</streamingAppDataConnectorType>

</StreamingAppDataConnector>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <fullName>MyPackage</fullName>

   <namespacePrefix>ns1</namespacePrefix>

   <types>

     <members>My_Web_Application_Behavioral_Events_F4DA8759</members>

     <name>DataStreamDefinition</name>

   </types>

   <types>

     <members>My_Web_Application_61826b62_6b90_49ff_8259</members>

     <name>ExternalDataConnector</name>

   </types>

   <types>

```


### Metadata Types AccountPlanObjMeasCalcDef

```
        <members>My_Web_Application_61826b62_6b90_49ff_8259</members>

        <name>StreamingAppDataConnector</name>

      </types>

      <version>55.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### AccountPlanObjMeasCalcDef

Represents the metadata associated with an account plan objective measure calculation definition. An account plan objective measure
calculation definition contains a target object, rollup field, and logic for calculating the current value of a sales account plan objective
measure.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### AccountPlanObjMeasCalcDef components have the suffix .accountPlanObjMeasCalcDef and are stored in the

`accountPlanObjMeasCalcDefs` folder.

Version

### AccountPlanObjMeasCalcDef components are available in API version 63.0 and later.

Special Access Rules

To access AccountPlanObjMeasCalcDef components, enable account plans.

Fields

**Field Name** **Description**

```
conditions

```

**Field Type**

AccountPlanObjMeasCalcCond

**Description**
The field and value combinations for filtering records to include in the calculation
definition.


Metadata Types AccountPlanObjMeasCalcDef

**Field Name** **Description**

```
description

developerName

masterLabel

rollupType

```

**Field Type**
string

**Description**
A summary of the calculation definition that’s visible to users when they select the
definition for an account plan objective measure.

**Field Type**
string

**Description**

Required.

The unique name of the object in the API. The name:

**•** must be 40 characters or fewer

**•** must begin with a letter

**•** can contain only underscores and alphanumeric characters

**•** can’t include spaces

**•** can’t end with an underscore

**•** can’t contain 2 consecutive underscores

**Field Type**
string

**Description**

Required.

Label for this calculation definition. This display value is the internal label that doesn't
get translated.

**Field Type**
string

**Description**

Required.

The method for calculating the account plan objective measure’s current value from
records that match the calculation definition and any optional conditions.

Possible values are:

**•** `Count`

**•** `Max`

**•** `Min`

**•** `Sum`

In Setup, this field’s label is Calculation Type.


Metadata Types AccountPlanObjMeasCalcDef

**Field Name** **Description**

```
status

targetField

targetObject

```

**Field Type**
string

**Description**

Required.

Specifies the status of the calculation definition. Possible values are:

**•** `Active`

**•** `Draft`

**•** `Inactive`

Only active calculation definitions are available for users to select when they specify
an account plan objective measure.

**Field Type**
string

**Description**
The field on `TargetObject` to use for calculating the account plan objective
measure’s current value. Rollup fields on the Campaign, Case, Contact, or Opportunity
object are supported.

In Setup, this field’s label is Rollup Field.

**Field Type**
string

**Description**

Required.

The object to use for calculating the account plan objective measure’s current value.

Possible values are:

**•** `Campaign`

**•** `Case`

**•** `Contact`

**•** `Opportunity`

AccountPlanObjMeasCalcCond

Represents a field and value combination for filtering records to include in the calculation of a sales account plan objective measure’s
current value.

**Field Name** **Description**

```
fieldName

```

**Field Type**
string


Metadata Types AccountPlanObjMeasCalcDef

**Field Name** **Description**

**Description**

Required.

A field on the calculation definition’s `TargetObject` that you want to filter by.
Fields on the Campaign, Case, Contact, or Opportunity objects are supported.

```
operation

value

```

**Field Type**
string

**Description**

Required.

The logical operator for matching records with the specified field value.

Possible values are:

**•** `Contains`

**•** `Equals`

**•** `GreaterOrEqual`

**•** `GreaterThan`

**•** `LessOrEqual`

**•** `LessThan`

**•** `NotContain`

**•** `NotEqual`

**•** `StartsWith`

**Field Type**
string

**Description**

Required.

The value to match for the specified field.

Declarative Metadata Sample Definition

The following is an example of an AccountPlanObjMeasCalcDef component.

```
<?xml version="1.0" encoding="UTF-8"?>

<AccountPlanObjMeasCalcDef xmlns="http://soap.sforce.com/2006/04/metadata">

 <conditions>

  <fieldName>StageName</fieldName>

  <operation>Equals</operation>

  <value>ClosedWon</value>

 </conditions>

 <description>Define sales revenue goals. Current Value will be

  auto-calculated as the sum of your selected Opportunities

  Amount with 'Closed Won' Stage.

```


### Metadata Types AccountRelationshipShareRule

```
    </description>

    <developerName>Opportunity_Revenue_Targets</developerName>

    <masterLabel>Opportunity Revenue Targets</masterLabel>

    <rollupType>Sum</rollupType>

    <status>Active</status>

    <targetField>Amount</targetField>

    <targetObject>Opportunity</targetObject>

   </AccountPlanObjMeasCalcDef>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

         <members>Opportunity_Revenue_Targets</members>

         <name>AccountPlanObjMeasCalcDef</name>

      </types>

      <version>63.0</version>

   </Package>

### AccountRelationshipShareRule

```

The rule that determines which object records are shared, how they’re shared, the account relationship type that shares the records,
and the level of access granted to the records.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

This type extends the MetadataWithContent metadata type and inherits its `content` and `fullName` fields.

File Suffix and Directory Location

### AccountRelationshipShareRule components have the suffix .accountRelationshipShareRule and are stored in the

`.accountRelationshipShareRules` folder.

Version

### AccountRelationshipShareRule components are available in API version 45.0 and later.

Special Access Rules

Access to the AccountRelationshipShareRule type requires orgs to enable the Account Relationships permission. The Manage Experiences
permission is required for user access.


Metadata Types AccountRelationshipShareRule

Fields

**Field Name** **Field Type** **Description**

`accessLevel` string Type of access granted by the share rule. Valid values are:

**•** Read

**•** Edit

`accountToCriteriaField` string

Criteria that must be met for the data to be shared. Valid values include
any custom or standard lookup to Account or User on top-level objects.

To get the full list for your org, do a Describe on the ARSR entity.

`description` string A meaningful explanation of the sharing rule.

`entityType` string The type of data shared by this share rule. Valid values are:

**•** Account

**•** Campaign

**•** Case

**•** Contact

**•** Custom Object

**•** Lead

**•** Opportunity

**•** Order

**•** Quote

API names of top-level custom objects in the org can also be used, for
example, CustomObject__c.

`masterLabel` string The label assigned to the sharing rule to identify it.

`staticFormulaCriteria` string A way to further filter what data gets shared. This string must be a
deterministic formula, and spanning isn’t allowed.

`type` string Match the type of an account relationship for data to be shared according
to the accountToCriteriaField and the staticFormulaCriteria fields.

Declarative Metadata Sample Definition

The following is an example of an AccountRelationshipShareRule component.

```
<?xml version="1.0" encoding="UTF-8"?>

<AccountRelationshipShareRule xmlns="http://soap.sforce.com/2006/04/metadata">

   <accessLevel>Edit</accessLevel>

   <accountToCriteriaField>Account.OwnerId</accountToCriteriaField>

   <description>TestDescription</description>

   <entityType>Account</entityType>

   <masterLabel>TestName</masterLabel>

   <staticFormulaCriteria>YearStarted = &quot;1980&quot;</staticFormulaCriteria>

```


### Metadata Types AccountingFieldMapping

```
      <type>Dealer</type>

   </AccountRelationshipShareRule>

```

The following is an example `package.xml` that references the previous definition.

```
   <Package>

   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>ArsrDevName</members>

        <name>AccountRelationshipShareRule</name>

      </types>

   <version>45.0</version>

   </Package>

```

This metadata type supports the wildcard character * (asterisk) in the package.xml manifest file.

### AccountingFieldMapping

Represents the accounting field mappings to organize your data and bring it to ledger entry records.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### AccountingFieldMapping components have the suffix .accountingFieldMapping and are stored in the

`accountingFieldMappings` folder.

Version

### AccountingFieldMapping components are available in API version 58.0 and later.

Fields

**Field Name** **Description**

```
accountingModelConfig

```

**Field Type**
string

**Description**
Required.

Record ID of the AccountingModelConfig record that the Field Mapping is associated
with.


Metadata Types AccountingFieldMapping

**Field Name** **Description**

```
isForAllocationType

isForPaymentType

isForTransactionType

isProtected

mappingBehavior

masterLabel

sourceField

```

**Field Type**
boolean

**Description**
Reserved for internal use.

**Field Type**
boolean

**Description**
Reserved for internal use.

**Field Type**
boolean

**Description**
Reserved for internal use.

**Field Type**
boolean

**Description**
Indicates whether this component is protected ( `true` ) or not protected ( `false` ).

Default value is `false` .

**Field Type**
MappingBehaviorType (enumeration of type string)

**Description**
Required.

Specifies how the target’s field data is mapped from the source field only when the
journal entry is created. When set to `CurrentValue`, Subledger reverses and
replaces journal entries whose value differs from the value in `sourceField` .

Valid values are:

**•** `CurrentValue`

**•** `PointInTime`

**Field Type**
string

**Description**
Required.

A user-friendly name for AccountingFieldMapping, which is defined when the
AccountingFieldMapping is created.

**Field Type**
string


Metadata Types AccountingFieldMapping

**Field Name** **Description**

**Description**
The API name of the field on the source object that is mapped to the target field.

```
targetField

```

**Field Type**
string

**Description**
Required.

The API name of the field on the Transaction Journal record for this mapping.

Declarative Metadata Sample Definition

The following is an example of an AccountingFieldMapping component.

```
<?xml version="1.0" encoding="UTF-8"?>

<AccountingFieldMapping xmlns="http://soap.sforce.com/2006/04/metadata">

 <accountingModelConfig>ModelConfigOne</accountingModelConfig>

 <fullName>FieldMappingOne</fullName>

 <masterLabel>FieldMappingOne</masterLabel>

 <isForAllocationType>true</isForAllocationType>

 <isForPaymentType>true</isForPaymentType>

 <isForTransactionType>true</isForTransactionType>

 <mappingBehavior>PointInTime</mappingBehavior>

 <sourceField>TransactionJournal.MappingTargetOne__c</sourceField>

 <targetField>MappingTargetOne__c</targetField>

 <isProtected>false</isProtected>

</AccountingFieldMapping>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package

 xmlns="http://soap.sforce.com/2006/04/metadata">

 <types>

  <members>FieldMappingOne</members>

  <name>AccountingFieldMapping</name>

 </types>

 <version>58.0</version>

</Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types AccountingModelConfig AccountingModelConfig

Represents the mapping of the financial data model to a logical data model and configuration for the generation of Transaction Journal
records.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### AccountingModelConfig components have the suffix .accountingModelConfig and are stored in the

`accountingModelConfigs` folder.

Version

### AccountingModelConfig components are available in API version 57.0 and later.

Fields

**Field Name** **Description**

```
accountingType

defaultAccrualAccountCode

defaultWriteOffAccountCode

```

**Field Type**
AccountingType (enumeration of type string)

**Description**

Required.

Determines whether the accounting set generates revenue or expense type transaction
journal records.

Valid values are:

**•** `Expense`

**•** `Revenue`

**Field Type**
string

**Description**
The code for your accounting system's default accrual account.

**Field Type**
string

**Description**
Represents the name of your account for written off payments.


Metadata Types AccountingModelConfig

**Field Name** **Description**

```
earliestCreatedDate

expectedCashFlowGrouping

financeBook

internalMappingDetails

isActive

isGroupedByFundAccount

```

**Field Type**
dateTime

**Description**

Required.

The date used to filter source records for processing. The Accounting Subledger only
considers records created on or after this date.

**Field Type**
ExpectedCashFlowGrouping (enumeration of type string)

**Description**
Determines whether Accounting Subledger groups transaction journal records by
fund account or by a combination of fund account and due date.

Note: Changing this setting doesn't impact existing records; it only affects
records created or reversed afterward.

Valid values are:

**•** `GroupByFundAccount`

**•** `GroupByFundAndDueDate`

**Field Type**
string

**Description**
Reserved for internal use.

**Field Type**
string

**Description**

Required.

Represents the structure of your financial data in JSON format.

**Field Type**
boolean

**Description**

Required.

Indicates whether only records that are true are processed when the Subledger Job
runs.

**Field Type**
boolean

**Description**
Reserved for internal use.


Metadata Types AccountingModelConfig

**Field Name** **Description**

```
isUsed

jobFilterCriteria

masterLabel

paidCashFlowGrouping

recordTypeFilter

```

**Field Type**
boolean

**Description**

Required.

Indicates whether the Accounting Model has been used or activated at least once
( `true` ) or not ( `false` ).

Note: If the value is set to `true`, you can’t select another object for the object
model or change the number of objects associated with that Accounting Model.

**Field Type**
string

**Description**
Reserved for internal use.

**Field Type**
string

**Description**

Required.

A user-friendly name for AccountingModelConfig, which is defined when the
AccountingModelConfig is created.

**Field Type**
PaidCashFlowGrouping (enumeration of type string)

**Description**
Determines the level of detail for generated transaction journal records.

Valid values are:

**•** `GroupByFundAccount` —Accounting Subledger splits all transaction journal
records into fund accounts. Secondary records are created for payment type records
but not for transaction type records.

**•** `GroupBySummary` —Accounting Subledger only splits credits for revenue and
debits for expenses by fund accounts.

**Field Type**
string

**Description**
Specify the record type IDs from the primary object to be processed. This field is
case-sensitive.

Note: If no record type is specified in the filter, all records are processed.


Metadata Types AccountingModelConfig

**Field Name** **Description**

```
runOrder

```

**Field Type**
int

**Description**
Determines the load order sequence of the multiple Accounting Model. The lower
number runs first. For example, load order 1 runs before load order 2.

Declarative Metadata Sample Definition

The following is an example of an AccountingModelConfig component.

```
<?xml version="1.0" encoding="UTF-8"?>

<AccountingModelConfig

 xmlns="http://soap.sforce.com/2006/04/metadata">

 <fullName>ModelConfigOne</fullName>

 <masterLabel>ModelConfigOne</masterLabel>

 <defaultAccrualAccountCode>abc</defaultAccrualAccountCode>

 <defaultWriteOffAccountCode>abc</defaultWriteOffAccountCode>

 <isUsed>false</isUsed>

 <isActive>false</isActive>

 <runOrder>123</runOrder>

 <recordTypeFilter>abcabc</recordTypeFilter>

 <earliestCreatedDate>2021-12-01T00:00:00.000Z</earliestCreatedDate>

 <internalMappingDetails>abcabc</internalMappingDetails>

 <accountingType>Revenue</accountingType>

 <expectedCashFlowGrouping>GroupByFundAccount</expectedCashFlowGrouping>

 <paidCashFlowGrouping>GroupBySummary</paidCashFlowGrouping>

</AccountingModelConfig>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package

 xmlns="http://soap.sforce.com/2006/04/metadata">

 <types>

  <members>ModelConfigOne</members>

  <name>AccountingModelConfig</name>

 </types>

 <version>57.0</version>

</Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types ActionLinkGroupTemplate ActionLinkGroupTemplate

Represents the action link group template. Action link templates let you reuse action link definitions and package and distribute action
links. An action link is a button on a feed element. Clicking on an action link can take a user to another Web page, initiate a file download,
or invoke an API call to an external server or Salesforce. Use action links to integrate Salesforce and third-party services into the feed.
Every action link belongs to an action link group and action links within the group are mutually exclusive.

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ActionLinkGroupTemplate components have the suffix .actionLinkGroupTemplate and are stored in the

`actionLinkGroupTemplates` folder.

Version

### ActionLinkGroupTemplate components are available in API version 33.0 and later.

Fields

**Field Name** **Field Type** **Description**

`actionLinkTemplates` ActionLinkTemplate Action link templates that are associated with the action link group
on page 272[] template.

```
category

executionsAllowed

```

PlatformAction Required. The location of the action link group within the feed element.
GroupCategory Values are:
(enumeration of

**•** `Primary` —The action link group is displayed in the body of the

type string)

feed element.

**•** `Overflow` —The action link group is displayed in the overflow
menu of the feed element.

### ActionLink Required. The number of times an action link can be executed. Values

ExecutionsAllowed are:
(enumeration of

**•** `Once` —An action link can be executed only once across all users.

type string)

**•** `Once` —An action link can be executed only once across all users.

**•** `OncePerUser` —An action link can be executed only once for
each user.

`hoursUntilExpiration` int

**•** `Unlimited` —An action link can be executed an unlimited number
of times by each user. If the action link’s `actionType` is `Api` or
`ApiAsync`, you can’t use this value.

Required. The number of hours from when the action link group is
created until it's removed from associated feed elements and can no
longer be executed. The maximum value is 8,760.


Metadata Types ActionLinkGroupTemplate

**Field Name** **Field Type** **Description**

`isPublished` boolean

Required. If `true`, the action link group template is published. Action
link group templates shouldn’t be published until at least one action
link template is associated with it.

`name` string Required. The name of the action link group template to use in code.

ActionLinkTemplate

ActionLinkTemplate components are used to create multiple action links that share properties.

**Field Name** **Field Type** **Description**

`actionUrl` string Required. The action link URL. For example, a `Ui` action link URL is a Web page.
A `Download` action link URL is a link to the file to download. `Ui` and

`Download` action link URLs are provided to clients. An `Api` or `ApiAsync`
action link URL is a REST resource. `Api` and `ApiAsync` action link URLs
aren’t provided to clients. Links to Salesforce can be relative. All other links
must be absolute and start with `https://` .

`headers` string Template for the HTTP headers sent when corresponding action links are
invoked. This field can be used only for `Api` and `ApiAsync` action links.

This field can contain context variables and binding variables in the form
`{!Bindings.` _**`key`**_ `}` .

`isConfirmationRequired` boolean Required. If `true`, a confirmation dialog appears before the action is executed.

`isGroupDefault` boolean

`label` string

Required. If `true`, action links derived from this template are the default or
primary action in their action groups. There can be only one default action per
action group.

A custom label to display on the action link button. If none of the `LabelKey`
values make sense for an action link, use a custom label. Set the `LabelKey`
field to `None` and enter a label name in the `Label` field.

`labelKey` string Required. Key for the set of labels to display for these action link states: new,
pending, success, failed. For example, the Approve set contains these labels:

Approve, Pending, Approved, Failed. For a complete list of keys and labels, see
[Action Link Labels in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/connect_appendices_action_links_labels.htm) _Connect REST API Developer Guide_ .

```
linkType

```

ActionLinkType Required. The type of action link. One of these values:
(enumeration of type

**•** `Api` —The action link calls a synchronous API at the action URL. Salesforce

string)

sets the status to `SuccessfulStatus` or `FailedStatus` based
on the HTTP status code returned by your server.

**•** `ApiAsync` —The action link calls an asynchronous API at the action URL.
The action remains in a `PendingStatus` state until a third party makes
a request to `/connect/action-links/` _**`actionLinkId`**_ to set
the status to `SuccessfulStatus` or `FailedStatus` when the
asynchronous operation is complete.

**•** `Download` —The action link downloads a file from the action URL.


Metadata Types ActionLinkGroupTemplate

**Field Name** **Field Type** **Description**

**•** `Ui` —The action link takes the user to a web page at the action URL.

`method` ActionLink Required. HTTP method for the action URL. One of these values:
HttpMethod

**•** `HttpDelete` —Returns HTTP 204 on success. Response body or output
(enumeration of type
class is empty.
string)

**•** `HttpGet` —Returns HTTP 200 on success.

**•** `HttpHead` —Returns HTTP 200 on success. Response body or output
class is empty.

**•** `HttpPatch` —Returns HTTP 200 on success or HTTP 204 if the response
body or output class is empty.

**•** `HttpPost` —Returns HTTP 201 on success or HTTP 204 if the response
body or output class is empty. Exceptions are the batch posting resources
and methods, which return HTTP 200 on success.

**•** `HttpPut` —Return HTTP 200 on success or HTTP 204 if the response body
or output class is empty.

`Ui` and `Download` action links must use `HttpGet` .

`position` int Required. An integer specifying the position of the action link template relative
to other action links in the group. 0 is the first position.

`requestBody` string Template for the HTTP request body sent when corresponding action links are
invoked. This field can be used only for `Api` and `ApiAsync` action links.

This field can contain context variables and binding variables in the form
`{!Bindings.` _**`key`**_ `}` .

`userAlias` string If you selected `CustomUser` or `CustomExcludedUser` for
`UserVisibility`, this field is the alias for the custom user. Use the alias

in a template binding to specify the custom user when an action link group is
created using the template.

```
userVisibility

```

ActionLink Required. Who can see the action link. This value is set per action link, not per
UserVisibility action link group. Values are:
(enumeration of type

**•** `Creator` —Only the creator of the action link can see the action link.

string)

**•** `Creator` —Only the creator of the action link can see the action link.

**•** `Everyone` —Everyone can see the action link.

**•** `EveryoneButCreator` —Everyone but the creator of the action link
can see the action link.

**•** `Manager` —Only the manager of the creator of the action link can see
the action link.

**•** `CustomUser` —Only the custom user can see the action link.

**•** `CustomExcludedUser` —Everyone but the custom user can see the
action link.


Metadata Types ActionLinkGroupTemplate

Declarative Metadata Sample Definition

The following is an example of an ActionLinkGroupTemplate component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ActionLinkGroupTemplate xmlns="http://soap.sforce.com/2006/04/metadata">

     <actionLinkTemplates>

       <actionUrl>/services/data/{!Bindings.word}/chatter/feed-elements</actionUrl>

       <headers>Content-Type:{!Bindings.word3}</headers>

       <isConfirmationRequired>true</isConfirmationRequired>

       <isGroupDefault>true</isGroupDefault>

       <labelKey>Add</labelKey>

       <linkType>API</linkType>

       <method>httpPost</method>

       <position>0</position>

       <requestBody>{"body":{"messageSegments":[{"type": "Text",

       "text": "{!Bindings.word1}"}]},"subjectId": "{!Bindings.word2}",

       "feedElementType": "feedItem"}</requestBody>

       <userAlias>customExcludedUser</userAlias>

       <userVisibility>CustomExcludedUser</userVisibility>

     </actionLinkTemplates>

     <category>Primary</category>

     <executionsAllowed>OncePerUser</executionsAllowed>

     <hoursUntilExpiration>10</hoursUntilExpiration>

     <isPublished>true</isPublished>

     <name>MyPackage</name>

   </ActionLinkGroupTemplate>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ActionLinkGroupTemplate</name>

      </types>

      <version>33.0</version>

   </Package>

```

Usage

If you modify action link group templates, you overwrite the related action link templates.

If you delete a published action link group template, you delete all related action link information which includes deleting all action links
that were instantiated using the template from feed items.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types ActionPlanTemplate ActionPlanTemplate

Represents the instance of an action plan template.

Parent Type

This type extends the Metadata metadata type and inherits its fullName field.

File Suffix and Directory Location

### ActionPlanTemplate components have the suffix .apt and are stored in the actionPlanTemplates folder.

Version

Action Plan Template components are available in API version 47.0 and later.

Special Access Rules

To create or access action plan templates, you must have the Customize Application permission and the IndustriesActionPlans license.

Fields

**Field Name** **Field Type** **Description**

### actionPlanTemplateItem ActionPlanTemplateItem The instance of an item on an action plan template version.

on page 276

### actionPlanTemplateItemDependencies ActionPlanTemplateItemDependency[] Defines the dependencies between action plan template items. Available

on page 277 in API version 59.0 and later.

```
actionPlanType

```

### ActionPlanTemplateType Type of the action plan template. Valid values are:

(enumeration of

**•** `Industries`

type string)

**•** `Industries`

**•** `Retail`

**•** `ITSM` —Available in API version 65.0 and later.

**•** `PrvdEngmtCompliance`

**•** `KAM`

Available in API version 63.0 and later.

`category` string Category for this action plan template. Available in API version 64.0 and
later.

`description` string The description of the action plan template.

`estimatedCompletionDays` int Estimated number of days required to complete the action plan. Available
in API version 64.0 and later.


Metadata Types ActionPlanTemplate

**Field Name** **Field Type** **Description**

`fileBasedTemplatePath` string File path for a file-based action plan template. Available in API version
64.0 and later.

`isAdHocItemCreationEnabled` boolean

Required. Indicates whether ad hoc item creation is enabled for this
action plan template ( `true` ) or not ( `false` ). Available in API version
59.0 and later.

`name` string Required. The name of the action plan template.

`ParentTemplateId` reference

The ID of the parent Action Plan Template record. This field is a
relationship field to the ParentTemplate and refers to
ActionPlanTemplate. Available in API version 66.0 and later.

`sourceType` string Source type of the action plan template. Available in API version 64.0
and later.

`status` string Status of the action plan template. Available in API version 64.0 and later.

`subcategory` string Subcategory for this action plan template. Available in API version 64.0
and later.

`targetEntityType` string Required. The parent object this action plan template relates to.
Supported parent objects are Account, BusinessMilestone, Campaign,

Case, Claim, Contact, Contract, InsurancePolicy, InsurancePolicyCoverage,
Lead, Opportunity, PersonLifeEvent, and Visit and custom objects with
activities enabled.

`uniqueName` string Required. The unique identifier for this action plan template record.

ActionPlanTemplateItem

Represents the instance of an item on an action plan template version.

**Field Name** **Field Type** **Description**

`actionPlanTemplateItemValue` ActionPlanTemplateItemValue The value associated with the action plan template item.
on page 277

`displayOrder` int The order in which this item is displayed within the action plan template version.

`isRequired` boolean Indicates whether the task created from this template item is required.

`itemEntityType` string Required. The name of the field on the action plan template item that this value
is for. Available in API version 48.0 and later.

`name` string Required. The name of the action plan template item.

`uniqueName` string Required. The unique identifier for this action plan template item record.


Metadata Types ActionPlanTemplate

ActionPlanTemplateItemDependency

Represents a dependency between action plan template items, defining the sequential relationship and creation timing of items. Available
in API version 59.0 and later.

**Field Name** **Field Type** **Description**

`creationType` string Required. Defines how the dependent item is created in the action plan.

`name` string Required. Name of the dependency relationship.

`previousTemplateItem` ActionPlanTemplateItem Required. Reference to the prerequisite template item that must be completed
on page 276 before the dependent item begins.

`templateItem` ActionPlanTemplateItem Required. Reference to the dependent template item that relies on the
on page 276 completion of the previous item.

ActionPlanTemplateItemValue

Represents the value associated with an action plan template item.

**Field Name** **Field Type** **Description**

`itemEntityType` string Required. The name of the field on the action plan template item that this value
is for. Available in API version 48.0 and later.

`name` string Required. The name of the action plan template item value.

`valueFormula` string The formula for this action plan template item.

`valueLiteral` string The value for this action plan template item.

Declarative Metadata Sample Definition

The following is an example of an ActionPlanTemplate component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ActionPlanTemplate xmlns="http://soap.sforce.com/2006/04/metadata">

      <actionPlanTemplateItem>

        <actionPlanTemplateItemValue>

           <name>Subject</name>

           <valueLiteral>APT 01 Account Packaging APTI 01</valueLiteral>

           <itemEntityType>Task</itemEntityType>

        </actionPlanTemplateItemValue>

        <actionPlanTemplateItemValue>

           <name>Priority</name>

           <valueLiteral>Normal</valueLiteral>

           <itemEntityType>Task</itemEntityType>

        </actionPlanTemplateItemValue>

        <actionPlanTemplateItemValue>

           <name>ActivityDate</name>

           <valueFormula>StartDate + 10</valueFormula>

           <itemEntityType>Task</itemEntityType>

```


Metadata Types ActionPlanTemplate

```
        </actionPlanTemplateItemValue>

        <displayOrder>1</displayOrder>

        <isRequired>true</isRequired>

        <itemEntityType>Task</itemEntityType>

        <name>APT 01 Account Packaging APTI 01</name>

   <uniqueName>APT_01_Account_Packaging_APTI_01_2827f387_9dbc_11e9_920a_e95716848ddd</uniqueName>

      </actionPlanTemplateItem>

      <actionPlanTemplateItem>

        <actionPlanTemplateItemValue>

           <name>Subject</name>

           <valueLiteral>APT 01 Account Packaging APTI 02</valueLiteral>

           <itemEntityType>Task</itemEntityType>

        </actionPlanTemplateItemValue>

        <actionPlanTemplateItemValue>

           <name>Priority</name>

           <valueLiteral>Normal</valueLiteral>

           <itemEntityType>Task</itemEntityType>

        </actionPlanTemplateItemValue>

        <actionPlanTemplateItemValue>

           <name>ActivityDate</name>

           <valueFormula>StartDate + 10</valueFormula>

           <itemEntityType>Task</itemEntityType>

        </actionPlanTemplateItemValue>

        <displayOrder>1</displayOrder>

        <isRequired>true</isRequired>

        <itemEntityType>Task</itemEntityType>

        <name>APT 01 Account Packaging APTI 02</name>

   <uniqueName>APT_01_Account_Packaging_APTI_02_3430da7b_9dbc_11e9_920a_b5d3292906c3</uniqueName>

      </actionPlanTemplateItem>

      <actionPlanTemplateItem>

        <actionPlanTemplateItemValue>

           <name>Subject</name>

           <valueLiteral>APT 01 Account Packaging APTI 03</valueLiteral>

           <itemEntityType>Task</itemEntityType>

        </actionPlanTemplateItemValue>

        <actionPlanTemplateItemValue>

           <name>Priority</name>

           <valueLiteral>Normal</valueLiteral>

           <itemEntityType>Task</itemEntityType>

        </actionPlanTemplateItemValue>

        <actionPlanTemplateItemValue>

           <name>ActivityDate</name>

           <valueFormula>StartDate + 10</valueFormula>

           <itemEntityType>Task</itemEntityType>

        </actionPlanTemplateItemValue>

        <displayOrder>1</displayOrder>

        <isRequired>true</isRequired>

        <itemEntityType>Task</itemEntityType>

        <name>APT 01 Account Packaging APTI 03</name>

```


Metadata Types ActionPlanTemplate

```
   <uniqueName>APT_01_Account_Packaging_APTI_03_2d0363d9_9dbc_11e9_920a_219a003f176d</uniqueName>

      </actionPlanTemplateItem>

      <actionPlanTemplateItemDependencies>

        <name>APT Task Dependency</name>

        <creationType>OnPreviousItemCompleted</creationType>

        <previousTemplateItem>

           <actionPlanTemplateItemValue>

             <name>Subject</name>

               <valueLiteral>APT 01 Account Packaging APTI 01</valueLiteral>

               <itemEntityType>Task</itemEntityType>

             </actionPlanTemplateItemValue>

             <actionPlanTemplateItemValue>

               <name>Priority</name>

               <valueLiteral>Normal</valueLiteral>

               <itemEntityType>Task</itemEntityType>

             </actionPlanTemplateItemValue>

             <actionPlanTemplateItemValue>

               <name>ActivityDate</name>

               <valueFormula>StartDate + 10</valueFormula>

               <itemEntityType>Task</itemEntityType>

           </actionPlanTemplateItemValue>

           <displayOrder>1</displayOrder>

           <isRequired>true</isRequired>

           <itemEntityType>Task</itemEntityType>

           <name>APT 01 Account Packaging APTI 01</name>

   <uniqueName>APT_01_Account_Packaging_APTI_01_2827f387_9dbc_11e9_920a_e95716848ddd</uniqueName>

        </previousTemplateItem>

        <templateItem>

           <actionPlanTemplateItemValue>

           <name>Subject</name>

           <valueLiteral>APT 01 Account Packaging APTI 02</valueLiteral>

           <itemEntityType>Task</itemEntityType>

           </actionPlanTemplateItemValue>

           <actionPlanTemplateItemValue>

             <name>Priority</name>

             <valueLiteral>Normal</valueLiteral>

             <itemEntityType>Task</itemEntityType>

           </actionPlanTemplateItemValue>

           <actionPlanTemplateItemValue>

             <name>ActivityDate</name>

             <valueFormula>StartDate + 10</valueFormula>

             <itemEntityType>Task</itemEntityType>

           </actionPlanTemplateItemValue>

           <displayOrder>1</displayOrder>

           <isRequired>true</isRequired>

           <itemEntityType>Task</itemEntityType>

           <name>APT 01 Account Packaging APTI 02</name>

   <uniqueName>APT_01_Account_Packaging_APTI_02_3430da7b_9dbc_11e9_920a_b5d3292906c3</uniqueName>

        </templateItem>

```


### Metadata Types ActionableListDefinition

```
      </actionPlanTemplateItemDependencies>

      <description>APT 01 Account Packaging Description</description>

      <name>APT 01 Account Packaging</name>

      <targetEntityType>Account</targetEntityType>

      <actionPlanType>Industries</actionPlanType>

     <uniqueName>APT_01_Account_Packaging_0c9e8b15_9dbc_11e9_920a_8d6ecf990219</uniqueName>

      <isAdHocItemCreationEnabled>false</isAdHocItemCreationEnabled>

      <category>Onboarding</category>

      <subcategory>OnBoarding Product</subcategory>

      <estimatedCompletionDays>4</estimatedCompletionDays>

      <sourceType>Migrated From SandBox</sourceType>

      <fileBasedTemplatePath>Action Plan Template</fileBasedTemplatePath>

      <status>Draft</status>

   </ActionPlanTemplate>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ActionPlanTemplate</name>

      </types>

      <version>47.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/file_based.htm)

### ActionableListDefinition

Represents the data source definition details associated with an actionable list.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ActionableListDefinition components have the suffix .actionableListDefinition and are stored in the

`actionableListDefinitions` folder.


Metadata Types ActionableListDefinition

Version

ActionableListDefinition components are available in API version 57.0 and later.

Fields

**Field Name** **Description**

```
actionableListDatasetColumns

actionableListMemberStatuses

batchCalcJobDefinition

datasetName

edgeMart

isActive

masterLabel

```

**Field Type**

ActionableListDatasetColumn[]

**Description**
The object that stores columns in a dataset associated with an actionable list.

**Field Type**

ActionableListMemberStatus[]

**Description**
The object that stores the status and the corresponding status icon details of an
individual actionable list member.

**Field Type**
string

**Description**
The batch calculation job definition that's associated with the creation of an actionable
list. This field is a relationship field.

**Field Type**
string

**Description**
The name of the dataset that is associated with the actionable list.

**Field Type**
string

**Description**
The edgemart dataset that's associated with the actionable list. Available in API version
58.0 and later.

**Field Type**
boolean

**Description**
Indicates whether the actionable list definition is active ( `true` ) or not ( `false` ).

The default value is `false` .

**Field Type**
string


Metadata Types ActionableListDefinition

**Field Name** **Description**

**Description**

Required.

The master label of the actionable list definition.

```
objectName

```

**Field Type**
string

**Description**

Required.

The object for which the actionable list is created.

Possible values are organized by the API version in which they were introduced. Values
are available in all versions after introduction unless noted otherwise.

Possible values are:

API version 60.0 and later:

```
  PersonLifeEvent

```

API version 60.0 and later with Insurance Managed Package:

**•** `Claim`

**•** `InsurancePolicy`

**•** `Quote`

API version 59.0 and later with Health Cloud:

**•** `CareFacilityBed`

**•** `CareRequest`

**•** `CareRequestItem`

**•** `CareServiceVisit`

**•** `CareServiceVisitPlan`

**•** `ClinicalServiceRequest`

API version 59.0 and later with Loyalty Cloud:

**•** `LoyaltyProgramMember`

API version 59.0 and later:

**•** `Case`

API version 58.0 and later with Automotive Cloud:

**•** `Vehicle`

API version 58.0 and later:

**•** `Asset`

**•** `Lead`

**•** `Opportunity`

API version 57.0 and later:


Metadata Types ActionableListDefinition

**Field Name** **Description**

**•** `Account`

**•** `Contact`

ActionableListDatasetColumn

Represents the information about the columns in a dataset associated with an actionable list.

**Table 2: Fields**

**Field Name** **Description**

```
dataDomain

dataType

```

**Field Type**
DatasetColumnDataType (enumeration of type string)

**Description**
The data domain that is mapped to the data type of the dataset column.

Possible values are:

**•** `Dates`

**•** `Dimensions`

**•** `Measures`

**Field Type**
DatatableDataType (enumeration of type string)

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The data type of the dataset column in the actionable list. Available in API version 58.0 and
later.

Possible values are:

**•** `Boolean`

**•** `Currency`

**•** `Date`

**•** `DateTime`

**•** `Email`

**•** `Location`

**•** `Number`

**•** `Percent`

**•** `Phone`

**•** `Text`

**•** `Url`


Metadata Types ActionableListDefinition

**Field Name** **Description**

```
displayOrder

isDefault

isGroupedByListDefObj

IsTypeAheadSearchEnabled

objectName

```

**Field Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order in which the actionable list dataset columns are displayed. Available in API version
58.0 and later.

**Field Type**
boolean

**Description**
Indicates whether the dataset column is added to the actionable list by default ( `true` ) or
not ( `false` ).

The default value is `false` .

**Field Type**
boolean

**Description**
Indicates whether the dataset column is grouped by the object defined in the actionable
list definition ( `true` ) or not ( `false` ). Available in API version 59.0 and later.

**Field Type**
boolean

**Description**
Indicates whether the type-ahead search for filters is enabled ( `true` ) or not ( `false` ).
Available in API version 60.0 and later.

**Field Type**
string

**Description**
The name of the object that's associated with the dataset column.

Possible values are:

API version 60.0 and later:

```
  PersonLifeEvent

```

API version 60.0 and later with Insurance Managed Package:

**•** `Claim`

**•** `InsurancePolicy`

**•** `Quote`

API version 59.0 and later with Health Cloud:

**•** `CareFacilityBed`


Metadata Types ActionableListDefinition

**Field Name** **Description**

**•** `CareRequest`

**•** `CareRequestItem`

**•** `CareServiceVisit`

**•** `CareServiceVisitPlan`

**•** `ClinicalServiceRequest`

API version 59.0 and later with Loyalty Cloud:

**•** `LoyaltyProgramMember`

API version 59.0 and later:

**•** `Case`

API version 58.0 and later with Automotive Cloud:

**•** `Vehicle`

API version 58.0 and later:

**•** `Asset`

**•** `Lead`

**•** `Opportunity`

API version 57.0 and later:

**•** `Account`

**•** `Contact`

```
sourceColumnApiName

sourceFieldName

```

**Field Type**
string

**Description**
The API name of the column in the source dataset.

**Field Type**
string

**Description**
The name of the field in the object for which the actionable list dataset is created.

ActionableListMemberStatus

Represents the status and the corresponding status icon details of an individual actionable list member.

**Table 3: Fields**

**Field Name** **Description**

```
iconName

```

**Field Type**
string


Metadata Types ActionableListDefinition

**Field Name** **Description**

**Description**
The name of the icon that's mapped to the status.

```
status

```

**Field Type**
string

**Description**
The status of the actionable list member.

Declarative Metadata Sample Definition

The following is an example of a ActionableListDefinition component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ActionableListDefinition

 xmlns="http://soap.sforce.com/2006/04/metadata">

 <actionableListDatasetColumns>

  <isDefault>true</isDefault>

  <sourceFieldName>NewColumn1</sourceFieldName>

 </actionableListDatasetColumns>

 <actionableListDatasetColumns>

  <sourceColumnApiName>ApiName</sourceColumnApiName>

  <dataDomain>Dimensions</dataDomain>

  <isDefault>false</isDefault>

  <sourceFieldName>NewColumn2</sourceFieldName>

  <objectName>Account</objectName>

  <displayOrder>1</displayOrder>

  <dataType>Text</dataType>

 </actionableListDatasetColumns>

 <actionableListMemberStatuses>

  <iconName>NewMember1</iconName>

  <status>Active</status>

 </actionableListMemberStatuses>

 <isActive>true</isActive>

 <masterLabel>NewMember2</masterLabel>

 <objectName>Account</objectName>

 <isProtected>true</isProtected>

 <batchCalcJobDefinition>Test1</batchCalcJobDefinition>

 <datasetName>AccountDef</datasetName>

</ActionableListDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

  <types>

    <members>*</members>

    <name>ActionableListDefinition</name>

  </types>

```


### Metadata Types AdvAccountForecastSet

```
     <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### AdvAccountForecastSet

Represents the forecast sets that define the forecast configurations for each business unit or different groups of accounts. With separate
forecast sets at account or business unit level, you can focus on account-specific data and manage configuration updates for one business
unit without impacting any other business unit’s data.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### AdvAccountForecastSet components have the suffix .advAccountForecastSet and are stored in the AdvAccountForecastSet folder.

Version

### AdvAccountForecastSet components are available in API version 53.0 and later.

Special Access Rules

The advanced account forecasting feature setting for Manufacturing Cloud is required to create an advanced account forecast set.

Fields

**Field Name** **Description**

```
accountFieldName

calculationFrequency

```

**Field Type**
string

**Description**
The field name for the account in the advanced account forecast fact record.

**Field Type**
AdvAcctFcstCalcFrequency (enumeration of type string)

**Description**
The frequency at which the forecast set is recalculated automatically.


Metadata Types AdvAccountForecastSet

**Field Name** **Description**

Possible values are:

**•** `Monthly`

**•** `Quarterly`

**•** `Weekly`

**•** `Yearly`

The default value is `Monthly` .

```
description

dimensions

displayGroups

forecastAdjPeriods

forecastFactObjectName

forecastFormulas

```

**Field Type**
string

**Description**
The description of the advanced account forecast set record.

**Field Type**

AdvAcctForecastDimension[]

**Description**
The dimensions selected for an advanced account forecast set to categorize the forecast
data.

**Field Type**

AdvAcctFrcstDisplayGroup[]

**Description**
The information about the groups for the advanced account forecast set measures or
dimensions.

**Field Type**

AdvAcctForecastAdjPeriod[]

**Description**
The details about the adjustment period of the advanced account forecast values.

**Field Type**
string

**Description**

Required.

The API name of the object that contains the advanced forecast fact records.

**Field Type**

AdvAccountForecastFormula[]

**Description**
The formulas based on which forecast values are calculated.


Metadata Types AdvAccountForecastSet

**Field Name** **Description**

```
forecastPeriodGroupName

forecastQuantityFieldName

forecastRevenueFieldName

forecastSetFieldName

forecastSetName

forecastStatusFieldName

generationDpeDefName

measureDefinitions

```

**Field Type**
string

**Description**

Required.

The name of the advanced account forecast period group record.

**Field Type**
string

**Description**
The field name for the forecast quantity in the advanced account forecast fact record.

**Field Type**
string

**Description**
The field name for the forecast revenue in the advanced account forecast record.

**Field Type**
string

**Description**
The field name for the Forecast Set ID in the advanced account forecast fact record.

**Field Type**
string

**Description**

Required.

The name of the advanced account forecast set record.

**Field Type**
string

**Description**
The field name for the status in the advanced account forecast fact record.

**Field Type**
string

**Description**
The name of the data processing engine (DPE) definition that’s used to generate
advanced account forecast fact records.

**Field Type**

AdvAcctForecastMeasureDef[]


Metadata Types AdvAccountForecastSet

**Field Name** **Description**

**Description**
The measures to display in the advanced account forecasts grid for the forecast set.

```
periodFieldName

recalculateDpeDefName

regenerationDpeDefName

rolloverDpeDefName

rolloverFrequency

status

```

**Field Type**
string

**Description**
The field name for the period in the advanced account forecast fact record.

**Field Type**
string

**Description**
The name of the data processing engine definition that’s used to recalculate the
advanced account forecast fact records.

**Field Type**
string

**Description**
The name of the data processing engine definition that’s used to regenerate the
advanced account forecast fact records.

**Field Type**
string

**Description**
The data processing engine definition that’s used to generate the rollover advanced
account forecast fact records.

**Field Type**
AdvAcctFcstCalcFrequency (enumeration of type string)

**Description**
The frequency of rollover of the advanced account forecast records.

Possible values are:

**•** `Monthly`

**•** `Quarterly`

**•** `Weekly`

**•** `Yearly`

The default value is `Monthly` .

**Field Type**
AdvAccForecastSetStatus (enumeration of type string)

**Description**

Required.


Metadata Types AdvAccountForecastSet

**Field Name** **Description**

The status of the advanced account forecast set.

Possible values are:

**•** `Active`

**•** `Inactive`

AdvAccountForecastFormula

Represents the formulas that are used to calculate forecast values in real time after applying the DPE calculations. For example, processing
forecast rollover for all accounts at the start of a month.

**Field Name** **Description**

```
endPeriod

formulaExpression

formulaType

startPeriod

```

**Field Type**
int

**Description**

Required.

The period until when the forecast formula is applicable.

**Field Type**
string

**Description**

Required.

The formula based on which forecast values are calculated.

**Field Type**
AdvAcctFcstFormulaType (enumeration of type string)

**Description**

Required.

Specifies the calculation type for the formula.

Possible values are:

**•** `QUANTITY`

**•** `REVENUE`

The default value is `QUANTITY` .

**Field Type**
int

**Description**

Required.

The period from when the forecast formula is applicable.


Metadata Types AdvAccountForecastSet

AdvAcctForecastAdjPeriod

Represents details about the adjustment period of the advanced account forecast values.

**Field Name** **Description**

```
adjustmentDayCount

frequency

profileName

startDay

```

**Field Type**
int

**Description**

Required.

The number of days during which you can make forecast adjustments.

**Field Type**
PeriodTypes (enumeration of type string)

**Description**

Required.

The frequency that’s applicable to make any forecast adjustments.

Possible values are:

**•** `Month`

**•** `Quarter`

**•** `Week`

**•** `Year`

The default value is `Month` .

**Field Type**
string

**Description**
The name of the profile with which you can adjust the forecast set.

**Field Type**
int

**Description**

Required.

The start date for forecast adjustments.

AdvAcctForecastDimension

Represents the dimensions selected for an advanced account forecast set to categorize the data. For example, a business unit requires
forecast data for each account aggregated by product and ship-from location.


Metadata Types AdvAccountForecastSet

**Field Name** **Description**

```
advAcctForecastDimName

dimensionFieldName

dimensionSourceName

hierarchySequenceNumber

```

**Field Type**
string

**Description**

Required.

The name of the advanced account forecast dimension.

**Field Type**
string

**Description**

Required.

The API name of the field for the dimension in the custom object that contains the
generated advanced account forecast records.

**Field Type**
string

**Description**
The name of the dimension source associated with the advanced account forecast set
dimension record.

**Field Type**
int

**Description**

Required.

The sequence number of the dimension source associated with the forecast set.

AdvAcctForecastMeasureDef

Represents information about the measures to display in the advanced account forecasts grid for the forecast set.

**Field Name** **Description**

```
advAcctForecastMeasureDefName

aggregationType

```

**Field Type**
string

**Description**

Required.

The name of the definition for the advanced account forecast measure.

**Field Type**
AdvAcctFcstAggregationType (enumeration of type string)


Metadata Types AdvAccountForecastSet

**Field Name** **Description**

**Description**

Required.

The type of aggregation that’s used for calculating the advanced account forecast
values.

Possible values are:

**•** `AVERAGE`

**•** `MAXIMUM`

**•** `MINIMUM`

**•** `SUM`

The default value is `SUM` .

```
computationMethod

forecastDataMeasureName

forecastMeasureName

forecastMeasureType

```

**Field Type**
AdvAcctFcstComputationMethod (enumeration of type string)

**Description**

Required.

The method that’s used for calculating the advanced account forecast values.

Values are:

**•** `CUSTOM`

**•** `DATA_PROCESSING_ENGINE_DEFINITION`

**•** `FORMULA`

The default value is `DATA_PROCESSING_ENGINE_DEFINITION` .

**Field Type**
string

**Description**

Required.

The field of the facts object used for the advanced account forecast measure.

**Field Type**
string

**Description**

Required.

The name for the advanced account forecast measure to show on UI.

**Field Type**
AdvAcctFcstMeasureType (enumeration of type string)

**Description**

Required.


Metadata Types AdvAccountForecastSet

**Field Name** **Description**

The measure type that’s used for the generated advanced forecast values.

Possible values are:

**•** `QUANTITY`

**•** `REVENUE`

The default value is `QUANTITY` .

```
isAdjustmentTracked

```

**Field Type**
boolean

**Description**
Indicates whether the adjustments made to the advanced account forecast values for
this metric are tracked ( `true` ) or not ( `false` ).

AdvAcctFrcstDisplayGroup

Represents information about the groups for the advanced account forecast set measures or dimensions.

**Field Name** **Description**

```
advAcctFrcstDisplayGroupName

displayGroupItems

displayGroupType

isDefault

```

**Field Type**
string

**Description**

Required.

The name of the advanced account forecast display group.

**Field Type**

AdvAcctFrcstDplyGroupItem[]

**Description**
The items associated with a display group for an advanced account forecast set.

**Field Type**
AdvAcctFrcstDisplayGroupType (enumeration of type string)

**Description**
The category of the display group.

Possible value is:

**•** `MEASURE`

**Field Type**
boolean

**Description**
Indicates whether the display group is the default group ( `true` ) or not ( `false` ).


Metadata Types AdvAccountForecastSet

**Field Name** **Description**

```
userProfileName

```

**Field Type**
string

**Description**
The name of the profile for which the display group is applicable.

AdvAcctFrcstDplyGroupItem

Represents information about the items associated with a display group for an advanced account forecast set.

**Field Name** **Description**

```
advAcctFrcstDplyGroupItemName

displayOrder

measureReferenceName

```

**Field Type**
string

**Description**

Required.

The name of the advanced account forecast display group that’s associated with the
group item.

**Field Type**
int

**Description**

Required.

The display order of the display group item.

**Field Type**
string

**Description**
The ID of the measure associated with the display group item.

Declarative Metadata Sample Definition

The following is an example of an AdvAccountForecastSet component.

```
<?xml version="1.0" encoding="UTF-8"?>

<AdvAccountForecastSet xmlns="http://soap.sforce.com/2006/04/metadata"

xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

   <calculationFrequency>Quarterly</calculationFrequency>

   <forecastAdjPeriods>

     <adjustmentDayCount>5</adjustmentDayCount>

     <frequency>Quarter</frequency>

     <profileName xsi:nil="true"/>

     <startDay>1</startDay>

```


Metadata Types AdvAccountForecastSet

```
      </forecastAdjPeriods>

      <forecastFormulas>

        <endPeriod>12</endPeriod>

        <formulaExpression>6</formulaExpression>

        <startPeriod>2</startPeriod>

        <formulaType>QUANTITY</formulaType>

      </forecastFormulas>

      <forecastPeriodGroupName>PeriodGroup1</forecastPeriodGroupName>

      <accountFieldName>Account</accountFieldName>

      <periodFieldName>Period</periodFieldName>

      <forecastQuantityFieldName>ForecastedQuantity</forecastQuantityFieldName>

      <forecastRevenueFieldName>ForecastedRevenue</forecastRevenueFieldName>

      <forecastFactObjectName>AdvAccountForecastFact</forecastFactObjectName>

      <forecastSetFieldName>AdvAcctForecastSetPartner</forecastSetFieldName>

      <rolloverFrequency>Monthly</rolloverFrequency>

      <forecastStatusFieldName>Status</forecastStatusFieldName>

      <description>sample forecast set</description>

      <regenerationDpeDefName xsi:nil="true"/>

      <rolloverDpeDefName xsi:nil="true"/>

      <recalculateDpeDefName xsi:nil="true"/>

      <generationDpeDefName xsi:nil="true"/>

      <status>Inactive</status>

      <forecastSetName>Forecast Set 1</forecastSetName>

      <dimensions>

        <dimensionFieldName>Account</dimensionFieldName>

        <dimensionSourceName>DimSource1</dimensionSourceName>

        <hierarchySequenceNumber>1</hierarchySequenceNumber>

        <advAcctForecastDimName>DimensionName</advAcctForecastDimName>

      </dimensions>

      <measureDefinitions>

        <forecastDataMeasureName>MeasureName</forecastDataMeasureName>

        <advAcctForecastMeasureDefName>Sample Def Name</advAcctForecastMeasureDefName>

        <isAdjustmentTracked>true</isAdjustmentTracked>

        <forecastMeasureName>Samplemeasure name</forecastMeasureName>

        <aggregationType>MINIMUM</aggregationType>

        <computationMethod>DATA_PROCESSING_ENGINE_DEFINITION</computationMethod>

        <forecastMeasureType>QUANTITY</forecastMeasureType>

      </measureDefinitions>

      <displayGroups>

        <advAcctFrcstDisplayGroupName>Sample Measure Group</advAcctFrcstDisplayGroupName>

        <displayGroupType>MEASURE</displayGroupType>

        <isDefault>false</isDefault>

        <userProfileName xsi:nil="true"/>

        <displayGroupItems>

          <advAcctFrcstDplyGroupItemName>Sample Quantity</advAcctFrcstDplyGroupItemName>

           <measureReferenceName>Sample Def Name</measureReferenceName>

           <displayOrder>1</displayOrder>

        </displayGroupItems>

      </displayGroups>

   </AdvAccountForecastSet>

```


### Metadata Types AffinityScoreDefinition

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>AdvAccountForecastSet</name>

      </types>

     <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### AffinityScoreDefinition

Represents the affinity information used in calculations to analyze and categorize contacts for marketing purposes.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

### AffinityScoreDefinition components have the suffix .affinityScoreDefinition and are stored in the

`affinityScoreDefinitions` folder.

Version

### AffinityScoreDefinition components are available in API version 66.0 and later.

Special Access Rules

This metadata type is available only if the Fundraising Access license is enabled for the org and the Fundraising admin permission is
assigned to users.

Fields

**Field Name** **Description**

```
affinityScoreDefinitionDesc

```

**Field Type**
string


Metadata Types AffinityScoreDefinition

**Field Name** **Description**

**Description**
Description of the affinity score definition.

```
affinityScoreDefinitionName

affinityScoreType

masterLabel

numberOfMonths

numberOfRanges

scoreRangeList

```

**Field Type**
string

**Description**
Name of the affinity score definition.

**Field Type**
AffinityScoreType (enumeration of type string)

**Description**
Type of the affinity score that’s defined.

Valid values are:

**•** `CAP` —Capacity, Ability, Propensity (CAP)

**•** `RFM` —Recency, Frequency, Monetary (RFM)

The default value is `RFM` .

**Field Type**
string

**Description**
Label for this affinity score definition value. This display value is the internal label that
doesn't get translated.

**Field Type**
int

**Description**
Number of months to analyze the records for calculating the affinity score.

**Field Type**
int

**Description**

Required.

Number of ranges to use in the calculation, ranging from 0 to 9. Provide the
corresponding range list values in the `scoreRangeList` field.

**Field Type**
string

**Description**

Required.


Metadata Types AffinityScoreDefinition

**Field Name** **Description**

Ranges that are referenced in the affinity score calculation. This field is used with
`scoreRangeList` . For example, to calculate RFM with `numberOfRanges` value
as 3, provide the values for the `scoreRangeList` field in this format.

```
                       {

                         "R ranges":"0-30, 31-100, 100+",

                         "F ranges":"0-10, 11-100, 100+",

                         "M ranges":"0-1000, 1001-5000, 5000+"

                       }

```

```
sourceFieldApiNameList

sourceObjectApiNameList

targetFieldApiNameList

targetObjectApiName

```

**Field Type**
string

**Description**

Required.

API names of the source fields that are referenced in the score calculation.

**Field Type**
string

**Description**
API names of the source objects that are referenced in the score calculation.

**Field Type**
string

**Description**

Required.

API names of the target fields where the calculated scores are added.

**Field Type**
string

API name of the target object where the calculated scores are added.

Declarative Metadata Sample Definition

This example shows a sample of an AffinityScoreDefinition component.

```
<?xml version="1.0" encoding="UTF-8"?>

<AffinityScoreDefinition

 xmlns="http://soap.sforce.com/2006/04/metadata">

 <affinityScoreDefinitionDesc>RFM Affinity Score</affinityScoreDefinitionDesc>

 <affinityScoreDefinitionName>AffinityScoreDefinition_RFM</affinityScoreDefinitionName>

 <affinityScoreType>RFM</affinityScoreType>

 <masterLabel>MasterLabel</masterLabel>

 <numberOfMonths>12</numberOfMonths>

 <numberOfRanges>3</numberOfRanges>

```


Metadata Types AffinityScoreDefinition

```
    <scoreRangeList>

        [

         {

           "name": "R Ranges",

           "direction": "ascending",

           "ranges": [30,90,180]

         },

         {

           "name": "F Ranges",

           "direction": "descending",

           "ranges": [10,15,100]

         },

         {

           "name": "M Ranges",

           "direction": "descending",

           "ranges": [500,1000,5000]

         }

      ]

       </scoreRangeList>

    <sourceFieldApiNameList>

        [

         {

           "name": "R Source",

           "values":

             [

              {

               "fieldName": "DonorGiftSummary.DaysSinceLastGift",

               "fieldWeight": 1

              }

             ]

         },

         {

           "name": "F Source",

           "values":

             [

              {

               "fieldName": "DonorGiftSummary.GiftCount",

               "fieldWeight": 1

              }

             ]

         },

         {

           "name": "M Source",

           "values":

             [

              {

               "fieldName": "DonorGiftSummary.TotalGiftsCount",

               "fieldWeight": 1

              }

             ]

         }

        ]

       </sourceFieldApiNameList>

    <targetFieldApiNameList>

```


Metadata Types AffinityScoreDefinition

```
        [

         {

           "name": "R Target",

           "values":

             [

              {

               "fieldName": "DonorGiftSummary.RecencyScore",

               "fieldWeight": 1

              }

             ]

         },

         {

           "name": "F Target",

           "values":

             [

              {

               "fieldName": "DonorGiftSummary.FrequencyScore",

               "fieldWeight": 1

              }

             ]

         },

         {

           "name": "M Target",

           "values":

             [

              {

               "fieldName": "DonorGiftSummary.MonetaryScore",

               "fieldWeight": 1

              }

             ]

         }

        ]

       </targetFieldApiNameList>

   </AffinityScoreDefinition>

```

This example shows a sample of the `package.xml` file that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>AffinityScoreDefinition</name>

      </types>

      <version> 66.0 </version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/file_based_zip_file.htm)


### Metadata Types AIApplication AIApplication

Represents an instance of an AI application. For example, Einstein Prediction Builder.

This type extends the Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### AIApplication components have the suffix .ai and are stored in the aiApplications folder.

Version

### AIApplication is available in API version 50.0 and later.

Fields

**Field Name** **Field Type** **Description**

`developerName` string Required. Represents the name of the application. Can contain only underscores
and alphanumeric characters and must be unique in your org. It must begin

with a letter, not include spaces, not end with an underscore, and not contain
two consecutive underscores.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

`masterLabel` string Label that identifies the AI application throughout the Salesforce user interface.

```
status

type

```

### AIApplicationStatus Required. The status of the application. Valid values are:

(enumeration of type

**•** `Disabled`

string)

**•** `Enabled`

**•** `Migrated`

### AIApplicationType The type of AI application. Valid values are:

(enumeration of type

**•** `PredictionBuilder`

string)

**•** `Disabled`

**•** `Draft`

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types AIApplicationConfig AIApplicationConfig

Additional prediction information related to an AI application. This type extends the Metadata metadata type and inherits its `fullName`
field.

File Suffix and Directory Location

### AIApplicationConfig components have the suffix .aiapplicationconfig and are stored in the aiApplicationConfigs

folder.

Version

### AIApplicationConfig is available in API version 50.0 and later.

Fields

**Field Name** **Field Type** **Description**

`aiApplicationDeveloperName` string Required. Represents the AIApplication to which AIApplicationConfig belongs.
Can contain only underscores and alphanumeric characters and must be unique

in your org. It must begin with a letter, not include spaces, not end with an
underscore, and not contain two consecutive underscores. Available in API
version 51.0 and later.

`applicationId` string Required. The ID of the parent AI application.

`developerName` string Represents the name of the application config. Can contain only underscores
and alphanumeric characters and must be unique in your org. It must begin

with a letter, not include spaces, not end with an underscore, and not contain
two consecutive underscores.

`insightReasonEnabled` boolean Required. When `true`, generates the predictors, or field values, that were
used to generate the prediction value.

`masterLabel` string Required. Label that identifies the AI application configuration throughout the
Salesforce user interface.

`rank` int Required. Reserved for future use.

```
scoringMode

```

AIScoringMode Required. Frequency with which the prediction scores are written back. Valid
(enumeration of type values are:
string)

**•** `Batch`

**•** `OnDemand`

**•** `Streaming`


### Metadata Types AiAuthoringBundle

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### AiAuthoringBundle

Represents an AI authoring bundle, which is a container for AI-related authoring content. For example, an AI authoring bundle for an
Agentforce agent contains an Agent Script file and the associated metadata content.

### AiAuthoringBundle packages and manages AI authoring artifacts with version control features. This metadata type provides a structured

way to organize, version, and target AI-related content within your Salesforce org.

Parent Type

This type extends the Metadata metadata type.

Directory Structure

### AiAuthoringBundle agents are stored in an aiAuthoringBundles folder with a specific structure. Here’s an example of the structure.

```
   +--aiAuthoringBundles

      +--my_service_agent (1)

        +--my_service_agent.agent (2)

        +--my_service_agent.bundle-meta.xml (3)

      +--my_employee_agent (1)

        +--my_employee_agent.agent (2)

        +--my_employee_agent.bundle-meta.xml (3)

```

The bundle includes the following resources:

**•** A folder (1) for each agent. If the folder suffix contains an underscore followed by a number (for example, `my_service_agent_5` ),
that number indicates the agent version. If there isn't a number in the suffix, the agent definition applies to the latest version of the
agent.

**•** [Each agent folder contains a file that defines the agent (2). For example, this file can be an Agent Script definition. See Agent Script](https://developer.salesforce.com/docs/einstein/genai/guide/get-started.html)
[in the Agentforce Developer Guide for details.](https://developer.salesforce.com/docs/einstein/genai/guide/get-started.html)

**•** Each agent folder contains the metadata associated with the agent (3). Be sure to review the description for the `target` field to
understand how to distinguish committed agent versions from uncommitted versions.

Version

### AiAuthoringBundle is available in API version 65.0 and later.


Metadata Types AiAuthoringBundle

Fields

**Field Name** **Description**

```
bundleType

target

versionDescription

versionTag

```

**AiAuthoringBundleType (enumeration of type string)**

**Description**
Specifies the type or category of the AI authoring bundle, indicating the kind of AI
authoring content contained within the bundle. Currently, this value must be

`AGENT` [, which represents an Agent Script agent. See Agent Script in the Agentforce](https://developer.salesforce.com/docs/einstein/genai/guide/get-started.html)
[Developer Guide for details.](https://developer.salesforce.com/docs/einstein/genai/guide/get-started.html)

**string**

**Description**

Specifies the context or destination for the AI authoring bundle, defining how the
bundle content should be applied or deployed.

To commit an agent version, Agentforce agents must specify the
`developerName` for the Bot on page 489 and BotVersion on page 510
components, separated by a period: `{Bot}.{BotVersion}` . For example,
`Agentforce_Service_Agent.v2` . These two components tie the AI
authoring bundle to a specific agent and a specific agent version.

[This field is automatically populated when you publish an agent with Agentforce](https://developer.salesforce.com/docs/einstein/genai/guide/agent-dx.html)
[DX. Publishing an agent with this field present is the equivalent to committing the](https://developer.salesforce.com/docs/einstein/genai/guide/agent-dx.html)
agent in Agentforce Builder with the **Commit Version** button.

If you want to deploy an agent to your org in draft state, omit this field.

**string**

**Description**
Provides a human-readable description of the bundle version, documenting what
changes or features are included in this version of the AI authoring bundle.

**string**

**Description**
Defines a version identifier or tag for the AI authoring bundle. This value can be
used for version tracking and management of different bundle iterations.

Declarative Metadata Sample Definition

The following `package.xml` file is an example of an AiAuthoringBundle component.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>New_Agent</members>

     <name>AiAuthoringBundle</name>

   </types>

```


### Metadata Types AiEvaluationDefinition

```
      <version>65.0</version>

   </Package>

```

In the `.zip` file for this bundle, each agent is nested in the `aiAuthoringBundles` folder. This example shows the directory
structure in the `.zip` file for an agent named `New_Agent` . Each agent bundle folder must contain an agent file and a metadata file.

```
   +--aiAuthoringBundles

      +--New_Agent

        +--New_Agent.agent

        +--New_Agent.bundle-meta.xml

```

[To see an example of an Agent Script agent file, see Agent Script in the Agentforce Developer Guide.](https://developer.salesforce.com/docs/einstein/genai/guide/get-started.html)

This example shows the metadata XML for the agent in the file `New_Agent.bundle-meta.xml` . The example commits the agent
version because it contains a `target` value. Uncommitted versions don't contain this field.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <AiAuthoringBundle xmlns="http://soap.sforce.com/2006/04/metadata">

      <bundleType>AGENT</bundleType>

      <target>Agentforce_Service_Agent.v2</target>

      <versionTag>DF 2026.3</versionTag>

   </AiAuthoringBundle>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### AiEvaluationDefinition

Represents an agent evaluation, including subject metadata and a set of test cases.

In Metadata API, you can create test definitions, including specifying inputs and expected outcomes, and deploy them to different orgs.
In Connect API, you can execute test scenarios, poll for results, and retrieve test outcomes.

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/metadata.htm) `fullName` [field. For more information on testing agents, see the Testing](https://developer.salesforce.com/docs/einstein/genai/guide/testing-api.html)
[API Developer Guide.](https://developer.salesforce.com/docs/einstein/genai/guide/testing-api.html)

File Suffix and Directory Location

### AiEvaluationDefinition components have the suffix .aiEvaluationDefinition and are stored in the

`aiEvaluationDefinitions` folder.

Version

### AiEvaluationDefinition is available in API version 63.0 and later. Individual fields may have specific minimum API version requirements

as noted in the field descriptions.

Special Access Rules

### AiEvaluationDefinition is available only if Agentforce is enabled. See Set Up Agents in Salesforce Help.


Metadata Types AiEvaluationDefinition

Fields

**Field Name** **Description**

```
description

name

```

**string**

**Description**
The
purpose

of the
test.

**string**

**Description**
Required.
The

API
name
of the
test.
Can
contain
only
underscores
and
alphanumeric
characters
and
must
be
unique
in your
org. It
must
begin
with a
letter,
not
include
spaces,
not
end
with
an
underscore,
and
not
contain
two


Metadata Types AiEvaluationDefinition

**Field Name** **Description**

consecutive
underscores.

```
subjectName

subjectType

```

**string**

**Description**
Required.
A

unique
identifier
for the
agent
being
tested.
Make
sure
that
this
identifier
matches
the API
name
of the
agent,
which
you
can
find on
the
agent
details
page
in
Setup.

**string**

**Description**
Required.
The

type of
subject
being
tested.
The
only
currently
supported


Metadata Types AiEvaluationDefinition

**Field Name** **Description**

value
is
`AGENT` .

```
subjectVersion

testCase

```

AiEvaluationTestCase

Represents a test case.

**string**

**Description**
The
agent

version
to test.
If not
provided,
the
latest
active
version
is used
by
default.
You
can
find
the
version
in the
BotVersion
metadata
type.

**AiEvaluationTestCase[]**
**on page**
**310**

**Description**
A list
of test
cases.


Metadata Types AiEvaluationDefinition

**Field Name** **Description**

```
expectation

inputs

number

```

AiEvaluationExpectation

Represents the expected outcome for a test case.

**AiEvaluationExpectation[]**
**on page**
**311**

**Description**
The
criteria

used
to test
the
artifact's
responses.

**AiEvaluationAgentTestCaseInput[]**
**on page**
**324**

**Description**
The
specific

input
provided
to the
artifact
being
tested.

**int**

**Description**
The
unique

number
for the
test
case. If
not
provided,
the
value
is
automaticay **l**
calculated.


Metadata Types AiEvaluationDefinition

**Field Name** **Description**

```
expectedValue

label

```

**string**

**Description**
The
expected

outcome
of the
test.
The
format
of this
field
depends
on the
value
of the
name
field.
The
expected
outcome
is
compared
against
the
response
generated
when
you
run
the
test
using
[Connect](https://developer.salesforce.com/docs/einstein/genai/guide/testing-api-connect.html)
[REST](https://developer.salesforce.com/docs/einstein/genai/guide/testing-api-connect.html)
[API](https://developer.salesforce.com/docs/einstein/genai/guide/testing-api-connect.html)

**string**

**Description**
An
optional

label
for an
expectation.
Typically
added
when


Metadata Types AiEvaluationDefinition

**Field Name** **Description**

using
the
same
custom
expectation
name
multiple
times
in a
test
case. If
provided,
this
label
appears
in the
test
results;
otherwise,
the
expectation
name
appears.

```
name

```

**string**

**Description**
Required.
The

expectation
name.
Valid
values
are:

**•** `topic_sequence_match` :
The

```
   expectedValue
```

field
value
is
a
string
represe **n** tig
the
topic
that
the


Metadata Types AiEvaluationDefinition

**Field Name** **Description**

agent
is
expected
to
use,
such
as
**`O`** `TBSingl` **`e`** `RcordSu` **`m`** `ary` .
For
a
list
of
agent
topics,
see
Standard
Agent
Topic
R **e** frence
in
Salesforce
Help.

**•** `action_sequence_match` :
The

```
                          expectedValue
```

field
value
is
a

```
                          string[]
```

represe **n** tig
a
list
of
actions
that
you
expect
the
artifact
to
take
during
the
test,
such
as


Metadata Types AiEvaluationDefinition

**Field Name** **Description**

```
                          ['IdentifyRecordByName',
```

`'action2']` .
For
a
list
of
agent
actions,
see
Standard
Agent
Action
R **e** frence
in
Salesforce
Help.
This
option
was
previously
caed **l**
`action_sequence_match` .

**•** `bot_response_rating` :
The

```
                          expectedValue
```

field
value
is
a
string
represe **n** tig
the
expected
response
gen **e** ratd
by
the
artifact,
such
as

```
                          Su m arization

                          of

                          the

                          Global

                          Media
```

`account` .


Metadata Types AiEvaluationDefinition

**Field Name** **Description**

**•** `coherence` :
A
gen **e** ratd
answer
is
coh **e** rnt
if
it’s
easy
to
understand
and
has
no
grammatical
e **r** ors.
If
you
use
this
quality
check,
you
don't
need
an

```
                          expectedValue
```

field
value.

**•** `completene` **`s`** :
A
gen **e** ratd
answer
is
compl **e** t
if
it
includes
all
the
e **s** ential
information.
If
you
use
this
quality


Metadata Types AiEvaluationDefinition

**Field Name** **Description**

check,
you
don't
need
an

```
                          expectedValue
```

field
value.

**•** `concisene` **`s`** :
A
gen **e** ratd
answer
is
concise
if
it's
brief
but
compreh **e** nsiv.
Shorter
is
be **t** er.
If
you
use
this
quality
check,
you
don't
need
an

```
                          expectedValue
```

field
value.

**•** `output_latency_mi` **`l`** `iseconds` :
Latency
in
milliseconds
from
sending
a
request
until
a
response
is


Metadata Types AiEvaluationDefinition

**Field Name** **Description**

received.
If
you
use
this
quality
check,
you
don't
need
an

```
                          expectedValue
```

field
value.

**•** `string_comparison` :
A
custom
evaluation
criteria
that
tests
a
response
for
a
specified
string
value.

**•** `numeric_comparison` :
A
custom
evaluation
criteria
that
tests
a
response
for
a
specified
numeric
value.


Metadata Types AiEvaluationDefinition

**Field Name** **Description**

```
parameter

```

**AiEvaluationTestCaseCritParam[]**
**on page**
**319**

**Description**
Required
for

custom
test
criteria.
An
array
of
parameters
for the
specific
custom
criteria
defined
by
`expectation.name` .
This
field
replaces

```
  expectedValue
```

for
custom
test
criteria.

AiEvaluationTestCaseCritParam

Defines a criterion parameter for expectations, including name, value, and whether it references another value. Available in API version
64.0 and later.

**Field Name** **Description**

```
isReference

```

**boolean**

**Description**
If
`true`,

indicates
that
value
is a

```
  JSONPath

```


Metadata Types AiEvaluationDefinition

**Field Name** **Description**

expression
referencing
runtime
data
from
the

```
                        generatedData
```

object
returned
by the
Get
Test
Results
resource.
If
`true`,
the
value
must
be a

```
                        JSONPath
```

string.
The
default
value
is
`false` .

```
name

```

**string**

**Description**
Required
for

custom
evaluation
criteria.
The
name
of the
parameter
required
by the
evaluation.
Valid
values
are:
`operator` —type
of


Metadata Types AiEvaluationDefinition

**Field Name** **Description**

comparison;
`actual` —runtime
value
to
evaluate;
`expected` —arge **t**
value
to
compare
against.
For
`operator`,
valid
options
include:

**•** `equals` :
Checks
if
the

```
                          actual
```

value
exactly
matches
the

```
                          expected
```

value
(string
or
numeric).

**•** `contains` :
Checks
if
the

```
                          actual
```

string
contains
the

```
                          expected
```

string.

**•** `startswith` :
Checks
if
the

```
                          actual
```

string
begins


Metadata Types AiEvaluationDefinition

**Field Name** **Description**

with
the

```
                          expected
```

string.

**•** `endswith` :
Checks
if
the

```
                          actual
```

string
ends
with
the

```
                          expected
```

string.

**•** `greater_than_or_equal` :
Checks
if
the
numeric

```
                          actual
```

value
is
greater
than
or
equal
to
the
numeric

```
                          expected
```

value
( `>=` ).

**•** `greater_than` :
Checks
if
the
numeric

```
                          actual
```

value
is
greater
than
the
numeric


Metadata Types AiEvaluationDefinition

**Field Name** **Description**

```
                          expected
```

value
( `>` ).

**•** `less_than` :
Checks
if
the
numeric

```
                          actual
```

value
is
less
than
the
numeric

```
                          expected
```

value
( `<` ).

**•** `le` **`s`** `_than_or_equal` :
Checks
if
the
numeric

```
                          actual
```

value
is
less
than
or
equal
to
the
numeric

```
                          expected
```

value
( `<=` ).

```
value

```

**string**

**Description**
Required
for

custom
evaluation
criteria.
The


Metadata Types AiEvaluationDefinition

**Field Name** **Description**

value
for the
parameter.
This
field
can be
a literal
value
or a

```
                        JSONPath
```

expression
if

```
                        isReference
```

is
`true` .
Typically,
JSONPath
expressions
are
used
to
dynamica **l** y
retrieve

```
                        actual
```

parameters.

AiEvaluationAgentTestCaseInput

Represents the inputs for a test case, including variables, conversation history, and the utterance.

**Field Name** **Description**

```
contextVariable

```

**AiEvalCopilotTestCaseCntxtVar[]**
**on page**
**325**

**Description**
An
XML

array
of
context
variables
sent to
the
agent.


Metadata Types AiEvaluationDefinition

**Field Name** **Description**

```
conversationHistory

utterance

```

**AiEvalCopilotTestCaseConv[]**
**on page**
**326**

**Description**
An
XML

array
of
conversation
history
elements
sent to
the
agent.

**string**

**Description**
Required.
The

request
sent to
the
agent.

AiEvalCopilotTestCaseCntxtVar

An XML array of context variables sent to the agent.

**Field Name** **Description**

```
variableName

variableValue

```

**string**

**Description**
Required.
The

name
of the
context
variable.

**string**

**Description**
Required.
The

value


Metadata Types AiEvaluationDefinition

**Field Name** **Description**

of the
context
variable.

AiEvalCopilotTestCaseConv

An XML array of conversation history sent to the agent.

**Field Name** **Description**

```
index

message

role

```

**integer**

**Description**
A zero
based

index
for this
conversation
message.

**string**

**Description**
The
text

from
the
user or
agent.

**string**

**Description**
The
role

associated
with a
message.
Valid
values
are

```
  user
```

or
`agent` .
A
conversation
must


Metadata Types AiEvaluationDefinition

**Field Name** **Description**

begin
with a
message
from
the
`user` .

```
topic

```

**string**

**Description**
Required
for

```
  agent
```

messages.
Represents
the
topic
the
agent
used
to
generate
a
response.

Declarative Metadata Sample Definition

Here's an example of an AiEvaluationDefinition component.

```
<?xml version="1.0" encoding="UTF-8"?>

<AiEvaluationDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

   <description>My Sample Tests</description>

   <name>my_test_n1</name>

   <subjectName>Agentforce_for_Salesforce</subjectName>

   <subjectType>AGENT</subjectType>

   <subjectVersion>v1</subjectVersion>

   <testCase>

     <number>1</number>

     <inputs>

      <utterance>Summarize the Global Media account</utterance>

     </inputs>

     <expectation>

        <name>topic_sequence_match</name>

        <expectedValue>OOTBSingleRecordSummary</expectedValue>

     </expectation>

     <expectation>

        <name>action_sequence_match</name>

        <expectedValue>['IdentifyRecordByName']</expectedValue>

     </expectation>

```


### Metadata Types AIScoringModelDefinition

```
        <expectation>

           <name>bot_response_rating</name>

           <expectedValue>Summarization of the Global Media account</expectedValue>

        </expectation>

        <expectation>

           <name>conciseness</name>

        </expectation>

      </testCase>

      <testCase>

        <number>2</number>

        <inputs>

         <utterance>give me a pizza recipe</utterance>

        </inputs>

        <expectation>

           <name>topic_sequence_match</name>

           <expectedValue>Small_Talk</expectedValue>

        </expectation>

        <expectation>

           <name>action_sequence_match</name>

           <expectedValue>[]</expectedValue>

        </expectation>

        <expectation>

           <name>bot_response_rating</name>

           <expectedValue>the agent cannot answer this</expectedValue>

        </expectation>

      </testCase>

   </AiEvaluationDefinition>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### AIScoringModelDefinition

Represents information about a machine learning model that’s used by the Scoring Framework for Industries Cloud Einstein. The machine
learning model is used for scoring, including its configuration.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### AIScoringModelDefinition components have the suffix .aiScoringModelDefinition and are stored in the

`aiScoringModelDefinitions` folder.


Metadata Types AIScoringModelDefinition

Version

AIScoringModelDefinition components are available in API version 58.0 and later.

Special Access Rules

To access this metadata type, you must have the AI Accelerator User permission set with Scoring Framework enabled for Industries Cloud
Einstein from Salesforce Setup. The Salesforce org must have the CRM Plus license and the product’s CRM license.

Fields

**Field Name** **Description**

```
aiModelConfig

aiScoringModelDefVersions

description

masterLabel

```

**Field Type**
string

**Description**

Required.

ID of an AI model configuration related to the AI scoring model record.

**Field Type**

AIScoringModelDefVersion[]

**Description**
Represents information of various versions of a model.

**Field Type**
string

**Description**
Description for an AIScoringModelDefinition record.

**Field Type**
string

**Description**

Required.

A user-friendly name for the AIScoringModelDefinition metadata component, which
is defined when the AIScoringModelDefinition metadata component is created.

AIScoringModelDefVersion

Represents information about a version of an AI scoring model.


Metadata Types AIScoringModelDefinition

**Field Name** **Description**

```
aiScoringModelDefinition

aiScoringSteps

developerName

masterLabel

modelMode

```

**Field Type**
string

**Description**

Required.

Parent AIScoringModelDefinition record that’s related to an AIScoringModelDefVersion
record.

**Field Type**

AIScoringStep[]

**Description**
Represents information about a step associated with an AI scoring model version.

**Field Type**
string

**Description**

Required.

The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with a
letter, not include spaces, not end with an underscore, and not contain two consecutive
underscores. In managed packages, this field prevents naming conflicts on package
installations. With this field, a developer can change the object’s name in a managed
package and the changes are reflected in a subscriber’s organization. Label is **Record**
**Type Name** .

**Field Type**
string

**Description**

Required.

A user-friendly name for the AIScoringModelDefVersion component name, which is
defined when the AIScoringModelDefVersion component name is created.

**Field Type**
AIScoringModelDefVersionMode (enumeration of type string)

**Description**

Required.

Mode of an AI scoring model.

Values are:

**•** `DEPLOY`

**•** `TRAIN`

**•** `TRAIN_AND_DEPLOY`


Metadata Types AIScoringModelDefinition

AIScoringStep

Represents information about a step associated with an AI scoring model version. For example, an AI scoring step can include steps,
such as propensity to purchase products or prediction scores for accounts.

**Field Name** **Description**

```
aiModelConfigStep

stepDetail

```

**Field Type**
string

**Description**

Required.

ID of the AI model config step that’s related to the AIScoringStep record.

**Field Type**
string

**Description**
Scoring step details in JSON format.

Declarative Metadata Sample Definition

Here’s an example of an AIScoringModelDefinition component.

```
<?xml version="1.0" encoding="UTF-8"?>

<AIScoringModelDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

   <aiModelConfig>Prediction_Scores_for_Accounts</aiModelConfig>

   <aiScoringModelDefVersions>

     <fullName>V1</fullName>

     <aiScoringModelDefinition>Test</aiScoringModelDefinition>

     <aiScoringSteps>

<aiModelConfigStep>Prediction_Scores_for_Accounts.GrainSelector</aiModelConfigStep>

        <stepDetail>{label:Account,name:Account}</stepDetail>

     </aiScoringSteps>

     <aiScoringSteps>

<aiModelConfigStep>Prediction_Scores_for_Accounts.AugmentedDataset</aiModelConfigStep>

     </aiScoringSteps>

     <aiScoringSteps>

<aiModelConfigStep>Prediction_Scores_for_Accounts.TargetConditionBuilder</aiModelConfigStep>

       <stepDetail>{specificOutcomeDefined:Yes,label:Financial accounts are associated

 with an account,name:FA_Target}</stepDetail>

     </aiScoringSteps>

     <aiScoringSteps>

<aiModelConfigStep>Prediction_Scores_for_Accounts.InputVariableSelector</aiModelConfigStep>

```


### Metadata Types AIUsecaseDefinition

```
        </aiScoringSteps>

        <aiScoringSteps>

   <aiModelConfigStep>Prediction_Scores_for_Accounts.CustomFilter</aiModelConfigStep>

        </aiScoringSteps>

        <aiScoringSteps>

   <aiModelConfigStep>Prediction_Scores_for_Accounts.WriteBackConnector</aiModelConfigStep>

        </aiScoringSteps>

        <developerName>V1</developerName>

        <masterLabel>V1</masterLabel>

        <modelMode>TRAIN_AND_DEPLOY</modelMode>

      </aiScoringModelDefVersions>

      <description>Test for metadata</description>

      <masterLabel>Test</masterLabel>

   </AIScoringModelDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>AIScoringModelDefVersion</name>

      </types>

      <types>

        <members>*</members>

        <name>AIScoringModelDefinition</name>

      </types>

      <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### AIUsecaseDefinition

Represents a collection of fields in your Salesforce org used to define a machine learning use case and get real-time predictions.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types AIUsecaseDefinition

File Suffix and Directory Location

AIUsecaseDefinition components have the suffix `.aiUsecaseDefinitions` and are stored in the `aiUsecaseDefinitions`
folder.

Version

AIUsecaseDefinition components are available in API version 56.0 and later.

Special Access Rules

The AIUsecaseDefinition object is available when the admin settings for AI Accelerator and for the product related to the use case are
enabled. The Salesforce org must have the CRM Plus license and the product’s CRM license.

Fields

**Field Name** **Description**

```
aiUsecaseFieldMappings

aiUsecaseModels

creatorType

masterLabel

```

**Field Type**

AIUsecaseFieldMapping[]

**Description**
The field mappings for the use case definition. Each use case definition can have
multiple field mappings.

**Field Type**

AIUsecaseModel[]

**Description**
The models for the use case definition. Each use case definition can have multiple use
case models.

**Field Type**
CreatorType (enumeration of type string)

**Description**
Required.

The type of user who created the use case definition that's used by AI Accelerator.
Valid values are:

**•** `INTERNAL_USER`

**•** `SALESFORCE_ADMIN`

Available in API version 57.0 and later.

**Field Type**
string

**Description**

Required.


Metadata Types AIUsecaseDefinition

**Field Name** **Description**

A user-friendly name for the use case definition, which is defined when the use case
definition is created.

```
maximumInsightCount

maximumRecommendationCount

maximumSuggestionCount

primaryResponseObject

recommendationResponseObject

recommendationSource

secondaryResponseObject

```

**Field Type**
int

**Description**
The maximum number of insights returned by the scoring response.

**Field Type**
int

**Description**
The maximum number of recommendations returned by the Next Best Action Strategy.

**Field Type**
int

**Description**
The maximum number of suggestions returned by the scoring response.

**Field Type**
string

**Description**
The primary object in which the scoring response is stored based on the specified field
mapping.

**Field Type**
string

**Description**
The recommendation response object associated with the use case definition.

**Field Type**
RcmdSourceType (enumeration of type string)

**Description**
The tool or platform that generates recommendations. Valid values are:

**•** `Next_Best_Action_Flow`

**•** `None`

Available in API version 57.0 and later.

**Field Type**
string

**Description**
The object in which the scoring response is stored based on the specified field mapping.


Metadata Types AIUsecaseDefinition

**Field Name** **Description**

```
shouldSaveFeatures

shouldSaveInsights

shouldSaveRecommendation

shouldSaveRequestResponse

shouldSaveScore

shouldSaveSuggestions

suggestionImpactMinimumPct

```

**Field Type**
boolean

**Description**
Indicates whether to save the features extracted for the scoring request ( `true` ) or not
( `false` ).

The default value is `false` .

**Field Type**
boolean

**Description**
Indicates whether to save the prediction insights that are used to generate the score
( `true` ) or not ( `false` ).

The default value is `false` .

**Field Type**
boolean

**Description**
Indicates whether to save the recommendation ( `true` ) or not ( `false` ).

The default value is `false` .

**Field Type**
boolean

**Description**
Indicates whether to save the request response ( `true` ) or not ( `false` ).

The default value is `false` .

**Field Type**
boolean

**Description**
Indicates whether to save the prediction score ( `true` ) or not ( `false` ).

The default value is `false` .

**Field Type**
boolean

**Description**
Indicates whether to save the suggestions for improving the prediction score ( `true` )
or not ( `false` ).

The default value is `false` .

**Field Type**
int


Metadata Types AIUsecaseDefinition

**Field Name** **Description**

**Description**
The minimum eligible percentage for improving the existing prediction score based
on the suggestions. Suggestions with an impact greater than the specified percentage
on the score are displayed on the prediction scorecard.

```
usecaseName

```

AIUsecaseFieldMapping

**Field Type**
string

**Description**

Required.

The name of the use case definition.

Represents information about the field mapping to store extracted features, prediction scores, prediction insights, and use case suggestions
in the response object.

**Field Name** **Description**

```
developerName

mappedFieldName

mappedFieldType

```

**Field Type**
string

**Description**
The unique name for the field mapping in the use case definition.

Required. The unique name of the object in the API. This name can contain only
underscores and alphanumeric characters, and must be unique in your org. It must
begin with a letter, not include spaces, not end with an underscore, and not contain
two consecutive underscores. In managed packages, this field prevents naming conflicts
on package installations. With this field, a developer can change the object’s name in
a managed package and the changes are reflected in a subscriber’s organization. Label
is **Record Type Name** .

**Field Type**
string

**Description**

Required.

The name of the field where the scoring response is stored.

**Field Type**
MappedFieldType (enumeration of type string)

**Description**

Required.

The type of the mapped field.


Metadata Types AIUsecaseDefinition

**Field Name** **Description**

Valid values are:

**•** `FEATURE`

**•** `PREDICTION_SCORE`

**•** `INSIGHT`

**•** `SUGGESTION`

**•** `SECONDARY_RESPONSE_RECORD_ID`

**•** `RECOMMENDATION_RESPONSE_RECORD_ID`

**•** `RECOMMENDATION`

The default value is `FEATURE` .

```
masterLabel

responseFieldName

responseObject

sequenceNumber

```

AIUsecaseModel

**Field Type**
string

**Description**

Required.

A user-friendly name for the use case field mapping, which is defined when the field
mapping is created.

**Field Type**
string

**Description**

Required.

The name of the response object’s field that’s mapped to the field storing the score.

**Field Type**
string

**Description**

Required.

The object whose field is mapped to the field storing the score. It’s either the
PrimaryResponseObject or the SecondaryResponseObject specified in the
AIUsecaseDefinition object.

**Field Type**
int

**Description**
The sequence number for the information stored in the field mapping.

Represents information about the machine learning models that generate predictions for your use case.


Metadata Types AIUsecaseDefinition

**Field Name** **Description**

```
aiFeatureExtractors

defaultFeatureExtractor

developerName

masterLabel

predictionDefinition

predictionPlatform

```

**Field Type**

AIFeatureExtractor[]

**Description**
The AI feature extractors to retrieve the input data.

**Field Type**

AIFeatureExtractor

**Description**
The default AI feature extractor to retrieve the input data.

**Field Type**
string

**Description**
The unique name for the use case model.

Required. The unique name of the object in the API. This name can contain only
underscores and alphanumeric characters, and must be unique in your org. It must
begin with a letter, not include spaces, not end with an underscore, and not contain
two consecutive underscores. In managed packages, this field prevents naming conflicts
on package installations. With this field, a developer can change the object’s name in
a managed package and the changes are reflected in a subscriber’s organization. Label
is **Record Type Name** .

**Field Type**
string

**Description**

Required.

A user-friendly name for the use case model, which is defined when the use case
model is created.

**Field Type**
string

**Description**

Required.

The unique identifier of the prediction definition that’s related to the use case model.
This identifier can be an external ID. If you use Einstein Discovery to create models, the
`predictionDefinition` field stores the developer name of the record.

**Field Type**
PredictionPlatform (enumeration of type string)

**Description**

Required.


Metadata Types AIUsecaseDefinition

**Field Name** **Description**

The platform on which the machine learning model is created and deployed. Valid
values are:

**•** `Data_Cloud`

**•** `Default` —For internal use only.

**•** `Einstein_Discovery`

**•** `Einstein_on_Data_Cloud` —Available in API version 63.0 and later.

The default value is `Einstein_Discovery` . Available in API version 57.0 and
later.

AIFeatureExtractor

Represents information about the feature extractor that’s used to retrieve the input data for the use case model that’s used to generate
predictions.

**Field Name** **Description**

```
batchInputSourceIdentifier

batchInputSourceInformation

batchInputSourceType

className

```

**Field Type**
string

**Description**
The identifier of the input source of the features computed by batch jobs, which can
be used by a model for generating predictions. Available in API version 57.0 and later.

**Field Type**
string

**Description**
The information about the batch input source, including query parameters, objects,
field mappings, and filter criteria. Available in API version 63.0 and later.

**Field Type**
BatchInputSourceType (enumeration of type string)

**Description**
The input source of the features computed in batch jobs.

Possible values are:

**•** `CRMA`

**•** `Data Cloud`

The default value is `CRMA` .

**Field Type**
string

**Description**

Required.


Metadata Types AIUsecaseDefinition

**Field Name** **Description**

The ID of the Apex class created for the feature extractor.

```
developerName

extractorType

featureInputType

inputContext

```

**Field Type**
string

**Description**
The unique name for the feature extractor.

Required. The unique name of the object in the API. This name can contain only
underscores and alphanumeric characters, and must be unique in your org. It must
begin with a letter, not include spaces, not end with an underscore, and not contain
two consecutive underscores. In managed packages, this field prevents naming conflicts
on package installations. With this field, a developer can change the object’s name in
a managed package and the changes are reflected in a subscriber’s organization. Label
is **Record Type Name** .

**Field Type**
ExtractorType (enumeration of type string)

**Description**

Required.

The type of the feature extractor.

Valid values are:

**•** `APEX`

**•** `JAVA`

**•** `HYBRID`

The default value is `APEX` .

**Field Type**
string

**Description**

Required.

The type of feature input that’s used in generating predictions. Valid values are:

**•** `Realtime_Input`

**•** `Sample_Input`

**•** `Batch_Input`

**•** `Batch_And_Realtime_Input`

Available in API version 57.0 and later.

**Field Type**
string


Metadata Types AIUsecaseDefinition

**Field Name** **Description**

**Description**
The JSON file with features that act as context for the feature extractor. This data can
also include the data in the uploaded CSV file. Available in API version 57.0 and later.

```
masterLabel

```

**Field Type**
string

**Description**

Required.

A user-friendly name for the feature extractor, which is defined when the feature
extractor is created.

Declarative Metadata Sample Definition

The following is an example of an AIUsecaseDefinition component.

```
<?xml version="1.0" encoding="UTF-8"?>

<AIUsecaseDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

   <aiUsecaseFieldMappings>

     <developerName>DevNamee1</developerName>

     <mappedFieldName>Name</mappedFieldName>

     <mappedFieldType>INSIGHT</mappedFieldType>

     <masterLabel>DevName</masterLabel>

     <responseFieldName>AnnualRevenue</responseFieldName>

     <responseObject>Lead</responseObject>

     <sequenceNumber>2</sequenceNumber>

   </aiUsecaseFieldMappings>

   <aiUsecaseFieldMappings>

     <developerName>DevNamee2</developerName>

     <mappedFieldName>Value</mappedFieldName>

     <mappedFieldType>INSIGHT</mappedFieldType>

     <masterLabel>DevName</masterLabel>

     <responseFieldName>Id</responseFieldName>

     <responseObject>Account</responseObject>

     <sequenceNumber>2</sequenceNumber>

   </aiUsecaseFieldMappings>

   <aiUsecaseFieldMappings>

     <developerName>DevNamee3</developerName>

     <mappedFieldName>Score</mappedFieldName>

     <mappedFieldType>PREDICTION_SCORE</mappedFieldType>

     <masterLabel>DevName</masterLabel>

     <responseFieldName>Company</responseFieldName>

     <responseObject>Lead</responseObject>

   </aiUsecaseFieldMappings>

   <aiUsecaseFieldMappings>

     <developerName>DevNamee4</developerName>

     <mappedFieldName>RecordId</mappedFieldName>

     <mappedFieldType>SECONDARY_RESPONSE_RECORD_ID</mappedFieldType>

     <masterLabel>DevName</masterLabel>

```


Metadata Types AIUsecaseDefinition

```
        <responseFieldName>Address</responseFieldName>

        <responseObject>Lead</responseObject>

        <joinFieldInformation>joinFieldInformation</joinFieldInformation>

      </aiUsecaseFieldMappings>

      <aiUsecaseFieldMappings>

        <developerName>DevName5</developerName>

        <mappedFieldName>DevName4</mappedFieldName>

        <mappedFieldType>PREDICTION_SCORE_INPUT</mappedFieldType>

        <masterLabel>DevName</masterLabel>

        <responseFieldName>Address</responseFieldName>

        <responseObject>Lead_Dmo</responseObject>

   <joinFieldInformation>{"recordIdField":"Value2","recordIdObject":"Value1","recordJoinRelation":"Value3"}</joinFieldInformation>

      </aiUsecaseFieldMappings>

      <aiUsecaseFieldMappings>

        <developerName>DevName6</developerName>

        <mappedFieldName>DevName5</mappedFieldName>

        <mappedFieldType>PREDICTION_SCORE_INPUT</mappedFieldType>

        <masterLabel>DevName</masterLabel>

        <responseFieldName>Address</responseFieldName>

        <responseObject>Lead_Dmo</responseObject>

   <joinFieldInformation>{"recordIdField":"Value2","recordIdObject":"Value1","recordJoinRelation":"Value3"}</joinFieldInformation>

   <additionalFieldInformation>{"customPredictionAttributes":[{"id":1,"fieldLabel":"Label

   1","sourceField":"Total_Spend_c__c"},{"id":2,"fieldLabel":"Label

   2","sourceField":"Predicted_Churned2_recommendation_impact__c"}]}</additionalFieldInformation>

        <customPredictionLabel>%%SCORE%%</customPredictionLabel>

      </aiUsecaseFieldMappings>

      <aiUsecaseModels>

        <aiFeatureExtractors>

           <className>01pxx0000004X2CAAU</className>

           <extractorType>APEX</extractorType>

           <developerName>DevNamee2</developerName>

           <masterLabel>DevName</masterLabel>

           <featureInputType>Realtime_Input</featureInputType>

           <inputContext>"{columnNames=[column1, column2], rawData=[S,

   315090]}"</inputContext>

           <batchInputSourceIdentifier>DatasetName</batchInputSourceIdentifier>

           <batchInputSourceType>CRMA</batchInputSourceType>

   <batchInputSourceInformation>{"streamingTransformName":"SDT_Name","recordIdField":"fieldname","featureFieldsMapping":{"feature1":"field1","feature2":"field2"},"streaminTransformLabel":"SDT_Label","batchInputSourceLabel":"DMO_Label"}</batchInputSourceInformation>

        </aiFeatureExtractors>

        <defaultFeatureExtractor>

           <className>01pxx0000004X0aAAE</className>

           <extractorType>APEX</extractorType>

           <developerName>DevNamee1</developerName>

           <masterLabel>DevName</masterLabel>

           <featureInputType>Realtime_Input</featureInputType>

           <inputContext>"{columnNames=[column1, column2], rawData=[S,

```


Metadata Types AIUsecaseDefinition

```
   315090]}"</inputContext>

           <batchInputSourceIdentifier>DatasetName</batchInputSourceIdentifier>

           <batchInputSourceType>CRMA</batchInputSourceType>

   <batchInputSourceInformation>{"streamingTransformName":"SDT_Name","recordIdField":"fieldname","featureFieldsMapping":{"feature1":"field1","feature2":"field2"},"streaminTransformLabel":"SDT_Label","batchInputSourceLabel":"DMO_Label"}</batchInputSourceInformation>

        </defaultFeatureExtractor>

        <developerName>DevNamee1</developerName>

        <masterLabel>DevName</masterLabel>

        <predictionDefinition>PredictionDefinitionD</predictionDefinition>

        <predictionPlatform>Einstein_Discovery</predictionPlatform>

        <arePredctGenInRealTime>true</arePredctGenInRealTime>

      </aiUsecaseModels>

      <aiUsecaseModels>

        <developerName>DevNamee2</developerName>

        <masterLabel>DevName</masterLabel>

        <predictionDefinition>PredictionDefinitionBA</predictionDefinition>

        <predictionPlatform>Einstein_Discovery</predictionPlatform>

        <arePredctGenInRealTime>true</arePredctGenInRealTime>

      </aiUsecaseModels>

      <aiUsecaseModels>

        <developerName>DevNamee3</developerName>

        <masterLabel>DevName</masterLabel>

        <predictionDefinition>PredictionDefinitionCA</predictionDefinition>

        <predictionPlatform>Einstein_Discovery</predictionPlatform>

        <arePredctGenInRealTime>true</arePredctGenInRealTime>

      </aiUsecaseModels>

      <aiUsecaseModels>

        <developerName>DevName4</developerName>

        <masterLabel>DevName</masterLabel>

        <predictionDefinition>Model1</predictionDefinition>

        <predictionPlatform>Data_Cloud</predictionPlatform>

        <arePredctGenInRealTime>false</arePredctGenInRealTime>

      </aiUsecaseModels>

      <aiUsecaseModels>

        <developerName>DevName5</developerName>

        <masterLabel>DevName</masterLabel>

        <predictionDefinition>Model1</predictionDefinition>

        <predictionPlatform>Einstein_on_Data_Cloud</predictionPlatform>

        <arePredctGenInRealTime>false</arePredctGenInRealTime>

      </aiUsecaseModels>

      <masterLabel>DevName</masterLabel>

      <maximumInsightCount>3</maximumInsightCount>

      <maximumSuggestionCount>3</maximumSuggestionCount>

      <maximumRecommendationCount>3</maximumRecommendationCount>

      <primaryResponseObject>Lead</primaryResponseObject>

      <secondaryResponseObject>Account</secondaryResponseObject>

      <recommendationResponseObject>Contact</recommendationResponseObject>

      <shouldSaveFeatures>true</shouldSaveFeatures>

      <shouldSaveInsights>true</shouldSaveInsights>

      <shouldSaveRecommendation>false</shouldSaveRecommendation>

      <shouldSaveRequestResponse>false</shouldSaveRequestResponse>

      <shouldSaveScore>true</shouldSaveScore>

      <shouldSaveSuggestions>true</shouldSaveSuggestions>

```


### Metadata Types AnalyticsDashboard

```
      <suggestionImpactMinimumPct>50</suggestionImpactMinimumPct>

      <usecaseName>FTestSampleMLUsecase</usecaseName>

      <recommendationSource>Next_Best_Action_Flow</recommendationSource>

      <creatorType>INTERNAL_USER</creatorType>

   </AIUsecaseDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>*AIUsecaseDefinition*</name>

      </types>

      <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### AnalyticsDashboard

Represents a Tableau Next dashboard.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### AnalyticsDashboard components have the suffix .uadash and are stored in the analyticsDashboards folder.

Version

### AnalyticsDashboard components are available in API version 64.0 and later.

Limits

**Definition** **Limit**

The maximum number of AnalyticsDashboard 50
components in a single deploy operation.


Metadata Types AnalyticsDashboard

**Definition** **Limit**

The maximum number of AnalyticsDashboard 100
components in a single retrieve operation.

The maximum number of AnalyticsDashboard 100
components across all deploy operations in
a 24-hour window.

The maximum number of AnalyticsDashboard 200
components across all retrieve operations in
a 24-hour window.

Fields

**Field Name** **Description**

```
analyticsWorkspace

description

lastDraftModifiedDate

lastPublishedDate

layouts

masterLabel

```

**Field Type**
string

**Description**

Required.

The Tableau Next workspace the dashboard belongs to.

**Field Type**
string

**Description**
The description of the dashboard.

**Field Type**
dateTime

**Description**
The date the dashboard draft was last modified.

**Field Type**
dateTime

**Description**
The date the dashboard was last published.

**Field Type**

AnalyticsDashboardLayout[]

**Description**
The layouts for the dashboard. A dashboard has 0 or more layouts.

**Field Type**
string


Metadata Types AnalyticsDashboard

**Field Name** **Description**

**Description**

Required.

The name of the dashboard.

```
style

templateAssetSourceName

templateSource

version

widgets

workspaceAssetRelationships

```

**Field Type**
string

**Description**
The style of the dashboard. This is a JSON string.

Example:

```
  {"widgetStyle":{"backgroundColor":"#ffffff","borderEdges":[],"borderColor":"#cccccc","borderWidth":1,"borderRadius":0}}

```

**Field Type**
string

**Description**
If the dashboard was created from a template, the name of the source dashboard in
the template.

**Field Type**
string

**Description**
If the dashboard was created from a template, the name of the source template.

**Field Type**
double

**Description**
The API version of the dashboard.

**Field Type**

AnalyticsDashboardWidget[]

**Description**
A list of widgets in the dashboard. A dashboard has 0 or more widgets.

**Field Type**

AnalyticsWorkspaceAsset[]

**Description**
A list of analytics assets in the workspace this dashboard is associated with. A dashboard
has 0 or more workspace asset relationships.


Metadata Types AnalyticsDashboard

AnalyticsDashboardLayout

Represents a layout for a Tableau Next dashboard. A dashboard can have multiple layouts, like Desktop and Mobile.

**Field Name** **Description**

```
analyticsDashboard

analyticsDashboardVersion

columnCount

label

layoutName

maxWidth

pages

rowHeight

```

**Field Type**
string

**Description**

Required.

The name of the dashboard the layout is associated with.

**Field Type**
string

**Description**
The version of the dashboard the layout is associated with.

**Field Type**
string

**Description**
The number of columns in the layout.

**Field Type**
string

**Description**
The label for the layout.

**Field Type**
string

**Description**
The name of the layout.

**Field Type**
string

**Description**
The max width of the layout, in pixels.

**Field Type**

AnalyticsDashboardPage[]

**Description**
The pages to display for this dashboard layout. A layout has 0 or more pages.

**Field Type**
string


Metadata Types AnalyticsDashboard

**Field Name** **Description**

**Description**
The row height for layout rows.

```
style

version

```

**Field Type**
string

**Description**
The style for the layout. This is a JSON string.

Example:

```
  {"backgroundColor":"#ffffff","gutterColor":"#f3f3f3","cellSpacingX":8,"cellSpacingY":8

```

**Field Type**
double

**Description**
The API version of the dashboard layout.

AnalyticsDashboardPage

Represents a page in a Tableau Next dashboard.

**Field Name** **Description**

```
index

label

pageName

pageWidgets

```

**Field Type**
int

**Description**
The index of the page in the dashboard. An index of `0` is the first page of the dashboard.
No index is required if there is only the default page of the dashboard.

**Field Type**
string

**Description**
The label for the dashboard page.

**Field Type**
string

**Description**
The generated unique ID for the dashboard page.

**Field Type**

AnalyticsDashPageWidget[]

**Description**
A list of dashboard page widgets. A page has 0 or more page widgets.


Metadata Types AnalyticsDashboard

AnalyticsDashPageWidget

Represents an dashboard page widget for a Tableau Next dashboard page.

**Field Name** **Description**

```
analyticsDashboardWidget

colspan

column

row

rowspan

```

**Field Type**
string

**Description**

Required.

The name of dashboard widget, defined in the list of widgets for the dashboard.

**Field Type**
string

**Description**
The column span for the widget on the page. This is a numeric value.

**Field Type**
string

**Description**
The column the widget is placed in on the page. This is a numeric value.

**Field Type**
string

**Description**
The row the widget is placed in on the page. This is a numeric value.

**Field Type**
string

**Description**
The row span for the widget on the page. This is a numeric value.

AnalyticsDashboardWidget

Represents a widget on a Tableau Next dashboard.

**Field Name** **Description**

```
analyticsDashboard

```

**Field Type**
string

**Description**

Required.

The API name of the dashboard the widget is associated with.


Metadata Types AnalyticsDashboard

**Field Name** **Description**

```
buttonWidgetDefs

containerWidgetDefs

dynamicTokens

filterWidgetDefs

imageWidgetDefs

label

metricWidgetDefs

parameterWidgetDefs

```

**Field Type**

AnalyticsButtonWidgetDef[]

**Description**
The definition for a button widget type. A dashboard has 0 or more button widgets.
Required for button widget.

**Field Type**

AnalyticsContainerWidgetDef[]

**Description**
The definition for a container widget type. A dashboard has 0 or more container
widgets. Required for container widget.

**Field Type**

AnlytDshbrdWdgtDynamicTkn[]

**Description**
The definition for a dynamic widget token. A dashboard has 0 or more dynamic tokens.

**Field Type**

AnalyticsFilterWidgetDef[]

**Description**
The definition for a filter widget type. A dashboard has 0 or more filter widgets. Required
for filter widget.

**Field Type**

AnalyticsImageWidgetDef[]

**Description**
The definition for a image widget type. A dashboard has 0 or more image widgets.
Required for image widget.

**Field Type**
string

**Description**
The label for the widget.

**Field Type**

AnalyticsMetricWidgetDef[]

**Description**
The definition for a metric widget type. A dashboard has 0 or more metric widgets.
Required for metric widget.

**Field Type**

AnalyticsParamWidgetDef[]


Metadata Types AnalyticsDashboard

**Field Name** **Description**

**Description**
The definition for a parameter widget type. A dashboard has 0 or more paramet widgets.
Required for parameter widget.

```
textWidgetDefs

type

vizWidgetDefs

widgetActions

widgetName

```

**Field Type**

AnalyticsTextWidgetDef[]

**Description**
The definition for a text widget type. A dashboard has 0 or more text widgets. Required
for text widget.

**Field Type**
AnalyticsWidgetType (enumeration of type string)

**Description**

Required.

The widget type.

Values are:

**•** `button`

**•** `container`

**•** `extension`

**•** `filter`

**•** `image`

**•** `metric`

**•** `parameter`

**•** `text`

**•** `summary`

**•** `visualization`

**Field Type**

AnalyticsVizWidgetDef[]

**Description**
The definition for a visualization widget type. A dashboard has 0 or more visualization
widgets. Required for visualization widget.

**Field Type**

AnalyticsAssetAction[]

**Description**
The actions for the widget. A widget has 0 or more text widgets.

**Field Type**
string


Metadata Types AnalyticsDashboard

**Field Name** **Description**

**Description**
The API name of the widget. Use this for the `analyticsDashboardWidget`
value in `AnalyticsDashPageWidget` .

AnalyticsAssetAction

Represents an action for a Tableau Next asset.

**Field Name** **Description**

```
actionType

analyticsAssetVerson

eventType

parameters

```

**Field Type**
AnalyticsActionType (enumeration of type string)

**Description**

Required.

The action type.

Values are:

**•** `flow`

**•** `navigate`

**•** `parameter`

**•** `recordaction`

**Field Type**
string

**Description**

Optional.

The version of the Analytics asset the action is associated with.

**Field Type**
AnalyticsActionEventType (enumeration of type string)

**Description**

Required.

The action event type.

Values are:

**•** `click`

**•** `select`

**Field Type**
string


Metadata Types AnalyticsDashboard

**Field Name** **Description**

**Description**
The parameter for the action. This is a JSON string.

Example:

```
                       {"destination":{"type":"url","target":"www.salesforce.com"}}

```

```
version

```

**Field Type**
double

**Description**
The API version of the action.

AnalyticsButtonWidgetDef

Represents a button widget definition for a Tableau Next dashboard.

**Field Name** **Description**

```
parameters

```

**Field Type**
string

**Description**
The parameters for the button widget. This is a JSON String.

Example:

```
  {"text":"Button","alignmentX":"center","alignmentY":"center","fontSize":16}

```

AnalyticsContainerWidgetDef

Represents a container widget definition for a Tableau Next dashboard.

**Field Name** **Description**

```
parameters

```

**Field Type**
string

**Description**
The parameters for the container widget. This is a JSON String.

Example:

```
  {"widgetStyle":{"backgroundColor":"#1295FF","borderEdges":[]}}

```


Metadata Types AnalyticsDashboard

AnlytDshbrdWdgtDynamicTkn

Represents a widget dynamic token for a Tableau Next dashboard.

**Field Name** **Description**

```
description

label

source

tokenName

tokenSpec

type

```

AnalyticsFilterWidgetDef

**Field Type**
string

**Description**
The description for the dynamic token.

**Field Type**
string

**Description**
The label for the dynamic token.

**Field Type**
string

**Description**
The source object of the dynamic token.

**Field Type**
string

**Description**
The name of the dynamic token.

**Field Type**
string

**Description**
The specification for the dynamic token.

**Field Type**
AnalyticsDynamicTokenType

**Description**
The type of dynamic token. Valid values include `query` and `insights` .

Represents a filter widget definition for a Tableau Next dashboard.

**Field Name** **Description**

```
initialValues

```

**Field Type**
string


Metadata Types AnalyticsDashboard

**Field Name** **Description**

**Description**
The initial values for the filter.

```
parameters

source

```

**Field Type**
string

**Description**
The parameters for the filter widget. This is a JSON String.

Example:

```
  {"receiveFilterSource":{"filterMode":"all","widgetIds":[]},"filterOption":{"objectName":"Account","fieldName":"Account_Id","dataType":"Text","selectionType":"multiple"},"isLabelHidden":false}

```

**Field Type**
string

**Description**
The data source to apply the filter to.

AnalyticsImageWidgetDef

Represents a image widget definition for a Tableau Next dashboard.

**Field Name** **Description**

```
parameters

source

```

**Field Type**
string

**Description**
The parameters for the image widget. This is a JSON String.

**Field Type**
string

**Description**
The data source the image is associated with.

AnalyticsMetricWidgetDef

Represents a metric widget definition for a Tableau Next dashboard.

**Field Name** **Description**

```
parameters

```

**Field Type**
string


Metadata Types AnalyticsDashboard

**Field Name** **Description**

**Description**
The parameters for the filter widget. This is a JSON String.

Example:

```
                       {"metricOption":{"layout":{"componentVisibility":{"details":true,"title":true,"value":true,"comparison":true,"chart":true,"insights":false}},"sdmApiName":"AccountModel","sdmId":"2SMxx0000004CFUGA2"},"receiveFilterSource":{"filterMode":"all","widgetIds":[]}}

```

```
semanticModel

source

sourceDeprecated

version

```

**Field Type**
string

**Description**
The semantic model the metric is associated with.

**Field Type**
string

**Description**
The data source the metric is associated with.

**Field Type**
string

**Description**
Present if the data source the metric is associated with is deprecated.

**Field Type**
double

**Description**
The API version of the metric.

AnalyticsParamWidgetDef

Represents a parameters widget definition for a Tableau Next dashboard.

**Field Name** **Description**

```
initialValues

parameters

```

**Field Type**
string

**Description**
The initial values for the parameters.

**Field Type**
string


Metadata Types AnalyticsDashboard

**Field Name** **Description**

**Description**
The parameters for the filter widget. This is a JSON String.

Example:

```
                       {"parameterName":"AccountParameter_prm","isLabelHidden":false}

```

```
source

```

AnalyticsTextWidgetDef

**Field Type**
string

**Description**
The data source the parameters are associated with.

Represents a text widget definition for a Tableau Next dashboard.

**Field Name** **Description**

```
parameters

```

AnalyticsVizWidgetDef

**Field Type**
string

**Description**
The parameters for the filter widget. This is a JSON String.

Example:

```
  {"content":[{"attributes":{"color":"#000000","size":"12px"},"insert":"full

  dashboard"},{"attributes":{"align":"left"},"insert":"\n"}]}

```

Represents a visualization widget definition for a Tableau Next dashboard.

**Field Name** **Description**

```
analyticsVisualization

analyticsVizVersion

```

**Field Type**
string

**Description**
The API name of the visualization.

**Field Type**
string


Metadata Types AnalyticsDashboard

**Field Name** **Description**

**Description**
The version of the visualization.

```
parameters

```

**Field Type**
string

**Description**
The parameters for the filter widget. This is a JSON String.

Example:

```
  {"legendPosition":"Right","receiveFilterSource":{"filterMode":"all","widgetIds":[]}}

```

Declarative Metadata Sample Definition

The following is an example of an AnalyticsDashboard component.

```
<?xml version="1.0" encoding="UTF-8"?>

<AnalyticsDashboard xmlns="http://soap.sforce.com/2006/04/metadata"

xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

   <analyticsWorkspace>My_Workspace</analyticsWorkspace>

   <description>A dashboard</description>

   <layouts>

     <analyticsDashboard>My_Dashboard</analyticsDashboard>

     <columnCount>36</columnCount>

     <layoutName>default</layoutName>

     <maxWidth>1200</maxWidth>

     <label>layoutLabel</label>

     <pages>

        <index>0</index>

        <label>Page 1</label>

        <pageName>e412bc11-d43b-4fba-ab44-b31bb842b49a</pageName>

        <pageWidgets>

          <analyticsDashboardWidget>visualization_1</analyticsDashboardWidget>

          <colspan>11</colspan>

          <column>1</column>

          <row>2</row>

          <rowspan>10</rowspan>

        </pageWidgets>

        <pageWidgets>

          <analyticsDashboardWidget>button_1</analyticsDashboardWidget>

          <colspan>9</colspan>

          <column>13</column>

          <row>8</row>

          <rowspan>2</rowspan>

        </pageWidgets>

        <pageWidgets>

          <analyticsDashboardWidget>container_1</analyticsDashboardWidget>

          <colspan>11</colspan>

          <column>23</column>

          <row>2</row>

```


Metadata Types AnalyticsDashboard

```
             <rowspan>10</rowspan>

           </pageWidgets>

           <pageWidgets>

             <analyticsDashboardWidget>text_2</analyticsDashboardWidget>

             <colspan>9</colspan>

             <column>13</column>

             <row>5</row>

             <rowspan>2</rowspan>

           </pageWidgets>

           <pageWidgets>

             <analyticsDashboardWidget>metric_1</analyticsDashboardWidget>

             <colspan>11</colspan>

             <column>1</column>

             <row>13</row>

             <rowspan>10</rowspan>

           </pageWidgets>

           <pageWidgets>

             <analyticsDashboardWidget>list_4</analyticsDashboardWidget>

             <colspan>9</colspan>

             <column>13</column>

             <row>13</row>

             <rowspan>2</rowspan>

           </pageWidgets>

           <pageWidgets>

             <analyticsDashboardWidget>list_1</analyticsDashboardWidget>

             <colspan>9</colspan>

             <column>13</column>

             <row>2</row>

             <rowspan>2</rowspan>

           </pageWidgets>

        </pages>

        <rowHeight>24</rowHeight>

   <style>{&quot;backgroundColor&quot;:&quot;#ffffff&quot;,&quot;gutterColor&quot;:&quot;#f3f3f3&quot;,&quot;cellSpacingX&quot;:8,&quot;cellSpacingY&quot;:8}</style>

      </layouts>

      <masterLabel>My Dashboard</masterLabel>

   <style>{&quot;widgetStyle&quot;:{&quot;backgroundColor&quot;:&quot;#ffffff&quot;,&quot;borderEdges&quot;:[],&quot;borderColor&quot;:&quot;#cccccc&quot;,&quot;borderWidth&quot;:1,&quot;borderRadius&quot;:0}}</style>

      <version>64.0</version>

      <widgets>

        <analyticsDashboard>My_Dashboard</analyticsDashboard>

        <type>visualization</type>

        <vizWidgetDefs>

           <analyticsVisualization>New_Visualization</analyticsVisualization>

   <parameters>{&quot;legendPosition&quot;:&quot;Right&quot;,&quot;receiveFilterSource&quot;:{&quot;filterMode&quot;:&quot;all&quot;,&quot;widgetIds&quot;:[]}}</parameters>

        </vizWidgetDefs>

        <widgetName>visualization_1</widgetName>

      </widgets>

      <widgets>

        <analyticsDashboard>My_Dashboard</analyticsDashboard>

```


Metadata Types AnalyticsDashboard

```
        <buttonWidgetDefs>

   <parameters>{&quot;text&quot;:&quot;Button&quot;,&quot;alignmentX&quot;:&quot;center&quot;,&quot;alignmentY&quot;:&quot;center&quot;,&quot;fontSize&quot;:16}</parameters>

        </buttonWidgetDefs>

        <type>button</type>

        <widgetActions>

           <actionType>navigate</actionType>

           <eventType>click</eventType>

   <parameters>{&quot;destination&quot;:{&quot;type&quot;:&quot;url&quot;,&quot;target&quot;:&quot;www.salesforce.com&quot;}}</parameters>

           <version>63.0</version>

        </widgetActions>

        <widgetName>button_1</widgetName>

      </widgets>

      <widgets>

        <analyticsDashboard>My_Dashboard</analyticsDashboard>

        <containerWidgetDefs>

   <parameters>{&quot;widgetStyle&quot;:{&quot;backgroundColor&quot;:&quot;#1295FF&quot;,&quot;borderEdges&quot;:[]}}</parameters>

        </containerWidgetDefs>

        <type>container</type>

        <widgetName>container_1</widgetName>

      </widgets>

      <widgets>

        <analyticsDashboard>My_Dashboard</analyticsDashboard>

        <textWidgetDefs>

   <parameters>{&quot;content&quot;:[{&quot;attributes&quot;:{&quot;color&quot;:&quot;#000000&quot;,&quot;size&quot;:&quot;12px&quot;},&quot;insert&quot;:&quot;full

   dashboard&quot;},{&quot;attributes&quot;:{&quot;align&quot;:&quot;left&quot;},&quot;insert&quot;:&quot;\n&quot;}]}</parameters>

        </textWidgetDefs>

        <type>text</type>

        <widgetName>text_2</widgetName>

      </widgets>

      <widgets>

        <analyticsDashboard>My_Dashboard</analyticsDashboard>

        <metricWidgetDefs>

   <parameters>{&quot;metricOption&quot;:{&quot;layout&quot;:{&quot;componentVisibility&quot;:{&quot;details&quot;:true,&quot;title&quot;:true,&quot;value&quot;:true,&quot;comparison&quot;:true,&quot;chart&quot;:true,&quot;insights&quot;:false}},&quot;sdmApiName&quot;:&quot;AccountModel&quot;,&quot;sdmId&quot;:&quot;2SMxx0000004CFUGA2&quot;},&quot;receiveFilterSource&quot;:{&quot;filterMode&quot;:&quot;all&quot;,&quot;widgetIds&quot;:[]}}</parameters>

           <source>AccountMetric_mtc</source>

        </metricWidgetDefs>

        <type>metric</type>

        <widgetName>metric_1</widgetName>

      </widgets>

      <widgets>

        <analyticsDashboard>My_Dashboard</analyticsDashboard>

        <filterWidgetDefs>

           <initialValues>null</initialValues>

```


Metadata Types AnalyticsDashboard

```
   <parameters>{&quot;receiveFilterSource&quot;:{&quot;filterMode&quot;:&quot;all&quot;,&quot;widgetIds&quot;:[]},&quot;filterOption&quot;:{&quot;objectName&quot;:&quot;Account&quot;,&quot;fieldName&quot;:&quot;Account_Id&quot;,&quot;dataType&quot;:&quot;Text&quot;,&quot;selectionType&quot;:&quot;multiple&quot;},&quot;isLabelHidden&quot;:false}</parameters>

           <source>AccountModel</source>

        </filterWidgetDefs>

        <label>Account Id</label>

        <type>filter</type>

        <widgetName>list_4</widgetName>

      </widgets>

      <widgets>

        <analyticsDashboard>My_Dashboard</analyticsDashboard>

        <label>AccountParameter</label>

        <parameterWidgetDefs>

           <initialValues>null</initialValues>

   <parameters>{&quot;parameterName&quot;:&quot;AccountParameter_prm&quot;,&quot;isLabelHidden&quot;:false}</parameters>

           <source>AccountModel</source>

        </parameterWidgetDefs>

        <type>parameter</type>

        <widgetName>list_1</widgetName>

      </widgets>

      <templateSource></templateSource>

      <templateAssetSourceName></templateAssetSourceName>

      <workspaceAssetRelationships>

        <asset xsi:nil="true"/>

        <assetType>AnalyticsDashboard</assetType>

        <assetUsageType>Created</assetUsageType>

        <workspace>My_Workspace</workspace>

      </workspaceAssetRelationships>

   </AnalyticsDashboard>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>My_Dashboard</members>

        <name>AnalyticsDashboard</name>

      </types>

      <version>64.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types AnalyticSnapshot AnalyticSnapshot

Represents a reporting snapshot. A reporting snapshot lets you report on historical data. Authorized users can save tabular or summary
report results to fields on a custom object, then map those fields to corresponding fields on a target object. They can then schedule
when to run the report to load the custom object's fields with the report's data. Reporting snapshots enable you to work with report
data similarly to how you work with other records in Salesforce.

Declarative Metadata File Suffix and Directory Location

Lightning Platform AnalyticSnapshot components are stored in the `analyticSnapshots` directory of the corresponding package
directory. The file name matches the unique name of the reporting snapshot, and the extension is `.snapshot` .

Version

Lightning Platform AnalyticSnapshot components are available in API version 16.0 and later.

Fields

**Field** **Field Type** **Description**

`description` string A description of the reporting snapshot.

`groupColumn` string A column that specifies which level to extract data from the
source report. It’s only applicable for summary reports.

### mappings AnalyticSnapshotMapping[] A list of reporting snapshot mappings. For valid values, see AnalyticSnapshotMapping.

`name` string Required. The display name of the reporting snapshot.

`runningUser` string The username of the user whose role and _sharing_ settings are
used to run the reporting snapshot.

`sourceReport` string Required. The report where data is extracted from.

`targetObject` string Required. The custom object where data is inserted.

### AnalyticSnapshotMapping AnalyticSnapshotMapping defines the mapping for the reporting snapshot. Valid values are:

**Field** **Field Type** **Description**

`aggregateType` ReportSummaryType[] List that defines if and how each report field is summarized. For valid
(enumeration of type string) values, see ReportSummaryType.

`sourceField` string The sourceField can be one of the following:

**•** The field on the sourceReport that you want to map to the targetField
in the targetObject


Metadata Types AnalyticSnapshot

**Field** **Field Type** **Description**

**•** A summary of a filed on the sourceReport (for Summary reports only)

**•** A field on the reporting snapshot, such as JobName, RunningUser, or
ExecutionTime (set through the user interface)

**Note:** The sourceField must correspond to the sourceType you specify.

`sourceType` ReportJobSourceTypes[] List that defines the report format for the reporting snapshot. For valid
(enumeration of type string) values, see ReportJobSourceTypes.

`targetField` string A field on the targetObject into which this particular sourceField is inserted.

ReportJobSourceTypes

An enumeration of type string that defines the report format for the reporting snapshot. Valid values are:

**Enumeration Value** **Description**

`snapshot` Use this option if the sourceField contains snapshot-specific information such as JobName,
RunningUser, or ExecutionTime.

`summary` Use this option if referencing a summary (Sum, Average, Minimum, Maximum) of a field from
the sourceReport.

`tabular` Use this option if referencing an available column from the sourceReport.

Declarative Metadata Sample Definition

Here’s a sample XML definition of a reporting snapshot.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <AnalyticSnapshot xmlns="http://soap.sforce.com/2006/04/metadata">

      <description>my description</description>

      <groupColumn>INDUSTRY</groupColumn>

      <mappings>

        <aggregateType>Average</aggregateType>

        <sourceField>SALES</sourceField>

        <sourceType>summary</sourceType>

        <targetField> myObject __c.Name</targetField>

      </mappings>

      <mappings>

        <sourceField>ExecutionTime</sourceField>

        <sourceType>snapshot</sourceType>

        <targetField> myObject __c.field3__c</targetField>

      </mappings>

      <mappings>

        <sourceField>INDUSTRY</sourceField>

        <sourceType>tabular</sourceType>

        <targetField>testObject__c.Name</targetField>

      </mappings>

      <name>my snapshot</name >

```


### Metadata Types AnalyticsVisualization

```
      <runningUser>user@salesforce.com</runningUser>

      <sourceReport>myFolder/mytSummaryReport</sourceReport>

      <targetObject>myObject__c</targetObject>

   </AnalyticSnapshot>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

Report

### AnalyticsVisualization

Represents a Tableau Next visualization.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### AnalyticsVisualization components have the suffix .uaviz and are stored in the analyticsVisualizations folder.

Version

### AnalyticsVisualization components are available in API version 64.0 and later.

Limits

**Definition** **Limit**

The maximum number of 50
### AnalyticsVisualization components in a single

deploy operation.

The maximum number of 100
### AnalyticsVisualization components in a single

retrieve operation.

The maximum number of 100
### AnalyticsVisualization components across all

deploy operations in a 24-hour window.


Metadata Types AnalyticsVisualization

**Definition** **Limit**

The maximum number of 200
AnalyticsVisualization components across all
retrieve operations in a 24-hour window.

Fields

**Field Name** **Description**

```
actions

analyticsWorkspace

creationSource

dataSource

description

fields

```

**Field Type**

AnalyticsAssetAction[]

**Description**
The actions for the visualization. A visualization has 0 or more actions.

**Field Type**
string

**Description**

Required.

The Tableau Next workspace the visualization belongs to.

**Field Type**
string

**Description**
The creation source for the visualization.

**Field Type**
string

**Description**

Required.

The data source for the visualization.

**Field Type**
string

**Description**
The description for the visualization.

**Field Type**

AnalyticsVizField[]

**Description**
A list of data fields for the visualization. A visualization has 0 or more fields.


Metadata Types AnalyticsVisualization

**Field Name** **Description**

```
lastDraftModifiedDate

lastPublishedDate

masterLabel

templateAssetSourceName

templateSource

version

views

visualSpecification

```

**Field Type**
dateTime

**Description**
The date and time the workspace draft was last modified.

**Field Type**
dateTime

**Description**
The date and time the workspace was last published.

**Field Type**
string

**Description**

Required.

The name of the visualization.

**Field Type**
string

**Description**
If the visualization was created from a template, the name of the source visualization
in the template.

**Field Type**
string

**Description**
If the visualization was created from a template, the name of the source template.

**Field Type**
double

**Description**
The API version of the visualization.

**Field Type**

AnalyticsVizViewDef[]

**Description**
A list of views for the visualization. A visualization has 0 or more views.

**Field Type**
base64Binary

**Description**

Required.


Metadata Types AnalyticsVisualization

**Field Name** **Description**

The visual specification for the visualization.

```
workspaceAssetRelationships

```

AnalyticsVizField

Represents a data field in a visualization.

**Field Type**

AnalyticsWorkspaceAsset[]

**Description**
A list of analytics assets in the workspace this visualization is associated with. A
visualization has 0 or more workspace asset relationships.

**Field Name** **Description**

```
adHoCalc

analyticsVizVersion

computeUsing

displayCategory

fieldKey

```

**Field Type**
string

**Description**
The expression to do an ad-hoc calculation with.

**Field Type**
string

**Description**
The version of the visualization the field is associated with.

**Field Type**
string

**Description**
The expression to compute the field value with.

**Field Type**
VisualizationFieldDisplayCategoryType (enumeration of type string)

**Description**
The display category type for the visualization field.

Values are:

**•** `Continuous`

**•** `Discrete`

**Field Type**
string

**Description**

Required.


Metadata Types AnalyticsVisualization

**Field Name** **Description**

The key for the field.

```
fieldName

function

```

**Field Type**
string

**Description**
The name of the field.

**Field Type**
VisualizationFieldFunctionType (enumeration of type string)

**Description**
The function type of the visualization field.

Values are:

**•** `Attr`

**•** `Avg`

**•** `Count`

**•** `CountD`

**•** `DatePartDay`

**•** `DatePartHour`

**•** `DatePartMinute`

**•** `DatePartMonth`

**•** `DatePartQuarter`

**•** `DatePartSecond`

**•** `DatePartWeek`

**•** `DatePartWeekDay`

**•** `DatePartYear`

**•** `DateTruncDay`

**•** `DateTruncHour`

**•** `DateTruncMinute`

**•** `DateTruncMonth`

**•** `DateTruncQuarter`

**•** `DateTruncSecond`

**•** `DateTruncWeek`

**•** `DateTruncYear`

**•** `FiscalDatePartMonth`

**•** `FiscalDatePartQuarter`

**•** `FiscalDatePartWeek`

**•** `FiscalDatePartYear`

**•** `FiscalDateTruncMonth`

**•** `FiscalDateTruncQuarter`


Metadata Types AnalyticsVisualization

**Field Name** **Description**

**•** `FiscalDateTruncWeek`

**•** `FiscalDateTruncYear`

**•** `Max`

**•** `Mdy`

**•** `Median`

**•** `Min`

**•** `My`

**•** `Stdev`

**•** `Stdevp`

**•** `Sum`

**•** `UserAgg`

**•** `Var`

**•** `Varp`

```
hierarchyName

label

objectName

quickTableCalc

role

```

**Field Type**
string

**Description**
The hierarchy name for the field.

**Field Type**
string

**Description**
The label for the field.

**Field Type**
string

**Description**
The name of the data source object for the field.

**Field Type**
string

**Description**
The expression to do a quick table calculation with.

**Field Type**
VisualizationFieldRoleType (enumeration of type string)

**Description**
The role type of the visualization field.

Values are:

**•** `Dimension`


Metadata Types AnalyticsVisualization

**Field Name** **Description**

**•** `Measure`

```
type

```

AnalyticsVizViewDef

**Field Type**
VisualizationFieldType (enumeration of type string)

**Description**
The type of the visualization field.

Values are:

**•** `Field`

**•** `MapPosition`

**•** `MeasureNames`

**•** `MeasureValues`

Represents a view definition for a Tableau Next visualization.

**Field Name** **Description**

```
analyticsVizVersion

fullName

isOriginal

masterLabel

```

**Field Type**
string

**Description**
The version of the visualization the view is associated with.

**Field Type**
string

**Description**

Required.

The full name of the view definition.

**Field Type**
boolean

**Description**

Required.

Indicates whether the view is original ( `true` ) or not ( `false` ).

**Field Type**
string

**Description**

Required.

The name of the view definition.


Metadata Types AnalyticsVisualization

**Field Name** **Description**

```
version

viewSpecification

```

**Field Type**
double

**Description**
The API version of the visualization view.

**Field Type**
string

**Description**
The specification for the view definition.

Declarative Metadata Sample Definition

The following is an example of an AnalyticsVisualization component.

```
<?xml version="1.0" encoding="UTF-8"?>

<AnalyticsVisualization xmlns="http://soap.sforce.com/2006/04/metadata"

xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

  <analyticsWorkspace>My_Workspace</analyticsWorkspace>

  <description>A visualization</description>

  <dataSource>My_Semantic_Model</dataSource>

  <fields>

   <displayCategory>Discrete</displayCategory>

   <fieldKey>Field1</fieldKey>

   <fieldName>Lead_Source18</fieldName>

   <objectName>Opportunity_Home</objectName>

   <role>Dimension</role>

   <type>Field</type>

  </fields>

  <fields>

   <fieldKey>Field2</fieldKey>

   <displayCategory>Continuous</displayCategory>

   <fieldName>Amount</fieldName>

   <function>Sum</function>

   <objectName>Opportunity_Home</objectName>

   <role>Measure</role>

   <type>Field</type>

  </fields>

  <views>

   <fullName>default</fullName>

   <masterLabel>My_Visualization_default</masterLabel>

   <viewSpecification>

{&quot;filters&quot;:[{&quot;fieldKey&quot;:&quot;Field1&quot;,&quot;filterInfos&quot;:[{&quot;isCustom&quot;:false,&quot;isExcludes&quot;:false,&quot;type&quot;:&quot;In&quot;,&quot;useA l &quot;:false,&quot;values&quot;:[&quot;NewBusine s &quot;]},{&quot;includeA l ValuesWhenEmpty&quot;:true,&quot;isExcludes&quot;:false,&quot;operator&quot;:&quot;Contains&quot;,&quot;type&quot;:&quot;WildCard&quot;,&quot;value&quot;:&quot;&quot;}],&quot;isContext&quot;:false}],&quot;sorts&quot;:[{&quot;byField&quot;:&quot;Field2&quot;,&quot;fieldKey&quot;:&quot;Field1&quot;,&quot;order&quot;:&quot;Ascending&quot;,&quot;type&quot;:&quot;Nested&quot;}]}</viewSpecification>

   <isOriginal>true</isOriginal>

  </views>

  <masterLabel>My_Visualization</masterLabel>

  <version>64.0</version>

```


### Metadata Types AnalyticsWorkspace

```
     <templateSource></templateSource>

     <templateAssetSourceName></templateAssetSourceName>

     <workspaceAssetRelationships>

      <asset xsi:nil="true"/>

      <assetType>AnalyticVisualization</assetType>

      <assetUsageType>Created</assetUsageType>

      <workspace>My_Workspace</workspace>

     </workspaceAssetRelationships>

   </AnalyticsVisualization>

```

The following is an example `package.xml` that references the metadata definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

    <Package xmlns="http://soap.sforce.com/2006/04/metadata">

    <types>

    <members>My_Visualization</members>

    <name>AnalyticsVisualization</name>

    </types>

    <version>64.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### AnalyticsWorkspace

Represents a Tableau Next workspace.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### AnalyticsWorkspace components have the suffix .analtyicsWorkspace and are stored in the analyticsWorkspaces

folder.

Version

### AnalyticsWorkspace components are available in API version 64 and later.


Metadata Types AnalyticsWorkspace

Limits

**Definition** **Limit**

The maximum number of AnalyticsWorkspace 50
components in a single deploy operation.

The maximum number of AnalyticsWorkspace 100
components in a single retrieve operation.

The maximum number of AnalyticsWorkspace 100
components across all deploy operations in
a 24-hour window.

The maximum number of AnalyticsWorkspace 200
components across all retrieve operations in
a 24-hour window.

Fields

**Field Name** **Description**

```
description

masterLabel

workspaceAssetRelationships

```

**Field Type**
string

**Description**
The workspace description.

**Field Type**
string

**Description**

Required.

The name of the workspace.

**Field Type**

AnalyticsWorkspaceAsset[]

**Description**
The workspace assets associated with the workspace. A workspace has 1 or more
assets.

AnalyticsWorkspaceAsset

Represents a Tableau Next analytics asset.


Metadata Types AnalyticsWorkspace

**Field Name** **Description**

```
asset

assetType

assetUsageType

metadataSourceType

```

**Field Type**
string

**Description**

Required.

The name of workspace asset

**Field Type**
AnalyticsWorkspaceAssetType (enumeration of type string)

**Description**

Required.

The workspace asset type

Values are:

**•** `AnalyticsDashboard` (Tableau Next Dashboard)

**•** `AnalyticsVisualization` (Tableau Next Visualization)

**•** `MktCalculatedInsightObject` (Data 360 Calculated Insight Object)

**•** `MktDataConnection` (Data 360 Connection)

**•** `MktDataLakeObject` (Data 360 Data Lake Object)

**•** `MktDataModelObject` (Data 360 Data Model Object)

**•** `SemanticModel` (Semantic Model)

**Field Type**
AnalyticsWorkspaceAssetUsageType (enumeration of type string)

**Description**

Required.

The workspace asset usage type.

Values are:

**•** `Created`

**•** `Referenced`

**Field Type**
AnalyticsWorkspaceAssetMetadataSourceType (enumeration of type string)

**Description**
The workspace asset metadata source type.

Values are:

**•** `Promoted`

**•** `Reused`


### Metadata Types AnimationRule

**Field Name** **Description**

```
workspace

```

**Field Type**
string

**Description**

Required.

The workspace the asset belongs to.

Declarative Metadata Sample Definition

The following is an example of an AnalyticsWorkspace component.

```
<?xml version="1.0" encoding="UTF-8"?>

  <AnalyticsWorkspace xmlns="http://soap.sforce.com/2006/04/metadata">

  <description>An example for Analytics Workspace</description>

  <masterLabel>Analytics Workspace</masterLabel>

  <workspaceAssetRelationships>

   <asset>My Test Dashboard</asset>

   <assetType>AnalyticsDashboard</assetType>

   <assetUsageType>Created</assetUsageType>

   <metadataSourceType>Promoted</metadataSourceType>

   <workspace>Analytics Workspace</workspace>

  </workspaceAssetRelationships>

</AnalyticsWorkspace>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

  <types>

   <members>*</members>

   <name>AnalyticsWorkspace</name>

  </types>

  <version>64.0</version>

</Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### AnimationRule

Represents criteria for determining when an animation is displayed to Path users.This type extends the Metadata metadata type and
inherits its `fullName` field.


Metadata Types AnimationRule

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

AnimationRule components have the suffix `animationRule` and are stored in the `animationRules` folder.

Version

AnimationRule components are available in API version 46.0 and later.

Fields

**Field Name** **Field Type** **Description**

`animationFrequency` picklist Required. The frequency with which an animation is displayed when a
user selects the designated picklist values in a path. Valid values are:

**•** `always`

**•** `often`

**•** `sometimes`

**•** `rarely`

A value of `always` triggers an animation every time. The values
`often`, `sometimes`, and `rarely` trigger an animation progressively
less frequently.

`developerName` string Required. The developer name for the animation rule.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this
field.

`isActive` boolean Required. Indicates whether the animation rule is active ( `true` ) or not
( `false` ).

`masterLabel` string Required. The label for the animation rule.

`recordTypeContext` picklist

Required. An enum to track whether this AnimationRule applies to all
record types for the associated sObject, or only to a single or main record
type. Valid values are `All`, `Master`, or `Custom` .

`recordTypeName` reference The record type selected for the sObject in which the animation is
displayed.

`sobjectType` string The object on which the animation rule is run.

`targetField` string Required. Name of the field used to determine when to display an
animation.


### Metadata Types AppFrameworkTemplateBundle

**Field Name** **Field Type** **Description**

`targetFieldChangeToValues` string

Required. Values used to determine when to display an animation. When
a user selects a value in `targetField` that matches a value stored
in `targetFieldChangeToValues`, the animation is displayed.

Declarative Metadata Sample Definition

The following is an example of an AnimationRule component.

```
<?xml version="1.0" encoding="UTF-8"?>

<AnimationRule xmlns="http://soap.sforce.com/2006/04/metadata">

   <animationFrequency>Always</animationFrequency>

   <developerName>AnimationRule_DeveloperName</developerName>

   <isActive>true</isActive>

   <masterLabel>AnimationRule Label</masterLabel>

   <recordTypeContext>All</recordTypeContext>

   <recordTypeName>__MASTER__</recordTypeName>

   <sobjectType>Opportunity</sobjectType>

   <targetField>StageName</targetField>

  <targetFieldChangeToValues>Delivered, Negotiating, Closed Won</targetFieldChangeToValues>

</AnimationRule>

```

The following is an example `package.xml` that references the AnimationRule component.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>PathAssistant</members>

     <name>Settings</name>

   </types>

   <types>

     <members>AnimationRule_Developer_Name</members>

     <name>AnimationRule</name>

   </types>

   <version>46.0</version>

</Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### AppFrameworkTemplateBundle

Represents the app framework template bundle. Use these templates for Data 360 and Tableau Next assets.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types AppFrameworkTemplateBundle

File Suffix and Directory Location

An app framework template bundle is a folder that contains definition files for a template. Unlike other metadata components, a
AppFrameworkTemplateBundle component isn’t represented with a single component file, but instead by a collection of JSON and
other definition files. Each definition file represents a resource in a template, such as semantic models, workspaces, visualizations, and
dashboards. For example, this directory structure shows the hierarchy of the folders and files for one app framework template definition,
myTemplate.

```
   appTemplates

     myTemplate

      template-info.json

      create-chain.json

      rules.json

      variables.json

      layout.json

      workspaces

       myWorkspace.json

      dashboards

       myDashboard.json

```

App framework template bundles must be under a top-level folder that’s named `appTemplates` . Each bundle must have its own
subfolder under the `appTemplate` folder and named with the template's fully qualified API name. The bundle folder must contain
a template-info.json file to specify the metadata about the template and the references to other definition files. An entire bundle doesn’t
have a suffix and definition files can have one of the these suffixes.

Version

AppFrameworkTemplateBundle components are available in API version 64.0 and later.

Special Access Rules

Create definitions in both managed and unmanaged packages.

Fields

**Field Name** **Description**

```
assetVersion

```

**Field Type**
double

**Description**
The API version of the template bundle.


Metadata Types AppFrameworkTemplateBundle

**Field Name** **Description**

```
description

label

maxAppCount

templateBadgeIcon

templateStatus

templateSubtype

templateType

```

**Field Type**
string

**Description**
The description for the template.

**Field Type**
string

**Description**
Required

The label for the template.

**Field Type**
int

**Description**
The maximum number of apps that can be created from this template.

**Field Type**
string

**Description**
The badge icon for the template. This must be a `.png` file type.

**Field Type**
string

**Description**
The status of the template.

**Field Type**
string

**Description**
The subtype of the template.

**Field Type**
string

**Description**
The type of the template.

Declarative Metadata Sample Definition

This is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

```


### Metadata Types ArticleType

```
   <types>

      <members>myTemplate</members>

      <name>AppFrameworkTemplateBundle</name>

   </types>

   <version>64.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about the manifest
[file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### ArticleType

Represents the metadata associated with an article type.

All articles in Salesforce Knowledge are assigned to an _article type_ . An article's type determines the type of content it contains, its
appearance, and which users can access it. For example, a simple FAQ article type can have two custom fields, `Question` and `Answer`,
where article managers enter data when creating or updating FAQ articles. A more complex article type can have dozens of fields
organized into several sections. Using layouts and templates, administrators can structure the article type in the most effective way for
its particular content. User access to article types is controlled by permissions. For each article type, an administrator can grant “Create,”
“Read,” “Edit,” or “Delete” permissions to users. For example, the article manager can allow internal users to read, create, and edit FAQ
[article types, but let partner users only read FAQs. See “Knowledge Article Types” in the Salesforce online help and Knowledge in the](https://help.salesforce.com/s/articleView?id=service.knowledge_article_types_manage.htm&type=5&language=en_US)
_SOAP API Developer Guide_ .

Declarative Metadata File Suffix and Directory Location

An ArticleType is defined as a custom object and is stored in the `objects` folder. ArticleTypes have a suffix `__kav` (instead of `__c`
for custom objects). ArticleType field names have a suffix of `__c` like other custom objects, and must be dot-qualified with the name
of the article type to which they belong. This is shown in the following sample `package.xml` file:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <fullName>articlefilemetadata</fullName>

      <apiAccessLevel>Unrestricted</apiAccessLevel>

      <types>

        <members>newarticle__kav.description__c</members>

        <name>CustomField</name>

      </types>

      <types>

        <members>newarticle__kav</members>

        <name>CustomObject</name>

      </types>

   </Package>

```

Version

### ArticleTypes are available in API version 19.0 and later.


Metadata Types ArticleType

Fields

**Field Name** **Field Type** **Description**

`articleTypeChannel` articleTypeChannelDisplay

```
Display

```

`deploymentStatus` DeploymentStatus
(enumeration of type string)

Represents the article-type templates used to display an article in the
[various channels. See “Article Type Templates” in the Salesforce online](https://help.salesforce.com/s/articleView?id=service.knowledge_article_templates_create.htm&type=5&language=en_US)
help.

A string which represents the deployment status of a custom object or
field. Valid values are:

**•** `InDevelopment`

**•** `Deployed`

`description` string A description of the article type. Maximum of 1000 characters.

`fields` CustomField[] Represents one or more fields in the article type.

`gender` Gender

Indicates the gender of the noun that represents the object. This is used
for languages where words need different treatment depending on their
gender.

`label` string Label that represents the object throughout the Salesforce user interface.

`pluralLabel` string Plural version of the `label` value.

`startsWith` StartsWith (enumeration of
type string)

ArticleTypeChannelDisplay

Indicates whether the noun starts with a vowel, consonant, or is a special
character. This is used for languages where words need different treatment
depending on the first character. Valid values are listed in StartsWith.

Determines the article-type templates that are used to display an article in its channels. Unless otherwise noted, all fields are createable,
filterable, and nillable.

**Field Name** **Field Type** **Description**

`articleTypeTemplates` ArticleTypeTemplate on page Indicates which article-type template applies in the specified channel.
381[]

ArticleTypeTemplate

Sets the article-type template for a specific channel. If not specified, the default article-type template applies.

**Field Name** **Field Type** **Description**

`channel` string Specifies the channel where the article-type template applies:

**•** `AllChannels` : all the available channels.

**•** `App` : the Articles tab in Salesforce Knowledge.

**•** `Pkb` : the public knowledge base.


Metadata Types ArticleType

**Field Name** **Field Type** **Description**

**•** `Csp` : the Customer Portal.

**•** `Prm` : the partner portal.

`page` string Represents the name of the custom Visualforce page used as a custom
article-type template. Use this field when you select template

`template` string Indicates the article-type template used for the specified channel:

**•** `Page` : custom Visualforce page. When specifying this value, you
must also set the `page` field with the Visualforce page name.

**•** `Tab` : display the sections you defined in the layout as tabs.

**•** `Toc` : display the sections you defined in the layout as table of content.

Declarative Metadata Sample Definitions

A sample article type definition follows:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

      <articleTypeChannelDisplay>

        <articleTypeTemplates>

           <channel>App</channel>

           <template>Tab</template>

        </articleTypeTemplates>

        <articleTypeTemplates>

           <channel>Prm</channel>

           <template>Tab</template>

        </articleTypeTemplates>

        <articleTypeTemplates>

           <channel>Csp</channel>

           <template>Tab</template>

        </articleTypeTemplates>

        <articleTypeTemplates>

           <channel>Pkb</channel>

           <template>Toc</template>

        </articleTypeTemplates>

      </articleTypeChannelDisplay>

      <deploymentStatus>Deployed</deploymentStatus>

      <description>Article type with custom fields</description>

      <fields>

        <fullName>description__c</fullName>

        <label>Description</label>

        <length>48</length>

        <type>Text</type>

      </fields>

      <label>newarticle</label>

      <pluralLabel>newarticles</pluralLabel>

   </CustomObject>

```


#### Metadata Types ArticleType Layout

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### ArticleType Layout

Represents the metadata associated with an article type page layout. Article type layouts determine which fields users can view and
edit when entering data for an article. Article type layouts also determine which sections appear when users view articles.

ChannelLayout
Represents the metadata associated with a communication channel layout. Communication channel layouts let admins share article
content inline into communication channels (for example, in email publishers, Experience Builder sites, or social media publishers).
Admins can create a list of fields for an article type or record type that they want to share for each communication channel. You can
customize the order of the fields.

ArticleType CustomField
Represents the metadata associated with an article type custom field. Use this metadata type to create, update, or delete article type
custom field definitions.

SEE ALSO:

#### ArticleType Layout

ArticleType CustomField

#### ArticleType Layout

Represents the metadata associated with an article type page layout. Article type layouts determine which fields users can view and edit
when entering data for an article. Article type layouts also determine which sections appear when users view articles.

The format of the article, for example whether layout sections display as subtabs or as a single page with links, is defined by the article-type
template. Each article type has only one layout, but you can choose a different template for each of the article type's four channels. See
[Knowledge in](https://developer.salesforce.com/docs/atlas.en-us.262.0.api.meta/api/sforce_api_guidelines_knowledge.htm) _SOAP API Developer Guide_ .

File Suffix and Directory Location

ArticleType layouts are stored in the `layouts` directory of the corresponding package directory. The prefix must match with the article
type API name. The extension is `.layout` .

Version

ArticleType layouts are available in API version 19.0 and later.

Fields

**Field Name** **Field Type** **Description**

`layoutSections` LayoutSection[] The main sections of the layout containing the article fields. The
order here determines the layout order.


Metadata Types ArticleType Layout

LayoutSection

LayoutSection represents a section of an ArticleType layout.

**Field Name** **Field Type** **Description**

`customLabel` boolean Indicates if this section's label is custom or standard (built-in). Custom
labels can be any text, but must be translated. Standard labels have a

predefined set of valid values, for example 'System Information', which
are automatically translated.

`label` string The label; either standard or custom, based on the `customLabel`
flag.

`layoutColumns` LayoutColumn[] The columns of the layout, depending on the style. Salesforce Knowledge
only supports one column in article type layouts.

```
style

```

LayoutColumn

LayoutSectionStyle The style of the layout. Salesforce Knowledge only supports the value
(enumeration of type `OneColumn`, which displays a one-column page.
string)

LayoutColumn represents the items in a column within a layout section.

**Field Name** **Field Type** **Description**

`layoutItems` LayoutItem[] The individual items within a column (ordered from top to bottom).

LayoutItem

LayoutItem represents the valid values that define a layout item.

**Field Name** **Field Type** **Description**

`field` string The field name reference, for example `MyField__c` .

Declarative Metadata Sample Definition

The following is the definition of an ArticleType page layout:

```
<?xml version="1.0" encoding="UTF-8"?>

<Layout xmlns="http://soap.sforce.com/2006/04/metadata">

   <layoutSections>

     <customLabel>true</customLabel>

     <label>Description</label>

     <layoutColumns>

        <layoutItems>

          <field>description__c</field>

        </layoutItems>

        <layoutItems>

```


#### Metadata Types ChannelLayout

```
             <field>dateTime__c</field>

           </layoutItems>

        </layoutColumns>

        <style>OneColumn</style>

      </layoutSections>

      <layoutSections>

        <label>Data Sheet</label>

        <layoutColumns>

           <layoutItems>

             <field>file__c</field>

           </layoutItems>

        </layoutColumns>

        <style>OneColumn</style>

      </layoutSections>

   </Layout>

```

SEE ALSO:

ArticleType

ArticleType CustomField

#### ChannelLayout

Represents the metadata associated with a communication channel layout. Communication channel layouts let admins share article
content inline into communication channels (for example, in email publishers, Experience Builder sites, or social media publishers).
Admins can create a list of fields for an article type or record type that they want to share for each communication channel. You can
customize the order of the fields.

File Suffix and Directory Location

Channel layout components have the suffix `.channelLayout` and are stored in the `channelLayouts` folder of the
corresponding package directory. The prefix must match with the article type API name. In Lightning Knowledge, the prefix must match
the API name for the knowledge object.

Version

Channel layout components are available in API version 32.0 and later.

Fields

**Field Name** **Field Type** **Description**

`doesExcludeFieldLabels` boolean Indicates whether field labels are excluded from the field contents in
the communication channels where this layout applies ( `true` ) or not

( `false` ). The default is `false`, meaning field labels are inserted.
Available when Lightning Knowledge is enabled in API version 48.0 and
later.

`doesExcludeFiles` boolean Indicates whether related files are left off emails ( `true` ) or attached to
emails ( `false` ). The default is `false`, meaning related files are


Metadata Types ChannelLayout

**Field Name** **Field Type** **Description**

attached. Available when Lightning Knowledge is enabled in API version
48.0 and later.

`enabledChannels` string[] The communication channels where this layout applies. In API version
32.0 to 46.0, the only valid value is `Email` . When Lightning Knowledge

is enabled in API version 47.0 and later, `Chat`, `Messaging`, and
`Social` are added valid values.

`label` string Required. The label for this configuration.

`layoutItems` ChannelLayoutItem The article fields contained in the layout. The order here determines the
on page 386[] field order.

`recordType` string The name of the record type that the channel layout applies to. The
default is the primary record type. Available in API version 41.0 and later.

ChannelLayoutItem

**Field Name** **Field Type** **Description**

`field` string Required. Name of the field. The format is _`ArticleTypeName`_ . _`FieldName`_
or, in Lightning Knowledge, _`KnowledgeBaseName`_ . _`FieldName`_ .

Declarative Metadata Sample Definition

The following is an example of a ChannelLayout component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ChannelLayout xmlns="http://soap.sforce.com/2006/04/metadata">

      <label>Layout for Email</label>

      <layoutItems>

        <field>Knowledge.Question</field>

      </layoutItems>

      <layoutItems>

        <field>Knowledge.Answer</field>

      </layoutItems>

      <enabledChannels>Email</enabledChannels>

      <enabledChannels>Social</enabledChannels>

      <enabledChannels>Chat</enabledChannels>

      <doesExcludeFiles>false</doesExcludeFiles>

      <doesExcludeFieldLabels>true</doesExcludeFieldLabels>

   </ChannelLayout>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ChannelLayout</name>

```


#### Metadata Types ArticleType CustomField

```
      </types>

      <version>41.0</version>

   </Package>

#### ArticleType CustomField

```

Represents the metadata associated with an article type custom field. Use this metadata type to create, update, or delete article type
custom field definitions.

This type extends the Metadata metadata type and inherits its `fullName` field.

Always specify the full name whenever you create or update a custom field. For example, a custom field on a custom object:

```
   MyArticleType__kav.MyCustomField__c

```

Declarative Metadata File Suffix and Directory Location

Custom fields are defined as part of the article type. ArticleType field names have a suffix of `__c` like other custom objects, and must
be dot-qualified with the name of the article type to which they belong. See ArticleType for more information.

Retrieving Custom Fields on Custom or Standard Objects

When you retrieve a custom or standard object, you return everything associated with the object. However, you can also retrieve only
the custom fields for an object by explicitly naming the object and fields in `package.xml` . The following definition in `package.xml`
retrieves the files `objects/MyCustomObject__c.object`, `objects/Account.object__c.object`, and
`objects/MyArticleType__kav.object`, each containing one custom field definition.

```
   <types>

      <members>MyCustomObject__c.MyCustomField__c</members>

      <members>Account.MyCustomAccountField__c</members>

      <members>MyArticleType__kav.MyOtherCustomField__c</members>

      <name>CustomField</name>

   </types>

```

Version

ArticleTypes custom fields are available in API version 19.0 and later.

Fields for ArticleType

Unless otherwise noted, all fields are createable, filterable, and nillable.

Note: If you create a knowledge validation rule, the errors always display at the top of the page, even if you add it beside the
field. Therefore, write the errors descriptively so authors know how to satisfy the validation rule. For example, identify which field
is causing the error. The Salesforce Classic user interface does not support field level error messages for articles.


Metadata Types ArticleType CustomField

**Field Name** **Field Type** **Description**

`defaultValue` string If specified, represents the default value of the field. This field
was deprecated in API version 48.0.

```
deleteConstraint

```

Metadata Field Types Provides deletion options for lookup relationships. Valid values
(enumeration of type are:
string)

**•** `Cascade` —Deletes the lookup record as well as
associated lookup fields.

**•** `Restrict` —Prevents the record from being deleted if
it's in a lookup relationship.

**•** `SetNull` —This is the default. If the lookup record is
deleted, the lookup field is cleared.

For more information on lookup relationships, see "Object
Relationships" in Salesforce Help.

`description` string Description of the field.

`formula` string If specified, represents a formula on the field.

```
formulaTreatBlankAs

```

Metadata Field Types Indicates how to treat blanks in a formula. Valid values are:
(enumeration of type `BlankAsBlank` and `BlankAsZero` .
string)

`fullName` string Inherited from Metadata, this field is defined in the WSDL for
this metadata type. It must be specified when creating,

updating, or deleting. See `createMetadata()` to see an
example of this field specified for a call.

This value cannot be `null` .

`inlineHelpText` string Represents the content of field-level help. For more information,
see "Define Field-Level Help" in Salesforce Help.

`label` string Label for the field. You cannot update the label for standard
fields in Article Type such as Title, UrlName, Summary, etc.

`length` int Length of the field.

`picklist` Picklist (Including ( **Deprecated.** Use this field in API version 37.0 and earlier only.
Dependent Picklist) In later versions, use `valueSet` instead.) If specified, the field

is a picklist, and this field enumerates the picklist values and
labels.

`referenceTo` string If specified, indicates a reference this field has to another object.

`relationshipLabel` string Label for the relationship.

`relationshipName` string

If specified, indicates the value for one-to-many relationships.
For example, in the object MyObject that had a relationship to
YourObject, the relationship name might be YourObjects.

`required` boolean Indicates whether the field requires a value on creation ( `true` )
or not ( `false` ).


Metadata Types ArticleType CustomField

**Field Name** **Field Type** **Description**

`type` FieldType Required. Indicates the field type for the field. Valid values are:

**•** `Checkbox` available in version 30.0 and later

**•** `Currency`

**•** `ArticleCurrency`

**•** `Date`

**•** `DateTime`

**•** `Email`

**•** `File`

**•** `Formula`

**•** `Html`

**•** `Lookup`

**•** `Number`

**•** `Percent`

**•** `Phone`

**•** `Picklist`

**•** `DependentPicklist`

**•** `MultiselectPicklist`

**•** `Text`

**•** `TextArea`

**•** `LongTextArea`

**•** `URL`

`visibleLines` int Indicates the number of lines displayed for the field.

Declarative Metadata Sample Definition

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

      <fields>

        <fullName>Comments__c</fullName>

        <description>add your comments about this object here</description>

        <label>Comments</label>

        <length>32000</length>

        <type>LongTextArea</type>

        <visibleLines>30</visibleLines>

      </fields>

   </CustomObject>

```

SEE ALSO:

ArticleType

ArticleType Layout


### Metadata Types ApexClass ApexClass

Represents an Apex class. An Apex class is a template or blueprint from which Apex objects are created. Classes consist of other classes,
user-defined methods, variables, exception types, and static initialization code.

[For more information, see the Lightning Platform Apex Code Developer's Guide. This type extends the MetadataWithContent metadata](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/)
type and inherits its `content` and `fullName` fields.

Note: By default, you can’t deploy updates to an Apex class if there are one or more active jobs for that class. To deploy updates
in this case, do one of the following.

**•** Cancel Apex jobs before deploying changes to Apex code. Reschedule the jobs after the deployment.

**•** Enable deployments with Apex jobs in the Salesforce user interface in the Deployment Settings page.

Supported Calls

All Metadata API calls except CRUD-Based Calls, which prevents deployment outside of proper deployment lifecycle and test-execution
constraints.

Declarative Metadata File Suffix and Directory Location

The file suffix is `.cls` for the class file. The accompanying metadata file is named _`ClassName`_ `.cls-meta.xml` .

Apex classes are stored in the `classes` folder in the corresponding package directory.

Version

Apex classes are available in API version 10.0 and later.

Fields

This metadata type contains the following fields:

**Field Name** **Field Type** **Description**

`apiVersion` double
The API version for this class. Every class has an API version specified at creation.

`content` base64 The Apex class definition. Base 64-encoded binary data. Before making an API
call, client applications must encode the binary attachment data as base64. Upon

receiving a response, client applications must decode the base64 data to binary.
This conversion is handled for you by a SOAP client. This field is inherited from
the MetadataWithContent component.

`fullName` string The Apex class name. The name can only contain characters, letters, and the
underscore (_) character, must start with a letter, and can’t end with an

underscore or contain two consecutive underscore characters. This field is
inherited from the Metadata component.


Metadata Types ApexClass

**Field Name** **Field Type** **Description**

`packageVersions` PackageVersion[]

The list of installed managed package versions that are referenced by this Apex
class.

[For more information about managed packages, see Second-Generation](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_dev2gp.htm)
[Managed Packages in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_dev2gp.htm) _Salesforce DX Developer Guide_ . This field is available in
API version 16.0 and later.

`status` ApexCodeUnitStatus
The status of the Apex class. The following string values are valid:
(enumeration of type string)

**•** `Active`                    - The class is active.

**•** `Deleted`                     - The class is marked for deletion. This value is useful for managed
packages, because it allows a class to be deleted when a managed package
is updated.

ApexCodeUnitStatus includes an `Inactive` option, but it’s only supported
for ApexTrigger; it isn’t supported for ApexClass.

PackageVersion

PackageVersion identifies a version of a managed package. A package version is a number that identifies the set of components included
in a package. The version number has the format _`majorNumber.minorNumber.patchNumber`_ (for example, 2.1.3). The major
and minor numbers increase to a chosen value during every major release. The _`patchNumber`_ is generated and updated only for a
patch release. It’s available in API version 16.0 and later.

[See Set Package Versions for Apex Classes and Triggers in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_manpkgs_subscriber_version.htm) _Apex Developer Guide_ .

**Field Name** **Field Type** **Description**

`namespace` string Required. In a packaging context, a namespace prefix is a one to 15-character
alphanumeric identifier that distinguishes your package and its contents from

packages of other developers on AppExchange. Namespace prefixes are
case-insensitive. For example, ABC and abc aren’t recognized as unique. Your
namespace prefix must be globally unique across all Salesforce orgs.

Salesforce automatically prepends your namespace prefix, followed by two
underscores (“__”), to all unique component names in your Salesforce
organization. A unique package component is one that requires a name that no
other component has within Salesforce, such as custom objects, custom fields,
custom links, s-controls, and validation rules. For more information about
[namespaces, see Create and Register Your Namespace in the](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp_create_namespace.htm) _Second-Generation_
_Managed Packaging Developer Guide_ .

`majorNumber` int Required. The major number of the package version. A package version number
has a _`majorNumber.minorNumber`_ format.

`minorNumber` int Required. The minor number of the package version. A package version number
has a _`majorNumber.minorNumber`_ format.


### Metadata Types ApexComponent

Declarative Metadata Sample Definition

The following sample creates the `MyhelloWorld.cls` class, and the corresponding `MyHelloWorld.cls-meta.xml`
metadata file.

`MyHelloWorld.cls` file:

```
   public class MyHelloWorld {

   // This method updates the Hello field on a list

   // of accounts.

   public static void addHelloWorld(Account[] accs){

    for (Account a:accs){

     if (a.Hello__c != 'World')

     a.Hello__c = 'World';

     }

    }

   }

```

`MyHelloWorld.cls-meta.xml` :

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ApexClass xmlns="http://soap.sforce.com/2006/04/metadata">

      <apiVersion>66.0</apiVersion>

   </ApexClass>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

ApexTrigger

### ApexComponent

Represents a Visualforce component.

For more information, see Visualforce in Salesforce Help and StaticResource: MetadataWithContent on page 2360

Declarative Metadata File Suffix and Directory Location

The file suffix is `.component` for the page file. The accompanying metadata file is named _`ComponentName`_ `-meta.xml` .

Visualforce components are stored in the `components` folder in the corresponding package directory.

Version

Visualforce components are available in API version 12.0 and later.


### Metadata Types ApexEmailNotifications

Fields

This metadata type contains the following fields:

**Field Name** **Field Type** **Description**

`apiVersion` double The API version for this Visualforce component. Every component has an API
version specified at creation. This field is available in API version 16.0 and later.

`content` base64Binary The component content. Base 64-encoded binary data. Before making an API
call, client applications must encode the binary attachment data as base64. Upon

receiving a response, client applications must decode the base64 data to binary.
This conversion is handled for you by a SOAP client. This field is inherited from
the MetadataWithContent component.

`description` string A description of what the component does.

`fullName` string The component developer name used as a unique identifier for API access. The
`fullName` can contain only underscores and alphanumeric characters. It must

be unique, begin with a letter, not include spaces, not end with an underscore,
and not contain two consecutive underscores. This field is inherited from the
Metadata component.

`label` string Required. The label for this component.

`packageVersions` PackageVersion[]

The list of installed managed package versions that are referenced by this
Visualforce component.

Package components and Visualforce custom component are distinct concepts.
A package is comprised of many elements, such as custom objects, Apex classes
and triggers, and custom pages and components.

[For more information about managed packages, see Second-Generation](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_dev2gp.htm)
[Managed Packages in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_dev2gp.htm) _Salesforce DX Developer Guide_ . This field is available in
API version 16.0 and later.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

ApexPage

### ApexEmailNotifications

The ApexEmailNotifications type allows you to define users and email addresses that receive email for unhandled Apex errors. Flow
errors can also use this metadata type.


Metadata Types ApexEmailNotifications

Declarative Metadata File Suffix and Directory Location

The component filename is `apexEmailNotifications.notifications` . The Apex email notification file is stored in the
`apexEmailNotifications` folder in the corresponding package directory.

Version

ApexEmailNotifications components are available in API version 49.0 and later.

Fields

**Field Name** **Field Type** **Description**

`apexEmailNotification` ApexEmailNotification A specific Apex email notification. You can specify multiple notifications.

ApexEmailNotification

Represents an Apex email notification.

Note: Each ApexEmailNotification can contain an email or a user but not both.

**Field Name** **Field Type** **Description**

`email` string The external email address to which the notification is sent. Mutually exclusive
with the `user` field.

`user` string The username of the Salesforce user to be notified. Mutually exclusive with the
`email` field.

Usage

Deploying ApexEmailNotifications deletes all previous notifications in the org. For example, consider two notifications, test1@example.com
and test2@example.com, that are deployed in an org. When the following `apexEmailNotifications.notifications` is
deployed, test1@example.com is deleted, because it's not in the deployed list.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ApexEmailNotifications xmlns="http://soap.sforce.com/2006/04/metadata">

      <apexEmailNotification>

        <email>test2@example.com</email>

      </apexEmailNotification>

   </ApexEmailNotifications>

```

Note: The ApexEmailNotifications metadata type isn't supported in `destructiveChanges.xml` . To delete specific
ApexEmailNotification items, deploy a new ApexEmailNotifications without those items. To delete all Apex email notifications in
an org, deploy an empty list of ApexEmailNotifications.


### Metadata Types ApexPage

Declarative Metadata Sample Definition

To deploy Apex email notifications, you can specify either the exact file name or use a wildcard in `package.xml` .

This example specifies the exact file name in `package.xml` .

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>apexEmailNotifications</members>

        <name>ApexEmailNotifications</name>

      </types>

      <version>49.0</version>

   </Package>

```

This example uses a wildcard in `package.xml` .

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ApexEmailNotifications</name>

      </types>

      <version>49.0</version>

   </Package>

```

This sample deploys an Apex email notification that notifies a Salesforce user in the org.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ApexEmailNotifications xmlns="http://soap.sforce.com/2006/04/metadata">

      <apexEmailNotification>

        <user>user1@example.com</user>

      </apexEmailNotification>

   </ApexEmailNotifications>

```

This sample deploys an Apex email notification that notifies an external email address.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ApexEmailNotifications xmlns="http://soap.sforce.com/2006/04/metadata">

      <apexEmailNotification>

        <email>test@example.com</email>

      </apexEmailNotification>

   </ApexEmailNotifications>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### ApexPage

Represents a Visualforce page.

For more information, see _Visualforce_ in Salesforce Help. This type extends the MetadataWithContent metadata type and inherits its
`content` and `fullName` fields.


Metadata Types ApexPage

Declarative Metadata File Suffix and Directory Location

The file suffix is `.page` for the page file. The accompanying metadata file is named _`PageName`_ `-meta.xml` .

Visualforce pages are stored in the `pages` folder in the corresponding package directory.

Version

Visualforce pages are available in API version 11.0 and later.

Fields

This metadata type contains the following fields:

**Field Name** **Field Type** **Description**

`apiVersion` double

Required. The API version for this page. Every page has an API version
specified at creation. This field is available in API version 15.0 and later.
If you set this field to a number lower than 15.0, it’s changed to 15.0.

`content` base64Binary The page content. Base 64-encoded binary data. Before making an
API call, client applications must encode the binary attachment data

as base64. Upon receiving a response, client applications must decode
the base64 data to binary. This conversion is handled for you by a
SOAP client. This field is inherited from the MetadataWithContent
component.

`description` string A description of what the page does.

`fullName` string The page developer name used as a unique identifier for API access.
The `fullName` can contain only underscores and alphanumeric

characters. It must be unique, begin with a letter, not include spaces,
not end with an underscore, and not contain two consecutive
underscores. This field is inherited from the Metadata component.

`availableInTouch` boolean Indicates if Visualforce tabs associated with the Visualforce page can
be used in the Salesforce mobile app. (Use of this field for Salesforce

Touch is deprecated.). This field is available in API version 27.0 and
later.

Standard object tabs that are overridden with a Visualforce page aren’t
supported in the Salesforce mobile app, even if you set this field for
the page. The default page for the object is displayed instead of the
Visualforce page.

`confirmationTokenRequired` boolean

Indicates whether `GET` requests for the page require a CSRF
confirmation token. This field is available in API version 28.0 and later.

If you change this field’s value from `false` to `true`, links to the
page require a CSRF token to be added to them, or the page is
inaccessible.

`label` string Required. The label for this page.


### Metadata Types ApexTestSuite

**Field Name** **Field Type** **Description**

`packageVersions` PackageVersion[]

The list of installed managed package versions that are referenced by
this Visualforce page.

For more information about managed packages, see
[Second-Generation Managed Packages in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_dev2gp.htm) _Salesforce DX Developer_
_Guide_ . This field is available in API version 16.0 and later.

Declarative Metadata Sample Definition

The following sample creates the `MyPage.page` page, and the corresponding `MyPage.page-meta.xml` metadata file.

`SampleApexPage.page` file:

```
<apex:page>

<h1>Congratulations</h1>

This is your new Page.

</apex:page>

```

`SampleApexPage.page-meta.xml` :

```
<?xml version="1.0" encoding="UTF-8"?>

<ApexPage xmlns="http://soap.sforce.com/2006/04/metadata">

   <description>This is a sample Visualforce page.</description>

   <label>SampleApexPage</label>

</ApexPage>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

ApexComponent

### ApexTestSuite

Represents a suite of Apex test classes to include in a test run.

File Suffix and Directory Location

### ApexTestSuite components have the suffix .testSuite and are stored in the testSuites folder.

Version

### ApexTestSuite components are available in API version 38.0 and later.


Metadata Types ApexTestSuite

Fields

**Field Name** **Field Type** **Description**

`testClassName` string[] A list of Apex test classes, specified by name, to include in this
test suite.

Declarative Metadata Sample Definition

To include namespaced tests in an Apex test suite, specify each namespace individually. Local Apex tests consist of all tests in the org
that don’t originate from managed packages.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ApexTestSuite xmlns="http://soap.sforce.com/2006/04/metadata">

     <testClassName> LocalTestClass </testClassName>

       <!-- LocalTestClass adds the test class named LocalTestClass. -->

     <testClassName> A*Class </testClassName>

       <!-- A*Class adds AClass, AnotherClass, AwesomeClass, and so on. -->

     <testClassName> Namespace1.NamespacedTestClass </testClassName>

     <testClassName>*</testClassName> <!-- Adds all local tests. -->

     <testClassName> Namespace1 .*</testClassName> <!-- Adds all tests in Namespace1. -->

     <testClassName> Namespace2 .*</testClassName> <!-- Adds all tests in Namespace2. -->

   </ApexTestSuite>

```

These syntaxes are supported in `package.xml` . If the test classes in your suites are already present in the target org, you can omit
the `ApexClass` type in `package.xml` .

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <types>

       <members>*</members>

       <name>ApexClass</name>

     </types>

     <types>

       <members>*</members>

       <name>ApexTestSuite</name>

     </types>

     <version>38.0</version>

   </Package>

   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <types>

       <members>*</members>

       <name>ApexClass</name>

     </types>

     <types>

       <members> Suite1 </members>

       <members> Suite2 </members>

       <name>ApexTestSuite</name>

     </types>

```


### Metadata Types ApexTrigger

```
     <version>38.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### ApexTrigger

Represents an Apex trigger. A trigger is Apex code that executes before or after specific data manipulation language (DML) events occur,
such as before object records are inserted into the database, or after records have been deleted.

For more information, see “Manage Apex Triggers” in Salesforce Help. This type extends the MetadataWithContent metadata type and
inherits its `content` and `fullName` fields.

Supported Calls

All Metadata API calls except CRUD-Based Calls, which prevents deployment outside of proper deployment lifecycle and test-execution
constraints.

Declarative Metadata File Suffix and Directory Location

The file suffix is `.trigger` for the trigger file. The accompanying metadata file is named _`TriggerName`_ `-meta.xml` .

Apex triggers are stored in the `triggers` folder in the corresponding package directory.

Version

Triggers are available in API version 10.0 and later.

Fields

This metadata type contains the following fields:

**Field Name** **Field Type** **Description**

`apiVersion` double Required. The API version for this trigger. Every trigger has an API version specified
at creation.

`content` base64 The Apex trigger definition. This field is inherited from the MetadataWithContent
component.

`fullName` string The Apex trigger name. The name can only contain characters, letters, and the
underscore (_) character, must start with a letter, and can’t end with an

underscore or contain two consecutive underscore characters. This field is
inherited from the Metadata component.


### Metadata Types AppMenu

**Field Name** **Field Type** **Description**

`packageVersions` PackageVersion[]

The list of installed managed package versions that are referenced by this Apex
trigger.

[For more information about managed packages, see the Second-Generation](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp.htm)
[Managed Packaging Developer Guide. This field is available in API version 16.0](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/sfdx_dev_dev2gp.htm)
and later.

`status` ApexCodeUnitStatus Required. The status of the Apex trigger. The following string values are valid:
(enumeration of type string)

**•** `Active`                    - The trigger is active.

**•** `Inactive`                     - The trigger is inactive, but not deleted.

**•** `Deleted`                     - The trigger is marked for deletion. Useful for managed packages,
because it allows a trigger to be deleted when a managed package is
updated.

Declarative Metadata Sample Definition

The following sample creates the `MyhelloWorld.trigger` trigger, and the corresponding
`MyHelloWorld.trigger-meta.xml` metadata file.

`MyHelloWorld.trigger` file:

```
trigger helloWorldAccountTrigger on Account (before insert) {

  Account[] accs = Trigger.new;

  MyHelloWorld.addHelloWorld(accs);

}

```

`MyHelloWorld.trigger-meta.xml` :

```
<?xml version="1.0" encoding="UTF-8"?>

<ApexTrigger xmlns="http://soap.sforce.com/2006/04/metadata">

   <apiVersion>66.0</apiVersion>

</ApexTrigger>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

ApexClass

### AppMenu

Represents the app menu or the Salesforce mobile navigation menu. Reserved for future use.


### Metadata Types AppointmentAssignmentPolicy AppointmentAssignmentPolicy

Represents the information about a resource assignment rule. This type extends the Metadata metadata type and inherits its `fullName`
field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### AppointmentAssignmentPolicy components have the suffix .policy and are stored in the appointmentSchedulingPolicies

folder.

Version

AppointmentSchedulingPolicy components are available in API version 53.0 and later.

Fields

**Field Name** **Field Type** **Description**

`masterLabel` string Required. The label for the appointment assignment policy.

`policyApplicableDuration` string Required. The frequency at which the utilization of service resources is
calculated. Valid values are:

**•** `Monthly`

**•** `ParameterBased`

**•** `Weekly`

`policyType` string Required. The type of appointment assignment policy. Valid value is:

**•** `loadBalancing`

`utilizationFactor` string Required. Specifies the count type for the resource utilization. Valid values
are:

**•** `NumberOfAppointments`

**•** `TotalAppointmentDuration`

Declarative Metadata Sample Definition

The following is an example of an appointmentAssignmentPolicy component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <AppointmentAssignmentPolicy xmlns="http://soap.sforce.com/2006/04/metadata">

     <masterLabel>loadBalancing Assignment Policy</masterLabel>

     <policyType>loadBalancing</policyType>

```


### Metadata Types AppointmentSchedulingPolicy

```
     <policyApplicableDuration>Weekly</policyApplicableDuration>

     <utilizationFactor>TotalAppointmentDuration</utilizationFactor>

   </AppointmentAssignmentPolicy>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <types>

      <members>sample</members>

      <name>AppointmentAssignmentPolicy</name>

     </types>

     <version>53.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### AppointmentSchedulingPolicy

Represents a set of rules for scheduling appointments using Lightning Scheduler. This type extends the Metadata metadata type and
inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### AppointmentSchedulingPolicy components have the suffix .policy and are stored in the appointmentSchedulingPolicies

folder.

Version

### AppointmentSchedulingPolicy components are available in API version 47.0 and later.

Special Access Rules

You must have the ViewSetup and CustomizeApplication user permissions to access the AppointmentSchedulingPolicy type.

Fields

**Field Name** **Field Type** **Description**

`appointmentAssignmentPolicy` string The name of the appointment assignment policy. This field is available
in API version 53.0 and later.


Metadata Types AppointmentSchedulingPolicy

**Field Name** **Field Type** **Description**

`appointmentStartTimeInterval` picklist Required. The proposed time interval in minutes between appointment
start times. For example, if you set the interval to `15`, appointments can

then begin at the top of the hour and at 15-minute intervals thereafter
(10:00 AM, 10:15 AM, 10:30 AM, and so on). Valid values are:

**•** `5`

**•** `10`

**•** `15`

**•** `20`

**•** `30`

**•** `45`

**•** `60`

**•** `90`

**•** `120`

**•** `150`

**•** `180`

**•** `240`

**•** `300`

**•** `360`

**•** `420`

**•** `480`

`extCalEventHandler` lookup Required. The API name of the custom Apex class that checks service
resources’ external calendar events and returns the time slots where

service resources are already booked. Available in API version 50.0 and
later.

`isSvcTerritoryMemberShiftUsed` boolean Required. Indicates whether to consider shifts of service territory
members when determining the availability of service resources for

appointments ( `true` ) or not ( `false` ). This field is available in API
version 54.0 and later.

`isSvcTerrOpHoursWithShiftsUsed` boolean Required. Indicates whether to consider the intersection of shifts and
service territory operating hours when determining the availability of

service resources for appointments ( `true` ) or not ( `false` ). This field
is available in API version 54.0 and later.

`masterLabel` string Required. The label for the appointment scheduling policy.

`shouldCheckExternalCalendar` boolean

`shouldConsiderCalendarEvents` boolean

Required. Indicates whether to check the external calendar for resource
availability ( `true` ) or not ( `false` ). This field is available in API version
53.0 and later.

Required. Indicates whether to consider events on the Salesforce calendar
to determine the availability of service resources to be assigned to
appointments ( `true` ) or not ( `false` ).


Metadata Types AppointmentSchedulingPolicy

**Field Name** **Field Type** **Description**

`shouldEnforceExcludedResource` boolean

`shouldEnforceRequiredResource` boolean

`shouldMatchSkill` boolean

`shouldMatchSkillLevel` boolean

`shouldRespectVisitingHours` boolean

`shouldUsePrimaryMembers` boolean

`shouldUseSecondaryMembers` boolean

Required. Indicates whether this appointment scheduling policy prevents
excluded service resources from being assigned to appointments ( `true` )
or not ( `false` ).

Required. Indicates whether this appointment scheduling policy allows
only required service resources to be assigned to appointments ( `true` )
or not ( `false` ).

Required. Indicates whether this appointment scheduling policy allows
only required service resources who have certain skills to be assigned
to appointments ( `true` ) or not ( `false` ).

Required. Indicates whether this appointment scheduling policy allows
only required service resources who have certain skills and skill levels to
be assigned to appointments ( `true` ) or not ( `false` ).

Required. Indicates whether this appointment scheduling policy prevents
users from scheduling appointments outside of an account’s visiting
hours ( `true` ) or not ( `false` ).

Required. Indicates whether this appointment scheduling policy allows
only service resources who are primary members of a service territory
to be assigned to appointments ( `true` ) or not ( `false` ).

Required. Indicates whether this appointment scheduling policy allows
service resources who are secondary members of a service territory to
be assigned to appointments ( `true` ) or not ( `false` ).

Declarative Metadata Sample Definition

The following is an example of an appointmentSchedulingPolicy component.

```
<?xml version="1.0" encoding="UTF-8"?>

<AppointmentSchedulingPolicy xmlns="http://soap.sforce.com/2006/04/metadata">

  <appointmentAssignmentPolicy>ResourceAssignmentRule1</appointmentAssignmentPolicy>

  <appointmentStartTimeInterval>15</appointmentStartTimeInterval>

  <masterLabel>Default Appointment Scheduling Policy</masterLabel>

  <shouldCheckExternalCalendar>true</shouldCheckExternalCalendar>

  <shouldConsiderCalendarEvents>true</shouldConsiderCalendarEvents>

  <shouldEnforceExcludedResource>true</shouldEnforceExcludedResource>

  <shouldEnforceRequiredResource>true</shouldEnforceRequiredResource>

  <shouldMatchSkill>true</shouldMatchSkill>

  <shouldMatchSkillLevel>false</shouldMatchSkillLevel>

  <shouldRespectVisitingHours>true</shouldRespectVisitingHours>

  <shouldUsePrimaryMembers>true</shouldUsePrimaryMembers>

  <shouldUseSecondaryMembers>true</shouldUseSecondaryMembers>

</AppointmentSchedulingPolicy>

```

The following is an example `package.xml` that references the previous definition.


### Metadata Types ApprovalProcess

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <types>

      <members>sample</members>

      <name>AppointmentSchedulingPolicy</name>

     </types>

     <version>47.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### ApprovalProcess

Represents the metadata associated with an approval process. An approval process automates how records are approved in Salesforce.
An approval process specifies each step of approval, including who to request approval from and what to do at each point of the process.

This type extends the Metadata metadata type and inherits its `fullName` field.

Note:

**•** To use approval processes on Salesforce Knowledge articles with the Metadata API, the article type must be deployed. For
article version (_kav) in approval processes, the supported action types are: Knowledge Action, Email Alert, Field Update, and
Outbound Message.

**•** Send actions and approval processes for email drafts aren’t supported in the Metadata API.

**•** The metadata doesn’t include the order of active approval processes. Sometimes you have to reorder the approval processes
in the destination org after deployment.

File Suffix and Directory Location

### ApprovalProcess components have the suffix .approvalProcess and are stored in the approvalProcesses folder.

Version

### ApprovalProcess components are available in API version 28.0 and later.

Fields

**Field Name** **Field Type** **Description**

`active` boolean

Required. Whether the approval process is active.

After an approval process is activated, you can’t add, delete,
or change the order of the steps or change its reject or skip
behavior, even if the process is inactive.


Metadata Types ApprovalProcess

**Field Name** **Field Type** **Description**

`allowRecall` boolean

Whether to allow submitters to recall approval requests.

If set to `false`, only administrators can recall approval
requests.

`allowedSubmitters` ApprovalSubmitter[] Required. An array of users who are allowed to submit records
for approval.

`approvalPageFields` ApprovalPageField

Specifies which fields to display on the approval page, where
the approver goes to approve or reject the record. By default,
the approval page displays the following:

**•** `Name` field

**•** `Owner` field (except for child objects)

If you enable notifications in the Salesforce mobile app, keep
in mind that approvers can view this list of fields on a mobile
device. Select only the fields necessary for users to decide
whether to approve or reject records.

`approvalStep` ApprovalStep[] An array of approval step definitions.

`description` string Describes the approval process.

`emailTemplate` string

Specifies which Classic email template to use for approval
requests. If not specified, the default email template is used.

Lightning email templates aren’t packageable. We recommend
using a Classic email template.

When an approval process assigns an approval request to a
user, Salesforce sends the user an approval request email.

`enableMobileDeviceAccess` boolean Whether users can access an external version of the approval
page from any browser, including browsers on mobile devices,

without logging in to Salesforce. Corresponds to `Security`
`Settings` in the user interface.

If set to `true`, approval steps can’t have approvers of `type`
`adhoc` .

If set to `false`, approvers must log in to Salesforce to access
the approval page.

`entryCriteria` ApprovalEntryCriteria

Determines which records can enter the approval process.
Exclude this field to allow all records to enter the approval
process.

When you deploy an approval process with no entry criteria
to overwrite an existing approval process with entry criteria,

then the entry criteria from the existing process are applied
to the deployed process.


Metadata Types ApprovalProcess

**Field Name** **Field Type** **Description**

`finalApprovalActions` ApprovalAction Specifies which workflow actions to execute when all required
approvals have been given for a record.

`finalApprovalRecordLock` boolean Whether to keep the record locked after it receives all necessary
approvals. Default: `false` .

`finalRejectionActions` ApprovalAction Specifies which workflow actions to execute after a record
enters the final rejection state.

`finalRejectionRecordLock` boolean Whether to keep the record locked after it’s finally rejected.
Default: `false` .

`initialSubmissionActions` ApprovalAction Specifies which workflow actions to execute when a record is
initially submitted for approval.

`label` string Required. Name of the approval process.

`nextAutomatedApprover` NextAutomatedApprover

`postTemplate` string

Specifies a standard or custom user hierarchy field that can be
used to automatically assign the approver for an approval step.

If you exclude this field, then no approval step can use a user
hierarchy field to automatically assign the approver.

Post template to use for Approvals in Chatter.

Chatter post approval notifications are only available for
approval processes associated with an object that has been
enabled for feed tracking.

`recallActions` ApprovalAction Specifies which workflow actions to execute when a pending
approval request is withdrawn.

`recordEditability` RecordEditabilityType Specifies which users can edit records that are pending
(enumeration of type string) approval. When a record is submitted for approval, it’s

automatically locked to prevent other users from editing it
during the approval process. Valid values are:

**•** `AdminOnly` —Records pending approval can be edited
by:

**–** Users with the “Modify All Data” permission

**–** Users with the “Modify All Records” object-level
permission for the given object

**•** `AdminOrCurrentApprover` —Records pending
approval can be edited by:

**–** Users with the “Modify All Data” permission

**–** Users with the “Modify All Records” object-level
permission for the given object

**–** The assigned approver, who must have edit access to
the record through user permissions and the
organization-wide sharing defaults for the given object


Metadata Types ApprovalProcess

**Field Name** **Field Type** **Description**

`showApprovalHistory` boolean Whether to add the Approval History related list to the
approval page, which is where the approver can view the

approval request details and approve or reject the record. The
Approval History related list tracks a record through the
approval process.

If you also want to add the Approval History related list to
record detail and edit pages, use the Salesforce user interface
to customize the page layouts for the given object.

ApprovalSubmitter

Represents a user or set of users who can submit records for approval.

**Field Name** **Field Type** **Description**

`submitter` string

Identifies a specific user or set of users who can submit records for approval. This field
is required, except when the following types are specified and the `submitter`
field is ignored:

**•** `owner`

**•** `creator`

**•** `allInternalUsers`

Example:

```
<allowedSubmitters>

   <type>allInternalUsers</type>

</allowedSubmitters>

<allowedSubmitters>

   <submitter>myGroup</submitter>

   <type>group</type>

</allowedSubmitters>

```

```
type

```

ProcessSubmitterType Required. Type of user or set of users who can submit records for approval. Valid values
(enumeration of type are:
string)

**•** `group`

**•** `role`

**•** `user`

**•** `roleSubordinates`

**•** `roleSubordinatesInternal`

**•** `owner`

**•** `creator`

**•** `partnerUser`

**•** `customerPortalUser`

**•** `portalRole`


Metadata Types ApprovalProcess

**Field Name** **Field Type** **Description**

**•** `portalRoleSubordinates`

**•** `allInternalUsers` —all Salesforce users in the organization

ApprovalPageField

Represents the selection of fields to display on the approval page, where an approver can view the approval request details and approve
or reject the record.

**Field Name** **Field Type** **Description**

`field` string[] An array of fields that are displayed on the page for the approver to approve
or reject the record.

ApprovalStep

Represents a step in the approval process. Approval steps define the chain of approval for a particular approval process. Each step
determines which records can advance to that step, who to assign approval requests to, and whether to let each approver’s delegate
respond to the requests. The first step specifies what to do if a record doesn’t advance to that step. Later steps specify what happens if
an approver rejects the request.

Note:

**•** The order of the `ApprovalStep` entries in the approval process definition determines the order in which the approval
steps are executed.

**•** After an approval process is activated, you can’t add, delete, or change the order of the steps or change its reject or skip
behavior, even if the process is inactive.

**•** Each approval process supports up to 30 steps.

**Field Name** **Field Type** **Description**

`allowDelegate` boolean

Whether to allow delegated approvers in this step of the
approval process. A delegated approver is a user appointed by
an assigned approver as an alternate for approval requests.

`approvalActions` ApprovalAction Specifies which workflow actions to execute when a record is
approved in this step of the approval process.

`assignedApprover` ApprovalStepApprover Specifies the assigned approvers for this step of the approval
process.

`description` string Describes the approval step.

`entryCriteria` ApprovalEntryCriteria Determines which records can enter this step of the approval
process.


Metadata Types ApprovalProcess

**Field Name** **Field Type** **Description**

`ifCriteriaNotMet` StepCriteriaNotMetType Specifies what to do for records that don't meet the entry
(enumeration of type string) criteria. Valid values are:

**•** `ApproveRecord` —Approve the request and execute
all final approval actions.

**•** `RejectRecord` —Reject the request and execute all
final rejection actions. This option is available only for the
first step in the approval process.

**•** `GotoNextStep` —Skip to the next approval step. If you
select this option for the first approval step, and a record
doesn’t meet the entry criteria for any other step, the record
is rejected.

`label` string Required. Name of the approval step.

`name` string Required. Unique name of the approval step. It must contain
only underscores and alphanumeric characters, begin with a

letter, not include spaces, not end with an underscore, and not
contain two consecutive underscores. The requirement for
uniqueness is only within the specific approval process.

`rejectBehavior` ApprovalStepRejectBehavior Required, except for the first step in the approval process.
Specifies what happens if the approver rejects the request

during this approval step, unless it's the first step in the approval
process.

If the approver rejects the request in the first step in the approval
process, the reject behavior is determined by the
`finalRejectionActions` .

`rejectionActions` ApprovalAction Specifies which workflow actions to execute when a record is
rejected in this step of the approval process.

ApprovalAction

Represents the actions that occur as a result of an approval process.

**Field Name** **Field Type** **Description**

`action` WorkflowActionReference[] An array of workflow actions to execute.

ApprovalStepApprover

Represents the assigned approvers for an approval step. Each step supports up to 25 approvers.

**Field Name** **Field Type** **Description**

`approver` Approver[] An array of assigned approvers for this step of the approval process.


Metadata Types ApprovalProcess

**Field Name** **Field Type** **Description**

```
whenMultipleApprovers

```

Approver

RoutingType Specifies how to handle approval or rejection when multiple approvers
(enumeration of are assigned to the step. Valid values are:
type string)

**•** `Unanimous` —(Default) Require unanimous approval from all
approvers for this step. If any of the approvers reject the request, the
approval request for this step is rejected.

**•** `FirstResponse` —Approve or reject based on the first response.

Represents an assigned approver for an approval step. Check out _Considerations for Setting Approvers_ in Salesforce Help.

**Field Name** **Field Type** **Description**

`name` string Identifies an assigned approver. This field is required, except when the `type` is one of
the following and the `name` is ignored:

**•** `adhoc`

**•** `userHierarchyField`

```
type

```

NextOwnerType Combined with the specified `name`, `type` identifies an assigned approver. Valid values
(enumeration of type are:
string)

**•** `adhoc` —The approver for the step must be selected manually. For the first step, the
submitter selects the approver. For the second and later steps, the approver for the
previous step selects the approver. For this value, exclude the `name` field.

**•** `user` —A user in your organization. For this value, enter a username for the `name`
field.

**•** `userHierarchyField` —A user specified in a standard or custom user hierarchy
field, such as the standard `Manager` field. For this value, exclude the `name` field.
The user hierarchy field must be defined in the nextAutomatedApprovers for the
approval process.

**•** `relatedUserField` —A user specified in a user lookup field on the submitted
record, such as the `Last Modified By` field. For this value, enter the name of
the user lookup field for the `name` field.

**•** `queue` —Automatically assign to a queue. For this value, enter the name of the queue
for the `name` field.

ApprovalEntryCriteria

Represents the criteria that records must meet to enter the approval process or an approval step. Specify either filter criteria or a formula,
but not both.

**Field Name** **Field Type** **Description**

`booleanFilter` string Filter logic for `criteriaItems` . Exclude this field if you enter a `formula` .


Metadata Types ApprovalProcess

**Field Name** **Field Type** **Description**

`criteriaItems` FilterItem[]

Filter criteria that a record must meet to enter the approval process or approval
step.

Approval processes don’t support `valueField` entries in filter criteria.

`formula` string Formula that must evaluate to true for a record to enter the approval process
or approval step.

ApprovalStepRejectBehavior

Represents what happens if the approver rejects the request during this approval step, unless it's the first step in the approval process.
For the first step in the approval process, the reject behavior is determined by the approval process's final rejection actions.

**Field Name** **Field Type** **Description**

`type` StepRejectBehaviorType Not allowed in the first step of the approval process. Valid values are:
(enumeration of type string)

**•** `RejectRequest` —Rejects the request even if previous steps were approved.
Salesforce performs all rejection actions specified for this step and all final rejection
actions.

**•** `BackToPrevious` —Rejects the request, and returns the approval request to
the previous approver. Salesforce performs all rejection actions specified for this
step.

NextAutomatedApprover

Represents the user hierarchy field to use as the next automated approver for the approval process. If defined, the user specified in the
hierarchy field can be automatically assigned as the approver in one or more approval steps.

**Field Name** **Field** **Description**
**Type**

`useApproverFieldOfRecordOwner` boolean Required. Whether the first executed approval step uses the specified
`userHierarchyField` in the record owner’s user record—instead

of the submitter’s user record—as the approver. All remaining steps use
the specified `userHierarchyField` in the user record of the
preceding step’s approver.

`userHierarchyField` string Required. Standard or custom user hierarchy field whose value specifies
which user to assign as the approver. For example, the standard

`Manager` hierarchy field can be used to assign approvers for employee
PTO (paid time off) requests.


Metadata Types ApprovalProcess

Declarative Metadata Sample Definition

The following is an example of an ApprovalProcess component:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ApprovalProcess xmlns="http://soap.sforce.com/2006/04/metadata">

      <active>false</active>

      <allowRecall>false</allowRecall>

      <allowedSubmitters>

        <type>owner</type>

      </allowedSubmitters>

      <allowedSubmitters>

        <submitter>USSalesRep</submitter>

        <type>role</type>

      </allowedSubmitters>

      <allowedSubmitters>

        <submitter>MarketingGroup</submitter>

        <type>group</type>

      </allowedSubmitters>

      <allowedSubmitters>

        <submitter>kcooper@example.com</submitter>

        <type>user</type>

      </allowedSubmitters>

      <approvalPageFields>

        <field>Name</field>

        <field>Owner</field>

        <field>MyLeadCustomField__c</field>

        <field>Address</field>

      </approvalPageFields>

      <approvalStep>

        <allowDelegate>false</allowDelegate>

        <approvalActions>

           <action>

             <name>LeadApprovedTask1</name>

             <type>Task</type>

           </action>

           <action>

             <name>LeadApprovedTask2</name>

             <type>Task</type>

           </action>

        </approvalActions>

        <assignedApprover>

           <approver>

             <type>adhoc</type>

           </approver>

        </assignedApprover>

        <label>Step1</label>

        <name>Step1</name>

        <rejectionActions>

           <action>

             <name>LeadRejectedTask</name>

             <type>Task</type>

           </action>

        </rejectionActions>

      </approvalStep>

```


Metadata Types ApprovalProcess

```
      <approvalStep>

        <allowDelegate>false</allowDelegate>

        <assignedApprover>

           <approver>

             <type>userHierarchyField</type>

           </approver>

        </assignedApprover>

        <entryCriteria>

           <criteriaItems>

             <field>Lead.CreatedDate</field>

             <operation>greaterThan</operation>

             <value>3/25/2013</value>

           </criteriaItems>

           <criteriaItems>

             <field>User.IsActive</field>

             <operation>notEqual</operation>

             <value>true</value>

           </criteriaItems>

        </entryCriteria>

        <ifCriteriaNotMet>ApproveRecord</ifCriteriaNotMet>

        <label>Step2</label>

        <name>Step2</name>

        <rejectBehavior>

           <type>RejectRequest</type>

        </rejectBehavior>

      </approvalStep>

      <approvalStep>

        <allowDelegate>true</allowDelegate>

        <assignedApprover>

           <approver>

             <name>MarketingTeamQueue</name>

             <type>queue</type>

           </approver>

           <approver>

             <name>LastModifiedBy</name>

             <type>relatedUserField</type>

           </approver>

           <approver>

             <name>awheeler@example.com</name>

             <type>user</type>

           </approver>

           <whenMultipleApprovers>FirstResponse</whenMultipleApprovers>

        </assignedApprover>

        <entryCriteria>

           <formula>CONTAINS( MyLeadCustomField__c, 'Salesforce')</formula>

        </entryCriteria>

        <label>Step3</label>

        <name>Step3</name>

        <rejectBehavior>

           <type>BackToPrevious</type>

        </rejectBehavior>

      </approvalStep>

      <emailTemplate>MyFolder/LeadsNewassignmentnotification</emailTemplate>

      <enableMobileDeviceAccess>false</enableMobileDeviceAccess>

```


Metadata Types ApprovalProcess

```
      <entryCriteria>

        <criteriaItems>

           <field>Lead.AnnualRevenue</field>

           <operation>greaterThan</operation>

           <value>10500</value>

        </criteriaItems>

        <criteriaItems>

           <field>Lead.MyLeadCustomField__c</field>

           <operation>equals</operation>

           <value>Salesforce</value>

        </criteriaItems>

      </entryCriteria>

      <finalApprovalActions>

        <action>

           <name>LeadEmailContacted</name>

           <type>Alert</type>

        </action>

      </finalApprovalActions>

      <finalApprovalRecordLock>true</finalApprovalRecordLock>

      <finalRejectionActions>

        <action>

           <name>ProcessRejectedMessageAction</name>

           <type>OutboundMessage</type>

        </action>

      </finalRejectionActions>

      <finalRejectionRecordLock>false</finalRejectionRecordLock>

      <initialSubmissionActions>

        <action>

           <name>LeadFieldUpdate</name>

           <type>FieldUpdate</type>

        </action>

        <action>

           <name>NewLeadEmail</name>

           <type>Alert</type>

        </action>

      </initialSubmissionActions>

      <label>SampleProcess</label>

      <nextAutomatedApprover>

        <useApproverFieldOfRecordOwner>false</useApproverFieldOfRecordOwner>

        <userHierarchyField>customlookupuserfield__c</userHierarchyField>

      </nextAutomatedApprover>

      <postTemplate>MyPostTemplate</postTemplate>

      <recallActions>

        <action>

           <name>ProcessRecalledMessageAction</name>

           <type>OutboundMessage</type>

        </action>

      </recallActions>

      <recordEditability>AdminOnly</recordEditability>

      <showApprovalHistory>false</showApprovalHistory>

   </ApprovalProcess>

```


### Metadata Types AssignmentRules

Wildcard Support in the Manifest File

Use the wildcard character `*` (asterisk) in the `package.xml` manifest file to retrieve all approval processes for all objects. You can’t
use it to retrieve a subset of approval processes. Syntax such as `Lead.*` isn’t supported. For information about using the manifest file,
see Deploying and Retrieving Metadata with the Zip File.

### AssignmentRules

Represents assignment rules that allow you to automatically route cases to the appropriate users or queues. You can access rules metadata
for all applicable objects, for a specific object, or for a specific rule on a specific object.

The `package.xml` syntax for accessing all assignment rules for all objects is:

```
      <types>

        <members>*</members>

        <name>AssignmentRules</name>

      </types>

```

All rules for a specific object use a similar syntax without the wildcard. For example, all assignment rules for the Case object would use
this syntax:

```
      <types>

        <members>Case</members>

        <name>AssignmentRules</name>

      </types>

```

You can also access specific assignment rules for an object. The following example only accesses the “samplerule” and “newrule”
### assignment rules on the Case object. Notice that for this example the type name syntax is AssignmentRule and not AssignmentRules .

```
      <types>

        <members>Case.samplerule</members>

        <members>Case.newrule</members>

        <name>AssignmentRule</name>

      </types>

```

File Suffix and Directory Location

Assignment rules for an object have the suffix `.assignmentRules` and are stored in the `assignmentRules` folder. For example,
all Case assignment rules are stored in the `Case.assignmentRules` file.

Version

### AssignmentRules components are available in API version 27.0 and later.

Fields

**Field Name** **Field Type** **Description**

`assignmentRule` AssignmentRule[] Represents the definitions of the named assignment rules.


Metadata Types AssignmentRules

AssignmentRule

Specifies whether the rule is active or not and its definition. Rules are processed in the order they appear within the AssignmentRules
container.

**Field Name** **Field Type** **Description**

`active` boolean Indicates whether the assignment rule is active ( `true` ) or
not ( `false` ).

`fullname` string Inherited from Metadata, this field is defined in the WSDL
for this metadata type. It must be specified when creating,

updating, or deleting. See `createMetadata()` to see
an example of this field specified for a call.

This value can't be `null` .

`ruleEntry` `RuleEntry[]` Represents the type and description for the assignment
rule.

RuleEntry

Represents the fields used by the rule.

**Field Name** **Field Type** **Description**

`assignedTo` string The name of the user or queue the item is assigned to.

`assignedToType` `AssignToLookupValueType` Valid values are:
(enumeration of type string)

**•** `User`

**•** `Queue`

`booleanFilter` string Advanced filter conditions that were specified for the rule.

`criteriaItems` `FilterItem[]` The items in the list that define the assignment criteria.

`formula` string

The validation formula.

Specify either `formula` or `criteriaItems`, but not
both fields.

`notifyCcRecipients` boolean Specifies whether email addresses included on the Cc line
of an incoming Email-to-Case or Web-to-Lead message are

included on the Cc line of the auto-response to that
message ( `true` ) or not ( `false` ). Available in API version
32.0 and later.

`overrideExistingTeams` boolean

Specifies whether the case team resets when the
assignment is done `true` ) or if the current team is added
to the case instead of replacing the previous team ( `false` ).

`team` string[] The name of the case team. It can occur 0 or more times.


Metadata Types AssignmentRules

**Field Name** **Field Type** **Description**

`template` string

Declarative Metadata Sample Definition

Specifies the template to use for the email that is
automatically sent to the designated recipient.

Lightning email templates aren’t packageable. We
recommend using a Classic email template.

The following is an example file showing two assignment rules on the Case object:

```
<AssignmentRules xmlns="http://soap.sforce.com/2006/04/metadata"

xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

   <assignmentRule>

     <fullName>samplerule</fullName>

     <active>false</active>

     <ruleEntry>

        <assignedTo>testUser@org.com</assignedTo>

        <assignedToType>User</assignedToType>

        <criteriaItems>

          <field>Case.IsEscalated</field>

          <operation>equals</operation>

          <value>True</value>

        </criteriaItems>

        <template>emailtemplate</template>

     </ruleEntry>

   </assignmentRule>

   <assignmentRule>

     <fullName>Another samplerule</fullName>

     <active>false</active>

     <ruleEntry>

        <assignedTo>otherUser@org.com</assignedTo>

        <assignedToType>User</assignedToType>

        <criteriaItems>

          <field>Case.IsEscalated</field>

          <operation>equals</operation>

          <value>False</value>

        </criteriaItems>

        <template>emailtemplate</template>

     </ruleEntry>

   </assignmentRule>

</AssignmentRules>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types AssessmentQuestion AssessmentQuestion

Represents the container object that stores the questions required for an assessment.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### AssessmentQuestion components have the suffix .AssessmentQuestion and are stored in the AssessmentQuestions

folder.

Version

### AssessmentQuestion components are available in API version 55.0 and later.

Fields

**Field Name** **Description**

```
assessmentQuestionVersion

dataType

developerName

displayTextCategory

```

**Field Type**
### AssessmentQuestionVersion

**Description**
The object that stores the question versions for the assessment questions.

**Field Type**
string

**Description**
Required.

The data type of the assessment question.

**Field Type**
string

**Description**

Required.

The developer name of the assessment question. Can contain only underscores and
alphanumeric characters and must be unique in your org. It must begin with a letter,
not include spaces, not end with an underscore, and not contain two consecutive
underscores.

**Field Type**
string


Metadata Types AssessmentQuestion

**Field Name** **Description**

**Description**
Specifies the category of the display text when the data type is Text Block.

```
formulaResponseDataType

name

questionCategory

relatedQuestion

```

**Field Type**
string

**Description**
Specifies the data type of the question response calculated by a formula.

**Field Type**
string

**Description**

Required.

The name of the record.

**Field Type**
string

**Description**

Required.

Stores the question category.

**Field Type**
string

**Description**
Specifies the related question. Used to define a question hierarchy.

AssessmentQuestionVersion

Stores the question versions for the assessment questions.

**Field Name** **Description**

```
additionalInformation

description

```

**Field Type**
string

**Description**
The additional details for a UI element, such as the disclosure text.

**Field Type**
string

**Description**
The description for the assessment question. This text isn’t rendered on the assessment.


Metadata Types AssessmentQuestion

**Field Name** **Description**

```
guidanceInformation

helpText

isActive

name

optionSourceResponseValue

questionText

responseValues

```

**Field Type**
string

**Description**
The guidance for the assessment question.

**Field Type**
string

**Description**
The text that's added as an info bubble in the UI element related to the assessment question.

**Field Type**
boolean

**Description**
Required.

Indicates whether the current version of the assessment question is set to active ( `true` )
or not ( `false` ).

The default value is `false` .

**Field Type**
string

**Description**
Required.

Name of the assessment question version record.

**Field Type**
boolean

**Description**
Indicates whether the response value source for an assessment question is configured as
custom ( `true` ) or sObject in the OmniStudio designer ( `false` ).

The default value is `false` .

**Field Type**
string

**Description**
Required.

The assessment question text. Contains the label for the assessment question that appears
on the assessment.

**Field Type**
string


Metadata Types AssessmentQuestion

**Field Name** **Description**

**Description**
Holds the values to be defined in the picklist, multiselect picklist, or radio buttons.

```
status

versionNumber

```

**Field Type**
string

**Description**
Required.

Status of the assessment question version. Possible values are Draft, Active, or Archived.

**Field Type**
int

**Description**
Required.

The assessment question version number.

Declarative Metadata Sample Definition

The following is an example of an AssessmentQuestion component.

```
<?xml version="1.0" encoding="UTF-8"?>

<AssessmentQuestion

 xmlns="http://soap.sforce.com/2006/04/metadata">

 <assessmentQuestionVersion>

  <additionalInformation>ParentQuestionDevName AI</additionalInformation>

  <description>ParentQuestionDevName Desc</description>

  <helpText>ParentQuestionDevName HT</helpText>

  <isActive>true</isActive>

  <name>ParentQuestionDevName</name>

  <optionSourceResponseValue>true</optionSourceResponseValue>

  <questionText>ParentQuestionDevName Text</questionText>

  <status>Active</status>

  <versionNumber>1</versionNumber>

 </assessmentQuestionVersion>

 <dataType>DateTime</dataType>

 <developerName>ParentQuestionDevName</developerName>

 <name>ParentQuestionDevName</name>

 <questionCategory>Demographic</questionCategory>

</AssessmentQuestion>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package

 xmlns="http://soap.sforce.com/2006/04/metadata">

 <types>

```


### Metadata Types AssessmentQuestionSet

```
     <members>*</members>

     <name>AssessmentQuestion</name>

    </types>

    <version>55.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

Usage

Before you retrieve assessment questions, we recommend that you review these considerations.

**•** When you retrieve an assessment question, you also get the related assessment question version with the status Active..

Note: If an active assessment question version doesn’t exist for the assessment question, then the latest assessment question
version with Status as Draft is retrieved.

**•** The value for the `<status>` tag in the XML definition must match the status of the related assessment question version.

**•** If an assessment question has a related assessment question (parent question), the XML definition must include the developer name
of the related assessment question.

**•** If the fields of an assessment question contain values, the XML definition must contain tags with those values when retrieving it.

Before you deploy assessment questions, we recommend that you review these considerations.

**•** If the Related Question isn’t available in the target org, deploying the assessment question fails.

**•** If an assessment question with the same developer name exists in the target org, deploying the assessment question updates the
values of the other fields in the target org.

**•** If the `<versionNumber>` tag is present in the XML definition of an assessment question, deploying creates a version for that
question in the target org.

**•** If the Related Questions aren’t available in target org but available in the package, then deploying the questions inserts the Related
Questions in the correct order.

**•** If the assessment questions are associated with flows of type Discovery Framework Data Capture Flow, then deploy the assessment
questions first. After deploying the assessment questions, deploy the flows.

### AssessmentQuestionSet

Represents the container object for Assessment Questions.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types AssessmentQuestionSet

File Suffix and Directory Location

AssessmentQuestionSet components have the suffix `.AssessmentQuestionSet` and are stored in the
`AssessmentQuestionSets` folder.

Version

AssessmentQuestionSet components are available in API version 55.0 and later.

Fields

**Field Name** **Description**

```
assessmentQuestionDeveloperNames

developerName

name

```

**Field Type**
string[]

**Description**
The developer names for the assessment question. Can contain only underscores and
alphanumeric characters and must be unique in your org. It must begin with a letter,
not include spaces, not end with an underscore, and not contain two consecutive
underscores.

**Field Type**
string

**Description**
Required.

The developer name for the assessment question set. Can contain only underscores
and alphanumeric characters and must be unique in your org. It must begin with a
letter, not include spaces, not end with an underscore, and not contain two consecutive
underscores.

**Field Type**
string

**Description**
Required.

The question set name.

Declarative Metadata Sample Definition

The following is an example of an AssessmentQuestionSet component.

```
<?xml version="1.0" encoding="UTF-8"?>

<AssessmentQuestionSet

 xmlns="http://soap.sforce.com/2006/04/metadata">

 <developerName>QuestionSetDevName</developerName>

```


### Metadata Types Audience

```
    <name>QuestionSetName</name>

    <assessmentQuestionDeveloperNames>QuestionDevName</assessmentQuestionDeveloperNames>

   </AssessmentQuestionSet>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package

    xmlns="http://soap.sforce.com/2006/04/metadata">

    <types>

     <members>*</members>

     <name>AssessmentQuestion</name>

    </types>

    <types>

     <members>*</members>

     <name>AssessmentQuestionSet</name>

    </types>

    <version>55.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

Usage

Before you retrieve assessment question sets, we recommend that you review these considerations.

**•** When retrieving an assessment question set, if its fields contain values, then the XML definition must contain tags with those values.

**•** When retrieving an assessment question set, if that set is associated with multiple questions, then the XML definition must contain
developer names of all the associated questions.

Before you deploy assessment question sets, we recommend that you review these considerations.

**•** When deploying an assessment question set, if an assessment question set with the same developer name doesn't exist in the target
org, deploying creates one with that name.

**•** If an assessment question set with the same developer name exists in the target org, then deploying the question set updates the
values of the other fields in the target org.

**•** If the questions associated with the assessment question set don't exist in the target org, deploying the assessment question set
fails.

**•** If the questions associated with the assessment question set don’t exist in the target org but are available in the package, then
deploying the assessment question sets inserts the questions in the correct order.

### Audience

Represents the audience in an Experience Builder site. An audience consists of different types of criteria, where the audience can be
assigned and used for targeting in a site. This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types Audience

File Suffix and Directory Location

Audience components have the suffix `.audience` and are stored in the `audience` folder.

Version

Audience components are available in API version 44.0 and later.

Special Access Rules

Access to the Audience type requires the AudienceMetadata permission. This permission is on by default for orgs that have Networks
enabled.

Access to permission criteria for the Audience type requires the AudiencePermissionCriteria permission. This permission is available in
API version 45.0 and later and is on by default for orgs that have Networks enabled.

Fields

**Field Name** **Field Type** **Description**

`audienceName` string Required. The name of the audience.

`container` string Required. The name of the site or org that contains the audience.

`criteria` AudienceCriteria Required. Criteria in an audience. This field is available in API version 47.0
and later.

`criterion` AudienceCriterion[]

Removed. List of criteria in an audience.

This field is available in API version 44.0–46.0. In API version 47.0 and
later, use `criteria` instead.

`description` string The description of the audience.

`formula` string Formula used to determine the audience. This field is available in API
version 45.0 and later.

```
formulaFilterType

```

FormulaFilterType Indicates the audience’s formula type. Valid values are
(enumeration of

**•** `AllCriteriaMatch`

type string)

**•** `AllCriteriaMatch`

**•** `AnyCriterionMatches`

`isDefaultAudience` boolean

**•** `CustomLogicMatches` (available in API version 45.0 and later)

Indicates whether the audience is the default audience ( `true` ) or not
( `false` ). This field is available and required in API version 48.0. In API
version 49.0 and later, this field is optional.

The default audience file name is of format `Default_` _**`Network`**_
_**`Name`**_ `.audience` .

`targets` PersonalizationTarget Targets for the audience. This field is available in API version 47.0 and
Infos later.


Metadata Types Audience

AudienceCriteria

Represents criteria for an audience. This subtype is available in API version 47.0 and later.

**Field Name** **Field Type** **Description**

`criterion` AudienceCriterion[] List of criteria for an audience. An audience can have up to 100 criteria.

AudienceCriterion

Represents a criterion for an audience.

**Field Name** **Field Type** **Description**

`criteriaNumber` int The number associated with the criterion in a formula, for example (1 AND 2)
OR 3. This field is available in API version 45.0 and later.

`criterionValue` AudienceCriteriaValue The value of the criterion.

`operator` AudienceCriterionOperator(enumeration The operator associated with this criterion. Valid values are:
of type string)

**•** `Equal`

**•** `NotEqual`

**•** `GreaterThan`

**•** `GreaterThanOrEqual`

**•** `LessThan`

**•** `LessThanOrEqual`

**•** `Contains`

**•** `StartsWith`

**•** `Includes` (available in API version 45.0 and later)

**•** `NotIncludes` (available in API version 45.0 and later)

```
type

```

AudienceCriterion Required. Valid values are:
Type(enumeration of

**•** `GeoLocation`

type string)

**•** `GeoLocation`

**•** `Domain`

**•** `Profile`

**•** `FieldBased`

**•** `Permission` (available in API version 45.0 and later)

**•** `Default` (available in API version 47.0 and later)

**•** `Audience` (available in API version 53.0 and later)

For a list of AudienceCriteriaValue fields that you can use with each
AudienceCriterion `type` field value, see this table.


Metadata Types Audience

AudienceCriteriaValue

Represents the value of a criterion in an audience. For a list of AudienceCriteriaValue fields that you can use with each AudienceCriterion
`type` field value, see this table.

**Field Name** **Field Type** **Description**

`audienceDeveloperName` string

Developer name of the audience. This field is available in API version 53.0 and
later. You can use this field only when the value of the AudienceCriterion `type`
field is `Audience` .

`city` string City of a user. You can use this field only when the value of the
AudienceCriterion `type` field is `GeoLocation` .

`country` string Country of a user. You can use this field only when the value of the
AudienceCriterion `type` field is `GeoLocation` .

`domain` string Domain of a user. You can use this field only when the value of the
AudienceCriterion `type` field is `Domain` .

`entityField` string Field of an object. You can use this field only when the value of the
AudienceCriterion `type` field is `FieldBased` .

`entityType` string Type of object. You can use this field only when the value of the
AudienceCriterion `type` field is `FieldBased` .

`fieldValue` string Value of a field. You can use this field only when the value of the
AudienceCriterion `type` field is `FieldBased` .

`isEnabled` string

`permissionName` string

`permissionType` string

Indicates whether the permission is enabled ( `true` ) or not ( `false` ) for a user.
This field is available in API version 45.0 and later. You can use this field used
only when the value of the AudienceCriterion `type` field is `Permission` .

Valid API name of a standard user or custom permission. This field is available
in API version 45.0 and later. You can use this field only when the value of the
AudienceCriterion `type` field is `Permission` .

Type of permission. Valid values are `Standard` and `Custom` . This field is
available in API version 45.0 and later. You can use this field only when the
value of the AudienceCriterion `type` field is `Permission` .

`profile` string Profile of a user. You can use this field only when the value of the
AudienceCriterion `type` field is `Profile` .

`subdivision` string Subdivision of a user. You can use this field only when the value of the
AudienceCriterion `type` field is `GeoLocation` .

This table summarizes which AudienceCriteriaValue fields you can use with the different AudienceCriterion `type` field values.

**AudienceCriterion Type** **AudienceCriteriaValue Fields**

```
GeoLocation

```

```
city

country

```


Metadata Types Audience

**AudienceCriterion Type** **AudienceCriteriaValue Fields**

```
                                 subdivision

   Domain domain

   Profile profile

```

```
FieldBased

Permission

```

```
entityField

entityType

fieldValue

isEnabled

permissionName

permissionType

```

```
Audience audienceDeveloperName

```

PersonalizationTargetInfos

Represents targets for an audience. This subtype is available in API version 47.0 and later.

When deploying an audience, you must include ExperienceBundle in your package to support experience variation targets.

**Field Name** **Field Type** **Description**

`target` PersonalizationTarget List of targets for an audience.
Info[]

PersonalizationTargetInfo

Represents a target for an audience. This subtype is available in API version 47.0 and later.

**Field Name** **Field Type** **Description**

`groupName` string

Required. Group name of the target. Groups bundle related target and audience
pairs. You can have up to 2,000 groups and 500 targets per group.

To determine the target group name, see
h **t** [ps://developer.salesforce.com/docs/atlas.en-us.communities_dev.meta/communities_dev/communities_dev_personalization_names.htm](https://developer.salesforce.com/docs/atlas.en-us.262.0.communities_dev.meta/communities_dev/communities_dev_personalization_names.htm)
in the _Experience Cloud Developer Guide_ .

`priority` int Priority of the target. Within a group, priority determines which target is returned
when the user matches more than one audience.

`targetType` string Required. Type of target, indicating the nature of the data being targeted.
Supported values include:

**•** `ExperienceVariation` (API version 47.0 and later)

**•** `NavigationLinkSet` (API version 49.0 and later)


Metadata Types Audience

**Field Name** **Field Type** **Description**

**•** `Report` (API version 49.0 and later)

**•** `Dashboard` (API version 49.0 and later)

You can have up to 2,500 `ExperienceVariation` targets and 25,000
record targets.

For more information on the `ExperienceVariation` target type, see
ExperienceBundle.

`targetValue` string

Required. Value of the target, which is the developer name of the experience
variation, such as `ContactSupport_ContactSupportFor`
`California_Page` for a page variation.

To determine the target developer name, see
h **t** [ps://developer.salesforce.com/docs/atlas.en-us.communities_dev.meta/communities_dev/communities_dev_personalization_names.htm](https://developer.salesforce.com/docs/atlas.en-us.262.0.communities_dev.meta/communities_dev/communities_dev_personalization_names.htm)
in the _Experience Cloud Developer Guide_ .

Declarative Metadata Sample Definition

The following is an example of an Audience component.

```
<?xml version="1.0" encoding="UTF-8"?>

<Audience xmlns="http://soap.sforce.com/2006/04/metadata">

   <audienceName>Audience Metadata</audienceName>

   <container>Customer</container>

   <criteria>

     <criterion>

        <criteriaNumber>1</criteriaNumber>

        <criterionValue>

          <country>United States</country>

          <subdivision>Nevada</subdivision>

        </criterionValue>

        <operator>Equal</operator>

        <type>GeoLocation</type>

     </criterion>

     <criterion>

        <criteriaNumber>2</criteriaNumber>

        <criterionValue>

          <profile>customer community user</profile>

        </criterionValue>

        <operator>Equal</operator>

        <type>Profile</type>

     </criterion>

     <criterion>

        <criteriaNumber>3</criteriaNumber>

        <criterionValue>

          <domain>sampledomain.example.com</domain>

        </criterionValue>

        <operator>Equal</operator>

        <type>Domain</type>

     </criterion>

```


Metadata Types Audience

```
        <criterion>

           <criteriaNumber>4</criteriaNumber>

           <criterionValue>

            <entityField>Manager.Profile.CreatedBy.Contact.MailingCountry</entityField>

             <entityType>User</entityType>

             <fieldValue>USA</fieldValue>

           </criterionValue>

           <operator>StartsWith</operator>

           <type>FieldBased</type>

        </criterion>

        <criterion>

           <criteriaNumber>5</criteriaNumber>

           <criterionValue>

             <entityField>RecordTypeId</entityField>

             <entityType>CollaborationGroup</entityType>

             <fieldValue>CollaborationGroup.Group_RT2</fieldValue>

           </criterionValue>

           <operator>Equal</operator>

           <type>FieldBased</type>

        </criterion>

        <criterion>

           <criteriaNumber>6</criteriaNumber>

           <criterionValue>

             <isEnabled>true</isEnabled>

             <permissionName>ManageUsers</permissionName>

             <permissionType>Standard</permissionType>

           </criterionValue>

           <operator>Equal</operator>

           <type>Permission</type>

        </criterion>

        <criterion>

           <criteriaNumber>7</criteriaNumber>

           <criterionValue>

             <isEnabled>false</isEnabled>

             <permissionName>NamespaceXYZ__CustomPermABC</permissionName>

             <permissionType>Custom</permissionType>

           </criterionValue>

           <operator>Equal</operator>

           <type>Permission</type>

        </criterion>

        <criterion>

           <criteriaNumber>8</criteriaNumber>

           <criterionValue>

             <audienceDeveloperName>Audience1</audienceDeveloperName>

           </criterionValue>

           <operator>Equal</operator>

           <type>Audience</type>

        </criterion>

      </criteria>

      <formula>1 AND (2 OR 3 OR 4 OR 5 OR 6 OR 7) AND 8</formula>

      <formulaFilterType>CustomLogicMatches</formulaFilterType>

      <isDefaultAudience>false</isDefaultAudience>

      <targets>

```


Metadata Types Audience

```
        <target>

           <groupName>c194d79c-5c6b-4c6a-8d14-0e7042564355$#$Branding</groupName>

           <priority>1</priority>

           <targetType>ExperienceVariation</targetType>

           <targetValue>Customer_Service_testBrandingSet_Branding</targetValue>

        </target>

      </targets>

   </Audience>

```

Usage

You can’t use Metadata API to delete an audience.

In API version 47.0 and later, you can’t create an audience without criteria.

The list of targets provided in the input for an audience is considered the state of target assignments that you want. For example, see
the following information for deleting, creating, and updating targets.

If you don’t have a default audience, updating targets can result in the UI erroneously showing a target assigned to the default audience.
The target assignment data in the API is correct. To work around the UI issue, temporarily assign another target to the default audience
and then delete it.

Personalization using audience targeting varies what the user can see in the browser but doesn’t secure data in any way. To prevent
users accessing sensitive data, use standard Salesforce security features, such as sharing rules and permission sets.

**Delete targets**
To delete a single target from an audience, deploy the entire list of targets for the audience minus the one that you want to delete.

To delete all the targets from an audience, deploy the audience with empty targets tags. For example:

```
     <?xml version="1.0" encoding="UTF-8"?>

     <Audience

       xmlns="http://soap.sforce.com/2006/04/metadata">

       <audienceName>testAudience</audienceName>

       <container>testContainer</container>

       <criteria>

          <criterion>

            <criteriaNumber>1</criteriaNumber>

            <criterionValue>

               <country>United States</country>

               <subdivision>Nevada</subdivision>

            </criterionValue>

            <operator>Equal</operator>

            <type>GeoLocation</type>

          </criterion>

       </criteria>

       <formulaFilterType>AllCriteriaMatch</formulaFilterType>

       <isDefaultAudience>false</isDefaultAudience>

       <targets>

       </targets>

     </Audience>

```


### Metadata Types AuraDefinitionBundle

**Update an audience without updating targets**
To update an audience without updating targets, deploy the audience without targets tags. For example:

```
     <?xml version="1.0" encoding="UTF-8"?>

     <Audience

       xmlns="http://soap.sforce.com/2006/04/metadata">

       <audienceName>testAudience</audienceName>

       <container>testContainer</container>

       <criteria>

          <criterion>

            <criteriaNumber>1</criteriaNumber>

            <criterionValue>

               <country>United States</country>

               <subdivision>Nevada</subdivision>

            </criterionValue>

            <operator>Equal</operator>

            <type>GeoLocation</type>

          </criterion>

       </criteria>

       <formulaFilterType>AllCriteriaMatch</formulaFilterType>

       <isDefaultAudience>false</isDefaultAudience>

     </Audience>

```

**Create targets**
To create a target, deploy the entire list of targets for the audience plus the one that you want to create.

**Update the priority of a target**
To change the priority of a target within an audience, deploy the entire list of targets for the audience with the new priority values
for the targets.

To change the priority of a target that affects priority in another audience, deploy both audiences with their entire list of targets with
the new priority values for the targets.

**Update the target assignment for an audience**
To reassign a target to a new audience, deploy both audiences with their entire list of targets. Deploy one list with the target removed,
and the other list with the target added.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### AuraDefinitionBundle

Represents an Aura definition bundle. A bundle contains an Aura definition, such as an Aura component, and its related resources, such
as a JavaScript controller. The definition can be a component, application, event, interface, or a tokens collection.

File Suffix and Directory Location

An AuraDefinitionBundle component is a folder that contains definition files. Unlike most other metadata components, an
### AuraDefinitionBundle component isn’t a single file, it’s a collection of files. Each file represents a resource in a bundle, such as markup,


Metadata Types AuraDefinitionBundle

applications, code files (including controllers and helpers), events, documentation, and interfaces. For example, this directory structure
shows the hierarchy of the folders and files for two bundles: `bundle1` and `bundle2` .

```
   aura

      bundle1

        bundle1.cmp

        bundle1Controller.js

      bundle2

        bundle2.app

        bundle2Controller.js

        bundle2.auradoc

```

Aura definition bundles must be under a top-level folder named `aura` . Each bundle must have its own subfolder under the `aura`
folder. The name of each definition file must start with the bundle name.

A bundle doesn’t have a suffix. Definition files can have one of these suffixes:

Each bundle can have only one file each with a suffix of `.app`, `.cmp`, `.design`, `.evt`, `.intf`, or `.tokens` .

Version

AuraDefinitionBundle components are available in API version 32.0 and later.

Design and SVG components are available in API version 33.0 and later.

In API version 45.0 and later, there are two types of Lightning component: Aura components and Lightning web components. This
metadata type describes an Aura component.

Special Access Rules

Definitions can be created only in organizations with defined namespaces.


Metadata Types AuraDefinitionBundle

Fields

**Field Name** **Field Type** **Description**

`apiVersion` double

The API version for this definition bundle. When you create an Aura
bundle, you can specify the API version to save it with. Available in API
version 35.0 and later.

`auraDefinitions` AuraDefinitions Reserved for internal use.

`controllerContent` base64Binary The content of a JavaScript client-side controller.

`description` string The specification of the Aura bundle. Available in API version 35.0 and
later.

`designContent` base64Binary The content of a design definition. Only valid inside a component bundle.

`documentationContent` base64Binary The content of a documentation definition.

`helperContent` base64Binary The content of a JavaScript helper.

`markup` base64Binary The content of the markup for a definition.

`modelContent` base64Binary Deprecated. Do not use.

`packageVersions` PackageVersion[] The list of installed managed package versions that this Aura definition
bundle references. Available in API version 35.0 and later.

`rendererContent` base64Binary The content of a JavaScript client-side renderer.

`styleContent` base64Binary The CSS for the definition.

`SVGContent` base64Binary The SVG image for the definition.

`testsuiteContent` base64Binary Reserved for internal use.

```
type

```

AuraBundleType The definition type. Valid values are:
(enumeration of

**•** `Application`

type string)

**•** `Application`

**•** `Component`

**•** `Event`

**•** `Interface`

**•** `Tokens`

Declarative Metadata Sample Definition

This example shows the directory structure of an AuraDefinitionBundle component.

```
aura

   sampleCmp

     sampleCmp.cmp

     sampleCmpController.js

```

The following samples show the contents of the metadata definition files that correspond to the sample `aura` directory.


### Metadata Types AuthProvider

Content of `sampleCmp.cmp` :

```
   <aura:component>

      <aura:attribute name="val1" type="String" default="Value"/>

      <aura:attribute name="val2" type="String" />

      <aura:handler name="init" value="{!this}" action="{!c.myAction}"/>

        <ui:outputText value='Hello world!'/>

        <ui:outputText value='{!v.val1}'/>

        <ui:outputText value='{!v.val2}'/>

   </aura:component>

```

Content of `sampleCmpController.js` :

```
   ({

     myAction : function(component) {

      component.set('v.val1','Value1');

      component.set('v.val2','Value2');

     }

   })

```

This `package.xml` references the definitions of all Lightning components that are present in the `sampleCmp` bundle.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>sampleCmp</members>

        <name>AuraDefinitionBundle</name>

      </types>

      <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### AuthProvider

Represents an authentication provider (auth provider). An auth provider lets users log in to Salesforce from an external service provider
such as Facebook, Google, or GitHub. This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

Authentication providers are stored in the `authproviders` directory. The file name matches the URL suffix, and the extension is
`.authprovider` . For example, an auth provider with URL suffix `FacebookProvider` is stored in
`authproviders/FacebookProvider.authprovider` .

Version

Authentication providers are available in API version 27.0 and later.


Metadata Types AuthProvider

Special Access Rules

Only users with the Customize Application and Manage AuthProviders permissions can access this object.

Fields

**Field Name** **Field Type** **Description**

`appleTeam` string

`authorizeUrl` string

`consumerKey` string

Required when using Apple as a third-party authentication provider. A
10-character team ID, obtained from an Apple developer account. Available
in API version 48.0 and later.

Required when creating an OpenID Connect authentication provider. The
OAuth authorization endpoint URL. Available in API version 29.0 and later.

In API version 33.0 and later, for Salesforce-managed auth providers, leave
the field blank to let Salesforce supply and manage the value. For details,
see “Usage.”

The app’s key that is registered at the third-party (external) authentication
provider.

In API version 33.0 and later, for Salesforce-managed auth providers, leave
the field blank to let Salesforce supply and manage the value. For details,
see “Usage.”

`consumerSecret` string The consumer secret of the app that is registered at the third-party provider.
After it’s set, you can’t change the value. When using `create()`, this

field must be encrypted. To create an encrypted form of the consumer
secret from plaintext:

**1.** Create an authentication provider with the `consumerSecret`
plaintext value.

**2.** Save the authentication provider.

**3.** Create an outbound change set that includes the authentication
provider component.

The new change set .xml file has an entry in the form

`<consumerSecret>++XYZ++</consumerSecret>` where
++XYZ++ is the encrypted secret.

In API version 33.0 and later, for Salesforce-managed auth providers, leave
the field blank to let Salesforce supply and manage the value. For details,
see Usage.

If a consumer secret is defined on an authentication provider, the consumer
secret is always exported as a placeholder value, not as an encrypted secret.

```
controlPlane

```

`MuleSoftControlPlane` Required when using MuleSoft as a third-party authentication provider.
(enumeration of Environment where the MuleSoft Anypoint Platform control plane is hosted.
type string) The control plane is the part of the Anypoint Platform architecture that

includes Anypoint Exchange and determines the login URL. If you select
User-Specified, you must enter the Consumer Key and Consumer Secret.


Metadata Types AuthProvider

**Field Name** **Field Type** **Description**

Obtain the values from the MuleSoft connected app that you created to
store the authentication details for your Salesforce org. Available in API
version 57.0 and later. Valid values include:

**•** `None` —User-specified control plane. If you select `None`, you must
enter the Consumer Key and Consumer Secret. Obtain the values from
the MuleSoft connected app that you created to store the
authentication details for your Salesforce org.

**•** `US` —US control plane

**•** `EU` —EU control plane

`customMetadataTypeRecord` string

`defaultScopes` string

Required when creating a custom authentication provider plug-in. The
API name of the custom authentication provider. Available in API version
36.0 and later.

For OpenID Connect authentication providers, the scopes to send with the
authorization request, if not specified when a flow starts. Available in API
version 29.0 and later.

In API version 33.0 and later, for Salesforce-managed auth providers, leave
the field blank to let Salesforce supply and manage the value. See “Usage.”

`ecKey` string Required when using Apple as a third-party authentication provider. A
private key generated by Apple. Available in API version 48.0 and later.

`errorUrl` string A custom error URL for the authentication provider to use to report errors.

`executionUser` string

`flow` string

Required to specify a registration handler. The username of the Salesforce
admin or system user who runs the Apex handler or flow. The execution

user provides the context in which the registration handler runs. For
example, if the handler creates a contact, the creation can be easily traced
back to the registration process. In production, use a system user. The user
must have the Manage Users permission. Available in API version 27.0 and
later.

A flow for the registration handler. The flow must be of the Identity User
Registration Flow type.

You can use either a flow or an Apex class for the registration handler. To
use an Apex class instead, omit the `flow` field and specify an Apex class
in the `registrationHandler` field.

Available in API version 64.0 and later.

`flowDefaultAccount` string For authentication providers that use a flow registration handler, the default
account that new external users are assigned to. If you include this field,

Salesforce automatically uses it for the `defaultAccountId` variable
in the Authentication Provider User Registration standard flow.

A default account is required to use a flow registration handler to create
and update external users. You can specify a default account here or in the


Metadata Types AuthProvider

**Field Name** **Field Type** **Description**

flow itself. If you use both, the default account that's configured in the flow
takes precedent.

Available in API version 64.0 and later.

`flowDefaultProfile` string For authentication providers that use a flow registration handler, the default
profile that new users are assigned to. If you include this field, Salesforce

automatically uses it for the `defaultProfileId` variable in the
Authentication Provider User Registration standard flow.

A default profile is required to use a flow registration handler. You can
specify a default profile here or in the flow itself. If you use both, the default
profile that's configured in the flow takes precedent.

Available in API version 64.0 and later.

`friendlyName` string Required. A user-friendly name for the authentication provider.

`iconUrl` string

The path to an icon to use as a button on the login page. Users click the
button to log in with the associated authentication provider, such as Twitter
or Facebook. Available in API version 32.0 and later.

`idTokenIssuer` string The source of the authentication token in `https:` URI format. This field
is available when configuring an OpenID Connect or Microsoft

authentication provider. If provided, Salesforce validates the returned
`id_token` value. OpenID Connect requires returning an `id_token`
value with the `access_token` value. Available in API version 30.0 and
later.

`includeOrgIdInIdentifier` boolean Used to differentiate between users with the same user ID from two sources
(such as two sandboxes). If enabled ( `true` ), Salesforce stores the org ID

of the third-party identity in addition to the user ID. After you enable this
setting, you can’t disable it. Applies only to a Salesforce-managed auth
provider. Available in API version 32.0 and later.

`isPkceEnabled` boolean

Indicates whether the OAuth 2.0 Proof Key for Code Exchange (PKCE)
security extension is enabled ( `true` ) or not ( `false` ). You can enable
PKCE for these `providerType` values.

**•** `Custom`

**•** `Facebook`

**•** `Google`

**•** `Microsoft`

**•** `OpenIdConnect`

**•** `Salesforce` .

This field is available in API version 59.0 and later.

`linkKickoffUrl` string The URL for linking existing Salesforce users to a third-party account. This
field is read-only. Available in API version 43.0 and later.


Metadata Types AuthProvider

**Field Name** **Field Type** **Description**

`logoutUrl` string The destination for users after they log out if they authenticated using
single sign-on. The URL must be fully qualified with an http or https prefix,

such as `https://acme.my.salesforce.com` . Available in API
version 33.0 and later.

`oauthKickoffUrl` string The URL for obtaining OAuth access tokens for a third party. This field is
read-only. Available in API version 43.0 and later.

`paramForwardAllowlist` AuthProvParamFwdA **l** owlist[]

`plugin` string

An allowlisted URL parameter that can be forwarded from the
authentication provider's client configuration URLs to the authorization
URL. Available in API version 62.0 and later.

An existing Apex class that extends the
`Auth.AuthProviderPluginClass` abstract class. Available in
API version 36.0 and later.

`portal` string This field is used only with portals, which are deprecated. Salesforce doesn’t
support creating portals, but existing portals are supported.

```
providerType

```

`AuthProviderType` Required. The third-party authentication provider to use. Valid values
(enumeration of include:
type string)

**•** `Apple`

**•** `Bitbucket` —Provides authentication for a `Bitbucket` provider.
Enables you to connect to Bitbucket from a Lightning Platform
application. When logged in to Bitbucket, the app can makes calls to
Bitbucket APIs. The `Bitbucket` provider isn’t available as an SSO
provider, so users can’t log in to a Salesforce org using their Bitbucket
login credentials. Available in API version 61.0 and higher.

**•** `Custom` —A provider configured with a custom authentication
provider plug-in. Available in API version 36.0 and later.

**•** `Facebook` .

**•** `GitHub` —Provides authentication for a `GitHub` provider. Used to
log in users of your Lightning Platform app to GitHub using OAuth.
When logged in to GitHub, your app can make calls to GitHub APIs.
The `GitHub` provider isn’t available as an SSO provider, so users can’t
log in to your Salesforce org using their GitHub login credentials.
Available in API version 35.0 and later.

**•** `Google` .

**•** `Janrain` .

**•** `LinkedIn` . Available in API version 32.0 and later.

**•** `Microsoft` —Provides authentication for all services that can be
accessed via Microsoft Azure Active Directory. Available in API version
55.0 and later.

**•** `MicrosoftACS` —Microsoft Access Control Service typically provides
authentication for a Microsoft Office 365 service, like SharePoint Online.
The `MicrosoftACS` provider doesn't support SSO. Available in API
version 31.0 and later.


Metadata Types AuthProvider

**Field Name** **Field Type** **Description**

**•** `MuleSoft` . Available in API version 57.0 and later.

**•** `OpenIdConnect` . Available in API version 29.0 and later.

**•** `Salesforce` .

**•** `Slack` . Available in API version 54.0 and later.

**•** `Twitter` . Available in API version 32.0 and later.

`registrationHandler` string

An existing Apex class that implements the
`Auth.RegistrationHandler` interface.

You can use either an Apex class or a flow for the registration handler. To
use a flow instead, omit the `registrationHandler` field and specify
a flow in the `flow` field.

`requireMfa` boolean Requires multi-factor authentication (MFA) for single sign-on with this
auth provider based on the MFA status of each user. For this setting to

trigger MFA, you must apply MFA directly to users via one of two methods.
1) Enable the org setting Require multi-factor authentication (MFA) for all
direct UI logins to your Salesforce org. 2) Assign the user permission
multi-factor authentication for User Interface Logins.

`sendAccessTokenInHeader` boolean If enabled ( `true` ), the access token is sent to the `UserInfoUrl` in a
header instead of a query string. Available in API version 30.0 and later.

`sendClientCredentialsInHeader` boolean Required when creating an OpenID Connect authentication provider. If
enabled ( `true` ), the client credentials are sent in a header to the

`tokenUrl` instead of a query string. The credentials are in the standard
OpenID Connect Basic Credentials header format, which is `Basic`
`<token>`, where `<token>` is the base64-encoded string
`"clientkey:clientsecret"` . Available in API version 30.0 and
later.

`sendSecretInApis` boolean

`ssoKickoffUrl` string

Determines whether the encrypted consumer secret appears in API
responses. If enabled (default), the secret appears in the response. If

disabled ( `false` ), responses don’t include the consumer secret. For
security, you can disable the setting. However, keep in mind that:

**•** By disabling this setting, the consumer secret is excluded from API
responses in all API versions.

**•** Change sets and other metadata deployments break because both
the consumer key and secret are expected. To fix this problem, insert
the consumer key manually during deployment.

Available in API version 47.0 and later.

The consumer secret is always included in the response as a placeholder
value, regardless of the value provided for `sendSecretInApis` .

The URL for performing single sign-on into Salesforce from a third party
by using its third-party credentials. This field is read-only. Available in API
version 43 and later.


Metadata Types AuthProvider

**Field Name** **Field Type** **Description**

`tokenUrl` string

`userInfoUrl` string

AuthProvParamFwdAllowlist

The OAuth token endpoint URL of an OpenID Connect authentication
provider. Available in API version 29.0 and later.

In API version 33.0 and later, for Salesforce-managed auth providers, leave
the field blank to let Salesforce supply and manage the value. For details,
see “Usage.”

The OpenID Connect endpoint URL of the OpenID Connect authentication
provider. Available in API version 29.0 and later.

In API version 33.0 and later, for Salesforce-managed auth providers, leave
the field blank to let Salesforce supply and manage the value. For details,
see “Usage.”

Represents an allowlisted URL parameter that can be forwarded from authentication provider client configuration URLs to the authorization
URL. Use this type to add custom functionality to authentication providers. For example, allowlist a `ui_locales` parameter and use
it to send a user's language preference from Salesforce to the third-party provider's login page. You can allowlist up to 10 parameters.

Declarative Metadata Sample Definition

Note: Starting in November 2022, enter the `consumerSecret` value as plaintext, for example,
`<consumerSecret>yourplaintextconsumersecret</consumerSecret>` . Existing consumer secrets that
were entered as encrypted values can be deployed throughout the Winter ‘23 release.

```
<?xml version="1.0" encoding="UTF-8"?>

<AuthProvider xmlns="http://soap.sforce.com/2006/04/metadata">

   <consumerKey>yourappkey</consumerKey>

   <consumerSecret>PwdVxXjzu3NCZ3MD4He+wA==</consumerSecret>

   <executionUser>admin@your.org</executionUser>

   <friendlyName>FacebookAuthProvider</friendlyName>

   <providerType>Facebook</providerType>

   <registrationHandler>RegistrationHandler</registrationHandler>

   <sendSecretInApis>true</sendSecretInApis>

</AuthProvider>

```

This example package manifest references the previous AuthProvider definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

```


Metadata Types AuthProvider

```
      <types>

        <members>FacebookAuthProvider</members>

        <name>AuthProvider</name>

      </types>

      <version>28.0</version>

   </Package>

```

Usage

Salesforce provides default authentication providers, called Salesforce-managed auth providers, to simplify setting up these service
providers for authentication.

**•** Apple

**•** Bitbucket

**•** Facebook

**•** GitHub

**•** Google

**•** Janrain

**•** LinkedIn

**•** Microsoft

**•** Microsoft Access Control Service

**•** MuleSoft

**•** Salesforce

**•** Slack

To use a Salesforce-managed auth provider, leave these fields blank when creating your auth provider from the Auth. Provider Setup
page.

**•** `authorizeUrl`

**•** `consumerKey`

**•** `consumerSecret`

**•** `defaultScopes`

**•** `tokenURL`

**•** `userInfoUrl`

Note: If you provide a value for one of these fields, you must also provide a value for `consumerKey` and `consumerSecret` .

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types AutoResponseRules AutoResponseRules

Represents an auto-response rule that sets conditions for sending automatic email responses to lead or case submissions based on the
attributes of the submitted record. You can access rules metadata for all applicable objects, for a specific object, or for a specific rule on
a specific object.

The `package.xml` syntax for accessing all auto-response rules for all objects is:

```
      <types>

        <members>*</members>

        <name>AutoResponseRules</name>

      </types>

```

All rules for a specific object use a similar syntax without the wildcard. For example, all auto-response rules for the Case object would
use this syntax:

```
      <types>

        <members>Case</members>

        <name>AutoResponseRules</name>

      </types>

```

You can also access specific auto-response rules for an object. The following example only accesses the “samplerule” and “newrule”
### auto-response rules on the Case object. Notice that for this example the type name syntax is AutoResponseRule and not AutoResponseRules .

```
      <types>

        <members>Case.samplerule</members>

        <members>Case.newrule</members>

        <name>AutoResponseRule</name>

      </types>

```

File Suffix and Directory Location

### AutoResponseRules for an object have the suffix .autoResponseRules and are stored in the autoResponseRules folder.

For example, all Case auto-response rules are stored in the `Case.autoResponseRules` file.

Version

### AutoResponseRules components are available in API version 27.0 and later.

Fields

**Field Name** **Field Type** **Description**

`autoresponseRule` AutoResponseRule[] Represents the definitions of the named auto-response rules.

### AutoResponseRule

Represents whether a rule is active or not and the order in which the entry is processed in the rule.


Metadata Types AutoResponseRules

**Field Name** **Field Type** **Description**

`active` boolean Indicates whether the autoresponse rule is active ( `true` )
or not ( `false` ).

`fullname` string Inherited from Metadata, this field is defined in the WSDL
for this metadata type. It must be specified when creating,

updating, or deleting. See `createMetadata()` to see
an example of this field specified for a call.

This value can't be `null` .

`ruleEntry` RuleEntry[] Represents the type and description for the auto-response
rule.

RuleEntry

Represents the fields used by the rule.

**Field Name** **Field Type** **Description**

`booleanFilter` string Advanced filter conditions that were specified for the rule.

`criteriaItems` `FilterItem[]` The items in the list that define the assignment criteria.

`formula` string

The validation formula.

Specify either `formula` or `criteriaItems`, but not
both fields.

`replyToEmail` string The email address that appears in the reply-to header.

`senderEmail` string The email address of the person or queue sending the email
notification.

`senderName` string The name of the person or queue sending the email
notification.

`template` string

Declarative Metadata Sample Definition

The following is an example AutoResponseRules component:

Specifies the template to use for the email that is
automatically sent to the designated recipient.

Lightning email templates aren’t packageable. We
recommend using a Classic email template.

```
<AutoResponseRules xmlns="http://soap.sforce.com/2006/04/metadata">

   <autoResponseRule>

     <fullName>ajbdeploytest2</fullName>

     <active>false</active>

     <ruleEntry>

```


### Metadata Types BatchCalcJobDefinition

```
           <criteriaItems>

             <field>Case.Description</field>

             <operation>contains</operation>

             <value>testing</value>

           </criteriaItems>

           <senderEmail>test@test.org</senderEmail>

           <senderName>tester name j</senderName>

           <replyToEmail>test@@test.org</replyToEmail>

           <template>emailtemplate</template>

        </ruleEntry>

      </autoResponseRule>

   </AutoResponseRules>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### BatchCalcJobDefinition

Represents a Data Processing Engine definition.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### BatchCalcJobDefinition components have the suffix .batchCalcJobDefinition and are stored in the

`batchCalcJobDefinitions` folder.

Version

### BatchCalcJobDefinition components are available in API version 51.0 and later.

Special Access Rules

To use this metadata type, one of these licenses is required:

**•** Loyalty Management

**•** Financial Services Cloud

**•** Rebate Management

**•** Manufacturing Cloud

**•** Net Zero Cloud


Metadata Types BatchCalcJobDefinition

Fields

**Field Name** **Field Type** **Description**

`aggregates` BatchCalcJob Collection of aggregate nodes in a data processing engine.
Aggregate[]

`appends` BatchCalcJobUnion[] Collection of append nodes in a data processing engine.

`atomicWritebacks` BatchCalcJobAtomicWriteBack[] Collection of composite writeback nodes in a data processing engine
definition. Available in API version 62.0 and later.

`customNodes` BatchCalcJobCustomNode[] Collection of custom nodes in a data processing engine. Available in API
version 57.0 and later.

`dataSpaceApiName` string Stores the Data Space API Name from Data 360. Available in API version
60.0 and later.

`datasources` BatchCalcJob Collection of data source nodes in a data processing engine.
Datasource[]

`definitionRunMode` BatchCalcJobDefRunMode(enumeration Specifies the execution mode in a data processing engine. Valid values
of type string) are:

**•** `Batch`

**•** `OnDemand`

`description` string Description of a data processing engine definition.

`doesGenAllFailedRecords` boolean Indicates whether the error file includes a complete list of all failed
writeback records ( `true` ) or not ( `false` ). The default value is `false`,

and only the first instance of a failure is recorded in the error file. If set
to `true`, all failed records are recorded in the error file for the writeback
node.

Available in API version 65.0 and later.

`executionPlatformObjectType` ExecutionPlatformObjectType(enumeration
of type string)

The execution platform object type that's used during the read, transform,
and writeback process for the Data Processing Engine definition. Possible
values are:

**•** `CalculatedInsightsObject`

**•** `DataLakeObject`

**•** `DataModelObject`

**•** `None`

Available in API version 65.0 and later.

`executionPlatformType` ExecutionPlatformType(enumeration The platform that's used to run the Data Processing Engine definition.
of type string) Valid values are:

**•** `CRMA`

**•** `CDP`

**•** `CORE`


Metadata Types BatchCalcJobDefinition

**Field Name** **Field Type** **Description**

Available in API version 59.0 and later.

`filters` BatchCalcJobFilter[] Collection of filter nodes in a data processing engine. definition.

`forecasts` BatchCalcJobForecast[]

Collection of forecast nodes in a data processing engine. definition.

Available in API version 58.0 and later.

`hierarchyPaths` BatchCalcJobHierarchyPath[] Collection of hierarchy path nodes in a data processing engine definition.

`isTemplate` boolean Indicates whether it’s a template data processing engine definition.

`joins` BatchCalcJobSource Collection of join nodes in a data processing engine.
Join[]

`label` string The label of a data processing engine definition.

`parameters` BatchCalcJobParameter[] Collection of input variables in a data processing engine.

The process type of a data processing engine. These process types may
be available to you depending on your industry solution and permission
sets. Valid values are:

**•** `AccountingPeriodClosure`

**•** `AccountingSubledger` —This value is reserved for internal
use.

**•** `AccrualsAndPayoutEngine`

**•** `ActionableList`

**•** `AdvancedAccountForecast`

**•** `AutomotiveFoundation`

**•** `BenefitManagement`

**•** `BillingSchedulesforInvoiceGeneration`

**•** `CDPEnrichment`

**•** `ChannelInventoryManagement` —Available in API version
63.0 and later.

**•** `CollectionPlan` —Available in API version 65.0 and later.

**•** `CriteriaBsdSearchAndFilter`

**•** `DataProcessingEngine`

**•** `DecisionMatrixDataUpload`

**•** `Decisiontable`

**•** `Education`

**•** `EmployeeService` —Available in API version 63.0 and later.

**•** `EnergyUtilitiesSales`

**•** `FinancialSummaryRollup`

**•** `FlexibleHierarchy`


```
processType

```

BatchCalcProcessType
(enumeration of
type string)

Metadata Types BatchCalcJobDefinition

**Field Name** **Field Type** **Description**

**•** `ForeignExchangeGainLossCalculations` —Available
in API version 65.0 and later.

**•** `FSCHierarchyRollUp`

**•** `Fundraising` —Available in API version 64.0 and later.

**•** `FundraisingRollups` —Available in API version 63.0 and later.

**•** `GeneralLedgerAccountBalancesSummary` —Available
in API version 65.0 and later.

**•** `InventoryBatchSearch` —Available in API version 65.0 and
later.

**•** `InventorySearch` —Available in API version 65.0 and later.

**•** `InvoiceGeneration`

**•** `Loyalty`

**•** `LegalEntityAccountingPeriodClosureAdvanced` —Available
in API version 63.0 and later.

**•** `LifeSciencbatchcalesCommercialTerritoryAlignment` —Available
in API version 63.0 and later.

**•** `LifeSciencesCustomerEngagement` —Available in API
version 64.0 and later.

**•** `LoyaltyPartnerManagement`

**•** `LoyaltyPointsAggregation`

**•** `MediaAdSales`

**•** `NextGenForecasting` —Available in API version 64.0 and
earlier.

**•** `NetZero`

**•** `PatientServicesProgram` —Available in API version 64.0
and later.

**•** `PlanningAndForecasting`

**•** `PnmRosterFileUpload`

**•** `PriceProtection`

**•** `ProductCatalogManagement`

**•** `ProgramBasedBusiness`

**•** `ProviderSearch` —This value is reserved for internal use.

**•** `Rebates`

**•** `RebateAndAccrualManagementAdvanced`

**•** `Recruitment`

**•** `RevenueTransactionManagement` —Available in API version
63.0 and later.

**•** `SalesAgreement` —Available in API version 63.0 and later.

**•** `TestAtomicWritebackScale` —Available in API version 64.0
and later.


Metadata Types BatchCalcJobDefinition

**Field Name** **Field Type** **Description**

**•** `TestProcessType`

**•** `UsageManagement`

`status` BatchJobDefinition Status of a data processing engine definition. Valid values are:
Status

**•** `Active`
(enumeration of

**•** `Inactive`
type string)

`transforms` BatchCalcJobTransform[] Collection of data transformation nodes in a data processing engine.

`writebacks` BatchCalcJobWriteback Collection of writeback objects in which the results of the data processing
Object[] engine are written back.

BatchCalcJobAggregate

Represents a collection of fields relating to an aggregate node in a data processing engine.

Fields

**Field Name** **Field Type** **Description**

`description` string Description of an aggregate node.

`fields` BatchCalcJob Required. Collection of aggregation fields.
AggregateField[]

`groupBy` string[] Required. Collections of fields used to group data in an aggregate node.

`label` string Required. Label of an aggregate node.

`name` string Required. Name of an aggregate node.

`sourceName` string Required. Name of the source node.

BatchCalcJobAggregateField

Represents a collection of fields relating to an aggregation field in an aggregate node of a data processing engine.

Fields

**Field Name** **Field Type** **Description**

Required. Function used for aggregation.

Valid values are:

**•** `Unique` —A count of unique values.

**•** `Sum` —The sum of all values.


```
aggregateFunction

```

BatchCalcJobAggregateFunction
(enumeration of type
string)

Metadata Types BatchCalcJobDefinition

**Field Name** **Field Type** **Description**

**•** `Max` —The largest value.

**•** `Min` —The smallest value.

**•** `Avg` —The average value, calculated as the mean.

**•** `Std` —The standard deviation.

**•** `Stdp` —A standard deviation with population variance.

**•** `Var` —The variance.

**•** `VarP` —The variance with population.

**•** `Count` —The total count of values.

`alias` string Required. Name that subsequent nodes within the data processing engine use
to refer to the aggregate field.

`sourceFieldName` string Required. Source node field on which the aggregate is calculated.

BatchCalcJobAtomicWriteback

Represents a node in a DPE definition that stores the details about the relationship between the writeback nodes and the composite
writeback operations between the nodes.

**Field Name** **Field Type** **Description**

`description` string Description of the composite writeback object.

`label` string Required. Name of the composite writeback object.

`name` string Required. API name of the composite writeback object.

`writebackObject` BatchCalcJobAtomicWritebackRelationship[] Specifies the relationship between the writeback objects that are involved in
`Relationships` the writeback operation.

`writebackSequence` int Sequence in which the data processing engine executes the composite write
back node.

BatchCalcJobAtomicWritebackRelationship

Represents the relationships between the writeback objects that are involved in a composite writeback operation. It captures the
relationships between these objects and the sequence in which they should be processed.

**Field Name** **Field Type** **Description**

`childWriteback` string Field name that's associated with the child writeback object in a composite
`ObjectField` writeback relationship. Available in API version 63.0 and later.

`childWriteback` string Name of the child writeback object that's associated with the writeback
`ObjectName` relationship.


Metadata Types BatchCalcJobDefinition

**Field Name** **Field Type** **Description**

`parentWriteback` string Field name that's associated with the parent writeback object in a composite
`ObjectField` writeback relationship. Available in API version 63.0 and later.

`parentWriteback` string Required. Name of the parent writeback object that's associated with the
`ObjectName` writeback relationship.

`relationshipName` string Describes the relationship between the child and parent writeback objects in
a composite writeback node. Available in API version 64.0 and later.

`sequenceNumber` int Sequence number of the writeback node that's associated with its parent node
in the relationship.

BatchCalcJobCustomNode

Represents a collection of custom nodes in a data processing engine. Use a custom node to add a custom action.

Fields

**Field Name** **Field Type** **Description**

`description` string Description of a custom node.

`extensionName` string Required. Name of an extension node.

`extensionNamespace` string Required. Namespace of an extension node.

`label` string Required. Label of a custom node.

`name` string Required. Name of a custom node.

`parameters` BatchCalcJob The field mappings of an extension node.
CustomNodeParameter[]

`sources` string[] Sources of an extension node.

BatchCalcJobCustomNodeParameter

Represents the field mappings of an extension node.

Fields

**Field Name** **Field Type** **Description**

`name` string Required. Name of a parameter.

`value` string Required. Value of a parameter.


Metadata Types BatchCalcJobDefinition

BatchCalcJobDatasource

Represents a collection of fields relating to a data source node in a data processing engine.

Fields

**Field Name** **Field Type** **Description**

Specifies the field separator to read fields from a CSV file record.

Possible values are:

**•** `COMMA`

**•** `BACKQUOTE`

**•** `CARET`

**•** `PIPE`

**•** `SEMICOLON`

**•** `TAB`

The default value is `COMMA` .

The same delimiter value used for the CSV file can’t be used within any of the
column values in the file. If you mistakenly use the same delimiter value in
column values, it can cause data parsing issues.

```
CSVDelimiter

```

BatchCalcJobCSVDelimiter
(enumeration of type
string)

`description` string Description of a data source node.

`fields` BatchCalcJob Required. Collection of data source fields.
DatasourceField[]

`fileIdentifier` string Specifies the source of the file or file storage system.

`filePath` string The file path for the specified file.

Specifies the source of the file or file storage system.

Possible value is:

**•** `ContentManagement`

```
fileSource

```

BatchCalcJobFileSource
(enumeration of type
string)

`label` string Required. Label of a data source node.

`name` string Required. Name of a data source node.

`sourceName` string Required. Name of a standard or custom object from which the data source
node extracts data.

```
type

```

BatchCalcJobDataSource Required. Type of object for the source object field. Supported values are:
Type (enumeration of

**•** `Analytics`

type string)

**•** `Analytics`

**•** `CalculatedInsightsObject`

**•** `CRMObject`

**•** `CSV`

**•** `DataModelObject`


Metadata Types BatchCalcJobDefinition

**Field Name** **Field Type** **Description**

**•** `StandardObject`

.

BatchCalcJobDatasourceField

Represents a collection of fields relating to a source object field that are selected in the data source node of a data processing engine.

Fields

**Field Name** **Field Type** **Description**

`alias` string Name that subsequent nodes within the data processing engine use to refer
to the data source field. Required when the field name is lookup.

Specifies the data type of the input field when using a CSV file as a data source.

Possible values are:

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

