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

```


Metadata Types ExpressionSetDefinition

```
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

```


Metadata Types ExpressionSetDefinition

```
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

```


Metadata Types ExpressionSetDefinition

```
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

```


### Metadata Types ExpressionSetMessageToken

```
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
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based.htm)

### ExpressionSetMessageToken

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

```

**Field Type**
string

**Description**

Required.


### Metadata Types ExpressionSetObjectAlias

**Field Name** **Description**

Description of the expression set message token.

```
developerName

masterLabel

```

**Field Type**
string

**Description**

Required.

Developer name of the expression set message token.

**Field Type**
string

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
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### ExpressionSetObjectAlias

Represents information about the alias of the source object that’s used in an expression set.


Metadata Types ExpressionSetObjectAlias

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

ExpressionSetObjectAlias components have the suffix `.expressionSetObjectAlias` and are stored in the
`expressionSetObjectAlias` folder.

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


Metadata Types ExpressionSetObjectAlias

**Field Name** **Description**

The type of application associated with the industry that's using an expression set.
Your Salesforce org admin can define the values.

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

```


### Metadata Types ExternalAuthIdentityProvider

```
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
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based.htm)

### ExternalAuthIdentityProvider

Represents an external authentication (auth) identity provider. An external auth identity provider links to an external credential and
obtains OAuth tokens for outbound callouts to external systems.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ExternalAuthIdentityProvider components have the suffix .externalAuthIdentityProvider and are stored in the

`externalAuthIdentityProviders` folder.


Metadata Types ExternalAuthIdentityProvider

Version

ExternalAuthIdentityProvider components are available in API version 62.0 and later.

Special Access Rules

Only users with the Customize Application permission or the Manage Named Credentials permission can access this type.

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


Metadata Types ExternalAuthIdentityProvider

**Field Name** **Description**

**Description**

Required.

Name of the external auth identity provider.

ExternalAuthIdentityProviderParameter

Represents the parameters that configure an external auth identity provider.

These parameters are used internally to provide a flexible architecture and are exposed here for packaging reasons.

**Field Name** **Description**

```
description

parameterName

parameterType

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


Metadata Types ExternalAuthIdentityProvider

**Field Name** **Description**

**•** `TokenRequestBodyParameter`

**•** `TokenRequestHttpHeader`

**•** `TokenRequestQueryParameter`

**•** `TokenUrl`

**•** `UserInfoUrl`

```
parameterValue

sequenceNumber

```

**Field Type**
string

**Description**
If the `parameterType` field describes a literal value, then this field stores the literal
value.

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


### Metadata Types ExternalClientApplication

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

```

**Field Type**
string

**Description**
The email address that Salesforce uses to contact the external client app admin for
the subscriber org.


Metadata Types ExternalClientApplication

**Field Name** **Description**

```
contactPhone

description

distributionState

iconUrl

infoUrl

isProtected

label

```

**Field Type**
string

**Description**
The phone number that Salesforce uses to contact the external client app admin for
the subscriber org.

**Field Type**
string

**Description**
A description for the app.

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


Metadata Types ExternalClientApplication

**Field Name** **Description**

```
logoUrl

managedType

orgScopedExternalApp

```

**Field Type**
string

**Description**
The URL for the logo image.

**Field Type**
ExtlClntAppManagedType (enumeration of type string)

**Description**
For internal use only.

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

```


### Metadata Types ExternalCredential

```
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

### ExternalCredential

Represents the details of how Salesforce authenticates to the external system.

Note: All credentials stored within this entity are encrypted under a framework that is consistent with other encryption frameworks
on the platform. Salesforce encrypts your credentials by auto-creating org-specific keys. Credentials encrypted using the previous
encryption scheme have been migrated to the new framework.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

### ExternalCredential components have the suffix .externalCredential and are stored in the externalCredentials folder.

Version

### ExternalCredential components are available in API version 56.0 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.


Metadata Types ExternalCredential

Fields

**Field Name** **Description**

```
authenticationProtocol

description

externalCredentialParameters

label

```

**Field Type**
AuthenticationProtocol (enumeration of type string)

**Description**

Required.

The authentication protocol that’s required to access the external system. Valid values
are:

**•** `AwsSv4`

**•** `Basic`

**•** `Custom`  - User-created authentication. Specify the permission set, sequence
number, and authentication parameters. Each authentication parameter requires
a name and value.

**•** `Jwt`  - Reserved for future use

**•** `JwtExchange`  - Reserved for future use

**•** `NoAuthentication` —Reserved for future use

**•** `Oauth`

**•** `Password`  - Reserved for future use

For connections to Amazon Web Services using Signature Version 4, use `AwsSv4` .

For connections using a direct token system, select `Jwt` .

For Simple URL data sources, select `Custom` with no parameters.

For cloud-based Files Connect external systems, select `Oauth` . For on-premises
systems, select `Password` .

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


Metadata Types ExternalCredential

ExternalCredentialParameter

Represents the parameters that configure an external credential. External credential parameters are used to configure external credential
callouts through a combination of the type, name, and value and lookup fields. Available in API version 56.0 and later.

These parameters are used internally to provide a flexible architecture and are exposed here for packaging reasons.

**Field Name** **Description**

```
authProvider

certificate

description

externalAuthIdentityProvider

parameterGroup

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


Metadata Types ExternalCredential

**Field Name** **Description**

If a value for `parameterGroup` isn’t provided, `parameterGroup` defaults to
the `parameterName` value for PER_USER and NAMED_PRINCIPAL. For all other
parameters `parameterGroup` defaults to DEFAULT_GROUP.

```
parameterName

parameterType

```

**Field Type**
string

**Description**

Required.

The name of the external credential parameter.

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


Metadata Types ExternalCredential

**Field Name** **Description**

**•** `AwsStsPrincipal` : Configures AWS Signature V4 along with STS.
`parameterName` is `AwsStsPrincipal` and `parameterValue` isn’t
specified.

**•** `CreatedByNamespace` : Reserved for internal use.

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

**•** `SfHttpRequestExtensionName` : Reserved for internal use.

**•** `SigningCertificate` : Specifies the certificate used for an authentication
signature. Use the `certificate` field to specify the certificate name. Used for
OAuth with JWT Bearer Flow and AwsSv4 STS with RolesAnywhere authentication.

**•** `SystemUserPrincipal` : Reserved for internal use.

```
parameterValue

principal

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


Metadata Types ExternalCredential

**Field Name** **Description**

```
sequenceNumber

```

**Field Type**
int

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
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

SEE ALSO:

NamedCredential

_Salesforce Help_ [: Named Credentials](https://help.salesforce.com/s/articleView?id=xcloud.named_credentials_about.htm&type=5&language=en_US)

_Named Credentials Developer Guide_ [: Get Started with Named Credentials](https://developer.salesforce.com/docs/platform/named-credentials/guide/get-started.html)

_[Named Credentials Developer Guide](https://developer.salesforce.com/docs/platform/named-credentials/references/named-credentials-reference/nc-api-links.html)_ : Named Credential API Links

_Apex Developer Guide_ [: Invoking Callouts Using Apex](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_callouts.htm)

_Apex Developer Guide_ [: Named Credentials as Callout Endpoints](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_callouts_named_credentials.htm)

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

`catalogedApiVersion` string A version of an API synced from an external source and managed for
consumption in Salesforce by using API Catalog.

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
Aura-enabled, this field contains the Apex class name.

Available in API version 66.0 and later.


Metadata Types ExternalServiceRegistration

**Field Name** **Field Type** **Description**

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

**•** `ApexRest` —The API specification was created from an Apex REST
class. Available in API version 63.0 and later.

**•** `AuraEnabled` —The API specification was created from an Apex
class that has AuraEnabled methods. Available in API version 65.0
and later.

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

`schemaType` string The schema format. OpenAPI for Open API 2.0.x or Open API 3.0.x. If not
specified, schema type is derived based on the schema content. Nillable.


Metadata Types ExternalServiceRegistration

**Field Name** **Field Type** **Description**

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
version, you must create an external service using the same OpenAPI
spec and then replace any references to the old external service. See
[Register an External Service in Salesforce Help.](https://help.salesforce.com/s/articleView?id=platform.external_services_register.htm&language=en_US)


Metadata Types ExternalServiceRegistration

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

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

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


Metadata Types ExtlClntAppCanvasSettings

Fields

**Field Name** **Field Type** **Description**

`accessMethod` AccessMethod (enumeration of type string) Required. Indicates how the canvas app initiates the
OAuth authentication flow. The valid values are:

**•** `Get` —OAuth authentication is used, and the
user is prompted to allow the third-party
application to access their information. When you
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

Metadata Types ExtlClntAppCanvasSettings

**Field Name** **Field Type** **Description**

`canvasUrl` string Required. The URL of the third-party app that’s
exposed as a canvas app.

`externalClientApplication` string Required. The name of the associated external client
app.

`label` string The name of the app.

`lifeCycleHandler` string The name of the lifecycle handler Apex class.

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

```


### Metadata Types ExtlClntAppConfigurablePolicies

```
      </types>

      <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### ExtlClntAppConfigurablePolicies

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

```

**Field Type**
string

**Description**

Required.

The name of the external client app associated with the plugins.

**Field Type**
boolean


Metadata Types ExtlClntAppConfigurablePolicies

**Field Name** **Description**

**Description**

Required.

If `true`, all plugins are enabled unless individually disabled. If `false`, all plugins are
disabled. The default value is `true` . Available in API version 60.0 and later.

```
isCanvasPluginEnabled

isMobilePluginEnabled

isNotificationPluginEnabled

isOauthPluginEnabled

isPushPluginEnabled

isSamlPluginEnabled

```

**Field Type**
boolean

**Description**
If `true`, the Canvas app plugin is enabled. If `false`, the Canvas app plugin is disabled.
The default value is `true` . Available in API version 66.0 and later.

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


Metadata Types ExtlClntAppConfigurablePolicies

**Field Name** **Description**

```
label

startPage

```

startUrl

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

Available in API version 63.0 and later.

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

```


### Metadata Types ExtlClntAppGlobalOauthSettings

```
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


Metadata Types ExtlClntAppGlobalOauthSettings

Special Access Rules

Access to the OAuth plugin requires orgs to enable the Allow Access to OAuth Consumer Secrets via Metadata API permission in Setup.
The View External Client Apps Consumer Secrets in Metadata user permission is required for users with developer roles to configure
global OAuth settings.

Fields

**Field Name** **Description**

```
callbackUrl

certificate

consumerKey

consumerSecret

externalClientApplication

idTokenConfig

```

**Field Type**
string

**Description**
The endpoint that Salesforce calls back to your external client app during OAuth. It’s
the OAuth redirect_uri.

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


Metadata Types ExtlClntAppGlobalOauthSettings

**Field Name** **Description**

```
isClientCredentialsFlowEnabled

isCodeCredFlowEnabled

isCodeCredPostOnly

isConsumerSecretOptional

isDeviceFlowEnabled

```

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

To use this field, the Authorization Code and Credentials Flow must be enabled for
your org in OAuth and OpenID Connect settings.

Available in API version 61.0 and later.

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


Metadata Types ExtlClntAppGlobalOauthSettings

**Field Name** **Description**

```
isIntrospectAllTokens

isNamedUserJwtEnabled

isPkceRequired

isRefreshTokenRotationEnabled

isSecretRequiredForRefreshToken

isSecretRequiredForTokenExchange

isTokenExchangeEnabled

```

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


Metadata Types ExtlClntAppGlobalOauthSettings

**Field Name** **Description**

```
label

shouldRotateConsumerKey

shouldRotateConsumerSecret

```

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


Metadata Types ExtlClntAppGlobalOauthSettings

**Field Name** **Description**

**Description**
Indicates whether standard claims about the authentication event are included in the
ID token ( `true` ) or not ( `false` ).

```
idTokenValidityInMinutes

```

**Field Type**
int

**Description**
The length of time that the ID token is valid for after it’s issued. The value can be 1–720
minutes. The default value is 2 minutes.

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

```


### Metadata Types ExtlClntAppMobileConfigurablePolicies

```
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

### ExtlClntAppMobileConfigurablePolicies

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
[(enumeration](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_objects_intro.htm#enumeration_title) of ExtlClntAppMobileSettings metadata type, `screenLockTimeout`
type string)


### Metadata Types ExtlClntAppMobileSettings

**Field Name** **Field Type** **Description**

represents the amount of time after which the mobile app locks and
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

### ExtlClntAppMobileSettings

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


### Metadata Types ExtlClntAppNotificationSettings

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

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ExtlClntAppNotificationSettings components have the suffix .ecaNotifications and are stored in the

`extlClntAppNotifSettings` folder.

Version

### ExtlClntAppNotificationSettings components are available in API version 64.0 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Field Type** **Description**

externalClientApplication string Required. The name of the associated external client app.

label string Label for the external client app’s notification settings configuration.


### Metadata Types ExtlClntAppOauthConfigurablePolicies

**Field Name** **Field Type** **Description**

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

### ExtlClntAppOauthConfigurablePolicies

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


Metadata Types ExtlClntAppOauthConfigurablePolicies

Fields

**Field Name** **Description**

```
apexHandler

clientCredentialsFlowUser

commaSeparatedCustomScopes

commaSeparatedPermissionSet

commaSeparatedProfile

customAttributes

executeHandlerAs

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


Metadata Types ExtlClntAppOauthConfigurablePolicies

**Field Name** **Description**

```
externalClientApplication

guestJwtTimeout

guestJwtSessionTimeoutType

```

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

These values are available in API version 65.0 and later.

**•** `60` —1 Hour

**•** `90` —90 Minutes

**•** `120` —2 Hours

**•** `240` —4 Hours

**•** `480` —8 Hours

**•** `720` —12 Hours

If `guestJwtSessionTimeoutType` is set to `UserSession`, omit this field.

**Field Type**
JWTSessionTimeoutType (enumeration of type string)

**Description**
Specifies how the JWT-based access token timeout is defined for guest users. Valid
values are:

**•** `UserSession` —Salesforce uses the value from the `sessionTimeout` field
[in the ProfileSessionSetting type for the Experience Cloud guest user profile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_profilesessionsetting.htm)

If there's no profile session timeout for the user, Salesforce uses the
`sessionTimeout` [value from the SessionSettings type.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_securitysettings.htm)

If both are defined, Salesforce defaults to the profile session timeout.

**•** `Custom` —Salesforce uses the value from the `guestJwtTimeout` field.

Available in API version 65.0 and later.


Metadata Types ExtlClntAppOauthConfigurablePolicies

**Field Name** **Description**

```
ipRelaxationPolicyType

isClientCredentialsFlowEnabled

isGuestCodeCredFlowEnabled

isNamedUserJwtEnabled

isTokenExchangeFlowEnabled

label

```

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


Metadata Types ExtlClntAppOauthConfigurablePolicies

**Field Name** **Description**

**Description**
The OAuth policies name for the external client app.

```
namedUserJwtTimeout

namedUserJwtSessionTimeoutType

```

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

**•** `60` —1 Hour

**•** `90` —90 Minutes

**•** `120` —2 Hours

**•** `240` —4 Hours

**•** `480` —8 Hours

**•** `720` —12 Hours

If `namedUserJwtSessionTimeoutType` is set to `UserSession`, omit this
field.

**Field Type**
JWTSessionTimeoutType (enumeration of type string)

**Description**
Specifies how the JWT-based access token timeout is defined for named users. Valid
values are:

**•** `UserSession` —Salesforce uses the value from the `sessionTimeout` field
[in the ProfileSessionSetting type for the named user's profile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_profilesessionsetting.htm)

If there's no profile session timeout for the user, Salesforce uses the
`sessionTimeout` [value from the SessionSettings type.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_securitysettings.htm)

If both are defined, Salesforce defaults to the profile session timeout.

**•** `Custom` —Salesforce uses the value from the `namedUserJwtTimeout` field.

Available in API version 65.0 and later.


Metadata Types ExtlClntAppOauthConfigurablePolicies

**Field Name** **Description**

```
permittedUsersPolicyType

policyAction

refreshTokenPolicyType

refreshTokenValidityPeriod

refreshTokenValidityUnit

```

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


Metadata Types ExtlClntAppOauthConfigurablePolicies

**Field Name** **Description**

**•** `Days`

**•** `Hours`

**•** `Months`

```
requiredSessionLevel

sessionTimeoutInMinutes

singleLogoutUrl

startUrl

```

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

```

**Field Type**
string

**Description**

Required.

The existing field that includes the desired information. For example,
`Organization.Country` .


Metadata Types ExtlClntAppOauthConfigurablePolicies

**Field Name** **Description**

```
key

```

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

```


### Metadata Types ExtlClntAppOauthSettings

```
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

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ExtlClntAppOauthSettings components have the suffix .ecaOauth and are stored in the extlClntAppOauthSettings folder.

Version

### ExtlClntAppOauthSettings components are available in API version 59.0 and later.

Special Access Rules

Access to the OAuth plugin requires orgs to enable the Allow Access to OAuth Consumer Secrets via Metadata API permission in Setup.
The View External Client Apps Consumer Secrets in Metadata user permission is required for users with developer roles to configure
OAuth settings.

Fields

**Field Name** **Description**

```
areAttributesIncludedInAssetToken

```

**Field Type**
boolean


Metadata Types ExtlClntAppOauthSettings

**Field Name** **Description**

**Description**
Indicates whether custom attributes associated with the external client app are included
in the JSON Web Token (JWT) payload of an asset token issued as a result of the asset
token flow. The default value is `false` .

Available in API version 61.0 and later.

```
areCustomPermsIncludedInAssetToken

assetTokenAudiences

assetTokenSigningCertificate

assetTokenValidity

```

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
containing a `StringOrURI` value. Specify an audience for each intended consumer
of the asset token.

Available in API version 61.0 and later.

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


Metadata Types ExtlClntAppOauthSettings

**Field Name** **Description**

```
clientAssertionCertificate

commaSeparatedOauthScopes

```

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


Metadata Types ExtlClntAppOauthSettings

**Field Name** **Description**

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


Metadata Types ExtlClntAppOauthSettings

**Field Name** **Description**

```
isFirstPartyAppEnabled

label

oauthLink

singleLogoutUrl

trustedIpRanges

```

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

```

**Field Type**
string

**Description**

Required.

The existing field that includes the desired information. For example,
`Organization.Country` .


Metadata Types ExtlClntAppOauthSettings

**Field Name** **Description**

```
key

```

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

startIpAddress

```

**Field Type**
string

**Description**
Identifies the purpose of the range, such as which part of a network corresponds to
this range.

**Field Type**
string

**Description**

Required.

Last address in the IP range, inclusive. Required with start address.

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

```


### Metadata Types ExtlClntAppPushConfigurablePolicies

```
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


### Metadata Types ExtlClntAppPushSettings

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

ExtlClntAppPushConfigurablePolicies components have the suffix `.ecaPushPlcy` and are stored in the
`extlClntAppPushPolicies` folder.

Version

ExtlClntAppPushConfigurablePolicies components are available in API version 64.0 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Field Type** **Description**

externalClientApplication string Required. The name of the associated external client app.

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


Metadata Types ExtlClntAppPushSettings

File Suffix and Directory Location

ExtlClntAppPushSettings components have the suffix `.ecaPush` and are stored in the `extlClntAppPushSettings` folder.

Version

ExtlClntAppPushSettings components are available in API version 64.0 and later.

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


Metadata Types ExtlClntAppPushSettings

**Field Name** **Field Type** **Description**

pushServiceType

PushServiceType Required. Identifies the mobile operating system of the mobile app. Valid
[(enumeration](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_objects_intro.htm#enumeration_title) of values are:
type string)

**•** _`Apple`_

**•** _`Android`_

ExtlClntAppAndroidPushConfig

Represents the push notification configuration of an Android mobile app.

**Field Name** **Field Type** **Description**

fcmProject string Required. The ID of the Google Firebase project associated with the
mobile app.

serviceAccount string

ExtlClntAppApplePushConfig

Required. The Base64-encoded Admin SDK private key for your Google
Firebase service account. You can generate this key from the Service
accounts tab in the Google Firebase console.

The maximum length of the string is 8000 characters.

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
[(enumeration](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_objects_intro.htm#enumeration_title) of are:
type string)

**•** _`Production`_

**•** _`Sandbox`_

keyIdentifier string The key identifier for the private key entered in the `signingKey` field.
[See Get a key identifier in Apple Developer documentation.](https://developer.apple.com/help/account/keys/get-a-key-identifier/)

password string The password for the TLS certificate entered in the `certificate`
field.


### Metadata Types ExtlClntAppSamlConfigurablePolicies

**Field Name** **Field Type** **Description**

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

Version

### ExtlClntAppSamlConfigurablePolicies components are available in API version 63.0 and later.

Special Access Rules

To use the ExtlClntAppSamlConfigurablePolicies type, you must have the View all External Client Apps, view their settings, and edit their
policies user permission.

[This type must be related to a parent ExternalClientApplication. Because external client apps with SAML configurations can't be packaged,](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_externalclientapplication.htm)
the `distributionState` for the parent external client app must be set to `Local` .

[The parent external client app must also have an associated ExtlClntAppConfigurablePolicies metadata type where the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_extlclntappconfigurablepolicies.htm)
`isSamlPluginEnabled` field is set to `true` .

Fields

**Field Name** **Description**

```
acsUrl

```

**Field Type**
string


Metadata Types ExtlClntAppSamlConfigurablePolicies

**Field Name** **Description**

**Description**

Required. The assertion consumer service (ACS) URL from the third-party service
provider. The ACS URL is the endpoint where the service provider receives SAML
responses from Salesforce.

```
certificate

commaSeparatedPermissionSet

commaSeparatedProfile

customAttributes

encryptionCertificate

```

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

**Description**
A comma-separated list of profile IDs that defines the profiles required for an end user
to use the SAML SSO flow. Like permission sets, profiles define user permissions. The
profiles that you specify here apply to the entire app, not just its SAML configuration.
We recommend that you use permission sets to manage user permissions instead of
profiles.

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


Metadata Types ExtlClntAppSamlConfigurablePolicies

**Field Name** **Description**

settings. To get the certificate, work with a certificate provider. If you include an
`encryptionCertificate`, make sure that your service provider is configured
to decrypt SAML assertions.

```
encryptionType

entityUrl

externalClientApplication

issuer

label

```

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


Metadata Types ExtlClntAppSamlConfigurablePolicies

**Field Name** **Description**

```
nameIdFormat

signingAlgorithmType

singleLogoutBindingType

singleLogoutUrl

```

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
SAML responses, it validates the signature. Salesforce also applies this algorithm to
single logout requests and responses.

These values are valid.

**•** `SHA1` —Secure Hash Algorithm (SHA) 1 algorithm, which generates a 160-bit
hash value.

**•** `SHA256` —SHA-256 algorithm,which generates a 256-bit hash value.

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


Metadata Types ExtlClntAppSamlConfigurablePolicies

**Field Name** **Description**

**Description**
The SAML single logout endpoint on the service provider. When Salesforce initiates
single logout, it sends logout requests to this endpoint.

```
startUrl

subjectCustomAttribute

subjectType

```

**Field Type**
string

**Description**
A URL where users are directed after they authenticate. For example, direct users to a
specific page in the service provider app.

Deprecated. Use the `startUrl` [field on the ExtlClntAppConfigurablePolicies](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_extlclntappconfigurablepolicies.htm)
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


Metadata Types ExtlClntAppSamlConfigurablePolicies

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


### Metadata Types FeatureParameterBoolean

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

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### FeatureParameterBoolean components have the suffix .featureParameterBoolean . The components are stored in the

`featureParameters` folder, which contains components for all the feature parameter metadata types.

Version

### FeatureParameterBoolean components are available in API version 41.0 and later.

Special Access Rules

[Available to package developers who have access to the Feature Management App (FMA). For details, see Manage Features in the](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/fma_manage_features.htm)
_Second-Generation Managed Packaging Developer Guide_ .


Metadata Types FeatureParameterBoolean

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

`FeatureParameterDataFlowDirection` string After a package containing the components is installed,
indicates whether the feature parameter’s value is

editable in your License Management Org (LMO) and
read-only in your customer’s org or the other way around.
Valid values are:

**•** `LmoToSubscriber`

**•** `SubscriberToLmo`

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

```


### Metadata Types FeatureParameterDate

```
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
activation metrics in subscriber orgs that install your package.This type extends the Metadata metadata type and inherits its `fullName`
field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### FeatureParameterDate components have the suffix .featureParameterDate . The components are stored in the

`featureParameters` folder, which contains components for all the feature parameter metadata types.

Version

### FeatureParameterDate components are available in API version 41.0 and later.

Special Access Rules

[Available to package developers who have access to the Feature Management App (FMA). For details, see Manage Features in the](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/fma_manage_features.htm)
_Second-Generation Managed Packaging Developer Guide_ .

Fields

**Field Name** **Field Type** **Description**

`dataFlowDirection` FeatureParameterDataFlowDirection After a package containing the components is installed,
indicates whether the feature parameter’s value is

editable in your License Management Org (LMO) and
read-only in your customer’s org or the other way around.


Metadata Types FeatureParameterDate

**Field Name** **Field Type** **Description**

`masterLabel` string The feature parameter name that appears in the user
interface.

`value` date

FeatureParameterDataFlowDirection

The default value for this feature parameter. You can
reference this value in your code, just like you reference
other values in a subscriber’s org.

Represents the direction of the data flow between your License Management Org (LMO) and the customer’s org.

**Field Name** **Field Type** **Description**

`FeatureParameterDataFlowDirection` string After a package containing the components is installed,
indicates whether the feature parameter’s value is

editable in your License Management Org (LMO) and
read-only in your customer’s org or the other way around.
Valid values are:

**•** `LmoToSubscriber`

**•** `SubscriberToLmo`

Declarative Metadata Sample Definition

The following is an example of a FeatureParameterDate component.

```
<?xml version="1.0" encoding="UTF-8"?>

<FeatureParameterDate xmlns="http://soap.sforce.com/2006/04/metadata">

   <dataflowDirection>SubscriberToLmo</dataflowDirection>

   <masterLabel>Activation Date</masterLabel>

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

```


### Metadata Types FeatureParameterInteger

```
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

The default value for this feature parameter. You can
reference this value in your code, just like you reference
other values in a subscriber’s org.


Metadata Types FeatureParameterInteger

FeatureParameterDataFlowDirection

Represents the direction of the data flow between your License Management Org (LMO) and the customer’s org.

**Field Name** **Field Type** **Description**

`FeatureParameterDataFlowDirection` string After a package containing the components is installed,
indicates whether the feature parameter’s value is

editable in your License Management Org (LMO) and
read-only in your customer’s org or the other way around.
Valid values are:

**•** `LmoToSubscriber`

**•** `SubscriberToLmo`

Declarative Metadata Sample Definition

The following is an example of a FeatureParameterInteger component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <FeatureParameterInteger xmlns="http://soap.sforce.com/2006/04/metadata">

      <dataflowDirection>SubscriberToLmo</dataflowDirection>

      <masterLabel>Current Project Count</masterLabel>

      <value>42</value>

   </FeatureParameterInteger>

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


### Metadata Types FieldMappingConfig FieldMappingConfig

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

DeveloperName

Language

```

**Type**
textarea

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the field mapping configuration.

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


Metadata Types FieldMappingConfig

**Field** **Details**

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

```
MasterLabel

NamespacePrefix

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for the FieldMappingConfig.

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


### Metadata Types FieldRestrictionRule **Field Details**

**•** In organizations that are not Developer Edition organizations, `NamespacePrefix`
is only set for objects that are part of an installed managed package. There is no
namespace prefix for all other objects.

```
ProcessType

SourceObjectId

### FieldRestrictionRule

```

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

**Description**
The ID of the source object for all of the fields mapped in the configuration.

Possible values are:

**•** `GiftEntry`

Represents a field visibility rule that controls whether a field is visible to a user, based on the field’s inclusion in a field set. If Enhanced
Personal Information Management setting was enabled before Spring ’22, field visibility is based on the field’s compliance categorization.
This type extends the Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### FieldRestrictionRule components have the suffix .rule and are stored in the fieldRestrictionRules folder.


Metadata Types FieldRestrictionRule

Version

FieldRestrictionRule components are available in API version 52.0 and later.

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


Metadata Types FieldRestrictionRule

**Field Name** **Field Type** **Description**

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


### Metadata Types FlexiPage

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

**–** To customize the layout of record pages, the Salesforce Home page, and the Email Application pane in the Outlook and Gmail
integrations.

**–** As the home page for an app.

**–** As the utility bar for a Lightning app.

For more information on Lightning pages, see Salesforce Help.

Note: The namespace prefix is important to help identify the source of items like fields, custom objects, and more. For example,
when working with FlexiPages, we recommend keeping namespaces for object fields, because removing them can cause unexpected
results such as name collisions.

File Suffix and Directory Location

### FlexiPage components have the suffix .flexipage and are stored in the flexipages folder.

Version

### FlexiPage components are available in API version 29.0 and later.


Metadata Types FlexiPage

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

Metadata Types FlexiPage

**Field Name** **Field Type** **Description**

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


Metadata Types FlexiPage

**Field Name** **Field Type** **Description**

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


Metadata Types FlexiPage

**Field Name** **Field Type** **Description**

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


Metadata Types FlexiPage

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


Metadata Types FlexiPage

**Field Name** **Field Type** **Description**

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

**Field Name** **Field Type** **Description**

`appendable` RegionFlagStatus
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

Metadata Types FlexiPage

**Field Name** **Field Type** **Description**

`componentInstances` ComponentInstance[]

`itemInstances` ItemInstance[]

`mode` FlexiPageRegionMode
(enumeration of type string)

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

`replaceable` RegionFlagStatus
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

**•** If all the properties are set to `disabled`, the region is
locked

**•** If none of the properties are specified OR any of these three
properties are missing, the region is unlocked.

This field is available in API version 35.0 or later.

This field is available in Digital Experiences in API 45.0 or later,
but is reserved for future use for all other areas.

Valid values are:

**•** `disabled`

**•** `enabled`

This field is assessed in combination with `appendable` and
`prependable` .

**•** If all the properties are set to `enabled`, the region is
unlocked

Metadata Types FlexiPage

**Field Name** **Field Type** **Description**

**•** If all the properties are set to `disabled`, the region is
locked

**•** If none of the properties are specified OR any of these three
properties are missing, the region is unlocked.

This field is available in API version 35.0 or later.

`type` FlexiPageRegionType
(enumeration of type string)

ItemInstance

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

ComponentInstance

Instance of a component in a page, such as a filter list.

API name, label, and visibility rule information of the
field component. This field is available only on
Lightning pages that use Dynamic Forms.

**Field Name** **Field Type** **Description**

`componentInstanceProperties` ComponentInstanceProperty[] The value of a single property in a component instance.

`componentName` string Required. The name of a single instance of a
component.

`identifier` string Required. The unique name of the ComponentInstance.
Provides a way to uniquely identify an individual

instance of a component on a Lightning page. This
field has a maximum limit of 120 characters.

This field is available in API version 53.0 and later.


Metadata Types FlexiPage

**Field Name** **Field Type** **Description**

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


Metadata Types FlexiPage

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


Metadata Types FlexiPage

**API Name** **Available** **Available Values** **UI Label**
**Objects**

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

**Field Name** **Field Type** **Description**

`valueListItems` ComponentInstancePropertyListItem[] An array of elements in a component instance.

ComponentInstancePropertyListItem

Name of an element in an array in a component instance.

**Field Name** **Field Type** **Description**

`value` string Name of an element in an array in a component instance.

In API version 49.0 and later, arrays in a FlexiPage are represented as `valueList` . Each array element is represented as
`valueListItem`, and the element name is represented as `value` .


Metadata Types FlexiPage

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


Metadata Types FlexiPage

**Field Name** **Field Type** **Description**

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

`fieldInstanceProperties` FieldInstanceProperty on page 1203[] Properties of the field instance. Contains a name and
value pair for each property associated with the field.

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


Metadata Types FlexiPage

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

**Field Name** **Field Type** **Description**

`name` string Required. The name of a single instance of a template.

`properties` ComponentInstanceProperty[]


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

Metadata Types FlexiPage

PlatformActionList

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

`platformActionListItems` PlatformActionListItem[] The actions in the PlatformActionList.

`relatedSourceEntity` string

PlatformActionListItem

When the `ActionListContext` is RelatedList or RelatedListRecord,
this field represents the API name of the related list to which the action
belongs.

PlatformActionListItem represents an action in the PlatformActionList. Available in API version 34.0 and later.

**Field Name** **Field Type** **Description**

`actionName` string Required. The API name for the action in the list.


Metadata Types FlexiPage

**Field Name** **Field Type** **Description**

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

```


Metadata Types FlexiPage

```
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

```


Metadata Types FlexiPage

```
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

```


Metadata Types FlexiPage

```
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

```


Metadata Types FlexiPage

```
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


### Metadata Types Flow

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

**•** You can deploy changes to an active flow if in a non-production org, such as a scratch or sandbox org. To deploy changes in a
production org, you must enable the **Deploy processes and flows as active** preference. After you deploy changes to an active
flow, the flow’s detail page shows a new flow version that’s active. The new version includes your changes.

**•** You can delete a flow version if it isn’t active and doesn’t have any paused interviews. If the flow version has paused interviews, wait
for those interviews to resume and finish, or delete them.

Warning: Don’t edit the metadata of retrieved Process Builder processes, such as flow components whose processType is
`Workflow` or `InvocableProcess` . If you deploy process metadata that you edited, you can’t open the process in the target
org.

Declarative Metadata File Suffix and Directory Location

### Flows are stored in the Flow directory of the corresponding package directory. The file name matches the flow’s unique full name,

and the extension is `.flow` .


Metadata Types Flow

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


Metadata Types Flow

**Field Name** **Field Type** **Description**

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

`interviewLabel` string

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


Metadata Types Flow

**Field Name** **Field Type** **Description**

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


Metadata Types Flow

**Field Name** **Field Type** **Description**

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


Metadata Types Flow

**Field Name** **Field Type** **Description**

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


Metadata Types Flow

**Field Name** **Field Type** **Description**

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


Metadata Types Flow

**Field Name** **Field Type** **Description**

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


Metadata Types Flow

FlowActionCall

Defines a call to an action from the flow. It extends FlowNode.

This metadata type is available in API version 31.0 and later.

**Field Name** **Field Type** **Description**

`actionCallPaths` ActionCallPath[] Reserved for future use.

`actionName` string Required. Name for the action. Must be unique across
actions with the same `actionType` .

`actionType` InvocableActionType (enumeration of type Required. See InvocableActionType on page 1219.
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

**•** `CurrentTransaction`                            - Keeps the invocable
action running in the same transaction.

**•** `NewTransaction`                            - Creates a transaction before
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


Metadata Types Flow

**Field Name** **Field Type** **Description**

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

This field is available in API version 66.0 and later.

`versionSegment` int Specifies the version of the versioned action. By default, the
value is 1. Supported only when versionSegment is specified.

This field is available in API version 58.0 to 61.0. This field is
deprecated in API version 62.0 and later.

`versionString` string Reserved for future use.

InvocableActionType

The valid values in the required `actionType` on FlowActionCall on page 1218.

**Valid Value** **Description**

`activateSessionPermSet` Activates a session-based permission set for the running user.

`activationSchema` Gets the activation schema for the specified activation. This value is available in API version 64.0
and later.


Metadata Types Flow

**Valid Value** **Description**

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


Metadata Types Flow

**Valid Value** **Description**

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


Metadata Types Flow

**Valid Value** **Description**

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


Metadata Types Flow

**Valid Value** **Description**

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
in API version 61.0 and later.

`getSearchConfigurationMetadata` Retrieves all metadata details and search configurations for a given searchable object. Available
in API version 64.0 and later.

`getTranscriptForConversation` Gets the transcript for a specified conversation record such as voice call, messaging session, or
chat transcript. This value is available in API version 64.0 and later.

```
getVerificationData

```

Calls an invocable action to get verification data for selectedPrimaryVerificationContext and
adds the results to selectedPrimaryVerificationContext. This value is available in API version 54.0
and later.

`goToCadenceStep` Jumps to the specified step in the Sales cadence. This value is available in API version 57.0 and
later.

`internalTestAction` Reserved for internal use.

`internalTestConnectApiAction` Reserved for internal use.

```
limitRepetitions

```

Limit the number of times the same recommendation or offer appears on the same record or
for the same user during a time period in a recommendation strategy flow. This value is available
in API version 55.0 and later.

`lockRecord` Lock or unlock a workflow-enabled or approval-enabled record for editing during an approval
and specify who can edit the record while it's locked.

```
lwcComponent

```

Triggers the LWC component that targets the lightning__FlowAction target in the XML
configuration file and that's referenced by actionName. This value is available in API version 63.0
and later.

`massUpdateAccountForecast` Bulk updates forecasts asynchronously. This value is available in API version 48.0 and later.


Metadata Types Flow

**Valid Value** **Description**

`massUpdateSalesAgreement` Bulk updates sales agreements asynchronously. This value is available in API version 48.0 and
later.

`processDataUsingGenAi` Using Einstein generative AI, performs NLP to summarize text, extract key phrases, analyze
sentiment, and unlock valuable insights. This value is available in API version 61.0 and later.

`publishActionableOrchSrcEvent` Publishes events triggered by an external system. This value is available in API version 62.0 and
later.

`publishKnowledgeArticles` Mass publishes knowledge articles from article list views. This value is available in API version
44.0 and later.

`quickAction` Invokes a Quick Action.

`replenishInventoryUsingPolicy` Executes inventory policy to identify stock shortages, determine the optimal source location,
and automate replenishment. Available in API version 65.0 and later.

`rescheduleRecurringHomeVisits` Reschedules all the home visits based on the recurrence pattern and scheduling policy provided.
This value is available in API version 60.0 and later.

`restoreKnowledgeArticleVersion` Restores an archived version of a knowledge article. This value is available in API version 45.0
and later.

```
reviewBuyingCommittee

rpa

scheduleGroupVisits

```

Identifies and reviews key contacts associated with a deal, their influence on that deal, and other
deals that they’ve impacted. This value is available in API version 63.0 and later.

Performs a set of actions in a defined scope outside the flow, such as operating a session or
using an application on a on-premises computer via an RPA robot. This value is available in API
version 63.0 and later.

Create visiting records for patient home visits by bundling them into a group and scheduling
either a single start-of-care visit or a series of recurring visits associated with the bundled records.
This value is available in API version 60.0 and later.

`sendAlert` Sends Salesforce Anywhere alerts to users. This value is available in API version 49.0 and later.

`sendNotification` Sends an available notification type. This value is available in API version 54.0 and later.

`sendSurveyInvitation` Sends email survey invitations to leads, contacts, and users in your org based on an action, such
as when a customer support case closes. This value is available in API version 47.0 and later.

`pardotSlackCompletionActionNotification` Sends a user a Slack notification when a prospect completes an activity in Account Engagement.

`performSurveySentimentAnalysis` Perform survey sentiment analysis to create or update the AI Sentiment Result records. This
value is available in API version 55.0 and later.

`skillsBasedRouting` Creates a PendingServiceRouting record used for Omni-Channel skills-based routing. This value
is available in version 44.0 and later.

`slackArchiveChannel` Archives a Slack channel in a Slack workspace. This value is available in API version 54.0 and later.

`slackCheckUsersAreConnectedToSlack` Indicates whether a collection of Salesforce users is connected to a given Slack app. This value
is available in API version 54.0 and later.

`slackCreateChannel` Creates a Slack channel in a Slack workspace. This value is available in API version 54.0 and later.


Metadata Types Flow

**Valid Value** **Description**

`slackGetConversationInfo` Retrieves the name of a Slack channel or group direct message and finds out whether it's archived.
This value is available in API version 54.0 and later.

`slackInviteUsersToChannel` Adds users who are connected to a given Slack app to a Slack channel or group direct message.
This value is available in API version 54.0 and later.

`slackPinMessage` Pin or unpin a message in a Slack channel or group direct message. This value is available in API
version 54.0 and later.

`slackPostMessage` Send a message to a Slack channel or group direct message. This value is available in API version
54.0 and later.

```
slackSendMessageToLaunchFlow

```

Send a message to a Slack channel, direct message, or the Messages tab of a Slack app that
includes a button that a recipient can use to launch a screen flow. This value is available in API
version 55.0 and later.

`slackUpdateMessage` Edits a message that was previously sent to a Slack channel or group direct message. This value
is available in API version 54.0 and later.

`submitKnowledgeArticleForTranslation` Submits a published or draft knowledge article for translation. This value is available in API version
46.0 and later.

`submit` Submits a record for approval.

`transformMfgProgramForecasts` Transform an AI Natural Language Processing (NLP) result created by using Einstein Generative
AI into an Apex Object record. This value is available in API version 61.0 and later.

`transformNlpActionResult` Transform an AI Natural Language Processing (NLP) result created by using Einstein Generative
AI into an Apex Object record. This value is available in API version 61.0 and later.

`triggerJourney` Send an individual to a specified journey. This value is available in API version 64.0 and later

`verifyCustomerCode` Verifies the code entered by the customer to complete identity verification. This value is available
in API version 63.0 and later.

These values are used in Omnichannel Inventory. If no version is specified, the value is available in API version 51.0 and later.

**Valid Value** **Description**

`ociCreateReservation` Creates one or more inventory reservations at a location or location group.

`ociFulfillReservation` Fulfills one or more inventory reservations at a location.

`ociGetAvailability` Gets inventory availability data for one or more products at one or more inventory locations or
location groups.

`ociReleaseReservation` Releases one or more inventory reservations.

`ociTransferReservation` Transfers one or more inventory reservations between locations or location groups.

These values are used in the B2B Commerce Checkout Flow. If no version is specified, the value is available in API version 47.0 and later.


Metadata Types Flow

**Valid Value** **Description**

`updateCheckoutSessionStateAction` Updates the checkout session next state for checkout flows. This value is available in API version
49.0 and later.

`priceCart` Requests prices for all items in a cart during B2B Commerce checkout. This value is available in
API version 47.0 and later.

`checkoutSessionAction` Initiates or retrieves an existing Checkout Session for Checkout Flows. Available to B2B Commerce.
This value is available in API version 49.0 and later.

`cancelCartAsyncOperation` Cancels a WebCart's async operation. Available to B2B Commerce. This value is available in API
version 49.0 and later.

`calcCartPromotionsAction` Requests a full cart promotion calculation of all applicable line items in the Web Cart during B2B
Commerce checkout. This value is available in API version 52.0 and later.

`checkCartInventoryAction` Requests an inventory for all items in a Web Cart during B2B Commerce checkout. This value is
available in API version 47.0 and later.

`calcCartShipmentAction` Calculates the shipping cost for all items in a Web Cart during B2B Commerce checkout. This
value is available in API version 47.0 and later.

`cartToOrderAction` Creates a Salesforce Standard Order in draft mode. This value is available in API version 47.0 and
later.

`activateOrderAction` Activates a draft order, which creates an order summary. This value is available in API version
47.0 and later.

These values are used in the B2B Commerce and D2C Commerce.

**Valid Value** **Description**

`recordTaxReversal` Reverses the recorded tax transactions in an external system. This value is available in API version
62.0 and later.

`recordTaxTransaction` Records tax transactions from an order summary to an external system. This value is available
in API version 62.0 and later.

These values are used in Data Cloud.

**Valid Value** **Description**

`dataKitGetComponentAction` Gets the deployment status of data kit deployment jobs. This value is available in API version
64.

`dataKitDeployComponentAction` Deploys data kit components in a target org. This value is available in API version 64.

These values are used in Education Cloud.


Metadata Types Flow

**Valid Value** **Description**

`getAcademicTermData` Gets the details of the academic term that the specified learner is enrolled in. This value is available
in API version 65.0.

`getBatchJobIds` Gets the identifiers of batch jobs. This value is available in API version 64.

`getLearningProgramData` Gets the learning program data based on the learning program name. This value is available in
API version 65.0.

`getProgramTermApplTimelineData` Gets the program term application timeline data based on the academic term ID and learning
program ID. This value is available in API version 65.0.

`getRestrictionsAsgnToStudent` Gets the details of the restrictions (business process operations) assigned to a student. This value
is available in API version 65.0.

These values are used in the Commerce Checkout Flow. If no version is specified, the value is available in API version 55.0 and later.

**Valid Value** **Description**

`addCartItem` Adds an item to a cart during Commerce checkout.

`createCart` Creates a cart during Commerce checkout.

`deleteCart` Deletes a cart during Commerce checkout.

These values are used in Salesforce CMS Workflows and Approvals. If no version is specified, the value is available in API version 58.0 and
later.

**Valid Value** **Description**

`managedContentPublishVariant` Publishes a content variant associated with a flow. This value is available in API version 59.0 and
later.

`managedContentRoleStepInteractive` Assigns a content variant review to a CMS role.

`managedContentUnpublishVariant` Unpublishes a published content variant associated with a flow. This value is available in API
version 59.0 and later.

`managedContentVariantSetLockStatus` Sets the locked status of a content variant.

`managedContentVariantSetReadyStatus` Sets the ready for publication status of a content variant.

These values are used in Order Management. If no version is specified, the value is available in API version 48.0 and later.

**Valid Value** **Description**

`addOrderItemSummarySubmit` Adds order item summaries to an order summary. This value is available in API version 54.0 and
later.

`adjustOrderItemSummariesPreview` Previews the expected results of applying a price adjustment to order item summaries from an
order summary without actually applying it. This value is available in API version 49.0 and later.


Metadata Types Flow

**Valid Value** **Description**

`adjustOrderItemSummariesSubmit` Applies a price adjustment to order item summaries from an order summary. This value is
available in API version 49.0 and later.

`authorizePayment` Authorizes a card payment. This value is available in API version 55.0 and later.

`cancelFulfillmentOrderItem` Removes items from a fulfillment order.

`cancelOrderItemSummariesPreview` Previews the expected results of canceling order item summaries from an order summary without
actually canceling them.

`cancelOrderItemSummariesSubmit` Cancels order item summaries from an order summary.

`confirmHeldFulfillmentOrderCapacity` Confirms held fulfillment order capacity. This value is available in API version 55.0 and later.

`createCreditMemoOrderSummary` Creates a credit memo for an order summary.

`createFulfillmentOrder` Creates one or more fulfillment orders and fulfillment order products for an order delivery group
summary, which defines a recipient and delivery method.

```
createFulfillmentOrders

```

Creates fulfillment orders and fulfillment order products for multiple order delivery group
summaries, each of which defines a recipient and delivery method. This value is available in API
version 51.0 and later.

`createInvoiceFromChangeOrders` Creates an invoice for one or more change orders. This value is available in API version 56.0 and
later.

`createInvoiceFromFulfillmentOrder` Creates an invoice for a fulfillment order.

`createOrderPaymentSummary` Creates an order payment summary for an authorization or payments belonging to an order
summary.

`createOrderSummary` Creates an order summary for an order.

`createReturnOrder` Creates a return order and return order items for an order.

`ensureFundsOrderSummaryAsync` Triggers an asynchronous background process to ensure funds through a payment provider for
an invoice belonging to an order summary.

`ensureRefundsOrderSummaryAsync` Triggers an asynchronous background process to ensure refunds through a payment provider
for an invoice belonging to an order summary.

`getFulfillmentOrderCapacityValues` Gets fulfillment order capacity information. This value is available in API version 55.0 and later.

`holdFulfillmentOrderCapacity` Holds fulfillment order capacity. This value is available in API version 55.0 and later.

```
orderRoutingFindRoutesWithFewestSplits

orderRoutingFindRoutesWithFewestSplitsUsingOCI

```

Evaluates ordered product quantities against available inventory to determine the smallest
combination of locations that can fulfill the order. This value is available in API version 51.0 and
later.

Evaluates ordered product quantities against available inventory at specified location groups
and locations to determine the smallest combination of locations that can fulfill the order. This
value is available in API version 54.0 and later.

`orderRoutingRankByAverageDistance` Calculates the average distance from sets of inventory locations to an order recipient, and returns
the sets sorted by that average distance. This value is available in API version 51.0 and later.


Metadata Types Flow

**Valid Value** **Description**

`releaseHeldFulfillmentOrderCapacity` Releases held fulfillment order capacity. This value is available in API version 55.0 and later.

`returnOrderItemSummariesPreview` Previews the expected results of returning order item summaries from an order summary without
actually returning them.

`returnOrderItemSummariesSubmit` Returns order item summaries from an order summary.

`returnReturnOrderItems` Processes return order line items.

These values are used in the Employee Service. If no version is specified, the value is available in API version 63.0 and later.

**Valid Value** **Description**

`createServiceRequestCase` Creates a case or incident for the requested service.

`getDirectDepositDetails` Gets the direct deposit details for the specified record ID.

`getLeaveBalance` Gets the leave balance of a specific employee.

These values are used in Rebate Management.

**Valid Value** **Description**

`addRebateMemberList` Adds a list of members to a rebate program. This value is available in API version 51.0 and later.

`calculateProjectedRebateAmount` Calculates the projected rebate amount for rebate types associated with a specified transaction
ID. This value is available in API version 54.0 and later.

`calculateRebateAmountAndUpsertPayout` Calculates the rebate amount and upserts the rebate payout for the specified aggregate record.
This value is available in API version 51.0 and later.

`getBenefitAndCalculateRebateAmount` Gets benefit details, and optionally calculates the rebate amount for the specified aggregate
record. This value is available in API version 51.0 and later.

`getEligibleProgramRebateTypes` Retrieves the eligible program rebate types for a mapped object. This value is available in API
version 52.0 and later.

`generateRebatePayoutPeriods` Generates payout periods for a rebate program based on the frequency specified in the program.
This value is available in API version 51.0 and later.

`processRebatesBatchCalculationJob` Processes a rebate batch calculation job from the Data Processing Engine. This value is available
in API version 51.0 and later.

`processProgramRebateTypeProducts` Insert or delete records in the Program Rebate Type Product object. This value is available in API
version 53.0 and later.

`rebatesProcessCSV` Processes an uploaded CSV file using Bulk API 2.0 and converts the file’s data into records in the
target object. This value is available in API version 51.0 and later.

`upsertCustomRebatePayout` Upserts the custom calculated rebate payout for the specified aggregate record. This value is
available in API version 51.0 and later.


Metadata Types Flow

These values are for Decision Table. If no version is specified, the value is available in API version 51.0 and later.

**Valid Value** **Description**

`decisionTableAction` Runs an active decision table definition.

`refreshDecisionTable` Refreshes the decision table cache.

These values are used in Einstein generative AI features.

**Valid Value** **Description**

`generatePromptResponse` Generates a response based on the large language model (LLM) response for the specified
prompt template and inputs. This value is available in API version 60.0 and later.

`transformQueryForCase` Generates a natural language query for retrieval based on the specified case details, language,
and additional context. This value is available in API version 62.0 and later.

`transformQueryForConversation` Generates a natural language query for retrieval based on the specified conversation text,
language, and additional context. This value is available in API version 62.0 and later.

`transformQueryForEmail` Generates a natural language query for retrieval based on the specified email details, language,
and additional context. This value is available in API version 62.0 and later.

These values are used in flows for Engagement.

**Valid Value** **Description**

`createEngagementsDetailsRep` Creates a JSON representation. Use the details of Engagement Interaction, Messaging Session,
and Voice Call records; the related Engagement Topic and Note records; and transcripts from

the conversation to create a JSON representation. This value is available in API version 64.0 and
later.

`getConversationTranscripts` Gets the list of transcripts of the conversations between an agent and a customer.

`getEngagements` Gets engagement interaction, messaging session, and voice call records associated with a
specified account record.

`getRecordDetails` Gets the details of specified records, including the name of the parent record.

These values are used in Field Service. If no version is specified, the value is available in API version 52.0 and later.

**Valid Value** **Description**

`addWorkPlans` Creates work plan and work step objects from the work plan library.

`cancelWorkOrder` Cancels a work order.

`completeWorkOrder` Completes a work order.

`createWorkOrder` Creates a work order.


Metadata Types Flow

**Valid Value** **Description**

`createWorkOrderLineItem` Creates a work order line item.

`createWorkPlan` Creates a work plan.

`createWorkStep` Creates a work step.

`getWorkOrderDetails` Gets work order details.

`getWorkPlanDetails` Gets work plan details.

`getWorkStepDetails` Gets work step details.

`updateWorkOrder` Updates a work order.

`updateWorkOrderLineItem` Updates a work order line item.

`updateWorkPlan` Updates a work plan.

`updateWorkStep` Updates a work step.

`addWorkSteps` Creates work step objects from the work plan library.

`deleteWorkPlans` Deletes all the work plans and work steps associated with a work order or work order line item.

`generateWorkPlans` Generates work plans based off rules defined in the work plan library.

These values are used in Einstein Bots. If no version is specified, the value is available in API version 56.0 and later.

**Valid Value** **Description**

`getDataCategoryDetails` Gets the labels and API names for a specified data category associated with the knowledge base.
This value is available in API version 56.0 and later.

`getDataCategoryGroups` Gets the labels and API names of the active data category groups associated with the Knowledge
object that’s visible to the current user.

`searchKnowledgeArticles` Searches for knowledge articles with specified search terms, language, data category group,
and data category.

This value is used for Einstein Initiate Language Processing Action.

**Valid Value** **Description**

`initiateNaturalLangProcessing` Create a record for the AI natural language processing result and initiate text processing by using
the service specified in the related record. This value is available in API version 60.0 and later.

These values are used in Einstein Work summaries. If no version is specified, the value is available in API version 63.0 and later.


Metadata Types Flow

**Valid Value** **Description**

`getCaseInfoToSummarize` Gets case field details like subject, description, comments, emails, and conversation transcripts
for use with prompt templates in Prompt Studio.

`getConvTrscpForRecord` Gets the conversation transcript associated with a VoiceCall, MessagingSession, or
LiveChatTranscript record.

This value is used in Media Cloud.

**Valid Value** **Description**

`vlocity_cmt__MediaIntegrationProcedureInvocable` Call an Integration Procedure from a Salesforce Flow to process media content. This value is
available in API version 60.0 and later.

These values are used in the Get Forecast Guidance flow.

**Valid Value** **Description**

`getForecastContext` Gets the forecast context for a specified user. This value is available in API version 61.0 and later.

`getForecastOpportunities` Gets forecast opportunities for a user that matches the specified criteria. This value is available
in API version 61.0 and later.

This value is used in the Get Opportunity Grounding Data flow.

**Valid Value** **Description**

`getOpportunityContentNote` Gets the content note data for a specified opportunity record. This value is available in API version
64.0 and later.

This value is used in the Process Field Update Suggestions flow.

**Valid Value** **Description**

```
getOrExecFieldUpdtSuggestion

```

Enqueues requests to get a field update suggestion from a field generation prompt template.
Also enqueues requests to update a field based on the generated suggestion. This value is
available in API version 64.0 and later.

This value is used in Einstein Case Classification flow.

**Valid Value** **Description**

`applyCaseClassificationRecommendations` Takes a Case ID as input and outputs a case SObject with recommendations applied. This value
is available in API version 57.0 and later.


Metadata Types Flow

These values are used in the Activities: Match Email to Records flow. Sync Email as Salesforce Activity must be enabled.

**Valid Value** **Description**

`associateRecordsWithActivity` Updates the specified email message to associate it with specified records. This value is available
in API version 64.0 and later.

```
getAcctOpptyFromEmailAddr

```

Gets an account record associated with one of the specified contacts or unmatched email
addresses and also gets an opportunity record related to the account. This value is available in
API version 63.0 and later.

`getContcLeadsFromEmailAddr` Matches email addresses to contact and lead records related to specified active user records.
This value is available in API version 63.0 and later.

```
getUsersFromEmailAddresses

```

Gets user records with email addresses that match those specified in the To, From, or CC address
field after a sent email is captured by Einstein Activity Capture. This value is available in API
version 63.0 and later.

These values are used in the Identity User Registration flow.

**Valid Value** **Description**

`generateUserData` Generates placeholder user data for the fields that are required to create a user. Available in API
version 64.0 and later.

```
getUserDataFromJsonString

```

Gets an attribute value from a JSON object that has been serialized into a string. Use this action
to retrieve user information from the identity provider's ID token and user info response. Available
in API version 64.0 and later.

These values are used in the Contracts flow.

**Valid Value** **Description**

`checkInContractDocumentVersion` Check-in a contract document version. Available in API version 64.0 and later.

`checkOutContractDocumentVersion` Check-out a contract document version. Available in API version 64.0 and later.

`createContractDocumentVersion` Creates a contract document version. Available in API version 64.0 and later.

`deleteContractDocumentVersion` Deletes a contract document version. Available in API version 64.0 and later.

`getContractDocumentVersion` Gets a contract document version. Available in API version 64.0 and later.

`updateContractDocumentVersion` Updates a contract document version. Available in API version 64.0 and later.

`checkOutContractDocVersion` Check-out a contract document version. Available in API version 64.0 and later.

`createClmContract` Create a contract for a specified record. Available in API version 64.0 and later.

`getCntntDocDtlForCntrDocVer` Get content document details for the contract document version. Available in API version 64.0
and later.

`getContractDocumentVersions` Get contract document versions. Available in API version 64.0 and later.


Metadata Types Flow

**Valid Value** **Description**

`performContractAction` Perform actions on a contract based on its status. Available in API version 64.0 and later.

`sendContractForESignature` Send a contract to specified recipients for e-signature. Available in API version 64.0 and later.

`unlockContractDocumentVersion` Unlock an active contract document version that the user previously locked. Available in API
version 64.0 and later.

`updateClmContracts` Update contract for a specified record and update or create associated contract documents.
Available in API version 64.0 and later.

These values are used in the Einstein GPT Usecases flow.

**Valid Value** **Description**

`createCaseForFinclAcctAddrUpdt` Create a case to update the financial account address. Available in API version 64.0 and later.

`createVisitForContextRecord` Create a visit to record context. Available in API version 64.0 and later.

`draftAGiftProposal` Create a gift proposal for an account. Available in API version 64.0 and later.

`getCardDetailsForAccount` Get card details for an account. Available in API version 64.0 and later.

`getFinancialAccountAddresses` Get financial account address details for an account. Available in API version 64.0 and later.

`getFinancialTransactions` Get all financial account transactions associated with a specific financial account. Available in
API version 64.0 and later.

`summarizeMedicalHistoryForPatient` Summarize medical history of a specified patient. Available in API version 64.0 and later.

`summarizeMedicationDetailsForPatient` Summarize medication details of a specified patient. Available in API version 64.0 and later.

This value is used in the Grantmaking flow.

**Valid Value** **Description**

`getActiveApplicationReviewerIds` Retrieves the user IDs of all active users who have the ReviewApplication user permission. This
value is available in API version 64.0 and later.

These values are used in Unified Catalog. If no version is specified, the value is available in API version 64.0 and later.

**Valid Value** **Description**

`checkProductEligibility` Determines whether a user is eligible for a list of products, which represent service processes,
based on predefined criteria.

`checkSvcPrcActionEligibility` Determines whether an AI agent is eligible for a list of products, which represent service processes,
and if the list is linked to a service process.

These values are for the Batch Management jobs.


Metadata Types Flow

**Valid Value** **Description**

`batchJobAction` Runs the batch management jobs definitions. This value is available in API version 51.0 and later.

`submitFailedRecordsBatchJob` Resubmits an existing batch job with failed records for processing. This value is available in API
version 52.0 and later.

This value is for Data Processing Engine.

**Valid Value** **Description**

`dataProcessingEngineAction` Runs the data processing engine definitions. This value is available in API version 51.0 and later.

This value is used for Einstein Visit Recommendation.

**Valid Value** **Description**

`saveRecommendationDecision` Save visit and task recommendation decisions. This value is available in API version 51.0 and
later.

This value is used in Public Sector Solutions.

**Valid Value** **Description**

`createBenefitDisbursement` Creates a benefit disbursement for an eligible benefit assignment. This value is available in API
version 57.0 and later.

`runRecordAggrBatchProcDef` Runs a Data Processing Engine definition to process an asynchronous batch job that creates or
updates record aggregation results. This value is available in API version 59.0 and later.

These values are used in Einstein Conversation Insights.

**Valid Value** **Description**

`getConversationIntelligence` Gets the conversation intelligence information about a voice or video call, including any insights
and the conversation summary. This value is available in API version 65.0 and later.

`getConversationTranscript` Gets the conversation transcript for the specified voice or video call record. This value is available
in API version 63.0 and later.

This value is used in the Get Opportunity Details flow.

**Valid Value** **Description**

`getRecPrioData` Gets the record data and field metadata required to prioritize records. This value is available in
API version 62.0 and later.


Metadata Types Flow

These values are reserved for future use.

**•** `exportSurveyResponses`

**•** `extractDataFromDocument`

**•** `metricRefresh`

**•** `thanks`

For values used in other products or features, see:

**•** [Flow for Asset Lifecycle](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/asset_lifecycle_flow_metadata_api.htm)

**•** [Flow for B2B Referral Management](https://developer.salesforce.com/docs/atlas.en-us.260.0.referral_marketing.meta/referral_marketing/b2b_referral_management_flow_metadata_api.htm)

**•** [Flow for Billing](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/billing_flow_metadata_api.htm)

**•** [Flow for Business Rules Engine](https://developer.salesforce.com/docs/atlas.en-us.260.0.industries_reference.meta/industries_reference/bre_flow_metadata_api.htm)

**•** [Flow for Context Service](https://developer.salesforce.com/docs/atlas.en-us.260.0.industries_reference.meta/industries_reference/context_service_flow_metadata_api.htm)

**•** [Flow for Digital Lending.](https://developer.salesforce.com/docs/atlas.en-us.260.0.industries_reference.meta/industries_reference/digital_lending_flow_metadata_api.htm)

**•** [Flow for Dynamic Revenue Orchestrator](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/dynamic_revenue_orchestrator_flow_metadata_api.htm)

**•** [Flow for Financial Services Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.financial_services_cloud_object_reference.meta/financial_services_cloud_object_reference/fsc_meta_visual_workforce.htm)

**•** [Flow for Fundraising](https://developer.salesforce.com/docs/atlas.en-us.260.0.nonprofit_cloud.meta/nonprofit_cloud/fundraising_flow_metadata_api.htm)

**•** [Flow for Health Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.health_cloud_object_reference.meta/health_cloud_object_reference/health_cloud_flow_metadata_api.htm)

**•** [Flow for Insurance Brokerage](https://developer.salesforce.com/docs/atlas.en-us.260.0.insurance_developer_guide.meta/insurance_developer_guide/insurance_brokerage_flow_metadata_api.htm)

**•** [Flow for Insurance Claims](https://developer.salesforce.com/docs/atlas.en-us.260.0.insurance_developer_guide.meta/insurance_developer_guide/insurance_claim_flow_metadata_api.htm)

**•** [Flow for Insurance Group Benefits](https://developer.salesforce.com/docs/atlas.en-us.260.0.insurance_developer_guide.meta/insurance_developer_guide/insurance_group_benefits_flow_metadata_api.htm)

**•** [Flow for Insurance Policy Administration](https://developer.salesforce.com/docs/atlas.en-us.260.0.insurance_developer_guide.meta/insurance_developer_guide/insurance_policy_administration_flow_metadata_api.htm)

**•** [Flow for Insurance Quoting](https://developer.salesforce.com/docs/atlas.en-us.260.0.insurance_developer_guide.meta/insurance_developer_guide/insurance_quoting_flow_metadata_api.htm)

**•** [Flow for Intelligent Document Reader](https://developer.salesforce.com/docs/atlas.en-us.260.0.industries_reference.meta/industries_reference/intelligent_document_reader_standard_actions_parent.htm)

**•** [Flow for Intelligent Form Reader](https://developer.salesforce.com/docs/atlas.en-us.260.0.industries_reference.meta/industries_reference/form_reader_standard_actions_parent.htm)

**•** [Flow for Life Sciences Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.life_sciences_dev_guide.meta/life_sciences_dev_guide/life_sciences_flow_metadata_api.htm)

**•** [Flow for Loyalty Management](https://developer.salesforce.com/docs/atlas.en-us.260.0.loyalty.meta/loyalty/loyalty_management_flow_metadata_api.htm)

**•** [Flow for Manufacturing Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.mfg_api_devguide.meta/mfg_api_devguide/mfg_flow_metadata_api.htm)

**•** [Flow for Net Zero Cloud](https://developer.salesforce.com/docs/atlas.en-us.260.0.netzero_cloud_dev_guide.meta/netzero_cloud_dev_guide/net_zero_cloud_invocable_actions_parent.htm)

**•** [Flow for Omnistudio](https://developer.salesforce.com/docs/atlas.en-us.260.0.industries_reference.meta/industries_reference/omnistudio_flow_metadata_api.htm)

**•** [Flow for Process Compliance Navigator](https://developer.salesforce.com/docs/atlas.en-us.260.0.industries_reference.meta/industries_reference/process_compliance_navigator_flow_metadata_api.htm)

**•** [Flow for Product Configurator](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/product_configurator_flow_metadata_api.htm)

**•** [Flow for Product Discovery](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/product_discovery_flow_metadata_api.htm)

**•** [Flow for Quote and Order Capture](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/qoc_flow_metadata_api.htm)

**•** [Flow for Rate Management](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/rate_management_flow_metadata_api.htm)

**•** [Flow for Referral Marketing](https://developer.salesforce.com/docs/atlas.en-us.260.0.referral_marketing.meta/referral_marketing/referral_flow_metadata_api.htm)

**•** [Flow for Salesforce Pricing](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/pricing_flow_metadata_api.htm)

**•** [Flow for Usage Management](https://developer.salesforce.com/docs/atlas.en-us.260.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/usage_management_flow_metadata_api.htm)


Metadata Types Flow

FlowActionCallInputParameter

Defines an input parameter from the flow to the action. It extends FlowBaseElement and inherits all its fields. This metadata type is
available in API version 31.0 and later.

**Field Name** **Field Type** **Description**

`name` string Required. Unique name for the input parameter.

`value` FlowElementReferenceOrValue Defines the value of the input parameter.

FlowActionCallOutputParameter

Defines an output parameter from the action to the flow. It extends FlowBaseElement and inherits all its fields. This metadata type is
available in API version 31.0 and later.

**Field Name** **Field Type** **Description**

`assignToReference` string Required. Specifies the variable to which you want to assign the
output parameter value.

`name` string Required. Unique name for the output parameter.

FlowActionCallPath

A path determines which node of the flow is executed after the Einstein Decision element. A path defines and links to the subsequent
node. It extends FlowBaseElement and inherits all its fields. This metadata type is available in API version 63.0 and later.

**Field Name** **Field Type** **Description**

`connector` FlowConnector Required. Which node to execute after completing the current
node.

`pathName` string Required. Unique name for the path.

FlowApexPluginCall

Defines a call to an Apex plug-in from the flow. It extends FlowNode and inherits all its fields.

**Field Name** **Field Type** **Description**

`apexClass` string Required. The name of the Apex class.

`connector` FlowConnector Specifies which node to execute after this Apex plug-in call.

`faultConnector` FlowConnector Specifies which node to execute if the Apex plug-in call
results in an error.

`inputParameters` FlowApexPluginCallInputParameter[] An array of input parameters from the flow to the Apex
plug-in.


Metadata Types Flow

**Field Name** **Field Type** **Description**

`outputParameters` FlowApexPluginCallOutputParameter[] An array of output parameters from the Apex plug-in to the
flow.

FlowApexPluginCallInputParameter

Defines an input parameter from the flow to the Apex plug-in. It extends FlowBaseElement and inherits all its fields.

**Field Name** **Field Type** **Description**

`name` string Required. Unique name for the input parameter.

`value` FlowElementReferenceOrValue Defines the value of the input parameter.

FlowApexPluginCallOutputParameter

Defines an output parameter from the Apex plug-in to the flow. It extends FlowBaseElement and inherits all its fields.

**Field Name** **Field Type** **Description**

`assignToReference` string Required. Specifies the variable to which you want to assign the
output parameter value.

`name` string Required. Unique name for the output parameter.

FlowAssignment

Defines an assignment node that can dynamically change the value of a variable in the flow. It extends FlowNode and inherits all of its
fields.

**Field Name** **Field Type** **Description**

`assignmentItems` FlowAssignmentItem[] An array of assignment operations that’s executed in the given
order, starting from the index 0.

`connector` FlowConnector Specifies which node to execute after this assignment node.

FlowAssignmentItem

Defines an operation to apply to a variable. It extends FlowBaseElement and inherits all its fields.

**Field Name** **Field Type** **Description**

`assignToReference` string Reference to the variable to which you want to apply the
specified operator.


Metadata Types Flow

**Field Name** **Field Type** **Description**

`operator` FlowAssignmentOperator
(enumeration of type string)

`value` FlowElementReferenceOrValue

FlowAssignmentOperator

Operation to apply to the variable reference in the
`assignToReference` field. For valid values, see
FlowAssignmentOperator.

Defines the value that you want the operator to apply to
the variable reference in the `assignToReference`
field.

An enumeration of type string that specifies the operation to apply to the variable in the `assignToReference` [field. See “Flow](https://help.salesforce.com/articleView?id=flow_ref_operators_assignment.htm&language=en_US)
[Operators in Assignment Elements” in Salesforce Help.](https://help.salesforce.com/articleView?id=flow_ref_operators_assignment.htm&language=en_US)

These values are valid.

**Enumeration Value** **Description**

```
Add

```

When the `assignToReference` field is a variable of type number or currency, this operator
adds the `value` to the variable.

When the `assignToReference` field is a variable of type date, this operator adds the
`value` in days to the variable.

When the `assignToReference` field is a variable of type string, this operator appends
the `value` to the end of the string.

When the `assignToReference` field is a variable of type picklist, this operator appends
the `value` to the end of the last item in the picklist.

When the `assignToReference` field is a variable of type multipicklist, this operator
appends the `value` to the end of the last item in the multi-select picklist. To instead add an
item to the end of the multi-select picklist, use the `AddItem` operator.

When the `assignToReference` field is the `$Flow.ActiveStages` global variable,
this operator appends the `value` as a new item at the end of `$Flow.ActiveStages` .

When the `assignToReference` field is a collection variable, this operator appends the
`value` to the end of the collection. Support for a collection variable as the `value` is available
in API version 43.0 and later, but only via Metadata API. From Flow Builder, you can’t save an
Assignment element that contains a collection variable in the Value column for the `Add`
operator.

The `Add` operator isn’t supported when the `assignToReference` field is a variable of
type boolean, dateTime, or sObject.

`AddAtStart` Supported only when the `assignToReference` field is a collection variable or the
`$Flow.ActiveStages` global variable. Adds the `value` as a new item at the beginning

of the collection. When the `value` is a collection variable, the operator adds all items at the
beginning of the collection. This operator is available in API version 43.0 and later.

```
AddItem

```

Supported only when the `assignToReference` field is a variable of type multipicklist.
Adds the `value` to the picklist, including the semicolon that’s required to mark a `value` as
a separate item. This operator is available in API version 34.0 and later.


Metadata Types Flow

**Enumeration Value** **Description**

`Assign` Assigns the `value` to the variable in the `assignToReference` field.

`AssignCount` Supported only when the `value` is a collection variable or the `$Flow.ActiveStages`
global variable. Counts the number of stages or items in the collection, and assigns that number

to the variable in the `assignToReference` field. Corresponds to `equals count` in
the user interface. This operator is available in API version 43.0 and later.

`RemoveAfterFirst` Supported only when the `assignToReference` field is a collection variable or the
`$Flow.ActiveStages` global variable. Finds the first instance of the `value` within the

variable in the `assignToReference` field. Removes everything after that first instance
from the variable. This operator is available in API version 43.0 and later.

`RemoveAll` Supported only when the `assignToReference` field is a collection variable or the
`$Flow.ActiveStages` global variable. Removes all instances of the `value` from the

variable in the `assignToReference` field. When the `value` is a collection variable, the
operator removes all instances of each item from the variable in the `assignToReference`
field. This operator is available in API version 43.0 and later.

`RemoveBeforeFirst` Supported only when the `assignToReference` field is a collection variable or the
`$Flow.ActiveStages` global variable. Finds the first instance of the `value` within the

variable in the `assignToReference` field. Removes everything before that first instance
from the variable. This operator is available in API version 43.0 and later.

`RemoveFirst` Supported only when the `assignToReference` field is a collection variable or the
`$Flow.ActiveStages` global variable. Removes the first instance of the `value` from

the variable in the `assignToReference` field. This operator is available in API version 43.0
and later.

`RemovePosition` Supported only when the `assignToReference` field is a collection variable or the
`$Flow.ActiveStages` global variable. Removes the item at the specified position. For

example, if the collection contains three items, such as Red, Green, and Blue, and the `value`
is 2, the second item, Green, is removed from the collection variable. This operator is available
in API version 43.0 and later.

Make sure that the `value` at run time is a positive integer within the range of the number of
items in the collection variable.

```
RemoveUncommon

Subtract

```

Supported only when `assignToReference` and `value` are both collection variables.
Keeps items that are in both collections and removes the rest from the collection variable in
the `assignToReference` field. This operator is available in API version 43.0 and later.

Supported only when the `assignToReference` field is a variable of type currency, date,
or number.

When the `assignToReference` field is a variable of type number or currency, this operator
subtracts the `value` from the variable.

When the `assignToReference` field is a variable of type date, this operator subtracts the
`value` in days from the variable.


Metadata Types Flow

FlowBaseElement

Base class for all flow elements that require contextual information in metadata values. This class is an abstract class. FlowBaseElement
is available in API version 32.0 and later.

**Field Name** **Field Type** **Description**

`processMetadataValues` FlowMetadataValue[] Contextual information for the element.

FlowChoice

A choice resource is a standalone choice option that you can reference or reuse throughout the flow. It extends FlowElement and inherits
[all of its fields. See Salesforce Help: Flow Resource: Choice.](https://help.salesforce.com/s/articleView?id=platform.flow_ref_resources_choice.htm&language=en_US)

**Field Name** **Field Type** **Description**

`choiceIcon` FlowIcon The icon to display for the choice in the screen. This field is
available in API version 64.0 and later.

`choiceText` string Required. Choice label to display in the screen.

`dataType` FlowDataType (enumeration of type Required. Valid types are:
string)

**•** `Currency`

**•** `Date`

**•** `Number`

**•** `String`

**•** `Boolean`

**•** `Time`

`userInput` FlowChoiceUserInput Enables the choice to allow user input when the choice is
selected. Not supported for choices in multi-select fields.

`value` FlowElementReferenceOrValue

FlowChoiceUserInput

Actual value that’s used during flow execution, for example,
in assignments, calls to Apex plug-ins, and record elements. If
null, this choice always has the value of null.

Allows the choice to include a user input field that appears when the user selects a choice. User input isn’t supported for choices in
multi-select fields. It extends FlowBaseElement and inherits all its fields.

**Field Name** **Field Type** **Description**

`isRequired` boolean Indicates whether users are required to enter something into the
field when they select the choice.

`promptText` string Text that’s displayed to prompt the user for input at runtime.
Supports merge fields.


Metadata Types Flow

**Field Name** **Field Type** **Description**

`validationRule` FlowInputValidationRule A rule used at runtime to validate the user input.

FlowCollectionProcessor

Defines a node that processes the contents of a collection, depending on the `collectionProcessorType` . FlowCollectionProcessor
is available in API version 50.0 and later. FlowCollectionProcessor extends FlowNode and inherits all its fields.

**Field Name** **Field Type** **Description**

`assignNextValueToReference` string The name of the variable that’s assigned to the next value of
the collection.

`collectionProcessorType` FlowCollectionProcessorType The type of the collection processor. Valid values are:

**•** `SortCollectionProcessor` —This value is
available in API version 50.0 and later.

**•** `RecommendationMapCollectionProcessor`                              This value is available in API version 53.0 and later.

**•** `FilterCollectionProcessor`                              - This value is
available in API version 53.0 and later.

`collectionReference` string The collection being sorted, filtered, or assigned to
recommendations.

`conditionLogic` string Defines how the filtering conditions are evaluated. Valid values
are:

**•** `And`

**•** `Or`

**•** `Custom logic, such as (1 AND (2 OR`

```
                                3))

```

**•** `Formula`

`conditions` FlowCondition[] An array of conditions for the input collection.

`connector` FlowConnector Specifies which node to execute after processing the collection.

`formula` string

`limit` int

The formula expression that filters the input collection. If the
formula evaluates to `true`, the record is added to the output
collection.

The maximum number of records to include in the generated
collection. There’s no default value. All items of the collection
are kept if it’s greater than the size of the collection.

If sortField and sortOrder are also specified, the records are
sorted before the limit takes effect.

This field is available in API version 51.0 and later.

This field is nillable in API version 51.0 and later.


Metadata Types Flow

**Field Name** **Field Type** **Description**

`mapItems` FlowCollectionMapItem[] The rules to map each field of the collection variable.

`outputSObjectType` string The sObject type of the output collection.

`sortOptions` FlowCollectionSortOption[] An array of options to sort the items in the collection. This field
is available in API version 51.0 and later.

FlowCollectionSortOption

Sets the sorting field, sort order, and placement of empty or null values in the sorted collection. This metadata type is available in API
version 51.0 and later.

**Field Name** **Field Type** **Description**

`doesPutEmptyStringAndNullFirst` boolean Place empty or null values first in the sorted list by setting this
value to `true` . The default value is `false` .

`sortField` string

Determines the sorting of records that meet the filter criteria.
Required for record collections and collections of Apex-defined
variables.

If the collection is a primitive data type, such as a list of string
or integer values, `sortField` isn’t supported.

`sortOrder` SortOrder (enumeration of type string) The order that the collection is sorted in. Valid values are:

**•** `Asc` —Ascending

**•** `Desc` —Descending

FlowCustomError

Defines a custom error element to roll back a change that triggered a flow and inform the user exactly what caused the error. It extends
FlowNode and inherits all its fields.

**Field Name** **Field Type** **Description**

`description` string Describes the error message.

`connector` FlowConnector Required. Which node to execute after completing the
current node.

`customErrorMessages` FlowCustomErrorMessage[] An array of custom error messages.

FlowCustomErrorMessage

Defines a custom error message for a custom error element. It extends FlowBaseElement and inherits all its fields.


Metadata Types Flow

**Field Name** **Field Type** **Description**

`errorMessage` string Required. Specifies the custom error message.

`fieldSelection` string References the erroneous field that’s associated with the
custom error message.

`isFieldError` boolean Required. When this field is set to `true`, indicates that the
custom error message displays inline on a field. When it is

set to `false`, it displays in a window on a record page. The
default value is `false` .

FlowCondition

Defines a condition for a rule. It extends FlowBaseElement and inherits all its fields.

**Field Name** **Field Type** **Description**

`aggregationOperator` string Operation to apply to the variable reference in the
`assignToReference` field. The valid value is:

**•** `Count`

`conditionLogic` string Specifies logic for the conditions. Value can be:

**•** `and` —Evaluates to `true` only if all its conditions
evaluate to true

**•** `or` —Evaluates to `true` if any of its conditions evaluate
to true

`conditionType` FlowWaitConditionType (enumeration The type of condition that a requirement in an automation
of type string) is used for. Valid values are:

**•** Container

**•** EntryCondition

**•** ExitCondition

`conditions` FlowCondition[] An array of conditions that must be `true` for the flow to
execute the rule.

`leftValueReference` string Required. Unique name of the element that serves as the
left side of the condition expression.

`operator` FlowComparisonOperator Required. Comparison operators in conditions for flow
(enumeration of type string) elements and resources. Valid values are:

**•** `Contains`

**•** `EndsWith`

**•** `EqualTo`

**•** `GreaterThan`

**•** `GreaterThanOrEqualTo`


Metadata Types Flow

**Field Name** **Field Type** **Description**

**•** `HasError` —This value is available in API version 64.0
and later.

**•** `In`                              - This value is available in API version 56.0 and later.

**•** `IsBlank` —A text value with zero characters or with
only whitespace. Use to determine whether a text field
or variable is blank. For other data type values, use to
determine whether a field or variable is null. This value
is available in API version 61.0 and later.

**•** `IsChanged—` This value is available in API version 52.0
and later.

**•** `IsEmpty` —An empty collection. This value is available
in API version 61.0 and later.

**•** `IsNull` —A value that is either not set or references
no value. Use to determine whether a field or variable
value is set to no value.

**•** `LessThan`

**•** `LessThanOrEqualTo`

**•** `None`                              - Save a flow with an incomplete condition, so
you can finish building the flow later. This value is
available in API version 58.0 and later.

**•** `NotEqualTo`

**•** `NotIn`                              - This value is available in API version 56.0 and
later.

**•** `StartsWith`

**•** `WasSelected`                              - Requires a choice on the left side.

**•** `WasSet`                              - This value is available in API version 30.0
and later.

**•** `WasVisited`                              - Requires a node on the left side.

[See Flow Operators.](https://help.salesforce.com/s/articleView?id=platform.flow_ref_operators.htm&language=en_US)

`rightValue` FlowElementReferenceOrValue Unique name of an element or the actual value, such as text
or a number, for the right side of the condition expression.

FlowCustomProperty

Defines the name and value of a custom property in a flow. This metadata type is available in API version 63.0 and later.

**Field Name** **Field Type** **Description**

`name` string Required. Unique name for the custom property associated with
the flow.


Metadata Types Flow

**Field Name** **Field Type** **Description**

`value` FlowElementReferenceOrValue

FlowConnector

Defines the value of the custom property associated with the flow.
When the FlowCustomProperty’s name is set to
`ScreenProgressIndicator`, valid values are:

**•** `“Location":"Top","Type":"Simple”`

**•** `"Location":"Footer","Type":"Simple"`

**•** `"Location":"Top","Type":"Path”`

Connectors determine the order in which the nodes of the flow are executed. A connector defines and links to the subsequent node. It
extends FlowBaseElement and inherits all its fields.

**Field Name** **Field Type** **Description**

`isGoTo` boolean

Make the connector a Go To Connector by setting this value to
`true` . The default value is `false` . This value is available in API
[version 53.0 and later. See Flow Connectors.](https://help.salesforce.com/s/articleView?id=platform.flow_ref_connectors.htm&type=5&language=en_US)

`targetReference` string Required. Which node to execute after completing the current
node.

FlowCollectionMapItem

Defines the rule to assign a value to the field reference. This metadata type is available in API version 51.0 and later.

**Field Name** **Field Type** **Description**

`assignToFieldReference` string Required. Specifies the reference to the field to which the
specified operator is applied.

`operator` FlowAssignmentOperator (enumeration Required. Applies to the variable reference in the
of type string) `assignToFieldReference` field.

`value` FlowElementReferenceOrValue

FlowDataTypeMapping

Required. Defines the value that the operator applies to the
variable reference in the `assignToFieldReference`
field.

This data type mapping defines the specific sObject data type for input and out values that have the generic sObject data type. It extends
FlowBaseElement and inherits all its fields. This metadata type is available in API version 48.0 and later.

**Field Name** **Field Type** **Description**

`apexClass` string The name of the Apex class. This field is
available in API version 61.0 and later.


Metadata Types Flow

**Field Name** **Field Type** **Description**

`typeName` string Required. API name of the input or output
variable. The `T__` prefix is required for

input variables. The `U__` prefix is required
for output variables. For example,
`T__inputCollection` represents the
API name of the input variable
`inputCollection` .

`typeValue` string

FlowConstant

API name of the specific sObject data type
that this value maps to. For example,
`Account` .

A constant resource defines a fixed value that can be used throughout your flow. It extends FlowElement and inherits all its fields.

**Field Name** **Field Type** **Description**

`dataType` FlowDataType (enumeration of type Required. Valid types are:
string)

**•** `Currency`

**•** `Date`

**•** `Number`

**•** `String`

**•** `Boolean`

**•** `Time`

`value` FlowElementReferenceOrValue

FlowDecision

Default value of the constant. This field can’t have merge fields, nor
can it reference another resource besides
`$GlobalConstant.EmptyString` .

A node that evaluates a set of rules and routes the flow execution based on the first rule that evaluates to true. It extends FlowNode and
inherits all its fields.

**Field Name** **Field Type** **Description**

`attributes` FlowAttribute[] An array of attributes for the decision. This field is available in API
version 65.0 and later.

`defaultConnector` FlowConnector Specifies which node to execute if none of the rules evaluate to
true.

`defaultConnectorLabel` string Label for the default connector.


Metadata Types Flow

**Field Name** **Field Type** **Description**

`rules` FlowRule[] An array of rules for the decision. The rules are evaluated in the
order that they’re listed, and the connector of the first true rule is

used. If no rules are true, then the default connector is used. In Flow
Builder, rules are referred to as decision outcomes.

FlowAttribute

Defines an attribute that's shared across multiple Flow metadata subtypes. Available in API version 65.0 and later.

**Field Name** **Field Type** **Description**

`value` string The value of the flow attribute.

`type` FlowAttributeType Specifies the type of the flow attribute value. Valid values are:
(enumeration of type string)

**•** LlmDescription

**•** LlmPrompt

FlowDynamicChoiceSet

Retrieves data or metadata from an object and dynamically generates a set of choices at run time. It extends FlowElement and inherits
all its fields. Depending on the fields that are set, this element represents a record choice or a picklist choice.

**•** A _record choice_ dynamically generates choices based on records that meet specified filter criteria. If a dynamic choice doesn’t have
the `picklistField` and `picklistObject` parameters set, it’s a record choice and it can’t have a data type of `Picklist`
or `Multipicklist` .

**•** A _picklist choice_ dynamically generates choices based on the available values for a picklist or multi-select picklist field. If a dynamic
choice has the `picklistField` and `picklistObject` parameters set, it’s a picklist choice and it must have a data type of
`Picklist` or `Multipicklist` .

**Field Name** **Field Type** **Description**

`collectionReference` string The collection that’s used to generate choices. This field is
available in API version 54.0 and later.

`dataType` FlowDataType (enumeration of type Required. Valid types are:
string)

**•** `Boolean`

**•** `Currency`

**•** `Date`

**•** `Multipicklist` —Picklist choices only

**•** `Number`

**•** `Picklist` —Picklist choices only

**•** `Record`

**•** `String`

**•** `Time`


Metadata Types Flow

**Field Name** **Field Type** **Description**

`Picklist` and `Multipicklist` are available in API
version 35.0 and later. `Record` is available in API version
54.0 and later.

`displayField` string

`filters` FlowRecordFilter[]

`limit` int

Required for record choices. Specifies the object field. The
values of the object field are displayed to the user as choice
labels for selecting a record.

For example, for an account, if you want the dynamically
generated choices to be displayed as the account names

from the records that are retrieved from the database, specify
`Name` in `displayField` .

Not supported for picklist choices. Picklist choices always
display the labels for the retrieved picklist values.

An array of filters to apply to the records retrieved from the
database. For example, filter accounts to include only the
accounts that were created in the past three months.

Not supported for picklist choices.

Maximum number of choices to include in the generated
set of choices. Maximum and default: 200.

If `sortField` and `sortOrder` are also specified, the
records are sorted before the `limit` takes effect.

This field is available in API version 25.0 and later.

This field is nillable in API version 45.0 and later.

`object` string Required for record choices. The object whose fields you
want to retrieve from the database and use to generate the

set of choices. For example, use “Account” to dynamically
generate choices from the information in account records
in the database.

Not supported for picklist choices.

`outputAssignments` FlowOutputFieldAssignment[] An array that assigns fields from the user-selected record to
variables that can be used elsewhere in the flow. For

example, when the user selects an account name from the
dynamically generated list of choice options,
outputAssignments can assign the ID and AnnualRevenue
from the user-selected account to variables that you specify.

Not supported for picklist choices.

`picklistField` string Required for picklist choices. The field whose available values
you want to retrieve from the database and use to generate

the picklist choice. For example, use “Industry” to dynamically


Metadata Types Flow

**Field Name** **Field Type** **Description**

generate one choice for each available value on the Industry
picklist field.

Not supported for record choices.

This field is available in API version 35.0 and later.

`picklistObject` string Required for picklist choices. The object whose field
metadata you want to retrieve from the database and use

to generate the picklist choice. For example, use “Account”
to dynamically generate choices from a picklist field on the
Account object.

Not supported for record choices.

This field is available in API version 35.0 and later.

`sortField` string

`sortOrder` SortOrder (enumeration of type string)

Field that’s used for sorting records that meet the filter
criteria. If this field isn’t specified, the returned records aren’t
sorted.

You can only sort records by fields that have the `Sort` API
[field property, as specified in SOAP API.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/)

Not supported for picklist choices.

This field is available in API version 25.0 and later.

Order in which to sort the records. If this field isn’t specified,
then the results aren’t sorted.

Valid values are:

**•** `Asc` —Ascending

**•** `Desc` —Descending

Not supported for picklist choices.

This field is available in API version 25.0 and later.

`valueField` string Stored value for the choice, which can differ from what is
displayed to the user as the choice options

( `displayField` ). For example, the `displayField`
could be the account “Name” while the valueField is the
account “Id.”

Not supported for picklist choices. Picklist choices always
store the API value for the retrieved picklist values.

FlowElement

Base class for all flow elements. This class is an abstract class. It extends FlowBaseElement and inherits all its fields.


Metadata Types Flow

**Field Name** **Field Type** **Description**

`description` string Description of the flow element.

`name` string Unique name of the flow element.

FlowElementReferenceOrValue

Defines a reference to an existing element or a particular value that you specify. Make sure that you specify only _one_ of the fields.

**Field Name** **Field Type** **Description**

`apexValue` string Use this field to specify a JSON response value of an Apex-defined record. Use
this field only for `FlowScreenFieldInputParameter` and

`FlowActionCallInputParameter` . If you want to specify a different
data type or element reference, don’t use this field.

`booleanValue` boolean Use this field to specify a boolean value. If you want to specify a different data
type or element reference, don’t use this field.

`complexValue` string

When `complexValueType` is specified, use this field to specify flow
resources and fields in the data structure. Use these fields to describe the data
structure:

**•** `fieldReference` —The list of field API names.

**•** `objectType` —The object type, sObject or Apex.

**•** `type` —The API name of the sObject or Apex class.

**•** `elementReference` —The API name of the flow resource that contains
the list of fields specified in `fieldReference` .

This field is available in API version 63.0 and later.

```
complexValueType

```

FlowComplexValueType Use this field to specify the type of data structure to reference. Valid values are:
(enumeration of

**•** `ComplexObjectFieldDetails` —Use when referencing a field and

type string)

need the label and type in addition to the API name.

`dateTimeValue` dateTime

**•** `JoinDefinition` —When `InnerJoin` is specified in
`transformType`, indicates flow resources for source and target
collections, join keys, selected fields to join. and field mappings in a join
transformation. `JoinDefinition` isn't a valid value for
FlowInlineTransform.

**•** `FieldReference` —Use this field to define the flow resource and its
fields referenced in the flow.

This field is available in API version 63.0 and later. Use `complexValue` to
specify the data structure.

Use this field to specify a dateTime value. If you want to specify a different data
type or element reference, don’t use this field. This field is available in API version
30.0 and later.

`dateValue` date Use this field to specify a date value. If you want to specify a different data type
or element reference, don’t use this field.


Metadata Types Flow

**Field Name** **Field Type** **Description**

`elementReference` string Use this field to specify the name of an existing flow resource. If you want to
specify a value instead of an element reference, don’t use this field.

```
formulaDataType

```

FlowDataType Use this field to specify the formula result’s data type of the transformed data.
(enumeration of Corresponds to the target data field in Flow Builder. This field requires the
type string) `formulaExpression` field. This field is available in API version 59.0 and

later. See FlowTransform

Valid values are:

**•** `Apex`

**•** `Boolean`

**•** `Currency`

**•** `Date`

**•** `DateTime`

**•** `Number`

**•** `String`

**•** `sObject` —This value corresponds to a record variable.

**•** `Time`

`formulaExpression` string Use this field to specify the formula expression that transforms the data in the
flow. In Flow Builder, it corresponds to the target data field in the Transform

element. This field requires the `formulaDataType` field. This field is available
in API version 59.0 and later. See FlowTransform.

`numberValue` double Use this field to specify a double value. If you want to specify a different data
type or element reference, don’t use this field.

`setupReference` string Use this field to specify the name of an existing setup reference. Required for
Omni-Channel elements. If you want to specify a value instead of a setup

reference, don’t use this field. Required when `setupReferenceType` is
specified.

`setupReferenceType` string Use this field to specify the type of setup reference. Required when
setupReference is specified.

`sobjectValue` string Use this field to specify a JSON response value of an sObject record. Use this
field only for `FlowScreenFieldInputParameter` and

`FlowActionCallInputParameter` . If you want to specify a different
data type or element reference, don’t use this field.

`stringValue` string

Use this field to specify a string value. If you want to specify a different data type
or element reference, don’t use this field.

When the FlowMetadataValue's `name` field is set to
`SendNoApproverEmails`, valid values are `true` or `false` and are
case-insensitive.


Metadata Types Flow

**Field Name** **Field Type** **Description**

When the FlowMetadataValue's `name` field is set to `BuilderType` or
`OriginalBuilderType`, the valid value is `LightningFlowBuilder` .
The value is reserved for internal use.

`transform` FlowInlineTransform Use this field to specify a value for an inline data transformation. This field is
available in API version 62.0 and later.

`transformValueReference` string Reserved for future use.

FlowExitRule

Defines the conditions and logic that enables an exit rule to evaluate to true. It extends FlowElement and inherits all of its fields. This
metadata type is available in API version 62.0 and later.

**Field Name** **Field Type** **Description**

`conditions` FlowCondition[] An array of conditions for the exit rule.

`label` string
Required. Label for the exit rule.

`logicalOperator` string Required. Logical operator in conditions for the exit rule. Valid values
are:

**•** `and` —Evaluates to `true` only if all its conditions evaluate to
true

**•** `or` —Evaluates to `true` if any of its conditions evaluate to
true

`ruleOrder` int Indicates how the exit rule is ordered against other exit rules. The
`ruleOrder` value must be unique within the flow.

FlowExperiment

A node that routes the flow execution based on a specified experiment distribution percentage. It extends FlowNode and inherits all its
fields. This metadata type is available in API version 61.0 and later.

**Field Name** **Field Type** **Description**

`duration` int The amount of time that the experiment runs. This field is available
in API version 64.0 and later.

`durationUnit` string The unit of measurement for experiment duration. Valid values are:

**•** Minutes

**•** Hours

**•** Days

**•** Weeks


Metadata Types Flow

**Field Name** **Field Type** **Description**

**•** Months

This field is available in API version 64.0 and later.

`paths` FlowExperimentPath[] An array of flow experiment paths.

`testGroupPercentage` int

Specifies the distribution percentage of the test group. A valid
number in the range 0-99. This field is available in API version 64.0
and later.

`type` FlowExperimentType Required. The type of experiment. Valid value is:

**•** Random

FlowExperimentPath

Defines an experiment path. It extends FlowElement and inherits all its fields. This metadata type is available in API version 61.0 and later.

**Field Name** **Field Type** **Description**

`connector` FlowConnector Specifies which node to execute after this experiment path.

`label` string Required. Label for the path.

`percentage` int Required. The distribution percentage for this path.

FlowFormula

Calculates a value using functions and elements in the flow. It extends FlowElement and inherits all its fields.

**Field Name** **Field Type** **Description**

`dataType` FlowDataType (enumeration The data type for the formula. Valid values are:
of type string)

**•** `Boolean`

**•** `Currency`

**•** `Date`

**•** `DateTime`

**•** `Number`

**•** `String`

**•** `Time`

`dataType` defaults to `Number` if it isn’t defined in a formula.

This field is available in API version 31.0 and later.

`expression` string

Required. Salesforce formula expression. The return value must
match the data type. For API version 30.0 and earlier, the return
value must be numeric.


Metadata Types Flow

**Field Name** **Field Type** **Description**

`scale` int Scale of the return value, specifically, the number of digits to the
right of the decimal point. Available only when the data type is

Number or Currency. Corresponds to the Decimal Places field in
Flow Builder.

FlowIcon

Allows a resource to include an icon. This metadata type is available in API version 64.0 and later.

**Field Name** **Field Type** **Description**

`iconName` String The name of the selected Salesforce Lightning Design System icon.
This field is available in API version 64.0 and later.

FlowInlineTransform

Specifies how to transform source data to target data in an Action element within a flow. This metadata type is available in API version
62.0 and later.

**Field Name** **Field Type** **Description**

`apexClass` string The Apex class of the target data after transformation if its data type
is `Apex` .

`dataType` FlowDataType (enumeration Required. Specifies the data type of the transformed data. In Flow
of type string) Builder, it corresponds to the target data. Valid types are:

**•** `Apex`

**•** `Boolean`

**•** `Currency`

**•** `Date`

**•** `DateTime`

**•** `Multipicklist`

**•** `Number`

**•** `Picklist`

**•** `sObject` —This value corresponds to a record variable.

**•** `String`

**•** `Time`

`isCollection` boolean Indicates whether the variable is a collection of values. The default
value is `false` .

`transformValues` FlowTransformValue[] An array of values for data transformation.


Metadata Types Flow

FlowInputFieldAssignment

Assigns the value for a record field based on a resource or static value. It extends FlowBaseElement and inherits all its fields.

**Field Name** **Field Type** **Description**

`field` string Required. The name of the field to assign a value to when a record
is created or updated.

`value` FlowElementReferenceOrValue The value to assign to the field.

FlowInputValidationRule

Validation rules verify that the data entered by the user meets the specified requirements. If the validation rule evaluates to false, then
the specified error message is displayed.

**Field Name** **Field Type** **Description**

`errorMessage` string Required. The error message to display when
`formulaExpression` is `false` .

`formulaExpression` string Required. A formula that’s used to validate the user input.

FlowLoop

A construct for iterating through a collection. It extends FlowNode and inherits all its fields. FlowLoop is available in API version 30.0 and
later.

**Field Name** **Field Type** **Description**

`assignNextValueToReference` string The variable that’s assigned to the current value in the collection before navigating
to the target of `nextValueConnector` .

`collectionReference` string The collection being looped through.

```
iterationOrder

```

iterationOrder Valid values are:
(enumeration of

**•** `Asc` —Iterate through the collection in the order the values are listed (first

type string)

to last).

**•** `Desc` —Iterate through the collection in the reverse order the values are
listed (last to first).

`nextValueConnector` FlowConnector A reference to the next element in the collection.

`noMoreValuesConnector` FlowConnector The element to navigate to when all entries in the collection have been iterated
through.


Metadata Types Flow

FlowMetadataValue

Defines contextual information that can be passed between elements in a flow. Flow metadata values can be used in an application
that produces or consumes flows. FlowMetadataValue is available in API version 31.0 and later.

**Field Name** **Field Type** **Description**

`name` string

Required. Name for the metadata value. This name doesn’t need
to be unique across all elements.

To specify that a flow approval process send no email notifications
to approvers, use SendNoApproverEmails .

`value` FlowElementReferenceOrValue Reference or value for the metadata value.

FlowNode

A node is a type of element that’s visible in the flow diagram. It extends FlowElement and inherits all its fields.

**Field Name** **Field Type** **Description**

```
elementSubtype

```

FlowElementSubtype Reserved for internal use.
(enumeration of
type string)

`label` string Name of the node. This non-unique label is different from the unique name of
the node, which is inherited from FlowElement.

`locationX` int Required. Horizontal location of the node, in pixels from the left. In API version
64.0 and later, if a flow is saved in auto-layout, this field is set to 0.

`locationY` int Required. Vertical location of the node, in pixels from the top. In API version 64.0
and later, if a flow is saved in auto-layout, this field is set to 0.

FlowOrchestratedStage

[A stage node that contains steps in an orchestration. It extends FlowNode and inherits all its fields. This metadata type is available in API](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_visual_workflow.htm#FlowNode)
version 53.0 and later.

**Field Name** **Field Type** **Description**

`connector` FlowConnector Specifies which node to execute after this stage.

`exitActionInputParameters` FlowStageStepExitActionInputParameter[]

An array of input parameters from the stage to the
evaluation flow. These parameters specify an exit
condition for the stage.

`exitActionName` string The name of the evaluation flow used as an exit
condition for the stage.


Metadata Types Flow

**Field Name** **Field Type** **Description**

`exitActionOutputParameters` FlowStageStepExitActionOutputParameter[]

An array of output parameters from the evaluation flow
to the stage. These parameters specify an exit condition
for the stage.

`exitActionType` InvocableActionType (enumeration of type The type of the evaluation flow for the custom exit
string) condition. Valid values are:

**•** `EvaluationFlow`

**•** This value is available in API version 61.0 and later.

`exitConditionLogic` string Defines how the stage exit conditions are evaluated.
Valid values are:

**•** `And`

**•** `Or`

**•** `Custom logic, such as (1 AND (2`

```
                                OR 3))

```

**•** `Formula`

`exitConditions` FlowCondition[] An array of requirements that must be met to exit the
stage.

`faultConnector` FlowConnector Not used.

`runAsUser` boolean

Indicates whether an asynchronous background step
is run in the context of the user who completed the
most recently completed interactive step.

`stageSteps` FlowStageStep[] An array of stage step resources.

FlowOutputFieldAssignment

Assigns a record field’s value to a variable that can be used elsewhere in the flow. It extends FlowBaseElement and inherits all its fields.

**Field Name** **Field Type** **Description**

`assignToReference` string Required. Reference to the variable where you want to store the
value of the record field.

`field` string Required. Name of the field whose value is to be assigned after a
record lookup.

FlowRelatedRecordLookup (Beta)

[Note: This feature is a pilot or beta service that is subject to the Beta Services Terms at Agreements - Salesforce.com or a written](https://www.salesforce.com/company/legal/agreements/)
[Unified Pilot Agreement if executed by Customer, and applicable terms in the Product Terms Directory. Use of this pilot or beta](https://ptd.salesforce.com/)
service is at the Customer's sole discretion.


Metadata Types Flow

Finds records in the database that are related to the records specified in FlowRecordLookup and stores their field values in the flow.
Corresponds to a Get Records element in Flow Builder. It extends FlowBaseElement and inherits all its fields.

**Field Name** **Field Type** **Description**

`filterLogic` string The filter logic that’s applied to the filter
condition requirements. To require all

conditions, use `AND` . To require any
conditions, use `OR` . For custom
condition logic, enter the entire logic
string. For example, `1 AND 2 OR`
`(3 AND 4)` .

`filters` FlowRecordFilter[]

An array that specifies the criteria used
to select the record from the database.

If the filters return more than one
record, they’re sorted according to the

specified `sortField` and
`sortOrder` . If
`outputReference` specifies a
non-collection record variable or if
`getFirstRecordOnly` is `true`,
only the first record in the sorted list is
selected.

If `sortField` or `sortOrder` isn’t
specified, records aren’t returned in any
particular order. If
`outputReference` specifies a
non-collection record variable or if
`getFirstRecordOnly` is `true`,
only the first record in the unsorted list
is selected.

`getFirstRecordOnly` boolean Indicates whether to store field values
for only one record, even when

multiple records meet the filter criteria.
Supported only when

```
                                    storeOutputAutomatically
```

is `true` . When

```
                                    storeOutputAutomatically
```

is `false`, what determines whether
one or multiple records are stored is
whether `outputReference`
specifies a record variable or a record
collection variable.

`limit` FlowElementReferenceOrValue Specifies the maximum number of
records to store. Valid values are

between 2 and 20,000. Supported only


Metadata Types Flow

**Field Name** **Field Type** **Description**

when `getFirstRecordOnly` is
false.

`queriedFields` strings[]

An array that specifies which fields from
the selected record are saved to the
specified record variable.

`relatedObject` string Name of the related object from which
to select related records.

`relatedRecords` FlowRelatedRecordLookup[] An array that specifies the related
records to look up in the database.

`relationshipField` string Specifies the API name of the
relationship field used to link the object

to its related object. This field is
required for retrieving related records.

`sortField` string The field that’s used for sorting the
records that meet the filter criteria. If

this field isn’t specified, the returned
records aren’t sorted.

You can only sort records by fields that
have the `Sort` API field property, as
[specified in SOAP API.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/)

`sortOrder` SortOrder (enumeration of type string)

FlowRecordCreate

Order in which to sort the records. If
this field isn’t specified, then the results
aren’t sorted.

Valid values are:

**•** `Asc` —Ascending

**•** `Desc` —Descending

Create a record in the database using values from the flow. It extends FlowNode and inherits all its properties.

Note: The flow record `create`, `lookup`, `update`, and `delete` operations are different from the CRUD-based metadata
calls `create()`, `retrieve()`, `update()`, and `delete()` . The flow record methods apply to record operations from
within a flow, which aren’t the same as doing any metadata calls to CRUD setup entities.

**Field Name** **Field Type** **Description**

`assignRecordIdToReference` string Reference to the variable where you want to store the
ID after the record is created.

`connector` FlowConnector Specifies which node to execute after creating the record.


Metadata Types Flow

**Field Name** **Field Type** **Description**

`doesUpsert` boolean Indicates whether the element creates or updates
records. The default value is `false`, indicating that the

element only creates records. This field is available in API
version 62.0 and later.

`doesUpsertAllOrNone` boolean Indicates whether the element creates or updates records
only if all records are created or updated successfully. If

set to `true` and a record fails, then the transaction rolls
back and no records are created or updated.

If set to `false`, the transaction creates or updates only
the records that are successful. The default value is
`true` . This field is available in API version 62.0 and later.

`faultConnector` FlowConnector Specifies which node to execute if the attempt to create
a record results in an error.

`filterLogic` string The filter logic applied to the filter condition
requirements. To require all conditions, use `AND` . To

require any conditions, use `OR` . For custom condition
logic, enter the entire logic string. For example, `1 AND`
`2 OR (3 AND 4)` .

This field is available in API version 61.0 and later.

`filters` FlowRecordFilter[]

An array that specifies the criteria to select which records
to create or update in the database.

This field is available in API version 61.0 and later.

`inputAssignments` FlowInputFieldAssignment[] An array that assigns values to the specified fields of the
record being created.

`inputReference` string Specifies the record variable whose field values are used
to populate the new record’s fields.

`object` string Required. The object type that the element creates.

`operationMultMatchingRecords` string The operation to perform if multiple matching records
are found. Valid values are:

**•** `None`

**•** `UpdateAllRecords`

**•** `UpdateLatestRecord`

This field is available in API version 61.0 and later.

`operationOneMatchingRecord` string The operation to perform if one matching record is found.
Valid values are:

**•** `None`

**•** `UpdateAllRecords`


Metadata Types Flow

**Field Name** **Field Type** **Description**

This field is available in API version 61.0 and later.

`operationZeroMatchingRecords` string The operation to perform if no matching records are
found. Valid values are:

**•** `None`

This field is available in API version 61.0 and later.

`storeOutputAutomatically` boolean Indicates whether the record ID is automatically available
in the flow without creating any variables. When the

value is `true`, you can reference the record ID by
specifying the API name of the Create Records element
in the flow. The default value is `false` . When the value
is `false`, create a variable to store the record ID.

This field is available in API version 48.0 and later.

`upsertExternalIdField` string If `doesUpsert` is `true`, specifies the external ID field
on the record. You can provide a value for this property

or for the Upsert Standard ID Field property, but not both.
This field is available in API version 62.0 and later.

`upsertStandardIdField` string If `doesUpsert` is `true`, specifies the standard ID
field like Account ID on the object. You can provide a

value for this property or for the Upsert External ID Field
property, but not both. This field is available in API version
62.0 and later.

FlowRecordDelete

Deletes one or more records in the database. It extends FlowNode and inherits all its fields.

Note: The flow record `create`, `lookup`, `update`, and `delete` operations are different from the CRUD-based metadata
calls `create()`, `retrieve()`, `update()`, and `delete()` . The flow record methods apply to record operations from
within a flow, which aren’t the same as doing any metadata calls to CRUD setup entities.

**Field Name** **Field Type** **Description**

`connector` FlowConnector Specifies which node to execute after deleting the record.

`faultConnector` FlowConnector Specifies which node to execute if the attempt to delete a record results
in an error.

`filters` FlowRecordFilter[]

An array that specifies the criteria used to select which records to delete
from the database. For example, delete accounts whose last activity was
older than a specified date.

`inputReference` string Specifies the record variable whose record ID is used to identify which
record to delete in the database.


Metadata Types Flow

**Field Name** **Field Type** **Description**

`object` string Required. The name of the object whose records are deleted.

FlowRecordFilter

Sets the criteria for searching records in the database. It extends FlowBaseElement and inherits all its fields.

**Field Name** **Field Type** **Description**

`field` string Required. The field to be used for filtering records.

`operator` FlowRecordFilterOperator (enumeration Required. Valid values are:
of type string)

**•** `EqualTo`

**•** `NotEqualTo`

**•** `GreaterThan`

**•** `LessThan`

**•** `GreaterThanOrEqualTo`

**•** `LessThanOrEqualTo`

**•** `StartsWith`

**•** `EndsWith`

**•** `Contains`

**•** `IsNull`

`value` FlowElementReferenceOrValue Reference or value used with the field and operator to filter records.

FlowRecordLookup

Finds records in the database and stores their field values in the flow. Corresponds to a Get Records element in Flow Builder. It extends
FlowNode and inherits all its fields.

Note: The flow record `create`, `lookup`, `update`, and `delete` operations are different from the CRUD-based metadata
calls `create()`, `retrieve()`, `update()`, and `delete()` . The flow record methods apply to record operations from
within a flow, which aren’t the same as doing any metadata calls to CRUD setup entities.

**Field Name** **Field Type** **Description**

`assignNullValuesIfNoRecordsFound` boolean Specifies that all values are set to
`null` when no record is found.

Supported only when

```
                                       storeOutputAutomatically
```

is `false` .

This field is available in API version 30.0
and later.


Metadata Types Flow

**Field Name** **Field Type** **Description**

`connector` FlowConnector Specifies which node to execute after
getting records from the database.

`faultConnector` FlowConnector

Specifies which node to execute if the
attempt to get records results in an
error.

`filterLogic` string The filter logic that’s applied to the filter
condition requirements. To require all

conditions, use `AND` . To require any
conditions, use `OR` . For custom
condition logic, enter the entire logic
string. For example, `1 AND 2 OR`
`(3 AND 4)` . This field is available in
API version 50.0 and later.

`filters` FlowRecordFilter[]

An array that specifies the criteria used
to select the record from the database.

If the filters return more than one
record, they’re sorted according to the

specified `sortField` and
`sortOrder` . If
`outputReference` specifies a
non-collection record variable or if
`getFirstRecordOnly` is `true`,
only the first record in the sorted list is
selected.

If `sortField` or `sortOrder` isn’t
specified, records aren’t returned in any
particular order. If
`outputReference` specifies a
non-collection record variable or if
`getFirstRecordOnly` is `true`,
only the first record in the unsorted list
is selected.

`getFirstRecordOnly` boolean Indicates whether to store field values
for only one record, even when

multiple records meet the filter criteria.
Supported only when

```
                                    storeOutputAutomatically
```

is `true` . When

```
                                    storeOutputAutomatically
```

is `false`, what determines whether
one or multiple records are stored is
whether `outputReference`
specifies a record variable or a record
collection variable.


Metadata Types Flow

**Field Name** **Field Type** **Description**

This field is available in API version 47.0
and later.

`limit` FlowElementReferenceOrValue Specifies the maximum number of
records to store. Valid values are

between 2 and 20,000. Supported only
when `getFirstRecordOnly` is
false.

This field is available in API version 63.0
and later.

`object` string Name of the object from which to
select the record.

`outputAssignments` FlowOutputFieldAssignment[] An array that assigns fields from the
selected record to variables that can be

used elsewhere in the flow. Supported
only when

```
                                       storeOutputAutomatically
```

is `false` .

`outputReference` string Specifies the record variable or record
collection variable that stores the

queried fields’ values. Supported only
when

```
                                       storeOutputAutomatically
```

is `false` .

`queriedFields` string[]

An array that specifies which fields from
the selected record are saved to the
specified record variable.

`relatedRecords` (beta) FlowRelatedRecordLookup[] An array that specifies the related
records to look up in the database.

`sortField` string The field that’s used for sorting the
records that meet the filter criteria. If

this field isn’t specified, the returned
records aren’t sorted.

You can only sort records by fields that
have the `Sort` API field property, as
[specified in SOAP API.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/)

This field is available in API version 25.0
and later.


Metadata Types Flow

**Field Name** **Field Type** **Description**

`sortOrder` SortOrder (enumeration of type string)

Order in which to sort the records. If
this field isn’t specified, then the results
aren’t sorted.

Valid values are:

**•** `Asc` —Ascending

**•** `Desc` —Descending

This field is available in API version 25.0
and later.

`storeOutputAutomatically` boolean Indicates whether the returned records’
field values are automatically available

in the flow without creating any
variables. When the value is `true`, the
flow can reference a field by specifying
the `name` of the Get Records element
and the record field, such as
`Get_Contacts.AccountId` .
Supported only when
`processType` is `Flow` or
`AutoLaunchedFlow` .

This field is available in API version 47.0
and later.

FlowRecordRollback

Rolls back the current transaction and cancels its pending record changes. Corresponds to the Roll Back Records element in Flow Builder.
Available only in screen flows.

FlowRecordRollback extends FlowNode and inherits all its fields. This metadata type is available in API version 52.0 and later.

**Field Name** **Field Type** **Description**

`connector` FlowConnector Specifies which node to execute after rolling back the current
transaction.

FlowRecordUpdate

Finds records in the database and updates them with values from the flow. It extends FlowNode and inherits all its fields.

Note: The flow record `create`, `lookup`, `update`, and `delete` operations are different from the CRUD-based metadata
calls `create()`, `retrieve()`, `update()`, and `delete()` . The flow record methods apply to record operations from
within a flow, which aren’t the same as doing any metadata calls to CRUD setup entities.


Metadata Types Flow

**Field Name** **Field Type** **Description**

`connector` FlowConnector Specifies which node to execute after completing the record
update.

`faultConnector` FlowConnector Specifies which node to execute if the attempt to update a
record results in an error.

`filters` FlowRecordFilter[] An array that specifies the criteria used to select the records to
update in the database.

`inputAssignments` FlowInputFieldAssignment[] An array that assigns values to the specified fields of the record
being updated.

`inputReference` string Specifies the record variable whose field values are used to
update the record’s fields.

`object` string Required. Name of the object whose records are updated.

FlowRule

Defines the conditions and logic that enables a rule to evaluate to true. It extends FlowElement and inherits all of its fields.

**Field Name** **Field Type** **Description**

`attributes` FlowAttribute[] An array of attributes for the flow rule. This field is available in API
version 65.0 and later.

`conditionLogic` string Specifies logic for the conditions. Value can be:

**•** `and` —Evaluates to `true` if all of its conditions are true.

**•** `or` —Evaluates to `true` if any conditions are true.

**•** Advanced logic like `1 AND (2 OR 3)` —Evaluates to `true`
if the first condition is `true` and either the second or third
condition is `true` .

When you use advanced logic, the string can contain up to
1,000 characters.

`conditions` FlowCondition[] An array of conditions for the rule.

`connector` FlowConnector Specifies which node to execute if this rule evaluates to `true` in
a decision first.

`doesRequireRecordChangedToMeetCriteria` boolean If set to `true`, conditions evaluate to `true` only if the record
didn’t meet the required conditions before the triggering update

but now meets the conditions after the update. This field is available
in API version 50.0 and later.

`label` string Required. Label for the connector.


Metadata Types Flow

FlowSchedule

Specifies when and how frequently to run the flow. This metadata type is available in API version 47.0 and later.

**Field Name** **Field Type** **Description**

`dayOfMonthToRun` int The number of the day of the month on which the flow runs. For
example, `1` is the first day of the month, `2` is the second day of

the month, and so on. You can use `-1` for the last day of the month.
This field is available in API version 66.0 and later.

`daysOfWeekToRun` string

The number of the days of the week on which the flow is to run.
For example, `1`, `2`, `3`, where `1` is Sunday, 2 is Monday, and so on.
This field is available in API version 66.0 and later.

`endDate` date Reserved for future use.

`endTime` time Reserved for future use.

`frequency` FlowStartFrequency Specifies how frequently to run the flow. Valid values are:
(enumeration of type string)

**•** `Once`

**•** `Daily`

**•** `Weekly`

**•** `OnActivate` —For segment-triggered flows only. This value
is available in API version 49.0 and later.

**•** `Hourly` —For segment-triggered flows only. This value is
available in API version 66.0 and later.

**•** `Monthly` —For segment-triggered flows only. This value is
available in API version 66.0 and later.

**•** `Weekdays` —For segment-triggered flows only. This value is
available in API version 66.0 and later.

**•** `Yearly` —For segment-triggered flows only. This value is
available in API version 66.0 and later.

`frequencyNumber` int For segment-triggered flows only. The number of times to run the
flow for this schedule based on the `frequency` value. For

example, if this field is `2`, and `frequency` is `Hourly`, the flow
runs every hour for 2 hours . When this number is met, the flow no
longer runs for this schedule. This field is available in API version
66.0 and later.

`startDate` date The date when the flow runs, or when the flow’s run schedule starts
recurring.

`startTime` time The time of day when the flow runs, based on the org’s default time
zone.


Metadata Types Flow

FlowScheduledPath

Defines a scheduled path. It extends FlowElement and inherits all its fields. This metadata type is available in API version 51.0 and later.

**Field Name** **Field Type** **Description**

`connector` FlowConnector Specifies which node to execute after this scheduled path.

`label` string Label for the scheduled path.

`maxBatchSize` int The maximum number of scheduled path interviews to execute in
a single batch, from `1` to `200` . Default is `200` .

`offsetNumber` int Number of months, days, hours, or minutes to offset the time that
the scheduled path executes. Negative values offset the time to

execute before the provided time. Positive values offset the time
to execute after the provided time.

`offsetUnit` FlowScheduledPathOffsetUnit Specify the time unit used to offset when the scheduled path
(enumeration of type string) executes. Possible values are:

**•** `Months` —This value is available in API version 56.0 and later.

**•** `Days`

**•** `Hours`

**•** `Minutes`

`pathType` FlowScheduledPathType The type of scheduled path. `null` is used for time-triggered and
(enumeration of type string) record-triggered paths. The default value is `null` .

**•** `AsyncAfterCommit` —The scheduled path runs
asynchronously after a save.

`recordField` string Field used to determine when the scheduled path executes. The
field’s object is defined in FlowStart.

`timeSource` FlowScheduledPathTimeSource Specify if a field or event is used to determine when the scheduled
(enumeration of type string) path executes. Possible values are:

**•** `RecordField`

**•** `RecordTriggerEvent`

FlowScreen

Screens capture information from users and display information to users. It extends FlowNode and inherits all its fields.

**Field Name** **Field Type** **Description**

`actions` FlowScreenAction[]

An array of screen actions.

This field is available in API version 59.0 and later.

`allowBack` boolean Indicates whether to show ( `true` ) or hide ( `false` ) the **Previous**
button on the screen at runtime. When true, the **Previous** button


Metadata Types Flow

**Field Name** **Field Type** **Description**

appears only if the user visited a previous screen in the flow path
and if `showFooter` for the screen is set to `true` . Set this field
to false when revisiting the previous screen triggers an action that
you don’t want repeated, such as a credit card transaction.

This field is available in API version 26.0 and later.

Default: `true`

You can set either `allowBack` or `allowFinish` to false, but
not both.

`allowFinish` boolean Indicates whether to show ( `true` ) or hide ( `false` ) the **Finish**
button on the screen at runtime. When `true`, the **Finish** button

appears only if the screen element is the end of a flow path, and if
`showFooter` for the screen is set to `true` . The default value is
`true` .

Set to `false` if user is required to go back to a previous screen
to continue or complete the flow. For example, don’t include a
**Finish** button on a screen that tells the user to go back and make
corrections on a previous screen.

You can set `allowBack` or `allowFinish` to `false`, but
not both.

This field is available in API version 26.0 and later.

`allowPause` boolean

Indicates whether to show ( `true` ) or hide ( `false` ) the **Pause**
button on the screen at runtime. The default value is `true` .

A flow screen displays the **Pause** button if all these conditions are
`true` .

**•** **Let users pause flows** is enabled in the organization’s process
automation settings.

**•** `allowPause` for the screen is set to `true` .

**•** If the flow is embedded in a Visualforce page, the
<flow:interview> component has its `showAllowPause`
attribute set to `true` .

**•** The `showFooter` field for the screen is set to `true` .

This field is available in API version 33.0 and later.

`backButtonLabel` string A label for the Back button.

`connector` FlowConnector Specifies which node to execute after the screen node.

`fields` FlowScreenField[] An array of fields to display on the screen.

`helpText` string

Text that appears if the end user clicks a link for help text.

Supports merge fields in API version 26.0 and later.

`nextOrFinishButtonLabel` string A label for the Next or Finish button.


Metadata Types Flow

**Field Name** **Field Type** **Description**

`pauseButtonLabel` string A label for the Pause button.

`pausedText` string

A confirmation message that appears when an end user clicks
**Pause** .

This field is available in API version 33.0 and later.

`rules` Reserved for future use.

`showFooter` boolean

`showHeader` boolean

Indicates whether to show ( `true` ) or hide ( `false` ) the screen’s
footer at Lightning runtime. Classic runtime isn’t supported. The
default value is `true` .

The footer includes navigation actions for the screen. If
`showFooter` is hidden, use Lightning components on the screen
to show navigation actions.

This field is available in API version 42.0 and later.

Indicates whether to show ( `true` ) or hide ( `false` ) the screen’s
header at Lightning runtime. Classic runtime isn’t supported. The
default value is `true` .

The header includes access to help text for the screen. If
`showHeader` is hidden, use Lightning components on the screen
to show help text.

This field is available in API version 42.0 and later.

`stageReference` FlowElementReferenceOrValue The API name of the stage resource that’s associated with the screen.

`styleSettings` FlowScreenStyleSetting[]

`triggers` FlowScreenTrigger[]

FlowScreenAction

An array of flow screen style settings to customize the visual
experience of a screen at run time. This field is available in API
version 66.0 and later.

An array of triggers configured for a flow screen field or a flow screen
field attribute.

This field is available in API version 59.0 and later.

Defines an action that can be triggered by one or more flow screen components.

This metadata type is available in API version 59.0 and later.


Metadata Types Flow

FlowScreenActionInputParameter

Defines an iput parameter for a flow screen action. It extends FlowScreenFieldInputParameter and inherits all its fields.

This metadata type is available in API version 59.0 and later.

FlowScreenField

[Represents a screen component. FlowScreenField extends FlowElement and inherits all its fields. See Salesforce Help: Standard Flow](https://help.salesforce.com/s/articleView?id=platform.flow_ref_elements_screencmp.htm&language=en_US)
[Screen Components.](https://help.salesforce.com/s/articleView?id=platform.flow_ref_elements_screencmp.htm&language=en_US)

**Field Name** **Field Type** **Description**

`choiceReferences` string[] An array of references to FlowChoices or
FlowDynamicChoiceSets. The resulting choice

options appear in the order specified in this
array, where the element at index 0 provides
the top-most choice option. Supported for
these types of screen components.

**•** RadioButtons

**•** DropdownBox

**•** MultiSelectCheckboxes


Metadata Types Flow

**Field Name** **Field Type** **Description**

**•** MultiSelectPicklist

Multi-select checkboxes and multi-select
picklist fields are available in API version 26.0
and later.

`dataType` FlowDataType (enumeration of type Data type of the screen component. Only
string) supported for the InputField, RadioButtons, and

DropdownBox types of screen components.
Valid data types are:

**•** `Boolean`

**•** `Currency`

**•** `Date`

**•** `DateTime`

**•** `Number`

**•** `String`

**•** `Time`

Boolean input fields, which appear as checkbox
fields at runtime, are available in API version
26.0 and later.

Only the string data type is supported for
multi-select checkboxes and multi-select
picklist fields. Multi-select fields are available
in API version 26.0 and later.

Date/time input fields are available in API
version 43.0 and later.

`dataTypeMappings` FlowDataTypeMapping[] Reserved for future use.

`defaultSelectedChoiceReference` string The name of the FlowChoice element to use
as the default value for the screen component.

Supported for these types of screen
components.

**•** RadioButtons

**•** DropdownBox

**•** MultiSelectCheckboxes

**•** MultiSelectPicklist

For DropdownBox field types only, if

```
                                    defaultSelectedChoiceReference
```

is empty or null, the reference at index 0 of
`choiceReferences` is used as the default
value.

You can specify only one FlowChoice element
as the default value for multi-select checkboxes


Metadata Types Flow

**Field Name** **Field Type** **Description**

and multi-select picklist fields. Multi-select
fields are available in API version 26.0 and later.

`defaultValue` FlowElementReferenceOrValue The value that is used by default when the
screen component requires users to provide

input. Only supported for InputField,
LargeTextArea, and PasswordField.

`extensionName` string

`fields` FlowScreenField[]

The name of the Lightning component to
display. This field is available in API version 42.0
and later.

An array of columns to display in a section, or
an array of fields to display in a column. This
field is available in API version 49.0 and later.

`fieldText` string Field label that is displayed on the screen.
Supports merge fields.

`fieldType` FlowScreenFieldType (enumeration Required. The type of field to display on a flow
of type string) screen. Valid values are:

**•** `DisplayText`

**•** `InputField`

**•** `LargeTextArea`

**•** `PasswordField`

**•** `RadioButtons`

**•** `DropdownBox`

**•** `MultiSelectCheckboxes` —This
value is available in API version 26.0 and
later.

**•** `MultiSelectPicklist` —This value
is available in API version 26.0 and later.

**•** `ComponentInstance` —This value is
available in API version 42.0 and later.

**•** `ComponentChoice` and
`ComponentInput` —This value is
available in API version 48.0 and later for
the `Survey processType` value only.

**•** `Region`                                - Specifies that a screen field in
a section is a column. This value is available
in API version 51.0 and later.

**•** `RegionContainer` —Specifies that a
screen field is a section. This value is
available in API version 51.0 and later.

**•** `ObjectProvided` —Specifies that a
screen field is a field from a Salesforce


Metadata Types Flow

**Field Name** **Field Type** **Description**

object. This value is available in API version
51.0 and later.

At runtime, each multi-select field stores its
field value as a concatenation of the
user-selected choice values, separated by
semicolons. Any semicolons in the selected
choice values are removed when added to the
multi-select field value.

`helpText` string

`inputParameters` FlowScreenFieldInputParameter[]

Text that appears if the end user clicks the help
icon ( ) for the screen component.

Supports merge fields in API version 26.0 and
later.

An array of input parameters. Supported only
when `fieldType` is
`ComponentInstance` .

This field is available in API version 42.0 and
later.

`inputsOnNextNavToAssocScrn` FlowScreenFieldInputsRevisited Controls whether the flow remembers the
(enumeration of type string) input value if the user moves to any screen and

then returns to the screen component. Valid
values are:

**•** `UseStoredValues` —Uses values from
when the user last visited this screen.

**•** `ResetValues` —Refreshes inputs to
incorporate changes elsewhere in the flow.

The default value is `UseStoredValues` .

This property applies to screen components in
API version 51.0 and later and to record fields
on flow screens in API version 57.0 and later.

`isRequired` boolean

`isVisible` boolean

Indicates whether the user must select a choice
or provide input. Not supported for DisplayText
or boolean inputField.

`objectFieldReference` string Specifies the Salesforce object field for an
ObjectProvided field.

`outputParameters` FlowScreenFieldOutputParameter[] An array of output parameters. Supported only
when `fieldType` is

`ComponentInstance` and when


Metadata Types Flow

**Field Name** **Field Type** **Description**

`storeOutputAutomatically` is
`false` .

This field is available in API version 42.0 and
later.

`regionContainerType` FlowRegionContainerType Stores information about a section component
(enumeration of type string) header. Possible values include:

**•** `SectionWithHeader`

**•** `SectionWithoutHeader`

Available only when the component type is
`Section` . This field is available in API version
55.0 and later.

`scale` int Controls the number of digits to the right of
the decimal point up to 17 places. If you leave

this field blank or set it to zero, only whole
numbers appear when your flow runs.

Available only when the data type is Number
or Currency. Corresponds to the Decimal Places
field in Flow Builder.

`sourceTemplateApiName` string

`sourceTemplateProviderType` string

The API name of the template specified by the
provider. This field is available in API version
62.0 and later.

The API name of the source that provides the
template. This field is available in API version
62.0 and later.

`storeOutputAutomatically` boolean Indicates whether the screen component’s
output parameters are automatically available

in the flow without creating any variables.
When the value is `true`, you can reference an
output parameter by specifying the `name` of
the screen component and the output
parameter, such as
`Mailing_Address.City` .

Supported only when `fieldType` is
`ComponentInstance` .

This field is available in API version 47.0 and
later.

`styleProperties` FlowScreenFieldStyleProperties


Specifies the style properties of a screen
component.

This field is available in API version 64.0 and
later.

Metadata Types Flow

**Field Name** **Field Type** **Description**

`validationRule` FlowInputValidationRule

`visibilityRule` FlowVisibilityRule

FlowScreenFieldInputParameter

A rule that’s used to validate the user input
when the screen component is of type
InputField, LargeTextArea, or PasswordField.

A condition-based rule that’s used to render or
hide the screen component.

This field is available in API version 47.0 and
later.

Defines an input parameter from the flow to the extension. It extends FlowBaseElement and inherits all its fields.
FlowScreenFieldInputParameter is available in API version 42.0.

**Field Name** **Field Type** **Description**

`name` string Required. Unique name for the input
parameter.

`value` FlowElementReferenceOrValue Defines the value of the input parameter.

FlowScreenFieldOutputParameter

Defines an output parameter from the extension to the flow. It extends FlowBaseElement and inherits all its fields.
FlowScreenFieldOutputParameter is available in API version 42.0.

**Field Name** **Field Type** **Description**

`assignToReference` string Required. Specifies the variable to which you
want to assign the output parameter value.

`name` string Required. Unique name for the output
parameter.

FlowScreenFieldStyleProperties

Defines how a screen component looks on a screen element at run time.

This metadata type is available in API version 64.0 and later.

**Field Name** **Field type** **Description**

`styleSettings` FlowScreenStyleSetting[]

An array of flow screen style settings to customize the visual
experience of a screen component at run time. This field is available
in API version 66.0 and later.


Metadata Types Flow

**Field Name** **Field type** **Description**

`width` FlowElementReferenceOrValue

The number of columns the width of the screen component fills up
in a screen element's 12-column wide spatial grid. Valid values are
numbers `1` through `12` .

`verticalAlignment` FlowElementReferenceOrValue The vertical alignment of the screen component. Valid values are
`top`, `middle`, `bottom` .

FlowScreenStyleSetting

A style setting for a flow screen or flow screen component. FlowScreenStyleSetting extends FlowBaseElement and inherits all its fields.
FlowScreenStyleSetting is available in API version 66.0 and later.

**Field Name** **Field Type** **Description**

`propertyName` string The name of the screen style property such as,
`--slds-c-input-color-border` .

`propertyValue` FlowElementReferenceOrValue

Defines the value for the screen style property
such as,
`<stringValue>#4AC7CA</stringValue>` .

`scope` string Specifies where the style setting is applied on
a screen. Valid values:

**•** `Container`

**•** `Header`

**•** `NextOrFinish`

**•** `Previous`

**•** `Pause`

Not supported for screen components.

FlowScreenTrigger

Defines an event handler for a flow screen component.

This metadata type is available in API version 59.0 and later.


Metadata Types Flow

FlowScreenTriggerHandler

Defines conditions for a flow screen trigger handler.

This metadata type is available in API version 59.0 and later.


Metadata Types Flow

FlowStage

A section of your flow that can be represented in the UI, such as with breadcrumbs. It extends FlowElement and inherits all its fields.

When an interview starts, any stages where `isActive` is `true` are added to the `$Flow.ActiveStages` global variable, which
holds a collection of stages. Each stage’s `stageOrder` determines the order they’re added in. The stage with the lowest `stageOrder`
is assigned to the `$Flow.CurrentStage` global variable.

**Field Name** **Field Type** **Description**

`isActive` boolean Indicates whether the stage is active by default.

`label` string A user-friendly label for this stage.

`stageOrder` int Indicates how the stage is ordered against other stages. The
`stageOrder` value must be unique within the flow.

FlowStageStep

A step resource defines a step within a stage node. This metadata type is available in API version 53.0 and later.

**Field Name** **Field Type** **Description**

`actionName` string Required. Name of the flow associated with
the step.

`actionType` InvocableActionType (enumeration of type Required. The type of the step. Valid values
string) are:

**•** `stepApproval` —An Approval step
available only for flow approval
processes. This value is available in API
version 62.0 and later.

**•** `stepBackground` —A Background
step available for both flow approval
processes and orchestrations.

**•** `stepInteractive` —An Interactive
step available only for orchestrations.

**•** `stepMuleSoft` —A MuleSoft step
available only for orchestrations.


Metadata Types Flow

**Field Name** **Field Type** **Description**

`assignees` FlowStageStepAssignee An array of users, groups, or queues that are
assigned to complete the interactive step.

`canAssigneeEdit` boolean Reserved for future use.

`debugSimulateStep` boolean

`entryActionInputParameters` FlowStageStepEntryActionInputParameter[]

Specifies whether to run the step in rollback
mode. This field is available in API version
650 and later.

An array of input parameters from the step
to the evaluation flow that are used as an
entry condition for the step.

`entryActionName` string The name of the evaluation flow used as an
entry condition for the step.

`entryActionOutputParameters` FlowStageStepEntryActionOutputParameter[]

`entryActionType` InvocableActionType (enumeration of type
string)

An array of output parameters from the
evaluation flow to the step used to
determine if the step can be started.

The type of the evaluation flow used as a
custom entry condition for the step. Valid
values are:

**•** `EvaluationFlow`

`entryConditionLogic` string Defines how the entry requirements for a
step are evaluated. Valid values are:

**•** `And`

**•** `Or`

**•** `Custom logic, such as (1`

```
                                    AND (2 OR 3))

```

**•** `Formula`

`entryConditions` FlowCondition[] An array of requirements that must be met
to start the step.

`exitActionInputParameters` FlowStageStepExitActionInputParameter[]

An array of input parameters from the step
to the evaluation flow. These parameters
specify an exit condition for the step.

`exitActionName` string The name of the step exit evaluation flow.

`exitActionOutputParameters` FlowStageStepExitActionOutputParameter[] An array of output parameters from the
evaluation flow to the step. These

parameters specify an exit condition for the
step.


Metadata Types Flow

**Field Name** **Field Type** **Description**

`exitActionType` InvocableActionType (enumeration of type
string)

`exitConditionLogic` string

The type of the evaluation flow used as a
custom exit condition for the step. The only
possible value are:

**•** `EvaluationFlow`

.

Defines how the exit requirements for an
interactive step are evaluated. Valid values
are:

**•** `And`

**•** `Or`

**•** `Custom logic, such as (1`

```
  AND (2 OR 3))

```

**•** `Formula`

`exitConditions` FlowCondition[] An array of requirements to be met for
exiting an interactive step.

`inputParameters` FlowStageStepInputParameter[] An array of input parameters from the step
to its associated flow.

`label` string Required. The label for the step.

`outputConfigParams` FlowStageStepOutputConfigParam[]

An array of mock output values to use to
debug the step in rollback mode. This field
is available in API version 650 and later.

`outputParameters` FlowStageStepOutputParameter[] An array of output parameters from a flow
to its associated step.

`requiresAsyncProcessing` boolean Not used in API version 63.0.

`shouldLock` boolean Reserved for future use.

`stepSubtype` FlowElementSubtype (enumeration of type Reserved for internal use.
string)

FlowStageStepAssignee

An assignee associated with an Interactive step. Applicable only for interactive steps. This metadata type is available in API version 53.0
and later.

**Field Name** **Field Type** **Description**

`assignee` FlowElementReferenceOrValue Names of the user, group, or queue assigned to the interactive step.

`assigneeType` FlowStageStepAssigneeType Required. The type of the assignee associated with the interactive
(enumeration of type string) step. Valid values are:

**•** `Group`


Metadata Types Flow

**Field Name** **Field Type** **Description**

**•** `Queue`

**•** `User`

**•** `invalid—` This value is available in API version 61.0 and later.

FlowStageStepEntryActionInputParameter

Defines an input parameter from the step to its associated evaluation flow. It extends FlowBaseElement and inherits all its fields. This
metadata type is available in API version 53.0 and later.

**Field Name** **Field Type** **Description**

`name` string Required. The unique name for the input parameter of the
evaluation flow used by a step as an entry condition.

`value` FlowElementReferenceOrValue Defines the value of the input parameter of the evaluation flow
used by a step as an entry condition.

FlowStageStepEntryActionOutputParameter

Defines an output parameter from an evaluation flow used to determine if the step meets entry criteria. It extends FlowBaseElement
and inherits all its fields. This metadata type is available in API version 53.0 and later.

**Field Name** **Field Type** **Description**

`assignToReference` string Reserved for future use.

`name` string Required. A unique name for the output parameter of the evaluation
flow used by a step as an entry condition. Valid values are:

**•** `isOrchestrationConditionMet`

FlowStageStepExitActionInputParameter

Defines an input parameter from the stage or step to its associated evaluation flow. It extends FlowBaseElement and inherits all its fields.
This metadata type is available in API version 53.0 and later.

**Field Name** **Field Type** **Description**

`name` string Required. A unique name for the input parameter of the evaluation
flow used by a stage or step as an exit condition.

`value` FlowElementReferenceOrValue Defines the value of the input parameter of the evaluation flow
used by a stage or step as an exit condition.


Metadata Types Flow

FlowStageStepExitActionOutputParameter

Defines an output parameter from an evaluation flow used to determine if the stage or step meets exit criteria. It extends FlowBaseElement
and inherits all its fields. This metadata type is available in API version 53.0 and later.

**Field Name** **Field Type** **Description**

`assignToReference` string Reserved for future use.

`name` string

FlowStageStepInputParameter

Required. A unique name for the output parameter of the evaluation
flow used by a stage or step as an exit condition. The only possible
value is `isOrchestrationConditionMet` .

Defines an input parameter from the step to the flow. It extends FlowBaseElement and inherits all its fields. This metadata type is available
in API version 53.0 and later.

**Field Name** **Field Type** **Description**

`name` string Required. Unique name for the input parameter for a flow associated
with the step.

`value` FlowElementReferenceOrValue Defines the value of the input parameter of the flow associated
with a step.

FlowStageStepOutputConfigParam

Defines a mock output value for a step. It extends FlowBaseElement and inherits all its fields. This metadata type is available in API version
65.0 and later.

Field Name Field Type Description

`name` string Required. Unique name for the mock output
value associated with the step.

`value` FlowElementReferenceOrValue Required. Defines the value of the mock
output value. For enhanced security and

data privacy, don't store personal
identifiable information in this field.

FlowStageStepOutputParameter

Defines an output parameter from the step to the flow. It extends FlowBaseElement and inherits all its fields. This metadata type is
available in API version 53.0 and later.

**Field Name** **Field Type** **Description**

`assignToReference` string Reserved for future use.


Metadata Types Flow

**Field Name** **Field Type** **Description**

`name` string Required. Unique name for the output parameter for a flow
associated with the step.

FlowStart

Represents the flow’s Start element, which specifies how the flow starts. In an autolaunched flow, the Start element also defines when
and how frequently to run the flow. To run the flow only for specific records, the Start element can define filter criteria.

FlowStart extends FlowNode and inherits all its fields except `name` and `label` . This metadata type is available in API version 47.0 and
later.

**Field Name** **Field Type** **Description**

`activation` string The ID of the activation that triggers the flow. This field is available
in API version 63.0 and later.

`activationTemplate` string

`capabilityTypes` FlowCapability[]

The name of the activation template that determines the contact
point for each channel configured in the activation template for a
segment-triggered flow. This field is available in 66.0 and later.

An array of capabilities that can pass data with the flow. Only one
capability is supported in API version 60.0 and later. This field is
available in API version 60.0 and later.

`connector` FlowConnector Specifies which element to execute first.

`conditionLogic` string Defines how the filtering conditions are evaluated. Valid values are:

**•** `And`

**•** `Or`

`conditions` FlowCondition[] An array of conditions that must be true for the event to trigger.

`dataGraph` string

`dataTypeMappings` FlowDataTypeMapping[]

The data graph associated with the flow. Reference fields from this
data graph throughout the flow. This field is available in API version
61.0 and later.

An array of data type mappings for input and output values that
have the generic sObject data type. This field is available in API
version 63.0 and later.

`doesRequireRecordChangedToMeetCriteria` boolean If set to `true`, conditions evaluate to `true` only if the record
didn’t meet the required conditions before the triggering update

but now meets the conditions after the update. This field is available
in API version 50.0 and later.

`entryType` FlowEntryType (enumeration Specifies when a unified individual can join a flow. Valid values are:
of type string)

**•** `AfterCompletion` —Unified individuals can join the flow
only after they complete all previous flow runs of the same flow
definition.

**•** `Always` —Unified individuals can always join the flow.


Metadata Types Flow

**Field Name** **Field Type** **Description**

**•** Never—Unified individuals can never reenter the flow. This
value is available in API version 63.0 and later.

This field is available in API version 60.0 and later.

`eventName` string The name of the automation event that triggers the automation
event-triggered flow. Valid values are:

**•** `trgrOnSmsSubscription`

**•** `trgrOnEmailSubscription`

**•** `trgrOnOrderPlacement`

**•** The API name of a form

**•** The API name of an external service

This field is available in API version 61.0 and later.

`eventType` InvocableActionType The type of the automation event that triggers the automation
(enumeration of type string) event-triggered flow. Valid values are:

**•** `exploreConversation` —Available in API version 61.0
and later.

**•** `externalEvent`

**•** `processWebStoreUserRgstr`

**•** `trgrOnCustomEvent` —Available in API version 64.0 and
later.

**•** `trgrOnEmailBounceEngagement`

**•** `trgrOnEmailLinkClickEngagement`

**•** `trgrOnEmailOpenEngagement`

**•** `trgrOnEmailSubscription`

**•** `trgrOnFormSubmission`

**•** `trgrOnOrderPlacement`

**•** `trgrOnReferralEventSubmission` —Available in
API version 65.0 and later.

**•** `trgrOnSmsDeliveryFailureEngagement`

**•** `trgrOnSmsLinkClickEngagement`

**•** `trgrOnSmsResponseEngagement`

**•** `trgrOnSmsSubscription`

**•** `trgOnVoucherStsChgOtbdEngmt` —Available in API
version 65.0 and later.

**•** `trgrOnWebCartAbandoned`

**•** `trgrOnWhatsAppDeliveredEngagement`

**•** `trgrOnWhatsAppDlvrFailureEngmt`

**•** `trgrOnWhatsAppLinkClickEngmt`

**•** `trgrOnWhatsAppReadEngagement`


Metadata Types Flow

**Field Name** **Field Type** **Description**

**•** `trgrOnWhatsAppResponseEngmt`

**•** `trgrOnWhatsAppSubscription`

`fanOutAction` FlowActionCall The invocable action in the Start element of a broadcast flow. This
field is available in 66.0 and later.

`filterFormula` string

A formula that’s used to filter what records execute the flow during
a save. Available only in record-triggered flows. This field is available
in API version 55.0 and later.

`filterLogic` string The filter logic that’s applied to the filter condition requirements.
To require all conditions, use `AND` . To require any conditions, use

`OR` . For custom condition logic, enter the entire logic string, for
example `1 AND 2 OR (3 AND 4)` . This field is available in
API version 50.0 and later.

`filters` FlowRecordFilter[]

An array of filters to apply when retrieving records from the
database. For example, filter accounts to include only the records
that haven’t been updated in the last 4 weeks.

`flowRunAsUser` string Specifies who to run the flow as. Possible values are:

**•** `TriggeringUser` —Run the flow as the user that triggered
the flow.

**•** `DefaultWorkflowUser` —Run the flow as the default
workflow user.

This field is available in API version 60.0 and later.

`form` string

Required only for form-triggered flows. The content key value for
the form used to trigger the flow. This field is available in API version
59.0 and later.

`inputs` FlowStartInputParameter[] An array of inputs to the Start element.

`object` string

`prioritizedContactPointsList` string

The object whose records you want to retrieve from the database.
A flow interview starts for each record that meets the filter
conditions.

A comma-separated list of channels used to choose the individual
in the segment-triggered flow. The flow ranks these channels to
select an individual. Valid values are: `Email`, `Phone` .

If the flow finds contact points for both, it uses the higher-ranked
channel. For example, if the list is `Phone`, `Email` and both exist,

the flow selects the individual associated with the phone. This field
is available in 66.0 and later.

`publishSegment` boolean Indicates whether to republish the segment and update segment
membership before the flow runs or on the segment’s Data Cloud

publish schedule. When the value is `true`, the segment
is immediately republished before the flow runs, and ignores the


Metadata Types Flow

**Field Name** **Field Type** **Description**

segment's publish schedule. When the value is `false`, the
segment is republished on the segment's Data Cloud publish
schedule, but the segment isn't republished if the schedule is set
to `Do not refresh` .

The default value is `false` .

This field is available in API version 60.0 and later.

`recordTriggerType` RecordTriggerType Specifies what type of record changes can start the flow. Possible
(enumeration of type string) values are:

**•** `Create` —When a record is created.

**•** `Update` —When a record is updated.

**•** `CreateAndUpdate` —When a record is created and
updated.

**•** `Delete` —When a record is deleted. This value is available in
API version 50.0 and later.

**•** `None` —For flows that aren’t record-triggered flows. This value
is available in API version 55.0 and later.

Available only when `triggerType` is `RecordBeforeSave`
or `DataCloudDataChange` . This field is available in API version
48.0 and later.

`schedule` FlowSchedule Required when `triggerType` is `Scheduled` . Specifies when
and how frequently the flow runs.

`scheduledPaths` FlowScheduledPath[] Specifies the flow’s scheduled paths. This field is available in API
version 51.0 and later.

`segment` string The segment used to trigger the flow. This field is available in API
version 56.0 and later.

`sendMsgToOneContactPtPerIndv` boolean Indicates whether a segment-triggered flow sends a message to
only one contact per individual ( `true` ) or multiple contacts

( `false` ). The default value is ( `false` ). If
`activationTemplate` is set, this field must be `true` . This
field is available in 66.0 and later.

`TimeZoneSidKey` string Reserved for future use.

`triggeringDataGraph` string

`triggeringDataModelObjectPath` string

The API name of the data graph that includes the data model object
that triggers the automation event-triggered flow. This field is
available in API version 63.0 and later.

The Data Cloud path to the data model object that triggers the
automation event-triggered flow. This field is available in API version
63.0 and later.


Metadata Types Flow

**Field Name** **Field Type** **Description**

`triggerType` FlowTriggerType
(enumeration of type string)

Specifies what causes the flow to run. If you exclude this field, the
flow has no trigger and starts only when a user or app launches the
flow. Possible values are:

**•** `Activation` —The flow starts when an activation is
published. This value is available in API version 63.0 and later.

**•** `AutomationEvent` —The flow starts when an automation
event such as an SMS subscription occurs. This value is available
in API version 62.0 and later.

**•** `Capability` —When `capabilityTypes` is set, the
flow starts when the capability is run. This value is available in
API version 60.0 and later.

**•** `DataCloudDataChange` - The flow starts when data
model object (DMO) or calculated insight object (CIO)
conditions are met. This value is available in API version 59.0
and later.

**•** `DataGraphDataChange` - The flow starts when
conditions are met in the specified data graph field. This value
is available in API version 63.0 and later.

**•** `EventDrivenJourney` —Reserved for internal use.

**•** `ExternalSystemChange` —The flow starts when a
relevant change is detected in an external system. This value is
available in API version 63.0 and later.

**•** `PlatformEvent` —The flow starts when a platform event
message is received. This value is available in API version 49.0
and later.

**•** `RecordAfterSave` —The flow starts after a record is saved.
This value is available in API version 49.0 and later.

**•** `RecordBeforeDelete` —Deleting a record triggers an
autolaunched flow before the record is deleted from the
database. This value is available in API version 50.0 and later.

**•** `RecordBeforeSave` —Creating and/or updating a record
triggers an autolaunched flow to make more updates to that
record before it’s saved to the database. This value is available
in API version 48.0 and later.

**•** `Scheduled` —The flow starts at the scheduled time. This
value is available in API version 47.0 and later.

**•** `ScheduledJourney` - The flow starts only at the
scheduled time and frequency. This value is available in API
version 49.0 and later.

**•** `Segment` - At the scheduled time, the flow send emails to
individuals included in the chosen segment. This value is
available in API version 56.0 and later.


Metadata Types Flow

**Field Name** **Field Type** **Description**

Available only when `processType` is `AutoLaunchedFlow`
or `PromptFlow` . This field is available in API version 47.0 and
later.

`versionString` string
Specifies the version of the automation event.

This field is available in API version 65.0 and later.

FlowCapability

Defines the data structure of a capability. When the capability is invoked, it triggers the flow to run and data is passed between the flow
and capability. It extends FlowElement and inherits all of its fields. This metadata type is available in API version 60.0 and later.

**Field Name** **Field Type** **Description**

`capabilityName` string

Required. The specified capability that the flow integrates with. The
valid format is _`Name`_ :// _`Name`_, for example,
PromptBuilder://SalesEmail

`inputs` FlowCapabilityInput[] An array of capability inputs. The flow sets the input values and
passes the data to the capability.

FlowCapabilityInput

Defines the data structure of a capability input. It extends FlowElement and inherits all of its fields. This metadata type is available in API
version 60.0 and later.

**Field Name** **Field Type** **Description**

`capabilityInputName` string Required. The input name is the same for the capability and the
flow.

`dataType` string The data type of the capability input. Valid types are:

**•** `Boolean` —This value is available in API version 61.0 and later.

**•** `Currency` —This value is available in API version 61.0 and
later.

**•** `Date` —This value is available in API version 61.0 and later.

**•** `Number` —This value is available in API version 61.0 and later.

**•** `sObject` —This value corresponds to a record variable. This
value is available in API version 60.0 and later.

**•** `String` —This value is available in API version 61.0 and later.

`isCollection` boolean Required. Indicates whether the input is a collection of values. The
default value is `false` .


Metadata Types Flow

FlowStartInputParameter

Defines an input parameter to the flow Start element. It extends FlowBaseElement and inherits all its fields. This metadata type is available
in API version 62.0 and later.

**Field Name** **Field Type** **Description**

`name` string Required. The unique name for the input parameter to the Start
element.

`value` FlowElementReferenceOrValue Defines the value of the input parameter to the Start element.

FlowStep

Steps function as placeholders when you’re building a flow. It extends FlowNode and inherits all its fields.

**Field Name** **Field Type** **Description**

`connectors` FlowConnector[] Specifies which node to execute after the step node.

FlowSubflow

A subflow element references another flow, which it calls at run time. The flow that contains the subflow element is referred to as the
parent flow. FlowSubflow extends FlowNode and inherits all its fields. It’s available in API version 25.0 and later.

**Field Name** **Field Type** **Description**

`connector` FlowConnector Specifies which node to execute after the subflow.

`flowName` string

References the flow to call at runtime. The value must
be an API name of a flow and it can’t contain an
appended hyphen and version number.

`inputAssignments` FlowSubflowInputAssignment[] An array of input variable assignments that are set at the
start of the flow.

`outputAssignments` FlowSubflowOutputAssignment[] An array of output variable assignments that are set at
the end of the flow.

`storeOutputAutomatically` boolean Indicates whether the subflow’s output parameters are
automatically available in the flow without creating any

variables. When the value is `true`, you can reference
an output parameter by specifying the API name of the
subflow in the flow. When the value is `false`, create
variables manually to store output values from the
subflow. The default value is `false` .

This field is available in API version 49.0 and later.


Metadata Types Flow

FlowSubflowInputAssignment

Assigns an element or value from the parent flow to a variable in the referenced flow. Input assignments occur when the subflow calls
the referenced flow. It extends FlowBaseElement and inherits all its fields. It’s available in API version 25.0 and later.

**Field Name** **Field Type** **Description**

`name` string Required. Unique name for the variable in the referenced
flow.

`value` FlowElementReferenceOrValue Defines the value to assign to the variable.

FlowSubflowOutputAssignment

Assigns the value of a variable from the referenced flow to a variable in the parent flow. Output assignments occur when the referenced
flow is finished running. It extends FlowBaseElement and inherits all its fields. It’s available in API version 25.0 and later.

**Field Name** **Field Type** **Description**

`assignToReference` string Unique name for the variable in the parent flow.

`name` string Required. Unique name for the variable in the referenced flow.

FlowTransform

Defines a node that can dynamically transform the value of source data to target data in the flow. It extends FlowNode and inherits all
of its fields. This metadata type is available in API version 59.0 and later.

**Field Name** **Field Type** **Description**

`apexClass` string The Apex class of the target data after transformation if its data type
is `Apex` .

`connector` FlowConnector[] Specifies which node to execute after this data transformation.

`dataType` FlowDataType (enumeration
of type string)

Required. Specifies the data type of the transformed data. In Flow
Builder, it corresponds to the target data in the Transform element.
Valid types are:

**•** `Apex`

**•** `Boolean` —This value is available in API version 62.0.

**•** `Currency` —This value is available in API version 62.0.

**•** `Date` —This value is available in API version 62.0.

**•** `DateTime` —This value is available in API version 62.0.

**•** `Number` —This value is available in API version 62.0.

**•** `String` —This value is available in API version 62.0.

**•** `sObject` —This value corresponds to a record variable.

**•** `Time`


Metadata Types Flow

**Field Name** **Field Type** **Description**

`isCollection` boolean Indicates whether the variable is a collection of values. The default
value is `false` .

`objectType` string Object type of this variable resource if its data type is `sObject` .

`scale` int

Controls the number of digits to the right of the decimal point up
to 17 places. If you leave this field blank or set it to zero, only whole
numbers appear when your flow runs.

Corresponds to the Decimal Places field in Flow Builder.

`storeOutputAutomatically` boolean Reserved for future use.

`transformValues` FlowTransformValue[] An array of values for data transformation

FlowTransformValue

Defines the values for transforming specific data in the flow. It extends FlowBaseElement and inherits all its fields. This metadata type is
available in API version 59.0 and later.

**Field Name** **Field Type** **Description**

`transformValueActions` FlowTransformValueAction[] An array of actions for data transformation

`transformValueName` string Reserved for future use.

`transformValueLabel` string Reserved for future use.

`transformValueDescription` string Reserved for future use.

FlowTransformValueAction

Defines the data and actions to transform in the flow. It extends FlowBaseElement and inherits all its fields. This metadata type is available
in API version 59.0 and later.

**Field Name** **Field Type** **Description**

`actionName` string Reserved for future use.

`actionType` InvocableActionType Reserved for future use.
(enumeration of type string)

`actionVersionString` string Reserved for future use.

`assignToReference` string Reserved for future use.

`inputParameters` FlowTransformValueActionInputParameter[] An array of input parameters for data transformation. This field is
available in API version 60.0 and later.

`outputFieldApiName` string

The API name of the field for transformed data in a data
transformation mapping. In Flow Builder, it corresponds to the
target data field in the Transform element.


Metadata Types Flow

**Field Name** **Field Type** **Description**

`transformType` FlowTransformValueActionType Required. The type of transformation from source data to target
(enumeration of type string) data. Valid types are:

**•** `Count` —Calculates the number of items in a source collection.

**•** `GetItemByIndex` —Reserved for future use.

**•** `InnerJoin` —Joins selected data from two source collections
that are stored in a target collection in a flow. This value is
available in API version 63.0 and later. See
`complexValueType` on FlowElementReferenceOrValue.
`InnerJoin` isn't a valid value for FlowInlineTransform.

**•** `InvocableAction` —Reserved for future use.

**•** `Map` —Specifies a mapping between the datasets in flows. In
Flow Builder, it corresponds to the mapping between source
data fields and target data fields.

**•** `Sum` —Adds the numeric values of a field on each item in a
collection.

`value` FlowElementReferenceOrValue

Defines the value of the transformed data. In Flow Builder, the value
of this field corresponds to the result of the target data field in the
Transform element.

FlowTransformValueActionInputParameter

Defines the input parameters of the source data for data transformation. This metadata type is available in API version 60.0 and later.

**Field Name** **Field Type** **Description**

`name` string

A key that specifies the configuration of input parameters for this
data transformation when `transformType` is set to `Sum` or
`Count` . Valid values are:

**•** `aggregationField` —The field on each item in a source
collection that’s used to calculate the transformed value.

**•** `aggregationValues` —The source collection that’s used
to calculate the transformed value.

`value` FlowElementReferenceOrValue Defines the value of the specified key in `name` .

FlowTextTemplate

Defines a text template that can be used throughout the flow. It extends FlowElement and inherits all its fields.

**Field Name** **Field Type** **Description**

`isViewedAsPlainText` boolean If set to `true`, the flow resource remembers the View as Plain Text
setting used for the text template after the flow resource is saved.


Metadata Types Flow

**Field Name** **Field Type** **Description**

If set to `false`, the flow resource uses the View as Rich Text
setting.

The default value is `false` .

`text` string Actual text of the template. Supports merge fields.

FlowValueMappingType

Defines the specific data transformation type that converts the value of a source action output parameter in `valueMappingKey`
before assigning the result to the target output parameter in `valueMappingTarget` .

**Field Name** **Field Type** **Description**

`FirstEntry` string This configuration extracts the first item's
object in `valueMappingKey` and

assigns it to the target output parameter in
`valueMappingTarget` .

FlowVariable

With variables, creates updatable values to use in the flow. FlowVariable extends FlowElement and inherits all its fields.

**Field Name** **Field Type** **Description**

`apexClass` string

The Apex class of this variable if its data type
is `Apex` . This field is available in API version
46.0 and later.

`dataType` FlowDataType (enumeration of type string) Required. Valid types are:

**•** `Apex` —This value is available in API
version 46.0 and later.

**•** `Boolean`

**•** `Currency`

**•** `Date`

**•** `DateTime` —This value is available in
API version 30.0 and later.

**•** `Number`

**•** `Multipicklist` —This value is
available in API version 34.0 and later.

**•** `Picklist` —This value is available in
API version 34.0 and later.

**•** `String`

**•** `sObject` —This value corresponds to
a record variable.


Metadata Types Flow

**Field Name** **Field Type** **Description**

**•** `Time`

`isCollection` boolean Indicates whether the variable is a collection
of values. This field is available in API version

30.0 and later. In API version 32.0 and later,
a collection variable can be of any data type.

The default value is `False` .

`isInput` boolean Indicates whether the variable can be set at
the start of the flow using URL parameters,

Visualforce controllers, or subflow inputs.
This field is available in API version 25.0 and
later.

Default value:

**•** `False` for a variable created in API
version 25.0 and later or in the Flow
Builder in Summer ’12 and later.

**•** `True` for a variable created in API
version 24.0 or in Flow Builder in Spring
’12 and earlier.

Disabling input or output access for an
existing variable can break the functionality
of applications and pages that call the flow
and access the variable. For example, you
can access variables from URL parameters,
processes, and other flows.

`isOutput` boolean Indicates whether the variable’s value can
be accessed from Visualforce controllers and

other flows. This field is available in API
version 25.0 and later.

Default value:

**•** `False` for a variable created in API
version 25.0 and later or in the Flow
Builder in Summer ’12 and later.

**•** `True` for a variable created in API
version 24.0 or in Flow Builder in Spring
’12 and earlier.

Disabling input or output access for an
existing variable can break the functionality
of applications and pages that call the flow
and access the variable. For example, you
can access variables from URL parameters,
processes, and other flows.


Metadata Types Flow

**Field Name** **Field Type** **Description**

`objectType` string Object type of this variable if its data type is
`sObject` .

`scale` int Controls the number of digits to the right
of the decimal point up to 17 places. If you

leave this field blank or set it to zero, only
whole numbers appear when your flow
runs.

Corresponds to the Decimal Places field in
Flow Builder.

`value` FlowElementReferenceOrValue

FlowVisibilityRule

Default value of this variable.

Default values aren’t supported if the
variable’s data type is `Picklist` or
`Multipicklist` .

Visibility rules render a flow screen component when visibility rule conditions are met. Hides a flow screen component when visibility
rule conditions aren’t met. This metadata type is available in API version 47.0 and later.

**Field Name** **Field Type** **Description**

`conditionLogic` string Specifies logic for the conditions. Value can be:

**•** `and` —Evaluates to `true` only if all its conditions evaluate to
true.

**•** `or` —Evaluates to `true` if any of its conditions evaluate to
true.

**•** Advanced logic like `1 AND (2 OR 3)` —Evaluates to `true`
if the first condition is `true` and either the second or third
condition is `true` .

When you use advanced logic, the string must consist of 1,000
or fewer characters.

`conditions` FlowCondition[] An array of conditions that must be true for the flow to wait for this
event.

FlowWait

Waits for one or more defined events to occur. FlowWait extends FlowNode and inherits all its fields. FlowWait is available in API version
32.0 and later.


Metadata Types Flow

**Field Name** **Field Type** **Description**

`defaultConnector` FlowConnector

Specifies which node to execute if the
conditions are false for every event in the
Wait element.

`defaultConnectorLabel` string Label for the default connector.

`faultConnector` FlowConnector Specifies which node to execute if the
attempt to wait results in an error. If any of

the wait events fail, the flow takes the fault
connector.

`timeZoneId` string Reserved for future use.

`waitEvents` FlowWaitEvent[]

FlowWaitEvent

An array of events that the Wait element is
waiting for.

If the conditions for every event evaluate to
`false`, the `defaultConnector` is
used.

An event that a FlowWait element is waiting for. FlowWaitEvent extends FlowElement and inherits all its fields. FlowWaitEvent is available
in API version 32.0 and later.

**Field Name** **Field Type** **Description**

`conditionLogic` string Specifies logic for the conditions. Value can
be:

**•** `and` —Evaluates to `true` only if all its
conditions evaluate to `true`

**•** `or` —Evaluates to `true` if any of its
conditions evaluate to `true`

**•** Advanced logic like `1 AND (2 OR`
`3)` —Evaluates to `true` if the first
condition is `true` and either the
second or third condition is `true`

When you use advanced logic, the
string must consist of 1,000 or fewer
characters.

`associatedElement` string

The API name of the event that resumes the
flow. This field is available in API version 60.0
and later.

`conditions` FlowCondition[] An array of conditions that must be `true`
for the flow to wait for this event.


Metadata Types Flow

**Field Name** **Field Type** **Description**

`automationEventName` string Name of the automation event that the Wait
element is waiting for.

`automationEventType` InvocableActionType (enumeration of type
string)

The type of the automation event that
triggers the Wait element is waiting for.
Valid values are:

**•** `exploreConversation` —This
value is available in API version 61.0 and
later.

**•** `trgrOnCustomEvent` —This value
is available in API version 64.0 and later.

**•** `trgrOnSmsSubscription`

**•** `trgrOnEmailSubscription`

**•** `trgrOnOrderPlacement`

**•** `trgrOnFormSubmission`

`connector` FlowConnector Specifies which node to execute if this event
is the first event that occurs.

`eventType` string Required. The event’s type. The type
determines which input parameters are

available to define this event. Valid values
are:

**•** `AlarmEvent` —This event is an alarm
based off an absolute date/time value.

**•** `DateRefAlarmEvent` —This event
is an alarm based off a date/time field
on a record.

`extendUntil` Time Reserved for future use.

`filters` FlowRecordFilter[] An array of filters to apply when retrieving
records from the database. For example,

filter accounts to include only the records
that haven’t been updated in the last 4
weeks. This field is available in API version
60.0 and later.

`filterlogic` string The filter logic that’s applied to the filter
condition requirements. To require all

conditions, use AND. To require any
conditions, use OR. For custom condition
logic, enter the entire logic string, for
example 1 AND 2 OR (3 AND 4). This field is
available in API version 60.0 and later.


Metadata Types Flow

**Field Name** **Field Type** **Description**

`inputParameters` FlowWaitEventInputParameter[]

An array of the event’s input parameters.
The parameter values are set by using values
from the flow.

`interactionType` FlowWaitInteractionType (enumeration of Specifies what type of event can resume the
type string) flow. Possible values are:

**•** `SmsResponse` —An SMS response
event

**•** `WhatsappResponse` —A WhatsApp
response event

This field is available in API version 62.0 and
later.

`label` string Required. Label for the wait event.

`object` string

The object that contains the event you want
to use to resume the flow. This field is
available in API version 60.0 and later.

`offset` int Reserved for future use.

`offsetUnit` FlowScheduledPathOffsetUnit (enumeration Reserved for future use.
of type string)

`outputParameters` FlowWaitEventOutputParameter[]

An array of the event’s output parameters.
The parameter values are assigned from the
event to variables in the flow.

`recordTriggerType` RecordTriggerType Specifies what type of record changes can
resume the flow. Possible values are:

**•** `Create` —When a related record is
created

**•** `Update` —When a related record is
updated

**•** `CreateAndUpdate` —When a
related record is created and updated

This field is available in API version 60.0 and
later.

FlowWaitEventInputParameter

An input parameter for FlowWaitEvent. The parameter’s value is set by using values from the flow. It extends FlowBaseElement and
inherits all its fields. FlowWaitEventInputParameter is available in API version 32.0 and later.

**Field Name** **Field Type** **Description**

`name` string Unique name for the input parameter.


Metadata Types Flow

**Field Name** **Field Type** **Description**

`value` FlowElementReferenceOrValue Defines the value of the input parameter.

FlowWaitEventOutputParameter

An output parameter for FlowWaitEvent. The parameter’s value is assigned to a variable in the flow so that it can be referenced in another
part of the flow. It extends FlowBaseElement and inherits all its fields. FlowWaitEventOutputParameter is available in API version 32.0
and later.

**Field Name** **Field Type** **Description**

`assignToReference` string

Required. Specifies the variable to which
you want to assign the output parameter
value.

`name` string Required. Unique name for the output
parameter.

Upgrade Flow Files to API Version 44.0 or Later

In API version 43.0 and earlier, the Flow object’s fullName field included the flow’s version number. Starting in API version 44, the field
no longer includes the version number. Before you deploy using API version 44.0 via Metadata API or Salesforce CLI, make sure that:

**•** The `flows` directory doesn’t include any unused flow versions.

**•** For each active flow, the `status` field is `Active` . Any flow without a `status` value is deployed or retrieved with a `status`
value of `Draft` .

**•** The `flowDefinitions` directory is empty.

For Metadata API only.

**•** The `package.xml` file is set to API version 44.0.

**•** For the latest version of each flow, the file name doesn’t include a version number. For example, change `myflow-3.flow` to
`myflow.flow` .

For Salesforce CLI only.

**•** The `sfdx-project.json` file is set to `"sourceApiVersion": "44.0"` .

**•** For the latest version of each flow, the file name doesn’t include a version number. For example, change
`myflow-1.flow-meta.xml` to `myflow.flow-meta.xml` .

As part of this upgrade, flow definitions are no longer necessary when you deploy or retrieve via Metadata API. If you deploy with flow
definitions, the active version numbers in the flow definitions override the **status** fields in the flows. For example, the active version
number in the flow definition is version 3, and the latest version of the flow is version 4 with the **status** field as `Active` . After you
deploy your flow, the active version is version 3.

After you finished this upgrade, you can integrate with a version control system without worrying about flow file names changing. To
reduce deployment issues when you push the source code into a scratch org, make sure that you don’t reuse an existing scratch org.

[For more information, see Deploy Processes and Flows as Active in](https://help.salesforce.com/s/articleView?id=platform.flow_distribute_deploy_active.htm&type=5&language=en_US) _Salesforce Help_ .


Metadata Types Flow

Declarative Metadata Sample Definition

Here’s a sample XML definition of a flow.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Flow xmlns="http://soap.sforce.com/2006/04/metadata">

      <actionCalls>

        <name>Get_Info</name>

        <label>Get Info</label>

        <locationX>380</locationX>

        <locationY>242</locationY>

        <actionName>GetFirstFromCollection</actionName>

        <actionType>apex</actionType>

        <connector>

           <targetReference>Update_If_Existing</targetReference>

        </connector>

        <dataTypeMappings>

           <typeName>T__inputCollection</typeName>

           <typeValue>Account</typeValue>

        </dataTypeMappings>

        <dataTypeMappings>

           <typeName>U__outputMember</typeName>

           <typeValue>Account</typeValue>

        </dataTypeMappings>

        <flowTransactionModel>CurrentTransaction</flowTransactionModel>

        <inputParameters>

           <name>inputCollection</name>

           <value>

             <elementReference>accts.accounts</elementReference>

           </value>

        </inputParameters>

        <nameSegment>GetFirstFromCollection</nameSegment>

        <storeOutputAutomatically>true</storeOutputAutomatically>

        <versionSegment>1</versionSegment>

      </actionCalls>

      <actionCalls>

        <name>Post_to_Contact_s_Feed</name>

        <label>Post to Contact&apos;s Feed</label>

        <locationX>50</locationX>

        <locationY>890</locationY>

        <actionName>chatterPost</actionName>

        <actionType>chatterPost</actionType>

        <connector>

           <targetReference>Confirm</targetReference>

        </connector>

        <flowTransactionModel>CurrentTransaction</flowTransactionModel>

        <inputParameters>

           <name>text</name>

           <value>

             <elementReference>chatterMessage</elementReference>

           </value>

        </inputParameters>

        <inputParameters>

           <name>subjectNameOrId</name>

           <value>

```


Metadata Types Flow

```
             <elementReference>contact.Id</elementReference>

           </value>

        </inputParameters>

        <nameSegment>chatterPost</nameSegment>

        <storeOutputAutomatically>true</storeOutputAutomatically>

        <versionSegment>1</versionSegment>

      </actionCalls>

      <apiVersion>49.0</apiVersion>

      <assignments>

        <name>Set_Contact_ID</name>

        <label>Set Contact ID</label>

        <locationX>50</locationX>

        <locationY>674</locationY>

        <assignmentItems>

           <assignToReference>contact.Id</assignToReference>

           <operator>Assign</operator>

           <value>

             <elementReference>existingId</elementReference>

           </value>

        </assignmentItems>

        <connector>

           <targetReference>Update_Contact</targetReference>

        </connector>

      </assignments>

      <decisions>

        <name>Update_If_Existing</name>

        <label>Update If Existing?</label>

        <locationX>380</locationX>

        <locationY>350</locationY>

        <defaultConnector>

           <isGoTo>true</isGoTo>

           <targetReference>Create_Contact</targetReference>

        </defaultConnector>

        <defaultConnectorLabel>No</defaultConnectorLabel>

        <rules>

           <name>Update_Yes</name>

           <conditionLogic>and</conditionLogic>

           <conditions>

             <leftValueReference>updateExisting</leftValueReference>

             <operator>EqualTo</operator>

             <rightValue>

               <booleanValue>true</booleanValue>

             </rightValue>

           </conditions>

           <connector>

             <targetReference>Find_a_Match</targetReference>

           </connector>

           <label>Yes</label>

        </rules>

      </decisions>

      <decisions>

        <name>Update_or_Create</name>

        <label>Update or Create?</label>

        <locationX>182</locationX>

```


Metadata Types Flow

```
        <locationY>566</locationY>

        <defaultConnector>

           <targetReference>Create_Contact</targetReference>

        </defaultConnector>

        <defaultConnectorLabel>Create New</defaultConnectorLabel>

        <rules>

           <name>Update_Existing</name>

           <conditionLogic>and</conditionLogic>

           <conditions>

             <leftValueReference>existingId</leftValueReference>

             <operator>IsNull</operator>

             <rightValue>

               <booleanValue>false</booleanValue>

             </rightValue>

           </conditions>

           <connector>

             <targetReference>Set_Contact_ID</targetReference>

           </connector>

           <label>Update Existing</label>

        </rules>

      </decisions>

      <dynamicChoiceSets>

        <name>accounts</name>

        <dataType>String</dataType>

        <displayField>Name</displayField>

        <object>Account</object>

        <outputAssignments>

           <assignToReference>contact.AccountId</assignToReference>

           <field>Id</field>

        </outputAssignments>

        <valueField>Id</valueField>

      </dynamicChoiceSets>

      <environments>Default</environments>

      <formulas>

        <name>created_or_updated</name>

        <dataType>String</dataType>

        <expression>IF({!Create_Contact}, &quot;created&quot;,

   &quot;updated&quot;)</expression>

      </formulas>

      <interviewLabel>New Contact {!$Flow.CurrentDateTime}</interviewLabel>

      <isAdditionalPermissionRequiredToRun>true</isAdditionalPermissionRequiredToRun>

      <isTemplate>true</isTemplate>

      <label>New Contact</label>

      <processMetadataValues>

        <name>BuilderType</name>

        <value>

           <stringValue>LightningFlowBuilder</stringValue>

        </value>

      </processMetadataValues>

      <processMetadataValues>

        <name>CanvasMode</name>

        <value>

           <stringValue>AUTO_LAYOUT_CANVAS</stringValue>

        </value>

```


Metadata Types Flow

```
      </processMetadataValues>

      <processMetadataValues>

        <name>OriginBuilderType</name>

        <value>

           <stringValue>LightningFlowBuilder</stringValue>

        </value>

      </processMetadataValues>

      <processType>Flow</processType>

      <recordCreates>

        <name>Create_Contact</name>

        <label>Create Contact</label>

        <locationX>314</locationX>

        <locationY>674</locationY>

        <connector>

           <isGoTo>true</isGoTo>

           <targetReference>Post_to_Contact_s_Feed</targetReference>

        </connector>

        <inputReference>contact</inputReference>

      </recordCreates>

      <recordLookups>

        <name>Find_a_Match</name>

        <label>Find a Match</label>

        <locationX>182</locationX>

        <locationY>458</locationY>

        <assignNullValuesIfNoRecordsFound>true</assignNullValuesIfNoRecordsFound>

        <connector>

           <targetReference>Update_or_Create</targetReference>

        </connector>

        <filterLogic>and</filterLogic>

        <filters>

           <field>FirstName</field>

           <operator>EqualTo</operator>

           <value>

             <elementReference>contact.FirstName</elementReference>

           </value>

        </filters>

        <filters>

           <field>LastName</field>

           <operator>EqualTo</operator>

           <value>

             <elementReference>contact.LastName</elementReference>

           </value>

        </filters>

        <object>Contact</object>

        <outputAssignments>

           <assignToReference>existingId</assignToReference>

           <field>Id</field>

        </outputAssignments>

      </recordLookups>

      <recordUpdates>

        <name>Update_Contact</name>

        <label>Update Contact</label>

        <locationX>50</locationX>

        <locationY>782</locationY>

```


Metadata Types Flow

```
        <connector>

           <targetReference>Post_to_Contact_s_Feed</targetReference>

        </connector>

        <inputReference>contact</inputReference>

      </recordUpdates>

      <screens>

        <name>Confirm</name>

        <label>Confirm</label>

        <locationX>50</locationX>

        <locationY>998</locationY>

        <allowBack>false</allowBack>

        <allowFinish>true</allowFinish>

        <allowPause>true</allowPause>

        <fields>

           <name>confirmation_message</name>

         <fieldText>Thanks! &lt;a href=&quot;/{!contact.Id}&quot;&gt;The contact&lt;/a&gt;

    was {!created_or_updated}.</fieldText>

           <fieldType>DisplayText</fieldType>

        </fields>

        <showFooter>true</showFooter>

        <showHeader>true</showHeader>

      </screens>

      <screens>

        <name>Contact_Info</name>

        <label>Contact Info</label>

        <locationX>380</locationX>

        <locationY>134</locationY>

        <allowBack>true</allowBack>

        <allowFinish>true</allowFinish>

        <allowPause>true</allowPause>

        <connector>

           <targetReference>Get_Info</targetReference>

        </connector>

        <fields>

           <name>contactName</name>

           <extensionName>flowruntime:name</extensionName>

           <fieldType>ComponentInstance</fieldType>

           <inputsOnNextNavToAssocScrn>UseStoredValues</inputsOnNextNavToAssocScrn>

           <isRequired>true</isRequired>

           <outputParameters>

             <assignToReference>contact.FirstName</assignToReference>

             <name>firstName</name>

           </outputParameters>

           <outputParameters>

             <assignToReference>contact.LastName</assignToReference>

             <name>lastName</name>

           </outputParameters>

        </fields>

        <fields>

           <name>Account</name>

           <choiceReferences>accounts</choiceReferences>

           <dataType>String</dataType>

           <fieldText>Account</fieldText>

           <fieldType>DropdownBox</fieldType>

```


Metadata Types Flow

```
           <isRequired>true</isRequired>

        </fields>

        <fields>

           <name>update_toggle</name>

           <extensionName>flowruntime:toggle</extensionName>

           <fieldType>ComponentInstance</fieldType>

           <inputParameters>

             <name>label</name>

             <value>

               <stringValue>If this contact already exists, update the existing

   record.</stringValue>

             </value>

           </inputParameters>

           <inputParameters>

             <name>messageToggleActive</name>

             <value>

               <stringValue>Update existing</stringValue>

             </value>

           </inputParameters>

           <inputParameters>

             <name>messageToggleInactive</name>

             <value>

               <stringValue>Create other contact</stringValue>

             </value>

           </inputParameters>

           <inputsOnNextNavToAssocScrn>UseStoredValues</inputsOnNextNavToAssocScrn>

           <isRequired>true</isRequired>

           <outputParameters>

             <assignToReference>updateExisting</assignToReference>

             <name>value</name>

           </outputParameters>

        </fields>

        <showFooter>true</showFooter>

        <showHeader>true</showHeader>

      </screens>

      <start>

        <locationX>254</locationX>

        <locationY>0</locationY>

        <connector>

           <targetReference>Contact_Info</targetReference>

        </connector>

      </start>

      <status>Draft</status>

      <textTemplates>

        <name>chatterMessage</name>

        <isViewedAsPlainText>false</isViewedAsPlainText>

        <text>The contact was {!created_or_updated}.</text>

      </textTemplates>

      <variables>

        <name>accts</name>

        <apexClass>ComplexObjectExample</apexClass>

        <dataType>Apex</dataType>

        <isCollection>false</isCollection>

        <isInput>false</isInput>

```


Metadata Types Flow

```
        <isOutput>false</isOutput>

      </variables>

      <variables>

        <name>contact</name>

        <dataType>SObject</dataType>

        <isCollection>false</isCollection>

        <isInput>false</isInput>

        <isOutput>false</isOutput>

        <objectType>Contact</objectType>

      </variables>

      <variables>

        <name>existingId</name>

        <dataType>String</dataType>

        <isCollection>false</isCollection>

        <isInput>false</isInput>

        <isOutput>false</isOutput>

      </variables>

      <variables>

        <name>updateExisting</name>

        <dataType>Boolean</dataType>

        <isCollection>false</isCollection>

        <isInput>false</isInput>

        <isOutput>false</isOutput>

      </variables>

   </Flow>

```

Sample XML definition with a subflow element.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Flow xmlns="http://soap.sforce.com/2006/04/metadata">

      <apiVersion>65.0</apiVersion>

      <areMetricsLoggedToDataCloud>false</areMetricsLoggedToDataCloud>

      <assignments>

        <name>Assign_Value</name>

        <label>Assign Value</label>

        <locationX>0</locationX>

        <locationY>0</locationY>

        <assignmentItems>

           <assignToReference>Counter_Value</assignToReference>

           <operator>Assign</operator>

        </assignmentItems>

      </assignments>

      <customProperties>

        <name>ScreenProgressIndicator</name>

        <value>

   <stringValue>{&quot;location&quot;:&quot;top&quot;,&quot;type&quot;:&quot;simple&quot;}</stringValue>

        </value>

      </customProperties>

      <environments>Default</environments>

      <interviewLabel>Sample Definition Screen 1 {!$Flow.CurrentDateTime}</interviewLabel>

      <label>Sample Definition Screen 1</label>

      <processMetadataValues>

        <name>BuilderType</name>

```


Metadata Types Flow

```
        <value>

           <stringValue>LightningFlowBuilder</stringValue>

        </value>

      </processMetadataValues>

      <processMetadataValues>

        <name>CanvasMode</name>

        <value>

           <stringValue>AUTO_LAYOUT_CANVAS</stringValue>

        </value>

      </processMetadataValues>

      <processMetadataValues>

        <name>OriginBuilderType</name>

        <value>

           <stringValue>LightningFlowBuilder</stringValue>

        </value>

      </processMetadataValues>

      <processType>Flow</processType>

      <start>

        <locationX>0</locationX>

        <locationY>0</locationY>

        <connector>

           <targetReference>Call_My_Subflow</targetReference>

        </connector>

      </start>

      <status>Draft</status>

      <subflows>

        <name>Call_My_Subflow</name>

        <label>Call My Subflow</label>

        <locationX>0</locationX>

        <locationY>0</locationY>

        <connector>

           <targetReference>Assign_Value</targetReference>

        </connector>

        <flowName>Sample_Definition_Autolaunched</flowName>

        <inputAssignments>

           <name>Counter</name>

        </inputAssignments>

        <inputAssignments>

           <name>Counter_Value2</name>

        </inputAssignments>

      </subflows>

      <variables>

        <name>Counter_Value</name>

        <dataType>Number</dataType>

        <isCollection>false</isCollection>

        <isInput>true</isInput>

        <isOutput>true</isOutput>

        <scale>0</scale>

        <value>

           <numberValue>1.0</numberValue>

        </value>

      </variables>

   </Flow>

```


Metadata Types Flow

Sample XML definition of an autolaunched flow with a loop.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Flow xmlns="http://soap.sforce.com/2006/04/metadata">

      <apiVersion>65.0</apiVersion>

      <areMetricsLoggedToDataCloud>false</areMetricsLoggedToDataCloud>

      <assignments>

        <name>Assign_Counter</name>

        <label>Assign Counter</label>

        <locationX>0</locationX>

        <locationY>0</locationY>

        <assignmentItems>

           <assignToReference>Counter</assignToReference>

           <operator>Add</operator>

           <value>

             <numberValue>1.0</numberValue>

           </value>

        </assignmentItems>

        <assignmentItems>

           <assignToReference>Loop_Accounts.NumberOfEmployees</assignToReference>

           <operator>Add</operator>

           <value>

             <elementReference>Counter</elementReference>

           </value>

        </assignmentItems>

        <connector>

           <targetReference>Loop_Accounts</targetReference>

        </connector>

      </assignments>

      <environments>Default</environments>

     <interviewLabel>Sample Definition Autolaunched {!$Flow.CurrentDateTime}</interviewLabel>

      <label>Sample Definition Autolaunched</label>

      <loops>

        <name>Loop_Accounts</name>

        <label>Loop Accounts</label>

        <locationX>0</locationX>

        <locationY>0</locationY>

        <collectionReference>Get_Accounts</collectionReference>

        <iterationOrder>Asc</iterationOrder>

        <nextValueConnector>

           <targetReference>Assign_Counter</targetReference>

        </nextValueConnector>

      </loops>

      <processMetadataValues>

        <name>BuilderType</name>

        <value>

           <stringValue>LightningFlowBuilder</stringValue>

        </value>

      </processMetadataValues>

      <processMetadataValues>

        <name>CanvasMode</name>

        <value>

           <stringValue>AUTO_LAYOUT_CANVAS</stringValue>

        </value>

```


Metadata Types Flow

```
      </processMetadataValues>

      <processMetadataValues>

        <name>OriginBuilderType</name>

        <value>

           <stringValue>LightningFlowBuilder</stringValue>

        </value>

      </processMetadataValues>

      <processType>AutoLaunchedFlow</processType>

      <recordLookups>

        <name>Get_Accounts</name>

        <label>Get Accounts</label>

        <locationX>0</locationX>

        <locationY>0</locationY>

        <assignNullValuesIfNoRecordsFound>false</assignNullValuesIfNoRecordsFound>

        <connector>

           <targetReference>Loop_Accounts</targetReference>

        </connector>

        <getFirstRecordOnly>false</getFirstRecordOnly>

        <limit>

           <numberValue>10.0</numberValue>

        </limit>

        <object>Account</object>

        <storeOutputAutomatically>true</storeOutputAutomatically>

      </recordLookups>

      <runInMode>SystemModeWithoutSharing</runInMode>

      <start>

        <locationX>0</locationX>

        <locationY>0</locationY>

        <connector>

           <targetReference>Get_Accounts</targetReference>

        </connector>

      </start>

      <status>Draft</status>

      <variables>

        <name>AccountCollection</name>

        <dataType>SObject</dataType>

        <isCollection>true</isCollection>

        <isInput>false</isInput>

        <isOutput>false</isOutput>

        <objectType>Account</objectType>

      </variables>

      <variables>

        <name>Counter</name>

        <dataType>Number</dataType>

        <isCollection>false</isCollection>

        <isInput>false</isInput>

        <isOutput>false</isOutput>

        <scale>0</scale>

      </variables>

   </Flow>

```


### Metadata Types FlowCategory

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

_Salesforce Help_ [: Deploy Processes and Flows as Active](https://help.salesforce.com/s/articleView?id=platform.flow_distribute_deploy_active.htm&type=5&language=en_US)

### FlowCategory

Represents a list of flows that are grouped by category. Flows aren’t added directly to a Lightning Bolt Solution. Instead, add the category
the flows are in to the Lightning Bolt Solution. This type extends the Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### FlowCategory components have the suffix .flowCategory and are stored in the flowCategories folder.

Version

### FlowCategory components are available in API version 43.0 and later.

Fields

**Field Name** **Field Type** **Description**

`description` string The description of this flow category.

### flowCategoryItems FlowCategoryItems[] The list of flows in this flow category.

`masterLabel` string Required. The label for this flow category, which appears in Setup.

### FlowCategoryItems

Represents the list of flows in a flow category.

**Field Name** **Field Type** **Description**

`flow` string Required. The name of the flow.


### Metadata Types FlowDefinition

Declarative Metadata Sample Definition

The following is an example of a FlowCategory component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <FlowCategory xmlns="http://soap.sforce.com/2006/04/metadata"

   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

      <flowCategoryItems>

        <flow>PausableFlow</flow>

      </flowCategoryItems>

      <flowCategoryItems>

        <flow>BankingFlow</flow>

      </flowCategoryItems>

      <masterLabel>updateBenefits</masterLabel>

        <description>All the update benefits.</description>

   </FlowCategory>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>updateBenefits</members>

        <name>FlowCategory</name>

      </types>

      <version>43.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### FlowDefinition

Represents the flow definition’s description and active flow version number.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Important: In API version 44.0, we recommend upgrading your flows to flow metadata file names without version numbers and
discontinue using the FlowDefinition object to activate or deactivate a flow. Then use the Flow object to activate or deactivate a
flow. For more information, see Upgrade Flow Files to API Version 44.0.

If you deploy with flow definitions, the active version numbers in the flow definitions override the `status` fields in the flows. For
example, the active version number in the flow definition is version 3, and the latest version of the flow is version 4 with the `status`
field as `Active` . After you deploy your flow, the active version is version 3.

Declarative Metadata File Suffix and Directory Location

### FlowDefinitions are stored in the flowDefinitions directory of the corresponding package directory. The file name matches the

flow definition's unique full name, and the extension is `.flowDefinition` .


### Metadata Types FlowTest

Version

FlowDefinition is available in API version 34.0 and later.

**Field Name** **Field Type** **Description**

`activeVersionNumber` int The version number of the active flow.

`apiVersion` int Reserved for internal use.

`description` string Description of the flow definition.

`masterLabel` string

Wildcard Support in the Manifest File

Label for the flow definition. In managed packages, this field inherits
the flow’s active version name. To change this label from a
subscriber’s org, edit the packaged flow name.

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### FlowTest

Represents the metadata associated with a flow test. Before you activate a record-triggered flow, you can test it to verify its expected
results and identify flow run-time failures.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### FlowTest components have the suffix .flowtest, and Salesforce stores them in the flowtests folder.

Version

### FlowTest components are available in API version 55.0 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.


Metadata Types FlowTest

Fields

**Field Name** **Description**

```
description

flowApiName

```

**Field Type**
string

**Description**
The description of the flow test, such as what it does or how it works.

**Field Type**
string

**Description**

Required.

The API name of the flow associated with the flow test.

`flowTestDataSources` Reserved for future use.

```
flowTestFlowVersions

```

**Field Type**

FlowTestFlowVersion[]

**Description**
An array of flow versions that are associated with the flow test. This field is available
in API version 66.0 and later.

`isolatedObjectExternalKeys` Reserved for future use.

```
label

testPoints

testType

```

**Field Type**
string

**Description**

Required.

The label of the flow test.

**Field Type**

FlowTestPoint[]

**Description**
An array of test points for the test.

**Field Type**
FlowTestType (enumeration of type string)

**Description**

Required.

Specifies whether the test contains assertions. This field is available in API version 66.0
and later.

Possible values are:


Metadata Types FlowTest

**Field Name** **Description**

**•** `WithAssertion` —The automated comparison of the actual flow outcome
with the user-defined expected outcome that assertions define.

FlowTestFlowVersion

Defines the flow version for the flow test. This subtype is available in API version 66.0 and later.

**Field Name** **Description**

```
flowVersionNumber

```

FlowTestPoint

**Field Type**
string

**Description**
The version number of the flow version that’s associated with the flow test.

Defines a flow test point that Salesforce evaluates when a flow test runs. Salesforce evaluates each test point in the order that it’s listed.

**Field Name** **Description**

```
assertions

elementApiName

```

**Field Type**

FlowTestAssertion[]

**Description**
An array of assertions for the test.

**Field Type**
string

**Description**

Required.

The element API names for the start of the flow and the end of the flow.

Possible values are:

**•** `Start`

**•** `Finish`

`isUseMockOuput` Reserved for future use.

```
parameters

```

**Field Type**

FlowTestParameter[]

**Description**
An array of parameters for the test.


Metadata Types FlowTest

FlowTestAssertion

Defines an assertion for a test point that Salesforce evaluates when a flow test runs. If one assertion evaluates to false, the test run fails.

**Field Name** **Description**

```
conditions

errorMessage

```

FlowTestCondition

**Field Type**

FlowTestCondition[]

**Description**
An array of conditions for an assertion.

**Field Type**
string

**Description**
If the associated condition evaluates to false, this custom message appears in Flow
Builder.

Defines a condition for an assertion that Salesforce evaluates when a flow test runs. If one condition evaluates to false, the assertion fails.

**Field Name** **Description**

```
leftValueReference

operator

```

**Field Type**
string

**Description**

Required.

The reference to the flow resource that the specified operator applies to.

**Field Type**
FlowComparisonOperator (enumeration of type string)

**Description**

Required.

The flow test uses this value to evaluate the resource reference in the
`leftValueReference` field.

Possible values are:

**•** `Contains`

**•** `EndsWith`

**•** `EqualTo`

**•** `GreaterThan`

**•** `GreaterThanOrEqualTo`

**•** `HasError` —This value is available in API version 64.0 and later.

**•** `In` —This value is available in API version 56.0 and later.


Metadata Types FlowTest

**Field Name** **Description**

**•** `IsBlank` —This value is available in API version 61.0 and later.

**•** `IsChanged`

**•** `IsEmpty` —This value is available in API version 61.0 and later.

**•** `IsNull`

**•** `LessThan`

**•** `LessThanOrEqualTo`

**•** `NotEqualTo`

**•** `NotIn` —This value is available in API version 56.0 and later.

**•** `StartsWith`

**•** `WasSelected`

**•** `WasSet`

**•** `WasVisited`

```
rightValue

```

**Field Type**

FlowTestReferenceOrValue on page 1318

**Description**
The value that the operator applies to the resource reference in the
`leftValueReference` field.

FlowTestReferenceOrValue

Defines a specific value that the operator applies to the resource reference in flow test assertions and conditions.

**Field Name** **Description**

```
booleanValue

dateTimeValue

dateValue

```

**Field Type**
boolean

**Description**
Specifies a boolean value.

**Field Type**
dateTime

**Description**
Specifies a dateTime value.

**Field Type**
date

**Description**
Specifies a dateValue value.

`elementReference` Reserved for future use.


Metadata Types FlowTest

**Field Name** **Description**

`jsonValue` Reserved for future use.

```
numberValue

sobjectValue

stringValue

timeValue

```

FlowTestParameter

**Field Type**
double

**Description**
Specifies a number value.

**Field Type**
string

**Description**
Specifies an sObject value.

**Field Type**
string

**Description**
Specifies a string value.

**Field Type**
time

**Description**
Specifies a time value.

Defines parameters for the triggering record in the Start test point.

**Field Name** **Description**

```
leftValueReference

type

```

**Field Type**
string

**Description**

Required.

The name of the parameter. When `type` is
`InputTriggeringRecordInitial` or
`InputTriggeringRecordUpdated`, the value for `leftValueReference`
must be `$Record` . When `type` is `ScheduledPath`, the value for
`leftValueReference` must be `ScheduledPathApiName` .

**Field Type**
FlowTestParameterType (enumeration of type string)

**Description**

Required.


Metadata Types FlowTest

**Field Name** **Description**

The type of parameter.

Possible values are:

**•** `InputTriggeringRecordInitial`

**•** `InputTriggeringRecordUpdated`

**•** `InputVariable` —Reserved for future use.

**•** `ScheduledPath` —Available in API version 56.0 and later.

```
value

```

**Field Type**

FlowTestReferenceOrValue

**Description**

Required.

The value that the operator applies to the resource reference in the
`leftValueReference` field.

Declarative Metadata Sample Definition

The following is an example of a FlowTest component.

```
<?xml version="1.0" encoding="UTF-8"?>

<FlowTest xmlns="http://soap.sforce.com/2006/04/metadata">

   <flowApiName>Example_Test</flowApiName>

   <label>Test Two</label>

   <testPoints>

     <elementApiName>Start</elementApiName>

     <parameters>

        <leftValueReference>$Record</leftValueReference>

        <type>InputTriggeringRecordInitial</type>

        <value>

<sobjectValue>{&quot;AnnualRevenue&quot;:100000,&quot;BillingCity&quot;:&quot;New

York&quot;}}</sobjectValue>

        </value>

     </parameters>

     <parameters>

        <leftValueReference>ScheduledPathApiName</leftValueReference>

        <type>ScheduledPath</type>

        <value>Every_Monday</value>

     </parameters>

     <parameters>

        <leftValueReference>$Record</leftValueReference>

        <type>InputTriggeringRecordUpdated</type>

        <value>

<sobjectValue>{&quot;AnnualRevenue&quot;:100000,&quot;BillingCity&quot;:&quot;New

York&quot;}</sobjectValue>

        </value>

```


### Metadata Types FlowValueMap

```
        </parameters>

      </testPoints>

      <testPoints>

        <assertions>

           <conditions>

             <leftValueReference>$Record.Industry</leftValueReference>

             <operator>EqualTo</operator>

             <rightValue>

               <stringValue>Other</stringValue>

             </rightValue>

           </conditions>

           <errorMessage>Industry was not set.</errorMessage>

        </assertions>

        <elementApiName>Finish</elementApiName>

      </testPoints>

   </FlowTest>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

   <members>Test_Two</members>

   <name>FlowTest</name>

   </types>

   <version>55.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### FlowValueMap

Reserved for future use.

### Folder

Represents a folder. This type extends the Metadata metadata type and inherits its `fullName` field.

Five folder types currently exist in Salesforce:

**•** Document folder

**•** Email folder (available for Salesforce Classic email templates only)

**•** Email Template folder

**•** Report folder

**•** Dashboard folder

### Folder type names end with the “Folder” suffix. For example, the type name of a document folder is “DocumentFolder”.


Metadata Types Folder

File Suffix and Directory Location

Folders are stored in the corresponding component directory of the package. These directories are named `documents`, `email`,
`emailTemplates`, `reports`, and `dashboards` . Folders don’t have a text file representation—they’re containers for files. For
each folder, an accompanying metadata file named _`FolderName.folderType`_ `-meta.xml` is created at the same directory
level. The _`FolderName.folderType`_ `-meta.xml` metadata file contains the metadata information for that folder, such as the
`accessType` . For example, for a documents folder named sampleFolder, there’s a
_`sampleFolder.documentFolder-meta.xml`_ within the `documents` folder of the package.

Deploying or Retrieving Nested Folders

To deploy or retrieve only a nested folder component, and not its contents, you must use a specific syntax in your `package.xml` . To
reference the nested folder itself, append a trailing slash (/) to its full name in the `<members>` tag.

For example, to retrieve a nested `DocumentFolder` named `MyNestedFolder` located inside `MyTopFolder`, your
`package.xml` must list the member with a trailing slash (/).

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>MyTopFolder/MyNestedFolder/</members>

        <name>DocumentFolder</name>

      </types>

      <version>58.0</version>

   </Package>

```

If you omit the trailing slash (for example, `<members>MyTopFolder/MyNestedFolder</members>` ), the operation fails.
The API incorrectly searches for a `Document` component named `MyNestedFolder` instead of the folder.

This syntax applies to all folder types. For `ReportFolder`, you must use the `Report` type in the manifest. For Lightning Email
Template folders, use the `EmailTemplateFolder` type.

Version

Folders are available in API version 11.0 and later.

Fields

This metadata type contains the following fields:

**Field Name** **Field Type** **Description**

```
accessType

```

FolderAccessTypes Required. The type of access for this folder. Valid values are:
(enumeration of

**•** `Shared` . This folder is accessible only by the specified set of users.

type string)

**•** `Public` . This folder is accessible by all users, including portal users.

**•** `PublicInternal` . This folder is accessible by all users, excluding
portal users. This setting is available for report and dashboard folders
in organizations with a partner portal or Customer Portal enabled.

**•** `Hidden` . This folder is hidden from all users.


Metadata Types Folder

**Field Name** **Field Type** **Description**

`fullName` string The name used as a unique identifier for API access. The `fullName`
can contain only underscores and alphanumeric characters. It must be

unique, begin with a letter, not include spaces, not end with an
underscore, and not contain two consecutive underscores. This field is
inherited from the Metadata component.

`name` string Required. The name of the document folder.

```
publicFolderAccess

```

PublicFolderAccess If `Public` is the value for `accessType`, this field indicates the type
(enumeration of of access all users have to the contents of the folder. Valid values include:
type string)

**•** `ReadOnly` . All users can read the contents of the folder, but no
user can change the contents.

**•** `ReadWrite` . All users can read or change the contents of the
folder.

`sharedTo` SharedTo [Sharing access for the folder. See Sharing Considerations in Salesforce](https://help.salesforce.com/s/articleView?id=platform.security_sharing_considerations.htm&type=5&language=en_US)
Help.

Declarative Metadata Sample Definition

The following is the package manifest definition of a document folder that contains a document:

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <fullName>basic</fullName>

   <types>

     <members>sampleFolder</members>

     <members>sampleFolder/TestDocument.txt</members>

     <name>Document</name>

   </types>

   <version>66.0</version>

</Package>

```

The following is an example of the `sampleFolder-meta.xml` metadata file for the sampleFolder document folder:

```
<?xml version="1.0" encoding="UTF-8"?>

<DocumentFolder xmlns="http://soap.sforce.com/2006/04/metadata">

   <accessType>Public</accessType>

   <name>sampleFolder</name>

   <publicFolderAccess>ReadWrite</publicFolderAccess>

</DocumentFolder>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.


#### Metadata Types FolderShare 1. FolderShare

Represents the settings for enhanced analytics folder sharing. Users can control access to reports or dashboards by giving others
Viewer, Editor, or Manager access to the folder that contains the report or dashboard.

SEE ALSO:

Dashboard

Document

EmailTemplate

Report

#### FolderShare

Represents the settings for enhanced analytics folder sharing. Users can control access to reports or dashboards by giving others Viewer,
Editor, or Manager access to the folder that contains the report or dashboard.

Important: During package installation, FolderShare for DashboardFolder and ReportFolder is ignored.

File Suffix and Directory Location

#### FolderShare objects are stored in the reports and dashboards directories. For each report or dashboard folder it contains, there’s

a metadata file named _`FolderName`_ `-meta.xml` . The _`FolderName`_ `-meta.xml` metadata file contains the metadata information
for that folder, such as the `accessLevel` . For example, if the `reports` directory contains a reports folder named
`myReportsFolder`, it also has a _`myReportsFolder-meta.xml`_ file at the same level as `myReportsFolder` .

Version

#### FolderShare components are available in API version 28 and later.

Fields

**Field Name** **Field Type** **Description**

#### accessLevel FolderShareAccessLevel Required. Specifies the combination of actions that can be taken on

(enumeration of type string) the folder. Valid values are:

**•** `View` . User can run a report or refresh a dashboard, but can’t edit
them. All users have at least Viewer access to report and dashboard
folders that have been shared with them. (Some users can have
administrative permissions that give them greater access.)

**•** `EditAllContents` . Users can view and modify the reports or
dashboards in the folder, and move them to and from any other
folders that they have equivalent access to.

**•** `Manage` . Users can do everything Viewers and Editors can do,
plus control other users’ access to a folder.

`sharedTo` string Required. Specifies the user, group, or role that has the specified access
level to the folder.


Metadata Types FolderShare

**Field Name** **Field Type** **Description**

`sharedToType` FolderSharedToType (enumeration Required. Specifies the type of entity that the folder is shared with.
of type string) Valid values are:

**•** `Group` . Users in a specified public group have the specified access
level to the folder.

**•** `Manager` . Available in API version 29.0 and later.

**•** `ManagerAndSubordinatesInternal` . Available in API
version 29.0 and later.

**•** `Role` . Users with a specified role have the specified access level
to the folder.

**•** `RoleAndSubordinates` . Users with a specified role, and users
with a role subordinate to that role, have the specified access level
to the folder. Only available when digital experiences is enabled
for your org and Experience Cloud site users are created with
external account roles other than a shared person account role.

**•** `RoleAndSubordinatesInternal` . Users with a specified
role and users with a role subordinate to that role, except public
portal users, have the specified access level to the folder.

**•** `Organization` . All internal users have the specified access level
to the folder.

**•** `Territory` . Users in a specified territory have the specified
access level to the folder.

**•** `TerritoryAndSubordinates` . Users in a specified territory,
and users in territories subordinate to the specified territory, have
the specified access level to the folder.

**•** `AllPrmUsers` . All PRM Portal users have the specified level of
access to the folder.

**•** `User` . The specified individual user has the specified level of access
to the folder.

**•** `PartnerUser` . The specified individual user of a partner portal
has the specified level of access to the folder.

**•** `AllCspUsers` . All Customer Success Portal users have the
specified level of access to the folder.

**•** `CustomerPortalUser` . The specified individual user of a
customer portal has the specified level of access to the folder.

**•** `PortalRole` . Users with a specified role in a portal have the
specified access level to the folder.

**•** `PortalRoleAndSubordinates` . Portal users with a specified
role, and portal users with a role subordinate to that role, have the
specified access level to the folder.


### Metadata Types ForecastingFilter

Declarative Metadata Sample Definition

The following is an example of a FolderShare component for a dashboard folder:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <DashboardFolder xmlns="http://soap.sforce.com/2006/04/metadata">

     <folderShares>

        <accessLevel>View</accessLevel>

        <sharedTo>R1</sharedTo>

        <sharedToType>Role</sharedToType>

      </folderShares>

   </DashboardFolder>

```

Here’s an example of a FolderShare component for a report folder:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ReportFolder xmlns="http://soap.sforce.com/2006/04/metadata">

     <folderShares>

        <accessLevel>View</accessLevel>

        <sharedTo>R1</sharedTo>

        <sharedToType>Role</sharedToType>

      </folderShares>

   </ReportFolder>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

### ForecastingFilter

Represents the custom filter for including or excluding data from opportunity forecasts.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

### ForecastingFilter components have the suffix .forecastingFilter and are stored in the forecastingFilters folder.

Version

### ForecastingFilter components are available in API version 55.0 and later.


Metadata Types ForecastingFilter

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Description**

```
filterLogic

forecastingType

forecastingTypeSource

masterLabel

```

**Field Type**
string

**Description**
The logic that controls the evaluation of conditions. Only `AND` is supported. For example,
`1 AND 2 AND 3` .

**Field Type**
string

**Description**
Required. The ID of the forecast type. Can be linked only to forecast types created in Summer
’21 and later.

**Field Type**
string

**Description**
Required. The ID of the forecast type source. Can be linked only to forecast type sources
created in Summer ’21 or later and with a forecast source definition with source object of
'Opportunity.'

**Field Type**
string

**Description**
Required. The label for this object, which displays in Setup. The label is in the default language
locale for the organization. If there’s no default language locale, the label is in en_US.

Declarative Metadata Sample Definition

The following is an example of a ForecastingFilter component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ForecastingFilter xmlns="http://soap.sforce.com/2006/04/metadata">

   <filterLogic>1 AND 2</filterLogic>

   <forecastingType>d</forecastingType>

   <forecastingTypeSource>d7</forecastingTypeSource>

   <masterLabel>FF_OpportunityLineItem</masterLabel>

</ForecastingFilter>

```


### Metadata Types ForecastingFilterCondition

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ForecastingFilter</name>

      </types>

      <version>55.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### ForecastingFilterCondition

Represents the custom filter condition logic for including or excluding data from opportunity forecasts.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

### ForecastingFilterCondition components have the suffix .ForecastingFilterCondition and are stored in the ForecastingFilterConditions folder.

Version

### ForecastingFilterCondition components are available in API version 55.0 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Description**

```
fieldName

```

**Field Type**
string


Metadata Types ForecastingFilterCondition

**Field Name** **Description**

**Description**
Required. The name of the opportunity field to be filtered.

```
forecastingFilter

forecastingSourceDefinition

masterLabel

operation

sortOrder

value

```

**Field Type**
string

**Description**
Required. The ID of the forecast filter.

**Field Type**
string

**Description**
The ID of the forecasting source definition.

**Field Type**
string

**Description**
Required. The label for this object, which displays in Setup. The label is in the default language
locale for the organization. If there’s no default language locale, the label is in en_US.

**Field Type**
FilterOperation (enumeration of type string)

**Description**
Required. The operator in the filter condition. Possible values are:

**•** `equals`

**•** `greaterOrEqual` —greater than or equal to

**•** `greaterThan`

**•** `lessOrEqual` —less than or equal to

**•** `lessThan`

**•** `notEqual` —not equal to

**Field Type**
int

**Description**
Required. The index value for the condition. This value represents the condition in the
`FilterLogic` field on the ForecastingFilter object. For example, `1` .

**Field Type**
string

**Description**
The value of the filter condition. If multiple values are specified, they must be separated by
a comma delimiter.


### Metadata Types ForecastingSourceDefinition

**Field Name** **Description**

Note: If you have multiple currencies enabled, and add a custom filter on a currency
field as part of your forecast type definition, the corporate currency at the time the
filter was created is used. If you have a single currency enabled, the absolute value is
used in your filter condition.

Declarative Metadata Sample Definition

The following is an example of a ForecastingFilterCondition component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ForecastingFilterCondition xmlns="http://soap.sforce.com/2006/04/metadata">

      <colName>mostlikely</colName>

      <fieldName>Amount</fieldName>

      <forecastingFilter>d</forecastingFilter>

      <forecastingSourceDefinition>d7</forecastingSourceDefinition>

      <masterLabel>FFC_Opportunity</masterLabel>

      <operation>greaterThan</masterLabel>

      <sortOrder>1</masterLabel>

      <value>100000</value>

   </ForecastingFilterCondition>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ForecastingFilterCondition</name>

      </types>

      <version>55.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

Usage

A forecast type can contain up to three filter conditions.

### ForecastingSourceDefinition

Represents the object, measure, date type, and hierarchy that a forecast uses to project sales.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.


Metadata Types ForecastingSourceDefinition

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

`ForecastingSourceDefinition` components have the suffix `.forecastingSourceDefinition` and are stored in
the `forecastingSourceDefinitions` folder.

Version

ForecastingSourceDefinition components are available in API version 52.0 and later.

Fields

**Field Name** **Field Type** **Description**

`categoryField` string Name of the forecast category that is associated with the forecast type.
Possible values are:

**•** `Opportunity.ForecastCategoryName`

`dateField` string

Field that is used for the forecast type’s date type. For example, the
`CloseDate` field on Opportunity is used for opportunity close
date-based forecast types. Possible values are:

**•** `Opportunity.CloseDate`

**•** `OpportunityLineItem.ServiceDate`

**•** `OpportunityLineItemSchedule.ScheduleDate`

`familyField` string Use this field to group forecasts by product family. Possible values are:

**•** `Product2.Family`

`masterLabel` string Required. Controlling label for this forecasting source definition.

`measureField` string

Field that is used for the forecast type’s measure. For example, the
`Amount` field on Opportunity is associated with revenue-based forecast
types. Possible values are*:

**•** `Opportunity.Amount`

**•** `Opportunity.` _**`Custom`**_

**•** `Opportunity.TotalOpportunityQuantity`

**•** `OpportunityLineItem.` _**`Custom`**_

**•** `OpportunityLineItem.Quantity`

**•** `OpportunityLineItem.TotalPrice`

**•** `OpportunityLineItemSchedule.` _**`Custom`**_

**•** `OpportunityLineItemSchedule.Quantity`

**•** `OpportunityLineItemSchedule.Revenue`


Metadata Types ForecastingSourceDefinition

**Field Name** **Field Type** **Description**

**•** `OpportunitySplit.` _**`Custom`**_

**•** `OpportunitySplit.SplitAmount`

*Where _`Custom`_ represents the name of the custom field that a forecast
type’s measure is based on. Example: Use `Megawatts__c` to forecast
energy consumption.

`sourceObject` string Required. Object associated with this forecasting source definition.
Possible values are:

**•** `Opportunity`

**•** `OpportunityLineItem`

**•** `OpportunityLineItemSchedule`

**•** `OpportunitySplit`

**•** `Product2`

`territory2Field` string For a territory-based forecast type, indicates the field that is used for
territory information. Possible values are:

**•** `Opportunity.Territory2Id`

For user role-based forecast types, this value is `null` .

`userField` string Specifies who owns the forecast. Possible values are:

**•** `Opportunity.OwnerId`

**•** `OpportunitySplit.SplitOwnerId`

Declarative Metadata Sample Definition

The following is an example of a ForecastingSourceDefinition component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ForecastingSourceDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

      <masterLabel>TestFsd</masterLabel>

      <sourceObject>Opportunity</sourceObject>

      <measureField>Opportunity.Amount</measureField>

      <dateField>Opportunity.CloseDate</dateField>

      <userField>Opportunity.OwnerId</userField>

      <categoryField>Opportunity.ForecastCategoryName</categoryField>

   </ForecastingSourceDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ForecastingSourceDefinition</name>

      </types>

```


### Metadata Types ForecastingType

```
      <version>52.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

Usage

**•** Forecast types that were available before API version 52.0 can be activated, deactivated, and deleted but not created. To enable an
existing forecast type, update the active flag.

**•** Forecast types that are available only in API version 52.0 and later can be created, activated, deactivated, and deleted. If the forecast
type doesn’t exist, it is created in the inactive state. If the forecast type exists, the active flag is updated. Deploy the zip file twice to
create and activate the forecast type.

**•** Deploy Metadata API types in the following sequence: ForecastingSettings, ForecastingType, ForecastingSourceDefinition, and then
### ForecastingTypeSource. If all are specified in the package file, the sequence is followed automatically. ForecastingType

Represents a forecast type.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ForecastingType components have the suffix .forecastingType and are stored in the forecastingTypes folder.

Version

### ForecastingType components are available in API version 52.0 and later.

Fields

**Field Name** **Field Type** **Description**

`active` boolean Required. If `true`, the forecast type is active. If `false`, the forecast
type isn’t active. The default value is `false` .


Metadata Types ForecastingType

**Field Name** **Field Type** **Description**

`amount` boolean

Required. If `true`, the forecast type is based on a revenue measure. If
`false`, the forecast type is based on a quantity measure. The default
value is `true` .

`dateType` string Required. The date type that forecast amounts are based on.

**•** `OpportunityCloseDate` : Base forecasts on opportunity close
dates.

**•** `ProductDate` : Base forecasts on opportunity product line item
dates, if available.

**•** `ScheduleDate` : Base forecasts on opportunity product schedule
dates, if available.

The following values are available in API version 52.0 and later, in
Performance Edition and in Unlimited Edition with Sales Cloud.

**•** `OLIMeasureCloseDateOnly` : Base forecasts on opportunity
close dates.

**•** `ProductDateOnly` : Base forecasts on opportunity product line
item dates, if available.

**•** `ScheduleDateOnly` : Base forecasts on opportunity product
schedule dates, if available.

`developerName` string

Required. The name of the forecasting type. The `DeveloperName`
is called `name` in ForecastingSettings on page 2085 and Forecasting Type
in custom reports.

`forecastingGroupDeveloperName` string Indicates the forecast group assigned to the forecast type. Required if
`hasCustomGroup` is `true` .

`hasCustomGroup` boolean Indicates whether the forecasting type has a forecast group, based on
a custom picklist assigned. Use ForecastingGroup and

ForecastingGroupItems subtypes in ForecastingSettings to identify the
group and the values.

`hasProductFamily` boolean

Required. If `true`, the forecast type includes product families. If `false`,
the forecast type doesn’t include product families. The default value is
`false` .

`masterLabel` string Required. Controlling label for this ForecastingType value. This display
value is the internal label that doesn’t get translated.

`opportunitySplitType` string Indicates whether the forecasting type has a split type and, if so, the
name of the split type.

`opptyLineItemSplitType` string

`quantity` boolean

Indicates whether the forecasting type has an opportunity line item
(product) split type and, if so, the name of the line item split type.
Available in API version 58.0 and later.

Required. If `true`, the forecast type is based on a quantity measure. If
`false`, the forecast type is based on a revenue measure. The default
value is `false` .


Metadata Types ForecastingType

**Field Name** **Field Type** **Description**

`roleType` string

Required. Indicates whether the role type has a ForecastingType, and if
so, which ForecastingType. Possible values are `R` (user role-based forecast
type) and `Y` (Territory2-based forecast type).

`territory2Model` string Indicates whether the ForecastingType has a Territory2 model and, if so,
the name of the Territory2 model.

Declarative Metadata Sample Definition

The following is an example of a ForecastingType component using the role hierarchy.

```
<?xml version="1.0" encoding="UTF-8"?>

<ForecastingType xmlns="http://soap.sforce.com/2006/04/metadata">

   <active>false</active>

   <amount>true</amount>

   <dateType>0</dateType>

   <developerName>qqw</developerName>

   <hasProductFamily>false</hasProductFamily>

   <masterLabel>qqw</masterLabel>

   <quantity>false</quantity>

   <roleType>R</roleType>

</ForecastingType>

```

The following is an example of a ForecastingType component using the territory hierarchy.

```
<?xml version="1.0" encoding="UTF-8"?>

<ForecastingType xmlns="http://soap.sforce.com/2006/04/metadata">

   <active>false</active>

   <amount>false</amount>

   <dateType>0</dateType>

   <developerName>New_Model6</developerName>

   <hasProductFamily>false</hasProductFamily>

   <masterLabel>Opportunity Quantity by Territory</masterLabel>

   <quantity>true</quantity>

   <roleType>Y</roleType>

   <territory2Model>New_Model6</territory2Model>

</ForecastingType>

```

The following is an example of a ForecastingType component using an opportunity split type.

```
<?xml version="1.0" encoding="UTF-8"?>

<ForecastingType xmlns="http://soap.sforce.com/2006/04/metadata">

   <active>false</active>

   <amount>true</amount>

   <dateType>0</dateType>

   <developerName>split12</developerName>

   <hasProductFamily>false</hasProductFamily>

   <masterLabel>split12</masterLabel>

   <opportunitySplitType>Custom_Revenue</opportunitySplitType>

   <quantity>false</quantity>

   <roleType>R</roleType>

</ForecastingType>

```


### Metadata Types ForecastingTypeSource

The following is an example of a ForecastingType component using an opportunity line item split type.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ForecastingType xmlns="http://soap.sforce.com/2006/04/metadata">

      <active>true</active>

      <amount>true</amount>

      <dateType>0</dateType>

      <developerName>productrevenuesplit</developerName>

      <hasProductFamily>true</hasProductFamily>

      <masterLabel>productrevenuesplit</masterLabel>

      <opportunitySplitType>Revenue</opportunitySplitType>

      <opptyLineItemSplitType>Revenue</opptyLineItemSplitType>

      <quantity>false</quantity>

      <roleType>R</roleType>

   </ForecastingType>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ForecastingType</name>

      </types>

      <version>52.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

Usage

**•** Legacy forecast types that were available before API version 52.0 can be deactivated but not activated, created, or deleted.

**•** Forecast types that are available only in API version 52.0 and later can be created, activated, deactivated, and deleted. If the forecast
type doesn’t exist, it’s created in the inactive state. If the forecast type exists, the active flag is updated. Deploy the zip file twice to
create and activate the forecast type.

**•** Deploy Metadata API types in this sequence: ForecastingSettings, ForecastingType, ForecastingSourceDefinition, and then
### ForecastingTypeSource. If all are specified in the package file, the sequence is followed automatically. ForecastingTypeSource

Represents the mapping of a forecasting source definition to a forecast type.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.


Metadata Types ForecastingTypeSource

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

`ForecastingTypeSource` components have the suffix `.forecastingTypeSource` and are stored in the
`ForecastingTypeSources` folder.

Version

ForecastingTypeSource components are available in API version 52.0 and later.

Fields

**Field Name** **Field Type** **Description**

`forecastingSourceDefinition` string Required. ID of the forecasting source definition.

`forecastingType` string Required. ID of the forecast type. Can be linked only to forecast types
created in Summer ’21 and later.

`masterLabel` string Required. Controlling label for this forecasting type source.

`parentSourceDefinition` string

`relationField` string

For forecast types not based on the Opportunity object and not based
on a custom measure, this value represents the parent
ForecastingSourceDefinition of the linked ForecastingSourceDefinition.

**•** Opportunity Product is the parent of Opportunity.

**•** Opportunity Split is the parent of Opportunity.

**•** Line Item Schedule is the parent of Opportunity Product.

Represents the field that links the source objects of the parent
ForecastingSourceDefinition to the child ForecastingSourceDefinition.
Possible values are:

**•** `OpportunityLineItem.OpportunityId`

**•** `OpportunityLineItem.Product2Id`

**•** `OpportunityLineItemSchedule.OpportunityLineItemId`

**•** `OpportunitySplit.OpportunityId`

`sourceGroup` int Required. Represents a grouping of forecasting source definitions.


Metadata Types ForecastingTypeSource

Declarative Metadata Sample Definition

The following are two examples of a ForecastingTypeSource component. The first bases forecasts on the Opportunity Product object.
The second bases forecasts on the Line Item Schedule object.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ForecastingTypeSource xmlns="http://soap.sforce.com/2006/04/metadata">

      <forecastingSourceDefinition>FSD_OpportunityLineItem</forecastingSourceDefinition>

      <forecastingType>d</forecastingType>

      <masterLabel>ForecastingTypeSource_d7</masterLabel>

      <parentSourceDefinition>FSD_OpportunityLineItemSchedule1</parentSourceDefinition>

      <relationField>OpportunityLineItemSchedule.OpportunityLineItemId</relationField>

      <sourceGroup>1</sourceGroup>

   </ForecastingTypeSource>

   <?xml version="1.0" encoding="UTF-8"?>

   <ForecastingTypeSource xmlns="http://soap.sforce.com/2006/04/metadata">

   <forecastingSourceDefinition>FSDOpportunityLineItemSchedule</forecastingSourceDefinition>

      <forecastingType>c3</forecastingType>

      <masterLabel>ForecastingTypeSource_c37syR</masterLabel>

      <sourceGroup>1</sourceGroup>

   </ForecastingTypeSource>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ForecastingTypeSource</name>

      </types>

      <version>52.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

Usage

**•** Forecast types that were available before API version 52.0 can be activated, deactivated, and deleted but not created. To enable an
existing forecast type, update the active flag.

**•** Forecast types that are available only in API version 52.0 and later can be created, activated, deactivated, and deleted. If the forecast
type doesn’t exist, it is created in the inactive state. If the forecast type exists, the active flag is updated. Deploy the zip file twice to
create and activate the forecast type.

**•** Deploy Metadata API types in the following sequence: ForecastingSettings, ForecastingType, ForecastingSourceDefinition, and then
ForecastingTypeSource. If all are specified in the package file, the sequence is followed automatically.


### Metadata Types FuelType FuelType

Represents a custom fuel type in an org.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### FuelType components have the suffix .fuelType and are stored in the fuelTypes folder.

Version

### FuelType components are available in API version 57.0 and later.

Special Access Rules

The Net Zero Cloud permission set license is required to access this object along with the user access for carbon accounting and org
access for custom fuels and unit of measures (UOMs).

Fields

**Field Name** **Description**

```
description

isActive

isProtected

isStationaryAssetFuel

```

**Field Type**
string

**Description**
Description about the fuel type.

**Field Type**
boolean

**Description**
Indicates whether the fuel type is active ( `true` ) or not ( `false` ).

The default value is `false` .

**Field Type**
boolean

**Description**
An auto-generated value that doesn’t impact the behavior of the metadata type.

The default value is `false` .

**Field Type**
boolean


Metadata Types FuelType

**Field Name** **Description**

**Description**

Indicates whether the fuel type is used in stationary assets ( `true` ) or not ( `false` ).

The default value is `false` .

```
isVehicleAssetFuel

masterLabel

```

**Field Type**
boolean

**Description**
Indicates whether the fuel type is used in a vehicle asset ( `true` ) or not ( `false` ).

The default value is `false` .

**Field Type**
string

**Description**

Required.

A user-friendly name for FuelType, which is defined when the FuelType is created.

Declarative Metadata Sample Definition

The following is an example of a FuelType component.

```
<?xml version="1.0" encoding="UTF-8"?>

<FuelType xmlns="http://soap.sforce.com/2006/04/metadata">

   <description>This is Petrol Fuel Type</description>

   <isProtected>true</isProtected>

   <isActive>true</isActive>

   <isStationaryAssetFuel>true</isStationaryAssetFuel>

   <isVehicleAssetFuel>true</isVehicleAssetFuel>

   <masterLabel>Petrol</masterLabel>

</FuelType>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

  <types>

    <members>Petrol</members>

    <members>Diesel</members>

    <members>Kerosine</members>

    <name>FuelType</name>

  </types>

  <version>57.0</version>

</Package>

```


### Metadata Types FuelTypeSustnUom

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### FuelTypeSustnUom

Represents a mapping between the custom fuel types and their corresponding unit of measure (UOM) values defined by a customer in
an org.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### FuelTypeSustnUom components have the suffix .fuelTypeSustnUom and are stored in the fuelTypeSustnUoms folder.

Version

### FuelTypeSustnUom components are available in API version 57.0 and later.

Special Access Rules

The Net Zero Cloud permission set license is required to access this object along with the user access for carbon accounting and org
access for custom fuels and UOMs.

Fields

**Field Name** **Description**

```
fuelType

```

**Field Type**
string

**Description**

Required.

The name of the fuel type that’s mapped to the unit of measure.

Possible values are:

**•** `AutogasLPG`

**•** `Biodiesel`

**•** `Biomass`

**•** `CityGas`

**•** `CompressedNaturalGasCNG`

**•** `Cooling`


Metadata Types FuelTypeSustnUom

**Field Name** **Description**

**•** `Diesel`

**•** `Electricity`

**•** `Ethanol`

**•** `FuelOil`

**•** `Gasoline`

**•** `Heat`

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

unitOfMeasure

```

**Field Type**
boolean

**Description**
An auto-generated value that doesn’t impact the behavior of the metadata type.

The default value is `false` .

**Field Type**
string

**Description**
A user-friendly name for FuelTypeSustnUom, which is defined when the
FuelTypeSustnUom is created.

**Field Type**
string

**Description**

Required.

The unit of measure that’s mapped to the fuel type.

Possible values are:

**•** `1000m3`

**•** `GJ`

**•** `GWh`


Metadata Types FuelTypeSustnUom

**Field Name** **Description**

**•** `Kiloliters`

**•** `Liters`

**•** `MJ`

**•** `MMBtu`

**•** `MWh`

**•** `Therms`

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

Declarative Metadata Sample Definition

The following is an example of a FuelTypeSustnUom component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <FuelTypeSustnUom xmlns="http://soap.sforce.com/2006/04/metadata">

      <fuelType>FuelOil</fuelType>

      <isProtected>false</isProtected>

      <masterLabel>FuelOil_Liters</masterLabel>

      <unitOfMeasure>Liters</unitOfMeasure>

   </FuelTypeSustnUom>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <fullName>Pkg</fullName>

      <types>

        <members>FuelOil_Liters</members>

        <members>Gas_1000m3</members>

        <members>Heat_kWh</members>

        <name>FuelTypeSustnUom</name>

      </types>

      <version>57.0</version>

   </Package>

```


### Metadata Types FunctionReference

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### FunctionReference

Represents information about a deployed Salesforce Function that can be invoked from the org.This type extends the Metadata metadata
type and inherits its `fullName` field.

File Suffix and Directory Location

### FunctionReference does not support direct access and should be managed using Salesforce CLI commands associated with Functions.

A FunctionReference component file has the suffix `.functions` and is stored in the `functions` directory.

Version

### FunctionReference components are available in API version 52.0 and later.

Special Access Rules

### FunctionReference components can’t be used directly. Always use Salesforce CLI commands associated with Functions to properly

deploy Functions and associate Functions with orgs. Attempting to manipulate FunctionReference components directly without using
Functions CLI commands is not supported.

Fields

**Field Name** **Field Type** **Description**

`description` string Represents the description of the Salesforce Function.

`label` string Represents the label for the Salesforce Function.

`permissionSet` string Represents a set of permissions that's used to control org resources that
the Function has access to.

### FundraisingConfig

Represents a collection of settings to configure the fundraising product.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types FundraisingConfig

File Suffix and Directory Location

FundraisingConfig components have the suffix `.fundraisingConfig` and are stored in the `fundraisingConfigs` folder.

Version

FundraisingConfig components are available in API version 58.0 and later.

Special Access Rules

Your org must have Fundraising Access license as a part of the Nonprofit Cloud to access this object.

Fields

**Field Name** **Description**

```
donorMatchingMethod

failedTransactionCount

householdSoftCreditRole

installmentExtDayCount

isHshldSoftCrAutoCrea

```

**Field Type**
DonorMatchingMethod (enumeration of type string)

**Description**
Reserved for future use.

**Field Type**
int

**Description**
The count of consecutive failed past transactions before the gift commitment status
is changed to Failing. If set to 0, the status is never auto-changed to Failing.

**Field Type**
string

**Description**
Reserved for future use.

**Field Type**
int

**Description**
The duration in the number of days before or after an unpaid transaction in a gift
commitment is marked as another installment in the gift commitment schedule. The
unpaid transaction within the grace period is considered a gift transaction.

**Field Type**
boolean

**Description**
Reserved for future use.


Metadata Types FundraisingConfig

**Field Name** **Description**

```
lapsedUnpaidTrxnCount

masterLabel

shouldClosePaidRcrCmt

shouldCreateRcrSchdTrxn

utmCampaignSrcObj

utmCampaignSrcObjField

utmMediumSrcObj

```

**Field Type**
int

**Description**
The count of consecutive unpaid past transactions before the gift commitment status
is changed to Lapsed. If set to 0, the status is never auto-changed to Lapsed.

**Field Type**
string

**Description**
A user-friendly name for FundraisingConfig, which is defined when the
FundraisingConfig is created.

**Field Type**
boolean

**Description**
Indicates whether to automatically close a recurring gift commitment when it has no
ongoing or future schedule and no unpaid transaction ( `true` ) or not ( `false` ).

The default value is `false` . Available in API version 59.0 and later.

**Field Type**
boolean

**Description**
Indicates whether the next transaction in a recurring schedule is automatically created
( `true` ) or not ( `false` ).

The default value is `true` . Available in API version 59.0 and later.

**Field Type**
string

**Description**
Name of the sObject of the campaign for which the donation was received. Available
in API version 64.0 and later.

**Field Type**
string

**Description**
Name of the field on the sObject in `utmCampaignSrcObj` of the campaign for
which the donation was received. Available in API version 64.0 and later.

**Field Type**
string


Metadata Types FundraisingConfig

**Field Name** **Description**

**Description**
Name of the sObject that stores data about the message channel from which the
donation originated. Available in API version 64.0 and later.

```
utmMediumSrcObjField

utmSourceSrcObj

utmSourceSrcObjField

```

**Field Type**
string

**Description**
Name of the field on the sObject in `utmMediumSrcObj` that stores data about the
message channel from which the donation originated. Available in API version 64.0
and later.

**Field Type**
string

**Description**
Name of the sObject that stores data about the source of a donation. Available in API
version 64.0 and later.

**Field Type**
string

**Description**
Name of the field on the sObject in `utmSourceSrcObj` that stores data about the
source of a donation. Available in API version 64.0 and later.

Declarative Metadata Sample Definition

The following is an example of a FundraisingConfig component.

```
<?xml version="1.0" encoding="UTF-8"?>

<FundraisingConfig xmlns="http://soap.sforce.com/2006/04/metadata">

   <lapsedUnpaidTrxnCount>5</lapsedUnpaidTrxnCount>

   <householdSoftCreditRole>Admin</householdSoftCreditRole>

   <isHshldSoftCrAutoCrea>true</isHshldSoftCrAutoCrea>

   <installmentExtDayCount>7</installmentExtDayCount>

   <donorMatchingMethod>No_Matching</donorMatchingMethod>

   <donorExternalIdField>TestExtId__c</donorExternalIdField>

   <failedTransactionCount>12</failedTransactionCount>

   <outreachSourceCodeGenFmla>OutreachSourceCodeGenFmla</outreachSourceCodeGenFmla>

   <shouldCreateRcrSchdTrxn>true</shouldCreateRcrSchdTrxn>

   <shouldClosePaidRcrCmt>false</shouldClosePaidRcrCmt>

   <masterLabel>MasterLabel</masterLabel>

   <utmMediumSrcObj>UTM Medium Src Obj</utmMediumSrcObj>

   <utmMediumSrcObjField>UTM Medium Src Obj Field</utmMediumSrcObjField>

   <utmSourceSrcObj>UTM Source Src Obj</utmSourceSrcObj>

   <utmSourceSrcObjField>UTM Source Src Obj Field</utmSourceSrcObjField>

   <utmCampaignSrcObj>UTM Campaign Src Obj</utmCampaignSrcObj>

```


### Metadata Types GatewayProviderPaymentMethodType

```
      <utmCampaignSrcObjField>UTM Campaign Src Obj Field</utmCampaignSrcObjField>

   </FundraisingConfig>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>FundraisingConfig</name>

      </types>

      <version>64.0</version>

   </Package>

### GatewayProviderPaymentMethodType

```

Represents an entity that allows integrators and payment providers to choose an active payment to receive an order's payment data
rather than allowing the Salesforce Order Management platform to select a default payment method. This object is available in API
version 51 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Version

gatewayProviderPaymentMethodType components are available in API version 51 and later.

Special Access Rules

Fields

**Field Name** **Description**

```
comment

gtwyProvPaymentMethodType

```

**Field Type**
textarea

**Description**
Additional details about the gateway provider payment method type record. Max
length is 1000 characters.

**Field Type**
string

**Description**
Links the Salesforce payment method to the payment method used in the Salesforce
Order Management storefront. Your payment gateway integration uses this field when
finding a payment method to link to a payment.


Metadata Types GatewayProviderPaymentMethodType

**Field Name** **Description**

The value of `GtwyProviderPaymentMethodType` must match the payment
method value sent to the order's Payment Instrument in Salesforce Order Management.

Here are examples of payment method values that Salesforce could receive from
Salesforce Order Management.

**•** `CREDIT_CARD`

**•** `BASIC_CREDIT`

**•** `CreditCard`

**•** `GooglePay`

**•** `ApplePay`

```
masterLabel

paymentGatewayProvider

paymentMethodType

recordType

```

**Field Type**
string

**Description**
Required. The gateway provider payment method type name that appears in the user
interface.

**Field Type**
reference

**Description**
Specifies the payment gateway provider that Salesforce Order Management should
use when processing payments. One payment gateway provider can be related to
multiple payment method types.

**Field Type**
picklist

**Description**
Specifies the type of payment method used on an order in Salesforce Order
Management.

Possible values are:

**•** `AlternativePaymentMethod`

**•** `CardPaymentMethod`

**•** `DigitalWallet`

**Field Type**
reference

**Description**
ID of the record type entity related to the gateway provider payment method type.

This is a relationship field.


### Metadata Types GenAiFunction

Declarative Metadata Sample Definition

The following is an example of a GatewayProviderPaymentMethodType component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <GatewayProviderPaymentMethodType xmlns="http://soap.sforce.com/2006/04/metadata">

      <gtwyProviderPaymentMethodType>Klarna</gtwyProviderPaymentMethodType>

      <masterLabel>Test</masterLabel>

      <paymentGatewayProvider>adyen__Adyen</paymentGatewayProvider>

      <paymentMethodType>AlternativePaymentMethod</paymentMethodType>

      <recordType>AlternativePaymentMethod.Klarna</recordType>

   </GatewayProviderPaymentMethodType>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>GatewayProviderPaymentMethodType</name>

      </types>

      <version>51.0</version>

   </Package>

### GenAiFunction

```

Represents an agent action that can be added to an AI agent.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### GenAiFunction components have the suffix .genAiFunction and are stored in the genAiFunctions folder. GenAiFunction components can contain folders for the input on page 1353 and output on page 1356 schemas. Here’s an example component,

showing the schema folders.

See the Input Folder on page 1353 and Output Folder on page 1356 sections for more information.


Metadata Types GenAiFunction

Version

GenAiFunction components are available in API version 60.0 and later.

Special Access Rules

GenAiFunction is available only if Agents is enabled in your org.

Fields

**Field Name** **Description**

```
description

invocationTarget

invocationTargetType

isConfirmationRequired

```

**Field Type**
string

**Description**
A description explaining the general purpose and domain of the action.

**Field Type**
string

**Description**

Required. Target invocation used by invocation operations.

**Field Type**
PlannerFunctionInvocableTargetType (enumeration of type string)

**Description**

Required. Invocable action type used by invocation operations.

Values are:

**•** `apex`

**•** `api`

**•** `createCatalogItemRequest`

**•** `flow`

**•** `generatePromptResponse`

**•** `externalService`

**•** `quickAction`

**•** `slack`

**•** `standardInvocableAction`

**Field Type**
boolean

**Description**
Indicates whether confirmation is required for this action.


Metadata Types GenAiFunction

**Field Name** **Description**

```
isIncludeInProgressIndicator

mappingAttributes

masterLabel

pluginField

progressIndicatorMessage

```

GenAiPlannerAttr

**Field Type**
boolean

**Description**
Indicates whether to display the progress indicator for this action.

**Field Type**

GenAiPlannerAttr[]

**Description**
List of attributes for the planner.

**Field Type**
string

**Description**

Required. The master label for the generative AI action.

**Field Type**
string

**Description**

Represents the action’s parent topic.

**Field Type**
string

**Description**

The progress message.

**Field Name** **Description**

```
description

label

```

**Field Type**
string

**Description**
Description of the planner attribute.

**Field Type**
string

**Description**

Required. Label for the planner attribute.


Metadata Types GenAiFunction

**Field Name** **Description**

```
name

parameterName

parameterType

```

Input Folder

**Field Type**
string

**Description**
Required. Name of the planner attribute.

**Field Type**
string

**Description**
Required. The parameter name.

**Field Type**
PlannerAttrMappingType (enumeration of type string)

**Description**
Required. The parameter type. Values are:

**•** `input`

**•** `output`

The `input` folder contains a `schema.json` file with the action inputs. Here’s a sample input schema file.

```
{

  "required" : ["OwnerId", "Status"],

  "properties" : {

   "OwnerId" : {

    "title" : "Owner Id",

    "description" : "ID of the Salesforce record that owns the request.",

    "lightning:type" : "lightning__textType",

    "lightning:isPII" : false,

    "copilotAction:isUserInput" : true

   },

   "Status" : {

    "title" : "Request Status",

    "description" : "The status of the contact request.",

    "lightning:type" : "lightning__textType",

    "lightning:isPII" : false,

    "copilotAction:isUserInput" : true

   }

  },

  "lightning:type" : "lightning__objectType"

}

```

This table describes the properties that you can specify in this JSON file.


Metadata Types GenAiFunction


Metadata Types GenAiFunction


Metadata Types GenAiFunction

Output Folder

The `output` folder contains a `schema.json` file with the action output. Here’s a sample output schema file.

```
   {

     "properties" : {

      "Id" : {

       "title" : "Contact Request Id",

       "description" : "ID of the Salesforce contact request record.",

       "lightning:type" : "lightning__recordIdType",

       "lightning:isPII" : false,

       "copilotAction:isDisplayable" : true,

       "copilotAction:isUsedByPlanner" : true

      }

     },

     "lightning:type" : "lightning__objectType"

   }

```

This table describes the properties that you can specify in this JSON file.


Metadata Types GenAiFunction


Metadata Types GenAiFunction

Usage

In Winter '26 orgs and later, use GenAiPlannerBundle on page 1367 to retrieve actions that are created within a particular agent. To retrieve
actions in the asset library, use GenAiFunction.

When deploying topic or action metadata to a Summer '25 (version 64.0) org, retrieve the metadata using Metadata API version 64.0,
even if your source org is Winter '26 or later (version 65.0). For Winter `26 and later, use Metadata API version 65.0 and later.

Declarative Metadata Sample Definition

The following is an example of a GenAiFunction component.

```
<?xml version="1.0" encoding="UTF-8"?>

<GenAiFunction xmlns="http://soap.sforce.com/2006/04/metadata">

   <description>get tracking information</description>

   <invocationTarget>TrackShipment</invocationTarget>

   <invocationTargetType>apex</invocationTargetType>

   <isConfirmationRequired>false</isConfirmationRequired>

   <masterLabel>get_tracking_info</masterLabel>

</GenAiFunction>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

  <types>

    <members>*</members>

    <name>GenAiFunction</name>

  </types>

```


### Metadata Types GenAiPlanner

```
     <version>60.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### GenAiPlanner

Represents a planner for an agent. It’s a container for all the topics and actions used to interact with a large language model (LLM).

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### GenAiPlanner components have the suffix .genAiPlanner and are stored in the genAiPlanners folder.

Version

### GenAiPlanner components are available in API version 60.0 to 63.0. GenAiPlannerBundle replaces GenAiPlanner in API version 64.0 and

later.

Special Access Rules

### GenAiPlanner is available only if Agents is enabled in your org.

Fields

**Field Name** **Description**

```
attributeMappings

capabilities

```

**Field Type**
### GenAiPlannerAttrMapping[]

**Description**

A list of action attribute mappings.

**Field Type**
string

**Description**

A set of tags associated with the agent.


Metadata Types GenAiPlanner

**Field Name** **Description**

```
description

genAiFunctions

genAiPlannerRuleExpressions

genAiPlugins

masterLabel

plannerType

ruleExpressionAssignments

```

**Field Type**
string

**Description**
A description explaining the general purpose and domain of the agent.

**Field Type**

GenAiPlannerFunctionDef[]

**Description**
A list of agent action definitions, such as a knowledge action, that are not contained
in a topic.

**Field Type**
GenAiPlannerRuleExpr[]

**Description**
Deprecated. Use `ruleExpressions` instead.

**Field Type**

GenAiPlannerFunctionDef[]

**Description**
A list of agent topic definitions.

**Field Type**
string

**Description**

Required. The master label for the planner.

**Field Type**
PlannerType (enumeration of type string)

**Description**

Required. A particular approach to problem solving that is given as prompt instructions
to a large language model (LLM).

The only supported value is:

**•** `AiCopilot__ReAct` —Uses a reactive reasoning strategy to solve problems
with the LLM. This strategy consists of prompting the LLM to generate the next
step in response to an event and the current context. It differs from a sequential
reasoning engine in that it doesn’t plan more than one step ahead of time.

**Field Type**

GenAiPlannerRuleExprAsgn[]

**Description**
A list of rule expression assignments.


Metadata Types GenAiPlanner

**Field Name** **Description**

```
ruleExpressions

```

**Field Type**

GenAiPlannerRuleExprDef[]

**Description**
A list of rule expressions.

GenAiPlannerAttrMapping

Represents an attribute mapping, which enables you to map the output of one action attribute to the input of another attribute. This
mapping enables you to propagate sensitive data safely without relying on untrusted user input.

**Field Name** **Description**

```
attributeName

attributeType

constantValue

mappingTargetName

mappingType

```

**Field Type**
string

**Description**

Required. The attribute name in the format:
`Namespace.TopicName.ActionName.AttributeName` .

**Field Type**
AttributeType (enumeration of type string)

**Description**

Required. The attribute type. Values are:

**•** `CustomPluginFunctionAttribute` —Map to a custom action input or
output

**•** `StandardPluginFunctionInput` —Map to a standard action input

**•** `StandardPluginFunctionOutput` —Map output to a variable

**Field Type**
string

**Description**

Reserved for future use.

**Field Type**
string

**Description**

The target name for the attribute mapping.

**Field Type**
AttributeMappingType (enumeration of type string)


Metadata Types GenAiPlanner

**Field Name** **Description**

**Description**

Required. The target type. Values are:

**•** `ActionAttribute`

**•** `Constant`

**•** `Variable`

**•** `ContextVariable`

GenAiPlannerFunctionDef

Represents an agent topic or action definition.

**Field Name** **Description**

```
genAiCustomizedPlugin

genAiFunctionName

genAiPluginName

```

GenAiLocalPlugin

Represents a custom agent topic.

**Field Type**

GenAiLocalPlugin[]

**Description**

A list of custom agent topics.

**Field Type**
string

**Description**

The name of the agent action.

**Field Type**
string

**Description**

The name of the agent topic.

**Field Name** **Description**

```
aiPluginUtterances

```

**Field Type**

AiPluginUtteranceDef[]

**Description**
A list of utterances that can be used to pick a topic during runtime.


Metadata Types GenAiPlanner

**Field Name** **Description**

```
description

genAiFunctions

genAiPluginInstructions

language

masterLabel

name

pluginType

```

**Field Type**
string

**Description**
The description of the topic.

**Field Type**

GenAiPluginFunctionDef[]

**Description**
A list of functions in the topic.

**Field Type**

GenAiPluginInstructionDef[]

**Description**
A list of instructions in the topic.

**Field Type**
string

**Description**

Required.

The language of the topic.

**Field Type**
string

**Description**

Required.

The master label for the topic.

**Field Type**
string

**Description**

Required.

Represents the API name of the topic. This name must be unique across all custom
and customized topics. Can contain only underscores and alphanumeric characters
and must be unique in your org. It must begin with a letter, not include spaces, not
end with an underscore, and not contain two consecutive underscores.

**Field Type**
PluginType (enumeration of type string)

**Description**

Required.


Metadata Types GenAiPlanner

**Field Name** **Description**

Values are:

**•** `Topic`

```
scope

```

**Field Type**
string

**Description**
A specific job description for a topic.

GenAiPlannerRuleExprAsgn

Represents a rule-expression assignment to either a topic or an action.

**Field Name** **Description**

```
ruleExpressionName

targetName

targetType

```

**Field Type**
string

**Description**

Required. The name of the rule expression.

**Field Type**
string

**Description**

Required. The target of the assignment, which is a
`Namespace.TopicName.ActionName` or a `TopicName` .

**Field Type**
string

**Description**

Required. The type of the target. Values are:

**•** `Function` —A knowledge action

**•** `Plugin` —A topic

**•** `PluginFunction` —An action in a topic

GenAiPlannerRuleExprDef

Represents a rule expression, which conditionally locks or unlocks topics and actions based on defined security criteria.


Metadata Types GenAiPlanner

**Field Name** **Description**

```
conditions

expression

expressionLabel

expressionName

expressionType

```

**Field Type**

GenAiPlannerRuleExprCondition[]

**Description**

A list of conditions for a rule expression.

**Field Type**
string

**Description**

An expression with the combined conditions.

**Field Type**
string

**Description**
Required. The expression label.

**Field Type**
string

**Description**
Required. The expression name.

**Field Type**
string

**Description**
The expression type. Values are:

**•** `handlebars` —Reserved for future use

**•** `sel` —Salesforce Expression Language, as used in formula fields

GenAiPlannerRuleExprCondition

Represents a condition for a rule expression.

**Field Name** **Description**

```
leftOperand

leftOperandType

```

**Field Type**
string

**Description**

Required. The left operand in the expression.

**Field Type**
GenAiAgentVariableType (enumeration of type string)


Metadata Types GenAiPlanner

**Field Name** **Description**

**Description**
Required. The type for the left operand. Values are:

**•** `Variable`

**•** `ContextVariable`

**•** `Attribute`

```
operator

rightOperandValue

```

**Field Type**
GenAiRuleExpressionOperator (enumeration of type string)

**Description**
Required. The operator in the expression. Values are:

**•** `equal`

**•** `greaterThan`

**•** `greaterThanOrEqual`

**•** `lessThan`

**•** `lessThanOrEqual`

**•** `notEqual`

**•** `isEmpty`

**•** `isNotEmpty`

**Field Type**
string

**Description**
The value for the right operand.

Declarative Metadata Sample Definition

The following is an example of a GenAiPlanner component.

```
<?xml version="1.0" encoding="UTF-8"?>

<GenAiPlanner xmlns="http://soap.sforce.com/2006/04/metadata">

   <description>Copilot reasoning engine description</description>

   <masterLabel>EmployeeCopilotPlanner</masterLabel>

   <plannerType>AiCopilot__SequentialPlannerIntentClassifier</plannerType>

</GenAiPlanner>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

  <types>

    <members>*</members>

    <name>GenAiPlanner</name>

  </types>

```


### Metadata Types GenAiPlannerBundle

```
     <version>60.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### GenAiPlannerBundle

Represents a planner for an agent or agent template. It’s a container for all the topics and actions used to interact with a large language
model (LLM).

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### GenAiPlannerBundle components have the suffix .genAiPlannerBundle and are stored in a subfolder for the agent in the

`genAiPlannerBundles` folder.

Version

### GenAiPlannerBundle components are available in API version 64.0 and later. GenAiPlannerBundle replaces GenAiPlanner, which is

available in API version 63.0 and earlier.

Special Access Rules

### GenAiPlannerBundle is available only if Agents is enabled in your org.

Fields

**Field Name** **Description**

```
attributeMappings

botTemplate

```

**Field Type**

GenAiPlannerAttrMapping[]

**Description**

A list of action attribute mappings.

**Field Type**
string


Metadata Types GenAiPlannerBundle

**Field Name** **Description**

**Description**
If this planner is used by an agent template instead of an agent, this field is the template
associated with the planner.

```
capabilities

description

genAiFunctions

genAiPlugins

masterLabel

plannerType

```

**Field Type**
string

**Description**

A set of tags associated with the agent.

**Field Type**
string

**Description**
A description explaining the general purpose and domain of the agent.

**Field Type**

GenAiPlannerFunctionDef[]

**Description**
A list of agent action definitions, such as a knowledge action, that are not contained
in a topic.

**Field Type**

GenAiPlannerFunctionDef[]

**Description**
A list of agent topic definitions.

**Field Type**
string

**Description**

Required. The master label for the planner.

**Field Type**
PlannerType (enumeration of type string)

**Description**

Required. A particular approach to problem solving that is given as prompt instructions
to a large language model (LLM).

The supported values are:

**•** `AiCopilot__AgileAppDev` —Uses an iterative development strategy to
assist with building applications using the LLM. This strategy prompts the LLM to
generate modular, testable components based on evolving user input and context.
Unlike linear workflows, it supports continuous refinement and feedback loops
throughout the development process.


Metadata Types GenAiPlannerBundle

**Field Name** **Description**

**•** `AiCopilot__ReAct` —Uses a reactive reasoning strategy to solve problems
with the LLM. This strategy consists of prompting the LLM to generate the next
step in response to an event and the current context. It differs from a sequential
reasoning engine in that it doesn’t plan more than one step ahead of time.

```
ruleExpressionAssignments

ruleExpressions

```

**Field Type**

GenAiPlannerRuleExprAsgn[]

**Description**
A list of rule expression assignments.

**Field Type**

GenAiPlannerRuleExprDef[]

**Description**
A list of rule expressions.

GenAiPlannerAttrMapping

Represents an attribute mapping, which enables you to map the output of one action attribute to the input of another attribute. This
mapping enables you to propagate sensitive data safely without relying on untrusted user input.

**Field Name** **Description**

```
attributeName

attributeType

constantValue

```

**Field Type**
string

**Description**

Required. The attribute name in the format:
`Namespace.TopicName.ActionName.AttributeName` .

**Field Type**
AttributeType (enumeration of type string)

**Description**

Required. The attribute type. Values are:

**•** `CustomPluginFunctionAttribute` —Map to a custom action input or
output

**•** `StandardPluginFunctionInput` —Map to a standard action input

**•** `StandardPluginFunctionOutput` —Map output to a variable

**Field Type**
string

**Description**

Reserved for future use.


Metadata Types GenAiPlannerBundle

**Field Name** **Description**

```
mappingTargetName

mappingType

```

**Field Type**
string

**Description**

The target name for the attribute mapping.

**Field Type**
AttributeMappingType (enumeration of type string)

**Description**

Required. The target type. Values are:

**•** `ActionAttribute`

**•** `Constant`

**•** `Variable`

**•** `ContextVariable`

GenAiPlannerFunctionDef

Represents an agent topic or action definition.

**Field Name** **Description**

```
genAiCustomizedPlugin

genAiFunctionName

genAiPluginName

```

GenAiLocalPlugin

Represents a custom agent topic.

**Field Type**

GenAiLocalPlugin[]

**Description**

A list of custom agent topics.

**Field Type**
string

**Description**

The name of the agent action.

**Field Type**
string

**Description**

The name of the agent topic.


Metadata Types GenAiPlannerBundle

**Field Name** **Description**

```
aiPluginUtterances

canEscalate

description

genAiFunctions

genAiPluginInstructions

language

masterLabel

name

```

**Field Type**

AiPluginUtteranceDef[]

**Description**
A list of utterances that can be used to pick a topic during runtime.

**Field Type**
boolean

**Description**
Determines whether this topic is applicable for escalation to a rep.

**Field Type**
string

**Description**

Required.

The description of the topic.

**Field Type**

GenAiPluginFunctionDef[]

**Description**
A list of functions in the topic.

**Field Type**

GenAiPluginInstructionDef[]

**Description**
A list of instructions in the topic.

**Field Type**
string

**Description**

Required.

The language of the topic.

**Field Type**
string

**Description**

Required.

The master label for the topic.

**Field Type**
string


Metadata Types GenAiPlannerBundle

**Field Name** **Description**

**Description**

Required.

Represents the API name of the topic. This name must be unique across all custom
and customized topics. Can contain only underscores and alphanumeric characters
and must be unique in your org. It must begin with a letter, not include spaces, not
end with an underscore, and not contain two consecutive underscores.

```
pluginType

scope

```

**Field Type**
PluginType (enumeration of type string)

**Description**

Required.

Values are:

**•** `Topic`

**•** `APICustomTopic`

**Field Type**
string

**Description**
A specific job description for a topic.

GenAiPlannerRuleExprAsgn

Represents a rule-expression assignment to either a topic or an action.

**Field Name** **Description**

```
ruleExpressionName

targetName

targetType

```

**Field Type**
string

**Description**

Required. The name of the rule expression.

**Field Type**
string

**Description**

Required. The target of the assignment, which is a
`Namespace.TopicName.ActionName` or a `TopicName` .

**Field Type**
string


Metadata Types GenAiPlannerBundle

**Field Name** **Description**

**Description**

Required. The type of the target. Values are:

**•** `Function` —A knowledge action

**•** `Plugin` —A topic

**•** `PluginFunction` —An action in a topic

GenAiPlannerRuleExprDef

Represents a rule expression, which conditionally locks or unlocks topics and actions based on defined security criteria.

**Field Name** **Description**

```
conditions

expression

expressionLabel

expressionName

expressionType

```

**Field Type**

GenAiPlannerRuleExprCondition[]

**Description**

A list of conditions for a rule expression.

**Field Type**
string

**Description**

An expression with the combined conditions.

**Field Type**
string

**Description**
Required. The expression label.

**Field Type**
string

**Description**
Required. The expression name.

**Field Type**
string

**Description**
The expression type. Values are:

**•** `handlebars` —Reserved for future use

**•** `sel` —Salesforce Expression Language, as used in formula fields


Metadata Types GenAiPlannerBundle

GenAiPlannerRuleExprCondition

Represents a condition for a rule expression.

**Field Name** **Description**

```
leftOperand

leftOperandType

operator

rightOperandValue

```

Usage

**Field Type**
string

**Description**

Required. The left operand in the expression.

**Field Type**
GenAiAgentVariableType (enumeration of type string)

**Description**
Required. The type for the left operand. Values are:

**•** `Variable`

**•** `ContextVariable`

**•** `Attribute`

**Field Type**
GenAiRuleExpressionOperator (enumeration of type string)

**Description**
Required. The operator in the expression. Values are:

**•** `equal`

**•** `greaterThan`

**•** `greaterThanOrEqual`

**•** `lessThan`

**•** `lessThanOrEqual`

**•** `notEqual`

**•** `isEmpty`

**•** `isNotEmpty`

**Field Type**
string

**Description**
The value for the right operand.

In Winter ‘26 orgs and later, use GenAiPlannerBundle to retrieve topics and actions created in an agent. To retrieve global topics and
actions, or those created in the Asset Library, use GenAiPlugin on page 1378 and GenAiFunction on page 1350.

In Summer ‘25 orgs and earlier, deploy topic and action metadata using GenAiPlugin on page 1378 and GenAiFunction on page 1350.


Metadata Types GenAiPlannerBundle

When deploying topic or action metadata to a Summer '25 (version 64.0) org, retrieve the metadata using Metadata API version 64.0,
even if your source org is Winter '26 or later (version 65.0). For Winter `26 and later, use Metadata API version 65.0 and later.

Declarative Metadata Sample Definition

Here’s an example of a GenAiPlannerBundle component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <GenAiPlannerBundle xmlns="http://soap.sforce.com/2006/04/metadata">

      <attributeMappings>

   attributeName>SvcCopilotTmpl__CaseManagement.SvcCopilotTmpl__CreateCaseEnhancedData.verifiedCustomerID</attributeName>

        <attributeType>StandardPluginFunctionInput</attributeType>

        <mappingTargetName>VerifiedCustomerId</mappingTargetName>

        <mappingType>Variable</mappingType>

      </attributeMappings>

      <attributeMappings>

   <attributeName>SvcCopilotTmpl__CaseManagement.SvcCopilotTmpl__GetCasesForVerifiedContact.verifiedContactID</attributeName>

        <attributeType>StandardPluginFunctionInput</attributeType>

        <mappingTargetName>VerifiedCustomerId</mappingTargetName>

        <mappingType>Variable</mappingType>

      </attributeMappings>

      <attributeMappings>

   <attributeName>SvcCopilotTmpl__CaseManagement.SvcCopilotTmpl__GetCaseByVerifiedCaseNumber.verifiedContactID</attributeName>

        <attributeType>StandardPluginFunctionInput</attributeType>

        <mappingTargetName>VerifiedCustomerId</mappingTargetName>

        <mappingType>Variable</mappingType>

      </attributeMappings>

      <attributeMappings>

   <attributeName>SvcCopilotTmpl__ServiceCustomerVerification.SvcCopilotTmpl__SendEmailVerificationCode.authenticationKey</attributeName>

        <attributeType>StandardPluginFunctionOutput</attributeType>

        <mappingTargetName>authenticationKey</mappingTargetName>

        <mappingType>Variable</mappingType>

      </attributeMappings>

      <attributeMappings>

   <attributeName>SvcCopilotTmpl__ServiceCustomerVerification.SvcCopilotTmpl__SendEmailVerificationCode.customerId</attributeName>

        <attributeType>StandardPluginFunctionOutput</attributeType>

        <mappingTargetName>customerId</mappingTargetName>

        <mappingType>Variable</mappingType>

      </attributeMappings>

      <attributeMappings>

   <attributeName>SvcCopilotTmpl__ServiceCustomerVerification.SvcCopilotTmpl__SendEmailVerificationCode.customerType</attributeName>

        <attributeType>StandardPluginFunctionOutput</attributeType>

```


Metadata Types GenAiPlannerBundle

```
        <mappingTargetName>customerType</mappingTargetName>

        <mappingType>Variable</mappingType>

      </attributeMappings>

      <attributeMappings>

   <attributeName>SvcCopilotTmpl__ServiceCustomerVerification.SvcCopilotTmpl__VerifyCustomer.authenticationKey</attributeName>

        <attributeType>StandardPluginFunctionInput</attributeType>

        <mappingTargetName>authenticationKey</mappingTargetName>

        <mappingType>Variable</mappingType>

      </attributeMappings>

      <attributeMappings>

   <attributeName>SvcCopilotTmpl__ServiceCustomerVerification.SvcCopilotTmpl__VerifyCustomer.customerId</attributeName>

        <attributeType>StandardPluginFunctionInput</attributeType>

        <mappingTargetName>customerId</mappingTargetName>

        <mappingType>Variable</mappingType>

      </attributeMappings>

      <attributeMappings>

   <attributeName>SvcCopilotTmpl__ServiceCustomerVerification.SvcCopilotTmpl__VerifyCustomer.customerType</attributeName>

        <attributeType>StandardPluginFunctionInput</attributeType>

        <mappingTargetName>customerType</mappingTargetName>

        <mappingType>Variable</mappingType>

      </attributeMappings>

      <attributeMappings>

   <attributeName>SvcCopilotTmpl__ServiceCustomerVerification.SvcCopilotTmpl__VerifyCustomer.isVerified</attributeName>

        <attributeType>StandardPluginFunctionOutput</attributeType>

        <mappingTargetName>isVerified</mappingTargetName>

        <mappingType>Variable</mappingType>

      </attributeMappings>

      <attributeMappings>

   <attributeName>SvcCopilotTmpl__ServiceCustomerVerification.SvcCopilotTmpl__VerifyCustomer.customerId</attributeName>

        <attributeType>StandardPluginFunctionOutput</attributeType>

        <mappingTargetName>VerifiedCustomerId</mappingTargetName>

        <mappingType>Variable</mappingType>

      </attributeMappings>

      <attributeMappings>

   <attributeName>SvcCopilotTmpl__AccountManagement.SvcCopilotTmpl__ResetSecurePassword.verifiedContactID</attributeName>

        <attributeType>StandardPluginFunctionInput</attributeType>

        <mappingTargetName>VerifiedCustomerId</mappingTargetName>

        <mappingType>Variable</mappingType>

      </attributeMappings>

      <attributeMappings>

   <attributeName>SvcCopilotTmpl__AccountManagement.SvcCopilotTmpl__UpdateVerifiedContact.verifiedContactID</attributeName>

```


Metadata Types GenAiPlannerBundle

```
        <attributeType>StandardPluginFunctionInput</attributeType>

        <mappingTargetName>VerifiedCustomerId</mappingTargetName>

        <mappingType>Variable</mappingType>

      </attributeMappings>

      <description>Deliver personalized customer interactions with an autonomous AI agent.

   Agentforce Service Agent intelligently supports your customers with common inquiries and

   escalates complex issues.</description>

      <genAiFunctions>

       <genAiFunctionName>EmployeeCopilot__AnswerQuestionsWithKnowledge</genAiFunctionName>

      </genAiFunctions>

      <genAiPlugins>

        <genAiPluginName>SvcCopilotTmpl__AccountManagement</genAiPluginName>

      </genAiPlugins>

      <genAiPlugins>

        <genAiPluginName>SvcCopilotTmpl__CaseManagement</genAiPluginName>

      </genAiPlugins>

      <genAiPlugins>

        <genAiPluginName>SvcCopilotTmpl__Escalation</genAiPluginName>

      </genAiPlugins>

      <genAiPlugins>

        <genAiPluginName>SvcCopilotTmpl__GeneralFAQ</genAiPluginName>

      </genAiPlugins>

      <genAiPlugins>

        <genAiPluginName>SvcCopilotTmpl__ServiceCustomerVerification</genAiPluginName>

      </genAiPlugins>

      <masterLabel>ASA Template Base</masterLabel>

      <plannerType>AiCopilot__ReAct</plannerType>

      <ruleExpressionAssignments>

        <ruleExpressionName>Verified_User</ruleExpressionName>

        <targetName>SvcCopilotTmpl__AccountManagement</targetName>

        <targetType>Plugin</targetType>

      </ruleExpressionAssignments>

      <ruleExpressionAssignments>

        <ruleExpressionName>Verified_User</ruleExpressionName>

        <targetName>SvcCopilotTmpl__CaseManagement</targetName>

        <targetType>Plugin</targetType>

      </ruleExpressionAssignments>

      <ruleExpressions>

        <conditions>

           <leftOperand>isVerified</leftOperand>

           <leftOperandType>Variable</leftOperandType>

           <operator>equal</operator>

           <rightOperandValue>true</rightOperandValue>

        </conditions>

        <expression>Verified_User</expression>

        <expressionLabel>Verified User</expressionLabel>

        <expressionName>Verified_User</expressionName>

        <expressionType>sel</expressionType>

      </ruleExpressions>

   </GenAiPlannerBundle>

```


### Metadata Types GenAiPlugin

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <types>

       <members>*</members>

       <name>GenAiPlannerBundle</name>

     </types>

     <version>64.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### GenAiPlugin

Represents an agent topic, which is a category of actions related to a particular job to be done by AI agents.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### GenAiPlugin components have the suffix .genAiPlugin and are stored in the genAiPlugins folder.

Version

### GenAiPlugin components are available in API version 62.0 and later.

Special Access Rules

### GenAiPlugin is available only if Agents is enabled in your org.

Fields

**Field Name** **Description**

```
aiPluginUtterances

```

**Field Type**

AiPluginUtteranceDef[]

**Description**
A list of utterances that can be used to pick a topic during runtime.


Metadata Types GenAiPlugin

**Field Name** **Description**

```
canEscalate

description

developerName

genAiFunctions

genAiPluginInstructions

language

masterLabel

```

**Field Type**
boolean

**Description**
Indicates whether this topic is eligible for escalation to a rep.

**Field Type**
string

**Description**
The description of the topic.

**Field Type**
string

**Description**

Required.

Represents the API name of the topic. This name must be unique across all custom
and customized topics. Can contain only underscores and alphanumeric characters
and must be unique in your org. It must begin with a letter, not include spaces, not
end with an underscore, and not contain two consecutive underscores.

**Field Type**

GenAiPluginFunctionDef[]

**Description**
A list of functions in the topic.

**Field Type**

GenAiPluginInstructionDef[]

**Description**
A list of instructions in the topic.

**Field Type**
string

**Description**

Required.

The language of the topic.

**Field Type**
string

**Description**

Required.

The master label for the topic.


Metadata Types GenAiPlugin

**Field Name** **Description**

```
plannerField

pluginType

scope

```

GenAiPluginFunctionDef

A function in the topic.

**Field Type**
string

**Description**
Represents the topic’s parent planner.

**Field Type**
PluginType (enumeration of type string)

**Description**

Required.

Values are:

**•** `Topic`

**•** `APICustomTopic`

**Field Type**
string

**Description**
A specific job description for a topic.

**Field Name** **Description**

```
functionName

```

Usage

**Field Type**
string

**Description**

Required.

The API name of the function.

In Winter '26 orgs and later, use GenAiPlannerBundle on page 1367 to retrieve topics that are created within a particular agent. To retrieve
topics in the asset library, use GenAiPlugin.

When deploying topic or action metadata to a Summer '25 (version 64.0) org, retrieve the metadata using Metadata API version 64.0,
even if your source org is Winter '26 or later (version 65.0). For Winter `26 and later, use Metadata API version 65.0 and later.


Metadata Types GenAiPlugin

Declarative Metadata Sample Definition

The following is an example of a GenAiPlugin component.

```
   <GenAiPlugin xmlns="http://soap.sforce.com/2006/04/metadata"

   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

      <description>Engages and interacts with the user about any request that could be CRM

   data related.

       This could be tasks such as identify and summarize records, answer queries, aggregate

    data,

      find and query objects, update records, or drafting and refining emails.</description>

      <developerName>General_CRM_Customized</developerName>

      <genAiFunctions>

        <functionName>EmployeeCopilot__IdentifyObjectByName</functionName>

      </genAiFunctions>

      <genAiFunctions>

        <functionName>EmployeeCopilot__IdentifyRecordByName</functionName>

      </genAiFunctions>

      <genAiFunctions>

        <functionName>EmployeeCopilot__QueryRecords</functionName>

      </genAiFunctions>

      <genAiFunctions>

        <functionName>EmployeeCopilot__QueryRecordsWithAggregate</functionName>

      </genAiFunctions>

      <genAiFunctions>

        <functionName>EmployeeCopilot__GetActivitiesTimeline</functionName>

      </genAiFunctions>

      <genAiFunctions>

        <functionName>EmployeeCopilot__GetActivityDetails</functionName>

      </genAiFunctions>

      <genAiFunctions>

        <functionName>EmployeeCopilot__GetRecordDetails</functionName>

      </genAiFunctions>

      <genAiFunctions>

        <functionName>EmployeeCopilot__DraftOrReviseEmail</functionName>

      </genAiFunctions>

      <genAiFunctions>

        <functionName>EmployeeCopilot__UpdateRecordFields</functionName>

      </genAiFunctions>

      <genAiFunctions>

        <functionName>EmployeeCopilot__WebSearch</functionName>

      </genAiFunctions>

      <genAiFunctions>

        <functionName>EmployeeCopilot__AnswerQuestionsWithKnowledge</functionName>

      </genAiFunctions>

      <genAiPluginInstructions>

       <description>There are multiple available data retrieval functions at your disposal.

         You can use each one of them multiple times if needed. You should use functions

         as many times as necessary until you have all the data required to fulfill the

   request of the user.

         You can perform extra calls if you think you can get additional relevant

   information.</description>

```


Metadata Types GenAiPlugin

```
        <developerName>therearemu0</developerName>

        <language xsi:nil="true"/>

        <masterLabel>therearemu</masterLabel>

      </genAiPluginInstructions>

      <genAiPluginInstructions>

       <description>Do not declare your intent i.e. &quot;I will now retrieve the data&quot;

    - Just fetch the data.</description>

        <developerName>donotdecla1</developerName>

        <language xsi:nil="true"/>

        <masterLabel>donotdecla</masterLabel>

      </genAiPluginInstructions>

      <genAiPluginInstructions>

        <description>Identify the object type (i.e., leads, opportunities, accounts) the

   user asks about.

          If unclear, confirm with the user and make a suggestion based on the query

   context and history.</description>

        <developerName>identifyth2</developerName>

        <language xsi:nil="true"/>

        <masterLabel>identifyth</masterLabel>

      </genAiPluginInstructions>

      <genAiPluginInstructions>

        <description>When only the name of a record is mentioned in the user request, you

    MUST call the IdentifyRecordByName action

         to get the necessary IDs.</description>

        <developerName>whenonlyth3</developerName>

        <language xsi:nil="true"/>

        <masterLabel>whenonlyth</masterLabel>

      </genAiPluginInstructions>

      <genAiPluginInstructions>

       <description>Always call QueryRecords &amp; QueryRecordsWithAggregate passing plain

    natural language english as input.

         You must Include the record ID in the input if available.</description>

        <developerName>alwayscall4</developerName>

        <language xsi:nil="true"/>

        <masterLabel>alwayscall</masterLabel>

      </genAiPluginInstructions>

      <genAiPluginInstructions>

        <description>For accounts and contacts, combine the WebSearch action with the CRM

    data retrieval actions.

          MUST maintain citations in the answer.</description>

        <developerName>foraccount5</developerName>

        <language xsi:nil="true"/>

        <masterLabel>foraccount</masterLabel>

      </genAiPluginInstructions>

      <genAiPluginInstructions>

        <description>When a user asks for a summary or overview of a record, use

   GetRecordDetails to get an overview

         of the data of the record, then use other data retrieval actions as

   needed.</description>

        <developerName>whenausera6</developerName>

        <language xsi:nil="true"/>

        <masterLabel>whenausera</masterLabel>

      </genAiPluginInstructions>

      <genAiPluginInstructions>

```


Metadata Types GenAiPlugin

```
        <description>When asked for a summary on multiple records, you must iterate over

   all record IDs and for each one,

         call GetRecordDetails.</description>

        <developerName>whenaskedf7</developerName>

        <language xsi:nil="true"/>

        <masterLabel>whenaskedf</masterLabel>

      </genAiPluginInstructions>

      <genAiPluginInstructions>

        <description>If the user asks about activities you must call

   GetActivitiesTimeline.</description>

        <developerName>iftheusera8</developerName>

        <language xsi:nil="true"/>

        <masterLabel>iftheusera</masterLabel>

      </genAiPluginInstructions>

      <genAiPluginInstructions>

        <description>When providing the Activity Types for GetActivitiesTimeline, choose

   all the types that are relevant

          to the user request. Examples - User Request 1 - &quot;What questions does John

    Doe have that need addressing?&quot;,

          Activity Types - &quot;Call&quot;, &quot;Email&quot;.

         User Request 2 - &quot;What are the next activities for John Doe?&quot;, Activity

    Types - &quot;Task&quot;, &quot;Event&quot;.</description>

        <developerName>whenprovid9</developerName>

        <language xsi:nil="true"/>

        <masterLabel>whenprovid</masterLabel>

      </genAiPluginInstructions>

      <genAiPluginInstructions>

        <description>When asked about recent activities, you should provide the answer,

   starting from the last 30 days

         and ending on the current date, unless a specific date range is specified by the

    user.</description>

        <developerName>whenaskeda10</developerName>

        <language xsi:nil="true"/>

        <masterLabel>whenaskeda</masterLabel>

      </genAiPluginInstructions>

      <genAiPluginInstructions>

        <description>When you are asked about a single Call, Meeting, Email or any other

   single specific activity, call GetActivityDetails.</description>

        <developerName>whenyouare11</developerName>

        <language xsi:nil="true"/>

        <masterLabel>whenyouare</masterLabel>

      </genAiPluginInstructions>

      <genAiPluginInstructions>

        <description>Always use DraftOrReviseEmail when asked to generate a new email or

   revise a previously generated email.</description>

        <developerName>alwaysused12</developerName>

        <language xsi:nil="true"/>

        <masterLabel>alwaysused</masterLabel>

      </genAiPluginInstructions>

      <genAiPluginInstructions>

        <description>ExtractRecordFieldsAndValuesFromUserInput must be called prior to

   UpdateRecordFields.</description>

        <developerName>extractrec13</developerName>

        <language xsi:nil="true"/>

```


### Metadata Types GenAiPluginInstructionDef

```
        <masterLabel>extractrec</masterLabel>

      </genAiPluginInstructions>

      <genAiPluginInstructions>

        <description>Avoid using structured lists, bullet points, or numbered lists.

   Instead, present the information in complete sentences

         and paragraphs as if you were writing an article or a report.</description>

        <developerName>avoidusing14</developerName>

        <language xsi:nil="true"/>

        <masterLabel>avoidusing</masterLabel>

      </genAiPluginInstructions>

      <genAiPluginInstructions>

       <description>User questions which can be answered by knowledge articles or documents.

    These questions usually want information,

         instructions or guidance, including but not limited to customer questions about

    company information, policies and frequently asked questions.</description>

        <developerName>userquesti15</developerName>

        <language xsi:nil="true"/>

        <masterLabel>userquesti</masterLabel>

      </genAiPluginInstructions>

      <language>en_US</language>

      <masterLabel>General CRM Customized</masterLabel>

      <pluginType>Topic</pluginType>

      <scope>Your job is to interact and answer questions for the user about anything

   Salesforce or CRM data related,

       combining all data retrieval functions. i.e: QueryRecords(), GetRecordDetails(),

   GetActivitiesTimeline(), GetActivityDetails(), WebSearch()</scope>

   </GenAiPlugin>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <types>

       <members>*</members>

       <name>GenAiPlugin</name>

     </types>

     <version>62.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### GenAiPluginInstructionDef

Represents a topic instruction.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types GenAiPluginInstructionDef

File Suffix and Directory Location

GenAiPluginInstructionDef components are part of a GenAiPlugin component and aren't used separately.

Version

GenAiPluginInstructionDef components are available in API version 62.0 and later.

Special Access Rules

GenAiPluginInstructionDef is available only if Agents is enabled in your org.

Fields

**Field Name** **Description**

```
description

developerName

language

masterLabel

```

**Field Type**
string

**Description**

Required.

Description of the topic instruction.

**Field Type**
string

**Description**

Required.

Represents the API name of the topic instruction. Can contain only underscores and
alphanumeric characters and must be unique in your org. It must begin with a letter,
not include spaces, not end with an underscore, and not contain two consecutive
underscores.

**Field Type**
string

**Description**

Required.

The language of the topic instruction.

**Field Type**
string

**Description**

Required.

The master label for the topic instruction.


### Metadata Types GenAiPromptTemplate

**Field Name** **Description**

```
sortOrder

```

**Field Type**
integer

**Description**
A numerical value used to determine the order the instructions will be executed in.

Declarative Metadata Sample Definition

See GenAiPlugin on page 1378.

### GenAiPromptTemplate

Represents the definition of a prompt template, including its related objects and fields.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

### GenAiPromptTemplate components have the suffix .genAiPromptTemplate and are stored in the

`genAiPromptTemplates` folder.

Version

### GenAiPromptTemplate components are available in API version 60.0 and later.

Special Access Rules

### GenAiPromptTemplate is available only if Prompt Builder is enabled in your org and you have the Prompt Template Manager permission.

Fields

**Field Name** **Description**

activeVersion

**Field Type**
int

**Description**
This tag will be deprecated in 63.0 and will not work in 64.0 and later. Use
activeVersionIdentifier instead.


Metadata Types GenAiPromptTemplate

**Field Name** **Description**

```
activeVersionIdentifier

description

masterLabel

relatedEntity

relatedField

templateVersions

type

```

**Field Type**
string

**Description**
Specifies the version identifier of the active prompt template version. This tag will use
versionIdentifier as the value for the active version.

**Field Type**
string

**Description**
A description of the prompt template.

**Field Type**
string

**Description**
Required. A user-friendly name for GenAiPromptTemplate, which is defined when the
GenAiPromptTemplate is created.

**Field Type**
string

**Description**
The Salesforce record type that the prompt template is associated with.

**Field Type**
string

**Description**
The Salesforce field that the prompt template is associated with.

**Field Type**

GenAiPromptTemplateVersion on page 1388[]

**Description**
Required. An array of prompt template versions.

**Field Type**
string

**Description**
Required. Represents the template type that the prompt template is based on. Valid
values are:

**•** `einstein_gpt__fieldCompletion`

**•** `einstein_gpt__salesEmail`

**•** `einstein_gpt__recordSummary`

**•** `einstein_gpt__flex`

**•** `einstein_gpt__caseEmailDraft`


Metadata Types GenAiPromptTemplate

**Field Name** **Description**

```
visibility

```

**Field Type**
[GenAiPromptTemplateVisibilityType (enumeration of type string)](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_objects_intro.htm#enumeration_title)

**Description**
Indicates the scope of visibility for the prompt template. Valid values are:

**•** `API`

**•** `Global`

GenAiPromptTemplateVersion

Represents a version of a prompt template.

**Field Name** **Description**

```
content

description

generationTemplateConfigs

inputs

primaryModel

status

```

**Field Type**
string

**Description**
Required. Text of the prompt template version.

**Field Type**
string

**Description**
Description of the prompt template version.

**Field Type**

GenAiPromptTemplateGenerationConfig on page 1389[]

**Description**
Reference to the policies for the prompt template version.

**Field Type**

GenAiPromptTemplateInput on page 1390[]

**Description**
An array of prompt template inputs associated with the prompt template version.

**Field Type**
string

**Description**
The model associated with the prompt template version.

**Field Type**
[GenAiPromptTemplateStatus (enumeration of type string)](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_objects_intro.htm)


Metadata Types GenAiPromptTemplate

**Field Name** **Description**

**Description**
Required. Indicates the status of the prompt template in Prompt Builder. Valid values
are:

**•** `Published` —Published version of a prompt template. The active version of the
prompt template must be published.

Published prompt templates can't be edited with UI or Metadata API.

**•** `Draft` —Draft version of a prompt template.

```
templateDataProviders

versionNumber

versionIdentifier

```

**Field Type**

GenAiPromptTemplateDataProvider on page 1390[]

**Description**
An array of prompt template data providers associated with the prompt template
version.

**Field Type**
int

**Description**
Required. Version number of the prompt template version. Versions are counted
sequentially from 1.

This tag will be deprecated in 63.0 and will not work in 64.0 and later. Use
versionIdentifier instead.

**Field Type**
string

**Description**

Version identifier of the prompt template version identifier. This is generated
automatically once a template is deployed and retrieved from an org.

If a unique value is not specified then it will be generated for you. It must be unique
for each version for a given template.

GenAiPromptTemplateGenerationConfig

References the policies for this prompt template version. A policy describes high-level behavior for the prompt template, such as the
allowed languages, conversation style, or desired response length. Currently, a policy is defined in a configuration file.

**Field Name** **Description**

```
generationConfigDeveloperName

```

**Field Type**
string

**Description**
Developer name of the policy for this prompt template version.


Metadata Types GenAiPromptTemplate

GenAiPromptTemplateInput

Represents an input for a prompt template, such as a Salesforce record, field, or Apex primitive data type.

**Field Name** **Description**

```
apiName

definition

description

masterLabel

referenceName

required

```

**Field Type**
string

**Description**
Required. Name of the prompt template input parameter.

**Field Type**
string

**Description**
Required. The URI definition of the input parameter. For example,
`SOBJECT://Account` and `SOBJECT://Account/Description` .

**Field Type**
string

**Description**
Description of the prompt template input parameter.

**Field Type**
string

**Description**
A user-friendly name for GenAiPromptTemplateInput, which is defined when the
GenAiPromptTemplateInput is created.

**Field Type**
string

**Description**
Required. Name of the prompt template input to use in expressions. For example,
`Input:Recipient` and `Input:Sender</referenceName>` .

**Field Type**
boolean

**Description**
Required. Specifies whether this input parameter is required ( `true` ) or optional
( `false` ).

GenAiPromptTemplateDataProvider

Represents a source of data for a prompt template version, such as an invocable action, flow, or Apex method.


Metadata Types GenAiPromptTemplate

**Field Name** **Description**

```
definition

parameters

referenceName

```

**Field Type**
string

**Description**
Required. The URI definition of the data provider, such
as `flow://ns__CallToActionFlow` .

**Field Type**

GenAiPromptTemplateDataProviderParam on page 1391[]

**Description**
An array of parameters associated with the data provider.

**Field Type**
string

**Description**
Required. Name of the data provider to use in expressions.

GenAiPromptTemplateDataProviderParam

Represents a parameter that a data provider uses to retrieve information.

**Field Name** **Description**

```
definition

isRequired

parameterName

valueExpression

```

**Field Type**
string

**Description**
Required. URI definition of the parameter. For example,
`SOBJECT://User</definition>` .

**Field Type**
boolean

**Description**
Required. Specifies whether the parameter is required ( `true` ) or optional ( `false` ).

**Field Type**
string

**Description**
Required. Name of the parameter.

**Field Type**
string


Metadata Types GenAiPromptTemplate

**Field Name** **Description**

**Description**
Value or expression of the parameter to use in prompt template text. For example,
`{!$Input:Recipient}` .

Declarative Metadata Sample Definition

The following is an example of a GenAiPromptTemplate component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <GenAiPromptTemplate xmlns="http://soap.sforce.com/2006/04/metadata">

   <activeVersionIdentifier>a94ACO8feseESrBtllQUNLvKEqlCHiPSDLX5rXUnvPs=_1</activeVersionIdentifier>

      <description>Recommend relevant financial products to client based on their needs and

    goals</description>

      <masterLabel>Recommend Relevant Products</masterLabel>

      <relatedEntity>Contact</relatedEntity>

      <templateVersions>

        <content>You are a financial advisor at {!$Input:Sender.CompanyName} and your name

    is {!$Input:Sender.Name}. You are writing an email to a prospective client recommending

   relevant financial products based on their data and goals. Reference the data below to

   generate your email, recommending only relevant products for the customer that match our

   recommendation criteria for each product.

   Client name: {!$Input:Recipient.Name}

   Client age: {!$Input:Recipient.Age__c}

   Client occupation: {!$Input:Recipient.Occupation__c}

   Client income: {!$Input:Recipient.Income__c}

   Client financial goals: {!$Input:Recipient.Financial_Goals__c}

   {!$Flow:Fetch_Products.Prompt}

   Generate a subject line that can increase the open rate using words and content that is

   related to the email body content. It must be no more than 10 words.

   Start the opening message of the email with an ice-breaker talking about relevant challenges

    or opportunities with personal finance and how you can help.

   Indirectly allude to a point of common interest, shared background, or relevant experience

    with {!$Input:Recipient.Name}. You aim to subtly reference or highlight this connection

   to establish rapport, demonstrate relevance, and foster a sense of familiarity.

   Indirectly encourage the lead {!$Input:Recipient.Name} to respond to your email by showing

    that you are willing to discuss opportunities for working together and answer any questions

    they may have.

   Be concise in your email.</content>

        <inputs>

           <apiName>Sender</apiName>

           <definition>SOBJECT://User</definition>

           <referenceName>Input:Sender</referenceName>

           <required>true</required>

        </inputs>

        <inputs>

           <apiName>Recipient</apiName>

```


### Metadata Types GenAiPromptTemplateActv

```
           <definition>SOBJECT://Contact</definition>

           <referenceName>Input:Recipient</referenceName>

           <required>true</required>

        </inputs>

        <primaryModel>sfdc_ai__DefaultOpenAIGPT4</primaryModel>

        <status>Published</status>

        <templateDataProviders>

           <definition>flow://Fetch_Products</definition>

           <parameters>

             <definition>SOBJECT://User</definition>

             <isRequired>true</isRequired>

             <parameterName>Sender</parameterName>

             <valueExpression>{!$Input:Sender}</valueExpression>

           </parameters>

           <parameters>

             <definition>SOBJECT://Contact</definition>

             <isRequired>true</isRequired>

             <parameterName>Recipient</parameterName>

             <valueExpression>{!$Input:Recipient}</valueExpression>

           </parameters>

           <referenceName>Flow:Fetch_Products</referenceName>

        </templateDataProviders>

        <versionIdentifier>a94ACO8feseESrBtllQUNLvKEqlCHiPSDLX5rXUnvPs=_1

   </versionIdentifier>

      </templateVersions>

      <type>einstein_gpt__salesEmail</type>

      <visibility>Global</visibility>

   </GenAiPromptTemplate>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>GenAiPromptTemplate</name>

      </types>

      <version>60.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### GenAiPromptTemplateActv

Represents the activation status of a Salesforce-provided prompt template.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.


Metadata Types GenAiPromptTemplateActv

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

`GenAiPromptTemplateActv` components have the suffix `.genAiPromptTemplateActivation` and are stored in the
`genAiPromptTemplateActivations` folder.

Version

GenAiPromptTemplateActv components are available in API version 60.0 and later.

Special Access Rules

GenAiPromptTemplate is available only if Prompt Builder is enabled in your org and you have the Prompt Template Manager permission.

Fields

**Field Name** **Description**

```
accessLevel

developerName

masterLabel

templateDeveloperName

```

**Field Type**
[GenAiPromptTemplateActvAccessLevel (enumeration of type string)](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_objects_intro.htm)

**Description**
Indicates which users can access the Salesforce-provided prompt template. Valid values
are:

**•** `Allowed` —Users with access to Prompt Builder can see the prompt template.

**•** `Blocked` —Only admin users with access to Prompt Builder can see the prompt
template.

**Field Type**
string

**Description**
Name of the activation record. This name can contain only underscores and
alphanumeric characters. It must begin with a letter, not include spaces, not end with
an underscore, and not contain two consecutive underscores.

**Field Type**
string

**Description**
A user-friendly name for GenAiPromptTemplateActv, which is defined when the
GenAiPromptTemplateActv is created.

**Field Type**
string


### Metadata Types GiftEntryGridTemplate

**Field Name** **Description**

**Description**
Name of the Salesforce-provided prompt template that the activation record is
associated with.

Declarative Metadata Sample Definition

The following is an example of a GenAiPromptTemplateActv component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <GenAiPromptTemplateActv xmlns="http://soap.sforce.com/2006/04/metadata">

      <MasterLabel> Activation Record for Prompt Template </MasterLabel>

      <PromptTemplateDeveloperName>einstein_gpt__introductionLeadEmail

      </PromptTemplateDeveloperName>

      <DeveloperName>HideIntroductionLeadEmail</DeveloperName>

      <Description>Status of template </Description>

      <AccessLevel>BLOCKED</AccessLevel>

   </GenAiPromptTemplateActv>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <name>GenAiPromptTemplateActv</name>

        <members>HideIntroductionLeadEmail.genAiPromptTemplateActivation</members>

      </types>

      <version>60.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### GiftEntryGridTemplate

Represents templates that customize the gift entry grid in Fundraising.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types GiftEntryGridTemplate

File Suffix and Directory Location

GiftEntryGridTemplate components have the suffix `.giftEntryGridTempate` and are stored in the `giftEntryGridTemplate`
folder.

Version

GiftEntryGridTemplate components are available in API version 66.0 and later.

Special Access Rules

This object is available only if the Fundraising Access license is enabled, the Fundraising User system permission is assigned to users,
and the Gift Entry Grid is enabled.

Fields

**Field Name** **Description**

```
Description

IsSingleGiftDefault

TemplateConfiguration

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the gift entry grid template.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the template is the default template for single gift entry (true) or
not (false, the default).

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The template configuration that includes the data for fields, columns, and components.


Metadata Types GiftEntryGridTemplate

Declarative Metadata Sample Definition

The following is an example of a GiftEntryGridTemplate component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <GiftEntryGridTemplate xmlns="http://soap.sforce.com/2006/04/metadata">

      <description>Demo of Default Template</description>

      <developerName>Demo_of_Default_Template</developerName>

      <isSingleGiftDefault>false</isSingleGiftDefault>

      <masterLabel>Demo of Default Template</masterLabel>

      <templateConfiguration>templateName: Demo of Default Template

   apiVersion: 66.0

   columns:

    
     columnId: Donor

     columnType: Component

     columnField:

      sourceField: DonorId

      isFieldRequired: true

      isFieldHidden: false

     columnComponent:

      componentNameDisplay: runtime_industries_frops/giftEntryGridColumnDisplay

      componentNameEdit: runtime_industries_frops/giftEntryGridLookup

     columnModal:

      modalTitleLabel: $Label.GiftEntryGrid.AddDonorDetailsModalTitle

      modalComponent:

       componentName: runtime_industries_frops/giftEntryGridFieldsModal

      modalIcon:

       expandIcon: utility:expand_alt

       expandIconAltText: $Label.GiftEntryGrid.DonorExpandIconAltText

       lockIcon: utility:lock

       lockIconAltText: $Label.GiftEntryGrid.LockIconAltText

       noIconAltText: &quot;&quot;

      isModalReadOnly: false

      modalAltTitleLabel: $Label.GiftEntryGrid.EditDonorDetailsModalTitle

      modalAltTitleLabelVisibilityRule:

      
       field: DonorId

       values:

        - null

       operator: NOT_EQUALS

       multipleRulesEvaluationOperator: AND

      modalFields:

      
       sourceField: GiftType

       fieldLabel: $Label.GiftEntryGrid.DonorType

       isFieldRequired: true

       isFieldHidden: false

       defaultValue: Individual

       fieldReadOnlyRule:

        
        field: DonorId

        values:

         - null

        operator: NOT_EQUALS

```


Metadata Types GiftEntryGridTemplate

```
        multipleRulesEvaluationOperator: AND

      
       sourceField: OrganizationName

       isFieldRequired: true

       isFieldHidden: false

       visibilityRules:

        
        field: GiftType

        values:

         - Organizational

        operator: EQUALS

        multipleRulesEvaluationOperator: AND

      
       sourceField: Salutation

       isFieldRequired: false

       isFieldHidden: false

       visibilityRules:

        
        field: GiftType

        values:

         - Individual

        operator: EQUALS

        multipleRulesEvaluationOperator: AND

      
       sourceField: FirstName

       isFieldRequired: false

       isFieldHidden: false

       visibilityRules:

        
        field: GiftType

        values:

         - Individual

        operator: EQUALS

        multipleRulesEvaluationOperator: AND

      
       sourceField: LastName

       isFieldRequired: true

       isFieldHidden: false

       visibilityRules:

        
        field: GiftType

        values:

         - Individual

        operator: EQUALS

        multipleRulesEvaluationOperator: AND

      
       sourceField: Email

       isFieldRequired: false

       isFieldHidden: false

       visibilityRules:

        
        field: GiftType

        values:

         - Individual

```


Metadata Types GiftEntryGridTemplate

```
        operator: EQUALS

        multipleRulesEvaluationOperator: AND

      
       sourceField: HomePhone

       isFieldRequired: false

       isFieldHidden: false

       visibilityRules:

        
        field: GiftType

        values:

         - Individual

        operator: EQUALS

        multipleRulesEvaluationOperator: AND

      
       sourceField: MobilePhone

       isFieldRequired: false

       isFieldHidden: false

       visibilityRules:

        
        field: GiftType

        values:

         - Individual

        operator: EQUALS

        multipleRulesEvaluationOperator: AND

      
       sourceField: MobilePhone

       fieldLabel: $Label.GiftEntryGrid.OrganizationPhone

       isFieldRequired: false

       isFieldHidden: false

       visibilityRules:

        
        field: GiftType

        values:

         - Organizational

        operator: EQUALS

        multipleRulesEvaluationOperator: AND

      
       sourceField: Street

       isFieldRequired: false

       isFieldHidden: false

      
       sourceField: City

       isFieldRequired: false

       isFieldHidden: false

      
       sourceField: State

       isFieldRequired: false

       isFieldHidden: false

      
       sourceField: PostalCode

       isFieldRequired: false

       isFieldHidden: false

      
       sourceField: Country

```


Metadata Types GiftEntryGridTemplate

```
       isFieldRequired: false

       isFieldHidden: false

     isColumnHidden: false

     isColumnReadOnly: false

     columnWidth: 240

     columnLabel: $Label.GiftEntryGrid.DonorLookup

    
     columnId: GiftReceivedDate

     columnType: Field

     columnField:

      sourceField: GiftReceivedDate

      isFieldRequired: true

      isFieldHidden: false

     isColumnHidden: false

     isColumnReadOnly: false

     columnWidth: 180

     columnLabel: GiftReceivedDate

    
     columnId: Commitments

     columnType: Component

     columnField:

      sourceField: GiftCommitmentId

      isFieldRequired: false

      isFieldHidden: false

     columnComponent:

      componentNameDisplay: runtime_industries_frops/giftEntryGridColumnDisplay

      componentNameEdit: runtime_industries_frops/giftEntryGridCommitmentColEdit

     columnModal:

      modalTitleLabel: $Label.GiftEntryGrid.NewCommitmentModalTitle

      modalComponent:

       componentName: runtime_industries_frops/giftEntryGridFieldsModal

      modalIcon:

       expandIcon: utility:expand_alt

       expandIconAltText: $Label.GiftEntryGrid.CommitmentExpandIconAltText

       lockIcon: utility:lock

       lockIconAltText: $Label.GiftEntryGrid.LockIconAltText

       noIconAltText: &quot;&quot;

      isModalReadOnly: false

      modalAltTitleLabel: $Label.GiftEntryGrid.ViewCommitmentModalTitle

      modalAltTitleLabelVisibilityRule:

      
       field: GiftCommitmentId

       values:

        - null

       operator: NOT_EQUALS

       multipleRulesEvaluationOperator: AND

      modalFields:

      
       sourceField: EffectiveStartDate

       fieldLabel: $Label.GiftEntryGrid.CommitmentEffectiveStartDateLabel

       isFieldRequired: true

       isFieldHidden: false

       fieldReadOnlyRule:

        
```


Metadata Types GiftEntryGridTemplate

```
        field: GiftCommitmentId

        values:

         - null

        operator: NOT_EQUALS

        multipleRulesEvaluationOperator: AND

      
       sourceField: ExpectedEndDate

       fieldLabel: $Label.GiftEntryGrid.CommitmentExpectedEndDateLabel

       isFieldRequired: false

       isFieldHidden: false

       fieldReadOnlyRule:

        
        field: GiftCommitmentId

        values:

         - null

        operator: NOT_EQUALS

        multipleRulesEvaluationOperator: AND

      
       sourceField: TransactionPeriod

       isFieldRequired: true

       isFieldHidden: false

       fieldReadOnlyRule:

        
        field: GiftCommitmentId

        values:

         - null

        operator: NOT_EQUALS

        multipleRulesEvaluationOperator: AND

      
       sourceField: TransactionInterval

       isFieldRequired: true

       isFieldHidden: false

       fieldReadOnlyRule:

        
        field: GiftCommitmentId

        values:

         - null

        operator: NOT_EQUALS

        multipleRulesEvaluationOperator: AND

      
       sourceField: TransactionDay

       isFieldRequired: true

       isFieldHidden: false

       visibilityRules:

        
        field: TransactionPeriod

        values:

         - Monthly

        operator: EQUALS

        multipleRulesEvaluationOperator: AND

       fieldReadOnlyRule:

        
        field: GiftCommitmentId

        values:

```


Metadata Types GiftEntryGridTemplate

```
         - null

        operator: NOT_EQUALS

        multipleRulesEvaluationOperator: AND

     isColumnHidden: false

     isColumnReadOnly: false

     columnWidth: 240

     columnLabel: $Label.GiftEntryGrid.CommitmentColumnLabel

    
     columnId: GiftAmount

     columnType: Field

     columnField:

      sourceField: GiftAmount

      isFieldRequired: false

      isFieldHidden: false

     isColumnHidden: false

     isColumnReadOnly: false

     columnWidth: 160

     columnLabel: GiftAmount

    
     columnId: PaymentMethod

     columnType: Field

     columnField:

      sourceField: PaymentMethod

      isFieldRequired: true

      isFieldHidden: false

     columnModal:

      modalTitleLabel: $Label.GiftEntryGrid.PaymentInformationModalTitle

      modalComponent:

       componentName: runtime_industries_frops/giftEntryGridFieldsModal

      modalIcon:

       expandIcon: utility:expand_alt

       expandIconAltText: $Label.GiftEntryGrid.PaymentMethodIconAltText

       lockIcon: utility:lock

       lockIconAltText: $Label.GiftEntryGrid.LockIconAltText

       noIconAltText: &quot;&quot;

      isModalReadOnly: false

      modalFields:

      
       sourceField: PaymentMethod

       isFieldRequired: true

       isFieldHidden: false

      
       sourceField: Last4

       isFieldRequired: false

       isFieldHidden: false

       visibilityRules:

        
        field: PaymentMethod

        values:

         - Credit Card

         - ACH

        operator: EQUALS

        multipleRulesEvaluationOperator: AND

      
```


Metadata Types GiftEntryGridTemplate

```
       sourceField: ExpiryMonth

       isFieldRequired: false

       isFieldHidden: false

       visibilityRules:

        
        field: PaymentMethod

        values:

         - Credit Card

        operator: EQUALS

        multipleRulesEvaluationOperator: AND

      
       sourceField: ExpiryYear

       isFieldRequired: false

       isFieldHidden: false

       visibilityRules:

        
        field: PaymentMethod

        values:

         - Credit Card

        operator: EQUALS

        multipleRulesEvaluationOperator: AND

      
       sourceField: CheckDate

       isFieldRequired: false

       isFieldHidden: false

       visibilityRules:

        
        field: PaymentMethod

        values:

         - Check

        operator: EQUALS

        multipleRulesEvaluationOperator: AND

      
       sourceField: PaymentIdentifier

       isFieldRequired: false

       isFieldHidden: false

       visibilityRules:

        
        field: PaymentMethod

        values:

         - Check

        operator: EQUALS

        multipleRulesEvaluationOperator: AND

     isColumnHidden: false

     isColumnReadOnly: false

     columnWidth: 180

     columnLabel: PaymentMethod

    
     columnId: OutreachSourceCode

     columnType: Field

     columnField:

      sourceField: OutreachSourceCodeId

      isFieldRequired: false

      isFieldHidden: false

```


Metadata Types GiftEntryGridTemplate

```
     isColumnHidden: false

     isColumnReadOnly: false

     columnWidth: 200

     columnLabel: $Label.GiftEntryGrid.OutreachSourceCodeLookup

    
     columnId: Campaign

     columnType: Field

     columnField:

      sourceField: CampaignId

      isFieldRequired: false

      isFieldHidden: false

     isColumnHidden: false

     isColumnReadOnly: false

     columnWidth: 200

     columnLabel: $Label.GiftEntryGrid.CampaignLookup

    
     columnId: Designations

     columnType: Component

     columnField:

      sourceField: GiftDesignation1Id

      isFieldRequired: false

      isFieldHidden: false

     columnComponent:

      componentNameDisplay: runtime_industries_frops/giftEntryGridColumnDisplay

      componentNameEdit: runtime_industries_frops/giftEntryGridLookup

     columnModal:

      modalTitleLabel: $Label.GiftEntryGrid.DesignationsModalTitle

      modalComponent:

       componentName: runtime_industries_frops/giftEntryGridDesignation

      modalIcon:

       expandIcon: utility:expand_alt

       expandIconAltText: $Label.GiftEntryGrid.DesignationExpandIconAltText

       lockIcon: utility:lock

       lockIconAltText: $Label.GiftEntryGrid.LockIconAltText

       noIconAltText: &quot;&quot;

      isModalReadOnly: false

     isColumnHidden: false

     isColumnReadOnly: false

     columnWidth: 240

     columnLabel: $Label.GiftEntryGrid.DesignationsLookup

    
     columnId: SoftCredits

     columnType: Component

     columnField:

      sourceField: RecipientId

      isFieldRequired: false

      isFieldHidden: false

     columnComponent:

      componentNameDisplay: runtime_industries_frops/giftEntryGridColumnDisplay

      componentNameEdit: runtime_industries_frops/giftEntryGridLookup

     columnModal:

      modalTitleLabel: $Label.GiftEntryGrid.SoftCreditsModalTitle

      modalComponent:

       componentName: runtime_industries_frops/giftEntryGridSoftCredit

```


### Metadata Types GlobalPicklist

```
      modalIcon:

       expandIcon: utility:expand_alt

       expandIconAltText: $Label.GiftEntryGrid.SoftCreditsExpandIconAltText

       lockIcon: utility:lock

       lockIconAltText: $Label.GiftEntryGrid.LockIconAltText

       noIconAltText: &quot;&quot;

      isModalReadOnly: false

     isColumnHidden: false

     isColumnReadOnly: false

     columnWidth: 240

     columnLabel: $Label.GiftEntryGrid.SoftCreditsLookup</templateConfiguration>

   </GiftEntryGridTemplate>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>GiftEntryGridTemplate</name>

      </types>

      <version>66.0</version>

   </Package>

### GlobalPicklist

```

Represents a global picklist, or the set of shared picklist values that custom picklist fields can use. In contrast, the custom picklist fields
that are based on a global picklist are of type CustomValue. This type extends the Metadata metadata type and inherits its `fullName`
field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### GlobalPicklist components have the suffix .globalPicklist and are stored in the globalPicklist folder.

Version

### GlobalPicklist components are available in API version 37.0 only. In API version 38.0 and later, GlobalPicklist is replaced by the GlobalValueSet

type.

Fields

**Field Name** **Field Type** **Description**

`description` string It’s useful to state the global picklist’s purpose, and which objects it’s intended
for. Limit: 255 characters.


Metadata Types GlobalPicklist

**Field Name** **Field Type** **Description**

`globalPicklistValues` GlobalPicklistValue[] Requires at least one value. The list of values, or “picklist value set,” that’s defined
for a global picklist. The picklist value set is inherited by any custom picklist

field that’s based on that global picklist. Each value is of type GlobalPicklistValue.
A global picklist can have up to 1,000 total values, including inactive values.

`masterLabel` string Required. A global picklist’s name, which is defined when the global picklist is
created. Appears as Label in the user interface.

`sorted` string Indicates whether a global picklist’s value set is sorted in alphabetical order.
By default this value is `false` .

Declarative Metadata Sample Definition

This Territories.globalPicklist is an example of a GlobalPicklist component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <GlobalPicklist xmlns="http://soap.sforce.com/2006/04/metadata">

      <description>Updated:This is a basic global picklist</description>

      <globalPicklistValues>

        <fullName>Northwest</fullName>

        <default>false</default>

      </globalPicklistValues>

      <globalPicklistValues>

        <fullName>Northeast</fullName>

        <default>false</default>

      </globalPicklistValues>

      <globalPicklistValues>

        <fullName>South</fullName>

        <default>true</default>

      </globalPicklistValues>

      <globalPicklistValues>

        <fullName>Southwest</fullName>

        <default>false</default>

        <isActive>false</isActive>

      </globalPicklistValues>

      <masterLabel>Territories</masterLabel>

      <sorted>true</sorted>

   </GlobalPicklist>

```

This example `package.xml` references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Territories</members>

        <name>GlobalPicklist</name>

      </types>

      <version>37.0</version>

   </Package>

```


### Metadata Types GlobalPicklistValue GlobalPicklistValue

Represents the definition of a value used in a global picklist. Custom picklist fields can inherit the picklist value set from a global picklist.

This type extends the Metadata metadata type and inherits its `fullName` field.

Note: GlobalPicklistValue components don’t have file suffixes or directories because they’re lists of values and not custom fields.
For file-based operations they can be accessed through GlobalPicklist (which is in API v37.0 only).

Version

### GlobalPicklistValue components are available in API version 37.0 only. In API version 38.0 and later, GlobalPicklistValue is replaced by

CustomValue on page 838.

Fields

**Field Name** **Field Type** **Description**

`color` string The color assigned to the picklist value when it’s used in charts on reports
and dashboards. The color is in hexadecimal format; for example,

#FF6600. If a color is not specified, it’s assigned dynamically upon chart
generation.

`default` boolean

`description` string

Required. Indicates whether this value is the default selection for the
global picklist and the custom picklists that share its picklist value set.
This field is set to _`true`_ by default.

The global picklist value’s description. It’s useful to include a description
for a global picklist value so the reason for creating it can be tracked.
Limit: 255 characters.

`isActive` boolean Indicates whether this value is currently active or inactive. The default
value is _`true`_ . Users can select only active values from a picklist. An API

retrieve operation for global picklist values returns all active and inactive
values in the picklist. (Meanwhile, retrieving the values of a non-global,
unrestricted picklist returns only the active values.)

PicklistValue

This metadata type defines a value in the picklist and specifies whether this value is the default value. This type extends the
### GlobalPicklistValue metadata type and inherits all its fields. In API version 36.0 and earlier, PicklistValue extends the Metadata type and

inherits its `fullName` field.

Note the following when working with picklist values:

**•** When you retrieve a standard object, all picklist values are retrieved, not just the customized picklist values.

**•** When you deploy changes to standard picklist fields, picklist values are added as needed.

**•** To deactivate a global picklist value, you can invoke an `update()` call on GlobalPicklist with the value omitted, or with the value’s
`isActive` field set to `false` . Or, you can invoke an `update()` call directly on GlobalPicklistValue with the `isActive` field
set to `false` .


Metadata Types GlobalPicklistValue

**•** If picklist values are missing from a component definition, they get deactivated when deployed. Deactivation occurs for picklist
values of both standard and custom fields.

**Field Name** **Field Type** **Description**

`allowEmail` boolean

Indicates whether this value lets users email a quote PDF ( `true` ), or not
( `false` ). This field is only relevant for the `Status` field in quotes.This
field is available in API version 18.0 and later.

`closed` boolean Indicates whether this value is associated with a closed status ( `true` ),
or not ( `false` ). This field is only relevant for the standard `Status`

field in cases and tasks. This field is available in API version 16.0 and up
to version 36.0. In version 37.0, this field is in GlobalPicklistValue.

`controllingFieldValues` string[] A list of values in the controlling field that are linked to this picklist value.
The controlling field can be a checkbox or a picklist. This field is available

in API version 14.0 and later. The values in the list depend on the field
type:

**•** `Checkbox` : `checked` or `unchecked` .

**•** `Picklist` : The `fullname` of the picklist value in the controlling
field.

`converted` boolean Indicates whether this value is associated with a converted status ( `true` ),
or not ( `false` ). This field is relevant for only the standard `Lead`

`Status` field in leads. Your organization can set its own guidelines for
determining when a lead is qualified, but typically, you want to convert
a lead as soon as it becomes a real opportunity that you want to forecast.
For more information, see “Convert Qualified Leads” in the Salesforce
online help. This field is available in API version 16.0 and later.

`cssExposed` boolean

Indicates whether this value is available in your Self-Service Portal ( `true` ),
or not ( `false` ). This field is only relevant for the standard `Case`
`Reason` field in cases.

Self-Service provides an online support channel for your customers allowing them to resolve their inquiries without contacting a customer

service representative. For more information about Self-Service, see
“Setting Up Your Self-Service Portal” in the Salesforce online help.

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


```
forecastCategory

```

ForecastCategories
(enumeration of
type string)

### Metadata Types GlobalValueSet

**Field Name** **Field Type** **Description**

**•** Forecast

**•** Closed

This field is available in API version 16.0 and later.

`highPriority` boolean Indicates whether this value is a high priority item ( `true` ), or not
( `false` ). This field is only relevant for the standard `Priority` field

in tasks. For more information about tasks, see “Start Using Tasks” in the
Salesforce online help. This field is available in API version 16.0 and later.

`probability` int

Indicates whether this value is a probability percentage ( `true` ), or not
( `false` ). This field is only relevant for the standard `Stage` field in
opportunities. This field is available in API version 16.0 and later.

`reverseRole` string A picklist value corresponding to a reverse role name for a partner. If the
role is “subcontractor”, then the reverse role might be “general

contractor”. Assigning a partner role to an account in Salesforce creates
a reverse partner relationship so that both accounts list the other as a
partner. This field is only relevant for partner roles.

For more information, see “Partner Fields” in the Salesforce online help.

This field is available in API version 18.0 and later.

`reviewed` boolean Indicates whether this value is associated with a reviewed status ( `true` ),
or not ( `false` ). This field is only relevant for the standard `Status`

field in solutions. For more information about opportunities, see “Creating
Solutions” in the Salesforce online help. This field is available in API
version 16.0 and later.

`won` boolean Indicates whether this value is associated with a closed or won status
( `true` ), or not ( `false` ). This field is only relevant for the standard

`Stage` field in opportunities. This field is available in API version 16.0
and later.

Declarative Metadata Sample Definition

For an example of GlobalPicklistValue components with a `package.xml` that references them, see GlobalPicklist.

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

### GlobalValueSet

Represents the metadata for a global picklist value set, which is the set of shared values that custom picklist fields can use. A global value
set isn’t a field itself. In contrast, the custom picklist fields that are based on a global picklist are of type ValueSet. This type extends the
Metadata metadata type and inherits its `fullName` field.


Metadata Types GlobalValueSet

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

GlobalValueSet components have the suffix `.globalValueSet` and are stored in the `globalValueSets` folder.

Version

GlobalValueSet components are available in API version 38.0 and later. In API version 37.0, this component is the GlobalPicklist type.

Fields

**Field Name** **Field Type** **Description**

`customValue` CustomValue[] Requires at least one value. The list of values, or “global value set,” that’s defined
for a global picklist. The global value set is inherited by any custom picklist field

that uses that value set. Each value is of type customValue. A global value set
can have up to 1,000 total values, including inactive values.

`description` string It’s useful to state the global value set’s purpose and which objects it’s intended
for. Limit: 255 characters.

`masterLabel` string Required. A global value set’s name, which is defined when the global value
set is created. Appears as Label in the user interface.

`sorted` boolean Required. Indicates whether a global value set is sorted in alphabetical order.
By default this value is `false` .

Declarative Metadata Sample Definition

This UpsellGlobal.globalValueSet is an example of a GlobalValueSet component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <GlobalValueSet xmlns="http://soap.sforce.com/2006/04/metadata">

     <description>Updated:This is a basic global value set.</description>

     <masterLabel>UpsellGlobal</masterLabel>

     <customValue>

       <fullName>Maybe</fullName>

       <default>false</default>

       <label>Maybe</label>

     </customValue>

     <customValue>

       <fullName>No</fullName>

       <default>false</default>

       <label>No</label>

     </customValue>

     <customValue>

       <fullName>Yes</fullName>

       <default>false</default>

```


### Metadata Types GlobalValueSetTranslation

```
       <label>Yes</label>

     </customValue>

     <sorted>false</sorted>

   </GlobalValueSet>

```

This example `package.xml` references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>UpsellGlobal</members>

        <name>GlobalValueSet</name>

      </types>

      <version>40.0</version>

   </Package>

```

Any global value set created in API version 57.0 or later automatically has the `__gvs` suffix appended to the developer name. When
you make any CRUD-based call with the GlobalValueSet type, you must append the suffix to the fullName field when you reference the
type.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### GlobalValueSetTranslation

Contains details for a global value set translation. Global value sets are lists of values that can be shared by multiple custom picklist fields,
optionally across objects. This type extends the Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### GlobalValueSetTranslation components have the suffix .globalValueSetTranslation and are stored in the

`globalValueSetTranslations` folder.

Translations are stored in a file with a format of `ValueSetName-lang.globalValueSetTranslation`, where
_`ValueSetName`_ is the global value set’s name, and _`lang`_ is the translation language.

Version

### GlobalValueSetTranslation components are available in API version 38.0 and later.


Metadata Types GlobalValueSetTranslation

Fields

**Field** **Field Type** **Description**

`valueTranslation` ValueTranslation[]

ValueTranslation

The translated name of a value in a translated global value set.
Each `valueTranslation` is paired with a `masterLabel`,
which is the original (untranslated) name of the value.

The original value name and the translated value name in a translated global value set.

**Field** **Field Type** **Description**

`masterLabel` string

Required. The original (untranslated) name of a value in a global
value set. Each `valueTranslation` has a `masterLabel`
paired with its `translation` .

`translation` string The translated name of a value in a translated global value set.

Declarative Metadata Sample Definition

This example shows a GlobalValueSetTranslation component. When a value isn’t translated, its translation becomes a comment that’s
paired with its masterLabel.

```
<?xml version="1.0" encoding="UTF-8"?>

<GlobalValueSetTranslation xmlns="http://soap.sforce.com/2006/04/metadata">

   <valueTranslation>

     <masterLabel>Three</masterLabel>

     <translation>Trois</translation>

   </valueTranslation>

   <valueTranslation>

     <masterLabel>Four</masterLabel>

     <translation>Quatre</translation>

   </valueTranslation>

   <valueTranslation>

     <masterLabel>Five</masterLabel>

     <translation><!-- Five --></translation>

   </valueTranslation>

</GlobalValueSetTranslation>

```

This example is a `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <types>

     <members>Numbers-fr</members>

     <name>GlobalValueSetTranslation</name>

   </types>

   <version>38.0</version>

</Package>

```


### Metadata Types GoogleAppsSettings

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

Translations

### GoogleAppsSettings

Represents the settings for Google Apps in Salesforce.

This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.

File Suffix and Directory Location

A GoogleAppsSettings component file has the suffix `.settings` and is stored in the `settings` directory. The `.settings` files
are different from other named components because there’s only one settings file for each settings component.

Version

### GoogleAppsSettings components are available in API version 46.0 and later.

Fields

**Field Name** **Field Type** **Description**

`enableGmailButtons` boolean Indicates whether the Gmail Buttons setting is enabled ( `true` ) or not
( `false` ).

`enableGmailButtonsAndLinks` boolean Indicates whether Gmail Buttons and Links are enabled ( `true` ) or not
( `false` ).

`enableGmailLinks` boolean Indicates whether the Gmail Links setting is enabled ( `true` ) or not
( `false` ).

`enableGoogleDocs` boolean Indicates whether the Add Google Docs to Salesforce setting is enabled
( `true` ) or not ( `false` ).

`enableGoogleDocsTab` boolean Indicates whether the Add Google Docs button on the Libraries tab is
enabled ( `true` ) or not ( `false` ).

`enableGoogleTalk` boolean Indicates whether the Google Talk Sidebar Component is enabled ( `true` )
or not ( `false` ).

`googleAppsDomain` string Specifies the domain registered for your organization’s Google Apps
account.


### Metadata Types Group

Declarative Metadata Sample Definition

The following is an example of a GoogleAppsSettings component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <GoogleAppsSettings xmlns="http://soap.sforce.com/2006/04/metadata">

      <enableGmailButtons>false</enableGmailButtons>

      <enableGmailButtonsAndLinks>false</enableGmailButtonsAndLinks>

      <enableGmailLinks>false</enableGmailLinks>

      <enableGoogleDocs>false</enableGoogleDocs>

      <enableGoogleDocsTab>false</enableGoogleDocsTab>

      <enableGoogleTalk>false</enableGoogleTalk>

      <googleAppsDomain>example.com</googleAppsDomain>

      <googleAppsDomainLinked>false</googleAppsDomainLinked>

      <googleAppsDomainValidated>false</googleAppsDomainValidated>

   </GoogleAppsSettings>

```

Example Package Manifest

The following is an example package manifest used to deploy or retrieve the Google Apps settings metadata for an organization:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

    <types>

     <members>GoogleApps</members>

     <name>Settings</name>

    </types>

    <version>46.0</version>

   </Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### Group

Represents a set of public groups, which can have users, roles, and other groups.

Declarative Metadata File Suffix and Directory Location

The file suffix for group components is `.group` and components are stored in the `groups` directory of the corresponding package
directory.

Version

### Group components are available in API version 24.0 and later.


### Metadata Types HomePageComponent

Special Access Rules

As of Spring ’20 and later, only authenticated internal and external users can access this type.

Fields

Note: Members of the public group are not migrated when you deploy the group type.

This metadata type represents the valid values that define a group:

**Field Name** **Field Type** **Description**

`description` string The description for the group. Available in API version 62.0 and later.

`doesIncludeBosses` boolean Indicates whether records shared with users in this group are also shared
with users higher in the role hierarchy ( `true` ) or not ( `false` ). This field

is only available for public groups. This field corresponds to the Grant
Access Using Hierarchies checkbox in Setup.

`fullName` string The unique identifier for API access. The `fullName` can contain only
underscores and alphanumeric characters. It must be unique, begin with

a letter, not include spaces, not end with an underscore, and not contain
two consecutive underscores. This field is inherited from the Metadata
component. Corresponds to **Group Name** in the user interface.

`name` string Required. The name of the group. Corresponds to **Label** in the user
interface.

Declarative Metadata Sample Definition

The following is the definition of a group.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Group xmlns="http://soap.sforce.com/2006/04/metadata">

      <doesIncludeBosses>true</doesIncludeBosses>

      <fullName>admin</fullName>

      <name>test</name>

   </Group>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### HomePageComponent

Represents the metadata associated with a home page component. You can customize the Home tab in Salesforce Classic to include
components such as sidebar links, a company logo, a dashboard snapshot, or custom components that you create. Use to create, update,
or delete home page component definitions.


Metadata Types HomePageComponent

[For more information, see “Salesforce Classic Home Tab Page Layouts” in the Salesforce Help.](https://help.salesforce.com/s/articleView?id=platform.customize_homepage.htm&type=5&language=en_US)

This type extends the Metadata metadata type and inherits its `fullName` field.

Declarative Metadata File Suffix and Directory Location

The file suffix for home page components is `.homePageComponent` and components are stored in the `homepagecomponents`
directory of the corresponding package directory.

Version

Home page components are available in API version 12.0 and later.

HomePageComponent

This metadata type represents the valid values that define a home page component:

**Field Name** **Field Type** **Description**

`body` string The text body inside the HTML page component.

`fullName` string

`height` int

The name can only contain characters, letters, and the underscore (_)
character. The name must start with a letter, and can’t end with an
underscore or contain two consecutive underscore characters.

Inherited from the Metadata component, this field isn’t defined in the
WSDL for this component. It must be specified when creating, updating,
or deleting. See create() to see an example of this field specified for a call.

Required for Visualforce Area components. Indicates the height (in pixels)
of the component.

This field is available in API version 31.0 and later.

`links` string[] If the `pageComponentType` is `links`, then zero or more names
of custom page links can be specified.

**•** `ObjectWebLink`

**•** `CustomPageWebLink`

`page` string

This field is only available for Visualforce Area components and indicates
the API name of the Visualforce page that is associated with the
component.

This field is available in API version 31.0 and later.

```
pageComponentType

```

PageComponentType Required. Valid values are:
(enumeration of type

**•** `links`

string)

**•** `links`

**•** `htmlArea`

**•** `imageOrNote`


Metadata Types HomePageComponent

**Field Name** **Field Type** **Description**

**•** `visualforcePage` (This value is available in API version 31.0
and later.)

`showLabel` boolean

`showScrollbars` boolean

This field is only available for Visualforce Area components and specifies
whether the component displays with a label ( `true` ) or not ( `false` ).

This field is available in API version 31.0 and later.

This field is only available for Visualforce Area components and specifies
whether the component displays with scrollbars ( `true` ) or not ( `false` ).

This field is available in API version 31.0 and later.

This field is only available for HTML and Visualforce Area components,
and indicates whether it’s a narrow or wide home page component. Valid
values are:

**•** `narrowComponents`

**•** `wideComponents`

```
width

```

PageComponentWidth
(enumeration of type
string)

Declarative Metadata Sample Definition

The following is the definition of a home page component. See Declarative Metadata Sample Definition and Declarative Metadata Sample
Definition for related samples.

```
<?xml version="1.0" encoding="UTF-8"?>

<HomePageComponent xmlns="http://soap.sforce.com/2006/04/metadata">

  <height>200</height>

  <page>MyVisualforcePage</page>

  <pageComponentType>visualforcePage</pageComponentType>

  <showLabel>true</showLabel>

  <showScrollbars>true</showScrollbars>

  <width>wideComponents</width>

</HomePageComponent>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

HomePageLayout

WebLink


### Metadata Types HomePageLayout HomePageLayout

Represents the metadata associated with a home page layout. You can customize home page layouts and assign the layouts to users
based on their user profile.

File Suffix and Directory Location

Home page layouts are stored in the `homePageLayouts` directory of the corresponding package directory. The extension is
`.homePageLayout` .

Version

Home page components are available in API version 12.0 and later. This type extends the Metadata metadata type and inherits its
`fullName` field.

Fields

This metadata type represents the valid values that define a home page layout:

**Field Name** **Field Type** **Description**

`fullName` string

The name can only contain characters, letters, and the underscore (_)
character. The name must start with a letter, and can’t end with an
underscore or contain two consecutive underscore characters.

Inherited from the Metadata component, this field isn’t defined in the
WSDL for this component. It must be specified when creating, updating,
or deleting. See create() to see an example of this field specified for a call.

`narrowComponents` string[] The list of elements in the narrow column on the left side of the home
page.

`wideComponents` string[] The list of elements in the wide column on the right side of the home
page.

Declarative Metadata Sample Definition

The following is the definition of a home page layout. See Declarative Metadata Sample Definition on page 1417 and Declarative Metadata
Sample Definition on page 806 for related samples.

```
<?xml version="1.0" encoding="UTF-8"?>

<HomePageLayout xmlns="http://soap.sforce.com/2006/04/metadata">

   <narrowComponents>google</narrowComponents>

</HomePageLayout>

```


### Metadata Types IdentityVerificationProcDef

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

HomePageComponent

WebLink

### IdentityVerificationProcDef

Represents the definition of the identity verification process.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### IdentityVerificationProcDef components have the suffix .IdentityVerificationProcDef and are stored in the IdentityVerificationProcDefs folder.

Version

### IdentityVerificationProcDef components are available in API version 54.0 and later.

Special Access Rules

The Health Cloud permission set license is required to use this metadata type.

Fields

**Field Name** **Description**

```
identityVerificationProcDtls

masterLabel

```

**Field Type**

IdentityVerificationProcDtl[]

**Description**
A list of Identity Verification Process Detail elements.

**Field Type**
string


Metadata Types IdentityVerificationProcDef

**Field Name** **Description**

**Description**

Required.

The label of the Identity Verification Process Definition record.

```
searchLayoutType

```

**Field Type**
IdentityVerificationSearchLayoutType (enumeration of type string)

**Description**

Required.

The display layout of the search component.

Valid values are:

**•** `Stack`

**•** `Tab`

IdentityVerificationProcDtl

Represents the verification-related details such as search criteria, verification criteria, or the custom apex class.

**Field Name** **Description**

```
apexClass

dataSourceType

developerName

```

**Field Type**
string

**Description**
The Apex class that is used to search and verify data in an external system.

**Field Type**
IdentityVerificationDataSourceType (enumeration of type string)

**Description**

Required.

The source type of the data.

Valid values are:

**•** `External`

**•** `Salesforce`

**Field Type**
string

**Description**

Required.

The developer name of Identity verification process detail. Can contain only underscores
and alphanumeric characters and must be unique in your org. It must begin with a


Metadata Types IdentityVerificationProcDef

**Field Name** **Description**

letter, not include spaces, not end with an underscore, and not contain two consecutive
underscores.

```
displayRecordFieldName

identityVerificationProcFlds

isActive

isRetryAllowedAfterLimit

linkedIdVerfProcessDet

masterLabel

objectName

```

**Field Type**
string

**Description**
The name of the field that contains information about the record that's shown to the
user after identity verification is successful. Available in API version 58.0 and later.

**Field Type**

IdentityVerificationProcFld[]

**Description**
A list of Identity Verification Process Field elements.

**Field Type**
boolean

**Description**
Indicates whether the record is active ( `true` ) or not ( `false` ).

**Field Type**
boolean

**Description**
For internal use only.

**Field Type**
string

**Description**
The record containing the details of the linked identity verification process. Available
in API version 58.0 and later.

**Field Type**
string

**Description**

Required.

The label of the Identity Verification Process Detail record.

**Field Type**
string

**Description**
The name of the object on which the search is performed and data is verified.


Metadata Types IdentityVerificationProcDef

**Field Name** **Description**

```
optionalVerifiersMinVerfCount

retryLimit

searchFilter

searchRecordUniqueIdField

searchResultSortBy

searchSequenceNumber

searchType

```

**Field Type**
int

**Description**
The number of optional verifiers that must be checked.

**Field Type**
int

**Description**
For internal use only.

**Field Type**
string

**Description**
A comma-separated list of predefined filter conditions that are used to refine the scope
of the search.

**Field Type**
string

**Description**
The field storing the unique identifier of a record displayed in the search results.

**Field Type**
string

**Description**
The values that are used to sort the search results.

**Field Type**
int

**Description**

Required.

The sequence in which the search is performed and the search result is displayed.

**Field Type**
IdentityVerificationSearchType (enumeration of type string)

**Description**

Required.

The type of search being performed.

Valid values are:

**•** `Object-Based`

**•** `Text-Based`


Metadata Types IdentityVerificationProcDef

IdentityVerificationProcFld

Represents a set of fields necessary to configure the questions that CCA asks the caller before providing them with the information they
need.

**Field Name** **Description**

```
customFieldLabel

dataSourceType

developerName

fieldDataType

```

**Field Type**
string

**Description**
The custom label for the field that contains the verification data.

**Field Type**
IdentityVerificationProcFldDataSourceType (enumeration of type string)

**Description**

Required.

The source type of the data.

Valid values are:

**•** `External`

**•** `Salesforce`

**Field Type**
string

**Description**

Required.

The developer name of Identity Verification Process Field. Can contain only underscores
and alphanumeric characters and must be unique in your org. It must begin with a
letter, not include spaces, not end with an underscore, and not contain two consecutive
underscores.

Available in API version 58.0 and later.

**Field Type**
IdentityVerificationProcFldFieldDataType (enumeration of type string)

**Description**
The data type of the field in the external data source that's defined in the identity
verification process detail. Available in API version 58.0 and later.

Valid values are:

**•** `address`

**•** `checkbox`

**•** `currency`

**•** `dateonly`

**•** `datetime`

**•** `email`


Metadata Types IdentityVerificationProcDef

**Field Name** **Description**

**•** `number`

**•** `other`

**•** `percent`

**•** `phone`

**•** `picklist`

**•** `reference`

**•** `text`

**•** `timeonly`

**•** `url`

```
fieldName

fieldType

fieldValueFormula

isActive

```

**Field Type**
string

**Description**

Required.

The label of the field that contains the verification data based on the selected field
type. Available in API version 58.0 and later.

**Field Type**
IdentityVerificationProcFldFieldType (enumeration of type string)

**Description**

Required.

Indicates the type of field.

Valid values are:

**•** `additionalResultField`

**•** `optionalVerifier`

**•** `requiredVerifier`

**•** `resultField`

**•** `searchField`

**•** `searchFilter`

**Field Type**
string

**Description**
Stores the formula that is applied to the field value.

**Field Type**
boolean

**Description**
Indicates whether the record is active ( `true` ) or not ( `false` ).


Metadata Types IdentityVerificationProcDef

**Field Name** **Description**

```
isManualInput

masterLabel

sequenceNumber

```

**Field Type**
boolean

**Description**
Indicates whether the user can manually enter the identity verification details ( `true` )
or not ( `false` ).

The default value of this field is `false` .

Available in API version 58.0 and later.

**Field Type**
string

**Description**

Required.

A user-friendly name for Identity Verification Process Field.

**Field Type**
int

**Description**

Required.

The sequence number of the field.

Declarative Metadata Sample Definition

This is an example of an IdentityVerificationProcDef component.

```
<?xml version="1.0" encoding="UTF-8"?>

<IdentityVerificationProcDef xmlns="http://soap.sforce.com/2006/04/metadata">

  <identityVerificationProcDtls>

    <fullName>Sample93AccountSearch</fullName>

    <dataSourceType>Salesforce</dataSourceType>

    <developerName>Sample93AccountSearch</developerName>

    <identityVerificationProcFlds>

      <fullName>Sample93AccountName</fullName>

      <dataSourceType>Salesforce</dataSourceType>

      <developerName>Sample93AccountName</developerName>

      <fieldName>Name</fieldName>

      <fieldType>requiredVerifier</fieldType>

      <isActive>false</isActive>

      <masterLabel>Sample93 Account Name</masterLabel>

      <fieldValueFormula>abcd</fieldValueFormula>

      <customFieldLabel>Name</customFieldLabel>

      <sequenceNumber>1</sequenceNumber>

      <isManualInput>false</isManualInput>

    </identityVerificationProcFlds>

    <identityVerificationProcFlds>

```


Metadata Types IdentityVerificationProcDef

```
         <fullName>Sample93Phone</fullName>

         <dataSourceType>Salesforce</dataSourceType>

         <developerName>Sample93Phone</developerName>

         <fieldName>phone</fieldName>

         <fieldType>optionalVerifier</fieldType>

         <isActive>false</isActive>

         <masterLabel>Sample93 Phone</masterLabel>

         <sequenceNumber>93</sequenceNumber>

         <isManualInput>false</isManualInput>

       </identityVerificationProcFlds>

       <identityVerificationProcFlds>

         <fullName>Sample93PostalCode</fullName>

         <dataSourceType>Salesforce</dataSourceType>

         <developerName>Sample93PostalCode</developerName>

         <fieldName>BillingPostalCode</fieldName>

         <fieldType>optionalVerifier</fieldType>

         <isActive>true</isActive>

         <masterLabel>Sample93 Postal Code</masterLabel>

         <sequenceNumber>4</sequenceNumber>

         <isManualInput>false</isManualInput>

       </identityVerificationProcFlds>

       <identityVerificationProcFlds>

         <fullName>Sample93Account</fullName>

         <dataSourceType>Salesforce</dataSourceType>

         <developerName>Sample93Account</developerName>

         <fieldName>Name</fieldName>

         <fieldType>resultField</fieldType>

         <isActive>false</isActive>

         <masterLabel>Sample93 Account</masterLabel>

         <sequenceNumber>1</sequenceNumber>

         <isManualInput>false</isManualInput>

       </identityVerificationProcFlds>

       <isActive>true</isActive>

       <masterLabel>Sample93 Account Search</masterLabel>

       <objectName>Account</objectName>

       <searchRecordUniqueIdField>Id</searchRecordUniqueIdField>

       <searchSequenceNumber>1</searchSequenceNumber>

       <searchType>Text-Based</searchType>

       <searchResultSortBy>Name</searchResultSortBy>

       <optionalVerifiersMinVerfCount>1</optionalVerifiersMinVerfCount>

       <isRetryAllowedAfterLimit>false</isRetryAllowedAfterLimit>

       <retryLimit>5</retryLimit>

       <searchFilter></searchFilter>

       <displayRecordFieldName>LastModifiedById</displayRecordFieldName>

     </identityVerificationProcDtls>

     <masterLabel>Sample93 Verification Flow</masterLabel>

     <searchLayoutType>Tab</searchLayoutType>

   </IdentityVerificationProcDef>

```

This is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

```


### Metadata Types IdentityVerificationProcDtl

```
        <name>IdentityVerificationProcDef</name>

      </types>

      <version>54.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### IdentityVerificationProcDtl

Represents the search functionality configuration and the minimum number of optional verifiers for identity verification. This type extends
the Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### IdentityVerificationProcDtl components have the suffix .IdentityVerificationProcDtl and are stored in the IdentityVerificationProcDtls folder.

Version

### IdentityVerificationProcDtl components are available in API version 54.0 and later.

Special Access Rules

The Health Cloud permission set license is required to use this metadata type.

Fields

**Field Name** **Description**

```
apexClass

dataSourceType

```

**Field Type**
string

**Description**
Reserved for future use.

**Field Type**
IdentityVerificationDataSourceType (enumeration of type string)

**Description**

Required.

The source type of the data.


Metadata Types IdentityVerificationProcDtl

**Field Name** **Description**

Valid values are:

**•** `External` —Reserved for future use.

**•** `Salesforce`

```
identityVerificationProcFlds

isActive

masterLabel

objectName

optionalVerifiersMinVerfCount

searchFilter

searchRecordUniqueIdField

```

**Field Type**

IdentityVerificationProcFld[]

**Description**
A list of Identity Verification Process Field elements.

**Field Type**
boolean

**Description**
Indicates whether the record is active ( `true` ) or not ( `false` ).

The default value is `false` .

**Field Type**
string

**Description**

Required.

The label of the Identity Verification Process Detail record.

**Field Type**
string

**Description**
The name of the object on which the search is performed and data is verified.

**Field Type**
int

**Description**
The minimum number of optional verifiers that must be checked.

**Field Type**
string

**Description**
Conditions on which to filter the search results.

For example, if you want to perform the search only on Person Account records, enter
`isPersonAccount = true` .

**Field Type**
string


Metadata Types IdentityVerificationProcDtl

**Field Name** **Description**

**Description**
The field that stores the unique identifier of the records that are displayed in the search
results.

```
searchResultSortBy

searchSequenceNumber

searchType

```

**Field Type**
string

**Description**
The values that are used to sort the search results.

For example, if you want to sort the results by policy date, enter `PolicyDate__c`
`Desc` .

**Field Type**
int

**Description**

Required.

Enter 1 as the search sequence number.

Note: In API version 54.0 and later, this field is reserved for future use, and the
value you enter doesn't affect sequencing.

**Field Type**
IdentityVerificationSearchType (enumeration of type string)

**Description**

Required.

The type of search being performed.

Valid values are:

**•** `Object-Based` —Reserved for future use.

**•** `Text-Based`

IdentityVerificationProcFld

Represents a set of fields necessary to configure the questions that CCA asks the caller before providing them with the information they
need.

**Field Name** **Description**

```
customFieldLabel

```

**Field Type**
string

**Description**
The custom label for the field that contains the verification data.


Metadata Types IdentityVerificationProcDtl

**Field Name** **Description**

```
dataSourceType

developerName

fieldDataType

```

**Field Type**
IdentityVerificationProcFldDataSourceType (enumeration of type string)

**Description**

Required.

The source type of the data.

Valid values are:

**•** `External`

**•** `Salesforce`

**Field Type**
string

**Description**

Required.

The developer name of Identity Verification Process Field. Can contain only underscores
and alphanumeric characters and must be unique in your org. It must begin with a
letter, not include spaces, not end with an underscore, and not contain two consecutive
underscores.

Available in API version 58.0 and later.

**Field Type**
IdentityVerificationProcFldFieldDataType (enumeration of type string)

**Description**
The data type of the field in the external data source that's defined in the identity
verification process detail. Available in API version 58.0 and later.

Valid values are:

**•** `address`

**•** `checkbox`

**•** `currency`

**•** `dateonly`

**•** `datetime`

**•** `email`

**•** `number`

**•** `other`

**•** `percent`

**•** `phone`

**•** `picklist`

**•** `reference`

**•** `text`

**•** `timeonly`


Metadata Types IdentityVerificationProcDtl

**Field Name** **Description**

**•** `url`

```
fieldName

fieldType

fieldValueFormula

isActive

isManualInput

```

**Field Type**
string

**Description**

Required.

The label of the field that contains the verification data based on the selected field
type. Available in API version 58.0 and later.

**Field Type**
IdentityVerificationProcFldFieldType (enumeration of type string)

**Description**

Required.

Indicates the type of field.

Valid values are:

**•** `additionalResultField`

**•** `optionalVerifier`

**•** `requiredVerifier`

**•** `resultField`

**•** `searchField`

**•** `searchFilter`

**Field Type**
string

**Description**
Stores the formula that is applied to the field value.

**Field Type**
boolean

**Description**
Indicates whether the record is active ( `true` ) or not ( `false` ).

**Field Type**
boolean

**Description**
Indicates whether the user can manually enter the identity verification details ( `true` )
or not ( `false` ).

The default value of this field is `false` .

Available in API version 58.0 and later.


Metadata Types IdentityVerificationProcDtl

**Field Name** **Description**

```
masterLabel

sequenceNumber

```

**Field Type**
string

**Description**

Required.

A user-friendly name for Identity Verification Process Field.

**Field Type**
int

**Description**

Required.

The sequence number of the field.

Declarative Metadata Sample Definition

The following is an example of an identityVerificationProcDtl component.

```
<?xml version="1.0" encoding="UTF-8"?>

<IdentityVerificationProcDtl xmlns="http://soap.sforce.com/2006/04/metadata">

   <dataSourceType>Salesforce</dataSourceType>

   <isActive>true</isActive> <developerName>Sample93AccountSearch</developerName>

   <identityVerificationProcFlds>

     <fullName>Sample93AccountName</fullName>

     <dataSourceType>Salesforce</dataSourceType>

     <developerName>Sample93AccountName</developerName>

     <fieldName>Name</fieldName>

     <fieldType>requiredVerifier</fieldType>

     <isActive>false</isActive>

     <masterLabel>Sample93 Account Name</masterLabel>

     <fieldValueFormula>abcd</fieldValueFormula>

     <customFieldLabel>Name</customFieldLabel>

     <sequenceNumber>1</sequenceNumber>

     <isManualInput>false</isManualInput>

   </identityVerificationProcFlds>

   <identityVerificationProcFlds>

     <fullName>Sample93Phone</fullName>

     <dataSourceType>Salesforce</dataSourceType>

     <developerName>Sample93Phone</developerName>

     <fieldName>phone</fieldName>

     <fieldType>optionalVerifier</fieldType>

     <isActive>false</isActive>

     <masterLabel>Sample93 Phone</masterLabel>

     <sequenceNumber>93</sequenceNumber>

     <isManualInput>false</isManualInput>

   </identityVerificationProcFlds>

   <masterLabel>detail1</masterLabel>

   <fullName>detail1</fullName>

```


### Metadata Types IdentityVerificationProcFld

```
      <objectName>Account</objectName>

      <optionalVerifiersMinVerfCount>11</optionalVerifiersMinVerfCount>

      <searchFilter>asd</searchFilter>

      <searchRecordUniqueIdField>Id</searchRecordUniqueIdField>

      <searchResultSortBy>asd</searchResultSortBy>

      <searchSequenceNumber>1</searchSequenceNumber>

      <searchType>Text-Based</searchType>

   </IdentityVerificationProcDtl>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>IdentityVerificationProcDtl</name>

      </types>

      <version>54.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### IdentityVerificationProcFld

Represents the search and verification fields used in identity verification. This type extends the Metadata metadata type and inherits its
`fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### IdentityVerificationProcFld components have the suffix .IdentityVerificationProcFld and are stored in the IdentityVerificationProcFlds folder.

Version

### IdentityVerificationProcFld components are available in API version 54.0 and later.

Special Access Rules

The Health Cloud permission set license is required to use this metadata type.


Metadata Types IdentityVerificationProcFld

Fields

**Field Name** **Description**

```
customFieldLabel

dataSourceType

fieldDataType

```

**Field Type**
string

**Description**
The custom label for the field that contains the verification data. Translation of custom
field labels isn't supported in API version 54.0.

**Field Type**
IdentityVerificationProcFldDataSourceType (enumeration of type string)

**Description**

Required.

The source type of the data.

Valid values are:

**•** `External`

An external data source isn’t supported in API version 54.0.

**•** `Salesforce`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of data stored in an external data source field.

Possible values are:

**•** `address`

**•** `checkbox`

**•** `currency`

**•** `dateonly`

**•** `datetime`

**•** `email`

**•** `number`

**•** `other`

**•** `percent`

**•** `phone`

**•** `picklist`

**•** `reference`

**•** `text`


Metadata Types IdentityVerificationProcFld

**Field Name** **Description**

**•** `timeonly`

**•** `url`

```
fieldName

fieldType

fieldValueFormula

isActive

```

**Field Type**
string

**Description**

Required.

The label of the field that contains the verification data based on the selected field
type.

**Field Type**
IdentityVerificationProcFldFieldType (enumeration of type string)

**Description**

Required.

Indicates the type of field.

Possible values are:

**•** `additionalResultField` —Fetches data as part of the search query, but
the data isn’t displayed in search results. Use this value if, for example, you want
to fetch the policy number and the age of the policy owner as a result of the search,
but the agent isn’t supposed to see this data. You can write custom logic to process
this additional data.

**•** `optionalVerifier` —Optional verifier.

**•** `requiredVerifier` —Required verifier.

**•** `resultField` —Displays field type in search results. Use this value if, for
example, when an agent searches for a caller, you’d like the search results to include
the account name, phone number, and email ID.

**•** `searchField` —Reserved for future use.

**•** `searchFilter` —A comma-separated list of predefined filter conditions that
are used to refine the scope of the search.

**Field Type**
string

**Description**
Reserved for future use.

**Field Type**
boolean

**Description**
Indicates whether the record is active ( `true` ) or not ( `false` ).

The default value is `false` .


Metadata Types IdentityVerificationProcFld

**Field Name** **Description**

```
isManualInput

masterLabel

sequenceNumber

```

**Field Type**
boolean

**Description**
Indicates whether the user can manually enter the identity verification details ( `true` )
or not ( `false` ).

The default value is `false` .

This field is available in API version 58.0 and later.

**Field Type**
string

**Description**

Required.

The label of the Identity Verification Process Field record.

**Field Type**
int

**Description**

Required.

The sequence number of the field.

Declarative Metadata Sample Definition

The following is an example of an IdentityVerificationProcFld component.

```
<?xml version="1.0" encoding="UTF-8"?>

<IdentityVerificationProcFld xmlns="http://soap.sforce.com/2006/04/metadata"

xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

   <customFieldLabel>field1</customFieldLabel>

   <dataSourceType>External</dataSourceType>

   <fieldName>sasa</fieldName>

   <fieldType>requiredVerifier</fieldType>

   <fullName>field1</fullName>

   <isActive>false</isActive>

   <masterLabel>field1</masterLabel>

   <sequenceNumber>1</sequenceNumber>

</IdentityVerificationProcFld>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

```


### Metadata Types InboundCertificate

```
        <members>*</members>

        <name>IdentityVerificationProcFld</name>

      </types>

      <version>54.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### InboundCertificate

Represents a mutual authentication certificate that is imported to your Salesforce org.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### InboundCertificate components have the suffix .inboundCertificate and are stored in the inboundCertificates

folder.

Special Access Rules

### InboundCertificate is available when the MutualAuthentication permission is enabled in your org.

Version

### InboundCertificate components are available in API version 49.0 and later.

Fields

This metadata type contains the following fields:

**Field Name** **Field Type** **Description**

`expirationDate` date Required. The date on which the certificate expires.

`issuer` string Required. The certificate’s issuer.

`masterLabel` string Required. A friendly name that you create for the certificate. Limited to
64 characters.

`serialId` string Required. The serial number for the certificate.


### Metadata Types InboundNetworkConnection

Declarative Metadata Sample Definition

The following is an example of an InboundCertificate component.

```
   <InboundCertificate xmlns="http://soap.sforce.com/2006/04/metadata">

      <expirationDate>2021-02-04</expirationDate>

      <issuer>C=USA,ST=CA,L=San

   Francisco,O=Salesforce.com,OU=00Dxx0000006Jm7,CN=newTestCert</issuer>

      <masterLabel>TestMutualAuthCert2</masterLabel>

      <serialId>29161320252531323757470546071624</serialId>

   </InboundCertificate>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>InboundCertificate</name>

      </types>

      <version>49.0</version>

   </Package>

```

Usage

To prevent simple impersonation from compromising security, you can require clients and servers to prove their identity to each other
with a mutual authentication certificate.

### InboundNetworkConnection

Represents a private connection between a third-party data service and a Salesforce org. The connection is inbound because the callouts
are coming _into_ Salesforce.This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### InboundNetworkConnection components have the suffix .inboundNetworkConnection and are stored in the

`inboundNetworkConnections` folder.

Version

### InboundNetworkConnection components are available in API version 49.0 and later.

Fields

**Field Name** **Field Type** **Description**

```
connectionType

```

ExternalConnectionType Required. Specifies the cloud provider of the connection.
(enumeration of

**•** `AwsPrivateLink`

type string)


Metadata Types InboundNetworkConnection

**Field Name** **Field Type** **Description**

**•** `DataCloudPrivateConnection` (Reserved for internal use)

`description` string Required. A description of the connection. Maximum of 255 characters.

`inboundNetworkConnProperties` InboundNetworkConnProperty Name-value pairs that describe the properties of the inbound network
connection. Specify a name-value pair for each of the properties.

`isActive` boolean Required. Specifies whether the connection is active ( `true` ) or
not( `false` ). The default value is `false` .

`label` string Required. A user-friendly label for the connection.

Required. Connection status. The connection is initially Unprovisioned
and moves through the other states automatically after an admin
performs a Provision, Sync, or Teardown action. The valid values are:

**•** `Unprovisioned`

**•** `Allocating`

**•** `PendingAcceptance`

**•** `PendingActivation`

**•** `RejectedRemotely`

**•** `DeletedRemotely`

**•** `TeardownInProgress`

**•** `Ready`

```
status

```

ExternalConnectionStatus
(enumeration of
type string)

InboundNetworkConnProperty

Represents a name-value pair that describes the properties of the inbound network connection.

**Field Name** **Field Type** **Description**

```
propertyName

```

InboundConnPropertyName Required. The name of a property used to establish an
(enumeration of type InboundNetworkConnection. Valid values are:
string)

**•** `AwsVpcEndpointId` —The unique endpoint ID for connections to an
AWS Virtual Private Cloud (VPC). The value is read-only when the `status`
is `Ready` .

**•** `Region` —The region in which the VPC is hosted.

**•** `SourceIpRanges` —The ranges of source IP address allocated to this
inbound connection by the Salesforce-managed VPC in your cloud provider.


Metadata Types InboundNetworkConnection

**Field Name** **Field Type** **Description**

`propertyValue` string

Required. The value of InboundConnPropertyName. An example of the
`propertyValue` of `Region` is `us-west-2.`

The `propertyValue` of `SourceIpRanges` is a JSON string that lists
the start and end IP address for each range. This example shows two IP address
ranges.

```
[

  {

   "startIp":"10.10.10.0",

   "endIp":"10.10.10.3"

  },

  {

   "startIp":"100.100.100.0",

   "endIp":"100.100.100.15"

  }

]

```

Declarative Metadata Sample Definition

The following sample definition has the suffix `.inboundNetworkConnection` .

```
<?xml version="1.0" encoding="UTF-8"?>

<InboundNetworkConnection xmlns="http://soap.sforce.com/2006/04/metadata">

   <connectionType>AwsPrivateLink</connectionType>

   <description>This is an Inbound Connection to make API calls into

Salesforce</description>

   <inboundNetworkConnProperties>

     <propertyName>Region</propertyName>

     <propertyValue>us-west-2</propertyValue>

   </inboundNetworkConnProperties>

   <inboundNetworkConnProperties>

     <propertyName>AwsVpcEndpointId</propertyName>

     <propertyValue>vpce-02ccb5fac2bacaceb</propertyValue>

   </inboundNetworkConnProperties>

   <inboundNetworkConnProperties>

     <propertyName>SourceIpRanges</propertyName>

     <propertyValue>[ { "startIp":"10.10.10.0", "endIp":"10.10.10.3" }, {

"startIp":"100.100.100.0", "endIp":"100.100.100.15" } ]</propertyValue>

   </inboundNetworkConnProperties>

   <isActive>true</isActive>

   <label>MyInboundConnection</label>

   <status>Unprovisioned</status>

</InboundNetworkConnection>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <fullName>sampleInboundConnection</fullName>

   <types>

```


### Metadata Types IndustriesPricingSettings

```
        <members>MyInboundConnection</members>

        <name>InboundNetworkConnection</name>

      </types>

      <version>49.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### IndustriesPricingSettings

Represents the settings for Salesforce Pricing.

Parent Type and Manifest Access

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

[In the package manifest, all the settings metadata types for the org are accessed using the “Settings” name. See Settings for more details.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_settings.htm)

File Suffix and Directory Location

### IndustriesPricingSettings values are stored in the IndustriesPricingSettings.settings file in the

`settings` folder. The `.settings` files are different from other named components, because there’s only one settings file for each
settings component.

Version

### IndustriesPricingSettings components are available in API version 60.0 and later.

Special Access Rules

This metadata type is available with Salesforce Pricing.

Fields

**Field Name** **Description**

```
enableDebugPriceLogs

```

**Field Type**
boolean

**Description**
Indicates whether to use price logs to diagnose and resolve pricing issues ( `true` ) or
not ( `false` ). The default value is `false` . Available in API version 63.0 and later.


Metadata Types IndustriesPricingSettings

**Field Name** **Description**

```
enableHighAvailability

enableHighestPriceCompliance

enableLowestPriceCompliance

enablePricingProcParallelization

enablePricingWaterfall

enablePricingWaterfallPersistence

enableSalesforcePricing

```

**Field Type**
boolean

**Description**
Reserved for internal use.

**Field Type**
boolean

**Description**
Indicates whether to track the maximum price of a product over a period of 30 days
( `true` ) or not ( `false` ). The default value is `false` . Available in API version 64.0
and later.

**Field Type**
boolean

**Description**
Indicates whether to track the minimum price of a product over a period of 30 days
( `true` ) or not ( `false` ). The default value is `false` . Available in API version 62.0
and later.

**Field Type**
boolean

**Description**
Indicates whether to run pricing elements in parallel within a pricing procedure to
optimize the performance of the pricing execution process ( `true` ) or not ( `false` ).
The default value is `false` . Available in API version 64.0 and later.

**Field Type**
boolean

**Description**
Indicates whether to enable Price Waterfall ( `true` ) or not ( `false` ). The default value
is `false` . Price Waterfall provides insights that include price breakups and reasons
for every step of the pricing process.

**Field Type**
boolean

**Description**
Indicates whether to enable Price Waterfall Persistence ( `true` ) or not ( `false` ). The
default value is `false` . Price Waterfall Persistence stores the process logs that provide
insights into the internal pricing processes.

**Field Type**
boolean


### Metadata Types IndustriesRatingSettings

**Field Name** **Description**

**Description**
Indicates whether to enable Salesforce Pricing ( `true` ) or not ( `false` ). The default
value is `false` .

Declarative Metadata Sample Definition

This example shows a sample IndustriesPricingSettings component.

```
   <IndustriesPricingSettings xmlns="http://soap.sforce.com/2006/04/metadata">

      <enableDebugPriceLogs>true</enableDebugPriceLogs>

      <enableHighAvailability>true</enableHighAvailability>

      <enableHighestPriceCompliance>true</enableHighestPriceCompliance>

      <enableLowestPriceCompliance>true</enableLowestPriceCompliance>

      <enablePricingProcParallelization>true</enablePricingProcParallelization>

      <enablePricingWaterfall>true</enablePricingWaterfall>

      <enablePricingWaterfallPersistence>true</enablePricingWaterfallPersistence>

      <enableSalesforcePricing>true</enableSalesforcePricing>

   </IndustriesPricingSettings>

```

This example shows a sample `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>IndustriesPricing</members>

        <name>Settings</name>

      </types>

      <version> 66.0 </version>

   </Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The wildcard
[applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the manifest](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_settings.htm)
[file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### IndustriesRatingSettings

Represents the settings for Rate Management.

Parent Type and Manifest Access

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

[In the package manifest, all the settings metadata types for the org are accessed using the “Settings” name. See Settings for more details.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_settings.htm)


Metadata Types IndustriesRatingSettings

File Suffix and Directory Location

The `IndustriesRatingSettings` values are stored in the `IndustriesRating.settings` file in the `settings` folder.
The `.settings` files are different from other named components, because there’s only one settings file for each settings component.

Version

IndustriesRatingSettings components are available in API version 62.0 and later.

Special Access Rules

This metadata type is available with Rate Management.

Fields

**Field Name** **Description**

```
enableRating

enableRatingWaterfall

enableRatingWaterfallPersistence

```

**Field Type**
boolean

**Description**
Indicates whether to enable Rate Management ( `true` ) or not ( `false` ). The default
value is `false` .

**Field Type**
boolean

**Description**
Indicates whether to enable Rating Waterfall ( `true` ) or not ( `false` ). The default
value is `false` . Rating Waterfall provides insights into the rating data, which you can
synchronize with your rating lookup tables.

**Field Type**
boolean

**Description**
Indicates whether to enable Rating Waterfall Persistence ( `true` ) or not ( `false` ). The
default value is `false` . Rating Waterfall Persistence stores rating data, which you can
use to enhance the internal processes and increase efficiency.

Declarative Metadata Sample Definition

The following is an example of an IndustriesRatingSettings component.

```
<IndustriesRatingSettings xmlns="http://soap.sforce.com/2006/04/metadata">

   <enableRating>true</enableRating>

   <enableRatingWaterfall>true</enableRatingWaterfall>

```


### Metadata Types IndustriesUnifiedInventorySettings

```
      <enableRatingWaterfallPersistence>true</enableRatingWaterfallPersistence>

   </IndustriesRatingSettings>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>IndustriesRating</members>

        <name>Settings</name>

      </types>

      <version> 66.0 </version>

   </Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The wildcard
[applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the manifest](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_settings.htm)
[file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### IndustriesUnifiedInventorySettings

Represents the settings for Industries Unified Inventory.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### IndustriesUnifiedInventorySettings components have the suffix IndustriesUnifiedInventory.settings  and are stored

in the `settings` folder.

Version

### IndustriesUnifiedInventorySettings components are available in API version 64.0 and later.

Fields

**Field Name** **Description**

```
enableBatchManagement

```

**Field Type**
Boolean

**Description**
Indicates whether the batch-based inventory management features are enabled
( `true` ) or not ( `false` ). Within Life Sciences Cloud, this is a core component of the
Unified Inventory Extension Entities, supporting Sample Inventory use cases. When


### Metadata Types InstalledPackage

**Field Name** **Description**

enabled, it provides access to the entities ProductionBatch, ProductBatchItem, and
InventoryCntProdtBatchItem.

```
enableInventoryCount

enableProductInventoryOperations

```

**Field Type**
Boolean

**Description**
Indicates whether the Inventory Count is enabled ( `true` ) or not ( `false` ). The
Inventory Count provides the ability to manage inventory count processes by planning
inventory counts, counting inventory at designated locations, and tracking count
results.

**Field Type**
Boolean

**Description**
Indicates whether the Product Inventory Operations that provides the capabilities to
perform various actions related to managing product inventory is enabled ( `true` ) or
not ( `false` ).

Declarative Metadata Sample Definition

The following is an example of an IndustriesUnifiedInventorySettings component.

```
<?xml version="1.0" encoding="UTF-8"?>

<IndustriesUnifiedInventorySettings xmlns="http://soap.sforce.com/2006/04/metadata">

   <enableBatchManagement>true</enableBatchManagement>

   <enableInventoryCount>true</enableInventoryCount>

   <enableProductInventoryOperations>true</enableProductInventoryOperations>

</IndustriesUnifiedInventorySettings>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>IndustriesUnifiedInventory</members>

     <name>Settings</name>

   </types>

   <version>64.0</version>

</Package>

### InstalledPackage

```

Represents a first-generation managed package to be installed or uninstalled. Deploying a newer version of a currently installed package
upgrades the package. You can install up to 20 first-generation managed packages in a single deployment. To install an unlocked or
second-generation managed package, use the `sf package install` Salesforce CLI command.


Metadata Types InstalledPackage

Note: You can’t deploy a package along with other metadata types. When you deploy InstalledPackage, it must be the only
metadata type specified in the manifest file.

File Suffix and Directory Location

The package is specified in the `installedPackages` directory, in a file named after the package’s namespace prefix. The file
extension is `.installedPackage` .

Version

InstalledPackage is available in API version 28.0 and later.

Fields

**Field Name** **Field Type** **Description**

`activateRSS` boolean

Required. Determines the state of Remote Site Settings (RSS) and Content
Security Policy (CSP) at the time of installing the package and must be
set to either of these values.

**true**
Keep the isActive state of any RSS or CSP in the package.

**false**
Override the isActive state of any RSS or CSP in the package and set
it to `false` .

The default value is `false` . Available in API version 43.0 and later.

`password` string Specifies the package password.

`securityType` string

`versionNumber` string

Determines user access for the installed package.

Valid values are:

**•** `AdminsOnly`

**•** `AllUsers`

The default value is `AllUsers` . Available in API version 57.0 and later.

Required. The version number of the package. The version number has
the format _**`majorNumber.minorNumber.patchNumber`**_ (for
example, `2.1.3` ).

Declarative Metadata Sample Definition

The following example specifies a sample package to be installed or uninstalled.

```
<?xml version="1.0" encoding="UTF-8"?>

     <InstalledPackage xmlns="http://soap.sforce.com/2006/04/metadata">

     <versionNumber>1.0</versionNumber>

     <password> optional_password </password>

```


### Metadata Types IntegArtifactDef

```
        <securityType>AdminsOnly</securityType>

        <activateRSS>true</activateRSS>

        </InstalledPackage>

```

The `securityType` field is optional. If it’s not specified, the default security type is `AllUsers` .

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### IntegArtifactDef

For internal use only.

### IntegrationProviderDef

Represents an integration definition associated with a service process. Stores data for the Industries: Send Apex Async Request and
Industries: Send External Async Request invocable actions.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### IntegrationProviderDef components have the suffix .integrationProviderDefinition and are stored in the

`.integrationProviderDefinition` folder.

Version

### IntegrationProviderDef components are available in API version 57.0 and later.

Special Access Rules

Access to the IntegrationProviderDef type requires the AccessToServiceProcess permission.

Fields

**Field Name** **Description**

```
active

```

**Field Type**
boolean

**Description**
Specifies whether this Integration Definition is active. The default is `false` .


Metadata Types IntegrationProviderDef

**Field Name** **Description**

```
apexClass

description

developerName

externalServiceOperationName

externalServiceRegistration

fileBasedApexClass

fileBasedExternalService

```

**Field Type**
string

**Description**
The custom Apex class that the related Industries: Send Apex Async Request invocable
action invokes. Specify either apexClass or fileBasedApexClass but not both. Applies
only if the type is `Apex` .

**Field Type**
string

**Description**
A meaningful explanation of the Integration Definition.

**Field Type**
string

**Description**

Required.

A system name for the Integration Definition.

**Field Type**
string

**Description**
The external service operation that the related Industries: Send External Async Request
invocable action invokes. Applies only if the type is `LowCode` .

**Field Type**
string

**Description**
The external service that the related Industries: Send External Async Request invocable
action invokes. Applies only if the type is `LowCode` .

**Field Type**
string

**Description**
The Salesforce-provided Apex class that the related Industries: Send Apex Async Request
invocable action invokes. Specify either apexClass or fileBasedApexClass but not both.
Applies only if the type is `Apex` .

**Field Type**
string


Metadata Types IntegrationProviderDef

**Field Name** **Description**

**Description**
The Salesforce-provided external service that the Integration Definition invokes. This
field is used for packaged or system-provided external service integrations. Applies
only if the type is `LowCode` .

Available in API version 64.0 and later.

```
fileBasedInputDataProcessor

fileBasedOmniUiCard

fileBasedOutputDataProcessor

inputDataProcessor

integrationProviderAttributes

javaClassName

```

**Field Type**
string

**Description**
The Salesforce-provided Integration Procedure that processes the specified data. This
field references packaged or system-provided data processors. Applies only if the type
is `LowCode` .

Available in API version 64.0 and later.

**Field Type**
string

**Description**
The Salesforce-provided OmniStudio UI Card that's associated with this Integration
Definition. This enables packaged UI components for integration configuration.

Available in API version 64.0 and later.

**Field Type**
string

**Description**
The Salesforce-provided Integration Procedure that processes the returned data. This
field references packaged or system-provided output processors. Applies only if the
type is `LowCode` .

Available in API version 64.0 and later.

**Field Type**
string

**Description**
The optional Integration Procedure that processes the sent data. Applies only if the
type is `LowCode` .

**Field Type**

IntegrationProviderAttr[]

**Description**
Custom attributes that store data associated with an Integration Definition.

**Field Type**
string


Metadata Types IntegrationProviderDef

**Field Name** **Description**

**Description**
Name of the Java class that the Integration Definition invokes. Applies only if the type
is `Java` .

Available in API version 59.0 and later.

```
outputDataProcessor

providerLabel

type

```

IntegrationProviderAttr

**Field Type**
string

**Description**
The optional Integration Procedure that processes the returned data. Applies only if
the type is `LowCode` .

**Field Type**
string

**Description**

Required.

A meaningful name for the Integration Definition.

**Field Type**
DefinitionType (enumeration of type string)

**Description**

Required.

What the Integration Definition calls, either an Apex class or an external service.

Values are:

**•** `Apex`

**•** `Java`

**•** `LowCode`

A custom attribute that stores data associated with an Integration Definition.

**Field Name** **Description**

```
dataType

```

**Field Type**
AttrDataType (enumeration of type string)

**Description**

Required.

The data type of the attribute.

Values are:


Metadata Types IntegrationProviderDef

**Field Name** **Description**

**•** `Date`

**•** `DateTime`

**•** `Double`

**•** `Integer`

**•** `Percentage`

**•** `String`

**•** `Boolean`

```
dateTimeValue

dateValue

description

developerName

doubleValue

integerValue

label

```

**Field Type**
dateTime

**Description**
The value of the attribute if the `dataType` is `DateTime` .

**Field Type**
date

**Description**
The value of the attribute if the `dataType` is `Date` .

**Field Type**
string

**Description**
A meaningful explanation of the attribute.

**Field Type**
string

**Description**

Required.

A system name for the attribute.

**Field Type**
double

**Description**
The value of the attribute if the `dataType` is `Double` .

**Field Type**
int

**Description**
The value of the attribute if the `dataType` is `Integer` .

**Field Type**
string


Metadata Types IntegrationProviderDef

**Field Name** **Description**

**Description**

Required.

A meaningful name for the attribute.

```
percentageValue

required

stringValue

trueOrFalseValue

```

**Field Type**
double

**Description**
The value of the attribute if the `dataType` is `Percentage` .

**Field Type**
boolean

**Description**

Required.

Specifies whether the attribute is required.

**Field Type**
string

**Description**
The value of the attribute if the `dataType` is `String` .

**Field Type**
boolean

**Description**
The value of the attribute if the `dataType` is `Boolean` .

Declarative Metadata Sample Definition

The following is an example of an IntegrationProviderDef component.

```
<?xml version="1.0" encoding="UTF-8"?>

<IntegrationProviderDef xmlns="http://soap.sforce.com/2006/04/metadata">

  <developerName>EmailUpdate</developerName>

  <providerLabel>EmailUpdate</providerLabel>

  <type>Apex</type>

  <apexClass>SendEmailUpdate</apexClass>

  <integrationProviderAttributes>

    <developerName>EmailAddress</developerName>

    <label>EmailAddress</label>

    <dataType>String</dataType>

    <stringValue>person@example.com</stringValue>

    <required>true</required>

  </integrationProviderAttributes>

</IntegrationProviderDef>

```


### Metadata Types IPAddressRange

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>IntegrationProviderDef</name>

      </types>

      <version>57.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### IPAddressRange

Represents a range of IP addresses to include in or exclude from the specified feature.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### IP Address Range components have the suffix .IPAddressRange and are stored in the IPAddressRanges folder.

Version

### IPAddressRange components are available in API version 52.0 and later.

Special Access Rules

To access IpAddressRange, enable the HtmlEmail permission in your org.

Fields

**Field Name** **Description**

```
Description

```

**Field Type**
string

**Description**
Not required. The description of the IP address range. For example, the name of the
company that owns the IP address range.


Metadata Types IPAddressRange

**Field Name** **Description**

```
developerName

endIpAddress

ipAddressFeature

ipAddressUsageScope

isProtected

masterLabel

startIpAddress

```

**Field Type**
string

**Description**
Not required. Gives you a way to distinguish ipAddressRange entries among developers
in your org.

**Field Type**
string

**Description**
The end of the IP address range. Must be an IPv4 or IPv6 Internet address and equal
to or greater than the `startIpAddress` .

**Field Type**
picklist

**Description**
The feature that uses the range of IP addresses. Possible values are:

**•** `EmailIpFiltering` (default) —Filter email engagement activities such as
email opens and email clicks.

**Field Type**
picklist

**Description**
Whether the specified IP addresses are included or excluded. Possible values are:

**•** `Exclusion`

**•** `Inclusion`

**Field Type**
boolean

**Description**
Whether the specified IP address range is protected. The default is `false` .

**Field Type**
string

**Description**
Master label for the IP address range. This internal label doesn’t get translated.

**Field Type**
string

**Description**
The start of the IP address range. Must be an IPv4 or IPv6 Internet address and equal
to or smaller than the `endIpAddress` .


### Metadata Types InvocableActionExtension

Declarative Metadata Sample Definition

The following is an example of an `ipAddressName` component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <IPAddressRange xmlns="http://soap.sforce.com/2006/04/metadata">

      <description>Filter emails from google.com</description>

      <endIpAddress>221.224.222.158</endIpAddress>

      <ipAddressFeature>EmailIpFiltering</ipAddressFeature>

      <ipAddressUsageScope>Exclusion</ipAddressUsageScope>

      <masterLabel>MasterLabelValue</masterLabel>

      <startIpAddress>221.224.0.158</startIpAddress>

      <isProtected>false</isProtected>

   </IPAddressRange>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>IPAddressRange</name>

      </types>

      <version>1.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

### InvocableActionExtension

Represents the configuration that defines how an action's inputs are presented in a user interface.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### InvocableActionExtension components have the suffix .invocableactionextension and are stored in the

`invocableactionextensions` folder.

Version

### InvocableActionExtension components are available in API version 65.0 and later.


Metadata Types InvocableActionExtension

Fields

**Field Name** **Description**

```
targets

```

**Field Type**

InvocableActionExtensionTarget[]

**Description**
The target of this invocable action extension.

InvocableActionExtensionTarget

Represents an extension that can contain attributes for an action's definition, parameters, and types. Use InvocableActionExtensionTarget
as the parent element for a given target, such as an ActionParameter. Each assigned attribute is a child of this element.

**Field Name** **Description**

```
attributes

targetName

targetType

```

**Field Type**

InvocableActionExtensionTargetAttribute[]

**Description**
The list of attributes.

**Field Type**
string

**Description**

Required.

The name of the target for the attributes.

**Field Type**
InvocableActionExtTargetType (enumeration of type string)

**Description**

Required.

Specifies the type of component within the invocable action.

Values are:

**•** `ActionDefinition` —Targets the action class.

**•** `ActionParameter` —Targets the specific input/output parameters.

**•** `TypeDefinition` —Targets the custom Apex types used by the action.

**•** `TypeProperty` —Targets the individual properties within those custom types.

InvocableActionExtensionTargetAttribute

Represents the individual configuration attributes within an extension target. Use InvocableActionExtensionTargetAttribute as the child
element of InvocableActionExtensionTarget to define specific behaviors, dependencies, and properties. Each attribute consists of a


Metadata Types InvocableActionExtension

key-value pair with an associated data type. This configuration determines how the target action parameter, type property, or action
definition behaves.

**Field Name** **Description**

```
dataType

key

value

```

**Field Type**
InvocableActionExtAttributeDataType (enumeration of type string)

**Description**

Required.

The data type of the value stored in the value field.

Values are:

**•** `Boolean`

**•** `Date`

**•** `Double`

**•** `Integer`

**•** `Long`

**•** `String`

**Field Type**
string

**Description**

Required.

The key field that specifies which standard attribute to provide a value for, or provides
a custom key. The available standard keys are:

**•** `Order`

**•** `GroupName`

**•** `ControllingField`

For a custom key, enter any value that contains letters, numbers, or single underscores,
starts with a letter, and ends with `__c` .

**Field Type**
string

**Description**

Required.

The value of the associated key. An Invocable Action Extension can have multiple
attributes, each with its own value.


Metadata Types InvocableActionExtension

Declarative Metadata Sample Definition

The following example shows an InvocableActionExtension component definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <InvocableActionExt xmlns="http://soap.sforce.com/2006/04/metadata">

      <targets>

        <targetType>ActionParameter</targetType>

        <targetName>Example.Request.inputOne</targetName>

        <attributes>

           <key>Order</key>

           <dataType>Integer</dataType>

           <value>1</value>

        </attributes>

        <attributes>

           <key>Group</key>

           <dataType>String</dataType>

           <value>Group A</value>

        </attributes>

      </targets>

      <targets>

        <targetType>ActionParameter</targetType>

        <targetName>Example.Request.inputTwo</targetName>

        <attributes>

           <key>Order</key>

           <dataType>Integer</dataType>

           <value>2</value>

        </attributes>

        <attributes>

           <key>Group</key>

           <dataType>String</dataType>

           <value>Group A</value>

        </attributes>

      </targets>

      <targets>

        <targetType>ActionParameter</targetType>

        <targetName>Example.Request.inputThree</targetName>

        <attributes>

           <key>Order</key>

           <dataType>Integer</dataType>

           <value>3</value>

        </attributes>

        <attributes>

           <key>Group</key>

           <dataType>String</dataType>

           <value>Group B</value>

        </attributes>

      </targets>

   </InvocableActionExt>

```

The following example shows a `package.xml` file that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

```


### Metadata Types KeywordList

```
        <members>Example</members>

        <name>InvocableActionExtension</name>

      </types>

      <version>65.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### KeywordList

Represents a list of keywords used in Experience Cloud site moderation. This keyword list is a type of moderation criteria that defines
offensive language or inappropriate content that you don’t want in your site.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

This type extends the Metadata metadata type and inherits its `fullName` field.

Keep the following things in mind when creating keyword list criteria:

**•** Your org can have up to 30 keyword list criteria. This limit is per org, not per Experience Cloud site.

**•** A keyword list can have up to 2,000 keywords.

**•** Capitalization and trailing punctuation are ignored when matching your keywords to user-generated content. For example, if your
criteria includes _`BadWord`_, it’s matched when a user types _`BADWORD`_ or _`badword.`_

File Suffix and Directory Location

### KeywordList components have the suffix .keywords and are stored in the moderation directory of the corresponding package

directory. The file name format follows _`site_name`_ `.` _`keyword_list_developer_name`_ `.keywords` .

Version

### KeywordList components are available in API version 36.0 and later.

Special Access Rules

To view, create, edit, and delete a keyword list, you need the Manage Experiences or Create and Set Up Experiences permission. As of
Spring ’20 and later, only users with permission to edit moderation rules can access this object.

Fields

**Field Name** **Field Type** **Description**

`Description` string A description of the keyword list.

`keywords` Keyword[] The keywords you want moderate in your Experience Cloud site.


Metadata Types KeywordList

**Field Name** **Field Type** **Description**

`masterLabel` string Required. Label for the keyword list.

Keyword

Keywords in the keyword list.

**Field Name** **Field Type** **Description**

`keyword` string Required. Keywords you want to moderate.

**•** Keywords can only be up to 100 characters and can include letters,
numbers, spaces, and special characters.

**•** Wildcard characters aren’t supported.

Declarative Metadata Sample Definition

The following is an example of a KeywordList component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <KeywordList xmlns="http://soap.sforce.com/2006/04/metadata">

     <masterLabel>Bad Word List</masterLabel>

     <description>List of bad words updated by Joe in Nov 2015.</description>

     <keywords>

      <keyword>bad-word</keyword>

     </keywords>

     <keywords>

      <keyword>b a d w o r d</keyword>

     </keywords>

     <keywords>

      <keyword>b@dword</keyword>

     </keywords>

   </KeywordList>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <types>

      <name>KeywordList</name>

      <members>site1.badword_list</members>

     </types>

     <version>36.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types Layout Layout

Represents the metadata associated with a page layout. For more information, see Page Layouts in Salesforce Help.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

This type extends the Metadata metadata type and inherits its `fullName` field.

Note: To edit the Ideas layout, specify it by name in the `package.xml` file. In `package.xml`, use this code to retrieve the
Ideas layout. In the `<members>` tag, specify the object name (Idea) and then the layout name (Idea Layout), separated by a
hyphen.

```
      <types>

        <members>Idea-Idea Layout</members>

        <name>Layout</name>

      </types>

```

File Suffix and Directory Location

### Layouts are stored in the layouts directory of the corresponding package directory. The extension is .layout .

Note: Retrieving a component of this metadata type in a project makes the component appear in any Profile and PermissionSet
components that are retrieved in the same package.

Version

### Layouts are available in API version 13.0 and later.

Fields

This metadata type represents the valid values that define a page layout.

**Field Name** **Field Type** **Description**

`customButtons` string[] The custom buttons for this layout. Each button is a
reference to a WebLink on the same object. For example,

a ButtonLink refers to a Weblink on the same standard or
custom object named ButtonLink.

`customConsoleComponents` CustomConsoleComponents Represents custom console components (Visualforce pages,
lookup fields, or related lists; Canvas apps not available) on

a page layout. Custom console components only display
in the Salesforce console.

`emailDefault` boolean Only relevant if showEmailCheckbox is set; indicates the
default value of that checkbox.

`excludeButtons` string[] List of standard buttons to exclude from this layout. For
example,


Metadata Types Layout

**Field Name** **Field Type** **Description**

```
                                <excludeButtons>Delete</excludeButtons>
```

excludes the **Delete** button from this layout.

`feedLayout` FeedLayout Represents the values that define the feed view of a
feed-based page layout. Feed-based layouts are available

on Account, Case, Contact, Lead, Opportunity, custom, and
external objects. They include a feed view and a detail view.

`headers` LayoutHeader[]
(enumeration of type string)

`layoutSections` LayoutSection[]

Layout headers are currently only used for tagging, and
only appear in the UI if tagging is enabled. Valid string
values are:

**•** `PersonalTagging` —tag is private to user.

**•** `PublicTagging` —tag is viewable any other user
who can access the record.

The main sections of the layout containing fields, s-controls,
and custom links. The order here determines the layout
order.

`miniLayout` MiniLayout A mini layout is used in the mini view of a record in the
Console tab, hover details, and event overlays.

`multilineLayoutFields` string[]

`platformActionList` PlatformActionList

`quickActionList` QuickActionList

Fields for the special multiline layout fields that appear in
OpportunityProduct layouts. These fields are otherwise
similar to `miniLayoutFields` .

The list of actions and their order that appear in the
Salesforce mobile app action bar for the layout.

This field is available in API version 34.0 and later.

The list of quick actions that display in the full Salesforce
site for the page layout. This field is available in API version
28.0 and later.

`relatedContent` RelatedContent The Related Content section of the page layout. This field
is available in API version 29.0 and later.

`relatedLists` RelatedListItem[] The related lists for the layout, listed in the order they
appear in the user interface.

`relatedObjects` string[] The list of related objects that appears in the mini view of
the console. In database terms, these objects are foreign

key fields on the object for the layout. For more information,
see Choose Related Objects for the Agent Console’s Mini
View in Salesforce Help.

`runAssignmentRulesDefault` boolean

Only relevant if
`showRunAssignmentRulesCheckbox` is set;
indicates the default value of that checkbox.


Metadata Types Layout

**Field Name** **Field Type** **Description**

`showEmailCheckbox` boolean Only allowed on Case, CaseClose, and Task layouts. If set, a
checkbox appears to show email.

`showHighlightsPanel` boolean

If set, the highlights panel displays on pages in the
Salesforce console. This field is available in API version 22.0
and later.

`showInteractionLogPanel` boolean If set, the interaction log displays on pages in the Salesforce
console. This field is available in API version 22.0 and later.

`showKnowledgeComponent` boolean

Only allowed on Case layouts. If set, the Knowledge sidebar
displays on cases in the Salesforce console. This field is
available in API version 20.0 and later.

`showRunAssignmentRulesCheckbox` boolean Only allowed on Case, Lead, and Account objects. If set, a
checkbox appears on the page to show assignment rules.

`showSolutionSection` boolean Only allowed on CaseClose layout. If set, the built-in solution
information section shows up on the page.

`showSubmitAndAttachButton` boolean

Only allowed on Case layout. If set, the **Submit & Add**
**Attachment** button displays on case edit pages to portal
users in the Customer Portal.

`summaryLayout` SummaryLayout Controls the appearance of the highlights panel in
Salesforce Classic, which summarizes key fields in a grid at

the top of a page layout, when Case Feed is enabled. This
field is available in API version 18.0 and later.

CustomConsoleComponents

Represents custom console components (Visualforce pages, lookup fields, or related lists; Canvas apps not available) on a page layout.
Custom console components only appear in the Salesforce console. Available in API version 25.0 and later.

**Field Name** **Field Type** **Description**

`primaryTabComponents` PrimaryTabComponents Represents custom console components on primary tabs in the Salesforce
console. Available in API version 25.0 and later.

`subtabComponents` SubtabComponents Represents custom console components on subtabs in the Salesforce
console. Available in API version 25.0 and later.

PrimaryTabComponents

Represents custom console components on primary tabs in the Salesforce console. Available in API version 25.0 and later.

**Field Name** **Field Type** **Description**

`component` ConsoleComponent[] Represents a custom console component (Visualforce page, lookup field,
or related lists; Canvas apps not available) on a section of a page layout.


Metadata Types Layout

**Field Name** **Field Type** **Description**

Custom console components only appear in the Salesforce console. This
field is available in API version 29.0 and earlier.

`containers` Container[] Represents a location and style to display more than one custom console
component on the sidebars of the Salesforce console. You can specify

up to five components for each of the four locations (left, right, top, and
bottom). This field is available in API version 30.0 and later.

ConsoleComponent

Represents a custom console component (Visualforce page, lookup field, or related lists; Canvas apps not available) on a section of a
page layout. Custom console components only appear in the Salesforce console. Available in API version 25.0 and later.

**Field Name** **Field Type** **Description**

`height` int

`location` string

Required for components with a location of top or bottom. The height
of the custom console component. The value must be specified in pixels
and be greater than 0 but less than 999.

Required. The location of the custom console component on the page
layout. Valid values are right, left, top, and bottom. A component can
have one location for each page layout.

`visualforcePage` string Required. The unique name of the custom console component. For
example, ConsoleComponentPage.

`width` int

Container

Required for components with a location of left or right. The width of the
custom console component. The value must be specified in pixels and
be greater than 0 but less than 999.

Represents a location and style to display more than one custom console component in the sidebars of the Salesforce console. For
example, you can show multiple components in the right sidebar of the console with a style of either stack, tabs, or accordion. Available
in API version 30.0 and later.

**Field Name** **Field Type** **Description**

`height` int

`isContainerAutoSizeEnabled` boolean

Required for components with a location of top or bottom. The height
of the components’ container. The `unit` field determines the unit of
measurement, in pixels or percent.

Required. If set to `true`, stacked console components in the sidebars
autosize vertically. Set to `true` by default for newly created console
components. Available in API version 32.0 and later.

`region` string Required. The location of the components’ container. Valid values include:

**•** `right`


Metadata Types Layout

**Field Name** **Field Type** **Description**

**•** `left`

**•** `top`

**•** `bottom`

`sidebarComponents` SidebarComponent[] Represents a specific custom console component to display in the
components’ container.

`style` string Required. The style of the container to display multiple components.
Valid values include:

**•** `stack` —a content area with multiple frames.

**•** `tabs` —a single content area with a list of multiple panels.

**•** `accordian` —a collapsible content area.

`unit` string

`width` int

SidebarComponent

Required. The unit of measurement, in pixels or percent, for the height
or width of the components’ container.

Pixel values are simply the number of pixels, for example, `500`, and must
be greater than 0 but less than 999. Percentage values must include the

percent sign, for example, `20%`, and must be greater than 0 but less than
100.

Required for components with a location of right or left. The width of the
components’ container. The `unit` field determines the unit of
measurement, in pixels or percent.

Represents a specific custom console component to display in a container that hosts multiple components in one of the sidebars of the
Salesforce console. You can specify up to five components for each of the four container locations (left, right, top, and bottom). Available
in API version 30.0 and later.

**Field Name** **Field Type** **Description**

`componentType` string Specifies the component type. Valid values are `KnowledgeOne`,
`Lookup`, `Milestones`, `RelatedList`, `Topics`, `Files`, and

`CaseExperts` . This field is available in API version 31.0 and later. The
`Files` and `CaseExperts` values are available in API version 32.0
and later.

Case Experts is available through a pilot program.

`createAction` string If the component is a lookup field, the name of the quick action used to
create a record. This field is available in API version 42.0 and later.

`enableLinking` boolean

If the component is a lookup field, lets users associate a record with this
field. This field is available in API version 42.0 and later.

If false, the createAction and updateAction can’t be retrieved.


Metadata Types Layout

**Field Name** **Field Type** **Description**

`height` int

Required for components with a location of top or bottom. The height
of the component in the container. The `unit` field determines the unit
of measurement, in pixels or percent.

`label` string The name of the component as it appears to console users. Available for
components in a container with the style of tabs or accordion.

`lookup` string If the component is a lookup field, the name of the field.

`page` string If the component is a Visualforce page, the name of the Visualforce page.

`relatedlists` RelatedList[] If the component is a related list, the name of the list. This field is available
in API version 31.0 and later.

`unit` string

The unit of measurement, in pixels or percent, for the height or width of
the component in the container.

Pixel values are simply the number of pixels, for example, `500`, and must
be greater than 0 but less than 999. Percentage values must include the

percent sign, for example, `20%`, and must be greater than 0 but less than
100.

`updateAction` string If the component is a lookup field, the name of the quick action used to
update a record. This field is available in API version 42.0 and later.

`width` int

RelatedList

Required for components with a location of right or left. The width of the
component in the container. The `unit` field determines the unit of
measurement, in pixels or percent.

Represents related list custom components on the sidebars of the Salesforce console. Available in API version 31.0 and later.

**Field Name** **Field Type** **Description**

`hideOnDetail` boolean If set to `true`, the related list is hidden from detail pages where it
appears as a component to prevent duplicate information from showing.

`name` string The name of the component as it appears to console users.

SubtabComponents

Represents custom console components on subtabs in the Salesforce console. Available in API version 25.0 and later.

**Field Name** **Field Type** **Description**

`component` ConsoleComponent[] Represents a custom console component (Visualforce page, lookup field,
or related lists; Canvas apps not available) on a section of a page layout.

Custom console components only appear in the Salesforce console. This
field is available in API version 29.0 and earlier.


Metadata Types Layout

**Field Name** **Field Type** **Description**

`containers` Container[] Represents a location and style to display more than one custom console
component on the sidebars of the Salesforce console. You can specify

up to five components for each of the four locations (left, right, top, and
bottom). This field is available in API version 30.0 and later.

FeedLayout

Represents the values that define the feed view of a feed-based page layout. Feed-based layouts are available on Account, Case, Contact,
Lead, Opportunity, custom, and external objects. They include a feed view and a detail view. Available in API version 30.0 and later.

**Field Name** **Field Type** **Description**

`autocollapsePublisher` boolean Specifies whether the publisher is automatically collapsed when the
page loads ( `true` ) or not ( `false` ).

`compactFeed` boolean

Specifies whether the feed-based page layout uses a compact feed
( `true` ) or not ( `false` ). If set to `true`, feed items on the page are
collapsed by default, and the feed view has an updated design.

```
feedFilterPosition

```

FeedLayoutFilterPosition Where the feed filters list is included in the layout. Valid values are:
(enumeration of type

**•** `centerDropDown` —as a dropdown list in the center column.

string)

**•** `centerDropDown` —as a dropdown list in the center column.

**•** `leftFixed` —as a fixed list in the left column.

**•** `leftFloat` —as a floating list in the left column.

`feedFilters` FeedLayoutFilter[] The individual filters displayed in the feed filters list.

`fullWidthFeed` boolean Specifies whether the feed expands horizontally to take up all available
space on the page ( `true` ) or not ( `false` ).

`hideSidebar` boolean Specifies whether the sidebar is hidden ( `true` ) or not ( `false` ).

`leftComponents` FeedLayoutComponent[] The individual components displayed in the left column of the feed view.

`rightComponents` FeedLayoutComponent[] The individual components displayed in the right column of the feed
view.

FeedLayoutComponent

Represents a component in the feed view of a feed-based page layout. Available in API version 30.0 and later.

**Field Name** **Field Type** **Description**

```
componentType

```

FeedLayoutComponentType Required. The type of component. Valid values are:
(enumeration of type

**•** `HelpAndToolLinks` —icons that link to the help topic for the

string)

page, the page layout, and, the printable view of the page. Available
only on Case layouts.

**•** `CustomButtons` —a custom button.


Metadata Types Layout

**Field Name** **Field Type** **Description**

**•** `Following` —an icon that toggles between a Follow button (if
the user viewing a record doesn’t already follow it) and a Following
indicator (if the user viewing a record does follow it).

**•** `Followers` —a list of users who follow the record.

**•** `CustomLinks` —a custom link.

**•** `Milestones` —the milestone tracker, which lets users see the
status of a milestone on a case. Available only on Case layouts.

**•** `Topics` —a list of topics related to the record.

**•** `CaseUnifiedFiles` —a list of all files that are attached to the
case.

**•** `Visualforce` —a custom Visualforce component.

`height` int The height, in pixels, of the component. Doesn’t apply to

```
                           standardComponents

```

`page` string The name of a Visualforce page being used as a custom component.

FeedLayoutFilter

Represents a feed filter option in the feed view of a feed-based page layout. A filter must have only `standardFilter` or
`feedItemType` set. Available in API version 30.0 and later.

**Field Name** **Field Type** **Description**

`feedFilterName` string

The name of a CustomFeedFilter component. Names are prefixed with
the name of the parent object. For example,
_`Case.MyCustomFeedFilter`_ .

```
feedFilterType

feedItemType

```

FeedLayoutFilterType The type of filter. Valid values are:
(enumeration of type

**•** `AllUpdates`

string)

FeedItemType The type of feed item to display. Valid values are:
(enumeration of type

**•** `ActivityEvent` —feed items related to activity on tasks and

string)

events associated with a case. Available only on Case layouts.

**•** `AdvancedTextPost` –feed items related to group
announcements posted on a feed. This value is available in API
version 31.0 and later.

**•** `AnnouncementPost` –Not used.

**•** `ApprovalPost` —feed items related to approvals that are
submitted on a feed.

**•** `AttachArticleEvent` —feed items for activity related to
attaching articles to cases. Available only on Case layouts.


**•** `AllUpdates` —shows all feed items on a record.

**•** `FeedItemType` —shows feed items only for a particular type of
activity on the record.

Metadata Types Layout

**Field Name** **Field Type** **Description**

**•** `BasicTemplateFeedItem` —Not used.

**•** `CallLogPost` —feed items for activity from the Log a Call action.
Available only on layouts for objects that support Activities (tasks
and events).

**•** `CanvasPost` —feed items related to posts that a canvas app
makes on a feed.

**•** `CaseCommentPost` —feed items for activity from the Case Note
action. Available only on Case layouts.

**•** `ChangeStatusPost` —feed items for activity from the Change
Status action. Available only on Case layouts.

**•** `ChatTranscriptPost` —feed items for activity related to
attaching Chat transcripts to cases. Available only on Case layouts.

**•** `CollaborationGroupCreated` —feed items related to
creating a public group.

**•** `CollaborationGroupUnarchived` —Not used.

**•** `ContentPost` —feed items related to attaching a file to a post.

**•** `CreatedRecordEvent` —feed items related to creating a record
from the publisher.

**•** `DashboardComponentSnapshot` —feed items related to
posting a dashboard snapshot on a feed.

**•** `EmailMessageEvent` —feed items for activity from the Email
action. Available only on Case layouts.

**•** `FacebookPost` —Not used.

**•** `LinkPost` —feed items related to attaching a URL to a post.

**•** `MilestoneEvent` —feed items for changes to the milestone
status on a case. Available only on Case layouts.

**•** `PollPost` —feed items related to posting a poll on a feed.

**•** `ProfileSkillPost` —feed items related to skills added to a
user’s Chatter profile. This value is available in API version 31.0 and
later.

**•** `QuestionPost` —feed items related to posting a question on a
feed. This value is available in API version 31.0 and later.

**•** `ReplyPost` —feed items for activity from the Portal action.
Available only on Case layouts.

**•** `RypplePost` —feed items related to creating a Thanks badge in
WDC.

**•** `SocialPost` —feed items for activity on Twitter from the Social
Post action.

**•** `TextPost` —feed items for creating a text post from the publisher.

**•** `TrackedChange` —feed items related to a change or group of
changes to a tracked field.

**•** `UserStatus` —Not used.


Metadata Types Layout

MiniLayout

Represents a mini view of a record in the Console tab, hover details, and event overlays.

**Field Name** **Field Type** **Description**

`fields` string[] The fields for the mini-layout, listed in the order they appear in the UI.
Fields that appear here must appear in the main layout.

`relatedLists` RelatedListItem[]

LayoutSection

The mini related list, listed in the order they appear in the UI. You can’t
set sorting on mini related lists. Fields that appear here must appear in
the main layout.

LayoutSection represents a section of a page layout, such as the Custom Links section.

**Field Name** **Field Type** **Description**

`customLabel` boolean Indicates if this section’s label is custom or standard (built-in). Custom
labels can be any text, but must be translated. Standard labels have a

predefined set of valid values, for example System Information, which
are automatically translated.

`detailHeading` boolean Controls if this section appears in the detail page. In the UI, this setting
corresponds to the checkbox in the section details dialog.

`editHeading` boolean Controls if this section appears in the edit page.

`label` string The label; either standard or custom, based on the `customLabel`
flag.

`layoutColumns` LayoutColumn[] The columns of the layout, depending on the style. 1, 2, or 3 columns,
ordered left to right, are possible.

```
style

```

LayoutColumn

LayoutSectionStyle The style of the layout:
(enumeration of type

**•** `TwoColumnsTopToBottom`          - Two columns, tab goes top to

string)

bottom

**•** `TwoColumnsLeftToRight`          - Two columns, tab goes left to
right

**•** `OneColumn`          - One column

**•** `CustomLinks`          - Contains custom links only

LayoutColumn represents the items in a column within a layout section.

**Field Name** **Field Type** **Description**

`layoutItems` LayoutItem[] The individual items within a column (ordered from top to bottom).


Metadata Types Layout

**Field Name** **Field Type** **Description**

`reserved` string This field is reserved for Salesforce. The field resolves an issue with some
SOAP libraries. Any value entered in the field is ignored.

LayoutItem

LayoutItem represents the valid values that define a layout item. An item must have only one of the following values set: component,
customLink, field, s-control, page, analyticsCloudComponent, or reportChartComponent.

**Field Name** **Field Type** **Description**

`behavior` UiBehavior (enumeration of type string) Determines the field behavior. Valid string values:

**•** `Edit` —The layout field can be edited but isn’t
required.

**•** `Required` —The layout field can be edited and is
required.

**•** `Readonly` —The layout field is read-only.

Explicitly specifying UiBehavior for Knowledge articles
results in an exception.

`canvas` string

`component` string

Reference to a canvas app.

This field is available in API version 31.0 and later.

Reference to a component. Value must be
_`sfa:socialCard`_ .

This field is available in API version 30.0 and later. This
field is allowed only inside a `RelatedContentItem` .

_`sfa:socialCard`_ is supported only on page layouts
for contacts, accounts, and leads.

`customLink` string The `customLink` reference. This field is allowed only
inside a `CustomLink layoutSection` .

`emptySpace` boolean Controls if this layout item is a blank space.

`field` string The field name reference, relative to the layout object,
for example `Description` or `MyField__c` .

`height` int For s-control and pages only, the height in pixels.

`page` string Reference to a Visualforce page.

`analyticsCloudComponent` AnalyticsCloudComponentLayoutItem

Refers to a CRM Analytics dashboard that you can add
to a standard or custom object page.

This field is available in API version 34.0 and later.

`reportChartComponent` ReportChartComponentLayoutItem Refers to a report chart that you can add to a standard
or custom object page.


Metadata Types Layout

**Field Name** **Field Type** **Description**

`scontrol` string Reference to an s-control.

`showLabel` boolean For s-control and pages only, whether to show the label.

`showScrollbars` boolean For s-control and pages only, whether to show scrollbars.

`width` string For s-control and pages only, the width in pixels or
percent. Pixel values are simply the number of pixels, for

example, `500` . Percentage values must include the
percent sign, for example, `20%` .

AnalyticsCloudComponentLayoutItem

Represents the settings for a CRM Analytics dashboard on a standard or custom page. Available in API version 34.0 and later.

**Field Name** **Field Type** **Description**

`assetType` string Required. Specifies the type of CRM Analytics asset to add. The available
asset type is `dashboard` .

`devName` string Required. Unique development name of the dashboard to add.

`error` string Error string; only populated if an error occurred in the underlying
dashboard.

`filter` string

Communicates initial dashboard filters for mapping data fields in the
dashboard to the object’s fields, so that the dashboard shows only the
data that’s relevant for the record being viewed.

`height` int Specifies the height of the dashboard, in pixels. The default is `400` .

`hideOnError` boolean Controls whether users see a dashboard that has an error. When this
attribute is set to `true`, if the dashboard has an error, the dashboard

doesn’t appear on the page. When set to `false`, the dashboard appears
but doesn’t show any data except the error. An error can happen when
a user doesn’t have access to CRM Analytics or to the dashboard. The
default is `true` .

`showSharing` boolean If set to `true`, and the dashboard is shareable, then the dashboard
shows the Share icon. Users can click the icon to open the Share dialog

and post or download from the dashboard. If set to `false`, the
dashboard doesn’t show the Share icon. This field is available in API
version 37.0 and later.

`showTitle` boolean If `true`, includes the dashboard’s title above the dashboard. If `false`,
the dashboard appears without a title. The default is `true` .

`width` string

Specifies the width of the dashboard, in pixels or percent. Pixel values
are simply the number of pixels, for example, `500` . Percentage values
must include the percent sign, for example, `20%` . The default is `100%` .


Metadata Types Layout

ReportChartComponentLayoutItem

Represents the settings for a report chart on a standard or custom page.

**Field Name** **Field Type** **Description**

`cacheData` boolean

Indicates whether to use cached data when displaying the chart. When
the attribute is set to `true`, data is cached for 24 hours. If the attribute
is set to `false`, the report isn’t run every time the page is refreshed.

This field is available in API version 29.0 and later.

`contextFilterableField` string Unique development name of the field by which a report chart is filtered
to return data relevant to the page. If set, the ID field for the parent object

of the page or report type is the chart data filter. The parent object for
the report type and the page must match for a chart to return relevant
data.

`error` string

Error string; only populated if an error occurred in the underlying report.

This field is available in API version 31.0 and later.

`hideOnError` boolean Controls whether users see a chart that has an error. When there’s an
error and this attribute is set, the chart doesn’t show any data except the

error. An error can happen for many reasons, such as when a user doesn’t
have access to fields used by the chart or a chart has been removed from
the report. Set the attribute to `true` to hide the chart from a page on
error.

This field is available in API version 29.0 and later.

`includeContext` boolean If `true`, filters the report chart to return data that’s relevant to the page.

`reportName` string Unique development name of a report that includes a chart.

`showTitle` boolean If `true`, applies the title from the report to the chart.

`size` The chart size is medium when no value is specified. Valid values:
ReportChartComponentSize

**•** `SMALL`
(enumeration of type
string) **•** `MEDIUM`

**•** `LARGE`

PlatformActionList

PlatformActionList represents the list of actions and their order that appear in the Salesforce mobile app action bar for the layout. Available
in API version 34.0 and later.

**Field Name** **Field Type** **Description**

```
actionListContext

```

PlatformActionListContext Required. The context of the action list. Valid values are:
(enumeration of

**•** `Assistant`

type string)


Metadata Types Layout

**Field Name** **Field Type** **Description**

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

`platformActionListItems` PlatformActionListItem[] The actions in the PlatformActionList.

`relatedSourceEntity` string

PlatformActionListItem

When the `ActionListContext` is RelatedList or RelatedListRecord,
this field represents the API name of the related list to which the action
belongs.

PlatformActionListItem represents an action in the PlatformActionList. Available in API version 34.0 and later.

**Field Name** **Field Type** **Description**

`actionName` string The API name for the action in the list.

```
actionType

```

PlatformActionType The type of action. Valid values are:
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


Metadata Types Layout

**Field Name** **Field Type** **Description**

Call, Map, View Website, and Read News. Except for the Call action, you
can’t edit productivity actions.

**•** `QuickAction` —A global or object-specific action.

**•** `StandardButton` —A predefined Salesforce button such as New, Edit,
and Delete.

`sortOrder` int The placement of the action in the list.

`subtype` string The subtype of the action. For quick actions, the subtype is
`QuickActionType` . For custom buttons, the subtype is

`WebLinkTypeEnum` . For action links, subtypes are `Api`, `ApiAsync`,
`Download`, and `Ui` . Standard buttons and productivity actions have no
subtype.

QuickActionList

QuickActionList represents the list of actions associated with the page layout. Available in API version 28.0 and later.

**Field Name** **Field Type** **Description**

`quickActionListItems` QuickActionListItem[] Array of zero or more QuickActionList objects.

QuickActionListItem

QuickActionListItem represents an action in the QuickActionList. Available in API version 28.0 and later.

**Field Name** **Field Type** **Description**

`quickActionName` string The API name of the action.

RelatedContent

RelatedContent represents the Mobile Cards section of the page layout. Available in API version 29.0 and later.

**Field Name** **Field Type** **Description**

`relatedContentItems` RelatedContentItem[] A list of layout items in the Mobile Cards section of the page layout.

RelatedContentItem

RelatedContentItem represents an individual item in the RelatedContentItem list. Available in API version 29.0 and later.

**Field Name** **Field Type** **Description**

`layoutItem` LayoutItem An individual LayoutItem in the Mobile Cards section.


Metadata Types Layout

RelatedListItem

RelatedListItem represents a related list in a page layout.

**Field Name** **Field Type** **Description**

`customButtons` string[] A list of custom buttons that are used on the related list.

`excludeButtons` string[] A list of buttons that are excluded from the related list.

`fields` string[]

A list of fields that are displayed in the related list.

Retrieval of standard fields on related lists uses aliases instead of field or
API names. For example, the `Fax`, `Mobile`, and `Home Phone` fields
are retrieved as Phone2, Phone3, and Phone4, respectively.

`quickActions` string[] A list of quick actions that are used on the related list.

`relatedList` string Required. The name of the related list.

`sortField` string The name of the field that is used for sorting.

```
sortOrder

```

SummaryLayout

SortOrder If the `sortField` is set, the `sortOrder` field determines the sort
(enumeration of type order.
string)

**•** `Asc`          - Sort in ascending order

**•** `Desc`          - Sort in descending order

When Case Feed is enabled, controls the appearance of the highlights panel in Salesforce Classic, which summarizes key fields in a grid
at the top of a page layout. Available in API version 25.0 and later.

**Field Name** **Field Type** **Description**

`masterLabel` string Required. The name of the layout label.

`sizeX` int Required. Number of columns in the highlights pane, from 1 through 4
(inclusive).

`sizeY` int Required. Number of rows in each column, either 1 or 2.

`sizeZ` int Reserved for future use. If provided, the setting is visible to users.

`summaryLayoutItems` SummaryLayoutItem[]

Controls the appearance of an individual field and its column and row
position within the highlights panel grid, when Case Feed is enabled. At
least one is required.

```
summaryLayoutStyle

```

SummaryLayoutStyle Highlights panel style. Valid string values are:
(enumeration of type

**•** Default

string)

**•** Default

**•** QuoteTemplate

**•** DefaultQuoteTemplate

**•** CaseInteraction


Metadata Types Layout

**Field Name** **Field Type** **Description**

**•** QuickActionLayoutLeftRight (Available in API version 28.0 and later.)

**•** QuickActionLayoutTopDown (Available in API version 28.0 and later.)

SummaryLayoutItem

Controls the appearance of an individual field and its column and row position within the highlights panel grid, when Case Feed is
enabled. You can have two fields per each grid in a highlights panel. Available in API version 25.0 and later.

**Field Name** **Field Type** **Description**

`customLink` string The `customLink` reference, if the item is a custom link.

`field` string The field name reference, relative to the page layout. Must be a standard
or custom field that also exists on the detail page.

`posX` int Required. The item’s column position in the highlights panel grid. Must
be within the range of `sizeX` .

`posY` int Required. The item’s row position in the highlights panel grid. Must be
within the range of `sizeY` .

`posZ` int Reserved for future use. If provided, the setting is visible to users.

Declarative Metadata Sample Definition

This sample defines a page layout.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Layout xmlns="http://soap.sforce.com/2006/04/metadata">

     <customConsoleComponents>

      <primaryTabComponents>

        <container>

          <region>left</region>

         <style>Stack</style>

         <unit>Pixel</unit>

         <width>101</width>

         <sidebarComponent>

             <width>60</width>

             <page>simplepage1</page>

             <unit>Percentage</unit>

         </sidebarComponent>

         <sidebarComponent>

             <width>40</width>

             <page>Hello_World</page>

             <unit>Percentage</unit>

         </sidebarComponent>

        </container>

      </primaryTabComponents>

      <subtabComponents>

```


Metadata Types Layout

```
        <component>

         <location>top</location>

         <visualforcePage>ConsoleComponentPage2</visualforcePage>

         <height>200</height>

        </component>

      </subtabComponents>

     </customConsoleComponents>

      <customButtons>ButtonLink</customButtons>

      <layoutSections>

        <editHeading>true</editHeading>

        <label>Information</label>

        <layoutColumns>

           <layoutItems>

             <behavior>Required</behavior>

             <field>Name</field>

           </layoutItems>

           <layoutItems>

             <height>180</height>

             <scontrol>LayoutSControl</scontrol>

             <showLabel>true</showLabel>

             <showScrollbars>true</showScrollbars>

             <width>50%</width>

           </layoutItems>

           <layoutItems>

             <reportChartComponent>

               <contextFilterableField>CUST_ID</contextFilterableField>

               <includeContext>true</includeContext>

               <reportName>Open_Accounts_by_Cases</reportName>

               <showTitle>false</showTitle>

               <size>LARGE</size>

             <reportChartComponent>

           </layoutItems>

        </layoutColumns>

        <layoutColumns>

           <layoutItems>

             <behavior>Edit</behavior>

             <field>OwnerId</field>

           </layoutItems>

           <layoutItems>

             <behavior>Edit</behavior>

             <field>CurrencyIsoCode</field>

           </layoutItems>

        </layoutColumns>

        <style>TwoColumnsTopToBottom</style>

      </layoutSections>

      <layoutSections>

        <editHeading>true</editHeading>

        <label>System Information</label>

        <layoutColumns>

           <layoutItems>

             <behavior>Readonly</behavior>

             <field>CreatedById</field>

           </layoutItems>

           <layoutItems>

```


Metadata Types Layout

```
             <behavior>Readonly</behavior>

             <field>Alpha1__c</field>

           </layoutItems>

           <layoutItems>

             <height>200</height>

             <page>mcanvasPage</page>

             <showLabel>true</showLabel>

             <showScrollbars>false</showScrollbars>

             <width>100%</width>

           </layoutItems>

        </layoutColumns>

        <layoutColumns>

           <layoutItems>

             <behavior>Readonly</behavior>

             <field>LastModifiedById</field>

           </layoutItems>

           <layoutItems>

             <behavior>Edit</behavior>

             <field>TextArea__c</field>

           </layoutItems>

        </layoutColumns>

        <style>TwoColumnsTopToBottom</style>

      </layoutSections>

      <layoutSections>

        <customLabel>true</customLabel>

        <detailHeading>true</detailHeading>

        <label>Custom Links</label>

        <layoutColumns>

           <layoutItems>

             <customLink>CustomWebLink</customLink>

           </layoutItems>

        </layoutColumns>

        <style>CustomLinks</style>

      </layoutSections>

      <quickActionList>

        <quickActionListItems>

           <quickActionName>FeedItem.TextPost</quickActionName>

        </quickActionListItems>

        <quickActionListItems>

           <quickActionName>FeedItem.ContentPost</quickActionName>

        </quickActionListItems>

        <quickActionListItems>

           <quickActionName>FeedItem.LinkPost</quickActionName>

        </quickActionListItems>

        <quickActionListItems>

           <quickActionName>FeedItem.PollPost</quickActionName>

        </quickActionListItems>

      </quickActionList>

      <relatedContent>

        <relatedContentItems>

           <layoutItem>

             <component>sfa:socialPanel</component>

           </layoutItem>

        <relatedContentItems>

```


Metadata Types Layout

```
      </relatedContent>

      <miniLayoutFields>Name</miniLayoutFields>

      <miniLayoutFields>OwnerId</miniLayoutFields>

      <miniLayoutFields>CurrencyIsoCode</miniLayoutFields>

      <miniLayoutFields>Alpha1__c</miniLayoutFields>

      <miniLayoutFields>TextArea__c</miniLayoutFields>

      <miniRelatedLists>

        <relatedList>RelatedNoteList</relatedList>

      </miniRelatedLists>

      <relatedLists>

        <fields>StepStatus</fields>

        <fields>CreatedDate</fields>

        <fields>OriginalActor</fields>

        <fields>Actor</fields>

        <fields>Comments</fields>

        <fields>Actor.Alias</fields>

        <fields>OriginalActor.Alias</fields>

        <relatedList>RelatedProcessHistoryList</relatedList>

      </relatedLists>

      <relatedLists>

        <relatedList>RelatedNoteList</relatedList>

      </relatedLists>

   </Layout>

```

This example shows a layout using `<summaryLayout>` .

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Layout xmlns="http://soap.sforce.com/2006/04/metadata">

      <layoutSections>

        <editHeading>true</editHeading>

        <label>System Information</label>

        <layoutColumns>

           <layoutItems>

             <behavior>Readonly</behavior>

             <field>CreatedById</field>

           </layoutItems>

           <layoutItems>

             <behavior>Required</behavior>

             <field>Name</field>

           </layoutItems>

        </layoutColumns>

        <layoutColumns>

           <layoutItems>

             <behavior>Readonly</behavior>

             <field>LastModifiedById</field>

           </layoutItems>

        </layoutColumns>

        <style>TwoColumnsTopToBottom</style>

      </layoutSections>

      <summaryLayout>

        <masterLabel>Great Name</masterLabel>

        <sizeX>4</sizeX>

        <sizeY>2</sizeY>

        <summaryLayoutItems>

           <posX>0</posX>

```


### Metadata Types LearningItemType

```
           <posY>0</posY>

           <field>Name</field>

        </summaryLayoutItems>

      </summaryLayout>

   </Layout>

```

This example shows a feed-based layout.

```
   <Layout>

   ...

      <feedLayout>

        <leftComponents>

           <componentType>customLinks</componentType>

        </leftComponents>

        <rightComponents>

           <componentType>follow</componentType>

        </rightComponents>

        <rightComponents>

           <componentType>followers</componentType>

        </rightComponents>

        <rightComponents>

           <componentType>visualforce</componentType>

           <page>accountCustomWidget</page>

           <height>200</height>

        </rightComponents>

        <hideSidebar>true</hideSidebar>

        <feedFilterPosition>centerDropDown</feedFilterPosition>

        <feedFilters>

      <feedFilerType>allUpdates</feedFilerType>

        </feedFilters>

        <feedFilters>

      <feedFilerType>feedItemType</feedFilerType>

      <feedItemType>CallLogPost</feedItemType>

        </feedFilters>

        <feedFilters>

      <feedFilerType>feedItemType</feedFilerType>

      <feedItemType>TextPost</feedItemType>

        </feedFilters>

      </feedLayout>

   ...

   </Layout>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### LearningItemType

Represents a custom exercise type that an Enablement user takes in an Enablement program in the Guidance Center. A custom exercise
type also requires a corresponding LearningItem record for the Guidance Center and corresponding EnblProgramTaskDefinition and
EnblProgramTaskSubCategory records for when admins create a program in Program Builder.


Metadata Types LearningItemType

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

LearningItemType components have the suffix `.learningItemType` and are stored in the `learningItemTypes` folder.

Version

LearningItemType components are available in API version 62.0 and later.

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
apexEvaluationHandler

apexSerializerDeserializer

customField

```

**Field Type**
string

**Description**
The ID of the Apex class that specifies how progress and completion of the custom
exercise is assessed when users take the program in the Guidance Center.

**Field Type**
string

**Description**
The ID of the Apex class that specifies how data related to the custom exercise type
is retrieved and deployed with change sets or managed packages.

**Field Type**
string


Metadata Types LearningItemType

**Field Name** **Description**

**Description**

[Required. The programmatic name of a custom lookup field on the LearningItem](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_learningitem.htm)
[object that references the custom object used with this custom exercise.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_learningitem.htm)

For example, if a custom exercise type shows a screen flow, maybe the custom object’s
name is `ScreenFlow_Object__c` and the custom field on LearningItem is
named `ScreenFlow_Field__c` [. For details, see Implement Custom Exercise](https://developer.salesforce.com/docs/sales/enablement/guide/enablement-custom-exercises-intro.html)
[Types for Enablement Programs in the](https://developer.salesforce.com/docs/sales/enablement/guide/enablement-custom-exercises-intro.html) _Sales Programs and Partner Tracks with_
_Enablement Developer Guide_ .

This field is unique within your organization.

```
customObject

developerName

icon

lightningComponentDefinition

```

**Field Type**
string

**Description**

Required. The programmatic name of the custom object used with this custom exercise.

For example, if a custom exercise type shows a screen flow, maybe the custom object’s
name is `ScreenFlow_Field__c` [. For details, see Implement Custom Exercise](https://developer.salesforce.com/docs/sales/enablement/guide/enablement-custom-exercises-intro.html)
[Types for Enablement Programs in the](https://developer.salesforce.com/docs/sales/enablement/guide/enablement-custom-exercises-intro.html) _Sales Programs and Partner Tracks with_
_Enablement Developer Guide_ .

This field is unique within your organization.

**Field Type**
string

**Description**

Required. The unique programmatic name for the LearningItemType record.

**Field Type**
string

**Description**
Required. The icon to use for the custom exercise type in the Guidance Center.

Use the format _**`iconType`**_ `:` _**`iconName`**_, where the values correspond to icon
[categories and names from the Salesforce Lightning Design System.](https://www.lightningdesignsystem.com/icons/)

**•** _**`iconType`**_ is the type of icon, such as `standard` or `doctype` .

**•** _**`iconName`**_ is the icon name, such as `flow` or `slide` .

For example, to use the Standard type Flow icon, this value is `standard:flow` .

**Field Type**
string

**Description**

Required. The ID of the Lightning Web Component used to show the custom exercise’s
content when a user opens the exercise in the Guidance Center.


### Metadata Types Letterhead

**Field Name** **Description**

This field sets the value of the `LightningComponentName` field on the
[LearningItemType object.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_learningitemtype.htm)

```
masterLabel

```

**Field Type**
string

**Description**

Required. A user-friendly name for the LearningItemType, which is defined when it’s
created.

Declarative Metadata Sample Definition

The following is an example of a LearningItemType component for a custom exercise type that shows a screen flow.

```
<?xml version="1.0" encoding="UTF-8"?>

<LearningItemType xmlns="http://soap.sforce.com/2006/04/metadata">

   <apexEvaluationHandler>ScreenFlowEvaluationHandler</apexEvaluationHandler>

  <apexSerializerDeserializer>ScreenFlowSerializerDeserializer</apexSerializerDeserializer>

   <customField>ScreenFlow_Field__c</customField>

   <customObject>ScreenFlow_Object__c</customObject>

   <developerName>ScreenFlowLearningItemType</developerName>

   <icon>standard:flow</icon>

   <lightningComponentDefinition>screenFlowViewer</lightningComponentDef>

   <masterLabel>Screen Flow Exercise</masterLabel>

</LearningItemType>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>ScreenFlowLearningItemType</members>

     <name>LearningItemType</name>

   </types>

   <version>62.0</version>

</Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### Letterhead

Represents formatting options for the letterhead in an email template. A letterhead defines the logo, page color, and text settings for
your HTML email templates. Use letterheads to ensure a consistent look and feel in your company’s emails.


Metadata Types Letterhead

For more information, see “Create Classic Letterheads for Email Templates” in the Salesforce online help. This type extends the Metadata
metadata type and inherits its `fullName` field.

File Suffix and Directory Location

The file suffix for letterheads is `.letter` and components are stored in the `letterhead` directory of the corresponding package
directory.

Version

Letterheads are available in API version 12.0 and later.

Fields

With the exception of logo, and horizontal and vertical alignment, all of these fields are required.

**Field Name** **Field Type** **Description**

`available` boolean Required. Indicates whether this letterhead can be used
( `true` ) or not ( `false` ), for example, in an email template.

`backgroundColor` string Required. The background color, in hexadecimal, for example
`#FF6600` .

`bodyColor` string Required. The body color in hexadecimal.

`bottomLine` LetterheadLine (enumeration of type string) Required. The style for the bottom line. Valid style values
include:

**•** `color` . The color of the line in hexadecimal, as a string
value.

**•** `height` . The height of the line, as an int value.

`description` string Text description of how this letterhead differs from other
letterheads.

`fullName` string

The internal name of the letterhead, based on the `name`,
but with white spaces and special characters escaped out
for validity.

`footer` LetterheadHeaderFooter Required. The style for the footer.

`header` LetterheadHeaderFooter Required. The style for the header.

`middleLine` LetterheadLine Required. The style for the middle border line in your
letterhead. Valid style values include:

**•** `color` . The color of the line in hexadecimal, as a string
value.

**•** `height` . The height of the line, as an int value.

`name` string Required. The name of the letterhead.


Metadata Types Letterhead

**Field Name** **Field Type** **Description**

`topLine` LetterheadLine Required. The style for the top horizontal line below the
header. Valid style values include:

**•** `color` . The color of the line in hexadecimal, as a string
value.

**•** `height` . The height of the line, as an int value.

LetterheadHeaderFooter

LetterheadHeaderFooter represents the properties of a header or footer.

**Field** **Field Type** **Description**

`backgroundColor` string Required. The background color of the header or footer in
hexadecimal format.

`height` DashboardComponent[] Required. The height of the header or footer.

`horizontalAlignment` LetterheadHorizontalAlignment The horizontal alignment of the header or footer. Valid values
(enumeration of type string) are:

**•** `None`

**•** `Left`

**•** `Center`

**•** `Right`

`logo` string The logo which is a reference to a document, for example
`MyFolder/MyDocument.gif` .

`verticalAlignment` LetterheadVerticalAlignment The vertical alignment of the header or footer. Valid values are:
(enumeration of type string)

**•** `None`

**•** `Top`

**•** `Middle`

**•** `Bottom`

LetterheadLine

LetterheadLine represents the properties of a line.

**Field** **Field Type** **Description**

`color` string Required. The color of the line in hexadecimal format.

`height` int Required. The height of the line.


### Metadata Types LightningBolt

Declarative Metadata Sample Definition

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Letterhead xmlns="http://soap.sforce.com/2006/04/metadata">

      <available>true</available>

      <backgroundColor>#CCCCCC</backgroundColor>

      <bodyColor>#33FF33</bodyColor>

      <bottomLine>

        <color>#3333FF</color>

        <height>5</height>

      </bottomLine>

      <description>INITIAL</description>

      <footer>

        <backgroundColor>#FFFFFF</backgroundColor>

        <height>100</height>

        <horizontalAlignment>Left</horizontalAlignment>

        <verticalAlignment>Top</verticalAlignment>

      </footer>

      <header>

        <backgroundColor>#FFFFFF</backgroundColor>

        <height>100</height>

        <horizontalAlignment>Left</horizontalAlignment>

        <verticalAlignment>Top</verticalAlignment>

      </header>

      <middleLine>

        <color>#AAAAFF</color>

        <height>5</height>

      </middleLine>

      <name>SimpleLetterheadLabel</name>

      <topLine>

        <color>#FF99FF</color>

        <height>5</height>

      </topLine>

   </Letterhead>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

### LightningBolt

Represents the definition of a Lightning Bolt Solution, which can include custom apps, flow categories, and Experience Builder templates.
This type extends the Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### LightningBolt components have the suffix .lightningBolt and are stored in the lightningBolts folder.


Metadata Types LightningBolt

Version

LightningBolt components are available in API version 43.0 and later.

Special Access Rules

To add Experience Builder templates to a Lightning Bolt Solution, enable digital experiences in your org.

Fields

**Field Name** **Field Type** **Description**

```
category

```

LightningBoltCategory Required. The primary industry that the Lightning Bolt Solution is aimed
(enumeration of at. Valid values are:
type string)

**•** `Communications`

**•** `Education`

**•** `FinancialServices`

**•** `GeneralBusiness`

**•** `Government`

**•** `HealthcareLifeSciences`

**•** `HighTech`

**•** `Manufacturing`

**•** `Media`

**•** `Nonprofits`

**•** `ProfessionalServices`

**•** `RealEstate`

**•** `Retail`

**•** `TravelTransportationHospitality`

`lightningBoltFeatures` LightningBoltFeatures[]
The list of feature descriptions of this Lightning Bolt Solution.

`lightningBoltImages` LightningBoltImages[] The list of images of this Lightning Bolt Solution.

`lightningBoltItems` LightningBoltItems[] The list of items (custom apps, flow categories, and Experience Builder
templates) that comprise this Lightning Bolt Solution.

`masterLabel` string Required. The label of the Lightning Bolt Solution, which appears on the
solution detail page.

`publisher` string Required. The name of the partner org associated with this Lightning
Bolt Solution.

`summary` string Required. The summary description of the Lightning Bolt Solution.


Metadata Types LightningBolt

LightningBoltFeatures

Represents the list of feature descriptions of a Lightning Bolt Solution.

**Field Name** **Field Type** **Description**

`description` string A description of the feature of the Lightning Bolt Solution.

`order` int Required. An integer specifying the position of this feature relative to others
in the list. 1 is the first position, and 4 is the max position.

`title` string Required. The title of the feature, which appears on the solution detail page.

LightningBoltImages

Represents the list of images of a Lightning Bolt Solution.

**Field Name** **Field Type** **Description**

`image` string Required. The developer name of the `ContentAsset` type, which is used
as a preview image for this Lightning Bolt Solution.

`order` int Required. An integer specifying the position of this image relative to others in
the list. 1 is the first position, and 3 is the max position.

LightningBoltItems

Represents the list of items (custom apps, flow categories, and Experience Builder templates) that comprise a Lightning Bolt Solution.

**Field Name** **Field Type** **Description**

`name` string Required. The name of the item, which appears on the solution detail page.

`type` string Required. The type of the item included in the Lightning Bolt Solution. Valid
values are:

**•** `CommunityTemplateDefinition`

**•** `CustomApplication`

**•** `FlowCategory`

Declarative Metadata Sample Definition

The following is an example of a LightningBolt component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <LightningBolt xmlns="http://soap.sforce.com/2006/04/metadata"

   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

      <category>Sales</category>

      <lightningBoltFeatures>

        <description>bb</description>

```


### Metadata Types LightningComponentBundle

```
        <order>1</order>

        <title>aa</title>

      </lightningBoltFeatures>

      <lightningBoltImages>

        <image>prm1</image>

        <order>1</order>

      </lightningBoltImages>

      <lightningBoltItems>

        <name>PolaConsole</name>

        <type>CustomApplication</type>

      </lightningBoltItems>

      <lightningBoltItems>

        <name>Banking_Service_Console</name>

        <type>CustomApplication</type>

      </lightningBoltItems>

      <lightningBoltItems>

        <name>Banking_Service_Portal</name>

        <type>CommunityTemplateDefinition</type>

      </lightningBoltItems>

      <lightningBoltItems>

        <name>Banking_Sales_Portal</name>

        <type>CommunityTemplateDefinition</type>

      </lightningBoltItems>

      <lightningBoltItems>

        <name>myorgdev__updatebenefits</name>

        <type>FlowCategory</type>

      </lightningBoltItems>

      <masterLabel>BoltTe</masterLabel>

      <publisher>aaaa</publisher>

      <summary>This is a summary.</summary>

   </LightningBolt>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>BoltTe</members>

        <name>LightningBolt</name>

      </types>

      <version>43.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### LightningComponentBundle

Represents a Lightning web component bundle. A bundle contains Lightning web component resources.


Metadata Types LightningComponentBundle

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Special Access Rules

LightningComponentBundle components can be created only in orgs with defined namespaces.

As of Summer ’20 and later, only your Salesforce org's internal users can access this type.

[For more information on packaging a Lightning web component bundle, see the Second-Generation Managed Packaging Developer](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/packaging_packageable_components.htm#mdc_lightning_component)
[Guide.](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/packaging_packageable_components.htm#mdc_lightning_component)

Fields

**Field Name** **Field Type** **Description**

`ai` (Beta) base64Binary An internal AI description of the Lightning web component. This description
[is supported only in orgs that have Setup with Agentforce (Beta) enabled. This](https://help.salesforce.com/s/articleView?id=release-notes.rn_setup_with_agentforce_beta.htm&release=260&type=5&language=en_US)

description enables Agentforce to analyze the component for inclusion in
[agent-generated Lightning pages. For more information, see Configure a](https://developer.salesforce.com/docs/platform/lwc/guide/use-config-for-agentforce.html)
[Component for Use in Setup with Agentforce (Beta).](https://developer.salesforce.com/docs/platform/lwc/guide/use-config-for-agentforce.html)

```
                          <ai>

                            <description>AI component description Example:

                          The component enables users to add and style text

