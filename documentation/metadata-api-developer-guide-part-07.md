#### OrderSettings components are available in API version 30.0 and later.


Metadata Types OrderSettings

Fields

**Field Name** **Field Type** **Description**

`enableEnhancedCommerceOrders` boolean Indicates whether enhanced commerce orders are enabled for the org
( `true` ) or not ( `false` ). This preference is available only in orgs with

the Salesforce Order Management license. Default value is `false.`
Available in API versions 48.0 and later.

`enableNegativeQuantity` boolean

`enableOptionalPricebook` boolean

`enableOrderEvents` boolean

Indicates whether users in the org can add order products with quantities
of less than zero ( `true` ) or not ( `false` ).

To enable this preference, `enableOrders` must be set to `true` .

Indicates whether users in the org can create orders without price books
( `true` ) or not ( `false` [). For more information, see Enable Orders](https://help.salesforce.com/s/articleView?id=sales.customize_order_enable_without_pricebooks.htm&type=5&language=en_US)
[Without Price Books in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sales.customize_order_enable_without_pricebooks.htm&type=5&language=en_US)

Indicates whether order events are enabled for the org ( `true` ) or not
`(false)` . For more information, see OrderStatusChangedEvent in the
[Platform Events Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_intro.htm)

`enableOrders` boolean Indicates whether orders are enabled for the org ( `true` ) or not ( `false` ).

`enableOrderWithMultiplePriceBooks` boolean

`enableReductionOrders` boolean

`enableZeroQuantity` boolean

Indicates whether users in the org can create orders containing order
items that refer to multiple price books ( `true` ) or not ( `false` ). Available
in API version 60.0 and later.

To enable this preference, `enableOrders` and
`enableEnhancedCommerceOrders` must be set to `true` .

This field helps to offer different pricing structures for various customer
segments, regions, or promotional periods.

Indicates whether reduction orders are enabled for the org ( `true` ) or
not ( `false` [). For more information, see Reduction Orders in Salesforce](https://help.salesforce.com/s/articleView?id=sales.orderreduction_overview.htm&type=5&language=en_US)
Help.

To enable this preference, `enableOrders` must be set to `true` .

Indicates whether users in the org can add order products with quantities
of zero ( `true` ) or not ( `false` ). Default value is `false` .

To enable this preference, `enableOrders` must be set to `true` .

Available in API version 42.0 and later.

Declarative Metadata Sample Definition

This is a sample OrderSettings component.

```
<?xml version="1.0" encoding="UTF-8"?>

<OrderSettings xmlns="http://soap.sforce.com/2006/04/metadata">

   <enableNegativeQuantity>false</enableNegativeQuantity>

   <enableZeroQuantity>false</enableZeroQuantity>

```


#### Metadata Types OrgPreferenceSettings

```
      <enableOrders>true</enableOrders>

      <enableReductionOrders>true</enableReductionOrders>

      <enableEnhancedCommerceOrders>true</enableEnhancedCommerceOrders>

      <enableOptionalPricebook>false</enableOptionalPricebook>

      <enableOrderEvents>false</enableOrderEvents>

      <enableOrderWithMultiplePriceBooks>false</enableOrderWithMultiplePriceBooks>

   </OrderSettings>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Order</members>

        <name>Settings</name>

      </types>

      <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### OrgPreferenceSettings

Removed in API version 48.0. Represents the unique org preference settings in a Salesforce org.

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

#### OrgPreferenceSettings values are stored in the OrgPreference.settings file in the settings directory. The .settings files

are different from other named components because there is only one settings file for each settings component.

Version

#### OrgPreferenceSettings components are available in API versions 37.0 to 47.0. OrgPreferenceSettings is deprecated in API version 47.0 and removed in API version 48.0. In API version 47.0, most of the settings

supported in the `preferences` field were made available in the form of Boolean fields on other Settings types. For example, in API
version 47.0 and later, you can enable and disable the `CompileOnDeploy` preference by using the `enableCompileOnDeploy`
field on the ApexSettings type.

Fields

**Field Name** **Field Type** **Description**

`preferences` OrganizationSettingsDetail[] The preferences associated with the org settings. In the following list of
preferences, click hyperlinked preference names to go to the topic for


Metadata Types OrgPreferenceSettings

**Field Name** **Field Type** **Description**

the Settings type that contains that preference. If there is no link, the
preference hasn’t been moved to another Settings type.

**•** `AnalyticsSharingEnable` (available in API version 40.0 and
later)

**•** `ApexApprovalLockUnlock`

**•** `AsyncSaveEnabled` (available in API versions 40.0 to 46.0)

**•** `ChatterEnabled`

**•** `CompileOnDeploy` (available in API version 43.0 and later)

**•** `ConsentManagementEnabled` (available in API version 45.0
and later)

**•** `EnhancedEmailEnabled`

**•** `EventLogWaveIntegEnabled`

**•** `LoginForensicsEnabled`

**•** `NetworksEnabled` (available in API version 40.0 and later)

**•** `NotesReservedPref01`

**•** `OfflineDraftsEnabled`

**•** `PathAssistantsEnabled`

**•** `S1DesktopEnabled`

Note: After it is enabled, `S1DesktopEnabled` can’t be
disabled in any version of the API.

**•** `S1EncryptedStoragePref2`

**•** `S1OfflinePref`

**•** `ScratchOrgManagementPref on page 2029` (available
in API version 41.0 and later)

**•** `SendThroughGmailPref`

**•** `SocialProfilesEnable`

**•** `Translation` (available in API version 40.0 and later)

**•** `VoiceEnabled`

Note: The `VoiceEnabled` preference isn’t being moved
to another metadata type. If you want to use it in a scratch
org in API version 48.0 and later, you can enable it as a scratch
org feature.

OrganizationSettingsDetail

**Field Name** **Field Type** **Description**

`settingName` string The name of the setting. For example,
“S1EncryptedStoragePref2.”


#### Metadata Types OrgSettings

**Field Name** **Field Type** **Description**

`settingValue` boolean Indicates whether the setting is enabled
( `true` ) or not ( `false` ).

Declarative Metadata Sample Definition

The following is an example of a OrgPreferenceSettings component. The example shows only the `preferences` values that are
supported but not yet available as fields on another Settings type in API version 47.0.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <OrgPreferenceSettings xmlns="http://soap.sforce.com/2006/04/metadata">

      <preferences>

        <settingName>AnalyticsSharingEnable</settingName>

        <settingValue>true</settingValue>

      </preferences>

      <preferences>

        <settingName>NetworksEnabled</settingName>

        <settingValue>true</settingValue>

      </preferences>

      <preferences>

        <settingName>NotesReservedPref01</settingName>

        <settingValue>false</settingValue>

      </preferences>

      <preferences>

        <settingName>ScratchOrgManagementPref</settingName>

        <settingValue>true</settingValue>

      </preferences>

      <preferences>

        <settingName>VoiceEnabled</settingName>

        <settingValue>false</settingValue>

      </preferences>

   </OrgPreferenceSettings>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### OrgSettings

Represents the settings for org-wide functionality that isn’t associated with any specific feature.This type extends the Metadata metadata
type and inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.

File Suffix and Directory Location

A OrgSettings component file has the suffix `.settings` and is stored in the `settings` directory. The `.settings` files are
different from other named components because there’s only one settings file for each settings component.


Metadata Types OrgSettings

Version

OrgSettings components are available in API version 46.0 and later.

Before API version 51.0, the fields `enableExtendedMailMerge` and `saveMailMergeDocsAsSalesforceDocs` were
found within OrgSettings components. In API version 51.0 and later, those fields are found within MailMergeSettings on page 2161.

Fields

**Field Name** **Field Type** **Descriptions**

`enableCustomerSuccessPortal` boolean Indicates whether Customer Portal is enabled ( `true` ) or not ( `false` ).

`enableManageSelfServiceUsers` boolean Indicates whether mass management of self-service users is enabled
through the Self-Service Portal ( `true` ) or not ( `false` ).

`enableOrgFeedSentimentAnalysis` boolean Indicates whether feed sentiment analysis is enabled for the org ( `true` )
or not ( `false` ).

Declarative Metadata Sample Definition

The following is an example of a OrgSettings component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <OrgSettings xmlns="http://soap.sforce.com/2006/04/metadata"

   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

      <enableCustomerSuccessPortal>false</enableCustomerSuccessPortal>

      <enableMakeDeploymentsMandatory>true</enableMakeDeploymentsMandatory>

      <enableManageSelfServiceUsers>false</enableManageSelfServiceUsers>

      <enableOrgFeedSentimentAnalysis>false</enableOrgFeedSentimentAnalysis>

      <enableRADeploymentAttributeOnly>true</enableRADeploymentAttributeOnly>

      <enableResetDivisionOnLogin xsi:nil="true"/>

   </OrgSettings>

```

Example Package Manifest

The following is an example package manifest used to deploy or retrieve the org settings metadata for an organization:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Org</members>

        <name>Settings</name>

      </types>

      <version>47.0</version>

   </Package>

```


#### Metadata Types PartyDataModelSettings

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### PartyDataModelSettings

Represents an organization’s party data model settings, including options around the Individual object and consent enablement. This
type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.

File Suffix and Directory Location

#### PartyDataModelSettings values are stored in the PartyDataModel.settings file in the settings directory. The .settings

files are different from other named components because there’s only one settings file for each settings component.

Version

#### PartyDataModelSettings is available in API version 47.0 and later.

Fields

**Field Name** **Field Type** **Description**

`enableAutoSelectIndividualOnMerge` boolean Indicates whether the most recently modified data privacy record for
the Individual is retained when merging lead, contact, and person

accounts ( `true` ) or users must manually determine which data privacy
record to retain during the merge process ( `false` ). This field has a
default value of `false` .

`enableConsentManagement` boolean Indicates whether data protection details are available in records ( `true` )
or not ( `false` ). This has a default value of `true` .

Note: Setting this field to `false` purges all data protection
details, such as privacy preferences and stored consent forms.

`enableIndividualAutoCreate` boolean Deprecated in API version 48.0 and removed in API version 49.0 and
later.

Declarative Metadata Sample Definition

The following is an example of a PartyDataModelSettings component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <PartyDataModelSettings xmlns="http://soap.sforce.com/2006/04/metadata">

      <enableAutoSelectIndividualOnMerge>true</enableAutoSelectIndividualOnMerge>

      <enableConsentManagementEnabled>true</enableConsentManagementEnabled>

   </PartyDataModelSettings>

```


#### Metadata Types PardotSettings

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>PartyDataModel</members>

        <name>Settings</name>

      </types>

      <version>47.0</version>

   </Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### PardotSettings

Represents Marketing Cloud Account Engagement settings in your Salesforce org. Account Engagement, formerly known as Pardot, is
a B2B marketing automation solution that helps you create meaningful connections, generate more pipeline, and close more deals. Use
these settings to configure how Account Engagement collects and displays data.

This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.

File Suffix and Directory Location

This object is stored in a file named `Pardot.Settings` in the `settings` folder of the corresponding package directory. The
`.settings` files are different from other named components because there’s only one settings file for each settings component.

Version

#### PardotSettings is available in API version 47.0 and later.

Special Access Rules

This metadata type is available only to orgs with Account Engagement.

Fields

**Field Name** **Field Type** **Description**

`cdpEnablementStatus` string The status of the enablement in Data 360 for the account engagement
business unit.

`enableAeDataConnector` boolean Enable the Account Engagement Data 360 Connector for creating
Account Engagement Data Streams.


Metadata Types PardotSettings

**Field Name** **Field Type** **Description**

`enableAIOptimizedSendTime` boolean Enable Einstein Send Time Optimization for sending Account
Engagement emails.

`enableB2bmaAppEnabled` boolean Deprecated.

`enableEngagementHistoryDashboards` boolean Enable the Engagement History Dashboard and allow related Account
Engagement data to be shared to campaign records in Salesforce by

setting this value to `true` . The default value is `false` . If
`enableEnagementHistoryDashboards` is disabled after being
enabled, the Engagement History Dashboard is removed, but
engagement data continues to be retained and updated.

`enableEnhancedProspectCustomFieldsSync` boolean

Enable Object Sync to enhance with B2B Marketing Analytics or B2B
Marketing Analytics Plus by setting this property to `true` . The default
value is `false` . Available in API version 52.0 and later.

`enablePardotAppV1Enabled` boolean Enable the Account Engagement Lightning App by setting this property
to `true` . The default value is `false` .

`enablePardotEnabled` boolean Deprecated.

`enablePardotObjectSync` boolean Deprecated.

`enableProspectActivityDataset` boolean Enable the Prospect and Activity Dataset for B2B Marketing Automation
apps by setting this property to `true` . When

`enableProspectActivityDataset` is `true`, the datasets
take some time to populate. Depending on how much data and the
type of licenses you have, enabling this preference can impact the
account’s row limit for Analytics.

If `enableProspectActivityDataset` is disabled after being
enabled:

**•** The data that makes up the datasets is deleted.

**•** The Prospect and Activity Dataset in existing B2B Marketing
Automation apps stops getting updates.

**•** The dataset isn’t available to add to new apps.

**•** When apps are reconfigured, the dataset is deleted.

Requires that `enableEnagementHistoryDashboards` is set
to `true` .

`PardotEngageFreqSetting` boolean Enable Einstein Engagement Frequency for sending Account
Engagement emails.

Declarative Metadata Sample Definition

The following is an example of a PardotSettings component.

```
1 <?xml version="1.0" encoding="UTF-8"?>

2 <PardotSettings xmlns="http://soap.sforce.com/2006/04/metadata">

3 <enablePardotEnabled>true</enablePardotEnabled>

```


#### Metadata Types PardotEinsteinSettings

```
   4 <enablePardotAppV1Enabled>true</enablePardotAppV1Enabled>

   5 <enableB2bmaAppEnabled>true</enableB2bmaAppEnabled>

   6 <enableEngagementHistoryDashboards>true</enableEngagementHistoryDashboards>

   7 <enableEnhancedProspectCustomFieldsSync>true</enableEnhancedProspectCustomFieldsSync>

   8 <enablePardotObjectSync>true</enablePardotObjectSync>

   9 <enableProspectActivityDataset>true</enableProspectActivityDataset>

   10 <enableAIOptimizedSendTime>true</enableAIOptimizedSendTime>

   11 </PardotSettings>

```

The following is an example `package.xml` that references the previous definition.

```
   1 <?xml version="1.0" encoding="UTF-8"?>

   2 <Package xmlns="http://soap.sforce.com/2006/04/metadata">

   3 <types>

   4 <members>Pardot</members>

   5 <name>Settings</name>

   6 </types>

   7 <version>47</version>

   8 </Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### PardotEinsteinSettings

Represents PardotEinsteinSettings. Use these settings to learn what factors drive your campaign performance, and get the best possible
engagement score for your prospects. This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.

File Suffix and Directory Location

#### PardotEinsteinSettings values are stored in the PardotEinstein.settings file in the settings folder. The .settings

files are different from other named components because there’s only one settings file for each settings component.

Version

#### PardotEinsteinSettings is available in API versions 48.0 and later.

Fields

**Field Name** **Field Type** **Description**

`enableCampaignInsight` boolean

Indicates whether Einstein Campaign Insights is enabled ( `true` ) or not
( `false` ). Einstein Campaign Insights helps you understand what factors
drive campaign performance.

The default value is `false` .


#### Metadata Types PathAssistantSettings

**Field Name** **Field Type** **Description**

`enableEngagementScore` boolean Indicates whether Einstein Behavior Scoring is enabled ( `true` ) or not
( `false` ). Einstein Behavior Scoring identifies prospects whose behavior

suggests that they are ready to buy, and scores them based on Einstein’s
engagement model.

The default value is `false` .

Declarative Metadata Sample Definition

The following is an example of the PardotEinstein.settings file:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <PardotEinsteinSettings xmlns="http://soap.sforce.com/2006/04/metadata">

    <enableCampaignInsight>true</enableCampaignInsight>

    <enableEngagementScore>true</enableEngagementScore>

   </PardotEinsteinSettings>

```

Example Package Manifest

The following is an example package manifest used to deploy or retrieve the PardotEinstein settings metadata:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

    <types>

     <members>PardotEinstein</members>

     <name>Settings</name>

    </types>

    <version>29.0</version>

   </Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### PathAssistantSettings

Represents the Path preference setting. This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.

File Suffix and Directory Location

#### PathAssistantSettings components have the suffix .settings and are stored in the settings folder.


Metadata Types PathAssistantSettings

Version

PathAssistantSettings components are available in API version 34.0 and later.

Fields

**Field Name** **Field Type** **Description**

`canOverrideAutoPathCollapseWithUserPref` boolean

`pathAssistantEnabled` boolean

`pathAssistantForOpportunityEnabled` boolean

Keeps a user's path expanded to show guidance and key fields on all
their records. A user's path stays expanded until the user collapses it. To
use this preference, Path must be enabled.

Default value is `false` for all editions. When set to `false`, the user’s
path is collapsed when the page loads.

Available in API version 47.0 and later.

Determines whether the preference is enabled for Path. Default value is
`true` for Enterprise Edition and `false` for other editions. Available
in API version 35.0 and later.

Determines whether the preference is enabled for Path in Opportunity
or not.

Available in API version 34.0 and earlier.

Declarative Metadata Sample Definition

The following is an example of a PathAssistantSettings component.

```
<?xml version="1.0" encoding="UTF-8"?>

<PathAssistantSettings xmlns="http://soap.sforce.com/2006/04/metadata">

   <pathAssistantEnabled>true</pathAssistantEnabled>

  <canOverrideAutoPathCollapseWithUserPref>true</canOverrideAutoPathCollapseWithUserPref>

</PathAssistantSettings>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>PathAssistant</members>

     <name>Settings</name>

   </types>

   <version>API</version>

</Package

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


#### Metadata Types PaymentsSettings PaymentsSettings

Represents the Salesforce Payments settings when this feature is enabled for the org.

Parent Type and Manifest Access

This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all the settings metadata types for the org are accessed using the “Settings” name. See Settings for more details.

File Suffix and Directory Location

#### PaymentsSettings values are stored in the Payments.settings file in the settings folder.

The `.settings` files are different from other named components because there’s only one settings file for each settings component.

Version

#### PaymentsSettings is available in API version 57.0 and later.

Special Access Rules

This metadata type is only accessible by developers and customers using Salesforce Payments.

Fields

**Field Name** **Description**

```
enablePayments

```

**Field Type**
boolean

**Description**
Indicates whether Salesforce Payments is enabled ( `true` ) or not ( `false` ) for an org.
The default is false.

Declarative Metadata Sample Definition

The following is a sample `payments.settings` metadata file.

```
<?xml version="1.0" encoding="UTF-8"?>

  <PaymentsSettings xmlns="http://soap.sforce.com/2006/04/metadata">

   <enablePayments>true</enablePayments>

  </PaymentsSettings>

```

The following is an example `package.xml` that references the previous definition.

```
<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>Payments</members>

     <name>Settings</name>

   </types>

```


#### Metadata Types PicklistSettings

```
      <version>57.0</version>

   </Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### PicklistSettings

Represents an org’s picklist settings. These settings control the behavior of a picklist. This type extends the Metadata metadata type and
inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.

File Suffix and Directory Location

#### PicklistSettings values are stored in a single file named Picklist.settings in the settings directory. The .settings files

are different from other named components because there’s only one settings file for each settings component.

Version

Picklist settings are available in API version 47.0 and later.

Fields

**Field Name** **Field Type** **Description**

`isPicklistApiNameEditDisabled` boolean While `true`, users, including admins with Customize
Application permission, can’t change the API name of a picklist

field. Formulas reference a picklist’s API name so that the formula
continues to work even if the displayed name value changes.
Prevent changes to the API name to protect the references to
fields in formulas or during integrations, such as during a data
import. The default is `false` .

Declarative Metadata Sample Definition

The following is a sample `picklist.settings` metadata file.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <PicklistSettings xmlns="http://soap.sforce.com/2006/04/metadata">

     <isPicklistApiNameEditDisabled>true</isPicklistApiNameEditDisabled>

   </PicklistSettings>

```


#### Metadata Types PlatformEncryptionSettings

The following is an example `package.xml` manifest that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

    <types>

     <members>Picklist</members>

     <name>Settings</name>

    </types>

    <version>47.0</version>

   </Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### PlatformEncryptionSettings

Represents an org’s Platform Encryption settings, such as settings for available encryption schemes, permissions, encryption policy access,
and which fields can be encrypted. This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.

File Suffix and Directory Location

#### PlatformEncryptionSettings values are stored in the PlatformEncryption.settings file in the settings folder. The

`.settings` files are different from other named components because there’s only one settings file for each settings component.

Version

#### PlatformEncryptionSettings is available in API versions 47.0 and later.

Special Access Rules

To enable and disable PlatformEncryptionSettings attributes, you need the Customize Application permission. Attributes that allow key
[management tasks require the Manage Encryption Keys permission. For a complete list of required permissions, read Which User](https://developer.salesforce.com/docs/atlas.en-us.260.0.securityImplGuide.meta/securityImplGuide/security_pe_permissions.htm#!)
[Permissions Does Shield Platform Encryption Require?.](https://developer.salesforce.com/docs/atlas.en-us.260.0.securityImplGuide.meta/securityImplGuide/security_pe_permissions.htm#!)

Fields

**Field Name** **Field Type** **Description**

`canEncryptManagedPackageFields` boolean Indicates whether users can enable encryption on custom fields in
installed managed packages ( `true` ) or not ( `false` ).

`isUseHighAssuranceKeysRequired` boolean This field is for internal use.


Metadata Types PlatformEncryptionSettings

**Field Name** **Field Type** **Description**

`isMEKForEncryptionRequired` boolean

`enableDeterministEncryption` boolean

Indicates whether encryption policy tasks, such as enabling encryption
on fields, also require the Manage Encryption Keys permission ( `true` )
or not ( `false` ), in addition to those tasks’ baseline permissions.

Indicates whether customers apply the deterministic encryption scheme
to supported fields ( `true` ) or not ( `false` ). The deterministic encryption
scheme lets customers filter on encrypted data..

`enableEncryptFieldHistory` boolean Indicates whether the background encryption process applies the
customer's active key material to field history and feed tracking values

( `true` ) or not ( `false` ). The default value is `false` . If `false`,
background encryption processes apply active key material to all
encrypted data except duplicates of that data stored in field history or
feed tracking.

`enableEventBusEncryption` boolean This field is for internal use.

Declarative Metadata Sample Definition

The following is an example of the PlatformEncryption.settings file:

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>

<PlatformEncryptionSettings xmlns="http://soap.sforce.com/2006/04/metadata">

   <canEncryptManagedPackageFields>true</canEncryptManagedPackageFields>

   <isUseHighAssuranceKeysRequired>true</isUseHighAssuranceKeysRequired>

   <isMEKForEncryptionRequired>true</isMEKForEncryptionRequired>

   <enableDeterministEncryption>true</enableDeterministEncryption>

  <enableEncryptFieldHistory>true</enableEncryptFieldHistory></PlatformEncryptionSettings>

```

Example Package Manifest

The following is an example package manifest used to deploy or retrieve the Platform Encryption settings metadata for an organization:

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>PlatformEncryption</members>

     <name>Settings</name>

   </types>

   <version>47.0</version>

</Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


#### Metadata Types PlatformEventSettings PlatformEventSettings

Represents settings for platform events and change data capture events.

Parent Type and Manifest Access

This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all the settings metadata types for the org are accessed using the “Settings” name. See Settings for more details.

File Suffix and Directory Location

#### PlatformEventSettings values are stored in the PlatformEvent.settings file in the settings folder. The

`.settings` files are different from other named components, because there’s only one settings file for each settings component.

Version

#### PlatformEventSettings components are available in API version 58.0 and later.

Special Access Rules

There are no additional access requirements that are specific to this type.

Fields

**Field Name** **Description**

```
enableEnhancedUsageMetrics

```

**Field Type**
boolean

**Description**
Enables enhanced usage metrics for queries run against PlatformEventUsageMetric.
Enhanced usage metrics provide additional fields for the queries and granular time
[segments. For more information, see Enhanced Usage Metrics in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/platform_events_monitor_enhanced_usage.htm) _Platform Events_
_Developer Guide_ . Default value is `false` .

Declarative Metadata Sample Definition

The following is an example of a PlatformEventSettings component that enables the enhanced usage metrics feature.

```
<?xml version="1.0" encoding="UTF-8"?>

<PlatformEventSettings xmlns="http://soap.sforce.com/2006/04/metadata">

   <enableEnhancedUsageMetrics>true</enableEnhancedUsageMetrics>

</PlatformEventSettings>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

```


#### Metadata Types PredictionBuilderSettings

```
        <members>PlatformEvent</members>

        <name>Settings</name>

      </types>

      <version>58.0</version>

   </Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The wildcard
applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the manifest
file, see Deploying and Retrieving Metadata with the Zip File.

#### PredictionBuilderSettings

Represents the settings that determine how a user can interact with Einstein Prediction Builder. This type extends the Metadata metadata
type and inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.

File Suffix and Directory Location

#### PredictionBuilderSettings values are stored in the PredictionBuilder.settings file in the settings directory. The .settings files are different

from other named components in that each settings component has only one settings file.

Version

#### PredictionBuilderSettings components are available in API version 47.0 and later.

Special Access Rules

This type is available only if the CRM Analytics Plus or Einstein Predictions license is enabled in your org.

Fields

**Field Name** **Field Type** **Description**

`enablePredictionBuilder` boolean Indicates whether Einstein Prediction Builder is enabled ( `true` ) or not
( `false` ).

`isPredictionBuilderStarted` boolean Indicates whether to display the predictions list view to the user ( `true` )
or not ( `false` ).

Declarative Metadata Sample Definition

This is a sample Prediction Builder settings file.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <PredictionBuilderSettings xmlns="http://soap.sforce.com/2006/04/metadata">

      <isPredictionBuilderStarted>false</isPredictionBuilderStarted>

```


#### Metadata Types PrivacySettings

```
      <enablePredictionBuilder>false</enablePredictionBuilder>

   </PredictionBuilderSettings>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### PrivacySettings

Represents an organization’s settings for data privacy and consent management. This type extends the Metadata metadata type and
inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.

File Suffix and Directory Location

#### PrivacySettings values are stored in the Privacy.settings file in the settings directory. The .settings files are different

from other named components because there’s only one settings file for each settings component.

Version

#### PrivacySettings components are available in API version 47.0 and later.

Special Access Rules

To use PrivacySettings, you need the Customize Application or Modify Data Classification user permission.

Fields

**Field Name** **Field Type** **Description**

`authorizationCaptureBrowser` boolean

`authorizationCaptureEmail` boolean

`authorizationCaptureIp` boolean

`authorizationCaptureLocation` boolean

Indicates whether browser information is captured during authorization
consent capture ( `true` ) or not ( `false` ). The default value is `false` .
Available in API version 59.0 and later.

Indicates whether email address is captured during authorization consent
capture ( `true` ) or not ( `false` ). The default value is `false` . Available
in API version 59.0 and later.

Indicates whether IP address is captured during authorization consent
capture ( `true` ) or not ( `false` ). The default value is `false` . Available
in API version 59.0 and later.

Indicates whether location information is captured during authorization
consent capture ( `true` ) or not ( `false` ). The default value is `false` .
Available in API version 59.0 and later.


Metadata Types PrivacySettings

**Field Name** **Field Type** **Description**

`authorizationCustomSharing` boolean

`authorizationCustomSharingPCU` boolean

`authorizationLockingAndVersioning` boolean

`enableConfigurableUserPIIActive` boolean

Indicates whether custom sharing is enabled for authorization consent
records ( `true` ) or not ( `false` ). The default value is `false` . Available
in API version 59.0 and later.

Indicates whether custom sharing for authorization consent records uses
permission-based access control ( `true` ) or not ( `false` ). The default
value is `false` . Available in API version 62.0 and later.

Indicates whether locking and versioning is enabled for authorization
consent records ( `true` ) or not ( `false` ). The default value is `false` .
Available in API version 59.0 and later.

Indicates whether configurable user PII (Personally Identifiable
Information) classification is active ( `true` ) or not ( `false` ). The default
value is `false` . Available in API version 59.0 and later.

`enableConsentAuditTrail` boolean Reserved for future use.

`enableConsentEventStream` boolean

`enableDefaultMetadataValues` boolean

`enableSalesforceArchive` boolean

`useUmaDefaultConsentRecs` boolean

Allows orgs to stream consent changes to the party data model via
platform events. This field has a default value of `false` . Available in
API version 47.0 and later.

Indicates whether a default data sensitivity value is applied to all contacts,
leads, person accounts, and users ( `true` ) or not ( `false` ). This field has
a default value of `false` . Available in API version 47.0 and later.

Indicates whether Salesforce Archive is enabled for privacy-related data
archival ( `true` ) or not ( `false` ). The default value is `false` . Available
in API version 61.0 and later.

Indicates whether a Preference Manager setup in Privacy Center uses
default Marketing Cloud consent parameters and features. This field has
a default value of `false` . Available in API version 58.0 and later.

Declarative Metadata Sample Definition

The following is an example of a PrivacySettings component.

```
<?xml version="1.0" encoding="UTF-8"?>

<PrivacySettings xmlns="http://soap.sforce.com/2006/04/metadata">

   <enableDefaultMetadataValues>false</enableDefaultMetadataValues>

</PrivacySettings>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>Privacy</members>

     <name>Settings</name>

   </types>

```


#### Metadata Types ProcessFlowMigration

```
      <version>47.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

#### ProcessFlowMigration

Represents a process's migrated criteria and the resulting migrated flow.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

Version

#### ProcessFlowMigration components are available in API version 58.0 and later.

Special Access Rules

Fields

**Field Name** **Description**

```
destinationFlowDefinition

destinationFlowVersion

developerName

```

**Field Type**
string

**Description**
Required. The ID of the resulting migrated flow.

**Field Type**
string

**Description**
Required. The version ID of the migrated flow.

**Field Type**
string

**Description**
Required. The unique name of the object in the API. This name can contain only
underscores and alphanumeric characters, and must be unique in your org. It must


Metadata Types ProcessFlowMigration

**Field Name** **Description**

begin with a letter, not include spaces, not end with an underscore, and not contain
two consecutive underscores.

```
masterLabel

migratedCriteriaLabel

migratedCriteriaName

processVersion

```

**Field Type**
string

**Description**
Required. The label for the ProcessFlowMigration.

**Field Type**
string

**Description**
The label of the criteria that was migrated.

**Field Type**
string

**Description**
The name of the criteria that was migrated.

**Field Type**
string

**Description**
Required. The version ID of the originating process.

Declarative Metadata Sample Definition

The following is an example of a ProcessFlowMigration component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ProcessFlowMigration xmlns="http://soap.sforce.com/2006/04/metadata"

xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

   <destinationFlowDefinition>Migration_1</destinationFlowDefinition>

   <destinationFlowVersion>Migration_1-1</destinationFlowVersion>

   <developerName>Migration</developerName>

   <masterLabel>Migration_1</masterLabel>

   <migratedCriteriaLabel>myCriteria_1</migratedCriteriaLabel>

   <migratedCriteriaName>myDecision</migratedCriteriaName>

   <processVersion>Migration-1</processVersion>

</ProcessFlowMigration>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>*</members>

     <name>ProcessFlowMigration</name>

   </types>

```


#### Metadata Types ProductSettings

```
      <types>

        <members>*</members>

        <name>Flow</name>

      </types>

      <version>58.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

#### ProductSettings

Represents organization preferences for quantity schedules, revenue schedules, and active flag interaction with prices. This type extends
the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

#### ProductSettings values are stored in a single file named Product.settings in the settings directory of the corresponding

package directory. The `.settings` files are different from other named components because there’s only one settings file for each
settings component.

Version

#### ProductSettings is available in API version 28.0 and later.

Fields

**Field Name** **Field Type** **Description**

`enableCascadeActivateToRelatedPrices` boolean When changing active flag on a product record, automatically updates
active flag on related prices.

`enableMySettings` boolean Moves users’ personal settings pages from Setup to a separate My
Settings pane ( `true` ) or not ( `false` ). When set to ( `true` ), Salesforce

makes a reorganized Setup pane accessible to admins via one click in
the header. This setting affects all users in your organization. The default
is `true` . Available in API version 47.0 and later.

`enableQuantitySchedule` boolean Enables quantity schedules for products.

`enableRevenueSchedule` boolean Enables revenue schedules for products.


#### Metadata Types QuoteSettings

Declarative Metadata Sample Definition

The following is an example of the package file.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Product</members>

        <name>Settings</name>

      </types>

      <version>28.0</version>

   </Package>

```

The package file references the following Product.settings file.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ProductSettings xmlns="http://soap.sforce.com/2006/04/metadata">

      <enableCascadeActivateToRelatedPrices>true</enableCascadeActivateToRelatedPrices>

      <enableQuantitySchedule>false</enableQuantitySchedule>

      <enableRevenueSchedule>false</enableRevenueSchedule>

   </ProductSettings>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### QuoteSettings

Represents an org’s quotes settings, such as enabling quotes or creating quotes without an associated opportunity. This type extends
the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.

File Suffix and Directory Location

#### QuoteSettings values are stored in a single file named Quote.settings in the settings directory of the corresponding package

directory. The `.settings` files are different from other named components because there’s only one settings file for each settings
component.

Version

#### QuoteSettings is available in API version 28.0 and later.

Fields

**Field Name** **Field Type** **Description**

`enableQuote` boolean When set to `true`, users can access Quotes.


#### Metadata Types RealTimeEventSettings

**Field Name** **Field Type** **Description**

`enableQuotesWithoutOppEnabled` boolean

When set to `true`, users can create quotes independently of an
opportunity. For example, a user can create a quote for budgeting
purposes, before creating the Opportunity. Default value is `false` .

When set to `false`, users can only create quotes from an Opportunity.
Before setting to `false`, delete any quotes that do not have
opportunities.

Available in API version 47.0 and later.

Declarative Metadata Sample Definition

The following is an example of the package file.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>Quote</members>

     <name>Settings</name>

   </types>

   <version>28.0</version>

</Package>

```

The package file references the following Quote.settings file.

```
<?xml version="1.0" encoding="UTF-8"?>

<QuoteSettings xmlns="http://soap.sforce.com/2006/04/metadata">

   <enableQuote>true</enableQuote>

   <enableQuotesWithoutOppEnabled>true</enableQuotesWithoutOppEnabled>

</QuoteSettings>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### RealTimeEventSettings

Represents the list of Real-Time Event entities that you want to enable or disable. This type extends the Metadata metadata type and
inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.

File Suffix and Directory Location

Real-Time Event settings are stored in a single file named `RealTimeEvent.settings` in the `settings` directory. The
`.settings` files are different from other named components because there’s only one settings file for each settings component.


Metadata Types RealTimeEventSettings

Version

RealTimeEventSettings is available in API version 50.0 and later.

Fields

**Field Name** **Field Type** **Description**

`realTimeEvents` RealTimeEvent[] Represents the list of Real-Time Event entities that you want
to enable or disable.

RealTimeEvent

Represents one of the Real-Time Event entities that you want to enable or disable.

**Field Name** **Field Type** **Description**

`entityName` string The storage or streaming entity name that you want to modify. For
example: ApiEvent or ApiEventStream.

`isEnabled` boolean Indicates whether you want the storage or streaming capability to be
enabled ( `true` ) or disabled ( `false` ).

Declarative Metadata Sample Definition

The following is an example `RealTimeEvent.settings` metadata file:

```
   <?xml version=“1.0” encoding=“UTF-8"?>

   <RealTimeEventSettings xmlns=“http://soap.sforce.com/2006/04/metadata”/>

     <realTimeEvents>

      <entityName>ApiEventStream</entityName>

      <isEnabled>true</isEnabled>

     </realTimeEvents>

     <realTimeEvents>

      <entityName>ApiEvent</entityName>

      <isEnabled>true</isEnabled>

     </realTimeEvents>

   </RealTimeEventSettings>

```

The following is an example `package.xml` manifest that references the RealTimeEventSettings definitions:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>RealTimeEvent</members>

        <name>Settings</name>

      </types>

      <version>51.0</version>

   </Package>

```


#### Metadata Types RecordPageSettings

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### RecordPageSettings

Represents an org’s record page settings. This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.

Declarative Metadata File Suffix and Directory Location

#### RecordPageSettings values are stored in a single file named RecordPage.settings in the settings directory. The .settings

files are different from other named components because there’s only one settings file for each settings component.

Version

Record page settings are available in API version 47.0 and later.

Fields

**Field** **Field Type** **Description**

`enableActivityRelatedList` boolean

`enableDynamicForms` boolean

`enableFullRecordView` boolean

Declarative Metadata Sample Definition

This is a sample `recordpage.settings` metadata file.

Indicates whether the default activities view
is related lists ( `true` ) or activity timeline
( `false` ).

Indicates whether Dynamic Forms is
enabled for the org. Removed in API version
50.0 and later.

Indicates whether the default record page
view is full view ( `true` ) or grouped view
( `false` ).

```
<?xml version="1.0" encoding="UTF-8"?>

<RecordPageSettings xmlns="http://soap.sforce.com/2006/04/metadata">

   <enableDynamicForms>true</enableDynamicForms>

   <enableActivityRelatedList>true</enableActivityRelatedList>

   <enableFullRecordView>true</enableFullRecordView>

</RecordPageSettings>

```


#### Metadata Types RetailExecutionSettings

Example Package Manifest

The following is an example package manifest used to deploy or retrieve the Record Page settings metadata for an organization

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>RecordPage</members>

        <name>Settings</name>

      </types>

      <version>47.0</version>

   </Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

Settings

#### RetailExecutionSettings

Represents settings to manage your inventory, promotions, planograms, and in-store activities.

This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for more details.

File Suffix and Directory Location

#### RetailExecutionSettings are stored in a single file named RetailExecution.settings in the settings directory.

Version

#### RetailExecutionSettings are available in API version 47.0 and later.

Fields

**Field Name** **Field Type** **Description**

`enableProductHierarchy` boolean

`enableRetailExecution` boolean

Indicates whether Product Hierarchy is enabled for your org ( `true` ) or
not `false` ).

This field is available in API version 53.0 and later.

Indicates whether Retail Execution is enabled for your org ( `true` ) or
not ( `false` ).

The default value is `false` .


#### Metadata Types SalesAgreementSettings

**Field Name** **Field Type** **Description**

`enableVisitSharing` boolean

Indicates whether Visit Share is enabled for your org ( `true` ) or not
( `false` ).

The default value is `false` .

This field is available in API version 55.0 and later.

Declarative Metadata Sample Definition

The following is an example of a RetailExecutionSettings component.

```
<?xml version="1.0" encoding="UTF-8"?>

<RetailExecutionSettings xmlns="http://soap.sforce.com/2006/04/metadata">

   <enableRetailExecution>true</enableRetailExecution>

   <enableProductHierarchy>true</enableProductHierarchy>

   <enableVisitSharing>false</enableVisitSharing>

</RetailExecutionSettings>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>RetailExecution</members>

     <name>Settings</name>

   </types>

   <version>55.0</version>

</Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### SalesAgreementSettings

Represents settings that control the display of agreement terms metrics in sales agreements and the calculation of the actual quantity
of products in sales agreements. These settings also control the approval of sales agreements.

This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for more details.

File Suffix and Directory Location

#### SalesAgreementSettings values are stored in the SalesAgreementSettings.salesAgreementSetting file in the

`salesAgreementSettings` directory.


Metadata Types SalesAgreementSettings

Version

SalesAgreementSettings components are available in API version 47.0 and later.

Fields

**Field Name** **Field Type** **Description**

`actualsCalculationMode` ActualsCalculationMode(enumeration Required. Source from which the actual ordered quantity of a product
of type string) in a sales agreement is calculated. Valid values are:

**•** `DataProcessingEngine` —Available in API version 63.0 and
later.

**•** `Manual: Default`

**•** `Orders`

**•** `OrdersThroughContracts`

`decimalScale` int Required. Number of decimal places applied to values in sales
agreements. Available in API version 62.0 and later.

`displayGroups` AdvAcctFrcstDisplayGroup

`displayedAgreementTermsMetrics` string

Represents information about the groups for the advanced account
forecast set measures or dimensions. Available in API version 56.0 and
later.

Required. Metrics that are selected for display in the sales agreement
terms in the specified sequence. There can be a maximum of 10
comma-separated metric names in this list.

`futureActCalcSchedules` `int` Required. Number of future schedules to include in actuals calculations
in the sales agreement. Available in API version 63.0 and later.

`measureDefinitions` AdvAcctForecastMeasureDef
on page 2225

`objectMapping` ObjectMapping on
page 2226

Represents information about the measures to be displayed in the
advanced account forecasts grid for the forecast set. Available in API
version 56.0 and later.

Foreign key to ObjectMapping on page 2226 that maps fields from the
input object of SalesAgreementSettings to fields in the output object of
SalesAgreementSettings.

`primaryNotifEmailAddress` string The email address to which notifications are sent.

`renewalPeriodDayCount` int The number of days before the end date of a sales agreement from when
the agreement can be renewed. Available in API version 50.0 and later.

`secondaryNotifEmailAddress` string The second email address to which notifications are sent.

AdvAcctFrcstDisplayGroup

Represents information about the groups for the advanced account forecast set measures or dimensions. Available in API version 56.0
and later.


Metadata Types SalesAgreementSettings

**Field Name** **Field Type** **Description**

`advAcctFrcstDisplayGroupName` string Required. Name of the advanced account forecast display group.

`displayGroupItems` AdvAcctFrcstDplyGroupItem Represents information about the items associated with a display group for an
on page 2225 advanced account forecast set.

`displayGroupType` AdvAcctFrcstDisplayGroupType(enumeration
of type string)

Category for the display group.

Possible values are:

**•** `MEASURE`

`isDefault` boolean Indicates whether the display group is the default group ( `true` ) or not
( `false` ). The default value is `false` .

`userProfileName` string Profile for which the display group is applicable.

AdvAcctFrcstDplyGroupItem

Represents information about the items associated with a display group for an advanced account forecast set. Available in API version
56.0 and later.

**Field Name** **Field Type** **Description**

`advAcctFrcstDplyGroupItemName` string Required. Name of the advanced account forecast display group item.

`displayOrder` string Required. Display order of the display group item.

`measureReferenceName` string Name of the measure associated with the display group item.

AdvAcctForecastMeasureDef

Represents information about the measures to be displayed in the advanced account forecasts grid for the forecast set. Available in API
version 56.0 and later.

**Field Name** **Field Type** **Description**

`advAcctForecastMeasureDefName` string Required. Name for the measure.

`aggregationType` AdvAcctFcstAggregationType(enumeration
of type string)

Required. Type of aggregation used for calculating advanced account forecast
values.

Possible values are:

**•** `AVERAGE`

**•** `MAXIMUM`

**•** `MINIMUM`

**•** `SUM`


Metadata Types SalesAgreementSettings

**Field Name** **Field Type** **Description**

`computationMethod` AdvAcctFcstComputationMethodenumeration
of type string)

Required. Method used for calculating advanced account forecast values.

Possible values are:

**•** `CUSTOM`

**•** `DATA_PROCESSING_ENGINE_DEFINITION`

**•** `FORMULA`

`forecastDataMeasureName` string Required. Field of the facts object used for this measure.

`forecastMeasureName` string Required. Name for the measure to show on UI.

`forecastMeasureType` AdvAcctFcstMeasureType(enumeration
of type string)

`isAdjustmentTracked` boolean

ObjectMapping

Required. Measure type used for the generated advanced forecast values.

Possible values are:

**•** `QUANTITY`

**•** `REVENUE`

Indicates whether the adjustments made to the advanced account forecast
values for this metric are tracked ( `true` ) or not ( `false` ). The default value is
`false` .

Represents a map of fields in the input object of SalesAgreementSettings to fields in the output object of SalesAgreementSettings. The
input object is SalesAgreementProductSchedule. The output object is SalesAgreementProduct.

**Field Name** **Field Type** **Description**

`inputObject` string

Required. The input object for the SalesAgreementSettings.
SalesAgreementProductSchedule is the input object for the
SalesAgreementSettings.

`mappingFields` ObjectMappingField The mapping of source object fields to target object fields for
on page 2226 SalesAgreementSettings.

`outputObject` string Required. The output object for the SalesAgreementSettings.
SalesAgreementProduct is the output object for the SalesAgreementSettings.

ObjectMappingField

A field name in the SalesAgreementProductSchedule object and the corresponding field name in the SalesAgreementProduct object.

For example, you can create a field named Revenue on the SalesAgreementProductSchedule object and a field named Total Revenue
on the SalesAgreementProduct object. To view these field values in the agreement terms of a sales agreement, select the input object
as SalesAgreementProductSchedule and the output object as SalesAgreementProduct. In this case, the input field is Revenue and the
output field is Total Revenue.


Metadata Types SalesAgreementSettings

**Field Name** **Field Type** **Description**

`inputField` string Required. Field in the object specified by the `inputObject` field in
ObjectMapping on page 2226. This field is mapped to the field in

`outputField`, which is a field in the object specified by the
`outputObject` field in ObjectMapping on page 2226.

`outputField` string Required. Field in the object specified by the `outputObject` field in
ObjectMapping on page 2226. This field is mapped to the field name in

`inputField`, which is a field in the object specified by the `inputObject`
field in ObjectMapping on page 2226.

Declarative Metadata Sample Definition

The following is an example of SalesAgreementSettings component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <SalesAgreementSettings

    xmlns="http://soap.sforce.com/2006/04/metadata"

    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

    <actualsCalculationMode>Orders</actualsCalculationMode>

       <decimalScale>0.2</decimalScale>

    <displayGroups>

     <advAcctFrcstDisplayGroupName>Test Measure Group</advAcctFrcstDisplayGroupName>

     <displayGroupItems>

     <advAcctFrcstDplyGroupItemName>PlannedQuantity</advAcctFrcstDplyGroupItemName>

     <displayOrder>1</displayOrder>

     <measureReferenceName>PlannedQuantity</measureReferenceName>

     </displayGroupItems>

     <displayGroupType>MEASURE</displayGroupType>

     <isDefault>false</isDefault>

     <userProfileName xsi:nil="true"/>

    </displayGroups>

   <displayedAgreementTermsMetrics>PlannedQuantity,ActualQuantity,SalesPrice,DiscountPercentage,DerivedPlannedAmount</displayedAgreementTermsMetrics>

       <futureActCalcSchedules>10</futureActCalcSchedules>

    <isOnlyApprovalProcessUsed>false</isOnlyApprovalProcessUsed>

    <measureDefinitions>

     <advAcctForecastMeasureDefName>PlannedQuantity</advAcctForecastMeasureDefName>

     <aggregationType>MINIMUM</aggregationType>

     <computationMethod>DATA_PROCESSING_ENGINE_DEFINITION</computationMethod>

     <forecastDataMeasureName>PlannedQuantity</forecastDataMeasureName>

     <forecastMeasureName>PlannedQuantity</forecastMeasureName>

     <forecastMeasureType>QUANTITY</forecastMeasureType>

     <isAdjustmentTracked>true</isAdjustmentTracked>

    </measureDefinitions>

    <secondaryNotifEmailAddress>abc@salesforce.com</secondaryNotifEmailAddress>

    <primaryNotifEmailAddress>abc@salesforce.com</primaryNotifEmailAddress>

    <renewalPeriodDayCount>50</renewalPeriodDayCount>

    <objectMapping>

     <inputObject>SalesAgreementProductSchedule</inputObject>

     <mappingFields>

```


#### Metadata Types SandboxSettings

```
     <inputField>SAPS1__c</inputField>

     <outputField>SAP1__c</outputField>

     </mappingFields>

     <outputObject>SalesAgreementProduct</outputObject>

    </objectMapping>

   </SalesAgreementSettings>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

         <members>SalesAgreementProduct.SAP1__c</members>

         <members>SalesAgreementProductSchedule.SAPS1__c</members>

         <name>CustomField</name>

      </types>

      <types>

         <members>*</members>

         <name>SalesAgreementSettings</name>

      </types>

      <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### SandboxSettings

Represents Sandbox settings. This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.

File Suffix and Directory Location

#### SandboxSettings values are stored in the Sandbox.settings file in the settings folder. The .settings files are different

from other named components because there is only one settings file for each settings component.

Version

#### SandboxSettings are available in API version 56.0 and later.

Fields

**Field Name** **Field Type** **Description**

`disableSandboxExpirationEmails` boolean Indicates whether to disable sandbox expiration email notifications for
the source (production) org: `true` or `false` . When disabled in the

source (production) org, users no longer receive email notifications for


#### Metadata Types SchemaSettings

**Field Name** **Field Type** **Description**

impending deletions of sandboxes that have been inactive for 180 days
or longer.

Declarative Metadata Sample Definition

The following is an example of a SandboxSettings component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <SandboxSettings xmlns="http://soap.sforce.com/2006/04/metadata">

      <disableSandboxExpirationEmails>true</disableSandboxExpirationEmails>

   </SandboxSettings>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
[wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_settings.htm)
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

#### SchemaSettings

Represents an org’s schema settings, which manage the availability of custom settings and custom metadata type values. This type
extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.

File Suffix and Directory Location

#### SchemaSettings values are stored in the Schema.settings file in the settings directory. The .settings files are different

from other named components because there’s only one settings file for each settings component.

Version

#### SchemaSettings is available in API version 47.0 and later.

Fields

**Field Name** **Field Type** **Description**

`enableAdvancedCMTSecurity` boolean Indicates whether custom metadata type values are available only to
Apex, flow, and formula operations ( `true` ) or exposed in other contexts

such as through the Enterprise WSDL or SOAP API ( `false` ). This field
has a default value of `false` .

`enableAdvancedCSSecurity` boolean Indicates whether custom settings type values are available only to Apex,
flow, and formula operations ( `true` ) or exposed in other contexts such

as through the Enterprise WSDL or SOAP API ( `false` ). This field has a
default value of `false` .


#### Metadata Types SearchSettings

**Field Name** **Field Type** **Description**

`enableListCustomSettingCreation` boolean

`enableSOSLOnCustomSettings` boolean

Indicates whether you can create custom settings when using
application-level data definitions ( `true` ) or not ( `false` ). This field has
a default value of `false` .

Indicates whether custom settings values are returned in Salesforce
Object Search language (SOSL) queries ( `true` ) or not ( `false` ). This
field has a default value of `false` .

Declarative Metadata Sample Definition

The following is an example of a SchemaSettings component.

```
<?xml version="1.0" encoding="UTF-8"?>

<SchemaSettings xmlns="http://soap.sforce.com/2006/04/metadata">

   <enableAdvancedCMTSecurity>true</enableAdvancedCMTSecurity>

   <enableAdvancedCSSecurity>true</enableAdvancedCSSecurity>

   <enableListCustomSettingCreation>false</enableListCustomSettingCreation>

   <enableSOSLOnCustomSettings>true</enableSOSLOnCustomSettings>

</SchemaSettings>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>Schema</members>

     <name>Settings</name>

   </types>

   <version>47.0</version>

</Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### SearchSettings

Represents an org's search settings.

This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for more details.

File Suffix and Directory Location

#### SearchSettings values are stored in a single file named Search.settings in the settings folder. The .settings files are

different from other named components because there’s only one settings file for each settings component.


Metadata Types SearchSettings

Version

SearchSettings is available in API version 37.0 and later.

Fields

**Field Name** **Field Type** **Description**

`documentContentSearchEnabled` boolean Indicates whether a full-text document search is performed.

`enableAdvancedSearchInAlohaSidebar` boolean

Indicates whether advanced search is available in the search
sidebar ( `true` ) or not ( `false` ). Available in Salesforce Classic
only. Available in API version 46.0 and later.

`enableEinsteinSearchAssistantDialog` boolean Indicates whether the Einstein search experience is enabled
( `true` ) or not ( `false` ). Available in API version 50.0 and later.

`enableEinsteinSearchEs4kPilot` boolean

Indicates whether Einstein Search for Knowledge
enhancements are enabled ( `true` ) or not ( `false` ). Available
in API version 54.0 and later.

This feature became generally available in Winter '23. In API
version 56.0 and later, the default value is `true` .

`enableEinsteinSearchNaturalLanguage` boolean Indicates whether natural language search is enabled ( `true` )
or not ( `false` ). Available in API version 50.0 and later.

`enableEinsteinSearchNLSFilters` boolean

`enableEinsteinSearchPersonalization` boolean

Indicates whether the Natural Language Search Filters (Pilot)
feature is enabled ( `true` ) or not ( `false` ). Available in API
version 54.0 and later.

Indicates whether search personalization is enabled ( `true` )
or not ( `false` ). Available in Lightning Experience only.
Available in API version 47.0 and later.

`enablePersonalTagging` boolean Indicates whether users are allowed to group records from
various objects by a common theme ( `true` ) or not ( `false` ).

Personal tags are visible to the user only. Available in Salesforce
Classic only. Available in API version 48.0 and later.

`enablePublicTagging` boolean Indicates whether users are allowed to group records from
various objects by a common theme ( `true` ) or not ( `false` ).

Personal tags are visible to all users. Available in Salesforce
Classic only. Available in API version 48.0 and later.

`enableSalesforceGeneratedSynonyms` boolean Indicates whether search synonyms are enabled ( `true` ) or
not ( `false` ). Available in API version 47.0 and later.

`enableSearchTermHistory` boolean Indicates whether users are allowed to group records from
various objects by a common theme ( `true` ) or not ( `false` ).

Public tags are visible to everyone in the organization. Available
in Salesforce Classic only. Available in API version 48.0 and
later.


Metadata Types SearchSettings

**Field Name** **Field Type** **Description**

`enableSetupSearch` boolean Indicates whether the search box in the Setup sidebar returns
matching custom fields, custom objects, and other supported

setup items when you press Enter ( `true` ) or not ( `false` ).
The default is `true` in Developer, Performance, Professional,
Enterprise, and Unlimited editions, and `false` in all other
editions. Available in API version 47.0 and later.

`enableSuggestArticlesLinksOnly` boolean

`enableUseDefaultSearchEntity` boolean

Indicates whether links are provided to knowledge articles
from Cases similar to the current Case ( `true` ) or not ( `false` ).
Available in API version 48.0 and later.

Indicates whether to use the admin-specified default entity in
sidebar search ( `true` ) or not ( `false` ). Available in Salesforce
Classic only. Available in API version 48.0 and later.

`optimizeSearchForCJKEnabled` boolean Required. Indicates whether the search is optimized for the
Japanese, Chinese, and Korean languages ( `true` ) or not

( `false` ). This setting affects sidebar search and the account
search for **Find Duplicates** on a lead record in sidebar search
and global search. Enable this option if users are searching
mostly in Japanese, Chinese, or Korean, and if the text in
searchable fields is mostly in those languages.

`recentlyViewedUsersForBlankLookupEnabled` boolean Required. Indicates whether the list of records that are returned
from a user autocomplete lookup and from a blank user lookup

is taken from the user’s recently viewed user records ( `true` ).
Otherwise this setting is `false` if the lookup shows a list of
recently accessed user records from across your org ( `false` ).
Only applies to User object blank lookup searches.

`searchSettingsByObject` SearchSettingsByObject Required. Represents a list of search settings for each object.

`sidebarAutoCompleteEnabled` boolean Required. Indicates whether autocomplete is enabled for
sidebar search ( `true` ) or not ( `false` ). Autocomplete is when

users start typing search terms and sidebar search displays a
matching list of recently viewed records.

`sidebarDropDownListEnabled` boolean Required. Indicates whether a dropdown list appears in the
sidebar search section ( `true` ) or not ( `false` ). From this list,

users can select to search within tags, within a specific object,
or across all objects.

`sidebarLimitToItemsIOwnCheckboxEnabled` boolean Required. Indicates whether the **Limit to Items I Own**
checkbox appears ( `true` ) or not ( `false` ). The checkbox

allows your users to include only records for which they are
the record owner when entering search queries in the sidebar.

`singleSearchResultShortcutEnabled` boolean Required. Indicates whether a shortcut is enabled ( `true` ) or
not ( `false` ). With the shortcut, users skip the search results

page and go directly to the record’s detail page when their


Metadata Types SearchSettings

**Field Name** **Field Type** **Description**

search returns only a single item. This setting doesn't apply to
tags, case comments (in advanced search), and global search.

`spellCorrectKnowledgeSearchEnabled` boolean Required. Indicates whether spell check is enabled for
Knowledge search ( `true` ) or not ( `false` ).

SearchSettingsByObject

**Field Name** **Field Type** **Description**

`searchSettingsByObject` ObjectSearchSetting Contains a list of search settings for each object.

ObjectSearchSetting

A list of search settings for each object.

**Field Name** **Field Type** **Description**

`enhancedLookupEnabled` boolean Required. Indicates whether enhanced lookups is enabled for the object
( `true` ) or not ( `false` ).

`lookupAutoCompleteEnabled` boolean

Required. Indicates whether autocomplete is enabled for lookup search
( `true` ) or not ( `false` ). Autocomplete is when users edit the lookup
field inline by choosing an autosuggestion.

`name` string Required. The entity name of the object being configured.

`resultsPerPageCount` int Required. The number of search results per page.

Declarative Metadata Sample Definition

The following is an example of the `Search.settings` file.

```
<?xml version="1.0" encoding="UTF-8"?>

   <SearchSettings xmlns="http://soap.sforce.com/2006/04/metadata">

     <enableSetupSearch>false</enableSetupSearch>

     <enableAdvancedSearchInAlohaSidebar>false</enableAdvancedSearchInAlohaSidebar>

     <enableQuerySuggestionPigOn>false</enableQuerySuggestionPigOn>

     <enableSalesforceGeneratedSynonyms>false</enableSalesforceGeneratedSynonyms>

     <enableSearchTermHistory>false</enableSearchTermHistory>

     <enablePublicTagging>false</enablePublicTagging>

     <enablePersonalTagging>false</enablePersonalTagging>

     <enableSuggestArticlesLinksOnly>false</enableSuggestArticlesLinksOnly>

     <enableUseDefaultSearchEntity>false</enableUseDefaultSearchEntity>

        <documentContentSearchEnabled>true</documentContentSearchEnabled>

        <optimizeSearchForCJKEnabled>true</optimizeSearchForCJKEnabled>

<recentlyViewedUsersForBlankLookupEnabled>true</recentlyViewedUsersForBlankLookupEnabled>

```


Metadata Types SearchSettings

```
           <searchSettingsByObject>

           <searchSettingsByObject>

             <enhancedLookupEnabled>false</enhancedLookupEnabled>

             <lookupAutoCompleteEnabled>false</lookupAutoCompleteEnabled>

             <name>Account</name>

             <resultsPerPageCount>25</resultsPerPageCount>

           </searchSettingsByObject>

           <searchSettingsByObject>

             <enhancedLookupEnabled>false</enhancedLookupEnabled>

             <lookupAutoCompleteEnabled>false</lookupAutoCompleteEnabled>

             <name>Activity</name>

             <resultsPerPageCount>25</resultsPerPageCount>

           </searchSettingsByObject>

           <searchSettingsByObject>

             <enhancedLookupEnabled>false</enhancedLookupEnabled>

             <lookupAutoCompleteEnabled>false</lookupAutoCompleteEnabled>

             <name>Asset</name>

             <resultsPerPageCount>25</resultsPerPageCount>

           </searchSettingsByObject>

           </searchSettingsByObject>

           <sidebarAutoCompleteEnabled>true</sidebarAutoCompleteEnabled>

           <sidebarDropDownListEnabled>true</sidebarDropDownListEnabled>

   <sidebarLimitToItemsIOwnCheckboxEnabled>true</sidebarLimitToItemsIOwnCheckboxEnabled>

           <singleSearchResultShortcutEnabled>true</singleSearchResultShortcutEnabled>

          <spellCorrectKnowledgeSearchEnabled>true</spellCorrectKnowledgeSearchEnabled>

        <enableEinsteinSearchPersonalization>true</enableEinsteinSearchPersonalization>

      </SearchSettings>

```

Example Package Manifest

The following is an example package manifest used to deploy or retrieve the Search settings metadata for an organization.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Search</members>

        <name>Settings</name>

      </types>

      <version>37.0</version>

   </Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


#### Metadata Types SecuritySettings SecuritySettings

Represents an org’s security settings. For example, settings define trusted IP ranges for network access, password and login requirements,
session expiration, and single sign-on settings.

This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for more details.

File Suffix and Directory Location

#### SecuritySettings values are stored in a single file named Security.settings in the settings directory. The .settings

files are different from other named components because there’s only one settings file for each settings component.

Version

Security settings are available in API version 27.0 and later. API versions 26 and earlier are no longer available.

Fields

**Field Name** **Field Type** **Description**

`canUsersGrantLoginAccess` boolean

If `true`, users can grant login access to Support. If `false`,
only an admin can grant login access.

Users can’t grant login access to managed packages that are
licensed to your entire Salesforce org. Only admins with the
Manage Users permission enabled on their profiles can grant
access to these publishers. Also, some managed packages don’t
have login access. If a package isn’t listed on the Login Access
Policies page, login access isn’t available for that package.

`enableAdminLoginAsAnyUser` boolean If `true`, the **Administrators Can Log in as Any User** field is
enabled. The default isn’t enabled ( `false` ).

`enableAuditFieldsInactiveOwner` boolean

If `true`, this setting enables audit fields and updating the owner
for records that are owned by inactive users. The default value
is `false` . This field is available in API version 47.0 and later.

`enableAuraSecureEvalPref` boolean If `true`, this setting prevents the creation of function
expressions in dynamically created Aura components. The

default is `false` . This field is available in API version 47.0 and
later.

`enableCoepHeader` boolean Indicates whether the Cross-Origin Embedder Policy (COEP)
response header is applied to this org’s custom Visualforce pages

( `true` ) or not ( `false` ). If `true`, externally sourced embedded
content loads only when the external origin allows it via CORS
or CORP. The default value is `false` .

Available in API version 55.0 and later.


Metadata Types SecuritySettings

**Field Name** **Field Type** **Description**

`enableCoopHeader` boolean Indicates whether the Cross-Origin Opener Policy (COOP)
response header is applied to this org’s custom Visualforce pages

( `true` ) or not ( `false` ). If `true`, each custom Visualforce page
opens in a new browsing context group. The default value is
`false` .

Available in API version 55.0 and later.

`enableCrossOrgRedirects` boolean

Indicates whether redirections to other Salesforce orgs are
allowed ( `true` ) or blocked ( `false` ). In Summer ’24 and later,
this field is always `false` .

This setting applies to user redirections to another Salesforce
org via a direct link, a post-action URL, or a post-login URL in

Salesforce. An example of a direct link with a redirection is `<a`

`href="/?startURL=` _**`targetUrl`**_ `">` _**`linkText`**_ `">` _**`linkText`**_ `</a>` .
Post-action URLs and post-login URLs use a protected URL
redirect parameter, such as `retURL`, `startURL`, `saveURL`,
`cancelURL`, and `targetURL` . Subsequent redirections
can’t be verified because they occur outside Salesforce.

To allow cross-org redirections, add the URLs for the Salesforce
orgs that you own to RedirectWhitelistUrl.

Available in API version 59.0 to 60.0.

`enablePermissionsPolicy` boolean Indicates whether the pages that Salesforce serves for this org
include the `Permissions-Policy` HTTP header. This HTTP

header controls access to browser features such as cameras and
microphones. When this field is `false`, access to the browser
features is always permitted. The default value is `false` .

Available in API version 59.0 and later.

`enableRequireHttpsConnection` boolean Deprecated in API version 47.0 and later.

`grantCameraAccess` PermissionsPolicy
(enumeration)

When `enablePermissionsPolicy` is `true`, indicates
when apps and websites loaded from Salesforce can access the
user’s camera.

Possible values are:

**•** `Always` —All apps and websites loaded from Salesforce
can access the user’s camera.

**•** `Never` —No apps or websites, including scripts from
Salesforce domains, can access the user’s camera.

**•** `TrustedUrls` —Only CspTrustedSite entries with
`canAccessCamera` set to `true` can access the user’s
camera.

If `enablePermissionsPolicy` is `false`, this field has
no effect.


Metadata Types SecuritySettings

**Field Name** **Field Type** **Description**

This field is available in API version 59.0 and later.

`grantMicrophoneAccess` Permissions Policy
(enumeration)

When `enablePermissionsPolicy` is `true`, indicates
when apps and websites loaded from Salesforce can access the
user’s microphone.

Possible values are:

**•** `Always` —All apps and websites loaded from Salesforce
can access the user’s microphone.

**•** `Never` —No apps or websites, including scripts from
Salesforce domains, can access the user’s microphone.

**•** `TrustedUrls` —Only CspTrustedSite entries with
`canAccessMicrophone` set to `true` can access the
user’s microphone.

If `enablePermissionsPolicy` is `false`, this field has
no effect.

This field is available in API version 59.0 and later.

`isTLSv12Required` boolean Indicates whether connections to or from your Salesforce org
must use TLS 1.2 or higher ( `true` ) or not ( `false` ). This field

has a default value of `false` . Removed in API version 51.0 and
later.

`isTLSv12RequiredCommunities` boolean Indicates whether connections with your Salesforce sites and
portals or Experience Cloud sites must use TLS 1.2 or higher

( `true` ) or not ( `false` ). This field has a default value of `false` .
Removed in API version 51.0 and later.

`networkAccess` NetworkAccess The trusted IP address ranges from which users can always log
in without requiring computer activation.

`passwordPolicies` PasswordPolicies The requirements for passwords and logins, and assistance with
retrieving forgotten passwords.

`sendCspForUncommonClients` boolean

In rare cases, Salesforce can’t identify whether the requesting
app or specialized browser supports the

```
Content-Security-Policy: frame-ancestors
```

HTTP header directive. In those cases, this field indicates whether
that directive is included in ( `true` ) or omitted from ( `false` )
the HTTP response header for pages that Salesforce serves for
this org. The default value is `false` .

When `sendCspForUncommonClients` is `true`, users
who access Salesforce via an app or browser that doesn’t support
the `Content-Security-Policy:`
`frame-ancestors` HTTP header directive can experience
errors if that lack of support is unclear.

This field is available in API version 59.0 and later.


Metadata Types SecuritySettings

**Field Name** **Field Type** **Description**

`sessionSettings` SessionSettings The settings for session expiration and security.

`singleSignOnSettings` SingleSignOnSettings The settings for single sign-on (SSO).

NetworkAccess

Represents your org’s trusted IP address ranges for network access.

**Field** **Field Type** **Description**

`ipRanges` IpRange[]

IpRange

Defines a range of trusted IP addresses for network access.

The trusted IP address ranges from which users can always log
in without requiring computer activation.

To add an IP range, deploy all existing IP ranges, including the
one you want to add. Otherwise, the existing IP ranges are

replaced with the ones you deploy. To remove all the IP ranges,
leave the networkAccess field blank
(<networkAccess></networkAccess>).

**Field** **Field Type** **Description**

`description` string

The description of the trusted IP range. Use this field to identify
the range, such as which corporate network corresponds to this
range. Available in API version 34.0 and later.

`end` string The IP address that defines the high end of a range of trusted
addresses.

`start` string The IP address that defines the low end of a range of trusted
addresses.

PasswordPolicies

Represents your org’s password and login policies, which show up under **Security Controls | Password Policies** .

**Field** **Field Type** **Description**

`apiOnlyUserHomePageURL` string The URL to which users with the API Only User permission are
redirected instead of the login page.

`complexity` Complexity (enumeration of
type string)


The types of characters that must be used in a user’s password.
Valid values are:

**•** `NoRestriction` —Has no requirements and is the least
secure option.

Metadata Types SecuritySettings

**Field** **Field Type** **Description**

**•** `AlphaNumeric` —The default setting. Requires at least
one alphabetic character and one number. This value is the
default value.

**•** `SpecialCharacters` —Requires at least one alphabetic
character, one number, and one of the following characters:

```
                               ! " # $ % & ' ( ) * +, - . / : ; < =
```

_`> ? @ [ \ ] ^ _ ` { | } ~`_ .

**•** `UpperLowerCaseNumeric` —Requires at least one
number, one uppercase letter, and one lowercase letter.
This value is available in API version 31.0 and later.

**•** `UpperLowerCaseNumericSpecialCharacters` —Requires
at least one number, one uppercase letter, one lowercase
letter, and one of the following characters: _`! " # $ %`_

```
                               & ' ( ) * +, - . / : ; < = > ? @ [ \
```

_`] ^ _ ` { | } ~`_ . This value is available in API version
31.0 and later.

**•** `Any3UpperLowerCaseNumericSpecialCharacters` —Requires
at least three of the following options: one number, one
uppercase letter, one lowercase letter, and one special
character ( _`! " # $ % & ' ( ) * +, - . /`_
_`: ; < = > ? @ [ \ ] ^ _ ` { | } ~`_ ). This
value is available in API version 46.0 and later.

`enableSetPasswordInApi` boolean Deprecated in API version 51.0. Removed in API version 52.0.

`expiration` Expiration (enumeration of type
string)

The length of time until a user password expires and must be
changed. Valid values are:

**•** `Never`

**•** `ThirtyDays`

**•** `SixtyDays`

**•** `NinetyDays` . This value is the default value.

**•** `SixMonths`

**•** `OneYear`

`historyRestriction` string The number of previous passwords saved for users so that they
must always reset a new, unique password. Valid values are `0`

through `24` passwords remembered. The maximum value of
24 applies to API version 31.0 and later. In earlier versions, the
maximum value is 16. The default value is `3` .

`lockoutInterval` LockoutInterval (enumeration
The duration of the login lockout. Valid values are:
of type string)

**•** `FifteenMinutes` . This value is the default value.

**•** `ThirtyMinutes`

**•** `SixtyMinutes`


Metadata Types SecuritySettings

**Field** **Field Type** **Description**

**•** `Forever` (must be reset by admin)

`maxLoginAttempts` MaxLoginAttempts
(enumeration of type string)

`minimumPasswordLength` string

The number of login failures allowed for a user before the user
is locked out. Valid values are:

**•** `NoLimit`

**•** `ThreeAttempts`

**•** `FiveAttempts`

**•** `TenAttempts` . This value is the default value.

The minimum number of characters required for a password.
The number can contain from 5 to 50 characters (default is 8).
Available in API version 35.0 and later.

Before API version 35.0, specify minimum password length with
the enumeration `minPasswordLength`, with valid values
`FiveCharacters`, `EightCharacters` (default),
`TenCharacters`, `TwelveCharacters` (API version
31.0 and later), and `FifteenCharacters` (API version 34.0
and later).

`minimumPasswordLifetime` boolean If **Require a minimum 1 day password lifetime** is enabled
( `true` ), passwords can’t be changed more than one time during

a 24-hour period. The default is `false` . Available in API version
31.0 and later.

`obscureSecretAnswer` boolean

`passwordAssistanceMessage` string

If enabled ( `true` ), hide answers to security questions as the
user types. The default is `false` .

If your org uses the Microsoft Input Method Editor (IME) with
the input mode set to Hiragana, when you type ASCII characters,

they’re converted in to Japanese characters in normal text fields.
However, the IME doesn’t work properly in fields with obscured
text. If your org’s users can’t properly enter their passwords or
other values after enabling this feature, disable the feature.

The text that appears in the Account Lockout email and at the
bottom of the Confirm Identity screen for users resetting their
passwords.

`passwordAssistanceURL` string The URL that users can click to retrieve forgotten passwords.

`questionRestriction` QuestionRestriction
(enumeration of type string)


The restriction on whether the answer to the password hint
question can contain the password itself. Valid values are:

**•** `None`

**•** `DoesNotContainPassword` . This value is the default
value.

Metadata Types SecuritySettings

SessionSettings

Represents your org’s session expiration and security settings.

**Field** **Field Type** **Description**

`allowUserAuthenticationByCertificate` boolean

`allowUserCertBasedAuthenticationWithOcspValidation` boolean

If enabled ( `true` ), users can authenticate with a PEM-encoded
X.509 digital certificate. Not enabled by default. Available in API
version 47.0 and later.

If enabled ( `true` ), authentication certificates are validated
using the Online Certificate Status Protocol (OCSP) or a
Certificate Revocation List (CRL).

`auraBoxcarReductionPref` boolean If `true`, dynamic boxcar optimization for the Aura framework
is disabled. With dynamic boxcar optimization, a limited number

of server-side Aura actions are grouped in a single network
request, which improves the performance of Lightning
[components and apps. For more information, see Boxcar](https://developer.salesforce.com/docs/atlas.en-us.260.0.lightning.meta/lightning/controllers_server_actions_boxcar_dynamic.htm)
[Grouping and Optimization in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.lightning.meta/lightning/controllers_server_actions_boxcar_dynamic.htm) _Lightning Aura Components_
_Developer Guide_ .

The default value is `false` .

`canConfirmEmailChangeInLightningCommunities` boolean If **Require email confirmations for email address changes**
is enabled ( `true` ), when users change their email address, they

receive an email at the new address with a link. After they click
the link, their new email address takes effect. For orgs created
before Winter ’20, the field isn’t enabled by default. For new
orgs, this field is always enabled. To disable the field (not
recommended), contact Salesforce Customer Support. Available
in API version 47.0 and later.

`canConfirmIdentityBySmsOnly` boolean Prevents identity verification by email for users who have
registered other verification methods, such as SMS or Salesforce

Authenticator. If no other verification methods are configured,
users are verified by email.

By default, this setting is disabled ( `false` ) for existing orgs.
For new orgs, this setting is enabled ( `true` ) by default.
Available in API version 48.0 and later.

`disableTimeoutWarning` boolean Indicates whether the session timeout warning popup is
disabled ( `true` ) or enabled ( `false` ).

`enableBuiltInAuthenticator` boolean Indicates whether users can verify their identity with a built-in
authenticator that's already on their device ( `true` ), such as

Touch ID or Windows Hello, or not ( `false` ). The default value
is `false` .

`enableCSPOnEmail` boolean Indicates whether a content security policy is enabled for the
email template. A content security policy helps prevent


Metadata Types SecuritySettings

**Field** **Field Type** **Description**

cross-site scripting attacks by listing allowed sources of images
and other content.

`enableCSRFOnGet` boolean

`enableCSRFOnPost` boolean

`enableCacheAndAutocomplete` boolean

Indicates whether Cross-Site Request Forgery (CSRF) protection
on GET requests on non-setup pages is enabled ( `true` ) or
disabled ( `false` ).

Indicates whether Cross-Site Request Forgery (CSRF) protection
on POST requests on non-setup pages is enabled ( `true` ) or
disabled ( `false` ).

Indicates whether the user’s browser is allowed to store
usernames and auto-fill the `User Name` field on the login
page ( `true` ) or not ( `false` ).

`enableClickjackNonsetupSFDC` boolean Indicates whether clickjack protection for non-setup Salesforce
pages is enabled ( `true` ) or disabled ( `false` ).

`enableClickjackNonsetupUser` boolean

`enableClickjackNonsetupUserHeaderless` boolean

Indicates whether clickjack protection for customer Visualforce
pages with standard headers turned on is enabled ( `true` ) or
disabled ( `false` ).

Indicates whether clickjack protection for customer Visualforce
pages with standard headers turned off is enabled ( `true` ) or
disabled ( `false` ). Available in API version 34.0 and later.

`enableClickjackSetup` boolean Indicates whether clickjack protection for setup pages is enabled
( `true` ) or disabled ( `false` ).

`enableContentSniffingProtection` boolean

`enableLightningLogin` boolean

`enableLightningLoginOnlyWithUserPerm` boolean

Indicates whether the browser is prevented from inferring the
MIME type from the document content and from executing
malicious files (JavaScript, Style sheet) as dynamic content.

This field is available in API version 39.0 and later. In API version
58.0 and later, `enableContentSniffingProtection`
is always `true` .

If enabled ( `true` ), users can use Lightning Login (Salesforce
Authenticator) to log in instead of a password. Available in API
Version 47.0 and later.

If enabled ( `true` ), only users with the Lightning Login User
permission can log in with Salesforce Authenticator instead of
a password. Available in API version 47.0 and later.

`enableMFADirectUILoginOptIn` boolean Requires all users in your Salesforce org to provide an additional
verification method when logging in directly to the UI with their

username and password. Users who are already enabled via
the Multi-Factor Authentication for User Interface Logins user
permission experience no change. The Waive Multi-Factor
Authentication for Exempt Users user permission overrides this
setting.


Metadata Types SecuritySettings

**Field** **Field Type** **Description**

`enableOauthCorsPolicy` boolean

If set to `true`, enables Cross-Origin Resource Sharing (CORS)
for these OAuth endpoints:

**•** `/services/oauth2/token`

**•** `/services/oauth2/revoke`

**•** `/services/oauth2/introspect`

Default setting is `false` . Available in API version 50.0 and
later.

`enablePostForSessions` boolean Indicates whether cross-domain session information is
exchanged using a POST request instead of a GET request, such

as when a user is using a Visualforce page. In this context, POST
requests are more secure than GET requests. Available in API
version 31.0 and later.

`enableSMSIdentity` boolean If enabled ( `true` ), the default, users can receive a one-time
password in a text message (SMS) to verify their identity. Users

must verify their mobile phone number before they can receive
SMS messages.

`enableU2F` boolean If enabled ( `true` ), users can use a physical U2F-compatible
security key for multi-factor authentication (MFA) and identity

verification. The default is `false` . Available in API version 47.0
and later.

`enableUpgradeInsecureRequests` boolean

`enableXssProtection` boolean

Indicates whether HTTPS is required for connecting to
third-party domains.

This setting is enabled by default on accounts created after the
Summer ’17 release.

This field is available in API version 42.0 to 60.0.

Indicates whether the HTTP `X-XSS-Protection` response
header is enabled to protect against reflected cross-site scripting
attacks.

This field is available in API version 39.0 to 59.0. The HTTP
`X-XSS-Protection` response header is deprecated. To
help prevent cross-site scripting (XSS) and other code injection
[attacks, use the CSPTrustedSite metadata type.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_csptrustedsite.htm)

`enforceIpRangesEveryRequest` boolean If `true`, the IP addresses in Login IP Ranges are enforced when
a user accesses Salesforce (on every page request), including

access from a client app. If `false`, the IP addresses in Login
IP Ranges are enforced only when a user logs in. This field affects
all user profiles with login IP restrictions. Available in API version
34.0 and later.


Metadata Types SecuritySettings

**Field** **Field Type** **Description**

`enforceUserDeviceRevoked` boolean

If enabled, and a UserDevice’s status is set to revoked, that
device can’t log in from a Salesforce app. Logins from browsers
aren’t affected.

This field is available in API version 50.0 and later.

`forceLogoutOnSessionTimeout` boolean If enabled ( `true` ), the default, when sessions time out for
inactive users, current sessions become invalid. The browser

refreshes and returns to the login page. To access the org, the
user must log in again. Available in API version 31.0 and later.

`forceRelogin` boolean If `true`, an admin who is logged in as another user must log
in again to their original session, after logging out as the

secondary user. If `false`, the admin isn’t required to log in
again.

`hasRetainedLoginHints` boolean If you enable **Remember me until logout** ( `true` ), usernames
(login hints) are cached until the user logs out. If a session times

out, usernames appear on the Switcher as inactive. If `false`
(default), usernames aren't cached for SSO sessions.

`hasUserSwitching` boolean If **Enable user switching** is `true` (default), users can log in to
other orgs by selecting their profile picture and using the

Switcher. You must also enable the **Enable caching and**
**autocomplete on login page** setting.

If `false`, the Switcher isn’t enabled and your org doesn’t
appear in Switchers on other orgs.

`hstsOnForcecomSites` boolean

`identityConfirmationOnEmailChange` boolean

`identityConfirmationOnTwoFactorRegistrationEnabled` boolean

Indicates whether Visualforce, Salesforce sites, or Experience
Cloud sites must use HTTPS. Available in API version 41.0 and
later.

Indicates whether a user’s identity is confirmed when changing
their email address, instead of requiring a relogin.

This field is available in API version 42.0 and later.

Indicates whether users are required to confirm their identities
when adding a verification method such as Salesforce

Authenticator for multi-factor authentication (MFA), instead of
requiring a relogin. (Multi-factor authentication was formerly
called two-factor authentication.)

This field is available in API version 40.0 and later.

`lockSessionsToDomain` boolean Indicates whether the current UI session for a user is associated
with a specific domain. This check helps prevent unauthorized

use of the session ID in another domain. The value is `true` by
default for orgs created with the Spring ’15 release or later.
Available in API version 33.0 and later.


Metadata Types SecuritySettings

**Field** **Field Type** **Description**

`lockSessionsToIp` boolean Indicates whether user sessions are locked to the IP address
from which the user logged in ( `true` ) or not ( `false` ).

`lockerServiceAPIVersion` string The API version that Lightning Locker enforces for security of
custom Lightning components. The default value matches the

Salesforce API version of the current release. Only valid
Salesforce API versions between 46.0 and the current release
can be specified. The version must be specified as a string in
the format `"` _**`nn`**_ `.0"`, such as `"48.0"` . This setting has no
effect on the `lockerServiceNext` setting, which enables
Lightning Web Security.

This field is available in API version 47.0 and later.

`lockerServiceCSP` boolean If `true`, a stricter Content Security Policy is enabled to disallow
the `unsafe-inline` source for the `script-src` CSP

directive. Script tags can’t be used to load JavaScript, and event
handlers can’t use inline JavaScript. Lightning Locker and
Lightning Web Security depend on this setting to be enabled
to protect Lightning components.

`lockerServiceNext` boolean If `true`, Lightning Web Security is used instead of Lightning
Locker to protect Lightning web components. Lightning Locker

continues to protect Aura components. If `false`, Lightning
Locker protects Lightning web components and Aura
components. Available in API version 53.0 and later.

`lockerServiceNextControl` boolean Reserved for internal use.

`lockerTrustedMode` boolean Reserved for internal use.

`lockerTrustedResources` string Reserved for internal use.

`logoutURL` string The URL to which users are redirected when they log out of
Salesforce. If no value is specified, the default is

`https://` _`MyDomainName`_ `.my.salesforce.com` .
Available in API version 34.0 and later.

`redirectBlockModeEnabled` boolean If `true`, users can’t access untrusted URLs outside the
Salesforce domains via links in URL or Long Text Area fields.

When a user who accesses Salesforce via Salesforce Classic clicks
the link, a message informs the user that they can’t access the
page because the external site isn’t trusted. The default is
`false` .

To specify the URLs that you trust, use the RedirectWhitelistUrl
Metadata type.

The `redirectBlockModeEnabled` and
`redirectionWarning` fields are mutually exclusive. Only
one of those fields can be `true` .

Available in API 56.0 and later.


Metadata Types SecuritySettings

**Field** **Field Type** **Description**

`redirectionWarning` boolean If `true`, users who accesses Salesforce via Salesforce Classic
see an alert when they click a link in a URL or Long Text Area

field that redirects them to an untrusted URL outside the
Salesforce domains. The default is `true` in orgs created in
Spring ’18 and later and `false` in orgs created in Winter ’18
and earlier.

To specify the URLs that you trust, use the RedirectWhitelistUrl
Metadata type.

The `redirectBlockModeEnabled` and
`redirectionWarning` fields are mutually exclusive. Only
one of those fields can be `true` .

Available in API version 42.0 and later.

`referrerPolicy` boolean If `true`, pages served by Salesforce for this org include the
`referrer-policy` HTTP header with the directive defined

by `referrerPolicyDirective` . If `false`, that HTTP
header isn’t included and requests can always see the full URL
of the Salesforce page. The default is `true` . Available in API
version 42.0 and later.

In API version 42.0–57.0, if `referrerPolicy` is `true`,
pages served by Salesforce for this org include the
`referrer-policy` HTTP header with the
`origin-when-cross-origin` directive.

```
referrerPolicyDirective

```

ReferrerPolicy The HTTP referrer policy directive for pages served by Salesforce.
(enumeration The default is `strict-origin-when-cross-origin` .
of type string) If `referrerPolicy` is `false`, this value has no effect.

Available in API version 58.0 and later.

Valid current values are:

**•** `no-referrer` —Never include the referrer.

**•** `origin` —Always send the origin only.

**•** `same-origin` —Omit the referrer for cross-origin
requests.

**•** `strict-origin` —For requests with the same protocol
level (HTTPS to HTTPS), send the origin only. Omit the
referrer when the target website is on a downgraded
protocol. An example of a downgraded protocol is a request
made from an HTTPS URL to an HTTP site.

**•** `strict-origin-when-cross-origin` —For
same-origin requests, send the full referrer URL. For
cross-origin requests with the same protocol level (HTTPS
to HTTPS), send the origin only. Omit the referrer when the
target website is on a downgraded protocol. This is the
default.


Metadata Types SecuritySettings

**Field** **Field Type** **Description**

These policies are deprecated. Although the values are valid,
they aren’t recommended.

**•** `no-referrer-when-downgrade` —Omit the referrer
when the target website is on a downgraded protocol. For
example, when making a request to an HTTP site from an
HTTPS URL.

This `referrerPolicyDirective` isn’t
recommended because this policy exposes the full URL of
the page to cross-origin requests to the same or a higher
protocol level. For example, requests from HTTPS to HTTPS
and requests from HTTP to either HTTP or HTTPS.

**•** `origin-when-cross-origin` —Send the origin
only for cross-domain requests or when the target website
is on a downgraded protocol. An example of a downgraded
protocol is a request made from an HTTPS URL to an HTTP
site.

This `referrerPolicyDirective` isn’t
recommended because multiple browsers no longer
support it. Use
`strict-origin-when-cross-origin` instead.

**•** `unsafe-url` —Always include the full referrer URL.

This `referrerPolicyDirective` isn’t
recommended because this policy exposes the full URL of
the page to requests from insecure origins.

For more information on HTTP referrer policy directives,
[including examples, see the Referrer-Policy entry in the](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy) _MDN_
_Docs HTTP Guide_ .

`requireHttpOnly` boolean

`requireHttps` boolean

Sets the `HttpOnly` attribute on session cookies, making them
inaccessible via JavaScript. If `true`, session ID cookie access is
restricted. If `false`, access is restricted.

If you have a custom or packaged application that uses
JavaScript to access session ID cookies, your application breaks

if `requireHttpOnly` is set to `true` . The application can't
access the cookie.

This field is available in API version 40.0 and later.

Determines whether HTTPS is required to log in to or access
Salesforce. This option is enabled by default for security reasons

and can’t be disabled. To change to HTTP, contact Salesforce
Customer Support.

This field is available in API version 40.0 to 60.0.


Metadata Types SecuritySettings

**Field** **Field Type** **Description**

`securityCentralKillSession` boolean Deprecated in API version 36.0 to 50.0. Removed in API version
51.0 and later.

```
sessionTimeout

```

SessionTimeout
(enumeration
of type string)

`sidToken3rdPartyAuraApp` boolean

`skipSFAWhenMFADirectUILogin` boolean

`terminateUserSessionsWhenAdminResetsPassword` boolean

The length of time after which users without activity are
prompted to log out or continue working. Valid values are:

**•** `FifteenMinutes`

**•** `ThirtyMinutes`

**•** `SixtyMinutes`

**•** `NinetyMinutes` —Available in API version 58.0 and
later.

**•** `TwoHours`

**•** `FourHours`

**•** `EightHours`

**•** `TwelveHours`

**•** `TwentyFourHours` —Available in API version 38.0 and
later.

If `true`, a Lightning app replaces the authentication cookie
with a session token when the Lightning app is in a third-party
context, such as Lightning Out.

Browsers are restricting the use of third-party cookies. This org
setting is an alternative for the authentication cookie to

requiring that users disable browser settings, such as Safari’s
`Prevent cross-site tracking` setting.

This field is available in API version 59.0 and later.

Indicates which screen users see first when they're prompted
to register a verification method for multi-factor authentication
(MFA).

If `true`, users see a list of all supported verification methods.

If `false`, users see only the Salesforce Authenticator option.
To see a list of all supported verification methods, users must
navigate to a new page.

Indicates what happens to a user's UI sessions when an admin
resets that user's password. If `true`, all of the user's UI sessions
are terminated. If `false`, no UI sessions are terminated.

The redirection behavior when a user who accesses Salesforce
via Lightning Experience clicks a hyperlink in a URL field with a
target URL that isn’t trusted. Valid values are:

**•** `AlwaysAllowed`

**•** `NeverAllowed`

```
untrustedRedirect

```

untrustedRedirect
(enumeration
of type string)


Metadata Types SecuritySettings

**Field** **Field Type** **Description**

**•** `WithUserPermission`

To specify the URLs that you trust, use the RedirectWhitelistUrl
Metadata type.

Available in API version 64.0 and later.

Secure redirections to untrusted URLs in Lightning Experience
is a pilot or beta service that is subject to the Beta Services Terms
[at Agreements - Salesforce.com or a written Unified Pilot](https://www.salesforce.com/company/legal/agreements/)
Agreement if executed by Customer, and applicable terms in
[the Product Terms Directory. Use of this pilot or beta service is](https://ptd.salesforce.com/)
at the Customer's sole discretion.

`useLocalStorageForLogoutUrl` boolean

`welcomeEmailTemplateId` string

SingleSignOnSettings

Redirects all expired tabs in your browser to your custom logout
URL ( `true` ). By default, this option is enabled for all new orgs
and is available in API version 52.0 and later.

For orgs created prior to the Summer ’21 release, the default
setting is `false` . Before enabling this setting, review these
considerations.

**•** This setting uses the browser’s local storage to store the
custom logout URL.

**•** Verify that this setting doesn’t interfere with your custom
login integrations.

Custom email template for the welcome email that new internal
users receive when they're registered. This field supports only
Classic email templates.

Available in API version 63.0 and later.

Represents your org’s single sign-on (SSO) settings. These settings are available API version 47.0 and later.

**Field Name** **Field Type** **Description**

`enableCaseInsensitiveFederationID` boolean If you enable **Make Federation ID case-insensitive** ( `true` ),
the Federation ID field on a user object isn’t case-sensitive. If

disabled ( `false` ), the Federation ID field remains case-sensitive.
The default is `false` .

`enableForceDelegatedCallout` boolean If you enable **Force Delegated Authentication Callout**
( `true` ), a callout to the SSO endpoint occurs regardless of login

restriction failures. If disabled ( `false` ), the default, and if a
user’s first login attempt fails due to login restrictions within the
Salesforce org, a call isn’t made to the SSO endpoint.


Metadata Types SecuritySettings

**Field Name** **Field Type** **Description**

`enableMultipleSamlConfigs` boolean If `true` (default), you can configure multiple SAML providers.
After enabling the setting, it can’t be disabled.

`enableSamlJitProvisn’tioning` boolean If you enable **User Provisioning Enabled** ( `true` ), you can
provision users through a SAML assertion (called just-in-time

provisioning). Requires `EnableSamlLogin` to be `true`
and `enableMultipleSamlConfigs` to be `false` . The
default is enabled ( `false` ).

`enableSamlLogin` boolean

`isLoginWithSalesforceCredentialsDisabled` boolean

Declarative Metadata Sample Definition

Here’s a sample `security.settings` metadata file.

If you enable **SAML Enabled** ( `true` ), users can SSO into
Salesforce from providers via SAML. The default isn’t enabled
( `false` ).

If **Disable login with Salesforce credentials** is `true`, users
are redirected to third-party identity providers for authentication.
The default is enabled ( `false` ).

If you enabled this feature prior to the Summer ’20 release and
want to disable it prior to July 27, 2020, contact Customer
Support.

```
<?xml version="1.0" encoding="UTF-8"?>

<SecuritySettings xmlns="http://soap.sforce.com/2006/04/metadata"

xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

   <canUsersGrantLoginAccess>true</canUsersGrantLoginAccess>

   <enableAdminLoginAsAnyUser xsi:nil="true"/>

   <enableAuditFieldsInactiveOwner xsi:nil="true"/>

   <enableAuraSecureEvalPref xsi:nil="true"/>

   <enableCoopHeader>true</enableCoopHeader>

   <enableCoepHeader>false</enableCoepHeader>

   <enableCrossOrgRedirects>false</enableCrossOrgRedirects>

   <enablePermissionsPolicy>true</enablePermissionsPolicy>

   <grantCameraAccess>TrustedUrls</grantCameraAccess>

   <grantMicrophoneAccess>TrustedUrls</grantMicrophoneAccess>

   <networkAccess/>

   <passwordPolicies>

     <complexity>NoRestriction</complexity>

     <expiration>Never</expiration>

     <historyRestriction>0</historyRestriction>

     <lockoutInterval>FifteenMinutes</lockoutInterval>

     <maxLoginAttempts>TenAttempts</maxLoginAttempts>

     <minimumPasswordLength>5</minimumPasswordLength>

     <minimumPasswordLifetime>false</minimumPasswordLifetime>

     <obscureSecretAnswer>false</obscureSecretAnswer>

     <questionRestriction>DoesNotContainPassword</questionRestriction>

   </passwordPolicies>

   <redirectBlockModeEnabled>false</redirectBlockModeEnabled>

```


Metadata Types SecuritySettings

```
      <sendCspForUncommonClients>false</sendCspForUncommonClients>

      <sessionSettings>

       <allowUserAuthenticationByCertificate>false</allowUserAuthenticationByCertificate>

        <disableTimeoutWarning>false</disableTimeoutWarning>

        <enableBuiltInAuthenticator>false</enableBuiltInAuthenticator>

        <enableCSPOnEmail>true</enableCSPOnEmail>

        <enableCSRFOnGet>true</enableCSRFOnGet>

        <enableCSRFOnPost>true</enableCSRFOnPost>

        <enableCacheAndAutocomplete>true</enableCacheAndAutocomplete>

        <enableClickjackNonsetupSFDC>true</enableClickjackNonsetupSFDC>

        <enableClickjackNonsetupUser>false</enableClickjackNonsetupUser>

       <enableClickjackNonsetupUserHeaderless>false</enableClickjackNonsetupUserHeaderless>

        <enableClickjackSetup>true</enableClickjackSetup>

        <enableContentSniffingProtection>true</enableContentSniffingProtection>

        <enableLightningLogin>true</enableLightningLogin>

       <enableLightningLoginOnlyWithUserPerm>false</enableLightningLoginOnlyWithUserPerm>

        <useLocalStorageForLogoutUrl>false</useLocalStorageForLogoutUrl>

        <enableOauthCorsPolicy>false</enableOauthCorsPolicy>

        <enablePostForSessions>false</enablePostForSessions>

        <enableSMSIdentity>true</enableSMSIdentity>

        <enableU2F>false</enableU2F>

        <enforceIpRangesEveryRequest>false</enforceIpRangesEveryRequest>

        <enforceUserDeviceRevoked>false</enforceUserDeviceRevoked>

        <forceLogoutOnSessionTimeout>true</forceLogoutOnSessionTimeout>

        <forceRelogin>true</forceRelogin>

        <hasRetainedLoginHints>false</hasRetainedLoginHints>

        <hasUserSwitching>true</hasUserSwitching>

        <hstsOnForcecomSites>false</hstsOnForcecomSites>

        <identityConfirmationOnEmailChange>true</identityConfirmationOnEmailChange>

   <identityConfirmationOnTwoFactorRegistrationEnabled>true</identityConfirmationOnTwoFactorRegistrationEnabled>

        <lockSessionsToDomain>true</lockSessionsToDomain>

        <lockSessionsToIp>false</lockSessionsToIp>

        <lockerServiceAPIVersion>56.0</lockerServiceAPIVersion>

        <lockerServiceCSP>true</lockerServiceCSP>

        <lockerServiceNext>true</lockerServiceNext>

        <logoutURL>https://mycompany.com</logoutUrl>

        <redirectionWarning>true</redirectionWarning>

        <referrerPolicy>true</referrerPolicy>

       <referrerPolicyDirective>strict-origin-when-cross-origin</referrerPolicyDirective>

        <requireHttps>false</requireHttps>

        <sessionTimeout>TwoHours</sessionTimeout>

        <untrustedRedirect>WithUserPermission</untrustedRedirect>

        <useLocalStorageForLogoutUrl>true</useLocalStorageForLogoutUrl>

        <welcomeEmailTemplateId>X000000000000</welcomeEmailTemplateId>

      </sessionSettings>

      <singleSignOnSettings>

        <enableCaseInsensitiveFederationID>false</enableCaseInsensitiveFederationID>

        <enableForceDelegatedCallout>false</enableForceDelegatedCallout>

        <enableMultipleSamlConfigs>true</enableMultipleSamlConfigs>

```


#### Metadata Types ServiceCloudVoiceSettings

```
        <enableSamlJitProvisioning>false</enableSamlJitProvisioning>

        <enableSamlLogin>false</enableSamlLogin>

   <isLoginWithSalesforceCredentialsDisabled>true</isLoginWithSalesforceCredentialsDisabled>

      </singleSignOnSettings>

   </SecuritySettings>

```

The following is an example `package.xml` manifest that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Security</members>

        <name>Settings</name>

      </types>

      <version>65.0</version>

   </Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### ServiceCloudVoiceSettings

Represents an organization’s Service Cloud Voice settings.

This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.

File Suffix and Directory Location

#### ServiceCloudVoiceSettings values are stored in the ServiceCloudVoice.settings file in the settings folder. The

`.settings` files are different from other named components because there’s only one settings file for each settings component.

Version

#### ServiceCloudVoiceSettings is available in API versions 52.0 and later.

Fields

**Field Name** **Field Type** **Description**

`disableSCVTaskCreationForHVS` boolean Indicates whether to prevent the Sales Engagement automatic task
creation feature from generating tasks from voice calls except click-to-dial

calls initiated from Sales Engagements, To Do List, and Work Queue. The
default value is `false` . Available in API version 61.0 and later. This field
is optional.


Metadata Types ServiceCloudVoiceSettings

**Field Name** **Field Type** **Description**

`enableAmazonQueueManagement` boolean Indicates whether to enable the Amazon Connect queue management
integration for Service Cloud Voice. When enabled, the system

automatically synchronizes contact center queues across Salesforce and
Amazon Connect, including voice groups and users. The default value
is `false` . Available in API version 55.0 and later. This field is optional.

`enableDefaultChannelForSCV` boolean

Indicates whether Service Cloud Voice uses the default phone channel
for all end user identification. The default value is `false` . Available in
API version 53.0 and later. This field is optional.

`enableDigitalVoiceWhatsapp` boolean Reserved for internal use.

`enableEndUserForSCV` boolean

Indicates whether Service Cloud Voice matches callers to end user
records. The default value is `false` . Available in API version 53.0 and
later. This field is optional.

`enableOmniCapacityForSCV` boolean Indicates whether to enable Omni-Channel capacity management for
Service Cloud Voice. If enabled, Service Cloud Voice Agentwork honors

Omni-Channel capacity. The default value is `false` . Available in API
version 54.0 and later. This field is optional.

`enablePhoneNumberMaskingForSCV` boolean Indicates whether to enable phone number masking functionality in
Service Could Voice to protect sensitive data by redacting inbound and

outbound phone numbers. When enabled, phone numbers are masked
in Omni-Channel views, call recordings, and call transcripts. Masking
doesn't apply to numbers used in rep-to-rep calls managed by partner
telephony providers. The default value is `false` . Available in API version
61.0 and later. This field is optional.

`enablePTQueueManagement` boolean Indicates whether to enable queue management for Service Cloud Voice
with Partner Telephony. When enabled, the system automatically

synchronizes contact center queues across Salesforce and partner
telephony services, including groups and users. The default value is
`false` . Available in API version 56.0 and later. This field is optional.

`enableRZoneCloudVoiceOptIn` boolean

`enableSCVASAContextLinkingEnabled` boolean

Indicates whether you agree to the terms of using Service Cloud Voice
with Amazon Connect in a Salesforce Government Cloud environment.
The default value is `false` . This field is optional.

Amazon Connect is a third-party Amazon service that sits outside the
Salesforce Government Cloud FedRAMP environment. Amazon Connect
is a separate service offered by Amazon and not a FedRAMP authorized
service. Therefore, Amazon Connect’s processing environment falls
outside the Government Cloud FedRAMP authorization boundary. To
[learn more, see Amazon Connect.](https://aws.amazon.com/connect/)

Indicates whether to link related voice calls, specifically the partner
telephony/rep call and the voice-enabled agent (PSTN Voice) call.
Available in API version 65.0 and later. This field is optional.


#### Metadata Types ServiceSetupAssistantSettings

**Field Name** **Field Type** **Description**

`enableSCVBYOT` Indicates whether to enable Service Cloud Voice with Partner Telephony.
The default value is `false` . This field is optional. For API version 52.0

and later, we recommend using `enableSCVExternalTelephony`
instead.

`enableSCVExternalTelephony` boolean

`enableSCVOpenVCAsNewTabHVS` boolean

`enableSCVSupportBannerDisplayed` boolean

Indicates whether to enable a third-party telephony service to work with
Service Cloud Voice with Partner Telephony. The default value is `false` .
This field is optional.

Indicates whether to open the Service Cloud Voice Console in a new tab
for Sales Engagement scenarios. The default value is `false` . Available
in API version 62.0 and later. This field is optional.

Indicates whether to display the Service Cloud Voice support banner.
The default value is `false` . Available in API version 59.0 and later. This
field is optional.

`enableServiceCloudVoice` boolean Indicates whether to enable Service Cloud Voice with Amazon Connect.
The default value is `false` . This field is optional.

Declarative Metadata Sample Definition

The following is an example of a ServiceCloudVoice.settings component.

```
<?xml version="1.0" encoding="UTF-8"?>

<ServiceCloudVoiceSettings xmlns="http://soap.sforce.com/2006/04/metadata">

 <enableServiceCloudVoice>true</enableServiceCloudVoice>

</ServiceCloudVoiceSettings>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>ServiceCloudVoice</members>

     <name>Settings</name>

   </types>

   <version>52.0</version>

</Package>

#### ServiceSetupAssistantSettings

```

Represents an organization’s Service Setup Assistant settings. The Service Setup Assistant can be used to set up a basic service console
app.

This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.


#### Metadata Types SharingSettings

File Suffix and Directory Location

ServiceSetupAssistantSettings values are stored in the `ServiceSetupAssistant.settings` file in the `settings` directory.
The `.settings` files are different from other named components because there’s only one settings file for each settings component.

Version

ServiceSetupAssistantSettings components are available in API version 50.0 and later.

Fields

**Field Name** **Field Type** **Description**

`enableServiceSetupAssistant` boolean Indicates whether the Service Setup Assistant is enabled ( `true` ) or not
( `false` ).

Declarative Metadata Sample Definition

The following is an example of a ServiceSetupAssistantSettings component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <ServiceSetupAssistantSettings xmlns="http://soap.sforce.com/2006/04/metadata">

    <enableServiceSetupAssistant>true</enableServiceSetupAssistant>

   </ServiceSetupAssistantSettings>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### SharingSettings

Represents an organization’s sharing, visibility, and data access settings. This type extends the Metadata metadata type and inherits its
`fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.

File Suffix and Directory Location

#### SharingSettings values are stored in the Sharing.settings file in the settings directory. The .settings files are different

from other named components because there’s only one settings file for each settings component.

Version

#### SharingSettings is available in API version 47.0 and later.


Metadata Types SharingSettings

Special Access Rules

To use SharingSettings, you need the Manage Sharing permission.

Fields

**Field Name** **Field Type** **Description**

`deferGroupMembership` boolean

`deferSharingRules` boolean

Indicates whether group membership calculations are suspended ( `true` )
or not ( `false` ). This field has a default value of `false` . This field is
available in API version 49.0 and later.

Important:

**•** The defer sharing calculation feature isn't enabled by default.
To enable it for your Salesforce org, contact Salesforce
Customer Support.

**•** When you change the value of this field from `true` to
`false`, group membership is automatically recalculated.
Sharing rules are also automatically recalculated, unless the
`deferSharingRules` field is set to `true` prior to
modifying `deferGroupMembership` . Depending on
your org, these recalculations can take a significant amount
of time to complete.

**•** If the `deferGroupMembership` field is set to `true`,
you can’t change the value of `deferSharingRules` .
Sharing rule calculations are suspended regardless of the
value of `deferSharingRules` .

Indicates whether sharing rule calculations are suspended ( `true` ) or
not ( `false` ). This field has a default value of `false` . This field is
available in API version 49.0 and later.

Important:

**•** The defer sharing calculation feature isn't enabled by default.
To enable it for your Salesforce org, contact Salesforce
Customer Support.

**•** When you change the value of this field from `true` to
`false`, sharing rules are automatically recalculated.
Depending on your org, this recalculation can take a
significant amount of time to complete.

**•** If the `deferGroupMembership` field is set to `true`,
you can’t change the value of `deferSharingRules` .
Sharing rule calculations are suspended regardless of the
value of `deferSharingRules` .


Metadata Types SharingSettings

**Field Name** **Field Type** **Description**

`enableAccountRoleOptimization` boolean

`enableAssetSharing` boolean

Indicates whether person roles are assigned to new site users in accounts
without existing users ( `true` ) or if regular site roles are created for new
users ( `false` ). This field has a default value of `false` .

Indicates whether sharing is enabled for assets ( `true` ) or asset access
is determined by the parent object’s sharing rules ( `false` ). This field
has a default value of `false` .

`enableCommunityUserVisibility` boolean Indicates whether site users in the same site can see each other regardless
of the organization-wide defaults ( `true` ) or not ( `false` ). This field has

a default value of `false` . In orgs created in API version 47.0 and later,
this setting doesn’t apply to guest users.

`enableExternalSharingModel` boolean Indicates whether the external sharing model is enabled ( `true` ) or not
( `false` ). This field has a default value of `true` if Salesforce Experiences

are enabled, and a default value of `false` if not. To use this field, you
need the Customize Application permission.

`enableManagerGroups` boolean Indicates whether users can share records with their managers and
manager subordinates groups ( `true` ) or not ( `false` ). This field has a

default value of `false` . To use this field, you need the View and Manage
Users permission.

`enableManualUserRecordSharing` boolean Indicates whether users can share their own user record ( `true` ) or not
( `false` ). This field has a default value of `false` .

`enablePartnerSuperUserAccess` boolean

`enablePortalUserCaseSharing` boolean

Indicates whether you can grant super user access to partners in sites
( `true` ) or not ( `false` ). This field has a default value of `false` . To use
this field, you need the Customize Application permission

Indicates whether portal users can access related contacts for cases that
they own ( `true` ) or not ( `false` ). This field has a default value of
`false` .

`enablePortalUserVisibility` boolean Indicates whether portal users in the same customer or partner portal
account can see each other regardless of the organization-wide defaults

( `true` ) or not ( `false` ). This field has a default value of `false` . To
enable this field, contact Salesforce Support.

`enableRemoveTMGroupMembership` boolean Removes group membership info for the original territory management
feature after migrating to Sales Territories when set to `true` . This field

has a default value of `false` . Once this field is set to `true`, it can't be
set to `false` again.

`enableRestrictAccessLookupRecords` boolean Indicates whether users must have read access to a record to see the
record’s name in lookup and system fields ( `true` ) or not ( `false` ). This

field has a default value of `true` in Salesforce orgs created in Spring
’20 or later and a default value of `false` in all other orgs. This field is
available in API version 48.0 and later.


Metadata Types SharingSettings

**Field Name** **Field Type** **Description**

`enableSecureGuestAccess` boolean

`enableStandardReportVisibility` boolean

`enableTerritoryForecastManager` boolean

When `true`, guest users have org-wide defaults set to Private. To share
records with them, you must use guest user sharing rules.

As of API version 50.0, this field's value is always `true`, regardless of
the value that you set. Changing its value has no effect on Salesforce,
even if it reads `false` .

This change applies retroactively back to API version 47.0, when this field
was first introduced. Previously, in API version 47.0 to 49.0, this field
indicated whether guest users’ record access is secured ( `true` ) or not
( `false` ), and the field's default value was `false` . Now, in all API
versions, this field's value is always `true`, even if it reads `false` .

Indicates whether users can view reports based on standard report types
that may expose data of users to whom they don't have access ( `true` )
or not ( `false` ). This field has a default value of `false` .

Indicates whether forecast managers can act as delegated administrators
for territories below them in the hierarchy ( `true` ) or not ( `false` ). This
field has a default value of `false` .

Declarative Metadata Sample Definition

The following is an example of a SharingSettings component.

```
<?xml version="1.0" encoding="UTF-8"?>

<SharingSettings xmlns="http://soap.sforce.com/2006/04/metadata">

   <deferGroupMembership>false</deferGroupMembership>

   <deferSharingRules>false</deferSharingRules>

   <enableAccountRoleOptimization>false</enableAccountRoleOptimization>

   <enableAssetSharing>false</enableAssetSharing>

   <enableCommunityUserVisibility>false</enableCommunityUserVisibility>

   <enableExternalSharingModel>true</enableExternalSharingModel>

   <enableManagerGroups>false</enableManagerGroups>

   <enableManualUserRecordSharing>true</enableManualUserRecordSharing>

   <enablePartnerSuperUserAccess>false</enablePartnerSuperUserAccess>

   <enablePortalUserCaseSharing>false</enablePortalUserCaseSharing>

   <enablePortalUserVisibility>true</enablePortalUserVisibility>

   <enableRemoveTMGroupMembership>false</enableRemoveTMGroupMembership>

   <enableRestrictAccessLookupRecords>true</enableRestrictAccessLookupRecords>

   <enableSecureGuestAccess>true</enableSecureGuestAccess>

   <enableStandardReportVisibility>false</enableStandardReportVisibility>

   <enableTerritoryForecastManager>false</enableTerritoryForecastManager>

</SharingSettings>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>Sharing</members>

     <name>Settings</name>

```


#### Metadata Types SiteSettings

```
      </types>

      <version>47.0</version>

   </Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### SiteSettings

[Represents the settings for Experience Cloud sites and for Salesforce Sites.](https://help.salesforce.com/articleView?id=sites_overview.htm&type=5&language=en_US)

This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.

File Suffix and Directory Location

#### SiteSettings values are stored in a single file named Site.settings in the settings directory. The .settings files are

different from other named components because there’s only one `.settings` file for each settings component.

Version

#### SiteSettings components are available in API version 47.0 and later.

Fields

**Field Name** **Field Type** **Description**

`enableEnhancedSitesAndContentPlatform` boolean Indicates whether the enhanced sites and content platform for
Experience Cloud is enabled for your org ( `true` ) or not ( `false` ). The

default is `true` . When `true`, new LWR sites and enhanced CMS
workspaces are hosted together on a redesigned platform that offers
partial deployment, site content search, and easy content management.
Enhanced LWR sites are represented by the DigitalExperienceBundle
and DigitalExperienceConfig types. Available in API version 56.0 and
later.

`enableExpBuilderCopilot` boolean Enables Agentforce (beta) in Experience Builder for enhanced LWR sites.
The default value is `false` . Available in API 64.0 and later.

Note: Agentforce Experience Builder Agent is a pilot or beta
[service that is subject to the Beta Services Terms at Agreements](https://www.salesforce.com/company/legal/)

[- Salesforce.com or your written Unified Pilot Agreement, and](https://www.salesforce.com/company/legal/)
[following terms in the Product Terms Directory: Non-GA](https://ptd.salesforce.com/?_ga=2.247987783.1372150065.1709219475-629000709.1639001992)
[Agentforce, the Non-GA Open AI LLM Provider and the Non-GA](https://ptd.salesforce.com/?_ga=2.247987783.1372150065.1709219475-629000709.1639001992)
Credit Consumption. Use of this pilot or beta service consumes
Einstein Requests and is at the Customer’s sole discretion.


Metadata Types SiteSettings

**Field Name** **Field Type** **Description**

`enableExperienceFriendlyUrls` boolean Indicates whether SEO-friendly URL snippets, or “slugs,” are enabled for
your org ( `true` ) or not ( `false` ). The default is `false` . When `true`,

available only in B2C Commerce LWR sites. Available only in API version
58.0. In API version 59.0 and later, use
`expFriendlyUrlsAsDefault` in the Network type.

`enableProxyLoginICHeader` boolean

Indicates whether security tokens for API logins from callouts (in API
version 31.0 and earlier) are required ( `true` ) or not ( `false` ). The default
value is `true` .

`enableSitesRecordReassignOrgPref` boolean Deprecated in API version 63.0 and later. When `true`, indicates when
the org assigns records created by guest users of a site to a default owner

in the org. When `false`, the guest user remains the owner of the
record. The default value is `false` . Available in API version 48.0 through
63.0.

`enableTopicsInSites` boolean

Indicates whether guest and authenticated external users can view topics
in Salesforce Sites and Salesforce portals ( `true` ) or not ( `false` ). The
default value is `false` .

`enableVisualforceApiAccessAllowed` boolean Deprecated in API version 52.0 and later. Allow users of Visualforce pages
to override API access control restrictions and access APIs when the

`enableAdminApprovedAppsOnly` in ConnectedAppSettings is
enabled ( `true` ). The default value is `false` .

`enableWebruntimeBYOTemplate` boolean

Indicates whether the Build Your Own (LWC) template is available in
Experience Builder. The default value is `false` . Available in API version
48.0 and later. Removed in API version 51.0.

Declarative Metadata Sample Definition

The following is an example of a SiteSettings component.

```
<?xml version="1.0" encoding="UTF-8"?>

<SiteSettings xmlns="http://soap.sforce.com/2006/04/metadata">

   <enableProxyLoginICHeader>true</enableProxyLoginICHeader>

   <enableTopicsInSites>false</enableTopicsInSites>

</SiteSettings>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>Site</members>

     <name>Settings</name>

   </types>

   <version>47.0</version>

</Package>

```


#### Metadata Types SocialCustomerServiceSettings

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### SocialCustomerServiceSettings

Represents Social Customer Service settings such as how to format inbound content from social posts to cases. This type extends the
Metadata metadata type and inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.

File Suffix and Directory Location

#### SocialCustomerServiceSettings components have the suffix settings and are stored in the settings folder. The .settings

files are different from other named components because there’s only one settings file for each settings component.

Version

#### SocialCustomerServiceSettings is available in API version 41.0 and later.

Fields

**Field Name** **Field Type** **Description**

Required. Specifies an option from which inbound social
content is formatted to appear in case records’ **Case Subject**
field. Valid values are:

**•** `SocialPostSource`

**•** `SocialPostContent`

**•** `BuildCustom`

```
caseSubjectOption

```

CaseSubjectOption
(enumeration of type
string)

`enableAllFBResponseAccounts` boolean Indicates whether responses from all Facebook managed
accounts are enabled. If this setting is disabled, responses to

a Facebook post can only be sent from the account that the
original customer post was directed to. The default value is
`true` . Available in API version 56.0 and later.

`enableSocialApprovals` boolean

Indicates whether social approvals are enabled. To learn more,
[see Enable Social Post Approvals.The default value is](https://help.salesforce.com/articleView?id=social_customer_service_approvals.htm&language=en_US) `false` .
Available in API version 47.0 and later.

`enableSocialCaseAssignmentRules` boolean Indicates whether case assignment rules are enabled. Use
case assignment rules to determine how cases are assigned

to users or put into queues as they are created. The default
value is `false` . Available in API version 47.0 and later.


Metadata Types SocialCustomerServiceSettings

**Field Name** **Field Type** **Description**

`enableSocialCustomerService` boolean

Indicates whether to enable the Social Customer Service
feature. The default value is `false` . Available in API version
47.0 and later.

`enableSocialPersonaHistoryTracking` boolean Indicates whether to enable Social Persona history tracking.
History tracking helps identify who made what changes

when, and for differentiating between automatic and manual
changes. The default value is `false` . Available in API version
47.0 and later.

`enableSocialPostHistoryTracking` boolean Indicates whether to enable Social Post history tracking.
History tracking helps identify who made what changes

when, and for differentiating between automatic and manual
changes. The default value is `false` . Available in API version
47.0 and later.

`enableSocialReceiveParentPost` boolean

Declarative Metadata Sample Definition

Indicates whether to use the original social post that initiated
the case as the parent record. The default value is `false` .
Available in API version 47.0 and later.

This is a sample of a `SocialCustomerServiceSettings.settings` file.

```
<?xml version="1.0" encoding="UTF-8"?>

<SocialCustomerServiceSettings xmlns="http://soap.sforce.com/2006/04/metadata">

   <caseSubjectOption>SocialPostSource</caseSubjectOption>

   <enableSocialApprovals>true</enableSocialApprovals>

   <enableSocialCaseAssignmentRules>false</enableSocialCaseAssignmentRules>

   <enableSocialCustomerService>true</enableSocialCustomerService>

   <enableSocialPersonaHistoryTracking>false</enableSocialPersonaHistoryTracking>

   <enableSocialPostHistoryTracking>false</enableSocialPostHistoryTracking>

   <enableSocialReceiveParentPost>true</enableSocialReceiveParentPost>

</SocialCustomerServiceSettings>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

     <members>SocialCustomerService</members>

     <name>Settings</name>

   </types>

   <version>47.0</version>

</Package>

```


#### Metadata Types SocialProfileSettings

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### SocialProfileSettings

Represents org preferences for social media features such as enabling Twitter and Facebook.Represents org preferences for social media
features such as enabling Twitter and Facebook. This type extends the Metadata metadata type and inherits the fullName field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.

File Suffix and Directory Location

#### SocialProfileSettings values are stored in a single file named SocialProfile.settings in the settings directory of the

corresponding package directory. The `.settings` files are different from other named components because there’s only one settings
file for each settings component.

Version

#### SocialProfileSettings is available in API versions 47.0 through 58.0.

Fields

**Field Name** **Field Type** **Description**

`isFacebookSocialProfilesDisabled` boolean

`isLinkedInSocialProfilesDisabled` boolean

`isTwitterSocialProfilesDisabled` boolean

`isYouTubeSocialProfilesDisabled` boolean

Prevents users from accessing Facebook in social CRM ( `true` ) or not
( `false` ). `enableSocialProfiles` must be `true` to enable
Facebook social profiles.

Prevents users from accessing LinkedIn in social CRM ( `true` ) or not
( `false` ). `enableSocialProfiles` must be `true` to enable
LinkedIn social profiles.

Prevents users from accessing Twitter in social CRM ( `true` ) or not
( `false` ). `enableSocialProfiles` must be `true` to enable
Twitter social profiles.

This setting is permanently set to True because Twitter access was
removed in API version 59.0.

Prevents users from accessing YouTube in social CRM ( `true` ) or not
( `false` ). `enableSocialProfiles` must be `true` to enable
YouTube social profiles.

This setting is permanently set to True because YouTube access was
removed in API version 60.0.

`enableSocialProfiles` boolean Indicates whether users can access social media profiles in social CRM
( `true` ) or not ( `false` ).


#### Metadata Types SourceTrackingSettings (Beta)

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### SourceTrackingSettings (Beta)

Represents settings for source tracking, so that changes you make in your Developer and Developer Pro sandboxes or local workspace
can be tracked. This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.

File Suffix and Directory Location

SourceTrackingSettings values are stored in the `SourceTracking.settings` file in the `settings` folder. The `.settings`
files are different from other named components because there is only one settings file for each settings component.

Version

SourceTrackingSettings is available in API version 49.0 and later.

Fields

**Field Name** **Field Type** **Description**

`enableSourceTrackingSandboxes` boolean

Indicates whether to enable source tracking automatically when
Developer or Developer Pro sandboxes are created or refreshed ( `true` )
or not ( `false` ). The default value is `false` .

If you set `enableSourceTrackingSandboxes` back to `false`
after it was enabled, a sandbox that is tracking source changes continues
to do so until it is refreshed.

Note: You don't need to have the Developer Hub (DevHub)
enabled in the same org to enable source tracking.

This field applies to production orgs only; in other orgs, this field is
ignored.

Declarative Metadata Sample Definition

The following is an example of a SourceTrackingSettings component.

```
<?xml version="1.0" encoding="UTF-8"?>

<SourceTrackingSettings xmlns="http://soap.sforce.com/2006/04/metadata">

   <enableSourceTrackingSandboxes>true</enableSourceTrackingSandboxes>

</SourceTrackingSettings>

```


#### Metadata Types SubscriptionManagementSettings

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### SubscriptionManagementSettings

Represents the settings used to manage recurring subscriptions.

Parent Type and Manifest Access

This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all the settings metadata types for the org are accessed using the “Settings” name. See Settings for more details.

File Suffix and Directory Location

#### SubscriptionManagementSettings values are stored in the subscriptionmanagement.settings file in the

`settings` folder. The `.settings` files are different from other named components, because there’s only one settings file for each
settings component.

Version

#### SubscriptionManagementSettings components are available in API version 55.0 and later.

Special Access Rules

This metadata type is available with Subscription Management.

Fields

**Field Name** **Field Type** **Description**

`enableBillingDocGen` boolean Indicates whether document
generation is enabled in the org

( `true` ) or not ( `false` ). The
default value is `false` .

`enableConvert` boolean Indicates whether to convert
`NegativeInvoiceLines` negative invoice lines into a credit
`ToCreditMemoAndApply` note ( `true` ) or not ( `false` ). This
credit note holds a positive
balance that you can later use to
apply against future invoices. The
default value is `false` .

`enableInvHeaderLvlSettlement` boolean Indicates whether payments can
be applied on the whole invoice

( `true` ) or only on invoice lines


Metadata Types SubscriptionManagementSettings

**Field Name** **Field Type** **Description**

( `false` ). The default value is
`false` .

`enablePaymentScheduleAutomation` boolean Indicates whether the payment
schedule and payment schedule

item are created automatically
( `true` ) or not ( `false` ). The
default value is `false` .

`enableRefundAutomation` boolean Indicates whether refunds are
processed automatically ( `true` )

or not ( `false` ). The default value
is `false` .

`enableRevSubMgmtBlngOptOut` boolean Indicates whether the billing
schedules in Subscription

Management are disabled ( `true` )
or not ( `false` ). The default value
is `false` .

`enableSubscriptionManagement` boolean Indicates whether Subscription
Management is enabled ( `true` )

or not ( `false` ). The default value
is `false` .

Declarative Metadata Sample Definition

This example shows a sample SubscriptionManagementSettings component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <SubscriptionManagementSettings xmlns="http://soap.sforce.com/2006/04/metadata">

      <enableSubscriptionManagement>true</enableSubscriptionManagement>

   </SubscriptionManagementSettings>

```

This example shows a sample `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>SubscriptionManagementSettings</members>

        <name>Settings</name>

      </types>

      <version> 66.0 </version>

   </Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The wildcard
applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the manifest
file, see Deploying and Retrieving Metadata with the Zip File.


#### Metadata Types SurveySettings SurveySettings

Represents an org’s survey settings. Use the SurveySettings component to enable Salesforce Surveys, enable Customer Lifecycle Maps,
and choose whether the owner of a survey can manage the responses.

Parent Type and Manifest Access

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

[In the package manifest, all the settings metadata types for the org are accessed using the “Settings” name. See Settings for more details.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_settings.htm)

File Suffix and Directory Location

#### SurveySettings values are stored in a single file named Survey.settings in the settings folder. The .settings

files are different from other named components because there is only one settings file for each settings component.

Version

#### SurveySettings is available in API version 47.0 and later.

Fields

**Field Name** **Field Type** **Description**

`enableGenerativeAISurveys` boolean

Indicates whether AI-Generated Surveys is enabled for your org (true)
or not (false). The default value is `false` . Available in API version 62.0
and later.

`enableIndustriesCxmEnabled` boolean Indicates whether Customer Lifecycle Maps is enabled for your org (true)
or not (false). The default value is `false` .

`enableSurvey` boolean Indicates whether Surveys is enabled for your org (true) or not (false).
The default value is `false` .

`enableSurveyOwnerCanManageResponse` boolean Indicates whether the owner of a survey can manage its responses. The
default value is `false` .

Declarative Metadata Sample Definition

This example shows a sample SurveySettings component.

```
<?xml version="1.0" encoding="UTF-8"?>

<SurveySettingsxmlns="http://soap.sforce.com/2006/04/metadata">

<enableIndustriesCxmEnabled>false</enableIndustriesCxmEnabled>

<enableSurvey>true</enableSurvey>

<enableSurveyOwnerCanManageResponse>false</enableSurveyOwnerCanManageResponse>

<enableGenerativeAISurveys>false</enableGenerativeAISurveys>

</SurveySettings>

```


#### Metadata Types Territory2Settings

This example shows a sample `package.xml` file that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Survey</members>

        <name>Settings</name>

      </types>

      <version> 61.0 </version>

   </Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
[wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/meta_settings.htm)
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

#### Territory2Settings

Represents an org’s Territory2 settings. Use Territory2 settings to set the access level that Sales Territories users have to records associated
with sales territories, and to enable features. The standard record access settings apply to accounts and opportunities. With _`Private`_
default internal access for contacts or cases, you can also set access for those records.

This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.

File Suffix and Directory Location

#### Territory2Settings values are stored in a single file named Territory2.settings in the settings directory of the corresponding

package directory. The `.settings` files are different from other named components because there’s only one settings file for each
settings component.

Version

#### Territory2Settings is available in API version 32.0 and later.

Special Access Rules

Fields

**Field Name** **Field Type** **Description**

`defaultAccountAccessLevel` string

`defaultCaseAccessLevel` string

Sets the default level of access that users have to account records in
territories: _`view`_ and _`edit`_ accounts assigned to territories or _`view`_,
_`edit`_, _`transfer`_, and _`delete`_ accounts assigned to territories.

Sets the default level of access that users have to case records in
territories: _`view`_ and _`edit`_ accounts assigned to territories or _`view`_,
_`edit`_, _`transfer`_, and _`delete`_ accounts assigned to territories.


Metadata Types Territory2Settings

**Field Name** **Field Type** **Description**

`defaultContactAccessLevel` string

`defaultOpportunityAccessLevel` string

Sets the default level of access that users have to contact records in
territories: _`view`_ and _`edit`_ accounts assigned to territories or _`view`_,
_`edit`_, _`transfer`_, and _`delete`_ accounts assigned to territories.

Sets the default level of access that users have to opportunity records
in territories: _`view`_ and _`edit`_ accounts assigned to territories or _`view`_,
_`edit`_, _`transfer`_, and _`delete`_ accounts assigned to territories.

`enableTerritoryManagement2` boolean Enables and disables Sales Territories only. If `true`, Sales Territories is
enabled. If `false` (default), Enterprise Territory Management isn’t

enabled. Enabling and disabling Sales Territories is exclusive of all other
operations, and the field value must be `true` before other
territory-management operations can run.

Available in API version 47.0 and later.

`opportunityFilterSettings` Territory2SettingsOpportunityFilter

`showTM2EnabledBanner` boolean

`supportedObjects` Territory2SupportedObject[]

`t2ForecastAccessLevel` string

`tm2BypassRealignAccInsert` boolean

`tm2EnableUserAssignmentLog` boolean

Optional. Specifies an Apex class to assign territories to opportunities
and whether you want to run it when an opportunity is created. Available
in API version 34.0 and later.

If `true`, a success banner appears on the Territory Settings page in
Setup.

Available in API version 49.0 and later.

Sets the user access levels of all objects that support territory assignments
in the org. Available in API version 57.0 and later.

Sets the access level that users in a parent territory get to the
opportunities assigned to its child territories, regardless of who owns
the opportunities.

Valid values are:

**•** `View`

**•** `Edit`

Available in API version 49.0 and later.

If `true`, account assignment rules don’t run during account insert jobs.

Available in API version 53.0 and later.

If `true`, when a user is assigned to a territory, the assignment action is
logged.

Available in API version 57.0 and later.


Metadata Types Territory2Settings

Territory2SettingsOpportunityFilter

This subtype specifies an Apex class that assigns territories to opportunities. You can run the Apex class automatically every time a user
creates an opportunity, or run it by using multithreading.

**Field Name** **Description**

```
apexClassName

enableFilter

runMultiThreaded

runOnCreate

```

Territory2SupportedObject

**Field Type**
string

**Description**

Represents the Apex class name.

**Field Type**
boolean

**Description**

If `true`, the Apex class is used to assign territories to opportunities.

**Field Type**
boolean

**Description**

Required. If `true`, the Apex class runs by using multithreading, which can improve
performance. Set this value to `true` only if you’re assigning opportunity or opportunity
product splits, and your Apex code can run with multithreading. This field has a default
value of `false` .

Available in API version 62.0 and later.

**Field Type**
boolean

**Description**

If `true`, the Apex class runs automatically every time a user creates an opportunity.

Sets the user access levels of all objects that support territory assignments in the org.

**Field Name** **Description**

```
defaultAccessLevel

```

**Field Type**
string

**Description**
Required. The default user access level as permitted by the organization’s sharing
settings. Valid values are:

**•** `Read`

**•** `Edit`


Metadata Types Territory2Settings

**Field Name** **Description**

**•** `Transfer`

**•** `All`

```
objectType

state

```

**Field Type**
string

**Description**
Required. The only supported object type is `Lead` .

**Field Type**
string

**Description**

Required. Valid values are:

**•** `Disabled`

**•** `Enabled`

Declarative Metadata Sample Definition

The following example shows the definition of a Territory2Settings component.

```
<?xml version="1.0" encoding="UTF-8"?>

<Territory2Settings xmlns="http://soap.sforce.com/2006/04/metadata">

   <defaultAccountAccessLevel>Owner</defaultAccountAccessLevel>

   <defaultOpportunityAccessLevel>Read</defaultOpportunityAccessLevel>

   <defaultCaseAccessLevel>None</defaultCaseAccessLevel>

   <defaultContactAccessLevel>Edit</defaultContactAccessLevel>

   <enableTerritoryManagement2>true</enableTerritoryManagement2>

   <showTM2EnabledBanner>true</showTM2EnabledBanner>

   <supportedObjects>

     <defaultAccessLevel>Read</defaultAccessLevel>

     <state>Disabled</state>

     <objectType>Lead</objectType>

   </supportedObjects>

   <tm2EnableUserAssignmentLog>true</tm2EnableUserAssignmentLog>

   <t2ForecastAccessLevel>View</t2ForecastAccessLevel>

</Territory2Settings>

```

Usage

Sales Territories components don’t support packaging or change sets and aren’t supported in CRUD calls.


#### Metadata Types TrailheadSettings

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### TrailheadSettings

Represents an org’s integration with Trailhead for Learning Paths or Enablement programs, including access to enablement sites (formerly
myTrailhead).

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.

File Suffix and Directory Location

#### TrailheadSettings values are stored in the Trailhead.settings file in the settings directory. The .settings files are

different from other named components because there's only one settings file for each settings component.

Version

#### TrailheadSettings components are available in API version 47.0 and later.

Special Access Rules

To access enablement site (myTrailhead) content, the org must have a Sales Enablement license.

Fields

**Field Name** **Field Type** **Description**

`enableConfettiEffect` boolean

Indicates whether animated confetti plays on the screen after a user
reaches certain milestones, such as completing an Enablement program
in the Guidance Center. The default value of this field is `false` .

`enableMyTrailheadPref` boolean Indicates whether the org is connected to an enablement site
(myTrailhead). The default value of this field is `true` .

`enableTrailheadInLexTerms` boolean

Indicates whether the terms and conditions for showing Trailhead
content in Lightning Experience are accepted in your org. The default
value of this field is `false` .

Declarative Metadata Sample Definition

The following is an example of a TrailheadSettings component.

```
<?xml version="1.0" encoding="UTF-8"?>

<TrailheadSettings xmlns="http://soap.sforce.com/2006/04/metadata">

   <enableMyTrailheadPref>true</enableMyTrailheadPref>

</TrailheadSettings>

```


#### Metadata Types TrialOrgSettings

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>Trailhead</members>

        <name>Settings</name>

      </types>

      <version>47.0</version>

   </Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### TrialOrgSettings

Represents the settings in a trial user’s org. This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.

File Suffix and Directory Location

#### TrialOrgSettings values are stored in the TrialOrg.settings file in the settings directory.The .settings files are different

from other named components because there’s only one settings file for each settings component.

Version

TrialOrgsettings is available in API version 48.0 and later.

Special Access Rules

Access to TrialOrgSettings requires users to complete the checkout flow in Enterprise, Professional, or Essentials editions. For Essentials,
you can also access TrialOrgSettings by completing step 7 of the Setup Assistant.

Fields

**Field Name** **Field Type** **Description**

`enableSampleDataDeleted` boolean Indicates whether sample data may be deleted on trial orgs ( `true` ) or
not ( `false` ). The default value is `false` .


#### Metadata Types UserEngagementSettings

Declarative Metadata Sample Definition

The following is an example of a TrialOrgSettings component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <TrialOrgSettings xmlns="http://soap.sforce.com/2006/04/metadata">

      <enableSampleDataDeleted>false</enableSampleDataDeleted>

   </TrialOrgSettings>

```

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### UserEngagementSettings

Represents the metadata associated with various feature settings around Lightning Experience transition and adoption, user engagement
and adoption assistance, and adoption apps.

Parent Type

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

#### UserEngagementSettings components have the suffix .settings and are stored in the settings folder.

Version

Prompt components are available in API version 47.0 and later.

Special Access Rules

See related Salesforce Help for each feature for permission and edition requirements.

Fields

**Field Name** **Field Type** **Description**

`canUseAdoptionApps` boolean Indicates whether an org can access Lightning Experience transition
tools ( `true` ) or not ( `false` ). Examples of these tools are Salesforce

Optimizer, Lightning Experience Transition Assistant, and the Lightning
Experience Readiness Report. The default is `false` . This field applies
only to orgs with the External Application Settings page in Setup.
Otherwise, this field has no effect. Available in API version 62.0 and later.

`doesScheduledSwitcherRunDaily` boolean Indicates where users are automatically switched from Salesforce Classic
to Lightning Experience every day ( `true` ) or weekly ( `false` ). If `false`,


Metadata Types UserEngagementSettings

**Field Name** **Field Type** **Description**

then users are switched weekly. The default is `false` [. See Encourage](https://help.salesforce.com/articleView?id=lex_enable_users_autoswitch.htm&language=en_US)
[Users to Stay in Lightning Experience in Salesforce Help.](https://help.salesforce.com/articleView?id=lex_enable_users_autoswitch.htm&language=en_US)

`enableCustomHelpGlobalSection` boolean Indicates whether a custom section has been added to the Lightning
Experience Help Menu ( `true` ) or not ( `false` ). The default is `false` .

[See Define Custom Help for the Lightning Experience Help Menu in](https://help.salesforce.com/articleView?id=customhelp_lexhelpmenu.htm&language=en_US)
Salesforce Help for more information.

`enableHelpMenuShowFeedback` boolean Indicates whether the Give Feedback to Salesforce link in the Lightning
Experience Help Menu is visible to users ( `true` ) or not ( `false` ). The

default is `true` . Even if `false`, admins always see all links in the Help
[Menu. See Define Custom Help for the Lightning Experience Help Menu](https://help.salesforce.com/articleView?id=customhelp_lexhelpmenu.htm&language=en_US)
in Salesforce Help for more information.

`enableHelpMenuShowHelp` boolean Indicates whether the Help For This Page section in the Lightning
Experience Help Menu is visible to users ( `true` ) or not ( `false` ). The

default is `true` . Even if `false`, admins always see all links in the Help
[Menu. See Define Custom Help for the Lightning Experience Help Menu](https://help.salesforce.com/articleView?id=customhelp_lexhelpmenu.htm&language=en_US)
in Salesforce Help for more information.

Available in API version 64.0 and earlier.

`enableHelpMenuShowNewUser` boolean Indicates whether the Getting Started section in the Lightning Experience
Help Menu is visible to users ( `true` ) or not ( `false` ). The default is

`true` . Even if `false`, admins always see all links in the Help Menu.
[See Define Custom Help for the Lightning Experience Help Menu in](https://help.salesforce.com/articleView?id=customhelp_lexhelpmenu.htm&language=en_US)
Salesforce Help for more information.

Available in API version 64.0 and earlier.

`enableHelpMenuShowSearch` boolean Indicates whether the Search Documentation link in the Lightning
Experience Help Menu is visible to users ( `true` ) or not ( `false` ). The

default is `true` . Even if `false`, admins always see all links in the Help
[Menu. See Define Custom Help for the Lightning Experience Help Menu](https://help.salesforce.com/articleView?id=customhelp_lexhelpmenu.htm&language=en_US)
in Salesforce Help for more information.

Available in API version 64.0 and earlier.

`enableHelpMenuShowSfdcContent` boolean Indicates whether any Salesforce-created help resources in Lightning
Experience Help Menu are visible to users ( `true` ) or not ( `false` ). The

default is `true` . Even if `false`, admins always see all links in the Help
[Menu. See Define Custom Help for the Lightning Experience Help Menu](https://help.salesforce.com/articleView?id=customhelp_lexhelpmenu.htm&language=en_US)
in Salesforce Help for more information.

`enableHelpMenuShowShortcut` boolean Indicates whether the View Keyboard Shortcuts link in the Lightning
Experience Help Menu is visible to users ( `true` ) or not ( `false` ). The

default is `true` . Even if `false`, admins always see all links in the Help
[Menu. See Define Custom Help for the Lightning Experience Help Menu](https://help.salesforce.com/articleView?id=customhelp_lexhelpmenu.htm&language=en_US)
in Salesforce Help for more information.


Metadata Types UserEngagementSettings

**Field Name** **Field Type** **Description**

`enableHelpMenuShowSupport` boolean Indicates whether the Go to Salesforce Help link in the Lightning
Experience Help Menu is visible to users ( `true` ) or not ( `false` ). The

default is `true` . Even if `false`, admins always see all links in the Help
[Menu. See Define Custom Help for the Lightning Experience Help Menu](https://help.salesforce.com/articleView?id=customhelp_lexhelpmenu.htm&language=en_US)
in Salesforce Help for more information.

`enableHelpMenuShowTrailhead` boolean Indicates whether the Go to Trailhead link in the Lightning Experience
Help Menu is visible to users ( `true` ) or not ( `false` ). The default is

`true` . Even if `false`, admins always see all links in the Help Menu.
[See Define Custom Help for the Lightning Experience Help Menu in](https://help.salesforce.com/articleView?id=customhelp_lexhelpmenu.htm&language=en_US)
Salesforce Help for more information.

`enableIBILOptOutDashboards` boolean

`enableIBILOptOutEvents` boolean

`enableIBILOptOutReports` boolean

`enableIBILOptOutTasks` boolean

Indicates whether the It’s Better in Lightning prompt about Dashboards
is hidden from users ( `true` ) or not ( `false` ). The default is `true` .
Deprecated in API version 51.0 and later.

Indicates whether the It’s Better in Lightning prompt about
Events/Calendar is hidden from users ( `true` ) or not ( `false` ). The
default is `true` . Deprecated in API version 51.0 and later.

Indicates whether the It’s Better in Lightning prompt about Reports is
hidden from users ( `true` ) or not ( `false` ). The default is `true` .
Deprecated in API version 51.0 and later.

Indicates whether the It’s Better in Lightning prompt about Tasks is
hidden from users ( `true` ) or not ( `false` ). The default is `true` .
Deprecated in API version 51.0 and later.

`enableLexToClassicFeedbackEnable` boolean Indicates whether the Switch to Salesforce Classic Feedback Form is
shown to users ( `true` ) or not ( `false` ). The default is `false` . See

[Switch to Salesforce Classic Feedback Form in Salesforce Help for more](https://help.salesforce.com/articleView?id=lex_encourage_work_feedback.htm&language=en_US)
information.

`enableOrchestrationInSandbox` boolean Indicates whether adoption assistance and other in-app guidance is
shown to users in sandbox orgs ( `true` ) or not ( `false` ). The default is

`false` [. See Define Prompts in Lightning Experience in Salesforce Help](https://help.salesforce.com/articleView?id=customhelp_lex_prompt_add.htm&language=en_US)
for more information.

`enableOrgUserAssistEnabled` boolean Indicates whether all custom in-app guidance created by an org is shown
to users ( `true` ) or not ( `false` ). Doesn’t affect active status. The default

is `true` [. See Define Prompts in Lightning Experience in Salesforce Help](https://help.salesforce.com/articleView?id=customhelp_lex_prompt_add.htm&language=en_US)
for more information.

`enableScheduledSwitcher` boolean Indicates whether users are automatically switched from Salesforce
Classic to Lightning Experience ( `true` ) or not ( `false` ). The default is

`true` [. See Encourage Users to Stay in Lightning Experience in Salesforce](https://help.salesforce.com/articleView?id=lex_enable_users_autoswitch.htm&language=en_US)
Help.

`enableSfdcProductFeedbackSurvey` boolean

Indicates whether the Salesforce Product Feedback Form is shown to
users ( `true` ) or not ( `false` ). The default is `true` [. See Salesforce](https://help.salesforce.com/articleView?id=lex_encourage_work_sfdc_feedback.htm&language=en_US)
[Product Feedback Form in Salesforce Help for more information.](https://help.salesforce.com/articleView?id=lex_encourage_work_sfdc_feedback.htm&language=en_US)


Metadata Types UserEngagementSettings

**Field Name** **Field Type** **Description**

`enableShowSalesforceUserAssist` boolean Indicates whether all standard in-app guidance created by Salesforce is
shown to users ( `true` ) or not ( `false` ). Doesn’t affect active status. The

default is `true` [. See Define Prompts in Lightning Experience in](https://help.salesforce.com/articleView?id=customhelp_lex_prompt_add.htm&language=en_US)
[Salesforce Help for more information.](https://help.salesforce.com/articleView?id=customhelp_lex_prompt_add.htm&language=en_US)

`isCrucNotificationDisabled` boolean

Indicates whether all notifications about the Winter ’20 Turn on Lightning
Experience critical update are hidden from admins ( `true` ) or not
( `false` ). The default is `false` .

`isLEXWelcomeMatDisabled` boolean Indicates whether the Lightning Experience welcome mat is hidden
from users the first time they log into the user interface ( `true` ) or not

( `false` ). The default is `false` [. See Lightning Experience Welcome](https://help.salesforce.com/articleView?id=lex_encourage_work_welcome_mat.htm&language=en_US)
[Mat in Salesforce Help for more information.](https://help.salesforce.com/articleView?id=lex_encourage_work_welcome_mat.htm&language=en_US)

`isMeetTheAssistantDisabledInClassic` boolean

`isMeetTheAssistantDisabledInLightning` boolean

`optimizerAppEnabled` boolean

`suggestedForYou` boolean

Indicates whether all notifications about the Lightning Experience
Transition Assistant are hidden from admins in Salesforce Classic ( `true` )
or not ( `false` ). The default is `false` .

Indicates whether all notifications about the Lightning Experience
Transition Assistant are hidden from admins in Lightning Experience
( `true` ) or not ( `false` ). The default is `false` .

Indicates whether Salesforce Optimizer is turned on in the org ( `true` )
or not ( `false` ). The default is `false` [. See Improve Your](https://help.salesforce.com/articleView?id=optimizer_introduction.htm&language=en_US)
[Implementation with Salesforce Optimizer in Salesforce Help.](https://help.salesforce.com/articleView?id=optimizer_introduction.htm&language=en_US)

Indicates whether Suggested For You is turned on in the org ( `true` ) or
not ( `false` ). The default is `true` [. See Suggested For You in Salesforce](https://help.salesforce.com/s/articleView?id=sf.suggested_for_you.htm&language=en_US)
Help.

Declarative Metadata Sample Definition

The following is an example of a UserEngagementSettings component.

```
<?xml version="1.0" encoding="UTF-8"?>

<UserEngagementSettings xmlns="http://soap.sforce.com/2006/04/metadata">

  <canUseAdoptionApps>false</canUseAdoptionApps>

  <doesScheduledSwitcherRunDaily>true</doesScheduledSwitcherRunDaily>

  <enableCustomHelpGlobalSection>true</enableCustomHelpGlobalSection>

  <enableHelpMenuShowSfdcContent>true</enableHelpMenuShowSfdcContent>

  <enableHelpMenuShowShortcut>true</enableHelpMenuShowShortcut>

  <enableHelpMenuShowSupport>true</enableHelpMenuShowSupport>

  <enableHelpMenuShowTrailhead>true</enableHelpMenuShowTrailhead>

  <enableIBILOptOutDashboards>true</enableIBILOptOutDashboards>

  <enableIBILOptOutEvents>true</enableIBILOptOutEvents>

  <enableIBILOptOutReports>true</enableIBILOptOutReports>

  <enableIBILOptOutTasks>true</enableIBILOptOutTasks>

  <enableLexToClassicFeedbackEnable>true</enableLexToClassicFeedbackEnable>

  <enableOrgUserAssistEnabled>true</enableOrgUserAssistEnabled>

  <enableScheduledSwitcher>true</enableScheduledSwitcher>

  <enableSfdcProductFeedbackSurvey>true</enableSfdcProductFeedbackSurvey>

```


#### Metadata Types UserInterfaceSettings

```
     <enableOrchestrationInSandbox>true</enableOrchestrationInSandbox>

     <enableShowSalesforceUserAssist>true</enableShowSalesforceUserAssist>

     <isCrucNotificationDisabled>false</isCrucNotificationDisabled>

     <isLEXWelcomeMatDisabled>false</isLEXWelcomeMatDisabled>

     <isMeetTheAssistantDisabledInClassic>false</isMeetTheAssistantDisabledInClassic>

     <isMeetTheAssistantDisabledInLightning>false</isMeetTheAssistantDisabledInLightning>

     <optimizerAppEnabled>true</optimizerAppEnabled>

   </UserEngagementSettings>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <types>

       <members>UserEngagement</members>

       <name>Settings</name>

     </types>

     <version>47.0</version>

   </Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### UserInterfaceSettings

Represents the settings that modify the behavior of the org’s user interface.

Parent Type and Manifest Access

This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.

File Suffix and Directory Location

A UserInterfaceSettings component file has the suffix `.settings` and is stored in the `settings` directory. The `.settings` files
are different from other named components because there’s only one settings file for each settings component.

Version

#### UserInterfaceSettings components are available in API version 46.0 and later.


Metadata Types UserInterfaceSettings

Fields

**Field Name** **Field Type** **Description**

`dynamicMruActionsOff` boolean

`enableAsyncRelatedLists` boolean

`enableClickjackUserPageHeaderless` boolean

`enableCollapsibleSections` boolean

`enableCollapsibleSidebar` boolean

Indicates whether users can create custom actions for their Recently
Viewed lists ( `true` ) or not ( `false` ). The default is `true` . Available in
API version 52.0 and later. Applies to Lightning Experience only.

Indicates whether related lists are loaded asynchronously ( `true` ) or not
( `false` ). The default is `false` . Available in API version 47.0 and later.
Salesforce Classic only.

Indicates whether a Visualforce page that hides the standard header has
clickjack protections ( `true` ) or not ( `false` ). The default is `true` . This
setting applies to all of your Visualforce pages.

Indicates whether users are allowed to collapse or expand sections in
record details by using the arrow icon next to the section heading. The
default is `true` .

Indicates whether users are allowed to show or hide the sidebar on every
page that normally includes it ( `true` ) or not ( `false` ). The default is
`false` . Applies to Salesforce Classic only.

`enableCustomObjectTruncate` boolean Indicates whether users with Customize Application permission can
truncate custom objects ( `true` ) or not ( `false` ). When you truncate

an object, you delete the object’s associated records permanently, while
preserving the empty object and its metadata. The default is `false` .
Available in API version 47.0 and later.

`enableCustomSidebarOnAllPages` boolean

`enableDeleteFieldHistory` boolean

`enableExternalObjectAsyncRelatedLists` boolean

Indicates whether custom sidebar components are available on all pages
for all org users ( `true` ) or not ( `false` ). The default is `false` . Applies
to Salesforce Classic only.

Indicates whether users can delete field history and field history archive
records ( `true` ) or not ( `false` ). The default is `false` . Available in API
version 47.0 and later.

Indicates whether related lists of external objects are loaded
asynchronously ( `true` ) or not ( `false` ). The default is `true` . Available
in API version 48.0 and later. Salesforce Classic only.

`enableHoverDetails` boolean Indicates whether an interactive overlay containing record details is
displayed ( `true` ) or not ( `false` ). The default is `true` .

Note: To view hover details for a record, users need the
appropriate sharing access and field-level security access for the
fields in the mini page layout.

`enableInlineEdit` boolean Indicates whether users are allowed to edit field values on a record’s
detail page ( `true` ) or not ( `false` ). The default is `true` .


Metadata Types UserInterfaceSettings

**Field Name** **Field Type** **Description**

`enablePersonalCanvas` boolean

Indicates whether users can install and use personal canvas apps
`(true)` or not `(false)` . The default is `true` . This setting applies
to all of your Visualforce pages.

`enableRelatedListHovers` boolean Indicates whether related list hover links display at the top of record
detail pages and custom object detail pages in Setup ( `true` ) or not

( `false` ). Users can hover over a related list link to display the list and
its number of records in an interactive overlay. Users quickly view and
manage the related list items from the overlay. Users can also click a
related list hover link to jump to the related list without having to scroll
down the page. The default is `true` . Available in API version 50.0 and
later.

`enableSldsV2DarkModeInCosmos` boolean Indicates whether individual users can enable dark mode ( `true` ) or not
(beta) ( `false` ) for the Salesforce Cosmos theme. The default value is `false` .
[Available for SLDS 2 themes in select editions. See Salesforce Cosmos](https://help.salesforce.com/s/articleView?id=xcloud.customize_ui_enhancedlex.htm&type=5&language=en_US)
[Theme and SLDS 2 Availability. Available in API version 65.0 and later.](https://help.salesforce.com/s/articleView?id=xcloud.customize_ui_enhancedlex.htm&type=5&language=en_US)

Note: Dark mode is a pilot or beta service that is subject to the
[Beta Services Terms at Agreements - Salesforce.com or a written](https://www.salesforce.com/company/legal/agreements/)
Unified Pilot Agreement if executed by Customer, and applicable
[terms in the Product Terms Directory. Use of this pilot or beta](https://ptd.salesforce.com/)
service is at the Customer's sole discretion.

`enableQuickCreate` boolean Indicates whether an area displays on a tab home page (corresponds to
the **Show Quick Create** setting), allowing users to create a record quickly

with minimal information ( `true` ) or not ( `false` ). The Quick Create
area displays by default on the tab home pages for leads, accounts,
contacts, and opportunities. You can control whether the Quick Create
area is displayed on all relevant tab home pages.

`multiColumnSortLv` boolean

`multiColumnSortRL` boolean

Indicates whether users can sort list views by multiple columns ( `true` )
or not ( `false` ). The default is `true` . Available in API version 63.0 and
later.

Indicates whether users can sort related lists by multiple columns ( `true` )
or not ( `false` ). The default is `true` . Available in API version 63.0 and
later.

Declarative Metadata Sample Definition

The following is an example of a UserInterfaceSettings component.

```
<?xml version="1.0" encoding="UTF-8"?>

<UserInterfaceSettings xmlns="http://soap.sforce.com/2006/04/metadata">

  <enableDeleteFieldHistory>false</enableDeleteFieldHistory>

  <enableInlineEdit>true</enableInlineEdit>

  <enableHoverDetails>false</enableHoverDetails>

  <enableQuickCreate>true</enableQuickCreate>

  <enablePersonalCanvas>false</enablePersonalCanvas>

```


#### Metadata Types UserManagementSettings

```
     <enableClickjackUserPageHeaderless>true</enableClickjackUserPageHeaderless>

   </UserInterfaceSettings>

```

Example Package Manifest

The following is an example package manifest used to deploy or retrieve the user interface settings metadata for an organization:

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

    <types>

     <members>UserInterface</members>

     <name>Settings</name>

    </types>

    <version>46.0</version>

   </Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### UserManagementSettings

Represents a selection of user management options that appear on the User Management Settings Setup page. This type extends the
Metadata metadata type and inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.

File Suffix and Directory Location

UserMangementSettings are stored in the `UserManagement.settings` directory. The `.settings` files are different from
other named components because there’s only one settings file for each settings component.

Version

Manage org-wide settings for certain options. User Management Settings are available in API version 46.0 and later.

Fields

**Field** **Field Type** **Description**

`enableConcealPersonalInfo` boolean Indicates if personal information fields in user records are
hidden from external users ( `true` ) or not ( `false` ).

When this field is set to `true`, 10 personal information
fields are hidden. The default value is `false` . This field
is unavailable for orgs created in Winter ’22 or later.

Salesforce recommends that you use the
`enableEnhancedConcealPersonalInfo` field


Metadata Types UserManagementSettings

**Field** **Field Type** **Description**

instead of `enableConcealPersonalInfo` . Before
you set the
`enableEnhancedConcealPersonalInfo` field
to `true`, make sure that
`enableConcealPersonalInfo` is set to `false` .

`enableContactlessExternalIdentityUsers` boolean If `true` and your org has the External Identity license,
you can create contactless users. Having users without

contact information reduces the overhead of managing
customers. Purchase the External Identity license to
access the Customer 360 Identity product.

The default is `false` . Available in API version 47.0 and
later.

`enableEnhancedConcealPersonalInfo` boolean Indicates if personal information fields in user records are
hidden from external users ( `true` ) or not ( `false` ).

When this field is set to `true`, you can choose which
fields are classified as personal information and hidden
on the User Management Settings Setup page. The
default value is `false` . This field is available in API
version 53.0 and later.

Before you set the
`enableEnhancedConcealPersonalInfo` field
to `true`, make sure that
`enableConcealPersonalInfo` is set to `false` .

`enableEnhancedPermsetMgmt` boolean If you enable **Enhanced Permission Set Component**
**Views** ( `true` ), you can work with permission sets more

easily. For example, when you have large numbers of
Apex class assignments for permission sets, you can
enable a paginated result set, standard filtering, and
sorting.

`enableEnhancedProfileMgmt` boolean If you enable **Enhanced Profile Lists Views** ( `true` ),
you can quickly view, customize, and edit list data.

`enableEnhcUiUserAccessPolicies` boolean Indicates whether you create and manage user access
policies through an improved user interface ( `true` ) or

not ( `false` ). The default value is `false` . If user access
policies aren’t enabled, this field has no effect. If user
access policies are enabled, this field is automatically set
to `true`, but you can change it to `false` . Available in
API version 60.0 and later.

`enableNewProfileUI` boolean If you enable **Enhanced Profile User Interface** ( `true` ),
you can use the streamlined, enhanced profile user

interface to browse, search, and modify settings. You can
use only one user interface at a time.


Metadata Types UserManagementSettings

**Field** **Field Type** **Description**

`enableProfileFiltering` boolean With profile filtering enabled ( `true` ), you can restrict
who sees profile names to the users who require the

access for their job roles. If profile filtering is disabled
( `false` ), users can see all profiles in a Salesforce org,
regardless of which permissions they have.

Important: Profile names are also exposed when
users with permissions to perform the following
tasks take these actions:

**•** Create a tab or record type with a wizard step
that includes the assignment of tabs and
record types to profiles.

**•** Configure a login flow where viewing profile
lists is required to make flow associations.

**•** Set up delegated admins where looking up
profiles is needed to identify assignable
profiles.

**•** Administer an org as a delegated customer
admin.

**•** Administer an org as a delegated admin to
view and assign profiles of the delegated
group.

This field is available in API version 50.0 and later.

`enableRestrictEmailDomains` boolean

Indicates whether the Email Domain Allowlist is visible
( `true` ) or hidden ( `false` ) in Setup. The default value
is `false` .

This field is available in API version 53.0 and later.

`enableScrambleUserData` boolean If you enable **Let Users Scramble Their User Data**
( `true` ), users can request that Salesforce remove all their

personal data. Because Salesforce can’t delete
information, it scrambles their data. Scrambling a user’s
data is unrecoverable. So this org-wide setting serves as
an extra precaution. If a user requests it, you scramble
the data programmatically with the `obfuscateUser`
Apex method. You can use the method, for example, in
a custom Apex trigger, workflow, or the Developer
Console.

This field is available in API version 47.0 and later.

`enableUserSelfDeactivate` boolean

If you enable **User Self Deactivate** ( `true` ), users can
deactivate their Experience Cloud site or Chatter
accounts.


Metadata Types UserManagementSettings

**Field** **Field Type** **Description**

`enhancedPermSetList` boolean Indicates whether you manage permission sets with an
updated user interface on the Permissions Setup page

( `true` ) or not ( `false` ). The default value is `false` .
Available in API version 63.0 and later.

`enhancedUserListView` boolean Indicates whether you manage users with an updated
user interface on the Users Setup page ( `true` ) or not

( `false` ). The default value is `false` . Available in API
version 62.0 and later.

`enhancedUserRoleListView` boolean Indicates whether you manage roles with an updated
user interface on the Roles Setup page ( `true` ) or not

( `false` ). The default value is `false` . Available in API
version 63.0 and later.

`groupSummaryUIEnhancement` boolean Indicates whether you use an improved user interface to
add or remove public group members through the

group’s summary page `true` or not ( `false` ). If this
field is set to `true`, you can still manage public group
membership through the group’s detail page. The default
value is `true` . Available in API version 62.0 and later.

`permsetsInFieldCreation` boolean If `true`, users can assign field-level security to
permission sets instead of to profiles when creating a

field on an object, setting field-level security on a field,
or changing a field type on a field. The default is `false` .

Available in API version 56.0 and later.

`psaExpirationUIEnabled` boolean Indicates if admins can use an updated user interface
that includes an assignment expiration for permission

sets and permission set groups ( `true` ) or not ( `false` ).
The default value is `false` . This field is available in API
version 52.0 and later.

`restrictedProfileCloning` boolean When enabled ( `true` ), only permissions accessible to
your org are enabled when you clone profiles. When

disabled ( `false` ), all permissions currently enabled in
the source profile are also enabled for the cloned profile,
even if your org can't currently access them.

This field is available in API version 50.0 and later.

`userAccessPoliciesEnabled` boolean Indicates if user access policies are enabled ( `true` ) or
not ( `false` ). With user access policies, you can automate

and migrate your users’ assignments to managed
package licenses, permission sets, and other access
mechanisms based on criteria that you set. The default
value is `false` . This field is available in API version 58.0
and later.


Metadata Types UserManagementSettings

**Field** **Field Type** **Description**

`userFieldHistoryTracking` boolean Indicates if user field history tracking is enabled (true) or
not (false). With user field history tracking, you can keep

track of changes in user fields. The default value is
`false` . This field is available in API version 64.0 and
later.

Declarative Metadata Sample Definition

The following is an example of a UserManagementSettings component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <UserManagementSettings xmlns="http://soap.sforce.com/2006/04/metadata"

   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

      <enableConcealPersonalInfo>false</enableConcealPersonalInfo>

     <enableContactlessExternalIdentityUsers>false</enableContactlessExternalIdentityUsers>

      <enableEnhancedConcealPersonalInfo>true</enableEnhancedConcealPersonalInfo>

      <enableEnhancedPermsetMgmt>false</enableEnhancedPermsetMgmt>

      <enableEnhancedProfileMgmt>true</enableEnhancedProfileMgmt>

      <enableNewProfileUI>false</enableNewProfileUI>

      <enableProfileFiltering>false</enableProfileFiltering>

      <enableRestrictEmailDomains>true</enableRestrictEmailDomains>

      <enableScrambleUserData>false</enableScrambleUserData>

      <enableUserSelfDeactivate>false</enableUserSelfDeactivate>

      <enhancedPermSetList>true</enhancedPermSetList>

      <enhancedUserListView>true</enhancedUserListView>

      <enhancedUserRoleListView>true</enhancedUserRoleListView>

      <groupSummaryUIEnhancement>true</groupSummaryUIEnhancement>

      <restrictedProfileCloning>true</restrictedProfileCloning>

      <userAccessPoliciesEnabled>true</userAccessPoliciesEnabled>

   </UserManagementSettings>

```

The following is an example `package.xml` manifest that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>UserManagement</members>

        <name>Settings</name>

      </types>

      <version>53.0</version>

   </Package>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


#### Metadata Types VoiceSettings VoiceSettings

Represents an org’s Sales Dialer settings, such as call recording, conferencing, and voicemail.

This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for details.

File Suffix and Directory Location

#### VoiceSettings values are stored in the Voice.settings file in the settings directory. The .settings files are different from

other named components because there’s only one settings file for each settings component.

Version

#### VoiceSettings is available in API version 47.0 and later.

Fields

**Field Name** **Field Type** **Description**

`enableCallDisposition` boolean

`enableConsentReminder` boolean

enableDefaultRecording boolean

`enableVoiceCallList` boolean

Indicates whether call disposition is enabled ( `true` ) or not ( `false` ).
With call disposition, also called Call Result, sales reps can track whether
a call was connected and how it went.

Default value is `false` . To use this feature, enable Dialer in Lightning
Experience.

Indicates whether the consent reminder is enabled ( `true` ) or not
( `false` ). With the consent reminder, prior to recording a call, users see
a prompt reminding them not to record phone calls without consent.

Default value is `false` . To use this feature, enable Dialer in Lightning
Experience.

Indicates whether the default recording is enabled ( `true` ) or not
( `false` ). With default recording, sales reps can record calls automatically
in the Sales Dialer.

Default value is `false` . This field is available in API version 54.0 and
later.

Indicates whether Call List is enabled ( `true` ) or not ( `false` ). Sales reps
can use call list to keep a running list of the calls they want to make.

Default value is `false` . To use this feature, enable Dialer in Lightning
Experience.


Metadata Types VoiceSettings

**Field Name** **Field Type** **Description**

`enableVoiceCallRecording` boolean

`enableVoiceCoaching` boolean

Indicates whether Call Recording is enabled ( `true` ) or not ( `false` ).
Sales reps can record important calls directly from the call panel in Sales
Dialer.

Default value is `false` . To use this feature, enable Dialer in Lightning
Experience.

Indicates whether Call Monitoring is enabled ( `true` ) or not ( `false` ).
Using the Monitor tab in the call panel, managers can listen to the calls
of their sales reps for personalized coaching.

Default value is `false` . To use this feature, enable Dialer in Lightning
Experience.

`enableVoiceConferencing` boolean Reserved for future use.

`enableVoiceLocalPresence` boolean

`enableVoiceMail` boolean

`enableVoiceMailDrop` boolean

Indicates whether Local Presence is enabled ( `true` ) or not ( `false` ).
Local Presence displays phone numbers with the same area code as the
prospects your reps are calling, so more calls are answered.

Default value is `false` . To use this feature, enable Dialer in Lightning
Experience.

Indicates whether voicemail is enabled ( `true` ) or not ( `false` ). Sales
reps can receive and store up to 20 personal voicemail messages in
Salesforce.

Default value is `false` . To use this feature, enable Dialer in Lightning
Experience.

Indicates whether Voicemail Drop is enabled ( `true` ) or not ( `false` ).
Sales reps can “drop” (or send) prerecorded messages to recipients’
voicemail boxes.

Default value is `false` . To use this feature, enable Dialer in Lightning
Experience.

Declarative Metadata Sample Definition

The following is an example of the package file.

```
<?xml version="1.0" encoding="UTF-8"?>

<Package xmlns="http://soap.sforce.com/2006/04/metadata">

   <types>

   </types>

   <version>28.0</version>

</Package>

```

The package file references the following Voice.settings file.

```
<?xml version="1.0" encoding="UTF-8"?>

<VoiceSettings xmlns="http://soap.sforce.com/2006/04/metadata">

```


#### Metadata Types WarrantyLifeCycleMgmtSettings

```
      <enableCallDisposition>true</enableCallDisposition>

      <enableVoiceCallList>true</enableVoiceCallList>

      <enableVoiceCallRecording>true</enableVoiceCallRecording>

      <enableVoiceCoaching>true</enableVoiceCoaching>

      <enableVoiceConferencing>true</enableVoiceConferencing>

      <enableVoiceLocalPresence>true</enableVoiceLocalPresence>

      <enableVoiceMail>true</enableVoiceMail>

      <enableVoiceMailDrop>true</enableVoiceMailDrop>

   </VoiceSettings>

```

Wildcard Support in the Manifest File

The wildcard character `*` (asterisk) in the `package.xml` manifest file doesn’t apply to metadata types for feature settings. The
wildcard applies only when retrieving all settings, not for an individual setting. For details, see Settings. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### WarrantyLifeCycleMgmtSettings

Represents settings that control the Warranty Administration for your org.

This type extends the Metadata metadata type and inherits its `fullName` field.

In the package manifest, all organization settings metadata types are accessed using the Settings name. See Settings for more details.

File Suffix and Directory Location

#### WarrantyLifeCycleMgmtSettings values are stored in the WarrantyLifecycleMgmt.settings file in the settings directory.

Version

#### WarrantyLifeCycleMgmtSettings components are available in API version 54.0 and later.

Fields

**Field Name** **Field Type** **Description**

`enableWarrantyLCMgmt` boolean Indicates whether warranty life-cycle management is enabled in your
org ( `true` ) or not `false` ).

Declarative Metadata Sample Definition

The following is an example of WarrantyLifeCycleMgmtSettings component.

```
   <!-
     ~ Copyright 2022 salesforce.com, inc.

     ~ All Rights Reserved

     ~ Company Confidential

     -->

   <WarrantyLifecycleMgmtSettings

    xmlns="http://soap.sforce.com/2006/04/metadata">

```


#### Metadata Types WorkDotComSettings

```
    <enableWarrantyLCMgmt>true</enableWarrantyLCMgmt>

   </WarrantyLifecycleMgmtSettings>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <!-
     ~ Copyright 2022 salesforce.com, inc.

     ~ All Rights Reserved

     ~ Company Confidential

     -->

   <Package

    xmlns="http://soap.sforce.com/2006/04/metadata">

    <types>

     <members>WarrantyLifecycleMgmt</members>

     <name>Settings</name>

    </types>

    <version>54.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### WorkDotComSettings

Represents WorkDotCom settings. This type extends the Metadata metadata type and inherits its `fullName` field.

Version

#### WorkDotComSettings components are available in API version 31.0 and later.

Fields

**Field Name** **Field Type** **Description**

`enableCoachingManagerGroupAccess` boolean

`enableGoalManagerGroupAccess` boolean

Indicates whether Coaching Manager Group Access is available to users
`(true)` or not `(false)` . Default value is `true` .

Deprecated.

Indicates whether Goal Manager Group Access is available to users
`(true)` or not `(false)` . Default value is `true` .

Deprecated.

`enableProfileSkills` boolean Indicates whether Profile Skills is available to users `(true)` or not
`(false)` . Default value is `true` .

`enableProfileSkillsAddFeedPost` boolean Indicates whether Add Skills as Feed Posts is available to users `(true)` or
not `(false)` . Default value is `true` .


Metadata Types WorkDotComSettings

**Field Name** **Field Type** **Description**

`enableProfileSkillsAutoSuggest` boolean Indicates whether Profile Skills Auto Suggest is available to users
`(true)` or not `(false)` . Default value is `true` .

`enableProfileSkillsUsePlatform` boolean Indicates whether Profile Skills Use Platform is available to users
`(true)` or not `(false)` . Default value is `true` .

`enableWorkBadgeDefRestrictPref` boolean

`enableWorkCalibration` boolean

`enableWorkCanvasPref` boolean

`enableWorkCertification` boolean

`enableWorkCertificationNotification` boolean

`enableWorkRewardsPref` boolean

Indicates whether Badge Definition Restriction is available to users
`(true)` or not `(false)` . Default value is `true` .

Deprecated.

Indicates whether Calibration is available to users `(true)` or not
`(false)` . Default value is `false` .

Deprecated.

Indicates whether Canvas is available to users `(true)` or not `(false)` .
Default value is `true` .

Deprecated.

Indicates whether Certification is available to users `(true)` or not
`(false)` . Default value is `true` .

Deprecated.

Indicates whether Certification Notification is available to users
`(true)` or not `(false)` . Default value is `false` .

Deprecated.

Indicates whether Rewards is available to users `(true)` or not
`(false)` . Default value is `true` .

Deprecated.

`enableWorkThanksPref` boolean Indicates whether Thanks is available to users `(true)` or not
`(false)` . Default value is `true` .

Declarative Metadata Sample Definition

The following is an example of a WorkDotComSettings component.

```
<?xml version="1.0" encoding="UTF-8"?>

<WorkDotComSettings xmlns="http://soap.sforce.com/2006/04/metadata">

   <enableCoachingManagerGroupAccess>true</enableCoachingManagerGroupAccess>

   <enableGoalManagerGroupAccess>true</enableGoalManagerGroupAccess>

   <enableProfileSkills>true</enableProfileSkills>

   <enableProfileSkillsAddFeedPost>true</enableProfileSkillsAddFeedPost>

   <enableProfileSkillsAutoSuggest>true</enableProfileSkillsAutoSuggest>

   <enableProfileSkillsUsePlatform>true</enableProfileSkillsUsePlatform>

   <enableWorkBadgeDefRestrictPref>true</enableWorkBadgeDefRestrictPref>

   <enableWorkCalibration>true</enableWorkCalibration>

```


#### Metadata Types WorkforceEngagementSettings

```
      <enableWorkCanvasPref>true</enableWorkCanvasPref>

      <enableWorkCertification>true</enableWorkCertification>

      <enableWorkCertificationNotification>true</enableWorkCertificationNotification>

      <enableWorkRewardsPref>true</enableWorkRewardsPref>

      <enableWorkThanksPref>true</enableWorkThanksPref>

      </WorkDotComSettings>

#### WorkforceEngagementSettings

```

Represents settings for Workforce Engagement Management.

File Suffix and Directory Location

#### WorkforceEngagementSettings components are stored in the WorkforceEngagement.settings folder.

Version

#### WorkforceEngagementSettings is available in API version 52.0 and later.

Special Access Rules

To use Workforce Engagement settings, the org requires a Workforce Engagement license.

Fields

Field Type

**Field Name** **Field Type** **Description**

`enableMachineLearningForecasting` boolean Indicates whether machine learning-based forecasting is used ( `true` )
or not used ( `false` ).

`enableWorkforceEngagement` boolean Indicates whether Workforce Engagement is enabled ( `true` ) or not
enabled ( `false` ).

`enableWorkforceEngagementConfiguration` boolean

Indicates whether the Workforce Engagement Configuration App is
installed or enabled ( `true` ) or not ( `false` ). If `true`, it grants access

to the Lightning App as well as the app's Job Profile Mapping tab. It also
defaults the standard and custom profile tab settings to On. If `false`,
it removes access to the app and tab but doesn’t delete the app
metadata. This field is available in API version 53.0 and later.

`enableHistoricalAdherence` boolean Indicates whether historical adherence is enabled ( `true` ) or not enabled
( `false` ). This field is available in API version 54.0 and later.

`enableIndividualAdherence` boolean Indicates whether individual adherence is enabled ( `true` ) or not enabled
( `false` ). This field is available in API version 54.0 and later.


### Metadata Types SharedTo

**Field Name** **Field Type** **Description**

`enableIntradayManagement` boolean

`enableRealTimeAdherence` boolean

Indicates whether the intraday management dashboard is enabled
( `true` ) or not enabled ( `false` ). This field is available in API version
55.0 and later.

Indicates whether real-time adherence is enabled ( `true` ) or not enabled
( `false` ). To use real-time adherence, you must also enable
Omni-Channel. This field is available in API version 55.0 and later.

Declarative Metadata Sample Definition

The following is an example of a `WorkforceEngagement.settings` component.

```
<?xml version="1.0" encoding="UTF-8"?>

<WorkforceEngagementSettings xmlns="http://soap.sforce.com/2006/04/metadata">

  <enableMachineLearningForecasting>true</enableMachineLearningForecasting>

  <enableWorkforceEngagement>true</enableWorkforceEngagement>

  <enableWorkforceEngagementConfiguration>true</enableWorkforceEngagementConfiguration>

  <enableHistoricalAdherence>true</enableHistoricalAdherence>

  <enableenableIndividualAdherence>true</enableIndividualAdherence>

  <enableIntradayManagement>true</enableIntradayManagement>

  <enableRealTimeAdherence>true</enableRealTimeAdherence>

</WorkforceEngagementSettings>

```

The following is an example `package.xml` that references the previous definition.

```
<?xml version="1.0" encoding="UTF-8"?>

2 <Package xmlns="http://soap.sforce.com/2006/04/metadata">

3 <types>

4 <members>WorkforceEngagement</members>

5 <name>Settings</name>

6 </types>

7 <55.0>[ftest]</55.0>

8 </Package>

```

Usage

When enableMachineLearningForecasting is set to `false`, we clean up data from our Ofek forecasting platform. The original copy of
the same set of data is stored in the Core app, so no data is lost.

### SharedTo SharedTo defines the sharing access for a list view or a folder. It can be used to specify the target and source for owner-based sharing

rules.

[See Sharing Considerations and Public and Personal Groups in Salesforce Help.](https://help.salesforce.com/s/articleView?id=platform.security_sharing_considerations.htm&type=5&language=en_US)

### Note: SharedTo on page 2292 is included in the metadata for shared and private list views. SharedTo on page 2292 isn’t in the

metadata for public list views.


Metadata Types SharedTo

Declarative Metadata File Suffix and Directory Location

SharedTo on page 2292 is used with ListView, Folder, and SharingRules.

Version

SharedTo on page 2292 is available in API version 17.0 and later.

Fields

**Field** **Field Type** **Description**

`allCustomerPortalUsers` string

`allInternalUsers` string

`allPartnerUsers` string

`channelProgramGroup` string

`channelProgramGroups` string[]

`group` string[]

`guestUser` string[]

`groups` string[]

A group containing all customer portal users.

This field is available in API version 24.0 and later.

A group containing all internal and nonportal users.

This field is available in API version 24.0 and later.

A group containing all partner users.

This field is available in API version 24.0 and later.

A system-managed group with sharing access containing all
partner members of the corresponding channel program or
level.

This field is available in API version 41.0 and later.

A list of system-managed groups with sharing access containing
all partner members of the corresponding channel programs or
levels.

This field is available in API version 41.0 and later.

A list of groups with sharing access. Use this field instead of the
`groups` field.

This field is available in API version 22.0 and later.

A list of guest user nicknames with sharing access. This field can
be used only with SharingGuestRule.

This field is available in API version 47.0 and later.

A list of groups with sharing access.

Use the `group` field instead for API version 22.0 and later.

`managerSubordinates` string[] A list of users whose direct and indirect subordinates receive
sharing access. This field is available in API version 24.0 and later.

`managers` string[] A list of users whose direct and indirect managers receive sharing
access. This field is available in API version 24.0 and later.


Metadata Types SharedTo

**Field** **Field Type** **Description**

`portalRole` string[]

`portalRoleandSubordinates` string[]

`role` string[]

A list of groups with sharing access containing all users in a
portal role.

This field is available in API version 24.0 and later.

A list of groups with sharing access containing all users in a
portal role or any users under that role.

This field is available in API version 24.0 and later.

A list of roles with sharing access. Use this field instead of the
`roles` field.

This field is available in API version 22.0 and later.

`roleAndSubordinates` string[] A list of roles with sharing access. All roles below each of these
roles in the role hierarchy also have sharing access. If portal

accounts are enabled, then all roles and portal accounts below
each of these roles in the role hierarchy also have sharing access.
Use this field instead of the `rolesAndSubordinates`
field.

This field is available in API version 22.0 and later and is only
available when digital experiences is enabled for your org and
Experience Cloud site users are created with external account
roles other than a shared person account role.

`roleAndSubordinatesInternal` string[]

`roles` string[]

A list of roles with sharing access. All roles below each of these
roles in the role hierarchy also have sharing access.

This field is available in API version 22.0 and later.

A list of roles with sharing access.

Use the `role` field instead for API version 22.0 and later.

`rolesAndSubordinates` string[] A list of roles with sharing access. All roles below each of these
roles in the role hierarchy also have sharing access. If portal

accounts are enabled, then all roles and portal accounts below
each of these roles in the role hierarchy also have sharing access.

Use the `roleAndSubordinates` field instead for API
version 22.0 and later.

`territories` string[]

A list of territories with sharing access.

Use the `territory` field instead for API version 22.0 and
later.


### Metadata Types SharingBaseRule

**Field** **Field Type** **Description**

`territoriesAndSubordinates` string[]

`territory` string[]

A list of territories with sharing access. All territories below each
of these territories in the territory hierarchy also have sharing
access.

Use the `territoryAndSubordinates` field instead for
API version 22.0 and later.

A list of territories with sharing access. Use this field instead of
the `territories` field.

If you’re using Sales Territories, use
_`modelName.territoryName`_ for the shared-to and
shared-from `territory` values, where:

**•** _`modelName`_ equals the name of the active territory model
in the API.

**•** _`territoryName`_ equals the territory’s name in the API.

This field is available in API version 22.0 and later.

`territoryAndSubordinates` string[] A list of territories with sharing access. All territories below each
of these territories in the territory hierarchy also have sharing

access. Use this field instead of the
`territoriesAndSubordinates` field.

If you’re using Sales Territories, use
_`modelName.territoryName`_ for the shared-to and
shared-from `territoryAndSubordinates` values,
where:

**•** _`modelName`_ equals the name of the active territory model
in the API.

**•** _`territoryName`_ equals the territory’s name in the API.

This field is available in API version 22.0 and later.

`queue` string[]

### SharingBaseRule

A list of queues with sharing access. Applies only to lead, case,
and CustomObject sharing rules.

This field is available in API version 24.0 and later.

Represents sharing rule settings such as access level and to whom access is granted.

This type extends the Metadata metadata type and inherits its `fullName` field.

Note: You can’t create a SharingBaseRule on page 2295 component directly. Use the components under SharingRules instead.


Metadata Types SharingBaseRule

Version

SharingBaseRule on page 2295 replaces BaseSharingRule and is available in API version 33.0 and later.

Fields

**Field** **Field Type** **Description**

`accessLevel` string Required. The access level that the sharing rule
grants.

`accountSettings` AccountSharingRuleSettings[] The access level for the account’s children (case,
contact, and opportunity).

`description` string Describes the sharing rule. Maximum of 1000
characters.

`label` string Required. Label for the sharing rule.

`sharedTo` SharedTo Required. Specifies who the record is shared
with.

AccountSharingRuleSettings

Defines the access level for the case, contact, and opportunity associated with the account.

**Field** **Field Type** **Description**

`caseAccessLevel` string

`contactAccessLevel` string

`opportunityAccessLevel` string

Required. The access level that the user or group
has to cases associated with the account.
Possible values are:

**•** None

**•** Read

**•** Edit

Required. The access level that the user or group
has to contacts associated with the account.
Possible values are:

**•** None

**•** Read

**•** Edit

Required. The access level that the user or group
has to opportunities associated with the account.
Possible values are:

**•** None

**•** Read

**•** Edit


### Metadata Types SharingRules

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

### SharingRules

Represents the base container for sharing rules, which can be criteria-based, ownership-based, territory-based, or for guest user access.
### SharingRules enables you to share records with a set of users, using rules that specify the access level for the target user group.

This type extends the Metadata metadata type and inherits its `fullName` field. For more information, see “Sharing Rules” in Salesforce
Help.

In API version 33.0 and later, retrieving, deleting, or deploying of all sharing rules in an organization is available. Wildcard support is also
available. You can’t retrieve, delete, or deploy manual sharing rules or sharing rules by their type (owner, criteria-based, territory, or guest
user).

Declarative Metadata File Suffix and Directory Location

In API version 33.0 and later, components are stored in the sharingRules folder and their file name matches the object name with the
suffix `.sharingRules` . Criteria-based, owner-based, territory-based, and guest user sharing rules are all contained in a
`object.sharingRule` file.

Before API version 33.0, SharingRules components are stored in their corresponding object directory and the file name matches the
object name. For example, the `accountSharingRules` directory contains an `Account.sharingRules` file for account
sharing rules. SharingRules for custom objects are stored in the `customObjectSharingRules` directory, which contains files
with the `.sharingRules` extension such as `ObjA__c.sharingRules`, where ObjA refers to the developer name of a custom
object type.

Version

### SharingRules components are available in API version 24.0 and later, but these components are no longer available in API version 33.0

and later: AccountSharingRules, CampaignSharingRules, CaseSharingRules, ContactSharingRules, LeadSharingRules,
OpportunitySharingRules, AccountTerritorySharingRules, CustomObjectSharingRules, UserSharingRules.

In API version 33.0 and later, use SharingCriteriaRule, SharingOwnerRule and SharingTerritoryRule.

Special Access Rules

As of Spring ’20 and later, only users with the View Setup and Configuration permission can access this object, and only users with the
Manage Sharing permission can edit this object.

Fields

The following information assumes that you’re familiar with implementing sharing rules for standard objects and custom objects. For
more information on these fields, see “Sharing Settings” in Salesforce Help.


Metadata Types SharingRules

**Field** **Field Type** **Description**

`sharingCriteriaRules` SharingCriteriaRule[] An array of criteria-based sharing rules. Available in API
version 33.0 and later.

`sharingGuestRules` SharingGuestRule[] An array of guest user sharing rules. Available in API
version 47.0 and later.

`sharingOwnerRules` SharingOwnerRule[] An array of ownership-based sharing rules. Available in
API version 33.0 and later.

`sharingTerritoryRules` SharingTerritoryRule[] An array of territory-based sharing rules. Available in API
version 33.0 and later.

SharingCriteriaRule

Defines a criteria-based sharing rule. It extends SharingBaseRule and inherits all its fields. Available in API version 33.0 and later.

**Field** **Field Type** **Description**

`booleanFilter` string Advanced filter conditions that are specified for the sharing
rule.

`criteriaItems` FilterItem[] An array of the boolean criteria (conditions) for the sharing
rule.

`includeRecordsOwnedByAll` boolean Required. Indicates whether records owned by users who
can’t have an assigned role are included in the records

shared ( `true` ) or not ( `false` ). Examples of users who
can’t have an assigned role are high-volume users and
system users such as automated process users.or
Salesforce system users.

You can’t edit this field after the sharing rule is created.

SharingGuestRule

Defines a guest user sharing rule. It extends SharingBaseRule and inherits all its fields, except `accountSettings` . Available in API
version 47.0 and later.

Note: For SharingGuestRule, the `accessLevel` field can be set only to `Read` .

**Field** **Field Type** **Description**

`booleanFilter` string Advanced filter conditions that are specified for the sharing
rule. Available in API version 48.0 and later.

`criteriaItems` FilterItem[] An array of the boolean criteria (conditions) for the sharing
rule. Available in API version 48.0 and later.

`includeHVUOwnedRecords` boolean Required. Indicates whether records owned by
high-volume community or site users are included in the


Metadata Types SharingRules

**Field** **Field Type** **Description**

records shared ( `true` ) or not ( `false` ). By default, only
records owned by authenticated users, guest users, and
queues are included in sharing rules. This field has a default
value of `false` . Available in API version 52.0 and later.

You can’t edit this field after the sharing rule is created.

SharingOwnerRule

Defines an ownership-based sharing rule. It extends SharingBaseRule and inherits all its fields. Available in API version 33.0 and later.

**Field** **Field Type** **Description**

`sharedFrom` SharedTo

SharingTerritoryRule

Required. Specifies the record owners.

If you’re using Sales Territories, use
_`modelName.territoryName`_ for the shared-to

and shared-from `territory` and
`territoryAndSubordinates` values on the
SharedTo type, where:

**•** _`modelName`_ equals the name of the active territory
model in the API.

**•** _`territoryName`_ equals the territory’s name in
the API.

Defines a territory-based sharing rule. It extends SharingOwnerRule and inherits all its fields. Available in API version 33.0 and later.

AccountSharingRules

Represents the sharing rules for accounts. It extends the SharingRules metadata type and inherits its `fullName` field. Only available
in API version 32.0 and earlier.

**Field** **Field Type** **Description**

`criteriaBasedRules` AccountCriteriaBasedSharingRule[] List that defines user criteria-based rules.

`ownerRules` AccountOwnerSharingRule[] List that defines user membership-based rules.

CampaignSharingRules

Represents the sharing rules for campaigns. It extends the SharingRules metadata type and inherits its `fullName` field. Only available
in API version 32.0 and earlier.


Metadata Types SharingRules

**Field** **Field Type** **Description**

`criteriaBasedRules` CampaignCriteriaBasedSharingRule[] List that defines user criteria-based rules.

`ownerRules` CampaignOwnerSharingRule[] List that defines user membership-based rules.

CaseSharingRules

Represents the sharing rules for cases. It extends the SharingRules metadata type and inherits its `fullName` field. Only available in
API version 32.0 and earlier.

**Field** **Field Type** **Description**

`criteriaBasedRules` CaseCriteriaBasedSharingRule[] List that defines user criteria-based rules.

`ownerRules` CaseOwnerSharingRule[] List that defines user membership-based rules.

ContactSharingRules

Represents the sharing rules for contacts. It extends the SharingRules metadata type and inherits its `fullName` field. Only available
in API version 32.0 and earlier.

**Field** **Field Type** **Description**

`criteriaBasedRules` ContactCriteriaBasedSharingRule[] List that defines user criteria-based rules.

`ownerRules` ContactOwnerSharingRule[] List that defines user membership-based rules.

LeadSharingRules

Represents the sharing rules for leads. It extends the SharingRules metadata type and inherits its `fullName` field. Only available in
API version 32.0 and earlier.

**Field** **Field Type** **Description**

`criteriaBasedRules` LeadCriteriaBasedSharingRule[] List that defines user criteria-based rules.

`ownerRules` LeadOwnerSharingRule[] List that defines user membership-based rules.

OpportunitySharingRules

Represents the sharing rules for opportunities. It extends the SharingRules metadata type and inherits its `fullName` field. Only available
in API version 32.0 and earlier.

**Field** **Field Type** **Description**

`criteriaBasedRules` OpportunityCriteriaBasedSharingRule[] List that defines user criteria-based rules.

`ownerRules` OpportunityOwnerSharingRule[] List that defines user membership-based rules.


Metadata Types SharingRules

AccountTerritorySharingRules

Represents the sharing rules for account territories in the original territory management feature. It extends the SharingRules metadata
type and inherits its `fullName` field. Only available in API version 32.0 and earlier.

**Field** **Field Type** **Description**

`rules` AccountTerritorySharingRule[] List that defines user membership-based rules. The list of
acceptable values for the `sharedFrom` fields are:

**•** `territory`

**•** `territoryAndSubordinates`

CustomObjectSharingRules

Represents the sharing rules for custom objects. It extends the SharingRules metadata type and inherits its `fullName` field. Only
available in API version 32.0 and earlier.

**Field** **Field Type** **Description**

`criteriaBasedRules` CustomObjectCriteriaBasedSharingRule[] List that defines user criteria-based rules.

`ownerRules` CustomObjectOwnerSharingRule[] List that defines user membership-based rules.

UserSharingRules

Represents the sharing rules for users. With user sharing rules, you can share members of a group with members of another group. It
extends the SharingRules metadata type and inherits its `fullName` field. Only available in API version 32.0 and earlier.

**Field** **Field Type** **Description**

`criteriaBasedRules` UserCriteriaBasedSharingRule[] List that defines user criteria-based rules.

`membershipRules` UserMembershipSharingRule[] List that defines user membership-based rules.

Declarative Metadata Sample Definition

For retrieving sharing rules, see `package.xml` sample at SharingRules.

The following sample XML definition represents a criteria-based sharing rule in API version 33.0.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <SharingRules xmlns="http://soap.sforce.com/2006/04/metadata">

      <sharingCriteriaRules>

        <fullName>AccountCriteriaShareWithCEO</fullName>

        <accessLevel>Edit</accessLevel>

        <accountSettings>

           <caseAccessLevel>Read</caseAccessLevel>

           <contactAccessLevel>Edit</contactAccessLevel>

           <opportunityAccessLevel>Edit</opportunityAccessLevel>

```


Metadata Types SharingRules

```
        </accountSettings>

        <criteriaItems>

           <field>Name</field>

           <operation>startsWith</operation>

           <value>Test</value>

        </criteriaItems>

        <description>my account criteria rule description</description>

        <label>AccountCriteriaShareWithCEO</label>

        <sharedTo>

           <role>CEO</role>

        </sharedTo>

      </sharingCriteriaRules>

   </SharingRules>

```

The following sample XML definition represents an ownership-based sharing rule in API version 33.0.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <SharingRules xmlns="http://soap.sforce.com/2006/04/metadata">

      <sharingOwnerRules>

        <fullName>MyCase</fullName>

        <accessLevel>Edit</accessLevel>

        <description>my case test owner sharing rule desc</description>

        <label>MyCase</label>

        <sharedFrom>

           <role>COO</role>

        </sharedFrom>

        <sharedTo>

           <role>CEO</role>

        </sharedTo>

      </sharingOwnerRules>

   </SharingRules>

```

The following sample XML definition represents a territory-based sharing rule in API version 33.0.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <SharingRules xmlns="http://soap.sforce.com/2006/04/metadata">

      <sharingTerritoryRules>

        <fullName>MyAccountTerritoryRule</fullName>

        <accessLevel>Read</accessLevel>

        <accountSettings>

           <caseAccessLevel>None</caseAccessLevel>

           <contactAccessLevel>Read</contactAccessLevel>

           <opportunityAccessLevel>None</opportunityAccessLevel>

        </accountSettings>

        <description>MyAccountTerritoryRule desc</description>

        <label>MyAccountTerritoryRule</label>

        <sharedFrom>

           <territory>My_territory</territory>

        </sharedFrom>

        <sharedTo>

           <role>CEO</role>

        </sharedTo>

      </sharingTerritoryRules>

   </SharingRules>

```


Metadata Types SharingRules

The following is the definition of two account owner-based sharing rules in API version 32.0 and earlier. The file name corresponds to
`Account.sharingRules` under the `accountSharingRules` directory. In this definition, ownerRules corresponds to
AccountOwnerSharingRule.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <AccountSharingRules xmlns="http://soap.sforce.com/2006/04/metadata">

      <ownerRules>

        <fullName>G1Dev_G2New</fullName>

        <sharedFrom>

           <group>G1Dev</group>

        </sharedFrom>

        <sharedTo>

           <group>G2New</group>

        </sharedTo>

        <accountAccessLevel>Read</caseAccessLevel>

        <caseAccessLevel>None</caseAccessLevel>

        <contactAccessLevel>Read</contactAccessLevel>

        <name>G1Dev_G2New</name>

        <opportunityAccessLevel>Edit</opportunityAccessLevel>

      </ownerRules>

      <ownerRules>

        <fullName>G2New_R1New</fullName>

        <sharedFrom>

           <group>G2New</group>

        </sharedFrom>

        <sharedTo>

           <roleAndSubordinates>R1New</roleAndSubordinates>

        </sharedTo>

        <accountAccessLevel>Edit</accountAccessLevel>

        <caseAccessLevel>Read</caseAccessLevel>

        <contactAccessLevel>Edit</contactAccessLevel>

        <name>G2New_R1New</name>

        <opportunityAccessLevel>None</opportunityAccessLevel>

      </ownerRules>

   </AccountSharingRules>

```

The following is the definition of a user criteria-based sharing rule and a user membership-based sharing rule in API version 32.0 and
earlier. The file name corresponds to `User.sharingRules` under the `userSharingRules` directory.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <UserSharingRules xmlns="http://soap.sforce.com/2006/04/metadata">

      <criteriaBasedRules>

        <fullName>shareUsers2</fullName>

        <sharedTo>

           <group>Asia_Division</group>

        </sharedTo>

        <criteriaItems>

           <field>FirstName</field>

           <operation>equals</operation>

           <value>John</value>

        </criteriaItems>

        <name>shareUsers2</name>

        <userAccessLevel>Read</userAccessLevel>

      </criteriaBasedRules>

      <membershipRules>

```


#### Metadata Types BaseSharingRule

```
        <fullName>shareUsers1</fullName>

        <sharedTo>

           <group>South_America_Division</group>

        </sharedTo>

        <sharedFrom>

           <group>Asia_Division</group>

        </sharedFrom>

        <name>shareUsers1</name>

        <userAccessLevel>Read</userAccessLevel>

      </membershipRules>

   </UserSharingRules>

```

The following shows a sample `package.xml` file.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>ObjA__c.*</members>

        <name>SharingCriteriaRule</name>

      </types>

      <types>

        <members>ObjA__c.*</members>

        <name>SharingOwnerRule</name>

      </types>

      <version>66.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### 1. BaseSharingRule

This component is removed as of API version 33.0 and is available in earlier versions only. Use SharingBaseRule instead. Represents
the base container for criteria-based and owner-based sharing rules.

2. CriteriaBasedSharingRule
This component is removed as of API version 33.0 and is available in earlier versions only. Use SharingRules instead. Represents a
criteria-based sharing rule. CriteriaBasedSharingRule enables you to share records based on specific criteria.

3. OwnerSharingRule
Represents an ownership-based sharing rule. OwnerSharingRule enables you to share records owned by a set of users with another
set, using rules that specify the access level of the target user group. This component is removed as of API version 33.0 and is available
in earlier versions only.

#### BaseSharingRule

This component is removed as of API version 33.0 and is available in earlier versions only. Use SharingBaseRule instead. Represents the
base container for criteria-based and owner-based sharing rules.

This type extends the Metadata metadata type and inherits its `fullName` field.


#### Metadata Types CriteriaBasedSharingRule

Note: You can’t create a BaseSharingRule component directly. Use the components under the CriteriaBasedSharingRule or
OwnerSharingRule metadata types instead.

Version

BaseSharingRule on page 2304 components are available in API version 24.0 and later.

Fields

**Field** **Field Type** **Description**

`sharedTo` SharedTo Required. Specifies who the record is shared
with.

`fullName` string The unique identifier for API access.The
`fullName` can contain only underscores and

alphanumeric characters. It must be unique,
begin with a letter, not include spaces, not end
with an underscore, and not contain two
consecutive underscores. This field is inherited
from the Metadata component.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

#### CriteriaBasedSharingRule

This component is removed as of API version 33.0 and is available in earlier versions only. Use SharingRules instead. Represents a
criteria-based sharing rule. CriteriaBasedSharingRule enables you to share records based on specific criteria.

It extends the BaseSharingRule metadata type and inherits its `sharedTo` field. For more information, see “Criteria-Based Sharing Rules
Overview” in Salesforce Help.

Note: You can’t create a CrteriaBasedSharingRule component directly. Use the child components instead.

Declarative Metadata File Suffix and Directory Location

#### CriteriaBasedSharingRule components are stored within the SharingRules component in the criteriaBasedRules field.

Version

#### CriteriaBasedSharingRule components are available in API version 24.0 and later.


Metadata Types CriteriaBasedSharingRule

Special Access Rules

As of Spring ’20 and later, only users with the View Setup and Configuration permission can access this object, and only users with the
Manage Sharing permission can edit this object.

Fields

The following information assumes that you’re familiar with implementing sharing rules for standard objects and custom objects. For
more information on these fields, see Sharing Settings in Salesforce Help.

**Field** **Field Type** **Description**

`criteriaItems` FilterItem[] List that represents the criteria for the sharing
rule. The possible values are:

**•** `field`

**•** `operation`

**•** `value`

AccountCriteriaBasedSharingRule

Represents a criteria-based sharing rule for accounts. It extends the CriteriaBasedSharingRule metadata type and inherits its
`criteriaItems` field.

AccountCriteriaBasedSharingRule is used by the `criteriaBasedRules` field in AccountSharingRules.

**Field** **Field Type** **Description**

`accountAccessLevel` `ShareAccessLevelNoNone` Required. A value that represents the level of access that the
(enumeration of type string) user or group has to the account. The possible values are:

**•** `Read`

**•** `Edit`

**•** `All`

`booleanFilter` string Represents the filter logic of the sharing rule.

```
caseAccessLevel ShareAccessLevelNoAll
```

(enumeration of type string)

```
contactAccessLevel ShareAccessLevelNoAll
```

(enumeration of type string)


Required. A value that represents the level of access that the
user or group has to cases associated with the account. The
possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

Required. A value that represents the level of access that the
user or group has to contacts associated with the account. The
possible values are:

**•** `None`

**•** `Read`

Metadata Types CriteriaBasedSharingRule

**Field** **Field Type** **Description**

**•** `Edit`

`description` string

Represents the description of the sharing rule. Maximum of 1000
characters.

This field is available in API version 29.0 and later.

`name` string Required. Name for the sharing rule. Corresponds to **Label** in
the user interface.

```
opportunityAccessLevel ShareAccessLevelNoAll
```

(enumeration of type string)

CampaignCriteriaBasedSharingRule

Required. A value that represents the level of access that a target
group is granted for any associated opportunity. The possible
values are:

**•** `None`

**•** `Read`

**•** `Edit`

Represents a criteria-based sharing rule for campaigns. It extends the CriteriaBasedSharingRule metadata type and inherits its
`criteriaItems` field.

CampaignCriteriaBasedSharingRule is used by the `criteriaBasedRules` field in CampaignSharingRules.

**Field** **Field Type** **Description**

`booleanFilter` string Represents the filter logic of the sharing rule.

`description` string Represents the description of the sharing rule. Maximum of 1000
characters. This field is available in API version 29.0 and later.

`campaignAccessLevel` `ShareAccessLevelNoNone` Required. A value that represents the level of access that a target
(enumeration of type string) group is granted for a campaign. The possible values are:

**•** `Read`

**•** `Edit`

**•** `All`

`name` string Required. Name for the sharing rule. Corresponds to **Label** in
the user interface.

CaseCriteriaBasedSharingRule

Represents a criteria-based sharing rule for cases. It extends the CriteriaBasedSharingRule metadata type and inherits its
`criteriaItems` field.

CaseCriteriaBasedSharingRule is used by the `criteriaBasedRules` field in CaseSharingRules.


Metadata Types CriteriaBasedSharingRule

**Field** **Field Type** **Description**

`booleanFilter` string Represents the filter logic of the sharing rule.

`description` string

Represents the description of the sharing rule. Maximum of 1000
characters.

This field is available in API version 29.0 and later.

`caseAccessLevel` `ShareAccessLevelReadEdit` Required. A value that represents the level of access being
(enumeration of type string) granted for a case. The possible values are:

**•** `Read`

**•** `Edit`

`name` string Required. Name for the sharing rule. Corresponds to **Label** in
the user interface.

ContactCriteriaBasedSharingRule

Represents a criteria-based sharing rule for contacts. It extends the CriteriaBasedSharingRule metadata type and inherits its
`criteriaItems` field.

ContactCriteriaBasedSharingRule is used by the `criteriaBasedRules` field in ContactSharingRules.

**Field** **Field Type** **Description**

`booleanFilter` string Represents the filter logic of the sharing rule.

`description` string

```
contactAccessLevel ShareAccessLevelReadEdit
```

(enumeration of type string)

Represents the description of the sharing rule. Maximum of 1000
characters.

This field is available in API version 29.0 and later.

Required. A value that represents the level of access being
granted to the target group, role, or user for a contact. The
possible values are:

**•** `Read`

**•** `Edit`

`name` string Required. Name for the sharing rule. Corresponds to **Label** in
the user interface.

LeadCriteriaBasedSharingRule

Represents a criteria-based sharing rule for leads. It extends the CriteriaBasedSharingRule metadata type and inherits its `criteriaItems`
field.

LeadCriteriaBasedSharingRule is used by the `criteriaBasedRules` field in LeadSharingRules.


Metadata Types CriteriaBasedSharingRule

**Field** **Field Type** **Description**

`booleanFilter` string Represents the filter logic of the sharing rule.

`description` string Represents the description of the sharing rule. Maximum of 1000
characters. This field is available in API version 29.0 and later.

`leadAccessLevel` `ShareAccessLevelReadEdit` Required. A value that represents the level of allowed access.
(enumeration of type string) The possible values are:

**•** `Read`

**•** `Edit`

`name` string Required. Name for the sharing rule. Corresponds to **Label** in
the user interface.

OpportunityCriteriaBasedSharingRule

Represents a criteria-based sharing rule for opportunities. It extends the CriteriaBasedSharingRule metadata type and inherits its
`criteriaItems` field.

OpportunityCriteriaBasedSharingRule is used by the `criteriaBasedRules` field in OpportunitySharingRules.

**Field** **Field Type** **Description**

`booleanFilter` string Represents the filter logic of the sharing rule.

`description` string

Represents the description of the sharing rule. Maximum of 1000
characters.

This field is available in API version 29.0 and later.

`opportunityAccessLevel` `ShareAccessLevelReadEdit` Required. A value that represents the level of allowed access.
(enumeration of type string) The possible values are:

**•** `Read`

**•** `Edit`

`name` string Required. Name for the sharing rule. Corresponds to **Label** in
the user interface.

CustomObjectCriteriaBasedSharingRule

Represents a criteria-based sharing rule for custom objects. It extends the CriteriaBasedSharingRule metadata type and inherits its
`criteriaItems` field.

CustomObjectCriteriaBasedSharingRule is used by the `criteriaBasedRules` field in CustomObjectSharingRules.


Metadata Types CriteriaBasedSharingRule

**Field** **Field Type** **Description**

`accessLevel` string Required. A value that represents the type of allowed sharing.
The possible values are:

**•** `Read`

**•** `Edit`

**•** `All`

`booleanFilter` string Represents the filter logic of the sharing rule.

`description` string

Represents the description of the sharing rule. Maximum of 1000
characters.

This field is available in API version 29.0 and later.

`name` string Required. Name for the sharing rule. Corresponds to **Label** in
the user interface.

UserCriteriaBasedSharingRule

Represents a criteria-based sharing rule for users. It extends the CriteriaBasedSharingRule metadata type and inherits its `criteriaItems`
field.

UserCriteriaBasedSharingRule is used by the `criteriaBasedRules` field in UserSharingRules.

**Field** **Field Type** **Description**

`booleanFilter` string Represents the filter logic of the sharing rule.

`description` string

Represents the description of the sharing rule. Maximum of 1000
characters.

This field is available in API version 29.0 and later.

`name` string Required. Name for the sharing rule. Corresponds to **Label** in
the user interface.

`userAccessLevel` `ShareAccessLevelReadEdit` Required. A value that represents the type of allowed sharing.
(enumeration of type string) The possible values are:

**•** `Read`

**•** `Edit`

Declarative Metadata Sample Definition

The following is the definition of two owner-based sharing rules and one criteria-based sharing rule containing two criteria items. The
file name corresponds to the Account.sharingRules file under the accountSharingRules directory.

```
<?xml version="1.0" encoding="UTF-8"?>

<AccountSharingRules xmlns="http://soap.sforce.com/2006/04/metadata">

  <ownerRules>

   <fullName>G1Dev_G2New</fullName>

```


Metadata Types CriteriaBasedSharingRule

```
      <sharedTo>

       <group>G2New</group>

      </sharedTo>

      <sharedFrom>

       <group>G1Dev</group>

      </sharedFrom>

      <accountAccessLevel>Read</accountAccessLevel>

      <caseAccessLevel>None</caseAccessLevel>

      <contactAccessLevel>Read</contactAccessLevel>

     </ownerRules>

      <fullName>G2New_R1New</fullName>

      <sharedTo>

       <roleAndSubordinates>R1New</roleAndSubordinates>

      </sharedTo>

      <sharedFrom>

       <group>G2New</group>

      </sharedFrom>

      <accountAccessLevel>Edit</accountAccessLevel>

      <caseAccessLevel>Read</caseAccessLevel>

      <contactAccessLevel>Edit</contactAccessLevel>

      <name>G2New_R1New</name>

      <opportunityAccessLevel>None</opportunityAccessLevel>

     </ownerRules>

     <criteriaBasedRules>

      <fullName>AccountCriteria</fullName>

      <sharedTo>

       <group>G1</group>

      </sharedTo>

      <criteriaItems>

       <field>BillingCity</field>

       <operation>equals</operation>

       <value>San Francisco</value>

      </criteriaItems>

      <criteriaItems>

       <field>MyChkBox__c</field>

       <operation>notEqual</operation>

       <value>False</value>

      </criteriaItems>

      <accountAccessLevel>Read</accountAccessLevel>

      <booleanFilter>1 OR 2</booleanFilter>

      <caseAccessLevel>None</caseAccessLevel>

      <contactAccessLevel>Read</contactAccessLevel>

      <name>AccountCriteria</name>

      <opportunityAccessLevel>None</opportunityAccessLevel>

     </criteriaBasedRules>

   </AccountSharingRules>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


#### Metadata Types OwnerSharingRule OwnerSharingRule

Represents an ownership-based sharing rule. OwnerSharingRule enables you to share records owned by a set of users with another set,
using rules that specify the access level of the target user group. This component is removed as of API version 33.0 and is available in
earlier versions only.

#### OwnerSharingRule extends the BaseSharingRule metadata type and inherits its SharedTo field. For more information, see “Sharing Rules”

in the Salesforce online help.

Note: You can’t create a OwnerSharingRule component directly. Use the child components instead.

Declarative Metadata File Suffix and Directory Location

#### OwnerSharingRules components are stored within the SharingRules component in the ownerRules field.

Version

#### OwnerSharingRules components are available in API version 24.0 and later.

Special Access Rules

As of Spring ’20 and later, only users with the View Setup and Configuration permission can access this object, and only users with the
Manage Sharing permission can edit this object.

Fields

The following information assumes that you are familiar with implementing sharing rules for standard objects and custom objects. For
more information on these fields, see “Sharing Settings” in the Salesforce online help.

**Field** **Field Type** **Description**

`sharedFrom` SharedTo Required. Specifies the record owners.

`sharedTo` SharedTo Required. Specifies who the record should be
shared with.

`fullName` string The unique identifier for API access. The
`fullName` can contain only underscores and

alphanumeric characters. It must be unique,
begin with a letter, not include spaces, not end
with an underscore, and not contain two
consecutive underscores. This field is inherited
from the Metadata component.

AccountOwnerSharingRule

Represents a sharing rule for an account with users other than the owner. It extends the OwnerSharingRule metadata type and inherits
its `fullName`, `sharedFrom`, and `sharedTo` fields.

AccountOwnerSharingRule is used by the `ownerRules` field in AccountSharingRules.


Metadata Types OwnerSharingRule

**Field** **Field Type** **Description**

`accountAccessLevel` `ShareAccessLevelNoNone` Required. A value that represents the level of access that a group
(enumeration of type string) or role has to the account. The possible values are:

**•** `Read`

**•** `Edit`

**•** `All`

```
caseAccessLevel ShareAccessLevelNoAll
```

(enumeration of type string)

```
contactAccessLevel ShareAccessLevelNoAll
```

(enumeration of type string)

Required. A value that represents the level of access that a group
or role has to cases associated with the account. The possible
values are:

**•** `None`

**•** `Read`

**•** `Edit`

Required. A value that represents the level of access that a group
or role has to contacts associated with the account. The possible
values are:

**•** `None`

**•** `Read`

**•** `Edit`

`description` string Represents the description of the sharing rule. Maximum of 1000
characters.This field is available in API version 29.0 and later.

`name` string Required. Name for the sharing rule. Corresponds to **Label** in
the user interface.

```
opportunityAccessLevel ShareAccessLevelNoAll
```

(enumeration of type string)

CampaignOwnerSharingRule

Required. A value that represents the level of access that a group
or role is granted for any associated opportunity. The possible
values are:

**•** `None`

**•** `Read`

**•** `Edit`

Represents a sharing rule for a campaign with users other than the owner. It extends the OwnerSharingRule metadata type and inherits
its `fullName`, `sharedFrom`, and `sharedTo` fields.

CampaignOwnerSharingRule is used by the `ownerRules` field in CampaignSharingRules.

**Field** **Field Type** **Description**

`campaignAccessLevel` `ShareAccessLevelNoNone` A value that represents the level of access that a group or role
(enumeration of type string) is granted for a campaign. The possible values are:

**•** `Read`


Metadata Types OwnerSharingRule

**Field** **Field Type** **Description**

**•** `Edit`

**•** `All`

`description` string Represents the description of the sharing rule. Maximum of 1000
characters.This field is available in API version 29.0 and later.

`name` string Name for the sharing rule. Corresponds to **Label** in the user
interface.

CaseOwnerSharingRule

Represents a sharing rule for a case with users other than the owner. It extends the OwnerSharingRule metadata type and inherits its
`fullName`, `sharedFrom`, and `sharedTo` fields.

CaseOwnerSharingRule is used by the `ownerRules` field in CaseSharingRules. All the following fields are required.

**Field** **Field Type** **Description**

`caseAccessLevel` `ShareAccessLevelReadEdit` Required. A value that represents the level of access that a group
(enumeration of type string) or role is granted for a case. The possible values are:

**•** `Read`

**•** `Edit`

`description` string Represents the description of the sharing rule. Maximum of 1000
characters.This field is available in API version 29.0 and later.

`name` string Required. Name for the sharing rule. Corresponds to **Label** in
the user interface.

ContactOwnerSharingRule

Represents a sharing rule for a contact with users other than the owner. It extends the OwnerSharingRule metadata type and inherits
its `fullName`, `sharedFrom`, and `sharedTo` fields.

ContactOwnerSharingRule is used by the `ownerRules` field in ContactSharingRules.

**Field** **Field Type** **Description**

`contactAccessLevel` `ShareAccessLevelReadEdit` Required. A value that represents the level of access that a group
(enumeration of type string) or role is granted for a contact. The possible values are:

**•** `Read`

**•** `Edit`

`description` string Represents the description of the sharing rule. Maximum of 1000
characters.This field is available in API version 29.0 and later.

`name` string Required. Name for the sharing rule. Corresponds to **Label** in
the user interface.


Metadata Types OwnerSharingRule

LeadOwnerSharingRule

Represents a sharing rule for a lead with users other than the owner. It extends the OwnerSharingRule metadata type and inherits its
fullName, `sharedFrom`, and `sharedTo` fields.

LeadOwnerSharingRule is used by the `ownerRules` field in LeadSharingRules.

**Field** **Field Type** **Description**

`leadAccessLevel` `ShareAccessLevelReadEdit` Required. A value that represents the level of access that a group
(enumeration of type string) or role is granted for a lead. The possible values are:

**•** `Read`

**•** `Edit`

`description` string Represents the description of the sharing rule. Maximum of 1000
characters.This field is available in API version 29.0 and later.

`name` string Required. Required. Name for the sharing rule. Corresponds to
**Label** in the user interface.

OpportunityOwnerSharingRule

Represents a sharing rule for an opportunity with users other than the owner. It extends the OwnerSharingRule metadata type and
inherits its `fullName`, `sharedFrom`, and `sharedTo` fields.

OpportunityOwnerSharingRule is used by the `ownerRules` field in OpportunitySharingRules.

**Field** **Field Type** **Description**

`name` string Required. Name for the sharing rule. Corresponds to **Label** in
the user interface.

`description` string Represents the description of the sharing rule. Maximum of 1000
characters.This field is available in API version 29.0 and later.

`opportunityAccessLevel` `ShareAccessLevelReadEdit` Required. A value that represents the level of access that a group
(enumeration of type string) or role is granted for an opportunity. The possible values are:

**•** `Read`

**•** `Edit`

AccountTerritorySharingRule

Represents a rule for sharing an account within a territory. It extends the OwnerSharingRule metadata type and inherits its `fullName`,
`sharedFrom`, and `sharedTo` fields.

AccountTerritorySharingRule is used by the `ownerRules` field in AccountTerritorySharingRules.


Metadata Types OwnerSharingRule

**Field** **Field Type** **Description**

```
accountAccessLevel ShareAccessLevelNoNone
```

(enumeration of type string)

```
caseAccessLevel ShareAccessLevelNoAll
```

(enumeration of type string)

```
contactAccessLevel ShareAccessLevelNoAll
```

(enumeration of type string)

Required. A value that represents the level of access that a
Territory or TerritoryAndSubordinates group is granted for an
account territory. The possible values are:

**•** `Read`

**•** `Edit`

**•** `All`

Required. A value that represents the level of access that a
Territory or TerritoryAndSubordinates group is granted for all
child cases to an account. The possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

Required. A value that represents the level of access that a
Territory or TerritoryAndSubordinates group is granted for all
related contacts on an account. The possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

`description` string Represents the description of the sharing rule. Maximum of 1000
characters.This field is available in API version 29.0 and later.

`name` string Required. Name for the sharing rule. Corresponds to **Label** in
the user interface.

`opportunityAccessLevel` `ShareAccessLevelNoAll` Required. A value that represents the level of access that a
(enumeration of type string) Territory or TerritoryAndSubordinates group is granted for all

opportunities associated with an account. The possible values
are:

**•** `None`

**•** `Read`

**•** `Edit`

CustomObjectOwnerSharingRule

Represents a sharing rule for custom objects. It extends the OwnerSharingRule metadata type and inherits its `fullName`, `sharedFrom`,
and `sharedTo` fields.

CustomObjectOwnerSharingRule is used by the `ownerRules` field in CustomObjectSharingRules.


### Metadata Types SharingSet

**Field** **Field Type** **Description**

`accessLevel` string Required. A value that represents the level of access that a group
or role is granted to a custom object. The possible values are:

**•** `Read`

**•** `Edit`

**•** `All`

`description` string

Represents the description of the sharing rule. Maximum of 1000
characters.

This field is available in API version 29.0 and later.

`name` string Required. Name for the sharing rule. Corresponds to **Label** in
the user interface.

UserMembershipSharingRule

Represents a sharing rule to share members of a group with another group of users. It extends the OwnerSharingRule metadata type
and inherits its `fullName`, `sharedFrom`, and `sharedTo` fields.

UserMembershipSharingRule is used by the `ownerRules` field in UserSharingRules on page 2301.

**Field** **Field Type** **Description**

`description` string Represents the description of the sharing rule. Maximum of 1000
characters.This field is available in API version 29.0 and later.

`name` string Required. Name for the sharing rule. Corresponds to **Label** in
the user interface.

`userAccessLevel` `ShareAccessLevelReadEdit` Required. A value that represents the level of access that a group
(enumeration of type string) or role is granted for a user. The possible values are:

**•** `Read`

**•** `Edit`

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### SharingSet

Represents a sharing set. A sharing set defines an access mapping that grants portal or community users access to objects that are
associated with their accounts or contacts.

This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types SharingSet

For example, you can grant portal or community users access to all cases related to their account record. Similarly, you can grant portal
or community users access to all cases related to a parent account that is identified on the user’s account record.

File Suffix and Directory Location

SharingSet components have the suffix `.sharingSet` and are stored in the `sharingSets` folder.

Version

SharingSet components are available in API version 30.0 and later.

Special Access Rules

As of Spring ’20 and later, only users with the View Setup and Configuration permission can access this object, and only users with the
Manage Sharing permission can edit this object. To create or update sharing sets, you need the Customize Application permission.

Sharing sets are available with these licenses.

**•** Authenticated Website

**•** Customer Community Login

**•** Customer Community Plus

**•** Partner Community

**•** Customer Community User

**•** High Volume Customer Portal

**•** High Volume Portal

**•** Overage Authenticated Website User

**•** Overage High Volume Customer Portal User

Fields

**Field Name** **Field Type** **Description**

`accessMappings` AccessMapping[] A list of access mappings on a sharing set.

`description` string The sharing set description. Limit: 255 characters.

`name` string Required. The unique identifier for API access. Corresponds to **Sharing**
**Set Name** on the user interface.

`profiles` string[]

AccessMapping

The profiles of users that are granted access to the target objects. Profiles
must be associated with a license that can use sharing sets. See Special
Access Rules for more information.

AccessMapping represents an access mapping in the sharing set, which grants access to a target object by looking up to an account or
contact associated with the user.


Metadata Types SharingSet

You can grant portal users access to a target object, or to both a target object and its associated objects, such as an account and its
contacts and cases.

**Field Name** **Field Type** **Description**

`accessLevel` string Required. The target object access level granted to the portal user. Valid values
are:

**•** `Read`

**•** `Edit`

`objectField` string

Required. A lookup to the target object, which supports standard or custom
fields, or an ID. For accounts or cases associated with entitlements, use
`Entitlement.Account` or `Entitlement.Case` .

`object` string Required. The target object to which the portal user is gaining access, and
refers to one of the following:

**•** `Account`

**•** `Campaign`

**•** `Contact`

**•** `Case`

**•** Custom Objects (for example, `ObjA__c` )

**•** `Opportunity`

**•** `Order`

**•** `ServiceContract`

**•** `User`

**•** `WorkOrder`

Portal users gain access to all order entitlements and order items under an
account to which they have access.

`userField` string

Required. The user’s lookup to an account, contact, or a standard or custom
field derived from an account or contact. Either the user or the user’s manager
can be used in the lookup. Valid values are:

**•** `Account`

**•** `Account.` _**`Field`**_

**•** `Contact`

**•** `Contact.` _**`Field`**_

**•** `Contact.RelatedAccount`

**•** `Manager.Account`

**•** `Manager.Contact`

_**`Field`**_ refers to a standard or custom field based on an account or contact.


Metadata Types SharingSet

Declarative Metadata Sample Definition

The following is an example of a SharingSet component that grants users access to all contacts whose `ReportsTo` fields match the
users’ contacts.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <SharingSet xmlns="http://soap.sforce.com/2006/04/metadata">

     <accessMappings>

      <accessLevel>Read</accessLevel>

      <objectField>ReportsTo</objectField>

      <object>Contact</object>

      <userField>Contact</userField>

     </accessMappings>

     <description>User Access Mapping</description>

     <name>User</name>

     <profiles>customer community user</profiles>

   </SharingSet>

```

The following is an example of a SharingSet component that grants users access to all cases that are related to an entitlement, which is
associated with the user’s account.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <SharingSet xmlns="http://soap.sforce.com/2006/04/metadata">

     <name>Case</name>

     <accessMappings>

      <accessLevel>Edit</accessLevel>

      <objectField>Entitlement.Account</objectField>

      <object>Case</object>

      <userField>Account</userField>

     </accessMappings>

   </SharingSet>

```

The following is an example of a SharingSet component with a list of access mappings.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <SharingSet xmlns="http://soap.sforce.com/2006/04/metadata">

     <description>This is a basic sharing set with several access mappings.</description>

     <name>Basic</name>

     <profiles>customer community user</profiles>

     <accessMappings>

      <accessLevel>Read</accessLevel>

      <objectField>Id</objectField>

      <object>Account</object>

      <userField>Account</userField>

     </accessMappings>

     <accessMappings>

      <accessLevel>Edit</accessLevel>

      <objectField>Account</objectField>

      <object>Contact</object>

      <userField>Account</userField>

     </accessMappings>

     <accessMappings>

      <accessLevel>Edit</accessLevel>

      <objectField>Contact</objectField>

      <object>Case</object>

```


### Metadata Types SiteDotCom

```
      <userField>Contact</userField>

     </accessMappings>

     <accessMappings>

      <accessLevel>Read</accessLevel>

      <objectField>AccountLookup__c</objectField>

      <object>HVPUAccessible__c</object>

      <userField>Account</userField>

     </accessMappings>

   </SharingSet>

```

The following is an example `package.xml` that references the previous definition.

```
   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

     <fullName>SharingSetBasic</fullName>

     <types>

      <members>HVPUAccessible__c.AccountLookup__c</members>

      <members>HVPUAccessible__c.ContactLookup__c</members>

      <name>CustomField</name>

     </types>

     <types>

      <members>HVPUAccessible__c</members>

      <name>CustomObject</name>

     </types>

     <types>

      <members>Basic</members>

      <name>SharingSet</name>

     </types>

     <version>30.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### SiteDotCom

Represents a site for deployment.

### SiteDotCom extends the MetadataWithContent type and inherits its fullName and content fields.

Declarative Metadata File Suffix and Directory Location

### SiteDotCom components are stored in the siteDotComSites directory of the corresponding package directory.

The file name for the metadata `.xml` file is `[sitename]1.site-meta.xml` . The file name for the site file is

`[sitename]1.site` .

When a Lightning site is created, two sites are made behind the scenes: CustomSite (of type ChatterNetwork) and SiteDotComSite (of
type ChatterNetworkPicasso). These sites are named, respectively, _<site_name>_ and _<site_name>1_ . The corresponding MDAPI file
names are _`<site_name>.`_ `site-meta.xml` and _`<site_name>`_ `1.site-meta.xml` . 1 is appended to the SiteDotComSite
type to keep the name unique from the corresponding CustomSite site.


Metadata Types SiteDotCom

Note: There is a file size limitation when using the Metadata API to deploy a site from sandbox to production. The assets in the
`.site` file can't be larger than 40 MB. The site gets created, but the assets show in the new site as broken. To fix the assets, export
the assets from the sandbox environment separately and then import them into your new site.

Version

`SiteDotCom` components are available in API version 30.0 and later.

Fields

**Field** **Field Type** **Description**

`label` string The name of the site that you’re deploying.

`siteType` (enumeration of type
string)

Declarative Metadata Sample Definition

Here are two examples of a SiteDotCom XML definition.

Required. Identifies whether the site is a
`ChatterNetworkPicasso` site for Experience
Cloud Sites, or a `Siteforce` site for Site.com sites.

```
<?xml version="1.0" encoding="UTF-8"?>

<SiteDotCom xmlns="http://soap.sforce.com/2006/04/metadata">

   <label>testsite</label>

   <siteType>Siteforce</siteType>

</SiteDotCom>

<?xml version="1.0" encoding="UTF-8"?>

<SiteDotCom xmlns="http://soap.sforce.com/2006/04/metadata">

   <label>testCommunity</label>

   <siteType>ChatterNetworkPicasso</siteType>

</SiteDotCom>

```

Usage

You can only deploy a `.site` file retrieved in Summer ’19 or later. Older files aren’t supported.

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types Skill Skill

Represents the settings for a skill used for field service or to route chats to agents in Chat, such as the name of the skill and which agents
the skills are assigned to.

This type extends the Metadata metadata type and inherits its `fullName` field.

File Suffix and Directory Location

### Skill values are stored in the <developer_name>.skill file in the skills directory.

Version

### Skill is available in API version 28.0 and later.

Fields

**Field Name** **Field Type** **Description**

### assignments SkillAssignments Specifies how skills are assigned to Chat users. Skills can be

assigned to sets of users or sets of profiles.

`description` string Specifies the description of the skill. This field is available in
API version 38.0 and later.

`label` string Specifies the name of the skill.

`skillType` string

### SkillAssignments

Specifies the skill type, such as language or department,
associated with the skill. This field is available in API version
58.0 and later.

Represents which users and user profiles to whom specific skills are assigned.

Fields

**Field Name** **Field Type** **Description**

### profiles SkillProfileAssignments Specifies the profiles that are associated with a specific skill. users SkillUserAssignments Specifies the users that are associated with a specific skill. SkillProfileAssignments

Represents the profiles that are associated with a specific skill.


### Metadata Types StandardValueSet

Fields

**Field Name** **Field Type** **Description**

`profile` string Specifies the custom name of the profile associated with a
specific skill.

SkillUserAssignments

Represents the users that are associated with a specific skill.

Fields

**Field Name** **Field Type** **Description**

`user` string Specifies the username of the user associated with a specific
skill.

Declarative Metadata Sample Definition

This is a sample of a `skill` file.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Skill xmlns="http://soap.sforce.com/2006/04/metadata">

      <label>My Skill 1</label>

      <assignments>

        <profiles>

           <profile>LiveAgentOperator</profile>

           <profile>LiveAgentSupervisor</profile>

        </profiles>

        <users>

           <user>jdoe@acme.com</user>

        </users>

      </assignments>

   </Skill>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

### StandardValueSet

Represents the set of values in a standard picklist field. This type extends the Metadata metadata type and inherits its `fullName` field.


Metadata Types StandardValueSet

File Suffix and Directory Location

StandardValueSet components have the suffix `.standardValueSet` and are stored in the `standardValueSets` folder.

Version

StandardValueSet components are available in API version 38.0 and later.

Fields

**Field Name** **Field Type** **Description**

`groupingStringEnum` string Groups picklist and enumerated values. For example, for the picklist
values of the `Status` field on the Service Appointment object, `Done`

and `Finished` can both have a grouping string of `Completed` .
Available in API version 41.0 and later.

`sorted` boolean Required. Indicates whether a global value set is sorted in alphabetical
order. By default, this value is `false` .

`standardValue` StandardValue[]

Defines each value in a standard picklist’s value set. The
`groupingString` value is available in API version 38.0 and later.

When you deploy a StandardValueSet, this array must contain at least
one picklist value. Otherwise, you receive an error.

Note: When setting `standardValue` on Record Types,
including person account record types, new picklist values loaded
into your organization through the Metadata API don’t display in
the picklist UI by default. For users to see the new values, go to
the Record Types list for the object containing the picklist field,
click **Edit**, and add the new value to the Selected Fields list.

Declarative Metadata Sample Definition

The following example shows a StandardValueSet component that’s defined as the Stage standard picklist on a customized opportunity
object.

```
<?xml version="1.0" encoding="UTF-8"?>

<StandardValueSet xmlns="http://soap.sforce.com/2006/04/metadata">

   <fullName>OpportunityStage</fullName> <!-- Enum name -->

   <standardValue>

     <fullName>Closed Abandoned</fullName>

   </standardValue>

   <standardValue>

     <fullName>Closed Won</fullName>

   </standardValue>

   <standardValue>

     <fullName>Closed Lost</fullName>

   </standardValue>

```


### Metadata Types StandardValueSetTranslation

```
   </StandardValueSet>

   <CustomObject>

      <fullName>Opportunity</fullName>

      <fields>

        <fullName>StageName</fullName> <!-- field name -->

        <label>Stage</label>

        <type>Picklist</type>

      </fields>

      <label>ObjectWithValueSet</label>

      <pluralLabel>ObjectWithValueSet</pluralLabel>

      <sharingModel>ReadWrite</sharingModel>

   </CustomObject>

```

For a list of standard value set names for standard picklists, see StandardValueSet Names and Standard Picklist Fields.

Wildcard Support in the Manifest File

This metadata type doesn’t support the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about
using the manifest file, see Deploying and Retrieving Metadata with the Zip File.

### StandardValueSetTranslation

Contains details for a standard picklist translation. It returns a translated standard value set.This type extends the Metadata metadata
type and inherits its `fullName` field.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

File Suffix and Directory Location

### StandardValueSetTranslation components have the suffix .standardValueSetTranslation and are stored in the

`standardValueSetTranslations` folder.

Translations are stored in a file with a format of `ValueSetName-lang.standardValueSetTranslation`, where
_`ValueSetName`_ is the global value set’s name, and lang is the translation language.

Version

### StandardValueSetTranslation components are available in API version 38.0 and later.

Fields

**Field** **Field Type** **Description**

`valueTranslation` ValueTranslation[] A list of values from global value sets to be translated.


### Metadata Types StaticResource

Declarative Metadata Sample Definition

The following is an example of a StandardValueSetTranslation component. When a value isn’t translated, its translation becomes a
comment that’s paired with its label.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <StandardValueSetTranslation xmlns="http://soap.sforce.com/2006/04/metadata">

      <valueTranslation>

        <masterLabel>Cold</masterLabel>

        <translation><!-- Cold --></translation>

      </valueTranslation>

      <valueTranslation>

        <masterLabel>Hot</masterLabel>

        <translation><!-- Hot --></translation>

      </valueTranslation>

      <valueTranslation>

        <masterLabel>Warm</masterLabel>

        <translation><!-- Warm --></translation>

      </valueTranslation>

   </StandardValueSetTranslation>

```

The following is an example `package.xml` that references the StandardValueSetTranslation definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

        <types>

        <members>AccountRating-fr</members>

        <name>StandardValueSetTranslation</name>

      </types>

      <version>38.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.

SEE ALSO:

Translations

### StaticResource

Represents a static resource file, often a code library in a ZIP file. Static resources allow you to upload content that you can reference in
a Visualforce page, including archives (such as .zip and .jar files), images, style sheets, JavaScript, and other files. Static resources can be
used only within your Salesforce org, so you can’t host content here for other apps or websites.

This type extends the MetadataWithContent metadata type and inherits its `content` and `fullName` fields.

File Suffix and Directory Location

The file suffix is `.resource` for the template file. The accompanying metadata file is named _`resource`_ `-meta.xml` .


Metadata Types StaticResource

Static resource components are stored in the `staticresources` folder in the corresponding package directory.

Version

Static resources are available in API version 12.0 and later.

Fields

This metadata type contains the following fields:

**Field Name** **Field Type** **Description**

`cacheControl` StaticResourceCacheControl
(enumeration of type string)

Required. Indicates whether the static resource is marked with a public caching
tag so that a third-party delivery client can cache the content. This field is available
in API version 14.0. The valid values are:

**•** Private

**•** Public

`content` base64Binary The static resource content. Base 64-encoded binary data. Before making an API
call, client applications must encode the binary attachment data as base64. Upon

receiving a response, client applications must decode the base64 data to binary.
This conversion is handled for you by a SOAP client. This field is inherited from
the MetadataWithContent component.

`contentType` string Required. The content type of the file, for example text/plain.

`description` string The description of the static resource.

`fullName` string

The static resource name. The name can only contain characters, letters, and the
underscore (_) character. The name must start with a letter, and can’t end with
an underscore or contain two consecutive underscore characters.

Inherited from the Metadata component, this field isn’t defined in the WSDL for
this component. It must be specified when creating, updating, or deleting. See
create() to see an example of this field specified for a call.

Declarative Metadata Sample Definition

```
<?xml version="1.0" encoding="UTF-8"?>

<StaticResource xmlns="http://soap.sforce.com/2006/04/metadata">

   <contentType>text/plain</contentType>

   <description>Test Resource</description>

</StaticResource>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
manifest file, see Deploying and Retrieving Metadata with the Zip File.


### Metadata Types StageAssignment StageAssignment

Represents a collection of fields to automatically assign stage definitions to records based on rule criteria.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

### StageAssignment components have the suffix .stageAssignment and are stored in the stageAssignments folder.

Version

### StageAssignment components are available in API version 64.0 and later.

Fields

**Field Name** **Description**

```
active

description

masterLabel

referenceObject

```

**Field Type**
boolean

**Description**

Required. Indicates whether the stage assignment rule is active ( `true` ) or not ( `false` ).
The default value is `true` . Active rules are evaluated when determining stage definition
assignments.

**Field Type**
string

**Description**
Description for the stage assignment rule.

**Field Type**
string

**Description**

Required. A user-friendly name for the stage assignment rule, which is defined when
the metadata component is created.

**Field Type**
string


Metadata Types StageAssignment

**Field Name** **Description**

**Description**

Required. Reference object that's associated with the stage assignment rule. This is
the API name of the Salesforce object for which the stage assignment rule applies (for
example, ApplicationForm or Order).

```
referenceObjectRecordType

ruleCriteria

stageDefinition

```

**Field Type**
string

**Description**
Record type of a reference object that's associated with the stage assignment rule.
When specified, the assignment rule applies only to records of the specified record
type.

**Field Type**

StgAssignmentRuleCriteria[]

**Description**
Collection of rule criteria to determine stage definition assignment. Rules are evaluated
in priority order, and the first matching rule determines which stage definition is
assigned to the record.

**Field Type**
string

**Description**
Default stage definition to assign when no rule criteria match. This provides a fallback
assignment when none of the defined rule criteria evaluate to true.

StgAssignmentRuleCriteria

Represents a collection of fields to define rule criteria for stage definition assignment. Rule criteria are evaluated in priority order, with
lower priority numbers evaluated first.

**Field Name** **Description**

```
condition

criteriaType

```

**Field Type**

StgAssignmentRuleCond[]

**Description**
Collection of conditions to evaluate for this rule criteria. You can combine multiple
conditions by using the `criteriaType` field to determine the overall evaluation
result.

**Field Type**
StageCriteriaType (enumeration of type string)


Metadata Types StageAssignment

**Field Name** **Description**

**Description**

Required. Specifies the criteria type that's used to evaluate the rule conditions. Valid
values are:

**•** `AND`

**•** `CUSTOMLOGIC`

**•** `OR`

```
logicalExpression

name

priority

stageDefinition

```

**Field Type**
string

**Description**
Formula to specify custom logic for evaluating conditions. It's used when
`criteriaType` is set to `CUSTOMLOGIC` .

**Field Type**
string

**Description**

Required. Name of the rule criteria.

**Field Type**
int

**Description**

Required. Priority order for evaluating this rule criteria when multiple criteria are defined.

Rules are evaluated in ascending priority order where lower numbers have higher
priority. For example, a rule with priority 1 is evaluated before a rule with priority 2.
The first rule that evaluates to true determines the stage definition assignment.

**Field Type**
string

**Description**

Required. Stage definition to assign when this rule criteria matches. This must be the
API name of a valid StageDefinition for the same reference object.

StgAssignmentRuleCond

Represents a collection of fields to define individual condition rules for stage assignment rule criteria. Each condition compares a field
value against a specified value using a comparison operator.

**Field Name** **Description**

```
fieldName

```

**Field Type**
string


Metadata Types StageAssignment

**Field Name** **Description**

**Description**

Required. API name of the field to evaluate for this condition.

```
operator

sequenceNumber

value

```

Usage

**Field Type**
StageConditionOperator (enumeration of type string)

**Description**

Required. Operator that's used to evaluate the field value. Valid values are:

**•** `Contains`

**•** `DoesNotContain`

**•** `Equals`

**•** `GreaterOrEqual`

**•** `GreaterThan`

**•** `LessOrEqual`

**•** `LessThan`

**•** `NotEqualTo`

**•** `StartsWith`

**Field Type**
int

**Description**

Required. Specifies the sequence number of this condition for reference in logical
expressions.

The sequence number is used in the `logicalExpression` field to create custom
boolean logic. For example, a condition with sequenceNumber 1 is referenced as "1"
in the expression "1 AND 2".

**Field Type**
string

**Description**

Required. Defines the value to compare against the field value.

The value is specified as a string regardless of the field type. For example, numeric
values are specified as "10000", dates as "2025-10-27", and text values as "Approved".

StageAssignment works in conjunction with StageDefinition to provide automated stage management. While StageDefinition defines
the stages, transitions, and workflows, StageAssignment determines which stage definition to apply to a record based on rule criteria.

Evaluation Process:

**•** When a record is created or updated, the system evaluates active StageAssignment rules for the object.


Metadata Types StageAssignment

**•** Rule criteria are evaluated in priority order where lower numbers have higher priority.

**•** The first rule criteria that evaluates to `true` determines the stage definition assignment.

**•** If no rule criteria matches, the default stageDefinition from the StageAssignment is used.

**•** The assigned stage definition governs the stage behavior for that record.

Use Cases:

**•** Value-based Assignment—Assign different stage definitions based on transaction amounts. For example, premium stages for
high-value applications.

**•** Type-based Assignment—Use different stage workflows for different record types.

**•** Status-based Assignment—Apply specific stage definitions based on record status or classification.

**•** Complex Criteria—Combine multiple conditions to create sophisticated assignment rules.

Declarative Metadata Sample Definition

The following is an example of a StageAssignment component.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <StageAssignment xmlns="http://soap.sforce.com/2006/04/metadata">

      <active>true</active>

      <description>Assigns stage definitions to applications based on amount</description>

      <masterLabel>Application Stage Assignment</masterLabel>

      <referenceObject>ApplicationForm</referenceObject>

      <ruleCriteria>

        <name>High Value Applications</name>

        <priority>1</priority>

        <criteriaType>AND</criteriaType>

        <condition>

           <fieldName>Amount</fieldName>

           <operator>GreaterThan</operator>

           <sequenceNumber>1</sequenceNumber>

           <value>10000</value>

        </condition>

        <condition>

           <fieldName>Status</fieldName>

           <operator>Equals</operator>

           <sequenceNumber>2</sequenceNumber>

           <value>Approved</value>

        </condition>

        <stageDefinition>Premium_Application_Stages</stageDefinition>

      </ruleCriteria>

      <ruleCriteria>

        <name>Standard Applications</name>

        <priority>2</priority>

        <criteriaType>AND</criteriaType>

        <condition>

           <fieldName>Amount</fieldName>

           <operator>LessOrEqual</operator>

           <sequenceNumber>1</sequenceNumber>

           <value>10000</value>

        </condition>

        <stageDefinition>Standard_Application_Stages</stageDefinition>

      </ruleCriteria>

```


### Metadata Types StageDefinition

```
      <stageDefinition>Basic_Application_Stages</stageDefinition>

   </StageAssignment>

```

The following is an example `package.xml` that references the previous definition.

```
   <?xml version="1.0" encoding="UTF-8"?>

   <Package xmlns="http://soap.sforce.com/2006/04/metadata">

      <types>

        <members>*</members>

        <name>StageAssignment</name>

      </types>

      <version>64.0</version>

   </Package>

```

Wildcard Support in the Manifest File

This metadata type supports the wildcard character `*` (asterisk) in the `package.xml` manifest file. For information about using the
[manifest file, see Deploying and Retrieving Metadata with the Zip File.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

### StageDefinition

Represents a collection of fields to set up the states and transitions for Stage Management.

Parent Type

[This type extends the Metadata metadata type and inherits its](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/metadata.htm) `fullName` field.

File Suffix and Directory Location

### StageDefinition components have the suffix .stageDefinition and are stored in the stageDefinitions folder.

Version

### StageDefinition components are available in API version 62.0 and later.

Fields

**Field Name** **Description**

```
active

description

```

**Field Type**
boolean

**Description**

Required. Indicates whether the stage definition is active `(true)` or not `(false)` .

**Field Type**
string


Metadata Types StageDefinition

**Field Name** **Description**

**Description**
The description of the stage definition.

```
masterLabel

referenceObject

referenceObjectField

referenceObjectRecordType

stageTransition

stageValue

```

StageTransition

**Field Type**
string

**Description**

Required. A user-friendly name for stage definition, which is defined when the metadata
component is created.

**Field Type**
string

**Description**

Required. The reference object associated with the stage definition.

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

