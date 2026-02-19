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

                          content for dashboards, supporting features such as

                          hyperlinks, bullet points, and text alignment. Ideal

                          for adding formatted text sections such as

                          instructions</description>

                            <property name="prop1" aiDescription="AI

                          description for prop1"/>

                            <property name="prop2" aiDescription="AI

                          description for prop2"/>

                          </ai>

```

Available in API version 66.0 and later.

`apiVersion` double A double value that binds the component to a Salesforce API version.

`capabilities` Capabilities[]

`description` string

A list of capabilities. A capability is something that a component can do, as
opposed to a target, which defines where you can use a component. Available
in API version 48.0 and later.

A user-facing description of the Lightning web component. This description
appears in list views, like the list of Lightning Components in Setup, and as a
tooltip in the builders like Lightning App Builder and Experience Builder.

`isExplicitImport` boolean Indicates whether imports between files are done explicitly by the developer
( `true` ) or implicitly by the framework ( `false` ).

`isExposed` boolean If `true`, the component is available to other namespaces. If `true` and a
`targets` value is also provided, the component is available to Salesforce


Metadata Types LightningComponentBundle

**Field Name** **Field Type** **Description**

builders such as Lightning App Builder and Experience Builder. If `false`, the
component isn't available to builders and other namespaces.

`lwcResources` LwcResources[] A list of resources inside a bundle.

`masterLabel` string The component title that appears in the list view.

`targetConfigs` base64Binary

Configurations for each target. Each target is a Lightning page type. For example,
this configuration allows a Lightning web component to be used on a Contact
record page in Lightning App Builder.

```
<targetConfigs>

   <targetConfig targets="lightning__RecordPage">

     <objects>

        <object>Contact</object>

     </objects>

   </targetConfig>

</targetConfigs>

```

`targets` Targets[] A list of targets where the Lightning web component can be used, such as in
Lightning App Builder or Experience Builder sites.

Capabilities

Represents a list of capabilities. A capability is something that a component can do, as opposed to a target, which defines where you
[can use a component. Available in API version 48.0 and later. For more information, see XML Configuration File Elements.](https://developer.salesforce.com/docs/platform/lwc/guide/reference-configuration-tags.html)

**Field** **Field Type** **Description**

`capability` string Specifies something that a component can do. Valid values are:

**•** `lightningCommunity__RelaxedCSP`

**•** `lightning__dynamicComponent`

**•** `lightning__ServerRenderable`

**•** `lightning__ServerRenderableWithHydration`

**•** `lightning__ServiceCloudVoiceToolkitApi`

LwcResources

Represents a list of resources inside a LightningComponentBundle.

**Field** **Field Type** **Description**

`lwcResource` LwcResource A resource inside a LightningComponentBundle.


Metadata Types LightningComponentBundle

LwcResource

Represents a resource inside a LightningComponentBundle.

**Field** **Field Type** **Description**

`filePath` string Required. The file path of a resource.

`source` base64Binary Required. The content of a resource.

Targets

[Represents a list of supported containers for a Lightning web component. For more information, see XML Configuration File Elements.](https://developer.salesforce.com/docs/platform/lwc/guide/reference-configuration-tags.html)

**Field** **Field Type** **Description**

`target` string

Specifies the type of Lightning page the component can be
added to in the builders, such as in Lightning App Builder,
Experience Builder, Flow Builder, or Document Builder.

[For valid values, see XML Configuration File Elements: target.](https://developer.salesforce.com/docs/platform/lwc/guide/reference-configuration-tags.html#target)

Declarative Metadata Sample Definition

This `package.xml` file retrieves all the LightningComponentBundle components in an org.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>*</members>

     <name>LightningComponentBundle</name>

   </types>

   <version>45.0</version>

</Package>

```

In the retrieved `zip` file, each Lightning web component is nested under an `lwc` folder.

This example shows the directory structure in the zip file of one component with a name of `hello` .

```
lwc

   hello

     hello.html

     hello.js

     hello.js-meta.xml

```

Here are the contents of the files in the `hello` directory.

Content of `hello.html` :

```
<template>

   <lightning-card title="Hello" icon-name="custom:custom14">

     <div class="slds-m-around_medium">

        Hello, {greeting}!

```


### Metadata Types LightningExperienceTheme

```
        </div>

      </lightning-card>

   </template>

```

Content of `hello.js` :

```
   import { LightningElement } from 'lwc';

   export default class Hello extends LightningElement {

      greeting = 'World';

   }

```

Content of `hello.js-meta.xml` .

```
   <?xml version="1.0" encoding="UTF-8"?>

   <LightningComponentBundle xmlns="http://soap.sforce.com/2006/04/metadata">

      <apiVersion>45.0</apiVersion>

      <isExposed>true</isExposed>

      <targets>

        <target>lightning__AppPage</target>

        <target>lightning__RecordPage</target>

        <target>lightning__HomePage</target>

      </targets>

   </LightningComponentBundle>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### LightningExperienceTheme

Represents the details of a custom theme, including the BrandingSet. Themes enable admins to specify configurable attributes, such as
three colors and five images. The colors and some of the images override SLDS token values and influence the generation of `app.css` .

To activate a custom theme with Metadata API, set the `activeThemeField` on the LightningExperienceSettings component to
the API name of the LightningExperienceTheme.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### LightningExperienceTheme components have the suffix .lightningExperienceTheme and are stored in the

`lightningExperienceThemes` folder.

Version

### LightningExperienceTheme components are available in API version 42.0 and later.


Metadata Types LightningExperienceTheme

Special Access Rules

The LightningExperieceTheme type is available when the S1DesktopAllowed permission is enabled in your org.

Fields

**Field Name** **Field Type** **Description**

`defaultBrandingSet` string Required. The ID of the BrandingSet properties associated with this
LightningExperienceTheme.

`description` string The optional description text of this LightningExperienceTheme. Limited
to 1000 characters.

Represents the version of Salesforce Lightning Design System (SLDS) on
which the theme is built.

Valid values are:

**•** `SLDS_v1`

**•** `SLDS_v2`

If you don’t define a value, the default value is `SLDS_v1` .

Available in API version 64.0 and later.

```
designSystemVersion

```

LightningDesignSystemVersion
(enumeration of
type string)

`isDarkModeEnabled` (beta) boolean Indicates whether individual users can enable dark mode ( `true` ) or not
( `false` ) for this LightningExperienceTheme. The default value is

`false` . Available for custom SLDS 2 themes in select editions. See
[Salesforce Cosmos Theme and SLDS 2 Availability. Available in API version](https://help.salesforce.com/s/articleView?id=xcloud.customize_ui_enhancedlex.htm&type=5&language=en_US)
65.0 and later.

Note: Dark mode is a pilot or beta service that is subject to the
[Beta Services Terms at Agreements - Salesforce.com or a written](https://www.salesforce.com/company/legal/agreements/)
Unified Pilot Agreement if executed by Customer, and applicable
[terms in the Product Terms Directory. Use of this pilot or beta](https://ptd.salesforce.com/)
service is at the Customer's sole discretion.

`masterLabel` string Required. The label for this LightningExperienceTheme, which displays
in Setup. Limited to 70 characters.

`shouldOverrideLoadingImage` boolean If `true`, the LightningExperienceTheme overrides the splash screen
image.

Declarative Metadata Sample Definition

The following is an example of a LightningExperienceTheme component. See BrandingSet on page 536 for an example of the BrandingSet
component.

```
<?xml version="1.0" encoding="UTF-8"?>

<LightningExperienceTheme xmlns="http://soap.sforce.com/2006/04/metadata">

   <defaultBrandingSet>SummerCelebrationBrand</defaultBrandingSet>

   <description>Theme for summer celebration week.</description>

```


### Metadata Types LightningMessageChannel

```
      <masterLabel>Summer Celebration</masterLabel>

      <shouldOverrideLoadingImage>false</shouldOverrideLoadingImage>

   </LightningExperienceTheme>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>LEXTHEMINGThemeName</members>

        <name>BrandingSet</name>

      </types>

      <types>

      <members>Summer Celebration</members>

      <name>LightningExperienceTheme</name>

      </types>

      <version>42.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### LightningMessageChannel

Represents the metadata associated with a Lightning Message Channel. A Lightning Message Channel represents a secure channel to
communicate across UI technologies, such as Lightning Web Components, Aura Components, and Visualforce.

This type extends the Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Note: Before you include a Lightning Message Channel in a managed package, review these considerations.

**•** [To pass the AppExchange Security Review, you must set the](https://developer.salesforce.com/docs/atlas.en-us.260.0.packagingGuide.meta/packagingGuide/security_review_guidelines.htm) `isExposed` field to `false` .

**•** If you set the `isExposed` field to `true`, you can’t change the value to `false` at a later time. This consideration applies
to Lightning Message Channels in managed packages and Lightning Message Channels that other components reference.

**•** Visualforce supports only Lightning Message Channels where `isExposed` is `true`, so managed packages with a Lightning
[Message Channel in Visualforce can’t pass the AppExchange Security Review. See Considerations and Limitations in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.pages.meta/pages/message_channel_considerations.htm)
_Visualforce Developer Guide_ .

File Suffix and Directory Location

### LightningMessageChannel components have the suffix .messageChannel and are stored in the messageChannels folder.

Version

### LightningMessageChannel components are available in API version 47.0 and later.


Metadata Types LightningMessageChannel

Fields

**Field Name** **Field Type** **Description**

`description` string The description of the Lightning Message Channel.

`isExposed` boolean

Indicates whether a Lightning Message Channel is exposed to
components in other namespaces ( `true` ) or not ( `false` ). The default
value is `false` .

`lightningMessageFields` LightningMessageField A list of message payload fields for a given Lightning Message Channel.
on page 1497[]

`masterLabel` string Required. The label for a Lightning Message Channel.

LightningMessageField

Represents a message payload field for a given Lightning Message Channel.

**Field Name** **Field Type** **Description**

`description` string The description for a Lightning Message Field.

`fieldName` string Required. Unique identifier of the Lightning Message Field.

Declarative Metadata Sample Definition

Here’s a simple example of a LightningMessageChannel component.

```
<?xml version="1.0" encoding="UTF-8"?>

<LightningMessageChannel xmlns="http://soap.sforce.com/2006/04/metadata">

   <masterLabel>SampleMessageChannel</masterLabel>

   <isExposed>true</isExposed>

   <description>This is a sample Lightning Message Channel.</description>

</LightningMessageChannel>

```

Here’s an example of a LightningMessageChannel component with LightningMessageFields.

```
<?xml version="1.0" encoding="UTF-8"?>

<LightningMessageChannel xmlns="http://soap.sforce.com/2006/04/metadata">

   <masterLabel>SampleMessageChannel</masterLabel>

   <isExposed>true</isExposed>

   <description>This is a sample Lightning Message Channel.</description>

   <lightningMessageFields>

     <fieldName>recordId</fieldName>

     <description>This is the record Id that changed</description>

   </lightningMessageFields>

   <lightningMessageFields>

     <fieldName>recordData</fieldName>

     <description>The current data representing the record that changed</description>

   </lightningMessageFields>

</LightningMessageChannel>

```


### Metadata Types LightningOnboardingConfig

Here’s an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>LightningMessageChannel</name>

      </types>

      <version>47.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

_Lightning Web Components Developer Guide_ [: Communicate Across the DOM with Lightning Message Service](https://developer.salesforce.com/docs/platform/lwc/guide/use-message-channel.html)

_[Second-Generation Managed Packaging Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.pkg2_dev.meta/pkg2_dev/packaging_packageable_components.htm)_ : Components Available in Managed Packages

### LightningOnboardingConfig

Represents the feedback provided when users switch from Lightning Experience to Salesforce Classic. Admins can customize the question,
how frequently the form appears, and where the feedback is stored in Chatter from the Adoption Assistance page in Lightning Experience
Setup. This type extends the Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### LightningOnboardingConfig components have the suffix .lightningOnboardingConfig and are stored in the LightningOnboardingConfigs folder.

Version

### LightningOnboardingConfig components are available in API version 49.0 and later.

Special Access Rules

[See Switch to Salesforce Classic Feedback Form in Salesforce Help for details.](https://help.salesforce.com/articleView?id=lex_encourage_work_feedback.htm&language=en_US)

Fields

**Field Name** **Field Type** **Description**

`collaborationGroup` string Required. The ID of the Chatter Group where the user feedback is posted.


### Metadata Types LightningTypeBundle

**Field Name** **Field Type** **Description**

`customQuestion` string Text of the custom question added by the admin. Maximum of 1,000
characters.

`feedbackFormDaysFrequency` int Required. The number of days between showing the feedback form
when a user switches between Lightning Experience and Salesforce

Classic. A value of `0` indicates that the form is shown for every switch.
Maximum of 30.

`isCustom` boolean Required. Indicates if a feedback form includes a custom question (
`true` ) or not ( `false` ).

`masterLabel` string Required. The label of the in-app guidance. Maximum of 80 characters.

`promptDelayTime` int Required. Indicates the amount of time, in seconds, to delay between
instances of all in-app content, both custom content created by org and

standard content created by Salesforce. Minimum of 0 hours and 0
minutes. Maximum of 99 hours and 59 minutes.

`sendFeedbackToSalesforce` boolean Required. Indicates if the user feedback can be shared with Salesforce
( `true` ) or not ( `false` ). Even if the feedback isn’t shared with Salesforce,

the feedback is shared in the Chatter Group chosen when customizing
the feedback form. The default is `false` .

Declarative Metadata Sample Definition

The following is an example of a LightningOnboardingConfig component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <LightningOnboardingConfig xmlns="http://soap.sforce.com/2006/04/metadata">

      <collaborationGroup>{Org ID}</collaborationGroup>

      <customQuestion>Please take a minute to tell us why you’re switching.</customQuestion>

      <feedbackFormDaysFrequency>0</feedbackFormDaysFrequency>

      <isCustom>true</isCustom>

      <masterLabel>Feedback Form</masterLabel>

      <promptDelayTime>3600</promptDelayTime>

      <sendFeedbackToSalesforce>true</sendFeedbackToSalesforce>

   </LightningOnboardingConfig>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### LightningTypeBundle

Represents a custom Lightning type. Use this type to override the default user interface to create a customized appearance based on
your business requirements. Deploy this bundle to your organization to implement the overrides.


Metadata Types LightningTypeBundle

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Structure and Directory Location

LightningTypeBundle components are stored in the `lightningTypes` folder.

Here’s an example of the `LightningTypeBundle` structure.

```
   +--myMetadataPackage

      +--lightningTypes (1)

        +--TYPE_NAME (2)

          +--schema.json (3)

          +--CHANNEL_NAME (4)

            +--editor.json (5) OR +--renderer.json (6)

```

The bundle includes these resources.

**•** The `lightningTypes` folder (1) contains a folder for each created custom Lightning type in the format `{typeName}` (2).

**•** Each custom lightning type folder contains a `schema.json` file (3) that defines the JSON schema that drives the custom Lightning
type validation.

**•** Optional channel-specific folders (4). To override the default UI for a specific Salesforce application, the bundle contains a folder
named after that channel. The supported channel folders are:

**–** `lightningDesktopGenAi` (Agentforce Employee agent in Lightning Experience)

**–** `enhancedWebChat` (Agentforce Service agent via Enhanced Chat v2)

**–** `experienceBuilder` (Experience Builder)

Inside the `{channelName}` folder, you can configure:

**–** The `editor.json` file (5) containing custom user interface and editor information

**–** The `renderer.json` file (6) containing custom user interface and renderer information

Note: This file isn’t supported in `experienceBuilder` .

Version

LightningTypeBundle components are available in API version 64.0 and later.

Fields

**Field Name** **Description**

```
description

```

**Field Type**
string


Metadata Types LightningTypeBundle

**Field Name** **Description**

**Description**
Describes the lightning type.

```
masterLabel

resources

```

**Field Type**
string

**Description**

Required. Represents the name of a LightningTypeBundle which is defined when the
LightningTypeBundle is created.

**Field Type**

LightningTypeBundleResource[]

**Description**
The list of resource files in the `lightningTypes` folder.

LightningTypeBundleResource

Represents a resource inside a LightningTypeBundle.

**Field Name** **Description**

```
fileName

filePath

source

```

**Field Type**
string

**Description**

Required. Name of the resource file.

**Field Type**
string

**Description**

Required. Path of the resource file.

**Field Type**
base64Binary

**Description**

Required. The JSON content of the resource.

Declarative Metadata Sample Definition

This `package.xml` file retrieves all the LightningTypeBundle components in an org.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

```


Metadata Types LightningTypeBundle

```
      <types>

        <members>*</members>

        <name>LightningTypeBundle</name>

      </types>

      <version>64.0</version>

   </Package>

```

In the retrieved `.zip` file, each custom Lightning type is nested under a `lightningTypes` folder.

This example shows the directory structure in the `.zip` file of a custom Lightning type named `flightResponse` :

```
   +--lightningTypes

      +--flightResponse

        +--schema.json

        +--lightningDesktopGenAi

           +--renderer.json

```

In this example, the custom Lightning type `flightResponse` is a complex type that references an Apex class named `Flight` .

```
   global class Flight {

      @AuraEnabled

      global String flightId;

      @AuraEnabled

      global Integer numLayovers;

      @AuraEnabled

      global Boolean isPetAllowed;

      @AuraEnabled

      global Long price;

      @AuraEnabled

      global Double discountPercentage;

      @AuraEnabled

      global Integer durationInMin;

      global Flight(String flightId, Integer numLayovers, Boolean isPetAllowed,

              Long price, Double discountPercentage, Integer durationInMin) {

        this.flightId = flightId;

        this.numLayovers = numLayovers;

        this.isPetAllowed = isPetAllowed;

        this.price = price;

        this.discountPercentage = discountPercentage;

        this.durationInMin = durationInMin;

      }

   }

   global class FlightRequestFilter {

      @AuraEnabled

      global Long price;

      @AuraEnabled

```


Metadata Types LightningTypeBundle

```
      global Double discountPercentage;

   }

```

Here are the contents of the files in the `flightResponse` directory. This sample code shows the contents of the `schema.json`
file.

```
   {

     "title": "My Flight Response",

     "description": "My Flight Response",

     "lightning:type": "@apexClassType/c__Flight"

   }

```

The `lightningDesktopGenAi` folder (optional) includes a `renderer.json` file that overrides the default UI of the custom
Lightning type `flightResponse` when you use the `Flight` Apex class as an output parameter for an agent action.

Contents of the `renderer.json` file.

```
   {

     "renderer": {

      "componentOverrides": {

       "$": {

        "definition": "c/flightDetails"

       }

      }

     }

   }

```

Note: flightDetails is a custom LWC component referenced in `renderer.json` file.

This example shows the directory structure in the `.zip` file of a custom Lightning type named `flightFilter` :

```
   +--lightningTypes

      +--flightFilter

        +--schema.json

        +--lightningDesktopGenAi

           +--editor.json

```

In this example, the custom Lightning type `flightFilter` is a complex type that references an Apex class named
`FlightRequestFilter` .

```
   global class Flight {

      @AuraEnabled

      global String flightId;

      @AuraEnabled

      global Integer numLayovers;

      @AuraEnabled

      global Boolean isPetAllowed;

      @AuraEnabled

      global Long price;

      @AuraEnabled

      global Double discountPercentage;

```


Metadata Types LightningTypeBundle

```
      @AuraEnabled

      global Integer durationInMin;

      global Flight(String flightId, Integer numLayovers, Boolean isPetAllowed,

              Long price, Double discountPercentage, Integer durationInMin) {

        this.flightId = flightId;

        this.numLayovers = numLayovers;

        this.isPetAllowed = isPetAllowed;

        this.price = price;

        this.discountPercentage = discountPercentage;

        this.durationInMin = durationInMin;

      }

   }

   global class FlightRequestFilter {

      @AuraEnabled

      global Long price;

      @AuraEnabled

      global Double discountPercentage;

   }

```

Here are the contents of the files in the `flightFilter` directory. This sample code shows the contents of the `schema.json` file.

```
   {

     "title": "Flight Filter",

     "description": "Flight Filter",

     "lightning:type": "@apexClassType/c__FlightRequestFilter"

   }

```

The `lightningDesktopGenAi` folder (optional) includes an `editor.json` file that overrides the default UI of the custom
Lightning type `flightFilter` when you use the `Flight` Apex class as an input parameter for an agent action.

Contents of the `editor.json` file.

```
   {

     "editor": {

      "componentOverrides": {

       "$": {

        "definition": "c/flightFilter"

       }

      }

     }

   }

```

Note: flightFilter is a custom LWC component referenced in `editor.json` file.


### Metadata Types LiveChatAgentConfig

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

[Custom Lightning Types Developer Guide](https://developer.salesforce.com/docs/einstein/genai/guide/lightning-types.html)

[Custom Lightning Type Examples](https://developer.salesforce.com/docs/einstein/genai/guide/lightning-types-examples.html)

### LiveChatAgentConfig

Represents the configuration of an organization’s Chat deployment, such as how many chats can be assigned to an agent and whether
chat sounds are enabled.

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### LiveChatAgentConfig configurations are referenced in the <developer_name>.liveChatAgentConfig file in the

`liveChatAgentConfigs` directory.

Version

### LiveChatAgentConfig is available in API version 28.0 and later.

Fields

**Field Name** **Field Type** **Description**

`assignments` AgentConfigAssignments

Specifies how agent configurations are assigned to Chat
users. Agent configurations can be assigned to sets of users
or sets of profiles.

`autoGreeting` string Specifies the greeting that displays when a customer begins
a chat with an agent.

`capacity` int Specifies the maximum number of chats in which an agent
can be engaged at a time.

`criticalWaitTime` int

Specifies the number of seconds an agent can wait to answer
an engaged chat before the chat tab flashes to alert the agent
to answer it.

`customAgentName` string Specifies the custom name for an agent, if one has been set.
Available in API version 29.0 and later.

`disableTransferConferenceGreeting` boolean

Indicates whether the greeting is disabled for agents during
chat transfer and chat conferencing ( `true` ) or not ( `false` ).
Available in API version 53.0 and later.


Metadata Types LiveChatAgentConfig

**Field Name** **Field Type** **Description**

`enableAgentFileTransfer` boolean Indicates whether file transfer is enabled for agents ( `true` )
or not ( `false` ). Available in API version 31.0 and later.

`enableAgentSneakPeek` boolean

`enableAssistanceFlag` boolean

Specifies whether a supervisor can see the content of an
agent’s message before they send it to a customer ( `true` )
or not ( `false` ).

Indicates whether agents can raise an assistance flag to notify
a supervisor that they need help. Available in API version
35.0 and later.

`enableAutoAwayOnDecline` boolean Indicates whether an agent appears as “away” ( `true` ) or
not ( `false` ) when an agent declines a chat with a customer.

`enableAutoAwayOnPushTimeout` boolean

`enableChatConferencing` boolean

`enableChatMonitoring` boolean

`enableChatTransferToAgent` boolean

`enableChatTransferToButton` boolean

`enableChatTransferToSkill` boolean

Indicates whether an agent appears as “away” ( `true` ) or
not ( `false` ) when a chat request that's been pushed to the
agent times out. Available in API version 34.0 and later.

Indicates whether chat conferencing is enabled for agents
( `true` ) or not ( `false` ). Available in API version 34.0 and
later.

Indicates whether chat monitoring is enabled for support
supervisors ( `true` ) or not ( `false` ). Available in API version
29.0 and later.

Indicates whether agents can transfer a chat to another agent
( `true` ) or not ( `false` ). Available in API version 36.0 and
later.

Indicates whether agents can transfer a chat to a button
( `true` ) or not ( `false` ). Available in API version 36.0 and
later.

Indicates whether agents can transfer a chat to a skill group
( `true` ) or not ( `false` ). Available in API version 36.0 and
later.

`enableLogoutSound` boolean Indicates whether a sound plays ( `true` ) or not ( `false` )
when an agent logs out of Chat.

`enableNotifications` boolean Indicates whether notifications of incoming chats appear for
agents ( `true` ) or not ( `false` ).

`enableRequestSound` boolean Indicates whether a sound plays ( `true` ) or not ( `false` )
when a customer requests to chat with an agent.

`enableSneakPeek` boolean

Indicates whether previews of customers’ messages are
displayed as customers type ( `true` ) or not ( `false` ) in the
agent’s Chat window. Available in API version 29.0 and later.


Metadata Types LiveChatAgentConfig

**Field Name** **Field Type** **Description**

`enableVisitorBlocking` boolean

`enableWhisperMessage` boolean

Indicates whether an agent can block a visitor by IP address
( `true` ) or not ( `false` ). Available in API version 34.0 and
later.

Indicates whether support supervisors can send whisper
messages to agents during a chat ( `true` ) or not ( `false` ).
Available in API version 29.0 and later.

`label` string Required. Specifies the name of the configuration for agents’
default chat settings.

```
supervisorDefaultAgentStatusFilter

```

SupervisorAgentStatusFilter Specifies the Chat status for filtering the Agent Status list in
(enumeration of type the Supervisor Panel. Valid values are:
string)

**•** `Online`

**•** `Away`

**•** `Offline`

Available in API version 29.0 and later.

`supervisorDefaultButtonFilter` string

Specifies the default button for filtering the Agent Status list
in the Supervisor Panel. Available in API version 29.0 and
later.

`supervisorDefaultSkillFilter` string Specifies the default skill for filtering the Agent Status list in
the Supervisor Panel. Available in API version 29.0 and later.

`supervisorSkills` SupervisorAgentConfigSkills

Specifies the list of agent skills that are assigned to a
supervisor, as specified in their assigned Chat configuration.
Available in API version 29.0 and later.

`transferableButtons` AgentConfigButtons Specifies the list of chat buttons that agents can transfer
chats to. Available in API version 31.0 and later.

`transferableSkills` AgentConfigSkills Specifies the list of skill groups that agents can transfer chats
to. Available in API version 31.0 and later.

AgentConfigAssignments

Represents the assignments of an organization’s profiles and users to a Chat configuration.

**Field Name** **Field Type** **Description**

`profiles` AgentConfigProfileAssignments Specifies the profiles that are associated with a specific
agent configuration.

`users` AgentConfigUserAssignments Specifies the users that are associated with a specific agent
configuration.


Metadata Types LiveChatAgentConfig

AgentConfigButtons

Represents the chat buttons that agents who are associated with the Chat configuration can transfer chats to.

**Field Name** **Field Type** **Description**

`button` string[] Specifies the chat buttons that agents can transfer chats
to.

AgentConfigProfileAssignments

Represents the profiles associated with a specific Chat configuration.

**Field Name** **Field Type** **Description**

`profile` string Specifies the custom name of the profile associated with a
specific agent configuration.

AgentConfigSkills

Represents the skill groups that agents who are associated with the Chat configuration can transfer chats to.

**Field Name** **Field Type** **Description**

`skill` string[] Specifies the skill groups that agents can transfer chats to.

AgentConfigUserAssignments

Represents the users associated with a specific Chat configuration.

**Field Name** **Field Type** **Description**

`user` string Specifies the username of the user associated with a specific
agent configuration.

SupervisorAgentConfigSkills

Represents the agent skills associated with a supervisor’s Chat configuration. Available in API version 29.0 and later.

**Field Name** **Field Type** **Description**

`skill` string Specifies the agent skills available for filtering the Agent
Status list in the Supervisor Panel.


### Metadata Types LiveChatButton

Declarative Metadata Sample Definition

This is a sample of a `liveChatAgentConfig` file.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <LiveChatAgentConfig xmlns="http://soap.sforce.com/2006/04/metadata">

      <label>My Agent Configuration 1</label>

      <autoGreeting>Hi, how can I help you?</autoGreeting>

      <capacity>5</capacity>

      <enableAutoAwayOnDecline>true</enableAutoAwayOnDecline>

      <enableLogoutSound>true</enableLogoutSound>

      <enableNotifications>true</enableNotifications>

      <enableRequestSound>true</enableRequestSound>

      <enableSneakPeek>true</enableSneakPeek>

      <enableWhisperMessage>true</enableWhisperMessage>

      <assignments>

        <profiles>

           <profile>standard</profile>

        </profiles>

        <users>

           <user>jdoe@acme.com</user>

        </users>

      </assignments>

   </LiveChatAgentConfig>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### LiveChatButton

Represents a Chat deployment’s settings for the button that customers click to chat with an agent and the chat window, such as the
label that appears on the button and the pre-chat form that appears before a chat begins. This type extends the Metadata metadata
type and inherits its `fullName` field.

Chats routed with Omni-Channel aren’t supported in the Metadata API.

File Suffix and Directory Location

### LiveChatButton on page 1509 configurations are stored in the <developer_name>.liveChatButton file in the

`liveChatButtons` directory.

Version

### LiveChatButton on page 1509 is available in API version 28.0 and later.


Metadata Types LiveChatButton

Fields

**Field Name** **Field Type** **Description**

`animation` LiveChatButtonPresentation (enumeration The type of animation for a chat invitation. Valid
of type string) values are:

**•** `Slide`

**•** `Fade`

**•** `Appear`

**•** `Custom`

`autoGreeting` string

The customized greeting message that the
customer receives when an agent accepts a chat
request from the chat button or invitation.

Available in API version 29.0 and later.

`chasitorIdleTimeout` int Specifies the amount of idle time before the chat
times out. The idle time starts being counted

after the agent sends the last chat message.
Available in API version 35.0 and later.

`chasitorIdleTimeoutWarning` int Specifies the amount of idle time before a
warning appears. The idle time starts being

counted after the agent sends the last chat
message. Available in API version 35.0 and later.

`chatPage` string Specifies the page that hosts your chat if that
page differs from the Chat window.

`customAgentName` string

The agent’s name as it appears to customers in
the chat window.

Available in API version 29.0 and later.

`deployments` LiveChatButtonDeployments Specifies the deployments associated with the
button.

`enableQueue` boolean Indicates whether queuing is enabled ( `true` )
or not ( `false` ).

`inviteEndPosition` LiveChatButtonInviteEndPosition The end position of the chat invitation. Valid
(enumeration of type string) values include:

**•** `TopLeft`

**•** `Top`

**•** `TopRight`

**•** `Left`

**•** `Center`

**•** `Right`

**•** `BottomLeft`


Metadata Types LiveChatButton

**Field Name** **Field Type** **Description**

**•** `Bottom`

**•** `BottomRight`

`inviteImage` string The custom button graphic that appears for the
invitation.

`inviteStartPosition` LiveChatButtonInviteStartPosition The start position of the chat invitation. Valid
(enumeration of type string) values include:

**•** `TopLeft`

**•** `TopLeftTop`

**•** `Top`

**•** `TopRightTop`

**•** `TopRight`

**•** `TopRightRight`

**•** `Right`

**•** `BottomRightRight`

**•** `BottomRight`

**•** `BottomRightBottom`

**•** `Bottom`

**•** `BottomLeftBottom`

**•** `BottomLeft`

**•** `BottomLeftLeft`

**•** `Left`

**•** `TopLeftLeft`

`isActive` boolean Specifies whether the chat button or invitation
is active.

`label` string Specifies the text that appears on the button.

`numberOfReroutingAttempts` int Specifies the number of times a chat request can
be rerouted to available agents if all agents reject

the chat request. Available in API version 30.0
and later.

`offlineImage` string Specifies the image that appears on the button
when no agents are available to chat.

`onlineImage` string Specifies the image that appears on the button
when agents are available to chat.

`optionsCustomRoutingIsEnabled` boolean

Indicates whether custom routing is enabled for
incoming chat requests ( `true` ) or not ( `false` ).
Available in API version 30.0 and later.


Metadata Types LiveChatButton

**Field Name** **Field Type** **Description**

`optionsHasChasitorIdleTimeout` boolean Indicates whether the visitor idle timeout feature
is enabled. Available in API version 35.0 and later.

`optionsHasInviteAfterAccept` boolean

`optionsHasInviteAfterReject` boolean

Indicates whether a new chat invitation triggers
after a customer accepts a previous chat
invitation ( `true` ) or not ( `false` ).

Indicates whether a new chat invitation triggers
after a customer rejects a previous chat invitation
( `true` ) or not ( `false` ).

`optionsHasRerouteDeclinedRequest` boolean Indicates whether a chat request, which has been
rejected by all available agents, is rerouted to

available agents again ( `true` ) or not ( `false` ).
Available in API version 30.0 and later.

`optionsIsAutoAccept` boolean Indicates whether a chat request is automatically
accepted by the agent it’s assigned to ( `true` )

or not ( `false` ). For chat buttons and automated
chat invitations with `routingType` set to
`MostAvailable` or `LeastActive` .
Available in API version 30.0 and later.

`optionsIsInviteAutoRemove` boolean Indicates whether a chat invitation is set to
automatically disappear from a customer’s screen

after a certain amount of time ( `true` ) or not
( `false` ).

`overallQueueLength` int Specifies the maximum number of chat requests
that are allowed to queue.

`perAgentQueueLength` int

Specifies the number of chat requests that are
allowed to queue for an agent with the required
skills.

`postChatPage` string Specifies the name of the post-chat form to
which customers are routed when the chat ends.

`postChatUrl` string Specifies the URL of the post-chat form to which
customers are routed when the chat ends.

`preChatFormPage` string Specifies the name of the pre-chat form to which
customers are routed before a chat begins.

`preChatFormUrl` string Specifies the URL of the pre-chat form to which
customers are routed when the chat begins.

`pushTimeOut` int

Specifies the number of seconds an agent has
to answer an incoming chat request before the
request is routed to another agent.


Metadata Types LiveChatButton

**Field Name** **Field Type** **Description**

`routingType` LiveChatButtonRoutingType (enumeration
of type string)

`site` string

Specifies how incoming chats are routed to
agents when a customer pushes a button. Valid
values are:

**•** `Choice`

**•** `LeastActive`

**•** `MostAvailable`

Specifies the Salesforce site that hosts your
custom chat button images or custom chat page.

You must have the CustomDomain permission
enabled in your organization before you can use
a Salesforce site with Chat.

`skills` LiveChatButtonSkills Specifies the skills associated with the button.
When a customer clicks the button to chat,

they’re automatically routed to agents with those
skills.

`timeToRemoveInvite` int Specifies how long the invitation is displayed (in
seconds) to customers before it disappears.

`type` LiveChatButtonType (enumeration of type Required. The chat button type. Valid values are:
string)

**•** `Standard`

**•** `Invite`

`windowLanguage` Language Specifies the language preferences for the chat
window associated with the button.

LiveChatButtonSkills

Represents the skills associated with a chat button or invitation.

Fields

**Field Name** **Field Type** **Description**

`skill` string Specifies the name of the skill.

LiveChatButtonDeployments

Represents the deployments associated with a chat button or invitation.


### Metadata Types LiveChatDeployment

Fields

**Field Name** **Field Type** **Description**

`deployment` string Specifies the name of the deployment.

Declarative Metadata Sample Definition

Here’s a sample of a `liveChatButton` file.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <LiveChatButton xmlns="http://soap.sforce.com/2006/04/metadata">

      <deployments/>

      <enableQueue>false</enableQueue>

      <isActive>true</isActive>

      <label>CustomerSupportButton</label>

      <optionsCustomRoutingIsEnabled>false</optionsCustomRoutingIsEnabled>

      <optionsHasChasitorIdleTimeout>false</optionsHasChasitorIdleTimeout>

      <optionsHasInviteAfterAccept>false</optionsHasInviteAfterAccept>

      <optionsHasInviteAfterReject>false</optionsHasInviteAfterReject>

      <optionsHasRerouteDeclinedRequest>false</optionsHasRerouteDeclinedRequest>

      <optionsIsAutoAccept>false</optionsIsAutoAccept>

      <optionsIsInviteAutoRemove>false</optionsIsInviteAutoRemove>

      <postChatUrl>https://help.salesforce.com</postChatUrl>

      <routingType>Choice</routingType>

      <skills>

        <skill>Chat</skill>

      </skills>

      <type>Standard</type>

   </LiveChatButton>

```

Note: If you update your chat button through the Metadata API, be sure to update all Web pages that use the same chat button
code.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### LiveChatDeployment

Represents the configuration settings for a specific Chat deployment, such as the branding image for the deployment and whether or
not chat transcripts are automatically saved.

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### LiveChatDeployment values are stored in the <developer_name>.liveChatDeployment file in the

`liveChatDeployments` directory.


Metadata Types LiveChatDeployment

Version

LiveChatDeployment is available in API version 28.0 and later.

Fields

**Field Name** **Field Type** **Description**

`brandingImage` string Specifies the branding image for the
deployment.

`connectionTimeoutDuration` int Indicates the amount of time before the chat
times out, in seconds.

`ConnectionWarningDuration` int Indicates the amount of time before a time-out
warning is displayed to the agent, in seconds.

`displayQueuePosition` boolean (Pilot) Determines whether a customer’s queue
position is displayed in a standard chat window

while the customer waits for an agent to
respond to the chat request ( `true` ) or not
( `false` ). This field is available as a pilot in API
version 32.0. To enable this field, contact
Salesforce.

`domainWhiteList` LiveChatDeploymentDomainWhiteList Specifies the list of domains that can host the
deployment.

`enablePrechatApi` boolean

`enableTranscriptSave` boolean

Indicates whether or not the pre-chat API is
enabled for the deployment ( `true` ) or not
( `false` ).

Indicates whether chat transcripts are
automatically saved after a chat ends ( `true` )
or not ( `false` ).

`label` string Specifies the name of the deployment.

`mobileBrandingImage` string

Specifies the branding image for the
deployment that appears when customers
access the deployment on a mobile device.

`site` string Specifies the site that hosts the images for the
deployment.

Note: You must have the
CustomDomain permission enabled in
your organization before you can use a
Salesforce site with Chat.

`windowTitle` string Specifies the title of the window associated
with the deployment.


### Metadata Types LiveChatSensitiveDataRule

LiveChatDeploymentDomainWhiteList

Represents a Chat deployment’s domain whitelist.

Fields

**Field Name** **Field Type** **Description**

`domain` string Specifies a domain that can host the deployment.

Declarative Metadata Sample Definition

This is a sample of a `liveChatDeployment` file.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <LiveChatDeployment xmlns="http://soap.sforce.com/2006/04/metadata">

      <label>My Deployment 1</label>

      <brandingImage>pkb_image_bannerBg</brandingImage>

      <mobileBrandingImage>pkb_image_bgBottom</mobileBrandingImage>

      <domainWhiteList>

        <domain>mydomain</domain>

        <domain>test</domain>

      </domainWhiteList>

      <enableTranscriptSave>true</enableTranscriptSave>

      <site>GL_Knowledge_Base</site>

      <windowTitle>My window title</windowTitle>

   </LiveChatDeployment>

```

Note: If you update your deployment through the Metadata API, be sure to update all Web pages that use the same deployment
code.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### LiveChatSensitiveDataRule

Represents a rule for masking or deleting data of a specified pattern. Written as a regular expression (regex).

Use this object to mask or delete data of specified patterns, such as credit card, social security, phone and account numbers, or even
profanity. This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### LiveChatSensitiveDataRule components have the suffix .liveChatSensitiveDataRule and are stored in the

`liveChatSensitiveDataRule` folder.


Metadata Types LiveChatSensitiveDataRule

Version

LiveChatSensitiveDataRule components are available in API version 35.0 and later.

Fields

**Field Name** **Field Type** **Description**

```
actionType

```

SensitiveDataActionType Required. The action to take on the text when the sensitive data rule is
(enumeration of triggered. Possbile values are:
type string)

**•** `Remove`

**•** `Replace`

`description` string The description of the sensitive data rule—for example, “Block social
security numbers.”

`enforceOn` int

Required. Determines the roles on which the rule is enforced. The value
is determined using bitwise OR operation. There are seven possible
values:

**1.** Rule enforced on Agent

**2.** Rule enforced on Visitor

**3.** Rule enforced on Agent and Visitor

**4.** Rule enforced on Supervisor

**5.** Rule enforced on Agent and Supervisor

**6.** Rule enforced on Visitor and Supervisor

**7.** Rule enforced on Agent, Visitor, and Supervisor

`isEnabled` boolean Required. Specifies whether a sensitive data rule is active ( `true` ) or not
( `false` ). Default value (if none is provided) is `false` .

`pattern` string Required. The pattern of text blocked by the rule. Written as a JavaScript
regular expression (regex).

`replacement` string The string of characters that replaces the blocked text (if `ActionType`
_`Replace`_ is selected).

Declarative Metadata Sample Definition

The following is an example of a LiveChatSensitiveDataRule component.

```
<LiveChatSensitiveDataRule xmlns="http://soap.sforce.com/2006/04/metadata">

   <actionType>REPLACE</actionType>

   <enforceOn>7</enforceOn>

   <isEnabled>true</isEnabled>

   <pattern>[aeiou]</pattern>

   <replacement>œ</replacement>

</LiveChatSensitiveDataRule>

```


### Metadata Types LoyaltyProgramSetup

The following is an example `package.xml` that references the previous definition.

```
   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <!-- To be used from

   support.liveagent.testsuite.unifiedouting.testDeployButtonMDAPIWithExistingQueue -->

      <apiAccessLevel>Unrestricted</apiAccessLevel>

      <types>

        <members>Change_For_all</members>

        <name>LiveChatSensitiveDataRule</name>

      </types>

      <version>35.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### LoyaltyProgramSetup

Represents the configuration of a loyalty program process including its parameters and rules. Program processes determine how new
transaction journals are processed. When new transaction journals meet the criteria and conditions for a program process, actions that
are set up in the process are triggered for the transaction journals.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### LoyaltyProgramSetup components have the suffix loyaltyProgramSetup and are stored in the loyaltyProgramSetups

folder.

Version

### LoyaltyProgramSetup components are available in API version 54.0 and later for Loyalty Management and in API version 59.0 and later

for Referral Marketing.

Special Access Rules

To use this metadata type, your org must have either B2C - Loyalty, B2C - Loyalty Plus, Loyalty Management - Growth, Loyalty Management

    - Advanced, or Referral Marketing license enabled.


Metadata Types LoyaltyProgramSetup

Fields

**Field Name** **Description**

```
label

programProcesses

```

LoyaltyProgramProcess

**Field Type**
string

**Description**
Name of the loyalty program that the program process is associated with. If a loyalty
program or referral program with the specified name doesn't exist, a new
LoyaltyProgram record is created. The name of a program must contain at least one
alphanumeric character.

**Field Type**

LoyaltyProgramProcess[] on page 1519

**Description**
Collection of loyalty program processes associated with a loyalty program or a referral
program.

Represents a collection of fields relating to a loyalty program process.

**Field Name** **Description**

```
description

executionType

journalSubType

```

**Field Type**
string

**Description**
The description of the loyalty program process.

**Field Type**
LoyaltyPgmProcExecutionType (enumeration of type string)

**Description**
The mode of processing transaction journals by the loyalty program process.

Possible values are:

**•** `Batch`

**•** `BatchAndRealTime`

**•** `RealTime`

**Field Type**
string

**Description**
The subtype of transaction journals processed by the loyalty program process.


Metadata Types LoyaltyProgramSetup

**Field Name** **Description**

```
journalType

loyaltyTierGroup

parameters

processName

processType

rules

```

**Field Type**
string

**Description**
The type of transaction journal processed by the loyalty program process.

Possible values for loyalty program:

**•** `Accrual`

**•** `Redemption`

Possible value for referral program:

**•** `Referral`

**Field Type**
string

**Description**
The tier group of a loyalty program. This field is available in API version 56.0 and later.
This field isn’t applicable for referral programs.

**Field Type**

LoyaltyProgramProcessParameter[] on page 1521

**Description**
The parameters associated with the loyalty program process.

**Field Type**
string

**Description**

Required.

The name of the loyalty program process.

**Field Type**
string

**Description**

Required.

The type of records processed by the loyalty program process. For referral programs,
the process type is `TransactionJournal` .

**Field Type**

LoyaltyProgramProcessRule[] on page 1525

**Description**
The rules associated with the loyalty program process.


Metadata Types LoyaltyProgramSetup

**Field Name** **Description**

```
status

```

**Field Type**
LoyaltyPgmProcStatus (enumeration of type string)

**Description**
The status of the loyalty program process.

Possible values are:

**•** `Active`

**•** `Draft`

**•** `Inactive`

Note: Only active program processes can process transaction journals.

LoyaltyProgramProcessParameter

Represents a collection of fields relating to a parameter that's associated with the program process. Parameters are dynamic or fixed
values that are used in rule. You can define the value of a parameter based on its type and data type.

**Field Name** **Description**

```
condition

dataType

decimalPlaces

```

**Field Type**

LoyaltyProgramProcessCondition on page 1523

**Description**
The filter condition that decides which records are stored in the parameter.

**Field Type**
LoyaltyPgmProcParmDataType (enumeration of type string)

**Description**
The data type of the parameter. Determines the type of value that can be stored in
the parameter.

Possible values are:

**•** `Boolean`

**•** `Date`

**•** `DateTime`

**•** `Numeric`

**•** `Sobject`

**•** `Text`

**Field Type**
int

**Description**
The number of decimal places supported by the parameter when it is of the type
Variable and data type Numeric.


Metadata Types LoyaltyProgramSetup

**Field Name** **Description**

```
description

isCollection

isInput

isOutput

objectName

parameterName

parameterType

```

**Field Type**
string

**Description**
The description of the parameter.

**Field Type**
boolean

**Description**
Indicates whether the parameter can store multiple values when it is of the type
Variable.

**Field Type**
boolean

**Description**
Indicates whether a parameter can be used as an input outside the loyalty program
process.

**Field Type**
boolean

**Description**
Indicates whether a parameter can be used as an output outside the loyalty program
process.

**Field Type**
string

**Description**
Name of the object whose records are stored by the parameter when it is of the type
Variable and data type sObject.

**Field Type**
string

**Description**

Required.

The name of the parameter.

**Field Type**
LoyaltyPgmProcParmType (enumeration of type string)

**Description**
The type of value the parameter can store.

Possible values are:

**•** `Constant`


Metadata Types LoyaltyProgramSetup

**Field Name** **Description**

**•** `Formula`

**•** `Variable`

```
value

```

**Field Type**
string

**Description**
The value of the parameter when it is of the type Variable or Formula and isn't of the
data type sObject.

LoyaltyProgramProcessCondition

Represents a collection of fields relating to a condition. Conditions filter records that parameters store or check whether child actions
must be triggered for a transaction journal.

**Field Name** **Description**

```
conditionCriteria

conditionFilterCriteria

conditionName

```

**Field Type**
string

**Description**

Required.

The criteria that determine when the condition is met by a record or by a transaction
journal.

**Field Type**

LoyaltyProgramProcessConditionFilterCriteria[] on page 1523

**Description**
The filter criteria that determines which records or transaction journals are filtered.

**Field Type**
string

**Description**

Required.

The name of the condition.

LoyaltyProgramProcessConditionFilterCriteria

Represents a collection of fields relating to a filter criteria that's part of a condition. Multiple filter criteria can be added for a condition.
Filter criteria determine which records are filtered by related condition.


Metadata Types LoyaltyProgramSetup

**Field Name** **Description**

```
operator

sequence

sourceFieldName

value

valueType

```

**Field Type**
LoyaltyPgmProcCondOperator (enumeration of type string)

**Description**

Required.

The operator of the filter criteria.

Possible values are:

**•** `Contains`

**•** `DoesNotContain`

**•** `EndsWith`

**•** `Equals`

**•** `GreaterThan`

**•** `GreaterThanOrEquals`

**•** `IsNotNull`

**•** `IsNull`

**•** `LessThan`

**•** `LessThanOrEquals`

**•** `NotEquals`

**•** `StartsWith`

**Field Type**
int

**Description**

Required.

The sequence number of the filter criteria within a condition.

**Field Type**
string

**Description**

Required.

The name of the field used in the filter criteria.

**Field Type**
string

**Description**
The value of the filter criteria.

**Field Type**
LoyaltyPgmProcCondType (enumeration of type string)


Metadata Types LoyaltyProgramSetup

**Field Name** **Description**

**Description**

Required.

The type of value specified in the filter criteria.

Possible values are:

**•** `Formula`

**•** `Literal`

**•** `Lookup`

**•** `Parameter`

LoyaltyProgramProcessRule

Represents a collection of fields relating to a rule. A rule consists of a set of conditions and actions.

**Field Name** **Description**

```
actions

conditions

description

endDate

previousRule

```

**Field Type**

LoyaltyProgramProcessAction[] on page 1526

**Description**
The actions associated with the rule.

**Field Type**

LoyaltyProgramProcessCondition[] on page 1523

**Description**
The conditions associated with the rule.

**Field Type**
string

**Description**
The description of the rule.

**Field Type**
date

**Description**
The date until which the rule processes transaction journals.

**Field Type**
string

**Description**
The rule that processes new transaction journals before the current rule. The current
rule is triggered when the previous rule completes processing transaction journals.


Metadata Types LoyaltyProgramSetup

**Field Name** **Description**

```
promotion

ruleName

startDate

status

stepMappings

```

**Field Type**
string

**Description**
The promotion associated with the rule. When a promotion is associated with a rule,
the start date, end date, and status of the promotion determines the corresponding
fields of the rule.

**Field Type**
string

**Description**

Required.

The name of the rule.

**Field Type**
date

**Description**
The date from which the rule starts processing transaction journals.

**Field Type**
LoyaltyPgmProcRuleStatus (enumeration of type string)

**Description**
The status of the rule.

Possible values are:

**•** `Active`

**•** `Draft`

**•** `Inactive`

**Field Type**

LoyaltyProgramProcessRuleStepMapping[] on page 1531

**Description**
The list of step mappings associated with rule.

LoyaltyProgramProcessAction

Represents a collection of fields relating to an action.

**Field Name** **Description**

```
actionName

```

**Field Type**
string


Metadata Types LoyaltyProgramSetup

**Field Name** **Description**

**Description**
Required.

The name of the action.

```
actionParameters

actionType

```

**Field Type**

LoyaltyProgramProcessActionParameter[] on page 1530

**Description**
The parameters of the action.

**Field Type**
LoyaltyPgmProcActionType (enumeration of type string)

**Description**
Required.

The type of action.

Possible values are:

**•** These values are used in Loyalty Management:

**–** `AssignParameterValues` —Assigns values to parameters.

**–** `AssignBadgeToMember` —Assigns a badge to a loyalty program member.
This value is available in API version 56.0 and later.

**–** `Crud` —Creates or updates records in the target object. This value is available
in API version 56.0 and later.

**–** `CheckMemberBadgeAssignment` —Checks whether a badge is assigned
to a loyalty program member. This value is available in API version 56.0 and
later.

**–** `ChangeMemberTier` —Changes the tier of a loyalty program member.
This value is available in API version 56.0 and later.

**–** `CreditPoints` —Credits points to the loyalty program member associated
with the transaction journal that's processed by the rule.

**–** `DebitPoints` —Debits points from the points balance of the loyalty
program member associated with the transaction journal that's processed by
the rule.

**–** `GetMemberAttributesValues` —Gets the details of a loyalty program
member’s attribute value for the selected engagement attribute. This value is
available in API version 55.0 and later.

**–** `GetMemberPointBalance` —Gets the points balance of a loyalty program
member.

**–** `GetMemberPromotions` —Get promotions of a loyalty program member.
This value is available in API version 56.0 and later.

**–** `GetMemberTier` —Gets the tier details of a loyalty program member.

**–** `GetOutputsFromDecisionTable` —Gets outputs provided by a
decision table. This value is available in API version 56.0 and later.


Metadata Types LoyaltyProgramSetup

**Field Name** **Description**

**–** `IncreaseUsageForCumulativePromotion` —Increases a loyalty
program member’s usage for a cumulative promotion.

**–** `IssueVoucher` —Issues a voucher to the loyalty program member
associated with the transaction journal that's processed by the rule.

**–** `RedeemVoucher` —Redeems a voucher for the loyalty program member
associated with the transaction journal that's processed by the rule. This value
is available in API version 58.0 and later.

**–** —Updates the loyalty program member's usage towards achieving a
cumulative promotion by a specified value.

**–** `RunFlow` —Runs a flow.

**–** `RunProgramProcess` —Runs an active loyalty program process as a
subprocess. This value is available in API version 56.0 and later.

**–** `SendMail` —Sends emails to the loyalty program member for whom the
process is run. This value is available in API version 59.0 and later.

**–** `UpdateCurrentValueForMemberAttribute` —Updates the loyalty
program member's current attribute value for the selected engagement
attribute. This value is available in API version 55.0 and later.

**–** `UpdatePointBalance` —Updates the points balance of the loyalty
program member associated with the transaction journal that's processed by
the rule.

**–** `UpdateUsageForCumulativePromotion` —Updates a loyalty
program member’s usage for a cumulative promotion.

**•** These values are used in Referral Marketing:

**–** `AssignParameterValues` —Assigns values to parameters.

**–** `Crud` —Creates or updates records in the target object.

**–** `GetMemberAttributesValues` —Gets the details of an advocate's
attribute value for the selected engagement attribute.

**–** `GetMemberPromotions` —Gets the promotions of an advocate.

**–** `GetOutputsFromDecisionTable` —Gets outputs provided by a
decision table.

**–** `IssueExtendedReward` —Issues an extended reward to an advocate or
a referred friend. This value is available in API version 64.0 and later.

**–** `IssueVoucher` —Issues a voucher to an advocate or a referred friend.

**–** `RedeemVoucher` —Redeems a voucher for an advocate or a friend.

**–** `SendMail` —Sends emails to a referral program’s advocates and referrals.

**–** `UpdateCurrentValueForMemberAttribute` —Updates an
advocate’s current attribute value for the selected engagement attribute.

**•** These values are reserved for internal use:

**–** `GetCustomerPromotionAttrValue` —This value is available in API
version 64.0 and later.


Metadata Types LoyaltyProgramSetup

**Field Name** **Description**

**–** `UpdateCustomerPromotionAttrValue` —This value is available in
API version 64.0 and later.

```
crudActionType

decisionTable

decisionTableDatasetLink

entityApiName

flowDefinition

loyaltyProgramProcess

```

**Field Type**
LoyaltyPgmProcCrudActType (enumeration of type string)

**Description**
The type of operation to perform on target object records by the action. This field is
available from API version 56.0 and later.

Note: This field is required when the `actionType` field value is `CRUD` .

Possible values are:

**•** `create`

**•** `update`

**Field Type**
string

**Description**
The decision that's invoked by the action for the transaction journal that's processed
by the rule.

**Field Type**
string

**Description**
The dataset link associated with the selected decision table.

**Field Type**
string

**Description**
The API name of the target object. This field is available from API version 56.0 and later.

Note: This field is required when the `actionType` field value is `CRUD` .

**Field Type**
string

**Description**
The flow that's run by the action for the transaction journal that's processed by the
rule. The selected flow must be of the type LoyaltyManagementFlow.

**Field Type**
string


Metadata Types LoyaltyProgramSetup

**Field Name** **Description**

**Description**
The subprogram processes that’s run by the action. This field is available from API
version 56.0 and later.

Note: This field is required when the `actionType` field value is
`RunProgramProcess` .

LoyaltyProgramProcessActionParameter

Represents a collection of fields relating to an action parameter. A parameter is either an input or an output for the action. Input parameters
store the values used by the action. Output parameters store the result of the action.

**Field Name** **Description**

```
operator

parameterName

sequenceNumber

value

```

**Field Type**
LoyaltyPgmProcActParamOper (enumeration of type string)

**Description**
The type of operator used in the action. This field is available in API version 56.0 and
later.

Possible value is:

**•** `Equals`

**Field Type**
string

**Description**

Required.

The name of parameter. The parameter name must be the same as the input or the
output field that's supported depending on the associated action's type.

**Field Type**
int

**Description**
The sequence number of the parameter in the action. This field is available in API
version 56.0 and later.

**Field Type**
string

**Description**
Required.

The value of the parameter.


Metadata Types LoyaltyProgramSetup

**Field Name** **Description**

```
valueType

```

**Field Type**
LoyaltyPgmProcActParamType (enumeration of type string)

**Description**
The type of value to provide in the parameter. This field is available in API version 56.0
and later.

Possible values are:

**•** `Literal` —A constant value.

**•** `Parameter` —A runtime value passed using a parameter.

LoyaltyProgramProcessRuleStepMapping

Represents a collection of fields relating to a step mapping. Map conditions with child actions or map an action without a parent step.

**Field Name** **Description**

```
associatedStep

parentStep

sequence

```

**Field Type**
string

**Description**

Required.

The action that's associated with the mapping.

**Field Type**
string

**Description**
The condition that contains one or more child actions.

**Field Type**
int

**Description**

Required.

The sequence number of the mapping within a rule.

Declarative Metadata Sample Definition

The following is an example of a LoyaltyProgramSetup component.

```
<?xml version="1.0" encoding="UTF-8"?>

<LoyaltyProgramSetup xmlns="http://soap.sforce.com/2006/04/metadata">

   <label>Cloud Kicks Inner Circle</label>

   <programProcesses>

     <executionType>RealTime</executionType>

```


Metadata Types LoyaltyProgramSetup

```
        <parameters>

           <dataType>Numeric</dataType>

           <decimalPlaces>0</decimalPlaces>

           <isCollection>false</isCollection>

           <isInput>false</isInput>

           <isOutput>false</isOutput>

           <parameterName>VoucherValue</parameterName>

           <parameterType>Constant</parameterType>

           <value>50</value>

        </parameters>

        <processName>Issue Vouchers</processName>

        <processType>Transaction Journal</processType>

        <rules>

           <actions>

             <actionName>Issue High Transaction Value Voucher</actionName>

             <actionParameters>

               <operator>Equals</operator>

               <parameterName>VoucherDefinitionName</parameterName>

               <sequenceNumber>1</sequenceNumber>

               <value>Voucher for High Value Transactions</value>

               <valueType>Literal</valueType>

             </actionParameters>

             <actionParameters>

               <operator>Equals</operator>

               <parameterName>VoucherCode</parameterName>

               <sequenceNumber>2</sequenceNumber>

               <value>{!TransactionJournal.Order.Id}</value>

             </actionParameters>

             <actionParameters>

               <operator>Equals</operator>

               <parameterName>VoucherEffectiveDate</parameterName>

               <sequenceNumber>3</sequenceNumber>

               <value>DATEVALUE(&quot;2021-11-21 00:00:00&quot;)</value>

             </actionParameters>

             <actionParameters>

               <operator>Equals</operator>

               <parameterName>VoucherExpirationDate</parameterName>

               <sequenceNumber>4</sequenceNumber>

               <value>DATEVALUE(&quot;2022-01-01 00:00:00&quot;)</value>

             </actionParameters>

             <actionParameters>

               <operator>Equals</operator>

               <parameterName>VoucherFaceValue</parameterName>

               <sequenceNumber>5</sequenceNumber>

               <value>{!VoucherValue}</value>

             </actionParameters>

             <actionType>IssueVoucher</actionType>

           </actions>

           <conditions>

             <conditionCriteria>1</conditionCriteria>

             <conditionFilterCriteria>

               <operator>GreaterThanOrEquals</operator>

               <sequence>1</sequence>

              <sourceFieldName>TransactionJournal.TransactionAmount</sourceFieldName>

```


Metadata Types LoyaltyProgramSetup

```
               <value>100</value>

               <valueType>Literal</valueType>

             </conditionFilterCriteria>

             <conditionName>New Condition</conditionName>

             <conditionType>Condition</conditionType>

           </conditions>

           <endDate>2022-01-01</endDate>

           <ruleName>Issue Voucher for Transactions Above $100</ruleName>

           <startDate>2021-11-21</startDate>

           <status>Draft</status>

           <stepMappings>

             <associatedStep>New Condition</associatedStep>

             <sequence>1</sequence>

           </stepMappings>

           <stepMappings>

             <associatedStep>Issue High Transaction Value Voucher</associatedStep>

             <parentStep>New Condition</parentStep>

             <sequence>1</sequence>

           </stepMappings>

        </rules>

        <status>Draft</status>

      </programProcesses>

   </LoyaltyProgramSetup>

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

       <name>LoyaltyProgramSetup</name>

     </types>

     <version>54.0</version>

   </Package>

```

Note: To retrieve metadata specific to any loyalty program, mention the loyalty program name in the <members> tag. The
generated file contains all the information regarding that loyalty program.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types ManagedContentType ManagedContentType

Represents the definition of custom content types for use with Salesforce CMS. Custom content types are displayed as forms with defined
fields.

This type extends the Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### ManagedContentType components have the suffix managedContentType and are stored in the managedContentTypes

folder.

Version

### ManagedContentType components are available in API version 47.0 and later.

Special Access Rules

### ManagedContentType is only available if Salesforce CMS and digital experiences are enabled for your org.

Fields

**Field Name** **Field Type** **Description**

`description` string Describes the custom content type defined in this ManagedContentType
declaration.

`developerName` string Required. Unique name for the custom content type. For example:

```
                           OurSpecialContent_c

```

`isMetadataContent` boolean

`managedContentNodeTypes` ManagedContentNodeType[]

When `true`, any content created from this content type is converted
to metadata. Default value is `false` . Availabe in API version 63.0 and
later.

Nodes included as part of this custom content type. When rendered as
a form in the Digital Experiences app, each node is represented as an
individual field.

`masterLabel` string Required. Declares the name of the content type as it appears in the UI.

ManagedContentNodeType

Represents the structure of individual nodes within the custom content type.


Metadata Types ManagedContentType

**Field Name** **Field Type** **Description**

`helpText` string

Provides assistive text in the UI, displayed as an info bubble for the field. If this
field is empty, no info bubble icon or text is displayed.

For example: <IMG?>

`isLocalizable` boolean Declares a field as localizable and consumable by <loc MDAPI reference>
( `true` ) or not ( `false` ). Default is `false` .

Note: NodeTypes `IMG`, `URL`, `DATE`, and `DATETIME` can’t be
localized.

`isRequired` boolean Declares a field as required ( `true` ) or not ( `false` ). Fields declared as required
are indicated by a red asterisk. If a value isn’t added to the field in the custom

content type, the form can’t be saved and a standard error is displayed. Default
is `false` .

Note: When `nodeType on page 1535` is set to `NAMEFIELD` on
a field, `isRequired` must also be set to `True` for that field.

`nodeLabel` string

Required. Declares the label for the field as it appears in the UI.

In enhanced workspaces, the system generates a Title field by default. To
prevent having multiple Title fields on the UI when you create a custom content

type for use in an enhanced workspace, don't use Title as the label for
`nodeLabel` .

`nodeName` string Required. Unique name of the `nodeType` within the content type.
`nodeName` is a simple text field that allows up to 100 alphanumeric characters

and underscores. The name must begin with a letter, not include spaces, can’t
have two consecutive underscores, and can’t end with an underscore.

In enhanced workspaces, the system generates a Title field by default. To
prevent having multiple Title fields on the UI when you create a custom content
type for use in an enhanced workspace, don't use Title as the label for
`nodeName` .

Required. Identifies the supported type of content in the node. Passed as a
string. There’s a maximum of 15 node types per content type. Values are case
insensitive but are returned in all capital letters as shown. Valid values are:

**•** `TEXT`

Simple text node (max length=255 characters)

**•** `MTEXT`

Multi-line text node (max length=2000 characters)

**•** `RTE`

Rich text node (max length=65536 characters)

**•** `IMG`

Image node


```
nodeType

```

MCNodeType
(enumeration of type
string)

Metadata Types ManagedContentType

**Field Name** **Field Type** **Description**

Note: `IMG` node types can’t be localized. Set `isLocalizable`
to false for images.

**•** `URL`

URL node (max length=255 characters)

Note: `URL` accepts protocol string values starting with http://,
https://, mailto:, tel:, and /.

Note: `URL` node types can’t be localized. Set `isLocalizable`
to false for URLs.

**•** `DATE`

Date node

Note: `DATE` accepts dates only in the format yyyy-MM-dd.

Note: `DATE` node types can’t be localized. Set
`isLocalizable` to false for dates.

**•** `DATETIME`

Datetime node

Note: `DATETIME` accepts date and time in the format:
yyyy-MM-dd'T'HH:mm:ss.SSS'Z' (UTC datetime in ISO 8601 format).

Note: `DATETIME` node types can’t be localized. Set
`isLocalizable` to false for datetime notes.

**•** `NAMEFIELD`

Note: `NAMEFIELD` declares the field as the name that represents
the content when referenced in the UI. For example, text entered
in this field displays as a list of available content in the Digital
Experiences app or as a piece of content available for inclusion in a
collection in an Experience Cloud site.

One, and only one, `nodeType` in your managed content type
must be declared as `NAMEFIELD` . `NAMEFIELD` is a string of 200
characters or fewer.

In enhanced workspaces, the system generates a Title field by
default. To prevent having multiple Title fields on the UI when you
create a custom content type for use in an enhanced workspace,
don't use Title as the label for `nodeName` or `nodeLabel` for
the `NAMEFIELD` node. If you've already named `nodeName` Title,
choose a different label for `nodeLabel` to prevent confusion on
the content creation page.

When `NAMEFIELD` is used, `isRequired` must also be set to
`true` for the field.


Metadata Types ManagedContentType

**Field Name** **Field Type** **Description**

`placeholderText` string

Provides assistive text in the UI, displayed as placeholder, or ghost text, in a
field before any entry is made. For example, `Enter a title for your`

```
article...

```

Declarative Metadata Sample Definition

The following is an example of a ManagedContentType component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ManagedContentType xmlns="http://soap.sforce.com/2006/04/metadata">

  <developerName>myContentType</developerName>

 <masterLabel>My Content Type</masterLabel>

 <description>This is the description for my content type</description>

 <managedContentNodeTypes>

  <nodeName>title</nodeName>

  <nodeLabel>Content Title</nodeLabel>

  <nodeType>NAMEFIELD</nodeType>

  <placeholderText>Placeholder Text for title</placeholderText>

  <helpText>Help Text for title</helpText>

  <isLocalizable>true</isLocalizable>

  <isRequired>true</isRequired>

 </managedContentNodeTypes>

 <managedContentNodeTypes>

  <nodeName>textnode</nodeName>

  <nodeLabel>Content Text</nodeLabel>

  <nodeType>TEXT</nodeType>

  <placeholderText>Placeholder Text for Content Text</placeholderText>

  <helpText>Help Text for Content Text</helpText>

  <isLocalizable>true</isLocalizable>

  <isRequired>false</isRequired>

 </managedContentNodeTypes>

 <managedContentNodeTypes>

  <nodeName>richtextnode</nodeName>

  <nodeLabel>Content RichText</nodeLabel>

  <nodeType>RTE</nodeType>

 </managedContentNodeTypes>

 <managedContentNodeTypes>

  <nodeName>multilinetextnode</nodeName>

  <nodeLabel>Content MultilineText</nodeLabel>

  <nodeType>MTEXT</nodeType>

 </managedContentNodeTypes>

 <managedContentNodeTypes>

  <nodeName>imagenode</nodeName>

  <nodeLabel>Content Image</nodeLabel>

  <nodeType>IMG</nodeType>

 </managedContentNodeTypes>

</ManagedContentType>

```


### Metadata Types ManagedEventSubscription (Beta)

Usage

For each custom content type you create, there must also be a CMS Content page created in any Experience Cloud site that displays the
[content. Each Content page serves as the detail page for all content of a single content type. See Create Custom Pages with Experience](https://help.salesforce.com/articleView?id=community_builder_create_page.htm&type=0&language=en_US)
[Builder.](https://help.salesforce.com/articleView?id=community_builder_create_page.htm&type=0&language=en_US)

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### ManagedEventSubscription (Beta)

Represents a managed event subscription in Pub/Sub API. Use a managed event subscription to track the events that a subscriber client
consumed and resume a subscription where it left off. This type extends the metadata type and inherits its `fullName` field.

Note: This feature is a Beta Service. Customer may opt to try such Beta Service in its sole discretion. Any use of the Beta Service
is subject to the applicable Beta Services Terms provided at Agreements and Terms.

File Suffix and Directory Location

ManagedEventSubscription components have the suffix `.managedEventSubscription` and are stored in the
`managedEventSubscriptions` folder.

Version

ManagedEventSubscription components are available in API version 60.0 and later.

Special Access Rules

You must have the Customize Application permission to deploy and retrieve this type.

Fields

**Field Name** **Field Type** **Description**

The position in the stream where the subscription starts when the client
initiates the subscription for the first time or if the client doesn’t commit
a Replay ID. Possible values are:

**•** `LATEST` —(Default) The subscription starts from the latest events
received. This option skips sending events that were published when
the client was disconnected.

**•** `EARLIEST` —The subscription starts from the earliest events stored
in the event bus. This option sends new events and any other events
less than 72 hours old. You can reprocess all stored events and catch
up on missed events. Use this option sparingly. Subscribing with the


```
defaultReplay

```

EventSubscriptionReplayPreset
(enumeration of
type string)

Metadata Types ManagedEventSubscription (Beta)

**Field Name** **Field Type** **Description**

`EARLIEST` option when a large number of event messages are
stored can slow performance and exhaust the event delivery
allocation.

The position in the stream where the subscription restarts if the
committed Replay ID is invalid. The Replay ID can be invalid if it’s older
than the event retention window. Possible values are:

**•** `LATEST` —(Default) The subscription restarts from the latest events
received. This option skips sending events that were published when
the client was disconnected.

**•** `EARLIEST` —The subscription restarts from the earliest events
stored in the event bus. This option sends new events and any other
events less than 72 hours old. You can reprocess all stored events
and catch up on missed events. Use this option sparingly. Subscribing
with the `EARLIEST` option when a large number of event
messages are stored can slow performance and exhaust the event
delivery allocation.

```
errorRecoveryReplay

```

EventSubscriptionReplayPreset
(enumeration of
type string)

`label` string The label for the managed subscription.

```
state

```

EventSubscriptionAdminState The execution state that the `ManagedSubscribe` RPC call consumes.
(enumeration of If `state` is set to `RUN`, the subscription starts when the
type string) `ManagedSubscribe` RPC call is made. Otherwise, the subscription

doesn't start. If an administrator later changes `state` from `RUN` to
`STOP`, the system notifies the Pub/Sub API client of the new `state`
value and the subscription disconnects. Also, the stored Replay ID value
that was committed previously is deleted. The next time the
`ManagedSubscribe` RPC call is made after `state` is changed
from `STOP` to `RUN`, the subscription starts from the
`defaultReplay` value.

The possible values for `state` are:

**•** `RUN` —(Default) The subscription is running and delivering new
events to the Pub/Sub API client.

**•** `STOP` —The subscription is stopped. No events are delivered to the
Pub/Sub API client during this state and the previously committed
Replay ID is deleted.

**•** `PAUSE` —Reserved for internal use.

`topicName` string

The topic name of the platform event or change event or the channel
name of a custom platform event channel or custom or standard change
data capture channel. The topic name can be one of the following values.

**•** For a platform event— `/event/EventName__e`

**•** For a custom platform event
channel— `/event/CustomPEChannel__chn`


### Metadata Types ManagedTopics

**Field Name** **Field Type** **Description**

**•** For the standard change event
channel— `/data/ChangeEvents`

**•** For a change event (replace `Object` with the object
name)— `/data/ObjectChangeEvent` . For example, for
Account, it’s `/data/AccountChangeEvent` .

**•** For a custom change event
channel— `/data/CustomChangeChannel__chn`

`version` string Reserved for internal use.

Declarative Metadata Sample Definition

The following is an example of a ManagedEventSubscription component with the file name
`My_Managed_Subscription.managedSubscription` .

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ManagedEventSubscription xmlns="http://soap.sforce.com/2006/04/metadata">

      <defaultReplay>LATEST</defaultReplay>

      <errorRecoveryReplay>LATEST</errorRecoveryReplay>

      <label>My Managed Subscription</label>

      <state>RUN</state>

      <topicName>/event/Order_Event__e</topicName>

   </ManagedEventSubscription>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>My_Managed_Subscription</members>

        <name>ManagedEventSubscription</name>

      </types>

      <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### ManagedTopics

Represents navigational and featured topics managed in an Experience Cloud site.

Note: The related Experience Cloud site must exist before you deploy managed topics. (This occurs automatically when deploying
an entire org.)


Metadata Types ManagedTopics

File Suffix and Directory Location

Components have the suffix managedTopics and are stored in the managedTopics folder. In that folder, you find separate files for each
Experience Cloud site (for example, `SiteNameA.managedTopics` and `SiteNameB.managedTopics` ).

Version

ManagedTopics components are available in API version 32.0 and later.

Fields

**Field Name** **Field Type** **Description**

`ManagedTopic` ManagedTopic Represents a specific navigational or featured topic.

ManagedTopic

**Field Name** **Field Type** **Description**

`name` string The topic name.

`managedTopicType` string The topic type: “Navigational” or “Featured”

`topicDescription` string An optional description of topic contents. This field is accessible only via
the API; there is no corollary in the user interface.

`parentName` string

The name of a parent topic for which this topic is a child. Child topics are
accessible from the subtopics section of the parent topic page and their
feeds are added to the parent topic feed.

Only navigational topics support parent-child relationships.

`position` int The placement of this topic relative to others of the same type. The results
differ depending on topic type:

**•** For top-level navigational topics, `position` arranges the Topics
menu in the Experience Cloud site.

**•** For child navigational topics, it arranges sibling topics in the subtopics
section.

**•** For featured topics, it arranges topic thumbnail images on the
Experience Cloud site home page.

Enter a number between 0 and 24. (The maximum amount of navigational
or featured topics is 25.)


Metadata Types ManagedTopics

Declarative Metadata Sample Definition

The following example retrieves or deploys managed topics for all sites:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ManagedTopics</name>

      </types>

      <version>32.0</version>

   </Package>

```

The following example shows a package.xml file referencing the ManagedTopics component:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>SiteName</members>

        <name>ManagedTopics</name>

      </types>

      <version>32.0</version>

   </Package>

```

The following example shows the ManagedTopics component itself:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ManagedTopics>

      <ManagedTopic>

        <name>Running</name>

        <managedTopicType>Navigational</managedTopicType>

        <topicDescription>Training advice</topicDescription>

        <parentName></parentName>

        <position>0</position>

      </ManagedTopic>

      <ManagedTopic>

        <name>Hiking</name>

        <managedTopicType>Navigational</managedTopicType>

        <topicDescription>Routes and gear</topicDescription>

        <parentName></parentName>

        <position>1</position>

      </ManagedTopic>

        <ManagedTopic>

           <name>Trails</name>

           <managedTopicType>Navigational</managedTopicType>

           <topicDescription>Maps for local favorites</topicDescription>

           <parentName>Hiking</parentName>

           <position>0</position>

        </ManagedTopic>

        <ManagedTopic>

           <name>Backpacks</name>

           <managedTopicType>Navigational</managedTopicType>

           <topicDescription>Recommended models</topicDescription>

           <parentName>Hiking</parentName>

           <position>1</position>

        </ManagedTopic>

```


### Metadata Types MarketingAppExtension

```
      <ManagedTopic>

        <name>Footwear</name>

        <managedTopicType>Featured</managedTopicType>

        <topicDescription>Suggested types for each sport</topicDescription>

        <parentName></parentName>

        <position>0</position>

      </ManagedTopic>

      <ManagedTopic>

        <name>Conditioning</name>

        <managedTopicType>Featured</managedTopicType>

        <topicDescription>How to get fit for any activity</topicDescription>

        <parentName></parentName>

        <position>1</position>

      </ManagedTopic>

   </ManagedTopics>

```

Usage

Managed topic images that are uploaded in API version 50.0 and later are stored as asset files. To migrate managed topic images that
are uploaded in API version 50.0 and later, use the ContentAsset metadata type. To migrate managed topic images that were uploaded
in API version 49.0 and earlier, use the Document metadata type.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### MarketingAppExtension

Represents an integration with a third-party app or service that is used to work with prospects.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### MarketingAppExtension components have the suffix .marketingappextension and are stored in the

`marketingappextensions` folder.

Version

### MarketingAppExtension components are available in API version 54.0 and later.


Metadata Types MarketingAppExtension

Special Access Rules

The first Salesforce or designated marketing admin to access Marketing App Extensions in an org must have the Manage Public List
Views user permission. Subsequent users don’t need the permission to work with the feature.

Fields

**Field Name** **Description**

```
description

isActive

isProtected

marketingAppExtActions

marketingAppExtActivities

masterLabel

```

MarketingAppExtActivity

**Field Type**
string

**Description**
The description of the extension for internal reference. Appears in the UI.

**Field Type**
boolean

**Description**
This field makes data for a Marketing App Extension available to use in Account
Engagement automations. Label is Active in Automations.

The default value is `false` . Appears in the UI.

**Field Type**
boolean

**Field Type**

MarketingAppExtAction on page 1547[]

**Description**
This field is a related list of associated external actions.

**Field Type**

MarketingAppExtActivity on page 1544[]

**Description**
This field is a related list of associated external prospect activities.

**Field Type**
string

**Description**

Required. Label for the MarketingAppExtension. In the UI, this field is Extension Name.

Represents an Activity Type, which is a prospect activity that occurs in a third-party app and can be used in Account Engagement
automations.


Metadata Types MarketingAppExtension

**Field Name** **Description**

```
description

endpointUrl

isActive

isProtected

marketingAppExtension

masterLabel

```

**Field Type**
string

**Description**
The description of the activity for internal reference. Appears in the UI.

**Field Type**
string

**Description**
A sample endpoint that can be used to help connect the activity type to a third-party
app. Appears in the UI.

**Field Type**
boolean

**Description**
This field makes data for the Activity Type available to use in Account Engagement
automations. Label is Active in Automations.

The default value is `false` . Appears in the UI.

**Field Type**
boolean

**Field Type**
string

**Description**
Required. The Marketing App Extension associated with the activity.

**Type**
string

**Description**
Required. Label for the MarketingAppExtActivity. In the UI, this field is Activity Name.

Declarative Metadata Sample Definition

This example retrieves all Activity Types associated with the MarketingAppExtension component.

```
<?xml version="1.0" encoding="UTF-8"?>

<MarketingAppExtension xmlns="http://soap.sforce.com/2006/04/metadata">

   <description>VidLand extension for US region</description>

   <isActive>true</isActive>

   <marketingAppExtActivities>

     <fullName>user_attended</fullName>

     <description>User attended activity capture for VidLand</description>

     <isActive>true</isActive>

```


Metadata Types MarketingAppExtension

```
        <marketingAppExtension>VidLand_US</marketingAppExtension>

        <masterLabel>user attended</masterLabel>

      </marketingAppExtActivities>

      <marketingAppExtActivities>

        <fullName>user_registered</fullName>

        <description>User registered activity capture for VidLand</description>

        <isActive>true</isActive>

        <marketingAppExtension>VidLand_US</marketingAppExtension>

        <masterLabel>user registered</masterLabel>

      </marketingAppExtActivities>

      <masterLabel>VidLand_US</masterLabel>

   </MarketingAppExtension>

```

This example `package.xml` references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <!-
   ~ Copyright 2021 Salesforce, Inc.

   ~ All Rights Reserved

   ~ Company Confidential

   -->

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

   <members>VidLand_US</members>

   <name>MarketingAppExtension</name>

   </types>

   </Package>

```

This example retrieves a specific Activity Type from the associated MarketingAppExtension component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <MarketingAppExtension xmlns="http://soap.sforce.com/2006/04/metadata">

      <description>VidLand extension for US region</description>

      <isActive>true</isActive>

      <marketingAppExtActivities>

        <fullName>user_attended</fullName>

        <description>User attended activity capture for VidLand</description>

        <isActive>true</isActive>

        <marketingAppExtension>VidLand_US</marketingAppExtension>

        <masterLabel>user attended</masterLabel>

      </marketingAppExtActivities>

      <masterLabel>VidLand_US</masterLabel>

   </MarketingAppExtension>

```

This example `package.xml` references the previous definition.

```
   <<?xml version="1.0" encoding="UTF-8"?>

   <!-
   ~ Copyright 2021 salesforce.com, inc.

   ~ All Rights Reserved

   ~ Company Confidential

   -->

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

   <members>VidLand_US.user_attended</members>

   <name>MarketingAppExtActivity</name>

```


Metadata Types MarketingAppExtension

```
   </types>

   <types>

   <members>VidLand_US</members>

   <name>MarketingAppExtension</name>

   </types>

   </Package>

```

MarketingAppExtAction

Represents an Action Type, which is an action that executes in a third-party app and can be used in Engagement Studio programs.

**Field Name** **Description**

```
actionName

actionParams

actionSchema

actionSelector

apiName

Description

```

**Field Type**
string

**Description**
The name of the action for internal use. Appears in the UI.

**Field Type**
string

**Description**
The parameters for the invocable action. Appears in the UI.

**Field Type**
string

**Description**
The JSON schema for the invocable action. Appears in the UI.

**Type**
string

**Description**
Invocable action selector. Appears in the UI.

**Field Type**
string

**Description**
This name can contain only underscores and alphanumeric characters, and must be
unique in your org. It must begin with a letter, not include spaces, not end with an
underscore, and not contain two consecutive underscores. This field is automatically
generated, but you can supply your own value if you create the record using the API.
Appears in the UI.

**Field Type**
string

**Description**
The description of the action for internal reference. Appears in the UI.


Metadata Types MarketingAppExtension

**Field Name** **Description**

```
isActive

isProtected

marketingAppExtension

```

**Field Type**
boolean

**Description**
This field makes data for the Action Type available to use in Engagement Studio Label
is Active in Automations.

The default value is `false` . Appears in the UI.

**Field Type**
boolean

**Field Type**
string

**Description**
Required. The Marketing App Extension associated with the action.

Declarative Metadata Sample Definition

This example retrieves a specific action associated the MarketingAppExtension component.

```
<?xml version="1.0" encoding="UTF-8"?>

<MarketingAppExtension xmlns="http://soap.sforce.com/2006/04/metadata">

   <fullName>VidLand_US</fullName>

   <description>VidLand extension for US region</description>

   <isActive>true</isActive>

   <marketingAppExtActions>

     <marketingAppExtension>VidLand_US</marketingAppExtension>

     <apiName>register_user</apiName>

     <isActive>true</isActive>

     <description>Register User for VidLand</description>>

     <actionSelector>VidLand_Register_User</actionSelector>

     <actionSchema>

  <![CDATA[

     {

 "properties": {

  "UserId": {

  "type": "string",

  "title": ""

  },

  "WebinarId": {

  "type": "string",

  "value": "webinarIdXYZ"

  }

 },

 "view": {

  "components": [{

  "definition": "lightning/control",

  "scope": "#/properties/UserId"

```


### Metadata Types MatchingRule

```
     }]

    },

    "required": [

     "UserId",

     "WebinarId",

     "From",

     "Body"

    ]

     }

     ]]>

        </actionSchema>

        <actionParams>

        <![CDATA[

        {

    "isStandard": false,

      "type": "apex"

     }

     ]]>

        </actionParams>

        <actionName>Register User</actionName>

      </marketingAppExtActions>

      <masterLabel>VidLand US</masterLabel>

   </MarketingAppExtension>

```

This example `package.xml` references the previous definition.

```
   <<?xml version="1.0" encoding="UTF-8"?>

   <!-
   ~ Copyright 2021 salesforce.com, inc.

   ~ All Rights Reserved

   ~ Company Confidential

   -->

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

   <members>VidLand_US</members>

   <name>MarketingAppExtension</name>

   </types>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### MatchingRule

Represents a matching rule that is used to identify duplicate records.

This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types MatchingRule

File Suffix and Directory Location

Matching rule components have the `.matchingRule` suffix and are stored in the `matchingRules` folder. The name of the
component file is the standard or custom object name that is associated with the matching rule.

In API version 39.0 and later, MatchingRule supports the Person Account object.

**•** The component file name is `PersonAccount.matchingRule` .

**•** The component directory is `matchingRules` .

Version

MatchingRule is available in API version 33.0 and later.

Fields

**Field Name** **Field Type** **Description**

`booleanFilter` string Specifies filter logic conditions.

`description` string The description of the matching rule.

`label` string Required. The name of the matching rule.

`matchingRuleItems` MatchingRuleItem The criteria that make up a matching rule.

```
ruleStatus

```

MatchingRuleItem

MatchingRuleStatus Required. The activation status of the matching rule. Values are:
(enumeration of

**•** _`Inactive`_

type string)

**•** _`Inactive`_

**•** _`Deactivating`_

**•** _`DeactivationFailed`_

**•** _`Active`_

**•** _`Activating`_

**•** _`ActivationFailed`_

Important: The only valid values you can declare when
deploying a package are _`Active`_ and _`Inactive`_ .

**Field Name** **Field Type** **Description**

```
blankValueBehavior

```

BlankValueBehavior Specifies how blank fields affect whether the fields being compared are
(enumeration of type considered matches. Valid values are:
string)

**•** _`MatchBlanks`_

**•** _`NullNotAllowed`_ (default)

`fieldName` string Required. Indicates which field to compare when determining if a record is
similar enough to an existing record to be considered a match.


Metadata Types MatchingRule

**Field Name** **Field Type** **Description**

```
matchingMethod

```

MatchingMethod Required. Defines how the fields are compared. Choose between the exact
(enumeration of type matching method and various fuzzy matching methods. Valid values are:
string)

**•** _`Exact`_

**•** _`FirstName`_

**•** _`LastName`_

**•** _`CompanyName`_

**•** _`Phone`_

**•** _`City`_

**•** _`Street`_

**•** _`Zip`_

**•** _`Title`_

For details on each matching method, see “Matching Methods Used with
Matching Rules” in the Salesforce Help.

Declarative Metadata Sample Definition

The following is a sample XML definition of a matching rule. A matching rule can be associated with either a standard or a custom object.

```
<?xml version="1.0" encoding="UTF-8"?>

<MatchingRules xmlns="http://soap.sforce.com/2006/04/metadata">

<matchingRules>

<fullName>AccountMatchingRule</fullName>

<label>Matching rule for accounts</label>

<description>this is sample rule description</description>

<matchingRuleItems>

<blankValueBehavior>NullNotAllowed</blankValueBehavior>

<fieldName>BillingCity</fieldName>

<matchingMethod>City</matchingMethod>

</matchingRuleItems>

<matchingRuleItems>

<blankValueBehavior>NullNotAllowed</blankValueBehavior>

<fieldName>Name</fieldName>

<matchingMethod>CompanyName</matchingMethod>

</matchingRuleItems>

<ruleStatus>Inactive</ruleStatus>

</matchingRules>

</MatchingRules>

```

The following `package.xml` shows how to reference a matching rule by name. It specifies the type name of MatchingRule.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

<types>

<members>Account.AccountMatchingRule</members>

<name>MatchingRule</name>

```


### Metadata Types MessagingChannel

```
   </types>

   <version>66.0</version>

   </Package>

```

The following `package.xml` shows how to reference all matching rules by specifying the plural MatchingRules type name and using
a wildcard to include all members.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

   <members>*</members>

   <name>MatchingRules</name>

   </types>

   <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### MessagingChannel

Represents the metadata associated with an Embedded Service Messaging channel.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### MessagingChannel components have the suffix messagingChannel and are stored in the messagingChannels folder.

Version

### MessagingChannel components are available in API version 55.0 and later.

Special Access Rules

This type is available if your org has the “Configure Messaging” and “View Setup and Configuration” permissions for Messaging enabled.


Metadata Types MessagingChannel

Fields

**Field Name** **Description**

```
automatedResponses

channelUsages

countryCode

customParameters

description

embeddedConfig

externalAccountId

masterLabel

```

**Field Type**

MessagingAutoResponse[]

**Description**
The auto-responses associated with the messaging channel.

**Field Type**

MessagingChannelUsage[]

**Description**
The deployment types and consent configuration for the messaging channel. Available
in API version 62.0 and later.

**Field Type**
string

**Description**
The ISO country code for the messaging channel. Available in API version 62.0 and
later.

**Field Type**

MessagingChannelCustomParameter[]

**Description**
The custom parameters associated with the messaging channel.

**Field Type**
string

**Description**
The channel description.

**Field Type**

EmbeddedConfig[]

**Description**
The settings associated with the messaging channel.

**Field Type**
string

**Description**
The external account identifier for the messaging channel. Available in API version
62.0 and later.

**Field Type**
string


Metadata Types MessagingChannel

**Field Name** **Description**

**Description**

Required. The channel label.

```
messagingChannelType

messagingKeywords

platformKey

queueRoutingConfig

sessionHandlerFlow

```

**Field Type**
MessagingChannelType (enumeration of type string)

**Description**

Required. Values are:

**•** `AppleMessagesForBusiness` —Apple Messages for Business. Available
in API version 65.0 and later.

**•** `Custom` —Bring Your Own Channel for Messaging or Bring Your Own Channel
for CCaaS. Available in API version 61.0 and later.

**•** `EmbeddedMessaging` —Enhanced Chat.

**•** `Facebook` —Facebook Messenger. Available in API version 65.0 and later.

**•** `Line` —Line. Available in API version 65.0 and later.

**•** `PstnVoice` —Agentforce Voice (PSTN). Available in API version 65.0 and later.

**•** `Text` —SMS. Available in API version 65.0 and later.

**•** `Voice` —Service Cloud Voice. Available in API version 58.0 and later.

**•** `WhatsApp` —WhatsApp. Available in API version 65.0 and later.

**•** `WhatsAppVoice` —Available in API version 65.0 and later.

Third-party Messaging channels in Salesforce, such as WhatsApp and Facebook
Messenger, don’t use this metadata type.

**Field Type**

MessagingKeyword[]

**Description**
Keywords associated with the messaging channel.

**Field Type**
string

**Description**
The platform key for the messaging channel. Available in API version 62.0 and later.

**Field Type**
string

**Description**
The queue routing configuration for the messaging channel. Available in API version
64.0 and later.

**Field Type**
string


Metadata Types MessagingChannel

**Field Name** **Description**

**Description**
The Omni-Channel flow used to route the channel’s messaging sessions.

```
sessionHandlerQueue

sessionHandlerType

sessionHandlerUser

standardParameters

```

EmbeddedConfig

**Field Type**
string

**Description**

Required. The queue used to route messages. If a sessionHandlerFlow is also selected,
sessionHandlerQueue is the fallback queue used if a message can’t be routed using
the selected flow.

**Field Type**
MessagingSessionHandlerType (enumeration of type string)

**Description**

Required. The method used to route messages in the channel. Values are:

**•** `AgentforceServiceAgent`

**•** `Flow`

**•** `Queue`

**•** `User`

**Field Type**
string

**Description**
The user to handle routing for the messaging channel. Available in API version 62.0
and later.

**Field Type**

MessagingChannelStandardParameter[]

**Description**
Parameters added to the messaging channel.

Represents settings specific to an embedded messaging channel.


Metadata Types MessagingChannel


Metadata Types MessagingChannel

MessagingAuthorization

This junction entity stores the messaging channel authorization for a Messaging Channel (Embedded Messaging Channel). On this entity,
we configure different authorization methods supported by the Messaging for In-App and Web `(Embedded Messaging) channel. This
entity is available in API version 62.0 or later.


Metadata Types MessagingChannel

MessagingAutoResponse

Represents an automated response used in a channel.

**Field Name** **Description**

autoResponseContentType

language

messageDefinitionName

```
response

```

responseTimeoutInMins

```
type

```

**Field Type**
string

**Description**
The content type of the auto-response: TextResponse or MessageDefinition.

**Field Type**
string

**Description**
The language of the auto response.

**Field Type**
string

**Description**
The name of the messaging component.

**Field Type**
string

**Description**
The text of the auto response.

**Field Type**
integer

**Description**
The number of minutes after which a response can no longer be sent. The value can
range from 5 to 60.

**Field Type**
MessagingAutoResponseType (enumeration of type string)


Metadata Types MessagingChannel

**Field Name** **Description**

**Description**
Required. The type of response, which determines when it’s used in a messaging
session. Values are:

**•** `AgentEndEngagementResponse`

**•** `AgentEngagedResponse`

**•** `CustomResponse` (Available in API version 65.0 and later.)

**•** `DoubleOptInPrompt` (Available in API version 65.0 and later.)

**•** `EndUserIdleResponse` (Available in API version 65.0 and later.)

**•** `EndUserInactiveResponse` (Available in API version 65.0 and later.)

**•** `HelpResponse` (Available in API version 65.0 and later.)

**•** `InitialResponse`

**•** `OptInConfirmation` (Available in API version 65.0 and later.)

**•** `OptInPrompt` (Available in API version 65.0 and later.)

**•** `OptOutConfirmation` (Available in API version 65.0 and later.)

MessagingChannelCustomParameter

Represent a custom parameter added to a channel.

**Field Name** **Description**

```
actionParameterMappings

externalParameterName

masterLabel

maxLength

```

**Field Type**

MessagingChannelActionParameterMapping[]

**Description**
The mapping used to map the parameter value to a flow or task.

**Field Type**
string

**Description**
Required. The external name of the parameter.

**Field Type**
string

**Description**
Required. The label of the parameter.

**Field Type**
int

**Description**
The maximum length of the parameter value.


Metadata Types MessagingChannel

**Field Name** **Description**

```
name

parameterDataType

```

**Field Type**
string

**Description**
Required. The name of the parameter.

**Field Type**
FlowDataType (enumeration of type string)

**Description**
Required. The format of the parameter. Values are:

**•** `Apex`

**•** `Boolean`

**•** `Currency`

**•** `Date`

**•** `DateTime`

**•** `Multipicklist`

**•** `Number`

**•** `Picklist`

**•** `SObject`

**•** `String`

**•** `Time`

MessagingChannelActionParameterMapping

Represents a mapping between a parameter and an Omni-Channel flow or agent task.

**Field Name** **Description**

```
actionParameterName

```

**Field Type**
string

**Description**
Required. The name of the flow that the custom or standard parameters are mapped
to.

MessagingChannelStandardParameter

Represents a standard parameter used to pass information into a channel.


Metadata Types MessagingChannel

**Field Name** **Description**

```
actionParameterMappings

externalInteractionId

externalInteractionName

externalInteractionType

parameterType

```

**Field Type**

MessagingChannelActionParameterMapping[]

**Description**
The mapping associated with the parameter.

**Field Type**
MessagingChannelStandardParameterType (enumeration of type string)

**Description**
An ID assigned to the external interaction, such as a campaign ID.

**Field Type**
MessagingChannelStandardParameterType (enumeration of type string)

**Description**
The name of the external interaction, such as a campaign name.

**Field Type**
MessagingChannelStandardParameterType (enumeration of type string)

**Description**
The type of external interaction, such as MarketingCampaign.

**Field Type**
MessagingChannelStandardParameterType (enumeration of type string)

**Description**

Required. The type of parameter. Values are:

**•** `Email`

**•** `FirstName`

**•** `LastName`

**•** `Subject`

MessagingChannelUsage

Represents the deployment type and consent configuration for a messaging channel. Available in API version 62.0 and later.


Metadata Types MessagingChannel

MessagingKeyword

Represents settings specific to an EmbeddedMessaging MessagingChannel. Available in API version 62 or later.


Metadata Types MessagingChannel

Declarative Metadata Sample Definition

The following is an example of a MessagingChannel component. This messaging channel passes custom and standard parameters from
the messaging channel to a flow, and it routes to a flow with a fallback queue.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <MessagingChannel xmlns="http://soap.sforce.com/2006/04/metadata">

      <description>Test in-app messaging channel</description>

      <masterLabel>TestInAppChannel</masterLabel>

      <messagingChannelType>EmbeddedMessaging</messagingChannelType>

      <sessionHandlerQueue>Demo_Queue</sessionHandlerQueue>

      <sessionHandlerType>Queue</sessionHandlerType>

      <embeddedConfig>

        <authMode>Auth</authMode>

        <isAttachmentUploadEnabled>true</isAttachmentUploadEnabled>

        <isSaveTranscriptEnabled>false</isSaveTranscriptEnabled>

        <isEstimatedWaitTimeEnabled>false</isEstimatedWaitTimeEnabled>

        <verifiedUserJwtExpirationTime>360</verifiedUserJwtExpirationTime>

        <messagingAuthorizations>

           <authorizationType>PublicKeyCertificateSet</authorizationType>

           <authProviderName></authProviderName>

           <publicKeyCertificateSetName>pcks1</publicKeyCertificateSetName>

           <enabled>false</enabled>

           <authIdentifier>auth_identifier_one</authIdentifier>

        </messagingAuthorizations>

      </embeddedConfig>

      <automatedResponses>

        <autoResponseContentType>MessageDefinition</autoResponseContentType>

        <messageDefinitionName>Sample</messageDefinitionName>

        <type>EndUserInactiveResponse</type>

        <responseTimeoutInMins>10</responseTimeoutInMins>

      </automatedResponses>

      <automatedResponses>

        <autoResponseContentType>MessageDefinition</autoResponseContentType>

        <messageDefinitionName>Sample</messageDefinitionName>

        <type>InitialResponse</type>

      </automatedResponses>

      <automatedResponses>

        <autoResponseContentType>MessageDefinition</autoResponseContentType>

        <messageDefinitionName>Sample</messageDefinitionName>

        <type>AgentEndEngagementResponse</type>

      </automatedResponses>

      <automatedResponses>

        <autoResponseContentType>MessageDefinition</autoResponseContentType>

        <messageDefinitionName>Sample</messageDefinitionName>

        <type>AgentEngagedResponse</type>

      </automatedResponses>

      <automatedResponses>

        <autoResponseContentType>TextResponse</autoResponseContentType>

        <language>en_US</language>

        <response>You've opted out of receiving messages from us, so we won't contact you

    again.</response>

        <type>OptOutConfirmation</type>

      </automatedResponses>

      <automatedResponses>

```


Metadata Types MessagingChannel

```
        <autoResponseContentType>TextResponse</autoResponseContentType>

        <language>en_US</language>

        <response>Custom response1</response>

        <type>CustomResponse</type>

      </automatedResponses>

      <automatedResponses>

        <autoResponseContentType>TextResponse</autoResponseContentType>

        <language>en_US</language>

        <response>Opt In Confirmation response</response>

        <type>OptInConfirmation</type>

      </automatedResponses>

      <automatedResponses>

        <autoResponseContentType>TextResponse</autoResponseContentType>

        <language>en_US</language>

        <response>Text STOP to opt out of further messages.</response>

        <type>HelpResponse</type>

      </automatedResponses>

      <messagingKeywords>

        <keyword>stopall</keyword>

        <keyword>cancel</keyword>

        <keyword>stop</keyword>

        <keyword>unsubscribe</keyword>

        <keyword>end</keyword>

        <keyword>quit</keyword>

        <keywordType>OptOut</keywordType>

        <language>en_US</language>

      </messagingKeywords>

      <messagingKeywords>

        <keyword>help</keyword>

        <keywordType>Help</keywordType>

        <language>en_US</language>

      </messagingKeywords>

      <messagingKeywords>

        <keyword>customkeyword1</keyword>

        <keywordType>Custom</keywordType>

        <language>en_US</language>

      </messagingKeywords>

      <messagingKeywords>

        <keyword>OptInkeyword1</keyword>

        <keywordType>OptIn</keywordType>

        <language>en_US</language>

      </messagingKeywords>

   </MessagingChannel>

```

If you route the messaging channel to a queue, there’s no fallback flow.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <MessagingChannel xmlns="http://soap.sforce.com/2006/04/metadata">

      <masterLabel>EmbeddedChannel2</masterLabel>

      <messagingChannelType>EmbeddedMessaging</messagingChannelType>

      <sessionHandlerQueue>DemoQueueName</sessionHandlerQueue>

      <sessionHandlerType>Queue</sessionHandlerType>

   </MessagingChannel>

```


### Metadata Types Metadata

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>MessagingChannel</name>

      </types>

      <version>55.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### Metadata

The base class for all metadata types. You can’t edit this object. A component is an instance of a metadata type.

### Metadata is analogous to sObject, which represents all standard objects. Metadata represents all components and fields in the Metadata

API. Instead of identifying each component with an ID, each custom object or custom field has a unique `fullName`, which must be
distinct from standard object names, as it must be when you create custom objects or custom fields in the Salesforce user interface.

Version

### Metadata components are available in API version 10.0 and later.

Fields

**Field Name** **Field Type** **Description**

`fullName` string Required. The name of the component. For components with parent
objects, such as fields and list views, the name must specify the name of

the parent, for example `Account.FirstName` . The __c suffix must
be appended to custom object names and custom field names when
you’re setting the `fullName` . For example, a custom field in a custom
object could have a `fullName` of
`MyCustomObject__c.MyCustomField__c` .

To reference a component in a package, prepend the package’s
namespace prefix to the component name in the `fullName` field. Use
the following syntax: _**`namespacePrefix`**_ `__` _**`ComponentName`**_ .
For example, for the custom field component
`MyCustomObject__c.MyCustomField__c` and the namespace
`MyNS`, the full name is
`MyNS__MyCustomObject__c.MyCustomField__c` .

A namespace prefix is a 1-character to 15-character alphanumeric
identifier that distinguishes your package and its contents from other


### Metadata Types MetadataWithContent

**Field Name** **Field Type** **Description**

publishers’ packages. For more information, see Create and Register Your
Namespace for Second-Generation Managed Packages.

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

CustomObject

CustomField

### MetadataWithContent MetadataWithContent MetadataWithContent is the base type for all metadata types that contain content, such as documents or email templates. It extends

Metadata. You can’t edit this object.

Version

### MetadataWithContent components are available in API version 14.0 and later.

Fields

**Field Name** **Field Type** **Description**

`content` base64Binary Base 64-encoded binary data. Before making an API call, client applications
must encode the binary attachment data as base64. Upon receiving a

response, client applications must decode the base64 data to binary. This
conversion is handled for you by a SOAP client.

`fullName` string Required. The name of the component. The `fullName` can contain
only underscores and alphanumeric characters. It must be unique, begin

with a letter, not include spaces, not end with an underscore, and not
contain two consecutive underscores.

Inherited from the Metadata component, this field isn’t defined in the
WSDL for this component. It must be specified when creating, updating,
or deleting. See create() to see an example of this field specified for a call.


### Metadata Types MfgProgramTemplate

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

Metadata

### MfgProgramTemplate

Represents a definition of a program to create a program-based business. A program-based business, also known as a Manufacturing
Program, enables manufacturers to drive their business models with forecasting tools and manage the end-to-end sales process efficiently.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### MfgProgramTemplate components have the suffix .mfgProgramTemplate and are stored in the MfgProgramTemplate

folder.

Version

### MfgProgramTemplate components are available in API version 54.0 and later.

Special Access Rules

The program-based business feature setting for Manufacturing Cloud is required to create a program template.

Fields

**Field Name** **Description**

```
description

programTemplateItems

```

**Field Type**
string

**Description**
The description of the manufacturing program template.

**Field Type**
### MfgProgramTemplateItem[]

**Description**
The list of templates associated with the manufacturing program template.


Metadata Types MfgProgramTemplate

**Field Name** **Description**

```
programTemplateName

status

```

**Field Type**
string

**Description**

Required.

The unique identifier for the manufacturing program template.

**Field Type**
MfgProgramTemplateStatus (enumeration of type string)

**Description**

Required.

The status of the manufacturing program template.

Values are:

**•** `Active`

**•** `Draft`

**•** `Inactive`

The default value is `Active` .

MfgProgramTemplateItem

A program template item defines each of the templates associated with a manufacturing program. A template item includes program
details, such as a data transformation type and a display order. Transformation type is the method to forecast business visibility to
manufacturers.

**Field Name** **Description**

```
advAccountForecastSet

contextDefinition

description

```

**Field Type**
string

**Description**
The forecast set associated with the transformation.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The context definition that defines how data is mapped and transformed to the target,
such as an opportunity or account.

**Field Type**
string


Metadata Types MfgProgramTemplate

**Field Name** **Description**

**Description**
The description of the manufacturing program template item.

```
sourceContextMappingName

targetContextMappingName

templateItemName

transformationDisplayOrder

transformationType

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The context mapping that defines how data is mapped from a list of facts(Input Data)
to create structured information.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The context mapping that defines how the structured data is saved to the target, such
as an opportunity or sales agreement.

**Field Type**
string

**Description**

Required.

The name of the manufacturing program template item.

**Field Type**
int

**Description**

Required.

The display order of the transformation in the manufacturing program template.

**Field Type**
MfgProgramTransformationType (enumeration of type string)

**Description**

Required.

Specifies the type of transformation.

Values are:

**•** `BusinessTransformation`

**•** `ForecastSetRelation`


### Metadata Types MilestoneType

Declarative Metadata Sample Definition

The following is an example of a MfgProgramTemplate component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <MfgProgramTemplate xmlns="http://soap.sforce.com/2006/04/metadata"

   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

      <description>Program Template</description>

      <programTemplateItems>

         <templateItemName>Template Item #1</templateItemName>

         <transformationDisplayOrder>1</transformationDisplayOrder>

         <transformationType>BusinessTransformation</transformationType>

         <description>Program Template Item</description>

      </programTemplateItems>

      <programTemplateName>Sample Program Template</programTemplateName>

      <status>Draft</status>

   </MfgProgramTemplate>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

         <members>*</members>

         <name>MfgProgramTemplate</name>

      </types>

      <version>54.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### MilestoneType

Represents the name and description of a milestone, which you can use in an entitlement process to track important steps in cases.

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

Milestone types are stored in the `milestoneTypes` directory of the corresponding package directory. The extension is
`.milestoneType` .

Version

### MilestoneType on page 1570 is available in API version 27.0 and later.


### Metadata Types MlDomain

Fields

**Field Name** **Field Type** **Description**

`description` string The description of the milestone.

```
RecurrenceType

```

`MilestoneTypeRecurrenceType` The type of recurrence for the milestone. Available in API version 29.0
(enumeration of and later. Valid values are:
type string)

**•** `none` —Specifies no recurrence for the milestone. The milestone
occurs only one time until the entitlement process exits.

**•** `recursIndependently` —Specifies independent recurrence
for the milestone.

**•** `recursChained` —Specifies sequential recurrence for the
milestone.

Declarative Metadata Sample Definition

Here’s a sample milestone type.

```
<?xml version="1.0" encoding="UTF-8"?>

<MilestoneType xmlns="http://soap.sforce.com/2006/04/metadata">

   <description>First Response Time</description>

</MilestoneType>

```

And, here’s the sample `package.xml` file that references the MilestoneType component definition:

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>* or a valid name of a milestone type</members>

     <name>MilestoneType</name>

   </types>

   <version>29.0</version>

</Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### MlDomain

Represents an Einstein Intent Set.

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### MlDomain components have the suffix .mlDomain and are stored in the mlDomains folder.


Metadata Types MlDomain

Version

MlDomain components are available in API version 43.0 and later.

Special Access Rules

This object is available only if Chat and Einstein Bots are enabled in your org.

Fields

**Field Name** **Field Type** **Description**

`description` string Einstein Intent Set description.

`label` string Einstein Intent Set name.

`mlIntents` MlIntent[] List of intents under this Einstein Intent Set.

`mlSlotClasses` MlSlotClass[] List of entities under this Einstein Intent Set.

MlIntent

An intent in an Einstein Intent Set.

**Field Name** **Field Type** **Description**

`description` string Einstein Intent Set description.

`developerName` string Required. This unique name prevents conflicts with other Einstein Intent Sets
associated with the same bot version. This name can contain only underscores

and alphanumeric characters and must be unique in your org. It must begin
with a letter, not include spaces, not end with an underscore, and not contain
two consecutive underscores.

Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

`label` string Einstein Intent Set name.

`mlIntentUtterances` MlIntentUtterance[] List of customer inputs for this intent.

`relatedMlIntents` MlRelatedIntent[] List of intents within an Einstein Intent Set used to expand customer inputs for
this intent. Only intents within local Einstein Intent Sets have related intents.

MlIntentUtterance

A customer input for this intent.


Metadata Types MlDomain

**Field Name** **Field Type** **Description**

`utterance` string A customer input or natural language query that triggers the parent intent.

MlRelatedIntent

An intent in an Einstein Intent Set used to expand customer inputs for this intent. Only intents within local Einstein Intent Sets have
related intents.

**Field Name** **Field Type** **Description**

`relatedMlIntent` string Name of the intent that is used to extend the customer inputs of the current
parent intent.

MlSlotClass

An entity in this Einstein Intent Set.

**Field Name** **Field Type** **Description**

```
dataType

```

MlSlotClassDataType A list of the data types available for the MISlotClass. Valid values are:
(enumeration of type

**•** `Text`

string)

**•** `Text`

**•** `Number`

**•** `Boolean`

**•** `Date`

**•** `DateTime`

**•** `Currency`

`description` string A description of an Einstein Bot entity.

`developerName` string Required. This unique name prevents conflicts with other entities in an Einstein
Intent Set. This name can contain only underscores and alphanumeric

characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive
underscores.

Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

`extractionRegex` string Regular expression used to extract an entity when the type is set to `Pattern` .

```
extractionType

```

MlSlotClassExtractionType Required. Valid values are:
(enumeration of type

**•** `Pattern`

string)

**•** `Pattern`

**•** `Value`

`label` string Label that identifies an entity throughout the Salesforce user interface.

`mlSlotClassValues` MlSlotClassValue[] List of entity values associated with an entity of type `Value` .


Metadata Types MlDomain

MlSlotClassValue

An entity value associated with an entity of type `Value` .

**Field Name** **Field Type** **Description**

`synonymGroup` SynonymGroup Represents a list of terms or synonyms for the current entity value.

`value` string Single value used to extract an entity of type `Value` .

SynonymGroup

Represents a group of synonymous words or phrases.

**Field Name** **Field Type** **Description**

Required. Specifies the languages the value list applies to. If value list items are
specific to a single language, specify only that language. If the value list items
apply to multiple languages, specify multiple languages for one value list.

```
languages

```

Language
(enumeration of type
string)

`terms` string Required. A word or phrase synonymous with other terms in the value list.

Declarative Metadata Sample Definition

The following is an example of an MlDomain.

```
<?xml version="1.0" encoding="UTF-8"?>

<MlDomain xmlns="http://soap.sforce.com/2006/04/metadata">

   <label>TestDomainMetadata</label>

   <description>This is domain 2 for metadata testing</description>

   <mlIntents>

     <developerName>Test_Intent_New</developerName>

     <label>Test Intent New</label>

     <mlIntentUtterances>

        <utterance>Utterance Hello</utterance>

     </mlIntentUtterances>

     <mlIntentUtterances>

        <utterance>Utterance Hi</utterance>

     </mlIntentUtterances>

     <mlIntentUtterances>

        <utterance>Utterance What</utterance>

     </mlIntentUtterances>

   </mlIntents>

   <mlIntents>

     <developerName>Test_Intent_New2</developerName>

     <label>Test Intent New 2</label>

   </mlIntents>

   <mlSlotClasses>

     <developerName>Test_Entity1</developerName>

     <label>Test Entity 1</label>

     <extractionType>Value</extractionType>

     <mlSlotClassValues>

```


Metadata Types MlDomain

```
             <value>Choice value 1</value>

           </mlSlotClassValues>

           <mlSlotClassValues>

             <value>Choice value 2</value>

           </mlSlotClassValues>

      </mlSlotClasses>

      <mlSlotClasses>

        <developerName>Test_Entity2</developerName>

        <label>Test Entity 2</label>

        <extractionType>Pattern</extractionType>

      </mlSlotClasses>

      <mlSlotClasses>

           <dataType>Text</dataType>

           <description>Valid Email Address</description>

           <developerName>Email</developerName>

           <extractionRegex>\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b</extractionRegex>

           <extractionType>Pattern</extractionType>

           <label>Email</label>

      </mlSlotClasses>

      <mlSlotClasses>

        <developerName>airport</developerName>

        <extractionType>Value</extractionType>

        <label>airport</label>

        <mlSlotClassValues>

           <synonymGroup>

             <languages>en_US</languages>

             <terms>San Francisco</terms>

             <terms>The City</terms>

           </synonymGroup>

           <value>SFO</value>

        </mlSlotClassValues>

        <mlSlotClassValues>

           <synonymGroup>

             <languages>en_US</languages>

             <terms>Oakland</terms>

             <terms>The Town</terms>

           </synonymGroup>

           <value>OAK</value>

        </mlSlotClassValues>

      </mlSlotClasses>

   </MlDomain>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>TestDomainMetadata</members>

        <name>MlDomain</name>

      </types>

      <version>43.0</version>

   </Package>

```


### Metadata Types MLDataDefinition

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### MLDataDefinition

Represents a modeling data definition, which specifies the data used to create a model. Such data can include filters, fields to include,
fields to exclude, and so on. This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### MLDataDefinition components have the suffix .mlDataDefinition and are stored in the mlDataDefinitions folder.

Version

### MLDataDefinition is available in API version 50.0 and later.

Fields

**Field Name** **Field Type** **Description**

`developerName` string Required. Represents the name of the data definition. Can contain only
underscores and alphanumeric characters and must be unique in your

org. It must begin with a letter, not include spaces, not end with an
underscore, and not contain two consecutive underscores. Only users
with View DeveloperName OR View Setup and Configuration permission
can view, group, sort, and filter this field.

`entityDeveloperName` string

Required. The developer name of the object from which the model data
is retrieved. After the MLDataDefinition entity is created,
`entityDeveloperName` can’t be updated.

`excludedFields` string[] Fields that are excluded from the model.

`includedFields` string[] Fields that are included in the model.

`joinFields` MLField[] Reserved for future use.

`parentDefinitionDevName` string Reserved for future use.

`scoringFilter` MLFilter Specifies records to which the prediction scores are written.

`segmentFilter` MLFilter

This field further filters data used in training and scoring when
`segmentFilter` is combined with both `scoringFilter` and
`trainingFilter` . For example, select all records in a specific region.

`trainingFilter` MLFilter Specifies the records that make up the training set.


Metadata Types MLDataDefinition

**Field Name** **Field Type** **Description**

```
type

```

MLField

MLDataDefinitionType Required. Valid values are:
(enumeration of

**•** `Candidate`

type string)

**•** `Candidate`

**•** `Interaction`

**•** `Prediction`

**•** `Recipient`

After the model is created, `type` can’t be updated.

Represents a single field in the data definition. Available in API version 50.0 and later.

**Field Name** **Field Type** **Description**

`entity` string Required. The object that contains the field.

`field` string Required. The name of the field.

`relatedField` MLField Reserved for future use.

```
relationType

type

```

MLFilter

MLRelationType Reserved for future use. Valid values are:
(enumeration of type

**•** `Full`

string)

**•** `Full`

**•** `Inner`

**•** `Leftinner`

**•** `Leftouter`

MLFieldType Required. How the field is used in a prediction. Valid values are:
(enumeration of type

**•** `Excluded`

string)

**•** `Excluded`

**•** `Expression`

**•** `Included`

**•** `Join`

**•** `Prediction`

**•** `Pushback`

**•** `Related`

**•** `SourceDate`

Represents a data filter based on a data comparison. For each comparison, there’s a left-hand element, an operator, and a right-hand
element. For each record, only one of these left-hand elements is populated: `lhFilter`, `lhPredictionField`, or `lhValue` .
Similarly, for each record, only one of these right-hand elements is populated: `rhFilter`, `rhPredictionField`, or `rhValue` .
Available in API version 50.0 and later.


Metadata Types MLDataDefinition

**Field Name** **Field Type** **Description**

`filterName` string Required. Name of the filter.

`lhFilter` MLFilter Left-hand filter condition.

`lhPredictionField` string Left-hand prediction field.

```
lhType

lhUnit

```

AIValueType The value type if a left-hand value is specified. Valid values are:
(enumeration of type

**•** `Boolean`

string)

AIFilterUnit The unit if a left-hand filter is specified. Valid values are:
(enumeration of type

**•** `Milliseconds`

string)

**•** `Boolean`

**•** `Comparison`

**•** `Currency`

**•** `Date`

**•** `DateTime`

**•** `Number`

**•** `String`

**•** `Supplier`

**•** `Varchar`

**•** `Milliseconds`

**•** `Seconds`

**•** `Minutes`

**•** `Hours`

**•** `Days`

**•** `Weeks`

**•** `Months`

**•** `Years`

`lhValue` string The left-hand value.

```
operation

```

AIFilterOperation Required. Valid values are:
(enumeration of type

**•** `And`

string)

**•** `And`

**•** `Or`

**•** `Not`

**•** `LessThan`

**•** `LessThanOrEqual`

**•** `GreaterThan`

**•** `GreaterThanOrEqual`

**•** `Equals`

**•** `NotEquals`

**•** `Add`

**•** `Subtract`

**•** `Multiply`


Metadata Types MLDataDefinition

**Field Name** **Field Type** **Description**

**•** `Divide`

**•** `IsNull`

**•** `IsNotNull`

**•** `StartsWith`

**•** `EndsWith`

**•** `Contains`

**•** `Concat`

**•** `DoesNotContain`

**•** `Between`

**•** `In`

`rhFilter` MLFilter Right-hand filter condition.

`rhPredictionField` string Right-hand prediction field.

```
rhType

rhUnit

```

AIValueType The value type if a right-hand value is specified. Valid values are:
(enumeration of type

**•** `Boolean`

string)

AIFilterUnit The unit if a right-hand filter is specified. Valid values are:
(enumeration of type

**•** `Milliseconds`

string)

**•** `Boolean`

**•** `Comparison`

**•** `Currency`

**•** `Date`

**•** `DateTime`

**•** `Number`

**•** `String`

**•** `Supplier`

**•** `Varchar`

**•** `Milliseconds`

**•** `Seconds`

**•** `Minutes`

**•** `Hours`

**•** `Days`

**•** `Weeks`

**•** `Months`

**•** `Years`

`rhValue` string The right-hand value.

`sortOrder` int

Specifies the order of operations for evaluating the expressions. For example,
if you have two conditions, this field specifies which condition is evaluated
first.


### Metadata Types MLPredictionDefinition

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### MLPredictionDefinition

Represents a prediction definition that specifies details about the prediction. This type extends the Metadata metadata type and inherits
its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### MLPredictionDefinition components have the suffix .mlPrediction and are stored in the mlPredictions folder.

Version

### MLPredictionDefinition is available in API version 50.0 and later.

Fields

**Field Name** **Field Type** **Description**

`aiApplicationDeveloperName` string Required. Represents the developer name of the parent AI application. Can
contain only underscores and alphanumeric characters and must be unique

in your org. It must begin with a letter, not include spaces, not end with an
underscore, and not contain two consecutive underscores.

`description` string Description of the prediction.

`developerName` string Required. Represents the name of the prediction definition. Can contain only
underscores and alphanumeric characters and must be unique in your org. It

must begin with a letter, not include spaces, not end with an underscore, and
not contain two consecutive underscores.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

`masterLabel` string Label that identifies the ML prediction definition throughout the Salesforce
user interface.

`negativeExpression` MLFilter Reserved for future use.

`positiveExpression` MLFilter Reserved for future use.

`predictionField` string Field that the prediction is based on.


### Metadata Types MobileApplicationDetail

**Field Name** **Field Type** **Description**

`priority` int Reflects the priority of the MLPD object when an AIApplication has multiple
child MLPDs. Nillable.

`pushbackField` string Field that the prediction writes scores to.

```
status

type

```

MLPredictionDefinitionStatus Required. The status of the prediction. Valid values are:
(enumeration of type

**•** `Enabled`

string)

**•** `Draft`

AIPredictionType Required. The type of model that returns the prediction values. Valid values
(enumeration of type are:
string)

**•** `BinaryClassification`

**•** `DeepLearningIntentClassification`

**•** `DeepLearningNameEntityRecognition`

**•** `GlobalDeepLearningIntentClassification`

**•** `GlobalDeepLearningNameEntityRecognition`

**•** `LanguageDetection`

**•** `MulticlassClassification`

**•** `Regression`

**•** `ScoringSpecificOutcome`

**•** `Enabled`

**•** `Disabled`

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### MobileApplicationDetail

Represents the packaging attributes for a mobile connected app. This type extends the Metadata metadata type and inherits its
`fullName` field.

File Suffix and Directory Location

### MobileApplicationDetail components have the suffix MobileApplicationDetail and are stored in the MobileApplicationDetails folder.

Version

### MobileApplicationDetail components are available in API version 47.0 and later.


Metadata Types MobileApplicationDetail

Fields

**Field Name** **Field Type** **Description**

`applicationBinaryFile` base64 Base 64-encoded binary data file for the mobile app.

`applicationBinaryFileName` string Filename for the mobile app binary data file.

`applicationBundleIdentifier` string iOS apps only: the unique application bundle identifier.

`applicationFileLength` int The length of the mobile app binary data file.

`applicationIconFile` string iOS apps only: the application icon.

`applicationIconFileName` string iOS apps only: the application icon filename.

`applicationInstallUrl` string URL to install the mobile app.

```
devicePlatform

```

DevicePlatformType Required. Platform that supports the mobile app. The valid values are:
(enumeration of

**•** `android`

type string)

**•** `android`

**•** `ios`

`deviceType` string Supported device type for mobile app. The valid values are:

**•** `minitablet`

**•** `phone`

**•** `tablet`

`minimumOsVersion` string Minimum OS version required to install the mobile app.

`privateApp` boolean Specifies whether the mobile app is private ( `true` ) or not ( `false` ).

`version` string Required. Version number of the mobile app.

Usage

When you create a connected app in Salesforce Classic or Lightning Experience and enter mobile app settings, those settings are stored
in a MobileApplicationDetail component. In this example, the metadata retrieved for a connected app includes MobileApplicationDetail
metadata.

```
<?xml version="1.0" encoding="UTF-8"?>

<<ConnectedApp xmlns="http://soap.sforce.com/2006/04/metadata">

  <contactEmail>paul.chen@salesforce.com</contactEmail>

  <label>MobileApplicationDetailConnectedApp</label>

  <mobileAppConfig>

   <applicationBinaryFile></applicationBinaryFile>

   <applicationInstallUrl>https://appstore.apple.com/MobileApplicationDetail

     </applicationInstallUrl>

   <devicePlatform>ios</devicePlatform>

   <deviceType>phone</deviceType>

   <privateApp>false</privateApp>

   <version>0.0.0.0</version>

  </mobileAppConfig>

```


### Metadata Types MobileSecurityAssignment

```
   < . mobileStartUrl>https://www.salesforce.com</mobileStartUrl>

   </ConnectedApp>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

### MobileSecurityAssignment

Represents the assignment of mobile app security policies to a profile. The policies apply to the Salesforce mobile app with Enhanced
Mobile App Security enabled.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### MobileSecurityAssignment components have the suffix .mobileSecurityAssignment and are stored in the

`mobileSecurityAssignments` folder.

Version

### MobileSecurityAssignment components are available in API version 54.0 and later.

Special Access Rules

The Enhanced Mobile App Security add-on subscription and the Enforce Enhanced Mobile App Security user permission are required
to use this metadata type.

Fields

**Field Name** **Description**

```
connectedApplication

```

**Field Type**
string

**Description**
The name of the connected app that’s associated with the mobile security policies
assignment.


Metadata Types MobileSecurityAssignment

**Field Name** **Description**

```
isProtected

masterLabel

profile

```

**Field Type**
boolean

**Description**
An auto-generated value that doesn’t impact the behavior of the metadata type. The
default is `false` .

**Field Type**
string

**Description**

Required. A user-friendly name for MobileSecurityAssignment, which is defined when
the MobileSecurityAssignment component is created.

**Field Type**
string

**Description**
The profile that the mobile security policies are assigned to.

Declarative Metadata Sample Definition

The following is an example of a MobileSecurityAssignment component.

```
<?xml version="1.0" encoding="UTF-8"?>

<MobileSecurityAssignment xmlns="http://soap.sforce.com/2006/04/metadata">

   <connectedApplication>MyMobileConnectedApp</connectedApplication>

   <isProtected>false</isProtected>

   <masterLabel>MyMobileSecurityAssignment</masterLabel>

   <profile>admin</profile>

</MobileSecurityAssignment>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>*</members>

     <name>MobileSecurityAssignment</name>

   </types>

   <version>61.0</version>

</Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types MobileSecurityPolicy MobileSecurityPolicy

Represents a mobile app security policy on the Salesforce mobile app with Enhanced Mobile App Security enabled. For a full description
[of each policy, see Enable and Configure Mobile App Security Policies.](https://help.salesforce.com/s/articleView?id=xcloud.mobile_security_mam_setup_ui.htm&type=5&language=en_US)

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### MobileSecurityPolicy components have the suffix .mobileSecurityPolicy and are stored in the mobileSecurityPolicies

folder.

Version

### MobileSecurityPolicy components are available in API version 53.0 and later.

Special Access Rules

The Enhanced Mobile App Security add-on subscription and the Enforce Enhanced Mobile App Security user permission are required
to use this metadata type.

Fields

**Field Name** **Description**

```
effectiveDate

isEnabled

isProtected

```

**Field Type**
dateTime

**Description**
The date that a mobile security policy is enforced.

**Field Type**
boolean

**Description**

Required. Indicates whether the mobile security policy is enabled. The default value
is `false`, which means that the policy is disabled.

**Field Type**
boolean


Metadata Types MobileSecurityPolicy

**Field Name** **Description**

**Description**
An auto-generated value that doesn’t impact the behavior of the metadata type. The
default value is `false` .

```
masterLabel

mobilePlatform

mobileSecurityAssignment

ruleValue

ruleValueType

severityLevel

```

**Field Type**
string

**Description**

Required. A user-friendly name for MobileSecurityPolicy, which is defined when the
MobileSecurityPolicy component is created.

**Field Type**
MobileSecurityMobilePlatform (enumeration of type string)

**Description**
The mobile operating system of the mobile security policy.

Values are:

**•** `Android`

**•** `iOS`

**Field Type**
string

**Description**
The name of the mobile security assignment associated with the mobile security policy.
See MobileSecurityAssignment on page 1583.

**Field Type**
string

**Description**

Required. The value of the mobile security policy rule.

**Field Type**
MobileSecurityPolicyRuleValueType (enumeration of type string)

**Description**

Required. The type of mobile security policy rule.

Values are:

**•** `Boolean`

**•** `Text`

**•** `TextList`

**Field Type**
MobileSecurityPolicySeverityLevel (enumeration of type string)


Metadata Types MobileSecurityPolicy

**Field Name** **Description**

**Description**

Required. The severity level of a mobile security policy.

Values are:

**•** `Critical`                     - Wipes app data and logs user out

**•** `Error` —Blocks access to the app until the issue is resolved, but doesn’t log user
out

**•** `Info`                     - Blocks prohibited action or logs user action and informs user

**•** `Warn` —Notifies the user of the violation and recommends how to resolve, but
user is able to continue using the app

```
type

```

**Field Type**
MobileSecurityPolicyType (enumeration of type string)

**Description**

Required. The type of mobile security policy.

Values are:

**•** `AllowedDeviceList`

**•** `Block3dTouch`

**•** `BlockCalendar`

**•** `BlockCamera`

**•** `BlockContacts`

**•** `BlockCustomKeyboard`

**•** `BlockFileBackup`

**•** `BlockMicrophone`

**•** `BlockOsSharing`

**•** `BlockedDeviceList`

**•** `BrowserUriScheme`

**•** `CheckBiometric`

**•** `DevicePasscode`

**•** `DisableUrlCaching`

**•** `JailbrokenDevice`

**•** `LogCertPin`

**•** `LogEmail`

**•** `LogPhonecall`

**•** `LogPolicyResult`

**•** `LogScreenshot`

**•** `LogTextmessage`

**•** `LogoutAfterRestart`

**•** `LogoutOnBiometricChange`


Metadata Types MobileSecurityPolicy

**Field Name** **Description**

**•** `MalwareDetection`

**•** `ManInMiddle`

**•** `MaxOffline`

**•** `MaximumAppVersion`

**•** `MaximumOsVersion`

**•** `MinimumAppVersion`

**•** `MinimumOsVersion`

**•** `MinimumSecurityPatchVersion`

**•** `MininumAppVersion`

**•** `PhonecallUriScheme`

**•** `Screenshot`

Declarative Metadata Sample Definition

The following is an example of a MobileSecurityPolicy component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <MobileSecurityPolicy xmlns="http://soap.sforce.com/2006/04/metadata">

      <effectiveDate>2022-08-09T22:04:56.000Z</effectiveDate>

      <isEnabled>true</isEnabled>

      <isProtected>false</isProtected>

      <masterLabel>MyMobileSecurityPolicy</masterLabel>

      <mobileSecurityAssignment>MyMobileSecurityAssignment</mobileSecurityAssignment>

      <ruleValue>true</ruleValue>

      <ruleValueType>Boolean</ruleValueType>

      <severityLevel>info</severityLevel>

      <type>BlockCalendar</type>

      <mobilePlatform>Android</mobilePlatform>

   </MobileSecurityPolicy>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>MobileSecurityPolicy</name>

      </types>

      <version>61.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types MobSecurityCertPinConfig MobSecurityCertPinConfig

Represents the authentication server certificate pin configuration on the Salesforce mobile app with Enhanced Mobile Security.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### MobSecurityCertPinConfig components have the suffix .mobSecurityCertPinConfig and are stored in the

`mobSecurityCertPinConfigs` folder.

Version

### MobSecurityCertPinConfig components are available in API version 53.0 and later.

Special Access Rules

The Enhanced Mobile App Security add-on subscription and the Enforce Enhanced Mobile App Security user permission are required
to use this metadata type.

Fields

**Field Name** **Description**

```
certificateHash

domainName

isEnabled

```

**Field Type**
string

**Description**

Required. The unique identifier for the certificate.

**Field Type**
string

**Description**

Required.

The name of the domain for the server that you want to pin the certificate to. For
example, `https://MyDomainName.my.salesforce.com` .

**Field Type**
boolean


Metadata Types MobSecurityCertPinConfig

**Field Name** **Description**

**Description**

Required. Indicates whether authentication server certificate pinning is enabled. The
default value is `false`, which means that certificate pinning is disabled.

```
isProtected

isSubdomainIncluded

masterLabel

mobilePlatform

mobileSecurityAssignment

severityLevel

```

**Field Type**
boolean

**Description**
An auto-generated value that doesn’t impact the behavior of the metadata type. The
default value is `false` .

**Field Type**
boolean

**Description**

Required. Indicates whether subdomains use the same certificate pinning configuration
as the specified `domainName` . The default value is `false` .

**Field Type**
string

**Description**

Required. A user-friendly name for MobSecurityCertPinConfig, which is defined when
the MobSecurityCertPinConfig component is created.

**Field Type**
MobileSecurityMobilePlatform (enumeration of type string)

**Description**
The mobile operating system.

Values are:

**•** `Android`

**•** `iOS`

**Field Type**
string

**Description**
The name of the mobile security assignment associated with the mobile security policy.
See MobileSecurityAssignment on page 1583.

**Field Type**
MobileSecurityPolicySeverityLevel (enumeration of type string)

**Description**

Required. The severity level of the mobile security policy.

Values are:


Metadata Types MobSecurityCertPinConfig

**Field Name** **Description**

**•** `Critical`                     - Wipes app data and logs user out

**•** `Error` —Blocks access to the app until the issue is resolved, but doesn’t log user
out

**•** `Info`                     - Blocks prohibited action or logs user action and informs user

**•** `Warn` —Notifies the user of the violation and recommends how to resolve, but
user is able to continue using the app

```
type

```

**Field Type**
MobileSecurityCertPinType (enumeration of type string)

**Description**

Required. The type of pin.

Values are:

**•** `AuthServer`

**•** `Resource`

Declarative Metadata Sample Definition

The following is an example of a MobSecurityCertPinConfig component.

```
<?xml version="1.0" encoding="UTF-8"?>

<MobileSecurityCertPinConfig xmlns="http://soap.sforce.com/2006/04/metadata">

   <certificateHash>AaBbCcDdEeFfGg</certificateHash>

   <domainName>login.salesforce.com</domainName>

   <isEnabled>true</isEnabled>

   <isProtected>false</isProtected>

   <masterLabel>AuthenticationServerCertificatePinning</masterLabel>

   <mobilePlatform>Android</mobilePlatform>

   <mobileSecurityAssignment>MyMobileSecurityAssignment</mobileSecurityAssignment>

   <severityLevel>info</severityLevel>

   <type>AuthServer</type>

</MobileSecurityCertPinConfig>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>*</members>

     <name>MobileSecurityCertPinConfig</name>

   </types>

   <version>61.0</version>

</Package>

```


### Metadata Types ModerationRule

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### ModerationRule

Represents a rule used in your Experience Cloud site to moderate member-generated content. Each rule specifies the member-generated
content the rule applies to, the criteria to enforce the rule on, and the moderation action to take. Moderation rules help protect your
site from spammers, bots, and offensive or inappropriate content. This type extends the Metadata metadata type and inherits its
`fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Moderation rules created with the Metadata API are more powerful than moderation rules set up in the Experience Management UI. For
example, in the UI you could create a rule that moderates posts and comments. In the Metadata API you could create a rule that moderates
only the Link Name of a Link feed type. Use the Metadata API to express complex moderation rules.

Important: Don’t update moderation rules you create using the Metadata API in the Experience Management UI. If you do, you
overwrite relevant Metadata API fields or the fields are ignored.

Keep the following things in mind when creating moderation rules:

**•** Your org can have up to 30 rules. This limit is per org, not per site. This limit includes both content rules and rate rules.

**•** Each rule can have up to three keyword criteria.

**•** Rules that block content run first, followed by rules to review and approve content, then rules that replace content, and last by rules
that flag content. If two or more rules perform the same action, the oldest rule runs first, based on the date the rule was created.
Rules to replace content don’t run when the content also applies to a review rule—we want community managers to review the
original content.

File Suffix and Directory Location

### ModerationRule components have the suffix .rule and are stored in the moderation directory of the corresponding package

directory. The file name format follows _`site_name`_ `.` _`moderation_rule_developer_name`_ `.rule` .

Version

### ModerationRule components are available in API version 36.0 and later.

Special Access Rules

To view, create, edit, and delete moderation rules, you need the Manage Experiences or Create and Set Up Experiences permission. As
of Spring ’20 and later, only users with permission to edit moderation rules can access this object.


Metadata Types ModerationRule

Fields

**Field Name** **Field Type** **Description**

```
action

```

ModerationRuleAction Required. Indicates the moderation action that you want to take. The
(enumeration of valid values are:
type string)

**•** `Block`

**•** `Review`

**•** `Replace`

**•** `Flag`

**•** `FreezeAndNotify` (Reserved for future use.)

`actionLimit` int Indicates the moderation action limit. Available in API 39.0 and later.

`active` boolean Required. Indicates whether the moderation rule is active ( `true` ) or
inactive ( `false` ).

`description` string A description of the moderation rule.

`entitiesAndFields` ModerateEntityField[] Indicates the types of user-generated content this moderation rule
applies to.

`masterLabel` string Required. Label for the moderation rule.

`notifyLimit` int Indicates the notification limit of the moderation rule. Available in API
39.0 and later.

`userCriteria` string Represents the member criteria to use in moderation rules. Available in
API 39.0 and later.

`userMessage` string The message you want your members to see when their content is
blocked. Use the _`%BLOCKED_KEYWORD%`_ variable to display up to

five blocked words in the user message. If you don’t specify a message,
the member sees the standard message: “You can’t use
_`%BLOCKED_KEYWORD%`_ or other inappropriate words in this site.
Review your content and try again.”

ModeratedEntityField

The fields and entities you want to moderate.

**Field Name** **Field Type** **Description**

`entityName` string

Required. Indicates the types of user-generated content the moderation rule
applies to. Post and comments only apply to content created in groups and
user profiles. All feed types, such as polls and links, are supported.

`fieldName` string Indicates the field the moderation rule applies to.

Note: To moderate feed posts, use `entityName FeedItem` with
`fieldName RawBody` . To moderate feed comments, use


Metadata Types ModerationRule

**Field Name** **Field Type** **Description**

`entityName FeedComment` with `fieldName`
`RawCommentBody` . The `RawBody` and `RawCommentBody`
fields aren’t available in any other API.

`keywordList` KeywordList string Indicates the keyword list that you want to moderate against.

ModerationRuleType

Required. Indicates the type of rule to run on user-generated content.

**Field Name** **Field Type** **Description**

`type` (enumeration of type Required. Indicates the type of rule to run on user-generated content. Valid
string) values are:

**•** Content

**•** Rate

Available in API 39.0 and later.

RateLimitTimePeriod

Required. Indicates the time period that is applied to the rate limit.

**Field Name** **Field Type** **Description**

`timePeriod` (enumeration of type Required. Indicates the time period that is applied to the rate limit. Valid values
string) are:

**•** Short

**•** Medium

Available in API 39.0 and later.

Declarative Metadata Sample Definition

The following is an example of a ModerationRule component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ModerationRule xmlns="http://soap.sforce.com/2006/04/metadata">

     <description>Blocks Bad Word List in posts, comments, Link URLs, titles, and poll

   choices.</description>

     <masterLabel>Blocking Rule</masterLabel>

     <action>Block</action>

     <active>true</active>

     <userMessage>You can't use %BLOCKED_KEYWORD% or other inappropriate words in this site.

    Review your content and try again.</userMessage>

     <!-- Applies the rule to FeedComment.RawCommentBody (an internal only field), if it

   contains words from the keyword list specified -->

```


### Metadata Types MutingPermissionSet

```
     <entitiesAndFields>

      <entityName>FeedComment</entityName>

      <fieldName>RawCommentBody</fieldName>

      <keywordList>site1.badword_list</keywordList>

     </entitiesAndFields>

     <entitiesAndFields>

      <entityName>FeedItem</entityName>

      <fieldName>LinkUrl</fieldName>

      <keywordList>site1.badword_list</keywordList>

     </entitiesAndFields>

     <!-- Applies the rule to FeedItem.RawBody (an internal only field), if it contains words

    from the keyword list specified -->

     <entitiesAndFields>

      <entityName>FeedItem</entityName>

      <fieldName>RawBody</fieldName>

      <keywordList>site1.badword_list</keywordList>

     </entitiesAndFields>

     <entitiesAndFields>

      <entityName>FeedItem</entityName>

      <fieldName>Title</fieldName>

      <keywordList>site1.badword_list</keywordList>

     </entitiesAndFields>

     <entitiesAndFields>

      <entityName>FeedPollChoice</entityName>

      <fieldName>ChoiceBody</fieldName>

      <keywordList>site1.badword_list</keywordList>

     </entitiesAndFields>

   </ModerationRule>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <types>

      <name>ModerationRule</name>

      <members>site1.blocking_rule</members>

     </types>

     <version>36.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### MutingPermissionSet

Represents a set of disabled permissions and is used in conjunction with PermissionSetGroup.

This type extends the PermissionSet metadata type.


Metadata Types MutingPermissionSet

Declarative Metadata File Suffix and Directory Location

Muting permission sets are stored in the `mutingpermissionsets` directory. The file name matches the muting permission set
API name and the extension is `.mutingpermissionset` . For example, a `mutingpermissionsets` with the name
`Finance_Mgmt_MutingPermSet` is stored in
`mutingpermissionsets/Finance_Mgmt_MutingPermSet.mutingpermissionset` .

Version

This object is available in API version 46.0 and later.

Special Access Rules

As of Summer ’20 and later, only users who have one of these permissions can access this type:

**•** View Setup and Configuration

**•** Manage Session Permission Set Activations

**•** Assign Permission Sets

**•** Manage Profiles and Permission Sets

To view the following settings, assignments, and permissions for standard and custom objects in a specified muting permission set, the
View Setup and Configuration permission is required.

**•** Client settings

**•** Field permissions

**•** Layout assignments

**•** Object permissions

**•** Permission dependencies

**•** Permission set tab settings

**•** Permission set group components

**•** Record types

Fields

MutingPermissionSet has the same fields as PermissionSet, plus a single field, `label`, used to name a MutingPermissionSet. Unlike
PermissionSet, settings enabled by MutingPermissionSet are turned off for the permission set group that it’s a component of.

**Field** **Field Type** **Description**

`label` string Required. The name of the muting permission set.


Metadata Types MutingPermissionSet

Declarative Metadata Sample Definition

The following example deploys a MutingPermissionSet used in a Permission Set Group intended for users submitting job applications
for a custom application. The muting permission set has administrative permissions enabled to ensure that they’re muted in the Permission
Set Group.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <MutingPermissionSet xmlns="http://soap.sforce.com/2006/04/metadata">

      <label>Job Apps User Muted</label>

      <description>Mutes any administrative tasks for the Job Apps user</description>

      <hasActivationRequired>false</hasActivationRequired>

      <license>Salesforce</license>

      <applicationVisibilities>

        <application>JobApps__Approval</application>

        <visible>true</visible>

      </applicationVisibilities>

      <classAccesses>

        <apexClass>ApprovalUtility</apexClass>

        <enabled>true</enabled>

      </classAccesses>

      <customPermissions>

        <enabled>true</enabled>

        <name>JobAppApprover</name>

      </customPermissions>

      <fieldPermissions>

        <editable>false</editable>

        <field>Job_Request__c.Salary__c</field>

        <readable>true</readable>

      </fieldPermissions>

      <objectPermissions>

        <allowCreate>true</allowCreate>

        <allowDelete>true</allowDelete>

        <allowEdit>true</allowEdit>

        <allowRead>true</allowRead>

        <customizeSetup>true</customizeSetup>

        <deleteSetup>true</deleteSetup>

        <modifyAllRecords>true</modifyAllRecords>

        <object>Approval_Confirmation__c</object>

        <viewAllRecords>true</viewAllRecords>

        <viewSetup>true</viewSetup>

      </objectPermissions>

      <pageAccesses>

        <apexPage>Job_Approval_Web_Form</apexPage>

        <enabled>true</enabled>

      </pageAccesses>

      <recordTypeVisibilities>

        <recordType>Approval_Confirmation__c.DevManager</recordType>

        <visible>true</visible>

      </recordTypeVisibilities>

      <tabSettings>

        <tab>Approval_Confirmation__c</tab>

        <visibility>Visible</visibility>

      </tabSettings>

   </MutingPermissionSet>

```


### Metadata Types MyDomainDiscoverableLogin

The following is an example package.xml manifest used to retrieve the MutingPermissionSet metadata for an organization.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Job_Apps_User</members>

        <name>PermissionSetGroup</name>

      </types>

      <types>

        <members>Job_Apps_User_Muted</members>

        <name>MutingPermissionSet</name>

      </types>

      <version>49.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

PermissionSet

### MyDomainDiscoverableLogin

Represents the configuration settings when the My Domain login page type is Discovery. Login Discovery provides an identity-first login
experience, where the login page contains the identifier field only. Based on the identifier entered, a handler determines how to
authenticate the user. This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### MyDomainDiscoverableLogin components have the suffix .myDomainDiscoverableLogin in the

`myDomainDiscoverableLogins` folder.

Version

### MyDomainDiscoverableLogin components are available in API version 48.0 and later.

Fields

**Field Name** **Field Type** **Description**

`apexHandler` string Required. The Apex handler class that contains the Discovery
authentication logic.

`executeApexHandlerAs` string The user who is executing the handler. Requires the Manage User
permission.


### Metadata Types NamedCredential

**Field Name** **Field Type** **Description**

`usernameLabel` string The login prompt when the My Domain login page type is Discovery.
This label supports localization with custom labels.

Declarative Metadata Sample Definition

The following is an example of a MyDomainDiscoverableLogin component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <MyDomainDiscoverableLogin xmlns="http://soap.sforce.com/2006/04/metadata">

      <apexHandler>MyDomainDiscLoginHandler</apexHandler>

      <executeApexHandlerAs>executeUser@example.com</executeApexHandlerAs>

      <usernameLabel>Enter your email</usernameLabel>

   </MyDomainDiscoverableLogin>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>MyDomainDiscoverableLogin</name>

      </types>

      <version>48.0</version>

   </Package>

```

Usage

Use this type to access the My Domain Login Discovery Page. This type of login page prompts users to identity themselves with an email
address, phone number, or custom identifier. My Domain Login Discovery performs an interview-based login process, where users are
prompted to provide identity for authentication. For example, users receive a verification code that they enter to complete the login
process.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### NamedCredential

Represents a named credential, which specifies the URL of a callout endpoint and its required authentication parameters in one definition.
A named credential can be specified as an endpoint to simplify the setup of authenticated callouts.

Note: All credentials stored within this entity are encrypted under a framework that is consistent with other encryption frameworks
on the platform. Salesforce encrypts your credentials by auto-creating org-specific keys. Credentials encrypted using the previous
encryption scheme have been migrated to the new framework.


Metadata Types NamedCredential

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

NamedCredential components have the suffix `.namedCredential` and are stored in the `namedCredentials` folder.

Version

NamedCredential components are available in API version 33.0 and later.

Special Access Rules

As of Spring ’20 and later, only users with the View Setup and Configuration permission can access this type.

Fields

**Field Name** **Description**

```
allowMergeFieldsInBody

allowMergeFieldsInHeader

authProvider

```

**Field Type**
boolean

**Description**
Specifies whether Apex code can use merge fields to populate the HTTP request body
with org data when a callout is made. Corresponds to **Allow Merge Fields in HTTP**
**Body** in the user interface. Defaults to `false` .

This field is available in API version 41.0 and later.

**Field Type**
boolean

**Description**
Specifies whether Apex code can use merge fields to populate the HTTP header with
org data when a callout is made. Corresponds to **Allow Merge Fields in HTTP Header**
in the user interface. Defaults to `false` .

This field is available in API version 41.0 and later.

**Field Type**
string

**Description**
The authentication provider that the AuthProvider component represents.

This field is valid only when NamedCredentialType is set to `Legacy` .

**This field is deprecated in API version 56.0.**


Metadata Types NamedCredential

**Field Name** **Description**

```
authTokenEndpointUrl

awsAccessKey

awsAccessSecret

awsRegion

awsService

```

**Field Type**
string

**Description**
The URL where JWTs are exchanged for access tokens.

This field is valid only when NamedCredentialType is set to `Legacy` .

**First available in API version 46.0, this field is deprecated in API version 56.0**
**and later.**

**Field Type**
string

**Description**
First part of the access key used to sign programmatic requests to AWS. Use when
AWS Signature Version 4 is your authentication protocol.

This field is valid only when NamedCredentialType is set to `Legacy` .

**First available in API version 46.0, this field is deprecated in API version 56.0**
**and later.**

**Field Type**
string

**Description**
The second part of the access key used to sign programmatic requests to AWS. Use
when AWS Signature Version 4 is your authentication protocol.

This field is valid only when NamedCredentialType is set to `Legacy` .

**First available in API version 46.0, this field is deprecated in API version 56.0**
**and later.**

**Field Type**
string

**Description**
Specifies which AWS Region the named credential accesses.

This field is valid only when NamedCredentialType is set to `Legacy` .

**First available in API version 46.0, this field is deprecated in API version 56.0**
**and later.**

**Field Type**
string

**Description**
Specifies which AWS resource the named credential accesses.

This field is valid only when NamedCredentialType is set to `Legacy` .

**First available in API version 46.0, this field is deprecated in API version 56.0**
**and later.**


Metadata Types NamedCredential

**Field Name** **Description**

```
calloutStatus

certificate

description

endpoint

generateAuthorizationHeader

jwtAudience

```

**Field Type**
calloutStatus (enumeration of type string)

**Description**
Specifies whether the named credential is enabled for callouts. Valid values are:

**•** `Disabled` : The named credential is disabled for callouts.

**•** `Enabled` : The named credential is enabled for callouts.

This field is available in API version 59.0 and later.

**Field Type**
string

**Description**
If you specify a certificate, your Salesforce org supplies it when establishing each
two-way SSL connection with the external system. The certificate is used for digital
signatures, which verify that requests are coming from your Salesforce org.

This field is valid only when NamedCredentialType is set to `Legacy` .

**This field is deprecated in API version 56.0.**

**Field Type**
string

**Description**
A meaningful description of the named credential.

**Field Type**
string

**Description**
The URL or root URL of the callout endpoint. Corresponds to **URL** in the user interface.

This field is valid only when NamedCredentialType is set to `Legacy` .

**This field is deprecated in API version 56.0.**

**Field Type**
boolean

**Description**
Specifies whether Salesforce generates an authorization header and applies it to each
callout that references the named credential. Corresponds to **Generate Authorization**
**Header** in the user interface. Defaults to `true` .

This field is available in API version 41.0 and later.

**Field Type**
string


Metadata Types NamedCredential

**Field Name** **Description**

**Description**
External service or other allowed recipients for the JWT. Written as JSON, with a quoted
string for a single audience and an array of quoted strings for multiple audiences.
Single audience example: “aud1” Multiple audiences example: [“aud1”, “aud2”, “aud3”].

This field is valid only when NamedCredentialType is set to `Legacy` .

**This field is deprecated in API version 56.0.**

```
jwtFormulaSubject

jwtIssuer

jwtSigningCertificate

jwtTextSubject

```

**Field Type**
string

**Description**
Formula string calculating the Subject of the JWT. API names and constant strings, in
single quotes, can be included. Allows a dynamic Subject unique per user requesting
the token. For example, _`'User='+$User.Id`_ . Use this field when
`principalType` is set to `PerUser` . Corresponds to `Per User Subject`
in the user interface.

This field is valid only when NamedCredentialType is set to `Legacy` .

**First available in API version 46.0, this field is deprecated in API version 56.0**
**and later.**

**Field Type**
string

**Description**
Specify who issued the JWT using a case-sensitive string.

This field is valid only when NamedCredentialType is set to `Legacy` .

**First available in API version 46.0, this field is deprecated in API version 56.0**
**and later.**

**Field Type**
string

**Description**
Certificate verifying the JWT’s authenticity to external sites.

This field is valid only when NamedCredentialType is set to `Legacy` .

**First available in API version 46.0, this field is deprecated in API version 56.0**
**and later.**

**Field Type**
string

**Description**
Static text, without quotes, that specifies the JWT Subject. Use this field when
`principalType` is set to `NamedUser` . Corresponds to `Named Principal`
`Subject` in the user interface.


Metadata Types NamedCredential

**Field Name** **Description**

This field is valid only when NamedCredentialType is set to `Legacy` .

**First available in API version 46.0, this field is deprecated in API version 56.0**
**and later.**

```
jwtValidityPeriodSeconds

label

namedCredentialParameters

namedCredentialType

```

**Field Type**
int

**Description**
Specify the number of seconds that the token is valid.

This field is valid only when NamedCredentialType is set to `Legacy` .

**First available in API version 46.0, this field is deprecated in API version 56.0**
**and later.**

**Field Type**
string

**Description**

Required.

A user-friendly name for the named credential that appears in the Salesforce user
interface, such as in list views.

**Field Type**

NamedCredentialParameter[]

**Description**
Reference to the (one or more) NamedCredentialParameter used to configure a named
credential.

This field is available in API version 56.0 and later.

**Field Type**
NamedCredentialType (enumeration of type string)

**Description**
Specifies the type or behavior of this named credential. Valid values are:

**•** `Legacy` : The named credential is a legacy type, which means that it doesn’t use
the schema introduced in the Winter ‘23 release. Used for backward compatibility.

**•** `PrivateEndpoint` : The named credential sends traffic through a private
connection, bypassing the public internet. If the credential type is
`PrivateEndpoint`, you must specify the value of
`OutboundNetworkConnection` .

**•** `SecuredEndpoint` : The named credential is extensible and uses external
credentials to control authentication and permissions.

**•** `Standard` : Reserved for internal use.

This field is available in API version 56.0 and later.


Metadata Types NamedCredential

**Field Name** **Description**

```
oauthRefreshToken

oauthScope

oauthToken

outboundNetworkConnection

password

```

**Field Type**
string

**Description**
The OAuth refresh token. Used to obtain a new access token for an end user when a
token expires.

This field is valid only when NamedCredentialType is set to `Legacy` .

**This field is deprecated in API version 56.0.**

**Field Type**
string

**Description**
Specifies the scope of permissions to request for the access token. Corresponds to
**Scope** in the user interface.

This field is valid only when NamedCredentialType is set to `Legacy` .

**This field is deprecated in API version 56.0.**

**Field Type**
string

**Description**
The access token that’s issued by your authorization server.

This field is valid only when NamedCredentialType is set to `Legacy` .

**This field is deprecated in API version 56.0.**

**Field Type**
string

**Description**
Specifies the outbound network connection that uses the named credential to send
callouts to AWS.

This field is valid only when NamedCredentialType is set to `Legacy` .

**First available in API version 49.0, this field is deprecated in API version 56.0**
**and later.**

**Field Type**
string

**Description**
The password to be used by your org to access the external system. Ensure that the
credentials have adequate privileges to access the external system. Depending on
how you set up access, you might need to provide the administrator password.

This field is valid only when NamedCredentialType is set to `Legacy` .

**This field is deprecated in API version 56.0.**


Metadata Types NamedCredential

**Field Name** **Description**

```
principalType

protocol

username

```

**Field Type**
ExternalPrincipalType (enumeration of type string)

**Description**
Determines whether you're using one set or multiple sets of credentials to access the
external system. Corresponds to **Identity Type** in the user interface. Values are:

**•** `Anonymous`

**•** `NamedUser`

**•** `PerUser`

This field is valid only when NamedCredentialType is set to `Legacy` .

**This field is deprecated in API version 56.0.**

**Field Type**
AuthenticationProtocol (enumeration of type string)

**Description**
The authentication protocol that’s required to access the external system. Valid values
are:

**•** `AwsSv4`

**•** `Jwt`

**•** `JwtExchange`

**•** `NoAuthentication`

**•** `Oauth`

**•** `Password`

For connections to Amazon Web Services using Signature Version 4, use `AwsSv4` .

For connections using a direct token system, select `Jwt` . If using an intermediary
authorization provider to process JWTs and return access tokens, use `JwtExchange` .

For Simple URL data sources, select `NoAuthentication` .

For cloud-based Files Connect external systems, select `Oauth` . For on-premises
systems, select `Password` .

This field is valid only when NamedCredentialType is set to `Legacy` .

**This field is deprecated in API version 56.0.**

**Field Type**
string

**Description**
The username to be used by your org to access the external system. Ensure that the
credentials have adequate privileges for performing callouts to the external system.
Depending on how you set up access, you might need to provide the administrator
username.

This field is valid only when NamedCredentialType is set to `Legacy` .


Metadata Types NamedCredential

**Field Name** **Description**

**This field is deprecated in API version 56.0.**

NamedCredentialParameter

Represents the parameters that configure a named credential. Named credential parameters are used to configure Named Credential
callouts through a combination of the type, name, and value/lookup fields. Available in API version 56.0 and later.

These parameters are used internally to provide a flexible architecture and are exposed here for packaging reasons.

**Field Name** **Description**

```
certificate

description

externalCredential

globalNamedPrincipalCredential

managedFeatureEnabledCallout

outboundNetworkConnection

```

**Field Type**
string

**Description**
If the value of the `parameterType` field is `ClientCertificate` then this
field references the certificate.

**Field Type**
string

**Description**
A human-readable description of this named credential parameter.

**Field Type**
string

**Description**
If the value of the `parameterType` field is `Authentication`, then this field
references an external credential that in turn references a set of authenticated user
credentials.

**Field Type**
boolean

**Description**
Reserved for internal use.

**Field Type**
boolean

**Description**
Reserved for internal use.

**Field Type**
string


Metadata Types NamedCredential

**Field Name** **Description**

**Description**
The lookup field for the `OutboundNetworkConnection` parameter type. Used
when `namedCredentialType` is `PrivateEndpoint` .

```
parameterName

parameterType

```

**Field Type**
string

**Description**

Required.

The name of the named credential parameter.

**Field Type**
NamedCredentialParamType (enumeration of type string)

**Description**

Required.

The type of the named credential parameter. Valid values are:

**•** `AllowedManagedPackageNamespaces` : Allows managed packages
identified by specified namespaces to use the named credential and make callouts
through it.

**•** `Authentication` : Specifies that this parameter configures authentication
using the credentials specified in the external credential, referenced by the
`externalCredential` field.

**•** `ClientCertificate` : Specifies that this parameter configures a client
certificate, referenced by the `certificate` field.

**•** `ConnectionStatus` : Reserved for internal use.

**•** `CreatedByNamespace` : Reserved for internal use.

**•** `CustomParameter` : Reserved for internal use.

**•** `HttpHeader` : Allows the user to specify custom headers to be added to the
callout at run time. When using `HttpHeader`, the `parameterName` field
must be the header name as a string, and `parameterValue` must be a formula
of a header value that is evaluated at run time.

**•** `ManagedByComponent` : Reserved for internal use.

**•** `ManagedByFeature` : Reserved for internal use.

**•** `OutboundNetworkConnection` : Specifies a lookup to an outbound network
connection. When using this parameter type, the
`outboundNetworkConnection` field is a string representing the lookup.
Used when `namedCredentialType` is `PrivateEndpoint` .

**•** `StandardNamedCredentialType` : Reserved for internal use.

**•** `Url` : Specifies that this parameter configures the URL of the endpoint. Store the
actual URL in the `parameterValue` field.


Metadata Types NamedCredential

**Field Name** **Description**

```
parameterValue

readOnlyNamedCredential

sequenceNumber

systemUserNamedCredential

```

**Field Type**
string

**Description**
If the `parameterType` field describes a literal value, such as `Url`, then the literal
value is stored in this field, such as `https://iam.amazonaws.com/` .

**Field Type**
boolean

**Description**
Reserved for internal use.

**Field Type**
int

**Description**
Used to order `HttpHeader` parameters.

**Field Type**
boolean

**Description**
Reserved for internal use.

Declarative Metadata Sample Definition

The following is an example of a NamedCredential component.

```
<?xml version="1.0" encoding="UTF-8"?>

<NamedCredential xmlns="http://soap.sforce.com/2006/04/metadata">

   <label>SampleNamedCredential</label>

   <namedCredentialType>SecuredEndpoint</namedCredentialType>

   <namedCredentialParameters>

     <description>IAM Endpoint</description>

     <parameterName>DefaultEndpoint</parameterName>

     <parameterType>Url</parameterType>

     <parameterValue>https://iam.amazonaws.com/</parameterValue>

   </namedCredentialParameters>

   <namedCredentialParameters>

     <description>AWS Auth</description>

     <parameterName>DefaultAuth</parameterName>

     <parameterType>Authentication</parameterType>

     <externalCredential>SampleExternalCredential</externalCredential>

   </namedCredentialParameters>

   <namedCredentialParameters>

     <description>Cert</description>

     <parameterName>DefaultCert</parameterName>

     <parameterType>ClientCertificate</parameterType>

     <certificate>MyCertificate</certificate>

```


### Metadata Types NavigationMenu

```
      </namedCredentialParameters>

      <allowMergeFieldsInBody>true</allowMergeFieldsInBody>

      <allowMergeFieldsInHeader>true</allowMergeFieldsInHeader>

      <generateAuthorizationHeader>true</generateAuthorizationHeader>

   </NamedCredential>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>NamedCredential</name>

      </types>

      <version>56.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

SEE ALSO:

ExternalCredential

_Salesforce Help_ [: Named Credentials](https://help.salesforce.com/s/articleView?id=xcloud.named_credentials_about.htm&type=5&language=en_US)

_Named Credentials Developer Guide_ [: Get Started with Named Credentials](https://developer.salesforce.com/docs/platform/named-credentials/guide/get-started.html)

_[Named Credentials Developer Guide](https://developer.salesforce.com/docs/platform/named-credentials/references/named-credentials-reference/nc-api-links.html)_ : Named Credential API Links

_Apex Developer Guide_ [: Invoking Callouts Using Apex](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_callouts.htm)

_Apex Developer Guide_ [: Named Credentials as Callout Endpoints](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_callouts_named_credentials.htm)

### NavigationMenu

Represents the navigation menu in an Experience Builder site. A navigation menu consists of items that users can click to go to other
parts of the site. This type replaces the NavigationLinkSet subtype on Network. NavigationMenu is available in API version 47.0 and later.
This type extends the Metadata metadata type and inherits its `fullName` field.

The Help Center and LWR templates (Build Your Own and Microsites) don’t include generic record pages. So if you create an object or
global action type menu item that links to a Salesforce object, make sure that you also create the corresponding object pages. If you
don't create the associated object pages, end users won't see anything if they click on the menu item.

File Suffix and Directory Location

### NavigationMenu components have the suffix .navigationMenu and are stored in the navigationMenus folder.

Version

### NavigationMenu components are available in API version 47.0 and later.


Metadata Types NavigationMenu

Special Access Rules

The MultipleNavigationMenu permission is required.

Fields

**Field** **Field Type** **Description**

`container` string The name of the navigation menu container.

`containerType` string The container type. The options are Network
or CommunityTemplateDefinition.

`label` string The navigation menu label as it appears in
the Experience Builder UI.

`navigationMenuItem` NavigationMenuItem[]

NavigationMenuItem

A list of menu items in a NavigationMenu.
Use this object to create, delete, or update
menu items in your site’s navigation menu.

Represents a single menu item in the NavigationLinkSet subtype on Network (API version 37.0 to 46.0) or in the NavigationMenu type
(API version 47.0 and later). Use this object to create, delete, or update menu items in your site’s navigation menu.

**Field** **Field Type** **Description**

`defaultListViewId` string

If the value of the `type` field is
`SalesforceObject`, the value is the
ID of the default list view for the object.

`label` string Required. The text that appears in the
navigation menu for this item.

`menuItemBranding` NavigationMenuItemBranding Branding for the navigation menu item.
Available in API version 47.0 and later.

`position` int Required. The location of the menu item in
the navigation menu.

`publiclyAvailable` boolean When set to `true`, gives access to guest
users.

`subMenu` NavigationSubMenu A list of child menu items. This field is
available in API 39.0 and later.

`target` string Required if `type` is `ExternalLink`,
`InternalLink`, or

`SalesforceObject` . If `type` is
`ExternalLink` or `InternalLink`,
the target is the URL that the link points to.
For `ExternalLink`, your entry looks like


Metadata Types NavigationMenu

**Field** **Field Type** **Description**

this: _`https://salesforce.com`_ . For
`InternalLink`, use a relative URL, such
as _`/contactsupport`_ . If `type` is
`MenuLabel` or
`NavigationalTopic`, `target` isn’t
used.

`targetPreference` string

Backed by a picklist that includes
preferences for the target field. Valid values
are:

**•** `None`

**•** `OpenInExternalTab` —Used for
external links to determine whether to
open in an external tab.

`type` string Required. The type of navigation menu item.
Valid values are:

**•** `SalesforceObject` —Available
objects include accounts, cases,
contacts, and custom objects.

**•** `ExternalLink` —Links to a URL
outside of your site. For example,
_`https://salesforce.com`_ .

**•** `InternalLink` —Links to a relative
URL inside your site. For example,
_`/contactsupport`_ .

**•** `MenuLabel` —A parent heading for
your navigation menu. See
NavigationSubMenu for how to nest
items underneath the menu label. This
value is available in API 39.0 and later.

**•** `NavigationalTopic` —A
dropdown list with links to the
navigational topics in your site.

You can’t nest other items of type
`MenuLabel` or
`NavigationalTopic` under
`MenuLabel` .

NavigationMenuItemBranding

Branding for a menu item.


Metadata Types NavigationMenu

**Field** **Field Type** **Description**

`tileImage` string Name of the ContentAsset to use for the
navigation menu item.

NavigationSubMenu

A list of child menu items. Only NavigationMenuItem items of type `MenuLabel` can have items in a NavigationSubMenu. Available
in API 39.0 and later.

**Field** **Field Type** **Description**

`navigationMenuItem` NavigationMenuItem[] A list of menu items in a
NavigationSubMenu. Use

`navigationMenuItem` to create,
delete, or update child items under a parent
heading.

Declarative Metadata Sample Definition

The following is an example of a NavigationMenu component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <NavigationMenu xmlns="http://soap.sforce.com/2006/04/metadata">

      <container>Service</container>

      <containerType>Network</containerType>

      <label>Test Navigation</label>

      <navigationMenuItem>

        <label>Accounts</label>

        <position>1</position>

        <publiclyAvailable>false</publiclyAvailable>

        <target>Account</target>

        <type>SalesforceObject</type>

      </navigationMenuItem>

      <navigationMenuItem>

        <label>External Link</label>

        <menuItemBranding>

           <tileImage>google_image</tileImage>

        </menuItemBranding>

        <position>2</position>

        <publiclyAvailable>false</publiclyAvailable>

        <target>http://google.com</target>

        <targetPreference>OpenExternalLinkInSameTab</targetPreference>

        <type>ExternalLink</type>

      </navigationMenuItem>

      <navigationMenuItem>

        <label>All Objects</label>

        <position>3</position>

        <publiclyAvailable>false</publiclyAvailable>

        <subMenu>

```


### Metadata Types Network

```
           <navigationMenuItem>

             <label>Leads</label>

             <position>0</position>

             <publiclyAvailable>false</publiclyAvailable>

             <target>Account</target>

             <type>SalesforceObject</type>

           </navigationMenuItem>

        </subMenu>

        <type>MenuLabel</type>

      </navigationMenuItem>

   </NavigationMenu>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <types>

      <members>*</members>

      <name>NavigationMenu</name>

     </types>

     <version>47.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### Network

Represents an Experience Cloud site. Salesforce Experience Cloud lets you create branded spaces for your employees, customers, and
partners. You can customize and create experiences, whether they’re communities, sites, or portals, to meet your business needs, then
transition seamlessly between them. If you want to create zones that contain Chatter Answers and Ideas, use the Community (Zone)
component.

This type extends the Metadata metadata type and inherits its `fullName` field.

Declarative Metadata File Suffix and Directory Location

### Network components are stored in the networks directory of the corresponding package directory. The file name matches the site

name, and the extension is `.network` .

Version

This object is available in API version 28.0 and later.


Metadata Types Network

Fields

**Field** **Field Type** **Description**

`allowedExtensions` string Specifies the types of files allowed in your site. This list of
file types lets you control what your members upload and

also prevents spammers from polluting your site with
inappropriate files. Available in API version 36.0 and later.

`allowInternalUserLogin` boolean

Determines whether internal users can log in with their
internal credentials on the site login page. Available in API
version 40.0 and later.

`allowMembersToFlag` boolean Determines whether users in the site can flag posts or
comments as inappropriate. Flagged items are sent to a

moderator for review. Available in API version 29.0 and
later.

`branding` Branding

`caseCommentEmailTemplate` string

`changePasswordTemplate` string

The color scheme, header, and footer used in the site.
Deprecated in API version 41.0 and later. Replaced by the
NetworkBranding type.

Email template used when notifying members when a
case comment has been modified or added to a case.

Lightning email templates aren’t packageable. We
recommend using a Classic email template.

Email template used when notifying a user that their
password has been reset.

Lightning email templates aren’t packageable. We
recommend using a Classic email template.

`chgEmailVerNewTemplate` string Email template used to verify a user’s email address
change. This email is sent to the new email address.

Note: You can't update this template via Metadata
API.

`chgEmailVerOldTemplate` string Email template used to verify a user’s email address
change. This email is sent to the old email address.

Note: You can't update this template via Metadata
API.

`communityRoles` CommunityRoles Identifies users with Customer, Partner, or Employee roles
in a site. Available in API version 41.0 and later.

`description` string Description of the site.

`deviceActEmailTemplate` string The ID of the device activation email template. The
template is used to customize the device activation email


Metadata Types Network

**Field** **Field Type** **Description**

for community users. Available in API version 53.0 and
later.

`disableReputationRecord` boolean When reputation levels are enabled for the site,
`Conversations` determines whether to exclude contributions to records
when counting points toward reputation levels. Available
in API version 41.0 and later.

`emailFooterLogo` string The document name of the logo that appears in the footer
of emails. Available in API version 41.0 and later.

`emailFooterText` string The text that appears in the footer of emails. Available in
API version 41.0 and later.

`emailSenderAddress` string Required. Email address from which emails are sent.

Note: You can't update this field via Metadata
API. Instead, you can edit the Email Address field
on the Emails page of the site's Administration
workspace.

`emailSenderName` string Required. Name from which emails are sent.

`embeddedLoginEnabled` boolean

`enableApexCDNCaching` boolean

`enableCustomVFError` boolean

```
PageOverrides

```

`enableDirectMessages` boolean

Option to place Salesforce login form directly on an
external website. This setting enables users to log in
without being redirected to a separate Salesforce page.

Determines whether public data from @wire calls to Apex
methods is cached for guest users. This setting applies
only to sites using Salesforce's CDN for Digital Experiences.

Determines whether to use custom Visualforce error pages
instead of the default Visualforce error pages. Available in
API version 41.0 and later.

Determines whether site users can send direct messages
to start a private conversation with one or more members.
Available in API version 41.0 and later.

`enableExperienceBundleBasedSnaOverrideEnabled` boolean Determines whether the Builder-based SNA page is used
( `true` ) or not ( `false` ) and overrides the existing SNA

page when an experience is published. Available in API
version 52.0 and later.

`enableGuestChatter` boolean Specifies whether guest users can access public Chatter
groups in the site without logging in.

`enableGuestFileAccess` boolean Determines whether guest users view asset files shared
with the site on publicly accessible pages and login pages.

If public access is enabled in Experience Builder at the
page or site level, this property is automatically enabled.
Available in API version 41.0 and later.


Metadata Types Network

**Field** **Field Type** **Description**

`enableGuestMemberVisibility` boolean

`enableImageOptimizationCDN` boolean

Determines if unauthenticated guest users can see the
authenticated members ( `true` ) or not ( `false` ). Available
in API version 47.0 and later.

Determines whether to optimize cached images for guest
users on all devices when a site uses Salesforce’s CDN for
Digital Experiences. Available in API version 56.0 and later.

`enableInvitation` boolean Determines whether users can invite others to the site.

`enableKnowledgeable` boolean

`enableMemberVisibility` boolean

`enableNicknameDisplay` boolean

Determines if members can see who’s knowledgeable on
topics and endorse people for their knowledge on a topic.
Available in API version 30.0 and later.

Controls user visibility on a per-site basis. If `true`, the
See other members of this site preference is enabled for
the selected site. Available in API version 45.0 and later.

Determines if user nicknames display instead of their first
and last names in most places in the site. Set to `false`
by default. Available in API version 32.0 and later.

`enablePrivateMessages` boolean Determines if members can send and receive private
messages. Available in API version 30.0 and later.

`enableReputation` boolean

Determines if reputation is calculated and displayed for
members. Available in API version 31.0 and later.

If enabled, `reputationLevels` and
`reputationPointsRules` are used. If no

`reputationLevels` or
`reputationPointsRules` are defined in the data
file, the default values are used.

`enableShowAllNetworkSettings` boolean Shows settings that are hidden by default based on how
the site is set up. Available in API version 41.0 and later.

`enableSiteAsContainer` boolean Determines whether the site is an Experience Builder site
( `true` ) or a Salesforce Tabs + Visualforce site ( `false` ).

`enableTalkingAboutStats` boolean Determines whether users see how many people are
discussing a topic. The number of people discussing the

topic appears as the user types the topic and the system
gives topic suggestions. Available in API version 41.0 and
later.

`enableTopicAssignmentRules` boolean Enables the org to use rules to automatically assign topics
to articles in a site. After it’s enabled, admins set up rules

to map topics to Salesforce Knowledge data categories.
This field is available in API version 40.0 and later.

`enableTopicSuggestions` boolean Enables topic suggestions when users write posts.
Available in API version 41.0 and later.


Metadata Types Network

**Field** **Field Type** **Description**

`enableUpDownVote` boolean

Replaces the option to like a question or answer with the
option to upvote or downvote. Available in API version
41.0 and later.

`expFriendlyUrlsAsDefault` boolean Determines whether URL slugs are enabled by default on

**•** Product and Category pages of LWR Commerce stores
(available in API version 58.0 and later)

**•** Custom object pages on enhanced LWR sites
(available in API version 60.0 and later)

**•** Account and contact pages on enhanced LWR sites
(available in API version 61.0 and later)

`feedChannel` string

`forgotPasswordTemplate` string

`gatherCustomerSentimentData` boolean

`lockoutTemplate` string

`logoutUrl` string

Displays the feed of all channel program record or group
interactions, including posts, questions, and attachments.
This field is available in API version 28.0 and later.

Required. The email template used when a user forgets
their password.

Lightning email templates aren’t packageable. We
recommend using a Classic email template.

Gathers data when a customer looks at articles and cases
in sites, for use in the Community 360 feature. This field
is available in API version 40.0 and later.

The email template used to communicate with users when
they get locked out of their org because of too many failed
login attempts. Available in API version 43.0 and later.

Lightning email templates aren’t packageable. We
recommend using a Classic email template.

Specifies the URL that members are redirected to when
they log out from your site. This field is available in API
version 28.0 and later.

`maxFileSizeKb` int Specifies the maximum file size (in KBs) that members can
upload in your site. Available in API version 36.0 and later.

Enter a number between 3072 KB and your org’s
maximum file size. To use the default limit of 2 GB, leave
this field empty.

`navigationLinkSet` NavigationLinkSet Represents the navigation menu in a site. A navigation
menu consists of items that users can click to go to other

parts of the site. This field is available in API versions 37.0
to 46.0. In API version 47.0 and later, use the
NavigationMenu type instead.

`networkAuthApiSettings` NetworkAuthApiSettings The settings that control enablement, access, and security
for the Headless Registration Flow, Headless Forgot


Metadata Types Network

**Field** **Field Type** **Description**

Password Flow, Headless Passwordless Login Flow, and
their associated APIs. Available in API version 60.0 and
later.

`networkMemberGroups` NetworkMemberGroups

The profiles and permission sets that have access to the
site. Users with these profiles or permission sets are
members of the site.

Note: If a Chatter customer (from a customer
group) is assigned a permission set that is also
associated with a site, the Chatter customer isn’t
added to the site.

`networkPageOverrides` NetworkPageOverride The settings in the Administration area (in Experience
Management or Experience Workspaces) that control

which page type Change Password, Forgot Password,
Home, and Login each point to. Available in API version
40.0 and later.

`newSenderAddress` string Email address that has been entered as the new value for
`EmailSenderAddress` but hasn’t been verified yet.

After a user has requested to change the sender email
address and has successfully responded to the verification
email, the `NewSenderAddress` value overwrites the
value in `EmailSenderAddress` . This value becomes
the email address from which emails are sent.

`pwdlessRegEmailTemplate` string The email template used when a user registers without a
password. Instead of a password,they use an identity

verification method, such as a verification code or link,
which the user completes to finalize the registration or
login process.

Lightning email templates aren’t packageable. We
recommend using a Classic email template.

`picassoSite` string Name of the site of ChatterNetworkPicasso type that's
linked to the Experience Cloud site.

`recommendationAudience` RecommendationAudience Creates an audience of new members, or can be used to
manage customized lists of audience members to organize

and target recommendations. Available in API version 41.0
and later.

`recommendationDefinition` RecommendationDefinition Represents a custom recommendation to drive
engagement. Targets a specific audience and uses

channels to specify a location for the recommendation.
Available in API version 41.0 and later.

`reputationLevels` ReputationLevelDefinitions The reputation levels assigned to members when they
accrue points by performing certain actions.


Metadata Types Network

**Field** **Field Type** **Description**

`reputationPointsRules` ReputationPointsRules The points members accrue when they perform certain
defined actions.

`selfRegMicroBatchSubErrorEmailTemplate` reference

`selfRegProfile` string

The email template used to communicate with users when
their self-registration request, using micro-batching failed.
Available in API version 54.0 and later.

The profile assigned to users who self-register. This value
is used only if `selfRegistration` is enabled for the
site. Available in API version 29.0 and later.

`selfRegistration` boolean Determines whether self-registration is available for the
site.

`sendWelcomeEmail` boolean Determines whether a welcome email is sent when a new
user is added to the site.

`site` string Required. The CustomSite associated with the Experience
Cloud site.

`siteArchiveStatus` SitesArchiveStatus Specifies whether the site has been archived. Available
values are:

**•** `NotArchived` —The site hasn’t been archived.

**•** `TemporarilyArchived` —The site is archived,
but can be unarchived in the future.

`status` NetworkStatus[] Required. Status of the site. Available values are:

**•** `Live` —The site is online and members can access
it.

**•** `DownForMaintenance` —The site was previously
published but was taken offline. Members with the
Create and Set Up Experiences permission can still
access the setup for offline sites regardless of profile
or membership. Members aren’t able to access offline
sites, but they still appear in the user interface
dropdown as `SiteName (Offline)` .

**•** `UnderConstruction` —The site hasn’t yet been
published. Users with the Create and Set Up
Experiences permission can access sites in this status
if their profile is associated with the site.

After a site is published, it can never be in this status
again.

`tabs` NetworkTabSet Required. The tabs that are available in the site. The user
that created the site selected these tabs.

`urlPathPrefix` string The first part of the path on the site's URL that
distinguishes this site from other sites. For example, if your


Metadata Types Network

**Field** **Field Type** **Description**

site URL is
_`MyDomainName`_ `.my.site.com/partners`, then
`partners` is the `urlPathPrefix` .

`verificationTemplate` string The email template used to communicate with users when
they must verify their identity, for example, when they log

in without a password or from a new device. Available in
API version 44.0 and later.

Lightning email templates aren’t packageable. We
recommend using a Classic email template.

`welcomeTemplate` string

Branding

The email template used when sending welcome emails
to new members.

Lightning email templates aren’t packageable. We
recommend using a Classic email template.

Represents the branding and color scheme applied to the Experience Cloud site. Available in API version 40.0 and earlier. Replaced by
NetworkBranding in API version 41.0 and later.

**Field** **Field Type** **Description**

`loginFooterText` string The text that appears in the footer of the
login page.

`loginLogo` string The logo that appears on the login page for
external users.

`pageFooter` string An image that appears on the footer of the
pages. Must be an .html file.

`pageHeader` string An image that appears on the header of the
pages. Can be an .html, .gif, .jpg, or .png file.

`primaryColor` string The color used for the active tab.

`primaryComplementColor` string Font color used with `primaryColor` .

`quaternaryColor` string The background color for pages.

`quaternaryComplementColor` string Font color used with
`quaternaryColor` .

`secondaryColor` string The color used for the top borders of lists
and tables.

`tertiaryColor` string The background color for section headers
on edit and detail pages.


Metadata Types Network

**Field** **Field Type** **Description**

`tertiaryComplementColor` string Font color used with `tertiaryColor` .

`zeronaryColor` string The background color for the header.

`zeronaryComplementColor` string Font color used with `zeronaryColor` .

CommunityRoles

The labels used to identify users with Customer, Partner, or Employee roles in an Experience Cloud site. Available in API version 41.0 and
later.

**Field** **Field Type** **Description**

`customerUserRole` string The label for the Customer user role.

`employeeUserRole` string The label for the Employee user role.

`partnerUserRole` string The label for the Partner user role.

NavigationLinkSet

Represents the navigation menu in an Experience Cloud site. A navigation menu consists of items that users can click to go to other
parts of the site. Available in API versions 37.0 to 46.0. In API version 47.0, use NavigationMenu instead.

**Field** **Field Type** **Description**

`navigationMenuItem` NavigationMenuItem[]

NavigationMenuItem

A list of menu items in a NavigationLinkSet.
Use this object to create, delete, or update
menu items in your site’s navigation menu.

Represents a single menu item in the NavigationLinkSet subtype (API version 37.0 to 46.0) or in the NavigationMenu type (API version
47.0 and later). Use this subtype to create, delete, or update menu items in your site’s navigation menu.

**Field** **Field Type** **Description**

`defaultListViewId` string

If the value of the `type` field is
`SalesforceObject`, the value is the
ID of the default list view for the object.

`label` string Required. The text that appears in the
navigation menu for this item.

`menuItemBranding` NavigationMenuItemBranding Branding for the navigation menu item.
Available in API version 47.0 and later.

`position` int Required. The location of the menu item in
the navigation menu.


Metadata Types Network

**Field** **Field Type** **Description**

`publiclyAvailable` boolean When set to `true`, gives access to guest
users.

`subMenu` NavigationSubMenu A list of child menu items. This field is
available in API 39.0 and later.

`target` string Required if `type` is `ExternalLink`,
`InternalLink`, or

`SalesforceObject` . If `type` is
`ExternalLink` or `InternalLink`,
the target is the URL that the link points to.
For `ExternalLink`, your entry looks like
this: _`https://salesforce.com`_ . For
`InternalLink`, use a relative URL, such
as _`/contactsupport`_ . If `type` is
`MenuLabel` or
`NavigationalTopic`, `target` isn’t
used.

`targetPreference` string

Backed by a picklist that includes
preferences for the target field. Valid values
are:

**•** `None`

**•** `OpenInExternalTab` —Used for
external links to determine whether to
open in an external tab.

`type` string Required. The type of navigation menu item.
Valid values are:

**•** `SalesforceObject` —Available
objects include accounts, cases,
contacts, and custom objects.

**•** `ExternalLink` —Links to a URL
outside of your site. For example,
_`https://salesforce.com`_ .

**•** `InternalLink` —Links to a relative
URL inside your site. For example,
_`/contactsupport`_ .

**•** `MenuLabel` —A parent heading for
your navigation menu. See
NavigationSubMenu for how to nest
items underneath the menu label. This
value is available in API 39.0 and later.

**•** `NavigationalTopic` —A
dropdown list with links to the
navigational topics in your site.


Metadata Types Network

**Field** **Field Type** **Description**

You can’t nest other items of type
`MenuLabel` or
`NavigationalTopic` under
`MenuLabel` .

NavigationSubMenu

A list of child menu items. Only NavigationMenuItem items of type `MenuLabel` can have items in a NavigationSubMenu. Available
in API 39.0 and later.

**Field** **Field Type** **Description**

`navigationMenuItem` NavigationMenuItem[] A list of menu items in a
NavigationSubMenu. Use

`navigationMenuItem` to create,
delete, or update child items under a parent
heading.

NetworkAuthApiSettings

Represents the settings that control enablement, access, and security for the Headless Registration Flow, Headless Forgot Password
Flow, Headless Passwordless Login Flow, and their associated APIs. Available in API version 60.0 and later.

**Field** **Field** **Details**
**Type**

`doesForgotPasswordRequireAuth` leanb **o** Determines whether authentication is required to access Headless Forgot Password API when
a password reset is requested. If `true`, an access token issued to an internal integration user

in your initial POST request to the `/services/auth/headless/forgot_password`
endpoint is required. The access token must include the `forgot_password` scope.

`doesPasswordLoginRequireAuth` leanb **o** Determines whether reCAPTCHA is required for headless username-password login that uses
the OAuth 2.0 for First-Party Applications draft protocol.

`doesPwdlessLoginRequireAuth` leanb **o** Determines whether authentication is required to access Headless Passwordless Login API
when user information is submitted to Salesforce. If `true`, an access token issued to an internal

integration user is required in your initial POST request to the
`/services/auth/headless/init/passwordless/login` endpoint. The access
token must include the `pwdless_login_api` scope.

`doesRegistrationRequireAuth` leanb **o** Determines whether authentication is required to access Headless Registration API when user
registration information is submitted to Salesforce. If `true`, an access token issued to an

internal integration user in your initial POST request to the
`/services/auth/headless/init/registration` endpoint is required. The
access token must include the `user_registration_api` scope.


Metadata Types Network

**Field** **Field** **Details**
**Type**

`emailTmplsAllowlist` NetworkEAlowst[] **m** lTpa **i** The email template allowlist for the Headless Registration Flow, Headless Passwordless Login **l**

Flow, and Headless Forgot Password Flow. The allowlist defines which email templates can be
used for verification emails sent to end users during these flows.

`headlessDiscoveryExecutionUser` Id An integration user account to run a headless user discovery Apex handler.

`headlessDiscoveryHandler` string An Apex class that implements the `Auth.HeadlessUserDiscoveryHandler`
interface.

`isFirstPartyAppsAllowed` leanb **o** Determines whether the Experience Cloud site can use headless identity flows that use the
OAuth 2.0 for First-Party Applications draft protocol.

`isForgotPwdAllowed` leanb **o** Determines whether the Headless Forgot Password Flow is enabled.

`isForgotPwdEmailTemplateAllowlistingEnabled` leanb **o**

Determines whether email template allowlisting is enabled for the Headless Forgot Password
Flow. If `true`, the `emailtemplate` parameter in the initial request to Headless Forgot
Password API can include only allowlisted email templates.

`isHeadlessUserRegistrationAllowed` leanb **o** Determines whether the Headless Registration Flow is enabled.

`IsPwdlessLoginAllowed` leanb **o** Determines whether the Headless Passwordless Login Flow is enabled ( `true` ) or not ( `false` ).

`isRecaptchaRequiredForgotPwd` leanb **o**

Determines whether a reCAPTCHA token is required to access Headless Forgot Password API
when a password reset is requested. If `true`, a reCAPTCHA token is required in your initial
POST request to the `/services/auth/headless/forgot_password` endpoint.

`isRecaptchaRequiredPwdlessLogin` leanb **o** Determines whether a reCAPTCHA token is required to access Headless Passwordless Login
API when user information is submitted to Salesforce. If `true`, a reCAPTCHA token is required

in your initial POST request to the
`/services/auth/headless/init/passwordless/login` endpoint.

`isRecaptchaRequiredRgstr` leanb **o** Determines whether a reCAPTCHA token is required to access Headless Registration API when
user registration information is submitted to Salesforce. If `true`, a reCAPTCHA token is required

in your initial POST request to the
`/services/auth/headless/init/registration` endpoint.

`isUniversalClientRgstrAllowed` leanb **o** Determines whether self-registration and passwordless login via Universal Registration API are
enabled.

`isUserDisambiguationAllowedForgotPwd` leanb **o** Determines whether the Headless Forgot Password Flow uses the headless user discovery
Apex handler that's specified in the `HeadlessDiscoveryHandlerId` field. The handler

enables users to reset their password with an identifier other than their username, such as an
email address, phone number, or order number.

`isUserDisambiguationAllowedUsernamePwd` leanb **o** Determines whether headless login flows use the headless user discovery Apex handler that's
specified in the `HeadlessDiscoveryHandlerId` field. The handler enables users to

log in with an identifier other than their username, such as an email address, phone number,
or order number. This field applies to the Authorization Code and Credentials Flow and the
OAuth 2.0 for First-Party Applications login flow.

`maxPasswordResetAttempts` int The maximum number of password reset attempts you allow for the Headless Forgot Password
Flow before the user must request a new one-time password (OTP).


Metadata Types Network

**Field** **Field** **Details**
**Type**

`recaptchaScoreThreshold` double

The lowest reCAPTCHA score that is accepted before rejecting a request to access Headless
Identity APIs. This value must be between 0.5 and 1. Scores closer to 0.5 are more likely to be
bots, while scores closer to 1 are more likely to be valid users.

You must set a score threshold if `doesForgotPasswordRequireAuth` or
`doesRegistrationRequireAuth` fields are set to `true` . reCAPTCHA settings apply
to both the Headless Registration Flow and the Headless Forgot Password Flow.

Google issues a reCAPTCHA score only for reCAPTCHA v3 implementations. If you implement
reCAPTCHA v2, this field doesn’t apply.

`recaptchaSecretKey` string The reCAPTCHA secret key from your API key pair. You get the API key pair from Google when
you set up reCAPTCHA. The secret key helps your app securely communicate with Google. You

must enter a secret key if `doesForgotPasswordRequireAuth` or
`doesRegistrationRequireAuth` are set to `true` . reCAPTCHA settings apply to all
headless identity flows for which reCAPTCHA is enabled.

`registrationExecutionUser` string The user who runs your headless registration Apex handler.

`registrationHandler` string The headless registration Apex handler.

`registrationUserDefaultProfile` string The default profile that gets assigned to new users when they register.

NetworkEmailTmplAllowlist

Represents the allowlist for one-time password (OTP) email templates sent to end users during the Headless Registration Flow, Headless
Passwordless Login Flow, and Headless Forgot Password Flow. Available in API version 60.0 and later.

**Field** **Field Type** **Description**

`emailTemplate` string Required. The email templates that can be
sent to users during the headless

authorization flows for registration,
passwordless login, and forgot password.
You can list multiple templates. When your
app sends its initial request to Headless
Registration API or Headless Passwordless
Login API, the `emailtemplate`
parameter can include only an email
template ID from the allowlist. For Headless
Forgot Password API, it works the same way,
but only if the

```
                                   isForgotPwdEmailTemplateAllowlistingEnabled
```

field on the

```
                                   NetworkAuthApiSettings
```

metadata type is `true` .


Metadata Types Network

NetworkMemberGroup

Represents the profiles and permission sets that are assigned to the Experience Cloud site. Users with one of the profiles or permission
sets are members of the site, unless the user is a Chatter customer (from a customer group).

**Field** **Field Type** **Description**

`permissionSet` string A permission set that is assigned to the site.

Note: If a Chatter customer (from a
customer group) is assigned a
permission set that is also associated
with a site, the Chatter customer isn’t
added to the site.

`profile` string A profile that is part of the site.

NetworkPageOverride

Represents settings in the Administration area (in Experience Management or Experience Workspaces) that control which page type
the Change Password, Forgot Password, Home, and Login pages each point to.

Note: Assigned Visualforce page overrides are specified and deployed via the corresponding CustomSite metadata field.

**Field** **Field Type** **Description**

`changePasswordPageOverrideSetting` NetworkPageOverrideSetting (enumeration
of type string)

`forgotPasswordPageOverrideSetting` NetworkPageOverrideSetting (enumeration
of type string)


Required. Specifies the page type that the
Change Password page setting applies to.
The valid values are:

**•** `Configurable` —a configurable
self-registration page

**•** `Designer` —an Experience Builder
page

**•** `Standard` —the default page

**•** `VisualForce` —a Visualforce page

Required. Specifies the page type that the
Forgot Password page setting applies to.
The valid values are:

**•** `Configurable` —a configurable
self-registration page

**•** `Designer` —an Experience Builder
page

**•** `Standard` —the default page

**•** `VisualForce` —a Visualforce page

Metadata Types Network

**Field** **Field Type** **Description**

`homePageOverrideSetting` NetworkPageOverrideSetting (enumeration
of type string)

`loginPageOverrideSetting` NetworkPageOverrideSetting (enumeration
of type string)

`selfRegProfilePageOverrideSetting` NetworkPageOverrideSetting (enumeration
of type string)

RecommendationAudience

Required. Specifies the page type that the
Experience Home page setting applies to.
The valid values are:

**•** `Configurable` —a configurable
self-registration page

**•** `Designer` —an Experience Builder
page

**•** `Standard` —the default page

**•** `VisualForce` —a Visualforce page

Required. Specifies the page type that the
Login page setting applies to. The valid
values are:

**•** `Configurable` —a configurable
self-registration page

**•** `Designer` —an Experience Builder
page

**•** `Standard` —the default page

**•** `VisualForce` —a Visualforce page

Note: To configure an Experience
Builder page for your Home and
Login pages, make sure you publish
your site. Unpublished pages show
up as Default Page from the
dropdown menu in Admin settings.

Required. Specifies the page type that the
Self Registration page setting applies to. The
valid values are:

**•** `Configurable` —a configurable
self-registration page

**•** `Designer` —an Experience Builder
page

**•** `Standard` —the default page

**•** `VisualForce` —a Visualforce page

Creates an audience of new Experience Cloud site members, or can be used to manage customized lists of audience members to organize
and target recommendations. Available in API version 41.0 and later.


Metadata Types Network

**Field** **Field Type** **Description**

`recommendationAudienceDetails` RecommendationAudienceDetail The specific details of an audience for
recommendations.

RecommendationAudienceDetail

The specific details of an audience for recommendations. Available in API version 41.0 and later.

**Field** **Field Type** **Description**

`audienceCriteriaType` AudienceCriteriaType (enumeration of type The criteria for the recommendation
string) audience type. Values are:

**•** `CustomList`

**•** `MaxDaysInCommunity`

`audienceCriteriaValue` string

For new member criteria, the maximum
number of days since a user became a
member. Null in case of custom list criteria.

`setupName` string Name of the recommendation audience.

RecommendationDefinition

Represents a list of custom recommendations to drive engagement for an Experience Cloud site. Available in API version 41.0 and later.

**Field** **Field Type** **Description**

`recommendationDefinitionDetails` RecommendationDefinitionDetail[] A list of custom recommendations and their
details.

RecommendationDefinitionDetail

The specific details of a custom recommendation. Available in API version 41.0 and later.

**Field** **Field Type** **Description**

`actionUrl` string The URL for the button that lets users act on
the recommendation.

`description` string An explanation of the recommendation that
suggests what users can do.

`linkText` string The text label for the button.

`scheduledRecommendations` ScheduledRecommendation A list of scheduled recommendations.

`setupName` string The name of the recommendation, which
appears in Setup.


Metadata Types Network

**Field** **Field Type** **Description**

`title` string The title of the recommendation.

ReputationBranding

Branding for the reputation level.

**Field** **Field Type** **Description**

`smallImage` string Custom image associated with a reputation
level. Use files with these extensions: .jpeg,

.png, or .gif. Images are stored as
documents. If not specified, the default
reputation level image is used. Available in
API version 32.0 and later.

ReputationLevelDefinitions

Represents reputation levels members can achieve by performing certain defined actions in an Experience Cloud site.

**Field** **Field Type** **Description**

`level` ReputationLevel[] Represents reputation levels.

ReputationLevel

Represents the name and lower value of the reputation level. The application calculates the upper value.

**Field** **Field Type** **Description**

`branding` ReputationBranding[]

`label` string


Represents any branding associated with
the reputation level, specifically, the custom
image for the reputation level.

This field is optional. If not specified, the
default reputation level image is used.
Available in API version 32.0 and later.

Name of the reputation level.

This field is optional. If not specified, one of
the 10 defaults is used.

**•** Level 1

**•** Level 2

**•** Level 3

**•** Level 4

**•** Level 5

Metadata Types Network

**Field** **Field Type** **Description**

**•** Level 6

**•** Level 7

**•** Level 8

**•** Level 9

**•** Level 10

`lowerThreshold` double Required. The lower value in the range for
this reputation level. For example, if this

reputation level is for points 1–50, 1 is the
`lowerThreshold` .

ReputationPointsRules

Represents points rules in an Experience Cloud site’s point system.

**Field** **Field Type** **Description**

`pointsRule` ReputationPointsRule[] Represents events and their associated
points.

ReputationPointsRule

Represents the event and associated point value for a points rule. When a user acts, they accrue the associated points.

**Field** **Field Type** **Description**

`eventType` string Required. The type of event a member has to perform to get points.
The available values are:

**•** `FeedItemWriteAPost`

**•** `FeedItemWriteAComment`

**•** `FeedItemReceiveAComment`

**•** `FeedItemLikeSomething`

**•** `FeedItemReceiveALike`

**•** `FeedItemMentionSomeone`

**•** `FeedItemSomeoneMentionsYou`

**•** `FeedItemShareAPost`

**•** `FeedItemSomeoneSharesYourPost`

**•** `FeedItemPostAQuestion`

**•** `FeedItemAnswerAQuestion`

**•** `FeedItemReceiveAnAnswer`

**•** `FeedItemMarkAnswerAsBest`

**•** `FeedItemYourAnswerMarkedBest`


Metadata Types Network

**Field** **Field Type** **Description**

**•** `FeedItemEndorseSomeoneForKnowledgeOnATopic`

**•** `FeedItemEndorsedForKnowledgeOnATopic`

`points` int Required. The number of points a member gets for performing the
event. The default number of points per event is:

**•** FeedItemWriteAPost +1

**•** FeedItemWriteAComment: +1

**•** FeedItemReceiveAComment: +5

**•** FeedItemLikeSomething: +1

**•** FeedItemReceiveALike: +5

**•** FeedItemMentionSomeone: +1

**•** FeedItemSomeoneMentionsYou: +5

**•** FeedItemShareAPost: +1

**•** FeedItemSomeoneSharesYourPost: +5

**•** FeedItemPostAQuestion: +1

**•** FeedItemAnswerAQuestion: +5

**•** FeedItemReceiveAnAnswer: +5

**•** FeedItemMarkAnswerAsBest: +5

**•** FeedItemYourAnswerMarkedBest: +20

**•** FeedItemEndorseSomeoneForKnowledgeOnATopic: +5

**•** FeedItemEndorsedForKnowledgeOnATopic: +20

ScheduledRecommendation

Represents a list of scheduled recommendations. Available in API version 41.0 and later.

**Field** **Field Type** **Description**

`scheduledRecommendationDetails` ScheduledRecommendationDetail[] A list of scheduled recommendations.

ScheduledRecommendationDetail

The specific details of a scheduled recommendation. Available in API version 41.0 and later.

**Field** **Field Type** **Description**

`channel` RecommendationChannel (enumeration of
type string)


A way to group recommendations together
to determine where they show up in the
site. The valid values are:

**•** `DefaultChannel` —The default
recommendation channel.

Metadata Types Network

**Field** **Field Type** **Description**

Recommendations in the default
channel appear in predefined locations,
such as directly in the feed in Salesforce
mobile web and on the Home and
Question Detail pages of the Customer
Service (Napili) template.

**•** `CustomChannel1` —A custom
recommendation channel. Choose
where you want recommendations to
appear by adding the
Recommendations Carousel component
to the page in Experience Builder.

**•** `CustomChannel2` —A custom
recommendation channel.

**•** `CustomChannel3` —A custom
recommendation channel.

**•** `CustomChannel4` —A custom
recommendation channel.

**•** `CustomChannel5` —A custom
recommendation channel.

`enabled` boolean

`rank` int

Indicates whether scheduling is enabled. If
`true`, the recommendation is enabled and
appears in sites.

If `false`, recommendations in feeds in
Salesforce mobile web aren’t removed, but

no new recommendations appear. In sites,
disabled recommendations no longer
appear.

The rank of the recommendation within the
channel, which determines the order in
which it’s displayed.

The scheduled recommendation is inserted
into the position specified by the rank. The

rank of all the scheduled recommendations
after it is pushed down. If the specified rank
is larger than the size of the list, the
scheduled recommendation is put at the
end of the list.

If a rank isn’t specified, the scheduled
recommendation is put at the end of the
list.


Metadata Types Network

**Field** **Field Type** **Description**

`recommendationAudience` string The name of the audience for this scheduled
recommendation.

NetworkTabSet

**Field** **Field Type** **Description**

`customTab` string Custom tab that is part of the site.

`defaultTab` string The Home tab for the site. When members
log in, this tab is the first page they see.

`standardTab` string Standard tab that is part of the site.

Declarative Metadata Sample Definition

A sample XML definition of a network.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Network xmlns="http://soap.sforce.com/2006/04/metadata">

      <allowMembersToFlag>true</allowMembersToFlag>

   <changePasswordTemplate>unfiled$public/CommunityChangePasswordEmailTemplate</changePasswordTemplate>

      <description>Metadata Community</description>

      <emailSenderAddress>admin@networkMetadata.com</emailSenderAddress>

      <emailSenderName>Admin User</emailSenderName>

      <enableInvitation>false</enableInvitation>

      <enableKnowledgeable>true</enableKnowledgeable>

      <enableNicknameDisplay>false</enableNicknameDisplay>

      <enablePrivateMessages>true</enablePrivateMessages>

      <enableReputation>true</enableReputation>

      <enableUpDownVote>true</enableUpDownVote>

   <forgotPasswordTemplate>unfiled$public/CommunityForgotPasswordEmailTemplate</forgotPasswordTemplate>

      <networkMemberGroups>

        <permissionSet>Admin</permissionSet>

        <permissionSet>Standard</permissionSet>

        <permissionSet>ReadOnly</permissionSet>

        <profile>Admin</profile>

        <profile>Standard</profile>

        <profile>ReadOnly</profile>

      </networkMemberGroups>

      <recommendationDefinition>

        <recommendationDefinitionDetails>

           <actionUrl>https://www.apple.com/iphone</actionUrl>

           <description>Better specs and high performance for iPhones</description>

           <linkText>iPhone 7</linkText>

```


Metadata Types Network

```
           <scheduledRecommendations>

             <scheduledRecommendationDetails>

               <channel>DefaultChannel</channel>

               <enabled>false</enabled>

               <rank>1</rank>

               <recommendationAudience>New Member Audience</recommendationAudience>

             </scheduledRecommendationDetails>

           </scheduledRecommendations>

           <setupName>Apple iPhone</setupName>

           <title>iPhone7</title>

        </recommendationDefinitionDetails>

        <recommendationDefinitionDetails>

           <actionUrl>https://www.bose.com/qc35</actionUrl>

           <description>New Amazing Noise cancellation Headphones</description>

           <linkText>Bose QC35</linkText>

           <scheduledRecommendations>

             <scheduledRecommendationDetails>

               <channel>DefaultChannel</channel>

               <enabled>true</enabled>

               <rank>2</rank>

               <recommendationAudience>Custom Audience</recommendationAudience>

             </scheduledRecommendationDetails>

           </scheduledRecommendations>

           <setupName>Bose Headphones</setupName>

           <title>Bose QC35</title>

        </recommendationDefinitionDetails>

      </recommendationDefinition>

      <reputationLevels>

        <level>

           <branding>

             <smallImage>communities_shared

   _document_folder/replevel_beginner.png</smallImage>

           </branding>

           <label>Beginner</label>

           <lowerThreshold>0</lowerThreshold>

        </level>

        <level>

           <branding>

             <smallImage>communities_shared

   _document_folder/replevel_apprentice.png</smallImage>

           </branding>

           <label>Apprentice</label>

           <lowerThreshold>51</lowerThreshold>

        </level>

        <level>

           <branding>

             <smallImage>communities_shared

   _document_folder/replevel_gettingthere.png</smallImage>

           </branding>

           <label>Getting There</label>

           <lowerThreshold>101</lowerThreshold>

        </level>

        <level>

           <branding>

```


Metadata Types Network

```
             <smallImage>communities_shared

   _document_folder/replevel_skilled.png</smallImage>

           </branding>

           <label>Skilled</label>

           <lowerThreshold>151</lowerThreshold>

        </level>

        <level>

           <branding>

             <smallImage>communities_shared

   _document_folder/replevel_expert.png</smallImage>

           </branding>

           <label>Expert</label>

           <lowerThreshold>201</lowerThreshold>

        </level>

        <level>

           <branding>

             <smallImage>communities_shared

   _document_folder/replevel_mentor.png</smallImage>

           </branding>

           <label>Mentor</label>

           <lowerThreshold>251</lowerThreshold>

        </level>

        <level>

           <branding>

             <smallImage>communities_shared

   _document_folder/replevel_guru.png</smallImage>

           </branding>

           <label>Guru</label>

           <lowerThreshold>301</lowerThreshold>

        </level>

      </reputationLevels>

      <reputationPointsRules>

        <pointsRule>

           <eventType>FeedItemWriteAPost</eventType>

           <points>5</points>

        </pointsRule>

        <pointsRule>

           <eventType>FeedItemWriteAComment</eventType>

           <points>3</points>

        </pointsRule>

        <pointsRule>

           <eventType>FeedItemReceiveAComment</eventType>

           <points>10</points>

        </pointsRule>

        <pointsRule>

           <eventType>FeedItemLikeSomething</eventType>

           <points>3</points>

        </pointsRule>

        <pointsRule>

           <eventType>FeedItemReceiveALike</eventType>

           <points>5</points>

        </pointsRule>

        <pointsRule>

           <eventType>FeedItemMentionSomeone</eventType>

```


Metadata Types Network

```
           <points>5</points>

        </pointsRule>

        <pointsRule>

           <eventType>FeedItemSomeoneMentionsYou</eventType>

           <points>10</points>

        </pointsRule>

        <pointsRule>

           <eventType>FeedItemShareAPost</eventType>

           <points>5</points>

        </pointsRule>

        <pointsRule>

           <eventType>FeedItemSomeoneSharesYourPost</eventType>

           <points>10</points>

        </pointsRule>

      </reputationPointsRules>

      <selfRegistration>false</selfRegistration>

      <sendWelcomeEmail>true</sendWelcomeEmail>

      <site>Network_11</site>

      <status>UnderConstruction</status>

      <tabs>

        <defaultTab>Chatter</defaultTab>

        <standardTab>Chatter</standardTab>

        <standardTab>Account</standardTab>

        <standardTab>Campaign</standardTab>

        <standardTab>Case</standardTab>

        <standardTab>Console</standardTab>

        <standardTab>Contact</standardTab>

        <standardTab>Contract</standardTab>

        <standardTab>Dashboard</standardTab>

        <standardTab>JigsawSearch</standardTab>

        <standardTab>File</standardTab>

        <standardTab>CollaborationGroup</standardTab>

        <standardTab>home</standardTab>

        <standardTab>Idea</standardTab>

        <standardTab>Lead</standardTab>

        <standardTab>Opportunity</standardTab>

        <standardTab>Product2</standardTab>

        <standardTab>UserProfile</standardTab>

        <standardTab>report</standardTab>

        <standardTab>Solution</standardTab>

      </tabs>

      <urlPathPrefix>network1</urlPathPrefix>

      <welcomeTemplate>unfiled$public/CommunityWelcomeEmailTemplate</welcomeTemplate>

   </Network>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

Community (Zone)


### Metadata Types NetworkBranding NetworkBranding

Represents the branding and color scheme applied to the login pages of an Experience Cloud site. (Experience Cloud sites are represented
by the Network component.)

This type extends the MetadataWithContent type and inherits its `content` and `fullName` fields.

Note: For branding properties that apply to Experience Builder sites, see BrandingSet.

Declarative Metadata File Suffix and Directory Location

### NetworkBranding components have the suffix .networkBranding and are stored in the networkBranding folder.

Version

This object is available in API version 41.0 and later. It replaces the Branding subtype in the Network component.

Fields

**Field** **Field Type** **Description**

`loginBackgroundImageUrl` string The path to the image URL that appears as
the background on the Experience Cloud

site’s login page. This URL can be fixed,
dynamic, or an uploaded image. A dynamic
URL contains the experience ID parameter,
`{expid}`, and is resolved dynamically at
runtime.

`loginFooterText` string The text that appears in the footer of the
Experience Cloud site login page.

`loginLogo` string The logo that appears on the Experience
Cloud site login page for external users.

`loginLogoName` string

The name of the logo that appears on the
Experience Cloud site login page for external
users.

`loginPrimaryColor` string The background color of the Login button.
Available in API version 42.0 and later.

`loginQuaternaryColor` string The background color for the Experience
Cloud site’s login page.

`loginRightFrameUrl` string The path to the content of the right frame
of the Experience Cloud site login page. This

URL can be either fixed or dynamic. A
dynamic URL contains the experience ID
parameter, `{expid}` . If the URL contains


Metadata Types NetworkBranding

**Field** **Field Type** **Description**

`{expid}`, the URL is resolved dynamically
at runtime depending on the parameter's
value.

`network` string The name of the Experience Cloud site
associated with the branding.

`pageFooter` string

`pageHeader` string

An image that appears on the footer of the
Experience Cloud site pages. Must be an
.html file.

An image that appears on the header of the
Experience Cloud site pages. Can be an
.html, .gif, .jpg, or .png file.

`primaryColor` string Required. The color used for the active tab.

`primaryComplementColor` string Required. Font color used with
`primaryColor` .

`quaternaryColor` string Required. The background color for pages
in the Experience Cloud site.

`quaternaryComplementColor` string Required. Font color used with
`quaternaryColor` .

`secondaryColor` string Required. The color used for the top borders
of lists and tables.

`staticLogoImageUrl` string The path to the logo that appears on the
Experience Cloud site’s login page. This URL

can be fixed, dynamic, or an uploaded
image. A dynamic URL contains the
experience ID parameter, `{expid}` . If the
URL contains `{expid}`, the URL is
resolved dynamically at runtime depending
on the parameter's value.

`tertiaryColor` string Required. The background color for section
headers on edit and detail pages.

`tertiaryComplementColor` string Required. Font color used with
`tertiaryColor` .

`zeronaryColor` string Required. The background color for the
header.

`zeronaryComplementColor` string Required. Font color used with
`zeronaryColor` .


### Metadata Types NotificationTypeConfig

Declarative Metadata Sample Definition

A sample XML definition of network branding.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <NetworkBranding xmlns="http://soap.sforce.com/2006/04/metadata">

      <loginFooterText>salesforce.com</loginFooterText>

      <loginLogo>Communities_Shared_Document_Folder/header2_png.png</loginLogo>

      <loginLogoName>header2.png</loginLogoName>

   <loginBackgroundImageUrl>http://identitycms.herokuapp.com/promo-background.jpg</loginBackgroundImageUrl>

      <loginQuaternaryColor>#B1BAC1</loginQuaternaryColor>

      <loginRightFrameUrl>https://www.example.com/test</loginRightFrameUrl>

      <network>Network 1</network>

      <pageFooter>Branding/footer_html.html</pageFooter>

      <pageHeader>Branding/header_Image.jpg</pageHeader>

      <primaryColor>#AF5800</primaryColor>

      <primaryComplementColor>#FFFFFF</primaryComplementColor>

      <quaternaryColor>#286FB8</quaternaryColor>

      <quaternaryComplementColor>#FFFFFF</quaternaryComplementColor>

      <secondaryColor>#000000</secondaryColor>

      <tertiaryColor>#FFFFFF</tertiaryColor>

      <tertiaryComplementColor>#222222</tertiaryComplementColor>

      <zeronaryColor>#0A3764</zeronaryColor>

      <zeronaryComplementColor>#FFFFFF</zeronaryComplementColor>

   </NetworkBranding>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### NotificationTypeConfig

Represents the metadata associated with org-level notification settings for standard and custom notification types. This type extends
the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### NotificationTypeConfig components have the suffix .config and are stored in the notificationTypeConfig folder.

Version

### NotificationTypeConfig components are available in API version 48.0 and later.


Metadata Types NotificationTypeConfig

Fields

**Field Name** **Field Type** **Description**

`notificationTypeSettings` NotificationTypeSettings on An array of delivery settings for an org’s notification types.
page 1641[]

NotificationTypeSettings

Represents the delivery settings for a standard or custom notification type.

**Field Name** **Field Type** **Description**

`notificationType` string
Required. Specifies a notification type’s API name.

For standard notification types, this is the predefined API name of the standard
notification type. For custom notification types, this is the API name of the custom
notification type. If a custom notification type was installed with a managed package,
it includes the namespace prefix.

Retrieve NotificationTypeConfig to see the API names of the notification types available
in your org.

`appSettings` AppSettings on page 1641[] An array of settings for the connected apps supported for a notification type.

`notificationChannels` NotificationChannels on Defines the delivery channels for a notification type.
page 1641

AppSettings

Represents the settings for the connected apps supported for a notification type.

**Field Name** **Field Type** **Description**

`connectedAppName` string

Required. Specifies the API name of a connected app. If a connected app was installed
with a managed package, it includes the namespace prefix.

Retrieve NotificationTypeConfig to see the API names of the connected apps supported
for a notification type.

`enabled` boolean Indicates whether a connected app is enabled ( `true` ) or not ( `false` ) for the
notification type.

NotificationChannels

Represents the settings for the delivery channels for a notification type.

**Field Name** **Field Type** **Description**

`desktopEnabled` boolean Indicates whether desktop notifications are enabled ( `true` ) or not ( `false` ).


Metadata Types NotificationTypeConfig

**Field Name** **Field Type** **Description**

`mobileEnabled` boolean Indicates whether mobile notifications are enabled ( `true` ) or not ( `false` ).

`slackEnabled` boolean Indicates whether Slack notifications are enabled ( `true` ) or not ( `false` ).

Declarative Metadata Sample Definition

The following is an example of a NotificationTypeConfig component.

```
   <NotificationTypeConfig xmlns="http://soap.sforce.com/2006/04/metadata">

      <notificationTypeSettings>

        <notificationType>chatter_mention</notificationType>

        <notificationChannels>

           <desktopEnabled>false</desktopEnabled>

           <mobileEnabled>true</mobileEnabled>

        </notificationChannels>

        <appSettings>

           <connectedAppName>Datawatch</connectedAppName>

           <enabled>false</enabled>

        </appSettings>

           <appSettings>

           <connectedAppName>package2__ConnectedApp2</connectedAppName>

           <enabled>true</enabled>

        </appSettings>

      </notificationTypeSettings>

     <notificationTypeSettings>

        <notificationType>namespace__Custom_Notification</notificationType>

        <notificationChannels>

           <desktopEnabled>true</desktopEnabled>

           <mobileEnabled>true</mobileEnabled>

        </notificationChannels>

        <appSettings>

           <connectedAppName>namespace__Connected_App</connectedAppName>

           <enabled>false</enabled>

        </appSettings>

        <appSettings>

           <connectedAppName>namespace2__ConnectedApp2</connectedAppName>

           <enabled>true</enabled>

        </appSettings>

      </notificationTypeSettings>

   </NotificationTypeConfig>

```

The following is an example of a package manifest used to retrieve all the available notification settings for an organization, using a
wildcard:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>NotificationTypeConfig</name>

      </types>

      <version>48.0</version>

   </Package>

```


### Metadata Types OauthCustomScope

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### OauthCustomScope

Represents a permission defining the protected data that a connected app can access from an external entity when Salesforce is the
OAuth authorization provider. This type extends the Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### OauthCustomScope components have the suffix .oauthcustomscope and are stored in the oauthcustomscopes directory.

Version

OAuth custom scopes are available in API version 46.0 and later.

Special Access Rules

You must have the “Manage Connected Apps” permission to access this object.

Fields

**Field Name** **Field Type** **Description**

Represents the name of the connected app to which the custom scope
is assigned. Available in API version 49.0 and later.

If the connected app is part of a package, include the package’s
namespace prefix with the connected app’s name. Use the following

format: _**`<namespace_prefix>`**_ `__` _**`<connected_app>`**_ . Use two
underscores (_) between the namespace prefix and connected app’s
name.

```
assignedTo

```

### OauthCustomScopeApp

(enumeration of
type string)

`description` string Required. The description of the permission provided to the connected
app by the scope. The custom scope’s description must be unique, can

only include alphanumeric characters, and can be up to 60 characters
long.

You can enter a custom label in place of a description. An advantage of
using a custom label is that you can maintain reusable text in a single
[location and translate the text into multiple languages. See Custom](https://help.salesforce.com/articleView?id=cl_about.htm&language=en_US)
[Labels.](https://help.salesforce.com/articleView?id=cl_about.htm&language=en_US)


Metadata Types OauthCustomScope

**Field Name** **Field Type** **Description**

Note: The description formatting requirements that apply to
custom scopes also apply to custom labels.

`developerName` string Required. Use when referring to the OAuth custom scope from a
program.

`isProtected` boolean

`isPublic` boolean

`masterLabel` string

Required. Indicates whether this component is protected () or not
( `false` ). Protected components cannot be linked to or referenced by
components created in the installing org.

Indicates whether the object is included in the connected app’s OpenID
Connect discovery endpoint. The default setting is `false` . For more
[information, see OpenID Connect Discovery Endpoint.](https://help.salesforce.com/articleView?id=remoteaccess_using_openid_discovery_endpoint.htm&language=en_US)

Required. The primary label for the custom scope record. This label must
be unique and begin with a letter. It can include only alphanumeric
characters and underscores. It can’t contain spaces.

Declarative Metadata Sample Definition

The following is an example of an OAuthCustomScope component. In this example, `basicScope` is the name of custom scope entity
being retrieved.

```
<?xml version="1.0" encoding="UTF-8"?>

<OauthCustomScope xmlns="http://soap.sforce.com/2006/04/metadata">

   <assignedTo>

     <connectedApp>MyOrgNamespace__TestApp</connectedApp>

   </assignedTo>

   <description>Example of a basic custom scope</description>

   <developerName>basicScope</developerName>

   <masterLabel>basicScope</masterLabel>

   <isProtected>false</isProtected>

   <isPublic>true</isPublic>

</OauthCustomScope>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

<types>

<members>basicScope</members>

<name>OauthCustomScope</name>

</types>

<version>49.0</version>

</Package>

```

Usage

An OAuth custom scope tells an external entity about a connected app’s permissions to access protected data. The OAuth custom scope
you create in your Salesforce org corresponds to the same custom scope defined in your external entity and assigned to the resource.


### Metadata Types OauthTokenExchangeHandler

For example, you define an Order Status custom scope in your external entity that allows access to customer order status data in your
order system’s API. In Salesforce, you create an OAuth custom scope that you also name Order Status. You assign this custom scope to
the connected app requesting access to the order status API. When the external entity receives the connected app’s request to access
a customer’s order status, it validates the connected app’s access token and Order Status scope. With a successful validation, the app
can access the customer order status information in the order system’s API.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### OauthTokenExchangeHandler

Represents a token exchange handler. The token exchange handler also consists of an Apex class. During the OAuth 2.0 token exchange
flow, the token exchange handler is used to validate tokens from an external identity provider and to map users to Salesforce.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### OauthTokenExchangeHandler components have the suffix .oauthtokenexchangehandler and are stored in the

`oauthtokenexchangehandlers` folder.

Version

### OauthTokenExchangeHandler components are available in API version 60.0 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Description**

```
description

```

**Field Type**
string

**Description**
Required. A description for your token exchange handler.


Metadata Types OauthTokenExchangeHandler

**Field Name** **Description**

```
developerName

enablements

isAccessTokenSupported

isContactCreationAllowed

isEnabled

isIdTokenSupported

isJwtSupported

```

**Field Type**
string

**Description**
Required. The API name for the handler.

**Field Type**

OauthTokenExchHandlerApp[]

**Description**
The enablement settings for the token exchange handler, including the execution
user who runs the Apex class, the connected apps or external client apps for which
it’s enabled, and whether or not it’s the default handler.

**Field Type**
boolean

**Description**
Required. Indicates whether the handler supports OAuth 2.0 access tokens from the
identity provider, including opaque access tokens and JSON Web Token (JWT)-based
access tokens.

**Field Type**
boolean

**Description**
For internal use only.

**Field Type**
boolean

**Description**
Required. Indicates whether the handler is enabled. To complete enablement, add an
`enablements` field that specifies the enablement settings.

**Field Type**
boolean

**Description**
Required. Indicates whether the handler supports OpenID Connect ID tokens from the
identity provider.

**Field Type**
boolean

**Description**
Required. Indicates whether the handler supports tokens from the identity provider
that are in JWT format, such as JWT-based access tokens.


Metadata Types OauthTokenExchangeHandler

**Field Name** **Description**

```
isProtected

isRefreshTokenSupported

isSaml2Supported

isUserCreationAllowed

masterLabel

tokenHandlerApex

```

**Field Type**
boolean

**Description**
Indicates whether the handler can be linked to or referenced by components created
[in a subscriber org. See Protected Components in Managed Packages.](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/packaging_protected_components.htm)

**Field Type**
boolean

**Description**

Required. Indicates whether the handler supports OAuth 2.0 refresh tokens from the
identity provider.

**Field Type**
boolean

**Description**

Required. Indicates whether the handler supports SAML 2.0 assertions from the identity
provider.

**Field Type**
boolean

**Description**

Required. Indicates whether the handler can set up new users. During the token
exchange flow, the Apex handler maps users from the identity provider to Salesforce.
If the `isUserCreationAllowed` field is `true`, the `canCreateUser` boolean
in the `getUserForTokenSubject` method is `true`, and the user doesn’t exist
in Salesforce, the handler sets up a new User object, which Salesforce automatically
inserts to finish creating the user.

**Field Type**
string

**Description**

Required. The label of the token exchange handler record.

**Field Type**
string

**Description**

Required. The Apex class associated with the token exchange handler. The class contains
methods to validate the token and map users to Salesforce. It must extend the
`Oauth2TokenExchangeHandler` Apex class.


Metadata Types OauthTokenExchangeHandler

OauthTokenExchHandlerApp

Represents the settings for a specific Salesforce connected app or external client app that’s enabled for the token exchange handler. A
handler can be enabled for multiple apps.

**Field Name** **Description**

```
apexExecutionUser

connectedApp

externalClientApp

isDefault

```

**Field Type**
string

**Description**

Required. A user who runs the Apex token exchange handler. We recommend that
you use an integration user.

**Field Type**
string

**Description**
The API name of the connected app that’s being used to integrate with Salesforce.

**Field Type**
string

**Description**
The API name of the external client app that’s being used to integrate with Salesforce.

**Field Type**
boolean

**Description**

Required. Indicates whether the token exchange handler is the default handler for this
app. During the token exchange flow, in the token request, you can optionally include
a `token_handler` parameter with the name of a specific handler’s Apex class. If
you don’t include this parameter, Salesforce defaults to the default handler.

Declarative Metadata Sample Definition

The following is an example of an OauthTokenExchangeHandler component.

```
<?xml version="1.0" encoding="UTF-8"?>

<OauthTokenExchangeHandler xmlns="http://soap.sforce.com/2006/04/metadata">

   <developerName>MyTokenExchangeHandler</developerName>

   <description>My token exchange handler</description>

   <isAccessTokenSupported>true</isAccessTokenSupported>

   <isEnabled>true</isEnabled>

   <isIdTokenSupported>false</isIdTokenSupported>

   <isJwtSupported>true</isJwtSupported>

   <isProtected>false</isProtected>

   <isRefreshTokenSupported>false</isRefreshTokenSupported>

   <isSaml2Supported>false</isSaml2Supported>

   <isUserCreationAllowed>true</isUserCreationAllowed>

```


### Metadata Types OcrSampleDocument

```
      <masterLabel>MyTokenExchangeHandler</masterLabel>

      <tokenHandlerApex>MyOauthTokenExchangeHandler</tokenHandlerApex>

      <enablements>

        <apexExecutionUser>integrationuser@mycompany.com</apexExecutionUser>

        <connectedApp>TokenExchangeApp1</conectedApp>

        <isDefault>true</isDefault>

      </enablements>

   </OauthTokenExchangeHandler>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>OauthTokenExchangeHandler</name>

      </types>

      <version>60.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### OcrSampleDocument

Represents the details of a sample document or a document type that's used as a reference while extracting and mapping information
from a customer form. This type extends the Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

The OcrSampleDocument type doesn’t need to represent a real sample document. It can also be an abstract document that represents
all documents of the same DocumentType. In such cases, the `contentAsset` and `documentHeight` fields are null.

File Suffix and Directory Location

### OcrSampleDocument components have the suffix .ocrSampleDocument and are stored in the ocrSampleDocuments

folder.

Version

OcrTemplate components are available in API version 52.0 and later.

Special Access Rules

To use this metadata type, your Salesforce org must have the AWSTextract1000LimitAddOn license.


Metadata Types OcrSampleDocument

Fields

**Field Name** **Field Type** **Description**

The type of application using the OCR sample document.

Possible values are:

**•** `EinsteinDocumentReader`

**•** `Industries`

The ID of the OCR sample document asset.

This field is null if the OcrSampleDocument is an abstract document
representing the DocumentType.

The normalized height of the OCR sample document page.

This field is null if the OcrSampleDocument is an abstract document
representing the DocumentType.

```
applicationType

```

OcrApplicationType
(enumeration of
type string)

`contentAsset` string

`documentHeight` double

`documentType` string Required. The type of the OCR sample document.

`masterLabel` string Required. The label for the OCR sample document.

`ocrSampleDocumentFields` OcrSampleDocumentField[] The details of the field in a form whose value is extracted and mapped
to a Salesforce object field.

`ocrSampleDocumentPages` OcrSampleDocumentPage[] A collection of fields that define a page in the OCR sample document.

OcrSampleDocumentField

Represents the details of the field in a form whose value is extracted and mapped to a Salesforce object field.

**Table 4: Fields**

**Field Name** **Field Type** **Description**

`cellColumnNumber` int The column number in the item with the cell storing this field’s value. Available
in API version 56.0 and later.

`cellColumnSpanValue` int The number of columns that span the cell storing this field’s value. Available
in API version 56.0 and later.

`cellRowNumber` int The row number in the item with the cell storing this field’s value. Available in
API version 56.0 and later.

`cellRowSpanValue` int The number of rows that span the cell storing this field’s value. Available in API
version 56.0 and later.

`fieldLabelMaxX` double A normalized coordinate representing the right edge of the bounding box of
the key.

`fieldLabelMaxY` double A normalized coordinate representing the bottom edge of the bounding box
of the key.


Metadata Types OcrSampleDocument

**Field Name** **Field Type** **Description**

`fieldLabelMinX` double A normalized coordinate representing the left edge of the bounding box of
the key.

`fieldLabelMinY` double A normalized coordinate representing the top edge of the bounding box of
the key.

`fieldValueName` string Name of the referred field value. Available in API version 56.0 and later.

`isAutoExtractedValue` boolean

Indicates whether the key is automatically extracted ( `true` ) or not ( `false` ).
Available in API version 57.0 and later.

This field helps to distinguish auto-extracted keys from manual ones.

`keyContent` string The content in a particular area of the form, representing the field that is
extracted by OCR.

`ocrSampleDocument` string Required. The associated OCR sample document used as a reference while
extracting and mapping information from a customer form.

`ocrSampleDocumentPage` string

A reference to a page of the OCR sample document that contains the key.

This field is null if the OcrSampleDocument is an abstract document
representing the DocumentType.

`ocrSampleDocumentPageItem` OcrTemplate A reference to the item on the sample document page containing this field's
value. Available in API version 56.0 and later.

OcrSampleDocumentPage

Represents a collection of fields that define a page in the OCR sample document. This type exists only if the OcrSampleDocument is a
real sample document and not an abstract document representing the DocumentType.

**Table 5: Fields**

**Field Name** **Field Type** **Description**

`ocrSampleDocument` string Required. The associated OCR sample document used as a reference while
extracting and mapping information from a customer form.

`ocrSampleDocument` OcrSampleDocument The collection of page items with the associated OCR sample document page.
`PageItems` Available in API version 56.0 and later.

`pageHeight` double The normalized height of the OCR sample document page.

`pageNumber` integer Required. The page number of the page in the associated OCR sample
document.

OcrSampleDocumentPageItem

Represents a foreign key reference to the item on the sample document page containing a value for the page item.


Metadata Types OcrSampleDocument

**Table 6: Fields**

**Field Name** **Field Type** **Description**

`hasHeader` boolean

Indicates whether the OCR sample document page item has a header ( `true` )
or not ( `false` ). The default value is `false` . Available in API version 56.0 and
later.

`sequenceNumber` int Required. The sequence number of the item on an OCR sample document
page with multiple items. Available in API version 56.0 and later.

`title` string The title of the OCR sample document page item. Available in API version 56.0
and later.

Required. Specifies the type of OCR sample document page item. Available in
API version 56.0 and later.

Valid value is `TABLE` .

```
type

```

ItemType
(enumeration of type
string)

Declarative Metadata Sample Definition

The following is an example of a OcrSampleDocument component.

```
<?xml version="1.0" encoding="UTF-8"?>

<OcrSampleDocument xmlns="http://soap.sforce.com/2006/04/metadata">

  <contentAsset>asset_01jpeg</contentAsset>

  <documentHeight>1.24</documentHeight>

  <documentType>Form</documentType>

  <masterLabel>Form</masterLabel>

  <ocrSampleDocumentFields>

  ...<cellColumnNumber>1</cellColumnNumber>

    <cellColumnSpanValue>1</cellColumnSpanValue>

    <cellRowNumber>1</cellRowNumber>

    <cellRowSpanValue>1</cellRowSpanValue>

    <fieldLabelMaxX>0.5975854</fieldLabelMaxX>

    <fieldLabelMaxY>0.46625894</fieldLabelMaxY>

    <fieldLabelMinX>0.5065626</fieldLabelMinX>

    <fieldLabelMinY>0.39605626</fieldLabelMinY>

    <keyContent>Last Name</keyContent>

   <ocrSampleDocument>image240</ocrSampleDocument>

   <ocrSampleDocumentPage>1</ocrSampleDocumentPage>

   <ocrSampleDocumentPageItem>

      <hasHeader>false</hasHeader>

      <sequenceNumber>1</sequenceNumber>

      <title>Table1</title>

      <type>TABLE</type>

   </ocrSampleDocumentPageItem>

  </ocrSampleDocumentFields>

  <ocrSampleDocumentPages>

    <ocrSampleDocument>Form</ocrSampleDocument>

    <pageHeight>1.0</pageHeight>

    <pageNumber>1</pageNumber>

  </ocrSampleDocumentPages>

```


### Metadata Types OcrTemplate

```
     <ocrSampleDocumentPages>

       <ocrSampleDocument>Form</ocrSampleDocument>

       <pageNumber>2</pageNumber>

     </ocrSampleDocumentPages>

   </OcrSampleDocument>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <types>

       <members>*</members>

       <name>DocumentType</name>

     </types>

     <types>

       <members>*</members>

       <name>ContentAsset</name>

     </types>

     <types>

       <members>*</members>

       <name>OcrSampleDocument</name>

     </types>

     <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### OcrTemplate

Represents the details of the mapping between a form and a Salesforce object using Intelligent Form Reader. This type extends the
Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### OcrTemplate components have the suffix .ocrTemplate and are stored in the ocrTemplates folder.

Version

### OcrTemplate components are available in API version 52.0 and later.

Special Access Rules

To use this metadata type, your Salesforce org must have the AWSTextract1000LimitAddOn license.


Metadata Types OcrTemplate

Fields

**Field Name** **Field Type** **Description**

`active` boolean Indicates whether the OCR template is active ( `true` ) or not ( `false` ).

`description` string The description of the OCR template.

`documentType` string Required. The document type for which this template defines mappings.

`masterLabel` string Required. The label for the OCR template.

`ocrTargetObjects` OcrTargetObject[] Represents the details of the object to which information from a form
is extracted and mapped.

`ocrTemplateSampleDocuments` OcrTemplateSampleDocument[]

Represents the details of a sample document or a document type that's
used as a reference while extracting and mapping information from a
customer form.

`pageCount` integer The number of pages in the form from which information is extracted.

`templateName` string Required. The name of the OCR template.

OcrTargetObject

Represents the details of the object to which information from a form is extracted and mapped.

**Table 7: Fields**

**Field Name** **Field Type** **Description**

`ocrTargetObjectFieldMappings` OcrTargetObjFieldMapping[] Represents the details of how information from a form field is mapped to fields
in an object.

`targetObject` string Required. The object to which information from a form is mapped.

`targetObjectRecordType` string The developer name of the record type of the target object. Available in API
version 56.0 and later.

OcrTargetObjFieldMapping

Represents the details of how information from a form field is mapped to fields in an object.

**Table 8: Fields**

**Field Name** **Field Type** **Description**

`ocrSampleDocField` OcrSampleDocumentField[] The details of the field in a form whose value is extracted and mapped to a
Salesforce object field.

`targetField` string Required. The field to which information is mapped.

Required. Specifies the type of mapping. Available in API version 56.0 and later.

Valid values are:


```
type

```

OcrMappingType
(enumeration of type
string)

Metadata Types OcrTemplate

**Field Name** **Field Type** **Description**

**•** `FormField`

**•** `TableColumn`

The default value is `FormField` .

OcrSampleDocumentField

Represents the details of the field in a form whose value is extracted and mapped to a Salesforce object field.

**Table 9: Fields**

**Field Name** **Field Type** **Description**

`cellColumnNumber` int The column number in the item with the cell storing this field’s value. Available
in API version 56.0 and later.

`cellColumnSpanValue` int The number of columns that span the cell storing this field’s value. Available
in API version 56.0 and later.

`cellRowNumber` int The row number in the item with the cell storing this field’s value. Available in
API version 56.0 and later.

`cellRowSpanValue` int The number of rows that span the cell storing this field’s value. Available in API
version 56.0 and later.

`fieldLabelMaxX` double A normalized coordinate representing the right edge of the bounding box of
the key.

`fieldLabelMaxY` double A normalized coordinate representing the bottom edge of the bounding box
of the key.

`fieldLabelMinX` double A normalized coordinate representing the left edge of the bounding box of
the key.

`fieldLabelMinY` double A normalized coordinate representing the top edge of the bounding box of
the key.

`fieldValueName` string The name of the referred field value. Available in API version 56.0 and later.

`isAutoExtractedValue` boolean

Indicates whether the key is automatically extracted ( `true` ) or not ( `false` ).
Available in API version 57.0 and later.

This field helps to distinguish auto-extracted keys from manual ones.

`keyContent` string The content in a particular area of the form, representing the field that is
extracted by OCR.

`ocrSampleDocument` string Required. The associated OCR sample document is used as a reference while
extracting and mapping information from a customer form.

`ocrSampleDocumentPage` string A collection of fields that define a page in the OCR sample document.

`ocrSampleDocumentPageItem` OcrSampleDocumentPageItem A reference to the item on the sample document page containing this field's
value. Available in API version 56.0 and later.


Metadata Types OcrTemplate

OcrSampleDocumentPageItem

Represents a foreign key reference to the item on the sample document page containing a value for the page item.

**Table 10: Fields**

**Field Name** **Field Type** **Description**

`hasHeader` boolean

Indicates whether the OCR sample document page item has a header ( `true` )
or not ( `false` ). The default value is `false` . Available in API version 56.0 and
later.

`sequenceNumber` int Required. The sequence number of the item on an OCR sample document
page with multiple items. Available in API version 56.0 and later.

`title` string The title of the OCR sample document page item. Available in API version 56.0
and later.

Required. Specifies the type of OCR sample document page item.

Valid value is `TABLE` .

Available in API version 56.0 and later.

```
type

```

ItemType
(enumeration of type
string)

OcrTemplateSampleDocument

Represents the details of a sample document or a document type that's used as a reference while extracting and mapping information
from a customer form.

**Table 11: Fields**

**Field Name** **Field Type** **Description**

`ocrSampleDocument` string The associated OCR sample document is used as a reference while extracting
and mapping information from a customer form.

Declarative Metadata Sample Definition

The following is an example of a OcrTemplate component.

```
<?xml version="1.0" encoding="UTF-8"?>

<OcrTemplate xmlns="http://soap.sforce.com/2006/04/metadata">

  <active>false</active>

  <documentType>Form</documentType>

  <masterLabel>Form Test 222</masterLabel>

  <ocrTargetObjects>

    <ocrTargetObjFieldMappings>

      <ocrSampleDocField>

        <cellColumnNumber>1</cellColumnNumber>

        <cellColumnSpanValue>1</cellColumnSpanValue>

        <cellRowNumber>1</cellRowNumber>

        <cellRowSpanValue>1</cellRowSpanValue>

        <fieldLabelMaxX>0.5975854</fieldLabelMaxX>

        <fieldLabelMaxY>0.46625894</fieldLabelMaxY>

```


### Metadata Types OutboundNetworkConnection

```
           <fieldLabelMinX>0.5065626</fieldLabelMinX>

           <fieldLabelMinY>0.39605626</fieldLabelMinY>

           <keyContent>Last Name</keyContent>

           <ocrSampleDocument>image240</ocrSampleDocument>

           <ocrSampleDocumentPage>1</ocrSampleDocumentPage>

           <ocrSampleDocumentPageItem>

             <hasHeader>false</hasHeader>

             <sequenceNumber>1</sequenceNumber>

             <title>Table1</title>

             <type>TABLE</type>

           </ocrSampleDocumentPageItem>

        </ocrSampleDocField>

       <targetField>Account.Name</targetField>

       <type>TableColumn</type>

       </ocrTargetObjFieldMappings>

       <targetObject>Account</targetObject>

       <targetObjectRecordType>Account.X240</targetObjectRecordType>

     </ocrTargetObjects>

     <ocrTemplateSampleDocuments>

       <ocrSampleDocument>Form</ocrSampleDocument>

     </ocrTemplateSampleDocuments>

     <pageCount>10</pageCount>

     <templateName>Form Test</templateName>

   </OcrTemplate>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <types>

       <members>*</members>

       <name>OcrTemplate</name>

     </types>

     <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### OutboundNetworkConnection

Represents a private connection between a Salesforce org and a third-party data service. The connection is outbound because the
callouts are going _out_ of Salesforce. This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### OutboundNetworkConnection components have the suffix .outboundNetworkConnection and are stored in the

`outboundNetworkConnections` folder.


Metadata Types OutboundNetworkConnection

Version

OutboundNetworkConnection components are available in API version 49.0 and later.

Fields

**Field Name** **Field Type** **Description**

```
connectionType

```

ExternalConnectionType Required. Specifies the cloud provider of the connection.
(enumeration of

**•** `AwsPrivateLink`

type string)

**•** `AwsPrivateLink`

**•** `DataCloudPrivateConnection` (Reserved for internal use)

`description` string A description of the connection. Maximum of 255 characters.

`isActive` boolean Required. Specifies whether the connection is active ( `true` ) or not
( `false` ).

`label` string Required. A user-friendly label for the connection.

`outboundNetworkConnProperties` OutboundNetworkConnProperty Name-value pairs that describe the properties of an outbound network
on page 1658[] connection. Specify a name-value pair for each of the properties.

Required. Connection status. The connection is initially Unprovisioned
and moves through the other statuses automatically after an admin
performs a Provision, Sync, or Teardown action. The valid values are:

**•** `Unprovisioned`

**•** `Allocation`

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

OutboundNetworkConnProperty

Represents a name-value pair that describes the properties of an outbound network connection.

**Field Name** **Field Type** **Description**

```
propertyName

```

OutboundConnPropertyName Required. The name of a property used to establish to an
(enumeration of type OutboundNetworkConnection. Valid values are:
string)

**•** `AwsVpcEndpointId` —The unique endpoint ID provided by Salesforce
after an outbound AwsPrivateLink is created. The value is read-only when
the `status` is `Ready` .


Metadata Types OutboundNetworkConnection

**Field Name** **Field Type** **Description**

**•** `AwsVpcEndpointServiceName` —The name of the customer’s
endpoint service running in an AWS VPC that’s used for private connections
with Salesforce.

**•** `Region` —The region in which the VPC is hosted.

Enumerated values `DataCloudPrivateNetwork*` are reserved for
internal use.

`propertyValue` `string` Required. The value of OutboundConnPropertyName. For example, the
`propertyValue` of `Region` can be `us-west-2.`

Declarative Metadata Sample Definition

The following sample definition has the suffix `.outboundNetworkConnection` .

```
   <?xml version="1.0" encoding="UTF-8"?>

   <OutboundNetworkConnection xmlns="http://soap.sforce.com/2006/04/metadata">

      <connectionType>AwsPrivateLink</connectionType>

      <description>Outbound Connection to make a callout to a Service deployed in AWS

   VPC</description>

      <isActive>true</isActive>

      <label>MyOutboundConnection</label>

      <outboundNetworkConnProperties>

        <propertyName>Region</propertyName>

        <propertyValue>us-west-2</propertyValue>

      </outboundNetworkConnProperties>

      <outboundNetworkConnProperties>

        <propertyName>AwsVpcEndpointServiceName</propertyName>

   <propertyValue>com.amazonaws.vpce.us-west-2.vpce-svc-00d7bd6285c123b4c</propertyValue>

      </outboundNetworkConnProperties>

      <status>Unprovisioned</status>

   </OutboundNetworkConnection>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <fullName>sampleOutboundConnection</fullName>

      <types>

        <members>MyOutboundConnection</members>

        <name>OutboundNetworkConnection</name>

      </types>

      <version>49.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types Package Package

Specifies which metadata components to retrieve as part of a `retrieve()` call or defines a package of components.

**Name** **Type** **Description**

### apiAccessLevel APIAccessLevel (enumeration of Package components have access via dynamic Apex and the

type string) API to standard and custom objects in the organization where

they’re installed. Administrators who install packages can
restrict this access after installation for improved security. The
valid values are:

**•** Unrestricted—Package components have the same API
access to standard objects as the user who is logged in
when the component sends a request to the API.

**•** Restricted—The administrator can select which standard
objects the components can access. Further, the
components in restricted packages can only access custom
objects in the current package if the user's permissions
allow access to them.

For more information, see “API and Dynamic Apex Access in
### Packages” in Salesforce Help.

`description` string A short description of the package.

`fullName` string The package name used as a unique identifier for API access.
The `fullName` can contain only underscores and

alphanumeric characters. It must be unique, begin with a letter,
not include spaces, not end with an underscore, and not
contain two consecutive underscores. This field is inherited
from the Metadata component.

`namespacePrefix` string The namespace of the developer organization where the
package was created.

`objectPermissions` ProfileObjectPermissions[] Indicates which objects are accessible to the package, and the
kind of access available (create, read, update, delete).

`packageType` string Reserved for future use.

`postInstallClass` string The name of the Apex class that specifies the actions to execute
after the package has been installed or upgraded. The Apex

class must be a member of the package and must implement
the Apex `InstallHandler` interface. In patch upgrades,
you can't change the class name in this field but you can
change the contents of the Apex class. The class name can be
changed in major upgrades.

This field is available in API version 24.0 and later.

`setupWeblink` string The weblink used to describe package installation.


### Metadata Types ParticipantRole

**Name** **Type** **Description**

`types` PackageTypeMembers on page The type of component being retrieved.
1661[]

`uninstallClass` string The name of the Apex class that specifies the actions to execute
after the package has been uninstalled. The Apex class must

be a member of the package and must implement the Apex
`UninstallHandler` interface. In patch upgrades, you
can't change the class name in this field but you can change
the contents of the Apex class. The class name can be changed
in major upgrades.

This field is available in API version 25.0 and later.

`version` string Required. The version of the component type.

PackageTypeMembers

Use to specify the name and type of components to be retrieved in a package.

**Name** **Type** **Description**

`members` string

`name` string

Wildcard Support in the Manifest File

One or more named components, or the wildcard character
( `*` ) to retrieve all metadata components of the type specified

in the `<name>` element. To retrieve a standard object, specify
it by name. For example,

`<members>Account</members>` retrieves the standard
Account object.

The type of metadata component to be retrieved. For example,

`<name>CustomObject</name>` retrieves one or more
custom objects as specified in the `<members>` element.

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

Sample package.xml Manifest Files

### ParticipantRole

Represents details, such as the name and associated default access level, for a role that a participant can have in the context of a parent
record.


Metadata Types ParticipantRole

[other]: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

`ParticipantRole` components have the suffix `.participantRole` and are stored in the `participantRoles` folder.

Version

ParticipantRole components are available in API version 50.0 and later.

Fields

**Field Name** **Description**

```
defaultAccessLevel

isActive

masterLabel

parentObject

```

**Field Type**
picklist

**Description**
Required. The default sharing access granted to the participant role.

Valid values are:

**•** `Edit` —Read/Write

**•** `None`

**•** `Read` —Read Only

**Field Type**
boolean

**Description**
Indicates whether the participant role is activated.

**Field Type**
string

**Description**
Required. The name for the participant role.

**Field Type**
string

**Description**
Required. The parent object for the participant role.

Valid values are:


Metadata Types ParticipantRole

**Field Name** **Description**

**•** `Account`

**•** `Budget`

Available in API version 59.0 and later.

**•** `IndividualApplication`

Available in API version 59.0 and later.

**•** `Interaction`

Available in API version 52.0 and later.

**•** `InteractionSummary`

Available in API version 51.0 and later.

**•** `FinancialDeal`

Available in API version 52.0 and later.

**•** `FundingAward`

Available in API version 59.0 and later.

**•** `FundingOpportunity`

**•** `Opportunity`

**•** `Team`

Available in API version 58.0 and later.

**•** Custom objects

Declarative Metadata Sample Definition

The following is an example of a ParticipantRole component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ParticipantRole xmlns="http://soap.sforce.com/2006/04/metadata">

      <defaultAccessLevel>Read</defaultAccessLevel>

      <isActive>true</isActive>

      <masterLabel>Advisor</masterLabel>

      <parentObject>Account</parentObject>

   </ParticipantRole>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ParticipantRole</name>

      </types>

      <version>50.0</version>

   </Package>

```


### Metadata Types PathAssistant

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### PathAssistant

Represents Path records.This type extends the Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Note the following when working with PathAssistant:

**•** Only one path can be created per record type for each object, including __Master__ record type.

**•** Rich text guidance information cannot be retrieved or deployed from or to translation workbench.

**•** The preference does not need to be on to retrieve or deploy PathAssistant.

File Suffix and Directory Location

### PathAssistant components have the suffix .pathAssistant and are stored in the pathAssistants folder.

Version

### PathAssistant components are available in API version 34.0 and later.

Fields

**Field Name** **Field Type** **Description**

`active` boolean Indicates whether the path is active ( `true` ) or not ( `false` ).

`entityName` string

Required. The entity name. This is hard coded for Opportunity, Lead, and
Quote. For a custom object, this field must be specified and should be
the name of the custom object. This field is not updateable.

`fieldName` string Required. The field name. This is hard coded for StageName and Status.
For a custom object, this field must be specified and should be the name

of the picklist field that determines the steps in the path. This field is not
updateable.

`masterLabel` string Required. The label of the path.

### pathAssistantSteps PathAssistantStep[]

on page 1665

List of all the steps that have been configured with fields and guidance
information. Note that a missing step in the .xml file means it has not
been configured, not that it doesn’t exist.

`recordTypeName` string Required. The name of the record type associated with the path. This
field is not updateable.


Metadata Types PathAssistant

PathAssistantStep

Represents the steps or stages in a Path.

**Field Name** **Field Type** **Description**

`fieldNames` string All the fields in `entityName` that will display in this step.

`info` string The guidance information displayed in this step.

`picklistValueName` string Required. The picklist value associated with the step.

Declarative Metadata Sample Definition

The following is an example of a PathAssistant component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <PathAssistant xmlns="http://soap.sforce.com/2006/04/metadata">

      <active>true</active>

      <entityName>Opportunity</entityName>

      <fieldName>StageName</fieldName>

      <masterLabel>Test Path</masterLabel>

      <pathAssistantSteps>

        <fieldNames>Amount</fieldNames>

        <fieldNames>CloseDate</fieldNames>

        <info>Some Text</info>

        <picklistValueName>Id. Decision Makers</picklistValueName>

      </pathAssistantSteps>

      <pathAssistantSteps>

        <fieldNames>Amount</fieldNames>

        <fieldNames>CloseDate</fieldNames>

        <info>Some Text</info>

        <picklistValueName>Proposal/Price Quote</picklistValueName>

      </pathAssistantSteps>

      <recordTypeName>Test_Record_Type</recordTypeName>

   </PathAssistant>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <types>

        <members>Opportunity.Test_Busines_Process</members>

        <name>BusinessProcess</name>

      </types>

      <types>

        <members>Opportunity.StageName</members>

        <members>Lead.LeadSource</members>

        <members>Opportunity.Type</members>

        <name>CustomField</name>

      </types>

      <types>

        <members>Test_Path</members>

        <name>PathAssistant</name>

```


### Metadata Types PaymentGatewayProvider

```
      </types>

      <types>

        <members>Opportunity.Test_Record_Type</members>

        <name>RecordType</name>

      </types>

      <types>

        <members>PathAssistant</members>

        <name>Settings</name>

      </types>

      <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### PaymentGatewayProvider

Represents the metadata associated with a payment gateway provider. This type extends the Metadata metadata type and inherits its
`fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### PaymentGatewayProvider components have the suffix paymentGatewayProvider and are stored in the

`paymentGatewayProviders` folder.

Version

### PaymentGatewayProvider components are available in API version 48.0 and later.

Special Access Rules

To access PaymentGatewayProvider, you must have a Salesforce Order Management license with the PaymentPlatform org permission
activated.

Fields

**Field Name** **Field Type** **Description**

`apexAdapter` string The Apex adapter class name for your payment gateway. This field is
unique within your organization.

`comments` string Users can add comments to provide additional details about a record.
Maximum of 1000 characters.


### Metadata Types PermissionSet

**Field Name** **Field Type** **Description**

Required. Defines whether the payment gateway ignores duplicate
payment gateway calls ( `Yes` ) or whether it processes duplicate gateway
calls ( `No` ).

**•** `Yes`

**•** `No`

```
idempotencySupported

```

IdempotencySupportStatus
(enumeration of
type String)

`masterLabel` string Required. The label of this payment gateway provider record.

Declarative Metadata Sample Definition

The following is an example of a PaymentGatewayProvider component.

```
<PaymentGatewayProvider xmlns="http://soap.sforce.com/2006/04/metadata">

   <apexAdapter>SalesforceAdapter</apexAdapter>

   <idempotencySupported>Yes</idempotencySupported>

   <masterLabel>SalesforceAdapter</masterLabel>

   <comments>Comments</comments>

</PaymentGatewayProvider>

```

The following is an example `package.xml` that references the previous definition.

```
<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>*</members>

     <name>PaymentGatewayProvider</name>

   </types>

   <version>48.0</version>

</Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### PermissionSet

Represents a set of permissions that's used to grant more access to one or more users without changing their profile or reassigning
profiles. You can use permission sets to grant access but not to deny access.

This type extends the Metadata metadata type and inherits its `fullName` field.

In API version 40.0 and later, when you retrieve permission set metadata, all content exposed in Metadata API for the permission sets is
included. The metadata includes Apex associated with the permission set, CRUD, and so on. Likewise, when you deploy a permission
set, you must include all of its metadata to avoid accidentally overwriting the permission set’s contents.

In API version 39.0 and earlier, retrieving or deploying permission set metadata returns only app and system permissions assigned to
the permission set. Junction metadata (such as Apex, CRUD) are included only if the metadata for the related component is also included
in the package definition.


Metadata Types PermissionSet

In API version 29.0 and later, you can retrieve and deploy access settings for these managed components in profiles and permission sets:

[For more information, see the Managed Component Access section of Sample package.xml Manifest Files in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/manifest_samples.htm) _Metadata API Developer_
_Guide_ .

Declarative Metadata File Suffix and Directory Location

Permission sets are stored in the `permissionsets` directory. The file name matches the permission set API name and the extension
is `.permissionset` . For example, a permission set with the name _User_Management_Perms_ is stored in
`permissionsets/User_Management_Perms.permissionset` .

Version

Permission sets are available in API version 22.0 and later.

Special Access Rules

As of Summer ’20 and later, only users who have one of these permissions can access this type:

**•** View Setup and Configuration

**•** Manage Session Permission Set Activations

**•** Assign Permission Sets

**•** Manage Profiles and Permission Sets

To view the following settings, assignments, and permissions for standard and custom objects in a specified permission set, the View
Setup and Configuration permission is required.

**•** Client settings

**•** Field permissions

**•** Layout assignments

**•** Object permissions

**•** Permission dependencies

**•** Permission set tab settings

**•** Permission set group components

**•** Record types

Fields

**Field** **Field Type** **Description**

`agentAccesses` PermissionSetAgentAccess[] Indicates which agents are visible to users assigned to
this permission set. Available in API version 63.0 and later.

`applicationVisibilities` PermissionSetApplicationVisibility[] Indicates which apps are visible to users assigned to this
permission set. Available in API version 29.0 and later. In

API version 29.0, this field supports custom apps only. In
API version 30.0 and later, this field supports both
standard and custom apps.


Metadata Types PermissionSet

**Field** **Field Type** **Description**

`classAccesses` PermissionSetApexClassAccess[]

`customMetadataTypeAccesses` PermissionSetCustomMetadataTypeAccess[]

`customPermissions` PermissionSetCustomPermissions[]

`customSettingAccesses` PermissionSetCustomSettingAccesses[]

Indicates which top-level Apex classes have methods
that users assigned to this permission set can execute.
Available in API version 23.0 and later.

Indicates the custom metadata types that are
read-accessible to a user assigned to this permission set.
Available in API version 47.0 and later.

Indicates which custom permissions are available to users
assigned to this permission set. Available in API version
31.0 and later.

Indicates the custom settings that are read-accessible to
a user assigned to this permission set. Available in API
version 47.0 and later.

`description` string The permission set description. Limit: 255 characters.

`emailRoutingAddressAccesses` PermissionSetEmailRoutingAddressAccess[]

`externalCredentialPrincipalAccesses` PermissionSetExternalCredentialPrincipalAccess[]

`externalDataSourceAccesses` PermissionSetExternal
DataSourceAccess[]

Indicates the Email Routing Address permissions that are
available to users assigned to a permission set. Available
in API version 62.0 and later.

Indicates which external credential principals are available
to users assigned to this permission set. Available in API
version 59.0 and later.

Indicates which data sources with identity type of `Per`
`User` are available to users assigned to this permission
set. Available in API version 27.0 and later.

`fieldPermissions` PermissionSetFieldPermissions[] Indicates which fields are accessible to a user assigned
to this permission set, and the kind of access available

(readable or editable). Available in API version 23.0 and
later.

`flowAccesses` PermissionSetFlowAccess[]

`hasActivationRequired` boolean

Indicates which flows can be accessed by a user assigned
to this permission set. Available in API version 47.0 and
later.

Indicates whether the permission set requires an
associated active session ( `true` ) or not ( `false` ).
Available in API version 37.0 and later.

`label` string Required. The permission set label. Limit: 80 characters.

`license` string Either the related permission set license or the user
license associated with this permission set. Available in

API version 38.0 and later. Use this field instead of
`userLicense`, which is deprecated and only available
up to API Version 37.0.

`objectPermissions` PermissionSetObjectPermissions[] Indicates the objects that are accessible to a user assigned
to this permission set, and the kind of access available


Metadata Types PermissionSet

**Field** **Field Type** **Description**

(create, read, edit, delete, and so on). Available in API
version 23.0 and later.

`pageAccesses` PermissionSetApexPageAccess[]

Indicates which Visualforce pages that users assigned to
this permission set can execute. Available in API version
23.0 and later.

`recordTypeVisibilities` PermissionSetRecordTypeVisibility[] Indicates which record types are visible to users assigned
to this permission set. Available in API version 29.0 and

later. This field is never retrieved or deployed for inactive
record types.

`ServicePresenceStatusAccesses` PermissionSetServicePresenceStatusAccess[]
on page 1675

Indicates which Service presence statuses that the user
assigned to this profile can execute. Available in API
version 64.0 and later.

`tabSettings` PermissionSetTabVisibility[] Indicates the tab visibility settings for this permission set.
Available in API version 26.0 and later.

`userLicense` string Deprecated. The user license for the permission set. A
user license determines the baseline of features that the

user can access. Every user must have exactly one user
license. Available up to API version 37.0. In API version
38.0 and later, use `license` .

`userPermissions` PermissionSetUserPermissions[] Specifies an app or system permission (such as “API
Enabled”) and whether it's enabled for this permission

set. In API version 28.0 and earlier, this field retrieves all
user permissions, enabled or disabled. In API version 29.0
and later, this field retrieves only enabled user
permissions. In API Version 40.0 and later, if a permission
isn’t specified for a deployment, it’s disabled.

PermissionSetAgentAccess

PermissionSetAgentAccess represents the agent access configuration for users assigned through a permission set.

**Field Name** **Field Type** **Description**

`agentName` string Required. The name of the employee agent.

`enabled` boolean Required. Indicates whether users assigned to this permission set can
use the Agentforce Employee Agent ( `true` ) or not ( `false` ).

PermissionSetApplicationVisibility

PermissionSetApplicationVisibility on page 1670 determines whether an app is visible to a user assigned to this permission set.


Metadata Types PermissionSet

**Field Name** **Field Type** **Description**

`application` string Required. The app name.

`visible` boolean Required. Indicates whether this app is visible to users assigned to this
permission set ( `true` ) or not ( `false` ).

PermissionSetApexClassAccess

PermissionSetApexClassAccess on page 1671 represents the Apex class access for users assigned to a permission set.

**Field** **Field Type** **Description**

`apexClass` string Required. The Apex class name.

`enabled` boolean Required. Indicates whether users assigned to this permission set
can execute methods in the top-level class ( `true` ) or not ( `false` ).

PermissionSetCustomMetadataTypeAccess

PermissionSetCustomMetadataTypeAccess on page 1671 represents the custom metadata type access for users assigned to a permission
set. Available in API version 47.0 and later.

**Field** **Field Type** **Description**

`enabled` boolean Required. Indicates whether the records for this custom metadata
type are readable ( `true` ) or not ( `false` ).

`name` string Required. The custom metadata type name.

PermissionSetCustomPermissions

PermissionSetCustomPermissions represents the custom permissions access for users assigned to a permission set. Only enabled custom
permissions are retrieved.

**Field Name** **Field Type** **Description**

`enabled` boolean Required. Indicates whether the custom permission is enabled ( `true` )
or not ( `false` ).

`name` string Required. The custom permission name.

PermissionSetCustomSettingAccesses

PermissionSetCustomSettingAccesses represents the custom setting access for users assigned to a permission set. Available in API version
47.0 and later.


Metadata Types PermissionSet

**Field** **Field Type** **Description**

`enabled` boolean Required. Indicates whether the records for this custom setting are
readable ( `true` ) or not ( `false` ).

`name` string Required. The custom setting name.

PermissionSetEmailRoutingAddressAccess

PermissionSetEmailRoutingAddressAccess represents the Email Routing Address access for users assigned to a permission set. Only
enabled email routing addresses are retrieved.

**Field** **Field Type** **Description**

`enabled` boolean Required. Indicates whether the custom permission is enabled
( `true` ) or not ( `false` ).

`name` string Required. Represents an organization's Email-to-Case routing
address.

PermissionSetExternalCredentialPrincipalAccess

PermissionSetExternalCredentialPrincipalAccess on page 1672 represents the access to the external credential’s principals. Users assigned
to the permission set can make callouts using a named credential that references the external credential. Available in API version 59.0
and later.

**Field** **Field Type** **Description**

`enabled` boolean Required. Indicates whether external credential principal access is
enabled on the permission set ( `true` ) or not ( `false` ).

`externalCredentialPrincipal` string

Required. The name of the external credential and principal,
separated by a dash. For example,
`myExternalCredential-myPrincipal` .

If the external credential and principal are part of a package, include
the package’s namespace prefix with the principal’s name using

this format:
`namespacePrefix__` _**`myExternalCredential-myPrincipal`**_ .
Use two underscores (__) between the namespace prefix and the
external credential principal’s name.

PermissionSetExternalDataSourceAccess

PermissionSetExternalDataSourceAccess on page 1672 represents the data source access for users with identity type of `Per User` .
Available in API version 27.0 and later.


Metadata Types PermissionSet

**Field** **Field Type** **Description**

`enabled` boolean Required. Indicates whether the data source is enabled ( `true` ) or
not ( `false` ).

`externalDataSource` string The name of the external data source.

PermissionSetFieldPermissions

PermissionSetFieldPermissions on page 1673 represents the field permissions for users assigned to a permission set. In API version 30.0
and later, permissions for required fields can’t be retrieved or deployed. In API version 54.0 and later, only field permissions enabled in
the permission set are returned in queries.

As of API version 38.0, you can change field permissions to make a field editable using the Metadata API for fields that you can't change
through the user interface. For example, you can deploy `Asset.ProductCode` as an editable field even though you can't through
the user interface.

Note: If the View All Fields object permission is enabled for an object in the permission set, the individual fields aren't returned
under `fieldPermissions` . However, if you later disable the View All Fields object permission, the fields are returned under
`fieldPermissions` and you can remove access to the fields manually.

**Field** **Field Type** **Description**

`editable` boolean Required. Indicates whether the field can be edited by the users
assigned to this permission set ( `true` ) or not ( `false` ).

`field` string

Required. The API name of the field (such as
`Warehouse__c.Description__c` ).

When referencing shared Activity fields, specify Event or Task. For
example, `Event.Meeting__c` .

`readable` boolean Indicates whether the field can be read by the users assigned to
this permission set ( `true` ) or not ( `false` ).

PermissionSetFlowAccess

PermissionSetFlowAccess on page 1673 represents which flows a permission set grants access to. Available in API version 47.0 and later.

**Field** **Field Type** **Description**

`enabled` boolean

Required. Indicates whether users assigned this permission set can
access the flow ( `true` ) or not ( `false` ) The default value is
`false` .

`flow` string Required. The name of the flow to which access is granted.

PermissionSetObjectPermissions

PermissionSetObjectPermissions represents the object permissions for a permission set. Use one of these elements for each permission.


Metadata Types PermissionSet

**Field** **Field Type** **Description**

`allowCreate` boolean

`allowDelete` boolean

`allowEdit` boolean

`allowRead` boolean

Required. Indicates whether the object referenced by the `object`
field can be created by the users assigned to this permission set
( `true` ) or not ( `false` ).

Required. Indicates whether the object referenced by the `object`
field can be deleted by the users assigned to this permission set
( `true` ) or not ( `false` ).

Required. Indicates whether the object referenced by the `object`
field can be edited by the users assigned to this permission set
( `true` ) or not ( `false` ).

Required. Indicates whether the object referenced by the `object`
field can be viewed by the users assigned to this permission set
( `true` ) or not ( `false` ).

`modifyAllRecords` boolean Required. Indicates whether all records for the object referenced
by the `object` field can be viewed, edited, or deleted by the

users assigned to this permission set ( `true` ) or not ( `false` ),
regardless of the sharing settings for the object. Includes private
records (records with no parent object). Similar to the Modify All
Data user permission, but limited to the individual object level.

`object` string Required. The API name of the object (such as `Warehouse__c` ).

`viewAllFields` string Indicates whether all fields and field data for the object referenced
by the `object` field can be viewed by the users assigned to this

permission set ( `true` ) or not ( `false` ). Available in API version
63.0 and later.

`viewAllRecords` boolean Required. Indicates whether all records for the object referenced
by the `object` field can be viewed by the users assigned to this

permission set ( `true` ) or not ( `false` ), regardless of the sharing
settings for the object. This setting includes private records (records
with no parent object). The `viewAllRecords` field is similar
to the View All Data user permission but limited to the individual
object level.

PermissionSetApexPageAccess

PermissionSetApexPageAccess on page 1674 represents the Visualforce page access for users assigned to a permission set.

**Field** **Field Type** **Description**

`apexPage` string Required. The Visualforce page name.

`enabled` boolean Required. Indicates whether users assigned to this permission set
can execute the Visualforce page ( `true` ) or not ( `false` ).


Metadata Types PermissionSet

PermissionSetRecordTypeVisibility

PermissionSetRecordTypeVisibility on page 1675 represents the visibility of record types for this permission set.

**Field** **Field Type** **Description**

`recordType` string Required. The record type name, for example
`Account.MyRecordType` .

`visible` boolean Required. Indicates whether the record type is visible to users
assigned to this permission set ( `true` ) or not ( `false` ).

PermissionSetTabSetting

PermissionSetTabSetting on page 1675 represents the tab settings for a permission set.

**Field** **Field Type** **Description**

`tab` string Required. The tab name.

`visibility` PermissionSetTabVisibility Required. Indicates the visibility settings for the tab. Valid values
(enumeration of type string) are:

**•** `Available` —The tab is available on the All Tabs page.
Individual users can customize their display to make the tab
visible in any app.

**•** `None` —The tab isn’t available on the All Tabs page or visible
in any apps.

**•** `Visible` —The tab is available on the All Tabs page and
appears in the visible tabs for its associated app. Individual
users can customize their display to hide the tab or make it
visible in other apps.

PermissionSetUserPermission

In API version 28.0 and earlier, PermissionSetUserPermission represents an app or system permission for a permission set. In API version
29.0 and later, this field retrieves only enabled user permissions. Use one of these elements for each permission.

**Field** **Field Type** **Description**

`enabled` boolean Required. Indicates whether the permission is enabled ( `true` ) or
disabled ( `false` ).

`name` string Required. The name of the permission.

PermissionSetServicePresenceStatusAccess

Represents the presence statuses that reps assigned to this profile have access. Available in API version 64.0 and later.


Metadata Types PermissionSet

**Field** **Field Type** **Description**

`servicePresenceStatus` string Required. The name of Service Presence Status.

`enabled` boolean Required. Indicates whether the rep assigned to this profile has
access to the presence status ( `true` ) or not ( `false` ).

Declarative Metadata Sample Definition

The following is an example of a PermissionSet component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <PermissionSet xmlns="http://soap.sforce.com/2006/04/metadata">

      <description>Grants all rights needed for an HR administrator to manage

   employees.</description>

      <label>HR Administration</label>

      <userLicense>Salesforce</userLicense>

      <applicationVisibilities>

        <application>JobApps__Recruiting</application>

        <visible>true</visible>

      </applicationVisibilities>

      <userPermissions>

        <enabled>true</enabled>

        <name>ApiEnabled</name>

      </userPermissions>

      <objectPermissions>

        <allowCreate>true</allowCreate>

        <allowDelete>true</allowDelete>

        <allowEdit>true</allowEdit>

        <allowRead>true</allowRead>

        <viewAllRecords>true</viewAllRecords>

        <modifyAllRecords>true</modifyAllRecords>

        <viewAllFields>true</viewAllFields>

        <object>Job_Request__c</object>

      </objectPermissions>

      <fieldPermissions>

        <editable>true</editable>

        <field>Job_Request__c.Salary__c</field>

        <readable>true</readable>

      </fieldPermissions>

      <pageAccesses>

        <apexPage>Job_Request_Web_Form</apexPage>

        <enabled>true</enabled>

      </pageAccesses>

      <classAccesses>

       <apexClass>Send_Email_Confirmation</apexClass>

       <enabled>true</enabled>

      </classAccesses>

      <tabSettings>

        <tab>Job_Request__c</tab>

        <visibility>Available</visibility>

      </tabSettings>

      <recordTypeVisibilities>

```


### Metadata Types PermissionSetGroup

```
        <recordType>Recruiting.DevManager</recordType>

        <visible>true</visible>

      </recordTypeVisibilities>

   </PermissionSet>

```

The following is an example package.xml manifest used to retrieve the PermissionSet metadata for an organization. When you retrieve
permission sets, also retrieve the related components with assigned permissions. For example, to retrieve `objectPermissions`
and `fieldPermissions` for a custom object, you must also retrieve the CustomObject component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Job_Request__c</members>

        <name>CustomTab</name>

      </types>

      <types>

        <members>Job_Request__c</members>

        <name>CustomObject</name>

      </types>

      <types>

        <members>JobApps__Recruiting</members>

        <name>CustomApplication</name>

      </types>

      <types>

        <members>Recruiting.DevManager</members>

        <name>RecordType</name>

      </types>

      <types>

        <members>*</members>

        <name>PermissionSet</name>

      </types>

      <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### PermissionSetGroup

Represents a group of permission _sets_ and the permissions within them. Use permission set groups to organize permissions based on
job functions or tasks. Then, you can package the groups as needed.

This type extends the Metadata metadata type and inherits its `fullName` field.

Declarative Metadata File Suffix and Directory Location

Permission set groups are stored in the `permissionsetgroups` directory. The file name matches the permission set API name
and the extension is `.permissionsetgroup` . For example, a permission set group with the name


Metadata Types PermissionSetGroup

`Finance_Mgmt_PermSetGroup` is stored in
`permissionsetgroups/Finance_Mgmt_PermSetGroup.permissionsetgroup` .

Version

Permission set groups are available in API version 45.0 and later.

Special Access Rules

As of Summer ’20 and later, to view this type, users must have one of these permissions:

**•** View Setup and Configuration

**•** Manage Session Permission Set Activations

**•** Assign Permission Sets

To edit this type, users must have the Manage Profiles and Permission Sets permission.

Fields

**Field** **Field Type** **Description**

`description` string The permission set group description provided by the
permission set group creator.

`hasActivationRequired` boolean Indicates whether the permission set group requires an
associated active session ( `true` ) or not ( `false` ). The

default value is `false` . This field is available in API
version 53.0 and later.

`label` string Required. The permission set group label.

`mutingPermissionSets` string

A permission set containing permissions to disable in the
permission set group. This field is available in API version
46.0 and later.

`permissionSets` string A permission set or permission sets included in the
permission set group.

`status` string Indicates permission set group recalculation status. Valid
values are:

**•** `Updated` —The group is current.

**•** `Outdated` —The group requires recalculation.

**•** `Updating` —The group is in recalculation mode.

**•** `Failed` —The group recalculation failed.


Metadata Types PermissionSetGroup

Declarative Metadata Sample Definition

When adding a permission set group, you can do something like this. Individual permissions are included in the permission set referenced,
not in the permission set group.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <PermissionSetGroup xmlns="http://soap.sforce.com/2006/04/metadata">

      <fullName>Finance_Mgmt_PermSetGroup</fullName>

      <description>Finance_Mgmt_PermSetGroup desc</description>

      <label>Finance_Mgmt_PermSetGroup</label>

      <permissionSets>Billing_PS</permissionSets>

   </PermissionSetGroup>

```

The permission set `Billing_PS` contains the individual permissions included in `Finance_Mgmt_PermSetGroup` .

```
   <?xml version="1.0" encoding="UTF-8"?>

   <PermissionSet xmlns="http://soap.sforce.com/2006/04/metadata">

      <fullName>Billing_PS</fullName>

      <description>Billing_PS</description>

      <label>Billing_PS</label>

      <hasActivationRequired>false</hasActivationRequired>

      <license>Salesforce</license>

      <userPermissions>

         <enabled>true</enabled>

         <name>ViewSetup</name>

      </userPermissions>

      <userPermissions>

         <enabled>true</enabled>

         <name>ViewRoles</name>

      </userPermissions>

      <userPermissions>

         <enabled>true</enabled>

         <name>EditBillingInfo</name>

      </userPermissions>

   </PermissionSet>

```

This example `package.xml` manifest retrieves the PermissionSetGroup metadata for an org. When you retrieve permission set
groups, also retrieve the related components. For example, to retrieve PermissionSetGroup, you must also retrieve PermissionSet.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

         <members>Finance_Mgmt_PermSetGroup</members>

         <name>PermissionSetGroup</name>

      </types>

      <types>

         <members>Billing_PS</members>

         <name>PermissionSet</name>

      </types>

      <version>45.0</version>

   </Package>

```


### Metadata Types PermissionSetLicenseDefinition (Developer Preview)

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### PermissionSetLicenseDefinition (Developer Preview)

Represents the definition of a custom permission set license, which entitles specified features in a package.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### PermissionSetLicenseDefinition components have the suffix .permissionSetLicenseDefinition and are

stored in the `permissionSetLicenseDefinitions` folder.

Version

PermissionSetLicenseDefinition components are available in API version 54.0 and later.

Special Access Rules

To access PermissionSetLicenseDefinition, you must have the Partner Licensing Platform developer preview enabled. To participate in
[this developer preview, submit a participation request via the Partner Licensing Platform Developer Preview Partner Community group.](https://partners.salesforce.com/_ui/core/chatter/groups/GroupProfilePage?g=0F94V0000010zlV)

Note: The Partner Licensing Platform is available as a developer preview. The Partner Licensing Platform isn’t generally available
unless or until Salesforce announces its general availability in documentation or in press releases or public statements. All commands,
parameters, and other features are subject to change or deprecation at any time, with or without notice. Don't implement
functionality developed with these commands or tools in your production package.

Fields

**Field Name** **Field Type** **Description**

`customPermissions` PermissionSetLicenseDefinitionCustomPermission An array of licensed custom permissions included in the
permission set license definition.

`isSupplementLicense` boolean Indicates whether the custom permission set license is a
supplement license ( `true` ) or a foundation license ( `false` ).

The default value is `false` . This field is available in API version
55.0 and later.

`label` string Required. The name of the permission set license definition.


Metadata Types PermissionSetLicenseDefinition (Developer Preview)

**Field Name** **Field Type** **Description**

`licenseExpirationPolicy` LicenseExpirationPolicy The license expiration policy of the custom permission set
(enumeration of type string) license. Valid values are:

**•** `BlockNamespaceAccess` —Package access is
blocked for existing users when all custom permission set
licenses expire. This is the default value.

**•** `AllowNamespaceAccess` —Package access isn’t
blocked for existing users when all custom permission set
licenses expire.

This field is available in API version 55.0 and later.

`userLicenseRestrictions` string The user license categories that can be assigned the custom
permission set license. If no user license categories are

specified, all users can be assigned the license. Possible values
include:

**•** `${communities}`

**•** `${communitiesLogin}`

**•** `${customerCommunities}`

**•** `${customerCommunitiesLogin}`

**•** `${internal}`

**•** `${partnerCommunity}`

**•** `${partnerCommunityLogin}`

**•** `${platform}`

[For more information, see User License Restriction Categories](https://developer.salesforce.com/docs/atlas.en-us.260.0.plp_dev.meta/plp_dev/partner_licensing_platform_restriction_categories.htm)
[(Developer Preview). This field is available in API version 55.0](https://developer.salesforce.com/docs/atlas.en-us.260.0.plp_dev.meta/plp_dev/partner_licensing_platform_restriction_categories.htm)
and later.

PermissionSetLicenseDefinitionCustomPermission

Represents a licensed custom permission included in the permission set license definition.

**Field Name** **Field Type** **Description**

`name` string

Label of the licensed custom permission. This field must be a
reference to a CustomPermission that has the `isLicensed`
field set to `true` .

Declarative Metadata Sample Definition

The following is an example of a PermissionSetLicenseDefinition component.

```
<?xml version="1.0" encoding="UTF-8"?>

<PermissionSetLicenseDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

   <customPermissions>>

```


### Metadata Types PersonAccountOwnerPowerUser

```
        <name>AccessReportsPerm</name>

      </customPermissions>

      <isSupplementLicense>false</isSupplementLicense>

      <licenseExpirationPolicy>BlockNamespaceAccess</licenseExpirationPolicy>

      <label>ExampleFeatureLicenseDefinition</label>

      <userLicenseRestrictions>${internal}</userLicenseRestrictions>

   </PermissionSetLicenseDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>PermissionSetLicenseDefinition</name>

      </types>

      <version>54.0</version>

   </Package>

```

Usage

[For more information, see the Partner Licensing Platform Developer Guide (Developer Preview).](https://developer.salesforce.com/docs/atlas.en-us.260.0.plp_dev.meta/plp_dev/partner_licensing_platform_intro.htm)

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### PersonAccountOwnerPowerUser

Represents a user who can own more than 50,000 customer or partner portal accounts. Person account owner power users can own a
large number of either customer or partner users. They can’t change their role, look up to a parent role, or reparent their role. Person
account owner power user objects can't be created if deferred sharing is turned on for your org. This object is available in API version
57.0 and later.

Version

### PersonAccountOwnerPowerUser components are available in API version 57.0 and later.

Fields

**Field Name** **Description**

```
developerName

```

**Field Type**
string

**Description**
Required. The unique name of the object in the API.


### Metadata Types PipelineInspMetricConfig

**Field Name** **Description**

```
masterLabel

portalType

user

```

**Field Type**
string

**Description**
Required. The label entered when the person account owner power user is created.

**Field Type**
string

**Description**
Required. The type of portal user account that the person account owner power user
can own.

Possible values are:

**•** `CustomerPortal` —Customer Portal

**•** `Partner` —Partner Portal

**Field Type**
string

**Description**
Required. The unique ID associated with the person account owner power user.

### PipelineInspMetricConfig

Represents the settings of Pipeline Inspection forecast category metrics.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### PipelineInspMetricConfig components have the suffix .pipelineInspMetricConfig and are stored in the

`pipelineInspMetricConfigs` folder.

Version

### PipelineInspMetricConfig components are available in API version 57.0 and later.

Special Access Rules

Only users with the Customize Application or Modify All Data permission can access this type.


Metadata Types PipelineInspMetricConfig

Fields

**Field Name** **Description**

```
isCumulative

isProtected

masterLabel

metric

```

**Field Type**
boolean

**Description**

Required. Read only. Indicates whether the metric is cumulative ( `true` ) or not
( `false` ). The default value is `true` .

**Field Type**
boolean

**Description**
Indicates whether the component is protected ( `true` ) or not ( `false` ). The default
value is `false` .

**Field Type**
string

**Description**

Required. Customized label of the Pipeline Inspection metric. Limit: 50 characters.

**Field Type**
PipelineInspectionMetric (enumeration of type string)

**Description**

Required. The Pipeline Inspection metric. Possible values are:

**•** `BestCase` (available in API version 58.0 and later)

**•** `ClosedLost` (available in API version 58.0 and later)

**•** `ClosedWon` (available in API version 58.0 and later)

**•** `Commit` (available in API version 58.0 and later)

**•** `MostLikely` (available in API version 58.0 and later)

**•** `OpenPipeline` (available in API version 58.0 and later)

**•** `TotalPipeline` (available in API version 58.0 and later)

Declarative Metadata Sample Definition

The following is an example of a PipelineInspMetricConfig component.

```
<?xml version="1.0" encoding="UTF-8"?>

<PipelineInspMetricConfig xmlns="http://soap.sforce.com/2006/04/metadata">

   <isCumulative>true</isCumulative>

   <isProtected>false</isProtected>

   <masterLabel>Lost the opportunity</masterLabel>

   <metric>ClosedLost</metric>

```


### Metadata Types PlatformCachePartition

```
   </PipelineInspMetricConfig>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>PipelineInspMetricConfig</name>

      </types>

      <version>57.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### PlatformCachePartition

Represents a partition in the Platform Cache. This type extends the Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### PlatformCachePartition components have the suffix .cachePartition and are stored in the cachePartitions folder.

Version

### PlatformCachePartition components are available in API version 35.0 and later.

Special Access Rules

The “Author Apex” permission is required to deploy and retrieve PlatformCachePartition components.

Fields

**Field Name** **Field Type** **Description**

`description` string Describes the cache partition.

`isDefaultPartition` boolean Required. Indicates whether this cache partition is the default
partition in your organization ( `true` ) or not ( `false` ).

`masterLabel` string Required. The label of the cache partition that appears in the
Salesforce user interface.


Metadata Types PlatformCachePartition

**Field Name** **Field Type** **Description**

`platformCachePartitionTypes` PlatformCachePartitionType[] An array of cache types that the partition can store.

PlatformCachePartitionType

Contains information about a partition type, including its minimum and allocated capacity.

**Field Name** **Field Type** **Description**

`allocatedCapacity` int Required. The total storage capacity, in megabytes (MB), that is allocated
for the cache type, including free, purchased, and trial cache. Purchased

capacity includes organization-wide cache, which can be used in any
partition, and namespace-specific cache, which can be used only in
partitions associated with a namespace.

`allocatedPartnerCapacity` int

Required. Free capacity, in megabytes (MB). allocated to Developer Edition
orgs for the cache type. Use this capacity with security-reviewed managed
packages. Available in API version 51.0 and later.

`allocatedPurchasedCapacity` int Required. The amount of namespace-specific purchased storage capacity,
in MB, that is allocated for the cache type.

`allocatedTrialCapacity` int Required. The amount of trial cache space, in MB, that is allocated for the
cache type.

```
cacheType

```

PlatformCacheType The type of cache. Valid values are:
(enumeration of type

**•** `Session` —Session cache

string)

**•** `Session` —Session cache

**•** `Organization` —Org cache

Declarative Metadata Sample Definition

The following is an example of a PlatformCachePartition component.

```
<?xml version="1.0" encoding="UTF-8"?>

<PlatformCachePartition xmlns="http://soap.sforce.com/2006/04/metadata">

   <description>Custom partition and marked as default.</description>

   <isDefaultPartition>true</isDefaultPartition>

   <masterLabel>myPartition</masterLabel>

   <platformCachePartitionTypes>

     <allocatedCapacity>10</allocatedCapacity>

     <allocatedPurchasedCapacity>5</allocatedPurchasedCapacity>

     <cacheType>Session</cacheType>

   </platformCachePartitionTypes>

   <platformCachePartitionTypes>

     <allocatedCapacity>5</allocatedCapacity>

     <allocatedPurchasedCapacity>5</allocatedPurchasedCapacity>

     <cacheType>Organization</cacheType>

   </platformCachePartitionTypes>

</PlatformCachePartition>

```


### Metadata Types PlatformEventChannel

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>myPartition</members>

        <name>PlatformCachePartition</name>

      </types>

      <version>66.0</version>

   </Package>

```

If a namespace is defined in your organization, add the namespace prefix to your partition name. For example:

```
   <members>Namespace.myPartition</members>

```

To retrieve all cache partitions from your organization, use the wildcard character (*) as follows.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>PlatformCachePartition</name>

      </types>

      <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### PlatformEventChannel

Represents a channel that you can subscribe to in order to receive a stream of events. In API version 46.0 and earlier, it is the default
standard channel for change data capture events. In API version 47.0 and later, it is a custom channel for change data capture events.

The default standard channel corresponds to the entity selection in the Change Data Capture page in Setup. A custom channel is a
channel that you define using this metadata type. Starting in API version 47.0, the channel doesn’t contain the selected entities, which
are represented each by PlatformEventChannelMember. This type extends the Metadata metadata type and inherits its `fullName`
field.

File Suffix and Directory Location

### PlatformEventChannel components have the suffix .platformEventChannel and are stored in the platformEventChannels

folder.

Version

### PlatformEventChannel components are available in API version 45.0 and later.


Metadata Types PlatformEventChannel

Special Access Rules

You must have the Customize Application permission to deploy and retrieve this type.

Fields

**Field Name** **Field Type** **Description**

`channelMembers` PlatformEventChannel Removed. A list of event names of entities, including standard and
SelectedEntity[] custom objects, selected for Change Data Capture notifications.

Note: This field is removed in API version 47.0 and later and is
available only in API versions 45.0 and 46.0. In API version 47.0
and later, the channel members are each defined in a
PlatformEventChannelMember component.

```
channelType

```

PlatformEventChannel Required. The channel type. Valid values are:
Type (enumeration

**•** `data` —Change Data Capture channel corresponding to the selected

of type string)

entities.

**•** `event` —A channel that contains platform events.

`eventType` PlatformEventChannel The type of events that the channel can hold. A channel can hold only
EventType one type of events. Use this field to optionally specify a specific type of

(enumeration of events for a channel in combination with the `channelType` field.
type string) Valid values are:

**•** `custom` —The channel contains custom platform events. This value
is valid with the `channelType` of `event` .

**•** `data` —The channel contains change data capture events. This
value is valid with the `channelType` of `data` .

**•** `monitoring` —The channel contains Real-Time Event Monitoring
events. This value is valid with the `channelType` of `event` .

**•** `standard` —Reserved for internal use.

Available in API version 61.0 and later.

`label` string Required. The channel label.

PlatformEventChannelSelectedEntity

Note: This field type is removed in API version 47.0 and later and is available only in API versions 45.0 and 46.0.

**Field Name** **Field Type** **Description**

`selectedEntity` string Required. The event name of an entity selected for Change Data Capture
notifications. For example, for the Account standard object, the name

is `AccountChangeEvent`, or for a custom object MyObject__c, the
name is `MyObject__ChangeEvent` .


Metadata Types PlatformEventChannel

Usage

The createMetadata() and deleteMetadata() calls aren’t supported with the PlatformEventChannel metadata type.

In API version 47.0 and later, you can’t deploy or retrieve the ChangeEvents standard channel.

You can't delete the ChangeEvents standard channel with `destructiveChanges.xml`, but you can delete channel members
using the PlatformEventChannelMember type with `destructiveChanges.xml` .

You can delete a custom channel with `destructiveChanges.xml` . If you delete a custom channel, all its member
PlatformEventChannelMember components are also deleted.

You can update only the `fullName` field and the `label` field of a PlatformEventChannel component.

Declarative Metadata Sample Definition for a Custom Channel

The PlatformEventChannel component contains the label of the custom channel and the channel type.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <PlatformEventChannel xmlns="http://soap.sforce.com/2006/04/metadata">

      <channelType>data</channelType>

      <label>Custom Channel for Sales Events</label>

   </PlatformEventChannel>

```

This `package.xml` references the previous definition. The custom channel name is `SalesEvents__chn` .

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>SalesEvents__chn</members>

        <name>PlatformEventChannel</name>

      </types>

      <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

To deploy or retrieve all custom channels, specify the wildcard character `*` (asterisk) in the `<members>` field.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>PlatformEventChannel</name>

      </types>

      <version>66.0</version>

   </Package>

```

Upgrading to Version 47.0 or Later From an Earlier Version

The `channelMembers` field of the PlatformEventChannel type is removed in API version 47.0 and later. As a result,
PlatformEventChannel components created in prior versions can’t be deployed using a later API version but you can deploy them in the
same API version they were created with.


### Metadata Types PlatformEventChannelMember

To deploy a custom channel component using API version 47.0 and later, upgrade the PlatformEventChannel definition by removing
the `<channelMembers>` fields. For the ChangeEvents standard channel, it can’t be deployed or retrieved, so delete the
PlatformEventChannel definition file.

For example, if you had custom channel called SalesEvents__chn, this could be your custom channel definition in API version 46.0.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <PlatformEventChannel xmlns="http://soap.sforce.com/2006/04/metadata">

      <channelMembers>

        <selectedEntity>AccountChangeEvent</selectedEntity>

      </channelMembers>

      <channelMembers>

        <selectedEntity>ContactChangeEvent</selectedEntity>

      </channelMembers>

      <channelType>data</channelType>

      <label>Sales Events</label>

   </PlatformEventChannel>

```

To upgrade to version 47.0 or later, you would replace the custom channel definition with this definition, which doesn’t contain any
channel members.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <PlatformEventChannel xmlns="http://soap.sforce.com/2006/04/metadata">

      <channelType>data</channelType>

      <label>SalesEvents__chn</label>

   </PlatformEventChannel>

```

For each channel member that is part of either a custom or the standard ChangeEvents channel, add a PlatformEventChannelMember
metadata component. Also, in the `package.xml` file, reference both the PlatformEventChannel and PlatformEventChannelMember
components.

For example, this PlatformEventChannelMember component is for the AccountChangeEvent member.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <PlatformEventChannelMember xmlns="http://soap.sforce.com/2006/04/metadata">

      <eventChannel>SalesEvents__chn</eventChannel>

      <selectedEntity>AccountChangeEvent</selectedEntity>

   </PlatformEventChannelMember>

```

For more information, see PlatformEventChannelMember.

[For an example of a custom channel that holds custom platform events and Real-Time Event Monitoring events, see Group Platform](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_subscribe_custom_channels.htm)
[Events into One Stream with a Custom Channel in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_subscribe_custom_channels.htm) _Platform Events Developer Guide_ .

SEE ALSO:

_[Change Data Capture Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.change_data_capture.meta/change_data_capture/cdc_subscribe_channels.htm)_ : Subscription Channels

_Change Data Capture Developer Guide_ [: Compose Streams of Change Data Capture Notifications with Custom Channels](https://developer.salesforce.com/docs/atlas.en-us.260.0.change_data_capture.meta/change_data_capture/cdc_custom_channel.htm)

### PlatformEventChannelMember PlatformEventChannelMember

Represents an entity selected for Change Data Capture notifications on a standard or custom channel, or a platform event selected on
a custom channel.


Metadata Types PlatformEventChannelMember

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

PlatformEventChannelMember components have the suffix `.platformEventChannelMember` and are stored in the
`platformEventChannelMembers` folder.

Version

PlatformEventChannelMember components are available in API version 47.0 and later.

Special Access Rules

You must have the Customize Application permission to deploy and retrieve this type.

Fields

**Field Name** **Field Type** **Description**

`enrichedFields` EnrichedField[] One or more fields selected for Change Data Capture Enrichment. A
non-empty enriched field is added to an update or delete change event

[even when not changed. For more information, see Enrich Change Events](https://developer.salesforce.com/docs/atlas.en-us.260.0.change_data_capture.meta/change_data_capture/cdc_enrich_intro.htm)
[with Extra Fields When Subscribed with CometD in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.change_data_capture.meta/change_data_capture/cdc_enrich_intro.htm) _Change Data_
_Capture Developer Guide_ . Available in API version 51.0 and later.

`eventChannel` string

`filterExpression` string

Required. The name of a channel. For the standard channel, the name
is `ChangeEvents` . For a custom channel, the name is in this format:
_**`MyChannel`**_ `__chn` .

An expression that is used to filter the stream of events and deliver only
the events that match specific criteria. The filter expression can contain

one or more field-value expressions. The filter expression format is based
on SOQL and supports a subset of SOQL operators and field types.

For example, this filter expression delivers only events that contain the
City__c field with a value of 'San Francisco'. `City__c = 'San`

```
Francisco'

```

[For more information, see Filter Your Stream of Platform Events with](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_filter_section.htm)
[Custom Channels in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_filter_section.htm) _Platform Events Developer Guide_ [and Filter Your](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/cdc_filter_section.htm)
[Stream of Change Events with Channels in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/cdc_filter_section.htm) _Change Data Capture_
_Developer Guide_ . Available in API version 56.0 and later.

`selectedEntity` string Required. The change event name of an entity selected for Change Data
Capture notifications. For example, for the Account standard object, the

name is `AccountChangeEvent`, or for a custom object
MyObject__c, the name is `MyObject__ChangeEvent` .


Metadata Types PlatformEventChannelMember

EnrichedField

A field selected on PlatformEventChannelMember for Change Data Capture Enrichment. A non-empty enriched field is added to an
update or delete change event even when not changed.

**Field Name** **Field Type** **Description**

`name` string The name of a field selected to enrich change events with.

Usage

The createMetadata() and deleteMetadata() calls aren’t supported with the PlatformEventChannelMember metadata type.

To delete a channel member from a channel, deploy `destructiveChanges.xml` for this type and specify the full name of the
member.

Declarative Metadata Sample Definition

This PlatformEventChannelMember component represents the selection of the Lead change event as part of the Change Data Capture
selections (the standard `ChangeEvents` channel).

```
   <?xml version="1.0" encoding="UTF-8"?>

   <PlatformEventChannelMember xmlns="http://soap.sforce.com/2006/04/metadata">

      <eventChannel>ChangeEvents</eventChannel>

      <selectedEntity>LeadChangeEvent</selectedEntity>

   </PlatformEventChannelMember>

```

Note: The file name of the example component is
`ChangeEvents_LeadChangeEvent.platformEventChannelMember` . The file name, without the extension,
corresponds to the component full name ( `ChangeEvents_LeadChangeEvent` ).

If the channel has more than one selected entity, each entity is represented separately by a PlatformEventChannelMember component.
For example, this component is a second member of the standard ChangeEvents channel and represents the Contact change event.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <PlatformEventChannelMember xmlns="http://soap.sforce.com/2006/04/metadata">

      <eventChannel>ChangeEvents</eventChannel>

      <selectedEntity>ContactChangeEvent</selectedEntity>

   </PlatformEventChannelMember>

```

This example is a selected entity on the `SalesEvents__chn` custom channel.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <PlatformEventChannelMember xmlns="http://soap.sforce.com/2006/04/metadata">

      <eventChannel>SalesEvents__chn</eventChannel>

      <selectedEntity>ContactChangeEvent</selectedEntity>

   </PlatformEventChannelMember>

```

This example shows one enriched field, `Phone`, for a selected entity on the `SalesEvents__chn` custom channel. Enriched fields
are supported in API version 51.0 and later.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <PlatformEventChannelMember xmlns="http://soap.sforce.com/2006/04/metadata">

      <enrichedFields>

```


Metadata Types PlatformEventChannelMember

```
        <name>Phone</name>

      </enrichedFields>

      <eventChannel>SalesEvents__chn</eventChannel>

      <selectedEntity>ContactChangeEvent</selectedEntity>

   </PlatformEventChannelMember>

```

This example shows a filter expression for a ContactChangeEvent selected entity on the `SalesEvents__chn` custom channel.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <PlatformEventChannelMember xmlns="http://soap.sforce.com/2006/04/metadata">

      <eventChannel>SalesEvents__chn</eventChannel>

      <filterExpression><![CDATA[(Region__c='AMER')]]></filterExpression>

      <selectedEntity>ContactChangeEvent</selectedEntity>

   </PlatformEventChannelMember>

```

Underscores in Channel Member Full Names

Two consecutive underscores in full names designate either a component name suffix or a namespace prefix. In all other cases, two
consecutive underscores aren’t supported in full names. If your channel member name contains a custom channel name to make it
unique, ensure to replace the double underscores in the name with one underscore. For example, the member name would be
`SalesEvents_chn_AccountChangeEvent` and not `SalesEvents__chn_AccountChangeEvent` .

Referencing Channel Members and Channels in **`Package.xml`**

This manifest file references the example definitions on the `ChangeEvents` standard channel. It lists each member in the `<members>`
field of `PlatformEventChannelMember` . The `<members>` field contains the channel member full name in this format:
_**`ChannelName`**_ `_` _**`EventName`**_ .

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>ChangeEvents_LeadChangeEvent</members>

        <members>ChangeEvents_ContactChangeEvent</members>

        <name>PlatformEventChannelMember</name>

      </types>

      <version>66.0</version>

   </Package>

```

This manifest file references members of the `SalesEvents__chn` custom channel.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>SalesEvents_chn_AccountChangeEvent</members>

        <members>SalesEvents_chn_ContactChangeEvent</members>

        <members>SalesEvents_chn_MyCustomObj_ChangeEvent</members>

        <name>PlatformEventChannelMember</name>

      </types>

      <version>66.0</version>

   </Package>

```


### Metadata Types PlatformEventSubscriberConfig

To retrieve a custom channel and channel members, you can reference them in the same `package.xml` file, as this example shows.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>SalesEvents__chn</members>

        <name>PlatformEventChannel</name>

      </types>

      <types>

        <members>SalesEvents_chn_AccountChangeEvent</members>

        <members>SalesEvents_chn_ContactChangeEvent</members>

        <members>SalesEvents_chn_MyCustomObj_ChangeEvent</members>

        <name>PlatformEventChannelMember</name>

      </types>

      <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

_Change Data Capture Developer Guide_ [: Example Diagrams for Channels and Channel Members](https://developer.salesforce.com/docs/atlas.en-us.260.0.change_data_capture.meta/change_data_capture/cdc_channel_examples.htm)

_Change Data Capture Developer Guide_ [: Filter Your Stream of Change Events with Channels](https://developer.salesforce.com/docs/atlas.en-us.260.0.change_data_capture.meta/change_data_capture/cdc_filter_section.htm)

_Platform Events Developer Guide_ [: Filter Your Stream of Platform Events with Channels](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_filter_section.htm)

PlatformEventChannel

### PlatformEventSubscriberConfig

Represents configuration settings for a platform event Apex trigger, including the batch size and the trigger’s running user.

This type extends the Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### PlatformEventSubscriberConfig components have the suffix .platformEventSubscriberConfig and are stored in the PlatformEventSubscriberConfigs folder.

Version

### PlatformEventSubscriberConfig components are available in API version 51.0 and later.


Metadata Types PlatformEventSubscriberConfig

Fields

**Field Name** **Field Type** **Description**

`batchSize` int A custom batch size, from 1 through 2,000, for the platform event Apex
trigger. The batch size corresponds to the maximum number of event

messages that can be sent to a trigger in one execution. The default
batch size is 2,000 for platform event triggers.

We don't recommend setting the batch size to 1 to process one event
at a time. Small batch sizes can slow down the processing of event
messages.

`isProtected` boolean (Inherited field.) Indicates whether this component is protected ( `true` )
or not ( `false` ). Protected components can’t be linked to or referenced

by components created in a subscriber org. A developer can delete a
protected component in a future release without worrying about failing
installations. However, once a component is marked as unprotected and
is released globally, the developer can’t delete it.

`masterLabel` string Required. The label for the PlatformEventSubscriberConfig component.

`numPartitions` int Specifies the number of parallel subscriptions, or partitions, that are
created internally for an Apex trigger. Use this field to set up parallel

subscriptions for the platform event Apex trigger. It can be an integer
[from 1 through 10. See Platform Event Processing at Scale with Parallel](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_ps.htm)
[Subscriptions for Apex Triggers in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_ps.htm) _Platform Events Developer Guide_ .

The default value is 1. This field is available in API version 62.0 and later.

`partitionKey` string Can be the standard `EventUuid` field or a required custom field of
the custom platform event that the Apex trigger subscribes to. For the

standard `EventUuid` field, the partition key format is the field name
without the event name: `EventUuid` . For a custom field, the partition
key includes the event name as a prefix in this format:
_**`EventName__e`**_ `.` _**`FieldName__c`**_ . Based on the field’s generated
hash value, the system determines which partition to send the event to.
Use this field to specify the platform event field that is used as a partition
[key for parallel subscriptions. See Platform Event Processing at Scale with](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_ps.htm)
[Parallel Subscriptions for Apex Triggers in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_ps.htm) _Platform Events Developer_
_Guide_ .

The default value is `EventUuid` . This field is available in API version
62.0 and later.

`platformEventConsumer` string Required. The full name of the platform event Apex trigger to configure.

`user` string

The username of the user that the platform event Apex trigger runs as.
By default, the platform event trigger runs as the Automated Process
entity. Setting the running user to a specific user has these benefits:

**•** Records are created or modified as this user.


Metadata Types PlatformEventSubscriberConfig

**Field Name** **Field Type** **Description**

**•** Records with `OwnerId` fields have their `OwnerId` fields
populated to this user when created or modified.

**•** Debug logs for the trigger execution are created by this user.

**•** You can send email from the trigger, which isn’t supported with the
default Automated Process user.

Declarative Metadata Sample Definition

This PlatformEventSubscriberConfig component has the label `OrderEventTriggerConfig` . It contains the configuration of a
platform event trigger, `OrderEventTrigger`, and specifies the batch size and user.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <PlatformEventSubscriberConfig xmlns="http://soap.sforce.com/2006/04/metadata">

      <platformEventConsumer>OrderEventTrigger</platformEventConsumer>

      <batchSize>200</batchSize>

      <masterLabel>OrderEventTriggerConfig</masterLabel>

      <user>user@example.com</user>

      <isProtected>false</isProtected>

   </PlatformEventSubscriberConfig>

```

PlatformEventSubscriberConfig references an Apex trigger, which depends on a platform event. If the referenced items exist in the
Salesforce org, you can deploy the PlatformEventSubscriberConfig component. This `package.xml` specifies the
PlatformEventSubscriberConfig component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <name>PlatformEventSubscriberConfig</name>

        <members>OrderEventTriggerConfig</members>

      </types>

      <version>66.0</version>

   </Package>

```

If the referenced trigger and platform event don’t exist in the org, include their definitions in the package. Otherwise, the deployment
fails. This example `package.xml` includes all the referenced components.

**•** CustomObject represents the platform event.

**•** CustomField represents a custom field defined on the platform event.

**•** ApexTrigger represents the platform event trigger.

**•** PlatformEventSubscriberConfig represents the configuration options for the platform event trigger.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <name>CustomObject</name>

        <members>PlatformEvent__e</members>

      </types>

      <types>

        <name>CustomField</name>

        <members>PlatformEvent__e.Message__c</members>

```


### Metadata Types Portal

```
      </types>

      <types>

        <name>ApexTrigger</name>

        <members>OrderEventTrigger</members>

      </types>

      <types>

        <name>PlatformEventSubscriberConfig</name>

        <members>OrderEventTriggerConfig</members>

      </types>

      <version>66.0</version>

   </Package>

```

To specify all PlatformEventSubscriberConfig components, use the wildcard character, as shown in this example.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <name>PlatformEventSubscriberConfig</name>

        <members>*</members>

      </types>

      <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### Portal

The Portal metadata type represents a partner portal.

It extends Metadata and inherits its `fullName` field. To use this metadata type, you must have a partner portal or Customer Portal
enabled for your organization. For more information, see Partner Portal Overview in Salesforce Help.

Declarative Metadata File Suffix and Directory Location

Lightning Platform Portal components are stored in the `portals` directory of the corresponding package directory. The file name
matches the portal name, and the extension is `.portal` .

Version

Lightning Platform Portal components are available in API version 15.0 and later.

Special Access Rules

All users, including unauthenticated guest users, can view portals via the API.


Metadata Types Portal

Fields

**Field** **Field Type** **Description**

`active` boolean Required. Denotes whether this portal is active.

`admin` string The full name of the user designated to administer the portal.

`defaultLanguage` string

The default language for HTML messages for the portal. Use the
abbreviation for the language, for example, en_US for United
States English.

`description` string The portal description.

`emailSenderAddress` string

`emailSenderName` string

Required. The email address used when sending emails using
templates configured from the portal (for example, for resetting
the password).

Required. The name to display when sending emails using
templates configured from the portal (for example, for resetting
the password).

`enableSelfCloseCase` boolean For the Customer Portal, allows portal users to close their own
cases.

`footerDocument` string The file to be used as the footer for this portal.

`forgotPassTemplate` string

`fullName` string

The email template to use when a user clicks the **Forgot**
**Password** link.

Lightning email templates aren’t packageable. We recommend
using a Classic email template.

Required. The name of the portal.

Inherited from Metadata, this field is defined in the WSDL for
this metadata type. It must be specified when creating, updating,

or deleting. See `createMetadata()` to see an example of
this field specified for a call.

`headerDocument` string The file to be used as the header for this portal.

`isSelfRegistrationActivated` boolean Determines whether self-registration is active or not for this
portal.

`loginHeaderDocument` string The file to be used as the header for this portal's login page.

`logoDocument` string The file to be used as the logo for this portal.

`logoutUrl` string The URL that the user is redirected to on logout.

`newCommentTemplate` string The email template to be used for auto-notifications on new
case comments.


Metadata Types Portal

**Field** **Field Type** **Description**

`newPassTemplate` string

`newUserTemplate` string

`ownerNotifyTemplate` string

The email template to be used for auto-notifications on
password reset.

Lightning email templates aren’t packageable. We recommend
using a Classic email template.

The email template to be used for auto-notifications on new
user creation.

Lightning email templates aren’t packageable. We recommend
using a Classic email template.

The email template to be used for auto-notifications on owner
change.

Lightning email templates aren’t packageable. We recommend
using a Classic email template.

`selfRegNewUserUrl` string The URL of the self-registration page.

`selfRegUserDefaultProfile` string The default profile for self-registered users.

`selfRegUserDefaultRole` PortalRoles (enumeration of The default role for self-registered users. The valid values are:
type string)

**•** Executive

**•** Manager

**•** User

**•** PersonAccount

`selfRegUserTemplate` string

The email template to be used for auto-notifications on
self-registration.

Lightning email templates aren’t packageable. We recommend
using a Classic email template.

`showActionConfirmation` boolean Determines whether confirmation messages are displayed for
actions in the portal.

`stylesheetDocument` string The Document object to be used as the CSS style sheet for this
portal.

`type` PortalType (enumeration of type Required. The type for this portal. The valid values are:
string)

**•** CustomerSuccess

**•** Partner

Declarative Metadata Sample Definition

Here’s a sample XML definition of a portal.

```
<?xml version="1.0" encoding="UTF-8"?>

<Portal xmlns="http://soap.sforce.com/2006/04/metadata">

```


### Metadata Types PortalDelegablePermissionSet

```
      <active>true</active>

      <description>Customer Portal</description>

      <emailSenderName>rguest@albany.com</emailSenderName>

      <enableSelfCloseCase>false</enableSelfCloseCase>

      <forgotPassTemplate>unfiled$public/ChangePwdEmail</forgotPassTemplate>

      <isSelfRegistrationActivated>false</isSelfRegistrationActivated>

      <newPassTemplate>unfiled$public/ChangePwdEmail</newPassTemplate>

      <newUserTemplate>unfiled$public/NewUserEmail</newUserTemplate>

      <selfRegUserTemplate>unfiled$public/SelfRegUserEmail</selfRegUserTemplate>

      <showActionConfirmation>false</showActionConfirmation>

      <type>CustomerSuccess</type>

   </Portal>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

CustomSite

### PortalDelegablePermissionSet

Represents the org-level permission sets that can be assigned to a particular profile for external users or shoppers in a store after enabling
the Delegable Administration perm.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

### PortalDelegablePermissionSet components have the suffix .portaldelegablepermissionset and are stored in the

`portaldelegablepermissionsets` folder.

Version

### PortalDelegablePermissionSet components are available in API version 56.0 and later.


Metadata Types PortalDelegablePermissionSet

Fields

**Field Name** **Description**

```
isProtected

masterLabel

permissionSet

profile

```

**Field Type**
boolean

**Description**
An auto-generated value that doesn’t impact the behavior of the metadata type.

**Field Type**
string

**Description**
Required. The label for the service that appears to users.

**Field Type**
string

**Description**
Required. Foreign key to the permissionSet on page 1667 entity.

**Field Type**
string

**Description**
Required. Foreign key to the profile on page 1716 entity.

Declarative Metadata Sample Definition

The following is the definition of the PortalDelegablePermissionSet entity.

```
<xsd:complexType name="PortalDelegablePermissionSet">

   <xsd:complexContent>

   <xsd:extension base="tns:Metadata">

    <xsd:sequence>

     <xsd:element name="isProtected" minOccurs="0" type="xsd:boolean"/>

     <xsd:element name="masterLabel" type="xsd:string"/>

     <xsd:element name="permissionSet" type="xsd:string"/>

     <xsd:element name="profile" type="xsd:string"/>

    </xsd:sequence>

   </xsd:extension>

   </xsd:complexContent>

  </xsd:complexType>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>*</members>

     <name>PortalDelegablePermissionSet</name>

```


### Metadata Types PostTemplate

```
      </types>

      <types>

        <members>*</members>

        <name>Profile</name>

      </types>

      <types>

        <members>*</members>

        <name>PermissionSet</name>

      </types>

   <version>56.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### PostTemplate

Represents the metadata associated with an approval post template for Approvals in Chatter. With approval post templates, you can
customize the information included in approval request posts that appear in Chatter feeds. This type extends the Metadata metadata
type and inherits its `fullName` field.

Note: Review Chatter Post Templates for Approval Requests in the Salesforce Help before you create a post template.

File Suffix and Directory Location

### PostTemplate components have the suffix .postTemplate and are stored in the postTemplates folder.

Version

### PostTemplate components are available in API version 29.0 and later.

Fields

**Field Name** **Field Type** **Description**

`default` boolean

Required. Specifies whether this is the default post template for the given object.

When set to `true`, this post template is used by approval processes that are
associated with the same object and don’t specify a post template.

When an object has no default post template, each of its approval processes uses
the system default post template, unless the approval process specifies its own
post template.

`description` string Optional description of the post template.


### Metadata Types ProductAttributeSet

**Field Name** **Field Type** **Description**

`fields` string[]

Required. An array of up to four fields to include in approval request posts.

If the approval object is a detail object in a master-detail relationship, `Owner`
isn’t available for approval page layouts or approval post templates.

`label` string Required. Name of the post template. This non-unique label is different from the
unique name of the post template.

Declarative Metadata Sample Definition

The following is an example of a PostTemplate component:

```
<PostTemplate xmlns="http://soap.sforce.com/2006/04/metadata">

   <default>false</default>

   <fields>NumberOfEmployees</fields>

   <fields>NumberofLocations__c</fields>

   <fields>PartnerAccount</fields>

   <fields>LeadCustomFieldNumber__c</fields>

   <label>My Lead Post Template</label>

</PostTemplate>

```

The following is an example package manifest that references the previous PostTemplate component.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>Lead.leadtemplate</members>

     <name>PostTemplate</name>

   </types>

   <version>29.0</version>

</Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### ProductAttributeSet

Represents the ProductAttribute information being used as and attribute such as color_ _c, size_ _c .

Version

### ProductAttributeSet components are available in API version 54 and later.


### Metadata Types PresenceDeclineReason

Special Access Rules

Fields

**Field Name** **Field Type** **Description**

`description` string A meaningful explanation of the attribute set.

`developerName` string A unique name for the attribute set.

`masterLabel` string The name of the attribute set.

`productAttributeSetItems` ProductAttributeSetItem A list of ProductAttributeSetItem.

### PresenceDeclineReason

Represents an Omni-Channel decline reason that agents can select when declining work requests. This type extends the Metadata
metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### PresenceDeclineReason components have the suffix .presenceDeclineReason and are stored in the

`presenceDeclineReasons` folder.

Version

### PresenceDeclineReason components are available in API version 44.0 and later.

Special Access Rules

This type is available only if Omni-Channel is enabled in your org.

Fields

**Field Name** **Field Type** **Description**

`label` string The label for the decline reason.

Declarative Metadata Sample Definition

The following is an example of a PresenceDeclineReason component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <PresenceDeclineReason xmlns="http://soap.sforce.com/2006/04/metadata">

      <label>Incorrect queue</label>

   </PresenceDeclineReason>

```


### Metadata Types PresenceUserConfig

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>PresenceDeclineReason</name>

      </types>

      <version>44.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### PresenceUserConfig

Represents a configuration that determines a presence user’s settings.

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### PresenceUserConfig components have the suffix .presenceUserConfig and are stored in the presenceUserConfigs

folder.

Version

### PresenceUserConfig components are available in API version 44.0 and later.

Special Access Rules

This type is available only if Omni-Channel is enabled in your org.

Fields

**Field Name** **Field Type** **Description**

`acwExtensionDuration` int The maximum length of time, measured in seconds, an agent can spend
on After Conversation Work (ACW) each time they extend the timer. You

must set this field if `hasAcwExtensionEnabled` is set to `true` .
Specify a value from 10 through 3600. Available in API version 65.0 and
later.

`afterConvoWorkMaxTime` int The maximum length of time, measured in seconds, an agent has to
complete After Conversation Work (ACW). You must set this field if


Metadata Types PresenceUserConfig

**Field Name** **Field Type** **Description**

`hasAfterConvoWorkTimer` is set to `true` . Specify a value from
10 through 3600. Available in API version 65.0 and later.

`assignments` PresenceConfigAssignments

Specifies how presence configurations are assigned to Omni-Channel
users. Presence configurations can be assigned to sets of users or to sets
of profiles.

`capacity` int Required. The maximum number of work units an agent can be assigned
at one time.

`declineReasons` string Specifies the list of decline reasons that an agent can select when they
decline a work.

`enableAutoAccept` boolean

`enableDecline` boolean

`enableDeclineReason` boolean

Indicates whether work items that are routed to agents are automatically
accepted ( `true` ) or not ( `false` ). Available only if `enableDecline`
is set to `false` .

Indicates whether agents can decline work items that are routed to them
( `true` ) or not ( `false` ). Available only if `enableAutoAccept` is
set to `false` .

Indicates whether agents can select a reason for declining work requests
( `true` ) or not ( `false` ). This can be selected only if decline reasons are
enabled.

`enableDisconnectSound` boolean Indicates whether a sound is played when agents are disconnected from
Omni-Channel ( `true` ) or not ( `false` ).

`enableRequestSound` boolean Indicates whether a sound plays with incoming work requests ( `true` )
or not ( `false` ). Set to `true` by default.

`hasAcwExtensionEnabled` boolean If set to `true`, agents can extend their After Conversation Work (ACW)
time. Available only if `hasAfterConvoWorkTimer` is set to `true` .

If set to `true`, you must also set the `acwExtensionDuration`
and `maxExtensions` fields. The default value is `false` Available in
API version 65.0 and later..

`hasAfterConvoWorkTimer` boolean If set to `true`, After Conversation Work (ACW) time can be configured
for the user. If set to `true`, you must also set the

`afterConvoWorkMaxTime` field. The default value is
`false` Available in API version 65.0 and later..

`interruptibleCapacity` int Indicates the maximum number of work units using interruptible capacity
that can be pushed to an agent at a time. An empty value defaults this

field to the value set in the `capacity` field. Available in API version
57.0 and later when the Interruptible Capacity feature is enabled.

`label` string The label of the presence configuration.

`maxExtensions` string The maximum number of times an agent can extend their After Work
Conversation (ACW) time. Specify a value from 1 through 10. You must


Metadata Types PresenceUserConfig

**Field Name** **Field Type** **Description**

set this field if `hasAcwExtensionEnabled` is set to `true` .
Available in API version 65.0 and later.

`presenceStatusOnDecline` string

The presence status that’s automatically assigned to the agent when
the agent declines a work item. Available only if `enableDecline` is
set to `true` .

`presenceStatusOnPushTimeout` string The presence status that’s automatically assigned to the agent when
the agent doesn’t respond to a work item before push timeout occurs.

PresenceConfigAssignments

Represents the assignments of an org’s profiles and users to a Presence configuration.

**Field Name** **Field Type** **Description**

`profiles` PresenceConfigProfileAssignments Specifies the profiles that are associated with a specific presence configuration.

`users` PresenceConfigUserAssignments Specifies the users that are associated with a specific presence configuration.

PresenceConfigProfileAssignments

Represents the profiles associated with a specific presence configuration.

**Field Name** **Field Type** **Description**

`profile` string Specifies the name of the profile associated with a specific presence
configuration.

PresenceConfigUserAssignments

Represents the users associated with a specific presence configuration.

**Field Name** **Field Type** **Description**

`user` string Specifies the username of the user associated with a specific presence
configuration.

Declarative Metadata Sample Definition

The following is an example of a PresenceUserConfig component.

```
<?xml version="1.0" encoding="UTF-8"?>

<PresenceUserConfig xmlns="http://soap.sforce.com/2006/04/metadata">

   <assignments>

     <profiles>

        <profile>standard</profile>

```


### Metadata Types PricingActionParameters

```
        </profiles>

        <users>

           <user>jdoe@example.com</user>

        </users>

      </assignments>

      <capacity>5</capacity>

      <declineReasons>Incorrect_queue</declineReasons>

      <enableAutoAccept>false</enableAutoAccept>

      <enableDecline>true</enableDecline>

      <enableDeclineReason>true</enableDeclineReason>

      <enableDisconnectSound>true</enableDisconnectSound>

      <enableRequestSound>true</enableRequestSound>

      <label>My presence configuration</label>

      <presenceStatusOnDecline>Away</presenceStatusOnDecline>

      <presenceStatusOnPushTimeout>Break</presenceStatusOnPushTimeout>

   </PresenceUserConfig>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>PresenceUserConfig</name>

      </types>

      <version>44.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### PricingActionParameters

Represents the pricing action that's associated with a context definition and pricing procedure.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

### PricingActionParameters components have the suffix .pricingActionParameters and are stored in the

`pricingActionParameters` folder.


Metadata Types PricingActionParameters

Version

PricingActionParameters components are available in API version 60.0 and later.

Special Access Rules

This metadata type is available with Salesforce Pricing.

Fields

**Field Name** **Description**

```
contextDefinition

contextMapping

developerName

effectiveFrom

effectiveTo

```

**Field Type**
string

**Description**

Required.

Context definition record that's associated with the pricing action.

**Field Type**
string

**Description**

Required.

Context mapping record that's associated with the pricing action.

**Field Type**
string

**Description**

Required.

Unique name of the pricing action parameter record.

The name must begin with a letter and use only alphanumeric characters and
underscores. The name must not include spaces, end with an underscore, or have two
consecutive underscores.

**Field Type**
dateTime

**Description**

Required.

Date and time from when the pricing action becomes effective.

**Field Type**
dateTime


Metadata Types PricingActionParameters

**Field Name** **Description**

**Description**
Date and time till when the pricing action is in effect.

```
masterLabel

objectName

pricingProcedure

```

**Field Type**
string

**Description**

Required.

Master label of the pricing action parameter.

**Field Type**
string

**Description**
Name of the object that's associated with the pricing action. Valid values are:

**•** `Case`

**•** `Contract`

**•** `Opportunity`

**•** `Order`

**•** `Quote`

**•** `SalesAgreement`

**•** `WorkOrder`

**Field Type**
string

**Description**
Pricing procedure record that's associated with this pricing action.

Declarative Metadata Sample Definition

The following is an example of a PricingActionParameters component.

```
<PricingActionParameters xmlns="http://soap.sforce.com/2006/04/metadata">

   <developerName>CMEDefaultActionParameters</developerName>

   <objectName>ORDER</objectName>

   <pricingProcedure>PP</pricingProcedure>

   <effectiveFrom>2024-04-08T07:32:00.000Z</effectiveFrom>

   <effectiveTo>2024-04-11T07:32:00.000Z</effectiveTo>

   <contextDefinition>SalesTransactionContext__stdctx</contextDefinition>

   <contextMapping>SalesAgreementEntitiesMapping</contextMapping>

   <masterLabel>PAP_test</masterLabel>

</PricingActionParameters>

```


### Metadata Types PricingRecipe

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>PricingActionParameters</name>

      </types>

      <version> 66.0 </version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### PricingRecipe

Represents the data models or sets of objects of a particular cloud that the pricing data store consumes during design time and run
time.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

### PricingRecipe components have the suffix .pricingRecipe and are stored in the pricingRecipe folder.

Version

### PricingRecipe components are available in API version 60.0 and later.

Special Access Rules

This metadata type is available with Salesforce Pricing.

Fields

**Field Name** **Description**

```
defaultPricingProcedure

```

**Field Type**

[ExpressionSetDefinition](https://developer.salesforce.com/docs/atlas.en-us.260.0.industries_reference.meta/industries_reference/meta_expressionsetdefinition.htm)

**Description**
Expression set definition that's associated with this pricing recipe setting.


Metadata Types PricingRecipe

**Field Name** **Description**

```
defaultPricingProcedureDeveloperName

defaultPricingProcedureId

developerName

isActive

isInternal

masterLabel

pricingRecipeTableMapping

```

**Field Type**
string

**Description**
For internal use only.

**Field Type**
string

**Description**
ID of the pricing procedure of the pricing recipe.

**Field Type**
string

**Description**

Required.

API name of the pricing recipe.

**Field Type**
boolean

**Description**
Indicates whether the pricing recipe is active ( `true` ) or not ( `false` ).

The default value is `false`

**Field Type**
boolean

**Description**
Indicates whether the price recipe record is created internally by the Salesforce platform
( `true` ) or not ( `false` ).

The default value is `false`

**Field Type**
string

**Description**

Required.

Name for pricing recipe that's defined when the pricing recipe is created.

**Field Type**

PricingRecipeTableMapping[]

**Description**
Mapping of the pricing components of a lookup table with the chosen pricing recipe.


Metadata Types PricingRecipe

PricingRecipeTableMapping

Represents the mapping of the lookup table with the chosen pricing recipe.

**Field Name** **Description**

```
isInternal

lookupTable

lookupTableDeveloperName

pricingComponentType

pricingProcedureOutputMapList

```

**Field Type**
boolean

**Description**
Indicates whether the price recipe field mapping record is created internally by the
Salesforce platform ( `true` ) or not ( `false` ).

The default value is `false` .

**Field Type**

[DecisionTable](https://developer.salesforce.com/docs/atlas.en-us.260.0.industries_reference.meta/industries_reference/meta_decisiontable.htm)

[DecisionMatrixDefinition](https://developer.salesforce.com/docs/atlas.en-us.260.0.industries_reference.meta/industries_reference/meta_decisionmatrixdefinition.htm)

**Description**
Lookup table that's associated with either a decision matrix or decision table.

**Field Type**
string

**Description**
For internal use only.

**Field Type**
string

**Description**
Pricing component field data that the decision table is built on.

Valid values are:

**•** `AttributeDiscount`

**•** `BundleDiscount`

**•** `DerivedPricing`

**•** `ListPrice`

**•** `PriceAdjustmentMatrix`

**•** `PromotionsDiscount`

**•** `VolumeDiscount`

**•** `VolumeTierDiscount`

**•** `DiscountDistributionService` . This value is available in API version
60.0 and later.

**•** `MinimumPrice` . Available in API version 62.0 and later.

**Field Type**

PricingProcedureOutputMap[]


Metadata Types PricingRecipe

**Field Name** **Description**

**Description**
List of the mappings of the outputs of the pricing procedures to the associated lookup
tables. Available in API version 60.0 and later.

```
pricingRecipe

```

**Field Type**
string

**Description**

Required.

Pricing data store that's associated with this pricing recipe field mapping.

PricingProcedureOutputMap

Represents the mapping of the outputs of the pricing procedures to the associated lookup tables. Each record specifies the output
mapping of the associated lookup table based on the pricing component type specified in the PricingRecipeTableMapping object.

**Field Name** **Description**

```
fieldName

isPricingRecipeActive

outputFieldName

outputFieldNameString

outputType

```

**Field Type**
string

**Description**
For internal use only.

**Field Type**
boolean

**Description**
Indicates whether the associated pricing recipe is active ( `true` ) or not ( `false` ).

The default value is `false` .

**Field Type**
string

**Description**
Field name that contains the output type that's generated from the pricing element.

**Field Type**
string

**Description**
Derived field that references a specific column in a decision table or decision matrix.

**Field Type**
string


Metadata Types PricingRecipe

**Field Name** **Description**

**Description**
Output type that's generated from a pricing element.

Valid values are:

**•** `AdjustmentType`

**•** `AdjustmentValue`

**•** `CustomOutput`

**•** `HashOutput`

**•** `UnitPrice`

```
pricingElementType

```

**Field Type**
PricingElementType (enumeration of type string)

**Description**
Type of pricing element, which is a derived field from
`PricingRecipeTableMapping.PricingComponentType` .

Valid values are:

**•** `AssetDiscovery`

**•** `AttributeDiscount`

**•** `BundleDiscount`

**•** `DerivedPricing`

**•** `DiscountDistributionService`

**•** `ListPrice`

**•** `MinimumPrice`

**•** `PriceAdjustmentMatrix`

**•** `PriceRevision`

**•** `PromotionsDiscount`

**•** `RuleFetch`

**•** `VolumeDiscount`

**•** `VolumeTierDiscount`

Declarative Metadata Sample Definition

The following is an example of a PricingRecipe component.

```
<PricingRecipe xmlns="http://soap.sforce.com/2006/04/metadata">

   <defaultPricingProcedureId> </defaultPricingProcedureId>

   <developerName>CMEDefaultRecipe</developerName>

   <isActive>false</isActive>

   <isInternal>false</isInternal>

   <masterLabel>CMEDefaultRecipe</masterLabel>

   <pricingRecipeTableMapping>

     <isInternal>false</isInternal>

```


### Metadata Types Profile

```
   <lookupTableDeveloperName>Bundle_Based_Adjustment_Decision_Table</lookupTableDeveloperName>

        <pricingComponentType>CUSTOMDISCOUNT</pricingComponentType>

        <fileBasedDecisionTableName>Bundle Based Adjustment

   Entries</fileBasedDecisionTableName>

        <pricingProcedureOutputMapList>

           <fieldName>AdjustmentValue</fieldName>

           <isPricingRecipeActive>false</isPricingRecipeActive>

           <outputFieldName>0lPxx000000000f</outputFieldName>

           <outputFieldNameString>false</outputFieldNameString>

           <outputType>AdjustmentValue</outputType>

       <pricingElementType>BundleDiscount</pricingElementType>

        </pricingProcedureOutputMapList>

        <pricingProcedureOutputMapList>

           <fieldName>AdjustmentType</fieldName>

           <isPricingRecipeActive>false</isPricingRecipeActive>

           <outputFieldName>0lPxx000000000m</outputFieldName>

           <outputFieldNameString>false</outputFieldNameString>

           <outputType>AdjustmentType</outputType>

       <pricingElementType>BundleDiscount</pricingElementType>

        </pricingProcedureOutputMapList>

        <pricingRecipe>CMEDefaultRecipe</pricingRecipe>

      </pricingRecipeTableMapping>

   </PricingRecipe>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>PricingRecipe</name>

      </types>

      <version> 66.0 </version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### Profile

Represents a user profile. A profile defines a user’s permission to perform different functions within Salesforce. This type extends the
Metadata metadata type and inherits its `fullName` field.

In API version 29.0 and later, you can retrieve and deploy access settings for these managed components in profiles and permission sets:

**•** Apex classes

**•** Apps

**•** Custom field permissions


Metadata Types Profile

**•** Custom object permissions

**•** Custom tab settings

**•** External data sources

**•** Record types

**•** Visualforce pages

In API version 51.0 and later, you can retrieve and deploy access settings for login flows. For more information, see Managed Component
Access in the Components in a Module section of Sample `package.xml` Manifest Files.

As of API version 50.0 and later, only users with correct permissions can view profile names other than their own if the Profile Filtering
setting is enabled.

Important: Profile names are also exposed when users with permissions to perform the following tasks take these actions:

**•** Create a tab or record type with a wizard step that includes the assignment of tabs and record types to profiles.

**•** Configure a login flow where viewing profile lists is required to make flow associations.

**•** Set up delegated admins where looking up profiles is needed to identify assignable profiles.

**•** Administer an org as a delegated customer admin.

**•** Administer an org as a delegated admin to view and assign profiles of the delegated group.

Declarative Metadata File Suffix and Directory Location

The file suffix is `.profile` . There's one file for each profile, stored in the `profiles` folder in the corresponding package directory.

Version

Profiles are available in API version 10.0 and later.

Special Access Rules

As of Summer ’20 and later, Customer Portal and Partner Portal users can’t access this type.

To view the following settings, assignments, and permissions for standard and custom objects in a specified profile, the View Setup and
Configuration permission is required.

**•** Client settings

**•** Field permissions

**•** Layout assignments

**•** Object permissions

**•** Permission dependencies

**•** Permission set tab settings

**•** Permission set group components

**•** Record types


Metadata Types Profile

Fields

The content of a profile returned by Metadata API depends on the content requested in the `RetrieveRequest` message. For
example, profiles only include field-level security for fields included in custom objects returned in the same `RetrieveRequest` as
the profiles. The profile definition contains the following fields:

Important: We designed Profile metadata deployment to overlay the existing Profile settings in a target org. For example, if you
disable permissions for a profile, the newly disabled permission information isn't exported. To force all Profile changes to deploy
through metadata, including permission disablement, add code that explicitly indicates disabled permissions. For example, add
this code to the Profile metadata `.xml` file before deploying into a target org: `<value>false</value>` .

If you deploy a profile that doesn’t exist in the target org and don't specify any permissions or settings, then the resulting profile
contains all permissions and settings in the standard Minimum Access - Salesforce profile (API version 60.0 and later) or the standard
Standard User profile (API version 59.0 and earlier).

Note: As of API version 38.0, you can change field permissions to make a field editable using the Metadata API for fields that you
can't change through the user interface. For example, you can deploy `Asset.ProductCode` as an editable field even though
you can't through the user interface.

**Field Name** **Field Type** **Description**

`agentAccesses` ProfileAgentAccess[] Indicates which agents are visible to users assigned to
this profile. Available in API version 63.0 and later.

`applicationVisibilities` ProfileApplicationVisibility[] Indicates which apps are visible to users assigned to this
profile. In API version 29.0 and earlier, this field supports

custom apps only. In API version 30.0 and later, this field
supports both standard and custom apps.

`categoryGroupVisibilities` ProfileCategoryGroupVisibility[]

Indicates which data category groups are visible to users
assigned to this profile. Available in API version 41.0 and
later.

`classAccesses` ProfileApexClassAccess[] Indicates which top-level Apex classes have methods
that users assigned to this profile can execute.

`custom` boolean

`customMetadataTypeAccesses` ProfileCustomMetadataTypeAccess[]

`customPermissions` ProfileCustomPermissions[]

`customSettingAccesses` ProfileCustomSettingAccesses[]

Indicates whether the profile is a custom ( `true` ) or
standard ( `false` ) profile. Available in API version 30.0
and later.

Indicates the custom metadata types that are
read-accessible to a user assigned to this profile. Available
in API version 47.0 and later.

Indicates which custom permissions are available to users
assigned to this profile. Available in API version 31.0 and
later.

Indicates the custom settings that are read-accessible to
a user assigned to this profile. Available in API version
47.0 and later.

`description` string The profile description. Limit: 255 characters. Available
in API version 30.0 and later.


Metadata Types Profile

**Field Name** **Field Type** **Description**

`externalDataSourceAccesses` ProfileExternalDataSourceAccess[]

Indicates which data sources with identity type of `Per`
`User` are available to users assigned to this profile.
Available in API version 27.0 and later.

`fieldLevelSecurities` ProfileFieldLevelSecurity[] Indicates which fields are visible to a user assigned to this
profile, and the kind of access available (editable or

hidden). This field is available in API version 22.0 and
earlier.

`fieldPermissions` ProfileFieldLevelSecurity[] Indicates which fields are visible to a user assigned to this
profile, and the kind of access available (editable or

readable). This field is available in API version 23.0 and
later.

`flowAccesses` ProfileFlowAccess[] Indicates which flows can be accessed by a user assigned
to this profile. Available in API version 47.0 and later.

`fullName` string The name can only contain characters, letters, and the
underscore (_) character. The name must start with a

letter, and can’t end with an underscore or contain two
consecutive underscore characters.

Inherited from the Metadata component, this field isn’t
defined in the WSDL for this component. It must be
specified when creating, updating, or deleting. See
create() to see an example of this field specified for a call.

`layoutAssignments` ProfileLayoutAssignments[] Indicates which layout to use for this profile.

`loginFlows` LoginFlow[] Indicates a business process that you direct users to
before they access Salesforce.

`loginHours` ProfileLoginHours[]

`loginIpRanges` ProfileLoginIpRange[]

Indicates the hours within which a user with this profile
can log in. If not specified, the profile doesn’t restrict a
user’s login hours.

This field is available in API version 25.0 and later.

The list of IP address ranges from which users with a
particular profile can log in.

This field is available in API version 17.0 and later.

`objectPermissions` ProfileObjectPermissions[] Indicates which objects are accessible to a user assigned
to this profile, and the kind of access available (create,

read, edit, delete, and so on). In API version 28.0 and later,
this field is only retrieved when `allowRead` is `true` .

In API version 50.0 and later, editing standard objects on
standard profiles is disabled.

`pageAccesses` ProfileApexPageAccess[] Indicates which Visualforce pages that users assigned to
this profile can execute.


Metadata Types Profile

**Field Name** **Field Type** **Description**

`profileActionOverrides` ProfileActionOverride[] A list of the Lightning Experience Home page action
overrides that are assigned to this profile. When a user

logs in with a profile, a matching ProfileActionOverride
assignment takes precedence over existing overrides for
the Home tab specified in ActionOverride.

This field is available in API versions 37.0 to 44.0.

`recordTypeVisibilities` ProfileRecordTypeVisibility[]

`ServicePresenceStatusAccesses` ProfileServicePresenceStatusAccess[]
on page 1729

`tabVisibilities` ProfileTabVisibility[]

`userLicense` string

Indicates the visibility of record types for users assigned
to this profile. In API version 29.0 and later, this field isn’t
retrieved or deployed for inactive record types.

Indicates which Service presence statuses that the user
assigned to this profile can execute. Available in API
version 64.0 and later.

Indicates which record types are visible to a user assigned
to this profile, and therefore which tabs within an app
are visible.

The `User License` for the profile. A user license
determines the baseline of features that the user can
access. Every user must have exactly one user license.

This field is available in API version 17.0 and later.

`userPermissions` ProfileUserPermission[] Specifies a user permission (such as “API Enabled”) and
whether it’s enabled for this profile. This field retrieves

only enabled user permissions. Available in API version
29.0 and later.

LoginFlow

LoginFlow represents a business process that you direct users to before they access Salesforce. You can use Metadata API to define
[existing flows as login flows and to edit login flow definitions. To delete login flow definitions, use the Login Flow page.](https://help.salesforce.com/articleView?id=security_login_flow_associate.htm&language=en_US)

**Field Name** **Field Type** **Description**

`flow` string

Required only if the `uiLoginFlowType` is `VisualWorkflow` .
The `fullName` [of the Flow.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_visual_workflow.htm)

Before you can deploy the LoginFlow, the Flow referenced here must be
deployed in your org and its status must be `Active` .

```
flowtype

```

LoginFlowType Required. The value is `UI` .
(enumeration of type
string)

`friendlyname` string Required. The name of the LoginFlow.


Metadata Types Profile

**Field Name** **Field Type** **Description**

```
uiLoginFlowType

```

UiLoginFlowType Required. The type of login flow. These are valid values.
(enumeration of type

**•** `VisualWorkflow` [—Indicates a Salesforce Flow. You can create](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_visual_workflow.htm)

string)

these flows using Flow Builder.

**•** `VisualForce` —Indicates a flow created using Visualforce.

`useLightningRuntime` boolean Indicates if Lightning Runtime is used ( `true` ) or not ( `false` (default)).
Used only if `uiLoginFlowType` is `VisualWorkflow` .

`vfFlowPage` string Required only if the `uiLoginFlowType` is `VisualForce` . The
name of the VisualForce page.

`vfFlowPageTitle` string Required only if the `uiLoginFlowType` is `VisualForce` . The
name of the VisualForce page.

ProfileActionOverride

ProfileActionOverride represents a user profile-based override of an ActionOverride on a standard Home tab in Lightning Experience.

Note:

**•** ProfileActionOverride can be defined only on Profile for API version 39.0 to 44.0. In API version 45.0 and later, ProfileActionOverride
must be defined for CustomApplication instead. Beginning with API version 45.0, Home page assignments related to user
profile must also have a corresponding app assignment because more granular Home page assignments are supported. As a
result, ProfileActionOverride is defined for CustomApplication rather than Profile.

**•** ProfileActionOverride settings aren’t retrieved in the `.profile` file unless a Lightning page is referenced in the
`package.xml` file.

**Field Name** **Field Type** **Description**

`actionName` string Required. The possible values are the same as the actions you can
override:

**•** `accept`

**•** `clone`

**•** `delete`

**•** `edit`

**•** `list`

**•** `new`

**•** `tab`

**•** `view`

`content` string Set this field if `type` is set to `flexipage`,
`lightningcomponent`, `scontrol`, or `visualforce` . It refers

to the name of the Lightning page, Lightning component, s-control, or
Visualforce page to use as the override. To reference installed


Metadata Types Profile

**Field Name** **Field Type** **Description**

components, use this format:
_**`Component_namespace`**_ `__` _**`Component_name`**_ .

The size of the page being overridden.

The `Large` value represents the Lightning Experience desktop
environment and is valid only for the `flexipage` and

`lightningcomponent` types. The `Small` value represents the
Salesforce mobile app on a phone or tablet. The `Medium` value is
reserved for future use. The `null` value (which is the same as specifying
no value) represents Salesforce Classic.

The name of the sObject type being overridden. Valid values are
`standard` and `custom` .

This value must be `standard-home` when actionName is `tab` .

```
formFactor

```

FormFactor
(enumeration of type
string)

`pageOrSobjectType` string

`recordType` string The record type assigned to the ProfileActionOverride. If the
`PageOrSobjectType` is `standard-home`, this field is null.

```
type

```

ProfileAgentAccess

ActionOverrideType Required. Represents the type of action override. Valid values are
(enumeration of type described in ActionOverrideType.
string)

ProfileAgentAccess represents the agent access configuration for users assigned through a profile.

**Field Name** **Field Type** **Description**

`agentName` string Required. The name of the employee agent.

`enabled` boolean Required. Indicates whether users assigned to this profile can use the
Agentforce Employee Agent ( `true` ) or not ( `false` ).

ProfileApplicationVisibility

ProfileApplicationVisibility determines whether an app is visible to a user assigned to this profile.

**Field Name** **Field Type** **Description**

`application` string Required. The name of the app.

`default` boolean Required. Indicates whether the app is the default app ( `true` ) or not
( `false` ). Only one app per profile can be set to `true` .

`visible` boolean Required. Indicates whether this app is visible to users assigned to this
profile ( `true` ) or not ( `false` ).


Metadata Types Profile

ProfileCategoryGroupVisibility

ProfileCategoryGroupVisibility determines whether a data category group is visible to a user assigned to this profile. Available in API
version 41.0 and later.

ProfileCustomMetadataTypeAccess

ProfileCustomMetadataTypeAccess represents the custom metadata type access for users assigned to a profile. Available in API version
47.0 and later.

**Field** **Field Type** **Description**

`enabled` boolean Required. Indicates whether the records for this custom metadata
type are readable ( `true` ) or not ( `false` ).

`name` string Required. The custom metadata type name.

ProfileApexClassAccess

ProfileApexClassAccess determines which top-level Apex classes have methods that users assigned to this profile can execute.

**Field Name** **Field Type** **Description**

`apexClass` string Required. The Apex class name.

`enabled` boolean Required. Indicates whether users assigned to this profile can execute
methods in the top-level class ( `true` ) or not ( `false` ).

ProfileCustomPermissions

ProfileCustomPermissions represents the custom permissions access for users assigned to a profile. Only enabled custom permissions
are retrieved.


Metadata Types Profile

**Field Name** **Field Type** **Description**

`enabled` boolean Required. Indicates whether the custom permission is enabled ( `true` )
or not ( `false` ).

`name` string Required. The custom permission name.

ProfileCustomSettingAccesses

ProfileCustomSettingAccesses represents the custom setting access for users assigned to a profile. Available in API version 47.0 and later.

**Field** **Field Type** **Description**

`enabled` boolean Required. Indicates whether the records for this custom setting are
readable ( `true` ) or not ( `false` ).

`name` string Required. The custom setting name.

ProfileExternalDataSourceAccess

ProfileExternalDataSourceAccess represents the data source access for users with identity type of `Per User` . Available in API version
27.0 and later.

**Field Name** **Field Type** **Description**

`enabled` boolean Required. Indicates whether the data source is enabled ( `true` ) or not
( `false` ).

`externalDataSource` string The name of the external data source.

ProfileFieldLevelSecurity

ProfileFieldLevelSecurity represents the field level security for users assigned to a profile. In API version 30.0 and later, permissions for
required fields can’t be retrieved or deployed.

**Field Name** **Field Type** **Description**

`editable` boolean

`field` string

Required. Indicates whether this field is editable ( `true` ) or not ( `false` ).

In API version 30.0 and later, when deploying a new custom field, this
field is `false` by default.

Required. Indicates the name of the field.

When referencing shared Activity fields, specify Event or Task. For
example, `Event.Meeting__c` .


Metadata Types Profile

**Field Name** **Field Type** **Description**

`hidden` boolean

`readable` boolean

ProfileFlowAccess

Indicates whether this field is hidden ( `true` ) or not ( `false` ). This field
is available in API version 22.0 and earlier.

For portal profiles, this field is set to `true` by default in API version 19.0
and later.

Indicates whether this field is readable ( `true` ) or not ( `false` ). This field
is available in API version 23.0 and later. It replaces the `hidden` field.

In API version 30.0 and later, when deploying a new custom field, this
field is `false` by default.

For portal profiles, this field is set to `false` by default.

ProfileFlowAccess represents which flows a profile grants access to. Available in API version 47.0 and later.

**Field** **Field Type** **Description**

`enabled` boolean Required. Indicates whether users assigned this profile can access
the flow ( `true` ) or not ( `false` ). The default value is `false` .

`flow` string Required. The name of the flow to which access is granted.

ProfileLayoutAssignments

ProfileLayoutAssignments determines which layout to use for a profile and a given entity.

**Field Name** **Field Type** **Description**

`layout` string Required. Indicates the layout for this particular entity.

`recordType` string This field is optional. If the `recordType` of the record matches a layout
assignment rule, it uses the specified layout.

ProfileLoginHours

ProfileLoginHours restricts the days and times within which users with a particular profile can log in.

**Field Name** **Field Type** **Description**

_`weekday`_ `Start` string Specifies the earliest time on that day that a user with this profile can log
in. If a start time for a particular day is specified, an end time for that day

also must be specified. Start can’t be greater than end for a particular
day.

**•** Valid values for `weekday` : `monday`, `tuesday`, `wednesday`,
`thursday`, `friday`, `saturday`, or `sunday` . For example,


Metadata Types Profile

**Field Name** **Field Type** **Description**

`mondayStart` indicates the beginning of the login period for
Monday.

**•** Valid values for Start: the number of minutes since midnight. Must
be evenly divisible by 60 (full hours). For example, `300` is 5:00 AM.

_`weekday`_ `End` string Specifies the time on that day that a user with this profile must log out
by.

**•** Valid values for `weekday` : `monday`, `tuesday`, `wednesday`,
`thursday`, `friday`, `saturday`, or `sunday` . For example,
`mondayEnd` indicates the close of the login period for Monday.

**•** Valid values for End: the number of minutes since midnight. Must be
evenly divisible by 60 (full hours). For example, `1020` is 5:00 PM.

To delete login hour restrictions from a profile that previously had them, you must explicitly include an empty loginHours tag without
any start or end times.

ProfileLoginIpRange

ProfileLoginIpRange IP defines an IP address range that users with a particular profile can log in from.

**Field Name** **Field Type** **Description**

`description` string

Use this field to identify the purpose of the range, such as which part of
a network corresponds to this range. This field is available in API version
31.0 and later.

`endAddress` string Required. The end IP address for the range.

`startAddress` string Required. The start IP address for the range.

ProfileObjectPermissions

ProfileObjectPermissions represents a user's access to objects.

Note:

**•** In API version 18.0 and later, these permissions are disabled in new custom objects for any profiles where “View All Data” or
“Modify All Data” is disabled.

**•** In API version 50.0 and later, editing standard objects on standard profiles is disabled.

**Field Name** **Field Type** **Description**

`allowCreate` boolean

Indicates whether the object referenced by the `object` field can be
created by the users assigned to this profile ( `true` ) or not ( `false` ).

This field is named `revokeCreate` before version 14.0 and the logic
is reversed. The field name change and the update from `true` to


Metadata Types Profile

**Field Name** **Field Type** **Description**

`false` and the reverse is automatically handled between versions and
doesn’t require any manual editing of existing XML component files.

`allowDelete` boolean

`allowEdit` boolean

`allowRead` boolean

Indicates whether the object referenced by the `object` field can be
deleted by the users assigned to this profile ( `true` ) or not ( `false` ).

This field is named `revokeDelete` before version 14.0 and the logic
is reversed. The field name change and the update from `true` to

`false` and the reverse is automatically handled between versions and
doesn’t require any manual editing of existing XML component files.

Indicates whether the object referenced by the `object` field can be
edited by the users assigned to this profile ( `true` ) or not ( `false` ).

This field is named `revokeEdit` before version 14.0 and the logic is
reversed. The field name change and the update from `true` to `false`

and the reverse is automatically handled between versions and doesn’t
require any manual editing of existing XML component files.

Indicates whether the object referenced by the `object` field can be
seen by the users assigned to this profile ( `true` ) or not ( `false` ).

This field is named `revokeRead` before version 14.0 and the logic is
reversed. The field name change and the update from `true` to `false`

and the reverse is automatically handled between versions and doesn’t
require any manual editing of existing XML component files.

`modifyAllRecords` boolean Indicates whether all records for the object referenced by the `object`
field can be read, edited, or deleted by the users assigned to this profile

( `true` ) or not ( `false` ), regardless of the sharing settings for the object.
This setting is equivalent to the Modify All Data user permission limited
to the individual object level. Available in API version 15.0 and later.

This field isn’t available for all objects. Refer to the profile in the user
interface to determine which objects currently support these permissions.
Profiles with Modify All Data ignore `modifyAllRecords` entries in
Metadata API and don't return an error if Modify All Data is enabled on
the profile.

`object` string Required. The name of the object whose permissions are altered by this
profile, for example, `MyCustomObject__c` .

`viewAllFields` boolean

Indicates whether all fields and field data for the object referenced by
the `object` field can be read by the users assigned to this profile
( `true` ) or not ( `false` ). Available in API version 63.0 and later.

`viewAllRecords` boolean Indicates whether all records for the object referenced by the `object`
field can be read by the users assigned to this profile ( `true` ) or not

( `false` ), regardless of the sharing settings for the object. This setting
includes private records (records with no parent object). This setting is


Metadata Types Profile

**Field Name** **Field Type** **Description**

equivalent to the View All Data user permission limited to the individual
object level. Available in API version 15.0 and later.

This field isn’t available for all objects. Refer to the profile in the user
interface to determine which objects currently support these permissions.
Profiles with "View All Data" ignore `viewAllRecords` entries in the
Metadata API and don't return an error if View All Data is enabled on the
profile.

ProfileApexPageAccess

ProfileApexPageAccess determines which Visualforce pages that users assigned to this profile can execute.

**Field Name** **Field Type** **Description**

`apexPage` string Required. The Visualforce page name.

`enabled` boolean Required. Indicates whether users assigned to this profile can execute
the Visualforce page ( `true` ) or not ( `false` ).

ProfileRecordTypeVisibility

ProfileRecordTypeVisibility represents the visibility of record types for this profile. Record types let you offer different business processes,
picklist values, and page layouts to different users.

**Field Name** **Field Type** **Description**

`default` boolean Required. Indicates whether the record type is the default when users
with this profile create records for this object ( `true` ) or not ( `false` ).

`personAccountDefault` boolean When Person Accounts is enabled, this field indicates whether the record
type is this profile’s default person account record type ( `true` ) or not

( `false` ). When Person Accounts is disabled, this field’s value has no
impact.

Person accounts aren’t enabled by default in Salesforce. To request person
accounts, contact Salesforce.

`recordType` string Required. The record type name, for example
`Account.MyRecordType` .

`visible` boolean Required. Indicates whether this record type is visible to users assigned
to this profile ( `true` ) or not ( `false` ).


Metadata Types Profile

ProfileTabVisibility

ProfileTabVisibility represents the visibility of tabs for this profile. For version 17.0 and later, ProfileTabVisibility supports visibility of tabs
for standard objects. The manifest file must include the standard object corresponding to a standard tab to retrieve the tab visibility in
a profile.

**Field Name** **Field Type** **Description**

`tab` string Required. The name of the tab.

```
visibility

```

TabVisibility Required. Indicates the visibility of the tab. Valid values are:
(enumeration of type

**•** `DefaultOff` —The tab is available on the All Tabs page. Users

string)

can individually customize their display to make the tab visible in
any app.

**•** `DefaultOn` —The tab is available on the All Tabs page and appears
in the visible tabs for its associated app. Users can individually
customize their display to hide the tab or make it visible in other
apps.

**•** `Hidden` —The tab isn’t available on the All Tabs page or visible in
any apps.

In API version 36.0 and earlier, `Hidden` is returned only if
`visibility` was set using the API. If it was set to `Hidden` from the
profile in Salesforce, the API doesn’t return a visibility value. For version
37.0 and later, when tab visibility is set to hidden, the API returns
`Hidden`, regardless of how the value was set.

ProfileUserPermission

ProfileUserPermission represents an app or system permission for a profile. Use one of these elements for each permission.

**Field** **Field Type** **Description**

`enabled` boolean Required. Indicates whether the permission is enabled ( `true` ) or
disabled ( `false` ).

`name` string Required. The permission name.

ProfileServicePresenceStatusAccess

Represents the presence statuses that reps assigned to this profile have access. Available in API version 64.0 and later.

**Field** **Field Type** **Description**

`servicePresenceStatus` string Required. The name of Service Presence Status.

`enabled` boolean Required. Indicates whether the rep assigned to this profile has
access to the presence status ( `true` ) or not ( `false` ).


Metadata Types Profile

Java Sample

This sample uses picklists, profiles, record types, and a custom app:

```
   public void profileSample() {

     try {

      // Create an expense report record, tab and app...

      CustomObject expenseRecord = new CustomObject();

      expenseRecord.setFullName("ExpenseReport__c");

      expenseRecord.setLabel("Expense Report");

      expenseRecord.setPluralLabel("Expense Reports");

      expenseRecord.setDeploymentStatus(DeploymentStatus.Deployed);

      expenseRecord.setSharingModel(SharingModel.ReadWrite);

      CustomField nameField = new CustomField();

      nameField.setType(FieldType.AutoNumber);

      nameField.setLabel("Expense Report Number");

      nameField.setDisplayFormat("ER-{0000}");

      expenseRecord.setNameField(nameField);

      AsyncResult[] arsExpenseRecord =

        metadataConnection.create(new Metadata[] {expenseRecord});

      Picklist expenseStatus = new Picklist();

      PicklistValue unsubmitted = new PicklistValue();

      unsubmitted.setFullName("Unsubmitted");

      PicklistValue submitted = new PicklistValue();

      submitted.setFullName("Submitted");

      PicklistValue approved = new PicklistValue();

      approved.setFullName("Approved");

      PicklistValue rejected = new PicklistValue();

      rejected.setFullName("Rejected");

      expenseStatus.setPicklistValues(new PicklistValue[] {

        unsubmitted, submitted, approved, rejected}

      );

      CustomField expenseStatusField = new CustomField();

      expenseStatusField.setFullName(

        "ExpenseReport__c.ExpenseStatus__c"

      );

      expenseStatusField.setLabel("Expense Report Status");

      expenseStatusField.setType(FieldType.Picklist);

      expenseStatusField.setPicklist(expenseStatus);

      AsyncResult[] arsStatusField =

        metadataConnection.create(new Metadata[]

           {expenseStatusField});

      CustomTab expenseTab = new CustomTab();

      expenseTab.setFullName("ExpenseReport__c");

      expenseTab.setMotif("Custom70: Handsaw");

      expenseTab.setCustomObject(true);

      AsyncResult[] arsTab =

        metadataConnection.create(new Metadata[] {expenseTab});

```


Metadata Types Profile

```
      CustomApplication application = new CustomApplication();

      application.setFullName("ExpenseForce");

      application.setTab(new String[] {expenseTab.getFullName()});

      AsyncResult[] arsApp =

        metadataConnection.create(new Metadata[] {application});

      // Employees and managers have the same app visibility...

      ProfileApplicationVisibility appVisibility =

        new ProfileApplicationVisibility();

      appVisibility.setApplication("ExpenseForce");

      appVisibility.setVisible(true);

      Profile employee = new Profile();

      employee.setFullName("Employee");

      employee.setApplicationVisibilities(

        new ProfileApplicationVisibility[] {appVisibility}

      );

      AsyncResult[] arsProfileEmp =

      metadataConnection.create(new Metadata[] {employee});

      Profile manager = new Profile();

      manager.setFullName("Manager");

      manager.setApplicationVisibilities(

        new ProfileApplicationVisibility[] {appVisibility}

      );

      AsyncResult[] arsProfileMgr =

        metadataConnection.create(new Metadata[] {manager});

      // But employees and managers have different access

      // to the state of the expense sheet

      RecordType edit = new RecordType();

      edit.setFullName("ExpenseReport__c.Edit");

      RecordTypePicklistValue editStatuses =

        new RecordTypePicklistValue();

      editStatuses.setPicklist("ExpenseStatus__c");

      editStatuses.setValues(new PicklistValue[]

        {unsubmitted, submitted});

      edit.setPicklistValues(new RecordTypePicklistValue[]

        {editStatuses});

      AsyncResult[] arsRecTypeEdit =

        metadataConnection.create(new Metadata[] {edit});

      RecordType approve = new RecordType();

      approve.setFullName("ExpenseReport__c.Approve");

      RecordTypePicklistValue approveStatuses =

        new RecordTypePicklistValue();

      approveStatuses.setPicklist("ExpenseStatus__c");

      approveStatuses.setValues(new PicklistValue[]

        {approved, rejected});

      approve.setPicklistValues(new RecordTypePicklistValue[]

        {approveStatuses});

      AsyncResult[] arsRecTypeApp =

        metadataConnection.create(new Metadata[] {approve});

     } catch (ConnectionException ce) {

```


Metadata Types Profile

```
      ce.printStackTrace();

     }

   }

```

Declarative Metadata Sample Definition

The definition of a profile in an organization with a custom app, custom object, record type, tab, and user permission is:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Profile xmlns="http://soap.sforce.com/2006/04/metadata">

      <applicationVisibilities>

        <application>PubApps__Myriad_Publishing</application>

        <default>false</default>

        <visible>true</visible>

      </applicationVisibilities>

      <custom>true</custom>

      <objectPermissions>

        <object>TestWeblinks__c</object>

        <allowCreate>true</allowCreate>

        <allowDelete>true</allowDelete>

        <allowEdit>true</allowEdit>

        <allowRead>true</allowRead>

        <viewAllRecords>false</viewAllRecords>

        <modifyAllRecords>false</modifyAllRecords>

        <viewAllFields>false</viewAllFields>

      </objectPermissions>

      <recordTypeVisibilities>

        <default>true</default>

        <recordType>TestWeblinks__c.My First Recordtype</recordType>

        <visible>true</visible>

      </recordTypeVisibilities>

      <tabVisibilities>

        <tab>Myriad Publications</tab>

        <visibility>DefaultOn</visibility>

      </tabVisibilities>

      <userPermissions>

        <enabled>true</enabled>

        <name>APIEnabled</name>

      </userpermissions>

   </Profile>

```

Usage

To create custom profiles, we recommend that you use the Profile object instead of the `deploy()` call on the Profile Metadata type.
The Profile object allows you to create empty profiles that start without any permissions enabled except for required permissions for the
profile’s user license.

When you use the `retrieve()` call to get information about profiles, the returned `.profile` files only include security settings
for the other metadata types referenced in the retrieve request. Exceptions include user permissions, IP address ranges, and login hours,
which are always retrieved. For example, the following `package.xml` file contains a `types` element that matches all custom


Metadata Types Profile

objects. The returned profiles contain object and field permissions for all custom objects in your organization but don’t include permissions
for standard objects, such as Account, and standard fields.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>CustomObject</name>

      </types>

     <types>

        <members>*</members>

        <name>Profile</name>

      </types>

      <version>66.0</version>

   </Package>

```

The wildcard “*” on CustomObject doesn’t match standard objects. This wildcard behavior helps you to avoid making unintended,
high-impact profile changes. If you create a few custom objects in a Developer Edition organization, `retrieve()` the information,
and later `deploy()` the custom objects to your production org, the profile and field-level security for all your standard objects and
fields aren’t overwritten. You can only overwrite these standard objects and fields by explicitly creating separate `types` elements for
the objects or fields.

Metadata API intentionally makes it difficult to include standard fields in `retrieve()` calls to prevent unexpected profile changes.
But you can still retrieve and deploy profile permissions for custom and standard fields in standard objects, such as Account.

This `package.xml` file allows you to return profile permissions for Account standard and custom fields. Note how the standard
Account object is defined in a `types` element by specifying it as a member of a CustomObject type.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Account</members>

        <name>CustomObject</name>

      </types>

     <types>

        <members>*</members>

        <name>Profile</name>

      </types>

      <version>66.0</version>

   </Package>

```

This `package.xml` file allows you to return profile permissions for the `MyCustomField__c` custom field in the Account object.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <types>

        <members>Account.MyCustomField__c</members>

        <name>CustomField</name>

     </types>

     <types>

        <members>*</members>

        <name>Profile</name>

     </types>

     <version>66.0</version>

   </Package>

```


### Metadata Types ProfileActionOverride

To retrieve field permissions for relationship fields, remove the “Id” part of the field. For example, in this `package.xml` file, to retrieve
field permissions for the `AccountId` field for Contacts, you reference this field as `Contact.Account` not
`Contact.AcccountId` .

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <types>

        <members>Contact.Account</members>

        <name>CustomField</name>

     </types>

     <types>

        <members>*</members>

        <name>Profile</name>

     </types>

     <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

_Salesforce DX Developer Guide_ [: Retrieve Changes to Profiles with Source Tracking](https://developer.salesforce.com/docs/atlas.en-us.260.0.sfdx_dev.meta/sfdx_dev/sfdx_dev_source_tracking_source_tracking_profiles.htm)

### ProfileActionOverride

Represents an override of an ActionOverride by a user profile. You can use it to override an ActionOverride on a standard Home tab or
object record page in Lightning Experience. When a user logs in with a profile, a matching ProfileActionOverride assignment takes
precedence over existing overrides for the Home tab or record page specified in ActionOverride. In API versions 39.0 to 44.0, you can
access ProfileActionOverride by accessing its encompassing CustomApplication on page 698 or Profile on page 1716 metadata types. In
API version 45.0 and later, you can access ProfileActionOverride only by accessing its encompassing CustomApplication on page 698.

Note: ProfileActionOverrides aren’t supported in packaging. They’re supported in change sets, but you have to add them manually.

File Suffix and Directory Location

Profile-based action overrides are defined as part of a custom application or profile.

Version

### ProfileActionOverrides are available in API version 39.0 and later. ProfileActionOverride can be defined on Profile or CustomApplication for API version 39.0 to 44.0. In API version 45.0 and later, ProfileActionOverride must be defined for CustomApplication instead. Beginning with API version 45.0, Home page assignments related

to user profile must also have a corresponding app assignment because more granular Home page assignments are supported. As a
result, ProfileActionOverride is defined for CustomApplication rather than Profile.


Metadata Types ProfileActionOverride

Fields

**Field Name** **Field Type** **Description**

`actionName` string

The name of the action. The only valid values are `Tab` and `View` .

If `pageOrSobjectType` is `standard-home`, this field must be
`Tab` . The `Tab` action is supported only when ProfileActionOverride is
being specified as part of a Profile in API version 39.0 to 44.0.

In API version 45.0 and later, this action is supported only when
ProfileActionOverride is being specified as part of a CustomApplication,
`pageOrSobjectType` is `standard-home`, and this field is `Tab` .

If `pageOrSobjectType` is `record-home`, this field must be
`View` . The `View` action is supported only when ProfileActionOverride
is being specified as part of a CustomApplication.

`content` string Read-only. Represents the name of the Lightning page being used as
the override.

```
formFactor

```

FormFactor The size of the page being overridden. The `Large` value represents
(enumeration of the Lightning Experience desktop environment.
type string)

`pageOrSobjectType` string

`recordType` string

The name of the page being overridden. The only valid values are
`record-home` and `standard-home` . If the `actionName` is
`Tab`, this field must be `standard-home`

The record type associated with the override. If
`pageOrSobjectType` is `standard-home`, this field must be
`null` . This field is required when `actionName` is set to `View` .

```
type

```

Usage

ActionOverrideType Read-only. The type of action override. The only valid value is
(enumeration of `flexipage` .
type string)

You can't delete custom app ProfileActionOverrides by deploying with `destructiveChange.xml` . To delete a ProfileActionOverride,
retrieve the app. In the app definition file, find the `<profileActionOverrides>` section, and remove the `<content>` row.
Then, change the `<type>` value in that same section to `default` instead of `flexipage` . Do this for every override you want to
reset. After making the changes, rezip the folder and deploy.

You can remove one override at a time each with its own deploy, or you can remove multiple overrides in a single deploy. However, we
recommend that you do a fresh retrieve every time you want to delete a new override. Don’t use a previously retrieved file.

Avoid creating duplicate ProfileActionOverrides in your org. Duplicate ProfileActionOverrides can cause problems, including being unable
to select or deselect the **Disable end user personalization of nav items in this app** option in app settings and the **Disable Navigation**
**Bar Personalization in Lightning Experience** User Interface setting.


### Metadata Types ProfilePasswordPolicy

Declarative Metadata Sample Definition

You can define a ProfileActionOverride like this.

```
   <CustomApplication xmlns="http://soap.sforce.com/2006/04/metadata">

      <profileActionOverrides>

        <actionName>View</actionName>

        <content>CustomObjectFlexiPage</content>

        <formFactor>Large</formFactor>

        <pageOrSobjectType>TestObj__c</pageOrSobjectType>

        <type>Flexipage</type>

        <profile>standard</profile>

        <recordType>TestObj__c.TestRecordType</recordType>

      </profileActionOverrides>

      <defaultLandingTab>standard-home</defaultLandingTab>

      <formFactors>Large</formFactors>

      <label>My Custom App</label>

      <tab>standard-Account</tab>

      <tab>standard-Opportunity</tab>

      <uiType>Lightning</uiType>

      <navType>Standard</navType>

   </CustomApplication>

```

Here’s an example `package.xml` .

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>MyCustomApp</members>

        <name>CustomApplication</name>

      </types>

      <version>39.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

### ProfilePasswordPolicy

Represents a profile’s password policies. Profile password policies override org-wide password policies for that profile’s users. Use
### ProfilePasswordPolicy to retrieve password policies for a given profile. This type extends the Metadata metadata type and inherits its

`fullName` field.

File Suffix and Directory Location

### ProfilePasswordPolicy components have the suffix .profilePasswordPolicy and are stored in the

`profilePasswordPolicies` folder.


Metadata Types ProfilePasswordPolicy

Version

ProfilePasswordPolicy components are available in API version 40.0 and later.

Fields

**Field Name** **Field Type** **Description**

`forgotPasswordRedirect` boolean If `true`, reset password links in forgot password emails don’t
immediately expire the first time they’re clicked. Instead, the links stay

active until a user confirms the password reset request on an interstitial
page. The default value is `false` .

This field is available in API version 43.0 and later.

`lockoutInterval` int

Required. The duration of the login lockout, in minutes. If users are locked
out, they must wait until the lockout period expires. Valid values: `0`, `15`,
`30`, `60` .

`maxLoginAttempts` int Required. The number of times a user can enter a wrong password before
getting locked out. Valid values: `0`, `3`, `5`, `10` .

`minimumPasswordLength` int Required. Minimum number of characters required for a password. Valid
values: `5`                                  - `50` .

`minimumPasswordLifetime` boolean If `true`, a user cannot change a password more than once in a 24-hour
period.

`obscure` boolean If `true`, answers to security questions are hidden as the user types.

`passwordComplexity` int Required. Level of complexity required for the character types in a user’s
password.

**•** If `0`, the password can contain any type of character.

**•** If `1`, the password must contain at least one alphabetic character
and 1 number.

**•** If `2`, the password must contain at least one alphabetic character,
one number, and one of the following special characters: ! # $ % _ = + < >.

**•** If `3`, the password must contain at least one number, one uppercase
letter, and one lowercase letter.

**•** If `4`, the password must contain at least one number, one uppercase
letter, one lowercase letter, and one of the following special
characters: ! # $ % - _ = + < >.

`passwordExpiration` int Required. Number of days until user passwords expire and must be
changed. Valid values:

**•** `0` —If set to `0`, the password never expires.

**•** `30`

**•** `60`


### Metadata Types ProfileSessionSetting

**Field Name** **Field Type** **Description**

**•** `90`

**•** `180`

**•** `365`

`passwordHistory` int Required. Number of previous passwords to save. Saving passwords is
required to ensure that users reset their password to a new, unique

password. This value must be set before a password reset succeeds. If
`0`, `passwordExpiration` must be set to `0` .

`passwordQuestion` int Required. If set to `1`, the answer to the password hint cannot contain
the password itself. If `0`, the answer has no restrictions.

`profile` string Required. Name of the user profile.

Declarative Metadata Sample Definition

The following is an example of a ProfilePasswordPolicy component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ProfilePasswordPolicy xmlns="http://soap.sforce.com/2006/04/metadata">

      <forgotPasswordRedirect>true</forgotPasswordRedirect>

      <lockoutInterval>30</lockoutInterval>

      <maxLoginAttempts>0</maxLoginAttempts>

      <minimumPasswordLength>7</minimumPasswordLength>

      <minimumPasswordLifetime>false</minimumPasswordLifetime>

      <obscure>false</obscure>

      <passwordComplexity>1</passwordComplexity>

      <passwordExpiration>0</passwordExpiration>

      <passwordHistory>0</passwordHistory>

      <passwordQuestion>1</passwordQuestion>

      <profile>platformportal</profile>

   </ProfilePasswordPolicy>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### ProfileSessionSetting

Represents a profile’s session settings. Use ProfileSessionSetting to retrieve the session settings for a given profile. This type extends the
Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ProfileSessionSetting components have the suffix .profileSessionSetting and are stored in the

`profileSessionSettings` folder.


Metadata Types ProfileSessionSetting

Version

ProfileSessionSetting components are available in API version 40.0 and later.

Fields

**Field Name** **Field Type** **Description**

`profile` string Required. Name of the user profile.

`requiredSessionLevel` SessionSecurityLevel Session security level.

`sessionPersistence` boolean Beta. If `true`, keep users logged in to their Experience Cloud site until
the session times out—even if they close their browser. Use

`sessionPersistence` to reduce how often users must log in to
their site. Applies only to the External Identity profile.

`sessionTimeout` int Required. Specifies how many minutes of inactivity elapse before a user’s
authenticated session times out. At the end of the session, the user must

log in again. This session timeout value applies to users of the profile
and overrides the org-wide timeout value. Changes to the org-wide
timeout value don’t apply to users of this profile. Valid values:

**•** `0` —2 Hours

**•** `15` —15 Minutes

**•** `30` —30 Minutes

**•** `60` —1 Hour

**•** `90` —90 Minutes

**•** `120` —2 Hours

**•** `240` —4 Hours

**•** `480` —8 Hours

**•** `720` —12 Hours

**•** `1440` —24 Hours

SessionSecurityLevel

Session security levels control access to certain types of resources based on the type of authentication used for logging in to the current
session. For example, username and password authentication requires the `standard` session security level. Multi-factor authentication
(MFA) requires `HIGH_ASSURANCE` .

**Field Name** **Field Type** **Description**

`SessionSecurityLevel` (enumeration of type User’s security level for the current session.
string)

**•** The `HIGH_ASSURANCE` security level for this session meets the High
Assurance requirements set in the org’s session settings under Session
Security Levels.


### Metadata Types Prompt

**Field Name** **Field Type** **Description**

**•** The `STANDARD` security level for this session meets the Standard
requirements set in the org’s session settings under Session Security Levels.

**•** The `LOW` level isn’t available or used in the Salesforce UI. It’s used at the
API level, but users assigned to this level experience unpredictable and
reduced functionality.

Declarative Metadata Sample Definition

The following is an example of a ProfileSessionSetting component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ProfileSessionSetting xmlns="http://soap.sforce.com/2006/04/metadata">

      <profile>platformportal</profile>

      <requiredSessionLevel>HIGH_ASSURANCE</requiredSessionLevel>

      <sessionTimeout>1440</sessionTimeout>

   </ProfileSessionSetting>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### Prompt

Represents the metadata related to in-app guidance, which includes prompts and walkthroughs. Help users discover your products and
services, adopt your processes, or learn how to use a new feature. Write the content, select the target audience, and specify where and
when the in-app guidance appears.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### Prompt components have the suffix prompt and are stored in the prompts folder.

Version

### Prompt components are available in API version 46.0 and later.


Metadata Types Prompt

Special Access Rules

[To add, edit, manage, and view prompts and walkthroughs in Lightning Experience or in Experience Cloud sites, see Considerations for](https://help.salesforce.com/s/articleView?id=sales.customhelp_lex_prompt_consider.htm&type=5&language=en_US)
[Creating In-App Guidance and Permissions for Creating and Accessing In-App Guidance in](https://help.salesforce.com/s/articleView?id=sales.customhelp_lex_prompt_consider.htm&type=5&language=en_US) _Salesforce Help_ for permissions.

Prompts and Walkthroughs in Managed Packages

[For considerations about including in-app guidance in a managed package, see Guidelines for In-App Guidance in Managed Packages](https://help.salesforce.com/articleView?id=customhelp_iag_packages.htm&language=en_US)
in Salesforce Help.

[For more information about creating managed packages, see Create a First-Generation Managed Package.](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/creating_packages.htm)

[Unmanaged packages must contain a namespace prefix. For more information, see Register a Namespace for a First-Generation Managed](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/register_namespace_prefix.htm)
[Packages and What happens to my namespace prefix when I install a package?.](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/register_namespace_prefix.htm)

Fields

**Field Name** **Description**

```
masterLabel

promptVersions

```

PromptVersion

**Field Type**
string

**Description**
Required. The label. Maximum of 80 characters.

**Field Type**

PromptVersion[]

**Description**
A list of in-app guidance entries. Each entry represents a different prompt or
walkthrough.

A list of in-app guidance entries. Each entry represents a different prompt or walkthrough.

**Field Name** **Description**

```
actionButtonLabel

actionButtonLink

```

**Field Type**
string

**Description**
Label for the action button or link. Maximum of 25 characters. For a walkthrough, specify
this value on the last step.

**Field Type**
string


Metadata Types Prompt

**Field Name** **Description**

**Description**
URL for the action button or link. Maximum of 1,000 characters. You can’t use the `GROUP`
`BY` option in a SOQL query for this field. For a walkthrough, specify this value on the last
step.

```
body

customApplication

delayDays

description

dismissButtonLabel

displayPosition

```

**Field Type**
string

**Description**
Required. Body content.

In API version 60.0 and later, enter up to 4,000 characters for all prompt types.

In earlier API versions, enter up to 240 characters for floating prompts and targeted prompts.
Enter up to 4,000 characters for docked prompts.

For docked prompts, the maximum characters include HTML markup, not just readable
text.

**Field Type**
string

**Description**
Internal use only. No data is populated for this field.

**Field Type**
int

**Description**
Required if recurrences are scheduled. Number of days in between occurrences. For a
walkthrough, specify this value on the first step.

**Field Type**
string

**Description**
Description. Maximum of 255 characters.

**Field Type**
string

**Description**
Label for the dismiss button of a floating or targeted prompt. Maximum of 15 characters.

**Field Type**
PromptDisplayPosition (enumeration of type string)

**Description**
The position of a floating prompt on the page. Valid values are:

**•** `BottomCenter`

**•** `BottomLeft`


Metadata Types Prompt

**Field Name** **Description**

**•** `BottomRight`

**•** `TopCenter`

**•** `TopLeft`

**•** `TopRight`

```
displayType

elementRelativePosition

endDate

header

```

**Field Type**
PromptDisplayType (enumeration of type string)

**Description**
Required. The type of prompt. Valid values are:

**•** `DockedComposer` —A docked prompt

**•** `FloatingPanel` —A floating prompt

**•** `Targeted` —A targeted prompt. Available in API version 52.0 and later.

**Field Type**
PromptElementRelativePosition (enumeration of type string)

**Description**
Indicates the location of a targeted prompt relative to the element. Available in API version
52.0 and later. Valid values are:

**•** `BottomCenter`

**•** `BottomLeft`

**•** `BottomRight`

**•** `LeftBottom`

**•** `LeftCenter`

**•** `LeftTop`

**•** `RightBottom`

**•** `RightCenter`

**•** `RightTop`

**•** `TopCenter`

**•** `TopLeft`

**•** `TopRight`

**Field Type**
date

**Description**
The date to stop showing the in-app guidance. For a walkthrough, specify this value on the
first step.

**Field Type**
string


Metadata Types Prompt

**Field Name** **Description**

**Description**
Label for the header of a docked prompt. This value is the label contained in the window’s
browser bar. Maximum of 36 characters.

```
image

imageAltText

imageLink

imageLocation

indexWithIsPublished

indexWithoutIsPublished

```

**Field Type**
string

**Description**
The developer name of the contentAsset that holds the image. You can specify this field or
the `imageLink` field, but not both.

**Field Type**
string

**Description**
Indicates the alt text of an image. Required if `imageLocation`, `imageLink`, or `image`
is specified.

**Field Type**
string

**Description**
The URL for a prompt’s image. You can specify this field or the image field, but not both.
Available in API version 53.0 and later.

**Field Type**
picklist

**Description**
Indicates the location of the image in relation to the body text. Required if `image`,
`imageLink`, or `imageAltText` is specified. Valid values are:

**•** `Top`

**•** `Bottom`

**•** `Right`, which is for floating or targeted prompts only

**•** `Left`, which is for floating or targeted prompts only

**Field Type**
string

**Description**
Used by Salesforce for efficient querying.

**Field Type**
string

**Description**
Used by Salesforce for efficient querying.


Metadata Types Prompt

**Field Name** **Description**

```
isPublished

masterLabel

publishedByUser

publishedDate

referenceElementContext

shouldDisplayActionButton

shouldIgnoreGlobalDelay

startDate

```

**Field Type**
boolean

**Description**
Indicates whether the in-app guidance is active ( `true` ) or not ( `false` ).

**Field Type**
string

**Description**
Required. The label.

**Field Type**
string

**Description**
Internal use only. No data is populated for this field.

**Field Type**
date

**Description**
Indicates the date the in-app guidance was activated. If installed from a package, this value
is the date when the package was installed. For walkthroughs, this field can only be specified
on the first step.

**Field Type**
textarea

**Description**
Used by Salesforce to identify the element that the targeted prompt is associated with.
Available in API version 52.0 and later.

**Field Type**
boolean

**Description**
Indicates whether an action button or link is included ( `true` ) or not ( `false` ).

**Field Type**
boolean

**Description**
Indicates whether the in-app guidance ignores the global time delay and instead shows
on page load ( `true` ) or not ( `false` ). This field is available in API version 48.0 and later.

**Field Type**
date


Metadata Types Prompt

**Field Name** **Description**

**Description**
Indicates the date to start showing the in-app guidance. For a walkthrough, specify this
value on the first step.

In API version 48.0 and earlier, this field is required.

```
stepNumber

targetAppDeveloperName

targetAppNamespacePrefix

targetPageKey1

targetPageKey2

targetPageKey3

```

**Field Type**
int

**Description**
Required for walkthroughs only. Indicates the number of the last step the user viewed or
interacted with in a walkthrough. Include up to 10 steps. Numbers must be consecutive
without repeated or skipped numbers. Available in API version 49.0 and later.

**Field Type**
string

**Description**
The app’s developer name where the in-app guidance appears. Deprecated in API version
51.0 and later.

**Field Type**
string

**Description**
The app’s namespace prefix where the in-app guidance appears. This value must match
the target app’s `NamespacePrefix` in the org that the package is being installed into.
Maximum of 15 characters. Deprecated in API version 51.0 and later.

**Field Type**
string

**Description**
Required. Used by Salesforce to identity the prompt’s page location along with
`targetPageKey2`, `targetPageKey3`, `targetPageKey4`, and
`targetPageType` .

**Field Type**
string

**Description**
Used by Salesforce to identity the prompt’s page location along with `targetPageKey1`,
`targetPageKey3`, `targetPageKey4`, and `targetPageType` .

**Field Type**
string

**Description**
Used by Salesforce to identify the prompt’s page location along with `targetPageKey1`,
`targetPageKey2`, `targetPageKey4`, and `targetPageType` .


Metadata Types Prompt

**Field Name** **Description**

```
targetPageKey4

targetPageType

targetRecordType

themeColor

themeSaturation

timesToDisplay

```

**Field Type**
string

**Description**
Used by Salesforce to identify the prompt’s page location along with `targetPageKey1`,
`targetPageKey2`, `targetPageKey3`, and `targetPageType` . This field is
available in API version 53.0 and later.

**Field Type**
string

**Description**
Required. Used by Salesforce to identity the page location along with `targetPageKey1`,
`targetPageKey2`, `targetPageKey3`, and `targetPageKey4` .

**Field Type**
string

**Description**
Used by Salesforce to determine if in-app guidance is specific to a record type. This field is
available in API version 53.0 and later.

**Field Type**
PromptThemeColor (enumeration of type string)

**Description**
Indicates which custom theme color is applied to the in-app guidance. Required if
`themeSaturation` is specified. For a walkthrough, specify this value on the first step.
Valid values are:

**•** `Theme1`, which is derived from the current brand color

**•** `Theme2`, which is derived from the current page background color

**•** `Theme3`, which is derived from the current global header color

**•** `Theme4`, which is derived from the current app theme color

**Field Type**
PromptThemeSaturation (enumeration of type string)

**Description**
Indicates which color value, or saturation, is applied to the in-app guidance that has a
custom theme color. Required if `themeColor` is specified. For a walkthrough, specify
this value on the first step. Valid values are:

**•** `Dark`

**•** `Light`

**Field Type**
int


Metadata Types Prompt

**Field Name** **Description**

**Description**
Required if recurrences are scheduled. The maximum number of times to show the in-app
guidance. Salesforce detects whether the user interacts with the in-app guidance, then
determines whether to show the in-app guidance again or cancel scheduled recurrences.
Maximum value of 30. For a walkthrough, specify this value on the first step.

```
title

uiFormulaRule

userAccess

userProfileAccess

versionNumber

```

**Field Type**
string

**Description**
Required. The label for the title. Maximum of 36 characters.

**Field Type**

UiFormulaRule[]

**Description**
A set of one or more permission filters that define the conditions under which the in-app
guidance displays on the page.

If the rule evaluates to `true`, the in-app guidance displays on the page. If `false`, it doesn't
display. If this field is `null`, the in-app guidance displays by default.

**Field Type**
PromptUserAccess (enumeration of type string)

**Description**
Indicates which permissions can see the in-app guidance. Valid values are:

**•** `Everyone`, which indicates that there’s no permission restrictions

**•** `SpecificPermissions`, which indicates that only users with all the specific user
permissions specified can see the in-app guidance

In API version 48.0 and earlier, this field is required.

**Field Type**
PromptUserProfileAccess (enumeration of type string)

**Description**
Indicates which profiles can see the in-app guidance. This field is available in API version
48.0 and later. Valid values are:

**•** `Everyone`, which indicates that there are no profile restrictions

**•** `SpecificProfiles`, which indicates that users with any of the specified user
profiles can see the in-app guidance

**Field Type**
int

**Description**
Required. The number remains `1` since multiple versions aren’t saved in the org.


Metadata Types Prompt

**Field Name** **Description**

```
videoLink

```

UiFormulaRule

**Field Type**
string

**Description**
The embed URL for a video in a docked prompt. Maximum of 1,000 characters. You can
specify this field or the `image` field, but not both. This field is available in API version 48.0
[and later. See Considerations for Creating In-App Guidance.](https://help.salesforce.com/s/articleView?id=sales.customhelp_lex_prompt_consider.htm&type=5&language=en_US)

A set of one or more filters that define the conditions under which a prompt displays on a Lightning Experience page.

**Field Name** **Description**

```
booleanFilter

criteria

```

UiFormulaCriterion

**Field Type**
string

**Description**
Specifies the AND filter condition.

**Field Type**

UiFormulaCriterion[]

**Description**
List of one or more filters that, when evaluated, determine visibility.

A single filter that, when evaluated, helps define visibility on a Lightning Experience page.

**Field Name** **Description**

```
leftValue

```

**Field Type**
string

**Description**
Required. The field used for filtering. Only standard and custom
permissions can be included. You can use these expressions in the
`leftValue` field when setting filters for visibility.

**•** `{!$Permission.CustomPermission.` _**`permissionName`**_ `}` —Use
this expression to control visibility based on the custom permissions
of the user viewing the Lightning page. Supported for app, Home,
and record pages only.

**•** `{!$Permission.StandardPermission.` _**`permissionName`**_ `}` —Use
this expression to control visibility based on the standard permissions


Metadata Types Prompt

**Field Name** **Description**

of the user viewing the Lightning page. Supported for app, Home,
and record pages only.

**•** `{!ENCODED:{!ID:$` _**`User.Profile.Key`**_ `}}` —Use this
expression to control visibility based on the custom or standard profile
of the user viewing the Lightning page. Available in API Version 48.0
and later.

```
operator

rightValue

```

**Field Type**
string

**Description**
Required. Defines the operator used to filter the data. Valid value is
`EQUAL` .

**Field Type**
string

**Description**
Specifies if you want to evaluate the visibility for permissions or the name
of the profile.

**•** For permissions, use `true` .

**•** For profiles, use the name of the profile. Available in API Version 48.0
and later. For example, `Standard` or `custom_regionalsales` .

Declarative Metadata Sample Definition

The following is an example of a Prompt component.

```
<?xml version="1.0" encoding="UTF-8"?>

<Prompt xmlns="http://soap.sforce.com/2006/04/metadata">

   <masterLabel>Prompt Label</masterLabel>

   <promptVersions>

     <actionButtonLabel>Learn How</actionButtonLabel>

<actionButtonLink>https://trailhead.salesforce.com/en/content/learn/modules/scrum-and-kanban-at-salesforce/learn-about-kanban</actionButtonLink>

     <body>Explore how the Path and the Kanban view can help you track, manage, and

update your records.</body>

     <delayDays>1</delayDays>

     <description>Kanban floating prompt</description>

     <dismissButtonLabel>OK</dismissButtonLabel>

     <displayPosition>TopLeft</displayPosition>

     <displayType>FloatingPanel</displayType>

     <endDate>2019-03-11</endDate>

     <isPublished>true</isPublished>

     <masterLabel>Prompt Label</masterLabel>

     <publishedDate>2019-03-11</publishedDate>

     <shouldDisplayActionButton>false</shouldDisplayActionButton>

```


Metadata Types Prompt

```
        <shouldIgnoreGlobalDelay>false</shouldIgnoreGlobalDelay>

        <startDate>2019-03-11</startDate>

        <targetAppDeveloperName>LightningSales</targetAppDeveloperName>

        <targetAppNamespacePrefix>standard</targetAppNamespacePrefix>

        <timesToDisplay>3</timesToDisplay>

        <title>Get on the Path to Success</title>

        <userAccess>SpecificPermissions</userAccess>

        <userProfileAccess>SpecificProfiles</userProfileAccess>

        <versionNumber>1</versionNumber>

        <videolink>https://www.youtube.com/embed/Ko-gcObzTVo</videolink>

        <uiFormulaRule>

           <booleanFilter>(1 AND 2 AND 3) AND (4 OR 5)</booleanFilter>

           <criteria>

             <leftValue>{!$Permission.StandardPermission.ActivitiesAccess}</leftValue>

             <operator>EQUAL</operator>

             <rightValue>TRUE</rightValue>

           </criteria>

           <criteria>

            <leftValue>{!$Permission.StandardPermission.ContentWorkspaces}</leftValue>

             <operator>EQUAL</operator>

             <rightValue>TRUE</rightValue>

           </criteria>

           <criteria>

             <leftValue>{!$Permission.CustomPermission.MyCustomPerm}</leftValue>

             <operator>EQUAL</operator>

             <rightValue>TRUE</rightValue>

           </criteria>

           <criteria>

             <leftValue>{!ENCODED:{!ID:$User.Profile.Key}}</leftValue>

             <operator>EQUAL</operator>

             <rightValue>Standard</rightValue>

           </criteria>

           <criteria>

             <leftValue>{!ENCODED:{!ID:$User.Profile.Key}}</leftValue>

             <operator>EQUAL</operator>

             <rightValue>custom_mysysadmin</rightValue>

           </criteria>

        </uiFormulaRule>

      </promptVersions>

   </Prompt>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>Prompt</name>

      </types>

      <version>46.0</version>

   </Package>

```


### Metadata Types PublicKeyCertificate

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### PublicKeyCertificate

Represents the public key certificate. On this entity we store a public certificate or a JSON web key, which is used to validate the
customer-provided JWT.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### PublicKeyCertificate components have the suffix .PublicKeyCertificate and are stored in the PublicKeyCertificate

folder.

Version

### PublicKeyCertificate components are available in API version 62 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Description**

```
description

isActive

```

**Field Type**
string

**Description**
A description of the public key certificate.

**Field Type**
boolean

**Description**
Indicates whether the public key certificate is active (true) or inactive (false). The default
value is false.


Metadata Types PublicKeyCertificate

**Field Name** **Description**

```
jsonWebKey

masterLabel

```

**Field Type**
string

**Description**
Represents a public cryptographic key that can be used to verify the validity of a token.

**Field Type**
string

**Description**

Required. The label for the public key certificate.

Declarative Metadata Sample Definition

The following is an example of a PublicKeyCertificate component.

```
<?xml version="1.0" encoding="UTF-8"?>

<PublicKeyCertificate xmlns="http://soap.sforce.com/2006/04/metadata">

   <masterLabel>pck1</masterLabel>

   <isActive>true</isActive>

   <description>This is my description for a test PublicKeyCertificate</description>

   <jsonWebKey>

{

  "kid":"123456",

  "alg":"RS256",

  "use":"sig",

  "kty":"RSA",

  "x5c":["<Your public certificate>"],

  "y":"y",

  "n":"<Base64-encoded modulus>",

  "e":"<Base64-encoded public exponent>",

  "crv":"crv",

  "d":"d",

  "k":"k"

}

   </jsonWebKey>

</PublicKeyCertificate>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<!-
  ~ Copyright 2024 salesforce.com, inc.

  ~ All Rights Reserved

  ~ Company Confidential

  -->

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>*</members>

     <name>PublicKeyCertificate</name>

```


### Metadata Types PublicKeyCertificateSet

```
      </types>

      <version>62.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### PublicKeyCertificateSet

Represents a set of public certificate keys. On this entity we store a public certificates or JSON web keys.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### PublicKeyCertificateSet components have the suffix .PublicKeyCertificateSet and are stored in the PublicKeyCertificateSet folder.

Version

### PublicKeyCertificateSet components are available in API version 62 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Description**

```
description

jwksEndPoint

```

**Field Type**
string

**Description**
A description of the public key certificate set.

**Field Type**
string


Metadata Types PublicKeyCertificateSet

**Field Name** **Description**

**Description**
The URL of the HTTPS Server that returns the JWKS.

```
jwtIssuer

masterLabel

publicKeyCertificateSetKeys

type

```

**Field Type**
string

**Description**
The user, organization, or service that issued the JSON web token. This value is
case-sensitive.

**Field Type**
string

**Description**

Required. The label for the public key certificate set.

**Field Type**

PublicKeyCertificateSetKey[]

**Description**
A set of public certificate keys associated with the public key certificate set.

**Field Type**
PublicKeyCertificateSetType (enumeration of type string)

**Description**

Required. Determines how the server's public key set is retrieved. The keys are
represented in JWK format.

Values are:

**•** `JWKS`  - Used to specify a certificate via the child Type PublicKeyCertificateSetKey.

**•** `JWKS_URL`  - Used to specify a certificate via the jwksEndPoint field on this Type.

PublicKeyCertificateSetKeys

Represents a set of public certificate keys associated with the public key certificate set.

**Field Name** **Description**

```
publicKeyCertificate

```

**Field Type**
string

**Description**

Required.

The PublicKeyCertificate we want to reference.


### Metadata Types Queue

Declarative Metadata Sample Definition

The following is an example of a PublicKeyCertificateSet component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <PublicKeyCertificateSet xmlns="http://soap.sforce.com/2006/04/metadata">

      <masterLabel>pcks1</masterLabel>

      <description>This is my description for a PublicKeyCertificateSet</description>

      <type>JWKS</type>

      <jwtIssuer>example.com</jwtIssuer>

      <publicKeyCertificateSetKeys>

           <publicKeyCertificate>pck1</publicKeyCertificate>

      </publicKeyCertificateSetKeys>

   </PublicKeyCertificateSet>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>PublicKeyCertificate</name>

      </types>

      <types>

        <members>*</members>

        <name>PublicKeyCertificateSet</name>

      </types>

      <version>62.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### Queue

Represents a holding area for items before they are processed.

Declarative Metadata File Suffix and Directory Location

The file suffix for queue components is `.queue` and components are stored in the `queues` directory of the corresponding package
directory. This component supports cases, leads, service contracts (if Entitlements are enabled), and custom objects.

Version

### Queue components are available in API version 24.0 and later.


Metadata Types Queue

Special Access Rules

As of Summer ’20 and later, only authenticated internal and external users can access this type.

Fields

This metadata type represents the valid values that define a queue:

**Field Name** **Field Type** **Description**

`doesSendEmailToMembers` boolean Indicates whether emails are sent to queue members ( `true` ) or not
( `false` ) when a new record is added to the queue.

`email` string The email address of the queue owner.

`name` string Required. The name of the queue. Corresponds to **Label** in the user
interface.

`queueMembers` QueueMembers[]

Represents queue members added to the queue. Members can be added
directly or selected by roles and public groups they belong to. Available
in API version 42.0 and later.

`queueRoutingConfig` string Routing configuration name. Applies to orgs that use Omni-Channel with
a routing configuration. Available in API version 42.0 and later.

`queueSobject` QueueSobject[] Indicates the supported entity types.

QueueMembers

Represents queue members added to the queue. Members can be added directly as users or selected by the roles and public groups
they belong to. Available in API version 42.0 and later.

**Field Name** **Field Type** **Description**

`publicGroups` PublicGroups[] Represents public groups in the org. Public groups are optionally used
to add queue members.

`roleAndSubordinates` RoleAndSubordinates[]

`roleAndSubordinatesInternal` RoleAndSubordinatesInternal[]

Represents roles and their subordinates in the org’s role hierarchy,
including customer and partner roles. Roles and their subordinate
hierarchy are optionally used to add queue members.

Represents internal roles and their subordinates in the org’s role hierarchy,
excluding customer and partner roles. Roles and their subordinate
hierarchy are optionally used to add queue members.

`roles` Roles[] Represents roles in the org. Roles are optionally used to add queue
members.

`users` Users[] Represents users in the org. Users can be added directly as queue
members.


Metadata Types Queue

PublicGroups

Represents public groups in the org. Public groups are optionally used to add queue members. Available in API version 42.0 and later.

**Field Name** **Field Type** **Description**

`publicGroup` string Represents a public group.

RoleAndSubordinates

Represents roles and their subordinates in the org’s role hierarchy, including customer and partner roles. Roles and their subordinate
hierarchy can be used to add queue members. Available in API version 42.0 and later.

**Field Name** **Field Type** **Description**

`roleAndSubordinate` string Represents a role and its subordinates, including customer and partner
roles. Only available when digital experiences is enabled for your org and

Experience Cloud site users are created with external account roles other
than a shared person account role.

RoleAndSubordinatesInternal

Represents internal roles and their subordinates in the org’s role hierarchy, excluding customer and partner roles. Roles and their
subordinate hierarchy can be used to add queue members. Available in API version 42.0 and later.

**Field Name** **Field Type** **Description**

`roleAndSubordinateInternal` string Represents a role and its subordinates, excluding customer and partner
roles.

Roles

Represents roles in the org. Roles can be used to add queue members. Available in API version 42.0 and later.

**Field Name** **Field Type** **Description**

`role` string Represents a role.

Users

Represents users in the org. Users can be added directly as queue members. Available in API version 42.0 and later.

**Field Name** **Field Type** **Description**

`user` string Represents a user. Specify the user’s username.


Metadata Types Queue

QueueSobject

QueueSobject represents an entity type that the queue supports.

**Field Name** **Field Type** **Description**

`sobjectType` string Valid values are:

**•** `Case`

**•** `ContactRequest`

**•** `Lead`

**•** `ServiceContract`

**•** `Task` (Available in API version 48.0 and later.)

**•** Custom objects (such as `ObjA_c` )

Declarative Metadata Sample Definition

The following is the definition of a queue, which supports Case, Lead, and a custom object named ObjA.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Queue xmlns="http://soap.sforce.com/2006/04/metadata">

      <doesSendEmailToMembers>true</doesSendEmailToMembers>

      <email>member@company.com</email>

      <fullName>Your Name</fullName>

      <name>memberQueue</name>

      <queueSobject>

        <sobjectType>Case</sobjectType>

      </queueSobject>

      <queueSobject>

        <sobjectType>Lead</sobjectType>

      </queueSobject>

      <queueSobject>

        <sobjectType>ObjA__c</sobjectType>

      </queueSobject>

   </Queue>

```

Here’s another definition of a queue containing queue members added directly or via public groups and roles. Queries retrieve values
using the `DeveloperName` field, not the `Name` field, so that the returned names are unique. The query also appends letters to the
end of duplicate names, so these groups and roles can be referred to independently.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Queue xmlns="http://soap.sforce.com/2006/04/metadata">

      <doesSendEmailToMembers>false</doesSendEmailToMembers>

      <name>queue1</name>

      <queueMembers>

        <publicGroups>

           <publicGroup>All Internal Users</publicGroup>

        <publicGroups>

        <queueRoleAndSubordinates>

           <queueRoleAndSubordinate>role1</queueRoleAndSubordinate>

           <queueRoleAndSubordinate>role2</queueRoleAndSubordinate>

           <queueRoleAndSubordinate>role3</queueRoleAndSubordinate>

```


### Metadata Types QueueRoutingConfig

```
        </queueRoleAndSubordinates>

        <roles>

           <role>role1</role>

        </roles>

        <users>

           <user>s@sm.com</user>

           <user>std@sm.com</user>

        </users>

      </queueMembers>

      <queueRoutingConfig>my_omni_routing_config</queueRoutingConfig>

      <queueSobject>

        <sobjectType>Case</sobjectType>

      </queueSobject>

      <queueSobject>

        <sobjectType>Lead</sobjectType>

      </queueSobject>

   </Queue>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### QueueRoutingConfig

Represents the settings that determine how work items are routed to agents.

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

ServicePresenceStatus components have the suffix `.queueRoutingConfig` and are stored in the `queueRoutingConfigs`
folder.

Version

### QueueRoutingConfig components are available in API version 44.0 and later.

Special Access Rules

This type is available only if Omni-Channel is enabled in your org.

Fields

**Field Name** **Field Type** **Description**

`capacityPercentage` double The percentage of an agent’s capacity for work items that’s consumed
by a specific type of work item from this service channel. Voice calls must


Metadata Types QueueRoutingConfig

**Field Name** **Field Type** **Description**

have a capacity percentage of 100. If an agent receives a voice call, the
agent won’t receive new work items until the call ends, because at that
point the agent’s capacity will have reached 100%.

`capacityType` CapacityType [The setting applies for PSRs (PendingServiceRouting) that are created](https://help.salesforce.com/s/articleView?id=service.omnichannel_psr_lifecycle.htm&type=5&language=en_US)
and managed by the system.

**•** When set to `INHERITED`, the value of the Interruptible check box
or value set on the Service Channel applies.

**•** When set to `INTERRUPTIBLE`, the generated PSR has the
`isInterruptible` flag set to true.

**•** When set to NOT `INTERRUPTIBLE`, the generated PSR has the
`isInterruptible` flag set to false.

**•** When not set, its behavior is equivalent to `INHERITED` .

`capacityWeight` double The amount of an agent’s capacity for work items that’s consumed by
a work item from this service channel. For example, if an agent has a

capacity of 6, and cases are assigned a capacity weight of 2, an agent
can be assigned up to 3 cases before the agent is at capacity and can’t
receive new work items. Voice calls must use the entire capacity weight.

`dropAdditionalSkillsTimeout` int

The number of seconds to elapse before additional skills are dropped
from Omni-Channel routing. In skills-based routing, you can set some

skills to **Additional Skill** . After the timeout elapses, a skill marked as
**Additional Skill** is dropped from Omni-Channel routing and the case
is routed to the best-matched agent, even if the agent doesn’t have all
the skills.

[If CustomRequestedDateTime is set in the PendingServiceRouting object,](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_pendingservicerouting.htm)
DropAdditionalSkillsTimeout uses CustomRequestedDateTime as the
start time. If CustomRequestedDateTime + DropAdditionalSkillsTimeout
has already passed, Omni-Channel immediately drops the additional
skills after the pending service request is created.

`isAttributeBased` boolean Indicates whether this routing configuration is used with skills-based
routing rules ( `true` ) or not ( `false` ).

`label` string Required. The label of the presence status.

`PausedCapacityPercentage` double The percentage of a rep’s capacity that’s consumed when this work item
is paused. The paused capacity feature is available with status-based

capacity and Enhanced Omni-Channel only. Available in API version 64.0
and later.

`PausedCapacityWeight` double The amount of a rep’s capacity that’s consumed when this work item is
paused. The paused capacity feature is available with status-based

capacity and Enhanced Omni-Channel only. Available in API version 64.0
and later.


Metadata Types QueueRoutingConfig

**Field Name** **Field Type** **Description**

`pushTimeout` int The number of seconds set for push timeout. `0` is returned when push
timeout isn’t enabled.

`queueOverflowAssignee` string The ID of the queue that’s set as the Overflow Assignee.

`QueueRoutingConfigSkill` QueueRoutingConfigSki **l** [] Default skills associated with the routing configuration. Work is routed
using a combination of rules and default skills.

```
routingModel

```

RoutingModel Required. The routing type that determines how work items are routed
(enumeration of (pushed) to agents. Possible values are:
type string)

**•** `LEAST_ACTIVE`

**•** `MOST_AVAILABLE`

**•** `EXTERNAL_ROUTING`

`routingPriority` int Required. The priority in which work items from the service channels
that are related to this routing configuration are routed to agents. Work

items from routing configurations that have lower priority values (for
example, 0) are routed to agents first.

`userOverflowAssignee` string The ID of the user that’s set as the Overflow Assignee.

QueueRoutingConfigSkill

Represents default skills associated with the routing configuration.

Fields

**Field Name** **Field Type** **Description**

`skill` string Skill used to route a work item.

Declarative Metadata Sample Definition

The following is an example of a QueueRoutingConfig component.

```
<?xml version="1.0" encoding="UTF-8"?>

<QueueRoutingConfig xmlns="http://soap.sforce.com/2006/04/metadata">

  <capacityWeight>1.0</capacityWeight>

  <label>Case Routing</label>

  <pushTimeout>120</pushTimeout>

  <queueOverflowAssignee>queueOverflow</queueOverflowAssignee>

  <routingModel>LEAST_ACTIVE</routingModel>

  <routingPriority>1</routingPriority>

  <capacityType>INHERITED</capacityType>

  <pausedCapacityWeight>0.25</pausedCapacityWeight>

</QueueRoutingConfig>

```


### Metadata Types QuickAction

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>QueueRoutingConfig</name>

      </types>

      <version>44.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### QuickAction

Represents a specified create or update quick action for an object that then becomes available in the Chatter publisher. For example,
you can create an action that, on the detail page of an account, allows a user to create a contact related to that account from the Chatter
feed on that page. QuickAction can be created on objects that permit custom fields.

The parent objects supported include:

**•** Account

**•** Campaign

**•** Case

**•** Contact

**•** ContentNote

**•** Custom objects

**•** Group

**•** Lead

**•** Opportunity

File Suffix and Directory Location

### QuickAction components have the suffix quickAction and are stored in the quickActions folder.

Version

### QuickAction components are available in API version 28.0 and later.


Metadata Types QuickAction

Fields

**Field Name** **Field Type** **Description**

`canvas` string If the custom action invokes a Canvas app, the app name. Returns the
fully qualified name of the Canvas app in the format

`<namespace>__<dev_name>`, if the quick action type is `Canvas` ;
otherwise, returns `null` .

This field is available in API version 29.0 and later.

`description` string The description of the action.

`fieldOverrides` FieldOverride on The specific field that can be overridden within a QuickAction on page
page 1766[] 1763.

`flowDefinition` string If the custom action invokes a flow, this field represents the API name
of the flow. Otherwise, this field is `null` .

`height` int If a custom action is created, this field represents the height in pixels of
the action pane.

`icon` string

`isProtected` boolean

The icon used to identify the action.

API version 32.0 and later returns different icons than in earlier API
versions.

Indicates whether this component is protected ( `true` ) or not ( `false` ).
Protected components cannot be linked to or referenced by components
created in the installing organization.

`label` string Identifies the action and displays to users. Also the default identifier used
for the API and managed packages.

`lightningComponent` string

`optionsCreateFeedItem` boolean

If the custom action invokes a Lightning component, this field represents
the fully qualified name of the component. Otherwise, this field is `null` .

Available in API version 38.0 and later.

Required. Indicates whether successful completion of the action creates
a feed item ( `true` ) or not ( `false` ). Applies only to Create Record,
Update Record, and Log a Call quick action types.

Available in API version 36.0 and later.

`page` string If the custom action invokes a Visualforce page, this field identifies the
page.

`quickActionLayout` QuickActionLayout The layout of fields on the action.

`quickActionParameter` QuickActionParameter[]

The input and output of the quick action.

Available in API version 63.0 and later.


Metadata Types QuickAction

**Field Name** **Field Type** **Description**

```
standardLabel

```

QuickActionLabel Specifies the standard label to use for the action. The valid values are:
(enumeration of

**•** `AddRecord`

type string)

**•** `AddMember`

**•** `ChangeDueDate`

**•** `ChangePriority`

**•** `ChangeStatus`

**•** `CreateNew`

**•** `CreateNewRecordType` (For example, a label with something
like “Create New Idea”)

**•** `Defer`

**•** `EditDescription`

**•** `EnrollInProgram` (Available in API versions 46.0 and later only
if the org has Health Cloud enabled)

**•** `Escalate`

**•** `EscalateToRecord`

**•** `Forward` (Available in API version 42.0 and later)

**•** `LogACall`

**•** `LogANote`

**•** `ModifyAppointment` (Available in API version 47.0 and later)

**•** `New` (A new record)

**•** `NewChild` (A new child record)

**•** `NewChildRecordType`

**•** `NewRecordType` (For example, a label with something like “New
Idea”)

**•** `OfferFeedback`

**•** `PatientDetails` (Available in API version 57.0 and later if the
org has Health Cloud enabled)

**•** `PerformCount` (Available in API version 63.0 and later.)

**•** `Quick` (A quick record)

**•** `QuickRecordType`

**•** `RelocateAsset` (Available in API version 63.0 and later)

**•** `ReplaceAsset` (Available in API version 63.0 and later)

**•** `Reply` (Available in API version 42.0 and later)

**•** `ReplyAll` (Available in API version 42.0 and later)

**•** `RequestFeedback`

**•** `SendEmail` (This value is available in API version 31.0 and later.)

**•** `Update`


Metadata Types QuickAction

**Field Name** **Field Type** **Description**

`successMessage` string

`targetObject` string

`targetParentField` string

The message that displays to the user upon successful completion of
the action.

Available in API version 36.0 and later.

The object for which the action is created and performed.

For example, you can create an action that, on the detail page of an
account, allows a user to create a contact related to that account from

the Chatter feed on that page. QuickAction can be created on objects
that permit custom fields. In this case, Contact is the `targetObject` .

The parent object type of the action. Links the target object to the parent
object. For example, use Account if the target object is Contact and the
parent object is Account.

`targetRecordType` string Specifies which record type to create. Valid values are:

**•** Business Account

**•** Person Account

**•** Master

```
type

```

QuickActionType Required. The type of quick action. Valid values are:
(enumeration of

**•** `Canvas`

type string)

**•** `Create`

**•** `Flow` (This value is available as a Beta in API version 41.0 and later)

**•** `LightningComponent` (This value is available in API version
38.0 and later.)

**•** `LogACall`

**•** `Post`

**•** `SendEmail` (This value is available in API version 31.0 and later.)

**•** `SocialPost`

**•** `Update`

**•** `VisualforcePage`

`width` int If a custom action is created, this field represents the width in pixels of
the action pane.

FieldOverride

Represents the field names and their respective formulas and literal values that comprise predefined value settings for a QuickAction on
page 1763. If a field on an action has both a predefined value and a default value set, the action uses the predefined value, not the default
value. A formula value takes precedence over a literal value if both are defined.


Metadata Types QuickAction

**Field Name** **Field Type** **Description**

`field` string Required. The name of the field to allow predefined values on.

`formula` string Specifies the formula to use when setting a field’s predefined value.
Supported for single-select picklists as of API version 43.0.

`literalValue` string

QuickActionLayout

Supported for picklists only. Specifies the literal value of the field defined
from values in the picklist. Corresponds to the Specific Value field in the
predefined value UI.

The layout of fields on the action. There’s no hard limit to the number of fields you can add to an action layout. However, for optimum
usability, we recommend a maximum of eight fields. Adding more than 20 fields can severely affect user efficiency.

**Field Name** **Field Type** **Description**

```
layoutSectionStyle

```

LayoutSectionStyle Required. The type of layout structure used. The valid values are:
(enumeration of type

**•** `TwoColumnsTopToBottom`

string)

**•** `TwoColumnsLeftToRight`

**•** `OneColumn`

**•** `CustomLinks`

`quickActionLayoutColumns` QuickActionLayoutColumn Specifies columns in a QuickActionLayout on page 1767.
on page 1767[]

QuickActionLayoutColumn

A column defined for a QuickActionLayout on page 1767.

**Field Name** **Field Type** **Description**

`quickActionLayoutItems` QuickActionLayoutItem Specifies row items in a QuickActionLayoutColumn on page 1767.
on page 1767 []

QuickActionLayoutItem

A row item comprised of fields and defined for a QuickActionLayoutColumn on page 1767.

**Field Name** **Field Type** **Description**

`emptySpace` boolean Controls if this layout item is a blank space ( `true` ) or not ( `false` ).

`field` string Represents a specific field in QuickActionLayoutItem on page 1767.


Metadata Types QuickAction

**Field Name** **Field Type** **Description**

```
uiBehavior

```

UiBehavior Specifies user input behavior for specific fields in QuickActionLayoutItem
(enumeration of type on page 1767. The valid values are:
string)

**•** `Edit`

**•** `Required`

**•** `Readonly`

QuickActionParameter

Represents the input and output of the associated quick action. Available in API version 63.0 and later.

**Field Name** **Field Type** **Description**

`name` string Required. Name of the parameter.

```
type

```

QuickActionParameterType Required. `Input` is the only valid value.
(enumeration of type
string)

`value` string Represents the value associated with the given parameter name.

Declarative Metadata Sample Definition

The following is an example of a QuickAction on page 1763 component:

```
<?xml version="1.0" encoding="UTF-8"?>

<QuickAction xmlns="http://soap.sforce.com/2006/04/metadata">

   <description>testActionDefinitionTypesCreateTask</description>

   <label>testActionDefinitionTypesCreateTask</label>

   <optionsCreateFeedItem>true</optionsCreateFeedItem>

   <quickActionLayout>

     <layoutSectionStyle>TwoColumnsLeftToRight</layoutSectionStyle>

     <quickActionLayoutColumns>

        <quickActionLayoutItems>

          <emptySpace>false</emptySpace>

          <field>OwnerId</field>

          <uiBehavior>Required</uiBehavior>

        </quickActionLayoutItems>

        <quickActionLayoutItems>

          <emptySpace>false</emptySpace>

          <field>WhoId</field>

          <uiBehavior>Edit</uiBehavior>

        </quickActionLayoutItems>

        <quickActionLayoutItems>

          <emptySpace>false</emptySpace>

          <field>WhatId</field>

          <uiBehavior>Edit</uiBehavior>

        </quickActionLayoutItems>

```


### Metadata Types RedirectWhitelistUrl

```
           <quickActionLayoutItems>

             <emptySpace>false</emptySpace>

             <field>ActivityDate</field>

             <uiBehavior>Edit</uiBehavior>

           </quickActionLayoutItems>

           <quickActionLayoutItems>

             <emptySpace>false</emptySpace>

             <field>Subject</field>

             <uiBehavior>Edit</uiBehavior>

           </quickActionLayoutItems>

           <quickActionLayoutItems>

             <emptySpace>false</emptySpace>

             <field>Status</field>

             <uiBehavior>Required</uiBehavior>

           </quickActionLayoutItems>

           <quickActionLayoutItems>

             <emptySpace>false</emptySpace>

             <field>Priority</field>

             <uiBehavior>Required</uiBehavior>

           </quickActionLayoutItems>

        </quickActionLayoutColumns>

        <quickActionLayoutColumns/>

      </quickActionLayout>

      <successMessage>This is a success message</successMessage>

      <targetObject>Task</targetObject>

      <targetParentField>What</targetParentField>

      <type>Create</type>

   </QuickAction>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### RedirectWhitelistUrl

Represents a trusted URL that’s excluded from redirection restrictions when the `redirectionWarning` or
`redirectBlockModeEnabled` field on the SessionSettings Metadata type is set to `true` . This type extends the Metadata
metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this metadata type’s name.

File Suffix and Directory Location

### RedirectWhitelistUrl components have the suffix .redirectWhitelistUrl and are stored in the redirectWhitelistUrls

folder.


### Metadata Types RecommendationStrategy

Version

RedirectWhitelistUrl components are available in API version 48.0 and later.

Special Access Rules

Only authenticated internal and external users with the View Setup and Customize Application permissions can access or edit this type.

Fields

**Field Name** **Field Type** **Description**

`url` string
Required. The trusted URL.

These formats are accepted: `example.com`, `*.example.com`,
and `https://example.com` .

The host section of the URL can include an asterisk ( `*` ) as a wildcard.
Otherwise, the URL cannot be malformed. Examples of malformed URLs
that fail a syntax check are `malformed^url.example.com`, and
`https://{subdomain}.example.com` .

To add a `URL` based on parameters, build the URL before you add it to
this Metadata Type.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### RecommendationStrategy

Represents a recommendation strategy. Recommendation strategies are applications, similar to data flows, that determine a set of
recommendations to be delivered to the client through data retrieval, branching, and logic operations.

File Suffix and Directory Location

### RecommendationStrategy components have the suffix .recommendationStrategy and are stored in the

`recommendationStrategies` folder.

Version

### RecommendationStrategy components are available in API version 45.0 and later.

Special Access Rules

Metadata access for the RecommendationStrategy type is backed by the ManageRecommendationStrategies user permission.


Metadata Types RecommendationStrategy

Fields

**Field Name** **Field Type** **Description**

`actionContext` StrategyAction[] An array of action contexts used by the strategy.

`contextRecordType` string The sObject type of the $record used by the flow.

`description` string Description of the recommendation strategy.

`filter` StrategyNodeFilter[] An array of filter nodes.

`if` StrategyNodeIf[] An array of if nodes.

`invocableAction` StrategyNodeInvocableAction[] An array of Apex invocable action nodes. Available in API version 46.0
and later.

`isTemplate` boolean Indicates whether the recommendation strategy is a template ( `true` )
or not ( `false` ). When installed from managed packages,

recommendation strategies can’t be viewed or cloned by subscribers
because of intellectual property (IP) protection. But when those
recommendation strategies are templates, subscribers can open them
in a builder, clone them, and customize the clones. The default value of
this field is `false` . Available in API version 47.0 and later.

`label` string Required. Label for the flow.

`map` StrategyNodeMap[] An array of map nodes. Available in API version 46.0 and later.

`mutuallyExclusive` StrategyNodeExclusive[] An array of mutuallyExclusive nodes.

`onBehalfOfExpression` string

Formula expression defining the intended target of the recommendations
(in other words, the Contact associated with a Case). Mainly used for
reaction tracking.

`recommendationLimit` StrategyNodeRecommendationLimit[] An array of recommendation limit nodes.

`recommendationLoad` StrategyNodeRecommendationLoad[] An array of recommendation load nodes.

`sort` StrategyNodeSort[] An array of sort nodes.

`union` StrategyNodeUnion[] An array of union nodes.

StrategyNodeBase

Base class for all strategy nodes. This is an abstract class.

**Field Name** **Field Type** **Description**

`childNode` string Array of child node names, in order of execution.

`description` string Description of the node.

`label` string Label of the node.

`name` string Required. Unique name of the node.


Metadata Types RecommendationStrategy

StrategyAction

Defines a call to an invocable action from the strategy. Results are used by decision elements in the strategy.

**Field Name** **Field Type** **Description**

`action` string Required. The name or id of the InvocableAction to execute.

`argument` StrategyActionArg[] List of strategy action arguments.

`description` string Description of the strategy.

`label` string Label for the strategy action.

`name` string Required. Unique name of the strategy action, which is referenced by
decisioning elements in the strategy.

```
type

```

InvocableActionType Required. The action type. Valid values are:
(enumeration of type

**•** `activateSessionPermSet` —Activates a session-based permission

string)

set for the running user.

**•** `activationSchema`         - Gets the activation schema for the specified
activation. This value is available in API version 64.0 and later.

**•** `addMessageToChat` —Adds a message to an existing Salesforce
Anywhere chat. This value is available in API version 49.0 and later.

**•** `addMessageToQuipChat` —Adds a Quip message to an existing chat
room. This value is available in API version 46.0 and later.

**•** `addMessageToQuipDocument` —Adds a Quip message to an existing
Quip document, spreadsheet, or slide. This value is available in API version
46.0 and later.

**•** `addQuipDocumentToFolder` —Adds an existing Quip document,
spreadsheet, or slide to an existing folder. This value is available in API
version 46.0 and later.

**•** `addUsersToChat` —Adds users to an existing Salesforce Anywhere
chat. This value is available in API version 49.0 and later.

**•** `addUsersToQuipDocument` —Adds users, identified by their email
addresses, to an existing Quip document, spreadsheet, or slide. This value
is available in API version 46.0 and later.

**•** `addUsersToQuipChat` —Adds users, identified by their email
addresses, to an existing Quip chat room. This value is available in API
version 46.0 and later.

**•** `answerQuestionsWithSalesforceDocumentation` —Searches
Salesforce documentation to answer questions and provide links to relevant
articles.

**•** `attachQuipDocumentToRecord` —Attaches a Quip document,
spreadsheet, or slide to a Salesforce record. This value is available in API
version 46.0 and later.

**•** `apex` —Invokes an Apex method that has the @invocableMethod
annotation.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `archiveKnowledgeArticles` —Archives a list of published
Knowledge articles. This value is available in API version 45.0 and later.

**•** `assignKnowledgeArticles` —Mass assigns knowledge articles
from article list views. This value is available in API version 44.0 and later.

**•** `cdpRunIdentityResolution` —Runs a Data 360 identity resolution
process. This value is available in API version 57.0 and later.

**•** `chat` —Creates a Salesforce Anywhere chat. This value is available in API
version 49.0 and later.

**•** `chatterPost` —Posts to Chatter.

**•** `choosePricebook` —Selects a price book.

**•** `contactRequestAction` —Creates a contact request record. This
value is available in API version 45.0 and later.

**•** `component` —Invokes the Lightning component that implements the
`lightning:availableForFlowActions` interface and that is
referenced by `actionName` . This value is available in API version 43.0
and later.

**•** `contentWorkspaceEnableFolders` —Enables folders in a library.

**•** `convertAttributesToJson` —Converts the given attributes into
a JSON string format. This value is available in API version 64.0 and later.

**•** `copyQuipDocument` —Creates a copy of an existing Quip document,
spreadsheet, or slide, and gives it a new title. This value is available in API
version 46.0 and later.

**•** `createDraftFromOnlineKnowledgeArticle` —Creates a draft
from a published knowledge article. This value is available in API version
45.0 and later.

**•** `createInvoiceFromFulfillmentOrder` —Creates an invoice
from a purchase order. Available to B2B Commerce. This value is available
in API version 49.0 and later.

**•** `createQuipChat` —Creates a Quip chat room. This value is available
in API version 46.0 and later.

**•** `createQuipDocument` —Creates a Quip document, spreadsheet, or
slide. This value is available in API version 46.0 and later.

**•** `createQuipFolder` —Creates a Quip folder. This value is available in
API version 46.0 and later.

**•** `customNotificationAction` —Sends a custom notification. This
value is available in API version 46.0 and later.

**•** `deactivateSessionPermSet` —Deactivates a session-based
permission set for the running user.

**•** `deleteKnowledgeArticle` —Deletes a draft version (translation
or master-language) or an entire archived knowledge article. This value is
available in API version 46.0 and later.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `dynamicSendSurveyInvitation` —Sends customized notifications
to users about important events or updates to the records that they’re
working on. This value is available in API version 51.0 and later.

**•** `editQuipDocument` —Modifies the contents of an existing Quip
document, spreadsheet, or slide. This value is available in API version 46.0
and later.

**•** `emailAlert` —Sends an email by referencing a workflow email alert

**•** `emailSimple` —Sends an email by using flow resources

**•** `exploreConversation` —Retrieves insights from a conversation.
This value is available in API version 61.0 and later.

**•** `externalConnector` —Executes a process or method exposed via a
connector to an external system. This value is available in API version 63.0
and later.

**•** `externalService` —Invokes an External Service operation that makes
an HTTP request to an external system made available by an External Service
schema registered through Setup. This value is available in API version 46.0
and later.

**•** `findMatchingIndividuals` —Finds contact, lead, or employee
records that match a search term.

**•** `flow` —Invokes an autolaunched flow. This action type isn’t available for
flows with a processType of Flow or AutolaunchedFlow. To invoke an
autolaunched flow from one of those types, use FlowSubflow. This value
is available in API version 32.0 and later.

**•** `generateAiAgentResponse` —Generates a response from the AI
agent based on input and instructions to support intelligent, conversational
experiences. This value is available in API version 63.0 and later.

**•** `generateVerificationCode` —Sends a verification code to the
customer's email to verify their identity. This value is available in API version
63.0 and later.

**•** `getArticleSmartLinkUrl` —Gets the Smart Link URL of the
Salesforce Knowledge article. Smart links go to the right article and version,
even when a new version is published or the URL name changes. This value
is available in API version 54.0 and later.

**•** `getPoliciesByObject` —Gets Policy Center policies that contain a
given object and returns a list of matching policy names.

**•** `getPoliciesByPolicyType` —Gets Policy Center policies of the
type specified in the user input, such as Data Backup or Data Archive.

**•** `getPolicyDetails` —Gets details about a policy in Policy Center,
such as the policy type and the objects the policy targets.

**•** `goToCadenceStep` —Jumps to the specified step in the Sales cadence.
This value is available in API version 57.0 and later.

**•** `internalTestAction` —Reserved for internal use.

**•** `internalTestConnectApiAction` —Reserved for internal use.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `limitRepetitions` —Limit the number of times the same
recommendation or offer appears on the same record or for the same user
during a time period in a recommendation strategy flow. This value is
available in API version 55.0 and later.

**•** `massUpdateAccountForecast` —Bulk updates forecasts
asynchronously. This value is available in API version 48.0 and later.

**•** `massUpdateSalesAgreement` —Bulk updates sales agreements
asynchronously. This value is available in API version 48.0 and later.

**•** `quickAction` —Invokes a QuickAction.

**•** `publishActionableOrchSrcEvent` —Publishes events triggered
by an external system. This value is available in API version 62.0 and later.

**•** `publishKnowledgeArticles` —Mass publishes knowledge articles
from article list views. This value is available in API version 44.0 and later.

**•** `restoreKnowledgeArticleVersion` —Restores an archived
version of a knowledge article. This value is available in API version 45.0
and later.

**•** `sendAlert` —Sends Salesforce Anywhere alerts to users. This value is
available in API version 49.0 and later.

**•** `sendNotification` —Sends an available notification type. This value
is available in API version 54.0 and later.

**•** `sendSurveyInvitation` —Sends email survey invitations to leads,
contacts, and users in your org based on an action, such as when a customer
support case closes. This value is available in API version 47.0 and later.

**•** `performSurveySentimentAnalysis` —Perform survey sentiment
analysis to create or update the AI Sentiment Result records. This value is
available in API version 55.0 and later.

**•** `skillsBasedRouting` [—Creates a PendingServiceRouting record](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_pendingservicerouting.htm)
used for Omni-Channel skills-based routing. This value is available in version
44.0 and later.

**•** `slackArchiveChannel` —Archives a Slack channel in a Slack
workspace. This value is available in API version 54.0 and later.

**•** `slackCheckUsersAreConnectedToSlack` —Indicates whether
a collection of Salesforce users is connected to a given Slack app. This value
is available in API version 54.0 and later.

**•** `slackCreateChannel` —Creates a Slack channel in a Slack workspace.
This value is available in API version 54.0 and later.

**•** `slackGetConversationInfo` —Retrieves the name of a Slack
channel or group direct message and finds out whether it’s archived. This
value is available in API version 54.0 and later.

**•** `slackInviteUsersToChannel` —Adds users who are connected
to a given Slack app to a Slack channel or group direct message. This value
is available in API version 54.0 and later.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `slackPinMessage` —Pin or unpin a message in a Slack channel or
group direct message. This value is available in API version 54.0 and later.

**•** `slackPostMessage` —Send a message to a Slack channel or group
direct message. This value is available in API version 54.0 and later.

**•** `slackSendMessageToLaunchFlow` —Send a message to a Slack
channel, direct message, or the Messages tab of a Slack app that includes
a button that a recipient can use to launch a screen flow. This value is
available in API version 55.0 and later.

**•** `slackUpdateMessage` —Edits a message that was previously sent
to a Slack channel or group direct message. This value is available in API
version 54.0 and later.

**•** `submitKnowledgeArticleForTranslation` —Submits a
published or draft knowledge article for translation. This value is available
in API version 46.0 and later.

**•** `submit` —Submits a record for approval.

**•** `triggerJourney`                        - Send an individual to a specified journey. This
value is available in API version 64.0 and later.

**•** `verifyCustomerCode` —Verifies the code entered by the customer
to complete identity verification. This value is available in API version 49.0
and later.

These values are used in Omnichannel Inventory. If no version is specified, the
value is available in API version 51.0 and later.

**•** `ociCreateReservation` —Creates one or more inventory
reservations at a location or location group.

**•** `ociFulfillReservation` —Fulfills one or more inventory
reservations at a location.

**•** `ociGetAvailability` —Gets inventory availability data for one or
more products at one or more inventory locations or location groups.

**•** `ociReleaseReservation` —Releases one or more inventory
reservations.

**•** `ociTransferReservation` —Transfers one or more inventory
reservations between locations or location groups.

These values are used in the B2B Commerce Checkout Flow. If no version is
specified, the value is available in API version 47.0 and later.

**•** `updateCheckoutSessionStateAction` —Updates the checkout
session next state for checkout flows. This value is available in API version
49.0 and later.

**•** `priceCart` —Requests prices for all items in a cart during B2B Commerce
checkout. This value is available in API version 47.0 and later.

**•** `checkoutSessionAction` —Initiates or retrieves an existing
Checkout Session for Checkout Flows. Available to B2B Commerce. This
value is available in API version 49.0 and later.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `cancelCartAsyncOperation` —Cancels a WebCart’s async
operation. Available to B2B Commerce. This value is available in API version
49.0 and later.

**•** `calcCartPromotionsAction` —Requests a full cart promotion
calculation of all applicable line items in the Web Cart during B2B
Commerce checkout. This value is available in API version 52.0 and later.

**•** `checkCartInventoryAction` —Requests an inventory for all items
in a Web Cart during B2B Commerce checkout. This value is available in
API version 47.0 and later.

**•** `calcCartShipmentAction` —Calculates the shipping cost for all
items in a Web Cart during B2B Commerce checkout. This value is available
in API version 47.0 and later.

**•** `cartToOrderAction` —Creates a Salesforce Standard Order in draft
mode. This value is available in API version 47.0 and later.

**•** `activateOrderAction` —Activates a draft order, which creates an
order summary. This value is available in API version 47.0 and later.

[For values used in Business Rules Engine, see Flow for Business Rules Engine.](https://developer.salesforce.com/docs/atlas.en-us.260.0.industries_reference.meta/industries_reference/bre_flow_metadata_api.htm)

These values are used in Context Service. If no version is specified, the value is
available in API version 64.0 and later.

**•** `deleteContextCache` —Deletes the context instance from the
context cache using specified context ID.

**•** `queryContextTags` —Queries context instance tags associated with
a context definition.

**•** `updateContextAttributes` —Updates attributes on the context
instance using context tags.

These values are used in the Commerce Checkout Flow. If no version is specified,
the value is available in API version 55.0 and later.

**•** `addCartItem` —Adds an item to a cart during Commerce checkout.

**•** `createCart` —Creates a cart during Commerce checkout.

**•** `deleteCart` —Deletes a cart during Commerce checkout.

These values are used in Data 360. If no version is specified, the value is available
in API version 64.0 and later.

**•** `dataKitGetComponentAction` Gets the deployment status of
data kit deployment jobs.

**•** `dataKitDeployComponentAction` Deploys data kit components
in a target org.

These values are used in Salesforce CMS Workflows and Approvals. If no version
is specified, the value is available in API version 58.0 and later.

**•** `managedContentPublishVariant` —Publishes a content variant
associated with a flow. This value is available in API version 59.0 and later.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `managedContentRoleStepInteractive` —Assigns a content
variant review to a CMS role.

**•** `managedContentUnpublishVariant` —Unpublishes a published
content variant associated with a flow. This value is available in API version
59.0 and later.

**•** `managedContentVariantSetLockStatus` —Sets the locked
status of a content variant.

**•** `managedContentVariantSetReadyStatus` —Sets the ready
for publication status of a content variant.

These values are used in Employee Service. If no version is specified, the value
is available in API version 64.0 and later.

**•** `createServiceRequestCase` —Creates a case or incident for the
requested service.

**•** `getDirectDepositDetails` —Gets the direct deposit details for
the specified record ID.

**•** `getLeaveBalance` —Gets the leave balance of a specific employee.

These values are used in Insurance. If no version is specified, the value is available
in API version 63.0 and later.

**•** `cancelInsurancePolicy` —Cancel an insurance policy by using a
set of user inputs that represent policy details.

**•** `endorseInsurancePolicy` —Endorse an insurance policy by using
a set of user inputs that represent policy details.

**•** `getInsurancePolicy` —Get the details of an insurance policy.

**•** `issueInsurancePolicy`                        - Issue an insurance policy by using a set
of user inputs that represent policy details.

**•** `renewInsurancePolicy` —Renew an insurance policy by using a
set of user inputs that represent policy details.

These values are used in Insurance Brokerage. If no version is specified, the
value is available in API version 63.0 and later.

**•** `computeProducerSplits` —Compute the producer splits for the
producers associated with an Insurance Policy, for a Commission Statement
Line Item.

**•** `createProducerCommissions` —Create records for the
commissions that producers receive for the insurance policy associated
with the specified commission statement line item, and update the
commission statement line item record status.

**•** `findInsurancePolicy` —Get the insurance policy associated with
a commission statement line item that matches the specified criteria, and
update the status of the commission statement line item record.

These values are used in Order Management. If no version is specified, the value
is available in API version 48.0 and later.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `addOrderItemSummarySubmit` —Adds order item summaries to
an order summary. This value is available in API version 54.0 and later.

**•** `adjustOrderItemSummariesPreview` —Previews the expected
results of applying a price adjustment to order item summaries from an
order summary without actually applying it. This value is available in API
version 49.0 and later.

**•** `adjustOrderItemSummariesSubmit` —Applies a price adjustment
to order item summaries from an order summary. This value is available in
API version 49.0 and later.

**•** `authorizePayment` —Authorizes a card payment. This value is
available in API version 55.0 and later.

**•** `cancelFulfillmentOrderItem` —Removes items from a
fulfillment order.

**•** `cancelOrderItemSummariesPreview` —Previews the expected
results of canceling order item summaries from an order summary without
actually canceling them.

**•** `cancelOrderItemSummariesSubmit` —Cancels order item
summaries from an order summary.

**•** `confirmHeldFulfillmentOrderCapacity` —Confirms held
fulfillment order capacity. This value is available in API version 55.0 and
later.

**•** `createCreditMemoOrderSummary` —Creates a credit memo for
an order summary.

**•** `createFieldGnrnPromptTmplResp` —Creates a field generation
prompt template response. This value is available in API version 62.0 and
later.

**•** `createFulfillmentOrder` —Creates one or more fulfillment orders
and fulfillment order products for an order delivery group summary, which
defines a recipient and delivery method.

**•** `createFulfillmentOrders` —Creates fulfillment orders and
fulfillment order products for multiple order delivery group summaries,
each of which defines a recipient and delivery method. This value is available
in API version 51.0 and later.

**•** `createInvoiceFromChangeOrders` —Creates an invoice for one
or more change orders. This value is available in API version 56.0 and later.

**•** `createInvoiceFromFulfillmentOrder` —Creates an invoice
for a fulfillment order.

**•** `createOrderPaymentSummary` —Creates an order payment
summary for an authorization or payments belonging to an order summary.

**•** `createOrderSummary` —Creates an order summary for an order.

**•** `createReturnOrder` —Creates a return order and return order items
for an order.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `ensureFundsOrderSummaryAsync` —Triggers an asynchronous
background process to ensure funds through a payment provider for an
invoice belonging to an order summary.

**•** `ensureRefundsOrderSummaryAsync` —Triggers an asynchronous
background process to ensure refunds through a payment provider for an
invoice belonging to an order summary.

**•** `getFulfillmentOrderCapacityValues` —Gets fulfillment
order capacity information. This value is available in API version 55.0 and
later.

**•** `holdFulfillmentOrderCapacity` —Holds fulfillment order
capacity. This value is available in API version 55.0 and later.

**•** `orderRoutingFindRoutesWithFewestSplits` —Evaluates
ordered product quantities against available inventory to determine the
smallest combination of locations that can fulfill the order. This value is
available in API version 51.0 and later.

**•** `orderRoutingFindRoutesWithFewestSplitsUsingOCI` —Evaluates
ordered product quantities against available inventory at specified location
groups and locations to determine the smallest combination of locations
that can fulfill the order. This value is available in API version 54.0 and later.

**•** `orderRoutingRankByAverageDistance` —Calculates the
average distance from sets of inventory locations to an order recipient, and
returns the sets sorted by that average distance. This value is available in
API version 51.0 and later.

**•** `releaseHeldFulfillmentOrderCapacity` —Releases held
fulfillment order capacity. This value is available in API version 55.0 and
later.

**•** `returnOrderItemSummariesPreview` —Previews the expected
results of returning order item summaries from an order summary without
actually returning them.

**•** `returnOrderItemSummariesSubmit` —Returns order item
summaries from an order summary.

**•** `returnReturnOrderItems` —Processes return order line items.

[For values used in Financial Services Cloud, see Flow for Financial Services](https://developer.salesforce.com/docs/atlas.en-us.260.0.financial_services_cloud_object_reference.meta/financial_services_cloud_object_reference/fsc_meta_visual_workforce.htm)
[Cloud.](https://developer.salesforce.com/docs/atlas.en-us.260.0.financial_services_cloud_object_reference.meta/financial_services_cloud_object_reference/fsc_meta_visual_workforce.htm)

For values used in Fundraising for Nonprofit Cloud, see Flow for Fundraising.

[For values used in Health Cloud, see Flow for Health Cloud.](https://developer.salesforce.com/docs/atlas.en-us.260.0.health_cloud_object_reference.meta/health_cloud_object_reference/health_cloud_flow_metadata_api.htm)

[For values used in Manufacturing Cloud, see Flow for Manufacturing Cloud.](https://developer.salesforce.com/docs/atlas.en-us.260.0.mfg_api_devguide.meta/mfg_api_devguide/mfg_flow_metadata_api.htm)

[For values used in Automotive Cloud, see Flow for Automotive Cloud.](https://developer.salesforce.com/docs/atlas.en-us.mfg_api_devguide.meta/mfg_api_devguide/https://developer.salesforce.com/docs/atlas.en-us.260.0.automotive_cloud.meta/automotive_cloud/auto_flow_metadata_api.htm)

This value is used in Omnistudio.

**•** `executeIntegrationProcedure` —Executes an Integration
Procedure with Agentforce configured. This value is available in API version
64.0 and later.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

These values are used in Rebate Management.

**•** `addRebateMemberList` —Adds a list of members to a rebate program.
This value is available in API version 51.0 and later.

**•** `calculateProjectedRebateAmount` —Calculates the projected
rebate amount for rebate types associated with a specified transaction ID.
This value is available in API version 54.0 and later.

**•** `calculateRebateAmountAndUpsertPayout` —Calculates the
rebate amount and upserts the rebate payout for the specified aggregate
record. This value is available in API version 51.0 and later.

**•** `getBenefitAndCalculateRebateAmount`                        - Gets benefit details,
and optionally calculates the rebate amount for the specified aggregate
record. This value is available in API version 51.0 and later.

**•** `getEligibleProgramRebateTypes` —Retrieves the eligible
program rebate types for a mapped object. This value is available in API
version 52.0 and later.

**•** `generateRebatePayoutPeriods` —Generates payout periods for
a rebate program based on the frequency specified in the program. This
value is available in API version 51.0 and later.

**•** `processRebatesBatchCalculationJob` —Processes a rebate
batch calculation job from the Data Processing Engine. This value is available
in API version 51.0 and later.

**•** `processProgramRebateTypeProducts` —Insert or delete records
in the Program Rebate Type Product object. This value is available in API
version 53.0 and later.

**•** `rebatesProcessCSV` —Processes an uploaded CSV file using Bulk
API 2.0 and converts the file’s data into records in the target object. This
value is available in API version 51.0 and later.

**•** `upsertCustomRebatePayout` —Upserts the custom calculated
rebate payout for the specified aggregate record. This value is available in
API version 51.0 and later.

These values are used in B2B Referral Management. If no version is specified,
the value is available in API version 64.0 and later.

**•** `enrollAdvocateB2bReferralProm` —Enroll an existing or new
customer as an advocate for a referral promotion.

**•** `processB2bReferralEvent` —Create referral event records when
an advocate refers a friend, or when referred friends sign up or make a
purchase.

These values are used in Referral Marketing.

**•** `processReferralEvent` —Create referral event records when an
advocate refers a friend, or when referred friends sign up or make a
purchase. This value is available in API version 60.0 and later.

These values are used in Loyalty Management.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `adjustPoints` —Adjusts loyalty points for a specified program member
or journal transaction. This value is available in API version 51.0 and later.

**•** `assignTierBenefits`                        - Assigns Member Benefits to a member tier
for benefits that are associated with a Benefit Action. This value is available
in API version 51.0 and later.

**•** `cancelAccrual` —Cancels a specific set of accrual transactions.

**•** `creditPoints` —Credits loyalty points to a specified program member’s
balance. This value is available in API version 51.0 and later.

**•** `cancelRedemption` —Reverts a specific set of redemption transactions.
This value is available in API version 51.0 and later.

**•** `changeTier` —Changes the tier for a specified program member. This
value is available in API version 51.0 and later.

**•** `changeTierWhenNoErrors` —Changes tier for a specified loyalty
program member only when all the input parameters meet the criteria.
This value is available in API version 51.0 and later.

**•** `debitPoints` —Debits loyalty points to a specified program member’s
balance. This value is available in API version 51.0 and later.

**•** `executeMemberBenefit` —Processes the benefit action associated
with the benefit, which is assigned to a loyalty program member. This value
is available in API version 51.0 and later.

**•** `generateMemberReferralCode` —Generates a unique 8-character
referral code for a loyalty program member. This value is available in API
version 57.0 and later.

**•** `getMemberActiveSegments` —Retrieve active Data 360 market
segments that a loyalty program member is a part of.

**•** `getTier` —Gets the current tier for a specified program member. This
value is available in API version 51.0 and later.

**•** `getPointsBalance` —Gets the loyalty points balance for a specified
program member. This value is available in API version 51.0 and later.

**•** `getLoyaltyPromotion` —Gets active loyalty promotions based on
a transaction journal. This value is available in API version 53.0 and later.

**•** `getLoyaltyPromotionBasedOnSalesforceCDP` —Gets
promotions for a member based on the market segment the member
belongs to. This value is available in API version 53.0 and later.

**•** `issueVoucher` —Issues a voucher for a member or contract. This value
is available in API version 51.0 and later.

**•** `mergeLoyaltyProgramMembership` —Merges two active loyalty
program member records that both belong to the same loyalty program.
This value is available in API version 56.0 and later.

**•** `transferMemberPointsToGroups` —Transfers points from an
individual member or a corporate member to the member’s associated
group. This value is available in API version 53.0 and later.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `transferPoints` —Transfers points from a source loyalty program
member to a target loyalty program member, or to a group that the
member is a part of. This value is available in API version 64.0 and later.

**•** `updateProgressForCumulativePromotionUsage` —Updates
the progress a member has made towards attaining a cumulative type
promotion. This value is available in API version 53.0 and later.

**•** `unmergeLoyaltyProgramMembership` —Unmerges loyalty
program member records that have a Merged status. The action unmerges
memberships in the Merged status from the previously merged
membership. This value is available in API version 56.0 and later.

**•** `runProgramProcess` —Triggers an active loyalty program process.
This value is available in API version 56.0 and later.

**•** `runProgramProcessForTransactionJournal` —Triggers an
active loyalty program process whose process type is TransactionJournal.
This value is available in API version 54.0 and later.

These values are for Decision Table.

**•** `decisionTableAction` —Runs an active decision table definition.
This value is available in API version 51.0 and later.

**•** `refreshDecisionTable` —Refreshes the decision table cache. This
value is available in API version 51.0 and later.

These values are for the Batch Management jobs.

**•** `batchJobAction` —Runs the batch management jobs definitions. This
value is available in API version 51.0 and later.

**•** `submitFailedRecordsBatchJob` —Resubmits an existing batch
job with failed records for processing. This value is available in API version
52.0 and later.

This value is for Data Processing Engine.

**•** `dataProcessingEngineAction` —Runs the data processing engine
definitions. This value is available in API version 51.0 and later.

This value is used for Einstein Visit Recommendation.

**•** `saveRecommendationDecision` —Save visit and task
recommendation decisions. This value is available in API version 51.0 and
later.

These values are used in Field Service. If no version is specified, the value is
available in API version 52.0 and later.

**•** `addWorkPlans` —Creates work plan and work step objects from the
work plan library. Available in API version 52.0 and later.

**•** `addWorkSteps` —Creates work step objects from the work plan library.
available in API version 52.0 and later.

**•** `deleteWorkPlans` —Deletes all the work plans and work steps
associated with a work order or work order line item. Available in API version
52.0 and later.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `generateWorkPlans` —Generates work plans based off rules defined
in the work plan library. Available in API version 52.0 and later.

**•** `assignApptForServiceResourceForFieldService` —Assigns
the service appointment selected by the dispatcher to a service resource,
in the gap identified in the service resource’s schedule on a specific date.
Available in API version 63.0 and later.

**•** `assignApptForServiceResourceForFieldService` —Assigns
the service appointment selected by the dispatcher to a service resource,
in the gap identified in the service resource’s schedule on a specific date.

For values used in Intelligent Form Reader, see Flow for Intelligent Form Reader.

For values used in Intelligent Document Reader, see Flow for Intelligent
Document Reader.

This value is used in Public Sector Solutions.

**•** `createBenefitDisbursement` —Creates a benefit disbursement
for an eligible benefit assignment. This value is available in API version 57.0
and later.

**•** `runRecordAggrBatchProcDef` —Runs a Data Processing Engine
definition to process an asynchronous batch job that creates or updates
record aggregation results. This value is available in API version 59.0 and
later.

These values are used in Unified Catalog. If no version is specified, the value is
available in API version 64.0 and later.

**•** `checkProductEligibility` —Determines whether a user is eligible
for a list of products, which represent service processes, based on
predefined criteria.

**•** `checkSvcPrcActionEligibility` —Determines whether an AI
agent is eligible for a list of products, which represent service processes,
and if the list is linked to a service process.

This value is used in the Get Opportunity Grounding Data flow.

**•** `getContentNote`                        - Gets the content note data for a specified record.
This value is available in API version 64.0 and later.

This value is used in the Process Field Update Suggestions flow.

**•** `getOrExecFieldUpdtSuggestion`                        - Enqueues requests to get
a field update suggestion from a field generation prompt template. This
value is available in API version 64.0 and later.

These values are used in Channel Revenue Management. Available in API
version 64.0 and later.

**•** `adjustPartnerInvShipAndDebit`                        - Adjusts the point of sale
during ship and debit claim processing to a different partner unsold
inventory. Available in API version 64.0 and later.

**•** `adjustPartnerUnsoldInventory`                        - Adjusts the partner unsold
inventory quantities and prices. Available in API version 64.0 and later.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

This value is used in Einstein Conversation Insights.

**•** `getConversationTranscript` —Gets the conversation transcript
for the specified voice or video call record. This value is available in API
version 63.0 and later.

These values are reserved for future use.

**•** `thanks`

**•** `metricRefresh`

**•** `exportSurveyResponses`

StrategyActionArg

Defines arguments passed to invocable actions associated with a strategy action.

**Field Name** **Field Type** **Description**

`name` string Required. Unique name for the parameter to pass to the invocable action.

`value` string Required. A Salesforce formula expression that is evaluated with the result
being used as the parameter value for the Strategy Action.

StrategyNodeUnionBase

Base class for nodes that perform a union of their children. Union nodes combine the outputs of their children to form the input to
themselves. StrategyNodeUnionBase extends StrategyNodeBase and inherits all of its fields. This is an abstract class.

**Field Name** **Field Type** **Description**

`limit` int Maximum number of results to output.

StrategyNodeFilter

Defines a filter element that filters recommendations. It extends StrategyNodeUnionBase and inherits all its fields.

**Field Name** **Field Type** **Description**

`expression` string

StrategyNodeIf

Required. A formula expression that results in a boolean value when executed
on each recommendation in the node’s input. Inputs that result in `true` form
the output, and inputs that result in `false` are excluded.

Selects specific children to execute and combines their results. Executes and returns results of children based on the array of child node
expressions. Extends StrategyNodeUnionBase and inherits all of its fields.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

`childNodeExpression` IfExpression[] Array of if expressions.

`onlyFirstMatch` boolean If `true`, selects only the results from the matching child. If `false`, selects
and combines results from all matching children. The default value is `false` .

IfExpression

Expression used by StrategyNodeIf.

**Field Name** **Field Type** **Description**

`childName` string Required. Name of child to match.

`expression` string Required. Formula expression returning `true` or `false` .

StrategyNodeInvocableAction

Defines an element that calls an Apex invocable action to generate or enhance a list of recommendations. It extends
StrategyNodeUnionBase and inherits all its fields.

**Field Name** **Field Type** **Description**

`action` string Required. The name of the invocable action to execute.

`argument` StrategyNodeInvocableActionArg[] List of arguments that are passed to the invocable action.

`isGenerator` boolean Required. If `true`, the UI displays the Generate element. If `false`, the UI
displays the Enhance element. Defaults to `false` .

```
type

```

InvocableActionType Required. The action type. Valid values are:
(enumeration of type

**•** `activateSessionPermSet` —Activates a session-based permission

string)

set for the running user.

**•** `activationSchema`         - Gets the activation schema for the specified
activation. This value is available in API version 64.0 and later.

**•** `addMessageToChat` —Adds a message to an existing Salesforce
Anywhere chat. This value is available in API version 49.0 and later.

**•** `addMessageToQuipChat` —Adds a Quip message to an existing chat
room. This value is available in API version 46.0 and later.

**•** `addMessageToQuipDocument` —Adds a Quip message to an existing
Quip document, spreadsheet, or slide. This value is available in API version
46.0 and later.

**•** `addQuipDocumentToFolder` —Adds an existing Quip document,
spreadsheet, or slide to an existing folder. This value is available in API
version 46.0 and later.

**•** `addUsersToChat` —Adds users to an existing Salesforce Anywhere
chat. This value is available in API version 49.0 and later.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `addUsersToQuipDocument` —Adds users, identified by their email
addresses, to an existing Quip document, spreadsheet, or slide. This value
is available in API version 46.0 and later.

**•** `addUsersToQuipChat` —Adds users, identified by their email
addresses, to an existing Quip chat room. This value is available in API
version 46.0 and later.

**•** `answerQuestionsWithSalesforceDocumentation` —Searches
Salesforce documentation to provide answer to questions, as well as links
to relevant articles.

**•** `attachQuipDocumentToRecord` —Attaches a Quip document,
spreadsheet, or slide to a Salesforce record. This value is available in API
version 46.0 and later.

**•** `apex` —Invokes an Apex method that has the @invocableMethod
annotation.

**•** `archiveKnowledgeArticles` —Archives a list of published
Knowledge articles. This value is available in API version 45.0 and later.

**•** `assignKnowledgeArticles` —Mass assigns knowledge articles
from article list views. This value is available in API version 44.0 and later.

**•** `cdpRunIdentityResolution` —Runs a Data 360 identity resolution
process. This value is available in API version 57.0 and later.

**•** `chat` —Creates a Salesforce Anywhere chat. This value is available in API
version 49.0 and later.

**•** `chatterPost` —Posts to Chatter.

**•** `choosePricebook` —Selects a price book.

**•** `contactRequestAction` —Creates a contact request record. This
value is available in API version 45.0 and later.

**•** `component` —Invokes the Lightning component that implements the
`lightning:availableForFlowActions` interface and that is
referenced by `actionName` . This value is available in API version 43.0
and later.

**•** `contentWorkspaceEnableFolders` —Enables folders in a library.

**•** `convertAttributesToJson` —Converts the given attributes into
a JSON string format. This value is available in API version 64.0 and later.

**•** `copyQuipDocument` —Creates a copy of an existing Quip document,
spreadsheet, or slide, and gives it a new title. This value is available in API
version 46.0 and later.

**•** `createDraftFromOnlineKnowledgeArticle` —Creates a draft
from a published knowledge article. This value is available in API version
45.0 and later.

**•** `createInvoiceFromFulfillmentOrder` —Creates an invoice
from a purchase order. Available to B2B Commerce. This value is available
in API version 49.0 and later.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `createQuipChat` —Creates a Quip chat room. This value is available
in API version 46.0 and later.

**•** `createQuipDocument` —Creates a Quip document, spreadsheet, or
slide. This value is available in API version 46.0 and later.

**•** `createQuipFolder` —Creates a Quip folder. This value is available in
API version 46.0 and later.

**•** `customNotificationAction` —Sends a custom notification. This
value is available in API version 46.0 and later.

**•** `deactivateSessionPermSet` —Deactivates a session-based
permission set for the running user.

**•** `deleteKnowledgeArticle` —Deletes a draft version (translation
or master-language) or an entire archived knowledge article. This value is
available in API version 46.0 and later.

**•** `dynamicSendSurveyInvitation` —Sends customized notifications
to users about important events or updates to the records that they’re
working on. This value is available in API version 51.0 and later.

**•** `editQuipDocument` —Modifies the contents of an existing Quip
document, spreadsheet, or slide. This value is available in API version 46.0
and later.

**•** `emailAlert` —Sends an email by referencing a workflow email alert

**•** `emailSimple` —Sends an email by using flow resources

**•** `exploreConversation` —Retrieves insights from a conversation.
This value is available in API version 61.0 and later.

**•** `externalService` —Invokes an External Service operation that makes
an HTTP request to an external system made available by an External Service
schema registered through Setup. This value is available in API version 46.0
and later.

**•** `findMatchingIndividuals` —Finds contact, lead, or employee
records that match a search term.

**•** `flow` —Invokes an autolaunched flow. This action type isn’t available for
flows with a processType of Flow or AutolaunchedFlow. To invoke an
autolaunched flow from one of those types, use FlowSubflow. This value
is available in API version 32.0 and later.

**•** `generateAiAgentResponse` —Generates a response from the AI
agent based on input and instructions to support intelligent, conversational
experiences. This value is available in API version 63.0 and later.

**•** `generateVerificationCode` —Sends a verification code to the
customer's email to verify their identity. This value is available in API version
63.0 and later.

**•** `getAgentConvTscp` —Retrieves the transcript of conversations
between the agent and the customer. This value is available in API version
50.0 and later.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `getArticleSmartLinkUrl` —Gets the Smart Link URL of the
Salesforce Knowledge article. Smart links go to the right article and version,
even when a new version is published or the URL name changes. This value
is available in API version 54.0 and later.

**•** `getPoliciesByObject` —Gets Policy Center policies that contain a
given object and returns a list of matching policy names.

**•** `getPoliciesByPolicyType` —Gets Policy Center policies of the
type specified in the user input, such as Data Backup or Data Archive.

**•** `getPolicyDetails` —Gets details about a policy in Policy Center,
such as the policy type and the objects the policy targets.

**•** `internalTestAction` —Reserved for internal use.

**•** `internalTestConnectApiAction` —Reserved for internal use.

**•** `limitRepetitions` —Limit the number of times the same
recommendation or offer appears on the same record or for the same user
during a time period in a recommendation strategy flow. This value is
available in API version 55.0 and later.

**•** `massUpdateAccountForecast` —Bulk updates forecasts
asynchronously. This value is available in API version 48.0 and later.

**•** `massUpdateSalesAgreement` —Bulk updates sales agreements
asynchronously. This value is available in API version 48.0 and later.

**•** `quickAction` —Invokes a QuickAction.

**•** `parseConvoAnalysis` —Parses conversation data to analyze
sentiment or extract actionable insights. This value is available in API version
51.0 and later.

**•** `publishActionableOrchSrcEvent` —Publishes events triggered
by an external system. This value is available in API version 62.0 and later.

**•** `publishKnowledgeArticles` —Mass publishes knowledge articles
from article list views. This value is available in API version 44.0 and later.

**•** `restoreKnowledgeArticleVersion` —Restores an archived
version of a knowledge article. This value is available in API version 45.0
and later.

**•** `sendAlert` —Sends Salesforce Anywhere alerts to users. This value is
available in API version 49.0 and later.

**•** `sendNotification` —Sends an available notification type. This value
is available in API version 54.0 and later.

**•** `sendSurveyInvitation` —Sends email survey invitations to leads,
contacts, and users in your org based on an action, such as when a customer
support case closes. This value is available in API version 47.0 and later.

**•** `performSurveySentimentAnalysis` —Perform survey sentiment
analysis to create or update the AI Sentiment Result records. This value is
available in API version 55.0 and later.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `skillsBasedRouting` [—Creates a PendingServiceRouting record](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_pendingservicerouting.htm)
used for Omni-Channel skills-based routing. This value is available in version
44.0 and later.

**•** `slackArchiveChannel` —Archives a Slack channel in a Slack
workspace. This value is available in API version 54.0 and later.

**•** `slackCheckUsersAreConnectedToSlack` —Indicates whether
a collection of Salesforce users is connected to a given Slack app. This value
is available in API version 54.0 and later.

**•** `slackCreateChannel` —Creates a Slack channel in a Slack workspace.
This value is available in API version 54.0 and later.

**•** `slackGetConversationInfo` —Retrieves the name of a Slack
channel or group direct message and finds out whether it’s archived. This
value is available in API version 54.0 and later.

**•** `slackInviteUsersToChannel` —Adds users who are connected
to a given Slack app to a Slack channel or group direct message. This value
is available in API version 54.0 and later.

**•** `slackPinMessage` —Pin or unpin a message in a Slack channel or
group direct message. This value is available in API version 54.0 and later.

**•** `slackPostMessage` —Send a message to a Slack channel or group
direct message. This value is available in API version 54.0 and later.

**•** `slackSendMessageToLaunchFlow` —Send a message to a Slack
channel, direct message, or the Messages tab of a Slack app that includes
a button that a recipient can use to launch a screen flow. This value is
available in API version 55.0 and later.

**•** `slackUpdateMessage` —Edits a message that was previously sent
to a Slack channel or group direct message. This value is available in API
version 54.0 and later.

**•** `submitKnowledgeArticleForTranslation` —Submits a
published or draft knowledge article for translation. This value is available
in API version 46.0 and later.

**•** `submit` —Submits a record for approval.

**•** `triggerJourney`                        - Send an individual to a specified journey. This
value is available in API version 64.0 and later.

**•** `verifyCustomerCode` —Verifies the code entered by the customer
to complete identity verification. This value is available in API version 63.0
and later.

These values are used in Omnichannel Inventory. If no version is specified, the
value is available in API version 51.0 and later.

**•** `ociCreateReservation` —Creates one or more inventory
reservations at a location or location group.

**•** `ociFulfillReservation` —Fulfills one or more inventory
reservations at a location.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `ociGetAvailability` —Gets inventory availability data for one or
more products at one or more inventory locations or location groups.

**•** `ociReleaseReservation` —Releases one or more inventory
reservations.

**•** `ociTransferReservation` —Transfers one or more inventory
reservations between locations or location groups.

These values are used in the B2B Commerce Checkout Flow. If no version is
specified, the value is available in API version 47.0 and later.

**•** `updateCheckoutSessionStateAction` —Updates the checkout
session next state for checkout flows. This value is available in API version
49.0 and later.

**•** `priceCart` —Requests prices for all items in a cart during B2B Commerce
checkout. This value is available in API version 47.0 and later.

**•** `checkoutSessionAction` —Initiates or retrieves an existing
Checkout Session for Checkout Flows. Available to B2B Commerce. This
value is available in API version 49.0 and later.

**•** `cancelCartAsyncOperation` —Cancels a WebCart’s async
operation. Available to B2B Commerce. This value is available in API version
49.0 and later.

**•** `calcCartPromotionsAction` —Requests a full cart promotion
calculation of all applicable line items in the Web Cart during B2B
Commerce checkout. This value is available in API version 52.0 and later.

**•** `checkCartInventoryAction` —Requests an inventory for all items
in a Web Cart during B2B Commerce checkout. This value is available in
API version 47.0 and later.

**•** `calcCartShipmentAction` —Calculates the shipping cost for all
items in a Web Cart during B2B Commerce checkout. This value is available
in API version 47.0 and later.

**•** `cartToOrderAction` —Creates a Salesforce Standard Order in draft
mode. This value is available in API version 47.0 and later.

**•** `activateOrderAction` —Activates a draft order, which creates an
order summary. This value is available in API version 47.0 and later.

[For values used in Business Rules Engine, see Flow for Business Rules Engine.](https://developer.salesforce.com/docs/atlas.en-us.260.0.industries_reference.meta/industries_reference/bre_flow_metadata_api.htm)

These values are used in Context Service. If no version is specified, the value is
available in API version 64.0 and later.

**•** `deleteContextCache` —Deletes the context instance from the
context cache using specified context ID.

**•** `queryContextTags` —Queries context instance tags associated with
a context definition.

**•** `updateContextAttributes` —Updates attributes on the context
instance using context tags.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

These values are used in the Commerce Checkout Flow. If no version is specified,
the value is available in API version 55.0 and later.

**•** `addCartItem` —Adds an item to a cart during Commerce checkout.

**•** `createCart` —Creates a cart during Commerce checkout.

**•** `deleteCart` —Deletes a cart during Commerce checkout.

These values are used in Salesforce CMS Workflows and Approvals. If no version
is specified, the value is available in API version 58.0 and later.

**•** `managedContentPublishVariant` —Publishes a content variant
associated with a flow. This value is available in API version 59.0 and later.

**•** `managedContentRoleStepInteractive` —Assigns a content
variant review to a CMS role.

**•** `managedContentUnpublishVariant` —Unpublishes a published
content variant associated with a flow. This value is available in API version
59.0 and later.

**•** `managedContentVariantSetLockStatus` —Sets the locked
status of a content variant.

**•** `managedContentVariantSetReadyStatus` —Sets the ready
for publication status of a content variant.

These values are used in Employee Service. If no version is specified, the value
is available in API version 64.0 and later.

**•** `createServiceRequestCase` —Creates a case or incident for the
requested service.

**•** `getDirectDepositDetails` —Gets the direct deposit details for
the specified record ID.

**•** `getLeaveBalance` —Gets the leave balance of a specific employee.

These values are used in Insurance. If no version is specified, the value is available
in API version 63.0 and later.

**•** `cancelInsurancePolicy` —Cancel an insurance policy by using a
set of user inputs that represent policy details.

**•** `endorseInsurancePolicy` —Endorse an insurance policy by using
a set of user inputs that represent policy details.

**•** `getInsurancePolicy` —Get the details of an insurance policy.

**•** `issueInsurancePolicy`                        - Issue an insurance policy by using a set
of user inputs that represent policy details.

**•** `renewInsurancePolicy` —Renew an insurance policy by using a
set of user inputs that represent policy details.

These values are used in Insurance Brokerage. If no version is specified, the
value is available in API version 63.0 and later.

**•** `computeProducerSplits` —Compute the producer splits for the
producers associated with an Insurance Policy, for a Commission Statement
Line Item.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `createProducerCommissions` —Create records for the
commissions that producers receive for the insurance policy associated
with the specified commission statement line item, and update the
commission statement line item record status.

**•** `findInsurancePolicy` —Get the insurance policy associated with
a commission statement line item that matches the specified criteria, and
update the status of the commission statement line item record.

These values are used in Order Management. If no version is specified, the value
is available in API version 48.0 and later.

**•** `addOrderItemSummarySubmit` —Adds order item summaries to
an order summary. This value is available in API version 54.0 and later.

**•** `adjustOrderItemSummariesPreview` —Previews the expected
results of applying a price adjustment to order item summaries from an
order summary without actually applying it. This value is available in API
version 49.0 and later.

**•** `adjustOrderItemSummariesSubmit` —Applies a price adjustment
to order item summaries from an order summary. This value is available in
API version 49.0 and later.

**•** `authorizePayment` —Authorizes a card payment. This value is
available in API version 55.0 and later.

**•** `calcPriceProtectPayoutAmt` —Calculates the payout after a
price protection adjustment or execution is made. This value is available
in API version 63.0 and later.

**•** `cancelFulfillmentOrderItem` —Removes items from a
fulfillment order.

**•** `cancelOrderItemSummariesPreview` —Previews the expected
results of canceling order item summaries from an order summary without
actually canceling them.

**•** `cancelOrderItemSummariesSubmit` —Cancels order item
summaries from an order summary.

**•** `confirmHeldFulfillmentOrderCapacity` —Confirms held
fulfillment order capacity. This value is available in API version 55.0 and
later.

**•** `createCreditMemoOrderSummary` —Creates a credit memo for
an order summary.

**•** `createFieldGnrnPromptTmplResp` —Creates a field generation
prompt template response. This value is available in API version 62.0 and
later.

**•** `createFulfillmentOrder` —Creates one or more fulfillment orders
and fulfillment order products for an order delivery group summary, which
defines a recipient and delivery method.

**•** `createFulfillmentOrders` —Creates fulfillment orders and
fulfillment order products for multiple order delivery group summaries,


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

each of which defines a recipient and delivery method. This value is available
in API version 51.0 and later.

**•** `createInvoiceFromChangeOrders` —Creates an invoice for one
or more change orders. This value is available in API version 56.0 and later.

**•** `createInvoiceFromFulfillmentOrder` —Creates an invoice
for a fulfillment order.

**•** `createOrderPaymentSummary` —Creates an order payment
summary for an authorization or payments belonging to an order summary.

**•** `createOrderSummary` —Creates an order summary for an order.

**•** `createReturnOrder` —Creates a return order and return order items
for an order.

**•** `ensureFundsOrderSummaryAsync` —Triggers an asynchronous
background process to ensure funds through a payment provider for an
invoice belonging to an order summary.

**•** `ensureRefundsOrderSummaryAsync` —Triggers an asynchronous
background process to ensure refunds through a payment provider for an
invoice belonging to an order summary.

**•** `getFulfillmentOrderCapacityValues` —Gets fulfillment
order capacity information. This value is available in API version 55.0 and
later.

**•** `holdFulfillmentOrderCapacity` —Holds fulfillment order
capacity. This value is available in API version 55.0 and later.

**•** `orderRoutingFindRoutesWithFewestSplits` —Evaluates
ordered product quantities against available inventory to determine the
smallest combination of locations that can fulfill the order. This value is
available in API version 51.0 and later.

**•** `orderRoutingFindRoutesWithFewestSplitsUsingOCI` —Evaluates
ordered product quantities against available inventory at specified location
groups and locations to determine the smallest combination of locations
that can fulfill the order. This value is available in API version 54.0 and later.

**•** `orderRoutingRankByAverageDistance` —Calculates the
average distance from sets of inventory locations to an order recipient, and
returns the sets sorted by that average distance. This value is available in
API version 51.0 and later.

**•** `releaseHeldFulfillmentOrderCapacity` —Releases held
fulfillment order capacity. This value is available in API version 55.0 and
later.

**•** `returnOrderItemSummariesPreview` —Previews the expected
results of returning order item summaries from an order summary without
actually returning them.

**•** `returnOrderItemSummariesSubmit` —Returns order item
summaries from an order summary.

**•** `returnReturnOrderItems` —Processes return order line items.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

These values are used in Financial Services Cloud.

**•** `createFinancialRecords` —Creates person accounts, contacts,
financial accounts, properties, assets, and liabilities from a residential loan
application. This value is available in API version 49.0 and later.

For values used in Fundraising for Nonprofit Cloud, see Flow for Fundraising.

[For values used in Health Cloud, see Flow for Health Cloud.](https://developer.salesforce.com/docs/atlas.en-us.260.0.health_cloud_object_reference.meta/health_cloud_object_reference/health_cloud_flow_metadata_api.htm)

[For values used in Manufacturing Cloud, see Flow for Manufacturing Cloud.](https://developer.salesforce.com/docs/atlas.en-us.260.0.mfg_api_devguide.meta/mfg_api_devguide/mfg_flow_metadata_api.htm)

This value is used in Omnistudio.

**•** `executeIntegrationProcedure` —Executes an Integration
Procedure with Agentforce configured. This value is available in API version
64.0 and later.

These values are used in Rebate Management.

**•** `addRebateMemberList` —Adds a list of members to a rebate program.
This value is available in API version 51.0 and later.

**•** `calculateProjectedRebateAmount` —Calculates the projected
rebate amount for rebate types associated with a specified transaction ID.
This value is available in API version 54.0 and later.

**•** `calculateRebateAmountAndUpsertPayout` —Calculates the
rebate amount and upserts the rebate payout for the specified aggregate
record. This value is available in API version 51.0 and later.

**•** `getBenefitAndCalculateRebateAmount`                        - Gets benefit details,
and optionally calculates the rebate amount for the specified aggregate
record. This value is available in API version 51.0 and later.

**•** `getEligibleProgramRebateTypes` —Retrieves the eligible
program rebate types for a mapped object. This value is available in API
version 52.0 and later.

**•** `generateRebatePayoutPeriods` —Generates payout periods for
a rebate program based on the frequency specified in the program. This
value is available in API version 51.0 and later.

**•** `processRebatesBatchCalculationJob` —Processes a rebate
batch calculation job from the Data Processing Engine. This value is available
in API version 51.0 and later.

**•** `processProgramRebateTypeProducts` —Insert or delete records
in the Program Rebate Type Product object. This value is available in API
version 53.0 and later.

**•** `rebatesProcessCSV` —Processes an uploaded CSV file using Bulk
API 2.0 and converts the file’s data into records in the target object. This
value is available in API version 51.0 and later.

**•** `upsertCustomRebatePayout` —Upserts the custom calculated
rebate payout for the specified aggregate record. This value is available in
API version 51.0 and later.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

These values are used in B2B Referral Management. If no version is specified,
the value is available in API version 64.0 and later.

**•** `enrollAdvocateB2bReferralProm` —Enroll an existing or new
customer as an advocate for a referral promotion.

**•** `processB2bReferralEvent` —Create referral event records when
an advocate refers a friend, or when referred friends sign up or make a
purchase.

These values are used in Referral Marketing.

**•** `processReferralEvent` —Create referral event records when an
advocate refers a friend, or when referred friends sign up or make a
purchase. This value is available in API version 60.0 and later.

These values are used in Loyalty Management.

**•** `adjustPoints` —Adjusts loyalty points for a specified program member
or journal transaction. This value is available in API version 51.0 and later.

**•** `assignTierBenefits`                        - Assigns Member Benefits to a member tier
for benefits that are associated with a Benefit Action. This value is available
in API version 51.0 and later.

**•** `cancelAccrual` —Cancels a specific set of accrual transactions.

**•** `creditPoints` —Credits loyalty points to a specified program member’s
balance. This value is available in API version 51.0 and later.

**•** `cancelRedemption` —Reverts a specific set of redemption transactions.
This value is available in API version 51.0 and later.

**•** `changeTier` —Changes the tier for a specified program member. This
value is available in API version 51.0 and later.

**•** `changeTierWhenNoErrors` —Changes tier for a specified loyalty
program member only when all the input parameters meet the criteria.
This value is available in API version 51.0 and later.

**•** `debitPoints` —Debits loyalty points to a specified program member’s
balance. This value is available in API version 51.0 and later.

**•** `executeMemberBenefit` —Processes the benefit action associated
with the benefit, which is assigned to a loyalty program member. This value
is available in API version 51.0 and later.

**•** `generateMemberReferralCode` —Generates a unique 8-character
referral code for a loyalty program member. This value is available in API
version 57.0 and later.

**•** `getMemberActiveSegments` —Retrieve active Data 360 market
segments that a loyalty program member is a part of.

**•** `getTier` —Gets the current tier for a specified program member. This
value is available in API version 51.0 and later.

**•** `getPointsBalance` —Gets the loyalty points balance for a specified
program member. This value is available in API version 51.0 and later.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

**•** `getLoyaltyPromotion` —Gets active loyalty promotions based on
a transaction journal. This value is available in API version 53.0 and later.

**•** `getLoyaltyPromotionBasedOnSalesforceCDP` —Gets
promotions for a member based on the market segment the member
belongs to. This value is available in API version 53.0 and later.

**•** `issueVoucher` —Issues a voucher for a member or contract. This value
is available in API version 51.0 and later.

**•** `mergeLoyaltyProgramMembership` —Merges two active loyalty
program member records that both belong to the same loyalty program.
This value is available in API version 56.0 and later.

**•** `transferMemberPointsToGroups` —Transfers points from an
individual member or a corporate member to the member’s associated
group. This value is available in API version 53.0 and later.

**•** `transferPoints` —Transfers points from a source loyalty program
member to a target loyalty program member, or to a group that the
member is a part of. This value is available in API version 64.0 and later.

**•** `updateProgressForCumulativePromotionUsage` —Updates
the progress a member has made towards attaining a cumulative type
promotion. This value is available in API version 53.0 and later.

**•** `unmergeLoyaltyProgramMembership` —Unmerges loyalty
program member records that have a Merged status. The action unmerges
memberships in the Merged status from the previously merged
membership. This value is available in API version 56.0 and later.

**•** `runProgramProcess` —Triggers an active loyalty program process.
This value is available in API version 56.0 and later.

**•** `runProgramProcessForTransactionJournal` —Triggers an
active loyalty program process whose process type is TransactionJournal.
This value is available in API version 54.0 and later.

These values are for Decision Table.

**•** `decisionTableAction` —Runs an active decision table definition.
This value is available in API version 51.0 and later.

**•** `refreshDecisionTable` —Refreshes the decision table cache. This
value is available in API version 51.0 and later.

These values are for the Batch Management jobs.

**•** `batchJobAction` —Runs the batch management jobs definitions. This
value is available in API version 51.0 and later.

**•** `submitFailedRecordsBatchJob` —Resubmits an existing batch
job with failed records for processing. This value is available in API version
52.0 and later.

This value is for Data Processing Engine.

**•** `dataProcessingEngineAction` —Runs the data processing engine
definitions. This value is available in API version 51.0 and later.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

This value is used for Einstein Visit Recommendation.

**•** `saveRecommendationDecision` —Save visit and task
recommendation decisions. This value is available in API version 51.0 and
later.

These values are used in Field Service. If no version is specified, the value is
available in API version 52.0 and later.

**•** `addWorkPlans` —Creates work plan and work step objects from the
work plan library.

**•** `addWorkSteps` —Creates work step objects from the work plan library.

**•** `deleteWorkPlans` —Deletes all the work plans and work steps
associated with a work order or work order line item.

**•** `generateWorkPlans` —Generates work plans based off rules defined
in the work plan library.

For values used in Intelligent Form Reader, see Flow for Intelligent Form Reader.

For values used in Intelligent Document Reader, see Flow for Intelligent
Document Reader.

This value is used in Public Sector Solutions.

**•** `createBenefitDisbursement` —Creates a benefit disbursement
for an eligible benefit assignment. This value is available in API version 57.0
and later.

**•** `runRecordAggrBatchProcDef` —Runs a Data Processing Engine
definition to process an asynchronous batch job that creates or updates
record aggregation results. This value is available in API version 59.0 and
later.

These values are used in Unified Catalog. If no version is specified, the value is
available in API version 64.0 and later.

**•** `checkProductEligibility` —Determines whether a user is eligible
for a list of products, which represent service processes, based on
predefined criteria.

**•** `checkSvcPrcActionEligibility` —Determines whether an AI
agent is eligible for a list of products, which represent service processes,
and if the list is linked to a service process.

This value is used in the Get Opportunity Grounding Data flow.

**•** `getOpportunityContentNote`                        - Gets the content note data for
a specified opportunity record. This value is available in API version 64.0
and later.

This value is used in the Process Field Update Suggestions flow.

**•** `getOrExecFieldUpdtSuggestion`                        - Enqueues requests to get
a field update suggestion from a field generation prompt template. Also
enqueues requests to update a field based on the generated suggestion.
This value is available in API version 64.0 and later.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

This value is used in Einstein Conversation Insights.

**•** `getConversationTranscript` —Gets the conversation transcript
for the specified voice or video call record. This value is available in API
version 63.0 and later.

These values are used in Channel Revenue Management. Available in API
version 64.0 and later.

**•** `adjustPartnerInvShipAndDebit`                        - Adjusts the point of sales
record during ship and debit claim processing to a different partner unsold
inventory. Available in API version 64.0 and later.

**•** `adjustPartnerUnsoldInventory`                        - Adjusts the partner unsold
inventory quantities and prices. Available in API version 64.0 and later.

These values are reserved for future use.

**•** `thanks`

**•** `metricRefresh`

**•** `exportSurveyResponses`

StrategyNodeInvocableActionArg

Defines arguments passed to an Apex invocable action that generates or enhances a list of recommendations.

**Field Name** **Field Type** **Description**

`name` string Required. Unique name for the parameter to pass to the invocable action. The
name must match a parameter that's defined in the invocable action.

`value` string Required. A Salesforce formula expression that is evaluated with the result used
as the parameter value for the action.

StrategyNodeRecommendationLimit

Filters out recommendations that have already been accepted or rejected. Extends StrategyNodeUnionBase and inherits all of its fields.

**Field Name** **Field Type** **Description**

```
filterMode

```

StrategyReactionType
Available reactions to filter out. The valid values are:
(enumeration of type

**•** `Accepted`

string)

**•** `Rejected`

`lookbackDuration` int Number of days to search back.

`maxRecommendationCount` int Maximum number of times recommendation has been accepted or rejected.


Metadata Types RecommendationStrategy

StrategyNodeRecommendationLoad

Retrieves Recommendation objects. Extends StrategyNodeUnionBase and inherits all of its fields.

**Field Name** **Field Type** **Description**

`condition` RecommendationLoadCondition[] Array of conditions specifying which recommendations to load.

`conditionLogic` string Logic to combine conditions, either AND or OR. All conditions are combined
(not mixed). For example: `Cond1 AND Cond2 AND Cond3` .

`object` string Required. Specifies the API name of the sObject from which recommendations
are loaded. For example, the field references `Account` or

`MyCustomObject__c` and not a specific record of that object. Available
in API version 48.0 and later.

`sortField` StrategyNodeSortField The field to sort on. Available in API version 48.0 and later.

RecommendationLoadCondition

Represents a condition used as part of the query constructed by StrategyNodeRecommendationLoad.

**Field Name** **Field Type** **Description**

`field` string Required. Any field from Recommendation BPO (SOAP) object.

Required.

Valid values are:

**•** `EQUALS`

**•** `GREATER_THAN`

**•** `GREATER_THAN_OR_EQUAL_TO`

**•** `LESS_THAN`

**•** `LESS_THAN_OR_EQUAL_TO`

**•** `NOT_EQUALS`

**•** `LIKE`

**•** `STARTS_WITH`

**•** `ENDS_WITH` =

**•** `CONTAINS`

```
operator

```

RecommendationCond **i** tonOperator
(enumeration of type
string)

`value` RecommendationConditionValue Required. Constant value to use in query.

RecommendationConditionValue

Represents a value used as part of a RecommendationCondition.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

Required.

Valid values are:

**•** `TEXT`

**•** `NUMBER`

**•** `BOOLEAN`

**•** `DATE`

**•** `DATE_TIME`

**•** `TIME`

```
type

```

RecommendationCondtonValueType **i**
(enumeration of type
string)

`value` string Required. The constant value.

StrategyNodeSortField

Defines the field to sort on for StrategyNodeSort and StrategyNodeRecommendationLoad.

**Field Name** **Field Type** **Description**

`name` string Required. Name of the field to sort.

`nullsFirst` boolean If `true`, null values are sorted to the beginning of the list. Defaults to `false` .

```
order

```

StrategyNodeSort

SortOrder
Order in which the list is sorted. Defaults to `Asc` . Valid values are:
(enumeration of type

**•** `Asc` (ascending)

string)

**•** `Desc` (descending)

Sorts the recommendations. Extends StrategyNodeUnionBase and inherits all of its fields.

**Field Name** **Field Type** **Description**

`field` StrategyNodeSortField Required. Field to sort on.

StrategyNodeUnion

StrategyNodeUnion combines the output of all its child nodes. StrategyNodeUnion is a concrete implementation of StrategtNodeUnionBase
and inherits all its fields.

StrategyNodeMap

Set recommendation fields with values. Extends StrategyNodeUnionBase and inherits all of its fields.


Metadata Types RecommendationStrategy

**Field Name** **Field Type** **Description**

`mapExpression` MapExpression on List of MaxExpressions.
page 1802[]

StrategyNodeExclusive

Returns results from the first child node that has results and no other. Extends StrategyNodeUnionBase and inherits all its fields.

MapExpression

Sets the value for a recommendation field used by the strategy.

**Field Name** **Field Type** **Description**

`expression` string Required. A formula expression that results in a valid value supported by the
data type specified in the `type` field.

`name` string Required. Recommendation field name that the expression sets the value for.

`type` string

Required. The data type of the value resulting from the value in the
`expression` field.

Valid values are:

**•** `BOOLEAN`

**•** `CURRENCY`

**•** `DATE`

**•** `DOUBLE`

**•** `DATE_TIME`

**•** `INTEGER`

**•** `LONG`

**•** `PERCENT`

**•** `TEXT`

**•** `TIME`

Declarative Metadata Sample Definition

The following is an example of a RecommendationStrategy component that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<RecommendationStrategy xmlns="http://soap.sforce.com/2006/04/metadata">

   <contextRecordType>Asset</contextRecordType>

   <description>Hills Brothers Coffee strategy to handle machine down

incidents</description>

   <if>

     <childNode>IfNoEscaladeOrBetterSupport</childNode>

     <childNode>IfModel</childNode>

```


Metadata Types RecommendationStrategy

```
        <description>If Machine Down</description>

        <label>RootNode</label>

        <name>RootNode</name>

        <childNodeExpression>

           <childName>IfModel</childName>

           <expression>ISPICKVAL($Record.Status, &quot;OutOfOrder&quot;)</expression>

        </childNodeExpression>

        <childNodeExpression>

           <childName>IfNoEscaladeOrBetterSupport</childName>

           <expression>ISPICKVAL($Record.Status, &quot;OutOfOrder&quot;)</expression>

        </childNodeExpression>

        <onlyFirstMatch>false</onlyFirstMatch>

      </if>

      <if>

        <childNode>LoadEscalade</childNode>

        <description>If Customer does not have escalade support plan</description>

        <label>IfNoEscaladeOrBetterSupport</label>

        <name>IfNoEscaladeOrBetterSupport</name>

        <childNodeExpression>

           <childName>LoadEscalade</childName>

           <expression>NOT(ISPICKVAL($Record.Account.SLA__c, &quot;Gold&quot;) ||

   ISPICKVAL($Record.Account.SLA__c, &quot;Platinum&quot;))</expression>

        </childNodeExpression>

        <onlyFirstMatch>false</onlyFirstMatch>

      </if>

      <if>

        <childNode>LoadMiniDiagnostic</childNode>

        <childNode>LoadMaxiDiagnostic</childNode>

        <description>If Machine Model switch node</description>

        <label>IfModel</label>

        <name>IfModel</name>

        <childNodeExpression>

           <childName>LoadMiniDiagnostic</childName>

         <expression>$Record.Product2.Name == &quot;Mini Coffee Roaster&quot;</expression>

        </childNodeExpression>

        <childNodeExpression>

           <childName>LoadMaxiDiagnostic</childName>

         <expression>$Record.Product2.Name == &quot;Maxi Coffee Roaster&quot;</expression>

        </childNodeExpression>

        <onlyFirstMatch>false</onlyFirstMatch>

      </if>

      <label>HillsBrothersCoffee</label>

      <recommendationLoad>

        <description>Load upgrade to escalade support plan</description>

        <label>LoadEscalade</label>

        <name>LoadEscalade</name>

        <condition>

           <field>Name</field>

           <operator>EQUALS</operator>

           <value>

             <type>TEXT</type>

             <value>Upgrade your Maintenance Package</value>

```


Metadata Types RecommendationStrategy

```
           </value>

        </condition>

        <conditionLogic>and</conditionLogic>

      </recommendationLoad>

      <recommendationLoad>

        <description>Load Mini Coffee Roaster Diagnostic Troubleshooting

   proposition</description>

        <label>LoadMiniDiagnostic</label>

        <name>LoadMiniDiagnostic</name>

        <condition>

           <field>Name</field>

           <operator>EQUALS</operator>

           <value>

             <type>TEXT</type>

             <value>Mini Coffee Roaster Diagnostic Troubleshooting</value>

           </value>

        </condition>

        <conditionLogic>and</conditionLogic>

      </recommendationLoad>

      <recommendationLoad>

        <description>Load Maxi Coffee Roaster Diagnostic Troubleshooting

   proposition</description>

        <label>LoadMaxiDiagnostic</label>

        <name>LoadMaxiDiagnostic</name>

        <condition>

           <field>Name</field>

           <operator>EQUALS</operator>

           <value>

             <type>TEXT</type>

             <value>Maxi Coffee Roaster Diagnostic Troubleshooting</value>

           </value>

        </condition>

        <conditionLogic>and</conditionLogic>

      </recommendationLoad>

      <union>

        <childNode>RootNode</childNode>

        <label>Output</label>

        <name>Output</name>

      </union>

      <invocableAction>

        <action>MyInvocableApexClass</action>

        <isGenerator>true</isGenerator>

        <type>apex</type>

        <argument>

           <name>MyNameParam</name>

           <value>$User.FirstName</value>

        </argument>

        <argument>

           <name>MyIdParam</name>

           <value>$Record.Id</value>

        </argument>

      </invocableAction>

      <map>

        <expression>

```


### Metadata Types RecordActionDeployment

```
           <name>Name</name>

           <expression>'Hello' & $User.FirstName</expression>

           <type>TEXT</type>

        </expression>

        <expression>

           <name>MyDynamicField</name>

           <expression>Id == $Record.Id</expression>

           <type>BOOLEAN</type>

        </expression>

      </map>

   </RecommendationStrategy>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### RecordActionDeployment

Represents configuration settings for the Actions & Recommendations, Action Launcher, and Bulk Action Panel components. For example,
you can have a deployment that specifies which types of actions to display, default actions for channels, and the actions that users can
add at runtime. If the component shows Next Best Action recommendations, the deployment configures which strategies to use and
how recommendations appear. This type extends the Metadata metadata type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### RecordActionDeployment values are stored in the developer_name .deployment file in the recordActionDeployments

directory.

Note: We don’t recommend programmatically changing the API name of a RecordActionDeployment.

Version

### RecordActionDeployment is available in API version 45.0 and later.

Fields

**Field Name** **Field Type** **Description**

### channelConfigurations RecordActionDeploymentChannel Specifies configuration settings for different channels in an Actions

& Recommendations deployment.

`componentName` ComponentName (enumeration Specifies the name of the component used in the deployment:
of type string)

**•** `ActionsAndRecommendations` —0


Metadata Types RecordActionDeployment

**Field Name** **Field Type** **Description**

**•** `ActionLauncher` —1

**•** `BulkActionPanel` —2. This value is available in API
version 60.0 and later

For example, a value of 1 indicates that 1 is stored in the database
if Action Launcher is used to create a deployment. Available in API
version 56.0 and later.

`deploymentContexts` RecordActionDeploymentContext Specifies the object context for quick actions and Next Best Action
strategies. Available in API version 46.0 and later.

`hasComponents` boolean

Indicates whether the record actions deployment includes
components ( `true` ) or not ( `false` ). Available in API version 61.0
and later.

`hasGuidedActions` boolean Specifies that the component shows standard actions; for example,
flows and quick actions. Available in API version 46.0 and later.

hasOmniscripts boolean

Indicates whether the record actions deployment includes
OmniScripts ( `true` ) or not ( `false` ). Available in API version 56.0
and later. The default value is `false` .

`hasRecommendations` boolean Specifies that the component shows recommendations from a
Next Best Action strategy. Available in API version 46.0 and later.

`masterLabel` string Required. Specifies the name of the deployment.

`recommendation` RecordActionRecommendation Specifies settings for how Next Best Action recommendations
appear in the component. Available in API version 46.0 and later.

`selectableItems` RecordActionDeploymentSelectableItems Specifies the actions that users can add at runtime.

`shouldLaunchActionOnReject` boolean Required. If `true`, launch the flow when the recommendation is
rejected by the agent. Available in API version 48.0 and later.

RecordActionDefaultItem

Represents actions and attributes specified as channel defaults in a deployment.

**Field Name** **Field Type** **Description**

`action` string Required. Specifies the API name of an action. For example, the API name of a
flow, such as `Verify_Information` .

`isMandatory` boolean Specifies whether the action is marked as mandatory. The default value is
`false` .

`isUiRemoveHidden` boolean Specifies whether the remove option is hidden in the UI. The default value is
false. If `true`, the UI hides the ability to remove the action from the list.


Metadata Types RecordActionDeployment

**Field Name** **Field Type** **Description**

```
pinned

```

PinnedAction Required. Indicates whether the action is pinned to the `Top` or `Bottom`, or
(enumeration of type unpinned ( `None` ). The default value is `None` .
string)

`position` int Required. Indicates the order of the action among all actions associated with
this record.

```
type

```

RecordActionType Required. The type of action that’s associated with the record. Valid values are:
(enumeration of type

**•** `Flow`

string)

**•** `Flow`

**•** `QuickAction` (Available in API version 46.0 and later.)

**•** `OmniScript` (Available in API version 56.0 and later.)

**•** `LWC` (Available in API version 62.0 and later.)

**•** `SvcCatalogItemDef` (Available in API version 62.0 and later.)

**•** `WebLink` (Available in API version 62.0 and later.)

RecordActionDeploymentChannel

Specifies channel-specific defaults to show in the Actions & Recommendations component. The component displays the channel defaults
when the list is otherwise empty.

**Field Name** **Field Type** **Description**

`channel` ChannelSource Required. Specifies the channel. Valid values are `Phone`, `Chat`, or
(enumeration of type string) `Default` .

`channelItems` RecordActionDefaultItem

`isAutopopEnabled` boolean

RecordActionDeploymentContext

Specifies default actions for a channel and attributes for each action,
such as whether the action is pinned to the list top or bottom or whether
an action is considered mandatory.

Specifies whether the first action in the list is launched when the record
page opens. If `true`, the first action is launched. The default value is
`false` .

Specifies an object that provides context for quick actions and Next Best Action strategies. When the component appears on this type
of page, it includes object-specific quick actions and uses an object-specific strategy to filter recommendations. Available in API version
46.0 and later.

Note: We support a maximum of 10 objects that provide context within a deployment.

**Field Name** **Field Type** **Description**

`entityName` string Required. Specifies the API name of an object to use as context.


Metadata Types RecordActionDeployment

**Field Name** **Field Type** **Description**

`recommendationStrategy` string Specifies the API name of a Next Best Action strategy that overrides the default
strategy on this page. A strategy is a metadata type RecommendationStrategy.

RecordActionRecommendation

Specifies settings to display Next Best Action recommendations in the component. Available in API version 46.0 and later.

**Field Name** **Field Type** **Description**

`defaultStrategy` string Specifies the API name of the default Next Best Action strategy, which is a
metadata type, RecommendationStrategy.

`hasDescription` boolean Required. If `true`, display the description for the recommendation.

`hasImage` boolean Required. If `true`, display the image for the recommendation.

`hasRejectAction` boolean Required. If `true`, display the label that the user clicks to reject the
recommendation.

`hasTitle` boolean Required. If `true`, display the title for the recommendation.

`maxDisplayRecommendations` int Required. Specifies the maximum number of recommendations to display.
Valid values are 1–4.

RecordActionSelectableItem

Represents the set of actions available for users to add to the component at runtime.

**Field Name** **Field Type** **Description**

`action` string Required. Specifies the API name of an action. For example, the API name of a
flow, such as `Verify_Information` .

```
type

```

RecordActionType Required. The type of action that’s associated with the record. Valid values are:
(enumeration of type

**•** `Flow`

string)

**•** `Flow`

**•** `QuickAction` (Available in API version 46.0 and later.)

`isFrequentAction` boolean

**•** `OmniScript` (Available in API version 56.0 and later.)

**•** `LWC` (Available in API version 62.0 and later.)

**•** `SvcCatalogItemDef` (Available in API version 62.0 and later.)

**•** `WebLink` (Available in API version 62.0 and later.)

Indicates whether an action is frequently accessed by users ( `true` ) or not
( `false` ). Available in version 57.0 and later.

This field applies only to Action Launcher.


Metadata Types RecordActionDeployment

**Field Name** **Field Type** **Description**

frequentActionSequenceNbr integer

The sequence number that's assigned to a frequently used action that's shown
on Action Launcher. Available in version 57.0 and later.

This field applies only to Action Launcher.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

Declarative Metadata Sample Definition

The following is a sample of a `recordActionDeployment` file.

```
<RecordActionDeployment xmlns="http://soap.sforce.com/2006/04/metadata">

   <channelConfigurations>

     <channel>Phone</channel>

     <channelItems>

        <action>Sample_Flow</action>

        <isMandatory>false</isMandatory>

        <isUiRemoveHidden>false</isUiRemoveHidden>

        <position>1</position>

        <pinned>Top</pinned>

        <type>Flow</type>

     </channelItems>

     <channelItems>

        <action>Another_Sample_Flow</action>

        <isMandatory>false</isMandatory>

        <isUiRemoveHidden>true</isUiRemoveHidden>

        <position>2</position>

        <pinned>Top</pinned>

        <type>Flow</type>

     </channelItems>

     <isAutopopEnabled>true</isAutopopEnabled>

   </channelConfigurations>

   <masterLabel>Sample Deployment</masterLabel>

   <selectableItems>

     <action>Sample_Flow</action>

     <type>Flow</type>

     <isFrequentAction>true</isFrequentAction>

     <frequentActionSequenceNbr>1</frequentActionSequenceNbr>

   </selectableItems>

   <selectableItems>

     <action>Sample_Flow_2</action>

     <type>Flow</type>

     <isFrequentAction>false</isFrequentAction>

   </selectableItems>

   <hasGuidedActions>true</hasGuidedActions>

   <hasRecommendations>true</hasRecommendations>

   <recommendation>

```


### Metadata Types RecordAggregationDefinition

```
        <defaultStrategy>Sample_Global_Strategy</defaultStrategy>

        <maxDisplayRecommendations>4</maxDisplayRecommendations>

        <hasImage>true</hasImage>

        <hasDescription>true</hasDescription>

        <hasRejectAction>true</hasRejectAction>

        <hasTitle>true</hasTitle>

      </recommendation>

      <deploymentContexts>

        <entityName>Case</entityName>

        <recommendationStrategy>Sample_Case_Strategy</recommendationStrategy>

      </deploymentContexts>

      <deploymentContexts>

        <entityName>Account</entityName>

        <recommendationStrategy>Sample_Acc_Strategy</recommendationStrategy>

      </deploymentContexts>

   </RecordActionDeployment>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <fullName>SecondTest</fullName>

      <types>

        <members>Sample_Flow</members>

        <members>Another_Sample_Flow</members>

        <members>Sample_Flow_2</members>

        <name>Flow</name>

      </types>

      <types>

        <members>SampleDeployment</members>

        <name>RecordActionDeployment</name>

      </types>

      <version>45.0</version>

   </Package>

```

SEE ALSO:

RecommendationStrategy

### RecordAggregationDefinition

Represents a data aggregation from one object to another object to which it is connected by other objects in the data model.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types RecordAggregationDefinition

File Suffix and Directory Location

RecordAggregationDefinition components have the suffix `.RecordAggregationDefinition` and are stored in the
`RecordAggregationDefinitions` folder.

Version

RecordAggregationDefinition components are available in API version 59.0 and later.

Special Access Rules

To access the RecordAggregationDefinition metadata type, you must have the Record Aggregation permission set license and the Record
Aggregation Access permission.

Fields

**Field Name** **Description**

```
aggregateFromObject

aggregateToObject

aggregationType

batchProcessingDefinition

```

**Field Type**
string

**Description**

Required.

API name of the object from which data is aggregated.

**Field Type**
string

**Description**

Required.

API name of the object to which data is aggregated.

**Field Type**
RecordAggregationDefinitionAggregationType (enumeration of type string)

**Description**

Required.

Type of the data aggregation.

Valid value is:

**•** `Record`

**Field Type**
string

**Description**
Data Processing Engine definition that aggregates data from one record to another.


Metadata Types RecordAggregationDefinition

**Field Name** **Description**

```
description

displayName

onDemandProcDefinition

recordAggregationObject

status

```

**Field Type**
string

**Description**
Description for this record aggregation definition.

**Field Type**
string

**Description**

Required.

Name of the record aggregation definition that's displayed in the record page.

**Field Type**
string

**Description**
Data Processing Engine definition that aggregates data from one record to another
on demand. Available in API version 63.0 and later.

**Field Type**

RecordAggregationObject[]

**Description**
List of record aggregation objects in the record aggregation join sequence.

**Field Type**
RecordAggregationDefinitionStatus (enumeration of type string)

**Description**

Required.

Status of this record aggregation definition.

Values are:

**•** `Active`

**•** `Draft`

**•** `Inactive`

RecordAggregationObject

Represents an object in the record aggregation join sequence.

**Field Name** **Description**

```
associatedObject

```

**Field Type**
string


Metadata Types RecordAggregationDefinition

**Field Name** **Description**

**Description**
Required.

API name of the object associated with this record aggregation object.

```
developerName

filterLogic

masterLabel

recordAggregationJoinCondition

recordAggregationObjectFilter

```

**Field Type**
string

**Description**
Developer name of the record aggregation object. May contain only underscores and
alphanumeric characters and must be unique in your org. It must begin with a letter,
not include spaces, not end with an underscore, and not contain two consecutive
underscores.

**Field Type**
string

**Description**
Logical sequence in which the record aggregation object filters associated with this
record aggregation object are applied to the associated object's records. If you define
two or more record aggregation object filters, but don’t specify the sequence in which
to apply the filters, the filters are applied by using a logical AND expression.

Available in API version 60.0 and later.

**Field Type**
string

**Description**

Required.

A user-friendly name for RecordAggregationDefinition, which is defined when the
RecordAggregationDefinition is created.

**Field Type**

RecordAggregationJoinCondition[]

**Description**
List of join conditions that apply to this record aggregation object.

**Field Type**

RecordAggregationObjectFilter[]

**Description**
List of filters that are applied to the records of this record aggregation object.

Available in API version 60.0 and later.


Metadata Types RecordAggregationDefinition

RecordAggregationJoinCondition

Represents a condition in a join between two record aggregation objects.

**Field Name** **Description**

```
joinField

navigationSequenceNumber

relatedJoinField

relatedRecordAggregationObject

type

```

**Field Type**
string

**Description**
Required.

API name of the field on the record aggregation object's associated object that is used
in the join condition.

**Field Type**
int

**Description**
Required.

Sequence number corresponding to this join in the join sequence from the object to
which the data is aggregated to the object that contains the data being aggregated.

**Field Type**
string

**Description**
Required.

API name of the field on the related record aggregation object's associated object that
is used in the join condition.

**Field Type**
string

**Description**
Required.

Second record aggregation object in the join condition.

**Field Type**
RecordAggregationJoinConditionType (enumeration of type string)

**Description**
Required.

Type of this record aggregation join in the join path from the object to which the data
is aggregated to the object that contains the data being aggregated.

Valid values are:

**•** `AggregateFrom`

**•** `AggregateTo`

**•** `Intermediate`


Metadata Types RecordAggregationDefinition

RecordAggregationObjectFilter

Represents a filter that is applied to the records of an object in the record aggregation join sequence. Available in API version 60.0 and
later.

**Field Name** **Description**

```
associatedObjectField

operator

sequenceNumber

value

```

**Field Type**
string

**Description**

Required.

API name of the associated object's field whose value is used to filter the object's
records. The associated object is specified in the record aggregation object.

**Field Type**
RecordAggregationObjectFilterOperator (enumeration of type string)

**Description**

Required.

Operator used in the filter expression.

Values are:

**•** `Contains`

**•** `Equals`

**•** `GreaterThan`

**•** `GreaterThanOrEquals`

**•** `In`

**•** `LessThan`

**•** `LessThanOrEquals`

**•** `NotEquals`

**•** `NotIn`

**Field Type**
int

**Description**

Required.

Sequence number of this record aggregation object filter.

**Field Type**
string

**Description**

Required.

Reference value with which the designated field's values are compared when the filter
is applied on the associated object's records.


Metadata Types RecordAggregationDefinition

Declarative Metadata Sample Definition

The following is an example of a RecordAggregationDefinition component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <RecordAggregationDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

      <aggregateToObject>PartyRelationshipGroup</aggregateToObject>

      <aggregateFromObject>PartyIncome</aggregateFromObject>

      <status>Active</status>

      <aggregationType>Record</aggregationType>

      <description>Aggregate head of household's income to household</description>

      <displayName>Party Income to Party Relationship Group</displayName>

      <recordAggregationObject>

        <associatedObject>PartyRelationshipGroup</associatedObject>

        <masterLabel>Party Relationship Group Object</masterLabel>

        <developerName>PartyRelationshipGroupObject</developerName>

        <recordAggregationJoinCondition>

           <joinField>Account</joinField>

           <navigationSequenceNumber>1</navigationSequenceNumber>

           <relatedJoinField>Account</relatedJoinField>

   <relatedRecordAggregationObject>AccountContactrelationObject</relatedRecordAggregationObject>

           <type>Intermediate</type>

        </recordAggregationJoinCondition>

        <recordAggregationObjectFilter>

         <associatedObjectField>Type</associatedObjectField>

         <operator>Equals</operator>

         <value>Household</value>

         <sequenceNumber>1</sequenceNumber>

        </recordAggregationObjectFilter>

      </recordAggregationObject>

      <recordAggregationObject>

        <associatedObject>AccountContactRelation</associatedObject>

        <masterLabel>Account Contact Relation Object</masterLabel>

        <developerName>AccountContactRelationObject</developerName>

        <recordAggregationJoinCondition>

           <joinField>Contact</joinField>

           <navigationSequenceNumber>2</navigationSequenceNumber>

           <relatedJoinField>Party</relatedJoinField>

   <relatedRecordAggregationObject>PartyIncomeObject</relatedRecordAggregationObject>

           <type>Intermediate</type>

        </recordAggregationJoinCondition>

        <recordAggregationObjectFilter>

         <associatedObjectField>IsPrimaryMember</associatedObjectField>

         <operator>Equals</operator>

         <value>true</value>

         <sequenceNumber>1</sequenceNumber>

        </recordAggregationObjectFilter>

      </recordAggregationObject>

      <recordAggregationObject>

        <associatedObject>PartyIncome</associatedObject>

        <masterLabel>Party Income Object</masterLabel>

        <developerName>PartyIncomeObject</developerName>

```


### Metadata Types RecordAlertCategory

```
        <filterLogic>1 AND 2</filterLogic>

        <recordAggregationObjectFilter>

         <associatedObjectField>IncomeFrequency</associatedObjectField>

         <operator>Equals</operator>

         <value>Monthly</value>

         <sequenceNumber>1</sequenceNumber>

        </recordAggregationObjectFilter>

        <recordAggregationObjectFilter>

         <associatedObjectField>IncomeStatus</associatedObjectField>

         <operator>Equals</operator>

         <value>Active</value>

         <sequenceNumber>2</sequenceNumber>

        </recordAggregationObjectFilter>

      </recordAggregationObject>

   </RecordAggregationDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>RecordAggregationDefinition</name>

      </types>

      <version>60.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based.htm)

### RecordAlertCategory

Represents a category to group and present record alerts.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### RecordAlertCategory components have the suffix recordAlertCategory and are stored in the recordAlertCategories

folder.


Metadata Types RecordAlertCategory

Version

RecordAlertCategory components are available in API version 54.0 and later.

Fields

**Field Name** **Description**

```
description

masterLabel

severity

```

**Field Type**
string

**Description**
The description of the record alert category.

**Field Type**
string

**Description**

Required.

The user-interface name of the record alert category.

**Field Type**
string

**Description**
Indicates the degree of impact that an alert in this category can have.

Possible Education Cloud values are:

**•** `High`

**•** `Low`

**•** `Medium`

Possible Financial Service Cloud values are:

**•** `Error`

**•** `Info`

**•** `Minor`

**•** `Warning`

Declarative Metadata Sample Definition

The following is an example of a RecordAlertCategory component.

```
<?xml version="1.0" encoding="UTF-8"?>

<RecordAlertCategory xmlns="http://soap.sforce.com/2006/04/metadata">

   <description>Tracks Financial Account Fraud Alerts</description>

   <masterLabel>Fraud</masterLabel>

```


### Metadata Types RegisteredExternalService

```
      <severity>Error</severity>

   </RecordAlertCategory>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Fraud</members>

        <name>RecordAlertCategory</name>

      </types>

      <version>54.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### RegisteredExternalService

Represents a registered external service, which provides an extension or integration.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### RegisteredExternalService components have the suffix .registeredExternalService and are stored in the

`registeredExternalServices` folder.

Version

### RegisteredExternalService components are available in API version 49.0 and later.

Special Access Rules

This metadata type is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field Name** **Description**

```
configUrl

```

**Field Type**
string


Metadata Types RegisteredExternalService

**Field Name** **Description**

**Description**
Link to the configuration page for the integration.

```
description

documentationUrl

extensionPointName

```

**Field Type**
string

**Description**
Description of the external service provider.

This field is available in API version 59.0 and later.

**Field Type**
string

**Description**
Link to documentation for the registered external service.

**Field Type**
ExtensionPointName (enumeration of type string)

**Description**
This field is available in API version 55.0 and later. Name of an extension point.

Possible values are:

**•** `Commerce_Domain_BuyerGroup_EvaluationService` —Available
in API version 65.0 and later.

**•** `Commerce_Domain_Cart_Calculate`

**•** `Commerce_Domain_Checkout_CreateOrder`

**•** `Commerce_Domain_Inventory_CartCalculator`

**•** `Commerce_Domain_Inventory_Service`

**•** `Commerce_Domain_OrderManagement_Product`

**•** `Commerce_Domain_Pricing_CartCalculator`

**•** `Commerce_Domain_Pricing_Service`

**•** `Commerce_Domain_Promotions_CartCalculator`

**•** `Commerce_Domain_Promotions_ShippingCalculator`

**•** `Commerce_Domain_Shipping_CartCalculator`

**•** `Commerce_Domain_Shipping_SplitShipment`

**•** `Commerce_Domain_Tax_CartCalculator`

**•** `Commerce_Domain_Tax_Service`

**•** `Commerce_Endpoint_Account_Address`

**•** `Commerce_Endpoint_Account_Addresses`

**•** `Commerce_Endpoint_Cart_Item` —Available in API version 62.0 and
later.

**•** `Commerce_Endpoint_Cart_ItemCollection` —Available in API
version 62.0 and later.


Metadata Types RegisteredExternalService

**Field Name** **Description**

**•** `Commerce_Endpoint_Catalog_Product`

**•** `Commerce_Endpoint_Catalog_Products`

**•** `Commerce_Endpoint_Search_ProductSearch`

**•** `Commerce_Endpoint_Gift_Wraps` —Available in API version 65.0 and
later.

**•** `Commerce_Endpoint_Search_Products`

**•** `Commerce_Endpoint_Search_ProductsByCategory`

```
externalServiceProvider

externalServiceProviderType

iconUri

```

**Field Type**
string

**Description**
Required. The ID of an Apex class functioning as a provider. The Apex class can either
implement one of the following interfaces:

**•** sfdc_checkout.CartInventoryValidation

**•** sfdc_checkout.CartPriceCalculations

**•** sfdc_checkout.CartShippingCharges

**•** sfdc_checkout.CartTaxCalculations

[or the Apex class can extend one of the base classes for an extension. See Available](https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/available-extensions.html)
[Extensions.](https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/available-extensions.html)

**Field Type**
RegistryProviderType (enumeration of type string)

**Description**
Required. The type of external service provider. For an extension, you set the type to
`Extension`, and you specify an `extensionPointName` . For example, for a
Pricing Cart Calculator extension, you specify
`Commerce_Domain_Pricing_CartCalculator` as the
`extensionPointName` . For an integration, you set the type to one of the other
possible values, such as `Price`, and you omit `extensionPointName` .

Possible values are:

**•** `Extension` (this value is available in API version 55.0 and later)

**•** `Inventory`

**•** `Price`

**•** `Promotions` (this value is available in API version 53.0 and later)

**•** `Shipment`

**•** `Tax`

**Field Type**
string

**Description**
URI of icon for the extension provider.


Metadata Types RegisteredExternalService

**Field Name** **Description**

This field is available in API version 59.0 and later.

```
isApplication

isProtected

masterLabel

```

**Field Type**
boolean

**Description**
Indicates if the extension provider is contained within a managed package.

The default value is `false` .

This field is available in API version 59.0 and later.

**Field Type**
boolean

**Description**
An auto-generated value that doesn’t impact the behavior of the metadata type.

The default value is `false` .

**Field Type**
string

**Description**

Required. The primary label for the RegisteredExternalService.

Declarative Metadata Sample Definition

The following is an example of a RegisteredExternalService component.

```
<?xml version="1.0" encoding="UTF-8"?>

<RegisteredExternalService xmlns="http://soap.sforce.com/2006/04/metadata">

   <externalServiceProvider>TaxSample</externalServiceProvider>

   <externalServiceProviderType>Tax</externalServiceProviderType>

   <documentationUrl>http://sample.com/doc</documentationUrl>

   <configUrl>http://sample.com/config</configUrl>

   <masterLabel>TaxService</masterLabel>

   <isProtected>false</isProtected>

</RegisteredExternalService>

```

The following is an example `package.xml` that references the previous definition.

```
<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>TaxSample</members>

     <name>ApexClass</name>

   </types>

   <types>

     <members>TaxService</members>

     <name>RegisteredExternalService</name>

   </types>

```


### Metadata Types ReferencedDashboard

```
      <version>60.0</version>

   </Package>

### ReferencedDashboard

```

Represents the ReferencedDashboard object in CRM Analytics. A referenced dashboard stores information about an externally referenced
dashboard.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

### ReferencedDashboard components have the suffix .refdash and are stored in the wave folder.

Version

### ReferencedDashboard components are available in API version 57.0 and later.

Special Access Rules

To view referenced dashboards, you need the Enables Tableau Dashboards in CRM Analytics permission.

Fields

**Field Name** **Field Type** **Description**

`application` string Required. The internal name of the Analytics app.

`description` string The dashboard description that appears in the user interface.

`embedUrl` string Required. The URL to the referenced dashboard.

`masterLabel` string Required. The dashboard name that appears in the user interface.

`templateAssetSourceName` string Links the dashboard to the template used to create it. Null for assets not
created from a template.

`visibility` string The visibility of the dashboard. Valid values are: `ALL` and `LIMITED` .


### Metadata Types RelatedRecordAssocCriteria

Declarative Metadata Sample Definition

The following is an example of a WaveDashboard component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ReferencedDashboard xmlns="http://soap.sforce.com/2006/04/metadata"

   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

      <application>my_app</application>

      <masterLabel>ReferencedDashboard1</masterLabel>

      <description>My Tableau Dashboard</description>

      <embedUrl>https://public.tableau.com/views/Superstore_24/Overview</embedUrl>

      <visibility>ALL</visibility>

   </ReferencedDashboard>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### RelatedRecordAssocCriteria

Represents criteria for automatically linking records like accounts, leads, opportunities, and cases with the branches that work with them.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### RelatedRecordAssocCriteria components have the suffix .relatedRecordAssocCriteria and are stored in the

`relatedRecordAssocCriteria` folder.

Version

### RelatedRecordAssocCriteria components are available in API version 52.0 and later.

Special Access Rules

To use this object, you must have the Financial Services Cloud Extension permission set.


Metadata Types RelatedRecordAssocCriteria

Fields

**Field Name** **Description**

```
associationHandlerApexClass

associationType

description

eventType

isProtected

```

**Field Type**
string

**Description**
The name of a custom Apex class that handles the creation of association records for
specific association criteria. This class must:

**•** Apply to an object that the Record Association Builder doesn't directly support

**•** Implement the `fscwmgen.BranchManagement`
`AssociationHandler` interface

**•** Return a list of Branch Unit Related Records

**•** Populate at least the minimum required fields in each Branch Unit Related Record:

**–** `BranchUnitId` : Represents the current branch unit of the user or contact

**–** `BusinessUnitMemberId` : The Banker ID of the user or contact

**–** `RelatedRecordId` : The ID of the custom object to be related

This field is a relationship field.

**Field Type**
AssociationType (enumeration of type string)

**Description**

Required.

The association type. Values are:

**•** `BranchManagement`

**Field Type**
string

**Description**
A description of the association criteria.

**Field Type**
AssociationEventType (enumeration of type string)

**Description**

Required.

The type of reference object event that triggers creation of the association. Values are:

**•** `Create`

**•** `Update`

**Field Type**
boolean


Metadata Types RelatedRecordAssocCriteria

**Field Name** **Description**

**Description**
An auto-generated value that doesn’t impact the behavior of the metadata type. The
default value is `false` .

```
masterLabel

preCondition

referenceObject

selectedOwnerField

status

```

**Field Type**
string

**Description**

Required.

The master label of the association criteria. This internal label doesn’t get translated.

**Field Type**
string

**Description**

Required.

A formula that, when true, causes a new association to be created.

**Field Type**
string

**Description**

Required.

The reference object for the association criteria.

**Field Type**
string

**Description**
A field to use instead of the default Owner ID.

**Field Type**
AssociationStatusType (enumeration of type string)

**Description**

Required.

The status of the association criteria. Values are:

**•** `Active`

**•** `Draft`

**•** `Inactive`


### Metadata Types RelationshipGraphDefinition

Declarative Metadata Sample Definition

The following is an example of a RelatedRecordAssocCriteria component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <RelatedRecordAssocCriteria xmlns="http://soap.sforce.com/2006/04/metadata">

     <associationType>BranchManagement</associationType>

     <eventType>Create</eventType>

     <masterLabel>RevenueThreeMillion</masterLabel>

     <preCondition>[Account].AnnualRevenue > 3000000</preCondition>

     <referenceObject>Account</referenceObject>

     <status>Active</status>

   </RelatedRecordAssocCriteria>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>RelatedRecordAssocCriteria</name>

      </types>

      <version>52.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### RelationshipGraphDefinition

Represents a definition of a graph that you can configure in your organization to traverse object hierarchies and record details, giving
you a glimpse of how your business works.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### RelationshipGraphDefinition components have the suffix .relationshipGraphDefinition and are stored in the

`relationshipGraphDefinitions` folder.

Version

### RelationshipGraphDefinition components are available in API version 55.0 and later.


Metadata Types RelationshipGraphDefinition

Special Access Rules

The Financial Services Cloud permission set license is required to access this object.

Fields

**Field Name** **Description**

```
isActive

isTemplate

masterLabel

relationshipGraphDefVersions

```

**Field Type**
boolean

**Description**

Required.

Indicates whether the relationship graph is available for use ( `true` ) or not
( `false` ). The default value is `true` .

Note: This field is read-only in API version 55.0.

**Field Type**
boolean

**Description**

Required.

Indicates whether you can configure this relationship graph as a template ( `true`
or not `false` ). The default value is `false` . In the UI, this field is _Set as Template_ .

**Field Type**
string

**Description**

Required.

A user-friendly name for RelationshipGraphDefinition, which is defined when the
RelationshipGraphDefinition is created. In the UI, this field is _Label_ .

**Field Type**

RelationshipGraphDefVersion[]

**Description**
Represents a list of graph versions associated with the relationship graph definition.

RelationshipGraphDefVersion

The list of graph versions associated with the relationship graph definition.


Metadata Types RelationshipGraphDefinition

**Field Name** **Description**

```
graphDefinition

graphType

```

**Field Type**
string

**Description**

Required.

Specifies a set of properties required to create a relationship graph, such as parent node,
child relationships, filter and sort fields, and graph UI elements.

**Field Type**
string

**Description**

Required.

Specifies the type of graph. In API version 55.0, only `HorizontalHierarchy` graph
type is supported.

Declarative Metadata Sample Definition

The following is an example of a RelationshipGraphDefinition component.

```
<?xml version="1.0" encoding="UTF-8"?>

<RelationshipGraphDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

   <isActive>false</isActive>

   <isTemplate>true</isTemplate>

   <masterLabel>Account Graph</masterLabel>

   <relationshipGraphDefVersions>

      <graphDefinition>{

  "graph" : {

   "rootNode" : {

     "object" : {

      "entity" : "Account"

     },

     "configurationType" : "Primary",

     "sortFields" : [ {

      "field" : {

       "field" : "LastModifiedDate",

       "whichEntity" : "TARGET"

      },

      "order" : "DESC"

     } ],

     "nodeUiConfig" : {

      "fieldsToDisplay" : [ ],

      "showFieldLabels" : true,

      "actions" : { }

     },

     "childRelationships" : [ {

      "OneToMany" : {

       "targetObjectNode" : {

```


Metadata Types RelationshipGraphDefinition

```
           "object" : {

            "entity" : "Contact"

           },

           "configurationType" :"Custom",

           "sortFields" : [ {

            "field" : {

              "field" : "LastModifiedDate",

              "whichEntity" : "TARGET"

            },

            "order" : "DESC"

           } ],

           "nodeUiConfig" : {

            "fieldsToDisplay" : [ {

              "field" : "Name",

              "whichEntity" : "TARGET"

            }, {

              "field" : "Phone",

              "whichEntity" :"TARGET"

            } ],

            "showFieldLabels" : true,

            "actions" : {

              "containerActions" : [ {

               "action" : "New"

              } ],

              "recordActions" : [ {

               "action" : "Edit"

              }, {

               "action" : "Delete"

              } ]

            }

           },

           "childRelationships" : [ ]

          },

          "relationshipUiConfig" : { },

          "filter" : {

           "filterCriteria" : [ {

            "field" : {

              "field" : "Name",

              "whichEntity" : "TARGET"

            },

            "operator" : "eq",

            "value" : "Salesforce"

           } ],

           "booleanFilter" : "1"

          },

          "targetObjectField" : {

           "field" : "AccountId",

           "whichEntity" : "TARGET"

          }

         }

        } ]

      },

      "globalUiConfig" : {

        "borderColor" : "Green2",

```


### Metadata Types RemoteSiteSetting

```
        "borderThickness" : "2px";,

        "colorShading" : "Black",

        "fieldLayout" : "Vertically Stacked",

        "recordContainerExpansion" : true,

        "recordExpansion" : true

      }

     }

    }</graphDefinition>

         <graphType>HorizontalHierarchy</graphType>

      </relationshipGraphDefVersions>

   </RelationshipGraphDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <fullName>Package1</fullName>

     <types>

        <members>*</members>

        <name>RelationshipGraphDefinition</name>

     </types>

     <version>55.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### RemoteSiteSetting

Represents a remote site setting. Before any Visualforce page, Apex callout, or JavaScript code using XmlHttpRequest in an s-control or
custom button can call an external site, that site must be registered in the Remote Site Settings page, or the call fails.

### RemoteSiteSetting on page 1831 extends the Metadata metadata type and inherits its fullName field.

Declarative Metadata File Suffix and Directory Location

### RemoteSiteSetting on page 1831 components are stored in the remoteSiteSettings directory of the corresponding package

directory. The file name matches the unique name of the remote site setting, and the extension is `.remoteSite` .

Version

### RemoteSiteSetting on page 1831 components are available in API version 19.0 and later.


### Metadata Types Report

Fields

**Field** **Field Type** **Description**

`description` string The description explaining what this remote site setting is used
for.

`disableProtocolSecurity` boolean Required. Indicates whether code within Salesforce can access
the remote site regardless of whether the user's connection is

over HTTP or HTTPS ( `true` ) or not ( `false` ). When `true`, code
within Salesforce can pass data from an HTTPS session to an
HTTP session, and vice versa.

Only set to `true` if you understand the security implications.

`fullName` string The name can only contain characters, letters, and the
underscore (_) character. The name must start with a letter, and

can’t end with an underscore or contain two consecutive
underscore characters.

Inherited from the Metadata component, this field isn’t defined
in the WSDL for this component. It must be specified when
creating, updating, or deleting. See create() to see an example
of this field specified for a call.

`isActive` boolean Required. Indicates if the remote site setting is active ( `true` ) or
not ( `false` ).

`url` string Required. The URL for the remote site.

Declarative Metadata Sample Definition

A sample XML definition of a remote site setting is shown in this code block.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <RemoteSiteSetting xmlns="http://soap.sforce.com/2006/04/metadata">

      <description>Used for Apex callout to mapping web service</description>

      <disableProtocolSecurity>false</disableProtocolSecurity>

      <isActive>true</isActive>

      <url>https://www.maptestsite.net/mapping1</url>

   </RemoteSiteSetting>

### Report

```

Represents a custom report. This metadata type only supports custom reports; standard reports aren’t supported.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types Report

Declarative Metadata File Suffix and Directory Location

Reports are stored in the `reports` directory of the package directory. The file name consists of the report title with the extension
`.report` .

Retrieving Reports

You can’t use the wildcard (*) symbol with reports in `package.xml` .

To retrieve the list of explicit report names to populate `package.xml` with, first call `listMetadata(ListMetadataQuery[])`
with a `ListMetadataQuery` entry with the `type` field set to `ReportFolder` and the `folder` field to `*` (wildcard). This
call returns an array of FileProperties objects with the names of report folders in the `fullName` field.

Now call `listMetadata` with `ListMetadataQuery` entries where the `type` field is Report and the `folder` fields are the
full name values from the first `listMetadata` call. These calls return `FileProperties` objects where the `fullName` field is
the combination of the folder name and report name. Use these values in the `package.xml` to designate the members for the Report
metadata type.

ReportFolder isn’t returned as a type in `describeMetadata()` . Report is returned from `describeMetadata()` with an
associated attribute of `inFolder` set to true. If that attribute is set to true, you can construct the type by using the component name
with the word Folder, such as ReportFolder.

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

To retrieve or deploy `ReportFolder` s, use the `Report` metadata type in your `package.xml` . When you reference a nested
folder by itself (without its contents), the API can misinterpret the path as a report component.

For example, the API interprets `<members>TopLevel/SubLevel</members>` as a request for a report named `SubLevel` .

To correctly reference the nested folder, append a trailing slash (/) to its full name. This syntax explicitly identifies the member as a folder.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

```


Metadata Types Report

```
        <members>TopLevel/SubLevel/</members>

        <members>TopLevel/SubLevel/MyReport</members>

        <name>Report</name>

      </types>

      <version>58.0</version>

   </Package>

```

Omitting the trailing slash (/) for the folder causes the operation to fail with an error: "Entity of type 'Report' named 'TopLevel/SubLevel'
cannot be found".

Version

Report components are available in API version 14.0 and later.

Fields

[The following information assumes that you’re familiar with creating and running reports. For more information on these fields, see Build](https://help.salesforce.com/s/articleView?id=analytics.rd_reports_build.htm&type=5&language=en_US)
[a Report in Salesforce Help.](https://help.salesforce.com/s/articleView?id=analytics.rd_reports_build.htm&type=5&language=en_US)

**Field** **Field Type** **Description**

`aggregateFilters` ReportAggregateFilter[]

List that defines filters on custom summary
formulas for summary, matrix, and joined reports.

Available in API version 64.0 and later.

`aggregates` ReportAggregate[] List that defines custom summary formulas for
summary, matrix, and joined reports.

`block` Report[] Represents each block in a joined report where
every block can be of a different report type.

`blockInfo` ReportBlockInfo Defines attributes for each block in a joined
report.

`buckets` ReportBucketField[] Defines a bucket field to be used in the report.
This field is available in API version 24.0 and later.

`chart` ReportChart Defines a chart for summary and matrix reports.

`colorRanges` ReportColorRange[] List that specifies conditional highlighting for
report summary data. Salesforce Classic only.

`columns` ReportColumn[]

`crossFilters` ReportCrossFilter[]

List that specifies the fields displayed in the
report. Fields appear in the report in the same
order as they appear in the Metadata API file.

Defines a cross filter's object, related object, and
condition (WITH or WITHOUT). This field is
available in API version 66.0 and later.

`currency` `CurrencyIsoCode` (enumeration of type When using multiple currencies, some reports
string) allow you to display converted amounts by


Metadata Types Report

**Field** **Field Type** **Description**

selecting the appropriate column to display. For
example, in opportunity reports, you can include
the Amount (converted) column on the report.
This field is an enumeration of type string that
defines the currency in which to display
converted amounts. Valid values: Must be one
of the valid alphabetic, three-letter currency ISO
codes defined by the ISO 4217 standard, such
as `USD`, `GBPSLE`, or `JPY` .

`dataCategoryFilters` string Specifies a filter according to the data category.

`description` string

Specifies a general description, which is
displayed with the report name. Maximum
characters: 255 characters.

`division` string If your organization uses divisions to segment
data and the Affected by Divisions permission

is enabled, records in the report must match this
division.

This field is available in API version 17.0 and later.

`filter` ReportFilter Limits report results to records with specific data.
For example, you can limit report results to

opportunities for which the amount is greater
than $1,000:

```
                                   <filter>

                                   <criteriaItems>

                                    <column>AMOUNT</column>

                                   <operator>greaterThan</operator>

                                    <value>1000</value>

                                   </criteriaItems>

                                   </filter>

```

`folderName` string

`format` ReportFormat (enumeration of type string)

Name of the folder that houses the report.

This field is available in API version 35.0 and later.

Defines the report format. For example,
`Tabular` for a simple data list without
subtotals.

`formattingRules` ReportFormattingRule[] (enumeration of type List that specifies conditional highlighting for
string) report data. Lightning Experience only.

`groupingsAcross` ReportGrouping[] List that defines the fields by which you want to
group and subtotal data across a matrix report

(row headings). When grouping by a date field,


Metadata Types Report

**Field** **Field Type** **Description**

you can further group the data by a specific time
period such as days, weeks, or months.
Maximum: 2 fields.

`groupingsDown` ReportGrouping[] For Summary and Matrix reports: List that defines
the fields by which you want to group and

subtotal. For summary reports, choosing more
than one sort field allows you to subsort your
data. For matrix reports, specifies summary fields
for column headings. When grouping by a date
field, you can further group the data by a specific
time period such as days, weeks, or months.
Maximum for matrix reports: 2. Maximum for
summary reports: 3

`historicalSelector` ReportHistoricalSelector

`isSmartTotalDisabled` boolean

Defines a date range for which historical trend
reporting data is to be captured. Default is “Any
Historical Date.”

Available in API version 29.0 and later.

`false` displays smart totalling on the report.

Available in API version 29.0 and later.

`name` string Required. The report name. For example,

```
                                 Opportunity Pipeline

```

`numSubscriptions` int

Indicates whether a user has subscribed to this
report Lightning Experience (1) or not (0). Tied
to user context.

This field is available in API version 38.0 and later.

`params` ReportParam[] List that specifies settings specific to each report
type, in particular options that let you filter a

report to obtain useful subsets. For example, the
Activities report type lets you specify whether
you want to see open or closed activities or both
and whether you want to see tasks or events or
both. Valid values depend on the report type.

`reportCustomDetailFormula` CustomDetailFormulas Allows you to apply row-level formulas to
reports.

`reportType` string

`reportTypeApiName` string

Required. Defines the type of data in the report.
For example, `Opportunity` to create a report
of opportunities data.

Defines the API Name for the report type.

This field is available in API version 48.0 and later.


Metadata Types Report

**Field** **Field Type** **Description**

`roleHierarchyFilter` string The role name for a report drill down. Some
reports, such as opportunity and activity reports,

display Hierarchy links that allow you to drill
down to different datasets based on the role
hierarchy.

This field is available in API version 17.0 and later.

`rowLimit` int Defines the maximum number of rows that can
be returned for the report.

`scope` string Defines the scope of data on which you run the
report. For example, whether you want to run

the report against all opportunities,
opportunities you own, or opportunities your
team owns. Valid values depend on the
`reportType` . For example, for Accounts
reports:

**•** `MyAccounts`

**•** `MyTeamsAccounts`

**•** `AllAccounts`

`showCurrentDate` boolean

`showDetails` boolean

Can be set to `true` for historical trending
reports in matrix format.

Available in API version 29.0 and later.

`false` shows a collapsed view of the report
with only the headings, subtotals, and total.
Default: `true`

`showGrandTotal` boolean `true` displays the calculated total for the full
report.

`showSubTotals` boolean `true` displays the calculated subtotals for
sections of the report.

`sortColumn` string

Specifies the field on which to sort data in the
report. Use `sortOrder` to specify the sort
order.

`sortOrder` SortOrder (enumeration of type string) Specifies the sort order. Use `sortColumn` to
specify the field on which to sort.

`territoryHierarchyFilter` string The territory name for a report drill down. If your
organization uses territory management, some

reports display Hierarchy links that allow you to
drill down to different datasets based on the
territory hierarchy.

This field is available in API version 17.0 and later.


Metadata Types Report

**Field** **Field Type** **Description**

`timeFrameFilter` ReportTimeFrameFilter Limits report results to records within a specified
time frame.

`userFilter` string The username for a report drill down. Some
reports, such as opportunity and activity reports,

display Hierarchy links that allow you to drill
down to different datasets based on the user
hierarchy.

This field is available in API version 17.0 and later.

ReportAggregateFilter

ReportAggregateFilter defines custom summary formula filters on summary, matrix, and joined reports.

**Field** **Field Type** **Description**

`aggregate` string Required. The name of the report aggregate to apply the filter
to.

`operator` string Required. The filter operator.

`value` string Required. The filter value.

ReportAggregate

ReportAggregate defines custom summary formulas on summary, matrix, and joined reports. For more information on these fields, see
[Add a Summary Formula Column to a Report in Salesforce Help.](https://help.salesforce.com/s/articleView?id=analytics.building_custom_summary_formulas.htm&type=5&language=en_US)

**Field** **Field Type** **Description**

`acrossGroupingContext` string

Defines the row grouping level at which you want your custom
summary formula to be displayed. This field is available in API
version 15.0.

`calculatedFormula` string Required. The custom summary formula. For example,

```
                           AMOUNT:SUM + OPP_QUANTITY:SUM

```

`datatype` ReportAggregateDatatype Required. Specifies the data type for formatting and display of
(enumeration of type string) the custom summary formula results.

`description` string The custom summary formula description. Maximum: 255
characters.

`developerName` string Required. The internal development name of the custom
summary formula, for example, `FORMULA1` . This name is used

to reference custom summary formulas from other report
components, including conditional highlighting.


Metadata Types Report

**Field** **Field Type** **Description**

`downGroupingContext` string

Defines the column grouping level at which you want your
custom summary formula to be displayed. This field is available
in API version 15.0 and later.

`isActive` boolean Required. `true` displays the formula result in the report.
`false` doesn’t display the result in the report.

`isCrossBlock` boolean Determines whether the custom summary formula is a
cross-block formula, which is available with joined reports.

`true` indicates a cross-block custom summary formula.
`false` indicates a standard custom summary formula.

This field is available in API version 25.0 and later.

`masterLabel` string Required. The custom summary formula label (name).

`reportType` string Required for joined reports. Specifies the `reportType` of the
blocks to which the `aggregate` can be added.

`scale` int The formula result is calculated to the specified number of
decimal places. Valid values `0` through `18` .

ReportBlockInfo

ReportBlockInfo defines blocks in a joined report.

**Field** **Field Type** **Description**

`aggregateReferences` ReportAggregateReference[] Lists the `aggregates` that represent the custom summary
formulas used in a joined report block.

`blockId` string Required. `blockId` is used in cross-block custom summary
formulas and joined report charts to identify the block containing

each summary field. `blockId` is assigned automatically. Valid
values are B1 through B5.

This field is available in API version 25.0 and later.

`joinTable` string

ReportAggregateReference

Required. Refers to the entity used to join blocks in a joined
report. The entity provides a list of fields that are available for
globally grouping across the blocks.

ReportAggregateReference defines the developer name used for custom summary formulas in joined reports.


Metadata Types Report

**Field** **Field Type** **Description**

`aggregate` string

ReportBucketField

ReportBucketField defines a bucket to be used in the report.

Required. The `developerName` of the ReportAggregate,
which specifies the custom summary formula used in a block
of a joined report.

**Field** **Field Type** **Description**

`bucketType` ReportBucketFieldType Required. Specifies the type of bucket. Valid values:
(enumeration of type string)

**•** text

**•** number

**•** picklist

`developerName` string Required. A unique name used as the `<field>` value to
display a bucket field in the column list and other report

components, including sort, filter, list, group, and chart. Must
be of the format `BucketField_` _**`name`**_ . For example,
`BucketField_BusinessSize` .

`masterLabel` string Required. The bucket field label. Maximum 40 characters. Any
line breaks, tabs, or multiple spaces at the beginning or end of

the label are removed. Any of these characters within the label
are reduced to a single space.

`nullTreatment` ReportBucketFieldNullTreatment For numeric bucket fields only. Specifies whether empty values
(enumeration of type string) are treated as zeros ( `z` ) or not ( `n` ).

`otherBucketLabel` string The label of the container for unbucketed values.

`sourceColumnName` string Required. The source field that the bucket is applied to. For
example, `SALES` or `INDUSTRY` .

`values` ReportBucketFieldValue
(enumeration of type string)

ReportBucketFieldValue

Defines one bucket value used in the bucket field.

While this name is plural, it represents a single bucket. In typical
use, a bucket field contains multiple buckets.

ReportBucketFieldValue defines a bucket value used in the bucket field.


Metadata Types Report

**Field** **Field Type** **Description**

`sourceValues` ReportBucketFieldSourceValue The value of a bucket in the bucket field. Valid values:
(enumeration of type string)

**•** `sourceValue` —Used for picklist and text bucket fields.
For picklists, describes the picklist item in the bucket. For
example, the sourceValue of a bucket on `TYPE` could be
`Customer` . For text, the full string for the item in the
bucket. For example, the sourceValue of a bucket on
`ADDRESS_STATE1` could be `NY` .

**•** `from` —Used only on numeric bucket fields. A non-inclusive
lower bound for a numeric bucket range. This value must
be a number.

**•** `to` —Used only on numeric bucket fields. The inclusive
upper bound for a numeric bucket range. This value must
be a number.

In numeric buckets, the first value must only have `to` and last
value must only have `from` . All other values must have both
`to` and `from` .

`value` string Required. The name of a specific bucket value within the bucket
field.

ReportGrouping

ReportGrouping defines how to group, subtotal, and sort data for summary, matrix, and joined reports.

**Field** **Field Type** **Description**

`aggregateType` ReportAggrType (enumeration The type of aggregate value to sort by. Valid values are:
of type string)

**•** `Sum`

**•** `Average`

**•** `Maximum`

**•** `Minimum`

**•** `RowCount`

**•** `Unique`

**•** `Median`

**•** `Noop`

`dateGranularity` UserDateGranularity When grouping by a date field, the time period by which to
(enumeration of type string) group.

`field` string Required. The field by which you want to summarize data. For
example, `CAMPAIGN_SOURCE`

`sortByName` string The API name of the column, aggregate, or custom summary
field used to order the grouping.


Metadata Types Report

**Field** **Field Type** **Description**

`sortOrder` SortOrder Required. Whether to sort data in ascending or descending
alphabetical and numerical order.

`sortType` ReportSortType (enumeration Indicates if the grouping is sorted by a column, aggregate, or
of type string) custom summary field. Valid values are:

**•** `Column`

**•** `Aggregate`

**•** `CustomSummaryFormula`

ReportHistoricalSelector

ReportHistoricalSelector defines a date range for historical data.

**Field** **Field Type** **Description**

`snapshot` string Represents the date value to apply a historical filter, either
relative (in the format `N_DAYS_AGO:2` ) or absolute (in the

format `yyyy-MM-dd` ). If unspecified, it’s assumed that the
filter is applied to all the columns the user sees.

Available in API version 29.0 and later.

CustomDetailFormulas

CustomDetailFormulas defines row-level formulas for reports.

**Field** **Field Type** **Description**

`calculatedFormula` string Required. The custom formula. For example, `AMOUNT:SUM`

```
                              + OPP_QUANTITY:SUM

```

`datatype` ReportCustomDetailFormulaDatatype Required. Specifies the data type for formatting and display of
(enumeration of type string) the formula results.

`description` string The formula description. Maximum: 255 characters.

`developerName` string Required. The internal development name of the formula, for
example, `FORMULA1` . This name is used to reference custom

formulas from other report components, including conditional
highlighting.

`label` string Required. The name that identifies this formula.

`scale` int The formula result is calculated to the specified number of
decimal places. Valid values `0` through `18` .


Metadata Types Report

ReportCustomDetailFormulaDatatype

An enumeration of type string that specifies the data type for formatting and display of row-level formula results. Valid values:

**Enumeration Value**

```
   Double

   DateOnly

   DateTime

   Text

```

SortOrder

An enumeration of type string that defines the order in which data is sorted in the report fields. Valid values:

**Field** **Description**

`Asc` Sorts data in ascending alphabetical and numerical order.

`Desc` Sorts data in descending alphabetical and numerical order.

UserDateGranularity

An enumeration of type string that defines the time period by which to group data. Valid values:

**Enumeration Value** **Description**

`None` No grouping by date

`Day` By day

`Week` By week

`Month` By month

`Quarter` By quarter

`Year` By year

`FiscalQuarter` [By fiscal quarter. You can set the fiscal year for your organization. See Set the Fiscal Year in](https://help.salesforce.com/s/articleView?id=xcloud.setting_the_fiscal_year.htm&type=5&language=en_US)
Salesforce Help.

`FiscalYear` By fiscal year

`MonthInYear` By calendar month in year

`DayInMonth` By calendar day in month

`FiscalPeriod` When custom fiscal years are enabled: By fiscal period

`FiscalWeek` When custom fiscal years are enabled: By fiscal week


Metadata Types Report

ReportSummaryType

An enumeration of type string that defines how report fields are summarized. Valid values:

**Enumeration Value** **Description**

`Sum` Total

`Average` Average

`Maximum` Largest value

`Minimum` Smallest value

`Unique` Unique values

`Median` Median value

`Noop` The summary is a no-op.

`None` The field isn’t summarized.

ReportColorRange

ReportColorRange defines conditional highlighting for report summary data.

**Field** **Field Type** **Description**

`aggregate` ReportSummaryType Required. Defines how the field specified in `columnName` is
(enumeration of type string) summarized. For example, `Sum` .

`columnName` string Required. Specifies the field whose value ranges are represented
by background colors.

`highBreakpoint` double Required. Specifies the number that separates the mid color
from the high color.

`highColor` string

Required. Specifies the color (in HTML format) to represent data
that falls into the high number range. This color spans from the
`highBreakpoint` value.

`lowBreakpoint` double Required. Specifies the number that separates the low color
from the mid color.

`lowColor` string

Required. Specifies a color (in HTML format) to represent data
that falls into the low value range, below the
`lowBreakpoint` value.

`midColor` string Required. Specifies a color (in HTML format) to represent data
that falls into the mid value range.

ReportColumn

ReportColumn defines how fields (columns) are displayed in the report.


Metadata Types Report

**Field** **Field Type** **Description**

`aggregateTypes` ReportSummaryType[] List that defines if and how each report field is summarized.
(enumeration of type string)

`field` string Required. The field name. For example, `AGE` or

```
                              OPPORTUNITY_NAME

```

`isExtendedColumn` boolean

`reverseColors` boolean

`showChanges` boolean

ReportFilter

ReportFilter limits the report results by filtering data on specified fields.

Indicates whether the column is extended ( `true` ) or not
( `false` ).

Available in API version 65.0 and later.

In historical trend reports, displays greater Date values as green
and greater Amount values as red, reversing the default colors.

Available in API version 29.0 and later.

In historical trend reports, adds a column displaying the
difference between current and historical Date and Amount
values.

Available in API version 29.0 and later.

**Field** **Field Type** **Description**

`booleanFilter` string Specifies filter logic conditions.

`criteriaItems` ReportFilterItem

`language` Language (enumeration of type
string)


The criteria by which you want to filter report data, either by
comparing historical values or by applying a date range.

```
<criteriaItems>

  criteriaItems ReportFilterItem

<column>Opportunity.Opportunity__hd$Amount__hst</column>

  <columnToColumn>false</columnToColumn>

  <operator>equals</operator>

  <snapshot>N_DAYS_AGO:90</snapshot>

  <value>100</value>

</criteriaItems>

```

The language used when a report filters against a picklist value
using the operators `contains` or `startsWith` . For a list
of valid language values, see Language.

Metadata Types Report

ReportFilterItem

ReportFilterItem limits the report results by filtering data on specified fields.

**Field** **Field Type** **Description**

`column` string Required. The field in which to filter data. For example, `AMOUNT`

`columnToColumn` boolean

Indicates whether the filter is a column-to-column (field-to-field)
filter.

Available in API version 29.0 and later for historical trending
reports. Available in API version 48.0 and later for general reports.

`isUnlocked` boolean Optional. Indicates whether the report filter is unlocked ( `true` )
or locked ( `false` ). You can edit unlocked filters on the report

run page in Lightning Experience. If unspecified, the default
value is `false` .

Available in API version 38.0 and later.

`operator` FilterOperation (enumeration of
type string)

`snapshot` string

Required. An enumeration of type string that defines the
operator used to filter the data, for example, `greaterThan` .
Valid values are:

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

Represents the date value, either relative (in the format
`N_DAYS_AGO:2` ) or absolute (in the format `yyyy-MM-dd` ).

Available in API version 29.0 and later.

`value` string The value by which you want to filter the data, for example,
`1000` . The Metadata API filter condition values don’t always

match the values that you enter in the report wizard. For
example, in the Metadata API dates are always converted to the
US date format and values entered in a non-US English language
can be converted to a standard US English equivalent.


Metadata Types Report

ReportFormat

An enumeration of type string that defines the report format. Valid values:

**Enumeration Value** **Description**

`Matrix` Summarizes data in a grid. Use to compare related totals.

`Summary` Lists, sorts, and subtotals data.

`Tabular` Lists data with no sorting or subtotals.

`Joined` Joins data from different report types storing each report’s data in its own block.

ReportFormattingRule

Defines conditional highlighting for report summary data. You can specify up to 5 formatting rules per report.

**Field** **Field Type** **Description**

`aggregate` ReportFormattingSummaryType Defines how the field specified in `columnName` is
(enumeration of type string) summarized. For example, `Sum` .

`columnName` string Required. Specifies the field whose value ranges are represented
by colors.

`values` ReportFormattingRuleValue Required. Specifies the background colors and associated ranges
(enumeration of type string) for formatted data values.

ReportFormattingSummaryType

An enumeration of type string that defines how report fields are summarized. Valid values:

**Enumeration Value** **Description**

`Sum` Total

`Average` Average

`Maximum` Largest value

`Minimum` Smallest value

`Unique` Unique values

ReportFormattingRuleValue

Specifies the background colors and associated ranges for formatted data values. You can specify up to 3 background colors and 0–3
range upper bounds. Valid values:


Metadata Types Report

**Field** **Field Type** **Description**

`backgroundColor` string (Required) Specifies a highlighting color for the field in
`columnName` . Must be a valid hex color string such as

#54C254. At least one color is required. You can optionally specify
a different color for up to 3 ranges as determined by
`rangeUpperBound` . If you don’t specify a color for a
particular range, the background is transparent.

`rangeUpperBound` double Delineates a range to which a background color applies. If you
don’t specify an upper bound for a particular range, the bound

is assumed to be plus infinity. The following example sets the
background color for the Sales column to #B50E03 for aggregate
sales less than or equal to 100, sets no background for sales from
100 to 1000, and sets the background color to #006714 for sales
greater than 1000.

```
                                <formattingRules>

                                <aggregate>Sum</aggregate>

                                <columnName>Sales</columnName>

                                     <values>

                                <backgroundColor>#B50E03</backgroundColor>

                                <rangeUpperBound>100.0</rangeUpperBound>

                                     </values>

                                     <values>

                                <rangeUpperBound>1000.0</rangeUpperBound>

                                     </values>

                                     <values>

                                <backgroundColor>#006714</backgroundColor>

                                     </values>

                                </formattingRules>

```

ReportParam

ReportParam represents settings specific to a report type, especially options that let you filter a report to certain useful subsets.

**Field** **Field Type** **Description**

`name` string Required. Specifies a specific `reportType` setting.

`value` string Required. The setting value.


Metadata Types Report

ReportAggregateDatatype

An enumeration of type string that specifies the data type for formatting and display of custom summary formula results. Valid values:

**Enumeration Value**

```
   currency

   number

   percent

```

ReportChart

ReportChart represents charts on summary, matrix, and joined reports.

**Field** **Field Type** **Description**

`backgroundColor1` string Specifies the beginning color (in HTML format) for a gradient
color background.

`backgroundColor2` string Specifies the end color (in HTML format) for a gradient color
background.

`backgroundFadeDir` ChartBackgroundDirection Specifies the direction for a gradient color background. Use with
(enumeration of type string) `backgroundColor1` to specify the beginning color and

`backgroundColor2` to specify the end color for the
gradient design. Use white for both if you don’t want a
background design. Valid values:

**•** `Diagonal`

**•** `LeftToRight`

**•** `TopToBottom`

`chartSummaries` ChartSummary[] Specifies the summaries you want to use for the chart. Invalid
summaries are ignored without notification. If there are no valid

summaries, RowCount is used by default for the axis value. This
field is available in API version 17.0 and later.

`chartType` ChartType (enumeration of type Required. Specifies the chart type. Available chart types depend
string) on the `report type` .

`enableHoverLabels` boolean Specifies whether to display values, labels, and percentages
when hovering over charts. Hover details depend on chart type.

Percentages apply to pie, donut, and funnel charts only. This
field is available in API version 17.0 and later.

`expandOthers` boolean Specifies whether to combine all groups less than or equal to
3% of the total into a single 'Others' wedge or segment. Only

applies to pie, donut, and funnel charts. Set to `true` to show
all values individually on the chart; set to `false` to combine


Metadata Types Report

**Field** **Field Type** **Description**

small groups into 'Others.' This field is available in API version
17.0 and later.

`groupingColumn` string

`legendPosition` ChartLegendPosition
(enumeration of type string)

Specifies the field by which to group data. This data is displayed
on the X-axis for vertical column charts and on the Y-axis for
horizontal bar charts.

Required.

The location of the legend with respect to the chart. The valid
values are:

**•** `Bottom`

**•** `OnChart`

**•** `Right`

`location` ChartPosition (enumeration of Required. Specifies whether the chart is displayed at the top or
type string) bottom of the report.

`secondaryGroupingColumn` string For grouped chart types: Specifies the field by which to group
the data.

`showAxisLabels` boolean For bar and line charts: Specifies whether the chart displays
names for each axis.

`showPercentage` boolean

Indicates if percentages are displayed for wedges and segments
of pie, donut, and funnel charts, as well as for gauges ( `true` ),
or not ( `false` ).

`showTotal` boolean Indicates if the total is displayed for donut charts and gauges
( `true` ), or not ( `false` ).

`showValues` boolean Indicates if the values of individual records or groups are
displayed for charts ( `true` ), or not ( `false` ).

`size` ReportChartSize (enumeration Required. Specifies the chart size.
of type string)

`summaryAggregate` ReportSummaryType
(enumeration of type string)

Defines how to summarize the chart data. For example, `Sum` .
No longer supported in version API 17.0 and later. See
`chartSummaries` .

`summaryAxisManualRangeEnd` double When specifying the axis range manually: Defines the ending
value.

`summaryAxisManualRangeStart` double When specifying the axis range manually: Defines the starting
value.

`summaryAxisRange` ChartRangeType (enumeration Required. For bar, line, and column charts: Defines whether to
of type string) specify the axis range manually or automatically.

`summaryColumn` string Required. Specifies the field by which to summarize the chart
data. Typically this field is displayed on the Y-axis. No longer


Metadata Types Report

**Field** **Field Type** **Description**

supported in version API 17.0 and later. See
`chartSummaries` .

`textColor` string The color (in HTML format) of the chart text and labels.

`textSize` int The size of the chart text and labels. Valid values:

**•** `8`

**•** `9`

**•** `10`

**•** `12`

**•** `14`

**•** `18`

**•** `24`

**•** `36`

The maximum size is 18. Larger values are shown at 18 points.

`title` string The chart title. Max 255 characters.

`titleColor` string The color (in HTML format) of the title text.

`titleSize` int The size of the title text. Valid values:

**•** `8`

**•** `9`

**•** `10`

**•** `12`

**•** `14`

**•** `18`

**•** `24`

**•** `36`

The maximum size is 18. Larger values are shown at 18 points.

ChartType

[An enumeration of type string that defines the chart type. For information on each of these chart types, see Chart Types in Salesforce](https://help.salesforce.com/s/articleView?id=analytics.chart_types.htm&type=5&language=en_US)
Help. Valid values:

**Enumeration Value**

```
   None

   HorizontalBar

   HorizontalBarGrouped

   HorizontalBarStacked

```


Metadata Types Report

**Enumeration Value**

```
   HorizontalBarStackedTo100

   VerticalColumn

   VerticalColumnGrouped

   VerticalColumnStacked

   VerticalColumnStackedTo100

   Line

   LineGrouped

   LineCumulative

   LineCumulativeGrouped

   Pie

   Donut

   Funnel

   Scatter

   ScatterGrouped

   VerticalColumnLine

   VerticalColumnGroupedLine

   VerticalColumnStackedLine

   Plugin

```

Reserved for future use. This value is available in API version 31.0 and later.

ChartPosition

An enumeration of type string that specifies the position of the chart in the report. Valid values:

**Enumeration Value**

```
   CHART_TOP

   CHART_BOTTOM

```

ChartSummary

ChartSummary defines how data in the chart is summarized. Valid values:


Metadata Types Report

**Field** **Field Type** **Description**

`aggregate` ReportSummaryType Specifies the aggregation method—such as `Sum`, `Average`,
`Min`, and `Max` —for the summary value. Use the `column`

field to specify the summary value to use for the aggregation.
You don't need to specify this field for RowCount or custom
summary formulas.

`axisBinding` ChartAxis Specifies the axis or axes to use on the chart. Use the `column`
field to specify the summary value to use for the axis.

`column` string Required. Specifies the summary field for the chart data. If all
columns are invalid, RowCount is used by default for the axis

value. For vertical column and horizontal bar combination charts,
you can specify up to four values.

ChartAxis

An enumeration of type string that specifies the axis or axes to be used in charts. Valid values:

**Enumeration Value** **Description**

`x` The summary value to use for the X-axis of a scatter chart.

`y` The Y-axis for the chart.

`y2` The secondary Y-axis for vertical column combination charts with a line added.

ReportChartSize

An enumeration of type string that specifies the chart size. Valid values:

**Enumeration Value**

```
   Tiny

   Small

   Medium

   Large

   Huge

```

ChartRangeType

An enumeration of type string that defines the report format. Valid values:

**Enumeration Value**

```
   Auto

```


Metadata Types Report

**Enumeration Value**

```
   Manual

```

ReportTimeFrameFilter

ReportTimeFrameFilter represents the report time period.

**Field** **Field Type** **Description**

`dateColumn` string Required. The date field on which to filter data. For example,

```
                              CLOSE_DATE

```

`endDate` date When `interval` is `INTERVAL_CUSTOM`, specifies the end
of the custom time period.

`interval` UserDateInterval (enumeration Required. Specifies the period.
of type string)

`startDate` date When `interval` is `INTERVAL_CUSTOM`, specifies the
start of the custom time period.

ReportCrossFilter

ReportCrossFilter represents the cross filter functionality in reports.

**Field** **Field Type** **Description**

`criteriaItems` ReportFilterItem Represents the subfilters of a cross filter. There can be up to five
subfilters. This field requires the following attributes.

**•** `Column`

**•** `Operator`

**•** `Value`

`operation` ObjectFilterOperator The action indicating whether to include or exclude an object.
(Enumeration of type string) Valid values: `with` and `without` .

`primaryTableColumn` string The field from the parent object used for the cross filter.

`relatedTable` string The child object used for the cross filter.

`relatedTableJoinColumn` string The field from the child object that is used to join the parent.

Declarative Metadata Sample Definition

A sample XML snippet using cross filters to build an Accounts report for cases where case status isn’t closed:

```
      <crossFilters>

        <criteriaItems>

           <column>Status</column>

```


Metadata Types Report

```
           <operator>notequal</operator>

           <value>Closed</value>

        </criteriaItems>

        <operation>with</operation>

        <primaryTableColumn>ACCOUNT_ID</primaryTableColumn>

        <relatedTable>Case</relatedTable>

        <relatedTableJoinColumn>Account</relatedTableJoinColumn>

      </crossFilters>

```

Note: This sample was generated using the API version 23.0.

UserDateInterval

An enumeration of type string that defines the period. Valid values:

**Enumeration Value** **Description**

`INTERVAL_CURRENT` Current fiscal quarter

`INTERVAL_CURNEXT1` Current and next fiscal quarters

`INTERVAL_CURPREV1` Current and previous fiscal quarters

`INTERVAL_NEXT1` Next fiscal quarter

`INTERVAL_PREV1` Previous fiscal quarter

`INTERVAL_CURNEXT3` Current and next three fiscal quarters

`INTERVAL_CURFY` Current fiscal year

`INTERVAL_PREVFY` Previous fiscal year

`INTERVAL_PREV2FY` Previous two fiscal years

`INTERVAL_AGO2FY` Two fiscal years ago

`INTERVAL_NEXTFY` Next fiscal year

`INTERVAL_PREVCURFY` Current and previous fiscal years

`INTERVAL_PREVCUR2FY` Current and previous two fiscal years

`INTERVAL_CURNEXTFY` Current and next fiscal year

`INTERVAL_CUSTOM` A custom time period. Use `startDate` and `endDate` fields to specify the
time period's start date and end date.

`INTERVAL_YESTERDAY` Yesterday

`INTERVAL_TODAY` Today

`INTERVAL_TOMORROW` Tomorrow

`INTERVAL_LASTWEEK` Last calendar week

`INTERVAL_THISWEEK` This calendar week


Metadata Types Report

**Enumeration Value** **Description**

`INTERVAL_NEXTWEEK` Next calendar week

`INTERVAL_LASTMONTH` Last calendar month

`INTERVAL_THISMONTH` This calendar month

`INTERVAL_NEXTMONTH` Next calendar month

`INTERVAL_LASTTHISMONTH` Current and previous calendar months

`INTERVAL_THISNEXTMONTH` Current and next calendar months

`INTERVAL_CURRENTQ` Current calendar quarter

`INTERVAL_CURNEXTQ` Current and next calendar quarters

`INTERVAL_CURPREVQ` Current and previous calendar quarters

`INTERVAL_NEXTQ` Next calendar quarter

`INTERVAL_PREVQ` Previous calendar quarter

`INTERVAL_CURNEXT3Q` Current and next three calendar quarters

`INTERVAL_CURY` Current calendar year

`INTERVAL_PREVY` Previous calendar year

`INTERVAL_PREV2Y` Previous two calendar years

`INTERVAL_AGO2Y` Two calendar years ago

`INTERVAL_NEXTY` Next calendar year

`INTERVAL_PREVCURY` Current and previous calendar years

`INTERVAL_PREVCUR2Y` Current and previous two calendar years

`INTERVAL_CURNEXTY` Current and next calendar years

`INTERVAL_LAST7` Last 7 days

`INTERVAL_LAST30` Last 30 days

`INTERVAL_LAST60` Last 60 days

`INTERVAL_LAST90` Last 90 days

`INTERVAL_LAST120` Last 120 days

`INTERVAL_NEXT7` Next 7 days

`INTERVAL_NEXT30` Next 30 days

`INTERVAL_NEXT60` Next 60 days

`INTERVAL_NEXT90` Next 90 days

`INTERVAL_NEXT120` Next 120 days


Metadata Types Report

**Enumeration Value** **Description**

`LAST_FISCALWEEK` When custom fiscal years are enabled: Last fiscal week

`THIS_FISCALWEEK` When custom fiscal years are enabled: This fiscal week

`NEXT_FISCALWEEK` When custom fiscal years are enabled: Next fiscal week

`LAST_FISCALPERIOD` When custom fiscal years are enabled: Last fiscal period

`THIS_FISCALPERIOD` When custom fiscal years are enabled: This fiscal period

`NEXT_FISCALPERIOD` When custom fiscal years are enabled: Next fiscal period

`LASTTHIS_FISCALPERIOD` When custom fiscal years are enabled: This fiscal period and last fiscal period

`THISNEXT_FISCALPERIOD` When custom fiscal years are enabled: This fiscal period and next fiscal period

`CURRENT_ENTITLEMENT_PERIOD` Current entitlement period

`PREVIOUS_ENTITLEMENT_PERIOD` Previous entitlement period

`PREVIOUS_TWO_ENTITLEMENT_PERIODS` Previous two entitlement periods

`TWO_ENTITLEMENT_PERIODS_AGO` Two entitlement periods ago

`CURRENT_AND_PREVIOUS_ENTITLEMENT_PERIOD` Current and previous entitlement period

`CURRENT_AND_PREVIOUS_TWO_ENTITLEMENT_PERIODS` Current and previous two entitlement periods

Declarative Metadata Sample Definition

A sample XML report definition:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Report xmlns="http://soap.sforce.com/2006/04/metadata">

      <aggregates>

        <acrossGroupingContext>CRT_Object__c$Id</acrossGroupingContext>

        <calculatedFormula>PREVGROUPVAL(CRT_Object__c.Currency__c:AVG, CRT_Object__c.Id)

   *

             PARENTGROUPVAL(CRT_Object__c.Number__c:MAX, CRT_Object__c.CreatedBy.Name,

             COLUMN_GRAND_SUMMARY)/RowCount</calculatedFormula>

        <datatype>number</datatype>

        <developerName>FORMULA1</developerName>

        <downGroupingContext>CRT_Object__c$CreatedBy</downGroupingContext>

        <isActive>true</isActive>

        <masterLabel>CurrCSF</masterLabel>

        <scale>2</scale>

      </aggregates>

      <aggregates>

        <acrossGroupingContext>CRT_Object__c$LastModifiedDate</acrossGroupingContext>

        <calculatedFormula>IF(RowCount&gt;10,

             BLANKVALUE(ROUND(PREVGROUPVAL(CRT_Object__c.Currency__c:SUM,

             CRT_Object__c.LastModifiedDate),3),

             PARENTGROUPVAL(CRT_Object__c.Number__c:SUM, ROW_GRAND_SUMMARY,

```


Metadata Types Report

```
             CRT_Object__c.Id)), 1000)</calculatedFormula>

        <datatype>number</datatype>

        <developerName>FORMULA2</developerName>

        <downGroupingContext>GRAND_SUMMARY</downGroupingContext>

        <isActive>true</isActive>

        <masterLabel>numCSF</masterLabel>

        <scale>2</scale>

      </aggregates>

      <buckets>

        <bucketType>number</bucketType>

        <developerName>BucketField_BusinessSize</developerName>

        <masterLabel>NumericBucket</masterLabel>

        <nullTreatment>z</nullTreatment>

        <sourceColumnName>SALES</sourceColumnName>

        <values>

           <sourceValues>

             <to>10000</to>

           </sourceValues>

           <value>low</value>

        </values>

        <values>

           <sourceValues>

             <from>10000</from>

             <to>25000</to>

           </sourceValues>

           <value>mid</value>

        </values>

        <values>

           <sourceValues>

             <from>25000</from>

           </sourceValues>

           <value>high</value>

        </values>

      </buckets>

      <buckets>

        <bucketType>text</bucketType>

        <developerName>BucketField_Region</developerName>

        <masterLabel>TextBucket</masterLabel>

        <nullTreatment>n</nullTreatment>

        <otherBucketLabel>Other</otherBucketLabel>

        <sourceColumnName>ADDRESS1_STATE</sourceColumnName>

        <values>

           <sourceValues>

             <sourceValue>CA</sourceValue>

           </sourceValues>

           <value>west</value>

        </values>

        <values>

           <sourceValues>

             <sourceValue>NY</sourceValue>

           </sourceValues>

           <sourceValues>

             <sourceValue>Ontario</sourceValue>

           </sourceValues>

```


Metadata Types Report

```
           <value>east</value>

        </values>

      </buckets>

      <chart>

        <backgroundColor1>#FFFFFF</backgroundColor1>

        <backgroundColor2>#FFFFFF</backgroundColor2>

        <backgroundFadeDir>Diagonal</backgroundFadeDir>

        <chartSummaries>

           <axisBinding>y</axisBinding>

           <column>FORMULA1</column>

        </chartSummaries>

        <chartSummaries>

           <axisBinding>y</axisBinding>

           <column>FORMULA2</column>

        </chartSummaries>

        <chartSummaries>

           <aggregate>Maximum</aggregate>

           <axisBinding>y</axisBinding>

           <column>CRT_Object__c$Number__c</column>

        </chartSummaries>

        <chartSummaries>

           <axisBinding>y</axisBinding>

           <column>RowCount</column>

        </chartSummaries>

        <chartType>VerticalColumn</chartType>

        <groupingColumn>CRT_Object__c$LastModifiedDate</groupingColumn>

        <legendPosition>Right</legendPosition>

        <location>CHART_TOP</location>

        <size>Medium</size>

        <summaryAxisRange>Auto</summaryAxisRange>

        <textColor>#000000</textColor>

        <textSize>12</textSize>

        <titleColor>#000000</titleColor>

        <titleSize>18</titleSize>

      </chart>

      <columns>

        <field>CRT_Object__c$Name</field>

      </columns>

      <columns>

        <aggregateTypes>Average</aggregateTypes>

        <field>CRT_Object__c$Currency__c</field>

      </columns>

      <columns>

        <aggregateTypes>Maximum</aggregateTypes>

        <field>CRT_Object__c$Number__c</field>

      </columns>

      <columns>

        <field>BucketField__Region</field>

      </columns>

      <format>Matrix</format>

      <groupingsAcross>

        <dateGranularity>Day</dateGranularity>

        <field>CRT_Object__c$Id</field>

        <sortOrder>Asc</sortOrder>

```


Metadata Types Report

```
      </groupingsAcross>

      <groupingsAcross>

        <dateGranularity>Year</dateGranularity>

        <field>CRT_Object__c$LastModifiedDate</field>

        <sortOrder>Asc</sortOrder>

      </groupingsAcross>

      <groupingsDown>

        <dateGranularity>Day</dateGranularity>

        <field>CRT_Object__c$CreatedBy</field>

        <sortOrder>Asc</sortOrder>

      </groupingsDown>

      <groupingsDown>

        <dateGranularity>Day</dateGranularity>

        <field>CRT_Object__c$Currency__c</field>

        <sortOrder>Desc</sortOrder>

      </groupingsDown>

      <name>CrtMMVC</name>

      <reportType>CRT1__c</reportType>

      <scope>organization</scope>

      <showDetails>false</showDetails>

      <timeFrameFilter>

        <dateColumn>CRT_Object__c$CreatedDate</dateColumn>

        <interval>INTERVAL_CUSTOM</interval>

      </timeFrameFilter>

   </Report>

```

Declarative Metadata Sample Definition for a Joined Report

A sample XML report definition:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Report xmlns="http://soap.sforce.com/2006/04/metadata">

   <!-- This is a cross-block custom summary formula. Note that the calculated formula reference

    for a blocks reference uses the BlockId#Aggregate. -->

      <aggregates>

        <calculatedFormula>B1#AMOUNT:SUM+B2#EMPLOYEES:SUM</calculatedFormula>

        <datatype>number</datatype>

        <developerName>FORMULA</developerName>

        <isActive>true</isActive>

        <isCrossBlock>true</isCrossBlock>

        <masterLabel>Cross-Block CSF Example</masterLabel>

        <scale>2</scale>

      </aggregates>

   <!-- This is a standard custom summary formula. Note that the calculated formula reference

    does not have block reference but just the aggregate name of the report type associated

   (Opportunity).-->

      <aggregates>

        <calculatedFormula>AMOUNT:SUM</calculatedFormula>

        <developerName>FORMULA2</developerName>

        <isActive>true</isActive>

        <isCrossBlock>false</isCrossBlock>

        <masterLabel>Standard CSF Example</masterLabel>

        <reportType>Opportunity</reportType>

        <scale>2</scale>

```


Metadata Types Report

```
      </aggregates>

      <block>

       <blockInfo>

   <!-- This is how the block defines that the custom summary formula should be referenced.

   In this example, it’s the in standard FORMULA 2 defined above. This block report has blockID

    B1.-->

        <aggregateReferences>

         <aggregate>FORMULA2</aggregate>

        </aggregateReference>

        <blockId>B1</blockId>

        <joinTable>a</joinTable>

       </blockInfo>

       <columns>

        <field>TYPE</field>

       </columns>

       <format>Summary</format>

       <name>Opportunities BLock 3</name>

       <params>

        <name>role_territory</name>

        <value>role</value>

       </params>

       <params>

        <name>terr</name>

        <value>all</value>

       </params>

       <params>

        <name>open</name>

        <value>all</value>

       </params>

       <params>

        <name>probability</name>

        <value>0</value>

       </params>

       <params>

        <name>co</name>

        <value>1</value>

       </params>

       <reportType>Opportunity</reportType>

       <scope>organization</scope>

       <timeFrameFilter>

        <dateColumn>CLOSE_DATE</dateColumn>

        <interval>INTERVAL_CUSTOM</interval>

       </timeFrameFilter>

      </block>

      <block>

       <blockInfo>

   <!-- This is how the block defines that the custom summary formula should be referenced.

   In this example, it’s the cross-block custom summary formula FORMULA 1 defined above. This

    block report has blockId B2.-->

        <aggregateReferences>

         <aggregate>FORMULA1</aggregate>

        </aggregateReferences>

        <blockId>B2</blockId>

        <joinTable>a</joinTable>

```


Metadata Types Report

```
       </blockInfo>

       <columns>

        <field>USERS.NAME</field>

       </columns>

       <columns>

        <field>TYPE</field>

       </columns>

       <columns>

         <field>DUE_DATE</field>

       </columns>

       <columns>

        <field>LAST_UPDATE</field>

       </columns>

       <columns>

        <field>ADDRESS1_STATE</field>

       </columns>

       <format>Summary</format

       <name>Accounts block 5</name>

       <params>

        <name>terr</name>

        <value>all</value>

       </params>

       <params>

        <name>co</name>

        <value>1</value>

       </params>

       <reportType>AccountList</reportType>

       <scope>organization</scope>

       <timeFrameFilter>

        <dateColumn>CREATED_DATE</dateColumn>

        <interval>INTERVAL_CUSTOM</interval>

       </timeFrameFilter>

      </block>

      <blockInfo>

       <blockId xsi:nil="true"/>

       <joinTable>a</joinTable>

      </blockInfo>

   <chart>

        <backgroundColor1>#FFFFFF</backgroundColor1>

        <backgroundColor2>#FFFFFF</backgroundColor2>

        <backgroundFadeDir>Diagonal</backgroundFadeDir>

        <chartSummaries>

           <axisBinding>y</axisBinding>

   <!-- This is how chart aggregates are designed in multiblock. We're using RowCount from

   Block 1.-->

           <column>B1#RowCount</column>

        </chartSummaries>

        <chartType>HorizontalBar</chartType>

        <enableHoverLabels>false</enableHoverLabels>

        <expandOthers>true</expandOthers>

        <groupingColumn>ACCOUNT_NAME</groupingColumn>

        <location>CHART_TOP</location>

        <showAxisLabels>true</showAxisLabels>

        <showPercentage>false</showPercentage>

```


### Metadata Types ReportType

```
        <showTotal>false</showTotal>

        <showValues>false</showValues>

        <size>Medium</size>

        <summaryAxisRange>Auto</summaryAxisRange>

        <textColor>#000000</textColor>

        <textSize>12</textSize>

        <titleColor>#000000</titleColor>

        <titleSize>18</titleSize>

      </chart>

      <format>MultiBlock</format>

      <groupingsDown>

        <dateGranularity>Day</dateGranularity>

        <field>ACCOUNT_NAME</field>

        <sortOrder>Asc</sortOrder>

      </groupingsDown>

      <name>mb_mbapi</name>

      <reportType>Opportunity</reportType>

      <showDetails>true</showDetails>

   </Report>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

Dashboard

### ReportType

Represents the metadata associated with a custom report type. Custom report types allow you to build a framework from which users
can create and customize reports.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

This type extends the Metadata metadata type and inherits its `fullName` field.

Declarative Metadata File Suffix and Directory Location

The file suffix is `.reportType` for the custom report type definition. There’s one file per custom report type. Report types are stored
in the `reportTypes` directory of the corresponding package directory.

Version

Custom report types are available in API version 14.0 and later.


Metadata Types ReportType

Fields

**Field Name** **Field Type** **Description**

`autogenerated` boolean

`baseObject` string

Indicates that the report type was automatically generated when historical
trending was enabled for an entity.

Available in API version 29 and later.

Required. The primary object for the custom report type, for example,
Account. All objects, including custom and external objects, are supported.
You can’t edit this field after initial creation.

Support for external objects is available in API version 38.0 and later.

`category` ReportTypeCategory This field controls the category for the report. The valid values are:
(enumeration of type string)

**•** `accounts`

**•** `opportunities`

**•** `forecasts`

**•** `cases`

**•** `leads`

**•** `campaigns`

**•** `activities`

**•** `busop`

**•** `products`

**•** `admin`

**•** `territory`

**•** `territory2` (This value is available in API version 31.0 and later.)

**•** `usage_entitlement`

**•** `wdc` (This value is available in API version 29.0 and later.)

**•** `calibration` (This value is available in API version 29.0 and later.)

**•** `other`

**•** `content`

**•** `quotes`

**•** `individual` (This value is available in API version 45.0 and later.)

**•** `employee` (This value is available in API version 46.0 and later.)

**•** `data_cloud` (This value is available in API version 55.0 and later.)

**•** `commerce` (This value is available in API version 60.0 and later.)

**•** `flow` (This value is available in API version 60.0 and later.)

**•** `semantic_model` (This value is available in API version 60.0 and
later.)

`deployed` boolean Required. Indicates whether the report type is available to users ( `true` )
or whether it's still in development ( `false` ).


Metadata Types ReportType

**Field Name** **Field Type** **Description**

`description` string The description of the custom report type.

`fullName` string The report type developer name used as a unique identifier for API access.
The `fullName` can contain only underscores and alphanumeric

characters. It must be unique, begin with a letter, not include spaces, not
end with an underscore, and not contain two consecutive underscores.

`join` ObjectRelationship The object joined to the `baseObject` . For example, Contacts can be
joined to the primary Accounts object.

`label` string Required. The report type label.

`sections` ReportLayoutSection[] The groups of columns available for the report type. Though columns
aren’t strictly required, a report without columns isn’t useful.

ObjectRelationship

ObjectRelationship represents a join to another object.

**Field Name** **Field Type** **Description**

`join` ObjectRelationship This field is a recursive reference that allows you to join more than two objects.
A maximum of four objects can be joined in a custom report type. When more

than two objects are joined, an inner join isn’t allowed if there has been an outer
join earlier in the join sequence. The `baseObject` is first joined to the object
specified in `relationship` ; the resulting dataset is then joined with any
objects specified in this field.

`outerJoin` boolean

Required. Indicates whether it’s an outer join ( `true` ) or not ( `false` ). An outer
join returns a row even if the joined table doesn’t contain a matching value in
the join column.

`relationship` string Required. The object joined to the primary object; for example, Contacts.

ReportLayoutSection

ReportLayoutSection represents a group of columns used in the custom report type.

**Field Name** **Field Type** **Description**

`columns` ReportTypeColumn[] The list of columns projected from the query, defined by
this custom report type.

`masterLabel` string Required. The label for this group of columns in the report
wizard.


Metadata Types ReportType

ReportTypeColumn

ReportTypeColumn represents a column in the custom report type.

**Field Name** **Field Type** **Description**

`checkedByDefault` boolean Required. Indicates whether this column is selected by default ( `true` ) or not
( `false` ).

`displayNameOverride` string A customized column name, if desired.

`field` string Required. The field name associated with the report column.

`table` string Required. The table associated with the field; for example, Account.

Declarative Metadata Sample Definition

The definition of a custom report type is shown in this example. Account is joined to Contacts and the resulting dataset is joined with
Assets.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ReportType xmlns="http://soap.sforce.com/2006/04/metadata">

      <baseObject>Account</baseObject>

      <category>accounts</category>

      <deployed>true</deployed>

      <description>Account linked to Contacts and Assets</description>

      <join>

        <join>

           <outerJoin>false</outerJoin>

           <relationship>Assets</relationship>

        </join>

        <outerJoin>false</outerJoin>

        <relationship>Contacts</relationship>

      </join>

      <label>Account Contacts and Assets</label>

      <sections>

        <columns>

           <checkedByDefault>true</checkedByDefault>

           <field>obj_lookup__c.Id</field>

           <table>Account</table>

        </columns>

        <columns>

           <checkedByDefault>false</checkedByDefault>

           <field>obj_lookup__c.Name</field>

           <table>Account</table>

        </columns>

        <columns>

           <checkedByDefault>false</checkedByDefault>

           <field>Opportunity__c.Amount</field>

           <table>Account</table>

        </columns>

        <columns>

           <checkedByDefault>false</checkedByDefault>

           <field>Owner.IsActive</field>

```


### Metadata Types RestrictionRule

```
           <table>Account</table>

        </columns>

        <masterLabel>Accounts</masterLabel>

      </sections>

      <sections>

        <columns>

           <checkedByDefault>false</checkedByDefault>

           <field>Owner.Email</field>

           <table>Account.Contacts</table>

        </columns>

        <columns>

           <checkedByDefault>false</checkedByDefault>

           <field>byr__c</field>

           <table>Account.Contacts</table>

        </columns>

        <columns>

           <checkedByDefault>true</checkedByDefault>

           <field>ReportsTo.CreatedBy.Contact.Owner.MobilePhone</field>

           <table>Account.Contacts</table>

        </columns>

        <masterLabel>Contacts</masterLabel>

      </sections>

   </ReportType>

```

Usage

The custom report type refers to fields by using their API names. For a historical field (one that has `trackTrending` set to `true` )
the API name includes `hst`, such as `Field2__c_hst` .

```
   <sections>

      <columns>

        <checkedByDefault>false</checkedByDefault>

        <field>Field2__c_hst</field>

        <table>CustomTrendedObject__c.CustomTrendedObject__c_hst</table>

      </columns>

      <masterLabel>History</masterLabel>

   </sections>

```

For more information, see `trackTrending` on page 771.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### RestrictionRule Represents a restriction rule or a scoping rule. A restriction rule has enforcementType set to Restrict and controls the access

that specified users have to designated records. A scoping rule has `enforcementType` set to `Scoping` and controls the default
records that your users see without restricting access. This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types RestrictionRule

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

RestrictionRule components have the suffix `.rule` and are stored in the `restrictionRules` folder.

Version

RestrictionRule components are available in API version 52.0 and later.

Special Access Rules

Only users with the View Restriction and Scoping Rules permission can view restriction rules and scoping rules via the API. Only users
with the Manage Sharing permission can view, create, update, and delete restriction rules and scoping rules.

Fields

**Field Name** **Field Type** **Description**

`active` boolean Indicates whether the rule is active ( `true` ) or not ( `false` ). The default
value is `false` .

`description` string Required. The description of the rule.

```
enforcementType

```

EnforcementType Required. The type of rule. Valid values are:
(enumeration of

**•** `FieldRestrict` —Don’t use.

type string)

**•** `FieldRestrict` —Don’t use.

**•** `Restrict` —Restriction rule.

**•** `Scoping` —Scoping rule.

`masterLabel` string Required. The name of the rule.

`recordFilter` string Required. The criteria that determine which records are accessible via
the rule.

`targetEntity` string

Required. The object for which you're creating the rule. We recommend
that you don’t edit this field after the rule is created.

If `enforcementType` is set to `Restrict`, custom objects, external
objects, and these objects are supported:

**•** Contract

**•** Event

**•** Task

**•** TimeSheet

**•** TimeSheetEntry

If `enforcementType` is set to `Scoping`, custom objects and these
objects are supported:


Metadata Types RestrictionRule

**Field Name** **Field Type** **Description**

**•** Account

**•** Case

**•** Contact

**•** Event

**•** Lead

**•** Opportunity

**•** Task

`userCriteria` string Required. The users that this rule applies to, such as all active users or
users with a specified role or profile.

`version` int Required. The rule's version number.

Declarative Metadata Sample Definition

The following is an example of a RestrictionRule component representing a restriction rule.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <RestrictionRule xmlns="http://soap.sforce.com/2006/04/metadata">

      <active>true</active>

      <description>Allows users with a specific profile to see only tasks that they

   own.</description>

      <enforcementType>Restrict</enforcementType>

      <masterLabel>Tasks You Own</masterLabel>

      <recordFilter>OwnerId = $User.Id</recordFilter>

      <targetEntity>Task</targetEntity>

      <userCriteria>$User.ProfileId = '00exxxxxxxxxxxx'</userCriteria>

      <version>1</version>

   </RestrictionRule>

```

The following is an example of a RestrictionRule component representing a scoping rule.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <RestrictionRule xmlns="http://soap.sforce.com/2006/04/metadata">

      <active>true</active>

      <description>View tasks contacts from Department A.</description>

      <enforcementType>Scoping</enforcementType>

      <masterLabel>SR for Department A contacts</masterLabel>

      <recordFilter>Department=$User.Department</recordFilter>

      <targetEntity>Contact</targetEntity>

      <userCriteria>$User.UserRoleId = '00Exxxxxxxxxxxx'</userCriteria>

      <version>1</version>

   </RestrictionRule>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

```


### Metadata Types RetrievalSummaryDefinition

```
        <name>RestrictionRule</name>

      </types>

      <version>55.0</version>

   </Package>

### RetrievalSummaryDefinition

```

Represents a metadata type that stores the header information of a retrieval definition. It enables the configuration of data retrieval
patterns for summarizing related records across object relationships.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### RetrievalSummaryDefinition components have the suffix .retrievalSummaryDefinition and are stored in the

`.retrievalSummaryDefinitions` folder.

Version

### RetrievalSummaryDefinition components are available in API version 61.0 and later. Individual fields may have specific minimum API

version requirements as mentioned in the field descriptions.

Fields

**Field Name** **Description**

```
masterLabel

retrievalSummaryDefFields

retrievalSummaryDefObjects

```

**Field Type**
string

**Description**

Required.

A user-friendly name when RetrievalSummaryDefinition is created.

**Field Type**

RetrievalSummaryDefField[]

**Description**
Collection of fields to retrieve from the root object of the retrieval definition. Each field
definition specifies which field from the target object should be included in the retrieval
and the order in which it should be processed.

**Field Type**

RetrievalSummaryDefObject[]


Metadata Types RetrievalSummaryDefinition

**Field Name** **Description**

**Description**
Collection of rollup definitions that aggregate data from related objects. Each object
definition specifies a related object, the aggregation logic to apply, and the fields to
retrieve from that object. This enables hierarchical data aggregation across object
relationships.

```
rootObject

```

**Field Type**
string

**Description**

Required.

API name of the primary object that serves as the starting point for the retrieval
definition. This object serves as the anchor point for all retrieval and rollup operations
defined in this metadata. The value must be a valid Salesforce object API name.

RetrievalSummaryDefField

Represents a field definition that specifies a single field to retrieve from a target object. Each field definition includes the field API name
and a sequence number that determines the processing order.

**Field Name** **Description**

```
field

sequenceNumber

```

**Field Type**
string

**Description**

Required.

API name of the field to retrieve from the target object. This must be a valid field API
name on the specified object.

**Field Type**
int

**Description**

Required.

Processing order of the field in the retrieval operation. Fields are processed in ascending
sequence number order. This allows you to control the order in which fields are
displayed.

RetrievalSummaryDefObject

Represents a rollup definition that aggregates data from a related object. Each rollup definition specifies the aggregation logic, the fields
to retrieve, and the processing order for summarizing data across object relationships.


Metadata Types RetrievalSummaryDefinition

**Field Name** **Description**

```
recordAggregationDefinition

retrievalSummaryDefFields

sequenceNumber

```

Usage

**Field Type**
string

**Description**

Required.

Reference to the aggregation definition that specifies how data from the related object
must be aggregated. This parameter references a RecordAggregationDefinition.

**Field Type**

RetrievalSummaryDefField[]

**Description**
Collection of fields to retrieve from this related object. Each field definition specifies
which field should be included and in what order. This is an optional array that allows
you to specify additional fields beyond those defined in the aggregation definition.

**Field Type**
int

**Description**

Required.

Processing order of the rollup operation. Rollups are processed in ascending sequence
number order, allowing you to control the hierarchy of data aggregation when multiple
related objects are involved.

RetrievalSummaryDefinition is commonly used in Financial Services Cloud to define patterns for retrieving and summarizing data across
related objects. Typical use cases include:

**•** Rollup Summarization: Aggregate data from child records to parent records, such as summing transaction amounts or counting
related activities.

**•** Hierarchical Data Aggregation: Retrieve and summarize data across multiple levels of object relationships, enabling complex reporting
and analytics.

**•** Data Consolidation: Combine information from multiple related objects into a single summary view for easier analysis and
decision-making.

**•** Performance Optimization: Pre-define retrieval patterns to improve query performance when accessing related data across multiple
objects.

Declarative Metadata Sample Definition

The following is an example of a RetrievalSummaryDefinition component that retrieves data from an Account object and includes a
rollup from related Opportunity records.

```
<?xml version="1.0" encoding="UTF-8"?>

<RetrievalSummaryDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

```


### Metadata Types Role

```
     <masterLabel>Account Revenue Summary</masterLabel>

     <rootObject>Account</rootObject>

     <retrievalSummaryDefFields>

       <field>Name</field>

       <sequenceNumber>1</sequenceNumber>

     </retrievalSummaryDefFields>

     <retrievalSummaryDefFields>

       <field>Industry</field>

       <sequenceNumber>2</sequenceNumber>

     </retrievalSummaryDefFields>

     <retrievalSummaryDefObjects>

       <recordAggregationDefinition>OpportunityRevenueRollup</recordAggregationDefinition>

       <sequenceNumber>1</sequenceNumber>

       <retrievalSummaryDefFields>

         <field>Amount</field>

         <sequenceNumber>1</sequenceNumber>

       </retrievalSummaryDefFields>

       <retrievalSummaryDefFields>

         <field>CloseDate</field>

         <sequenceNumber>2</sequenceNumber>

       </retrievalSummaryDefFields>

     </retrievalSummaryDefObjects>

   </RetrievalSummaryDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>RetrievalSummaryDefinition</name>

      </types>

      <version>61.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### Role

Represents a role in your organization.

Declarative Metadata File Suffix and Directory Location

The file suffix for role components is `.role` and components are stored in the `roles` directory of the corresponding package
directory.


### Metadata Types RoleOrTerritory

Version

Role components are available in API version 24.0 and later.

Fields

This metadata type extends to subtype RoleOrTerritory on page 1874.

**Field Name** **Field Type** **Description**

`fullName` string The unique identifier for API access. The `fullName` can contain only
underscores and alphanumeric characters. It must be unique, begin with

a letter, not include spaces, not end with an underscore, and not contain
two consecutive underscores. This field is inherited from the Metadata
component. Corresponds to **Role Name** in the user interface.

`parentRole` string The role above this role in the hierarchy.

Declarative Metadata Sample Definition

The following is the definition of a role.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Role xmlns="http://soap.sforce.com/2006/04/metadata">

      <caseAccessLevel>Edit</caseAccessLevel>

      <contactAccessLevel>Edit</contactAccessLevel>

      <description>Sample Role</description>

      <mayForecastManagerShare>false</mayForecastManagerShare>

      <name>R22</name>

      <opportunityAccessLevel>Read</opportunityAccessLevel>

   </Role>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### RoleOrTerritory

Represents the common base type and valid values for role or territory.

Version

### RoleOrTerritory components are available in API version 24.0 and later.

Note: You can’t create a RoleOrTerritory component directly. Use the Role or Territory metadata types instead.


Metadata Types RoleOrTerritory

Fields

**Field Name** **Field Type** **Description**

`caseAccessLevel` string Specifies whether a user can access other users’ cases that are associated
with accounts the user owns. Valid values are:

**•** `Read`

**•** `Edit`

**•** `None`

This field is not visible if your organization’s sharing model for cases is
Public Read/Write.

If no value is set for this field, this field value uses the default access level
that is specified in the Manage Territory page in Setup.

`contactAccessLevel` string Specifies whether a user can access other users’ contacts that are
associated with accounts the user owns. Valid values are:

**•** `Read`

**•** `Edit`

**•** `None`

This field is not visible if your organization’s sharing model for contacts
is Public Read/Write or Controlled by Parent.

If no value is set for this field, this field value uses the default access level
that is specified in the Manage Territory page in Setup.

`description` string The description of the role or territory.

`fullName` string The unique identifier for API access. The `fullName` can contain only
underscores and alphanumeric characters. It must be unique, begin with

a letter, not include spaces, not end with an underscore, and not contain
two consecutive underscores. This field is inherited from the Metadata
component.

`mayForecastManagerShare` boolean Indicates whether the forecast manager can manually share their own
forecast.

`name` string Required. The name of the role or territory.

`opportunityAccessLevel` string Specifies whether a user can access other users’ opportunities that are
associated with accounts the user owns. Valid values are:

**•** `Read`

**•** `Edit`

**•** `None`

This field is not visible if your organization’s sharing model for
opportunities is Public Read/Write.

If no value is set for this field, this field value uses the default access level
that is specified in the Manage Territory page in Setup.


### Metadata Types RpaRobotPoolMetadata

Declarative Metadata Sample Definition

The following is the definition of a role.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Role xmlns="http://soap.sforce.com/2006/04/metadata">

      <caseAccessLevel>Edit</caseAccessLevel>

      <contactAccessLevel>Edit</contactAccessLevel>

      <description>Sample Role</description>

      <mayForecastManagerShare>false</mayForecastManagerShare>

      <name>R22</name>

      <opportunityAccessLevel>Read</opportunityAccessLevel>

   </Role>

```

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

SEE ALSO:

Role

Territory

### RpaRobotPoolMetadata

Reserved for future use.

### SalesWorkQueueSettings

Represents settings used to customize work queue options for third-party scoring. In Sales Engagement, you can add a custom number
field on person accounts, contacts, or leads. Then, use the custom number field to sort the work queue. This type extends the Metadata
metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### SalesWorkQueueSettings components have the suffix .salesworkqueuesetting and are stored in the

`salesworkqueuesettings` folder.

Version

### SalesWorkQueueSettings components are available in API version 49.0 and later.


Metadata Types SalesWorkQueueSettings

Special Access Rules

You must be a Sales Engagement customer to access this metadata type.

Fields

**Field Name** **Field Type** **Description**

`featureName` string The feature that the SalesWorkQueueSettings record is configuring. The allowed
value is `ThirdPartyScore` .

`targetEntity` string The type that the SalesWorkQueueSettings record is configuring. Possible values
are:

**•** `Contact`

**•** `Lead`

**•** `PersonAccount`

`targetField` string The developer name or ID of the custom number field that is used to sort the
work queue. Custom fields must have a custom number data type.

**•** To use Einstein Intelligence Score for lead scoring, use
`ScoreIntelligence.Score` for the developer name.

**•** To remove custom number fields from the work queue, use `None` .

Declarative Metadata Sample Definition

The following is an example of a SalesWorkQueueSettings component. The value for `targetField` is set to `00NRM000001g55D`
as an example of a custom field ID. Replace this value with the ID of your custom field.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <SalesWorkQueueSettings xmlns="http://soap.sforce.com/2006/04/metadata">

      <featureName>ThirdPartyScore</featureName>

      <targetEntity>Contact</targetEntity>

      <targetField>00NRM000001g55D</targetField>

   </SalesWorkQueueSettings>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>SalesWorkQueueSettings</name>

      </types>

      <version>49.0</version>

   </Package>

```


### Metadata Types SamlSsoConfig

Usage

Create one SalesWorkQueueSettings record for each type. For example, suppose that you want to create a work queue to sort leads by
your custom field called `customLeadScore` . Create a SalesWorkQueueSettings record and set `featureName` to
`ThirdPartyScore`, `targetEntity` to `Lead`, and `targetField` to `customLeadScore` .

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### SamlSsoConfig

Represents a SAML Single Sign-On configuration. This type extends the Metadata metadata type and inherits its `fullName` field.
Single sign-on (SSO) is an authentication method that enables users to access multiple applications with one login and one set of
credentials. For example, after users log in to your org, they can automatically access all apps from the App Launcher. You can set up
your Salesforce org to trust a third-party identity provider to authenticate users. Or you can configure a third-party app to rely on your
org for authentication.

File Suffix and Directory Location

### SamlSsoConfig components have the suffix .samlssoconfig and are stored in the samlssoconfigs folder.

Version

### SamlSsoConfig components are available in API version 28.0 and later.

Special Access Rules

As of Summer ’20 and later, only users with the View Setup and Configuration permission or both the Customize Application and Modify
All Data permissions can access this type.

Fields

**Field Name** **Field Type** **Description**

`attributeNameIdFormat` string For SAML 2.0, only and when `identityLocation` is set to
`Attribute` . Possible values include `unspecified`,

`emailAddress`, or `persistent` . All legal values can be found in
[the “Name Identifier Format Identifiers” section of the Assertions and](http://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf)
[Protocols SAML 2.0 specification.](http://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf)

`attributeName` string The name of the identity provider’s application. Get this name from your
identity provider.


Metadata Types SamlSsoConfig

**Field Name** **Field Type** **Description**

`decryptionCertificate` string

`errorUrl` string

The name of the certificate to use for decrypting incoming SAML
assertions. This certificate is saved in the organization’s Certificate and
Key Management list. Available in API version 30.0 and later.

When there's an error during login, specify the URL of the page where
users are directed. It must be publicly accessible, such as a public site
Visualforce page. The URL can be absolute or relative.

`executionUserId` string The user that runs the Apex handler class. The user must have the Manage
Users permission. If you specify a SAML JIT handler class, a user is required.

```
identityLocation

identityMapping

```

SamlIdentityLocationType The location in the assertion where a user is identified. Valid values are:
(enumeration of type

**•** `SubjectNameId`           - The identity is in the `<Subject>`

string)

statement of the assertion.

**•** `Attribute`           - The identity is specified in an
`<AttributeValue>`, located in the `<Attribute>` of the
assertion.

SamlIdentityType The identifier the service provider uses for the user during Just-in-Time
(enumeration of type user provisioning. Valid values are:
string)

**•** `Username`           - The user’s Salesforce username.

**•** `FederationId`           - The federation ID from the user object; the
identifier used by the service provider for the user.

**•** `UserId`           - The user ID from the user’s Salesforce organization.

`issuer` string The identification string for the Identity Provider.

`loginUrl` string For SAML 2.0 only: The URL where Salesforce sends a SAML request to
start the login sequence.

`logoutUrl` string For SAML 2.0 only: The URL to direct the user to when they click the
Logout link. The default is `https://salesforce.com` .

`name` string The unique name used by the API and managed packages. The name
must begin with a letter and use only alphanumeric characters and

underscores. The name cannot end with an underscore or have two
consecutive underscores.

`oauthTokenEndpoint` string For SAML 2.0 only: The ACS URL used with enabling Salesforce as an
identity provider in the web single sign-on OAuth assertion flow.

`redirectBinding` boolean Choose the binding mechanism your identity provider requests for your
SAML messages. Values are:

**•** `HTTP POST`                       - HTTP POST binding sends SAML messages using
base64-encoded HTML forms.

**•** `HTTP Redirect`                       - HTTP Redirect binding sends base64-encoded
and URL-encoded SAML messages within URL parameters.


Metadata Types SamlSsoConfig

**Field Name** **Field Type** **Description**

`requestSignatureMethod` string The method that’s used to sign the SAML request. Valid values are
`RSA-SHA1` and `RSA-SHA256` .

`requestSigningCertId` string

The 18-digit ID for the certificate used to generate the signature on a
SAML request to the identity provider. The certificate is saved in the
Certificate and Key Management page in Setup.

`salesforceLoginUrl` string The URL associated with login for the web single sign-on flow.

Note: When encryption is enabled, the URL has a parameter
containing the ID of the SAML configuration,

`sc=` _**`samlSsoConfigId`**_ . For example,
`https://mycompany.my.salesforce.com?sc=0LEB0000000CCC` .
This change applies to API Version 47.0 and later.

`samlEntityId` string

The issuer in SAML requests generated by Salesforce, and is also the
expected audience of any inbound SAML Responses. Salesforce
recommends that you use your My Domain login URL.

`samlJitHandlerId` string The name of an existing Apex class that implements the
`Auth.SamlJitHandler` interface.

`samlVersion` SamlType (enumeration of The SAML version in use. Valid values are:
type string)

**•** `SAML1_1`                       - SAML 1.1

**•** `SAML2_0`                       - SAML 2.0

The HTTP binding type. This value determines where to put the
LogoutRequest or LogoutResponse in the SAML request during single
logout (SLO). The value is base64 encoded. Valid values are:

**•** `RedirectBinding` - Sent in the query string, deflated.

**•** `PostBinding` - Sent in the POST body, not deflated.

The SAML single logout endpoint. This URL is the endpoint where
Salesforce sends LogoutRequests (when Salesforce initiates a logout), or
LogoutResponses (when the identity provider initiates a logout).

```
singleLogoutBinding

```

SamlSpSLOBinding
(enumeration of type
string)

`singleLogoutUrl` string

`useConfigRequestMethod` boolean If `true`, applies the selected Request Signature Method (RSM) during
single logout. If `false`, the default RSM (RSA-SHA1) is applied.

`useSameDigestAlgoForSigning` boolean

If `true`, uses a digest algorithm based on the selected Request Signature
Method (RSM). For example, if the selected RSM is `RSA-SHA256`, the
digest algorithm is set to `SHA-256` .

If `false`, uses the default digest algorithm ( `SHA-1` ), regardless of the
selected RSM.

This field is available in API version 55.0 and later. You can edit this field
only for legacy SAML configurations created before Spring ’22. For
configurations created after Spring ’22, this field is `true` by default.


### Metadata Types SchedulingObjective

**Field Name** **Field Type** **Description**

`userProvisioning` boolean

If `true`, Just-in-Time user provisioning is enabled, which creates users
the first time they log in. Specify `Federation ID` for the
`identityMapping` value to use this feature.

`validationCert` string The certificate used to validate the request. Get this certificate from your
identity provider.

Declarative Metadata Sample Definition

The following is an example of a SamlSsoConfig component. The validation certificate string has been truncated for readability.

```
<?xml version="1.0" encoding="UTF-8"?>

<SamlSsoConfig xmlns="http://soap.sforce.com/2006/04/metadata">

  <identityLocation>SubjectNameId</identityLocation>

  <identityMapping>FederationId</identityMapping>

  <issuer>https://my-idp.my.salesforce.com</issuer>

  <loginUrl>

   https://my-idp.my.salesforce.com/idp/endpoint/HttpRedirect

  </loginUrl>

  <logoutUrl>https://www.salesforce.com</logoutUrl>

  <name>SomeCompany</name>

  <oauthTokenEndpoint>

   https://login.salesforce.com/services/oauth2/token?so=00DD0000000

  </oauthTokenEndpoint>

  <redirectBinding>true</redirectBinding>

  <requestSignatureMethod>RSA-SHA1</requestSignatureMethod>

  <salesforceLoginUrl>

   https://login.salesforce.com?so=00DD0000000JxeI

  </salesforceLoginUrl>

  <samlEntityId>

   https://saml.salesforce.com/customPath

  </samlEntityId>

  <samlVersion>SAML2_0</samlVersion>

  <useConfigRequestMethod>true</useConfigRequestMethod>

  <userProvisioning>false</userProvisioning>

  <validationCert>

   MIIEojCCA4qgAwIBAgIOATtxsoBFAAAAAD4...

  </validationCert>

</SamlSsoConfig>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### SchedulingObjective

Represents a scheduling objective in Workforce Engagement. Scheduling objectives define business goals that the scheduling tools
consider when identifying agents for shifts.


Metadata Types SchedulingObjective

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

`SchedulingObjective` components have the suffix `.SchedulingObjective` and are stored in the
`SchedulingObjective` folder.

Version

SchedulingObjective components are available in API version 55.0 and later.

Special Access Rules

This type is available only if Workforce Engagement is enabled in your org. To view, create, edit, and delete records, the user requires
the Workforce Engagement Planner permission set.

Fields

**Field Name** **Description**

```
isProtected

masterLabel

schedulingCategory

```

**Field Type**
boolean

**Description**
Indicates whether the component is protected ( `true` ) or not ( `false` ). The default
value is `false` .

**Field Type**
string

**Description**
Required. The name of the objective.

**Field Type**
SchedulingCategory (enumeration of type string)

**Description**
Required. What the scheduling logic applies the objective to. The valid values are:

**•** `A` —Service Appointment

**•** `B` —Shift


Metadata Types SchedulingObjective

**Field Name** **Description**

```
schedulingObjectiveParameters

schedulingObjectiveType

```

**Field Type**

```
  SchedulingObjectiveParameter[] on page 1883

```

**Description**
Parameters associated with a scheduling objective, such as the number of days before
and after a shift that the logic considers when balancing assignments.

**Field Type**
SchedulingObjectiveType (enumeration of type string)

**Description**
Required. Specifies the type of objective. Possible values are:

**•** `AgentPreference` —In the UI, this value appears as Maximized Preferences.

**•** `BalanceNonStandardShifts`

**•** `BalanceShifts`

SchedulingObjectiveParameter

Represents a parameter that’s associated with a scheduling objective.

**Field Name** **Description**

```
parameterKey

value

```

**Field Type**
ObjectiveParameterKey (enumeration of type string)

**Description**
Required. The scheduling objective parameter key. Possible values are:

**•** `DaysAhead`

**•** `DaysBack`

**Field Type**
string

**Description**
The scheduling objective parameter value.

Declarative Metadata Sample Definition

The following is an example of a `SchedulingObjective` component.

```
<?xml version="1.0" encoding="UTF-8"?>

<SchedulingObjective xmlns="http://soap.sforce.com/2006/04/metadata">

   <masterLabel>Balance Shifts</masterLabel>

   <schedulingCategory>B</schedulingCategory>

   <schedulingObjectiveType>BalanceShifts</schedulingObjectiveType>

   <schedulingObjectiveParameters>

```


### Metadata Types SchedulingRule

```
        <parameterKey>DaysAhead</parameterKey>

        <value>30</value>

      </schedulingObjectiveParameters>

   </SchedulingObjective>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <name>SchedulingObjective</name>

    <members>Balance Shifts</members>

      </types>

      <version>55.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### SchedulingRule

Represents a scheduling rule in Workforce Engagement Management. Scheduling rules determine when agents are assigned to shifts.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### SchedulingRule components have the suffix .schedulingRule and are stored in the SchedulingRules folder.

Version

### SchedulingRule components are available in API version 53.0 and later.

Special Access Rules

This type is available only if Workforce Engagement is enabled in your org. To view, create, edit, and delete records, the user requires
the Workforce Engagement Planner permission set.


Metadata Types SchedulingRule

Fields

**Field Name** **Description**

```
isProtected

masterLabel

schedulingCategory

schedulingRuleParameters

schedulingRuleType

```

**Field Type**
boolean

**Description**
Indicates whether the component is protected ( `true` ) or not ( `false` ). The default
value is `false` .

**Field Type**
string

**Description**
Required. The name of the rule.

**Field Type**
SchedulingCategory (enumeration of type string)

**Description**
Required. What the scheduling logic applies the rule to. The valid values are:

**•** `A` —Service Appointment

**•** `B` —Shift

**Field Type**

```
  SchedulingRuleParameter[] on page 1886

```

**Description**
Parameters associated with a scheduling rule, such as work limits.

**Field Type**
SchedulingRuleType (enumeration of type string)

**Description**
Required. Specifies the type of rule. The valid values are:

**•** `A` —Active Resources

**•** `B` —Match Skills

**•** `C` —Availability

**•** `M` —Match Territory

**•** `Q` —Match Queue

**•** `RestTimeMinutes` —Rest Time in Minutes. Available in API version 56.0 and
later.

**•** `W` —Work Limit

**•** `LimitNonstandardShifts` —Specifies a rule type that limits how many
non-standard shifts can be assigned to each agent. Available in API version 54.0
and later.


Metadata Types SchedulingRule

SchedulingRuleParameter

Represents a scheduling rule parameter, such as a work limit, that’s associated with a scheduling rule.

**Field Name** **Description**

```
schedulingParameterKey

value

```

**Field Type**
SchedulingParameterKey (enumeration of type string)

**Description**
Required. The scheduling rule parameter key.

**•** `C` —Constraint Field Name

**•** `L` —Limit Type

**•** `R` —Resolution

**•** `T` —Time Resolution

**•** `W` —Work Unit

**•** `ConsiderAbsence` —Consider resource absences when evaluating availability.
Available in API version 56.0 and later.

**•** `ConsiderSTM` —Consider service territory membership, which defines working
hours, when evaluating availability. Available in API version 56.0 and later.

**Field Type**
string

**Description**
The scheduling rule parameter value.

Declarative Metadata Sample Definition

The following is an example of a `SchedulingRule` component.

```
<?xml version="1.0" encoding="UTF-8"?>

<SchedulingRule xmlns="http://soap.sforce.com/2006/04/metadata">

   <masterLabel>Max Shifts Per Week</masterLabel>

   <schedulingCategory>B</schedulingCategory>

   <schedulingRuleParameters>

     <schedulingParameterKey>C</schedulingParameterKey>

     <value>MaxShiftsPerWeek</value>

   </schedulingRuleParameters>

   <schedulingRuleParameters>

     <schedulingParameterKey>W</schedulingParameterKey>

     <value>Shifts</value>

   </schedulingRuleParameters>

   <schedulingRuleParameters>

     <schedulingParameterKey>R</schedulingParameterKey>

     <value>Week</value>

   </schedulingRuleParameters>

   <schedulingRuleParameters>

     <schedulingParameterKey>L</schedulingParameterKey>

```


### Metadata Types Scontrol

```
        <value>Max</value>

      </schedulingRuleParameters>

      <schedulingRuleType>W</schedulingRuleType>

   </SchedulingRule>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <name>SchedulingRule</name>

    <members>MaxShiftsPerWeek</members>

      </types>

      <version>53.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### Scontrol

Deprecated. Represents an Scontrol component, corresponding to an s-control in the Salesforce user interface.

Important: Visualforce pages supersede s-controls. Organizations that haven't previously used s-controls can’t create them.
Existing s-controls are unaffected and can still be edited.

This type extends the MetadataWithContent metadata type and inherits its `content` and `fullName` fields.

Declarative Metadata File Suffix and Directory Location

### The file suffix is .scf for the s-control file. The accompanying metadata file is named ScontrolName -meta.xml . Scontrol components are stored in the scontrols folder in the corresponding package directory.

Version

### Scontrols are available in API version 10.0 and later.

Fields

This metadata type contains the following fields:

**Field Name** **Field Type** **Description**

`content` base64Binary Content of the s-control. Base 64-encoded binary data. Before making
an API call, client applications must encode the binary attachment

data as base64. Upon receiving a response, client applications must
decode the base64 data to binary. This conversion is handled for you


Metadata Types Scontrol

**Field Name** **Field Type** **Description**

by a SOAP client. This field is inherited from the MetadataWithContent
component.

`contentSource` SControlContentSource (enumeration Required. Determines how you plan to use the s-control:
of type string)

**•** `HTML` : Select this option if you want to enter the content for your
s-control in `content` .

**•** `URL` : Select this option if you want to enter the link or URL of an
external website in `content` .

**•** `Snippet` : Snippets are s-controls that are designed to be
included in other s-controls. Select this option if you want to enter
the content for your s-control snippet in `content` .

`description` string Optional text that describes the s-control. This only displays to users
with View All Data permission (administrator).

`encodingKey` Encoding (enumeration of type string) Required. The default encoding setting is Unicode: `UTF-8` . Change
it if you’re passing information to a URL that requires data in a different

format. This option is available when you select `URL` as the value for
`contentSource` .

`fileContent` base64 File contents displayed if you add this s-control to a custom link. The
file can contain a Java applet, Active-X control, or any other type of

content you want. This option only applies to s-controls with a value
of `HTML` for `contentSource` .

`fileName` string The unique name for the s-control. This name can contain only
underscores and alphanumeric characters, and must be unique in

your org. It must begin with a letter, not include spaces, not end with
an underscore, and not contain two consecutive underscores. This
field can’t be changed for components installed by a managed
package. It’s only relevant if the `fileContent` field also has a value.
This field is available in API version 14.0.

`fullName` string The s-control developer name used as a unique identifier for API access.
The `fullName` can contain only underscores and alphanumeric

characters. It must be unique, begin with a letter, not include spaces,
not end with an underscore, and not contain two consecutive
underscores. If this field contained characters before version 14.0 that
are no longer allowed, the characters were stripped out of this field,
and the previous value of the field was saved in the name field. This
field is inherited from the Metadata component.

`name` string

Required. The unique name for the s-control. It must contain
alphanumeric characters only and begin with a letter. For example
`example_s_control` .

`supportsCaching` boolean Required. Indicates whether the s-control supports caching ( `true` )
or not ( `false` ). Caching optimizes the page so that it remembers


### Metadata Types SearchCustomization

**Field Name** **Field Type** **Description**

which s-controls are on the page when it reloads. This option only
applies to HTML s-controls.

Declarative Metadata Sample Definition

The following sample creates the `Myriad_Publishing.scf` s-control, which creates a link to the website specified in the s-control.
The corresponding `Myriad_Publishing.scf-meta.xml` metadata file follows the s-control file.

`Myriad_Publishing.scf` file:

```
   http://www.myriadpubs.com

```

`Myriad_Publishing.scf-meta.xml` :

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Scontrol xmlns="http://soap.sforce.com/2006/04/metadata">

      <contentSource>URL</contentSource>

      <description>s-control to open Myriad Publishing website.</description>

      <encodingKey>UTF-8</encodingKey>

      <name>Myriad Publishing</name>

      <supportsCaching>true</supportsCaching>

   </Scontrol>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### SearchCustomization

Represents the configuration of search settings created in Search Manager. The configuration includes the search channel, searchable
objects and fields, and rules to filter search results.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### SearchCustomization components have the suffix .searchCustomization and are stored in the searchCustomizations

folder.


Metadata Types SearchCustomization

Version

SearchCustomization components are available in API version 61.0 and later.

Special Access Rules

Only users with the View Setup and Configuration permission can access this object, and only users with the Customize Application
permission can edit it.

Fields

**Field Name** **Description**

```
channel

masterLabel

objectOverride

objectToAlwaysSearch

profile

selectedObject

```

**Field Type**
string

**Description**

Required.

The search channel that the configuration applies to.

**Field Type**
string

**Description**

Required.

The name of the configuration.

**Field Type**

SearchCustomizationObjectOverride[]

**Description**
A list of object configurations.

**Field Type**
string[]

**Description**
A list of the objects that are always searched for the user profile if the search channel
is Einstein Global Search Bar.

**Field Type**
string

**Description**
Specifies user profile if the search channel is Einstein Global Search Bar.

**Field Type**
string[]


Metadata Types SearchCustomization

**Field Name** **Description**

**Description**
A list of the objects that are selected in the configuration if the search channel is LWR
Experience Sites.

```
selectedProfile

```

**Field Type**
string[]

**Description**
Specifies all user profiles that are associated with a Search configuration if the search
channel is Einstein Global Search Bar. This field is available in API version 62.0 and later.

SearchCustomizationObjectOverride

Represents the configuration for a specific object.

**Field Name** **Description**

```
fieldOverride

objectApiName

rule

searchable

```

**Field Type**

SearchCustomizationFieldOverride[]

**Description**
A list of field configurations.

**Field Type**
string

**Description**

Required.

The API name of the object that the configuration is applied to.

**Field Type**

SearchCustomizationRule[]

**Description**
A list of rules applied to filter search results.

**Field Type**
boolean

**Description**
Indicates whether the object is searchable ( `true` ) or not ( `false` ).

SearchCustomizationFieldOverride

Represents the configuration for a specific field within an object.


Metadata Types SearchCustomization

**Field Name** **Description**

```
fieldApiName

searchable

```

**Field Type**
string

**Description**

Required.

The API name of the field that the configuration is applied to.

**Field Type**
boolean

**Description**

Required.

Indicates whether the field is searchable ( `true` ) or not ( `false` ).

SearchCustomizationRule

Represents the rules defined in an object to filter search results.

**Field Name** **Description**

```
fieldApiName

operator

ruleValue

```

**Field Type**
string

**Description**

Required.

The field that the rule applies to.

**Field Type**
string

**Description**

Required.

The operator for the rule.

**Field Type**

SearchCustomizationRuleValue[]

**Description**
A list of rule values.

SearchCustomizationRuleValue

Represents the value of a rule used to filter search results.


Metadata Types SearchCustomization

**Field Name** **Description**

```
targetObjectApiName

value

```

**Field Type**
string

**Description**
The API name of the target object, in case the rule applies to a lookup field.

**Field Type**
string

**Description**

Required.

The value of the rule.

Declarative Metadata Sample Definition

The following is an example of a SearchCustomization component.

```
<?xml version="1.0" encoding="UTF-8"?>

<SearchCustomization xmlns="http://soap.sforce.com/2006/04/metadata">

   <channel>GlobalSearch</channel>

   <masterLabel>My_Standard_User_Configuration</masterLabel>

   <objectOverride>

     <fieldOverride>

        <fieldApiName>Description</fieldApiName>

        <searchable>false</searchable>

     </fieldOverride>

     <fieldOverride>

        <fieldApiName>Rating</fieldApiName>

        <searchable>true</searchable>

     </fieldOverride>

     <objectApiName>Account</objectApiName>

     <rule>

        <fieldApiName>My_Custom_Field__c</fieldApiName>

        <operator>ne</operator>

        <ruleValue>

          <value>Other</value>

        </ruleValue>

     </rule>

     <rule>

        <fieldApiName>Rating</fieldApiName>

        <operator>in</operator>

        <ruleValue>

          <value>Hot</value>

        </ruleValue>

        <ruleValue>

          <value>Warm</value>

        </ruleValue>

     </rule>

   </objectOverride>

   <objectOverride>

```


### Metadata Types SearchOrgWideObjectConfig

```
        <objectApiName>Asset</objectApiName>

        <searchable>false</searchable>

      </objectOverride>

      <objectOverride>

        <objectApiName>Contact</objectApiName>

        <rule>

           <fieldApiName>AccountId</fieldApiName>

           <operator>ne</operator>

           <ruleValue>

             <targetObjectApiName>Account</targetObjectApiName>

             <value>A Company</value>

           </ruleValue>

        </rule>

        <rule>

           <fieldApiName>DoNotCall</fieldApiName>

           <operator>eq</operator>

           <ruleValue>

             <value>false</value>

           </ruleValue>

        </rule>

      </objectOverride>

      <objectToAlwaysSearch>Account</objectToAlwaysSearch>

      <objectToAlwaysSearch>Contact</objectToAlwaysSearch>

      <objectToAlwaysSearch>My_Custom_Object__c</objectToAlwaysSearch>

      <objectToAlwaysSearch>Product2</objectToAlwaysSearch>

      <profile>standard</profile>

   </SearchCustomization>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>SearchCustomization</name>

      </types>

      <version>61.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### SearchOrgWideObjectConfig

Represents an object in the search index. The search index contains org-wide search settings created in Search Manager. Each object in
the search index includes searchable fields and fields protected by field-level security in search.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.


Metadata Types SearchOrgWideObjectConfig

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

SearchOrgWideObjectConfig components have the suffix `.searchOrgWideObjectConfig` and are stored in the
`searchOrgWideConfiguration` folder.

Version

SearchOrgWideObjectConfig components are available in API version 61.0 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Description**

```
masterLabel

objectReference

searchOrgWideFieldConfig

```

**Field Type**
string

**Description**

Required.

The name of the configuration.

**Field Type**
string

**Description**

Required.

The API name of the object.

**Field Type**

SearchOrgWideFieldConfig[]

**Description**
A list of field configurations.

SearchOrgWideFieldConfig

Represents the configuration in the search index for a field in an object.


Metadata Types SearchOrgWideObjectConfig

**Field Name** **Description**

```
fieldReference

isSearchable

isSecure

```

**Field Type**
string

**Description**

Required.

The API name of the field.

**Field Type**
boolean

**Description**
Indicates if the field is searchable ( `true` ) or not ( `false` ). If `true`, the field is shown
in search results and used to match results.

**Field Type**
boolean

**Description**
Indicates if the field is protected by field-level security in search ( `true` ) or not ( `false` ).
If `true`, the search engine uses this field to match results only for users with
permissions. If `false`, the search engine uses this field to match results even if the
user doesn’t have permissions to view this field.

Declarative Metadata Sample Definition

The following is an example of a SearchOrgWideObjectConfig component.

```
<?xml version="1.0" encoding="UTF-8"?>

<SearchOrgWideObjectConfig xmlns="http://soap.sforce.com/2006/04/metadata">

   <masterLabel>CustomerLabel</masterLabel>

   <objectReference>Customer</objectReference>

   <searchOrgWideFieldConfig>

     <fieldReference>Custom_Field_1__c</fieldReference>

     <isSearchable>false</isSearchable>

     <isSecure>false</isSecure>

   </searchOrgWideFieldConfig>

   <searchOrgWideFieldConfig>

     <fieldReference>Custom_Field_2__c</fieldReference>

     <isSearchable>true</isSearchable>

     <isSecure>true</isSecure>

   </searchOrgWideFieldConfig>

</SearchOrgWideObjectConfig>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>*</members>

```


### Metadata Types ServiceAISetupDefinition

```
        <name>SearchOrgWideObjectConfig</name>

      </types>

      <version>61.0</version>

   </Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The wildcard
applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the manifest
file, see Deploying and Retrieving Metadata with the Zip File.

### ServiceAISetupDefinition

Represents settings for an Einstein for Service feature such as Einstein Article Recommendations. This type extends the Metadata metadata
type and inherits its `fullName` field.

File Suffix and Directory Location

### ServiceAISetupDefinition components have the suffix .serviceAISetupDescription and are stored in the

`serviceAISetupDescriptions` folder.

Version

### ServiceAISetupDefinition components are available in API version 51.0 and later.

Special Access Rules

This type is available only when an org is configured to access the application in the `appSourceType` field. For example, if
`appSourceType` is set to ARTICLE_RECOMMENDATION, this type is available only if Einstein Article Recommendations is enabled
in the org and the Main Services Agreement has been accepted.

Fields

**Field Name** **Field Type** **Description**

```
appSourceType

```

ApplicationSourceType Required. The target application for the configuration. Valid values are:
(enumeration of

**•** `REPLY_RECOMMENDATION` —Einstein Reply Recommendations

type string)

**•** `REPLY_RECOMMENDATION` —Einstein Reply Recommendations

**•** `ARTICLE_RECOMMENDATION` —Einstein Article
Recommendations

**•** `UTTERANCE_RECOMMENDATION` —Einstein Bot utterances

**•** `FAQ` —Einstein Bot frequently asked questions

`name` string Required. A reference to the configuration.


### Metadata Types ServiceAISetupField

**Field Name** **Field Type** **Description**

```
setupStatus

```

ServiceAISetupDefStatus Required. The status of the configuration. Valid values are:
(enumeration of

**•** `FIELDS_SELECTED`

type string)

**•** `FIELDS_SELECTED`

**•** `TRAINING`

`supportedLanguages` string

**•** `READY_TO_ACTIVATE`

**•** `SERVING`

**•** `RETIRED`

**•** `ARCHIVED`

**•** `READY_FOR_REVIEW`

Required when `appSourceType` is
`ARTICLE_RECOMMENDATION` . Language codes for selected and
supported languages.

Declarative Metadata Sample Definition

Here’s an example of a ServiceAISetupDefinition component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ServiceAISetupDefinition xmlns="http://soap.sforce.com/2006/04/metadata">

   <appSourceType>ARTICLE_RECOMMENDATION</appSourceType>

   <name>SA1601228426202</name>

   <setupStatus>ARCHIVED</setupStatus>

   <supportedLanguages>en,de,fr,it,es,pt,nl</supportedLanguages>

</ServiceAISetupDefinition>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>*</members>

     <name>ServiceAISetupDefinition</name>

   </types>

</Package>

```

Usage

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### ServiceAISetupField

Represents a field on cases or knowledge articles that Einstein uses to identify relevant articles in Einstein Article Recommendations. This
type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types ServiceAISetupField

File Suffix and Directory Location

ServiceAISetupField components have the suffix `.serviceAiSetupField` and are stored in the `serviceAiSetupFields`
folder.

Version

ServiceAISetupField components are available in API version 51.0 and later.

Special Access Rules

This type is available only if Einstein Article Recommendations is enabled in your org and the Main Services Agreement has been accepted.

Fields

**Field Name** **Field Type** **Description**

`entity` string Required. The Case or KnowledgeArticle object for the field.

`field` string Required. The API name of the field.

```
fieldMappingType

```

ServiceAISetupFieldType Required. The field type. Valid values are:
(enumeration of

**•** `CASE_DESC`

type string)

**•** `CASE_SUBJ`

`fieldPosition` int

**•** `ARTICLE_TITLE`

**•** `ARTICLE_CONTENT`

**•** `ARTICLE_SUMMARY`

Required. A positive number used to rank the field’s importance. The
value 1 is most important; higher numbers indicate less important fields.
Einstein considers fields in the order of importance.

`name` string Required. A reference to the field.

`setupDefinition` string Required. A reference to the parent ServiceAISetupDefinition.

Declarative Metadata Sample Definition

The following is an example of a ServiceAISetupField component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ServiceAISetupField xmlns="http://soap.sforce.com/2006/04/metadata">

   <entity>Case</entity>

   <field>Subject</field>

   <fieldMappingType>CASE_SUBJ</fieldMappingType>

   <fieldPosition>1</fieldPosition>

   <name>SF16039900475920</name>

   <setupDefinition>4hQRM0000004CDK</setupDefinition>

</ServiceAISetupField>

```


### Metadata Types ServiceChannel

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ServiceAISetupField</name>

      </types>

   </Package>

```

Usage

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### ServiceChannel

Represents a channel of work items that are received from your organization—for example, cases, chats, or leads.

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ServiceChannel components have the suffix .serviceChannel and are stored in the serviceChannels folder.

Version

### ServiceChannel components are available in API version 44.0 and later.

Special Access Rules

This type is available only if Omni-Channel is enabled in your org.

Fields

**Field Name** **Field Type** **Description**

`acwExtensionDuration` int The maximum length of time, measured in seconds, an agent can spend
on After Conversation Work (ACW) each time they extend the timer. You

must set this field if `hasAcwExtensionEnabled` is set to `true` .
Specify a value from 10 through 3600. Available only for service channels
of type Messaging or Voice.

`afterConvoMaxTime` int The maximum length of time, measured in seconds, an agent has to
complete After Conversation Work (ACW). You must set this field if

`hasAfterConvoWorkTimer` is set to `true` . Specify a value from
10 through 3600. Available only for service channels of type Messaging
or Voice.


Metadata Types ServiceChannel

**Field Name** **Field Type** **Description**

For service channels of type Voice, this field is available in API version
52.0 and later. For service channels of type Messaging, this field is
available in API version 56.0 and later.

`capacityModel` picklist The method that determines when an agent's capacity for a work item
is released. With the status-based capacity routing model, work remains

assigned and applied to an agent’s capacity until the work is completed
or reassigned to a different agent. In contrast, the tab-based capacity
routing model releases an agent’s capacity when a work tab is closed in
the service console. This field is available in API version 65.0 and later.

Values are:

**•** `STATUS_BASED`

**•** `TAB_BASED`

`doesCheckCapOnOwnerChange` boolean Indicates whether the override for capacity check is on (true) or not
(false). If it is on, when work is reassigned to another agent it overrides

it and keeps the work assigned to the specific agent. The default value
is false.This field is available in API version 65.0 and later.

`doesCheckCapOnStatusChange` boolean Indicates whether the override for capacity check is on (true) or not
(false). If it is on, when work is reopened it is re-assigned to a specific

agent. The default value is false. This field is available in API version 65.0
and later.

`doesMinimizeWidgetOnAccept` boolean Automatically minimizes the Omni-Channel widget when an agent
accepts work. This field is available in API version 48.0 and later.

`hasAcwExtensionEnabled` Boolean If set to `true`, agents can extend their After Conversation Work (ACW)
time. Available only if `hasAfterConvoWorkTimer` is set to `true` .

If set to `true`, you must also set the `acwExtensionDuration`
and `maxExtensions` fields. The default value is `false` . Available
only for service channels of type Messaging or Voice. This field is available
in API version 56.0 and later.

`hasAfterConvoWorkTimer` Boolean If set to `true`, After Conversation Work (ACW) time can be configured
for the channel. If set to `true`, you must also set the

`afterConvoWorkMaxTime` field. The default value is `false` .
Available only for service channels of type Messaging or Voice.

For service channels of type Voice, this field is available in API version
52.0 and later. For service channels of type messaging, this field is
available in API version 56.0 and later.

`hasAutoAcceptEnabled` Boolean Work items in a service channel open automatically in the agent’s
workspace so that the agent doesn’t have to manually accept them.

`interactionComponent` string The custom console component to open in the footer when an agent
accepts a work item from this service channel.


Metadata Types ServiceChannel

**Field Name** **Field Type** **Description**

`isInterruptible` boolean

Indicates whether a work item consumes interruptible or primary
capacity. The default value is false. Available in API version 57.0 and later
when the Interruptible Capacity feature is enabled.

`label` string Required. The label of the service channel.

`maxExtensions` picklist The maximum number of times an agent can extend their After Work
Conversation (ACW) time. Specify a value from 1 through 10. You must

set this field if `hasAcwExtensionEnabled` is set to `true` .
Available only for service channels of type Messaging or Voice. This field
is available in API version 56.0 and later.

`relatedEntityType` string Required. The type of object that’s associated with this service channel.

`secondaryRoutingPriorityField` string

`serviceChannelStatusFieldMappings` ServiceChannelFieldPriority

The name of the standard field or the ID of the custom field that is used
for secondary routing priority. This field is available in API version 47.0
and later.

Represents the value to indicate completed and in-progress work item
status in the Status-Based Capacity routing model. This field is available
in API version 65.0 and later.

`serviceChannelFieldPriorities` ServiceChannelFieldPriority[] Required. A set of mappings between secondary routing priority field
values and priorities. This field is available in API version 47.0 and later.

`statusField` picklist The field that you use to track work status in the Status-Based capacity
routing model. Use `ServiceChannelStatusField` to specify

the values that indicate completed and in-progress work-item status.
This field is available in API version 65.0 and later.

ServiceChannelFieldPriority

Represents a secondary routing priority field value mapping. Available in API version 47.0 and later.

**Field Name** **Field Type** **Description**

`priority` int Required. The priority number assigned to the mapped field value.

`type` picklist Required. The work item status assigned to the mapped field value.
Possible types are `IN_PROGRESS`, `PAUSED`, `COMPLETED` .

`value` string Required. The value of Status Field defined in the parent ServiceChannel.

`value` string Required. The value of the secondaryRoutingPriorityField field defined
in the parent ServiceChannel.


### Metadata Types ServicePresenceStatus

Declarative Metadata Sample Definition

The following is an example of a ServiceChannel component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ServiceChannel xmlns="http://soap.sforce.com/2006/04/metadata">

      <doesMinimizeWidgetOnAccept>true</doesMinimizeWidgetOnAccept>

      <interactionComponent>ConsoleComponent</interactionComponent>

      <label>Case</label>

      <relatedEntityType>Case</relatedEntityType>

      <secondaryRoutingPriorityField>Status</secondaryRoutingPriorityField>

      <serviceChannelFieldPriorities>

        <priority>1</priority>

        <value>Escalated</value>

      </serviceChannelFieldPriorities>

      <serviceChannelFieldPriorities>

        <priority>2</priority>

        <value>On Hold</value>

      </serviceChannelFieldPriorities>

   </ServiceChannel>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ServiceChannel</name>

      </types>

      <version>44.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### ServicePresenceStatus

Represents a presence status that can be assigned to a service channel. This type extends the Metadata metadata type and inherits its
`fullName` field.

File Suffix and Directory Location

### ServicePresenceStatus components have the suffix .servicePresenceStatus and are stored in the

`servicePresenceStatuses` folder.

Version

### ServicePresenceStatus components are available in API version 44.0 and later.


Metadata Types ServicePresenceStatus

Special Access Rules

This type is available only if Omni-Channel is enabled in your org.

Fields

**Field Name** **Field Type** **Description**

`channels` ServiceChannelStatus Represents the status that’s associated with a specific service channel.

`label` string The label of the presence status.

ServiceChannelStatus

Represents the status that’s associated with a specific service channel.

**Field Name** **Field Type** **Description**

`channel` string Represents the channels assigned to the presence status.

Declarative Metadata Sample Definition

The following is an example of a ServicePresenceStatus component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ServicePresenceStatus xmlns="http://soap.sforce.com/2006/04/metadata">

      <channels>

        <channel>Case</channel>

      </channels>

      <label>Available for Cases</label>

   </ServicePresenceStatus>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ServicePresenceStatus</name>

      </types>

      <version>44.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types ServiceProcess ServiceProcess

Represents a process created in Service Process Studio and its associated attributes.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### ServiceProcess components have the suffix .serviceprocess and are stored in the .serviceprocess folder.

Version

### ServiceProcess components are available in API version 57.0 and later.

Special Access Rules

Access to the ServiceProcess type requires the AccessToServiceProcess permission.

Fields

**Field Name** **Description**

```
description

processLabel

serviceProcessAttributes

serviceProcessDependencies

```

**Field Type**
string

**Description**
A meaningful explanation of the service process.

**Field Type**
string

**Description**

Required.

A meaningful name for the service process.

**Field Type**
### ServiceProcessAttribute[]

**Description**
Custom attributes that store the data associated with the service process.

**Field Type**
### ServiceProcessDependency[]


Metadata Types ServiceProcess

**Field Name** **Description**

**Description**
Dependent components of the service process, such as OmniScripts or flows.

```
serviceProcessItemGroups

shortDescription

usageType

```

ServiceProcessAttribute

**Field Type**

ServiceProcessItemGroup[]

**Description**
Groups of related ServiceProcessAttribute records.

**Field Type**
string

**Description**
A brief meaningful explanation of the service process.

**Field Type**
SvcCatalogItemUsageType (enumeration of type string)

**Description**

Required.

The Cloud that uses this service process.

Values are:

**•** `CustomerService`

**•** `Employee`

**•** `FinancialServices`

**•** `Industry (available in version 58.0 and later)`

A custom attribute that stores data associated with a service process. For example, a service process that reverses a fee can have a Fee
Type attribute.

**Field Name** **Description**

```
attributeType

```

**Field Type**
SvcCtlgItemAttrAttributeType (enumeration of type string)

**Description**
A `Base` attribute corresponds to a SvcCatalogRequest field, which is subject to
field-level security. An `Extended` attribute is only a ServiceProcessAttribute object
record, which isn't subject to field-level security.

Values are:

**•** `Base`

**•** `Extended`


Metadata Types ServiceProcess

**Field Name** **Description**

The default is `Extended` .

```
dataType

```

**Field Type**
SvcCatalogItemAttrDataType (enumeration of type string)

**Description**
The data type of the attribute.

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


Metadata Types ServiceProcess

**Field Name** **Description**

The default is `Text` .

Note: Selecting `Currency` doesn't cause an error, but currency conversions
aren't supported.

```
description

developerName

fieldIdentifier

groupApiName

inputVariableValue

isRequired

label

```

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
string

**Description**
For a `Base` attribute, the Developer Name of the SvcCatalogRequest field. This field
can be standard or custom.

**Field Type**
string

**Description**
The `apiName` of the ServiceProcessItemGroup to which this attribute belongs.

**Field Type**
string

**Description**
The default value of the attribute.

**Field Type**
boolean

**Description**
Specifies whether the attribute is required. The default is `false` .

**Field Type**
string

**Description**

Required.

A meaningful name for the attribute.


Metadata Types ServiceProcess

**Field Name** **Description**

```
parentAttribute

sortOrder

```

**Field Type**
string

**Description**
The parent attribute of this attribute. For example, a Latitude attribute can have
GeoLocation as a parent.

**Field Type**
int

**Description**
The position of the attribute in the payload relative to other attributes having no parent
or the same parent.

ServiceProcessDependency

A dependent component of the service process, which can be a flow, an OmniScript, an Integration Definition, or a preprocessor Apex
class.

**Field Name** **Description**

```
dependencyReference

processStepName

type

```

**Field Type**
string

**Description**

Required.

The Developer Name of the flow, OmniScript, Integration Definition, or preprocessor
Apex class.

**Field Type**
SvcCtlgItemDpndProcType (enumeration of type string)

**Description**
Name of the step in a service process.

Values are:

**•** `FulfillmentFlow`

**•** `IntegrationDefinition`

**•** `Preprocessor`

**•** `RequestForm`

**Field Type**
SvcCatalogItemDependencyType (enumeration of type string)

**Description**

Required.


Metadata Types ServiceProcess

**Field Name** **Description**

The type of dependent component.

Values are:

**•** `FlowDefinition`

**•** `IntegrationProviderDef`

**•** `OmniScriptConfig`

**•** `PreprocessorApexClass`

ServiceProcessItemGroup

A group of related ServiceProcessAttribute records.

**Field Name** **Description**

```
apiName

groupName

sortOrder

```

**Field Type**
string

**Description**

Required.

The API Name of the group.

**Field Type**
string

**Description**

Required.

The name of the group.

**Field Type**
int

**Description**

Required.

The group display order.

Declarative Metadata Sample Definition

The following is an example of a ServiceProcess component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ServiceProcess xmlns="http://soap.sforce.com/2006/04/metadata">

  <processLabel>EmailUpdate</processLabel>

  <usageType>FinancialServices</usageType>

  <serviceProcessAttributes>

    <label>EmailAddress</label>

```


Metadata Types ServiceProcess

```
       <developerName>EmailAddress</developerName>

       <dataType>Text</dataType>

       <groupApiName>Info</groupApiName>

     </serviceProcessAttributes>

     <serviceProcessDependencies>

       <dependencyReference>EmailPreprocessor</dependencyReference>

       <type>PreprocessorApexClass</type>

     </serviceProcessDependencies>

     <serviceProcessItemGroups>

        <apiName>Info</apiName>

        <groupName>Info</groupName>

        <sortOrder>1</sortOrder>

      </serviceProcessItemGroups>

   </ServiceProcess>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>ServiceProcess</name>

      </types>

      <version>57.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

Usage Type

We recommend that you review these considerations before you retrieve or deploy service process metadata.

**•** If you deploy metadata with the same name as the definition when your service process definition is active, you get an error message.
Deactivate the service process definition and try again.

**•** When your service process definition is inactive, consider these guidelines.

**–** If a service process definition contains service catalog requests and service catalog request extended attribute values and you
deploy metadata with the same name as the definition, you get an error message. You can’t delete or change a service process
that has service catalog requests with attribute values in it. Make sure that all records are deleted in service catalog requests and
service catalog request extended attribute values before you deploy the metadata.

**–** If a service process definition contains service catalog requests but doesn’t contain service catalog request extended attribute
values and you deploy the metadata with the same name, the deployment works as expected.

**–** If a service process definition doesn’t contain service catalog requests and you deploy the metadata with the same name, the
deployment works as expected.


### Metadata Types Settings Settings

Represents the organization settings related to a feature. For example, your password policies, session settings and network access
controls are all available in the SecuritySettings component type.

Not all feature settings are available in the Metadata API. See Unsupported Metadata Types on page 170 for information on which feature
settings are not available.

### Settings can be accessed using the specific component member or via wildcard. For example, in the package manifest file you would

use the following section to access SecuritySettings:

```
      <types>

        <members>Security</members>

        <name>Settings</name>

      </types>

```

The member format when used in the package manifest is the component metadata type name without the “Settings” suffix, so in the
preceding example “Security” is used instead of “SecuritySettings”.

File Suffix and Directory Location

Each settings component gets stored in a single file in the `settings` directory of the corresponding package directory. The filename
uses the format _`Setting feature`_ `.settings` . For example, the SecuritySettings file would be `Security.settings` . See
“File Suffix and Directory Location” information for the individual settings components to determine the exact filename.

Version

### Settings is available in API version 27.0 and later. See the version information for the individual setting component to determine which

API version the settings component became available.

Declarative Metadata Sample Definition

The following is an example package manifest used to deploy or retrieve only the MobileSettings for an organization:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Mobile</members>

        <name>Settings</name>

      </types>

      <version>27.0</version>

   </Package>

```

The following is an example package manifest used to deploy or retrieve all the available settings metadata for an organization, using
a wildcard:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>Settings</name>

      </types>

```


Metadata Types Settings

```
      <version>27.0</version>

   </Package>

```

AccountPlanSettings
Represents an org’s account plan settings. These settings control features that make it easy for sales reps to set objectives with
actionable metrics and to store account research and analysis.

AccountSettings
Represents an org’s account settings for account teams, account owner report, and the **View Hierarchy** link.

AccountInsightsSettings
Represents an org’s Einstein Account Insights settings. This setting controls features that help your reps maintain their relationships
with their customers.

AccountIntelligenceSettings
Represents an org’s Account Intelligence settings. These settings control features that make it easy for sales reps to create accounts,
see relevant news articles, and add logos to account records. This type extends the Metadata metadata type and inherits its
`fullName` field.

AccountingSettings
Represents the settings for the Accounting Subledger feature.

ActionsSettings
Represents an org’s actions settings for default quick actions, multi-dimensional publisher, and third-party actions. This type extends
the Metadata metadata type and inherits its `fullName` field.

ActivitiesSettings
Represents an org's activity settings, and its user interface settings for the calendar. This type extends the Metadata metadata type
and inherits its `fullName` field.

AddressSettings
Represents the configuration of country/territory and state picklists. Use the AddressSettings component type to configure state
and country/territory data in your organization so that you can convert text-based values into standard picklist values. To convert
your state and country/territory values, from Setup, enter _`State and Country/Territory Picklists`_ in the Quick
Find box, then select **State and Country/Territory Picklists** .

AIReplyRecommendationsSettings
Represents the metadata used to manage settings for Einstein Reply Recommendations. This type extends the Metadata metadata
type and inherits its `fullName` field.

AgentPlatformSettings
Represents settings for Agentforce.

AgentforceForDevelopersSettings
Represents Agentforce for Developers settings.

AnalyticsSettings
Represents Analytics settings in Salesforce. CRM Analytics lets you explore all your data quickly and easily by providing AI-powered
advanced Analytics right inside Salesforce. Manage your datasets, query data with Salesforce Analytics Query Language (SAQL), and
customize dashboards. You can use these settings to configure which Analytics features are available to users in your organization.

ApexSettings
Represents Apex-related org settings. This type extends the Metadata metadata type and inherits its `fullName` field.

AppAnalyticsSettings
Represents settings to retrieve AppExchange App Analytics usage data.


Metadata Types Settings

AppExperienceSettings
Represents settings for the app experience.This type extends the Metadata metadata type and inherits its `fullName` field.

AssociationEngineSettings
Represents the record association builder settings for an org. This type extends the Metadata metadata type and inherits its
`fullName` field.

AutomatedContactsSettings
Represents an org’s Einstein Automated Contacts settings. These settings let you find new contacts and opportunity contact roles.
This type extends the Metadata metadata type and inherits its `fullName` field.

BotSettings
Represents an organization’s Einstein Bot settings, such as whether or not Einstein Bots is enabled. This type extends the Metadata
metadata type and inherits its `fullName` field.

BranchManagementSettings
Represents the branch management settings for an org. This type extends the Metadata metadata type and inherits its `fullName`
field.

BusinessHoursSettings
Represents the metadata used to manage settings for business hours and holidays in entitlements, entitlement templates, campaigns,
and cases. This type extends the Metadata metadata type and inherits its `fullName` field.

CampaignSettings
Represents an org’s Campaign Influence, Einstein Attribution, Einstein Key Accounts, and campaign member settings. These features
help you understand how your campaigns and accounts are affecting your opportunity pipeline.

CaseSettings
Represents an organization’s case settings, such as the default case owner, which case-related features are enabled, and which
Classic email templates are used for various case activities. This type extends the Metadata metadata type and inherits its `fullName`
field.

ChatterAnswersSettings
Represents the metadata used to manage settings for Chatter Answers.

ChatterEmailsMDSettings
Represents an org’s settings for Chatter email when Chatter is enabled. This type extends the Metadata metadata type and inherits
its `fullName` field.

ChatterSettings
Represents an org’s settings for their Chatter instance when Chatter is enabled for the org. This type extends the Metadata metadata
type and inherits its `fullName` field.

CodeBuilderSettings
Represents Code Builder settings. This type extends the Metadata metadata type and inherits its `fullName` field.

CollectionsDashboardSettings
Represents an org’s settings to add the Collections Dashboard application to an org.

CommunitiesSettings
Represents community settings for an org. Enable digital experiences and workspaces. Manage moderation, guest user and partner
settings, and more. This type extends the Metadata metadata type and inherits its `fullName` field.

CompanySettings
Represents global settings that affect multiple features in your organization. This type extends the Metadata metadata type and
inherits its `fullName` field.


Metadata Types Settings

ConnectedAppSettings
Represents settings for connected apps. This type extends the Metadata metadata type and inherits its `fullName` field.

ContentSettings
Represents content settings for an org. This type extends the Metadata metadata type and inherits its `fullName` field.

ContractSettings
Represents contract settings.

ConversationalIntelligenceSettings
Represents the org's Einstein Conversation Insights settings, such as whether Einstein Conversation Insights is enabled. Einstein
Conversation Insights lets you analyze your rep's call recordings, and gives you the insights you need to optimize every call.

ConversationChannelDefinition
Represents the conversation channel definition that’s implemented for Interaction Service for Bring Your Own Channel for Messaging
and Bring Your Own Channel for CCaaS messaging channels. This object is available in API version 60.0 and later.

CurrencySettings
Represents an organization’s currency settings, including supporting multiple currencies and currency effective dates. This type
extends the Metadata metadata type and inherits its `fullName` field.

CustomAddressFieldSettings
Represents the settings for custom address fields.

DataDotComSettings
Represents the org's Data.com settings. This type extends the Metadata metadata type and inherits its `fullName` field.

DataImportManagementSettings
Represents an org's contact and leads import settings.

DeploymentSettings
Represents the settings affecting how deployments behave in the org. This type extends the Metadata metadata type and inherits
its `fullName` field.

DevHubSettings
Represents Dev Hub settings.

DocumentGenerationSetting
Represents an org's settings for automatic document generation from templates. This type extends the Metadata metadata type
and inherits its `fullName` field.

DynamicFormsSettings
Represents the settings related to Dynamic Forms.

EACSettings
Represents the Einstein Activity Capture metadata type. Use Einstein Activity Capture to add emails and events from your Microsoft
or Google account to the activity timeline of related Salesforce records. Automatically sync contact and event data between your
Microsoft or Google account and Salesforce. This type extends the Metadata metadata type and inherits its `fullName` field.

EinsteinAISettings
Represents Einstein AI settings, including AI feedback integration with Data 360 and PII masking for AI trust features.

EinsteinAgentSettings
Represents settings for Einstein classification apps, Einstein Case Classification and Einstein Case Wrap-Up, in an org. This type
extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types Settings

EinsteinGptSettings
Represents settings for Einstein Generative AI features in an org. This type extends the Metadata metadata type and inherits its
`fullName` field

EmailAdministrationSettings
Represents an organization’s email administration settings, including email deliverability, security compliance, relay configurations,
and system notifications. This type extends the Metadata metadata type and inherits its `fullName` field.

EmailIntegrationSettings
Represents an org’s settings for the Outlook integration, Gmail integration, and Salesforce Inbox. This type extends the Metadata
metadata type and inherits its `fullName` field.

EmailTemplateSettings
Represents an org’s email template settings. This type extends the Metadata metadata type and inherits its `fullName` field.

EmployeeUserSettings
Represents the employee-user settings used for automatically creating or syncing employee and user data in work.com orgs. This
type extends the Metadata metadata type and inherits its `fullName` field.

EnhancedNotesSettings
Represents an org’s enhanced note settings, such as enabling enhanced notes and enabling tasks in enhanced notes.This type
extends the Metadata metadata type and inherits its `fullName` field.

EncryptionKeySettings
Represents an org’s encryption key settings, such as customer-supplied keys options and key derivation settings. This type extends
the Metadata metadata type and inherits its `fullName` field.

EntitlementSettings
Represents an organization’s entitlement settings.

EventSettings
Represents an org's platform event settings for Event Monitoring.

ExperienceBundleSettings
Represents the org setting that enables the ExperienceBundle metadata type for Aura sites in Experience Cloud. The setting doesn’t
affect LWR sites, which use ExperienceBundle by default. This type extends the Metadata metadata type and inherits its `fullName`
field.

ExternalClientAppSettings
Represents settings to enable the External Client App feature and provide access to the OAuth consumer secret.

ExternalServicesSettings
Represents settings for an External Services registration.

FieldServiceSettings
Represents an organization’s Field Service settings.

FilesConnectSettings
Represents the settings that modify the Files Connect feature.This type extends the Metadata metadata type and inherits its
`fullName` field.

FileUploadAndDownloadSecuritySettings
Represents the security settings for uploading and downloading files. This type extends the Metadata metadata type and inherits
its `fullName` field.

FlowSettings
Represents the Salesforce settings for processes and flows, such as whether Lightning runtime for flows is enabled.


Metadata Types Settings

ForecastingObjectListSettings
Represents an org’s forecasting object list settings. Use these settings to control which object types and field types appear in the list
of object details on the forecasts page. For example, pipeline forecasts use the Opportunity object, and the object list settings specify
which fields from that object are available in the opportunity list section of the forecasts page. This type extends the Metadata
metadata type and inherits its `fullName` field.

ForecastingSettings
Represents the Forecasts settings options. This type extends the Metadata metadata type and inherits its `fullName` field.

HighVelocitySalesSettings
Represents an org’s Sales Engagement settings. With Sales Engagement, you can make your inside sales team as effective as possible.

IdeasSettings
Represents the metadata used to manage settings for Ideas.

IdentityProviderSettings
Represents the settings used to enable or disable Salesforce as a SAML identity provider for single sign-on (SSO).

IframeWhiteListUrlSettings
Represents settings related to the list of trusted external domains that you allow to frame your Visualforce pages or surveys. This
type extends the Metadata metadata type and inherits its `fullName` field.

IncidentMgmtSettings
Represents settings for Customer Service Incident Management and Broadcast Communications.

IndustriesEinsteinFeatureSettings
Represents the settings for enabling the Industries Einstein feature.

IndustriesLoyaltySettings
Represents the settings to enable capabilities of Loyalty Management.

IndustriesSettings
Represents settings for industries verticals such as Financial Services Cloud, Consumer Goods Cloud, Public Sector Solutions, Education
Cloud, Salesforce Scheduler, Life Sciences Cloud, and Health Cloud.

InterestTaggingSettings
Represents settings for Interest Tags, which your users can add to client records to capture client needs, interests, and prospecting
opportunities.

InventorySettings
Represents options for the Salesforce Omnichannel Inventory product.This type extends the Metadata metadata type and inherits
its `fullName` field.

InvLatePymntRiskCalcSettings
Represents the org’s settings to identify the level of risks associated with payment of invoices.

InvocableActionSettings
Represents the org’s invocable action settings, such as whether partial save is allowed.This type extends the Metadata metadata
type and inherits its `fullName` field.

KnowledgeSettings
Represents the metadata used to manage settings for Salesforce Knowledge.

LanguageSettings
Represents an organization’s language settings. Language settings control end-user language selection, locale formats, and translation
options. This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types Settings

LeadConfigSettings
Represents configuration settings for Leads that control how they are converted and displayed, and what actions are available. This
type extends the Metadata metadata type and inherits its `fullName` field.

LeadConvertSettings
Represents an organization’s custom field mappings for lead conversion. Custom fields can be mapped from Leads to Accounts,
Contacts, and Opportunities. Options for creating opportunities during lead conversion can also be specified. This type extends the
Metadata metadata type and inherits its `fullName` field.

LiveAgentSettings
Represents an organization’s Chat settings, such as whether Chat is enabled. This type extends the Metadata metadata type and
inherits its `fullName` field.

LightningExperienceSettings
Represents the settings that modify an org’s Lightning Experience configuration. This type extends the Metadata metadata type and
inherits its `fullName` field.

LiveMessageSettings
Represents an org’s LiveMessage settings.

MacroSettings
