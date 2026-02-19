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


Metadata Types AuthProvider

**Field Name** **Field Type** **Description**

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


Metadata Types AuthProvider

**Field Name** **Field Type** **Description**

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


Metadata Types AuthProvider

**Field Name** **Field Type** **Description**

`<token>`, where `<token>` is the base64-encoded string
`"clientkey:clientsecret"` . Available in API version 30.0 and
later.

`sendSecretInApis` boolean

`ssoKickoffUrl` string

`tokenUrl` string

`userInfoUrl` string

AuthProvParamFwdAllowlist

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
it to send a user's language preference from Salesforce to the third-party provider's login page.


Metadata Types AuthProvider

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


### Metadata Types AutoResponseRules

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

### AutoResponseRules

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


Metadata Types AutoResponseRules

File Suffix and Directory Location

AutoResponseRules for an object have the suffix `.autoResponseRules` and are stored in the `autoResponseRules` folder.
For example, all Case auto-response rules are stored in the `Case.autoResponseRules` file.

Version

AutoResponseRules components are available in API version 27.0 and later.

Fields

**Field Name** **Field Type** **Description**

`autoresponseRule` AutoResponseRule[] Represents the definitions of the named auto-response rules.

AutoResponseRule

Represents whether a rule is active or not and the order in which the entry is processed in the rule.

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


### Metadata Types BatchCalcJobDefinition

**Field Name** **Field Type** **Description**

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


Metadata Types BatchCalcJobDefinition

File Suffix and Directory Location

BatchCalcJobDefinition components have the suffix `.batchCalcJobDefinition` and are stored in the
`batchCalcJobDefinitions` folder.

Version

BatchCalcJobDefinition components are available in API version 51.0 and later.

Special Access Rules

To use this metadata type, one of these licenses is required:

**•** Loyalty Management

**•** Financial Services Cloud

**•** Rebate Management

**•** Manufacturing Cloud

**•** Net Zero Cloud

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


Metadata Types BatchCalcJobDefinition

**Field Name** **Field Type** **Description**

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

**•** `ActionableList`

**•** `AdvancedAccountForecast`

**•** `BenefitManagement`


```
processType

```

BatchCalcProcessType
(enumeration of
type string)

Metadata Types BatchCalcJobDefinition

**Field Name** **Field Type** **Description**

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

**•** `FinancialSummaryRollup`

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

**•** `NextGenForecasting` —Available in API version 64.0 and
earlier.

**•** `NetZero`

**•** `PatientServicesProgram` —Available in API version 64.0
and later.

**•** `PnmRosterFileUpload`

**•** `PriceProtection`

**•** `ProductCatalogManagement`


Metadata Types BatchCalcJobDefinition

**Field Name** **Field Type** **Description**

**•** `ProgramBasedBusiness`

**•** `ProviderSearch` —This value is reserved for internal use.

**•** `Rebates`

**•** `Recruitment`

**•** `RevenueTransactionManagement` —Available in API version
63.0 and later.

**•** `SalesAgreement` —Available in API version 63.0 and later.

**•** `TestAtomicWritebackScale` —Available in API version 64.0
and later.

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


Metadata Types BatchCalcJobDefinition

Fields

**Field Name** **Field Type** **Description**

Required. Function used for aggregation.

Valid values are:

**•** `Unique` —A count of unique values.

**•** `Sum` —The sum of all values.

**•** `Max` —The largest value.

**•** `Min` —The smallest value.

**•** `Avg` —The average value, calculated as the mean.

**•** `Std` —The standard deviation.

**•** `Stdp` —A standard deviation with population variance.

**•** `Var` —The variance.

**•** `VarP` —The variance with population.

**•** `Count` —The total count of values.

```
aggregateFunction

```

BatchCalcJobAggregateFunction
(enumeration of type
string)

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


Metadata Types BatchCalcJobDefinition

**Field Name** **Field Type** **Description**

`childWriteback` string Field name that's associated with the child writeback object in a composite
`ObjectField` writeback relationship. Available in API version 63.0 and later.

`childWriteback` string Name of the child writeback object that's associated with the writeback
`ObjectName` relationship.

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


Metadata Types BatchCalcJobDefinition

Fields

**Field Name** **Field Type** **Description**

`name` string Required. Name of a parameter.

`value` string Required. Value of a parameter.

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


Metadata Types BatchCalcJobDefinition

**Field Name** **Field Type** **Description**

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

`isPrimaryKey` boolean Indicates whether a column name is the primary key ( `true` ) or not ( `false` )
for the Data Cloud CSV file.

`name` string Required. Name of the field. Can be either of the following:

**•** Name of the source field selected in the associated data source object.

**•** Name from a nested lookup object with three child levels.

BatchCalcJobFilter

Represents a collection of fields relating to a filter node in a data processing engine.


Metadata Types BatchCalcJobDefinition

Fields

**Field Name** **Field Type** **Description**

`criteria` BatchCalcJobFilter
Criteria[]

Collection of filter criteria in a filter node.

The field is required when `isDynamicFilter` is set to `False` .

`description` string Description of the batch calculation job filter.

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


Metadata Types BatchCalcJobDefinition

**Field** **Field Type** **Description**
**Name**

forecast values for the
specified forecast length.

`description` string The description of the
forecast node.

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

Metadata Types BatchCalcJobDefinition

**Field** **Field Type** **Description**
**Name**

`groupFields` BatchCalcJobFrcstGrpFld[] The source fields for
grouping the data to be

processed by the forecast
node.

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

Metadata Types BatchCalcJobDefinition

**Field** **Field Type** **Description**
**Name**

**•** `TwentyOne`

**•** `TwentyTwo`

**•** `TwentyThree`

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

Metadata Types BatchCalcJobDefinition

**Field Name** **Field Type** **Description**

**•** `Var`

**•** `VarP`

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
on page 460[]

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
on page 471[] the Batch Management job.

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

**•** `Flow`

**•** `Loyalty Program Process`

BatchDataSource

Represents the source of information whose records must be processed by the Batch Management job.

Fields

**Field Name** **Field Type** **Description**

`condition` string Required. Criteria defined to filter the records.

`criteria` string Type of filter criteria that’s used to filter records for processing.


Metadata Types BatchProcessJobDefinition

**Field Name** **Field Type** **Description**

`dataSourceType` string Type of data source that's used to create the batch job definition. Valid values
are:

**•** SingleSobject

**•** MultiSobject

Available in API version 64.0 and later.

`filters` BatchDataSrcFilterCriteria Filter criterion that decides which records must be processed by the Batch
on page 472[] Management job.

orderFields BatchDataSourceOrderField Fields that are used to order the records before the records are added to a
on page 473 batch in a job.

`sourceObject` string

`sourceObjectField` string

BatchDataSrcFilterCriteria

Required. API name of an object whose records must be processed by the
batch job.

If the batch job type is Loyalty Program Process, the source object must be:

**•** TransactionJournal if the batch job is used to process transaction journals
by applying the applicable loyalty program process.

**•** An object that stores the details of loyalty program members whose tier
must be assessed by the loyalty program process specified in the
executionProcessApiName field.

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


Metadata Types BatchProcessJobDefinition

**Field Name** **Field Type** **Description**

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

```


Metadata Types BatchProcessJobDefinition

```
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

```


Metadata Types BatchProcessJobDefinition

```
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


### Metadata Types BillingSettings BillingSettings

Represents the settings for Salesforce Billing.

Parent Type and Manifest Access

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

[In the package manifest, all the settings metadata types for the org are accessed using the “Settings” name. See Settings for more details.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_settings.htm)

File Suffix and Directory Location

### The BillingSettings values are stored in the BillingSettings.settings file in the settings folder. The .settings

files are different from other named components, because there’s only one settings file for each settings component.

Version

### BillingSettings components are available in API version 62.0 and later.

Special Access Rules

These settings are available when Billing is enabled.

Fields

**Field Name** **Description**

```
acctRecGlAccount

billingContextDefinition

billingContextSourceMapping

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
[Name of the context definition that the Create Billing Schedules for Orders API uses](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/connect_resources_create_billing_schedules.htm)
to understand your order data. Available in API version 64.0 and later.

**Field Type**
string

**Description**
Name of the context mapping that links Order fields to billing transaction context
nodes. Available in API version 64.0 and later.


Metadata Types BillingSettings

**Field Name** **Description**

```
billingIntraCtxtSrcMapping

defaultAPClosureDPEDefnName

defaultApplyCreditMemoFlow

defaultBillingTreatment

defaultEmailTemplate

defaultInvPreviewTemplate

defaultInvoiceDocTemplate

defaultLegalEntity

```

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

**Description**
Default flow that’s used to apply the credit memo to invoices. Available in API version
64.0 and later.

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


Metadata Types BillingSettings

**Field Name** **Description**

**Description**
Org-wide default value to specify the name of the legal entity. Available in API version
64.0 and later.

```
defaultTaxTreatment

enableBillingDisputeManagement

enableBillingSetup

enableCreditMemoSequenceService

enableCrMemoApplicationToPostedInvoices

enableFailedPaymentsRetry

```

**Field Type**
string

**Description**
Org-wide default value to specify the name of the tax treatment. Available in API
version 64.0 and later.

**Field Type**
boolean

**Description**
Indicates whether to enable Dispute Management ( `true` ) or not ( `false` ). The default
value is `false` . Available in API version 66.0 and later.

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


Metadata Types BillingSettings

**Field Name** **Description**

**Description**

Indicates whether to retry failed payment schedule items automatically based on the
defined payment retry rules ( `true` ) or not ( `false` ). The default value is `false` .
Available in API version 66.0 and later.

```
enableForeignExchangeTrxnJrnlCreation

enableInvoiceEmailDelivery

enableInvoicePdfGeneration

enableInvoiceSequenceService

enableNegInvoiceLnConversionToCrMemoLn

```

**Field Type**
boolean

**Description**

Indicates whether to create Transaction Journal records for invoices that hold balance
amounts (partially settled and not fully settled posted invoices) to record foreign
exchange unrealized gains or losses during the closure activity of a legal entity
accounting period. The default value is `false` . Available in API version 65.0 and later
with Revenue Cloud Billing.

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


Metadata Types BillingSettings

**Field Name** **Description**

```
enablePaymentSchedulesAndItemsCreation

enableTransactionJournalCreation

enableTransactionsApplicationToInvoices

```

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


Metadata Types BillingSettings

**Field Name** **Description**

**Revenue Cloud Billing**

This setting applies balances of credit memos and payments to invoices or balances
of credit memo lines and payments lines to invoice lines. For the latter, amounts and
balances on the invoices are rolled-up from the related invoice lines.

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


### Metadata Types BlacklistedConsumer

**Field Name** **Description**

**Description**
Name of the general ledger account to record unrealized losses in transaction journals.
Available in API version 64.0 and later.

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

      <version> 66.0 </version>

   </Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The wildcard
[applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the manifest](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_settings.htm)
[file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### BlacklistedConsumer

Represents a connected app that is inaccessible to your Salesforce org’s users.This type extends the Metadata metadata type and inherits
its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.


Metadata Types BlacklistedConsumer

File Suffix and Directory Location

BlacklistedConsumer components have the suffix `.blacklistedConsumer` and are stored in the `blacklistedConsumers`
folder.

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

```


### Metadata Types Bot

```
      <version>49.0</version>

   </Package>

```

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
page 485

Specifies the agent type for this agent. For example,
`AgentforceServiceAgent` . Available in API version 64.0 and
later.

Represents the Einstein intent set that groups intents, entities, and
variables associated with a bot. All Einstein Bot versions under the same
bot now share an intent set. Available in API version 44.0 and later.


Metadata Types Bot

**Field Name** **Field Type** **Description**

`botUser` string Specifies the username of the user account, not the first and last name
or the user ID. Available in API version 46.0 and later.

`botVersions` BotVersion on page Represents the configuration details for a specific Einstein Bots version,
505 including dialogs, intents, entities, and variables.

`contextVariables` ConversationContextVariable Represents the context variables that enable your bot to gather customer
on page 486 information regardless of channel. Available in API 45.0 and later.

`conversationChannelProviders` ConversationDefintonChannelProvider **i** Represents a list of the conversation channels linked to the bot. Available

[] on page 487 in API version 51.0 and later.

`defaultOutboundFlow` string Specifies a fallback escalation behavior if the primary agent escalation
behavior is not available. For example, Agentforce Service Agents can

route conversations to human service reps. Available in API version 65.0
and later.

`description` string A description of the bot.

`label` string Label that identifies the bot throughout the Salesforce user interface.

`logPrivateConversationData` boolean Specifies whether to log customer inputs as part of conversation data
( `true` ) or not ( `false` ). Available in API version 48.0 and later.

`pageContextVariables` PageContextVariable Provides page-level context variables for the bot. Available in API version
on page 488[] 64.0 and later.

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


Metadata Types Bot

**Field Name** **Field Type** **Description**

`name` string Required. This unique name prevents conflicts with other local Einstein Intent
Sets. This name can contain only underscores and alphanumeric characters

and must be unique in your org. It must begin with a letter, not include spaces,
not end with an underscore, and not contain two consecutive underscores.

ConversationContextVariable

A context variable local to the current bot version. Available in API version 45.0 and later.

**Field Name** **Field Type** **Description**

`contextVariableMappings` ConversationContextVariableMapping Represents the mapping between a context variable, channel type, and sObject
on page 487 field.

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


Metadata Types Bot

**Field Name** **Field Type** **Description**

`SObjectType` string Valid values are:

**•** `BotDefinition`

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

BotDialog[] on page 509


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

ConversationDefinitionGoal[] on page 529

**Description**
The list of goals in this bot block. Available in API version 57.0 and later.

**Field Type**
string

**Description**

Required.

Specifies the language of the bot block.

**Field Type**

ConversationVariable[] on page 530

**Description**
A container that stores a specific piece of data collected from the customer. You can
use variables within dialog actions as both inputs and outputs. Available in API version
44.0 and later.

**Field Type**
string

**Description**
A description of the bot block.

**Field Type**

LocalMlDomain on page 485

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

BotDialogGroup[] on page 508

**Description**
The list of dialog groups in this bot template.

**Field Type**

BotDialog[] on page 509

**Description**
The list of dialogs in this bot template.

**Field Type**
string

**Description**

Required.

Specifies the language of the bot template.

**Field Type**

ConversationContextVariable[] on page 486

**Description**
Represents the context variables that enable your bot to gather customer information
regardless of channel.

**Field Type**

ConversationDefinitionGoal[] on page 529

**Description**
The list of goals in this bot template. Available in API version 57.0 and later.

**Field Type**

ConversationSystemDialog[] on page 530

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

ConversationVariable[] on page 530

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

LocalMlDomain on page 485

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

BotDialogGroup[] on page 508

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

BotDialog[] on page 509

**Description**
The list of dialogs in this bot version.

**Field Type**
string

**Description**
Reserved for internal use.

**Field Type**

ConversationDefinitionGoal[] on page 529

**Description**
The list of goals in this bot verion. Available in API version 57.0 and later.

**Field Type**

ConversationDefinitionPlanner[] on page 529

**Description**
Represents the API name of the Agent planner service GenAiPlanner on page 1358.

Available in API version 60.0 and later.

**Field Type**

ConversationSystemDialog[] on page 530

**Description**
A system function assigned to a dialog. Available in API version 48.0 and later.

**Field Type**

ConversationVariable[] on page 530

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

ConversationDefinitionNlpProvider[] on page 532

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

BotStep[] on page 511

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

BotInvocation on page 513

**Description**
Bot Invocation used by a BotStep of type `Invocation` .

**Field Type**

BotMessage[] on page 515

**Description**
List of bot messages used by a BotStep of type `Message` .

**Field Type**

BotNavigation on page 515

**Description**
Bot Navigation used by a BotStep of type `Navigation` .

**Field Type**

BotStepCondition[] on page 517

**Description**
List of BotStep conditions associated with a BotStep of type `Group` .

**Field Type**

BotStep[] on page 511

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

BotVariableOperation[] on page 518

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

ConversationRecordLookup[] on page 523

**Description**
A lookup action to the Conversation record. Available in API version 46.0 and later.

**Field Type**

ConversationDefinitionStepGoalMapping[] on page 527

**Description**
The API name of a goal used by a BotStep of type GoalStep. Available in API version
57.0 and later.

**Field Type**

ConversationSystemMessage[] on page 527

**Description**
System messages that represent an action for a BotStep, such as transferring to an
agent or ending a chat. Available in API version 46.0 and later.

**Field Type**

ConversationDefinitionRichMessage[] on page 528

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

BotInvocationMapping[] on page 514

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

BotNavigationLink[] on page 516

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

BotInvocation on page 513

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

BotMessage[] on page 515

**Description**
List of Bot Messages used as prompt messages by a Bot Variable Operation of type
`Collect` .

**Field Type**

BotQuickReplyOption[] on page 521

**Description**
List of static choice options used by a Bot Variable Operation of type `Collect` and
`quickReplyType` of `Static` .

**Field Type**

BotVariableOperand[] on page 522

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

BotNavigation on page 515

**Description**
Bot Navigation used by a Bot Variable Operation of type `Collect` . This navigation
is executed when the associated Bot Invocation doesn’t return any options.

**Field Type**

ConversationDefinitionRichMessage on page 528

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

BotMessage[] on page 515

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

BotMessage[] on page 515

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

ConversationRecordLookupCondition[] on page 525


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

ConversationRecordLookupField[] on page 526

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

ConversationSystemMessageMapping on page 527

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

BotInvocationMapping[] on page 514

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
on page 551[]

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
on page 551[]

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

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

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
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### CareLimitType

Defines the characteristics of limits on benefit provision.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

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
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

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

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

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


### Metadata Types Certificate

```
      <version>44.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### Certificate

Represents a certificate used for digital signatures that verify that requests are coming from your org. Certificates are used for either
authenticated single sign-on with an external website, or when using your org as an identity provider. This type extends the Metadata
With Content metadata type and inherits its `content` and `fullName` fields.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### Certificate components have the suffix .crt and are stored in the certs folder.

Version

### Certificate components are available in API version 36.0 and later.

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

### keySize int Certificate keys can be either 2048 bits or 4096 bits. A certificate with

4096-bit keys lasts 2 years, and a certificate with 2048-bit keys lasts 1

year. Certificates with 2048-bit keys are faster than certificates with
4096-bit keys. If `keySize` isn’t specified when you create a certificate,
the key size defaults to 2048 bits.


Metadata Types Certificate

**Field Name** **Field Type** **Description**

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


### Metadata Types ChatterExtension ChatterExtension

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

     <masterLabel>primary</masterLabel>

     <renderComponent>xwRend</renderComponent>

     <type>Lightning</type>

   </ChatterExtension>

```

Version

### ChatterExtension is a new feature in API version 41.0.

Fields

**Field** **Field Type** **Description**

`compositionComponent` string Required. The composition component of the Rich Publisher
App that you provide. It’s comprised of the

```
                              lightning:availableForChatterExtensionComposer
```

interface.

`description` string Required. The description of your custom Rich Publisher App.


### Metadata Types ChoiceList

**Field** **Field Type** **Description**

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

Wildcard Support in the Manifest File

Required. Describes the type of the extension. Currently, the
only value supported is _`Lightning`_ . Included to allow for
other possible types in the future.

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

[Integrate Your Custom Apps into the Chatter Publisher](https://developer.salesforce.com/docs/atlas.en-us.260.0.lightning.meta/lightning/components_integrate_customapps_to_publisher.htm)

### ChoiceList

Represents the `Choicelist` dropdown field that’s used for pre-chat.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types ChoiceList

File Suffix and Directory Location

ChoiceList components have the suffix `.ChoiceList` and are stored in the `ChoiceList` folder.

Version

ChoiceList components are available in API version 62 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Description**

```
choiceListValue

description

masterLabel

```

ChoiceListValue

**Field Type**

ChoiceListValue[]

**Description**
A list of choices to display in the choice list.

**Field Type**
string

**Description**
A description of the choice list.

**Field Type**
string

**Description**

Required. The label for the choice list.

Represents a choice list value in the pre-chat dropdown. ChoiceListValue is available in API version 62 or later.

**Field Name** **Description**

```
embeddedServiceCustomLabels

isDefaultValue

```

**Field Type**

EmbeddedServiceCustomLabel[] on page 1003

**Description**
Custom labels for the choicelist value.

**Field Type**
boolean


Metadata Types ChoiceList

**Field Name** **Description**

**Description**

Required. Indicates whether the choicelist value should be selected by default.

```
order

valueName

```

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


### Metadata Types ClaimFinancialSettings

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
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### ClaimFinancialSettings

Represents the configuration settings for Insurance Claim Financial Services.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ClaimFinancialSettings components have the suffix claimFinancialSettings and are stored in the ClaimFinancialSettings folder.

Version

### ClaimFinancialSettings components are available in API version 57.0 and later.

Special Access Rules

To access this metadata type, you require access to either InsurancePolicyAdminAccess or InsuranceClaimMgmtAccess add-on license.

Fields

**Field Name** **Description**

```
claimCovPendingAuthStatus

```

**Field Type**
string


Metadata Types ClaimFinancialSettings

**Field Name** **Description**

**Description**

Required.

The status of pending financial authority for claim coverage.

```
claimPendingAuthorityStatus

clmCovPymtDtlPendAuthSts

masterLabel

```

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

```


### Metadata Types ClauseCatgConfiguration

```
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

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

### ClauseCatgConfiguration components have the suffix .clauseCatgConfiguration and are stored in the

`clauseCatgConfigurations` folder.

Version

### ClauseCatgConfiguration components are available in API version 57.0 and later.

Special Access Rules

The ClauseManagementAddOn license is required to access this object along with user access for the Clause Designer User permission
set license.

Fields

**Field Name** **Description**

```
description

isProtected

```

**Field Type**
string

**Description**
The description about the clause category configuration.

**Field Type**
boolean


Metadata Types ClauseCatgConfiguration

**Field Name** **Description**

**Description**
An auto-generated value that doesn’t impact the behavior of the metadata type. The
default is `false` .

```
masterLabel

usageType

```

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

```


### Metadata Types CleanDataService

```
    <version>57.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

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

`description` string Required. A description of the data service

`masterLabel` string Required. Label for this data service. Although this value is displayed, it’s
an internal label for the data service and isn’t translated.

`matchEngine` string Required. A key that maps to the internal data service identifier.

CleanRule

Represents information that controls how the data service adds and updates data in an org.


Metadata Types CleanDataService

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

FieldMapping

Required. A standard object that’s the target of additions and updates specified
by this CleanRule. Specifying an object that the data service does not support
causes an error.

Represents a mapping between fields in the data service and fields in an object in the org.

**Field Name** **Field Type** **Description**

`developerName` string Required. This name can contain only underscores and alphanumeric characters,
and must be unique in your org. It must begin with a letter, not include spaces,

not end with an underscore, and not contain two consecutive underscores.
This unique name prevents conflicts with field mappings from other packages
that have the same `masterLabel` .


Metadata Types CleanDataService

**Field Name** **Field Type** **Description**

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

`dataServiceObjectName` string

Required. An object in the data service that contains the FieldMappingRow
associated with this FieldMappingField. Specifying a non-existent object causes
an error.

`priority` int Required. Represents the priority that the data service uses when it updates
the field, relative to other update rules for the same field. Valid values are 1-100.


Metadata Types CleanDataService

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

```


Metadata Types CleanDataService

```
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

Usage

Use CleanDataService to retrieve all the metadata that describes a data enrichment service. To configure the service in a new org, deploy
the metadata you retrieved. Avoid using CRUD-Based Calls with CleanDataService.

To make small modifications to the CleanDataService component, use the Tooling API.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types CMSConnectSource CMSConnectSource

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
page 591[]

**•** 0–10 for CSS

**•** 0–10 for JavaScript

`cmsConnectLanguage` CMSConnectLanguage 0 to more. Represents language mappings defined for the connection.
on page 591[]

`cmsConnectPersonalization` CMSConnectPersonalization[] 0 or 1. Represents personalization defined for the connection. Only
on page 591 for use when `type` is `AEM` .

`cmsConnectResourceType` CMSConnectResourceType 0–5. Represents JSON definitions defined for the connection.
on page 592[]

`connectionType` CMSSourceConnectionType(enumeration Required. Type of authentication being used with outside system.
of type string) Valid values are:

**•** `Public`

**•** `Authenticated`

`cssScope` string The class name used to prefix and scope the CSS rules.


Metadata Types CMSConnectSource

**Field Name** **Field Type** **Description**

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

`websiteUrl` string Required if `connectionType` is `Public`

Note: Because there can be existing connections when a package comes in, there’s some INSERT or UPDATE logic to consider:

**•** If you find `developerName` in the destination, then update the existing collection with all details form source.

**•** `namedCredential` is handled through `developerName` . If you don’t find `namedCredential` with
`developerName`, then an error is generated.

**•** If the destination isn’t `sortOrder` from the source, then insert or update with the source `sortOrder` .

**•** If `sortOrder` from the source is already in the destination, then increase the source `sortOrder` by 1 for connections
such that the destination `sortOrder`     - `sortOrder` from the source.


Metadata Types CMSConnectSource

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

`language` string

CMSConnectPersonalization

Salesforce supported language.

For information see
[https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_translations.htm](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_translations.htm)

CMSConnectPersonalization is used only with Adobe Experience Manager (AEM).

Note: Because there can be existing connections when a package comes in, there’s some INSERT or UPDATE logic to consider. If
personalization isn’t enabled in the source system, but is enabled in the destination, the destination is disabled. The record for the
connection is deleted from the table.


Metadata Types CMSConnectSource

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
on page 592[]

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


Metadata Types CMSConnectSource

**Field Name** **Field Type** **Description**

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

```


Metadata Types CMSConnectSource

```
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


Metadata Types CMSConnectSource

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

[Developer Guide: Deploying and Retrieving Metadata](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based.htm)

[Salesforce Help: Use Personalized Content in CMS Connect](https://help.salesforce.com/articleView?id=communities_cms_connect_personalization.htm&type=5&language=en_US)

[Developer Guide: Translations](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_translations.htm)

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

**Field Name** **Field Type** **Description**

`active` boolean Indicates whether the zone is active ( `true` ) or not ( `false` ).

`chatterAnswersFacebookSsoUrl` string (Read only) The Facebook sign-on URL, which is based on the Facebook
authentication provider selected in your Chatter Answers settings. This

field is available only if Chatter Answers and Facebook Single Sign-On
for Chatter Answers are enabled.

`communityFeedPage` string The Visualforce page that hosts the zone’s feeds. This field is available
when Chatter Answers is enabled in the organization.


Metadata Types Community (Zone)

**Field Name** **Field Type** **Description**

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


Metadata Types Community (Zone)

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

```


### Metadata Types CommerceSettings

```
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

File Suffix and Directory Location

### CommerceSettings values are stored in the Commerce.settings file in the settings folder. The .settings files are different

from other named components, because there’s only one settings file for each settings component.

Version

Commerce Settings are available in API version 50.0 and later.

Special Access Rules

A B2B Commerce or D2C Commerce license and access to Commerce objects is required.


Metadata Types CommerceSettings

Fields

**Field Name** **Description**

```
buyerGroupExtensibility

commerceAnalyticsEnabled

commerceAppEnabled

commerceConciergeEnabled

commerceCopilotEcomEnabled

commerceDCSegmentEnabled

commerceDiscoveryExpansion

commerceEnabled

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

**Description**
Indicates whether the Data 360 segment integration is enabled ( `true` ) or not ( `false` ).

**Field Type**
boolean

**Description**
Indicates whether the Commerce Discovery Expansion service is enabled ( `true` ) or
not ( `false` ).

**Field Type**
boolean


Metadata Types CommerceSettings

**Field Name** **Description**

**Description**
Indicates whether Commerce is enabled ( `true` ) or not ( `false` ).

```
commerceNGPEnabled

commerceRLMSubs

generateInvPerSubscription

lowestUnitPriceTracking

messagingEngagementDataKit

```

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

```


### Metadata Types CommunityTemplateDefinition

```
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

Version

### CommunityTemplateDefinition components are available in API version 38.0 and later.

Special Access Rules

This type is available only if Salesforce Digital Experiences is enabled in your org.


Metadata Types CommunityTemplateDefinition

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
implemented in CommunityThemeDefinition on page 608.

`defaultThemeDefinition` string Required. The assigned theme definition for this
CommunityTemplateDefinition.

`description` string The optional description text of this CommunityTemplateDefinition.

`enableExtendedCleanUp` boolean False by default. Determines if deleting this
`OnDelete` CommunityTemplateDefinition attempts to delete other directly or
indirectly referenced objects automatically, for example,
CommunityThemeDefinition on page 608, Flexipage on page 1188, or
StaticResource on page 2314. Values are true or false.

`masterLabel` string Required. The label for this CommunityTemplateDefinition, which displays
in Setup.

`navigationLinkSet` NavigationLinkSet The navigation menu associated with this CommunityTemplateDefinition.
A navigation menu consists of items that users can click to go to other

parts of the site. Available in API versions 37.0 to 46.0. In API versions
47.0 and later, use NavigationMenu.

`pageSetting` CommunityTemplatePageSe **t** ing[] The list of FlexiPage of this CommunityTemplateDefinition.

`publisher` string

Defines the name of the publisher as seen in the Change Theme wizard.
If no name is provided, the name of the org from which the package
was originally exported is used.

This field is available in API version 45.0 and later.


Metadata Types CommunityTemplateDefinition

CommunityTemplateBundleInfo

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

```


Metadata Types CommunityTemplateDefinition

```
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

```


Metadata Types CommunityTemplateDefinition

```
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

```


Metadata Types CommunityTemplateDefinition

```
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

```


### Metadata Types CommunityThemeDefinition

```
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

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### CommunityThemeDefinition

Represents the definition of a theme for an Experience Builder site. This type extends the Metadata metadata type and inherits its
`fullName` field.


Metadata Types CommunityThemeDefinition

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

CommunityThemeDefinition components have the suffix `.communityThemeDefinition` and are stored in the
`communityThemeDefinitions` folder.

Version

CommunityThemeDefinition components are available in API version 38.0 and later.

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
CommunityThemeDefinition, as defined in the Theme panel in Experience
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

`publisher` string

Defines the name of the publisher as seen in the wizard for creating
Experience Builder sites. If no name is provided, the name of the org
from which the package was originally exported is used.

This field is available in API version 45.0 and later.

`themeRouteOverride` CommunityThemeRouteOve **r** ide[] List of theme layout type overrides for flexipages (currently only for
home). Available in API version 44.0 and later.

`themeSetting` CommunityTheme Required. The list of settings for this CommunityThemeDefinition.
Setting []


Metadata Types CommunityThemeDefinition

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


Metadata Types CommunityThemeDefinition

**Field Name** **Field Type** **Description**

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

```


### Metadata Types ConnectedApp

```
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

### ConnectedApp

Represents a connected app configuration. A connected app enables an external application to integrate with Salesforce using APIs and
standard protocols, such as SAML, OAuth, and OpenID Connect. Connected apps use these protocols to authenticate, authorize, and
provide single sign-on (SSO) for external apps. The external apps that are integrated with Salesforce can run on the customer success
platform, other platforms, devices, or SaaS subscriptions.

This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types ConnectedApp

Important: Connected apps creation is restricted as of Spring ‘26. You can use existing connected apps during and after Spring
[‘26. However, we recommend using external client apps instead. If you must continue creating connected apps, contact Salesforce](https://help.salesforce.com/s/articleView?id=xcloud.external_client_apps.htm&language=en_US)
Support.

[See New connected apps can no longer be created in Spring ‘26 for more details.](https://help.salesforce.com/s/articleView?id=005228017&type=1&language=en_US)

File Suffix and Directory Location

ConnectedApp components have the suffix `.connectedApp` and are stored in the `connectedApps` folder.

Version

ConnectedApp components are available in API version 29.0 and later.

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

`ipRanges` ConnectedAppIpRange[] Specifies the ranges of IP addresses that can access the app without
requiring the user to authenticate with the connected app.

`label` string Required. The name of the app.

`logoUrl` string An optional logo for the app. The logo appears with the app’s entry
in the list of apps and on the consent page the user sees when

authenticating. The URL must use HTTPS, and the logo can't be larger
than 125 pixels high or 200 pixels wide. The default logo is a cloud.

`mobileStartUrl` string Users are directed to this URL after they've authenticated when the
app is accessed from a mobile device. If you don't give a URL, the user

is sent to the app’s default start page after authentication completes.
If the connected app that you’re creating is a canvas app, then you
can leave this field blank. The Canvas App URL field contains the URL
that gets called for the connected app.

`oauthConfig` connectedAppOauthConfig Specifies how your app communicates with Salesforce.


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

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

`ConnectedAppPlugin` [class in the Apex Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_namespace_Auth.htm)
Available in API version 46.0 and later.

Enter a user that is part of your org. Otherwise, the user is removed
from this field when you deploy the connected app. If you don’t want
to specify a user, you can leave this field empty.

To use this field in an org, the ConAppPluginExecuteAsUser setting
must be enabled.

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


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

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


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

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


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

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


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

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
of headless login, headless registration, headless passwordless login,
and headless guest identity.

If set to `true`, the connected app can use the Authorization Code and
Credentials Flow and all associated Headless Identity features. The
default value is `false` .

This field is available in API version 57.0 and later.

`isCodeCredentialPostOnly` boolean For the Authorization Code and Credentials Flow, determines whether
the user’s credentials must be sent in the body of the initial HTTPS POST


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

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
we always recommend implementing PKCE for public clients. We also
strongly recommend that you implement PKCE for private clients.

If set to `true`, the PKCE extension is required and any authorization
code flow variations that don’t implement it fail. If set to `false`, you
can still implement PKCE but it isn’t required. The default value is
`false` .

This field is available in API version 59.0 and later.

`isRefreshTokenRotationEnabled` boolean If set to `true`, the connected app issues a new refresh token each
time the OAuth refresh token flow is invoked. The old refresh token is


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

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

`scopes` ConnectedAppOauthAccessScope The permissions given by the user running the connected app. When
(enumeration of type string)[] deploying metadata, valid values are:

**•** `Basic` —Allows access to your identity URL service (the same
behavior as deploying `Address`, `Email`, `Phone`, and
`Profile` ).

**•** `Api` —Allows access to the logged-in user's account over the APIs.

**•** `Web` —Allows use of the `access_token` on the web. This
usage also includes `visualforce`, allowing access to Visualforce
pages.


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

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

**•** `Content` —Allows hybrid apps to directly obtain content child
sessions through the OAuth 2.0 hybrid app token flow and hybrid
app refresh token flow. Available in API version 51.0 and later.

**•** `CDPIngest` —Allows access to Data Cloud ingest API services.
Customers use these API services to upload and maintain external
datasets in the Data 360. Available in API version 52.0 and later.

**•** `Chatbot` —Allows access to Einstein Bot API services. Available
in API version 54.0 and later.


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

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

**•** `RefreshToken` —Allows a refresh token to be returned if you’re
eligible to receive one and is synonymous with allowing
`OfflineAccess` .

**•** `Wave` —Allows access to the Analytics REST API resources. Available
in API version 35.0 and later.

**•** `Eclair` —Allows access to the Analytics REST API Charts Geodata
resource. Available in API version 35.0 and later.


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

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

`assetSigningCertId` string

`assetValidityPeriod` int

Required. If set to `true` (default), custom attributes associated with
the connected app are included in the asset token payload. If set to
`false`, these attributes aren’t included.

Required. If set to `true` (default), custom permissions associated with
the connected app are included in the asset token payload. If set to
`false`, these permissions aren’t included.

Required. The ID of the JWT certificate’s signing secret. The certificate
size can’t exceed 4 KB. If it does, try using a DER encoded file to reduce
the size.

Required. The asset token’s validity period. The validity must be the
expiration time of the assertion within 3 minutes, expressed as the
number of seconds from 1970-01-01T0:0:0Z measured in UTC.


Metadata Types ConnectedApp

ConnectedAppOauthIdToken

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
completes identity verification if accessing Salesforce from a
new browser or device.

**•** `BYPASS` —Allows a user to run this app without org IP restrictions.

**•** `ENFORCE_RELAXREFRESH` —Enforces the IP restrictions
configured for the org, such as the IP ranges assigned to a user
profile. However, this option bypasses these restrictions when the
connected app uses refresh tokens to get access tokens.


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

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

The single logout URL must be an absolute URL starting with
`https://` .

ConnectedAppSamlConfig

Specifies how an app uses single sign-on.


Metadata Types ConnectedApp

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

`samlSigningAlgoType` SamlSigningAlgoType Indicates the signing algorithm applied to SAML requests and responses
(enumeration of type string) when Salesforce is the identity provider. The selected signing algorithm

is applied to both single sign-on and single logout responses from your
org. Available in API version 50.0 and later. Valid values are:

**•** `SHA1`

**•** `SHA256`


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

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
a user approval step. For flows without a user approval step, API
logins with the High Assurance session security level are blocked.

`sessionLevel` string

Applies the High Assurance session security level to the connected
app. This session level requires users to verify their identity with
multi-factor authentication when they log in to the connected app.


Metadata Types ConnectedApp

**Field Name** **Field Type** **Description**

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

      <contactEmail>example@salesforce.com</contactEmail>

      <contactPhone>1231231234</contactPhone>

      <description>Test App</description>

   <iconUrl>https://c1.sfdcstatic.com/content/dam/sfdc-docs/www/logos/salesforce-logo-cloud.png</iconUrl>

```


Metadata Types ConnectedApp

```
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

     <consumerSecret>3MVG9AOp4k...</consumerSecret>

     <certificate>3MVG9AOp4kbriZOInmoLmTrguy9ryzcLbBjoNY...</certificate>

        <scopes>Basic</scopes>

        <scopes>Chatter</scopes>

        <scopes>OpenID</scopes>

        <scopes>CustomPermissions</scopes>

     <singleLogoutUrl>https://www.logout.com</singleLogoutUrl>

```


Metadata Types ConnectedApp

```
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

    <label>MyConnectedApp</label>

    <oauthConfig>

    <callbackUrl>https://example.com/callback1

   https://example.com/callback2

   https://example.com/callback3</callbackUrl>

    <consumerKey>3MVG9AOp4kbriZOcnmoLmTrguy9ryzcLbBjoNY...</consumerKey>

    <isAdminApproved>false</isAdminApproved>

```


### Metadata Types ContentAsset

```
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

### ContentAsset

Represents the metadata for creating an asset file. Asset files enable a Salesforce file to be used for org setup and configuration purposes.
This type extends the MetadataWithContent metadata type and inherits its `content` and `fullName` fields.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.


Metadata Types ContentAsset

File Suffix and Directory Location

ContentAsset components have the suffix `.asset` and are stored in the `contentassets` folder.

Version

ContentAsset components are available in API version 38.0 and later.

Special Access Rules

The system prevents metadata retrieval if the total size of the asset’s file content exceeds 30 MB. All pre-existing limits for packaging
apply to asset files.

Fields

**Field Name** **Field Type** **Description**

```
format

```

ContentAssetFormat Describes the format of the asset file. Valid values are:
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

`relationships` ContentAssetRelationships The list of ContentAssetLinks that describe whether the asset file can be
shared with the org.

`versions` ContentAssetVersions Required. Captures basic information about the file version included the
asset metadata. Typically the file has only one version.

ContentAssetRelationships

Represents the relationships between an asset file and the locations it's linked with.

**Field Name** **Field Type** **Description**

`emailTemplate` ContentAsset[] An array of email templates the content asset is related to. This field is available
in API version 51.0 and later.


Metadata Types ContentAsset

**Field Name** **Field Type** **Description**

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

ContentAssetVersion

Represents information about one file version included in the asset metadata.

**Field Name** **Field Type** **Description**

`number` string Required. The version number. This field is based on, or sets, the ContentVersion.


Metadata Types ContentAsset

**Field Name** **Field Type** **Description**

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

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types ContentTypeBundle ContentTypeBundle

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

Fields

**Name** **Description**

```
description

```

**Type**
string

**Description**
Explanatory text about the content type.


Metadata Types ContentTypeBundle

**Name** **Description**

```
masterLabel

resources

```

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

The content of the resource.


Metadata Types ContentTypeBundle

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

       "lightning:type": "lightning__richTextType",

       "minLength": 10,

       "maxLength": 3000,

       "lightning:textIndexed": false,

       "lightning:uiOptions": {

        "placeholderText": "Write something about yourself"

```


Metadata Types ContentTypeBundle

```
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

       "lightning:type": "lightning__booleanType",

       "lightning:uiOptions": {

        "placeholderText": "Check if host identity is verified"

       }

      },

      "hostingExperienceInYears": {

```


Metadata Types ContentTypeBundle

```
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
[for CMS Delivery Contents](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_cms_delivery_contents.htm) [and CMS Delivery Content.](https://developer.salesforce.com/docs/atlas.en-us.260.0.chatterapi.meta/chatterapi/connect_resources_cms_delivery_content.htm)

Wildcard Support in the Manifest

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving with the Zip .


### Metadata Types ContextDefinition ContextDefinition

Represents the details of a context definition that describe the relationship between the node structures within a context.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

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

contextDefinitionReferences

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

**Field Type**
### ContextDefinitionReference[]

**Description**
References of the context definition.


Metadata Types ContextDefinition

**Field Name** **Description**

```
contextDefinitionVersions

contextTtl

description

hasSystemTags

inheritedFrom

inheritedFromVersion

isProtected

```

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

**Field Type**
boolean

**Description**
Auto-generated value that doesn’t impact the behavior of the metadata type.


Metadata Types ContextDefinition

**Field Name** **Description**

```
masterLabel

title

```

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

**Field Name** **Description**

```
contextMappings

```

**Field Type**

ContextMapping[]


Metadata Types ContextDefinition

**Field Name** **Description**

**Description**
Mapping of attributes and nodes to related objects.

```
contextNodes

endDate

isActive

startDate

versionNumber

```

ContextMapping

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

**Description**
Purpose associated to a context mapping.


Metadata Types ContextDefinition

**Field Name** **Description**

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

Specifies the purpose that's used to identify the type of context mapping required.

Valid values are:


Metadata Types ContextDefinition

**Field Name** **Description**

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

**Description**
Name of the object used for the mapping.


Metadata Types ContextDefinition

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

**Field Name** **Description**

```
contextAttrHydrationDetails

```

**Field Type**

ContextAttrHydrationDetail[]


Metadata Types ContextDefinition

**Field Name** **Description**

**Description**
Details of the query that fetches the data for the specific query attribute.

```
inheritedFrom

objectName

queryAttribute

```

CtxAttrHydrationCtx

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
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### ConversationMessageDefinition

Represents a messaging component in an Enhanced Messaging channel or Messaging for In-App and Web session.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

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

description

```

**Field Type**

ConversationMessageConstant[]

**Description**
An array of constants that defines the messaging components. Constants support
multiple data types, including text, URL, and image.

**Field Type**
string


Metadata Types ConversationMessageDefinition

**Field Name** **Description**

**Description**
The description of the conversation message definition.

```
label

language

messageHandlers

messageLayouts

optionsParameter

parameters

type

```

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


Metadata Types ConversationMessageDefinition

**Field Name** **Description**

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

label

name

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

**•** `Options`

**•** `SubTitle`

**•** `Title`

**•** `Url`

**Field Type**
string

**Description**
The UI label of the conversation message constant.

**Field Type**
string


Metadata Types ConversationMessageDefinition

**Field Name** **Description**

**Description**
The name of the conversation message constant.

```
primitiveValues

valueType

```

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


Metadata Types ConversationMessageDefinition

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

**•** `ImageAsset`

**•** `Text`

**•** `Url`

**Field Type**
string

**Description**
Represents the value for type = Url

ConversationMessageHandler

Represents the conversation message handler.

**Field Name** **Description**

```
activeRequestDurationMinutes

handlerName

```

**Field Type**
int

**Description**
Required. The duration of an active request in minutes.

**Field Type**
string


Metadata Types ConversationMessageDefinition

**Field Name** **Description**

**Description**
Required. The name of the message handler.

```
handlerType

```

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

**•** `Carousel`

**•** `EncryptedOAuthToken`

**•** `ExternalTemplate`

**•** `Flow`

**•** `Inputs`

**•** `ListPicker`

**•** `Media`

**•** `Payment`

**•** `QuickReplies`


Metadata Types ConversationMessageDefinition

**Field Name** **Description**

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

accountName

language

```

**Field Type**
string

**Description**
Required. The account identifier. For WhatsApp channels, this is the WABA ID.

**Field Type**
string

**Description**
Required. The account name.

**Field Type**
string

**Description**
Required. The language of the conversation message external template.


Metadata Types ConversationMessageDefinition

**Field Name** **Description**

```
status

templateName

templateVersionIdentifier

```

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

ConversationMessageLayoutItem

Represents the conversation message layout item.

**Field Name** **Description**

```
collectionType

```

**Field Type**
ConversationMessageCollectionType (enumeration of type string)


Metadata Types ConversationMessageDefinition

**Field Name** **Description**

**Description**

Required. The type of conversation message collection. Valid values are:

**•** `DynamicList`

**•** `None`

**•** `StaticList`

```
compositeValues

name

primitiveValues

```

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

valueSourceReference

```

**Field Type**
string

**Description**
Required. The name of the conversation message layout composite value type.

**Field Type**

ConversationMessageLayoutItem[]

**Description**
An array of layout items.

**Field Type**
string

**Description**
The source of the conversation message layout composite value.


Metadata Types ConversationMessageDefinition

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

**•** `FormulaTemplate`

**•** `Literal`

**•** `MediaAsset`

**•** `SourcePrimitiveValue`

**•** `SourceSobjectField`

**•** `SourceSobjectFieldValue`

**•** `SourceSobjectFormula`


Metadata Types ConversationMessageDefinition

**Field Name** **Description**

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

**Description**
Required. The source of the conversation message merge field value.

ConversationMessageOptionsParameter

Represents a conversation message options parameter.


Metadata Types ConversationMessageDefinition

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

isRequired

```

**Field Type**
ConversationMessageParameterCompositeDetails[]

**Description**
The composite child items of the conversation message parameter.

**Field Type**
boolean

**Description**
Indicates whether the conversation message parameter composite details field is a
list item ( `true` ) or not ( `false` ). The default value is false.

**Field Type**
boolean

**Description**
Indicates whether the conversation message parameter is required ( `true` ) or not
( `false` ). The default value is false.


Metadata Types ConversationMessageDefinition

**Field Name** **Description**

```
label

maxListItems

name

primitiveChildItems

```

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

isRequired

label

```

**Field Type**
boolean

**Description**
Indicates whether the conversation message parameter primitive details field is a list
item ( `true` ) or not ( `false` ). The default value is false.

**Field Type**
boolean

**Description**
Indicates whether the conversation message parameter primitive details field is required
( `true` ) or not ( `false` ). The default value is false.

**Field Type**
string


Metadata Types ConversationMessageDefinition

**Field Name** **Description**

**Description**
The UI label of the conversation message parameter primitive details field.

```
maxListItems

name

sobjectType

valueType

```

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

ConversationMessageParameter

Represents a conversation message parameter.

**Field Name** **Description**

```
compositeTypeDetails

```

**Field Type**

ConversationMessageParameterCompositeDetails


Metadata Types ConversationMessageDefinition

**Field Name** **Description**

**Description**
An array of composite type details.

```
parameterType

primitiveTypeDetails

```

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

     <valueType>Text</valueType>

   </constants>

   <constants>

     <constantType>Custom</constantType>

     <label>Prompt1</label>

     <name>Prompt1</name>

```


Metadata Types ConversationMessageDefinition

```
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

             <primitiveValues>

               <textValue>Dec</textValue>

               <type>Text</type>

             </primitiveValues>

           </constantItems>

           <identifier>fb8bb328-7bc7-2830-6194-2ae7ece055ad</identifier>

```


Metadata Types ConversationMessageDefinition

```
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

                    <name>title</name>

                    <primitiveValues>

                       <type>SourcePrimitiveValue</type>

   <valueSourceReference>Constants.Options.ListItem.SubTitle</valueSourceReference>

                    </primitiveValues>

```


Metadata Types ConversationMessageDefinition

```
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

             <layoutItems>

               <collectionType>None</collectionType>

               <compositeValues>

                  <compositeTypeName>TitleImageItem</compositeTypeName>

                  <layoutItems>

                    <collectionType>None</collectionType>

```


Metadata Types ConversationMessageDefinition

```
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

           <collectionType>None</collectionType>

           <name>title</name>

           <primitiveValues>

             <type>SourcePrimitiveValue</type>

             <valueSourceReference>Constants.Title</valueSourceReference>

           </primitiveValues>

```


Metadata Types ConversationMessageDefinition

```
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

                       <type>SourcePrimitiveValue</type>

   <valueSourceReference>Constants.Options.ListItem.SubTitle</valueSourceReference>

                    </primitiveValues>

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

      <version>61.0</version>

   </Package>

```


### Metadata Types ConversationMessageDefinitionTranslation

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### ConversationMessageDefinitionTranslation

Represents translated labels and constant values for conversation message definitions in Enhanced Messaging and Messaging for In-App
and Web.

Note: This complex type is used as a nested element within the ConversationMessageDefinition metadata type and is not deployed
as a standalone metadata component. It enables multilingual support by allowing constant values and labels to be translated into
different languages for customer-facing messaging.

Parent Type

This type is used as a nested complex type within the ConversationMessageDefinition on page 656 metadata type.

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
the Single Sign-On connected app for the contact center. If set to `false`, an IdP other
than Salesforce is used or an IdP isn’t used at all. The default value is `false` .

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

For custom Visualforce pages, content is restricted to trusted
URLs only if the page’s `cspHeader` attribute is set to `true` .

This field is available in API version 44.0 and later.

`description` string The description of this trusted URL.


Metadata Types CspTrustedSite

**Field** **Field Type** **Description**

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


Metadata Types CspTrustedSite

**Field** **Field Type** **Description**

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

Usage

For each CSPTrustedSite component, at least one field starting with `grantAccess` or `isApplicableTo` must be set to `true.`

In API versions 50.0 to 58.0, if all `isApplicable` fields are `false`, the `isApplicableToImgSrc` field is set to `true` . In API
version 49.0 and earlier, if all `isApplicable` fields are `false`, those fields all default to `true` .

To ensure smooth integration across Salesforce products, Salesforce includes URLs in each of the CSP directives that correspond to the
`isApplicable` fields, even though those URLs aren’t defined as CspTrustedSite components. Salesforce regularly updates those
URLs based on the latest requirements.


### Metadata Types CustomApplication

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

`actionOverrides` AppActionOverride[]

`brand` AppBrand

`consoleConfig` ServiceCloudConsoleConfig

Represents an action override for an application. Use it
to create, update, edit, or delete action overrides.

This field is available for Lightning Experience in API
version 38.0 and later.

The color scheme and logo used for the app.

This field is available for Lightning Experience in API
version 38.0 and later.

Represents configuration settings for a Salesforce console
app.

This field is available in API version 42.0 and later.

`defaultLandingTab` string The `fullName` of a standard tab or custom tab that
opens when this application is selected.

`description` string The optional description text of the application.


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

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

`logo` string The optional reference to the image document for a
Salesforce app or Salesforce console app.

`navType` NavType (enumeration of type string) Not updateable. Indicates the type of navigation the app
uses. The value `Standard` is for a Lightning app with


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

standard navigation. The value `Console` is for a
Lightning app with console navigation.

This field is available in API version 38.0 and later.

`preferences` AppPreferences

Represents the preferences for a Salesforce Classic
console app. All of the AppPreferences fields are required.

This field is available in API version 42.0 and later.

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
example). In API version 13.0 and later, built-in tabs are
prefixed with `standard-` . For example, to reference
the Account tab you would use `standard-Account` .


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

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

`workspaceConfig` AppWorkspaceConfig Represents how records open in a Salesforce console
app. Required if `isServiceCloudConsole` is

`true` . In API version 42.0, this field was renamed to
`workspaceConfig` from `workspaceMappings` .

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

The `Large` value represents the Lightning Experience desktop
environment and is valid only for the `flexipage` and
`lightningcomponent` types. The `Small` value represents the
Salesforce mobile app on a phone or tablet. The `Medium` value is


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

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

**Field Name** **Field Type** **Description**

`footerColor` string Optional. Determines the footer color in the app. Specify the color with
a hexadecimal code, such as #0000FF for blue.


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

`headerColor` string Optional. Determines the header color in the app. Specify the color with
a hexadecimal code, such as #0000FF for blue.

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
`isServiceCloudConsole` is `true` .

`enableListViewHover` boolean Indicates if a Salesforce Classic console app has list view hovers enabled.
If set to `true`, summary information is displayed about a record in a


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

responsive list when the user hovers over a record name. For cases, hover
over the subject field.

`enableListViewReskin` boolean Indicates if Salesforce Classic console apps use responsive list views
instead of Salesforce Classic lists views.

`enableMultiMonitorComponents` boolean Indicates if a Salesforce Classic console app has multi-monitor
components enabled, which lets users move portions of a console from

their browsers to locations on their screens. This field is required if
`isServiceCloudConsole` is `true` .

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
again. Required if `isServiceCloudConsole` is `true` .

AppProfileActionOverride

Represents a ProfileActionOverride for a custom app. This type inherits from ProfileActionOverride on page 1734 and extends it by one
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

The record type associated with the override.If `pageOrSobjectType`
is `standard-home`, this field must be `null` . This field is required
when `actionName` is set to `View` .

```
type

```

ActionOverrideType Required. Read-only. The type of action override. The only valid value is
(enumeration of type `flexipage` .
string)

AppWorkspaceConfig

Represents how records open in a Salesforce console app. Required if `isServiceCloudConsole` is `true` . Available for Salesforce
Classic console apps in API version 25.0 and later. Available for Lightning console apps in API version 41.0 and later. In API version 42.0,
this type was renamed from WorkspaceMappings to AppWorkspaceConfig.

**Field Name** **Field Type** **Description**

`mappings` WorkspaceMappingSingle[] Represents how records for a specific tab open in a Salesforce console
app. Required for each tab specified in the CustomApplication. In API

version 42.0, this field was renamed from `workspaceMapping` to
`mappings` .

WorkspaceMapping

Represents how records for a specific tab open in a Salesforce console app. Required for each tab specified in the CustomApplication.
Available in API version 25.0 and later for Salesforce Classic console apps. Available in API version 41.0 and later for Lightning console
apps.

**Field Name** **Field Type** **Description**

`fieldName` string The name of the field that specifies the primary tab in which to display
`tab` as a subtab. If not specified, `tab` opens as a primary tab.

`tab` string Required. Name of the tab.


Metadata Types CustomApplication

CustomShortcut

Represents custom keyboard shortcuts assigned to a Salesforce console app in Salesforce Classic. Before you can create custom shortcuts,
a developer must define the shortcut’s action with the `addEventListener()` method in the Salesforce Console Integration Toolkit.
You can’t create keyboard shortcuts for actions performed outside of the console. Available in API version 28.0 and later.

**Field Name** **Field Type** **Description**

`action` string Required. The action performed in the console when a user presses the
keyboard shortcut.

`active` boolean Required. Indicates whether the keyboard shortcut is active ( `true` ) or
not ( `false` ).

`keyCommand` string Required. The combination of keys a user presses to trigger the keyboard
shortcut. Keyboard shortcuts aren’t case-sensitive, but they display as

uppercase on setup pages in the Salesforce user interface so that they’re
easier to read.

Each key command can include up to four modifier keys followed by one
non-modifier key. Modifier and non-modifier keys are separated by the
`+` key. Modifier keys can occur in any order, but you must place
non-modifier keys at the end of the key command sequence. For example,
`SHIFT+CTRL+ALT+META +A` .

Valid modifier keys are:

**•** `SHIFT`

**•** `CTRL`

**•** `ALT`

**•** `META` (represents the COMMAND key on Macs)

Valid non-modifier keys are letters A through Z and numbers 0 through
9. Other valid keys are:

**•** `TAB`

**•** `ENTER`

**•** `PAUSE/BREAK`

**•** `CAPS LOCK`

**•** `ESC`

**•** `SPACE`

**•** `PAGE UP`

**•** `PAGE DOWN`

**•** `END`

**•** `HOME`

**•** `LEFT ARROW`

**•** `UP ARROW`

**•** `RIGHT ARROW`

**•** `DOWN ARROW`


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

**•** `PRINT SCREEN`

**•** `INSERT`

**•** `DELETE`

**•** `RIGHT WINDOW`

**•** `NUMPAD 0`

**•** `NUMPAD 1`

**•** `NUMPAD 2`

**•** `NUMPAD 3`

**•** `NUMPAD 4`

**•** `NUMPAD 5`

**•** `NUMPAD 6`

**•** `NUMPAD 7`

**•** `NUMPAD 8`

**•** `NUMPAD 9`

**•** `MULTIPLY`

**•** `ADD`

**•** `SUBTRACT`

**•** `DECIMAL POINT`

**•** `DIVIDE`

**•** `F1`

**•** `F2`

**•** `F3`

**•** `F4`

**•** `F5`

**•** `F6`

**•** `F7`

**•** `F8`

**•** `F9`

**•** `F10`

**•** `F11`

**•** `F12`

**•** `NUM LOCK`

**•** `SCROLL LOCK`

**•** `;`

**•** `=`

**•** `,`

**•** `—`

**•** `.`


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

**•** `/`

**•** `‘`

**•** `[`

**•** `]`

**•** `\`

**•** `'`

`description` string The optional description text for the keyboard shortcut.

`eventName` string Required. Code available to developers who want to add custom shortcut
functions to the console via the Salesforce Console Integration Toolkit.

DefaultShortcut

Represents default keyboard shortcuts assigned to a Salesforce console app. After you enable keyboard shortcuts for a console, several
default shortcuts are available for customization. These include opening and closing tabs, moving between tabs, and saving records.
Available in API version 28.0 and later.

**Field Name** **Field Type** **Description**

`action` string Required. The action performed in the console when a user presses the
keyboard shortcut. Valid values are:

**•** `FOCUS_CONSOLE`

**•** `FOCUS_NAVIGATOR_TAB`

**•** `FOCUS_DETAIL_VIEW`

**•** `FOCUS_PRIMARY_TAB_PANEL`

**•** `FOCUS_SUBTAB_PANEL`

**•** `FOCUS_LIST_VIEW`

**•** `FOCUS_FIRST_LIST_VIEW`

**•** `FOCUS_SEARCH_INPUT`

**•** `MOVE_LEFT`

**•** `MOVE_RIGHT`

**•** `UP_ARROW`

**•** `DOWN_ARROW`

**•** `OPEN_TAB_SCROLLER_MENU`

**•** `OPEN_TAB`

**•** `CLOSE_TAB`

**•** `ENTER`

**•** `EDIT`

**•** `SAVE`


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

`active` boolean Required. Indicates whether the keyboard shortcut is active ( `true` ) or
not ( `false` ).

`keyCommand` string Required. The combination of keys a user presses to trigger the keyboard
shortcut. Keyboard shortcuts aren’t case-sensitive, but they display as

uppercase on setup pages in the Salesforce user interface so that they’re
easier to read.

Each key command can include up to four modifier keys followed by one
non-modifier key. Modifier and non-modifier keys are separated by the
`+` key. Modifier keys can occur in any order, but you must place
non-modifier keys at the end of the key command sequence. For example,
`SHIFT+CTRL+ALT+META +A` .

Valid modifier keys are:

Valid non-modifier keys are letters A through Z and numbers 0 through
9. Other valid keys are:

KeyboardShortcuts

Represents keyboard shortcuts assigned to a Salesforce console app. Required if `isServiceCloudConsole` is `true` . Available
in API version 28.0 and later.

**Field Name** **Field Type** **Description**

`customShortcuts` CustomShortcut[] Represents custom keyboard shortcuts assigned to a Salesforce console
app in Salesforce Classic. Before you can create custom shortcuts, a

developer must define the shortcut’s action with the
`addEventListener()` method in the Salesforce Console
Integration Toolkit. You can’t create keyboard shortcuts for actions
performed outside of the console.

In API version 42.0, this field was renamed from `customShortcut`
to `customShortcuts` .

`defaultShortcuts` DefaultShortcut[] Represents default keyboard shortcuts assigned to a Salesforce console
app. After you enable keyboard shortcuts for a console, several default

shortcuts are available for customization. These include opening and
closing tabs, moving between tabs, and saving records.

In API version 42.0, this field was renamed from `defaultShortcut`
to `defaultShortcuts` .

ListPlacement

Represents how lists display in a Salesforce console app. Required if `isServiceCloudConsole` is `true` . Available in API version
25.0 and later.


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

`height` int Height of the list in pixels or percentage. Required if `location` is top.

`location` string Required. Location of the list on the screen. Valid values are:

**•** full

**•** top

**•** left

`units` string Required. Represents if `height` or `width` is in pixels or percentage.

`width` int Width of the list in pixels or percentage. Required if `location` is left.

LiveAgentConfig

Represents your organization's settings for using Chat in the Salesforce Console.

**Field Name** **Field Type** **Description**

`enableLiveChat` boolean Specifies whether Chat is enabled in your organization ( `true` ) or not
( `false` ).

`openNewAccountSubtab` boolean

Specifies whether to open a new Account subtab in a Salesforce console
app automatically ( `true` ) or not ( `false` ) when an agent accepts a
chat.

`openNewCaseSubtab` boolean Specifies whether to open a new Case subtab in a Salesforce console app
automatically ( `true` ) or not ( `false` ) when an agent accepts a chat.

`openNewContactSubtab` boolean

`openNewLeadSubtab` boolean

`openNewVFPageSubtab` boolean

`pageNamesToOpen` string [array of strings]

Specifies whether to open a new Contact subtab in a Salesforce console
app automatically ( `true` ) or not ( `false` ) when an agent accepts a
chat.

Specifies whether to open a new Lead subtab in a Salesforce console
app automatically ( `true` ) or not ( `false` ) when an agent accepts a
chat.

Specifies whether to open a new Visualforce page as a subtab in a
Salesforce console app automatically ( `true` ) or not ( `false` ) when an
agent accepts a chat.

Specifies the Visualforce pages to open in subtabs when an agent accepts
a chat in a Salesforce console app.

This field is available in API version 42.0 and later.

`showKnowledgeArticles` boolean Specifies whether to display the Knowledge component while using
Chat in a Salesforce console app ( `true` ) or not ( `false` ).


Metadata Types CustomApplication

PushNotification

Represents a set of push notifications, which are visual indicators on lists and detail pages that show when a record or field has changed
during a user’s session. Available for use if `isServiceCloudConsole` is `true` . Available in API version 28.0 and later.

**Field Name** **Field Type** **Description**

`fieldNames` string] The name of the field or fields that trigger push notifications for the
selected object.

`objectName` string Required. Name of the object that triggers push notifications.

ServiceCloudConsoleConfig

Represents configuration settings for a Salesforce console app. Available in API version 42.0 and later.

**Field Name** **Field Type** **Description**

`componentList` AppComponentList Represents custom console components (Visualforce pages) assigned to
a Salesforce console app.

`detailPageRefreshMethod` string Determines how detail pages refresh in a Salesforce console app. Required
if `isServiceCloudConsole` is `true` . The valid values are:

**•** `none`

**•** `autoRefresh`

**•** `flag`

`footerColor` string Determines the footer color in a Salesforce console app.Specify the color
with a hexadecimal code, such as #0000FF for blue.

`headerColor` string Determines the header color in a Salesforce console app. Specify the
color with a hexadecimal code, such as #0000FF for blue.

`keyboardShortcuts` KeyboardShortcuts

Represents the keyboard shortcuts for a Salesforce console app. Keyboard
shortcuts let users perform actions by pressing a combination of keys
instead of having to use a mouse.

`listPlacement` ListPlacement Represents how lists display in a Salesforce console app. Required if
`isServiceCloudConsole` is `true` .

`listRefreshMethod` string Determines how lists refresh in a Salesforce console app. Required if
`isServiceCloudConsole` is `true` . The valid values are:

**•** `none`

**•** `refreshList`

**•** `refreshListRows`

`liveAgentConfig` LiveAgentConfig Represents the configurations for using Chat in the Salesforce Console.

`primaryTabColor` string Determines the primary tab color in a Salesforce console app.Specify the
color with a hexadecimal code, such as #0000FF for blue.


Metadata Types CustomApplication

**Field Name** **Field Type** **Description**

`pushNotifications` PushNotification[] Represents push notifications for a Salesforce console app. Push
notifications are visual indicators on lists and detail pages that show when

a record or field has changed during a user’s session. For example, assume
that two support agents are working on the same case. If one agent
changes the `Priority`, a push notification displays to the other agent
so the agent notices the change and doesn’t duplicate the effort.

`tabLimitConfig` TabLimitConfig

Represents the maximum number of primary tabs and subtabs allowed
in one Salesforce console session. Required if `enableTabLimits` is
`true` .

`whiteListedDomains` string[] Any external domains that users can access from within a Salesforce
console app. For example, `www.yourdomain.com` .

TabLimitConfig

Represents the maximum number of primary tabs and subtabs allowed in one Salesforce console session. Required if
`enableTabLimits` is `true` . Available in API version 36.0 and later.

**Field Name** **Field Type** **Description**

`maxNumberOfPrimaryTabs` string The maximum number of primary tabs allowed in one console session.
Valid values are:

**•** 5

**•** 10

**•** 20

**•** 30

`maxNumberOfSubTabs` string The maximum number of subtabs allowed in one console session. Valid
values are:

**•** 5

**•** 10

**•** 15

Usage

You can't delete custom app ProfileActionOverrides by deploying with `destructiveChange.xml` . To delete a ProfileActionOverride,
retrieve the app. In the app definition file, find the `<profileActionOverrides>` section, and remove the `<content>` row.
Then, change the `<type>` value in that same section to `default` instead of `flexipage` . Do this for every override you want to
reset. After making the changes, rezip the folder and deploy.

You can remove one override at a time each with its own deploy, or you can remove multiple overrides in a single deploy. However, we
recommend that you do a fresh retrieve every time you want to delete a new override. Don’t use a previously retrieved file.


Metadata Types CustomApplication

Retrieving Apps

To retrieve apps in your organization, use the CustomApplication type name in the `package.xml` manifest file. You can either retrieve
all apps or specify which apps to retrieve in the types section of `package.xml` .

To retrieve all apps in your organization—custom and standard apps, specify the wildcard character ( `*` ), as follows.

```
   <types>

      <members>*</members>

      <name>CustomApplication</name>

   </types>

```

Note: In API version 29.0 and earlier, use of the wildcard returns only all custom applications but not standard applications.

To retrieve a custom app, specify the app name.

```
   <types>

      <members>MyCustomApp</members>

      <name>CustomApplication</name>

   </types>

```

To retrieve a standard app, add the `standard__` prefix to the app name. For example, to retrieve the Chatter standard app, specify
`standard__Chatter` .

```
   <types>

      <members>standard__Chatter</members>

      <name>CustomApplication</name>

   </types>

```

To retrieve an app that is part of an installed package, add the package namespace prefix followed by two underscores and the app
name. For example, if the package namespace is `myInstalledPackageNS` and the app name is `PackageApp`, specify
`myInstalledPackageNS__PackageApp`, as follows.

```
   <types>

      <members>myInstalledPackageNS__PackageApp</members>

      <name>CustomApplication</name>

   </types>

```

Declarative Metadata Sample Definition

Here’s the definition of a custom Lightning Experience app:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomApplication xmlns="http://soap.sforce.com/2006/04/metadata">

      <actionOverrides>

        <actionName>View</actionName>

        <comment>Action override created by Lightning App Builder during

   activation.</comment>

        <content>Custom_Mobile_Oppty_Page</content>

        <formFactor>Small</formFactor>

        <skipRecordTypeSelect>false</skipRecordTypeSelect>

        <type>Flexipage</type>

        <pageOrSobjectType>Opportunity</pageOrSobjectType>

      </actionOverrides>

      <actionOverrides>

```


Metadata Types CustomApplication

```
        <actionName>View</actionName>

        <comment>Action override created by Lightning App Builder during

   activation.</comment>

        <content>Custom_Mobile_Oppty_Page</content>

        <formFactor>Large</formFactor>

        <skipRecordTypeSelect>false</skipRecordTypeSelect>

        <type>Flexipage</type>

        <pageOrSobjectType>Opportunity</pageOrSobjectType>

      </actionOverrides>

      <brand>

        <headerColor>#EE1518</headerColor>

        <shouldOverrideOrgTheme>true</shouldOverrideOrgTheme>

      </brand>

      <description>Manage inventory and deliveries for our warehouses.</description>

      <formFactors>Small</formFactors>

      <formFactors>Large</formFactors>

      <isNavAutoTempTabsDisabled>false</isNavAutoTempTabsDisabled>

      <isNavPersonalizationDisabled>false</isNavPersonalizationDisabled>

      <label>Warehouse Lightning</label>

      <navType>Standard</navType>

      <profileActionOverrides>

        <actionName>View</actionName>

        <content>Warehouse_test_page</content>

        <formFactor>Large</formFactor>

        <pageOrSobjectType>Warehouse__c</pageOrSobjectType>

        <type>Flexipage</type>

        <profile>Admin</profile>

      </profileActionOverrides>

      <profileActionOverrides>

        <actionName>View</actionName>

        <content>Warehouse_test_page</content>

        <formFactor>Small</formFactor>

        <pageOrSobjectType>Warehouse__c</pageOrSobjectType>

        <type>Flexipage</type>

        <profile>Admin</profile>

      </profileActionOverrides>

      <setupExperience>all</setupExperience>

      <tabs>standard-Feed</tabs>

      <tabs>standard-File</tabs>

      <tabs>standard-Account</tabs>

      <tabs>standard-Case</tabs>

      <tabs>Merchandise__c</tabs>

      <tabs>Invoice__c</tabs>

      <tabs>Warehouse__c</tabs>

      <tabs>Delivery__c</tabs>

      <tabs>standard-report</tabs>

      <tabs>standard-Dashboard</tabs>

      <uiType>Lightning</uiType>

   </CustomApplication>

```

The following is a definition of a standard app (Chatter):

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomApplication xmlns="http://soap.sforce.com/2006/04/metadata">

      <defaultLandingTab>standard-home</defaultLandingTab>

```


Metadata Types CustomApplication

```
      <label>Collaboration</label>

      <tabs>standard-Chatter</tabs>

      <tabs>standard-UserProfile</tabs>

      <tabs>standard-OtherUserProfile</tabs>

      <tabs>standard-CollaborationGroup</tabs>

      <tabs>standard-File</tabs>

   </CustomApplication>

```

Declarative Metadata Sample Definition—Salesforce Console

The following is the definition of a custom app where `isServiceCloudConsole` is `true` :

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomApplication xmlns="http://soap.sforce.com/2006/04/metadata">

      <consoleConfig>

        <componentList>

           <alignment>left</alignment>

           <components>MyComponent</components>

        </componentList>

        <detailPageRefreshMethod>autoRefresh</detailPageRefreshMethod>

        <keyboardShortcuts>

           <customShortcuts>

             <action>MyCustomShortcutAction</action>

             <active>true</active>

             <keyCommand>X</keyCommand>

             <description>Custom Shortcut example</description>

             <eventName>myCustomShortcutExample</eventName>

           </customShortcuts>

           <defaultShortcuts>

             <action>FOCUS_CONSOLE</action>

             <active>true</active>

             <keyCommand>ESC</keyCommand>

           </defaultShortcuts>

           <defaultShortcuts>

             <action>FOCUS_NAVIGATOR_TAB</action>

             <active>true</active>

             <keyCommand>V</keyCommand>

           </defaultShortcuts>

           <defaultShortcuts>

             <action>FOCUS_DETAIL_VIEW</action>

             <active>true</active>

             <keyCommand>SHIFT+S</keyCommand>

           </defaultShortcuts>

           <defaultShortcuts>

             <action>FOCUS_PRIMARY_TAB_PANEL</action>

             <active>true</active>

             <keyCommand>P</keyCommand>

           </defaultShortcuts>

           <defaultShortcuts>

             <action>FOCUS_SUBTAB_PANEL</action>

             <active>true</active>

             <keyCommand>S</keyCommand>

           </defaultShortcuts>

           <defaultShortcuts>

```


Metadata Types CustomApplication

```
             <action>FOCUS_LIST_VIEW</action>

             <active>true</active>

             <keyCommand>N</keyCommand>

           </defaultShortcuts>

           <defaultShortcuts>

             <action>FOCUS_FIRST_LIST_VIEW</action>

             <active>true</active>

             <keyCommand>SHIFT+F</keyCommand>

           </defaultShortcuts>

           <defaultShortcuts>

             <action>FOCUS_SEARCH_INPUT</action>

             <active>true</active>

             <keyCommand>R</keyCommand>

           </defaultShortcuts>

           <defaultShortcuts>

             <action>MOVE_LEFT</action>

             <active>true</active>

             <keyCommand>LEFT ARROW</keyCommand>

           </defaultShortcuts>

           <defaultShortcuts>

             <action>MOVE_RIGHT</action>

             <active>true</active>

             <keyCommand>RIGHT ARROW</keyCommand>

           </defaultShortcuts>

           <defaultShortcuts>

             <action>UP_ARROW</action>

             <active>true</active>

             <keyCommand>UP ARROW</keyCommand>

           </defaultShortcuts>

           <defaultShortcuts>

             <action>DOWN_ARROW</action>

             <active>true</active>

             <keyCommand>DOWN ARROW</keyCommand>

           </defaultShortcuts>

           <defaultShortcuts>

             <action>OPEN_TAB_SCROLLER_MENU</action>

             <active>true</active>

             <keyCommand>D</keyCommand>

           </defaultShortcuts>

           <defaultShortcuts>

             <action>OPEN_TAB</action>

             <active>true</active>

             <keyCommand>T</keyCommand>

           </defaultShortcuts>

           <defaultShortcuts>

             <action>CLOSE_TAB</action>

             <active>true</active>

             <keyCommand>C</keyCommand>

           </defaultShortcuts>

           <defaultShortcuts>

             <action>ENTER</action>

             <active>true</active>

             <keyCommand>ENTER</keyCommand>

           </defaultShortcuts>

```


Metadata Types CustomApplication

```
           <defaultShortcuts>

             <action>EDIT</action>

             <active>true</active>

             <keyCommand>E</keyCommand>

           </defaultShortcuts>

           <defaultShortcuts>

             <action>SAVE</action>

             <active>true</active>

             <keyCommand>CTRL+S</keyCommand>

           </defaultShortcuts>

        </keyboardShortcuts>

        <listPlacement>

           <location>left</location>

           <units>percent</units>

           <width>20</width>

        </listPlacement>

        <listRefreshMethod>refreshList</listRefreshMethod>

        <pushNotifications>

           <fieldNames>CreatedBy</fieldNames>

           <objectName>Campaign</objectName>

        </pushNotifications>

        <pushNotifications>

           <fieldNames>CustomField1__c</fieldNames>

           <objectName>CustomObject1__c</objectName>

        </pushNotifications>

      </consoleConfig>

      <defaultLandingTab>standard-home</defaultLandingTab>

      <isServiceCloudConsole>true</isServiceCloudConsole>

      <label>MyConsole</label>

      <preferences>

        <enableCustomizeMyTabs>false</enableCustomizeMyTabs>

        <enableKeyboardShortcuts>true</enableKeyboardShortcuts>

        <enableListViewHover>true</enableListViewHover>

        <enableListViewReskin>true</enableListViewReskin>

        <enableMultiMonitorComponents>true</enableMultiMonitorComponents>

        <enablePinTabs>true</enablePinTabs>

        <enableTabHover>false</enableTabHover>

        <enableTabLimits>false</enableTabLimits>

        <saveUserSessions>false</saveUserSessions>

      </preferences>

      <tabs>standard-Case</tabs>

      <tabs>standard-Account</tabs>

      <tabs>standard-Contact</tabs>

      <tabs>standard-Contract</tabs>

      <workspaceConfig>

        <mappings>

           <tab>standard-Case</tab>

        </mappings>

        <mappings>

           <fieldName>ParentId</fieldName>

           <tab>standard-Account</tab>

        </mappings>

        <mappings>

           <fieldName>AccountId</fieldName>

```


### Metadata Types CustomApplicationComponent

```
           <tab>standard-Contact</tab>

        </mappings>

        <mappings>

           <tab>standard-Contract</tab>

        </mappings>

      </workspaceConfig>

   </CustomApplication>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

CustomTab

### CustomApplicationComponent

Represents a custom console component (Visualforce page) assigned to a CustomApplication that is marked as a Salesforce console.
Custom console components extend the capabilities of Salesforce console apps. See Customize a Console with Custom Components
in Salesforce Classic in Salesforce Help.

File Suffix and Directory Location

Custom application components have the suffix `.customApplicationComponent` and are stored in the
`customApplicationComponents` folder.

Version

Custom applications are available in API version 25.0 and later.

Fields

**Field Name** **Field Type** **Description**

`buttonIconUrl` string The address of a page that hosts an icon for the button.

`buttonStyle` string The inline style used to define how the button looks.

`buttonText` string The label on the button used to launch the custom console component.

`buttonWidth` int The pixel width of the button displayed in the Salesforce console.

`height` int The pixel height of the window used to display the custom console
component.

`isHeightFixed` boolean Required. Indicates whether users can change the custom console
component height ( `false` ) or not ( `true` ).


### Metadata Types CustomFeedFilter

**Field Name** **Field Type** **Description**

`isHidden` boolean Required. Indicates whether the custom console component is hidden
from users ( `true` ) or not ( `false` ).

`isWidthFixed` boolean Required. Indicates whether users can change the component width
( `false` ) or not ( `true` ).

`visualforcePage` string Required. Name of the Visualforce page that represents the custom
console component.

`width` int The pixel width of the window used to display the custom console
component.

Declarative Metadata Sample Definition

The following is the definition of a custom application component:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomApplicationComponent xmlns="http://soap.sforce.com/2006/04/metadata">

      <buttonIconUrl>https://salesforce.com</buttonIconUrl>

      <buttonStyle>buttonStyleCSS</buttonStyle>

      <buttonText>buttonText</buttonText>

      <buttonWidth>200</buttonWidth>

      <height>200</height>

      <isHeightFixed>false</isHeightFixed>

      <isHidden>false</isHidden>

      <isWidthFixed>false</isWidthFixed>

      <visualforcePage>MyVisualforcePage</visualforcePage>

      <width>50</width>

   </CustomApplicationComponent>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### CustomFeedFilter

Represents a custom feed filter that limits the feed view to feeds from the Cases object. The custom feed filter shows only feed items
that satisfy the criteria specified in the CustomFeedFilter definition. This type extends the Metadata metadata type and inherits its
`fullName` field.

File Suffix and Directory Location

### CustomFeedFilter components have the suffix .feedFilter and are stored in the feedFilters folder.


Metadata Types CustomFeedFilter

Version

CustomFeedFilter components are available in API version 35.0 and later.

Fields

**Field Name** **Field Type** **Description**

`criteria` FeedFilterCriterion The criterion that defines which feed items are shown when the filter is
on page 720 [] applied. The feed filter displays all feed items that satisfy the criteria.

`description` string The description of the custom feed filter. For example, specify what feed
items that filter shows.

`label` string Required. The API label of the custom feed filter.

`isProtected` boolean An auto-generated value. It currently has no impact.

FeedFilterCriterion

Represents the conditions that a feed item must satisfy to be displayed when a feed filter is applied.

**Field Name** **Field Type** **Description**

`feedItemType` FeedItemType (enumeration of type
Required. The type of feed items that the filter shows.
string)

The feed item type can be one of the following values:

**•** AttachArticleEvent

**•** CallLogPost

**•** CanvasPost

**•** CaseCommentPost

**•** ChangeStatusPost

**•** ChatTranscriptPost

**•** ContentPost

**•** CreateRecordEvent

**•** EmailMessageEvent

**•** LinkPost

**•** MilestoneEvent

**•** QuestionPost

**•** PollPost

**•** ReplyPost

**•** SocialPost

**•** TextPost


Metadata Types CustomFeedFilter

**Field Name** **Field Type** **Description**

`feedItemVisibility` FeedItemVisibility (enumeration of
type string)

`relatedSObjectType` string

Declarative Metadata Sample Definition

The following is an example of a CustomFeedFilter on page 719 component.

The visibility of feed items that the filter shows. For
example, you can show only poll posts that are visible
internally.

Valid values are:

**•** AllUsers

**•** InternalUsers

The API name of the object that the feed item refers to.
This field is typically used with the CreateRecordEvent
feed item type.

For example, a feed filter can show CreateRecordEvent
feed items for the Cases object.

```
<?xml version="1.0" encoding="UTF-8"?>

<CustomFeedFilter xmlns="http://soap.sforce.com/2006/04/metadata">

   <criteria>

     <feedItemType>CreateRecordEvent</feedItemType>

     <relatedSObjectType>MyCO01__c</relatedSObjectType>

   </criteria>

   <criteria>

     <feedItemType>CreateRecordEvent</feedItemType>

     <relatedSObjectType>Case</relatedSObjectType>

   </criteria>

   <criteria>

     <feedItemType>PollPost</feedItemType>

     <feedItemVisibility>InternalUsers</feedItemVisibility>

   </criteria>

   <label>Sample Custom Feed Filter</label>

</CustomFeedFilter>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>myCaseFeedFilter</members>

     <name>CustomFeedFilter</name>

   </types>

   <version>66.0</version>

</Package>

```


### Metadata Types CustomFieldDisplay

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### CustomFieldDisplay

Represents the view type assigned to product attribute custom fields. This type extends the Metadata metadata type and inherits its
`fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### CustomFieldDisplay components have the suffix .customFieldDisplay .

Version

### CustomFieldDisplay components are available in API version 63.0 and later.

Fields

**Field Name** **Field Type** **Description**

Required. The view type of the product attribute custom fields. Values
are:

**•** `ColorSwatch`

**•** `Dropdown`

**•** `Pill`

```
displayType

```

### CustomFieldDisplayType

(enumeration of
type string)

`fieldApiName` string Required. The unique name of the product attribute, for example, color_c.

`isProtected` boolean Optional. An auto-generated value that doesn’t impact the behavior of
the metadata type. The default value is `false` .

`masterLabel` string Required. The primary label for this object.

Declarative Metadata Sample Definition

The following is an example of a CustomFieldDisplay component.

```
<?xml version="1.0" encoding="UTF-8"?>

<CustomFieldDisplay xmlns="http://soap.sforce.com/2006/04/metadata">

 <masterLabel>cfd1</masterLabel>

 <fieldApiName>Color__c</fieldApiName>

```


### Metadata Types CustomHelpMenuSection

```
    <displayType>Pill</displayType>

    <isProtected>false</isProtected>

   </CustomFieldDisplay>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

    <types>

    <members>*</members>

    <name>CustomFieldDisplay</name>

    </types>

    <version>63.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### CustomHelpMenuSection

Represents the section of the Lightning Experience help menu that the admin added to display custom, org-specific help resources for
the org. The custom section contains help resources added by the admin. This type extends the Metadata metadata type and inherits
its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### CustomHelpMenuSection components have the suffix .customHelpMenuSection and are stored in the

`customHelpMenuSections` folder.

Version

### CustomHelpMenuSection components are available in API version 45.0 and later.

Fields

**Field Name** **Field Type** **Description**

`customHelpMenuItems` CustomHelpMenuItems[] Items included in the custom section. Specify up to 15 items.

`masterLabel` string

Required. Name of the custom section. Only one custom section
can be added to the Lightning Experience help menu. Specify up
to 80 characters.


### Metadata Types CustomIndex

CustomHelpMenuItems

Items included in the custom section. Specify up to 15 items.

**Field Name** **Field Type** **Description**

`linkURL` string Required. The URL for the resource.

`masterLabel` string Required. The name of the resource. Specify up to 100 characters.

`sortOrder` int Required. The order of the item within the custom section. Valid values are `1`
through `15` .

Declarative Metadata Sample Definition

The following is an example of a CustomHelpMenuSection component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomHelpMenuSection xmlns="http://soap.sforce.com/2006/04/metadata">

      <masterLabel>MyOrgCustomHelp</masterLabel>

      <customHelpMenuItems>

        <linkUrl>https://www.yourcompanyhelp.com/gettingstarted</linkUrl>

        <masterLabel>Getting Started</masterLabel>

        <sortOrder>1</sortOrder>

      </customHelpMenuItems>

      <customHelpMenuItems>

        <linkUrl>https://www.yourcompanyhelp.com/features</linkUrl>

        <masterLabel>Feature to Start Using Right Away</masterLabel>

        <sortOrder>2</sortOrder>

      </customHelpMenuItems>

      <customHelpMenuItems>

        <linkUrl>https://www.yourcompanyhelp.com/salestips</linkUrl>

        <masterLabel>Tips for Sales Team Members</masterLabel>

        <sortOrder>3</sortOrder>

      </customHelpMenuItems>

   </CustomHelpMenuSection>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>MyOrgCustomHelp</members>

        <name>CustomHelpMenuSection</name>

      </types>

      <version>45.0</version>

   </Package>

### CustomIndex

```

Represents an index used to increase the speed of queries.This type extends the Metadata metadata type and inherits its `fullName`
field.


### Metadata Types CustomLabels

File Suffix and Directory Location

CustomIndex components have the suffix .indx-meta and are stored in the `customindex` folder.

Version

CustomIndex is available in API versions 50.0 and later.

Special Access Rules

[To use this metadata and create a custom index, review Indexes in](https://developer.salesforce.com/docs/atlas.en-us.260.0.salesforce_large_data_volumes_bp.meta/salesforce_large_data_volumes_bp/ldv_deployments_infrastructure_indexes.htm) _Best Practices for Deployments with Large Data Volumes_, and then
contact Salesforce Customer Support.

Fields

**Field Name** **Field Type** **Description**

`allowNullValues` boolean Indicates whether null values are allowed in the index ( `true` ) or not
( `false` ). The default value is `false` .

`booleanIndexedValue` boolean Indicates whether boolean fields are indexed (true) or not (false).
Available in API version 61.0 and later.

Declarative Metadata Sample Definition

The following is an example of a CustomIndex component.

```
   <?xml version="1.0" encoding="UTF-8" ?>

   <CustomIndex xmlns="http://soap.sforce.com/2006/04/metadata">

      <allowNullValues>false</allowNullValues>

      <booleanIndexedValue>true</booleanIndexedValue>

   </CustomIndex>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### CustomLabels

The CustomLabels metadata type allows you to create custom labels that can be localized for use in different languages, countries, and
currencies.

This type extends the Metadata metadata type and inherits its `fullName` field. Custom labels are custom text values, up to 1,000
characters in length that can be accessed from Apex classes or Visualforce pages. For more information, see “Custom Labels” in Salesforce
Help.


Metadata Types CustomLabels

Declarative Metadata File Suffix and Directory Location

Master custom label values are stored in the `CustomLabels.labels` file. Translations for custom labels can be retrieved through
Translations in Metadata API. Translations are stored in files under the `translations` folder with the name format of
_`localeCode`_ `.translation`, where _`localeCode`_ is the locale code of the translation language. The supported locale codes
are listed in Language on page 2377.

Version

CustomLabels components are available in API version 14.0 and later.

Fields

**Field** **Field Type** **Description**

`fullName` string

Required. The name of the custom label bundle.

Inherited from Metadata, this field is defined in the WSDL for
this metadata type. It must be specified when creating, updating,

or deleting. See `createMetadata()` to see an example of
this field specified for a call.

`labels` CustomLabel[] A list of custom labels.

CustomLabel

This metadata type represents a custom label. This type extends the Metadata metadata type and inherits its `fullName` field.

**Field** **Field Type** **Description**

`categories` string

`fullName` string

A comma-separated list of categories for the label. This field can
be used in filter criteria when creating custom label list views.
Maximum of 255 characters.

Required. The name of the custom label.

Inherited from Metadata, this field is defined in the WSDL for
this metadata type. It must be specified when creating, updating,

or deleting. See `createMetadata()` to see an example of
this field specified for a call.

`language` string Required. The language of the translated custom label.

`protected` boolean

Required. Indicates whether this component is protected ( `true` )
or not ( `false` ). Protected components can’t be linked to or
referenced by components created in the installing organization.

`shortDescription` string Required. An easily recognizable term to identify this custom
label. This description is used in merge fields.


Metadata Types CustomLabels

**Field** **Field Type** **Description**

`value` string Required. The translated custom label. Maximum of 1000
characters.

Usage

Use CustomLabels with the wildcard character (*) for members in the `package.xml` manifest file to retrieve all custom labels that
are defined in your organization. CustomLabels doesn’t support retrieving one or more custom labels by name. To retrieve specific labels
by name, use CustomLabel and specify the label names as members.

Declarative Metadata Sample Definition

This is a sample XML definition of a custom label component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomLabels xmlns="http://soap.sforce.com/2006/04/metadata">

      <labels>

        <fullName>quoteManual</fullName>

        <value>This is a manual quote.</value>

        <language>en_US</language>

        <protected>false</protected>

        <shortDescription>Manual Quote</shortDescription>

      </labels>

      <labels>

        <fullName>quoteAuto</fullName>

        <value>This is an automatically generated quote.</value>

        <language>en_US</language>

        <protected>false</protected>

        <shortDescription>Automatic Quote</shortDescription>

      </labels>

   </CustomLabels>

```

This is a sample manifest file for retrieving all custom labels in the organization by using the CustomLabels type.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <fullName>MyPkg</fullName>

      <types>

       <members>*</members>

       <name>CustomLabels</name>

      </types>

      <version>66.0</version>

   </Package>

```

This is a sample manifest file for retrieving two custom labels by name. Notice it uses the CustomLabel singular type.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <fullName>MyPkg</fullName>

      <types>

       <members>quoteManual</members>

       <members>quoteAuto</members>

```


### Metadata Types Custom Metadata Types (CustomObject)

```
       <name>CustomLabel</name>

      </types>

      <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

CustomLabels Limitation

Before you use the CustomLabels metadata type, understand the limitations of this feature. You can’t retrieve the CustomLabels metadata
type with a namespace.

SEE ALSO:

Translations

### Custom Metadata Types (CustomObject)

Represents the metadata associated with a custom metadata type.

[For more information, see Custom Metadata Types.](https://help.salesforce.com/s/articleView?id=platform.custommetadatatypes_overview.htm&language=en_US)

File Suffix and Directory Location

A custom metadata type is defined as a custom object and is stored in the objects folder. Custom metadata types have a suffix of `__mdt`
(instead of `__c` for custom objects). Custom metadata type field names have a suffix of `__c`, like other custom fields. Custom metadata
type field names must be dot-qualified with the name of the custom metadata type to which they belong.

Names of custom metadata types must be unique within their namespace. All custom metadata types belong to the `CustomMetadata`
namespace and can optionally belong to a second namespace. In your organization, you can use custom metadata types with your
namespace and also other organizations’ namespaces.

Version

Custom metadata type components are available in API version 31.0 and later.

Special Access Rules

To create custom metadata types, you must have the “Author Apex” permission. Apex code can create, read, and update (but not delete)
custom metadata records, as long as the metadata is subscriber-controlled and visible from within the code's namespace. You can edit
records in memory but not upsert or delete them. Apex code can deploy custom metadata records, but not via a DML operation.
Moreover, DML operations aren’t allowed on custom metadata in the Partner or Enterprise APIs. Customers who install a managed
custom metadata type can’t add new custom fields to it. With unpackaged metadata, both developer-controlled and subscriber-controlled
[access behave the same: like subscriber-controlled access. Refer to Trust, but Verify: Apex Metadata API and Security to learn more.](https://developer.salesforce.com/blogs/engineering/2017/06/apex-metadata-api-security.html)


Metadata Types Custom Metadata Types (CustomObject)

Note: Audit fields ( `CreatedDate`, `CreatedBy`, `LastModifiedDate`, `LastModifiedBy`, `SystemModStamp` )
remain uneditable.

Fields

Custom metadata types can contain the following CustomObject fields.

To make the fields on your custom metadata types unique and indexable, mark your fields as `Unique` and `ExternalId` .


Metadata Types Custom Metadata Types (CustomObject)

Declarative Metadata Sample Definition

In this example, Picklists R Us creates its Reusable Picklist custom metadata type by deploying a file in the objects folder, named
`ReusablePicklistOption__mdt.object`, with these contents.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

     <fields>

       <fullName>AlphaSort__c</fullName>

       <defaultValue>false</defaultValue>

       <externalId>false</externalId>

       <label>Sorted Alphabetically</label>

       <type>Checkbox</type>

     </fields>

     <label>Reusable Picklist</label>

     <pluralLabel>Reusable Picklist</pluralLabel>

     <visibility>Public</visibility>

   </CustomObject>

```

This excerpt from a `package.xml` file shows the use of dot notation and the `__mdt` suffix. If you’re using a namespace, for example
`picklist1234`, the full name of `ReusablePicklistOption__mdt` would be `picklist1234`
`__ReusablePicklistOption__mdt` .

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

   ...

     <types>

       <members>PicklistTest__c.PicklistTestField__c</members>

       <members>ReusablePicklistOption__mdt.Picklist__c</members>

       <members>ReusablePicklistOption__mdt.SortOrder__c</members>

       <members>PicklistUsage__mdt.Field__c</members>

       <members>PicklistUsage__mdt.Picklist__c</members>

       <members>PicklistUsage__mdt.SObjectType__c</members>

       <members>ReusablePicklist__mdt.AlphaSort__c</members>

       <name>CustomField</name>

     </types>

   ...

     <types>

       <members>PicklistTest__c</members>

       <members>ReusablePicklistOption__mdt</members>

       <members>PicklistUsage__mdt</members>

       <members>ReusablePicklist__mdt</members>

       <name>CustomObject</name>

     </types>

   ...

     <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


#### Metadata Types CustomMetadata 1. CustomMetadata

Represents a record of a custom metadata type.

#### CustomMetadata

Represents a record of a custom metadata type.

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

#### CustomMetadata components have the suffix .md and are stored in the customMetadata folder. Unlike custom metadata types,

custom metadata records don’t have a double-underscore suffix. Custom metadata record names are prepended with their custom
metadata type name, excluding the `__mdt` suffix but including the namespace of any types in an installed managed package.

Version

#### CustomMetadata components are available in API version 31.0 and later.

Special Access Rules

To create custom metadata records, you must have the “Customize Application” permission.

Fields

**Field Name** **Field Type** **Description**

`description` string A description of the custom metadata record. This field
can contain a maximum of 1,000 characters.

`label` string A label that represents the object throughout the
Salesforce Setup user interface. Custom metadata records

are currently visible only through the packaging user
interface.

`protected` boolean

Boolean. Indicates whether the record is protected (true)
or not (false). When a custom metadata type is released
in a managed package, access is limited in specific ways.

**•** Code that’s in the same managed package as custom
metadata records can read the records.

**•** Code that’s in the same managed package as custom
metadata types can read the records that belong to
that type.

**•** Code that’s in a managed package that doesn’t
contain either the type or the protected record can’t
read the protected records.


Metadata Types CustomMetadata

**Field Name** **Field Type** **Description**

**•** Code that the subscriber creates and code that’s in
an unmanaged package can’t read the protected
records.

**•** The developer can modify protected records with a
package upgrade or by using the Metadata Apex
classes (if the Apex code is in the same namespace
as either the records or their type). The subscriber
can’t read or modify protected records. The developer
name of a protected record can’t be changed after
release.

**•** The subscriber can’t create records of a protected
type.

Records that are hidden by these access rules are also
unavailable to REST, SOAP, SOQL, and Setup.

`values` CustomMetadataValue[] Represents one or more values for custom fields on the
custom metadata record.

CustomMetadataValue

Represents a value for a custom field on the custom metadata record.

**Field Name** **Field Type** **Description**

`field` string Required. The non-object-qualified name of a custom
field in the custom metadata type. This value corresponds

to the name of a field on the custom metadata record’s
custom metadata type. Include the namespace (if the
type is from a managed package) and the `__c` suffix.
The name of the custom metadata type isn’t required.
For example, `picklist1234__AlphaSort__c` .

`value` Any type The value on a custom metadata record. Where fields are
EntityDefinition and FieldDefinition, the qualified API

names of the entity and the field it points to. This value
can be null.

Declarative Metadata Sample Definitions

The following is an example of a CustomMetadata component. In this example, the sample app TravelApp deploys a Planets picklist,
specifies its sort order, and adds picklist items to it.


Metadata Types CustomMetadata

Assuming Picklists R Us’s namespace is `picklist1234`, to define the `Planets` picklist, TravelApp deploys a file in the
`customMetadata` folder, named `picklist1234__ReusablePicklist.Planets.md`, with these contents. The
`xsi:type` attribute specifies the type for the value of the `AlphaSort__c` checkbox field.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomMetadata xmlns="http://soap.sforce.com/2006/04/metadata"

               xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

               xmlns:xsd="http://www.w3.org/2001/XMLSchema">

      <description>All the planets in the solar system. Does not

              include asteroids.</description>

      <label>Planets</label>

      <values>

        <field>picklist1234__AlphaSort__c</field>

        <value xsi:type="xsd:boolean">false</value>

      </values>

   </CustomMetadata>

```

Picklists R Us creates its Reusable Picklist Option custom metadata type by deploying a file in the objects folder, named
`ReusablePicklist__mdt.object`, with these contents.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

      <fields>

        <fullName>Picklist__c</fullName>

        <externalId>false</externalId>

        <label>Picklist</label>

        <length>40</length>

        <required>true</required>

        <type>Text</type>

        <unique>false</unique>

      </fields>

      <fields>

        <fullName>SortOrder__c</fullName>

        <externalId>false</externalId>

        <label>Non-Alphabetical Sort Order</label>

        <precision>3</precision>

        <scale>0</scale>

        <required>false</required>

        <type>Number</type>

        <unique>false</unique>

      </fields>

      <label>Reusable Picklist Option</label>

      <pluralLabel>Reusable Picklist Options</pluralLabel>

   </CustomObject>

```

To define the `Mars` picklist item, TravelApp deploys a file, named `picklist1234__ReusablePicklistOption.Mars.md`,
with these contents. This component file specifies types that apply to the `ReusablePicklistOption__mdt` custom fields.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomMetadata xmlns="http://soap.sforce.com/2006/04/metadata"

     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

     xmlns:xsd="http://www.w3.org/2001/XMLSchema">

      <label>Mars</label>

      <values>

        <field>picklist1234__Picklist__c</field>

```


Metadata Types CustomMetadata

```
        <value xsi:type="xsd:string">Planets</value>

      </values>

      <values>

        <field>picklist1234__SortOrder__c</field>

        <value xsi:type="xsd:int">4</value>

      </values>

   </CustomMetadata>

```

To define the `Motel6` picklist item, TravelApp deploys a file, named
`picklist1234__ReusablePicklistOption.Motel6.md`, with these contents.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomMetadata xmlns="http://soap.sforce.com/2006/04/metadata"

     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

     xmlns:xsd="http://www.w3.org/2001/XMLSchema">

      <label>Motel 6</label>

      <values>

        <field>picklist1234__Picklist__c</field>

        <value xsi:type="xsd:string">Hotels</value>

      </values>

   </CustomMetadata>

```

Because the `SortOrder__c` field isn’t required, this file doesn’t require a value for `SortOrder__c` . Alternatively, the file could
have explicitly specified a value with `xsi:nil` to ensure that `SortOrder__c` was cleared of any previous value.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomMetadata xmlns="http://soap.sforce.com/2006/04/metadata"

   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

   xmlns:xsd="http://www.w3.org/2001/XMLSchema">

      <label>Motel 6</label>

      <values>

        <field>picklist1234__Picklist__c</field>

        <value xsi:type="xsd:string">Hotels</value>

      </values>

      <values>

        <field>picklist1234__SortOrder__c</field>

        <value xsi:nil="true" />

      </values>

   </CustomMetadata>

```

This excerpt from a `package.xml` file illustrates the inclusion of custom metadata types and their namespaces in custom metadata
records’ names. Assume that Picklists R Us’s namespace is `picklist1234` .

```
   <?xml version="1.0" encoding="UTF-8"?>

   <package xmlns="http://soap.sforce.com/2006/04/metadata">

   …

     <types>

       <members>picklist1234__ReusablePicklist.Hotels</members>

       <members>picklist1234__ReusablePicklist.Planets</members>

       <members>picklist1234__ReusablePicklistOption.Bellagio</members>

       <members>picklist1234__ReusablePicklistOption.Motel6</members>

       <members>picklist1234__ReusablePicklistOption.Mercury</members>

       <members>picklist1234__ReusablePicklistOption.Venus</members>

       <members>picklist1234__ReusablePicklistOption.Earth</members>

       <members>picklist1234__PicklistUsage.BookedHotel</members>

```


Metadata Types CustomMetadata

```
       <members>

         picklist1234__PicklistUsage.DestinationPlanetPL

       </members>

       <members>picklist1234__PicklistUsage.PlanetVisitedPl</members>

       <name>CustomMetadata</name>

     </types>

   …

   </package>

```

TravelApp, Inc.’s `package.xml` file uses a wildcard to install custom metadata, as is shown in this excerpt from their `package.xml`
file. Unless you want to deploy or retrieve specific records, using a wildcard is easier than listing all of your custom metadata records in
your `package.xml` file.

```
   <types>

     <members>*</members>

     <name>CustomMetadata</name>

   </types>

```

If the custom metadata is from a managed package, the name after the dot in the `package.xml` file—between the two dots in the
file name—is qualified by the managed package’s namespace. For example, assuming TravelApp uses the namespace `travelApp1234`,
the first member element in the TravelApp `package.xml` file appears to Galactic Tours as:

```
   <members>picklist1234__ReusablePicklist.travelApp1234__Hotels</members>

```

Here’s another example. In this case, we have an instance of custom metadata record, whose EntityDefinition field points to a custom
object named `SalesAgreement__c` . The FieldDefinition field points to the custom field `CustomerReference__c` on
`SalesAgreement__c` . You can deploy new custom metadata records and retrieve existing ones with EntityDefinition and
FieldDefinition fields using qualified API names of custom and standard entities and their fields.

```
   <?xml version="1.0" encoding="UTF-8"?><values>

   <field>EntityDefintionField__c</field>

   <value xsi:type="xsd:string">v1__SalesAgreement__c</value>

   </values>

   <values>

   <field>FieldDefinitionField__c</field>

   <value xsi:type="xsd:string">v1__CustomerReference__c</value>

   </values>

```

Usage

When specifying the `value` field in the CustomMetadataValue subtype, specify an appropriately typed object that’s based on your
field type definition. In declarative metadata definitions for CustomMetadataValue, use the `xsi:type` attribute of the value element.
For example, to specify a boolean value: `<value` `xsi:type="xsd:boolean">true</value>` . Valid `xsi:type` attributes
are:

**Custom metadata value** **Custom field definition**

`xsi:type="xsd:boolean"` Checkbox

`xsi:type="xsd:date"` Date

`xsi:type="xsd:dateTime"` Date/Time

`xsi:type="xsd:picklist"` Picklist


### Metadata Types CustomNotificationType

**Custom metadata value** **Custom field definition**

`xsi:type="xsd:string"` Text

`xsi:type="xsd:string"` Phone

`xsi:type="xsd:string"` TextArea

`xsi:type="xsd:string"` URL

`xsi:type="xsd:string"` Email

`xsi:type="xsd:int"` Number/Percent, with scale equal to 0

`xsi:type="xsd:double"` Number/Percent, with scale not equal to 0

You can also omit the `xsi:type` attribute. For example, `<value>true</value>` .

Although this attribute must be specified for any CustomMetadataValue, you can use an element with the `xsi:nil` attribute set to
`true` to explicitly set the field’s value to `null` . For example, `<value` `xsi:nil="true"/>` .

Using `null` field values differs from leaving out the CustomMetadataValue for a particular field entirely. If you leave out the
CustomMetadataValue, the value of the field doesn’t change. The field’s value is `null` for newly deployed custom metadata records
and left at its previous value for updated custom metadata records.

When you retrieve CustomMetadataValue objects, the `value` field of the returned object holds a value of the correct type, specified
by `xsi:type` in the case of declarative metadata definitions.

Custom number fields are stored as double values. When you retrieve a value from a Number type field with a scale 0, you will see a
decimal number. For example, if the value in UI is 1234567, a query through the API returns 1234567.0.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### CustomNotificationType

Represents the metadata associated with a custom notification type.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

For more information about custom notifications, see Custom Notification Actions. This type extends the Metadata metadata type and
inherits its `fullName` field.

Declarative Metadata File Suffix and Directory Location

The file suffix is `.notiftype` for the notification type definition. Notification types are stored in the `notificationtypes`
directory of the corresponding package directory.


Metadata Types CustomNotificationType

Version

CustomNotificationType components are available in API version 46.0 and later.

Fields

**Field Name** **Field Type** **Description**

`actionGroups` CustomNotificationActionGroup[]

```
(Beta)

```

Optional. Indicates whether mobile action groups are enabled, allowing
users to take actions directly from mobile notifications.

`actionGroups` is a pilot or beta service that is subject to the Beta
[Services Terms at Agreements - Salesforce.com or a written Unified Pilot](https://www.salesforce.com/company/legal/agreements/)

[Agreement if executed by Customer, and applicable terms in the Product](https://ptd.salesforce.com/)
[Terms Directory. Use of this pilot or beta service is at the Customer's sole](https://ptd.salesforce.com/)
discretion.

`customNotifTypeName` string Required. Specifies a notification type name. Maximum number of
characters: 80.

`description` string Specifies a general description of the notification type, which is displayed
with the notification type name. Maximum number of characters: 255.

`desktop` boolean Required. Indicates whether the desktop delivery channel is enabled
( `true` ) or not ( `false` ).

`masterLabel` string Required. Specifies the label for the notification type.

`mobile` boolean Required. Indicates whether the mobile delivery channel is enabled
( `true` ) or not ( `false` ).

`slack` boolean Reserved for future use.

CustomNotificationActionGroup (Beta)

CustomNotificationActionGroup represents the action group.

`CustomNotificationActionGroup` [is a pilot or beta service that is subject to the Beta Services Terms at Agreements -](https://www.salesforce.com/company/legal/agreements/)
[Salesforce.com or a written Unified Pilot Agreement if executed by Customer, and applicable terms in the Product Terms Directory. Use](https://www.salesforce.com/company/legal/agreements/)
of this pilot or beta service is at the Customer's sole discretion.

**Field Name** **Description**

```
actions

groupName

```

**Field Type**

CustomNotificationActionDefinition[]

**Description**
Represents the actions within a mobile action group.

**Field Type**
string


Metadata Types CustomNotificationType

**Field Name** **Description**

**Description**

Required.

Unique name of the mobile action group.

CustomNotificationActionDefinition

CustomNotificationActionDefinition represents the metadata that define an actionable notification.

`CustomNotificationActionDefinition` [is a pilot or beta service that is subject to the Beta Services Terms at Agreements](https://www.salesforce.com/company/legal/agreements/)

[- Salesforce.com or a written Unified Pilot Agreement if executed by Customer, and applicable terms in the Product Terms Directory.](https://www.salesforce.com/company/legal/agreements/)
Use of this pilot or beta service is at the Customer's sole discretion.

**Field Name** **Description**

```
actionLabel

actionName

actionTarget

actionType

```

**Field Type**
string

**Description**

Required.

The name of the action seen in the push notification.

**Field Type**
string

**Description**

Required.

Unique identifier of the action in an action group.

**Field Type**
string

**Description**
The name of the Apex class where the action is implemented.

**Field Type**
NotificationActionType (enumeration of type string)

**Description**

Type of action.

Required.

Values are:

**•** `NotificationApiAction` : Server-side action where client needs to make
action API call.


### Metadata Types CustomObject

**Field Name** **Description**

**•** `Share` : Client-side action where the app shares notification content to any
channel.

Declarative Metadata Sample Definition

The following is a definition of a custom notification type that is enabled for desktop and mobile.

```
   <CustomNotificationType xmlns="http://soap.sforce.com/2006/04/metadata">

      <customNotifTypeName>Custom Notification</customNotifTypeName>

      <desktop>true</desktop>

      <masterLabel>Custom Notification</masterLabel>

      <mobile>true</mobile>

   </CustomNotificationType>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

### CustomObject

Represents a custom object that stores data unique to your org or an external object that maps to data stored outside your org.

This type extends the Metadata metadata type and inherits its `fullName` field.

Specify all relevant fields when you create or update a custom object. You can’t update a single field on the object. For more information
[about custom objects, see Store Information That’s Unique to Your Organization in Salesforce Help.](https://help.salesforce.com/s/articleView?id=platform.dev_object_def.htm&type=5&language=en_US)

You can also use this metadata type to work with customizations of standard objects, such as accounts. For an example, see the section
[on Standard Objects in Sample package.xml Manifest Files in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/manifest_samples.htm) _Metadata API Developer Guide_

All metadata components have a `fullName` field, which must be fully specified for any custom object.

For example, the following are fully specified names for a standard object and a custom object respectively:

```
   Account

   MyCustomObject__c

```

And the following is a fully specified name for an external object:

```
   MyExternalObject__x

```

For sample Java code that creates a custom object, see Step 3: Walk Through the Java Sample Code on page 16.

Declarative Metadata File Suffix and Directory Location

Custom object names are automatically appended with __c. The file suffix is `.object` for the custom object or standard object file.

External object names are automatically appended with __x. The file suffix is `.object` for the external object file.

Custom, standard, and external objects are stored in the `objects` folder in the corresponding package directory.


Metadata Types CustomObject

Note: Retrieving a component of this metadata type in a project makes the component appear in any Profile and PermissionSet
components that are retrieved in the same package.

Version

Custom objects are available in API version 10.0 and later. External objects are available in API version 32.0 and later.

Fields

Unless otherwise noted, all fields are creatable, filterable, and nillable.

**Field Name** **Field Type** **Description**

`actionOverrides` ActionOverride[]

`allowInChatterGroups` boolean

`businessProcesses` BusinessProcess[]

`compactLayoutAssignment` string

`compactLayouts` CompactLayout[]

`customHelp` string

`customHelpPage` string

`customSettingsType` CustomSettingsType
(enumeration of type string)


A list of action overrides on the object.

This field is available in API version 18.0 and later.

Indicates whether records of this custom object type can be
added to Chatter groups.

This field is available in API version 34.0 and later.

A list of business processes associated with the object.

This field is available in API version 17.0 and later.

The compact layout assigned to the object.

This field is available in API version 29.0 and later. This field is
available for external objects in API version 42.0 and later.

A list of compact layouts associated with the object.

This field is available in API version 29.0 and later. This field is
available for external objects in API version 42.0 and later.

The s-control that contains the help content if the object has
customized help content. This field is available in API version
14.0 and later.

The Visualforce page that contains the help content if the
object has customized help content. This field is available in
API version 16.0 and later.

When this field is present, this component isn’t a custom
object, but a custom setting. This field returns the type of
custom setting. The following string values are valid:

**•** `List` —static data stored in cache, accessed as part of
your application, and available org-wide.

**•** `Hierarchy` —static data stored in cache, accessed as
part of your application, and available based on a hierarchy
of user, profile, or org. This value is the default.

Metadata Types CustomObject

**Field Name** **Field Type** **Description**

This field is available in API version 17.0 and later.

`customSettingsVisibility` CustomSettingsVisibility
(enumeration of type string)

When this field is present, this component isn’t a custom
object, but a custom setting. This field returns the visibility of
the custom setting. The following string values are valid:

**•** `Public` —if the custom setting is packaged, it’s
accessible to all subscribing orgs.

**•** `Protected` —if the custom setting is in a managed
package, it’s accessible only to the developer org.
Subscribing orgs can’t access it. This value is the default.

This field is available in API versions 17.0 through 33.0. In
versions 34.0 and later, use the `visibility` field instead
of this field.

`dataStewardGroup` string Removed in API version 47.0.

`dataStewardUser` string Removed in API version 47.0.

`deploymentStatus` DeploymentStatus Indicates the deployment status of the object.
(enumeration of type string)

`deprecated` boolean Reserved for future use.

`description` string A description of the object. Maximum of 1000 characters.

`enableActivities` boolean

`enableBulkApi` boolean

`enableDivisions` boolean

Indicates whether the object is enabled for activities ( `true` )
or not ( `false` ).

Not available for external objects.

When enabled, the object is classified as an Enterprise
Application object for usage tracking.

When enabled, `enableSharing` and
`enableStreamingApi` must also be enabled.

This field is available in API version 31.0 and later.

Indicates whether the object is enabled for divisions ( `true` )
or not ( `false` [). See Division in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_division.htm) _Salesforce Object Reference_ .
.

`enableEnhancedLookup` boolean Indicates whether the object is enabled for enhanced lookups
( `true` ) or not ( `false` ). The custom object must be

searchable for `enableEnhancedLookup` to work. Set
`enableSearch` as `true` before setting
`enableEnhancedLookup` as `true` . In API version 28.0
and later, this field can also be used for the Account, Contact,
and User objects. Enhanced lookups provide an updated
lookup dialog interface that lets users filter, sort, and page
through search results and customize search result columns.


Metadata Types CustomObject

**Field Name** **Field Type** **Description**

For more information about enhanced lookups, see “Enable
Enhanced Lookups” in Salesforce Help.

`enableFeeds` boolean

Indicates whether the object is enabled for feed tracking
( `true` ) or not ( `false` ). For more information, see “Customize
Chatter Feed Tracking” in Salesforce Help.

This field is available in API version 18.0 and later.

`enableHistory` boolean Indicates whether the object is enabled for history tracking
( `true` ) or not ( `false` ). Also available for standard objects

in API version 29.0 and later. History tracking on the Account
object includes person account history tracking.

`enableLicensing` boolean

`enableReports` boolean

`enableSearch` boolean

`enableSharing` boolean

Indicates whether this object is licensed by Salesforce and
users require a permission set license for it ( `true` ) or not
( `false` ). This field is available in API version 45.0 and later.

Indicates whether the object is enabled for reports ( `true` )
or not ( `false` ). Support for external objects is available in
API version 38.0 and later.

Indicates whether the object’s records can be found via SOSL
and Salesforce searches. Corresponds to `Allow Search`
in the user interface.

By default, search is disabled for new custom objects. This
field is available for custom objects in API version 35.0 and
later.

To enhance Einstein Search performance, searchability is
disabled for custom objects that haven't been searched for
more than 120 days. To enable object and field searchability,
contact your admin.

By default, search is disabled for new external objects.
However, you can validate and sync an external data source
to automatically create external objects. Syncing always
enables search on the external object when search is enabled
on the external data source, and vice versa.This field is
available for external objects in API version 37.0 and later.

When enabled, the object is classified as an Enterprise
Application object for usage tracking.

When enabled, `enableBulkApi` and
`enableStreamingApi` must also be enabled.

This field is available in API version 31.0 and later.


Metadata Types CustomObject

**Field Name** **Field Type** **Description**

`enableStreamingApi` boolean

When enabled, the object is classified as an Enterprise
Application object for usage tracking.

When enabled, `enableBulkApi` and `enableSharing`
must also be enabled.

This field is available in API version 31.0 and later.

`eventType` PlatformEventType This field applies only to platform events. Indicates the event
(enumeration of type string) type. The values are:

**•** `HighVolume` —For a high-volume platform event.

**•** `StandardVolume` —Deprecated. Creating a platform
event with this event type is supported and returns an
error.

This field is available in API version 41.0 and later.

`externalDataSource` string Required and available for external objects only. The name of
the external data source that stores the data for the external

object. The data source is represented by the
ExternalDataSource component.

This field is available in API version 32.0 and later.

`externalName` string

`externalRepository` string

`externalSharingModel` SharingModel (enumeration
of type string)

Required and available for external objects only. The name of
the table in the external data source that contains the data
for the external object.

This field is available in API version 32.0 and later.

Available for Salesforce Connect external objects only.
Corresponds to `Display URL Reference Field`
in the user interface.

The external object’s `Display URL` standard field values
are automatically generated from the external system. For

example, with the OData 2.0 adapter for Salesforce Connect,
the value is based on the `link href` that’s defined on the
OData producer. You can override the default values with the
values of a custom field on the same external object. Select
the field name, and make sure that the custom field’s values
are valid URLs.

This field is available in API version 32.0 and later.

Indicates the external org-wide defaults for the object, which
determines the access level for external users.

This field is available in API version 31.0 and later.

`fields` CustomField[] Represents one or more fields in the object.


Metadata Types CustomObject

**Field Name** **Field Type** **Description**

`fieldSets` FieldSet Defines the field set that exists on this object.

`fullName` string Inherited from Metadata, this field is defined in the WSDL for
this metadata type. It must be specified when creating,

updating, or deleting. See `createMetadata()` to see an
example of this field specified for a call.

This value can't be `null` .

`gender` Gender

Indicates the gender of the noun that represents the object.
This is used for languages where words need different
treatment depending on their gender.

`household` boolean This field supports relationship groups, a feature available only
with Salesforce for Wealth Management. For more

information, see “Salesforce for Wealth Management” in
Salesforce Help.

`historyRetentionPolicy` HistoryRetentionPolicy Reserved for future use.

`indexes` Index[] Defines the index for a custom big object.

`label` string

Label that represents the object throughout the Salesforce
user interface.

We recommend that you make object labels unique across
all standard, custom, and external objects in the org.

`listViews` ListView[] Represents one or more _list views_ associated with the object.

`namedFilter` NamedFilter[] Represents the metadata associated with a lookup filter. This
metadata type is used to create, update, or delete lookup filter

definitions. This component has been removed as of API
version 30.0 and is only available in previous API versions. The
metadata associated with a lookup filter is now represented
by the lookupFilter field in the CustomField component.

This field is available in API version 17.0 and later.

This field has been removed as of API version 30.0 and is only
available in prior versions. The metadata associated with a
lookup filter is now represented by the lookupFilter field in
the CustomField component.

`nameField` CustomField

Required for custom objects. On external objects, the name
field can instead be specified by setting `isNameField` to
`true` in the CustomField component.

The field that this object's name is stored in. Every custom
object must have a name, usually a string or autonumber.

Identifier for the custom object record. This name appears in
page layouts, related lists, lookup dialogs, search results, and


Metadata Types CustomObject

**Field Name** **Field Type** **Description**

key lists on tab home pages. By default, this field is added to
the custom object page layout as a required field.

`pluralLabel` string

Plural version of the label value.

Custom objects require a plural version of the label to ensure
that object names are localizable.

`profileSearchLayouts` ProfileSearchLayouts Represents a user profile’s search results layouts for an object.
With profile-specific layouts, each user profile can have a

different search results layout for an object. Available in API
version 47.0 and later.

`publishBehavior` PlatformEventPublishBehavior This field applies only to platform events. Indicates when
(enumeration of type string) platform event messages are published in a Lightning Platform

transaction. This field applies to event messages published
through the Lightning Platform, such as Apex, Process Builder,
and Flow Builder, but not through Salesforce APIs. Valid values
are:

**•** `PublishAfterCommit` —The event message is
published only after a transaction commits successfully.
If the transaction fails, the event message isn't published.

**•** `PublishImmediately` —The event message is
published when the publish call executes, regardless of
whether the transaction succeeds.

If you don’t specify this field, the default value used is
`PublishImmediately` .

This field is available in API version 46.0 and later.

`recordTypes` RecordType[] An array of one or more record types defined for this object.

`recordTypeTrackFeedHistory` boolean Indicates whether the record type is enabled for feed tracking
( `true` ) or not ( `false` ). To set this field to `true`, the

`enableFeeds` field on the associated CustomObject must
also be `true` . For more information, see “Customize Chatter
Feed Tracking” in Salesforce Help.

This field is available in API version 19.0 and later.

`recordTypeTrackHistory` boolean Indicates whether history tracking is enabled for this record
type ( `true` ) or not ( `false` ). To set

`recordTypeTrackHistory` to true, the
`enableHistory` field on the associated custom object
must also be `true` .

This field is available in API version 19.0 and later.

`searchLayouts` SearchLayouts The _Search Layouts_ related list information for the object.


Metadata Types CustomObject

**Field Name** **Field Type** **Description**

`sharingModel` SharingModel(enumeration Indicates the org-wide defaults for the object.
of type string)

Note: Using API version 29.0 and earlier, this field is
read-only and can’t be set using the Metadata API; you
must use the Salesforce user interface. Using API
version 30.0 and later, you can set this field for internal
users using the API and the Salesforce user interface.

`sharingReasons` SharingReason[] The reasons why the object is being shared.

`sharingRecalculations` SharingRecalculation[] A list of custom sharing recalculations associated with the
object.

`startsWith` StartsWith (enumeration of Indicates whether the noun starts with a vowel, consonant,
type string) or is a special character. This is used for languages where

words need different treatment depending on the first
character. Valid values are listed in StartsWith.

`validationRules` ValidationRule[] An array of one or more validation rules on the object.

`visibility` SetupObjectVisibility
(enumeration of type string)

This field returns the visibility of the custom object, custom
setting, or custom metadata type. The following values are
valid.

**•** `Public` —If the custom object, custom setting, or
custom metadata type is packaged, it’s accessible to all
subscribing orgs.

**•** `Protected` —If the custom object, custom setting, or
custom metadata type is in a managed package, it’s
accessible only to the developer org. Subscribing orgs
can’t access it.

**•** `PackageProtected` - (Custom metadata type only)
If the custom metadata type is `PackageProtected`,
it’s only accessible by the custom Apex code in the
package. Use this value to secure secrets such as API
access keys and security tokens. Available in API version
47.0 and later.

The default value is `Public` .

This field is available in API version 34.0 and later. For custom
settings, this field replaces the
`customSettingsVisibility` field.

`webLinks` WebLink[] An array of one or more weblinks defined for the object.

MktDataModelAttributes

This type is a Data 360 subtype of CustomObject.


Metadata Types CustomObject

**Field Name** **Field Type** **Description**

`creationType` DefinitionCreationType
enumeration

Indicates how this object is added.

Valid values availble in API version 62.0 and later are:

**•** `Activation_Audience`

**•** `Ad_Audience_Insights`

**•** `ADG`

**•** `Calculated_Insight`

**•** `CG_Audience`

**•** `Chunk`

**•** `Directory_Table`

**•** `External`

**•** `Problem_Records`

**•** `Segment_Membership`

**•** `Semantic`

**•** `Transform`

**•** `Vector_Embedding`

`dataModelTaxonomy` string When the model is a Standard Data 360 model, a Reference to the Data Model
from which this Object was started. Currently only supports the following

strings: if the creationType is Standard, it must be Reference, if creationType is
Custom, it must be View.

`description` string A description of the object. This field can contain a maximum of 521 characters.
This field is available in API version 55.0 and later.

`isEnabled` boolean True indicates that the Data Model Object is enabled.

`isSegmentable` boolean True indicates that the Data Model Object can be used as a target for
segmentation.

`isUsedForMetrics` boolean Indicates whether the Data Model Object is used for metrics ( `true` ) or not
( `false` ). This field is used to include additional attributes on the objects that

are not present in the Data Model Object POJO. This field is available in API
version 55.0 and later.

`objectCategory` string Reference to the Object Category. For modeling, the value is Profile,
Engagement, or Other.

`referenceEntityGroup` string When this is a Standard Object, the Entity Group of the Object from the
Reference Model.

`referenceEntityName` string When this is a Standard Object, the Name of the Object from the Reference
Model.

`referenceEntitySubjectArea` string When this is a Standard Object, the Subject Area of the Object from the
Reference Model.


Metadata Types CustomObject

MktDataLakeAttributes

Represents how Data 360 receives the data. MktDataLakeAttributes is a Data 360 subtype of CustomObject. Its components are available
in API version 50.0 and later.

Special Access Rules

You need an org with a Data Cloud license to access this object.

**Field Name** **Description**

```
creationType

isEnabled

```

**Field Type**
DefinitionCreationType enumeration of type string

**Description**
Indicates how this object is added.

Values are:

**•** `Activation_Audience`

**•** `Bridge`

**•** `Curated`

**•** `Custom`

**•** `Derived`

**•** `Ml_Prediction`

**•** `Segment_Membership`

**•** `Standard`

**•** `System`

Valid values availble in API version 62.0 and later are:

**•** `Activation_Audience`

**•** `Ad_Audience_Insights`

**•** `ADG`

**•** `Calculated_Insight`

**•** `CG_Audience`

**•** `Chunk`

**•** `Directory_Table`

**•** `External`

**•** `Problem_Records`

**•** `Segment_Membership`

**•** `Semantic`

**•** `Transform`

**•** `Vector_Embedding`

**Field Type**
boolean


Metadata Types CustomObject

**Field Name** **Description**

**Description**
Indicates whether the Landing Object is enabled.

```
objectCategory

```

**Field Type**
string

**Description**
Reference to the Object Category. For landing object, these would be Profile, Behavioral,
Other.

Declarative Metadata Additional Components

CustomObject definitions can include additional components defined in the custom object for declarative metadata. The following
components are defined in the CustomObject:

**•** ActionOverride

**•** BusinessProcess

**•** CompactLayout

**•** CustomField

**•** FieldSet

**•** HistoryRetentionPolicy

**•** ListView

**•** RecordType

**•** SearchLayouts

**•** SharingReason

**•** SharingRecalculation

**•** ValidationRule

**•** WebLink

Declarative Metadata Sample Definition

```
<?xml version="1.0" encoding="UTF-8"?>

<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

   <deploymentStatus>Deployed</deploymentStatus>

   <description>test object with one field for eclipse ide testing</description>

   <fields>

     <fullName>Comments__c</fullName>

     <description>add your comments about this object here</description>

    <inlineHelpText>This field contains comments made about this object</inlineHelpText>

     <label>Comments</label>

     <length>32000</length>

     <type>LongTextArea</type>

     <visibleLines>30</visibleLines>

   </fields>

```


Metadata Types CustomObject

```
      <label>MyFirstObject</label>

      <nameField>

        <label>MyFirstObject Name</label>

        <type>Text</type>

      </nameField>

      <pluralLabel>MyFirstObjects</pluralLabel>

      <sharingModel>ReadWrite</sharingModel>

   </CustomObject>

```

The following is the metadata definition of an external object for Salesforce Connect.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

      <actionOverrides>

        <actionName>CancelEdit</actionName>

        <type>Default</type>

      </actionOverrides>

      <actionOverrides>

        <actionName>Delete</actionName>

        <type>Default</type>

      </actionOverrides>

      <actionOverrides>

        <actionName>Edit</actionName>

        <type>Default</type>

      </actionOverrides>

      <actionOverrides>

        <actionName>Follow</actionName>

        <type>Default</type>

      </actionOverrides>

      <actionOverrides>

        <actionName>List</actionName>

        <type>Default</type>

      </actionOverrides>

      <actionOverrides>

        <actionName>New</actionName>

        <type>Default</type>

      </actionOverrides>

      <actionOverrides>

        <actionName>SaveEdit</actionName>

        <type>Default</type>

      </actionOverrides>

      <actionOverrides>

        <actionName>Tab</actionName>

        <type>Default</type>

      </actionOverrides>

      <actionOverrides>

        <actionName>View</actionName>

        <type>Default</type>

      </actionOverrides>

      <deploymentStatus>InDevelopment</deploymentStatus>

      <description>Products</description>

      <enableFeeds>false</enableFeeds>

      <externalDataSource>OData</externalDataSource>

      <externalIndexAvailable>false</externalIndexAvailable>

      <externalName>Products</externalName>

```


Metadata Types CustomObject

```
      <fields>

        <fullName>DiscontinuedDate__c</fullName>

        <description>DiscontinuedDate</description>

        <externalDeveloperName>DiscontinuedDate</externalDeveloperName>

        <externalId>false</externalId>

        <isFilteringDisabled>false</isFilteringDisabled>

        <isNameField>false</isNameField>

        <isSortingDisabled>false</isSortingDisabled>

        <label>DiscontinuedDate</label>

        <required>false</required>

        <type>DateTime</type>

      </fields>

      <fields>

        <fullName>ID__c</fullName>

        <description>ID</description>

        <externalDeveloperName>ID</externalDeveloperName>

        <externalId>false</externalId>

        <isFilteringDisabled>false</isFilteringDisabled>

        <isNameField>false</isNameField>

        <isSortingDisabled>false</isSortingDisabled>

        <label>ID</label>

        <precision>18</precision>

        <required>false</required>

        <scale>0</scale>

        <type>Number</type>

        <unique>false</unique>

      </fields>

      <fields>

        <fullName>Name__c</fullName>

        <description>Name</description>

        <externalDeveloperName>Name</externalDeveloperName>

        <externalId>false</externalId>

        <isFilteringDisabled>false</isFilteringDisabled>

        <isNameField>false</isNameField>

        <isSortingDisabled>false</isSortingDisabled>

        <label>Name</label>

        <length>128</length>

        <required>false</required>

        <type>Text</type>

        <unique>false</unique>

      </fields>

      <fields>

        <fullName>Price__c</fullName>

        <description>Price</description>

        <externalDeveloperName>Price</externalDeveloperName>

        <externalId>false</externalId>

        <isFilteringDisabled>false</isFilteringDisabled>

        <isNameField>false</isNameField>

        <isSortingDisabled>false</isSortingDisabled>

        <label>Price</label>

        <precision>16</precision>

        <required>false</required>

        <scale>2</scale>

        <type>Number</type>

```


Metadata Types CustomObject

```
        <unique>false</unique>

      </fields>

      <fields>

        <fullName>Products__c</fullName>

        <externalDeveloperName>Products</externalDeveloperName>

        <externalId>false</externalId>

        <isFilteringDisabled>false</isFilteringDisabled>

        <isNameField>false</isNameField>

        <isSortingDisabled>false</isSortingDisabled>

        <label>Products</label>

        <length>20</length>

        <referenceTo>Products__x</referenceTo>

        <relationshipLabel>Products</relationshipLabel>

        <relationshipName>Products</relationshipName>

        <type>ExternalLookup</type>

      </fields>

      <fields>

        <fullName>Rating__c</fullName>

        <description>Rating</description>

        <externalDeveloperName>Rating</externalDeveloperName>

        <externalId>false</externalId>

        <isFilteringDisabled>false</isFilteringDisabled>

        <isNameField>false</isNameField>

        <isSortingDisabled>false</isSortingDisabled>

        <label>Rating</label>

        <precision>18</precision>

        <required>false</required>

        <scale>0</scale>

        <type>Number</type>

        <unique>false</unique>

      </fields>

      <fields>

        <fullName>ReleaseDate__c</fullName>

        <description>ReleaseDate</description>

        <externalDeveloperName>ReleaseDate</externalDeveloperName>

        <externalId>false</externalId>

        <isFilteringDisabled>false</isFilteringDisabled>

        <isNameField>false</isNameField>

        <isSortingDisabled>false</isSortingDisabled>

        <label>ReleaseDate</label>

        <required>false</required>

        <type>DateTime</type>

      </fields>

      <label>Products</label>

      <pluralLabel>Products</pluralLabel>

      <searchLayouts>

        <customTabListAdditionalFields>ExternalId</customTabListAdditionalFields>

        <lookupDialogsAdditionalFields>ExternalId</lookupDialogsAdditionalFields>

       <lookupPhoneDialogsAdditionalFields>ExternalId</lookupPhoneDialogsAdditionalFields>

        <searchResultsAdditionalFields>ExternalId</searchResultsAdditionalFields>

        <searchResultsAdditionalFields>DisplayUrl</searchResultsAdditionalFields>

        <searchResultsAdditionalFields>ID__c</searchResultsAdditionalFields>

```


Metadata Types CustomObject

```
      </searchLayouts>

   </CustomObject>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file for Field Sets and Record Types
but not for other components. For information about using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

1. ActionOverride
Represents an action override on a standard or custom object. Use it to create, update, edit, or delete action overrides.You can access
ActionOverride only by accessing its encompassing CustomObject.

2. BusinessProcess
The BusinessProcess metadata type enables you to display different picklist values for users based on their profile.

3. CompactLayout
Represents the metadata associated with a compact layout. This type extends the Metadata metadata type and inherits its `fullName`
field.

4. CustomField
Represents the metadata associated with a field. Use this metadata type to create, update, or delete custom field definitions on
standard, custom, and external objects or standard field definitions on standard objects.

5. FieldSet
Represents a field set. A field set is a grouping of fields. For example, you could have a field set that contains fields describing a user's
first name, middle name, last name, and business title.

6. HistoryRetentionPolicy
Represents the policy for archiving field history data. When you set a policy, you specify the number of months that you want to
keep field history in Salesforce before archiving it. By default, when Field Audit Trail is enabled, all field history is retained.

7. Index
Represents an index defined within a custom big object. Use this metadata type to define the composite primary key (index) for a
custom big object. This type extends the Metadata metadata type and inherits its `fullName` field.

8. ListView
ListView allows you to see a filtered list of records, such as contacts, accounts, or custom objects.

9. NamedFilter
Represents the metadata associated with a lookup filter. This metadata type is used to create, update, or delete lookup filter definitions.
This component has been removed as of API version 30.0 and is only available in previous API versions. The metadata associated
with a lookup filter is now represented by the lookupFilter field in the CustomField component.

10. Picklist (Including Dependent Picklist)

Deprecated. Represents a picklist (or dependent picklist) definition for a custom field in a custom object or a custom or standard
field in a standard object, such as an account.

11. ProfileSearchLayouts

Represents a user profile’s search results layouts for an object. `ProfileSearchLayouts` are similar to `SearchLayouts` .
However, with profile-specific layouts, each user profile can have a different search results layout for an object.

12. RecordType

Represents the metadata associated with a record type. Record types let you offer different business processes, picklist values, and
page layouts to different users. Use this metadata type to create, update, or delete record type definitions for a custom object.


#### Metadata Types ActionOverride

13. SearchLayouts

Represents the metadata associated with the search layouts for an object. You can customize which fields to display for users in
search results, search filter fields, lookup dialogs, and recent record lists on tab home pages. You can access SearchLayouts only by
accessing its encompassing CustomObject.

14. SharingReason

Represents an Apex sharing reason, which is used to indicate why sharing was implemented for a custom object. Apex managed
sharing allows developers to use Apex to programmatically share custom objects. When you use Apex managed sharing to share a
custom object, only users with the “Modify All Data” permission can add or change the sharing on the custom object's record, and
the sharing access is maintained across record owner changes.

15. SharingRecalculation

Represents Apex classes that recalculate the Apex managed sharing for a specific custom object.

16. ValidationRule

Represents a validation rule, which is used to verify that the data a user enters in a record is valid and can be saved. A validation rule
contains a formula or expression that evaluates the data in one or more fields and returns a value of `true` or `false` . Validation
rules also include an error message that your client application can display to the user when the rule returns a value of `true` due
to invalid data.

17. WebLink

Represents a custom button or link defined in a custom object.

18. Metadata Field Types

These field types extend the field types described in the _Salesforce Object Reference_ .

SEE ALSO:

CustomField

Metadata

Picklist (Including Dependent Picklist)

SearchLayouts

WebLink

CustomObjectTranslation

ListView

CompactLayout

#### ActionOverride

Represents an action override on a standard or custom object. Use it to create, update, edit, or delete action overrides. You can access
#### ActionOverride only by accessing its encompassing CustomObject.

Declarative Metadata File Suffix and Directory Location

Action overrides are defined as part of a standard or custom object.

Version

Action overrides are available in API version 18.0 and later. As of Summer ’13, action overrides can be applied to both standard and
custom objects. Previously, action overrides only applied to custom objects.


Metadata Types ActionOverride

Fields

Unless otherwise noted, all fields are creatable, filterable, and nillable.

**Field Name** **Field Type** **Description**

`actionName` string Required. The possible values are the same as the actions you can override:

**•** `accept`

**•** `clone`

**•** `delete`

**•** `edit`

**•** `list`

**•** `new`

**•** `tab`

**•** `view`

`comment` string Any comments you want associated with the override.

`content` string Set this field if `type` is set to `flexipage`, `lightningcomponent`,
`scontrol`, or `visualforce` . It refers to the name of the Lightning

page, Lightning component, s-control, or Visualforce page to use as the
override. To reference installed components, use this format:
_**`Component_namespace`**_ `__` _**`Component_name`**_ .

`formFactor` FormFactor (enumeration of
type string)

The size of the page being overridden.

If the `type` field is set to `flexipage`, set this field to `Large` to
override the View action with a Lightning page in Lightning Experience.

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


Metadata Types ActionOverride

**Field Name** **Field Type** **Description**

**•** In API version 43.0 and later, a Lightning component override for
Lightning Experience returns the `Large` value and a Lightning
component override for mobile returns the `Small` value, as
expected.

`skipRecordTypeSelect` boolean Set this field to `true` if you prefer that any new records created by this
action override aren’t forwarded to the record type selection page. This

field is only valid if the `actionName` is a “create” type (like `new` ), and
`type` is set to `visualforce` . This field is available in API version 21.0
and later.

`type` ActionOverrideType Required. Represents the type of action override. Valid values are described
(enumeration of type string) in ActionOverrideType.

ActionOverrideType

ActionOverrideType on page 756 is an enumeration of type string that defines which kind of action override to use. The valid values are:

**•** `default` —The override uses a custom override provided by an installed package. If there isn’t one available, the standard Salesforce
behavior is used.

**•** `flexipage` —The override uses behavior from a Lightning page, and is only valid for the View action in Lightning Experience.

**•** `lightningcomponent` —The override uses behavior from a Lightning component.

**•** `scontrol` —The override uses behavior from an s-control.

**•** `standard` —The override uses regular Salesforce behavior.

**•** `visualforce` —The override uses behavior from a Visualforce page.

Note: Existing s-controls can be used as overrides for Salesforce Classic under certain conditions. However, s-controls have been
deprecated since the Spring ’09 release. We recommend using Visualforce pages instead.

Usage

You can't delete ActionOverrides by deploying with `destructiveChange.xml` . To delete an ActionOverride, retrieve the
CustomObject. In the definition file, find the `<ActionOverrides>` section, and remove the `<content>` row. Then, change the
`<type>` value in that same section to `Default` . Do this for every override you want to reset. After making the changes, rezip the
folder and deploy.

You can remove one override at a time each with its own deploy, or you can remove multiple overrides in a single deploy. However, we
recommend that you do a fresh retrieve every time you want to delete a new override. Don’t use a previously retrieved file.

Org default flexipage override assignment metadata can’t be retrieved from a managed package.

Declarative Metadata Sample Definitions

You can define action overrides, as in these examples for the Edit action.

A Visualforce page override for Salesforce Classic:

```
   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

      <actionOverrides>

```


Metadata Types ActionOverride

```
        <actionName>edit</actionName>

        <type>visualforce</type>

        <content>myEditVFPage</content>

        <comment>This edit action is a lot safer.</comment>

      </actionOverrides>

   </CustomObject

```

This example includes no value for FormFactor. Using no value is the same as using the `null` value, which represents Salesforce Classic.

A Lightning component override for Lightning Experience:

```
   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

      <actionOverrides>

        <actionName>edit</actionName>

        <type>lightningcomponent</type>

        <content>myEditLightningComponent</content>

        <formFactor>Large</formFactor>

        <comment>This edit action is a lot safer.</comment>

      </actionOverrides>

   </CustomObject>

```

A Lightning component override for the Salesforce mobile app:

```
   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

      <actionOverrides>

        <actionName>edit</actionName>

        <type>lightningcomponent</type>

        <content>myEditLightningComponent</content>

        <formFactor>Small</formFactor>

        <comment>This edit action is a lot safer.</comment>

      </actionOverrides>

   </CustomObject>

```

When overrides are included in a managed package, the overrides are represented as `default` type in the metadata. Calling retrieve()
presents the following:

```
   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

      <actionOverrides>

        <actionName>edit</actionName>

        <type>default</type>

      </actionOverrides>

   </CustomObject>

```

If you subscribe to a managed package with default overrides, you can replace the default override behavior by editing the XML. For
example, to replace the Visualforce page override with the Salesforce standard page for Salesforce Classic, use:

```
   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

      <actionOverrides>

        <actionName>edit</actionName>

        <type>standard</type>

      </actionOverrides>

   </CustomObject>

```

To set a Lightning page action override on the View standard button in Lightning Experience, use:

```
   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

      <actionOverrides>

```


#### Metadata Types BusinessProcess

```
        <actionName>View</actionName>

        <content>myLightningPage</content>

        <formFactor>Large</formFactor>

        <type>flexipage</type>

      </actionOverrides>

   </CustomObject>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

CustomObject

#### BusinessProcess

The BusinessProcess metadata type enables you to display different picklist values for users based on their profile.

Multiple business processes allow you to track separate sales, support, and lead lifecycles. A sales, support, lead, or solution process is
assigned to a record type. The record type determines the user profiles that are associated with the business process.

Important: Don’t use business processes as an access control mechanism. Profile assignment governs create and edit access for
business process but doesn’t govern read access. For example, a user assigned to a profile that isn't enabled for a particular business
process can't create or edit it, but they can read the business process record.

Users with access to a business process can read all information it stores. Don’t store sensitive information in the business process
description, name, or picklist values. Instead, store sensitive information in a separate object or fields to which you’ve applied
appropriate access controls.

Declarative Metadata File Suffix and Directory Location

Business processes are defined as part of the custom object or standard object definition. See CustomObject for more information.

Version

#### BusinessProcess on page 758 components are available in API version 17.0 and later.

Special Access Rules

Access to this object requires the View Setup and Configuration permission.

Fields

**Field** **Field Type** **Description**

`description` string Description for the business process.


Metadata Types BusinessProcess

**Field** **Field Type** **Description**

`fullName` string Required. The name used as a unique identifier for API access.
This field is inherited from the Metadata component, but the

string it contains is created differently than the `fullName`
strings for other types. For a `fullName` string BusinessProcess
on page 758, the `fullName` is created combining the Entity
Name and Business Process Name. For example, for a business
process called “Bulk Orders” for opportunities, the `fullName`
would be `Opportunity.Bulk Orders` .

`isActive` boolean Indicates if the business process is active ( `true` ) or not
( `false` ).

`namespacePrefix` string The namespace of the developer organization where the
package was created.

`values` PicklistValue[] A list of picklist values associated with this business process.

Declarative Metadata Sample Definition

The following is a sample XML definition of a lead business process.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

   ....

      <businessProcesses>

        <fullName>HardwareLeadProcess</fullName>

        <description>Lead Process for hardware division</description>

        <isActive>true</isActive>

        <values>

           <fullName>Closed - Converted</fullName>

           <default>false</default>

        </values>

        <values>

           <fullName>CustomLeadStep1</fullName>

           <default>false</default>

        </values>

        <values>

           <fullName>CustomLeadStep2</fullName>

           <default>false</default>

        </values>

        <values>

           <fullName>Open - Not Contacted</fullName>

           <default>false</default>

        </values>

        <values>

           <fullName>Working - Contacted</fullName>

           <default>true</default>

        </values>

      </businessProcesses>

   ....

   </CustomObject>

```


#### Metadata Types CompactLayout

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file only when a RecordType on page
793 is specified. For information about using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

_[Salesforce DX Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/packaging_packageable_components.htm#mdc_business_process_group)_ : BusinessProcessGroup

CustomObject

#### CompactLayout

Represents the metadata associated with a compact layout. This type extends the Metadata metadata type and inherits its `fullName`
field.

A compact layout displays a record’s key fields at a glance in the Salesforce mobile app, Lightning Experience, and in the Outlook and
Gmail integrations.

Compact layouts support all field types except:

**•** text area

**•** long text area

**•** rich text area

**•** multi-select picklist

[For more information on compact layouts, see Compact Layouts in the Salesforce Help.](https://help.salesforce.com/s/articleView?id=platform.compact_layout_overview.htm&type=5&language=en_US)

File Suffix and Directory Location

Compact layouts are defined as part of the custom object, standard object, or external object definition. See CustomObject for more
information.

Version

#### CompactLayout components are available in API version 29.0 and later. CompactLayout components are available for external objects

in API version 42.0 and later.

Fields

**Field Name** **Field Type** **Description**

`fields` string The fields assigned to the compact layout. Their order represents the
prioritization given to them when defining the compact layout.

`label` string Label that represents the object throughout the Salesforce user interface.


Metadata Types CompactLayout

Declarative Metadata Sample Definition

The following is an example of a CompactLayout component:

```
   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

      <actionOverrides>

        <actionName>Accept</actionName>

        <type>Default</type>

      </actionOverrides>

      <actionOverrides>

        <actionName>Clone</actionName>

        <type>Default</type>

      </actionOverrides>

      <actionOverrides>

        <actionName>Delete</actionName>

        <type>Default</type>

      </actionOverrides>

      <actionOverrides>

        <actionName>Edit</actionName>

        <type>Default</type>

      </actionOverrides>

      <actionOverrides>

        <actionName>List</actionName>

        <type>Default</type>

      </actionOverrides>

      <actionOverrides>

        <actionName>New</actionName>

        <type>Default</type>

      </actionOverrides>

      <actionOverrides>

        <actionName>Tab</actionName>

        <type>Default</type>

      </actionOverrides>

      <actionOverrides>

        <actionName>View</actionName>

        <type>Default</type>

      </actionOverrides>

      <compactLayouts>

        <fullName>testCompactLayout</fullName>

        <fields>textfield__c</fields>

        <label>testCompactLayoutLabel</label>

      </compactLayouts>

      <compactLayoutAssignment>SYSTEM</compactLayoutAssignment>

      <deploymentStatus>Deployed</deploymentStatus>

      <enableActivities>false</enableActivities>

      <enableFeeds>false</enableFeeds>

      <enableHistory>false</enableHistory>

      <enableReports>false</enableReports>

      <fields>

        <fullName>textfield__c</fullName>

        <externalId>false</externalId>

        <label>textfield</label>

        <length>255</length>

        <required>false</required>

        <type>Text</type>

```


#### Metadata Types CustomField

```
        <unique>false</unique>

      </fields>

      <label>customObj</label>

      <nameField>

        <label>customObj Name</label>

        <type>Text</type>

      </nameField>

      <pluralLabel>customObjs</pluralLabel>

      <recordTypes>

        <fullName>RT1</fullName>

        <active>true</active>

        <label>RT1</label>

        <compactLayoutAssignment>testCompactLayout</compactLayoutAssignment>

      </recordTypes>

      <recordTypes>

        <fullName>RT2</fullName>

        <active>true</active>

        <label>RT2</label>

      </recordTypes>

      <searchLayouts/>

      <sharingModel>ReadWrite</sharingModel>

   </CustomObject>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### CustomField

Represents the metadata associated with a field. Use this metadata type to create, update, or delete custom field definitions on standard,
custom, and external objects or standard field definitions on standard objects.

This type extends the Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Only standard fields that you can customize are supported, that is, standard fields to which you can add help text or enable history
tracking or Chatter feed tracking. Other standard fields aren't supported, including system fields (such as `CreatedById` or
`LastModifiedDate` ) and autonumber fields. Some standard picklist fields aren’t supported. See Unsupported Metadata Types. By
default, a custom object doesn’t have any standard fields that are customizable.

Specify the full name whenever you create or update a field. For example, a custom field on a custom object:

```
   MyCustomObject__c.MyCustomField__c

```

An example of a custom field on a standard object:

```
   Account.MyAcctCustomField__c

```

An example of a standard field on a standard object:

```
   Account.Phone

```


Metadata Types CustomField

An example of a custom field on an external object:

```
   MyExternalObject__x.MyCustomField__c

```

Note: In Metadata API, external objects are represented by the CustomObject metadata type.

These custom field types aren’t available for external objects.

**•** Auto-number (available only with the cross-org adapter for Salesforce Connect)

**•** Currency (available only with the cross-org adapter for Salesforce Connect)

**•** Formula

**•** Location

**•** Master-detail relationship

**•** Picklist and multi-select picklist (available only with the cross-org adapter for Salesforce Connect)

**•** Roll-up summary

**•** Text (encrypted)

**•** Text Area (rich)

Declarative Metadata File Suffix and Directory Location

Custom fields are user-defined fields and are part of the custom object or standard object definition. See CustomObject for more
information. Standard fields are predefined on standard objects.

Note: Retrieving a component of this metadata type in a project makes the component appear in any Profile and PermissionSet
components that are retrieved in the same package.

Retrieving Fields on Custom or Standard Objects

When you retrieve a custom or standard object, you return everything associated with the object, except for standard fields that aren't
customizable. You can also retrieve only specific fields for an object by explicitly naming the object and fields in `package.xml` . The
following definition in `package.xml` creates the files `objects/MyCustomObject__c.object` and
`objects/Account.object`, each containing the requested field definitions.

```
   <types>

     <members>MyCustomObject__c.MyCustomField__c</members>

     <members>Account.MyCustomAccountField__c</members>

     <members>Account.Phone</members>

     <name>CustomField</name>

   </types>

```

Retrieving or Deploying Fields on Data 360 Objects

When you retrieve a Data 360 object, such as a DLO or DMO, not all of the custom field properties are returned. The properties returned
depend on the data type of the custom field.

When you deploy a Data 360 object via Metadata API, in API version 60.0 or later, the call succeeds only if the properties are supported
by the custom field's data type. If you include a property that isn't supported by the field's data type, the API returns an error.

Data 360 objects support these data types.

**•** Boolean/Checkbox


Metadata Types CustomField

**•** Date

**•** DateTime

**•** Email

**•** Lookup (DMOs only)

**•** Number

**•** Percent

**•** Phone

**•** Text

**•** Url

Version

Custom and standard fields are available in API version 10.0 and later.

Fields

Unless otherwise noted, all fields are creatable, filterable, and nillable.

**Field Name** **Field Type** **Description**

`businessOwnerGroup` reference Indicates the group associated with this field. The business owner
group understands the importance of the field’s data to your

company, and can be responsible for determining the minimum
security classification. This field is available in API version 45.0 and
later.

`businessOwnerUser` reference Indicates the person associated with this field. The business owner
understands the importance of the field’s data to your company,

and can be responsible for determining the minimum security
classification. This field is available in API version 45.0 and later.

`businessStatus` picklist Indicates whether the field is in use. Valid values include:

**•** `Active`

**•** `DeprecateCandidate`

**•** `Hidden`

This field is available in API version 45.0 and later

`caseSensitive` boolean

Indicates whether the field is case-sensitive ( `true` ) or not
( `false` ).

For indirect lookup relationship fields on external objects, this
attribute affects how this custom field’s values are matched against
the values of the `referenceTargetField` .

`complianceGroup` multipicklist Indicates the compliance acts, definitions, or regulations related
to the field’s data. Valid values include:

**•** `CCPA`

**•** `COPPA`


Metadata Types CustomField

**Field Name** **Field Type** **Description**

**•** `GDPR`

**•** `HIPAA`

**•** `PCI`

**•** `PII`

This field is available in API version 47.0 and later.

`customDataType` string Deprecated in the Spring ‘19 (API version 45.0) release.

`defaultValue` string If specified, represents the default value of the field.

`deleteConstraint` DeleteConstraint (enumeration Provides deletion options for lookup relationships. Valid values are:
of type string)

**•** `Cascade` —Deletes the lookup record as well as associated
lookup fields.

**•** `Restrict` —Prevents the record from being deleted if it's
in a lookup relationship.

**•** `SetNull` —This value is the default. If the lookup record is
deleted, the lookup field is cleared.

For more information on lookup relationships, see "Object
Relationships" in Salesforce Help.

`deprecated` boolean Reserved for future use.

`description` string Description of the field.

`displayFormat` string The display format.

`displayLocationInDecimal` boolean Indicates how the geolocation values of a custom Location field
appear in the user interface. If `true`, the geolocation values appear

in decimal notation. If `false`, the geolocation values appear as
degrees, minutes, and seconds.

`elementType` ElementType (enumeration of Reserved for future use.
type string)

`encrypted` boolean

`encryptionScheme` EncryptionScheme
(enumeration of type string)

This entry is about Shield Platform Encryption, not Classic
Encryption.

Indicates whether this field is encrypted ( `true` ) or not ( `false` ).
This field is available in API version 34.0 through 43.0.

This entry is about Shield Platform Encryption, not Classic
Encryption.

For encrypted fields, determines which encryption scheme a field
takes. Valid values are

**•** `CaseInsensitiveDeterministicEncryption`

**•** `CaseSensitiveDeterministicEncryption`

**•** `None`


Metadata Types CustomField

**Field Name** **Field Type** **Description**

**•** `ProbabilisticEncryption`

This field is available in API version 44.0 and later.

`externalDeveloperName` string Available only for external objects. Name of the table column on
the external data source that maps to this custom field in Salesforce.

Corresponds to `External Column Name` in the user
interface. This field is available in API version 32.0 and later.

`externalId` boolean

Indicates whether the field is an external ID field ( `true` ) or not
( `false` ). This property is returned only if the custom field data
type is AutoNumber, Email, Number, or Text.

`fieldManageability` FieldManageability Determines who can update the field after it’s released in a
(enumeration of type string) managed package. Valid values:

**•** `Locked` —The field can’t be updated.

**•** `DeveloperControlled` —The creator of the record can
update the field with a package upgrade.

**•** `SubscriberControlled` —Anyone with proper
permissions can update the field. The field can’t be updated
with a package upgrade.

Available only for fields on custom metadata types. If the field type
is `MetadataRelationship`, and the manageability of the
entity definition field is:

**•** Subscriber-controlled, then the Field Definition field must be
subscriber-controlled.

**•** Upgradeable, then the Field Definition field must be either
upgradeable or subscriber-controlled.

`formula` string If specified, represents a formula on the field.

`formulaTreatBlanksAs` TreatBlanksAs (enumeration of Indicates how to treat blanks in a formula. Valid values are:
type string) `BlankAsBlank` and `BlankAsZero` .

`fullName` string Inherited from Metadata, this field is defined in the WSDL for this
metadata type. It must be specified when creating, updating, or

deleting. See `createMetadata()` to see an example of this
field specified for a call.

This value can't be `null` .

`globalPicklist` string. (This field is available in API version 37.0 only and removed from
later versions.) If this custom field is a picklist that’s based on a

global picklist, `globalPicklist` is the name of the global
picklist whose value set this picklist inherits. A custom picklist that’s
based on a global picklist is restricted. You can only add or remove
values by editing the global picklist.


Metadata Types CustomField

**Field Name** **Field Type** **Description**

`indexed` boolean Indicates if the field is indexed. If this field is unique or the
`externalId` is set true, the `isIndexed` value is set to true.

This field has been deprecated as of API version 14.0 and is only
provided for backward compatibility.

`inlineHelpText` string Represents the content of field-level help. For more information,
see "Define Field-Level Help" in Salesforce Help.

`isAIPredictionField` boolean Available for Number type custom fields when you use Einstein
Prediction Builder. Denotes whether the field can store and display

Einstein prediction data on an object. Use Einstein Prediction Builder
to determine the data for the target field. This field is available in
API version 43.0 and later.

`isFilteringDisabled` boolean

Available only for external objects. Indicates whether the custom
field is available in filters. This field is available in API version 32.0
and later.

`isNameField` boolean Available only for external object fields of type text. For each
external object, you can specify one field as the name field. If you

set this value to `true`, make sure that the external table column
identified by the `externalDeveloperName` attribute
contains name values. This field is available in API version 32.0 and
later.

`isSortingDisabled` boolean Available only for external objects. Indicates whether the custom
field is sortable. This field is available in API version 32.0 and later.

`label` string Label for the field. You can't update the label for standard picklist
fields, such as the `Industry` field for accounts.

`length` int Length of the field.

`lookupFilter` LookupFilter Represents the metadata associated with a lookup filter. This
metadata type is used to create, update, or delete lookup filter

definitions. This component has been removed as of API version
30.0 and is only available in previous API versions. The metadata
associated with a lookup filter is now represented by the
`lookupFilter` field in the CustomField component.

This field is available in API version 30.0 and later.

LookupFilter isn't supported on the article type object.

`maskChar` EncryptedFieldMaskChar
(enumeration of type string)

This page is about Classic Encryption, not Shield Platform
Encryption.

For encrypted fields, specifies the character to be used as a mask.
Valid values are:

**•** `asterisk`

**•** `X`


Metadata Types CustomField

**Field Name** **Field Type** **Description**

For more information on encrypted fields, see Classic Encryption
for Custom Fields in Salesforce Help.

`maskType` EncryptedFieldMaskType
(enumeration of type string)

This page is about Classic Encryption, not Shield Platform
Encryption.

For encrypted text fields, specifies the format of the masked and
unmasked characters in the field. Valid values are:

**•** `all` —All characters in the field are hidden. This option is
equivalent to the `Mask All Characters` option in
Salesforce.

**•** `creditCard` —The first 12 characters are hidden and the
last four display. This option is equivalent to the `Credit`
`Card Number` option in Salesforce.

**•** `lastFour` —All characters are hidden but the last four
display. This option is equivalent to the `Last Four`
`Characters Clear` option in Salesforce.

**•** `nino` —All characters are hidden. Salesforce automatically
inserts spaces after each pair of characters if the field contains
nine characters. This option is equivalent to the `National`
`Insurance Number` option in Salesforce.

**•** `sin` —All characters are hidden but the last four display. This
option is equivalent to the `Social Insurance Number`
option in Salesforce.

**•** `ssn` —The first five characters are hidden and the last four
display. This option is equivalent to the `Social Security`
`Number` option in Salesforce.

For more information on encrypted fields, see "Classic Encryption
for Custom Fields" in Salesforce Help.

`metadataRelationshipControllingField` string In custom metadata relationships, represents the controlling field
that specifies the standard or custom object in an entity definition

metadata relationship. Required when creating a field definition
or entity particle metadata relationship on a custom metadata
type. The object specified in the controlling field determines the
values available in its dependent field definition or entity particle.
For example, specifying the Account object filters the available
fields in the field definition to Account fields only. This field is
available in API version 39.0 and later.

`picklist` Picklist

( **Deprecated.** Use this field in API version 37.0 and earlier only. In
later versions, use `valueSet` instead.) If specified, the field is a
picklist, and this field enumerates the picklist values and labels.

`populateExistingRows` boolean Indicates whether existing rows are going to be populated ( `true` )
or not ( `false` ).


Metadata Types CustomField

**Field Name** **Field Type** **Description**

`precision` int

The precision for number values. Precision is the number of digits
in a number. For example, the number 256.99 has a precision value
of 5.

`referenceTargetField` string Available only for indirect lookup relationship fields on external
objects. Specifies the custom field on the parent object to match

against this indirect lookup relationship field, whose values come
from an external data source. The specified custom field on the
parent object must have both `externalId` and `unique` set
to `true` . This field is available in API version 32.0 and later.

`referenceTo` string If specified, indicates a reference this field has to another object.

`relationshipLabel` string Label for the relationship.

`relationshipName` string

If specified, indicates the value for one-to-many relationships. For
example, in the object MyObject that had a relationship to
YourObject, the relationship name can be YourObjects.

`relationshipOrder` int This field is valid for all master-detail relationships, but the value is
only non-zero for junction objects. A junction object has two

master-detail relationships, and is analogous to an association table
in a many-to-many relationship. Junction objects must define one
parent object as primary (0), the other as secondary (1). The
definition of primary or secondary affects delete behavior and
inheritance of look and feel, and record ownership for junction
objects. For more information, see Salesforce Help.

0 or 1 are the only valid values, and 0 is always the value for objects
that aren't junction objects.

`reparentableMasterDetail` boolean

Indicates whether the child records in a master-detail relationship
on a custom object can be reparented to different parent records.
The default value is `false` .

This field is available in API version 25.0 and later.

`required` boolean Indicates whether the field requires a value on creation ( `true` ) or
not ( `false` ).

`scale` int

The scale for the field. Scale is the number of digits to the right of
the decimal point in a number. For example, the number 256.99
has a scale of 2.

`securityClassification` picklist Indicates the sensitivity of the data contained in the field. Valid
values include:

**•** `Public`

**•** `Internal`

**•** `Confidential`

**•** `Restricted`


Metadata Types CustomField

**Field Name** **Field Type** **Description**

**•** `MissionCritical`

This field is available in API version 45.0 and later.

`startingNumber` int If specified, indicates the starting number for the field. When you
create records, `Starting Number` ’s value increments to store

the number that will be assigned to the next auto-number field
created.

**•** You can’t retrieve the starting number of an auto-number field
through Metadata API. To specify a `Starting Number`
while deploying, add a `startingNumber` tag for your field
to your `package.xml` file. For example:

```
                              <startingNumber>42</startingNumber>

```

**•** If you deploy without specifying a `Starting Number`
value in your `package.xml` file, the default starting number
for standard fields is `0` . The default starting number for custom
fields is `1` .

`stripMarkup` boolean Set to `true` to remove markup, or `false` to preserve markup.
Used when converting a rich text area to a long text area.

`summarizedField` string

`summaryFilterItems` FilterItem[]

Represents the field on the detail row that’s being summarized.
This field can't be null unless the `summaryOperation` value
is `count` .

Represents the set of filter conditions for this field if it's a summary
field. This field is summed on the child if the filter conditions are
met.

`summaryForeignKey` string Represents the master-detail field on the child that defines the
relationship between the parent and the child.

`summaryOperation` SummaryOperations Represents the type of sum operation to be performed. Valid values
(enumeration of type string) are:

**•** `Count`

**•** `Min`

**•** `Max`

**•** `Sum`

`trackFeedHistory` boolean Indicates whether the field is enabled for feed tracking ( `true` ) or
not ( `false` ). To set this field to `true`, the `enableFeeds` field

on the associated CustomObject must also be `true` . For more
information, see "Customize Chatter Feed Tracking" in Salesforce
Help.

This field is available in API version 18.0 and later.


Metadata Types CustomField

**Field Name** **Field Type** **Description**

`trackHistory` boolean

Indicates whether history tracking is enabled for the field ( `true` )
or not ( `false` ). Also available for standard object fields (picklist
and lookup fields only) in API version 30.0 and later.

To set `trackHistory` to `true`, the `enableHistory` field
on the associated standard or custom object must also be `true` .

For more information, see "Field History Tracking" in Salesforce
Help.

Field history tracking isn’t available for external objects.

`trackTrending` boolean Indicates whether historical trending data is captured for the field
( `true` ) or not ( `false` ).An object is enabled for historical trending

if this attribute is `true` for at least one field. Available in API
version 29.0 and later.

For more information, see "Report on Historical Changes" in
Salesforce Help.

`trueValueIndexed` boolean

`type` FieldType (enumeration of type
string)

Only relevant for a checkbox field. If set, `true` values are built
into the index. This field has been deprecated as of API version 14.0
and is only provided for backward compatibility.

Indicates the field type for the field. Valid values are enumerated
in FieldType.

For standard fields on standard objects, the `type` field is optional.
This field is included for some standard field types, such as Picklist

or Lookup, but not for others. The `type` field is included for
custom fields.

`unique` boolean Indicates whether the field is unique ( `true` ) or not ( `false` ).

`valueSet` ValueSet Represents the set of values that make up a picklist on a custom
field. Each value is defined as a CustomValue on page 838. If this

custom field is a picklist that uses a global value set, `valueSet`
is the name of the global value set whose values this picklist
inherits. A custom picklist that uses a global value set is restricted.
You can only add or remove values by editing the global value set.

A ValueSet component has either a `valueSetDefinition`
or a `valueName` specified, but never both.

This field is available in API version 38.0 and later.

`visibleLines` int Indicates the number of lines displayed for the field.


Metadata Types CustomField

**Field Name** **Field Type** **Description**

`writeRequiresMasterRead` boolean

Sets the minimum sharing access level required on the primary
record to create, edit, or delete child records. This field applies only
to master-detail or junction object custom field types.

**•** `true` —Allows users with Read access to the primary record
permission to create, edit, or delete child records. This setting
makes sharing less restrictive.

**•** `false` —Allows users with Read/Write access to the primary
record permission to create, edit, or delete child records. This
setting is more restrictive than `true`, and is the default value.

For junction objects, the most restrictive access from the two
parents is enforced. For example, if you set to `true` on both
master-detail fields, but users have Read access to one primary
record and Read/Write access to the other primary record, users
aren't able to create, edit, or delete child records.

Fields use additional data types. For more information, see Metadata Field Types on page 806.

MktDataModelFieldAttributes

This is a subtype of CustomField.

**Field Name** **Field Type** **Description**

`definitionCreationType` DefinitionCreationType Indicates how this object was added. Valid values are:
enumeration

**•** `Bridge`

**•** `Custom`

**•** `Derived`

**•** `Standard`

**•** `System`

Valid values availble in API version 62.0 and later are:

**•** `Activation_Audience`

**•** `Ad_Audience_Insights`

**•** `ADG`

**•** `Calculated_Insight`

**•** `CG_Audience`

**•** `Chunk`

**•** `Directory_Table`

**•** `External`

**•** `Problem_Records`

**•** `Segment_Membership`

**•** `Semantic`


Metadata Types CustomField

**Field Name** **Field Type** **Description**

**•** `Transform`

**•** `Vector_Embedding`

If this field is used for merging data, indicates what the system should do when
an invalid merge occurs.

Valid values are:

**•** `Drop`

**•** `Keep`

**•** `Override`

```
invalidMergeActionType

```

InvalidMergeActionType
(enumeration of type
string)

`isDynamicLookup` boolean When true, the existing data is queried for a unique set of values for this field.

`primaryIndexOrder` int If supplied, indicates that this field is part of the primary key. The number value
(starting at 1) indicates the order of attributes if it’s a compound primary key.

`refAttrDeveloperName` string When this is a Standard Field, it’s the Name of the field from the Reference
Model.

`mktDatalakeSrcKeyQualifier` string String storing the developer name of MktDataLakeSrcKeyQualifier configured
on the field

MktDataLakeFieldAttributes

This is a subtype of CustomField. MktDataLakeFieldAttributes is available in API version 50.0 or later.

**Field Name** **Field Type** **Description**

```
definitionCreationType

```

DefinitionCreationType Indicates how this object is added. Valid values are:
(enumeration of type

**•** `Bridge`

string)

**•** `Custom`

**•** `Derived`

**•** `Standard`

**•** `System`

Valid values available in API version 62.0 and later are:

**•** `ADG`

**•** `Calculated_Insight`

**•** `CG_Audience`

**•** `Chunk`

**•** `Directory_Table`

**•** `External`

**•** `Semantic`

**•** `Vector_Embedding`


Metadata Types CustomField

**Field Name** **Field Type** **Description**

`dateFormat` string

Optional: The Date format of date, time, date/time fields in this Lake field.

**This field is deprecated in API version 55.0 and later.**

`externalName` string The external name of this field.

`isEventDate` boolean When true, this field contains the event date for behavioral model area objects
that are used to partition data.

`primaryIndexOrder` int If supplied, indicates that this field is part of the primary key. The number value
(starting at 1) indicates the order of attributes if it’s a compound primary key.

`isInternalOrganization` boolean

When true, this field contains the value for internal organization. In this case,
the value of the field is the name of the internal organization. Landing Objects
don't have access to the Salesforce ID and thus are using the developer name.

`isRecordModified` boolean Indicates the record modified field used to calibrate latest record version.

`mktDatalakeSrcKeyQualifier` string String storing the developer name of MktDataLakeSrcKeyQualifier configured
on the field. Available in API version 55.0 and later.

`keyQualifierName` string Contains the developer name of key qualifier field. Available in API version 55.0
and later.

LookupFilter

Represents the metadata associated with a lookup filter. Replaces the NamedFilter component, which was removed as of API version
30.0. LookupFilter is available in API version 30.0 and later.

**Field** **Field Type** **Description**

`active` boolean Required. Indicates whether the lookup filter is active ( `true` ) or not
( `false` ).

`booleanFilter` string Specifies advanced filter conditions.

`description` string A description of what this filter does.

`errorMessage` string The error message that appears if the lookup filter fails.

`filterItems` FilterItem[] Required. The set of filter conditions. You can have up to 10 FilterItems
per lookup filter.

`infoMessage` string

The information message displayed on the page. Use to describe
things the user possibly doesn't understand, such as why certain items
are excluded in the lookup filter.

`isOptional` boolean Required. Indicates whether the lookup filter is optional ( `true` ) or
not ( `false` ).

Lookup filters use additional data types. For more information, see Metadata Field Types.


Metadata Types CustomField

FilterItem

Represents one entry in a set of filter criteria.

**Field** **Field Type** **Description**

`field` string Represents the field specified in the filter.

```
operation

```

FilterOperation Represents the filter operation for this filter item. Valid values are:
(enumeration of

**•** `equals`

type string)

**•** `equals`

**•** `notEqual`

`value` string

`valueField` string

Declarative Metadata Sample Definition

**•** `lessThan`

**•** `greaterThan`

**•** `lessOrEqual`

**•** `greaterOrEqual`

**•** `contains`

**•** `notContain`

**•** `startsWith`

**•** `includes`

**•** `excludes`

**•** `within` ( `DISTANCE` criteria only)

Represents the value of the filter item being operated upon, for
example, if the filter is `my_number_field__c > 1`, the value
of `value` is `1` .

Specifies if the final column in the filter contains a field or a field value.

Approval processes don’t support `valueField` entries in filter
criteria.

The following example shows a field definition for a custom field that’s named `Comments__c` .

```
<?xml version="1.0" encoding="UTF-8"?>

<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

....

<fields>

     <fullName>Comments__c</fullName>

     <description>Add your comments about this object here</description>

     <inlineHelpText>This field contains help text for this object</inlineHelpText>

     <label>Comments</label>

     <length>32000</length>

     <type>LongTextArea</type>

     <visibleLines>30</visibleLines>

</fields>

....

</CustomObject>

```


#### Metadata Types FieldSet

This XML is the definition for two fields on the Account standard object—a custom field ( `MyCustomAccountField__c` ), and a
standard field ( `Phone` ) that has history tracking enabled.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

      <fields>

        <fullName>MyCustomAccountField__c</fullName>

        <description>A custom field on the Account standard object.</description>

        <externalId>false</externalId>

        <inlineHelpText>Some help text.</inlineHelpText>

        <label>MyCustomAccountField</label>

        <length>100</length>

        <required>false</required>

        <trackFeedHistory>false</trackFeedHistory>

        <trackHistory>false</trackHistory>

        <type>Text</type>

        <unique>false</unique>

      </fields>

      <fields>

        <fullName>Phone</fullName>

        <trackFeedHistory>false</trackFeedHistory>

        <trackHistory>true</trackHistory>

      </fields>

   </CustomObject>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

CustomObject

Picklist (Including Dependent Picklist)

Metadata

NamedFilter

#### FieldSet

Represents a field set. A field set is a grouping of fields. For example, you could have a field set that contains fields describing a user's
first name, middle name, last name, and business title.

Field sets can be referenced on Visualforce pages dynamically. If the page is added to a managed package, administrators can add,
remove, or reorder fields in a field set to modify the fields presented on the Visualforce page without modifying any code.

Version

#### FieldSet components are available in API version 21.0 and later.


Metadata Types FieldSet

Fields

**Field** **Field Type** **Description**

`availableFields` FieldSetItem[] An array containing all the possible fields in the field set.

`description` string Required. A description provided by the developer that describes
the field set. This is required.

`displayedFields` FieldSetItem[]

An array containing all the fields that are presented on the
Visualforce page. The order in which a field is listed determines
the order of appearance on the page.

`label` string Required. The label used to reference the field set.

FieldSetItem

FieldSetItem represents an individual field in a field set.

**Field** **Field Type** **Description**

`field` string Required. The name of a field in a standard or custom object.

`isFieldManaged` boolean Read-only. Denotes whether the field was added to the field set
via a managed or unmanaged package.

`isRequired` boolean Read-only. Indicates whether the field is universally required
( `true` ) or not ( `false` ).

Declarative Metadata Sample Definition

A sample XML definition of a FieldSet component is shown below.

```
<?xml version="1.0" encoding="UTF-8"?>

<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

   <fieldSets>

     <fullName>FieldSetNames</fullName>

     <availableFields>

        <field>MiddleName__c</field>

     </availableFields>

     <availableFields>

        <field>Title__c</field>

     </availableFields>

     <description>FieldSet containing how to properly address someone</description>

     <displayedFields>

        <field>FirstName__c</field>

     </displayedFields>

     <displayedFields>

        <field>LastName__c</field>

     </displayedFields>

     <label>FieldSet Names</label>

```


#### Metadata Types HistoryRetentionPolicy

```
      </fieldSets>

   </CustomObject>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### HistoryRetentionPolicy

Represents the policy for archiving field history data. When you set a policy, you specify the number of months that you want to keep
field history in Salesforce before archiving it. By default, when Field Audit Trail is enabled, all field history is retained.

This component is only available to users with the RetainFieldHistory permission.

Declarative Metadata File Suffix and Directory Location

Field history retention policies are defined as part of a standard or custom object. You can set field history retention policies for objects
individually. See CustomObject for more information.

Version

Available in API version 31.0 and later.

Fields

**Field Name** **Field Type** **Description**

`archiveAfterMonths` int Required. The number of months that you want to keep field history data
in Salesforce before archiving. You can set a minimum of 1 month and a

maximum of 18 months. If you don't set a number, the default is 18
months. (That is, Salesforce maintains data for 18 months before
archiving.)

`archiveRetentionYears` int

The number of years until you manually delete data from the archive. Use
this field as a reminder for manually deleting data. By default, field history
data isn’t automatically deleted when Field Audit Trail is enabled.

`description` string A text description for the history retention.

`gracePeriodDays` int The number of days of extra time after the `archiveAfterMonths`
period before the data is archived. The `gracePeriodDays` interval

applies only to the first time that the data is archived; because all the data
is copied the first time, the operation can take longer than subsequent
times when only the data that changed since the last archival operation
is copied. The `gracePeriodDays` provides extra time for the
administrator to prepare the organization before the initial archive
operation. You can set a minimum of zero days and a maximum of 10
days. If no number is set, the default is 1 day.


#### Metadata Types Index

Declarative Metadata Sample Definition

This sample shows the definition of a history retention policy for a custom object.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

     <historyRetentionPolicy>

        <archiveAfterMonths>6</archiveAfterMonths>

        <archiveRetentionYears>5</archiveRetentionYears>

        <description>My field history retention</description>

     </historyRetentionPolicy>

   ...

   </CustomObject>

#### Index

```

Represents an index defined within a custom big object. Use this metadata type to define the composite primary key (index) for a custom
big object. This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

#### Indexes are user-defined and are part of the custom object definition for big objects. See CustomObject for more information.

Version

The Index type is available in API version 41.0 and later.

Fields

**Field Name** **Field Type** **Description**

#### fields IndexField[] The definition of the fields in the index.

`label` string Required. This name is used to refer to the big object in the user interface.
Available in API version 41.0 and later.

#### IndexField

Defines which fields make up the index, their order, and sort direction. The order in which the fields are defined determines the order
fields are listed in the index.


Metadata Types Index

**Field Name** **Field Type** **Description**

`name` string

Required. The API name for the field that’s part of the index. This value must
match the `fullName` value for the corresponding field in the fields section
and be marked as required.

Warning: When querying a big object record via SOQL and passing
the results as arguments to the delete API, if any index field name has
a leading or trailing white space, you can't delete the big object record.

`sortDirection` string Required. The sort direction of the field in the index. Valid values are `ASC` for
ascending order and `DESC` for descending order.

Declarative Metadata Sample Definition

The following is an example of an index contained within the definition of a custom big object,
`Customer_Interactions__b.object` .

```
<?xml version="1.0" encoding="UTF-8"?>

<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

   <deploymentStatus>Deployed</deploymentStatus>

// Define the fields within the big object

   <fields>

     <fullName>Purchase__c</fullName>

     <label>Purchase</label>

     <length>16</length>

     <required>false</required>

     <type>Text</type>

     <unique>false</unique>

   </fields>

   <fields>

     <fullName>Order_Number__c</fullName>

     <label>Order Number</label>

     <length>16</length>

     <required>false</required>

     <type>Text</type>

     <unique>true</unique>

   </fields>

   <fields>

     <fullName>Platform__c</fullName>

     <label>Platform</label>

     <length>16</length>

     <required>true</required>

     <type>Text</type>

     <unique>false</unique>

   </fields>

   <fields>

     <fullName>Account__c</fullName>

```


#### Metadata Types ListView

```
        <label>User Account</label>

        <referenceTo>Account</referenceTo>

        <relationshipName>User_Account</relationshipName>

        <required>true</required>

        <type>Lookup</type>

      </fields>

      <fields>

        <fullName>Order_Date__c</fullName>

        <label>Order Date</label>

        <required>true</required>

        <type>DateTime</type>

      </fields>

   // Define the index

      <indexes>

        <fullName>CustomerInteractionsIndex</fullName>

        <label>Customer Interactions Index</label>

        <fields>

           <name>Account__c</name>

           <sortDirection>DESC</sortDirection>

        </fields>

        <fields>

           <name>Platform__c</name>

           <sortDirection>ASC</sortDirection>

        </fields>

        <fields>

           <name>Order_Date__c</name>

           <sortDirection>DESC</sortDirection>

        </fields>

      </indexes>

      <label>Customer Interaction</label>

      <pluralLabel>Customer Interactions</pluralLabel>

   </CustomObject>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

CustomObject

Metadata

#### ListView ListView allows you to see a filtered list of records, such as contacts, accounts, or custom objects.

This type extends the Metadata metadata type and inherits its `fullName` field. See “Create a Custom List View in Salesforce Classic”
in Salesforce Help.


Metadata Types ListView

Note: List views with the Visible only to me `Restrict Visibility` option aren’t accessible in Metadata API. Each of these
list views is associated with a particular user.

Declarative Metadata File Suffix and Directory Location

List views are stored within a CustomObject component. The component can represent a custom object or a standard object, such as
an account.

Version

ListView components for custom objects are available in API version 14.0 and later. ListView components for standard objects, such as
accounts, are available in API version 17.0 and later.

Fields

**Field** **Field Type** **Description**

`booleanFilter` string This field represents an Advanced Option for a filter. Advanced
Options in filters allow you to build up filtering conditions that

use a mixture of AND and OR boolean operators across multiple
filter line items. For example, `(1 AND 2) OR 3` finds records
that match both the first two filter line items or the third.

`columns` string[]

The list of fields in the list view. The field name relative to the
object name, for example MyCustomField__c, is specified for
each custom field.

Field names in the ListView columns don’t always match their
API name counterparts. If person accounts are enabled in your

organization, standard fields merged from a contact into an
account start with the `PC_` prefix, while the corresponding API
name starts with the `Person` prefix. For example, the ListView
column name is `PC_Email` for a corresponding API field name
of `PersonEmail` .

`division` string If your organization uses divisions to segment data and you’ve
got the “Affected by Divisions” permission, records in the list

view must match this division. This field is only available if you’re
searching all records.

This field is available in API version 17.0 and later.

`filterScope` FilterScope (enumeration of Required. This field indicates whether you’re filtering by owner
type string) or viewing all records.

`filters` ListViewFilter[] The list of filter line items.

`fullName` string Required. Inherited from Metadata Metadata, this field is defined
in the WSDL for this metadata type. It must be specified when

creating, updating, or deleting. See `createMetadata()` to
see an example of this field specified for a call.


Metadata Types ListView

**Field** **Field Type** **Description**

`label` string Required. The list view name.

`language` Language The language used for filtering if your organization uses the
Translation Workbench and you’re using the `startsWith`

or `contains` operator. The values entered as search terms
must be in the same language as the filter language.

For a list of valid language values, see Language.

This field is available in API version 17.0 and later.

`queue` string The name of a queue. Objects are sometimes assigned to a
queue so that the users who have access to the queue can

monitor and manage them. When you create a queue, a
corresponding list view is automatically created. See “Create
Queues” in Salesforce Help.

`sharedTo` SharedTo

ListViewFilter

ListViewFilter represents a filter line item.

Sharing access for the list view.

This field is available in API version 17.0 and later.

**Field** **Field Type** **Description**

`filter` string Required. Represents the field specified in the filter.

`operation` FilterOperation (enumeration of Required. The operation used by the filter, such as `equals` .
type string) The valid values are:

**•** `equals`

**•** `notEqual`

**•** `lessThan`

**•** `greaterThan`

**•** `lessOrEqual`

**•** `greaterOrEqual`

**•** `contains`

**•** `notContain`

**•** `startsWith`

**•** `includes`

**•** `excludes`

**•** `within` ( `DISTANCE` criteria only)

`value` string

Represents the value of the filter item being operated upon, for
example, if the filter is `my_number_field__c > 1`, the
value of `value` is `1` .


Metadata Types ListView

FilterScope

The FilterScope is an enumeration of type string that represents the filtering criteria for the records. The valid values are listed in the
table:

**Enumeration Value** **Description**

`Everything` All records, for example All Opportunities.

`Mine` Records owned by the user running the list view, for example My Opportunities.

`MineAndMyGroups` Records owned by the user running the list view, and records assigned to the user’s queues.

```
AssignedToMe

```

Records assigned to the user running the list view.

The `AssignedToMe` scope is supported for the ServiceAppointment object only.

`Queue` Records assigned to a queue.

`Delegated` Records delegated to another user for action: for example, a delegated task. This option is
available in API version 17.0 and later.

```
MyTerritory

MyTeamTerritory

```

Records in the territory of the user seeing the list view. This option is available if territory
management is enabled for your organization. Opportunities can’t be filtered by
`MyTerritory` . This option is available in API version 17.0 and later.

Records in the territory of the team of the user seeing the list view. This option is available if
territory management is enabled for your organization. Opportunities can’t be filtered by
`MyTeamTerritory` . This option is available in API version 17.0 and later.

`Team` Records assigned to a team. In the Lightning Experience UI, the corresponding list view filter is
**My team’s opportunities** . This option is available in API version 17.0 and later.

`SalesTeam` Opportunities assigned to an opportunity team. In the Lightning Experience UI, the corresponding
list view filter is **My opportunity teams** . This option is available in API version 49.0 and later.

`ScopingRule` Records that meet a scoping rule's record criteria. In Lightning Experience, scoping rules are
applied to list views only if the user selects **Filter by scope** .

Declarative Metadata Sample Definition

A sample XML definition of a list view in a custom object is shown.

```
<?xml version="1.0" encoding="UTF-8"?>

<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

. . .

   <listViews>

     <fullName>All_Mileages</fullName>

     <filterScope>everything</filterScope>

     <label>All Mileages</label>

   </listViews>

   <listViews>

     <fullName>My_Mileages</fullName>

     <booleanFilter>1 AND 2</booleanFilter>

     <columns>NAME</columns>

```


#### Metadata Types NamedFilter

```
        <columns>CREATED_DATE</columns>

        <filterScope>mine</filterScope>

        <filters>

           <field>NAME</field>

           <operation>equals</operation>

           <value>Eric Bristow</value>

        </filters>

        <filters>

           <field>City__c</field>

           <operation>equals</operation>

           <value>Paris</value>

        </filters>

        <label>My Mileages</label>

      </listViews>

   . . .

   </CustomObject>

```

Usage

In general, avoid including unedited default list views in managed packages. We discourage including a modified default list view in a
[managed package, as it can result in duplicated list views in the target org. See Incorrect List View Loads Due to Possibility of Existing](https://help.salesforce.com/s/articleView?id=000386164&type=1&language=en_US)
[Duplicate List Views.](https://help.salesforce.com/s/articleView?id=000386164&type=1&language=en_US)

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

CustomObject

Sample package.xml Manifest Files

#### NamedFilter

Represents the metadata associated with a lookup filter. This metadata type is used to create, update, or delete lookup filter definitions.
This component has been removed as of API version 30.0 and is only available in previous API versions. The metadata associated with
a lookup filter is now represented by the lookupFilter field in the CustomField component.

This type extends the Metadata metadata type and inherits its `fullName` field. You can also use this metadata type to work with
customizations of lookup filters on standard fields.

Note: The namedFilter appears as a child of the target object of the associated lookup field.

Declarative Metadata File Suffix and Directory Location

Lookup filters are defined as part of the custom object or standard object definition. See CustomObject for more information.

Note: Retrieving a component of this metadata type in a project makes the component appear in any Profile and PermissionSet
components that are retrieved in the same package.


Metadata Types NamedFilter

Version

Lookup filters are available in API version 17.0 and later. However, the NamedFilter type was removed in API version 30.0. The metadata
associated with a lookup filter is now represented by the lookupFilter field in the CustomField type.

Fields

Unless otherwise noted, all fields are creatable, filterable, and nillable.

**Field Name** **Field Type** **Description**

`active` boolean Required. Indicates whether the lookup filter is active.

`booleanFilter` string Specifies advanced filter conditions.

`description` string A description of what this filter does.

`errorMessage` string The error message that appears if the lookup filter fails.

`field` string

Required. The `fullName` of the custom or standard field
associated with the lookup filter. You can associate one
relationship field with each lookup filter, and vice versa.

Note: You can’t update a field associated with a lookup
filter.

`filterItems` FilterItems[] Required. The set of filter conditions.

`infoMessage` string

The information message displayed on the page. Use to
describe things the user might not understand, such as why
certain items are excluded in the lookup filter.

`fullName` string Inherited from Metadata, this field is defined in the WSDL for
this metadata type. It must be specified when creating,

updating, or deleting. See `createMetadata()` to see an
example of this field specified for a call.

This value can’t be `null` .

`isOptional` boolean Required. Indicates whether the lookup filter is optional.

`name` string Required. The name of the lookup filter. If you create this field
in the user interface, a name is automatically assigned. If you

create this field through Metadata API, you must include the
`name` field.

`sourceObject` string

The object that contains the lookup field that uses this lookup
filter. Set this field if the lookup filter references fields on the
source object.

Lookup filters use additional data types. For more information, see Metadata Field Types.


Metadata Types NamedFilter

FilterItems

FilterItems contains the following properties:

**Field** **Field Type** **Description**

`field` string Represents the field specified in the filter.

```
operation

```

FilterOperation Represents the filter operation for this filter item. Valid values are
(enumeration of enumerated in FilterOperation.
type string)

`value` string

FilterOperation

Represents the value of the filter item being operated upon, for
example, if the filter is `my_number_field__c > 1`, the value
of `value` is `1` .

Here’s an enumeration of type string that lists different filter operations. Valid values are:

**•** `equals`

**•** `notEqual`

**•** `lessThan`

**•** `greaterThan`

**•** `lessOrEqual`

**•** `greaterOrEqual`

**•** `contains`

**•** `notContain`

**•** `startsWith`

**•** `includes`

**•** `excludes`

Declarative Metadata Sample Definition

```
<?xml version="1.0" encoding="UTF-8"?>

<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

....

   <namedfilters>

     <fullName>nf_Acc</fullName>

     <active>true</active>

     <booleanFilter>1 OR 2</booleanFilter>

     <field>Account.lk__c</field>

     <filterItems>

        <field>Account.Phone</field>

        <operation>notEqual</operation>

        <value>x</value>

     </filterItems>

     <filterItems>

        <field>Account.Fax</field>

```


#### Metadata Types Picklist (Including Dependent Picklist)

```
           <operation>notEqual</operation>

           <value>y</value>

        </filterItems>

        <name>Acc</name>

        <sourceObject>Account</sourceObject>

      </namedfilters>

   ....

   </CustomObject>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

CustomObject

#### Picklist (Including Dependent Picklist)

Metadata

CustomField

#### Picklist (Including Dependent Picklist)

Deprecated. Represents a picklist (or dependent picklist) definition for a custom field in a custom object or a custom or standard field
in a standard object, such as an account.

Version

Use this type in API version 37.0 and earlier only. Picklists for custom fields in custom objects are available in API version 12.0 and later.
Picklists for custom or standard fields in standard objects, such as accounts, are available in API version 16.0 and later.

In API version 38.0 and later, Picklist is replaced by ValueSet on page 809 on the CustomField type.

Declarative Metadata File Suffix and Directory Location

Picklist definitions are included in the custom object and field with which they’re associated.

Fields

Picklist contains the following fields:

**Field Name** **Field Type** **Description**

`controllingField` string The `fullName` of the controlling field if `controllingField` is
a dependent picklist. A dependent picklist works in conjunction with a

controlling picklist or checkbox to filter the available options. The value
chosen in the controlling field affects the values available in the
dependent field. This field is available in API version 14.0 and later.


Metadata Types Picklist (Including Dependent Picklist)

**Field Name** **Field Type** **Description**

`picklistValues` PicklistValue[]
Required. Represents a set of values for a picklist.

`restrictedPicklist` boolean

`sorted` boolean

Java Sample

Indicates whether the picklist’s value list is restricted. With a restricted
picklist, only an admin can add or change values; users can’t load or
remove values through the API. By default this value is `false` .

This field is available in API version 37.0 and later.

Indicates whether values are sorted ( `true` ), or not ( `false` ). By default
this value is `false` .

The following sample uses a picklist. For a complete sample of using a picklist with record types and profiles, see Profile on page 1716.

```
public void setPicklistValues() {

  // Create a picklist

  Picklist expenseStatus = new Picklist();

  PicklistValue unsubmitted = new PicklistValue();

  unsubmitted.setFullName("Unsubmitted");

  PicklistValue submitted = new PicklistValue();

  submitted.setFullName("Submitted");

  PicklistValue approved = new PicklistValue();

  approved.setFullName("Approved");

  PicklistValue rejected = new PicklistValue();

  rejected.setFullName("Rejected");

  expenseStatus.setPicklistValues(new PicklistValue[]

    {unsubmitted, submitted, approved, rejected});

  CustomField expenseStatusField = new CustomField();

  expenseStatusField.setFullName(

    "ExpenseReport__c.ExpenseStatus__c");

  expenseStatusField.setLabel("Expense Report Status");

  expenseStatusField.setType(FieldType.Picklist);

  expenseStatusField.setPicklist(expenseStatus);

  try {

   AsyncResult[] ars =

   metadataConnection.create(new Metadata[] {expenseStatusField});

  } catch (ConnectionException ce) {

   ce.printStackTrace();

  }

}

```


Metadata Types Picklist (Including Dependent Picklist)

Declarative Metadata Sample Definition

The following sample shows usage for picklists, including dependent picklists, in a custom object. The `isAmerican__c` checkbox
controls the list of manufacturers shown in the `manufacturer__c` picklist. The `manufacturer__c` checkbox in turn controls
the list of models shown in the `model__c` picklist.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

      <deploymentStatus>Deployed</deploymentStatus>

      <enableActivities>true</enableActivities>

      <fields>

        <fullName>isAmerican__c</fullName>

        <defaultValue>false</defaultValue>

        <label>American Only</label>

        <type>Checkbox</type>

      </fields>

      <fields>

        <fullName>manufacturer__c</fullName>

        <label>Manufacturer</label>

        <picklist>

           <controllingField>isAmerican__c</controllingField>

           <picklistValues>

             <fullName>Chrysler</fullName>

             <controllingFieldValues>checked</controllingFieldValues>

             <default>false</default>

           </picklistValues>

           <picklistValues>

             <fullName>Ford</fullName>

             <controllingFieldValues>checked</controllingFieldValues>

             <default>false</default>

           </picklistValues>

           <picklistValues>

             <fullName>Honda</fullName>

             <controllingFieldValues>unchecked</controllingFieldValues>

             <default>false</default>

           </picklistValues>

           <picklistValues>

             <fullName>Toyota</fullName>

             <controllingFieldValues>unchecked</controllingFieldValues>

             <default>false</default>

           </picklistValues>

           <sorted>false</sorted>

        </picklist>

        <type>Picklist</type>

      </fields>

      <fields>

        <fullName>model__c</fullName>

        <label>Model</label>

        <picklist>

           <controllingField>manufacturer__c</controllingField>

           <picklistValues>

             <fullName>Mustang</fullName>

             <controllingFieldValues>Ford</controllingFieldValues>

             <default>false</default>

           </picklistValues>

```


Metadata Types Picklist (Including Dependent Picklist)

```
           <picklistValues>

             <fullName>Taurus</fullName>

             <controllingFieldValues>Ford</controllingFieldValues>

             <default>false</default>

           </picklistValues>

           <picklistValues>

             <fullName>PT Cruiser</fullName>

             <controllingFieldValues>Chrysler</controllingFieldValues>

             <default>false</default>

           </picklistValues>

           <picklistValues>

             <fullName>Pacifica</fullName>

             <controllingFieldValues>Chrysler</controllingFieldValues>

             <default>false</default>

           </picklistValues>

           <picklistValues>

             <fullName>Accord</fullName>

             <controllingFieldValues>Honda</controllingFieldValues>

             <default>false</default>

           </picklistValues>

           <picklistValues>

             <fullName>Civic</fullName>

             <controllingFieldValues>Honda</controllingFieldValues>

             <default>false</default>

           </picklistValues>

           <picklistValues>

             <fullName>Prius</fullName>

             <controllingFieldValues>Toyota</controllingFieldValues>

             <default>false</default>

           </picklistValues>

           <picklistValues>

             <fullName>Camry</fullName>

             <controllingFieldValues>Toyota</controllingFieldValues>

             <default>false</default>

           </picklistValues>

           <sorted>false</sorted>

        </picklist>

        <type>Picklist</type>

      </fields>

   ....

   </CustomObject>

```

The following sample shows usage for the standard `Stage` field in opportunities.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

      <fields>

        <fullName>StageName</fullName>

        <picklist>

           <picklistValues>

             <fullName>Prospecting</fullName>

             <default>false</default>

             <forecastCategory>Pipeline</forecastCategory>

             <probability>10</probability>

           </picklistValues>

```


#### Metadata Types ProfileSearchLayouts

```
           <picklistValues>

             <fullName>Qualification</fullName>

             <default>false</default>

             <forecastCategory>Pipeline</forecastCategory>

             <probability>10</probability>

           </picklistValues>

           <picklistValues>

             <fullName>Needs Analysis</fullName>

             <default>false</default>

             <forecastCategory>Pipeline</forecastCategory>

             <probability>20</probability>

           </picklistValues>

           ...

        </picklist>

      </fields>

   <CustomObject>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### ProfileSearchLayouts Represents a user profile’s search results layouts for an object. ProfileSearchLayouts are similar to SearchLayouts .

However, with profile-specific layouts, each user profile can have a different search results layout for an object.

File Suffix and Directory Location

Profile search layouts are defined as part of a standard or custom object. `SearchLayout` is the default search results layout used
when no layout is specified for a user profile. For more information, see CustomObject.

Version

Profile search layouts for custom objects are available in API version 48.0 and later.

Fields

**Field** **Field Type** **Description**

`profileName` string[]

The name of the profile associated with a customized search
results layout. The profile name can be a standard Salesforce
profile or custom profile defined in your org.

`fields` string[] The list of fields displayed in search results for the object and
for the users that have the profile _`Profile Name`_ . The

`name` field is required and is always displayed as the first
column header, so it isn’t included in this list. All additional
fields are included. The field name relative to the object


#### Metadata Types RecordType

**Field** **Field Type** **Description**

name, for _`exampleMyCustomField__c`_, is specified
for each custom field.

Declarative Metadata Sample Definition

The following shows a sample definition of profile-specific search layouts in an object.

Note: To deploy a profile-specific search results layout, the profile must be defined in the destination org and if it's for a custom
object, you must enable search for that custom object. If the profile-specific search results layout is for a custom object, the custom
object's tab must exist in the destination org or must be included with the deployment.

```
   <?xml version="1.0" encoding="UTF-8"?>

             <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

             . . .

             <profileSearchLayouts>

             <fields>ACCOUNT.NAME</fields>

             <fields>ACCOUNT.SITE</fields>

             <fields>ACCOUNT.PHONE1</fields>

             <fields>CORE.USERS.ALIAS</fields>

             <fields>ACCOUNT.ADDRESS2_CITY</fields>

             <profileName>System Administrator</profileName>

             </profileSearchLayouts>

             <profileSearchLayouts>

             <fields>ACCOUNT.NAME</fields>

             <fields>ACCOUNT.SITE</fields>

             <profileName>WDC Only User</profileName>

             </profileSearchLayouts>

             . . .

             </CustomObject>

```

SEE ALSO:

SearchLayouts

#### RecordType

Represents the metadata associated with a record type. Record types let you offer different business processes, picklist values, and page
layouts to different users. Use this metadata type to create, update, or delete record type definitions for a custom object.

For more information, see _Tailor Busines Processes to Different Record Types Users_ in Salesforce Help. This type extends the Metadata
metadata type and inherits its `fullName` field.

Important: Don’t use record types as an access control mechanism. Profile assignment governs create and edit access for an
object but doesn’t govern read access. For example, a user assigned to a profile that isn't enabled for a particular record type can't
create records with that record type, but can access records associated with that record type.

Users with access to an object can read all record type information for that object. We strongly recommend against storing sensitive
information in the record type description, name, or label. Instead, store sensitive information in a separate object or fields to which
you’ve applied appropriate access controls.


Metadata Types RecordType

Note: Retrieving a component of this metadata type in a project makes the component appear in any Profile and PermissionSet
components that are retrieved in the same package.

Note: Metadata API doesn’t retrieve custom picklist values on person account record types, if the picklist exists on a contact. In
this case, Metadata API retrieves standard picklist values only.

Note: Metadata API doesn't retrieve specific picklist fields that are associated with a record type.

Version

Record types are available in API version 12.0 and later.

Fields

**Field** **Field Type** **Description**

`active` boolean Required. Indicates whether the record type is active.

`businessProcess` string The `fullName` of the business process associated with
the record type. This field is required in record types for lead,

opportunity, solution, and case, and not allowed otherwise.
See BusinessProcess on page 758.

This field is available in API version 17.0 and later.

`compactLayoutAssignment` string

Represents the compact layout that is assigned to the record
type.

This field is available in API version 29.0 and later.

`description` string Record type description. Maximum of 255 characters.

`fullName` string Record type name. The `fullName` can contain only
underscores and alphanumeric characters. It must be unique,

begin with a letter, not include spaces, not end with an
underscore, and not contain two consecutive underscores.
If this field contained characters before version 14.0 that are
no longer allowed, the characters were stripped out of this
field, and the previous value of the field was saved in the
`label` field.

Inherited from the Metadata component, this field isn’t
defined in the WSDL for this component. It must be specified
when creating, updating, or deleting. See create() to see an
example of this field specified for a call.

This value can't be `null` .

`label` string Required. Descriptive label for the record type. The list of
characters allowed in the `fullName` field has been reduced

for versions 14.0 and later. This field contains the value
contained in the `fullName` field before version 14.0.


Metadata Types RecordType

**Field** **Field Type** **Description**

`picklistValues` RecordTypePicklistValue[] Represents a set of values for a picklist.

RecordTypePicklistValue

RecordTypePicklistValue represents the combination of picklists and valid values that define a record type:

**Field Name** **Field Type** **Description**

`picklist` string Required. The name of the picklist.

`values` PicklistValue One or more of the picklist values in the picklist. Each value defined is
available in the record type that contains this component.

Java Sample

The following sample uses two record types. For the complete sample that includes profiles and picklists, see Profile on page 1716.

```
   public void recordTypeSample() {

     try {

      // Employees and managers have different access

      // to the state of the expense sheet

      RecordType edit = new RecordType();

      edit.setFullName("ExpenseReport__c.Edit");

      edit.setLabel("ExpenseReport__c.Label");

      PicklistValue unsubmitted = new PicklistValue();

      unsubmitted.setFullName("Unsubmitted");

      PicklistValue submitted = new PicklistValue();

      submitted.setFullName("Submitted");

      RecordTypePicklistValue editStatuses =

        new RecordTypePicklistValue();

      editStatuses.setPicklist("ExpenseStatus__c");

      editStatuses.setValues(

        new PicklistValue[] {unsubmitted, submitted});

      edit.setPicklistValues(

        new RecordTypePicklistValue[] {editStatuses});

      AsyncResult[] arsEdit =

        metadataConnection.create(new Metadata[] {edit});

      RecordType approve = new RecordType();

      approve.setFullName("ExpenseReport__c.Approve");

      PicklistValue approved = new PicklistValue();

      approved.setFullName("Approved");

      PicklistValue rejected = new PicklistValue();

      rejected.setFullName("Rejected");

      RecordTypePicklistValue approveStatuses =

        new RecordTypePicklistValue();

      approveStatuses.setPicklist("ExpenseStatus__c");

      approveStatuses.setValues(

        new PicklistValue[] {approved, rejected});

      approve.setPicklistValues(

```


#### Metadata Types SearchLayouts

```
        new RecordTypePicklistValue[] {approveStatuses});

      AsyncResult[] arsApprove =

       metadataConnection.create(new Metadata[] {approve});

     } catch (ConnectionException ce) {

      ce.printStackTrace();

     }

   }

```

Declarative Metadata Sample Definition

The definition of a record type in a custom object is shown in this code block.

```
   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

   . . .

     <recordTypes>

        <fullName>My First Recordtype</fullName>

      </recordTypes>

    . . .

   </CustomObject>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### SearchLayouts

Represents the metadata associated with the search layouts for an object. You can customize which fields to display for users in search
results, search filter fields, lookup dialogs, and recent record lists on tab home pages. You can access SearchLayouts only by accessing
its encompassing CustomObject.

[For more information, see Customize Layouts for Search Results and Customize Search Layouts for Custom Objects in Salesforce Help.](https://help.salesforce.com/articleView?id=ai.customizing_search_layouts.htm&type=5&language=en_US)

Version

Search layouts for custom objects are available in API version 14.0 and later. The ability to modify search layouts for standard objects
(except events and tasks) is available in API version 27.0 and later.

Fields

When defining metadata for search layouts:

**•** Any Name field defined as a text type is mandatory; it’s always displayed as the first column in the search results page. When you
query for a list of fields; the name field isn’t returned but all other fields are. If you define the Name field as an autonumber type, it’s
not mandatory and you can remove it from the list, but when you import the search layout with Metadata API, it will always add the
Name field back. These rules apply to `customTabListAdditionalFields`, `lookupDialogsAdditionalFields`,
`lookupPhoneDialogsAdditionalFields`, and `searchResultsAdditionalFields`

**•** For custom objects, the search layout uses the API name, for example, MyCustomField__c instead of the field name My Custom
Field.


Metadata Types SearchLayouts

**Field** **Field Type** **Description**

`customTabListAdditionalFields` string[] The list of fields displayed in the Recent _`Object Name`_
list view for an object.

`excludedStandardButtons` string[] The list of standard buttons excluded from the search layout.

`listViewButtons` string[]

`lookupDialogsAdditionalFields` string[]

`lookupFilterFields` string[]

`lookupPhoneDialogsAdditionalFields` string[]

`massQuickActions` string[]

The list of buttons available in list views for an object.

This field is equivalent to the Buttons Displayed value in the
_`Object Name`_ `List View` in the related list of the
object detail page in the UI.

The list of fields displayed in a lookup dialog for the object.

Salesforce objects often include one or more _lookup fields_
that allow users to associate two records together in a

relationship. For example, a contact record includes an
`Account` lookup field that represents the relationship
between the contact and the organization with which the
contact is associated. A lookup search dialog helps you search
for the record associated with the one being edited. Lookup
filter fields allow you to filter your lookup search by a
customized list of fields in the object.

This field is equivalent to the `Lookup Dialogs` related
list on the object detail page in the UI.

The list of fields that can be used to filter enhanced lookups
for an object. Enhanced lookups are optionally enabled by
your administrator.

This field is equivalent to the `Lookup Filter Fields`
related list on the object detail page in the application user
interface.

The list of phone-related fields displayed in a lookup dialog
for the object.

This list enables integration of the fields with a softphone
dial pad.

This field is equivalent to the `Lookup Phone Dialogs`
related list on the object detail page in the application user
interface.

The list of actions that you can use to perform mass quick
action on records. Use this field to add an existing create or
update action.

You can perform mass quick actions on custom objects and
all standard objects that support quick actions and have a

search layout in Lightning Experience. This includes but isn’t
limited to cases, leads, accounts, campaigns, contacts,
opportunities, and work orders.


Metadata Types SearchLayouts

**Field** **Field Type** **Description**

`searchFilterFields` string[]

`searchResultsAdditionalFields` string[]

`searchResultsCustomButtons` string[]

Declarative Metadata Sample Definition

A sample definition of object’s search layout is shown..

```
<?xml version="1.0" encoding="UTF-8"?>

```

The list of fields that can be used to filter a search for the
object.

This field is equivalent to the `Search Filter Fields`
related list on the object detail page in the application user
interface.

The list of fields displayed in a search result for the object.

This field is equivalent to the `Search Results` related
list on the object detail page in the application user interface.

The list of custom buttons available in a search result for the
object. The actions associated with the buttons can be
applied to any of the records returned in the search result.

```
          <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

          . . .

          <searchLayouts>

          <listViewButtons>New</listViewButtons>

          <listViewButtons>Accept</listViewButtons>

          <listViewButtons>ChangeOwner</listViewButtons>

         <lookupDialogsAdditionalFields>firstQuote__c</lookupDialogsAdditionalFields>

         <lookupDialogsAdditionalFields>finalQuote__c</lookupDialogsAdditionalFields>

          <massQuickActions>Create_MQA_Contact</massQuickActions>

         <searchResultsAdditionalFields>CREATEDBY_USER</searchResultsAdditionalFields>

          </searchLayouts>

          . . .

          </CustomObject>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

CustomObject

ProfileSearchLayouts


#### Metadata Types SharingReason SharingReason

Represents an Apex sharing reason, which is used to indicate why sharing was implemented for a custom object. Apex managed sharing
allows developers to use Apex to programmatically share custom objects. When you use Apex managed sharing to share a custom
object, only users with the “Modify All Data” permission can add or change the sharing on the custom object's record, and the sharing
access is maintained across record owner changes.

Use SharingReason to create, update, or delete sharing reason definitions for a custom object. This type extends the Metadata metadata
type and inherits its `fullName` field.

Version

Sharing reasons are available in API version 14.0 and later.

Fields

**Field** **Field Type** **Description**

`fullName` string

Required. Sharing reason name. The __c suffix is appended to custom
sharing reasons.

Inherited from Metadata, this field is defined in the WSDL for this
metadata type. It must be specified when creating, updating, or deleting.

See `createMetadata()` to see an example of this field specified for
a call.

`label` string Required. Descriptive label for the sharing reason. Maximum of 40
characters.

Declarative Metadata Sample Definition

The definition of a sharing reason in a custom object:

```
<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

. . .

   <sharingReasons>

     <fullName>recruiter__c</fullName>

     <label>Recruiter</label>

   </sharingReasons>

 . . .

</CustomObject>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.


#### Metadata Types SharingRecalculation SharingRecalculation

Represents Apex classes that recalculate the Apex managed sharing for a specific custom object.

Version

Sharing recalculations are available in API version 14.0 and later.

Fields

**Field** **Field Type** **Description**

`className` string

Required. The Apex class that recalculates the Apex sharing for a custom
object. This class must implement the `Database.Batchable`
interface.

Declarative Metadata Sample Definition

The definition of a sharing recalculation in a custom object:

```
<CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

. . .

   <sharingRecalculations>

     <className>RecruiterRecalculation</className>

   </sharingRecalculations>

 . . .

</CustomObject>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### ValidationRule

Represents a validation rule, which is used to verify that the data a user enters in a record is valid and can be saved. A validation rule
contains a formula or expression that evaluates the data in one or more fields and returns a value of `true` or `false` . Validation rules
also include an error message that your client application can display to the user when the rule returns a value of `true` due to invalid
data.

This type extends the Metadata metadata type and inherits its `fullName` field.

As of API version 20.0, validation rules can't have compound fields. Examples of compound fields include addresses, first and last names,
dependent picklists, and dependent lookups.

As of API version 40.0, you can use validation rules with custom metadata types.


Metadata Types ValidationRule

Version

Validation rules are available in API version 12.0 and later.

Fields

**Field Name** **Field Type** **Description**

`active` boolean Required. Indicates whether this validation rule is active, ( `true` ), or not
active ( `false` ).

`description` string A description of the validation rule.

`errorConditionFormula` string Required. The formula defined in the validation rule. If the formula returns
a value of `true`, an error message is displayed.

`errorDisplayField` string The fully specified name of a field in the application. If a value is supplied,
the error message appears next to the specified field. If you do not specify

a value or the field isn’t visible on the page layout, the value changes
automatically to `Top of Page` .

`errorMessage` string Required. The message that appears if the validation rule fails. The
message must be 255 characters or less.

`fullName` string The internal name of the object. White spaces and special characters are
escaped for validity. The name must:

**•** Contain characters, letters, or the underscore (_) character

**•** Must start with a letter

**•** Can’t end with an underscore

**•** Can't contain two consecutive underscore characters.

Inherited from the Metadata component, this field isn’t defined in the
WSDL for this component. It must be specified when creating, updating,
or deleting. See create() to see an example of this field specified for a call.

Declarative Metadata Sample Definition

A sample XML definition of a validation rule in a custom object is shown in this code block.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

      <deploymentStatus>Deployed</deploymentStatus>

      <fields>

        <fullName>Mommy_Cat__c</fullName>

        <label>Mommy Cat</label>

        <referenceTo>Cat__c</referenceTo>

        <relationshipName>Cats</relationshipName>

        <type>Lookup</type>

      </fields>

      <label>Cat</label>

      <nameField>

```


#### Metadata Types WebLink

```
        <label>Cat Name</label>

        <type>Text</type>

      </nameField>

      <pluralLabel>Cats</pluralLabel>

      <sharingModel>ReadWrite</sharingModel>

      <validationRules>

        <fullName>CatsRule</fullName>

        <active>true</active>

        <errorConditionFormula>OR(Name = &apos;Milo&apos;,Name =

   &apos;Moop&apos;)</errorConditionFormula>

        <validationMessage>Name must be that of one of my cats</validationMessage>

      </validationRules>

   </CustomObject>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### WebLink

Represents a custom button or link defined in a custom object.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

This type extends the Metadata metadata type and inherits its `fullName` field.

Version

#### WebLinks are available in API version 12.0 and later.

Fields

**Field Name** **Field Type** **Description**

#### availability WebLinkAvailability Required. Indicates whether the button or link is only available online

(enumeration of type string) ( `online`, or if it is also available offline ( `offline` ).

`description` string A description of the button or link.

#### displayType WebLinkDisplayType Represents how the button or link is rendered. Valid values are:

(enumeration of type string)

**•** `link` for a hyperlink

**•** `button` for a button

**•** `massActionButton` for a button attached to a related list

`encodingKey` Encoding

Required. The default encoding setting is Unicode: `UTF-8` . Change it
if your template requires data in a different format. This is available if
your content source is URL.

Valid values include:


Metadata Types WebLink

**Field Name** **Field Type** **Description**

**•** `UTF-8` —Unicode (UTF-8)

**•** `ISO-8859-1` —General US & Western Europe (ISO-8859–1,
ISO-LATIN-1)

**•** `Shift_JIS` —Japanese (Shift-JIS)

**•** `ISO-2022-JP` —Japanese (JIS)

**•** `EUC-JP` —Japanese (EUC-JP)

**•** `x-SJIS_0213` —Japanese (Shift-JIS_2004)

**•** `ks_c_5601-1987` —Korean (ks_c_5601-1987)

**•** `Big5` —Traditional Chinese (Big5)

**•** `GB2312` —Simplified Chinese (GB2312)

**•** `Big5-HKSCS` —Traditional Chinese Hong Kong (Big5–HKSCS)

`fullName` string The name of the custom button or link with white spaces and special
characters escaped for validity. The name can only contain characters,

letters, and the underscore (_) character. The name must start with a
letter, and can’t end with an underscore or contain two consecutive
underscore characters.

Inherited from the Metadata component, this field isn’t defined in the
WSDL for this component. It must be specified when creating, updating,
or deleting. See create() to see an example of this field specified for a
call.

`hasMenubar` boolean

`hasScrollbars` boolean

`hasToolbar` boolean

`height` int

`isResizable` boolean

`linkType` WebLinkType (enumeration of
type string)

If the `openType` is `newWindow`, this field indicates whether to show
the browser menu bar for the window ( `true` ) or not ( `false` ).
Otherwise, leave this field empty.

If the `openType` is `newWindow`, this field indicates whether to show
the scroll bars for the window ( `true` ) or not ( `false` ). Otherwise, leave
this field empty.

If the `openType` is `newWindow`, this field indicates whether to show
the browser toolbar for the window ( `true` ) or not ( `false` ). Otherwise,
leave this field empty.

Height in pixels of the window opened by the custom button or link.
Required if the `openType` is `newWindow` . Otherwise, leave this field
empty.

If the `openType` is `newWindow`, this field indicates whether to allow
resizing of the window ( `true` ) or not ( `false` ). Otherwise, leave this
field empty.

Required. Represents whether the content of the button or link is
specified by a URL, an sControl, a JavaScript code block, or a Visualforce
page.

**•** `url`


Metadata Types WebLink

**Field Name** **Field Type** **Description**

**•** `sControl`

**•** `javascript`

**•** `page`

**•** `flow` —Reserved for future use.

`masterLabel` string Master label for this object. This display value is the internal label that is
not translated.

`openType` WebLinkWindowType Required. When the button or link is clicked, specifies the window style
(enumeration of type string) that will be used to display the content. Valid values:

**•** `newWindow`

**•** `sidebar`

**•** `noSidebar`

**•** `replace`

**•** `onClickJavaScript`

`page` string If the value of `linkType` is `page`, this field represents the Visualforce
page. Otherwise, leave this field empty.

`position` WebLinkPosition (enumeration
of type string)

If the value of `OpenType` is `newWindow`, this field indicates how
the new window should be displayed. Otherwise, don’t specify a value.
Valid values are:

**•** `fullScreen`

**•** `none`

**•** `topLeft`

`protected` boolean Required. Indicates whether this subcomponent is protected ( `true` )
or not ( `false` ). Protected subcomponents can’t be linked to or

referenced by components or subcomponents created in the installing
organization.

`requireRowSelection` boolean

If the `displayType` is `massActionButton`, this field indicates
whether to require individual row selection to execute the action for
this button ( `true` ) or not ( `false` ). Otherwise, leave this field empty.

`scontrol` string If the value of `linkType` is `sControl`, this field represents the name
of the sControl. Otherwise, leave this field empty.

`showsLocation` boolean

If the `openType` is `newWindow`, this field indicates whether to show
the browser location bar for the window ( `true` ) or not ( `false` ).
Otherwise, leave this field empty.

`showsStatus` boolean If the `openType` is `newWindow`, this field indicates whether to show
the browser status bar for the window. Otherwise, leave this field empty.


Metadata Types WebLink

**Field Name** **Field Type** **Description**

`url` string

`width` int

Java Sample

If the value of `linkType` is `url`, this is the URL value. If the value of
`linkType` is `javascript`, this is the JavaScript content. If the value
is neither of these options, leave this field empty.

Content must be escaped in a manner consistent with XML parsing
rules.

Width in pixels of the window opened by the button or link.

Required if the `openType` is `newWindow` . Otherwise, leave this field
empty.

The following Java sample shows sample values for WebLink fields:

```
public void WebLinkSample(String name) throws Exception {

   WebLink WebLink = new WebLink();

   // name variable represents the full name of the object

   // on which to create the WebLink, for example, customObject__c

   WebLink.setFullName(name + ".googleButton");

   WebLink.setUrl("http://www.google.com");

   WebLink.setAvailability(WebLinkAvailability.online);

   WebLink.setLinkType(WebLinkType.url);

   WebLink.setEncodingKey(Encoding.fromString("UTF-8"));

   WebLink.setOpenType(WebLinkWindowType.newWindow);

   WebLink.setHeight(600);

   WebLink.setWidth(600);

   WebLink.setShowsLocation(false);

   WebLink.setHasScrollbars(true);

   WebLink.setHasToolbar(false);

   WebLink.setHasMenubar(false);

   WebLink.setShowsStatus(false);

   WebLink.setIsResizable(true);

   WebLink.setPosition(WebLinkPosition.none);

   WebLink.setMasterLabel("google");

   WebLink.setDisplayType(WebLinkDisplayType.link);

   AsyncResult[] asyncResults = metadataConnection.create(new WebLink[]{WebLink});

   // After the create() call completes, we must poll the results of checkStatus()

   //

}

```


#### Metadata Types Metadata Field Types

Declarative Metadata Sample Definition

The following is the definition of a WebLink in a custom object. For related samples, see Declarative Metadata Sample Definition and
Declarative Metadata Sample Definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomObject xmlns="http://soap.sforce.com/2006/04/metadata">

   ....

      <WebLinks>

        <fullName>googleButton</fullName>

        <availability>online</availability>

        <displayType>link</displayType>

        <encodingKey>UTF-8</encodingKey>

        <hasMenubar>false</hasMenubar>

        <hasScrollbars>true</hasScrollbars>

        <hasToolbar>false</hasToolbar>

        <height>600</height>

        <isResizable>true</isResizable>

        <linkType>url</linkType>

        <masterLabel>google</masterLabel>

        <openType>newWindow</openType>

        <position>none</position>

        <protected>false</protected>

        <showsLocation>false</showsLocation>

        <showsStatus>false</showsStatus>

        <url>http://www.google.com</url>

        <width>600</width>

      </WebLinks>

   ....

   </CustomObject>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

HomePageComponent

HomePageLayout

CustomPageWebLink

#### Metadata Field Types

These field types extend the field types described in the _Salesforce Object Reference_ .

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.


Metadata Types Metadata Field Types

**Field Type** **Objects** **What the Field Contains**

CustomField

Custom object Represents a custom field.

Custom field

DeleteConstraint Custom field A string that represents deletion options for lookup relationships. Valid values
are:

**•** `SetNull`

**•** `Restrict`

**•** `Cascade`

DeploymentStatus

Custom object

Custom field

A string that represents the deployment status of a custom object or field. Valid
values are:

**•** `InDevelopment`

**•** `Deployed`

FieldType Custom field Indicates the type of a custom field. Valid values are:

**•** `Address`

**•** `AutoNumber`

**•** `Lookup`

**•** `MasterDetail`

**•** `MetadataRelationship`

**•** `Checkbox`

**•** `Currency`

**•** `Date`

**•** `DateTime`

**•** `Email`

**•** `EncryptedText`

Note: This page is about Classic Encryption, not Shield Platform
[Encryption. What's the difference?](https://help.salesforce.com/s/articleView?id=xcloud.security_pe_vs_classic_encryption.htm&type=5&language=en_US)

**•** `ExternalLookup`

**•** `IndirectLookup`

**•** `Number` [1]

**•** `Percent`

**•** `Phone`

**•** `Picklist`

**•** `MultiselectPicklist`

**•** `Summary`

**•** `Text`

**•** `TextArea`

**•** `LongTextArea`


Metadata Types Metadata Field Types

**Field Type** **Objects** **What the Field Contains**

**•** `Url`

**•** `Hierarchy`

**•** `File`

**•** `Html`

**•** `Location` (use for geolocation fields)

**•** `Time`

**•** `Array`

**•** `Integer`

**•** `Long`

A `Number` custom field, internally represented as a field of type double. Setting
the scale of the `Number` field to 0 gives you a double that behaves like an int.

Gender Custom object

Picklist (Including Dependent Custom field
Picklist)

Indicates the gender of the noun that represents the object. Used for languages
where words need different treatment depending on their gender. Valid values
are:

**•** `Masculine`

**•** `Feminine`

**•** `Neuter`

**•** `AnimateMasculine` (Slavic languages—currently Czech, Polish, Russian,
Slovak, Slovenian, and Ukrainian)

**•** `ClassI`, `ClassIII`, `ClassV`, `ClassVII`, `ClassIX`, `ClassXI`,
`ClassXIV`, `ClassXV`, `ClassXVI`, `ClassXVII`, `ClassXVIII`
(African languages—currently Afrikaans, Xhosa, and Zulu)

Note: The following genders appear on the Rename Tabs and Labels
page in Setup but are stored internally as “Feminine”. When setting them
through the Metadata API, use “Feminine”.

**•** `Euter (Swedish)`

**•** `Common (Dutch)`

(This field type isn’t used in Metadata API. CustomField includes this field type for
Tooling API support). Represents a picklist, a set of labels and values that can be
selected from a picklist.

SharingModel Custom object Represents the sharing model for the custom object. Depending on the object,
valid values are:

**•** `Private`

**•** `Read`

**•** `ReadWrite`

**•** `ReadWriteTransfer`

**•** `FullAccess`

**•** `ControlledByParent`


Metadata Types Metadata Field Types

**Field Type** **Objects** **What the Field Contains**

**•** `ControlledByCampaign`

**•** `ControlledByLeadOrContact`

For example, the User object supports `Private` and `Read` values. Accounts,
opportunities, and custom objects support `Private`, `Read` and `ReadWrite`
values. Campaign members support `ControlledByCampaign` and
`ControlledByLeadOrContact` .

StartsWith

Custom object

Custom field

Indicates whether the noun starts with a vowel, consonant, or is a special character.
This is used for languages where words need different treatment depending on
the first character. Valid values are:

**•** `Consonant`

**•** `Vowel`

**•** `Special (for nouns starting with z, or s plus`

```
  consonants)

```

TreatBlanksAs Custom field Indicates how blanks should be treated. Valid values are:

**•** `BlankAsBlank`

**•** `BlankAsZero`

ValueSet Custom field Represents a set of values that can be selected from a custom picklist field. Defines
the valueSet of a custom picklist field.

ValueSet

Represents a set of values that can be selected from a custom picklist field. Defines the valueSet of a custom picklist field.

**Field Type** **Field Type** **Description**

`controllingField` string

The `fullname` of the controlling field if this is a dependent picklist. A
controlling field can be a checkbox or picklist field, but in this case it’s a picklist.
The controlling picklist filters the available values in the dependent picklist.

`restricted` boolean Whether the picklist’s values are limited to only the values defined by a
Salesforce admin. Values are `true` or `false` .

`valueSetDefinition` ValueSetValuesDefinition Defines value-specific settings for a custom dependent picklist. Indicates
whether the value set of the custom picklist field is sorted alphabetically.

`valueSetName` string The `masterLabel` of the global value set to be used for this picklist field.

`valueSettings` ValueSettings Used for the settings that describe a value in a custom picklist field. The picklist
can have its own unique value set, or inherit the values from a global value

set. You can add field dependency values via the Metadata API but not remove
them.


### Metadata Types CustomObjectTranslation

ValueSetValuesDefinition

**Field Name** **Field Type** **Description**

`sorted` boolean Whether the picklist’s value set is displayed in alphabetical order in the user
interface.

`value` CustomValue Required. The list of values for this local, custom picklist.

ValueSettings

**Field Name** **Field Type** **Description**

`controllingFieldValue` stringstring[]

Applies only to dependent custom picklists. A list of values in the controlling
or parent picklist (that the custom picklist values depend on). You can add field
dependency values via the Metadata API but not remove them.

`valueName` string Defines the values in the custom dependent picklist.

### CustomObjectTranslation

This metadata type allows you to translate custom objects for a variety of languages.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

This type extends the Metadata metadata type and inherits its `fullName` field. The ability to translate component labels is part of the
Translation Workbench.

Declarative Metadata File Suffix and Directory Location

Local translations are stored in a file with a format of _`customObjectName__c`_ `-` _`lang`_ `.objectTranslation`, where
_`customObjectName__c`_ is the custom object name, and _`lang`_ is the translation language. A sample file name for German
translations is `myCustomObject__c-de.objectTranslation` .

Similarly, packaged translations are stored in a file with a format of
_`customObjectName-pkgNamespace__c`_ `-` _`lang`_ `.objectTranslation`, where
_`customObjectName-pkgNamespace__c`_ is the custom object and package namespace, and _`lang`_ is the translation language.
A sample file name for German translations in a package with the namespace of Acme is
`myCustomObject-Acme__c-de.objectTranslation` . Custom object translations are stored in the objectTranslations
folder in the corresponding package directory.

Custom object translations are stored in the `objectTranslations` folder in the corresponding package directory.

Version

### CustomObjectTranslation components are available in API version 14.0 and later.


Metadata Types CustomObjectTranslation

Fields

**Field** **Field Type** **Description**

`caseValues` ObjectNameCaseValue[] Different combinations of the custom object with regard to
article, plural, possessive, and case.

`fields` CustomFieldTranslation[] A list of translations for the custom fields associated with the
custom object.

`fieldSets` FieldSetTranslation[] A list of field set translations. Available in API version 41.0 and
later.

`fullName` string The name of the custom object and the translation language
with a format of _`customObjectName`_                                         - _`lang`_, where

_`customObjectName`_ is the custom object name, and _`lang`_
is the translation language.

Inherited from Metadata, this field is defined in the WSDL for
this metadata type. It must be specified when creating, updating,
or deleting. See `createMetadata()` to see an example of
this field specified for a call.

`gender` Gender

Indicates the gender of the noun that represents the object.
Used for languages where words need different treatment
depending on their gender.

`layouts` LayoutTranslation[] A list of page layout translations.

`nameFieldLabel` string The label for the name field. Maximum of 80 characters.

`namedFilters` NamedFilterTranslation[]

A list of translations for lookup filter error messages associated
with the custom object.

This field has been removed as of API version 30.0 and is only
available in prior versions. The translation metadata associated

with a lookup filter is now represented by the `lookupFilter`
field in the CustomFieldTranslation on page 812 subtype.

`quickActions` QuickActionTranslation[] A list of translations for actions.

`recordTypes` RecordTypeTranslation[] A list of record type translations.

`sharingReasons` SharingReasonTranslation[] A list of sharing reason translations.

`startsWith` StartsWith (enumeration of type
string)

Indicates whether the noun starts with a vowel, consonant, or
is a special character. This is used for languages where words
need different treatment depending on the first character.

`validationRules` ValidationRuleTranslation[] A list of validation rule translations.

`webLinks` WebLinkTranslation[] A list of web link translations.

`workflowTasks` WorkflowTaskTranslation[] A list of workflow task translations.


Metadata Types CustomObjectTranslation

Note: When you retrieve or deploy translations from a package, the translations from the package might override existing
translations. The overridden translations appear in the Rename Tabs and Labels UI until you click **Reset** to restore the translations
installed by the latest package.

CustomFieldTranslation

CustomFieldTranslation contains details for a custom field translation. In API versions 37.0 and earlier standard picklist values could be
translated with CustomFieldTranslation. In API version 38.0, use StandardValueSetTranslation instead. For more details, see CustomField.

Note: Not every language supports all the possible values for the fields in CustomFieldTranslation. For language-specific supported
values, see the fully supported languages and end-user languages appendices.

**Field** **Field Type** **Description**

`caseValues` ObjectNameCaseValue[]

Different combinations of the custom object with regard to
article, plural, possessive, and case. Available in API version 29.0
and later.

`description` string Translation for the custom field description.

`gender` Gender Available in API version 29.0 and later.

`help` string Translation for the text that displays in the field-level help hover
text for this field.

`label` string Translation for the label. Maximum of 40 characters.

`lookupFilter` LookupFilterTranslation

Represents the translation metadata associated with a lookup
filter.

This field is available in API version 30.0 and later.

LookupFilter isn’t supported on the article type object.

`name` string Required. The name of the field relative to the custom object;
for example, `MyField__c` .

`picklistValues` PicklistValueTranslation[]

List of translations for picklist values. See PicklistValue.

Note: “Subject” on the Task object is a text field, not a picklist
value. It can’t be retrieved via Metadata API. Translations can be
provided via the Translation Workbench.

`relationshipLabel` string Translation for a lookup relationship label. A lookup relationship
allows a field to be associated with another field. The relationship

field allows users to select an option from a list of values defined
by the other field. Maximum of 80 characters.

`startsWith` StartsWith (enumeration of type Indicates whether the noun starts with a vowel, consonant, or
string) is a special character. Used for languages where words need

different treatment depending on the first character. Available
in API version 29.0 and later.


Metadata Types CustomObjectTranslation

FieldSetTranslation

FieldSetTranslation contains details for a field set translation. For more details, see FieldSet. Available in API 41.0 and later.

**Field** **Field Type** **Description**

`label` string Required. Translation for the field set label. Maximum of 80
characters.

`name` string Required. The field set name.

LayoutTranslation

LayoutTranslation contains details for a page layout translation. For more details, see Fields.

**Field** **Field Type** **Description**

`layout` string Required. The layout name.

`layoutType` string

`sections` LayoutSectionTranslation[] An array of layout section translations.

LayoutSectionTranslation

LayoutSectionTranslation contains details for a page layout section translation. For more details, see LayoutSection.

**Field** **Field Type** **Description**

`label` string Required. Translation for the label. Maximum of 765 characters.

`section` string Required. The section name.

LookupFilterTranslation

LookupFilterTranslation shows a translation for a lookup filter error message associated with the custom object. Replaces
NamedFilterTranslation.

LookupFilterTranslation is available in API version 30.0 and later.

**Field** **Field Type** **Description**

`errorMessage` string The error message that appears if the lookup filter fails.

`informationalMessage` string

The information message displayed on the page. Use to describe
things some users don't understand, such as why certain items
are excluded in the lookup filter.


Metadata Types CustomObjectTranslation

NamedFilterTranslation

NamedFilterTranslation has been removed as of API version 30.0 and is only available in previous API versions.

NamedFilterTranslation shows a list of translations for lookup filter error messages associated with the custom object. See NamedFilter
for more information.

**Field** **Field Type** **Description**

`errorMessage` string The error message that appears if the lookup filter fails.

`informationalMessage` string

The information message displayed on the page. Use to describe
things the user doesn’t understand, such as why certain items
are excluded in the lookup filter.

`name` string Required. The name of the lookup filter. If you create this field
in the user interface, a name is automatically assigned. If you

create this field through Metadata API, you must include the
`name` field.

ObjectNameCaseValue

ObjectNameCaseValue supports multiple cases and definitions of the custom object name to allow usage in various grammatical contexts.

Note: Not every language supports all the possible values for the fields in ObjectNameCaseValue. For language-specific supported
values, see the fully supported languages and end-user languages appendices.

**Field** **Field Type** **Description**

`article` Article (enumeration of type English has two types of articles: definite ( _`the`_ ) and indefinite
string) ( _`a`_, _`an`_ ). The usage of these articles depends mainly on whether

you're referring to any member of a group, or to a specific
member of a group. The valid values are:

**•** `Definite`

**•** `Indefinite`

**•** `None`

`caseType` CaseType (enumeration of type The case of the custom object name. The valid values are:
string)

**•** `Ablative`

**•** `Accusative`

**•** `Adessive`

**•** `Allative`

**•** `Causalfinal`

**•** `Dative`

**•** `Delative`

**•** `Distributive`

**•** `Elative`

**•** `Essive`


Metadata Types CustomObjectTranslation

**Field** **Field Type** **Description**

**•** `Essiveformal`

**•** `Genitive`

**•** `Illative`

**•** `Inessive`

**•** `Instrumental`

**•** `Lative`

**•** `Locative`

**•** `Nominative`

**•** `Objective`

**•** `Partitive`

**•** `Prepositional`

**•** `Subjective`

**•** `Sublative`

**•** `Superessive`

**•** `Termanative`

**•** `Translative`

**•** `Vocative`

`plural` boolean Indicates whether the `value` field is plural ( `true` ) or singular
( `false` ).

`possessive` Possessive (enumeration of type The possessive case of a language is a grammatical case used
string) to indicate a relationship of possession. The valid values are:

**•** `First`

**•** `None`

**•** `Second`

`value` string Required. The value or label in this grammatical context.

PicklistValueTranslation

PicklistValueTranslation contains details for translation of a picklist value from a local, custom picklist field. For more details, see Picklist
(Including Dependent Picklist).

**Field** **Field Type** **Description**

`masterLabel` string Required. The picklist value defined on the setup page in the
application. Displayed wherever a translated label isn't available.

`translation` string Required. Translation for the value.


Metadata Types CustomObjectTranslation

QuickActionTranslation

QuickActionTranslation contains details for an action label in the user interface. For more information, see QuickAction.

**Field** **Field Type** **Description**

`aspect` string Identifies which quick action label the translated text belongs
to. Use this field only when you want to use different strings for

the quick action's field label and informational message. Valid
values are `Master` and `InfoMessage` . Available in API
version 53.0 and later.

`label` string Required. Translation for the label. Maximum of 765 characters.

`name` string Required. The quick action name.

RecordTypeTranslation

RecordTypeTranslation contains details for a record type name translation. For more details, see RecordType.

**Field** **Field Type** **Description**

`label` string Required. Translation for the label. Maximum of 765 characters.

`name` string Required. The record type name.

`description` string Translation for the record type description. Available in API
version 42.0 and later.

SharingReasonTranslation

SharingReasonTranslation contains details for a sharing reason translation. For more details, see SharingReason.

**Field** **Field Type** **Description**

`label` string Required. Translation for the sharing reason.

`name` string Required. The sharing reason name.

ValidationRuleTranslation

ValidationRuleTranslation contains details for a validation rule translation. For more details, see ValidationRule.

**Field** **Field Type** **Description**

`errorMessage` string Required. Translation for the error message associated with the
validation rule failure.

`name` string Required. The validation rule name.


Metadata Types CustomObjectTranslation

WebLinkTranslation

WebLinkTranslation contains details for a web link translation. For more details, see WebLink.

**Field** **Field Type** **Description**

`label` string Required. Translation for the web link label. Maximum of 765
characters.

`name` string Required. The web link name.

WorkflowTaskTranslation

WorkflowTaskTranslation contains details for a workflow task translation. For more details, see Workflow.

**Field** **Field Type** **Description**

`description` string Translation for the workflow task description.

`name` string Required. The workflow task name.

`subject` string Translation for the workflow task subject.

Declarative Metadata Sample Definitions

This sample XML definition shows a CustomObjectTranslation for the Description__c object in German, with one custom field, Summary__c.
The name and location of the file containing this definition would be
`objectTranslations/Description__c-de.objectTranslation` .

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomObjectTranslation xmlns="http://soap.sforce.com/2006/04/metadata">

      <caseValues>

        <caseType>Nominative</caseType>

        <plural>false</plural>

        <value>Beschreibung</value>

      </caseValues>

      <caseValues>

        <caseType>Nominative</caseType>

        <plural>true</plural>

        <value>Beschreibungen</value>

      </caseValues>

      <caseValues>

        <caseType>Accusative</caseType>

        <plural>false</plural>

        <value>Beschreibung</value>

      </caseValues>

      <caseValues>

        <caseType>Accusative</caseType>

        <plural>true</plural>

        <value>Beschreibungen</value>

      </caseValues>

      <caseValues>

```


Metadata Types CustomObjectTranslation

```
        <caseType>Genitive</caseType>

        <plural>false</plural>

        <value>Beschreibung</value>

      </caseValues>

      <caseValues>

        <caseType>Genitive</caseType>

        <plural>true</plural>

        <value>Beschreibungen</value>

      </caseValues>

      <caseValues>

        <caseType>Dative</caseType>

        <plural>false</plural>

        <value>Beschreibung</value>

      </caseValues>

      <caseValues>

        <caseType>Dative</caseType>

        <plural>true</plural>

        <value>Beschreibungen</value>

      </caseValues>

      <fields>

        <label>Zusammenfassung</label>

        <name>Summary__c</name>

      </fields>

      <gender>Feminine</gender>

      <nameFieldLabel>Beschreibungen</nameFieldLabel>

   </CustomObjectTranslation>

```

This sample XML definition shows a CustomObjectTranslation for the Account object, renaming Account to Client (Kunde) in German.
The Account object has one standard field, account_number, and one custom field, Account_Code__c. The name and location of the
file containing this definition would be `objectTranslations/Account-de.objectTranslation` .

```
   <?xml version="1.0" encoding="UTF-8"?>

   <CustomObjectTranslation xmlns="http://soap.sforce.com/2006/04/metadata">

      <caseValues>

        <caseType>Nominative</caseType>

        <plural>false</plural>

        <value>Kunde</value>

      </caseValues>

      <caseValues>

        <caseType>Nominative</caseType>

        <plural>true</plural>

        <value>Kunden</value>

      </caseValues>

      <caseValues>

        <caseType>Accusative</caseType>

        <plural>false</plural>

        <value>Kunden</value>

      </caseValues>

      <caseValues>

        <caseType>Accusative</caseType>

        <plural>true</plural>

        <value>Kunden</value>

      </caseValues>

      <caseValues>

        <caseType>Genitive</caseType>

```


Metadata Types CustomObjectTranslation

```
        <plural>false</plural>

        <value>Kunden</value>

      </caseValues>

      <caseValues>

        <caseType>Genitive</caseType>

        <plural>true</plural>

        <value>Kunden</value>

      </caseValues>

      <caseValues>

        <caseType>Dative</caseType>

        <plural>false</plural>

        <value>Kunden</value>

      </caseValues>

      <caseValues>

        <caseType>Dative</caseType>

        <plural>true</plural>

        <value>Kunden</value>

      </caseValues>

      <fields>

        <caseValues>

           <caseType>Nominative</caseType>

           <plural>false</plural>

           <value>Kundennummer</value>

        </caseValues>

        <caseValues>

           <caseType>Nominative</caseType>

           <plural>true</plural>

           <value>Kundennummern</value>

        </caseValues>

        <gender>Feminine</gender>

        <name>account_number</name>

      </fields>

      <fields>

        <label>Kunden-Code</label>

        <name>Account_Code__c</name>

      </fields>

      <gender>Masculine</gender>

   </CustomObjectTranslation>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

CustomObject

Translations


### Metadata Types CustomPageWebLink CustomPageWebLink

Represents a custom link defined in a home page component.

This type extends the Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

All other custom links are stored as a WebLink in a CustomObject.

Declarative Metadata File Suffix and Directory Location

There is one file per custom link definition, stored in the `weblinks` folder in the corresponding package directory. The file suffix is
`.weblink` .

Version

### CustomPageWebLinks are available in API version 13.0 and later.

Fields

**Field Name** **Field Type** **Description**

`availability` WebLinkAvailability Required. Indicates whether the link is only available online ( `online`,
(enumeration of type string) or if it is also available offline ( `offline` ).

`description` string A description of the link.

`displayType` WebLinkDisplayType
(enumeration of type string)

`encodingKey` Encoding (enumeration of type
string)

Represents how this link is rendered.

Valid values:

**•** `link` for a hyperlink

**•** `button` for a button

**•** `massActionButton` for a button attached to a related list

Required. The default encoding setting is Unicode: `UTF-8` . Change it if
your template requires data in a different format. This is available if your
content source is URL. Valid values include:

**•** `UTF-8` —Unicode (UTF-8)

**•** `ISO-8859-1` —General US & Western Europe (ISO-8859–1,
ISO-LATIN-1)

**•** `Shift_JIS` —Japanese (Shift-JIS)

**•** `ISO-2022-JP` —Japanese (JIS)

**•** `EUC-JP` —Japanese (EUC-JP)

**•** `x-SJIS_0213` —Japanese (Shift-JIS_2004)

**•** `ks_c_5601-1987` —Korean (ks_c_5601-1987)

**•** `Big5` —Traditional Chinese (Big5)


Metadata Types CustomPageWebLink

**Field Name** **Field Type** **Description**

**•** `GB2312` —Simplified Chinese (GB2312)

**•** `Big5-HKSCS` —Traditional Chinese Hong Kong (Big5–HKSCS)

`fullName` string The name used as a unique identifier for API access. The `fullName`
can contain only underscores and alphanumeric characters. It must be

unique, begin with a letter, not include spaces, not end with an
underscore, and not contain two consecutive underscores.

`hasMenubar` boolean

`hasScrollbars` boolean

`hasToolbar` boolean

If the `openType` is `newWindow`, this field indicates whether to show
the browser menu bar for the window ( `true` or not ( `false` ). Otherwise,
leave this field empty.

If the `openType` is `newWindow`, this field indicates whether to show
the scroll bars for the window ( `true` ) or not ( `false` ). Otherwise, leave
this field empty.

If the `openType` is `newWindow`, this field indicates whether to show
the browser toolbar for the window ( `true` ) or not ( `false` ). Otherwise,
leave this field empty.

`height` int Height in pixels of the window opened by the link. Required if the
`openType` is `newWindow` . Otherwise, leave this field empty.

`isResizable` boolean

If the `openType` is `newWindow`, this field indicates whether to allow
resizing of the window ( `true` ) or not ( `false` ). Otherwise, leave this
field empty.

`linkType` WebLinkType (enumeration of Required. Represents whether the content of the button or link is specified
type string) by a URL, an sControl, a JavaScript code block, or a Visualforce page.

**•** `url`

**•** `sControl`

**•** `javascript`

**•** `page`

**•** `flow` —Reserved for future use.

`masterLabel` string The label for the link.

`openType` WebLinkWindowType
(enumeration of type string)

Required. When the link is clicked, this field specifies the window style
used to display the content.

Valid values are:

**•** `newWindow`

**•** `sidebar`

**•** `noSidebar`

**•** `replace`

**•** `onClickJavaScript`


Metadata Types CustomPageWebLink

**Field Name** **Field Type** **Description**

`page` string If the value of `linkType` is `page`, this field represents the Visualforce
page. Otherwise, leave this field empty.

`position` WebLinkPosition (enumeration
of type string)

`protected` boolean

`requireRowSelection` boolean

If the `openType` is `newWindow`, this field indicates how the new
window should be displayed. Otherwise, leave this field empty.

Valid values are:

**•** `fullScreen`

**•** `none`

**•** `topLeft`

Required. Indicates whether this component is protected ( `true` ) or not
( `false` ). Protected components cannot be linked to or referenced by
components created in the installing organization.

If the `openType` is `massAction`, this field indicates whether to
require individual row selection to execute the action for this button
( `true` ) or not ( `false` ). Otherwise, leave this field empty.

`scontrol` string If the value of `linkType` is `sControl`, this field represents the name
of the sControl. Otherwise, leave this field empty.

`showsLocation` boolean

`showsStatus` boolean

`url` string

`width` int

If the `openType` is `newWindow`, this field indicates whether or not
to show the browser location bar for the window. Otherwise, leave this
field empty.

If the `openType` is `newWindow`, this field indicates whether or not
to show the browser status bar for the window. Otherwise, leave this field
empty.

If the value of `linkType` is `url`, this field represents the URL value. If
the value of `linkType` is `javascript`, this field represents the
JavaScript content. If the value is neither of these, leave this field empty.

Content must be escaped in a manner consistent with XML parsing rules.

Width in pixels of the window opened by the link.

Required if the `openType` is `newWindow` . Otherwise, leave this field
empty.

Declarative Metadata Sample Definition

The following is the definition of a Weblink. For related samples, see HomePageComponent and HomePageLayout.

```
<?xml version="1.0" encoding="UTF-8"?>

<CustomPageWebLink xmlns="http://soap.sforce.com/2006/04/metadata">

   <availability>online</availability>

   <displayType>button</displayType>

   <encodingKey>UTF-8</encodingKey

```


### Metadata Types CustomPermission

```
      <hasMenubar>false</hasMenubar>

      <hasScrollbars>true</hasScrollbars>

      <hasToolbar>false</hasToolbar>

      <height>600</height>

      <isResizable>true</isResizable>

      <linkType>url</linkType>

      <masterLabel>detailPageButon</masterLabel>

      <openType>newWindow</openType>

      <position>none</position>

      <protected>false</protected>

      <showsLocation>false</showsLocation>

      <showsStatus>false</showsStatus>

      <url>http://google.com</url>

   </CustomPageWebLink>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

HomePageComponent

HomePageLayout

WebLink

### CustomPermission

Represents a permission that grants access to a custom feature.This type extends the Metadata metadata type and inherits its `fullName`
field.

File Suffix and Directory Location

### CustomPermission components have the suffix .customPermission and are stored in the customPermissions folder.

Version

### CustomPermission components are available in API version 31.0 and later.

Special Access Rules

As of Summer ’20 and later, only users who have one of these permissions can access this object:

**•** View Setup and Configuration

**•** Manage Session Permission Set Activations

**•** Assign Permission Sets


Metadata Types CustomPermission

Fields

**Field Name** **Field Type** **Description**

`connectedApp` string

The name of the connected app that’s
associated with this permission. Limit: 80
characters.

`description` string The custom permission description. Limit:
255 characters.

`isLicensed` boolean Required. Read-only. Indicates whether the
appropriate Salesforce license is required

before accessing the permission ( `true` ) or
not ( `false` ).

`label` string Required. The custom permission label.
Limit: 80 characters.

`requiredPermission` CustomPermissionDependencyRequired[] Indicates which custom permissions are
required by the parent custom permission.

This field is available in API version 32.0 and
later.

CustomPermissionDependencyRequired

CustomPermissionDependencyRequired determines whether a custom permission is required by the parent custom permission. A
required custom permission must be enabled when its parent is enabled.

**Field Name** **Field Type** **Description**

`customPermission` string Required. The custom permission name.

`dependency` boolean Required. Indicates whether this custom permission is required by the
parent custom permission ( `true` ) or not ( `false` ).

Declarative Metadata Sample Definition

The following is an example of a CustomPermission component.

```
<?xml version="1.0" encoding="UTF-8"?>

<CustomPermission xmlns="http://soap.sforce.com/2006/04/metadata">

  <connectedApp>Acme</connectedApp>

  <description>Read and edit access for Acme accounts.</description>

  <label>Acme Account Full Access</label>

  <requiredPermission>

    <customPermission>Acme_Account_Read</customPermission>

    <dependency>true</dependency>

  </requiredPermission>

</CustomPermission>

```


### Metadata Types CustomSite

The following is an example `package.xml` that references the previous definition, as well as other custom permissions that are
associated with a connected app.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <types>

       <members>Acme</members>

       <name>ConnectedApp</name>

     </types>

     <types>

       <members>Acme_Account_Email_Read</members>

       <members>Acme_Account_Phone_Edit</members>

       <members>Acme_Account_Full_Access</members>

       <members>Acme_Account_Read</members>

       <name>CustomPermission</name>

     </types>

     <types>

       <members>Acme_Account_Email_Read</members>

       <members>Acme_Account_Phone_Edit</members>

       <members>Acme_Account_Full_Access</members>

       <members>Acme_Account_Read</members>

       <name>PermissionSet</name>

     </types>

     <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### CustomSite

Represents a Salesforce site. Create public websites and applications that are directly integrated with your Salesforce organization, but
don't require users to log in with a username and password.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

[This Metadata API Type applies only to Salesforce sites and Visualforce sites. For Digital Experiences, also known as Experience Cloud](https://help.salesforce.com/s/articleView?id=experience.exp_cloud_basics_glossary.htm&type=5&language=en_US)
[sites, see Network.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_network.htm)

[For more information, see Salesforce Sites in Salesforce Help. This type extends the Metadata metadata type and inherits its](https://help.salesforce.com/s/articleView?id=platform.sites_overview.htm&type=5&language=en_US) `fullName`
field.

Note: CustomSite doesn’t currently support syndication feeds.

Declarative Metadata File Suffix and Directory Location

Lightning Platform CustomSite components are stored in the `sites` directory of the corresponding package directory. The file name
matches the site name, and the extension is `.site` .


Metadata Types CustomSite

Version

Lightning Platform CustomSite components are available in API version 14.0 and later.

Fields

**Field** **Field Type** **Description**

`active` boolean Required. Determines whether the site is active.

`allowHomePage` boolean

`allowStandardAnswersPages` boolean

`allowStandardIdeasPages` boolean

`allowStandardLookups` boolean

Required. Determines whether the standard home
page is visible to public users. This field is available in
API version 15.0 and later.

Determines whether the standard answer pages are
visible to public users. This field is available in API
version 19.0 and later.

Required. Determines whether the standard Ideas
pages are visible to public users. This field is available
in API version 15.0 and later.

Required. Determines whether the standard lookup
pages are visible to public users. This field is available
in API version 15.0 and later.

`allowStandardPortalPages` boolean Required. When enabled, authenticated users in this
site can access standard Salesforce pages as allowed

by their access controls. When disabled, authenticated
users in this site can't access standard Salesforce
pages, even if their access controls allow it. If your site
serves only Visualforce pages, disabling this setting
helps add a layer of access protection to your site. This
field is available in API version 39.0 and later.

`allowStandardSearch` boolean

Required. Determines whether the standard search
pages are visible to public users. This field is available
in API version 15.0 and later.

`analyticsTrackingCode` string The tracking code associated with your site. Services
such as Google Analytics can use this code to track

page request data for your site. This field is available
in API version 17.0 and later.

`authorizationRequiredPage` string

The name of the Visualforce page to display when the
guest user tries to access a page for which they aren’t
authorized.

`bandwidthExceededPage` string The name of the Visualforce page to display when the
site has exceeded its bandwidth quota.

`browserXssProtection` boolean Required. Determines whether protection against
reflected cross-site scripting attacks is enabled. If a


Metadata Types CustomSite

**Field** **Field Type** **Description**

reflected cross-site scripting attack is detected, the
browser shows a blank page with no content.
Available in API version 41.0 and later.

`cachePublicVisualforcePagesInProxyServers` boolean Indicates whether proxy servers cache this site’s
publicly available pages only for unauthenticated

guest users ( `true` ) or not ( `false` ). When this field
is `false`, this site’s cache-enabled Visualforce pages
are cached in the web browser for both authenticated
and unauthenticated users. The default is `true` . See
[Configure Site Caching in Salesforce Help for more](https://help.salesforce.com/articleView?id=platform.sites_caching.htm&type=5&language=en_US)
information.

This field is available in API version 52.0 and later.

`changePasswordPage` string

The name of the Visualforce page to display when the
portal user attempts to change their password for
either the portal or for Chatter Answers, when enabled.

`chatterAnswersForgotPasswordConfirmPage` string The name of the Visualforce page that informs the
user that an email has been sent to them with a

temporary password. This field is available if Chatter
Answers is enabled for your organization. This field is
available in API version 27.0 and later.

`chatterAnswersForgotPasswordPage` string The name of the Visualforce page to display when a
user clicks the link to retrieve a forgotten password.

This field is available if Chatter Answers is enabled for
your organization. This field is available in API version
27.0 and later.

`chatterAnswersHelpPage` string The name of the Visualforce page to display when the
user clicks the help link. This field is available if Chatter

Answers is enabled for your organization. This field is
available in API version 27.0 and later.

`chatterAnswersLoginPage` string The name of the Visualforce page to display where
users can log in to the portal. This field is available if

Chatter Answers is enabled for your organization. This
field is available in API version 27.0 and later.

`chatterAnswersRegistrationPage` string

The name of the Visualforce page to display where
users can register themselves and access the portal.
This field is available in API version 27.0 and later.

```
clickjackProtectionLevel

```

SiteClickjackProtectionLevel Required. Sets the clickjack protection level. The
(enumeration of type options are:
string)

**•** `AllowAllFraming`           - Allow framing by any
page (no protection)


Metadata Types CustomSite

**Field** **Field Type** **Description**

**•** `External`                                 - Allow framing of site or
Experience Cloud site pages on external domains
(good protection)

**•** `SameOriginOnly`                                 - Allow framing by the
same origin only (recommended)

**•** `NoFraming`                                 - Don’t allow framing by any
page (most protection)

This field is available in API version 30.0 and later.

`contentSniffingProtection` boolean Required. Determines whether the browser is
prevented from inferring the MIME type from the

document content. If enabled, it also prevents the
browser from executing some malicious files
(JavaScript, Stylesheet) as dynamic content. This field
is available in API version 41.0 and later.

`cspUpgradeInsecureRequests` boolean

This field is removed in API version 52.0 and later. In
API version 51.0 and earlier, the value in the field is
ignored.

`customWebAddresses` SiteWebAddress[] The root custom URLs associated with the site. Saving
or deploying a CustomSite replaces all root custom

URLs in the site with the root custom URLs in this list.
Custom URLs that use a non-root path prefix aren’t
included in this list and aren’t affected when saving
or deploying a CustomSite. This field is available in API
version 21.0 and later.

`description` string The site description.

`enableAuraRequests` boolean Determines whether guest users can view features
available only in Lightning ( `true` ). If set to `false`,

Lightning features don’t load. This field is available in
API version 46.0 and later.

`favoriteIcon` string

The name of the static resource, without the extension,
for the icon that appears in next to the site’s name in
browser tabs, bookmarks, and search results.

To update a site’s favorite icon, create a 16px by 16px
ICO file. Then store that images a static resource at

the base path for the site. For example, if the icon file
name is favico.ico,

```
https:// myDomainName .my.site.com/store/favicon.ico
```

is the required path for a site with the URL
`https://` _**`myDomainName`**_ `.my.site.com/store` .
To use that icon, set `favoriteIcon` to `favicon` .


Metadata Types CustomSite

**Field** **Field Type** **Description**

If the specified the ICO file doesn’t exist in the required
location, a 404 error is returned. Otherwise, if the file
isn’t present, no favorite icon is used.

`fileNotFoundPage` string The name of the Visualforce page to display when the
guest user tries to access a non-existent page.

`forgotPasswordPage` string The name of the Visualforce page to display when a
user clicks the Forgot Password link on the site’s login

page. This field is only applicable for Experience Cloud
sites.

`genericErrorPage` string The name of the Visualforce page to display for errors
not otherwise specified.

`guestProfile` string Read only. The name of the profile associated with
the guest user.

`inMaintenancePage` string The name of the Visualforce page to display when the
site is down for maintenance.

`inactiveIndexPage` string The name of the Visualforce page set as the inactive
site home page.

`indexPage` string Required. The name of the Visualforce page set as the
active site home page.

`masterLabel` string Required. The name of the site label in the Salesforce
user interface.

`myProfilePage` string The name of the Visualforce page to display as the
site user’s profile page, where users can update their

contact information. This field is available in API
version 20.0 and later.

`portal` string The name of the portal associated with this site for
login access.

`redirectToCustomDomain` boolean Indicates whether requests for this site’s
system-managed URLs are redirected to the HTTPS

custom domain serving this site ( `true` ) or not
( `false` ). System-managed site URLs end in
`*.my.salesforce-sites.com` or
`*.my.site.com` . In Experience Cloud sites, the
default is `false` . In Salesforce Sites, the default is
`true` .

If multiple custom domains serve this site and this
field is set to `true`, requests are routed to the site’s
primary custom URL only if it’s an HTTPS custom
domain. Otherwise, requests are redirected to the first
HTTPS custom domain associated with this site, in


Metadata Types CustomSite

**Field** **Field Type** **Description**

alphanumeric order. If no HTTPS custom domain
serves this site, this option has no effect.

This field is available in API version 52.0 and later.

`referrerPolicyOriginWhenCrossOrigin` boolean Required. Determines whether the referrer header
shows only Salesforce.com rather than the entire URL

when loading a page. This feature eliminates the
potential for a referrer header to reveal sensitive
information that could be present in a full URL, such
as an org ID. This field is available in API version 41.0
and later.

`requireHttps` boolean

This field is removed in API version 52.0 and later. In
API version 51.0 and earlier, the value in the field is
ignored.

`requireInsecurePortalAccess` boolean Determines whether to override your organization's
security settings and exclusively use HTTP when

logging in to the associated portal from your site.
Removed in API version 50.0 and later.

`robotsTxtPage` string The name of the Visualforce page to display for the
`robots.txt` file used by web crawlers.

`selfRegPage` string Visualforce page used for self-registration.

`serverIsDown` string The name of the static resource to be displayed from
the cache server when Salesforce servers are down.

The static resource must be a public zip file 1 MB or
smaller and must contain a page named
`maintenance.html` at the root level of the zip
file. Other resources in the zip file, such as images or
CSS files, can follow any directory structure. This field
is available in API version 17.0 and later.

`siteAdmin` string The username of the site administrator.

`siteGuestRecordDefaultOwner` string

`siteIframeWhiteListUrls` SiteIframeWhiteListUrl[]

The username of the user who owns all new records
that unauthenticated guest users create. This field is
available in API version 51.0 and later.

The list of external domains that you allow to frame
your Salesforce site. This field is available in API 49.0
and later.

`siteRedirectMappings` SiteRedirectMapping[] An array of all URL redirect rules set for your site. This
field is available in API version 20.0 and later.

`siteTemplate` string The name of the Visualforce page to be used as the
site template.


Metadata Types CustomSite

**Field** **Field Type** **Description**

`siteType` siteType Required. Identifies whether the site is a Visualforce
(Salesforce Sites), Site.com site, or ChatterNetwork

(Salesforce Sites).This field is available in API version
27.0 and later.

`subdomain` string Read only. The previous custom subdomain prefix for
the site. For example, if your site URL is

`mycompany.force.com/partners`,
`mycompany` is the `subdomain` .

This field is applicable and required only when the
`myDomainSuffix` MyDomainSettings field is set
to `MySalesforceLimited`,
`CloudforceLimited`, or
`DatabaseLimited` .

If you enabled Salesforce Sites or Digital Experiences
when the `myDomainSuffix` MyDomainSettings
field was set to one of those values, this field returns
this site’s previous subdomain. Otherwise, this field
returns a null value.

`urlPathPrefix` string The first part of the path on the site's URL that
distinguishes this site from other sites. For example,

if your site URL is
_`MyDomainName`_ `.my.salesforce-sites.com/partners`,
`partners` is the `urlPathPrefix` .

SiteIframeWhiteListUrl

Represents the external domains that you allow to frame your site or experience pages.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this metadata type’s name.

**Field** **Field Type** **Description**

`url` string Required. The trusted domain that you allow
to frame your site or Experience Cloud site

pages. Accepts these formats: `example`,
`example.com`, `*example.com`, and
`https://example.com` .

SiteRedirectMapping

SiteRedirectMapping represents a URL redirect rule on your Salesforce site.” in Salesforce Help.


Metadata Types CustomSite

**Field** **Field Type** **Description**

`action` SiteRedirect (enumeration of type string) Required. The type of the redirect. Available
string values are:

**•** `Permanent`

**•** `Temporary`

`isActive` boolean The status of the redirect: active or inactive.

`source` string Required. The URL that you want to redirect.
It must be a relative URL, but can have any

valid extension type, such as `.html` or
`.php` .

`target` string Required. The new URL you want users to
visit. It can be a relative URL or a

fully-qualified URL with an `http://` or
`https://` prefix.

SiteWebAddress

Represents the web address of a Salesforce site.

**Field** **Field Type** **Description**

`certificate` string Identifies the certificate associated with the
custom domain. If the custom domain is set

up for Salesforce to serve HTTPS, this field
indicates which certificate to use.

`domainName` string Required. The domain of the website, in the
form of `www.acme.com` .

`primary` boolean

Declarative Metadata Sample Definition

Here is a sample XML definition of a site.

```
<?xml version="1.0" encoding="UTF-8"?>

<CustomSite xmlns="http://soap.sforce.com/2006/04/metadata">

```

Required. Indicates whether this is the
primary domain ( `true` ). If `false`, this is
not the primary domain.

```
<active>true</active>

<allowHomePage>true</allowHomePage>

<allowStandardAnswersPages>true</allowStandardAnswersPages>

<allowStandardIdeasPages>true</allowStandardIdeasPages>

<allowStandardLookups>true</allowStandardLookups>

<allowStandardPortalPages>true</allowStandardPortalPages>

<allowStandardSearch>true</allowStandardSearch>

```


Metadata Types CustomSite

```
      <analyticsTrackingCode>UA-000000-2</analyticsTrackingCode>

      <authorizationRequiredPage>Unauthorized</authorizationRequiredPage>

      <bandwidthExceededPage>BandwidthExceeded</bandwidthExceededPage>

      <browserXssProtection>true</browserXssProtection>

   <cachePublicVisualforcePagesInProxyServers>false</cachePublicVisualforcePagesInProxyServers>

      <changePasswordPage>ChangePassword</changePasswordPage>

   <chatterAnswersForgotPasswordConfirmPage>ChatterAnswersForgotPasswordConfirm</chatterAnswersForgotPasswordConfirmPage>

   <chatterAnswersForgotPasswordPage>ChatterAnswersForgotPassword</chatterAnswersForgotPasswordPage>

      <chatterAnswersHelpPage>ChatterAnswersHelp</chatterAnswersHelpPage>

      <chatterAnswersLoginPage>ChatterAnswersLogin</chatterAnswersLoginPage>

   <chatterAnswersRegistrationPage>ChatterAnswersRegistration</chatterAnswersRegistrationPage>

      <clickjackProtectionLevel>SameOriginOnly</clickjackProtectionLevel>

      <contentSniffingProtection>true</contentSniffingProtection>

      <customWebAddresses>

       <domainName>www.testing123.com</domainName>

       <primary>true</primary>

      </customWebAddresses>

      <description>Partners portal for My Company</description>

      <enableAuraRequests>true</enableAuraRequests>

      <favoriteIcon>favicon</favoriteIcon>

      <fileNotFoundPage>FileNotFound</fileNotFoundPage>

      <forgotPasswordPage>ForgotPassword</forgotPasswordPage>

      <genericErrorPage>Exception</genericErrorPage>

      <guestProfile>Guest</guestProfile>

      <inMaintenancePage>InMaintenance</inMaintenancePage>

      <inactiveIndexPage>Inactive</inactiveIndexPage>

      <indexPage>UnderConstruction</indexPage>

      <masterLabel>customSite</masterLabel>

      <myProfilePage>UserProfile</myProfilePage>

      <portal>Customer Portal</portal>

      <redirectToCustomDomain>true</redirectToCustomDomain>

      <referrerPolicyOriginWhenCrossOrigin>true</referrerPolicyOriginWhenCrossOrigin>

      <robotsTxtPage>RobotsTxt</robotsTxtPage>

      <selfRegPage>SelfReg</selfRegPage>

      <serverIsDown>MyServerDownResource</serverIsDown>

      <siteAdmin>admin@myco.org</siteAdmin>

      <siteGuestRecordDefaultOwner>admin@myco.org</siteGuestRecordDefaultOwner>

      <siteIframeWhiteListUrl>

       <url>example.com</url>

      </siteIframeWhiteListUrl>

      <siteTemplate>SiteTemplate</siteTemplate>

      <siteType>Siteforce</siteType>

      <subdomain>myco</subdomain>

      <urlPathPrefix>partners</urlPathPrefix>

   </CustomSite>

```


### Metadata Types CustomTab

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

Portal

### CustomTab

Represents a custom tab. Custom tabs let you display custom object data or other web content in Salesforce. When you add a custom
tab to an app in Salesforce Classic, it appears as a tab. When you add a custom tab to an app in Lightning Experience, it appears as an
item in the app’s navigation bar and in the App Launcher. When a tab displays a custom object, the tab name is the same as the custom
object name. For page, s-control, or URL tabs, the name is arbitrary.

For more information, see _Custom Tabs_ in Salesforce Help. This type extends the Metadata metadata type and inherits its `fullName`
field.

File Suffix and Directory Location

The file suffix is `.tab` . There’s one file for each tab, stored in the `tabs` folder in the corresponding package directory.

Note: Retrieving a component of this metadata type in a project makes the component appear in any Profile and PermissionSet
components that are retrieved in the same package.

Version

Tabs are available in API version 10.0 and later.

Fields

This metadata type contains the following fields:

**Field Name** **Field Type** **Description**

`actionOverrides` ActionOverride[]

`auraComponent` string

A list of the action overrides that are assigned to the tab. Only one
override is allowed per `formFactor` for a given tab.

This field is available in API version 37.0 and later.

The name of the Aura component to display in this tab.

Only one of these fields can have a value set:

**•** `auraComponent`

**•** `customObject`

**•** `flexiPage`

**•** `lwcComponent`

**•** `page`


Metadata Types CustomTab

**Field Name** **Field Type** **Description**

**•** `scontrol`

**•** `url`

`customObject` boolean

Indicates whether this tab is for a custom object ( `true` ) or not ( `false` ).
If set to `true`, the name of the tab matches the name of the custom
object.

Only one of these fields can have a value set:

**•** `auraComponent`

**•** `customObject`

**•** `flexiPage`

**•** `lwcComponent`

**•** `page`

**•** `scontrol`

**•** `url`

`description` string The optional description text for the tab.

`flexiPage` string

The name of the Lightning page to display in this tab.

Only one of these fields can have a value set:

**•** `auraComponent`

**•** `customObject`

**•** `flexiPage`

**•** `lwcComponent`

**•** `page`

**•** `scontrol`

**•** `url`

`frameHeight` int The height, in pixels of the tab frame. Required for s-control and page
tabs.

`fullName` string The name of the tab. The value of this field depends on the type of tab,
and the API version.

**•** For custom object tabs, the `fullName` is the developer-assigned
name of the custom object (MyCustomObject__c, for example). For
custom object tabs, this name must be the same as the custom
object name, and `customObject` must be set to `true` .

**•** For web tabs, the `fullName` is the developer-assigned name of
the tab (MyWebTab, for example).

The `fullName` can contain only underscores and alphanumeric
characters. It must be unique, begin with a letter, not include spaces,
not end with an underscore, and not contain two consecutive
underscores. This field is inherited from the Metadata component.


Metadata Types CustomTab

**Field Name** **Field Type** **Description**

`hasSidebar` boolean Indicates if the tab displays the sidebar panel.

`icon` string

The optional reference to the image document for the tab if the tab isn’t
using one of the standard tab styles. This field is available in API version
14.0.

`label` string The label of the tab, for web tabs only.

`lwcComponent` string

`motif` string

The name of the Lightning web component to display in this tab.

Only one of these fields can have a value set:

**•** `auraComponent`

**•** `customObject`

**•** `flexiPage`

**•** `lwcComponent`

**•** `page`

**•** `scontrol`

**•** `url`

Required. The tab style for the color scheme and icon for the custom
tab.

For example, “'Custom70: Handsaw,” is the handsaw icon.

Valid Values for this field are: Custom1:Heart, Custom2:Fan, Custom3:Sun,
Custom4:Hexagon, Custom5:Leaf, Custom6:Triangle, Custom7:Square,
Custom8:Diamond, Custom9:Lightning, Custom10:Moon, Custom11:Star,
Custom12:Circle, Custom13:Box, Custom14:Hands, Custom15:People,
Custom16:Bank, Custom17:Sack, Custom18:Form, Custom19:Wrench,
Custom20:Airplane, Custom21:Computer, Custom22:Telephone,
Custom23:Envelope, Custom24:Building, Custom25:Alarmclock,
Custom26:Flag, Custom27:Laptop, Custom28:Cellphone, Custom29:PDA,
Custom30:Radardish, Custom31:Car, Custom32:Factory, Custom33:Desk,
Custom34:Insect, Custom35:Microphone, Custom36:Train,
Custom37:Bridge, Custom38:Camera, Custom39:Telescope,
Custom40:Creditcard, Custom41:Cash, Custom42:Treasurechest,
Custom43:Jewel, Custom44:Hammer, Custom45:Ticket, Custom46:Stamp,
Custom47:Knight, Custom48:Trophy, Custom49:CD/DVD,
Custom50:Bigtop, Custom51:Apple, Custom52:Balls, Custom53:Bell,
Custom54:Boat, Custom55:Books, Custom56:Bottle,
Custom57:BuildingBlock, Custom58:Caduceus, Custom59:Can,
Custom60:Umbrella, Custom61:Castle, Custom62:Chalkboard,
Custom63:Chip, Custom64:Compass, Custom65:Cup, Custom66:Dice,
Custom67:Gears, Custom68:Globe, Custom69:Guitar, Custom70:Handsaw,
Custom71:Headset, Custom72:Helicopter, Custom73:HighwaySign,
Custom74:HotAirBalloon, Custom75:IPPhone, Custom76:Keys,
Custom77:Locked, Custom78:Map, Custom79:MeasuringTape,
Custom80:Motorcycle, Custom81:MusicalNote, Custom82:Whistle,
Custom83:Pencil, Custom84:Presenter, Custom85:RealEstateSign,


Metadata Types CustomTab

**Field Name** **Field Type** **Description**

Custom86:RedCross, Custom87:Safe, Custom88:Sailboat,
Custom89:Saxophone, Custom90:Scales, Custom91:Shield,
Custom92:Ship, Custom93:ShoppingCart, Custom94:Stethoscope,
Custom95:Stopwatch, Custom96:StreetSign, Custom97:Thermometer,
Custom98:Truck, Custom99:TVCRT, Custom100:TVWidescreen.

`page` string

`scontrol` string

The name of the Visualforce page to display in this tab.

Only one of these fields can have a value set:

**•** `auraComponent`

**•** `customObject`

**•** `flexiPage`

**•** `lwcComponent`

**•** `page`

**•** `scontrol`

**•** `url`

The name of the s-control to display in this tab.

Only one of these fields can have a value set:

**•** `auraComponent`

**•** `customObject`

**•** `flexiPage`

**•** `lwcComponent`

**•** `page`

**•** `scontrol`

**•** `url`

`splashPageLink` string The custom link used as the introductory splash page when users click
the tab. References a HomePageComponent.

`url` string

The URL for the external web-page to embed in this tab.

Only one of these fields can have a value set:

**•** `auraComponent`

**•** `customObject`

**•** `flexiPage`

**•** `lwcComponent`

**•** `page`

**•** `scontrol`

**•** `url`


### Metadata Types CustomValue

**Field Name** **Field Type** **Description**

The default encoding setting is Unicode: `UTF-8` . Change it if you’re
passing information to a URL that requires data in a different format. This
option is available when the value `URL` is selected in the tab type.

```
urlEncodingKey

```

Encoding
(enumeration of
type string)

Declarative Metadata Sample Definition

The following is the definition of a tab:

```
<?xml version="1.0" encoding="UTF-8"?>

<CustomTab xmlns="http://soap.sforce.com/2006/04/metadata">

   <description>Myriad Publishing</description>

   <frameHeight>600</frameHeight>

   <motif>Custom53: Bell</motif>

   <url>https://www.example.com</url>

   <urlEncodingKey>UTF-8</urlEncodingKey>

</CustomTab>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

CustomApplication

### CustomValue

Represents the definition of a value used in a global value set or local custom picklist. Custom picklist fields can be local and unique, or
can inherit their values from a global picklist (called a _global value set_ in API version 38.0). This type extends the Metadata metadata type
and inherits its `fullName` field.

To deactivate a global picklist value, you can invoke an `update()` call on GlobalPicklist (API version 37.0) or GlobalValueSet (API
version 38.0 and later) with the value omitted, or with the value’s `isActive` field set to `false` . Or, you can invoke an `update()`
call directly on GlobalPicklistValue (API version 37.0) or CustomValue (API version 38.0 and later) with the `isActive` field set to `false` .

Note: If picklist values are missing from a component definition, they get deactivated when deployed. Deactivation occurs for
picklist values of both standard and custom fields.

### CustomValue doesn’t support file-based operations and only supports CRUD-based calls. CustomValue is retrieved or deployed together

with a GlobalValueSet or CustomObject component.

File Suffix and Directory Location

### CustomValue components have the suffix .customValue . A CustomValue component is returned with either a GlobalValueSet or

CustomObject component.


Metadata Types CustomValue

Version

CustomValue components are available in API version 38.0 and later. CustomValue replaces GlobalPicklistValue from API version 37.0.

Fields

**Field Name** **Field Type** **Description**

`color` string The color assigned to the picklist value when it’s used in charts on reports
and dashboards. The color is in hexadecimal format; for example,

#FF6600. If a color isn’t specified, it’s assigned dynamically upon chart
generation.

`default` boolean

`description` string

Required. Indicates whether this value is the default selection for the
global picklist and the custom picklists that share its picklist value set.
This field is set to _`true`_ by default.

A picklist value’s description. It’s useful to include a description for a
picklist value so the reason for creating it can be tracked. Limit: 255
characters.

`isActive` boolean Indicates whether this value is active or inactive. The default value is
_`true`_ . Users can select only active values from a picklist. An API retrieve

operation for global picklist values returns all active and inactive values
in the picklist. But retrieving the values of a non-global, unrestricted
picklist returns only the active values.

`label` string The value’s display label. If you don’t specify the label when creating a
value it defaults to the API name. Available in API version 39.0 and later.

StandardValue

This metadata type defines a value in a value set for a standard picklist and specifies whether this value is the default value. This type
extends the CustomValue metadata type and inherits all its fields.

When you deploy changes to standard picklist fields, picklist values are added as needed.

**Field Name** **Field Type** **Description**

`allowEmail` boolean

Indicates whether this value lets users email a quote PDF ( `true` ), or not
( `false` ). This field is only relevant for the `Status` field in quotes.This
field is available in API version 18.0 and later.

`closed` boolean Indicates whether this value is associated with a closed status ( `true` ),
or not ( `false` ). This field is only relevant for the standard `Status`

field in cases and tasks. This field is available in API version 16.0 and up
to version 36.0. In version 37.0, this field is in GlobalPicklistValue.

`converted` boolean Indicates whether this value is associated with a converted status ( `true` ),
or not ( `false` ). This field is relevant for only the standard `Lead`

`Status` field in leads. Your organization can set its own guidelines for


Metadata Types CustomValue

**Field Name** **Field Type** **Description**

determining when a lead is qualified, but typically, you want to convert
a lead as soon as it becomes a real opportunity that you want to forecast.
For more information, see Convert Qualified Leads in Salesforce Help.
This field is available in API version 16.0 and later.

`cssExposed` boolean

Indicates whether this value is available in your Self-Service Portal ( `true` ),
or not ( `false` ). This field is only relevant for the standard `Case`
`Reason` field in cases.

Self-Service provides an online support channel for your customers allowing them to resolve their inquiries without contacting a customer

service representative. For more information about Self-Service, see
Setting Up Your Self-Service Portal in Salesforce Help.

Note: Starting with Spring ’12, the Self-Service portal isn’t
available for new Salesforce orgs. Existing orgs continue to have
access to the Self-Service portal.

This field is available in API version 16.0 and later.

Indicates whether this value is associated with a forecast category
( `true` ), or not ( `false` ). This field is only relevant for the standard
`Stage` field in opportunities.

**•** Omitted

**•** Pipeline

**•** BestCase

**•** Forecast

**•** Closed

This field is available in API version 16.0 and later.

```
forecastCategory

```

ForecastCategories
(enumeration of
type string)

`highPriority` boolean Indicates whether this value is a high priority item ( `true` ), or not
( `false` ). This field is only relevant for the standard `Priority` field

in tasks. For more information about tasks, see Start Using Tasks in
Salesforce Help. This field is available in API version 16.0 and later.

`probability` int

Indicates whether this value is a probability percentage ( `true` ), or not
( `false` ). This field is only relevant for the standard `Stage` field in
opportunities. This field is available in API version 16.0 and later.

`reverseRole` string A picklist value corresponding to a reverse role name for a partner. If the
role is subcontractor, then the reverse role might be general contractor.

Assigning a partner role to an account in Salesforce creates a reverse
partner relationship so that both accounts list the other as a partner. This
field is only relevant for partner roles.

For more information, see Partner Fields in Salesforce Help.

This field is available in API version 18.0 and later.


### Metadata Types Dashboard

**Field Name** **Field Type** **Description**

`reviewed` boolean Indicates whether this value is associated with a reviewed status ( `true` ),
or not ( `false` ). This field is only relevant for the standard `Status`

field in solutions. For more information about opportunities, see Creating
Solutions in Salesforce Help. This field is available in API version 16.0 and
later.

`won` boolean Indicates whether this value is associated with a closed or won status
( `true` ), or not ( `false` ). This field is only relevant for the standard

`Stage` field in opportunities. This field is available in API version 16.0
and later.

Declarative Metadata Sample Definition

For an example of CustomValue components within a GlobalValueSet component that’s referenced by a `package.xml`, see
GlobalValueSet.

### Dashboard

Represents a dashboard. Dashboards are visual representations of data that allow you to see key metrics and performance at a glance.

This type extends the Metadata metadata type and inherits its `fullName` field. For more information, see “Edit Dashboards in
Accessibility Mode in Salesforce Classic” in the Salesforce online help.

Declarative Metadata File Suffix and Directory Location

### Dashboards are stored in the dashboards directory of the corresponding package directory. The file name matches the dashboard

title and the extension is `.dashboard` .

Retrieving Dashboards

You can’t use the wildcard (*) symbol with dashboards in `package.xml` . To retrieve the list of dashboards for populating
### package.xml with explicit names, call listMetadata() and pass in DashboardFolder as the type. Note that DashboardFolder is not returned as a type in describeMetadata() . Dashboard is returned from describeMetadata()

with an associated attribute of `inFolder` set to true. If that attribute is set to true, you can construct the type by using the component
name with the word Folder, such as DashboardFolder.

The following example shows folders in `package.xml` . The names used in `package.xml` must be developer names, not dashboard
titles.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>MyDBFolder/MyDBName</members>

        <name>Dashboard</name>

      </types>

      <types>

        <members>MyDocumentFolder/MyDocumentName</members>

```


Metadata Types Dashboard

```
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

Dashboard components are available in API version 14.0 and later.

Fields

**Field** **Field Type** **Description**

`backgroundEndColor` string Required. A dashboard can have a gradient color change on its
charts. This field defines the second color for the gradient and

`backgroundStartColor` defines the first color. If you
prefer your background to be all one color or do not want a
gradient color change, select the same color for this field and
`backgroundStartColor` . The color is in hexadecimal
format; for example #FF6600.

`backgroundFadeDirection` ChartBackgroundDirection
(enumeration of type string)

Required. The direction of the gradient color change, defined
by the `backgroundStartColor` and
`backgroundEndColor` fields. The valid values are:

**•** `Diagonal`

**•** `LeftToRight`

**•** `TopToBottom`

`backgroundStartColor` string Required. The starting color for the gradient color change on
the dashboard's charts. See `backgroundEndColor` for

more information. The color is in hexadecimal format; for
example #FF6600.

`chartTheme` ChartTheme (enumeration of Determines the default theme for all dashboard charts. Replaces
type string) `dashboardChartTheme` for API v42.0 and later.

**•** `light` —Light-colored theme.

**•** `dark` —Dark-colored theme.

This field is available in API version 42.0 and later.


Metadata Types Dashboard

**Field** **Field Type** **Description**

`colorPalette` ChartColorPalettes Determines the default palette for all dashboard charts. Replaces
(enumeration of type string) `dashboardColorPalette` for API v42.0 and later.

**•** `accessible`

**•** `bluegrass`

**•** `colorSafe`

**•** `Default`

**•** `dusk`

**•** `earth`

**•** `fire`

**•** `gray`

**•** `heat`

**•** `justice`

**•** `nightfall`

**•** `pond`

**•** `sunrise`

**•** `tropic`

**•** `unity`

**•** `water`

**•** `watermelon`

This field is available in API version 42.0 and later.

`dashboardChartTheme` ChartTheme (enumeration of Determines the default theme for all dashboard charts.
type string)

**•** `light` —Light-colored theme.

**•** `dark` —Dark-colored theme.

This field is available to maintain backward compatibility with
versions prior to API version 42.0.

`dashboardColorPalette` ChartColorPalettes Determines the default palette for all dashboard charts.
(enumeration of type string)

**•** `accessible`

**•** `bluegrass`

**•** `colorSafe`

**•** `Default`

**•** `dusk`

**•** `earth`

**•** `fire`

**•** `gray`

**•** `heat`

**•** `justice`

**•** `nightfall`


Metadata Types Dashboard

**Field** **Field Type** **Description**

**•** `pond`

**•** `sunrise`

**•** `tropic`

**•** `unity`

**•** `water`

**•** `watermelon`

This field is available to maintain backward compatibility with
versions prior to API version 42.0.

`dashboardFilters` DashboardFilter[]

`dashboardGridLayout` DashboardGridLayout

The list of filters in a dashboard.

This field is available in API version 23.0 and later.

Lists the included DashboardGridComponent objects, specifies
the number of dashboard columns, and sets each dashboard
row’s height in pixels.

This field is available in API version 35.0 and later.

`dashboardType` DashboardType (enumeration Determines the way visibility settings are set for a dashboard.
of type string) The valid values are:

**•** `SpecifiedUser` —All users see data at the access level
of one specific running user, specified in the
`runningUser` field, regardless of their own security
settings.

**•** `LoggedInUser` —Each logged-in user sees data
according to his or her own access level.

**•** `MyTeamUser` —Managers can choose to view the
dashboard from the point of view of their subordinates in
the role hierarchy. This value is available in API version 20.0
and later.

This field is available in API version 19.0 and later.

`description` string Description for the dashboard. Maximum of 255 characters.

`folderName` string

Name of the folder that houses the dashboard.

This field is available in API version 35.0 and later.

`fullName` string Inherited from Metadata, this field is defined in the WSDL for
this metadata type. It must be specified when creating, updating,

or deleting. See `createMetadata()` to see an example of
this field specified for a call.

This field specifies the folder and dashboard title; for example
`folderSales/California` .


Metadata Types Dashboard

**Field** **Field Type** **Description**

`isGridLayout` boolean

Specifies whether a dashboard uses the Lightning Experience
layout ( `true` ) or not ( `false` ).

Lightning Experience allows dashboards with more than three
columns with components that span multiple columns and
multiple rows in size.

This field is available in API version 35.0 and later.

`dashboardResultRefreshedDate` string Required. Date that the dashboard was last refreshed.

`dashboardResultRunningUser` string Required. User currently accessing the dashboard.

`leftSection` DashboardComponentSection Required. The left section or column of the dashboard.

`middleSection` DashboardComponentSection The middle section or column of the dashboard.

`numSubscriptions` int Number of subscriptions reported on the dashboard. This field
is available in API version 42.0 and later.

`owner` string The creator of the dashboard.

`rightSection` DashboardComponentSection Required. The right section or column of the dashboard.

`runningUser` string

The username of the user whose role and sharing settings are
used to determine the data shown in the dashboard.

When you deploy a dashboard and the value in this field is not
defined or does not correspond to a valid user, the field is

populated with the username of the user performing the
deployment.

Regardless of their security settings, all users viewing a
dashboard see exactly the same data, because dashboards are
always run using the security settings of a particular user.

Tip: To avoid inappropriate exposure of sensitive data,
save the dashboard to a folder that is visible only to
appropriate users.

`textColor` string Required. Color of the text on each chart in the dashboard. The
color is in hexadecimal format; for example #FF6600.

`title` string Required. The dashboard title.

`titleColor` string Required. Color of the titles on each dashboard component. The
color is in hexadecimal format; for example #FF6600.

`titleSize` int Required. Size of characters in title text. For example, a value of
12 indicates 12pt text.

DashboardFilter

DashboardFilter represents a filter in a dashboard.


Metadata Types Dashboard

**Field** **Field Type** **Description**

`dashboardFilterOptions` DashboardFilterOption[] The list of items you can select in the **Filter Options** section of
the Add Filter dialog.

`name` string Required. The filter label.

DashboardFilterOption

DashboardFilterOption represents a filter option in a dashboard.

**Field** **Field Type** **Description**

```
operator

```

DashboardFilterOperation Required. Represents the filter operation for this filter item. Valid
values are:

(enumeration of type string)

**•** `equals`

**•** `notEqual`

**•** `lessThan`

**•** `greaterThan`

**•** `lessOrEqual`

**•** `greaterOrEqual`

**•** `contains`

**•** `notContain`

**•** `startsWith`

**•** `includes`

**•** `excludes`

**•** `between`

Note: The “between” operator takes two operands
(for example, “between MinimumValue,
MaximumValue”). Note also that the minimum value
is inclusive, while the maximum value is exclusive.
All other dashboard filter operations take a single
operand only.

This field is available in API version 24.0 and later.

With API version 23.0, valid values are enumerated in
CustomField.

`values` string[]

Required. One or more values in the **Filter Options** area of the
Add Filter dialog. This field is available in API version 24.0 and
later.


Metadata Types Dashboard

DashboardGridLayout

Lightning Experience features dashboards with more than three columns and components that span multiple columns and multiple
rows in size. DashboardGridLayout lists the included dashboard components, specifies the number of dashboard columns, and sets each
dashboard row’s height in pixels.

**Field** **Field Type** **Description**

`dashboardGridComponents` DashboardGridComponent[] List of DashboardGridComponent objects in the dashboard.

`numberOfColumns` int Required. Total number of columns in the dashboard.

`rowHeight` int Required. Height of each row in pixels.

DashboardGridComponent

Lightning Experience features dashboards with more than three columns and components that span multiple columns and multiple
rows in size. DashboardGridComponent specifies location and size of a given dashboard component.

**Field** **Field Type** **Description**

`colSpan` int

Required. The width of the dashboard component in columns.

For example, if `colSpan` is 5, then the dashboard component
spans five columns.

`columnIndex` int Required. The left-most column that is occupied by the
dashboard component.

`dashboardComponent` DashboardComponent Required. The dashboard component that is being sized and
placed.

`rowIndex` int Required. The top-most row that is occupied by the dashboard
component.

`rowSpan` int Required. The height of the dashboard component in rows.

DashboardComponent

A dashboard consists of a group of different components or elements that display data. Each component can use a custom report or a
custom s-control as their data source to display corporate metrics or key performance indicators. You can create several dashboard
components and display them all in one dashboard aligned in up to three columns.

**Field** **Field Type** **Description**

`chartAxisRange` ChartRangeType (enumeration of type A manual or automatic axis range for bar or line charts.
string) The valid values are:

**•** `auto`

**•** `manual`


Metadata Types Dashboard

**Field** **Field Type** **Description**

`chartAxisRangeMax` double

`chartAxisRangeMin` double

`chartSummary` ChartSummary

The maximum axis range to be displayed. This only applies
to bar and line charts in which the `manual` axis range
is selected for the `chartAxisRange` field.

The minimum axis range to be displayed. This only applies
to bar and line charts in which the `manual` axis range
is selected for the `chartAxisRange` field.

Specifies the summary field for the chart data. Required
if `isAutoSelectFromReport` is set to `false` .

This field is available in API version 25.0 and later.

`componentType` DashboardComponentType Required. Dashboard component type. The valid values
(enumeration of type string) are:

**•** `Bar`

**•** `BarGrouped`

**•** `BarStacked`

**•** `BarStacked100`

**•** `Column`

**•** `ColumnGrouped`

**•** `ColumnLine`

**•** `ColumnLineGrouped`

**•** `ColumnLineStacked`

**•** `ColumnLineStacked100`

**•** `ColumnStacked`

**•** `ColumnStacked100`

**•** `Donut`

**•** `FlexTable`

**•** `Funnel`

**•** `Gauge`

**•** `Image`

**•** `Line`

**•** `lineCumulative`

**•** `LineGrouped`

**•** `lineGroupedCumulative`

**•** `Metric`

**•** `Pie`

**•** `PulseMetric`

**•** `RichText`

**•** `Scatter`

**•** `ScatterGrouped`


Metadata Types Dashboard

**Field** **Field Type** **Description**

**•** `Scontrol`

**•** `Table`

**•** `VisualforcePage`

`dashboardComponentContents` DashboardComponentContent on
page 852[]

`dashboardDynamicValues` DashboardDynamicValue on page
853[]

`dashboardFilterColumns` DashboardFilterColumn on page 853[]

A list of dashboard component contents.

This field is available in API version 58.0 and later.

A list of dashboard dynamic values.

This field is available in API version 36.0 and later.

A list of dashboard filter columns. Each report-based
component must have a dashboard filter column that
defines the column that the filter applies to.

This field is available in API version 23.0 and later.

`dashboardTableColumn` DashboardTableColumn[] Represents a list of columns on a customized dashboard
table component.

`displayUnits` ChartUnits (enumeration of type Chart Units. The valid values are:
string)

**•** `Auto`

**•** `Integer`

**•** `Hundreds`

**•** `Thousands`

**•** `Millions`

**•** `Billions`

**•** `Trillions`

`drillDownUrl` string For charts, specifies a URL that users go to when they click
the dashboard component. Use this option to send users

to another dashboard, report, record detail page, or other
system that uses a Web interface. This field overrides the
`drillEnabled` and `drillToDetailEnabled`
fields.

`drillEnabled` boolean Specifies whether to take users to the full or filtered source
report when they click the dashboard component. Set to

`false` to drill to the full source report; set to `true` to
drill to the source report filtered by what they clicked. If
set to `true`, users can click individual groups, axis values,
or legend entries.

This overrides the `drillToDetailEnabled` field.
This field is available in API version 17.0 and later.

`drillToDetailEnabled` boolean When enabled, users are taken to the record detail page
when they click a record name, record owner, or feed post


Metadata Types Dashboard

**Field** **Field Type** **Description**

in a table or chart. When set to `true` users can click axis
and legend values, chart elements, and table entries. The
`drillDownUrl` and `drillEnabled` fields override
this field. This field is available in API version 20.0 and later.

`enableHover` boolean Specifies whether to display values, labels, and
percentages when hovering over charts. Hover details

depend on chart type. Percentages apply to pie, donut,
and funnel charts only. This field is available in API version
17.0 and later.

`expandOthers` boolean Specifies whether to combine all groups less than or equal
to 3% of the total into a single 'Others' wedge or segment.

This only applies to pie, donut, and funnel charts. Set to
`true` to show all values individually on the chart; set to
`false` to combine small groups into 'Others.' This field
is available in API version 17.0 and later.

`flexComponentProperties` DashboardFlexTableComponentProperties

Defines metadata for Lightning Experience table columns
and sorting. This field is available in API version 41.0 and
later.

`footer` string Footer displayed at the bottom of the dashboard
component. Maximum of 255 characters.

`gaugeMax` double

The maximum value on a gauge. A gauge is used to see
how far you are from reaching a goal. It looks like a
speedometer in a car.

`gaugeMin` double The minimum value on a gauge.

`groupingColumn` string

Specifies the field by which to group data. This data is
displayed on the X-axis for vertical column charts and on
the Y-axis for horizontal bar charts.

This field is available in API version 25.0 and later.

`GroupingSortProperties` DashboardComponentGroupingSortProperties This field captures sort properties of the dashboard
component. If the component has one or more groupings,

sort information is stored here; otherwise, it is stored in
the `sortBy` field. This field is available in API version
46.0 and later.

`header` string Header displayed at the top of the dashboard component.
Maximum of 80 characters.

`indicatorBreakpoint1` double

The value that separates the `indicatorLowColor`
from the `indicatorMiddleColor` on the
dashboard.


Metadata Types Dashboard

**Field** **Field Type** **Description**

`indicatorBreakpoint2` double

The value that separates the
`indicatorMiddleColor` from the
`indicatorHighColor` on the dashboard.

`indicatorHighColor` string The color representing a high number range on the
gauge.

`indicatorLowColor` string The color representing a low number range on the gauge.

`indicatorMiddleColor` string The color representing a medium number range on the
gauge.

`legendPosition` ChartLegendPosition (enumeration of
type string)

The location of the legend with respect to the chart. The
valid values are:

**•** `Bottom`

**•** `OnChart`

**•** `Right`

`maxValuesDisplayed` int The maximum number of elements to include in the
top-level grouping of the horizontal axis of a horizontal

chart, vertical axis of a vertical chart, or selected axis of a
stacked bar chart. For example, if you want to list only
your top five salespeople, create an opportunity report
that lists total opportunity amounts by owner and enter
`5` in this field.

`metricLabel` string Descriptive label for the metric. This is relevant if `metric`
is the value of the `componentType` field.

`page` string Visualforce page associated with the component.

`pageHeightInPixels` int Display height of the Visualforce page in pixels.

`report` string Name of the report associated with the component.

`scontrol` string S-control associated with component if `scontrol` is
the value of the `componentType` field. For more

information, see “Defining Custom S-Controls” in the
Salesforce online help.

`scontrolHeightInPixels` int Display height of the s-control in pixels.

`showPercentage` boolean

Indicates if percentages are displayed for regions of
gauges and wedges and segments of pie, donut, and
funnel charts ( `true` ), or not ( `false` ).

`showPicturesOnCharts` boolean Display Chatter photos for up to 20 records in a horizontal
bar chart component whose source report is grouped by

a user or group name field. If there are more than 20
records with photos, record names are shown instead of
photos. Set `Grouping Display` to _`None`_ to show


Metadata Types Dashboard

**Field** **Field Type** **Description**

photos. Set the `Drill Down to` option to _`Record`_
_`Detail Page`_ to take users directly to user profile or
group pages when they click photos. Chatter must be
enabled for photos to be displayed. Depending on your
organization's setup, you may not see photos on tables
and charts.

`showPicturesOnTables` boolean Display Chatter photos for up to 20 records in a horizontal
bar chart component whose source report is grouped by

a user or group name field. If there are more than 20
records with photos, record names are shown instead of
photos. Set `Grouping Display` to _`None`_ to show
photos. Set the `Drill Down to` option to _`Record`_
_`Detail Page`_ to take users directly to user profile or
group pages when they click photos. Chatter must be
enabled for photos to be displayed. Depending on your
organization's setup, you may not see photos on tables
and charts.

`showTotal` boolean Indicates if the total of all wedges is displayed for gauges
and donut charts ( `true` ), or not ( `false` ).

`showValues` boolean Indicates if the values of individual records or groups are
displayed for charts ( `true` ), or not ( `false` ).

`sortBy` DashboardComponentFilter The sort option for the dashboard component.
(enumeration of type string)

`sortLegendValues` boolean Specifies whether to sort the legend values for the
dashboard component.

`title` string The title of the dashboard component. Maximum of 40
characters.

`useReportChart` boolean Specifies whether to use the chart defined in the source
report on this dashboard component. The chart settings

in the source report determine how the chart displays in
the dashboard, and any chart settings you define for the
dashboard are overridden. If you defined a combination
chart in the source report, use this option to use that
combination chart on this dashboard.

DashboardComponentContent

dashboardComponentContent represents the content of a dashboard’s components.

**Field** **Field Type** **Description**

`additionalInfo` string Any additional metadata the user wants to include for the
component contents.


Metadata Types Dashboard

**Field** **Field Type** **Description**

`altText` string The component’s alternative text.

`fileName` string The name of the component file.

`fit` Fit (enumeration of type string) The image alignment type. Valid values are:

**•** `FitHeight`

**•** `FitWidth`

**•** `Original`

**•** `Stretch`

**•** `Tile`

`horizontalAlignment` HorizontalAlignment The horizontal alignment type. Valid values are:
(enumeration of type string)

**•** `Left`

**•** `Center`

**•** `Right`

`componentParameters` string The parameters for the component.

`richTextContent` string The rich text content for the component.

`tooltip` string The dashboard component’s tooltip.

`verticalAlignment` VerticalAlignment (enumeration The vertical alignment type. Valid values are:
of type string)

**•** `Bottom`

**•** `Center`

**•** `Top`

DashboardDynamicValue

DashboardDynamicValue represents a dynamic value in a dashboard.

**Field** **Field Type** **Description**

`additionalInfo` string Any additional metadata the user wants to include for the
dynamic value.

`fieldName` string Required. The name of the field for the dynamic value.

`isDynamicUser` boolean Indicates whether the value should be retrieved as the user
running the dashboard ( `true` ) or not ( `false` ).

DashboardFilterColumn

DashboardFilterColumn represents a filter column in a dashboard.


Metadata Types Dashboard

**Field** **Field Type** **Description**

`column` string Required. The report column code for the filter.

DashboardTableColumn

DashboardTableColumn represents a column in a customized table component in a dashboard.

**Field** **Field Type** **Description**

`aggregateType` ReportSummaryType[] Specifies the aggregation type for the table column.
(enumeration of type string)

`column` string Required. The label of the column to use in the table.

`showTotal` boolean

Displays the totals for each summarizable column in the
dashboard table. This field is available in API version 19.0 and
later.

`sortBy` DashboardComponentSection(enumeration The sort option for the dashboard table component. Sort on just
of type string) one column per table.

DashboardFlexTableComponentProperties

DashboardFlexTableComponentProperties represents a column in a customized table component in a dashboard.

**Field** **Field Type** **Description**

`flexTableColumn` DashboardComponentColumn Represents a column in a Lightning Experience table component.
This field is available in API version 41.0 and later.

`flexTableSortInfo` DashboardComponentSortInfo

`hideChatterPhotos` boolean

Represents sorting column and order in a Lightning Experience
table component. This field is available in API version 41.0 and
later.

If `true`, hides any photos from Chatter feeds.

This field is available in API version 41.0 and later.

`decimalPrecision` integer For columns with numeric values, indicates the number of
significant digits.

`useReportTableSetting` boolean

If `true`, users can import report table settings to this
component.

This field is available in API version 65.0 and later.

DashboardComponentGroupingSortProperties

DashboardComponentGroupingSortProperties is composed of multiple elements of the type DashboardComponentGroupingSort.


Metadata Types Dashboard

**Field** **Field Type** **Description**

`groupingSorts` DashboardComponentGroupingSort

DashboardComponentGroupingSort

This field stores sort information for a dashboard at each
grouping level of granularity. This field is available in API version
46.0 and later.

DashboardComponentGroupingSort specifies properties for sorting on a dashboard component group.

**Field** **Field Type** **Description**

`groupingLevel` String Grouping at which this sort configuration is applied.

`inheritedReportGroupingSort` String `true` if the sort order is picked up from an underlying report
for this grouping level.

`sortColumn` String

If grouping is sorted by an aggregate, this value is the aggregate
value (such as `sortColumn` ). If the grouping is sorted by its
own value, this field is null.

`sortOrder` String `Ascending` or `Descending` to reflect the sort order.

DashboardComponentColumn

DashboardComponentColumn represents a component column in a dashboard. Available in API version 41.0 and later.

**Field** **Field Type** **Description**

`breakPoint1` double The value that separates the `lowRangeColor` from the
`midRangeColor` on the dashboard.

`breakPoint2` double The value that separates the `midRangeColor` from the
`highRangeColor` on the dashboard.

`breakPointOrder` double Conditional highlighting can be applied to multiple columns.
This field stores the order of conditional highlights.

`highRangeColor` int The color representing a high number range on the column.

`lowRangeColor` int The color representing a low number range on the column.

`midRangeColor` int The color representing a mid number range on the column.

`reportColumn` string Required. The report column code for the filter.

`showTotal` boolean If `true`, the column total is displayed.

`type` DashboardComponentColumnType Represents the type of Lightning Experience table column:
(enumeration of type string)

**•** `Details`

**•** `Aggregates`

**•** `Grouping`


Metadata Types Dashboard

**Field** **Field Type** **Description**

This field is available in API version 41.0 and later.

DashboardComponentSortInfo

DashboardFilterColumns represents a filter column in a dashboard.

**Field** **Field Type** **Description**

`ComponentSortColumn` string Indicates the column on which the table is sorted. This field is
available in API version 41.0 and later.

`sortOrder` string Indicates whether column sorting is ascending or descending.
This field is available in API version 41.0 and later.

DashboardComponentSection

DashboardComponentSection represents one of the sections or columns in a dashboard.

**Field** **Field Type** **Description**

`columnSize` DashboardComponentSize Required. The size of the column in the dashboard:
(enumeration of type string)

**•** `Medium`

**•** `Narrow`

**•** `Wide`

`components` DashboardComponent[] The list of DashboardComponent objects in the dashboard
column.

DashboardComponentFilter

DashboardComponentFilter is an enumeration of type string that lists the sort values for dashboard components. The valid values are:

**Enumeration Value** **Description**

`RowLabelAscending` Sorts in alphabetical order by the label.

`RowLabelDescending` Sorts in reverse alphabetical order by the label.

`RowValueAscending` Sorts lowest to highest by the value.

`RowValueDescending` Sorts highest to lowest by the value.


Metadata Types Dashboard

Declarative Metadata Sample Definition — Filtered Dashboard

A sample XML definition of a filtered dashboard is shown below. Note that this example is supported in API version 24.0 and later. The
file name matches the dashboard title and the extension is `.dashboard` .

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Dashboard xmlns="http://soap.sforce.com/2006/04/metadata">

      <backgroundEndColor>#FFFFFF</backgroundEndColor>

      <backgroundFadeDirection>Diagonal</backgroundFadeDirection>

      <backgroundStartColor>#FFFFFF</backgroundStartColor>

      <dashboardFilters>

        <dashboardFilterOptions>

           <operator>equals</operator>

           <values>Media</values>

        </dashboardFilterOptions>

        <dashboardFilterOptions>

           <operator>lessThan</operator>

           <values>Working</values>

        </dashboardFilterOptions>

        <dashboardFilterOptions>

           <operator>between</operator>

           <values>ABC</values>

           <values>XYZ</values>

        </dashboardFilterOptions>

        <name>Industry</name>

      </dashboardFilters>

      <dashboardFilters>

        <dashboardFilterOptions>

           <operator>equals</operator>

           <values>Analyst,Partner</values>

        </dashboardFilterOptions>

        <dashboardFilterOptions>

           <operator>startsWith</operator>

           <values>Integrator</values>

        </dashboardFilterOptions>

        <name>Account Type</name>

      </dashboardFilters>

      <dashboardType>SpecifiedUser</dashboardType>

      <leftSection>

        <columnSize>Medium</columnSize>

        <components>

           <chartAxisRange>Auto</chartAxisRange>

           <componentType>Bar</componentType>

           <dashboardFilterColumns>

             <column>INDUSTRY</column>

           </dashboardFilterColumns>

           <dashboardFilterColumns>

             <column>TYPE</column>

           </dashboardFilterColumns>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>false</drillEnabled>

           <drillToDetailEnabled>false</drillToDetailEnabled>

           <enableHover>false</enableHover>

           <expandOthers>false</expandOthers>

           <legendPosition>Bottom</legendPosition>

```


Metadata Types Dashboard

```
           <report>unfiled$public/SampleReportofAccounts</report>

           <showPercentage>false</showPercentage>

           <showPicturesOnCharts>false</showPicturesOnCharts>

           <showValues>false</showValues>

           <sortBy>RowLabelAscending</sortBy>

           <useReportChart>false</useReportChart>

        </components>

      </leftSection>

      <middleSection>

        <columnSize>Medium</columnSize>

        <components>

           <chartAxisRange>Auto</chartAxisRange>

           <componentType>Funnel</componentType>

           <dashboardFilterColumns>

             <column>ACCOUNT_INDUSTRY</column>

           </dashboardFilterColumns>

           <dashboardFilterColumns>

             <column>ACCOUNT.TYPE</column>

           </dashboardFilterColumns>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>false</drillEnabled>

           <drillToDetailEnabled>false</drillToDetailEnabled>

           <enableHover>false</enableHover>

           <expandOthers>false</expandOthers>

           <legendPosition>Bottom</legendPosition>

           <report>unfiled$public/SampleReportofCases</report>

           <showPercentage>false</showPercentage>

           <showValues>true</showValues>

           <sortBy>RowLabelAscending</sortBy>

           <useReportChart>false</useReportChart>

        </components>

      </middleSection>

      <rightSection>

        <columnSize>Medium</columnSize>

        <components>

           <chartAxisRange>Auto</chartAxisRange>

           <componentType>Column</componentType>

           <dashboardFilterColumns>

             <column>INDUSTRY</column>

           </dashboardFilterColumns>

           <dashboardFilterColumns>

             <column>ACCOUNT_TYPE</column>

           </dashboardFilterColumns>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>false</drillEnabled>

           <drillToDetailEnabled>false</drillToDetailEnabled>

           <enableHover>false</enableHover>

           <expandOthers>false</expandOthers>

           <legendPosition>Bottom</legendPosition>

           <report>unfiled$public/SampleReportofOpportunities</report>

           <showPercentage>false</showPercentage>

           <showValues>false</showValues>

           <sortBy>RowLabelAscending</sortBy>

           <useReportChart>false</useReportChart>

```


Metadata Types Dashboard

```
        </components>

      </rightSection>

      <runningUser>admin@TESTORGNUM</runningUser>

      <textColor>#000000</textColor>

      <title>My Dashboard</title>

      <titleColor>#000000</titleColor>

      <titleSize>12</titleSize>

   </Dashboard>

```

Declarative Metadata Sample Definition — Unfiltered Dashboard

A sample XML definition of a dashboard is shown below. The file name matches the dashboard title and the extension is `.dashboard` .

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Dashboard xmlns="http://soap.sforce.com/2006/04/metadata">

      <backgroundEndColor>#FFFFFF</backgroundEndColor>

      <backgroundFadeDirection>LeftToRight</backgroundFadeDirection>

      <backgroundStartColor>#FFFFFF</backgroundStartColor>

      <description>Dashboard with all possible chart types</description>

      <leftSection>

        <columnSize>Medium</columnSize>

        <components>

           <chartAxisRange>Auto</chartAxisRange>

           <componentType>BarStacked100</componentType>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>true</drillEnabled>

           <enableHover>true</enableHover>

           <report>testFolder/sourceRep</report>

           <sortBy>RowLabelAscending</sortBy>

        </components>

        <components>

           <componentType>Table</componentType>

           <dashboardTableColumn>

             <column>CLOSE_DATE</column>

             <sortBy>RowLabelAscending</sortBy>

           </dashboardTableColumn>

           <dashboardTableColumn>

             <aggregateType>Sum</aggregateType>

             <column>AMOUNT</column>

             <showTotal>true</showTotal>

           </dashboardTableColumn>

           <dashboardTableColumn>

             <column>STAGE_NAME</column>

           </dashboardTableColumn>

           <dashboardTableColumn>

             <column>PROBABILITY</column>

             <aggregateType>Maximum</aggregateType>

           </dashboardTableColumn>

           <displayUnits>Integer</displayUnits>

           <header>Opportunities Table</header>

           <indicatorHighColor>#54C254</indicatorHighColor>

           <indicatorLowColor>#C25454</indicatorLowColor>

           <indicatorMiddleColor>#C2C254</indicatorMiddleColor>

           <maxValuesDisplayed>10</maxValuesDisplayed>

```


Metadata Types Dashboard

```
           <report>testFolder/sourceRep</report>

        </components>

        <components>

           <chartAxisRange>Auto</chartAxisRange>

           <componentType>Bar</componentType>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>true</drillEnabled>

           <enableHover>true</enableHover>

           <report>testFolder/sourceRep</report>

           <sortBy>RowLabelAscending</sortBy>

        </components>

        <components>

           <chartAxisRange>Auto</chartAxisRange>

           <componentType>Column</componentType>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>true</drillEnabled>

           <legendPosition>Bottom</legendPosition>

           <report>testFolder/sourceRep</report>

           <sortBy>RowLabelAscending</sortBy>

           <useReportChart>true</useReportChart>

        </components>

        <components>

           <chartAxisRange>Auto</chartAxisRange>

           <componentType>Funnel</componentType>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>true</drillEnabled>

           <enableHover>true</enableHover>

           <expandOthers>true</expandOthers>

           <legendPosition>Bottom</legendPosition>

           <report>testFolder/sourceRep</report>

           <sortBy>RowLabelAscending</sortBy>

        </components>

      </leftSection>

      <middleSection>

        <columnSize>Medium</columnSize>

        <components>

           <chartAxisRange>Auto</chartAxisRange>

           <componentType>ColumnStacked100</componentType>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>true</drillEnabled>

           <enableHover>true</enableHover>

           <report>testFolder/sourceRep</report>

           <sortBy>RowLabelAscending</sortBy>

        </components>

        <components>

           <chartAxisRange>Auto</chartAxisRange>

           <componentType>ColumnStacked</componentType>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>true</drillEnabled>

           <enableHover>true</enableHover>

           <report>testFolder/sourceRep</report>

           <sortBy>RowLabelAscending</sortBy>

        </components>

        <components>

```


Metadata Types Dashboard

```
           <chartAxisRange>Auto</chartAxisRange>

           <componentType>ColumnStacked</componentType>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>true</drillEnabled>

           <enableHover>true</enableHover>

           <report>testFolder/sourceRep</report>

           <sortBy>RowLabelAscending</sortBy>

        </components>

        <components>

           <chartAxisRange>Auto</chartAxisRange>

           <componentType>ColumnGrouped</componentType>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>true</drillEnabled>

           <enableHover>true</enableHover>

           <report>testFolder/sourceRep</report>

           <sortBy>RowLabelAscending</sortBy>

        </components>

        <components>

           <chartAxisRange>Auto</chartAxisRange>

           <componentType>Column</componentType>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>true</drillEnabled>

           <enableHover>true</enableHover>

           <report>testFolder/sourceRep</report>

           <sortBy>RowLabelAscending</sortBy>

        </components>

      </middleSection>

      <rightSection>

        <columnSize>Medium</columnSize>

        <components>

           <chartAxisRange>Auto</chartAxisRange>

           <componentType>Bar</componentType>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>true</drillEnabled>

           <enableHover>true</enableHover>

           <report>testFolder/sourceRep</report>

           <sortBy>RowLabelAscending</sortBy>

        </components>

        <components>

           <chartAxisRange>Auto</chartAxisRange>

           <componentType>Pie</componentType>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>true</drillEnabled>

           <enableHover>true</enableHover>

           <expandOthers>true</expandOthers>

           <report>testFolder/sourceRep</report>

           <sortBy>RowLabelAscending</sortBy>

        </components>

        <components>

           <chartAxisRange>Auto</chartAxisRange>

           <componentType>LineGroupedCumulative</componentType>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>true</drillEnabled>

           <enableHover>true</enableHover>

```


Metadata Types Dashboard

```
           <report>testFolder/sourceRep</report>

           <sortBy>RowLabelAscending</sortBy>

        </components>

        <components>

           <chartAxisRange>Auto</chartAxisRange>

           <componentType>LineGrouped</componentType>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>true</drillEnabled>

           <enableHover>true</enableHover>

           <report>testFolder/sourceRep</report>

           <sortBy>RowLabelAscending</sortBy>

        </components>

        <components>

           <chartAxisRange>Auto</chartAxisRange>

           <componentType>LineCumulative</componentType>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>true</drillEnabled>

           <enableHover>true</enableHover>

           <report>testFolder/sourceRep</report>

           <sortBy>RowLabelAscending</sortBy>

        </components>

        <components>

           <chartAxisRange>Auto</chartAxisRange>

           <componentType>Donut</componentType>

           <displayUnits>Auto</displayUnits>

           <drillEnabled>true</drillEnabled>

           <enableHover>true</enableHover>

           <expandOthers>true</expandOthers>

           <report>testFolder/sourceRep</report>

           <sortBy>RowLabelAscending</sortBy>

        </components>

      </rightSection>

      <runningUser>admin@TESTORGNUM</runningUser>

      <textColor>#000000</textColor>

      <title>Db Title</title>

      <titleColor>#000000</titleColor>

      <titleSize>12</titleSize>

   </Dashboard>

```

Declarative Metadata Sample Definition — Lightning Experience Dashboard
with **`isGridLayout`** Equals **`true`**

A sample XML definition of a Lightning Experience dashboard with `isGridLayout` equals `true` is shown below. Note that this
example is supported in API version 35.0 and later. The file name matches the dashboard title and the extension is `.dashboard` .

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Dashboard xmlns="http://soap.sforce.com/2006/04/metadata">

      <backgroundEndColor>#FFFFFF</backgroundEndColor>

      <backgroundFadeDirection>Diagonal</backgroundFadeDirection>

      <backgroundStartColor>#FFFFFF</backgroundStartColor>

      <dashboardType>SpecifiedUser</dashboardType>

      <gridLayout>

        <dashboardGridComponents>

```


Metadata Types Dashboard

```
           <colSpan>3</colSpan>

           <columnIndex>0</columnIndex>

           <dashboardComponent>

             <autoselectColumnsFromReport>false</autoselectColumnsFromReport>

             <chartAxisRange>Auto</chartAxisRange>

             <chartSummary>

               <axisBinding>y</axisBinding>

               <column>RowCount</column>

             </chartSummary>

             <componentType>Donut</componentType>

             <drillEnabled>false</drillEnabled>

             <drillToDetailEnabled>false</drillToDetailEnabled>

             <enableHover>false</enableHover>

             <expandOthers>false</expandOthers>

             <groupingColumn>TITLE</groupingColumn>

             <legendPosition>Bottom</legendPosition>

             <report>unfiled$public/lead_rpt</report>

             <showPercentage>false</showPercentage>

             <showTotal>false</showTotal>

             <showValues>true</showValues>

             <sortBy>RowLabelAscending</sortBy>

             <useReportChart>false</useReportChart>

           </dashboardComponent>

           <rowIndex>0</rowIndex>

           <rowSpan>3</rowSpan>

        </dashboardGridComponents>

        <dashboardGridComponents>

           <colSpan>3</colSpan>

           <columnIndex>0</columnIndex>

           <dashboardComponent>

             <autoselectColumnsFromReport>false</autoselectColumnsFromReport>

             <chartAxisRange>Auto</chartAxisRange>

             <chartSummary>

               <axisBinding>y</axisBinding>

               <column>RowCount</column>

             </chartSummary>

             <componentType>Pie</componentType>

             <drillEnabled>false</drillEnabled>

             <drillToDetailEnabled>false</drillToDetailEnabled>

             <enableHover>false</enableHover>

             <expandOthers>false</expandOthers>

             <groupingColumn>TITLE</groupingColumn>

             <legendPosition>Bottom</legendPosition>

             <report>unfiled$public/lead_rpt</report>

             <showPercentage>false</showPercentage>

             <showValues>true</showValues>

             <sortBy>RowLabelAscending</sortBy>

             <useReportChart>false</useReportChart>

           </dashboardComponent>

           <rowIndex>3</rowIndex>

           <rowSpan>3</rowSpan>

        </dashboardGridComponents>

        <dashboardGridComponents>

           <colSpan>3</colSpan>

```


### Metadata Types DataCategoryGroup

```
           <columnIndex>0</columnIndex>

           <dashboardComponent>

             <autoselectColumnsFromReport>false</autoselectColumnsFromReport>

             <chartAxisRange>Auto</chartAxisRange>

             <chartSummary>

               <axisBinding>y</axisBinding>

               <column>RowCount</column>

             </chartSummary>

             <componentType>Column</componentType>

             <drillEnabled>false</drillEnabled>

             <drillToDetailEnabled>false</drillToDetailEnabled>

             <enableHover>false</enableHover>

             <expandOthers>false</expandOthers>

             <groupingColumn>TITLE</groupingColumn>

             <legendPosition>Bottom</legendPosition>

             <report>unfiled$public/lead_rpt</report>

             <showPercentage>false</showPercentage>

             <showValues>false</showValues>

             <sortBy>RowLabelAscending</sortBy>

             <useReportChart>false</useReportChart>

           </dashboardComponent>

           <rowIndex>9</rowIndex>

           <rowSpan>3</rowSpan>

        </dashboardGridComponents>

        <numberOfColumns>9</numberOfColumns>

        <rowHeight>90</rowHeight>

      </gridLayout>

      <isGridLayout>true</isGridLayout>

      <runningUser>admin@s1.com</runningUser>

      <textColor>#000000</textColor>

      <title>sfx</title>

      <titleColor>#000000</titleColor>

      <titleSize>12</titleSize>

   </Dashboard>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

Folder

Report

### DataCategoryGroup

Represents a data category group.

This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types DataCategoryGroup

Warning: Using Metadata API to deploy category changes from one organization to another permanently removes categories
and record categorizations that are not specified in your XML file. Salesforce recommends that you manually create data categories
and record associations in an organization from Setup by entering _`Data Categories`_ in the `Quick Find` box, then
selecting **Data Categories** rather than deploying changes from a sandbox to a production organization. For more information,
see Usage.

Data category groups are provided to:

**•** Classify and filter data.

**•** Share data among users.

Every data category group contains items or data categories that can be organized hierarchically.

The example below shows the `Geography` data category group and its data categories.

```
   Geography

      Worldwide

        North America

           United States of America

           Canada

           Mexico

        Europe

        Asia

```

Note: See "Work with Data Categories" in the Salesforce online help for more information on data category groups, data categories,
parent and sub categories.

File Suffix and Directory Location

The file suffix is `.datacategorygroup` . There is one file for each data category group stored in the `datacategorygroups`
folder in the corresponding package directory.

Version

Data category groups are available in API version 18.0 and later.

Fields

This metadata type contains the following fields:

**Field Name** **Field Type** **Description**

`active` boolean Required. The status of the category group. Indicates whether this
category group is active, ( `true` ), or not active ( `false` ).

`dataCategory` DataCategory on Required. The top-level category within the data category group.
page 866

`description` string The description of the data category group.

`fullName` string Required. The unique name of the data category group. When creating
a data category group, the `fullName` field and the file name (without

its suffix) must match.The `fullName` can contain only underscores


Metadata Types DataCategoryGroup

**Field Name** **Field Type** **Description**

and alphanumeric characters. It must be unique, begin with a letter, not
include spaces, not end with an underscore, and not contain two
consecutive underscores. This field is inherited from the Metadata
component.

`label` string Required. Label that represents the object in Salesforce.

`objectUsage` ObjectUsage on The objects that are associated with the data category group.
page 866

DataCategory

Represents an item (or data category) in the data category group. A data category can recursively contain a list of other data categories.

**Field Name** **Field Type** **Description**

`dataCategory` DataCategory[]

A recursive list of sub data categories. For example, a list of countries
within a continent. You can create up to 100 categories in a data category
group and have up to 5 levels in a data category group hierarchy.

`label` string Required. Label for the data category throughout the Salesforce user
interface.

`name` string Required. The developer name of the data category used as a unique
identifier for API access. The name can only contain characters, letters,

and the underscore (_) character, must start with a letter, and cannot
end with an underscore or contain two consecutive underscore
characters.

Important: The value for this field is defined once and cannot
be changed later.

Warning: If you deploy a category group that already exists in
an organization, any category that is not defined in the XML file
is permanently removed from your organization. For more
information see Usage.

ObjectUsage

Represents the objects that can be associated with the data category group. This association allows the object to be classified and filtered
using the data categories.

**Field Name** **Field Type** **Description**

`object` string[] A list of the object names that can be associated with the data category
group. Valid values are:

**•** `KnowledgeArticleVersion` —to associate articles. See
"Modify Default Category Group Assignments for Articles" in the


Metadata Types DataCategoryGroup

**Field Name** **Field Type** **Description**

Salesforce online help for more information on data category groups
association to articles.

**•** `Question` —to associate questions. You can associate the
`Question` object with at most one category group.

Warning: If you deploy a category group that already exists in
an organization, any object association that is not defined in the
XML file is permanently removed from your organization. Ensure
that your XML file specifies all the records associated with your
category group in the organization. For more information see
Usage.

Declarative Metadata Sample Definition

This sample is the definition of the `Geography` data category group and its data categories:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <DataCategoryGroup xmlns="http://soap.sforce.com/2006/04/metadata">

     <label>Geography</label>

     <description>Geography structure of service center locations</description>

     <fullName>geo</fullName>

     <dataCategory> <name>WW</name> <label>Worldwide</label>

       <dataCategory> <name>AMER</name> <label>North America</label>

         <dataCategory>

           <name>USA</name>

           <label>United States of America</label>

         </dataCategory>

         <dataCategory>

           <name>CAN</name>

           <label>Canada</label>

         </dataCategory>

         <dataCategory>

           <name>MEX</name>

           <label>Mexico</label>

         </dataCategory>

       </dataCategory>

       <dataCategory> <name>EMEA</name> <label>Europe, Middle East, Africa</label>

         <dataCategory>

           <name>FR</name>

           <label>France</label>

         </dataCategory>

         <dataCategory>

           <name>SP</name>

           <label>Spain</label>

        </dataCategory>

         <dataCategory>

           <name>UK</name>

           <label>United-Kingdom</label>

         </dataCategory>

```


Metadata Types DataCategoryGroup

```
       </dataCategory>

       <dataCategory>

         <name>APAC</name>

         <label>Asia</label>

       </dataCategory>

     </dataCategory>

     <objectUsage>

       <object>KnowledgeArticleVersion </object>

     <objectUsage>

   </DataCategoryGroup>

```

Usage

When you deploy a category group XML file, Metadata API checks whether the category group exists in the target organization. If the
category group does not exist, it is created. If the category group already exists, then Metadata API:

**•** Adds any new category or object defined in the XML file.

**•** Deletes any category that is not defined in the XML file. Records associated with the deleted categories are re-associated with the
parent category.

**•** Deletes any object association that is not defined in the XML file.

**•** Moves any category if its hierarchical position differs from the position specified in the XML file.

Note: When a category moves to a new parent category, users that have no visibility on the new parent category lose their
visibility to the repositioned category.

Note: For more information about category deletion, category repositioning and its impact on record categorization and visibility
see "Delete a Data Category" and "Modify and Arrange Data Categories" in the Salesforce online help.

Using Metadata API to deploy category changes from one organization to another permanently removes categories and record
categorizations that are not specified in your XML file. Salesforce recommends that you manually create data categories and record
associations in an organization from Setup by entering _`Data Categories`_ in the `Quick Find` box, then selecting **Data**
**Categories** rather than deploying changes from a sandbox to a production organization.

The following example illustrates what happens if you deploy an XML representation of a `Geography` data category group hierarchy
to an organization that already has this data category group defined. Note that the organization contains a `US` category, while the XML
file includes a `USA` category in the same hierarchical position. The Metadata API deployment process deletes the `US` category from
the organization and moves associations for any records from `US` to the parent `AMER` category. It also adds the `USA` category under
`AMER` . Note that all records that were previously categorized with `US` are now associated with the `AMER` category.


Metadata Types DataCategoryGroup

The next example illustrates what can happen when you delete or move a category in a data category group and deploy its XML
representation from a sandbox to a production organization that already has this data category group defined. Hierarchy 1 shows the
initial data category group in the sandbox organization. In hierarchy 2, we add an `EU` category under `EMEA` and move `FR`, `SP` and
`UK` below `EU` . In hierarchy 3, we delete `FR` and associate its records with its new parent, `EU` . Finally, we deploy the changes from the
sandbox to the production organization.


### Metadata Types DataObjectSearchIndexConf

Metadata API has no concept of the order of the changes made to the sandbox organization. It just deploys the changes from one
organization to another. During the deployment, it first notices the deletion of the `FR` category and removes it from the production
organization. Consequently, it moves associations for any records from `FR` to its parent on the production organization, `EMEA` . Metadata
API then adds the `EU` category and moves `SP` and `UK` below it. Although the category group hierarchy looks the same in both
organizations, record categorization in production is different from the sandbox organization. The records that were originally associated
with `FR` in hierarchy 1 are associated with `EU` in the sandbox organization, but are associated with `EMEA` in the production organization.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### DataObjectSearchIndexConf

Represents the source Data 360 data model object (DMO) for Search Answers and holds the search index that Search Answers uses
when searching DMO records.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### DataObjectSearchIndexConf components have the suffix .dataObjectSearchIndexConf and are stored in the

`dataObjectSearchIndexConfs` folder.


Metadata Types DataObjectSearchIndexConf

Version

DataObjectSearchIndexConf components are available in API version 63.0 and later.

Special Access Rules

To access this metadata type, you must have the Customize Application user permission. The Salesforce org must have a Data 360 license.

Fields

**Field Name** **Description**

```
application

channel

masterLabel

nameFieldReference

objectReference

retriever

```

**Field Type**
string

**Description**
Required.

The name of the app that the Search Answers index is associated with.

**Field Type**
string

**Description**
The search channel that the Search Answers configuration applies to.

**Field Type**
string

**Description**
Required.

The name of the Search Answers configuration.

**Field Type**
string

**Description**
Required.

The name field of the DMO selected as a source for Search Answers.

**Field Type**
string

**Description**
Required.

The DMO that the Search Answers configuration applies to.

**Field Type**
string


### Metadata Types DataWeaveResource

**Field Name** **Description**

**Description**
The retriever that accesses the Search Answers indexed data.

```
searchIndex

```

**Field Type**
string

**Description**
Required.

The name of the search index mapped to the DMO.

Declarative Metadata Sample Definition

The following is an example of a DataObjectSearchIndexConf component.

```
<?xml version="1.0" encoding="UTF-8"?>

<DataObjectSearchIndexConf xmlns="http://soap.sforce.com/2006/04/metadata">

 <application>SearchAnswers</application>

 <channel>SharedIndex</channel>

 <masterLabel>SearchAnswers</masterLabel>

 <nameFieldReference>Name__c</nameFieldReference>

 <objectReference>Account__dlm</objectReference>

 <searchIndex>searchAnswersIndex</searchIndex>

</DataObjectSearchIndexConf>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

  <types>

     <members>*</members>

     <name>DataObjectSearchIndexConf</name>

  </types>

  <version>63.0</version>

</Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### DataWeaveResource

Represents the `DataWeaveScriptResource` class that is generated for all DataWeave scripts. DataWeave scripts can be directly
invoked from Apex.


Metadata Types DataWeaveResource

Parent Type

This type extends the MetadataWithContent metadata type and inherits its `content` and `fullName` fields.

File Suffix and Directory Location

DataWeaveResource components have the suffix `.dwl` and are stored in the `dw` folder.

Version

DataWeaveResource components are available in API version 58.0 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Description**

```
apiVersion

isGlobal

isProtected

```

**Field Type**
double

**Description**
Required.

The API version for this component.

**Field Type**
boolean

**Description**
When set to `true`, the generated `DataWeaveScriptResource` class is global.

**Field Type**
boolean

**Description**
Not used.

Declarative Metadata Sample Definition

The following is an example of a DataWeaveResource component.

```
csvToContacts.dwl

%dw 2.0

input records application/csv

output application/apex

```


### Metadata Types DecisionTable

```
   --
   records map(record) -> {

    FirstName: record.first_name,

    LastName: record.last_name,

    Email: record.email

   } as Object {class: "Contact"}

   csvToContacts.dwl-meta.xml

   <?xml version="1.0" encoding="UTF-8"?>

   <DataWeaveResource xmlns="http://soap.sforce.com/2006/04/metadata">

      <apiVersion>58.0</apiVersion>

      <isGlobal>true</isGlobal>

   </DataWeaveResource>

```

The following is an example `package.xml` that references the csvToContacts definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package

       xmlns="http://soap.sforce.com/2006/04/metadata">

       <types>

           <members>csvToContacts</members>

           <name>DataWeaveResource</name>

       </types>

       <version>58.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### DecisionTable

Represents the information about a decision table.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### DecisionTable components have the suffix .decisionTable and are stored in the decisionTables folder.

Version

### DecisionTable components are available in API version 51.0 and later.


Metadata Types DecisionTable

Special Access Rules

To use this metadata type, your Salesforce org must have the Loyalty Management or the Rebate Management license.

Fields

**Field Name** **Description**

```
collectOperator

conditionCriteria

conditionType

dataSourceType

```

**Field Type**
DecisionTableCollectOperator (enumeration of type string)

**Description**
Specifies the operator that's used when the result is filtered by the Collect operator.

Valid values are:

**•** `Count`

**•** `Maximum`

**•** `Minimum`

**•** `None`

**•** `Sum`

**Field Type**
string

**Description**
Logic that's used to decide how the input fields are processed.

**Field Type**
DecisionTableConditionType (enumeration of type string)

**Description**
Condition logic that's used for input fields.

Valid values are:

**•** `All`

**•** `Any`

**•** `Custom`

**Field Type**
DecisionTableDataSourceType (enumeration of type string)

**Description**
Specifies the type of data source that's used to create a decision table.

Valid values are:

**•** `ContextDefinition`

**•** `CsvUpload`

**•** `MultipleSobjects`

**•** `SingleSobject`


Metadata Types DecisionTable

**Field Name** **Description**

```
decisionTableParameters

decisionTable

SourceCriterias

description

doesConsiderNullValue

downloadStatus

executionType

```

**Field Type**

DecisionTableParameter[]

**Description**
Parameters that you specify in a decision table.

**Field Type**

DecisionTableSourceCriteria[]

**Description**
The fields and values from a data source that are used to define the condition logic of
the data that's used in a decision table.

**Field Type**
string

**Description**
Description of the decision table.

**Field Type**
boolean

**Description**
Indicates whether a column that has a null value is considered for lookup ( `true` ) or
not ( `false` ). The default value is false.

**Field Type**
DecisionTableDownloadStatus (enumeration of type string)

**Description**
Specifies the progress status of a CSV download from a CSV-based lookup table.
Available in API version 64.0 and later.

Valid values are:

**•** `Completed`

**•** `DownloadInProgress`

**•** `Failed`

**Field Type**
DecisionTableExecutionType (enumeration of type string)

**Description**
Indicates the backing storage for the Decision Table.

Valid values are:

**•** `Dmo`

**•** `Hbase`

**•** `Hbpo`

**•** `Solr`


Metadata Types DecisionTable

**Field Name** **Description**

**•** `Soql`

Execution type of `Hbase` must be passed in all caps ( `HBASE` ) in POST and PATCH
calls.

```
filterResultBy

hasIncrementalSyncFailed

isIncrementalSyncEnabled

lastIncrementalSyncDate

lastSyncDate

refreshFailureReason

```

**Field Type**
DecisionTableHitPolicy (enumeration of type string)

**Description**
Specifies how the results of a decision table are filtered if a set of inputs returns multiple
matching outputs.

Valid values are:

**•** `AnyValue`

**•** `CollectOperator`

**•** `FirstMatch`

**•** `OutputOrder`

**•** `Priority`

**•** `RuleOrder`

**•** `UniqueValues`

**Field Type**
boolean

**Description**
Indicates if the last incremental refresh failed.

**Field Type**
boolean

**Description**
Indicates if incremental refresh is enabled for the Decision Table.

**Field Type**
string

**Description**
The date and time on which the last incremental refresh occured for the decision table.

**Field Type**
string

**Description**
Latest date on which the decision table was refreshed.

**Field Type**
string


Metadata Types DecisionTable

**Field Name** **Description**

**Description**
Reason why the refresh of the decision table data failed.

```
refreshStatus

setupName

sourceConditionLogic

sourceObject

status

```

**Field Type**
DecisionTableRefreshStatus (enumeration of type string)

**Description**
Specifies the refresh status of the cached data in the decision table.

Valid values are:

**•** `Completed`

**•** `Failed`

**•** `InProgress`

**•** `Initiated`

**Field Type**
string

**Description**

Required. Name of the decision table, which appears in Salesforce Setup.

**Field Type**
string

**Description**
The condition logic that's used to define the decision table from the source data.

**Field Type**
string

**Description**

Required. Object that contains the rules based on which the decision table must
provide outcomes.

**Field Type**
DecisionTableStatus (enumeration of type string)

**Description**

Required. Status of the decision table.

Valid values are:

**•** `ActivationInProgress`

**•** `Active`

**•** `Draft`

**•** `Inactive`


Metadata Types DecisionTable

**Field Name** **Description**

```
type

uploadStatus

usageType

```

**Field Type**
DecisionTableType (enumeration of type string)

**Description**
Stores the type of decision table.

Valid values are:

**•** `Advanced`

**•** `HighScaleExecution`

**•** `HighVolume`

**•** `LowVolume`

**•** `MediumVolume`

**•** `RealTime`

**Field Type**
DecisionTableUploadStatus (enumeration of type string)

**Description**
Specifies the progress status of the CSV upload for a CSV based Lookup table.

Valid values are:

**•** `Completed`

**•** `CompletedWithErrors`

**•** `Failed`

**•** `UploadInProgress`

**Field Type**
ExpsSetProcessType (enumeration of type string)

**Description**
Type of industry or the application within the industry that's using a decision table.

Valid values are:

**•** `Bre`

**•** `ComplianceControl`

**•** `DecompositionEnrichmentMapping`

**•** `DefaultPricing`

**•** `DefaultRating`

**•** `EventOrchestration`

**•** `FinancialServicesCloud`

**•** `FulfillmentCondition`

**•** `GpaCalculation`

**•** `InsuranceClaimProcessing` —Available in API version 65.0 and later.

**•** `ItServiceManagement` —Available in API version 65.0 and later.

**•** `PlanCostCalculation`


Metadata Types DecisionTable

**Field Name** **Description**

**•** `PriceProtection`

**•** `PricingDiscovery`

**•** `ProductCategoryQualification`

**•** `ProductQualification`

**•** `RatingDiscovery`

**•** `RecordAlert`

**•** `ShipAndDebit`

**•** `StudentInformationSystem` —Available in API version 65.0 and later.

**•** `StudentSuccess`

**•** `TestProcess`

**•** `WarrantyClaim`

When Business Rules Engine is enabled for a Salesforce instance, the default value is
' `Bre` ’. Other usage types are available to you depending on your industry solution
and permission sets.

DecisionTableParameter

Represents an input or output field of a decision table.

**Field Name** **Description**

```
dataType

decimalScale

```

**Field Type**
DTParameterDataType (enumeration of type string)

**Description**
The data type of the field used in a decision table.

Valid values are:

**•** `Boolean`

**•** `Currency`

**•** `Date`

**•** `DateTime`

**•** `Number`

**•** `Percent`

**•** `String`

**Field Type**
int

**Description**
The number of digits to the right of the decimal point.


Metadata Types DecisionTable

**Field Name** **Description**

```
domainObject

fieldName

fieldPath

isGroupByField

isPriorityField

isRequired

length

operator

```

**Field Type**
string

**Description**
For polymorhpic fields, indicates the domain object in the field hierarchy.

**Field Type**
string

**Description**

Required. API name of the fields that selected as an input or output for the decision
table.

**Field Type**
string

**Description**
The path of the field used in a decision table in relation to the object that the field
belongs to.

**Field Type**
boolean

**Description**
Indicates whether an input field is used to group the business rules of the decision
table.

**Field Type**
boolean

**Description**
Indicates whether a field is given priority.

**Field Type**
boolean

**Description**
Indicates whether a field is required to be used for lookups.

**Field Type**
int

**Description**
The maximum number of characters supported for a field that's used in a decision
table.

**Field Type**
DecisionTableOperator (enumeration of type string)


Metadata Types DecisionTable

**Field Name** **Description**

**Description**
Operator used for the input field.

Valid values are:

**•** `Contains`

**•** `DoesNotExistIn`

**•** `DoesNotMatch`

**•** `Equals`

**•** `ExistsIn`

**•** `GreaterOrEqual`

**•** `GreaterThan`

**•** `IsNotNull`

**•** `IsNull`

**•** `LessOrEqual`

**•** `LessThan`

**•** `Matches`

**•** `NotEquals`

```
sequence

sortType

usage

```

**Field Type**
int

**Description**
The sequence in which input fields are processed. This field is available in API version
52.0 and later.

**Field Type**
DecisionTableSortType (enumeration of type string)

**Description**
Sort outputs of a decision table based on the values of the input or output parameter
field. This field is available in API version 56.0 and later.

Valid values are:

**•** `AscNullFirst`

**•** `AscNullLast`

**•** `DescNullFirst`

**•** `DescNullLast`

**•** `None`

**Field Type**
DecisionTableParameterType (enumeration of type string)

**Description**

Required. Usage type of a field.


Metadata Types DecisionTable

**Field Name** **Description**

Valid values are:

**•** `INPUT`

**•** `OUTPUT`

**•** `ROWCRITERIA`

DecisionTableSourceCriteria

Represents the fields and values from a data source that are used to define the condition logic of the data that's used in a decision table.

**Field Name** **Description**

```
operator

sequenceNumber

sourceFieldName

```

**Field Type**
DTSourceCriteriaOperator (enumeration of type string)

**Description**

Required. The operator that’s applied to an associated decision table’s field to filter
the data.

Valid values are:

**•** `Contains`

**•** `DoesNotExistIn`

**•** `DoesNotMatch`

**•** `Equals`

**•** `ExistsIn`

**•** `GreaterOrEqual`

**•** `GreaterThan`

**•** `IsNotNull`

**•** `IsNull`

**•** `LessOrEqual`

**•** `LessThan`

**•** `Matches`

**•** `NotEquals`

**Field Type**
int

**Description**

Required. The sequence number used in the associated decision table's source condition
logic.

**Field Type**
string


Metadata Types DecisionTable

**Field Name** **Description**

**Description**

Required. The name of the field that's used in the decision table.

```
value

valueType

```

**Field Type**
string

**Description**
The value that’s expected in the source field used in the decision table.

**Field Type**
DTSourceCriteriaValueType (enumeration of type string)

**Description**

Required. The type of the value that’s used to filter the source data.

Valid values are:

**•** `Formula`

**•** `Literal`

**•** `Lookup`

**•** `Parameter`

**•** `Picklist`

Declarative Metadata Sample Definition

The following is an example of a DecisionTable component.

```
<?xml version="1.0" encoding="UTF-8"?>

<DecisionTable xmlns="http://soap.sforce.com/2006/04/metadata">

   <collectOperator>None</collectOperator>

   <conditionCriteria>1 and 2 and 3 and 4</conditionCriteria>

   <conditionType>All</conditionType>

   <dataSourceType>SingleSobject</dataSourceType>

   <decisionTableParameters>

     <fieldName>IsDeleted</fieldName>

     <operator>Equals</operator>

     <usage>INPUT</usage>

     <sequence>1</sequence>

     <isGroupByField>true</isGroupByField>

     <sortType>AscNullFirst</sortType>

     <dataType>Number</dataType>

     <fieldPath>AccountFeed.CommentsCount</fieldPath>

     <domainObject>AccountFeed</domainObject>

     <isPriorityField>false</isPriorityField>

     <decimalScale>2</decimalScale>

     <length>14</length>

     <isRequired>false</isRequired>

   </decisionTableParameters>

   <decisionTableParameters>

```


Metadata Types DecisionTable

```
        <fieldName>IsActive</fieldName>

        <usage>OUTPUT</usage>

      </decisionTableParameters>

      <decisionTableParameters>

        <fieldName>LimitNumber</fieldName>

        <operator>Equals</operator>

        <usage>INPUT</usage>

        <sequence>2</sequence>

        <isGroupByField>false</isGroupByField>

      </decisionTableParameters>

      <decisionTableParameters>

        <fieldName>LimitStartDate</fieldName>

        <usage>OUTPUT</usage>

      </decisionTableParameters>

      <decisionTableParameters>

        <fieldName>GivenBadgeCount</fieldName>

        <operator>Equals</operator>

        <usage>INPUT</usage>

        <sequence>3</sequence>

        <isGroupByField>false</isGroupByField>

      </decisionTableParameters>

      <decisionTableParameters>

        <fieldName>Name</fieldName>

        <operator>Equals</operator>

        <usage>INPUT</usage>

        <sequence>4</sequence>

        <isGroupByField>false</isGroupByField>

      </decisionTableParameters>

      <decisionTableSourceCriterias>

        <sourceFieldName>IsDeleted</sourceFieldName>

        <operator>Equals</operator>

        <value>false</value>

        <sequenceNumber>1</sequenceNumber>

        <valueType>Literal</valueType>

      </decisionTableSourceCriterias>

      <description>Sample DT created for md-common tests</description>

      <filterResultBy>UniqueValues</filterResultBy>

      <setupName>Sample DT</setupName>

      <sourceObject>WorkBadgeDefinition</sourceObject>

      <sourceConditionLogic>1</sourceConditionLogic>

      <status>Draft</status>

      <type>LowVolume</type>

      <usageType>Bre</usageType>

      <doesConsiderNullValue>false</doesConsiderNullValue>

      <refreshStatus>Failed</refreshStatus>

      <refreshFailureReason>Failed due to limit violation.</refreshFailureReason>

      <executionType>Hbpo</executionType>

      <lastIncrementalSyncDate>""</lastIncrementalSyncDate>

      <uploadStatus>Completed</uploadStatus>

      <isIncrementalSyncEnabled>false</isIncrementalSyncEnabled>

      <hasIncrementalSyncFailed>false</hasIncrementalSyncFailed>

   </DecisionTable>

```


### Metadata Types DecisionTableDatasetLink

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <fullName>Sample DT Package</fullName>

     <description>Package created for md-common tests</description>

     <types>

       <members>Sample_DT</members>

       <name>DecisionTable</name>

     </types>

     <types>

       <members>DSL_Sample</members>

       <members>Sample_DT_Default</members>

       <name>DecisionTableDatasetLink</name>

     </types>

     <version></version>

   </Package>

### DecisionTableDatasetLink

```

Represents the information about a dataset link associated with a decision table. In a dataset link, select an object for whose records,
the decision table must provide an outcome. This type extends the Metadata metadata type and inherits its `fullName` field.

Note: Dataset links are supported only for Standard decision tables.

File Suffix and Directory Location

### DecisionTableDatasetLink components have the suffix .decisionTableDatasetLink and are stored in the

`decisionTableDatasetLinks` folder.

Version

### DecisionTableDatasetLink components are available in API version 51.0 and later.

Special Access Rules

To use this metadata type, your Salesforce org must have the Loyalty Management or the Rebate Management license.

Fields

**Field Name** **Field Type** **Description**

`decisionTableName` string Required. The name of the associated decision table.

`decisionTblDatasetParameters` DecisionTblDatasetParameters Mapping between a decision table parameter and a field of the object
selected in the dataset link.

`description` string The description of the dataset link.


Metadata Types DecisionTableDatasetLink

**Field Name** **Field Type** **Description**

`isDefault` boolean Indicates whether a dataset link is the default dataset link for a decision
table.

`setupName` string Required. The name of the decision table dataset link, which appears in
Setup.

`sourceObject` string Required. The name of the object being evaluated.

DecisionTblDatasetParameters

Represents the mapping between a decision table parameter and a field of the object selected in the dataset link.

The mapping allows the decision table to know which object fields must be compared to the input-output fields of the decision table.

Fields

**Field Name** **Field Type** **Description**

`datasetFieldName` string Required. Name of the dataset field whose value must be compared against
an Input type decision table parameter when providing the outcome.

`fieldName` string Required. The API name of the decision table field that is selected as an input
or output for the decision table dataset link.

Declarative Metadata Sample Definition

The following is an example of a DecisionTableDatasetLink component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <DecisionTableDatasetLink xmlns="http://soap.sforce.com/2006/04/metadata">

     <decisionTableName>Sample_DT</decisionTableName>

     <decisionTblDatasetParameters>

       <fieldName>IsDeleted</fieldName>

       <datasetFieldName>IsDeleted</datasetFieldName>

     </decisionTblDatasetParameters>

     <decisionTblDatasetParameters>

       <fieldName>LimitNumber</fieldName>

       <datasetFieldName>CallDurationInSeconds</datasetFieldName>

     </decisionTblDatasetParameters>

     <decisionTblDatasetParameters>

       <fieldName>Name</fieldName>

       <datasetFieldName>Subject</datasetFieldName>

     </decisionTblDatasetParameters>

     <description>DSL created for md-common tests</description>

     <isDefault>false</isDefault>

     <sourceObject>Task</sourceObject>

     <setupName>DSL Sample</setupName>

   </DecisionTableDatasetLink>

```


### Metadata Types DecisionMatrixDefinition

The following is an example of a default DecisionTableDatasetLink component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <DecisionTableDatasetLink xmlns="http://soap.sforce.com/2006/04/metadata">

     <decisionTableName>Sample_DT</decisionTableName>

     <isDefault>true</isDefault>

     <sourceObject>WorkBadgeDefinition</sourceObject>

     <setupName>Default DSL Sample</setupName>

   </DecisionTableDatasetLink>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <fullName>Sample DT Package</fullName>

     <description>Package created for md-common tests</description>

     <types>

       <members>Sample_DT</members>

       <name>DecisionTable</name>

     </types>

     <types>

       <members>DSL_Sample</members>

       <members>Sample_DT_Default</members>

       <name>DecisionTableDatasetLink</name>

     </types>

     <version>51.0</version>

   </Package>

### DecisionMatrixDefinition

```

Represents a definition of a decision matrix.

[Note: Before deploying a decision matrix or a decision matrix version to a target org, review these decision matrix migration](https://help.salesforce.com/s/articleView?id=ind.decision_matrix_migration_considerations.htm&type=5&language=en_US)
[considerations.](https://help.salesforce.com/s/articleView?id=ind.decision_matrix_migration_considerations.htm&type=5&language=en_US)

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### DecisionMatrixDefinition components have the suffix .decisionMatrixDefinition and are stored in the

`decisionMatrixDefinition` folder.

Version

### DecisionMatrixDefinition components are available in API version 55.0 and later.


Metadata Types DecisionMatrixDefinition

Fields

**Field Name** **Description**

```
description

groupKey

label

processType

subGroupKey

```

**Field Type**
string

**Description**
Describes a decision matrix definition.

**Field Type**
string

**Description**
A key for grouping matrix rows in different versions, such as a geographic region or a
product code.

**Field Type**
string

**Description**

Required.

The UI label of a decision matrix definition.

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

Note: When Business Rules Engine is enabled for a Salesforce instance, the
default value is ' `Bre` ’. Other usage types may be available to you depending
on your industry solution and permission sets.

Available in API version 59.0 and later.

**Field Type**
string


Metadata Types DecisionMatrixDefinition

**Field Name** **Description**

**Description**
A subgroup key for grouping matrix rows in different versions, such as a geographic
region or a product code. For example, if the `groupKey` is `Country`, the
`subGroupKey` can be `State` or `Province` .

```
type

versions

```

**Field Type**
DecisionMatrixType (enumeration of type string)

**Description**
The type of a decision matrix.

Valid values are:

**•** `Grouped`

**•** `Standard`

**Field Type**

DecisionMatrixDefinitionVersion[]

**Description**
Represents an array of decision matrix version definitions in a decision matrix. This
array must contain at least one version.

DecisionMatrixDefinitionVersion

Represents a definition of a decision matrix version.

**Field Name** **Description**

```
columns

decisionMatrixDefinition

endDate

groupKeyValue

```

**Field Type**

DecisionMatrixDefinitionVersionColumn[]

**Description**
Represents an array of columns in a decision matrix definition version.

**Field Type**
string

**Description**
The full name of a decision matrix version.

**Field Type**
dateTime

**Description**
The date until which a decision matrix definition version is available for use.

**Field Type**
string


Metadata Types DecisionMatrixDefinition

**Field Name** **Description**

**Description**
The value of the `groupKey` for a decision matrix definition version. For example, if the
`groupKey` is `Country`, the `groupKeyValue` can be `United States` .

```
label

rank

startDate

status

subGroupKeyValue

```

**Field Type**
string

**Description**

Required.

The UI label of a decision matrix definition version.

**Field Type**
int

**Description**
The rank of the `Decision Matrix Definition Version` . When more than
one enabled version matches a decision matrix call, and the start date time to end date
time spans overlap, the version with the highest rank is chosen. Available in API version
64.0 and later.

**Field Type**
dateTime

**Description**

Required.

The date from when a decision matrix definition version is available for use.

**Field Type**
DecisionMatrixDefStatus (enumeration of type string)

**Description**

Required.

Specifies the status of a decision matrix definition version.

Valid values are:

**•** `Active`

**•** `Draft`

**•** `Inactive`

**•** `InvalidDraft`

**•** `Obsolete`

**Field Type**
string


Metadata Types DecisionMatrixDefinition

**Field Name** **Description**

**Description**
The value of the subgroup key for a decision matrix definition version. For example, if the
`subGroupKey` is `State` or `Province`, the `subGroupKeyValue` can be
`California` .

```
versionNumber

```

**Field Type**
int

**Description**

Required.

The version number of a decision matrix definition.

DecisionMatrixDefinitionVersionColumn

Represents a definition of a column in a decision matrix definition version.

**Field Name** **Description**

```
columnType

dataType

```

**Field Type**
DecisionMatrixColumnType (enumeration of type string)

**Description**

Required.

Specifies whether a column is for an input or output.

Valid values are:

**•** `Input`

**•** `Output`

**Field Type**
DecisionMatrixDataType (enumeration of type string)

**Description**
Required.

The type of data that’s stored in a column.

Valid values are:

**•** `Boolean`

**•** `Currency`

**•** `Number`

**•** `NumberRange`

**•** `Percent`

**•** `Text`

**•** `TextRange`


Metadata Types DecisionMatrixDefinition

**Field Name** **Description**

```
displaySequence

isWildcardColumn

name

rangeValue

wildcardValue

```

**Field Type**
int

**Description**
Required.

Represents the position of a column in the column order.

**Field Type**
boolean

**Description**
Required.

Specifies whether a column stores a wildcard value ( `true` ) or not ( `false` ).

The default value is `false` .

**Field Type**
string

**Description**
Required.

The full name of a decision matrix definition version column.

**Field Type**
string

**Description**
A list of values that define range boundaries.

**Field Type**
string

**Description**
The wildcard value such as `ALL` .

Declarative Metadata Sample Definition

The following is an example of a DecisionMatrixDefinition component.

```
<?xml version="1.0" encoding="UTF-8"?>

<DecisionMatrixDefinition

 xmlns="http://soap.sforce.com/2006/04/metadata">

 <label>HealthCloudUM_ValidRegions</label>

 <type>Standard</type>

 <versions>

  <fullName>HealthCloudUM_ValidRegions_V1</fullName>

  <columns>

  <columnType>Input</columnType>

  <dataType>Text</dataType>

```


### Metadata Types DelegateGroup

```
     <displaySequence>2</displaySequence>

     <isWildcardColumn>false</isWildcardColumn>

     <name>State</name>

     </columns>

     <columns>

     <columnType>Input</columnType>

     <dataType>Text</dataType>

     <displaySequence>1</displaySequence>

     <isWildcardColumn>false</isWildcardColumn>

     <name>City</name>

     </columns>

     <columns>

     <columnType>Output</columnType>

     <dataType>Boolean</dataType>

     <displaySequence>3</displaySequence>

     <isWildcardColumn>false</isWildcardColumn>

     <name>IsValid</name>

     </columns>

     <decisionMatrixDefinition>HealthCloudUM_ValidRegions</decisionMatrixDefinition>

     <label>HealthCloudUM_ValidRegions V1</label>

     <startDate>2022-05-02T13:04:06.000Z</startDate>

     <status>Draft</status>

     <versionNumber>1</versionNumber>

    </versions>

   </DecisionMatrixDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package

    xmlns="http://soap.sforce.com/2006/04/metadata">

    <types>

     <members>*</members>

     <name>DecisionMatrixDefinition</name>

    </types>

    <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based.htm)

### DelegateGroup

Represents a group of users who have the same administrative privileges. These groups are different from public groups used for sharing.

This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types DelegateGroup

File Suffix and Directory Location

DelegateGroup components have the suffix `.delegateGroup` and are stored in the `delegateGroups` folder. The file prefix
must match the developer name of the delegate group. For example, a delegate group with a developer name of MyDelegateGroup
would have a file name of `MyDelegateGroup.delegateGroup` .

Version

DelegateGroup components are available in API version 36.0 and later.

Special Access Rules

Only users with the “View Setup and Configuration” permission can be delegated administrators. As of Spring ’20 and later, only users
with “View Setup” or “Configuration” permission can access this object.

Fields

**Field Name** **Field Type** **Description**

`customObjects` string[] The custom objects associated with the group. Delegated administrators
can customize nearly every aspect of each of those custom objects,

including creating a custom tab. However, they can’t create or modify
relationships on the objects or set organization-wide sharing defaults.
Delegated administrators must have access to custom objects to access
the merge fields on those objects from formulas.

`groups` string[] The groups with users assigned by delegated administrators.

`label` string Required. The delegated group’s non-API name.

`loginAccess` boolean Required. Allows users in this group to log in as users in the role hierarchy
that they administer ( `true` ) or not ( `false` ). Depending on your

organization settings, individual users must grant login access to allow
their administrators to log in as them.

`permissionSetGroups` string[] The permission set groups that can be assigned to users in specified
roles and all subordinate roles by delegated administrators.

`permissionSets` string[] The permission sets that can be assigned to users in specified roles and
all subordinate roles by delegated administrators.

`profiles` string[] The profiles that can be assigned to users by delegated administrators.

`roles` string[] The roles and subordinates for which delegated administrators of the
group can create and edit users.


### Metadata Types DgtAssetMgmtProvider

Declarative Metadata Sample Definition

The following is an example of a DelegateGroup component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <DelegateGroup xmlns="http://soap.sforce.com/2006/04/metadata">

      <label>MyDelegateGroup</label>

      <loginAccess>true</loginAccess>

      <name>MyDelegateGroup</name>

      <profiles>Chatter Free User</profiles>

      <profiles>Chatter Moderator User</profiles>

      <profiles>Marketing User</profiles>

      <permissionSetGroups>My Permission Set Group</permissionSetGroups>

      <permissionSets>My Permset</permissionSets>

      <roles>LesserBossMan</roles>

   </DelegateGroup>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>DelegateGroup</name>

      </types>

      <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### DgtAssetMgmtProvider

Represents external content providers, such as digital asset management (DAM) systems, that integrate with Salesforce CMS. When
combined with the DgtAssetMgmtPrvdLghtCpnt type, this metadata type enables organizations to configure external content systems
as content providers within the Salesforce platform.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

### DgtAssetMgmtProvider components have the suffix .dgtAssetMgmtProvider and are stored in the

`dgtAssetMgmtProviders` folder.


Metadata Types DgtAssetMgmtProvider

Version

DgtAssetMgmtProvider components are available in API version 65.0 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Description**

```
icon

label

masterLabel

```

**Field Type**
string

**Description**
Stores a reference to the icon resource (typically a Lightning icon or custom image)
that visually represents the external content provider in the user interface.

**Field Type**
string

**Description**
Required. Specifies the display label for the external content provider that users see
when they select or view the provider.

**Field Type**
string

**Description**
Required. Specifies the primary identifier for the provider in metadata contexts and
localization.

Declarative Metadata Sample Definition

The following is an example of a DgtAssetMgmtProvider component.

```
<?xml version="1.0" encoding="UTF-8"?>

<DgtAssetMgmtProvider xmlns="http://soap.sforce.com/2006/04/metadata">

   <icon>My icon</icon>

   <label>My text</label>

   <masterLabel>My text</masterLabel>

</DgtAssetMgmtProvider>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>*</members>

```


### Metadata Types DgtAssetMgmtPrvdLghtCpnt

```
        <name>DgtAssetMgmtProvider</name>

      </types>

      <version>65.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### DgtAssetMgmtPrvdLghtCpnt

Represents the Lightning web component configurations for external content providers, such as digital asset management (DAM)
systems. This metadata type enables the integration of external content systems with Salesforce CMS using custom Lightning web
components.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

### DgtAssetMgmtPrvdLghtCpnt components have the suffix .dgtAssetMgmtPrvdLghtCpnt and are stored in the

`dgtAssetMgmtPrvdLghtCpnts` folder.

Version

### DgtAssetMgmtPrvdLghtCpnt components are available in API version 65.0 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Description**

```
dgtAssetMgmtProvider

```

**Field Type**
string

**Description**
Required. References the external content provider, represented by the
DgtAssetMgmtProvider on page 896 type, that this Lightning web component
configuration supports.


Metadata Types DgtAssetMgmtPrvdLghtCpnt

**Field Name** **Description**

```
lightningComponentBundle

masterLabel

type

```

**Field Type**
string

**Description**
References the Lightning web component, represented by the
LightningComponentBundle on page 1490 type, that implements the user interface for
the external content provider in Salesforce CMS.

The LightningComponentBundle must be deployed and available before you reference
it.

**Field Type**
string

**Description**
Required. Specifies the display name of the Lightning web component configuration
as it appears in the UI.

**Field Type**
DgtAssetMgmtPrvdLghtCpntType (enumeration of type string)

**Description**
Required. Specifies the type of external content provider Lightning web component
that’s being configured. Possible values are:

**•** DIGITAL_ASSET_MANAGER: Represents a component that provides full
management capabilities for external content providers, including browsing,
searching, and selecting.

**•** NONE: Represents an undefined or default provider type. Indicates that no specific
provider type is assigned.

Declarative Metadata Sample Definition

The following is an example of a DgtAssetMgmtPrvdLghtCpnt component.

```
<?xml version="1.0" encoding="UTF-8"?>

<DgtAssetMgmtPrvdLghtCpnt xmlns="http://soap.sforce.com/2006/04/metadata">

   <dgtAssetMgmtProvider>External Content Provider</dgtAssetMgmtProvider>

   <lightningComponentBundle>myLightningComponentBundle</lightningComponentBundle>

   <masterLabel>myComponent</masterLabel>

   <type>DIGITAL_ASSET_MANAGER</type>

</DgtAssetMgmtPrvdLghtCpnt>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>*</members>

     <name>DgtAssetMgmtPrvdLghtCpnt</name>

   </types>

```


### Metadata Types DigitalExperienceBundle

```
      <version>65.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### DigitalExperienceBundle

Represents a text-based code structure of your organization’s workspaces, organized by workspace type, and each workspace’s content
items.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### DigitalExperienceBundle components have the suffix .digitalExperience and are stored in the digitalExperiences

folder.

### DigitalExperienceBundle uses workspaces and content types to organize your data in a content-focused structure.

**•** Workspace: For enhanced Lightning Web Runtime (LWR) sites, a collection of related content items that form the site when combined
with data from the DigitalExperienceConfig metadata type.

For Salesforce CMS, a collection of related content items contained in a general workspace.

For Marketing Cloud, a collection of related content items contained in a marketing or general workspace.

Note: The maximum length for a workspace name is 80 characters.

**•** Workspace type: A way to categorize different kinds of workspaces. For example, the workspace type for enhanced LWR sites is
`site`, and the workspace type for marketing workspaces in Marketing Cloud is `marketing` . The workspace type determines
which content types are available in the workspace. In the DigitalExperienceBundle folder structure, all workspaces of a given type
are under that workspace type. `site`, `marketing`, and `general` are the supported workspace types.

**•** Content types: A way to categorize different kinds of content in a workspace. For example, all routes in an enhanced LWR site are
stored under a content type folder called `sfdc_cms__route` . Similarly, forms for a marketing workspace are stored under a
content type folder called `sfdc_cms__form` .

**•** Content items: For enhanced LWR sites, the individual settings and site components that make up an enhanced LWR site. For example,
each of the routes in an enhanced LWR site is a single content item.

For marketing workspaces, the content items used in marketing campaigns. For example, each form in a workspace is a single content
item.

Here’s an example of the DigitalExperienceBundle structure.


Metadata Types DigitalExperienceBundle

When retrieved, DigitalExperienceBundle contains workspace type folders (1) under the digitalExperiences folder.

The marketing folder contains one or more workspace folders (2), each representing a marketing workspace in Marketing Cloud. The
site folder contains one or more workspace folders (3), each representing the workspace for an individual enhanced LWR site. Each
workspace folder contains an `XML` file with information about the workspace, such as the label. For enhanced LWR sites, be sure to
keep the label value in sync with the site’s network name.

Each workspace folder also contains several content type folders that represent each of the different content types (4) used in that
workspace. For example, marketing workspaces support landing pages, forms, emails, and referenced images and branding.

Finally, each content type folder can contain one or more content subfolders. Each content subfolder can contain additional subfolders
and several files that, when combined, represent an individual content item, such as a specific view (5).

**•** A `_meta.json` file that contains the metadata for the content item. Use the `_meta.json` file to learn the location of a content
item within the workspace, or to move the content item to another location, including creating a new location for the content item.
You can also use the `_meta.json` file to view a content item’s parent-child relationships, to move the content item from one
parent to another, or to remove a parent-child relationship entirely.

**•** A `content.json` file that contains the primary version of the content item. Each `content.json` file includes values for the
content item’s type, title, and content body. Use this file to edit the content’s properties on your local machine or scratch org and
then deploy.

**•** If applicable, additional `JSON` files that represent variants of the content item, such as language translations.

Note: Before you deploy the DigitalExperienceBundle in a target org, make sure that any translated variants of content in the
target org are also in the source org. If the target org contains a `JSON` file for a translated variant that isn’t in the source org,
deploying the DigitalExperienceBundle fails.

The `_meta.json` file contains several properties:


Metadata Types DigitalExperienceBundle

Version

DigitalExperienceBundle components are available in API version 56.0 and later.


Metadata Types DigitalExperienceBundle

Special Access Rules

In Experience Cloud, you can use DigitalExperienceBundle for enhanced LWR sites created in Winter ’23 or later. For Aura sites and other
LWR sites, use the ExperienceBundle (recommended) or the SiteDotCom on page 2308 metadata types. Packaging is unsupported for
enhanced LWR sites.

In Salesforce CMS and in Marketing Cloud, you must have a contributor role in a workspace to retrieve it. For Marketing Cloud, you can
package the content of general and marketing workspaces, including landing pages, forms, and emails (and their associated images
and branding).

Fields

**Field Name** **Description**

```
description

digitalExperienceFolderShares

label

spaceResources

```

DigitalExperience

**Field Type**
string

**Description**
Contains the description of the workspace.

For site workspaces, this value is empty.

**Field Type**

DigitalExperienceFolderShare[]

**Description**
The list of folders in the source marketing workspace that are shared with target
marketing workspaces.

Available in API version 61.0 and later.

**Field Type**
string

**Description**
Required.

A user-friendly name for DigitalExperienceBundle, which is defined when the
DigitalExperienceBundle is created.

**Field Type**

DigitalExperience[]

**Description**
The list of resources in this DigitalExperienceBundle. Each resource represents a content
type, such as views, routes, themes, and languageSettings.

Represents content in the bundle. When retrieved as part of DigitalExperienceBundle, DigitalExperience represents all content for the
requested workspace or workspaces. When retrieved on its own, DigitalExperience represents only the content types you specify.


Metadata Types DigitalExperienceBundle

This subtype extends the MetadataWithContent metadata type and inherits its `content` and `fullName` fields.

When you retrieve DigitalExperience, the folder structure matches that of DigitalExperienceBundle, with only the specified content
returned.

**Field Name** **Description**

```
fileName

filePath

format

```

**Field Type**
string

**Description**
Required.

Name of the resource file.

**Field Type**
string

**Description**
Path to the file within the artifact folder.

**Field Type**
string

**Description**
Required.

Only `JSON` is allowed.

DigitalExperienceFolderShare

Represents a folder in a source marketing workspace that’s shared with other target marketing workspaces. Available in API version 61.0
and later.

**Field Name** **Description**

```
folderPath

sharedWith

```

SharedWith

**Field Type**
string

**Description**
The root folder of the shared workspace. The allowed value is `_root` .

**Field Type**

SharedWith[]

**Description**
The list of target workspaces that the source workspace is shared with.

Represents a target marketing workspace that the source marketing workspace is shared with. Available in API version 61.0 and later.


Metadata Types DigitalExperienceBundle

**Field Name** **Description**

```
fullyQualifiedName

```

**Field Type**
string

**Description**
The target workspace that the source workspace is shared with. It uses the format
_`workspace_type`_ / _`target_workspace_name`_ . For example,
`marketing/Workspace2` .

Declarative Metadata Sample Definition

The following is an example of a DigitalExperienceBundle component.

```
<?xml version="1.0" encoding="UTF-8"?>

<DigitalExperienceBundle xmlns="http://soap.sforce.com/2006/04/metadata">

   <description>content</description>

   <label>isv1</label>

</DigitalExperienceBundle>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>site/isv1</members>

     <name>DigitalExperienceBundle</name>

   </types>

   <version>56.0</version>

</Package>

```

Usage

Tip: Before you update the `JSON` files of an Experience Builder site, we recommend making a copy of the site’s folder as a backup.

To retrieve and deploy DigitalExperienceBundle, use legacy sfdx commands.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

DigitalExperienceBundle: Marketing Workspace Bundle and Folders
DigitalExperienceBundle uses the `marketing` workspace type to organize content items used in marketing campaigns in a
content-focused, text-based code structure.

DigitalExperienceBundle: Site Workspace Bundle and Folders
DigitalExperienceBundle uses the `site` workspace type to organize data for enhanced LWR sites in a content-focused, text-based
code structure.


#### Metadata Types DigitalExperienceBundle: Marketing Workspace Bundle and

Folders

#### DigitalExperienceBundle: Marketing Workspace Bundle and Folders

DigitalExperienceBundle uses the `marketing` workspace type to organize content items used in marketing campaigns in a
content-focused, text-based code structure.

For Marketing Cloud, the `marketing` folder contains one or more workspace folders, each representing an individual marketing
workspace. Each workspace folder contains a collection of related content items, such as landing pages, forms, and emails, and their
associated images and branding.

The folder for each marketing workspace includes content type folders, content item subfolders, and associated data that's contained
in `content.json` and `_meta.json` files.

The following content type folders represent the content types that are supported in a marketing workspace. For example, forms for a
marketing workspace are stored under a content type folder called `sfdc_cms__form` .

**•** sfdc_cms__brand Folder

**•** sfdc_cms__brandSettings Folder

**•** sfdc_cms__email Folder

**•** sfdc_cms__form Folder

**•** sfdc_cms__image Folder

**•** sfdc_cms__landingPage Folder

**•** sfdc_cms__languageSettings Folder

sfdc_cms__brand Folder

This content type folder contains one content subfolder per brand. Each content subfolder contains two or more `JSON` files:

**•** `_meta.json`

**•** `content.json`

**•** If applicable, additional `JSON` files that represent variations of the content item

```
   <apiName> /content.json

   {

     "type" : "sfdc_cms__brand",

     "title" : "brand 1",

     "contentBody" : {

```


Metadata Types DigitalExperienceBundle: Marketing Workspace Bundle and
Folders

```
      "baseFontFamily" : "{!$brand.fontFamily.arial}",

      "baseFontSize" : {

       "unit" : "px",

       "value" : 16.0

      },

      "borderRadius" : {

       "round" : {

        "unit" : "rem",

        "value" : 0.25

       },

       "square" : {

        "unit" : "rem",

        "value" : 0.0

       }

      },

      "borderWeight" : {

       "medium" : {

        "unit" : "rem",

        "value" : 0.125

       },

       "none" : {

        "unit" : "rem",

        "value" : 0.0

       },

       ...

      },

      "buttonStyleGroup" : {

       "primary" : {

        "lightning:borderRadius" : "{!$brand.borderRadius.round}",

        "lightning:borderWidth" : "{!$brand.borderWeight.thin}",

        "lightning:buttonColorGroup" : {

         "backgroundColor" : "{!$brand.colorScheme.primaryAccent}",

         "backgroundHoverColor" : "{!$brand.colorScheme.primaryAccentDerived}",

         "borderColor" : "{!$brand.colorScheme.primaryAccent}",

         "borderHoverColor" : "{!$brand.colorScheme.primaryAccentDerived}",

         "textColor" : "{!$brand.colorScheme.primaryAccentContrast}",

         "textHoverColor" : "{!$brand.colorScheme.primaryAccentContrastDerived}"

        },

        "lightning:padding" : {

         "bottom" : {

           "unit" : "rem",

           "value" : 0.5

         },

         ...

        },

        "lightning:typography" : "{!$brand.typography.button.button1}"

       },

       "secondary" : {...},

       "tertiary" : {...}

      },

      "colorScheme" : {

       "contrast" : "#000000",

       "neutral" : "#747474",

       "primaryAccent" : "#99F077",

```


Metadata Types DigitalExperienceBundle: Marketing Workspace Bundle and
Folders

```
       "primaryAccentContrast" : "#ffffff",

       "primaryAccentContrastDerived" : "#000000",

       "primaryAccentDerived" : "#7fd65f",

       "root" : "#ffffff"

      },

      "fontFamily" : {

       "arial" : {

        "category" : "sans-serif",

        "fallbacks" : [ "Helvetica" ],

        "name" : "Arial"

       },

       "arialBlack" : {

        "category" : "sans-serif",

        "fallbacks" : [ "Gadget" ],

        "name" : "Arial Black"

       },

       ...

      },

      "fontSize" : {

       "large" : {

        "unit" : "rem",

        "value" : 1.125

       },

       "medium" : {

        "unit" : "rem",

        "value" : 1.0

       },

       ...

      },

      "spacing" : {

       "large" : {

        "bottom" : {

         "unit" : "rem",

         "value" : 1.5

        },

        "left" : {

         "unit" : "rem",

         "value" : 1.5

        },

        "right" : {

         "unit" : "rem",

         "value" : 1.5

        },

        "top" : {

         "unit" : "rem",

         "value" : 1.5

        }

       },

       ...

      },

      "typography" : {

       "button" : {

        "button1" : {

         "fontFamily" : "{!$brand.baseFontFamily}",

```


Metadata Types DigitalExperienceBundle: Marketing Workspace Bundle and
Folders

```
         "fontSize" : "{!$brand.fontSize.medium}",

         "fontWeight" : "{!$brand.fontWeight.normal}",

         "letterSpacing" : "normal",

         "lineHeight" : 1.5,

         "textTransform" : "none"

        }

       },

       ...

      },

      ...

      "lightning:dataProviders" : [ ],

      "sfdc_cms:einsteinBrandProperties" : {

       "personality" : {

        "defaultPersonality" : "professional"

       }

      },

      "sfdc_cms:variants" : [ ]

     },

     "urlName" : "brand-1",

     "sfdc_cms:title" : "brand 1",

   }

```

sfdc_cms__brandSettings Folder

This content type folder contains one content subfolder called brandSettings. The brandSettings content subfolder contains two or
more `JSON` files:

**•** `_meta.json`

**•** `content.json`

**•** If applicable, additional `JSON` files that represent variations of the content item

```
   <apiName> /content.json

   {

     "type" : "sfdc_cms__brandSettings",

     "title" : "Brand Settings",

     "contentBody" : {

      "defaultBrand" : "brand3"

     },

     "urlName" : "brand-settings"

   }

```

sfdc_cms__email Folder

This content type folder contains one content subfolder per email. Each content subfolder contains two or more `JSON` files:

**•** `_meta.json`

**•** `content.json`

**•** If applicable, additional `JSON` files that represent variations of the content item


Metadata Types DigitalExperienceBundle: Marketing Workspace Bundle and
Folders

Note: In marketing workspaces, the default data graph, personalization recommenders, personalization points, and decisions
aren't included in the bundle. If the workspace includes emails with personalized content that’s based on these objects, then:

**•** Any merge field or repeater that uses the default data graph or a personalization recommender from the source org is broken
in the target org.

**•** Any dynamic content variations of email components are removed and only the default variations appear in the email.

```
   <apiName> /content.json

   {

     "type" : "sfdc_cms__email",

     "title" : "Email_marketingSpaceA",

     "contentBody" : {

      "backgroundColor" : "#f3f3f3",

      "lightning:brandSource" : {

       "defaultBrandOption" : "sfdcBrand"

      },

      "lightning:colorScheme" : "{!$brand.colorScheme}",

      "lightning:dataProviders" : [ {

       "attributes" : {

        "objectApiName" : "UnifiedIndividual__dlm"

       },

       "definition" : "sfdc_cms__unifiedIndividualDataProvider",

       "sfdcExpressionKey" : "unifiedIndividual"

      } ],

      "lightning:padding" : "{!$brand.spacing.none}",

      "messagePurpose" : "promotional",

      "sfdc_cms:block" : {

       "definition" : "sfdc_cms/rootContentBlock",

       "id" : "6458e24b-c1a8-4f7d-b6f0-3659c092f1c3",

       "type" : "block",

       "children" : [ {

        "attributes" : {

         "lightning:borderRadius" : "{!$brand.borderRadius.square}",

         "lightning:borderWidth" : "{!$brand.borderWeight.none}",

         "lightning:colorScheme" : "{!$brand.colorScheme}",

         "lightning:margin" : "{!$brand.spacing.none}",

         "lightning:padding" : "{!$brand.spacing.xSmall}",

         "stackOnMobile" : true,

         "lightning:backgroundImage" : {

           "repeat" : "no-repeat",

           "position" : "center center",

           "size" : "cover"

         }

        },

        "definition" : "lightning/section",

        "id" : "b61c4d08-7985-41f2-a38c-7f8338e56e00",

        "type" : "block",

        "children" : [ {

         "attributes" : {

           "columnWidth" : 12.0,

           "lightning:borderRadius" : "{!$brand.borderRadius.square}",

           "lightning:borderWidth" : "{!$brand.borderWeight.none}",

           "lightning:colorScheme" : "{!$brand.colorScheme}",

           "lightning:margin" : "{!$brand.spacing.none}",

```


Metadata Types DigitalExperienceBundle: Marketing Workspace Bundle and
Folders

```
           "lightning:padding" : "{!$brand.spacing.xSmall}",

           "lightning:verticalAlignment" : "top",

           "lightning:backgroundImage" : {

            "repeat" : "no-repeat",

            "position" : "center center",

            "size" : "cover"

           }

         },

         "definition" : "lightning/column",

         "id" : "778d9976-82ec-49aa-a3de-ac6485332434",

         "type" : "block",

         "children" : [ ]

        } ]

       } ]

      },

      "sfdc_cms:title" : "Email_marketingSpaceA",

      "subjectLine" : "Email_marketingSpaceA subject{!$organization.Address}",

      "lightning:expressions" : [ ],

      "lightning:backgroundImage" : {

       "repeat" : "no-repeat",

       "position" : "center center",

       "size" : "cover"

      },

      "sfdc_cms:variants" : [ ]

     },

     "urlName" : "email-mk1"

   }

```

sfdc_cms__form Folder

This content type folder contains one content subfolder per form. Each content subfolder contains two or more `JSON` files:

**•** `_meta.json`

**•** `content.json`

**•** If applicable, additional `JSON` files that represent variations of the content item

```
   <apiName> /content.json

   {

     "type" : "sfdc_cms__form",

     "title" : "Form1_mk1",

     "contentBody" : {

      "lightning:brandSource" : {

       "defaultBrandOption" : "sfdcBrand"

      },

      "lightning:dataProviders" : [ {

       "attributes" : {

        "objectApiName" : "Account",

        "recordTypeId" : "012000000000000AAA"

       },

       "definition" : "sfdc_cms__recordDataProvider",

       "sfdcExpressionKey" : "Flow1"

      } ],

      "sfdc_cms:block" : {

```


Metadata Types DigitalExperienceBundle: Marketing Workspace Bundle and
Folders

```
       "definition" : "sfdc_cms/rootContentBlock",

       "id" : "fef7b2b0-5ddf-4f0e-b0d5-cdbc77a897e9",

       "type" : "block",

       "children" : [ {

        "attributes" : {

         "lightning:borderRadius" : "{!$brand.borderRadius.square}",

         "lightning:borderWidth" : "{!$brand.borderWeight.none}",

         "lightning:colorScheme" : "{!$brand.colorScheme}",

         "lightning:margin" : "{!$brand.spacing.none}",

         "lightning:padding" : "{!$brand.spacing.xSmall}",

         "stackOnMobile" : true,

         "lightning:backgroundImage" : {

           "repeat" : "no-repeat",

           "position" : "center center",

           "size" : "cover"

         }

        },

        "definition" : "lightning/section",

        "id" : "43dc4273-47e2-43ad-9e64-f0862eb0fcdf",

        "type" : "block",

        "children" : [ {

         "attributes" : {

           "columnWidth" : 12.0,

           "lightning:borderRadius" : "{!$brand.borderRadius.square}",

           "lightning:borderWidth" : "{!$brand.borderWeight.none}",

           "lightning:colorScheme" : "{!$brand.colorScheme}",

           "lightning:margin" : "{!$brand.spacing.none}",

           "lightning:padding" : "{!$brand.spacing.xSmall}",

           "lightning:verticalAlignment" : "top",

           "lightning:backgroundImage" : {

            "repeat" : "no-repeat",

            "position" : "center center",

            "size" : "cover"

           }

         },

         "definition" : "lightning/column",

         "id" : "95fc1b5c-481d-4d32-bd03-fec0a4d7aaa0",

         "type" : "block",

         "children" : [ {

           "attributes" : {

            "lightning:borderRadius" : "{!$brand.borderRadius.square}",

            "lightning:borderWidth" : "{!$brand.borderWeight.none}",

            "lightning:formInputColorGroup" : {

             "backgroundColor" : "{!$brand.colorScheme.root}",

             "borderColor" : "{!$brand.colorScheme.neutral}",

             "textColor" : "{!$brand.colorScheme.contrast}"

            },

            "lightning:horizontalAlignment" : "left",

            "lightning:inputTypography" : "{!$brand.typography.input.input1}",

            "lightning:labelTypography" : "{!$brand.typography.label.label1}",

            "lightning:margin" : "{!$brand.spacing.none}",

            "lightning:padding" : "{!$brand.spacing.none}",

            "maxLength" : 255.0,

            "sfdc_cms:fieldReference" : "{!Flow1.Name}",

```


Metadata Types DigitalExperienceBundle: Marketing Workspace Bundle and
Folders

```
            "sfdc_cms:formInputLabelProperty" : "Account Name",

            "sfdc_cms:formInputNameProperty" : "Name",

            "sfdc_cms:formInputRequiredProperty" : true,

            "width" : "auto"

           },

           "definition" : "lightning/inputText",

           "id" : "6aac0596-26c6-457a-9a9a-cc43ba622739",

           "type" : "block"

         } ]

        } ]

       }, {

        "attributes" : {

         "lightning:borderRadius" : "{!$brand.borderRadius.square}",

         "lightning:borderWidth" : "{!$brand.borderWeight.none}",

         "lightning:colorScheme" : "{!$brand.colorScheme}",

         "lightning:margin" : "{!$brand.spacing.none}",

         "lightning:padding" : "{!$brand.spacing.xSmall}",

         "stackOnMobile" : true,

         "lightning:backgroundImage" : {

           "repeat" : "no-repeat",

           "position" : "center center",

           "size" : "cover"

         }

        },

        "definition" : "lightning/section",

        "id" : "7fe6298e-8c83-4dac-9596-02c629fdc519",

        "type" : "block",

        "children" : [ {

         "attributes" : {

           "columnWidth" : 12.0,

           "lightning:borderRadius" : "{!$brand.borderRadius.square}",

           "lightning:borderWidth" : "{!$brand.borderWeight.none}",

           "lightning:colorScheme" : "{!$brand.colorScheme}",

           "lightning:margin" : "{!$brand.spacing.none}",

           "lightning:padding" : "{!$brand.spacing.xSmall}",

           "lightning:verticalAlignment" : "top",

           "lightning:backgroundImage" : {

            "repeat" : "no-repeat",

            "position" : "center center",

            "size" : "cover"

           }

         },

         "definition" : "lightning/column",

         "id" : "976bff41-3fa9-4d04-aaf8-3590cb87909f",

         "type" : "block",

         "children" : [ {

           "attributes" : {

            "lightning:borderRadius" :

   "{!$brand.buttonStyleGroup.primary.lightning:borderRadius}",

            "lightning:borderWidth" :

   "{!$brand.buttonStyleGroup.primary.lightning:borderWidth}",

            "lightning:buttonColorGroup" :

   "{!$brand.buttonStyleGroup.primary.lightning:buttonColorGroup}",

            "lightning:horizontalAlignment" : "center",

```


Metadata Types DigitalExperienceBundle: Marketing Workspace Bundle and
Folders

```
            "lightning:margin" : "{!$brand.spacing.none}",

           "lightning:padding" : "{!$brand.buttonStyleGroup.primary.lightning:padding}",

            "lightning:typography" :

   "{!$brand.buttonStyleGroup.primary.lightning:typography}",

            "sfdc_cms:styleGroup" : "{!$brand.buttonStyleGroup.primary}",

            "text" : "Submit",

            "width" : "auto",

            "lightning:click" : {

             "actions" : [ {

              "definition" : "sfdc_cms/customEventAction",

              "attributes" : {

               "type" : "formsubmit",

               "options" : {

                 "bubbles" : true

               }

              }

             } ]

            }

           },

           "definition" : "lightning/actionButton",

           "id" : "84c67ba2-fffc-46d1-80af-35e66ae85ef3",

           "type" : "block"

         } ]

        } ]

       } ]

      },

      "sfdc_cms:title" : "Form1_mk1",

      "formsubmission" : {

       "actions" : [ {

        "definition" : "sfdc_cms/umaFormSubmissionAction",

        "attributes" : {

         "formId" : "{!$form.id}",

         "pageReferenceId" : "{!$page.id}",

         "formData" : "{!$form.fields}"

        }

       }, {

        "definition" : "sfdc_cms/showThankYouAction",

        "attributes" : {

         "message" : "Thank you for your submission."

        }

       } ]

      }

     },

     "urlName" : "form1-mk1"

   }

```

sfdc_cms__image Folder

This content type folder contains one content subfolder per image. Each content subfolder contains two or more `JSON` files and a
`_media` subfolder that contains the image file.

**•** `_meta.json`

**•** `content.json`


Metadata Types DigitalExperienceBundle: Marketing Workspace Bundle and
Folders

**•** If applicable, additional `JSON` files that represent variations of the content item

```
   <apiName> /content.json

   {

     "type" : "sfdc_cms__image",

     "title" : "Img1_mk1",

     "contentBody" : {

      "sfdc_cms:media" : {

       "source" : {

        "mimeType" : "image/png",

        "ref" : "0sNSB000001rKsr2AE",

        "type" : "file",

        "size" : 538158

       }

      }

     },

     "urlName" : "img1-mk1"

   }

```

sfdc_cms__landingPage Folder

This content type folder contains one content subfolder per landing page. Each content subfolder contains two or more `JSON` files:

**•** `_meta.json`

**•** `content.json`

**•** If applicable, additional `JSON` files that represent variations of the content item

```
   <apiName> /content.json

   {

     "type" : "sfdc_cms__landingPage",

     "title" : "LandingPageA_marketingSpaceA",

     "contentBody" : {

      "lightning:brandSource" : {

       "defaultBrandOption" : "sfdcBrand"

      },

      "sfdc_cms:block" : {

       "definition" : "sfdc_cms/rootContentBlock",

       "id" : "ac065643-646a-4b1e-b5ed-7eeeed90d0d3",

       "type" : "block",

       "children" : [ {

        "attributes" : {

         "lightning:borderRadius" : "{!$brand.borderRadius.square}",

         "lightning:borderWidth" : "{!$brand.borderWeight.none}",

         "lightning:colorScheme" : "{!$brand.colorScheme}",

         "lightning:margin" : "{!$brand.spacing.none}",

         "lightning:padding" : "{!$brand.spacing.xSmall}",

         "stackOnMobile" : true,

         "lightning:backgroundImage" : {

           "repeat" : "no-repeat",

           "position" : "center center",

           "size" : "cover"

         }

        },

```


Metadata Types DigitalExperienceBundle: Marketing Workspace Bundle and
Folders

```
        "definition" : "lightning/section",

        "id" : "f6371eda-aafc-4164-a18f-284e49071b76",

        "type" : "block",

        "children" : [ {

         "attributes" : {

           "columnWidth" : 12.0,

           "lightning:borderRadius" : "{!$brand.borderRadius.square}",

           "lightning:borderWidth" : "{!$brand.borderWeight.none}",

           "lightning:colorScheme" : "{!$brand.colorScheme}",

           "lightning:margin" : "{!$brand.spacing.none}",

           "lightning:padding" : "{!$brand.spacing.xSmall}",

           "lightning:verticalAlignment" : "top",

           "lightning:backgroundImage" : {

            "repeat" : "no-repeat",

            "position" : "center center",

            "size" : "cover"

           }

         },

         "definition" : "lightning/column",

         "id" : "db82b936-f2d8-4d47-b373-71dff7fc1f1d",

         "type" : "block",

         "children" : [ {

           "attributes" : {

            "imageFitConfig" : {

             "width" : {

              "unit" : "%",

              "value" : 100.0

             }

            },

            "imageInfo" : {

             "altText" : "",

             "overrideAltText" : false,

             "source" : {

              "ref" : "Img1_mk1",

              "type" : "imageReference"

             },

             "url" : "/cms/media/MCWJDAQWY2HREBRENINOZIKNNVNM"

            },

            "lightning:borderRadius" : "{!$brand.borderRadius.square}",

            "lightning:borderWidth" : "{!$brand.borderWeight.none}",

            "lightning:colorGroup" : {

             "backgroundColor" : "{!$brand.colorScheme.root}",

             "borderColor" : "{!$brand.colorScheme.neutral}",

             "linkColor" : "{!$brand.colorScheme.primaryAccent}",

             "textColor" : "{!$brand.colorScheme.contrast}"

            },

            "lightning:horizontalAlignment" : "center",

            "lightning:margin" : "{!$brand.spacing.none}",

            "lightning:padding" : "{!$brand.spacing.none}",

            "lightning:typography" : "{!$brand.typography.paragraph.paragraph1}"

           },

           "definition" : "lightning/image",

           "id" : "6775db07-8343-420c-918a-0d91c193902d",

           "type" : "block"

```


#### Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders

```
         } ]

        } ]

       } ]

      },

      "sfdc_cms:seoProperties" : {

       "isIndexed" : false,

       "title" : "LandingPageA_marketingSpaceA"

      },

      "sfdc_cms:title" : "LandingPageA_marketingSpaceA",

      "lightning:dataProviders" : [ ],

      "lightning:backgroundImage" : {

       "repeat" : "no-repeat",

       "position" : "center center",

       "size" : "cover"

      }

     },

     "urlName" : "lp1-mk1"

   }

```

sfdc_cms__languageSettings Folder

This content type folder contains one content subfolder called languages. The languages content subfolder contains two or more `JSON`
files:

**•** `_meta.json`

**•** `content.json`

**•** If applicable, additional `JSON` files that represent variations of the content item

```
   <apiName> /content.json

   {

     "type" : "sfdc_cms__languageSettings",

     "title" : "LanguageContent",

     "contentBody" : {

      "languages" : [ {

       "locale" : "en_US",

       "label" : "English (US)",

       "isActive" : true,

       "isAuthoringOnly" : false

      } ],

      "defaultLocale" : "en_US"

     },

     "urlName" : "languagecontent"

   }

#### DigitalExperienceBundle: Site Workspace Bundle and Folders

```

DigitalExperienceBundle uses the `site` workspace type to organize data for enhanced LWR sites in a content-focused, text-based code
structure.

The `site` folder contains one or more workspace folders, each representing the workspace for an individual enhanced LWR site. Each
workspace folder contains a collection of related content items, such as settings and site components, that form the site when combined
with data from the DigitalExperienceConfig metadata type.


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders

The workspace folder for each site includes content type folders, content item subfolders, and associated data that's contained in
`content.json` and `_meta.json` files.

The following content type folders represent the content types that are supported in an enhanced LWR site. For example, all routes in
an enhanced LWR site are stored under the `sfdc_cms__route` content type folder.

**•** sfdc_cms__appPage Folder

**•** sfdc_cms__brandingSet Folder

**•** sfdc_cms__languageSettings Folder

**•** sfdc_cms__route Folder

**•** sfdc_cms__site Folder

**•** sfdc_cms__theme Folder

**•** sfdc_cms__themeLayout Folder

**•** sfdc_cms__view Folder

sfdc_cms__appPage Folder

This content type folder exists at the root level and contains one content subfolder that represents the site’s single-page application.
Only one `sfdc_cms__appPage` content item is allowed per site.

The content subfolder contains two or more `JSON` files:

**•** `_meta.json`

**•** `content.json`

**•** If applicable, additional `JSON` files that represent variations of the content item

```
   <apiName> /content.json

```


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders

```
{

  "type" : "sfdc_cms__appPage",

  "title" : "main",

  "contentBody" : {

   "currentThemeId" : "Build_Your_Own_LWR",

   "headMarkup" : "<meta charset=\"UTF-8\" />\n<meta name=\"viewport\"

content=\"width=device-width, initial-scale=1\" />\n<title>Welcome to LWC

Communities!</title>\n\n<link rel=\"stylesheet\" href=\"{ basePath

}/assets/styles/styles.css?{ versionKey }\" />\n\n\n<!-- webruntime-branding-shared

stylesheets -->\n<link rel=\"stylesheet\" href=\"{ basePath

}/assets/styles/salesforce-lightning-design-system.min.css?{ versionKey }\" />\n<link

rel=\"stylesheet\" href=\"{ basePath }/assets/styles/dxp-site-spacing-styling-hooks.min.css?{

 versionKey }\" />\n<link rel=\"stylesheet\" href=\"{ basePath

}/assets/styles/dxp-styling-hooks.min.css?{ versionKey }\" />\n<link rel=\"stylesheet\"

href=\"{ basePath }/assets/styles/dxp-slds-extensions.min.css?{ versionKey }\" />\n\n\n<!-
 webruntime-branding-shared stylesheets -->",

   "isLockerServiceEnabled" : true,

   "isRelaxedCSPLevel" : false,

   "templateName" : "talon-template-byo"

  }

}

```

sfdc_cms__brandingSet Folder

This content type folder contains one content subfolder per branding set. Each content subfolder contains two or more `JSON` files:

**•** `_meta.json`

**•** `content.json`

**•** If applicable, additional `JSON` files that represent variations of the content item

```
<apiName> /content.json

```


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders

```
   {

     "type" : "sfdc_cms__brandingSet",

     "title" : "Build Your Own (LWR)",

     "contentBody" : {

      "brandingSetType" : "APP",

      "definitionName" : "talon-template-byo:branding",

      "values" : {

       "BackgroundColor" : "#ffffff",

       "BaseFontSize" : "1rem",

       "BodyFont" : "Salesforce Sans",

       "BodyFontSize" : "1rem",

       "BodyFontStyle" : "normal",

       "BodyFontWeight" : "400",

       "BodyLetterSpacing" : "0em",

       "BodyLineHeight" : "1.5",

       "BodySmallFont" : "Salesforce Sans",

       "BodySmallFontSize" : "0.75rem",

       "BodySmallFontStyle" : "normal",

       "BodySmallFontWeight" : "400",

       "BodySmallLetterSpacing" : "0em",

       "BodySmallLineHeight" : "1.25",

       "BodySmallTextColor" : "var(--dxp-g-root-contrast)",

       "BodySmallTextDecoration" : "none",

       "BodySmallTextTransform" : "none",

       "BodyTextColor" : "var(--dxp-g-root-contrast)",

       "BodyTextDecoration" : "none",

       "BodyTextTransform" : "none",

       "ButtonActiveColor" : "var(--dxp-s-button-color-1)",

       "ButtonBorderRadius" : "4px",

       "ButtonColor" : "var(--dxp-g-brand)",

       "ButtonFocusColor" : "var(--dxp-s-button-color-1)",

       "ButtonFont" : "Salesforce Sans",

       "ButtonFontSize" : "1rem",

       "ButtonFontStyle" : "normal",

       "ButtonFontWeight" : "400",

       "ButtonHoverColor" : "var(--dxp-s-button-color-1)",

       "ButtonLargeBorderRadius" : "4px",

       "ButtonLargeFontSize" : "1.25rem",

       "ButtonLargePadding" : "1.25rem",

       "ButtonLetterSpacing" : "0em",

       "ButtonLineHeight" : "2",

       "ButtonPadding" : "1rem",

       "ButtonSmallBorderRadius" : "4px",

       "ButtonSmallFontSize" : "0.75rem",

       "ButtonSmallPadding" : "0.75rem",

       "ButtonTextTransform" : "none",

       "ColumnSpacerSizeDesktop" : "1rem",

```


Metadata Types DigitalExperienceBundle: Site Workspace Bundle and Folders

```
       "ColumnSpacerSizeMobile" : "0.75rem",

       "ComponentSpacerSizeDesktop" : "1.5rem",

