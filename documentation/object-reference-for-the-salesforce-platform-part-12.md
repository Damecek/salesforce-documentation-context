Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of dataset.

Possible values are:

**•** `Baseline`

**•** `HoldOut`

**•** `Live`

**•** `Model`

**•** `Training`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects MLModelMetric

**Field** **Details**

**Description**
The date and time when the model training finished.

```
GraphType

MetricType

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of graph.

Possible values are:

**•** `ConfidencePlot`

**•** `ConfusionMatrixPerThreshold`

**•** `DiscountedCumulativeGainsGraph`

**•** `HitRateGraph`

**•** `KBasedRankingGraph`

**•** `LiftPlot`

**•** `MeanReciprocalRankGraph`

**•** `MultiClassConfusionMatrixPerThreshold`

**•** `MultiClassMisclassifications`

**•** `NormalizedDiscountedCumulativeGainsGraph`

**•** `PrecisionGraph`

**•** `RecallGraph`

**•** `RegressionErrorBands`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of metric.

Possible values are:

**•** `Accuracy`

**•** `AveragePrecision`

**•** `BalancedAccuracy`

**•** `DiscountedCumulativeGainAtK`

**•** `ExpectedTopAbsoluteRank`

**•** `ExpectedTopPercentileRank`

**•** `F1Score`

**•** `FMeasure`


Standard Objects MLModelMetric

**Field** **Details**

**•** `HitRateAtK`

**•** `LiftBucket`

**•** `MeanAbsoluteError`

**•** `MeanAbsoluteRank`

**•** `MeanAveragePrecisionAtK`

**•** `MeanPercentileRank`

**•** `MeanReciprocalRank`

**•** `MeanReciprocalRankAtK`

**•** `MeanTopReciprocalRank`

**•** `NormalizedDiscountedCumulativeGainsAtK`

**•** `Precision`

**•** `PrecisionAtK`

**•** `RSquared`

**•** `Recall`

**•** `RecallAtK`

**•** `RootMeanSquaredError`

**•** `auPR`

**•** `auROC`

```
ModelId

Name

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related MLModel.

This field is a polymorphic relationship field.

**Relationship Name**
Model

**Relationship Type**
Lookup

**Refers To**
MLModel

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An automatically generated ID that uniquely identifies the metric.


### Standard Objects MLRecommendationDefinition

**Field** **Details**

```
RowCount

Span

StartTime

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of rows.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The time span for the metric. Possible values are:

**•** `Day`

**•** `Hour`

**•** `Month`

**•** `SinceLastAction`

**•** `Week`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the model training started.

### MLRecommendationDefinition

For internal use only.

### MobileDeviceAppRegistration

Represents the details provided in a mobile device registration event from an app that uses the Engagement Mobile SDK. This object is
available in API version 65.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`update()`, `upsert()`


Standard Objects MobileDeviceAppRegistration

Fields

**Field** **Details**

```
DatetimeInDevice

DeviceModel

DevicePlatform

DeviceSystemToken

DeviceSystemTokenHash

DeviceTimezone

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time of the registration event, based on values provided by the device.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The model of the device that’s being registered, such as `iPhone 17` or `Google Pixel` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The operating system of the mobile device, such as `iPhone OS` or `Android` .

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A unique token that represents the mobile device. The push notification service (such as
Apple Push Notification service or Firebase Cloud Messaging) uses this token to deliver
messages to the device.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A hash of the device token.

**Type**
string


Standard Objects MobileDeviceAppRegistration

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The time zone that the device is located in when the registration event occurs.

```
DeviceVersion

Deviceid

Eventid

IsBackgroundRefreshEnabled

IsBluetoothEnabled

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The version or model number of the device.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A unique identifier for the mobile device.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A unique identifier for the registration event.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the device gives permission for the app to receive updates while it’s in
the background.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether Bluetooth is enabled on the device.


Standard Objects MobileDeviceAppRegistration

**Field** **Details**

The default value is `false` .

```
IsDst

IsLocationEnabled

IsPushEnabled

Locale

MobileAppName

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the device’s locale observes daylight saving time (DST).

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the device has location services enabled for the app.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the device has push notifications enabled for the app.

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The locale string for the device, such as `en_US` or `ja_JP` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the mobile app, as configured in Setup.


Standard Objects MobileDeviceAppRegistration

**Field** **Details**

```
MobileAppVersion

MobileAppid

PartyIdentificationName

PartyIdentificationNumber

PartyIdentificationType

RegistrationDatetime

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The version number of the mobile app that generated the registration event.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A unique ID that represents the mobile app.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the party identifier for identity resolution rules.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID used for identity resolution comparisons.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A string that provides additional information about the type of party identifier used, such as
`Driver License` or `SSN` .

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update


### Standard Objects MobileSecurityAssignment

**Field** **Details**

**Description**
The date and time when the registration event occurred.

```
Registrationid

SdkVersion

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A unique ID for the registration event.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The version of the Mobile Engagement SDK that the app uses.

### MobileSecurityAssignment

Represents the assignment of mobile security policies to a profile. The policies apply to the Salesforce mobile app with Enhanced Mobile
App Security enabled. This object is available in API version 54.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Accessing this object requires the Enhanced Mobile App Security add-on subscriptions and the Enforce Enhanced Mobile App Security
user permission.

Fields

**Field** **Details**

```
DeveloperName

```

**Type**
string


Standard Objects MobileSecurityAssignment

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. The name:

**•** must be 40 characters or fewer

**•** must begin with a letter

**•** can contain only underscores and alphanumeric characters

**•** can’t include spaces

**•** can’t end with an underscore

**•** can’t contain 2 consecutive underscores

In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

```
Language

MasterLabel

NamespacePrefix

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The combined language and locale ISO code, which controls the language of the
MobileSecurityAssignment.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for this MobileSecurityAssignment value. This display value is the internal label that
doesn't get translated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values.


### Standard Objects MobileSecurityPolicy

**Field** **Details**

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

```
ProfileId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The profile ID that the mobile security policies are assigned to.

This field is a relationship field.

**Relationship Name**
Profile

**Refers To**
Profile

### MobileSecurityPolicy

Enables mobile security policies on the Salesforce mobile app with Enhanced Mobile Security. This object is available in API version 50.0
and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Accessing this object requires the Enhanced Mobile App Security add-on subscriptions and the Enforce Enhanced Mobile App Security
user permission.


Standard Objects MobileSecurityPolicy

Fields

**Field** **Details**

```
DeveloperName

EffectiveDate

IsEnabled

Language

MasterLabel

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date a mobile security policy is enforced.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
A value indicating whether a mobile security policy is enabled.

The default value is 'false'.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The two-to five-character code that represents the language and locale ISO.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label of the mobile security policy.


Standard Objects MobileSecurityPolicy

**Field** **Details**

```
MobilePlatform

MobileSecurityAssignmentId

NamespacePrefix

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The mobile operating system.

Possible values are:

**•** `Android`

**•** `iOS`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the ID of the mobile security assignment.

This is a relationship field.

**Relationship Name**
MobileSecurityAssignment

**Relationship Type**
Lookup

**Refers To**
MobileSecurityAssignment

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.


Standard Objects MobileSecurityPolicy

**Field** **Details**

**•** In orgs that aren’t Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

```
RuleValue

RuleValueType

SeverityLevel

Type

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Value of the mobile security policy rule.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of mobile security policy rule.

Possible values are:

**•** `Boolean`

**•** `Text`

**•** `TextList`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The severity level of a mobile security policy.

Possible values are:

**•** `Critical`

**•** `Error`

**•** `Info`

**•** `Warn`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of mobile security policy.


Standard Objects MobileSecurityPolicy

**Field** **Details**

Possible values are:

**•** `AllowedDeviceList` —Allowed Device List

**•** `Block3dTouch` —Block 3D Touch

**•** `BlockCalendar` —Block Calendar

**•** `BlockCamera` —Block Camera

**•** `BlockContacts` —Block Contacts

**•** `BlockCustomKeyboard` —Block Custom Keyboard

**•** `BlockFileBackup` —Block File Backup

**•** `BlockMicrophone` —Block Microphone

**•** `BlockOsSharing` —Block OS Share Actions

**•** `BlockedDeviceList` —Blocked Device List

**•** `BrowserUriScheme` —Mobile Browser URI Scheme

**•** `CheckBiometric` —Check Biometric Login Data

**•** `DevicePasscode` —Require Device Passcode

**•** `DisableUrlCaching` —Disable URL Caching

**•** `JailbrokenDevice` —Block Jailbroken Device

**•** `LogCertPin` —Log Certificate Pinning

**•** `LogEmail` —Log Email

**•** `LogPhonecall` —Log Phone Call

**•** `LogPolicyResult` —Log Security Policy Evaluation Result

**•** `LogScreenshot` —Log Screenshot

**•** `LogTextmessage` —Log SMS

**•** `LogoutAfterRestart` —Log Out User After Device Restart

**•** `LogoutOnBiometricChange` —Log Out User After Changing Biometric Login
Data

**•** `MalwareDetection` —Malware Detection

**•** `ManInMiddle` —Block Man In The Middle Attack

**•** `MaxOffline` —Maximum Days Offline Without Policy Refresh

**•** `MaximumAppVersion` —Maximum Application Version

**•** `MaximumOsVersion` —Maximum OS Version

**•** `MinimumAppVersion` —Minimum Application Version

**•** `MinimumOsVersion` —Minimum OS Version

**•** `MinimumSecurityPatchVersion` —Minimum Security Patch Version

**•** `PhonecallUriScheme` —Phone Call Application Handler

**•** `Screenshot` —Block Screenshot


### Standard Objects MobileSecurityUserMetric MobileSecurityUserMetric

Represents the metrics for users who have Enhanced Mobile Security policies enforced. This object is available in API version 51.0 and
later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Accessing this object requires the Enhanced Mobile App Security add-on subscriptions and the Enforce Enhanced Mobile App Security
user permission.

Fields

**Field** **Details**

```
MetricsDate

UserCount

```

Usage

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
The date the metrics were collected.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of users who have mobile security policies enforced.

A user with the Manage Enhanced Mobile App Security permission can run this SOQL query.

```
SELECT MetricsDate, UserCount

FROM MobileSecurityUserMetric

ORDER BY MetricsDate DESC

### MobileSettingsAssignment

```

Represents the assignment of a particular field service mobile settings configuration to a user profile. This object is available in API version
41.0 and later.


### Standard Objects MobSecurityCertPinConfig

Supported Calls

`create()`, `delete()`, `describeLayout()` —available in API version 51.0 and later, `describeSObjects()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
FieldServiceMobileSettingsId

ProfileId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of a set of field service mobile settings.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the profile to associate with the set of field service mobile settings.

### MobSecurityCertPinConfig

Configuration of mobile security certificate pinning on the Salesforce mobile app with Enhanced Mobile Security. This object is available
in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Accessing this object requires the Enhanced Mobile App Security add-on subscriptions and the Enforce Enhanced Mobile App Security
user permission.


Standard Objects MobSecurityCertPinConfig

Fields

**Field** **Details**

```
CertificateHash

DeveloperName

DomainName

IsEnabled

IsSubdomainIncluded

Language

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique identifier for the certificate.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the domain.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The default value is False.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The default value is False.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects MobSecurityCertPinConfig

**Field** **Details**

**Description**
The two-to five-character code that represents the language and locale ISO.

```
MasterLabel

MobilePlatform

MobileSecurityAssignmentId

NamespacePrefix

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The master label of the mobile security pin.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The mobile operating system.

Possible values are:

**•** `Android`

**•** `iOS`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the ID of the mobile security assignment.

This is a relationship field.

**Relationship Name**
MobileSecurityAssignment

**Relationship Type**
Lookup

**Refers To**
MobileSecurityAssignment

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can


### Standard Objects MobSecurityCertPinEvent

**Field** **Details**

refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that aren’t Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

```
SeverityLevel

Type

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The severity level of a mobile security policy.

Possible values are:

**•** `Critical`

**•** `Error`

**•** `Info`

**•** `Warn`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of pin

Possible values are:

**•** `AuthServer` —Authentication Server

**•** `Resource` —Resource

### MobSecurityCertPinEvent

The event of mobile security certificate pinning on the Salesforce mobile app with Enhanced Mobile Security. This object is available in
API version 53.0 and later.


Standard Objects MobSecurityCertPinEvent

Supported Calls

`create()`, `describeSObjects()`

Special Access Rules

Accessing this object requires the Enhanced Mobile App Security add-on subscriptions and the Enforce Enhanced Mobile App Security
user permission.

Fields

**Field** **Details**

```
AppPackageIdentifier

AppVersion

CertPinResults

DeviceIdentifier

DeviceModel

```

**Type**
string

**Properties**
Create

**Description**
The unique identifier for the certificate.

**Type**
string

**Properties**
Create

**Description**
The version of the app.

**Type**
json

**Properties**
Create

**Description**
The results of certificate pinning.

**Type**
string

**Properties**
Create

**Description**
The hardware IDs or IDs to uniquely identify a mobile device.

**Type**
string


Standard Objects MobSecurityCertPinEvent

**Field** **Details**

**Properties**
Create

**Description**
The model of the mobile device.

```
EventDate

EventDescription

EventIdentifier

EventUuid

OsName

OsVersion

```

**Type**
dateTime

**Properties**
Create, Nillable

**Description**
The date of the certificate pinning event.

**Type**
string

**Properties**
Create, Nillable

**Description**
The description of the certificate pinning event.

**Type**
string

**Properties**
Create, Nillable

**Description**
The ID of the certificate pinning event.

**Type**
string

**Properties**
Nillable

**Description**
The universally unique identifier of the event.

**Type**
string

**Properties**
Create

**Description**
The name of the operating system.

**Type**
string


### Standard Objects MsgChannelLanguageKeyword

**Field** **Details**

**Properties**
Create

**Description**
The version of the operating system.

```
ReplayId

UserId

WebkitVersion

```

**Type**
string

**Properties**
Nillable

**Description**
The position of the event in the event stream.

**Type**
reference

**Properties**
Create

**Description**
This is polymorphic relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

**Type**
string

**Properties**
Create, Nillable

**Description**
The version of the web browser engine developed by Apple.

### MsgChannelLanguageKeyword

Represents the consent configuration for a Messaging channel. This object is available in API version 48.0 and later.

Supported Calls

`describeSObjects()`, `delete()`, `query()`, `retrieve()`, `search()`


Standard Objects MsgChannelLanguageKeyword

Fields

**Field** **Details**

```
CustomKeywords

CustomResponse

DoubleOptInKeywords

HelpKeywords

HelpResponse

MasterLanguage

```

**Type**
textarea

**Properties**
Nillable

**Description**
The keywords a Messaging end user can send to receive the Custom Response.

**Type**
textarea

**Properties**
Nillable

**Description**
The automated response sent when a Messaging end user sends a Custom Keyword.

**Type**
textarea

**Properties**
Nillable

**Description**
The keywords a Messaging end user can send to doubly opt in to receiving messages.

**Type**
textarea

**Properties**
Nillable

**Description**
The keywords a Messaging end user can send to request help during a Messaging session.

**Type**
textarea

**Properties**
Nillable

**Description**
The automated response sent when a Messaging end user requests help.

**Type**
textarea


Standard Objects MsgChannelLanguageKeyword

**Field** **Details**

**Properties**

**Description**
The language used for this consent configuration.

```
MessagingChannelId

MessagingChannelUsageId

OptInConfirmation

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the associated Messaging channel.

This is a relationship field.

**Relationship Name**
MessagingChannel

**Relationship Type**
Lookup

**Refers To**
MessagingChannel

**Type**
reference

**Properties**
Filter, Group, Sort

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

**Type**
textarea

**Properties**
Nillable

**Description**
The automated response sent when a Messaging end user opts in to receiving messages.


### Standard Objects MsgChannelUsageExternalOrg

**Field** **Details**

```
OptInKeywords

OptOutConfirmation

OptOutKeywords

```

**Type**
textarea

**Properties**
Nillable

**Description**
The keywords a Messaging end user can send to explicitly opt in to receiving messages.

**Type**
textarea

**Properties**
Nillable

**Description**
The automated response sent when a Messaging end user opts out of receiving messages.

**Type**
textarea

**Properties**
Nillable

**Description**
The keywords a Messaging end user can send to opt out of receiving messages.

### MsgChannelUsageExternalOrg

Represents the Enterprise ID (EID) and Business Unit (MID) for Marketing Cloud connections in a Unified Messaging channel. This object
is available in API version 60.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ExternalOrgIdentifier

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The Enterprise ID (EID) of a Marketing Cloud connection.


### Standard Objects MyDomainDiscoverableLogin

**Field** **Details**

```
ExternalSubOrgIdentifier

MessagingChannelUsageId

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Business Unit (MID) of a Marketing Cloud connection.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The associated MessagingChannelUsage record, which must have a DeploymentType of `MJ`
(referring to Marketing Cloud Journey Builder).

This field is a relationship field.

**Relationship Name**
MessagingChannelUsage

**Relationship Type**
Lookup

**Refers To**
MessagingChannelUsage

MsgChannelUsageExternalOrg records apply only to MessagingChannelUsage records related to Marketing Cloud.

Only one MsgChannelUsageExternalOrg record can exist for each MessagingChannelUsage record with a DeploymentType of `MJ` .
MsgChannelUsageExternalOrg records are created when an admin enters the EID and MID for a Marketing Cloud application in Unified
Messaging Setup and then clicks **Connect** .

The data saved in a MsgChannelUsageExternalOrg record is used for making a connection to Marketing Cloud. If an admin disconnects
a Marketing Cloud application in Unified Messaging Setup, the saved EID and MID are used during deprovisioning.

### MyDomainDiscoverableLogin

Represents configuration settings when the My Domain login page type is Discovery. Login Discovery provides an identity-first login
experience, where the login page contains the identifier field only. Based on the identifier entered, a handler determines how to
authenticate the user. This object is available in API version 45.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects MyDomainDiscoverableLogin

Fields

**Field Name** **Details**

```
ApexHandlerId

DeveloperName

ExecuteApexHandlerAsId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The ID of the Apex handler that contains the Discovery authentication logic.

This is a relationship field.

**Relationship Name**
ApexHandler

**Relationship Type**
Lookup

**Refers To**
ApexClass

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming
conflicts on package installations. With this field, a developer can change the
object's name in a managed package and the changes are reflected in a
subscriber's organization.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The ID of the user who is executing the handler. Requires Manage User permission.

This is a relationship field.

**Relationship Name**
ExecuteApexHandlerAs


Standard Objects MyDomainDiscoverableLogin

**Field Name** **Details**

**Relationship Type**
Lookup

**Refers To**
User

```
Language

MasterLabel

UsernameLabel

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the `MasterLabel` .

Possible values are:

**•** `da` (Danish)

**•** `de` (German)

**•** `en_US` (English)

**•** `es` (Spanish)

**•** `es_MX` (Spanish - Mexican)

**•** `fi` (Finnish)

**•** `fr` (French)

**•** `it` (Italian)

**•** `ja` (Japanese)

**•** `ko` (Korean)

**•** `nl_NL` (Dutch)

**•** `no` (Norwegian)

**•** `pt_BR` (Portuguese - Brazilian)

**•** `ru` (Russian)

**•** `sv` (Swedish)

**•** `th` (Thai)

**•** `zh_CN` (Chinese - Simplified)

**•** `zh_TW` (Chinese - Traditional)

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the action link group template.

**Type**
string


### Standard Objects MutingPermissionSet

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Login prompt on login page when the My Domain login page type is Discovery.
It supports localization with custom labels.

Usage

Use this object to access the My Domain Login Discovery Page, which is a login page type that prompts users to identity themselves
with an email address, phone number, or custom identifier. My Domain Login Discovery performs an interview-based login process,
where users are first prompted to provide identity and then authenticated. For example, users receive a verification code that they enter
to complete the login process.

### MutingPermissionSet

Represents a set of disabled permissions and is used in conjunction with PermissionSetGroup. This object is available in API version 46.0
and later.

Use a muting permission set with a permission set group to mute certain permissions. For instance, you have a subscriber org using a
managed package that contains a permission set group. To use the existing permission set group, the subscriber org can disable specific
permissions with a muting permission set. Or, perhaps you have a permission set group that contains several permission sets managed
by different departments. Use a muting permission set to disable specific permissions based on your organization's needs.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Summer ’20 and later, only users who have one of these permissions can access this object:

**•** View Setup and Configuration

**•** Manage Session Permission Set Activations

**•** Assign Permission Sets

Fields

**Field Name** **Details**

```
DeveloperName

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects MutingPermissionSet

**Field Name** **Details**

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique DeveloperName for
each record. If no DeveloperName is specified, performance can slow while Salesforce
generates one for each record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

```
Language

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the muting permission set.

Possible values are:

**•** `da` (Danish)

**•** `de` (German)

**•** `en_US` (English)

**•** `es` (Spanish)

**•** `es_MX` (Spanish - Mexican)

**•** `fi` (Finnish)

**•** `fr` (French)

**•** `it` (Italian)

**•** `ja` (Japanese)

**•** `ko` (Korean)

**•** `nl_NL` (Dutch)

**•** `no` (Norwegian)

**•** `pt_BR` (Portuguese - Brazilian)

**•** `ru` (Russian)

**•** `sv` (Swedish)

**•** `th` (Thai)

**•** `zh_CN` (Chinese - Simplified)

**•** `zh_TW` (Chinese - Traditional)


### Standard Objects Name

**Field Name** **Details**

```
MasterLabel

Permissions PermissionName

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The muting permission set label for the aggregated, disabled permissions.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
One field for each permission. If `true`, the permission is disabled in the related permission
set group. The number of fields varies depending on the permissions for the organization
and license type.

To get a list of available permissions, use `describeSObjects()` .

Use MutingPermissionSet to disable specified permissions within a permission set group.

### Name

Non-queryable object that provides information about foreign key traversals when the foreign key has more than one parent.

This object is used to retrieve information from related records where the related record can be from more than one object type (a
polymorphic foreign key). For example, the owner of a case can be either a user or a group (queue). This object allows retrieval of the
owner name, whether the owner is a user or a group (queue). You can use a describe call to access the information about parents for
an object, or you can use the `who`, `what`, or `owner` fields (depending on the object) in SOQL queries. This object can’t be directly
accessed.

Supported Calls

```
describeSObjects()

```

Fields

**Field** **Details**

```
Alias

```

**Type**
string


Standard Objects Name

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user alias. This field contains a value only if the related record is a user.

```
Email

FirstName

IsActive

LastName

LastReferencedDate

```

**Type**
email

**Properties**
Filter, Group, Nillable, Sort

**Description**
The email address of the user or group (queue).

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The first name of the user, contact, or lead.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the related record is an active user ( `true` ) or not ( `false` ). This field
contains a value only if the related record is a user.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The last name of the user, contact, or lead.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last interacted with this record, directly or indirectly.


Standard Objects Name

**Field** **Details**

```
LastViewedDate

MiddleName

Name

Phone

Profile

ProfileId

```

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it's possible that the user only accessed this record or list view ( `LastReferencedDate` ),
but not viewed it.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The middle name of the user contact, or lead.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the parent of the object queried. If the parent is a user, contact, or lead, the
value is a concatenation of the `FirstName`, `MiddleName`, `LastName`, and `Suffix`
fields of the related record.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
The phone number of the user. This field contains a value only if the related record is a user.

**Type**
reference

**Properties**
Filter, Nillable

**Description**
The Profile of the user. Only populated if the related record is a user.

**Type**
reference


Standard Objects Name

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the user’s Profile. Only populated if the related record is a user.

This field is a relationship field.

**Relationship Name**
Profile

**Relationship Type**
Lookup

**Refers To**
Profile

```
Suffix

Title

Type

Username

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name suffix of the user, contact, or lead.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The title of the user, for example CFO or CEO.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
A list of the types of sObject that can be an owner of this object. You can use this field to
filter on a type of owner, for example, return only the leads owned by a user.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects NamedCredential

**Field** **Details**

**Description**
Contains the name that a user enters to log into the API or the user interface. The value for
this field is in the form of an email address, and is only populated if the related record is a
user.

```
UserRole

 UserRoleId

```

Usage

**Type**
picklist

**Properties**
Filter, Nillable

**Description**
Name of the `Role` played by the user. Only populated for user rows.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user role associated with this object.

This field is a relationship field.

**Relationship Name**
UserRole

**Relationship Type**
Lookup

**Refers To**
UserRole

To query on relationships where the parent can be more than one type of object, use `who`, `what`, or `owner` relationship fields.

SEE ALSO:

Overview of Salesforce Objects and Fields

### NamedCredential

Represents a named credential, which specifies the URL of a callout endpoint and its required authentication parameters in one definition.
A named credential can be specified as an endpoint to simplify the setup of authenticated callouts. This object is available in API version
33.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.


Standard Objects NamedCredential

Note: All credentials stored within this entity are encrypted under a framework that is consistent with other encryption frameworks
on the platform. Salesforce encrypts your credentials by auto-creating org-specific keys. Credentials encrypted using the previous
encryption scheme have been migrated to the new framework.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

As of Spring ’20 and later, only users with the View Setup and Configuration permission can access this object.

Fields

**Field Name** **Details**

```
AuthProviderId

AuthTokenEndpointUrl

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

Salesforce ID of the authentication provider, which defines the
service that provides the login process and approves access
to the external system.

Only users with the “Customize Application” and “Manage
AuthProviders” permissions can view this field.

This field is a relationship field.

This field is only valid for legacy named credentials.

This field was first available in API version 39.0, this field is
deprecated in API version 56.0.

**Relationship Name**
AuthProvider

**Relationship Type**
Lookup

**Refers To**
AuthProvider

**Type**
textarea

**Properties**
Nillable


Standard Objects NamedCredential

**Field Name** **Details**

**Description**
The URL where SON Web Tokens (JWTs) are exchanged for
access tokens.

This field is only valid for legacy named credentials.

This field was first available in API version 46.0, this field is
deprecated in API version 56.0.

```
CalloutOptionsAllowMergeFieldsInBody

CalloutOptionsAllowMergeFieldsInHeader

CalloutOptionsGenerateAuthorizationHeader

DeveloperName

```

**Type**
boolean

**Properties**
Filter

**Description**
For Apex callouts, indicates whether the code can use merge
fields to populate HTTP request bodies with org data.

This field is available in API version 35.0 and later.

**Type**
boolean

**Properties**
Filter

**Description**
For Apex callouts, indicates whether the code can use merge
fields to populate HTTP headers with org data.

This field is available in API version 35.0 and later.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether Salesforce automatically generates a
standard authorization header for each callout to the named
credential–defined endpoint.

This field is available in API version 35.0 and later.

**Type**
string

**Properties**
Filter, Group, Sort


Standard Objects NamedCredential

**Field Name** **Details**

**Description**
The unique name of the object in the API. This name can
contain only underscores and alphanumeric characters, and
must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain
two consecutive underscores. In managed packages, this field
prevents naming conflicts on package installations. With this
field, a developer can change the object’s name in a managed
package and the changes are reflected in a subscriber’s
organization.

Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this
field.

```
Endpoint

JwtAudience

JwtFormulaSubject

```

**Type**
textarea

**Properties**
Nillable

**Description**
The root URL of the endpoint.

This field is only valid for legacy named credentials.

This field is deprecated in API version 56.0.

**Type**
textarea

**Properties**
Nillable

**Description**
External service or other allowed recipients for the JSON Web
Token. Written as JSON, with a quoted string for a single
audience and an array of quoted strings for multiple audiences.
Single audience example: `“aud1”` . Multiple audiences
example: `[”aud1”, “aud2”, “aud3”]` .

This field is only valid for legacy named credentials.

This field was first available in API version 46.0, this field is
deprecated in API version 56.0.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects NamedCredential

**Field Name** **Details**

**Description**
Formula string calculating the JSON Web Token’s subject. API
names and constant strings, in single quotes, can be included.
Allows a dynamic Subject unique per user requesting the token.
For example, `'User='+$User.Id` . Use this field when
`PrincipalType` is set to `PerUser` . Corresponds to Per
User Subject in the user interface.

This field is only valid for legacy named credentials.

This field was first available in API version 46.0, this field is
deprecated in API version 56.0.

```
JwtIssuer

JwtTextSubject

JwtValidityPeriodSeconds

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Specify who issued the JSON Web Token using a case-sensitive
string.

This field is only valid for legacy named credentials.

This field was first available in API version 46.0, this field is
deprecated in API version 56.0.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Static text, without quotes, that specifies the JSON Web Token
subject. Use this field when `PrincipalType` is set to
`NamedUser` . Corresponds to Named Principal Subject in the
user interface.

This field is only valid for legacy named credentials.

This field was first available in API version 46.0, this field is
deprecated in API version 56.0.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of seconds that the JSON Web Token is valid.

This field is only valid for legacy named credentials.


Standard Objects NamedCredential

**Field Name** **Details**

This field was first available in API version 46.0, this field is
deprecated in API version 56.0.

```
Language

MasterLabel

NamespacePrefix

PrincipalType

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the `MasterLabel` .

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label for the named credential. This display value is the
internal label that doesn’t get translated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each
Developer Edition org that creates a managed package has a
unique namespace prefix. Limit: 15 characters. You can refer
to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Tracks users who are accessing the external system.
`Anonymous` implies that a user identity isn’t specified for
external system access. `Named Principal` uses one user
identity for all users to access the external system.

This field is only valid for legacy named credentials.

This field is deprecated in API version 56.0.


### Standard Objects NamedCredentialEventLog

Usage

Use the NamedCredential object to query named credentials in your organization.

Note: Some named credential fields rely on per-user authentication to connect with an external system. If an admin edits one of
these fields, then the previously authenticated credentials can get invalidated, requiring individual users to reauthenticate.

SEE ALSO:

ExternalDataUserAuth

ExternalDataSource

_Salesforce Help_ [: Named Credentials](https://help.salesforce.com/s/articleView?id=xcloud.named_credentials_about.htm&type=5&language=en_US)

_Named Credentials Developer Guide_ [: Get Started with Named Credentials](https://developer.salesforce.com/docs/platform/named-credentials/guide/get-started.html)

_[Named Credentials Developer Guide](https://developer.salesforce.com/docs/platform/named-credentials/references/named-credentials-reference/nc-api-links.html)_ : Named Credential API Links

_Apex Developer Guide_ [: Invoking Callouts Using Apex](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_callouts.htm)

_Apex Developer Guide_ [: Named Credentials as Callout Endpoints](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_callouts_named_credentials.htm)

### NamedCredentialEventLog

The Named Credential event type captures information about Apex callouts that use named credentials as their endpoints. Use this
event type to audit the installed managed packages that use named credentials. If you don’t recognize the package namespace in the
named credential event log file, then you can investigate whether a security breach has occurred. This object is available in API version
65.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
BotIdentifier

BotSessionIdentifier

```

**Type**
String

**Description**
The ID of the bot.

**Type**
String

**Description**
The bot session ID.


Standard Objects NamedCredentialEventLog

**Field** **Details**

```
CallerPackageNamespace

ClientIp

CpuTime

LoginKey

NamedCredentialName

PlannerIdentifier

```

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
If an Apex callout using a Named Credential endpoint is initiated from a package, then this
field contains the package’s namespace. If the callout isn’t initiated from a package, then
this field is empty.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address of the client that is using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”.

**Type**
Double

**Properties**
Filter, Nillable, Sort

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the named credential that’s the endpoint of the Apex callout.

**Type**
String


Standard Objects NamedCredentialEventLog

**Field** **Details**

**Description**
The ID of the agent planner.

```
RequestIdentifier

RunTime

SessionKey

Timestamp

Uri

UserIdentifier

```

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same REQUEST_ID.

**Type**
Double

**Properties**
Filter, Nillable, Sort

**Description**
The amount of time that the request took in milliseconds..

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started.

**Type**
DateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the page that’s receiving the request.

**Type**
String


### Standard Objects NamespaceRegistry

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who is using Salesforce services through the UI or the API.

### NamespaceRegistry

Represents a namespace that you can link to scratch orgs that were created from your org’s Dev Hub. You use the namespace when
developing, packaging, and releasing an app. You can’t create this object with the API. Use the **Link Namespace** action in the Dev Hub
### graphical interface to insert a NamespaceRegistry record. This object is available in API version 41.0 and later.

Supported Calls

`delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,

```
   update()

```

Fields

**Field Name** **Details**

### `Name`

```
NamespaceOrg

NamespacePrefix

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
The name of this namespace registry entry.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The org ID of the Developer Edition org where you've registered the namespace
you want to link.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The namespace prefix that you want to link to the scratch org.


### Standard Objects NavigationLinkSet

Associated Objects

This object has these associated objects. Unless noted, they’re available in the same API version as this object.

**NamespaceRegistryFeed**

Feed tracking is available for the object.

**NamespaceRegistryHistory**

History is available for tracked fields of the object.

SEE ALSO:

ActiveScratchOrg

ScratchOrgInfo

### NavigationLinkSet

Represents the navigation menu in an Experience Cloud site. A navigation menu consists of items that users can click to go to other
parts of the site. This object is available in API version 35.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

`create()`, `delete()`, `update()`, and `upsert()` are available in API version 45.0 and later.

Special Access Rules

Navigation menus are available only in Experience Cloud sites created using Experience Builder templates. To use navigation menus in
LWR templates, you must build a custom navigation menu component.

Fields

**Field Name** **Details**

```
DeveloperName

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

Create and Update are available in API version 45.0 and later.

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming
conflicts on package installations. With this field, a developer can change the
object’s name in a managed package and the changes are reflected in a
subscriber’s organization.


Standard Objects NavigationLinkSet

**Field Name** **Details**

```
Language

MasterLabel

NetworkId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

Create, Defaulted on create, Nillable, and Update are available in API version 45.0
and later.

**Description**
Language for the navigation menu. Valid values are:

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

**•** Thai: `th` The Salesforce user interface is fully translated to Thai, but Help is
in English.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

Create and Update are available in API version 45.0 and later.

**Description**

Label for the navigation menu.

**Type**
reference


### Standard Objects NavigationMenuItem

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort

Create is available in API version 45.0 and later. Update is available in API versions
45.0 to 47.0.

**Description**
ID of the Experience Cloud site.

### NavigationMenuItem

Represents a single menu item in a NavigationLinkSet. Use this object to create, delete, or update menu items in your Experience Cloud
site’s navigation menu. This object is available in API version 35.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Navigation menus are available only in Experience Cloud sites created using Experience Builder templates. To use navigation menus in
LWR templates, you must build a custom navigation menu component.

Fields

**Field Name** **Details**

```
AccessRestriction

DefaultListViewId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Determines if the menu item is available to guest users who aren’t required to
log in to the Experience Cloud site.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If the value of the `Type` field is SalesforceObject, the value is the ID of the default
list view for the object.


Standard Objects NavigationMenuItem

**Field Name** **Details**

```
DraftRowID

Label

NavigationLinkSetId

ParentId

Position

Status

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the draft navigation menu item. The ID is unique within your
organization.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The text that appears in the navigation menu for this item.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The navigation menu that this item is included in.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The parent navigation menu.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The location of the menu item in the navigation menu.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort


Standard Objects NavigationMenuItem

**Field Name** **Details**

**Description**
Represents if the navigation menu item is published or not. The values can only
be DRAFT, LIVE, or null. In API versions 42 and earlier, if the Status field is not set,
the field defaults to LIVE. When queried and Status is not part of the query filter,
only the NavigationMenuItem objects with a status of LIVE return. In API versions
43 and later, if the Status field is not set, the field defaults to DRAFT. When queried
and Status is not part of the query filter, all NavigationMenuItem objects return
regardless of status.

```
Target

TargetPrefs

Type

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
If `Type` is ExternalLink or InternalLink, the target is the URL that the link points
to. For ExternalLink, your entry looks like this: _`https://salesforce.com`_ .
For InternalLink, use a relative URL, such as _`/contactsupport`_ .

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
If `Type` is ExternalLink, determines whether a navigation menu item opens in
the same tab.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of navigation menu item. The available values are:

**•** SalesforceObject—Available objects include accounts, cases, contacts, and
custom objects.

**•** ExternalLink—Links to a URL outside of your Experience Cloud site. For
example, _`https://salesforce.com`_ .

**•** Event—An event, such as logging in, logging out, or switching accounts.
Event is internal only and can’t be used in custom components.

**•** GlobalAction—Enables users to create object records, but the new record
has no relationship with other records.

**•** InternalLink—Links to a relative URL inside your Experience Cloud site. For
example, _`/contactsupport`_ .


### Standard Objects NavigationMenuItemLocalization

**Field Name** **Details**

**•** NavigationalTopic—A dropdown list with links to the navigational topics in
your Experience Cloud site.

**•** SystemLink—A system link, such as a link to Experience Builder, Workspaces,
or Salesforce setup.

Usage

You can add up to 20 navigation menu items. You can translate navigation menu items using the Translation Workbench.

### NavigationMenuItemLocalization

Represents the translated value of a navigation menu item in an Experience Cloud site. This object is available in API version 36.0 and
later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

Navigation menus are available only in Experience Cloud sites created using Experience Builder templates. To use navigation menus in
LWR templates, you must build a custom navigation menu component.

Fields

**Field Name** **Details**

```
Language

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**

The language of the translated navigation menu item. The picklist contains the
following supported languages:

**•** Chinese (Simplified): `zh_CN`

**•** Chinese (Traditional): `zh_TW`

**•** Danish: `da`

**•** Dutch: `nl_NL`

**•** English: `en_US`

**•** Finnish: `fi`


Standard Objects NavigationMenuItemLocalization

**Field Name** **Details**

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

**•** Thai: `th` The Salesforce user interface is fully translated to Thai, but Help is
in English.

```
NamespacePrefix

ParentId

```

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
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the navigation menu item that this translated value applies to.


### Standard Objects Network

**Field Name** **Details**

```
Value

### Network

```

**Type**
string

**Properties**
Create, Filter, Sort, Update

**Description**
The translated text for the navigation menu item. Label is **Translation Text** .

Represents an Experience Cloud site. Salesforce Experience Cloud lets you create branded spaces for your employees, customers, and
partners. You can customize and create experiences, whether they’re communities, sites, or portals, to meet your business needs, then
transition seamlessly between them. Experience Cloud sites let you share information, records, and files with coworkers and stakeholders
all in one place. This object is available in API version 26.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`, `update()`

Special Access Rules

This object is available only when your org has digital experiences enabled.

Fields

**Field Name** **Details**

```
AllowedExtensions

CaseCommentEmailTemplateId

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort, Update

**Description**
Specifies the types of files allowed in your site. This list of file types lets you control
what members upload and also prevents spammers from polluting your site with
inappropriate files. Available in API version 36.0 and later.

Separate file types with a comma (for example: _`jpg,docx,txt`_ ). You can
enter lowercase and uppercase letters. You can enter up to 1,000 characters. To
allow all file types, leave this field empty.

**Type**
reference


Standard Objects Network

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
ID of the email template used when submitting a comment on a case. This field
is available in API version 28.0 and later.

```
ChangePasswordEmailTemplateId

ChgEmailVerNewEmailTemplateId

ChgEmailVerOldEmailTemplateId

Description

DeviceActEmailTemplateId

```

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
ID of the email template used when notifying users that their password has been
reset.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
ID of the email template used when notifying users that their email address has
been changed. This email is sent to the user’s new email address.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
ID of the email template used when notifying users that their email address has
been changed. This email is sent to the user’s old email address.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Description of the site.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update


Standard Objects Network

**Field Name** **Details**

**Description**
ID of the email template used when users log in from an unrecognized browser,
app, or IP address. The email contains a one-time password that users enter to
verify their identity.

This field is available in API version 53.0 and later.

```
EmailFooterLogoId

EmailFooterText

EmailSenderAddress

EmailSenderName

enableImageOptimizationCDN

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
ID of the Document object that displays as an image in the footer of Chatter
emails.

**Type**
string

**Properties**
Filter, Nillable, Sort, Update

**Description**
Text that displays in the footer of Chatter emails.

**Type**
email

**Properties**
Filter, Group, Sort

**Description**
Read only. Email address from which emails are sent.

Note: To change the `EmailSenderAddress` value, you must first
specify `NewSenderAddress`, which triggers the sending of an address
change verification email. After you complete the address verification
process, `EmailSenderAddress` changes to the specified
`NewSenderAddress` .

**Type**
string

**Properties**
Filter, Group, Sort, Update

**Description**
Name from which emails are sent.

**Type**
boolean


Standard Objects Network

**Field Name** **Details**

**Properties**
Filter, Update

**Description**
The setting that optimizes cached images for guest users on all devices when a
site uses Salesforce’s CDN for Digital Experiences.

This field is available in API version 56.0 and later.

```
FirstActivationDate

ForgotPasswordEmailTemplateId

HeadlessForgotPasswordTemplateId

HeadlessRegistrationTemplateId

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date the site was first activated.

This field is available in API version 34.0 and later. If the site was activated or
inactive before the release of API version 34.0, this field returns the date that the
site was first created.

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
ID of the email template used when users forget their password.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
ID of the email template to use with the Headless Forgot Password Flow.

This field is available in API version 57.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
ID of the email template to use for identity verification during the Headless
Registration Flow.

This field is available in API version 59.0 and later.


Standard Objects Network

**Field Name** **Details**

```
LockoutEmailTemplateId

MaxFileSizeKb

Name

NewSenderAddress

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
ID of the email template used when users try to reset their password after locking
themselves out because of too many login attempts.

This field is available in API version 43.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Specifies the maximum file size (in KBs) that members can upload in your site.
Available in API version 36.0 and later.

Enter a number between 3072 KB and your org’s maximum file size. To use the
default limit of 2 GB, leave this field empty.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort, Update

**Description**
The name of the site.

**Type**
email

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Email address that has been entered as the new value for
`EmailSenderAddress` but hasn’t been verified yet. After a user has
requested to change the sender email address and has successfully responded
to the verification email, the `NewSenderAddress` value overwrites the value
in `EmailSenderAddress` . This value becomes the email address from which
emails are sent.

Note:

**•** If verification is pending for a new email address and you set
`NewSenderAddress` to null, the verification request is canceled.


Standard Objects Network

**Field Name** **Details**

**•** `NewSenderAddress` is automatically set to null after
`EmailSenderAddress` has been set to the new verified address.

**•** If verification is pending for a new email address, and you specify a
different new address for this field, only the latest value is retained
and used for verification.

```
OptionsActionOverrideEnabled

OptionsAllowInternalUserLogin

OptionsAllowMembersToFlag

OptionsApexCDNCachingEnabled

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
Override the action that occurs when users click a default button, like New or
Edit, with a Lightning component. For example, show a custom window instead
of the one that Salesforce provides. Assign action overrides in the Object Manager.
In the UI, this setting is available in the Administration Workspace, under
**Administration**  - **Preferences** under Experience Management

This field is available in API version 49.0 and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
Specifies whether internal users can log in with their internal credentials on the
site login page.

This field is available in API version 37.0 and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
Determines whether users can flag posts, comments, or files as inappropriate.

This field is available in API version 29.0 and later. The ability to flag files is available
in version 30.0 and later.

**Type**
boolean

**Properties**
Filter, Update


Standard Objects Network

**Field Name** **Details**

**Description**
Determines whether public data from @wire calls to Apex methods is cached
only for guest users. This setting applies only to sites using Salesforce's CDN for
Digital Experiences.

This field is available in API version 55.0 and later.

```
OptionsDirectMessagesEnabled

OptionsEmbeddedLoginEnabled

OptionsEnableTalkingAboutStats

OptionsEnableTopicAssignmentRules

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
Controls the availability of direct messages in an Experience Builder site.

This field is available in API version 39.0 and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
Determines whether the Embedded Login feature is enabled in a site. When
`true`, Embedded Login is turned on.

This field is available in API version 61.0 and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
Determines whether site users see how many people are discussing a topic. The
number of people discussing the topic appears as the user types the topic and
the system gives topic suggestions.

This field is available in API version 41.0 and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When true, displays knowledgeable people in key areas, for example, on Topic
Detail pages.


Standard Objects Network

**Field Name** **Details**

```
OptionsExpFriendlyUrlsAsDefault

OptionsExperienceBundleBasedSnaOverrideEnabled

OptionsGatherCustomerSentimentData

OptionsGuestChatterEnabled

OptionsGuestFileAccessEnabled

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
When true, URL slugs are on by default for

**•** Product and Category pages of LWR Commerce stores (available in API version
58.0 and later)

**•** Custom object pages on enhanced LWR sites (available in API version 60.0
and later)

**•** Account and contact pages on enhanced LWR sites (available in API version
61.0 and later)

**Type**
boolean

**Properties**
Filter, Update

**Description**
When true, the Service Not Available Page is an auto-generated Experience
Builder-based page. When false, the Service Not Available page uses a static
resource page that is set in **Workspaces**   - **Administration**   - **Pages** . The default
value is true. Available in API version 52.0 and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When true, collects data about user likes, upvotes, and downvotes.

**Type**
boolean

**Properties**
Filter, Update

**Description**
Specifies whether guest users can access public Chatter groups in the site without
logging in.

**Type**
boolean

**Properties**
Filter, Update


Standard Objects Network

**Field Name** **Details**

**Description**
When true, lets guest users view asset files and CMS content that’s available to
the site. Guest users can access shared asset files and published CMS content
that’s made for external use, even if it isn’t used. Shared asset files include images
that are associated with topics, recognition badges, branding, and account
branding. This preference is automatically enabled if public access is enabled at
the page or site level in Experience Builder.

```
OptionsGuestMemberVisibility

OptionsHeadlessFrgtPswEnabled

OptionsImageOptimizationCDNEnabled

OptionsInvitationsEnabled

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
When true, lets guest users see who else is part of the site, including non-guest
users. In the UI, this setting appears in the Administration Workspace under
**Administration**  - **Preferences** .

Available in API version 47.0 and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `true`, Headless Forgot Password Flow is enabled.

This field is available in API version 57.0 and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `true`, cached images are optimized to suit any device that guest users
use to access your site. This feature is available only for sites that use Salesforce’s
CDN for Digital Experiences. In the UI, this setting appears in the Administration
Workspace under **Administration**   - **Preferences** .

Available in API version 56.0 and later.

**Type**
boolean

**Properties**
Filter, Update


Standard Objects Network

**Field Name** **Details**

**Description**
Determines whether users can invite others to the site.

```
OptionsKnowledgeableEnabled

OptionsLWRExperienceConnectedAppEnabled

OptionsMemberVisibility

OptionsMobileImageOptimizationEnabled

OptionsNetworkSentimentAnalysis

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
Determines whether users can see knowledgeable people for topics and endorse
people for topics.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When true, enhances the performance and scalability of Connect API calls made
from Lightning web components in an enhanced LWR site. This field is available
in API version 58.0 and later.

Note: This feature is a Beta Service. Customer may opt to try such Beta
Service in its sole discretion. Any use of the Beta Service is subject to the
[applicable Beta Services Terms provided at Agreements and Terms.](https://www.salesforce.com/company/legal/agreements/)

**Type**
boolean

**Properties**
Filter, Update

**Description**
Controls user visibility on a per-site basis. If true, the See other members of this
site preference is enabled for the selected site. This field is available in API version
45.0 and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
If true, file asset images are optimized for mobile display. This field is available in
API version 45.0 and later.

**Type**
boolean


Standard Objects Network

**Field Name** **Details**

**Properties**
Filter, Update

**Description**
If true, enables sentiment analysis in a site. In the UI, this setting is available in
the Administration Workspace, under **Administration**                              - **Preferences** . This field
is available in API version 40.0 and later.

```
OptionsNicknameDisplayEnabled

OptionsPrivateMessagesEnabled

OptionsProfileBasedLayoutsForKnowledgeSearchEnabled

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
Determines whether user nicknames display instead of their first and last names
in most places in the site.

A few restrictions to keep in mind about nickname display:

**•** Records and user lookups on records show full names. Keep in mind, though,
that you can control record and user visibility with sharing rules.

**•** Mobile notifications in the Salesforce mobile app show full names. You can
turn off mobile notifications in the app to avoid this display.

**•** Searches by first, last, and full names aren’t restricted and return matches,
but the search results display only nicknames. Global search auto-complete
recommendations show any first, last, and full names that the user has
searched by or accessed via a record or another location. The recent items
list also shows first, last, and full under the same conditions.

**Type**
boolean

**Properties**
Filter, Update

**Description**
Determines whether users can send and receive Chatter messages in the site.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When true, provides a grid layout for Knowledge search results. With grid layout
in place, you can edit search profile layouts on the Knowledge object to show
and hide different search result fields for different profiles. When you enable the
standard grid layout, search-term highlighting isn’t available. This field is available
in API version 51.0 and later.


Standard Objects Network

**Field Name** **Details**

```
OptionsRecognitionBadgingEnabled

OptionsReputationEnabled

OptionsReputationRecordConversationsDisabled

OptionsSelfRegistrationEnabled

OptionsSendWelcomeEmail

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
Determines whether Recognition Badges is enabled for the site.

**Type**
boolean

**Properties**
Filter, Update

**Description**
Determines if reputation is calculated and displayed for members. This field is
available in API version 31.0 and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
Disables the feed on reputation records.

**Type**
boolean

**Properties**
Filter, Update

**Description**
Determines whether customers and partners can self-register to join the site.
Customers and partners are users with External Identity, Community, Customer
Portal, or partner portal licenses. If `true`, displays a **Not a member?** link on the
login page that points to the default self-registration page. This field is available
in API version 28.0 and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
Determines whether a welcome email is sent when a new user is added to the
site.


Standard Objects Network

**Field Name** **Details**

```
OptionsShowAllNetworkSettings

OptionsSiteAsContainerEnabled

OptionsThreadedDiscussionsEnabled

OptionsTopicFilteringForKnowledgeSearchEnabled

OptionsTopicSuggestionsEnabled

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
Determines whether settings in Experience Management that were hidden based
on how you set up your site are visible or remain hidden.

This field is available in API version 33.0 and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
Determines whether the site is an Experience Builder site ( `true` ) or a Salesforce
Tabs + Visualforce site ( `false` ).

This field is available in API version 29.0 and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
Indicates whether threaded discussions are enabled for the site. Available in API
version 44.0 and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
Determines whether topic filtering is enabled for Knowledge search.

This field is available in API version 55.0 and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
Enables topic suggestions when users write posts.

This field is available in API version 41.0 and later.


Standard Objects Network

**Field Name** **Details**

```
OptionsUpDownVoteEnabled

PwdlessRegEmailTemplateId

SelfRegMicroBatchSubErrorEmailTemplateId

SelfRegProfileId

Status

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
Determines whether up and down voting is enabled for the site.

This field is available in API version 41.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
ID of the email template for the welcome email that users receive when they
sign up with passwordless registration. This field is available in API version 61.0
and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
ID of the profile assigned to users who self-register using micro-batchng. Only
applies if self-registration using micro-batching is enabled for the site.

This field is available in API version 54.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
ID of the profile assigned to users who self-register. Only applies if self-registration
is enabled for the site.

This field is available in API version 29.0 and later.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Status of the site. Available values are:


Standard Objects Network

**Field Name** **Details**

**•** `Live` —The site is online and members can access it. Label is `Published` .

**•** `DownForMaintenance` —The site was previously published, but was
taken offline. Members with the Create and Set Up Experiences permission
can still access the setup for offline sites regardless of profile or membership.
Members aren’t able to access offline sites, but they still appear in the user
interface dropdown menu as `SiteName (Offline)` . Label is
`Offline` .

**•** `UnderConstruction` —The site hasn’t yet been published. When a
user’s profile is associated with the site, and they’ve Create and Set Up
Experiences permission, they can access sites in this status.

After a site is published, it can never be in this status again. Label is `Preview` .

```
UrlPathPrefix

VerificationEmailTemplateId

WelcomeEmailTemplateId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The UrlPathPrefix is a unique string at the end of the URL for the site. For example,
in the site URL _`MyDomainName`_ `.my.site.com/customers`,
`customers` is the `UrlPathPrefix` .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
ID of the email template used when users must verify their identity, for example,
when they log in without a password.

This field is available in API version 44.0 and later.

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
ID of the email template used when sending welcome emails to new members.


### Standard Objects NetworkActivityAudit

Usage

Use this object to find, view, and update sites in your org. If you’re assigned the Modify All Data, View All Data, or Create and Set Up
Experiences permission, you can view all sites in the org. Users without these permissions see only the Preview or Published sites that
they’re members of. If you’re assigned the Create and Set Up Experiences permission, you can customize site settings.

SEE ALSO:

WebStoreNetwork

### NetworkActivityAudit

Represents an audit trail of moderation actions in Experience Cloud sites. This object is available in API version 30.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available only when your org has digital experiences enabled.

Fields

**Field Name** **Details**

```
Action

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The moderation action a member performed on a post, comment, or file in an
Experience Cloud site.

Values are:

**•** Flagged as Inappropriate—A member flagged a post, comment, or file as
inappropriate.

**•** Flagged as Spam - A member flagged a post, comment, or file as spam.

**•** Unflagged—A member removed the flag from a post, comment, or file.

**•** RemovedFlags—A moderator removed all flags from a post, comment, or
file.

**•** DeletedFlaggedItem—A moderator deleted a flagged post, comment,
message, or file.


Standard Objects NetworkActivityAudit

**Field Name** **Details**

**•** DeletedPendingReviewItem—A moderator deleted a post or comment with
pending status.

**•** ModerationRuleFlag—A moderation rule flagged member-generated content.

**•** ModerationRuleBlock—A moderation rule blocked member-generated
content.

**•** ModerationRuleReplace—A moderation rule replaced member-generated
content.

**•** ModerationRuleReview—A moderation rule sent member-generated content
to be reviewed and approved by a moderator.

**•** ModerationRuleFreeze—A moderation rule froze a member because they
created content too frequently within a specific time frame.

**•** ModerationRuleNotify—A moderation rule notified moderators because a
member created content too frequently within a specific time frame.

```
Description

EntityCreatedById

EntityId

EntityType

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Notes entered by the user.

If the entity being tracked is a file, records the version number of the file when
it was flagged.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the user that created the entity being tracked.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the entity that is being tracked. The following entities are tracked:
ChatterMessage, ContentDocument, ContentVersion, FeedComment, and
FeedItem.

**Type**
picklist


Standard Objects NetworkActivityAudit

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The key prefix of the entity being tracked.

```
Name

NetworkId

ParentEntityId

ParentEntityType

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the item being tracked.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Experience Cloud site where the moderation action was performed.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the parent of the entity on which an action was performed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The key prefix of the parent of the entity being audited.

Use this object to view an audit trail of moderation activity for your Experience Cloud sites. You must have the Modify All Data permission
to access this object.

Users with Moderate Experiences Feeds, Moderate Experiences Files, or View All Data can view the audit trail using reports in the Salesforce
user interface.


### Standard Objects NetworkAffinity NetworkAffinity

Represents a junction object that associates a user profile with a Network object, that is, with an Experience Cloud site. Use NetworkAffinity
to assign a default Experience Cloud site to a user profile. This object is available in API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To work with the NetworkAffinity object, you must have View Setup or Customize Application permission.

Fields

**Field Name** **Details**

```
NetworkId

ProfileId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the default Experience Cloud site associated with a user profile.

**Type**
reference

**Properties**
CreateFilter, Group, Sort, Update

**Description**
ID of the user profile the default Experience Cloud site is assigned to.

The default Experience Cloud site allows you to stamp site-agnostic email notifications to all users with that profile with the selected
site's branding. The default Experience Cloud site also becomes the target destination for email notification links. Site-agnostic email
notifications include notifications about records, such as cases, accounts, and opportunities.

The `NetworkId` field is not updatable through the Apex, REST API, or SOAP API. If you want to change the value for `NetworkId`,
you must delete the record and create one with the right value.

### NetworkAuthApiSettings

Represents the settings that control enablement, access, and security for the Headless Registration Flow, Headless Forgot Password
Flow, Headless Passwordless Login Flow, and their associated APIs. This object is available in API version 58.0 and later.


Standard Objects NetworkAuthApiSettings

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Headless identity features are set up via Experience Cloud sites. You must have an Experience Cloud site to access Headless Identity APIs
and store users, even if users never interact with the site directly.

Fields

**Field** **Details**

```
CustomOtpDeliveryHandlerId

DoesForgotPasswordRequireAuth

DoesPasswordLoginRequireAuth

DoesPwdlessLoginRequireAuth

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
This field is a relationship field.

The ID of a custom one-time password (OTP) delivery handler that implements the
`Auth.CustomOneTimePasswordDeliveryHandler` interface.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether authentication is required to access Headless Forgot Password API
when a password reset is requested. If `true`, an access token issued to an internal integration
user in your initial POST request to the
`/services/auth/headless/forgot_password` endpoint is required. The
access token must include the `forgot_password` scope.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether reCAPTCHA is required for headless username-password login that uses
the OAuth 2.0 for First-Party Applications draft protocol.

**Type**
boolean


Standard Objects NetworkAuthApiSettings

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether authentication is required to access Headless Passwordless Login API
when user information is submitted to Salesforce. If `true`, an access token issued to an
internal integration user is required in your initial POST request to the
`/services/auth/headless/init/passwordless/login` endpoint. The
access token must include the `pwdless_login_api` scope.

The default value is `false` . This field is available in API version 59.0 and later.

```
DoesRegistrationRequireAuth

HeadlessDiscoveryExecutionUserId

HeadlessDiscoveryHandlerId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether authentication is required to access Headless Registration API when
user registration information is submitted to Salesforce. If `true`, an access token issued to
an internal integration user in your initial POST request to the
`/services/auth/headless/init/registration` endpoint is required. The
access token must include the `user_registration_api` scope.

The default value is `false` .

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
This field is a relationship field.

The ID of an integration user account to run a headless user discovery Apex handler.

**Relationship Name**
HeadlessDiscoveryExecutionUser

**Refers To**
User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
This field is a relationship field.

The ID of an Apex class that implements the
`Auth.HeadlessUserDiscoveryHandler` interface.


Standard Objects NetworkAuthApiSettings

**Field** **Details**

**Relationship Name**
HeadlessDiscoveryHandler

**Refers To**
ApexClass

```
isFirstPartyAppsAllowed

IsForgotPwdAllowed

IsForgotPwdEmailTemplateAllowlistingEnabled

IsHeadlessUserRegistrationAllowed

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether the Experience Cloud site can use headless identity flows that use the
OAuth 2.0 for First-Party Applications draft protocol.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether the Headless Forgot Password Flow is enabled.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Descriptions**
Determines whether email template allowlisting is enabled for the Headless Registration
Flow, Headless Passwordless Login Flow, and Headless Forgot Password Flow. If `true`, the
initial request to the headless API must include an `emailtemplate` parameter that
contains only allowlisted email templates.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether the Headless Registration Flow is enabled.

The default value is `false` .


Standard Objects NetworkAuthApiSettings

**Field** **Details**

```
IsPwdlessLoginAllowed

IsRecaptchaRequiredForgotPwd

IsRecaptchaRequiredPwdlessLogin

IsRecaptchaRequiredRgstr

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether the Headless Passwordless Login Flow is enabled ( `true` ) or not
( `false` ).

The flow is disabled by default. This field is available in API version 59.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether a reCAPTCHA token is required to access Headless Forgot Password
API when a password reset is requested. If `true`, a reCAPTCHA token is required in your
initial POST request to the `/services/auth/headless/forgot_password`
endpoint.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether a reCAPTCHA token is required to access Headless Passwordless Login
API when user information is submitted to Salesforce. If `true`, a reCAPTCHA token is required
in your initial POST request to the
`/services/auth/headless/init/passwordless/login` endpoint.

By default, a reCAPTCHA token isn’t required ( `false` ). This field is available in API version
59.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether a reCAPTCHA token is required to access Headless Registration API
when user registration information is submitted to Salesforce. If `true`, a reCAPTCHA token
is required in your initial POST request to the
`/services/auth/headless/init/registration` endpoint.

The default value is `false` .


Standard Objects NetworkAuthApiSettings

**Field** **Details**

```
IsUniversalClientRgstrAllowed

IsUserDisambiguationAllowedForgotPwd

IsUserDisambiguationAllowedUsernamePwd

MaxPasswordResetAttempts

NetworkId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether self-registration and passwordless login via Universal Registration API
are enabled.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether the Headless Forgot Password Flow uses the headless user discovery
Apex handler that's specified in the `HeadlessDiscoveryHandlerId` field. The
handler enables users to reset their password with an identifier other than their username,
such as an email address, phone number, or order number.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether headless login flows use the headless user discovery Apex handler
that's specified in the `HeadlessDiscoveryHandlerId` field. The handler enables
users to log in with an identifier other than their username, such as an email address, phone
number, or order number. This field applies to the Authorization Code and Credentials Flow
and the OAuth 2.0 for First-Party Applications login flow.

The default value is `false` .

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of password reset attempts you allow for the Headless Forgot
Password Flow before the user must request a new one-time password (OTP).

**Type**
reference


Standard Objects NetworkAuthApiSettings

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of your Experience Cloud site. This ID is unique within your org.

This field is a relationship field.

**Relationship Name**
Network

**Relationship Type**
Lookup

**Refers To**
Network

```
RecaptchaScoreThreshold

RecaptchaSecretKey

RegistrationExecutionUserId

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The lowest reCAPTCHA score that is accepted before rejecting a request to access Headless
Identity APIs. This value must be between 0.5 and 1. Scores closer to 0.5 are more likely to
be bots, while scores closer to 1 are more likely to be valid users.

You must set a score threshold if `DoesForgotPasswordRequireAuth` or
`DoesRegistrationRequireAuth` fields are set to `true` . reCAPTCHA settings apply
to both the Headless Registration Flow and the Headless Forgot Password Flow.

Google issues a reCAPTCHA score only for reCAPTCHA v3 implementations. If you implement
reCAPTCHA v2, this field doesn’t apply.

**Type**
encryptedstring

**Properties**
Create, Nillable, Update

**Description**
The reCAPTCHA secret key from your API key pair. You get the API key pair from Google when
you set up reCAPTCHA. The secret key helps your app securely communicate with Google.

You must enter a secret key if `DoesForgotPasswordRequireAuth` or
`DoesRegistrationRequireAuth` are set to `true` . reCAPTCHA settings apply to
both the Headless Registration Flow and the Headless Forgot Password Flow.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects NetworkAuthApiSettings

**Field** **Details**

**Description**
The ID of the user who runs your headless registration Apex handler.

This field is a relationship field.

**Relationship Name**
RegistrationExecutionUser

**Relationship Type**
Lookup

**Refers To**
User

```
RegistrationHandlerId

RegistrationUserDefaultProfileId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of your headless registration Apex handler.

This field is a relationship field.

**Relationship Name**
RegistrationHandler

**Relationship Type**
Lookup

**Refers To**
ApexClass

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the default profile that gets assigned to new users when they register.

This field is a relationship field.

**Relationship Name**
RegistrationUserDefaultProfile

**Relationship Type**
Lookup

**Refers To**
Profile


### Standard Objects NetworkDataCategory NetworkDataCategory

Represents data categories in Lightning Web Runtime (LWR) Experience Cloud Sites. This object is available in API version 59.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

This object is available only when your org has Digital Experiences and Knowledge or Service Catalog enabled.

Fields

**Field** **Details**

```
DataCategoryGroupName

DataCategoryName

Description

ImageId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the data category group that contains one or more data categories.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the data category.

**Type**
textarea

**Properties**
Nillable

**Description**
Description of the data category.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Image associated with the data category.


### Standard Objects NetworkDiscoverableLogin

**Field** **Details**

This field is a relationship field.

**Relationship Name**
Image

**Relationship Type**
Lookup

**Refers To**
ManagedContent

```
Label

NetworkId

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The name of the data category shown in the UI.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the associated Experience site.

This field is a relationship field.

**Relationship Name**
### Network

**Relationship Type**
Lookup

**Refers To**
### Network

### NetworkDiscoverableLogin

Represents the Login Discoverable page from where customers and partners log in to an Experience Cloud site. Customers and partners
are users with an External Identity license or any communities license for Experience Cloud. This object is available in API version 44.0
and later.

Supported Calls

`create()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects NetworkDiscoverableLogin

Fields

**Field Name** **Details**

```
ApexHandlerId

ExecuteApexHandlerAsId

NetworkId

UsernameLabel

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The ID of the Apex handler created by the Login Discovery page type.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The ID of the user who is executing the handler.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

Unique

**Description**

The ID of `NetworkId` is unique within your org.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Log in prompt on login page when the login page type is Login Discovery.

Use this object to access the Login Discovery Page, which is a login page type that prompts users to identify themselves with an email
address, phone number, or custom identifier. DiscoverableLogin performs an interview-based login process, where users are first prompted
to provide identity and then authenticated. For example, users receive a verification code that they enter to complete the login process.

Note: The NetworkDiscoverableLogin object is created when **Login Discovery Page** is selected as the login page type on the
Login & Registration (L&R) page. If you later switch to another login page type, such as a Visualforce Page or Experience Builder
Page, the object isn’t deleted. The object persistence means you can’t delete the Apex class associated with the


### Standard Objects NetworkEmailTmplAllowlist

NetworkDiscoverableLogin object. To delete the Apex class, return to the L&R page and change the login page type back to **Login**
**Discovery page** . Select another Apex class, and then you can delete the first one.

### NetworkEmailTmplAllowlist

Represents an allowlist for the one-time password (OTP) email templates that are sent to end users during the Headless Registration
Flow, the Headless Passwordless Login Flow, and the Headless Forgot Password Flow. This object is available in API version 60.0 and
later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
EmailTemplateId

NetworkId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The IDs of the allowlisted email templates that can be sent to users during the headless
authorization flows for registration, passwordless login, and forgot password. You can list
multiple template IDs. When your app sends its initial request to Headless Registration API
or Headless Passwordless Login API, the `emailtemplate` parameter can include only
an email template ID from the allowlist. For Headless Forgot Password API, it works the same
way, but only if email template allowlisting is enabled.

This field is a relationship field.

**Relationship Name**
EmailTemplate

**Relationship Type**
Lookup

**Refers To**
EmailTemplate

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the Experience Cloud site for which the allowlist is being configured.

This field is a relationship field.


### Standard Objects NetworkFeedResponseMetric

**Field** **Details**

**Relationship Name**
### Network

**Relationship Type**
Lookup

**Refers To**
### Network NetworkFeedResponseMetric

Represents an object that stores the date and time values of question posts. It captures information for question creation, answer creation,
and when an answer is marked as best answer This object is available in API version 51.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

The NetworkFeedResponseMetric object is available only if both NetworksEnabled and ChatterEnabled org preferences are enabled.

Fields

**Field** **Details**

```
BestCommentDateTime

BestCommentId

FeedItemCreatedById

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Represents the date and time a user created an answer that was later marked as best answer.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the comment that was marked as the best answer.

**Type**
reference


Standard Objects NetworkFeedResponseMetric

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
Represents the user who created the feed item.

```
FeedItemDateTime

FeedItemId

FirstCommentDateTime

FirstCommentId

MarkedAsBestCommentDateTime

NetworkId

```

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
Represents the date and time when the feed Item was created.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Represents the unique ID of the question post.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Represents the date and time when the first comment was created.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represent the first comment on a feed Item.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Represents the date and time the user marked the answer as best answer.

**Type**
reference


### Standard Objects NetworkMember

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
Represents where the feed item was created.

```
ParentRecordId

### NetworkMember

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Represents the parent record. Parent records can include records like user, account, or group.

Represents a member of an Experience Cloud site. Members can be either users in your company or external users with portal profiles.
This object is available in API version 26.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`, `update()`

Special Access Rules

This object is available only when your org has digital experiences enabled.

Fields

**Field Name** **Details**

```
DefaultGroupNotificationFrequency

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. The default frequency for sending the member’s group
email notifications when the member joins groups in the Experience
Cloud site. The valid values are:

**•** `P` —Email on every post

**•** `D` —Daily digests

**•** `W` —Weekly digests


Standard Objects NetworkMember

**Field Name** **Details**

**•** `N` —Never

The default value is `W` . In sites, the `Email on every post`
option is disabled once more than 10,000 members choose this setting
for the group. All members who had this option selected are
automatically switched to `Daily digests` . However, this field is
not currently enabled. These values are reserved for future use.

```
DigestFrequency

LastChatterActivityDate

MemberId

NetworkId

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. The frequency for sending the member’s personal email
digest for the Experience Cloud site. The valid values are:

**•** `D` —Daily

**•** `W` —Weekly

**•** `N` —Never

The default value is `D` . However, daily and weekly personal digests
aren’t currently available in sites. These values are reserved for future
use.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The last time the member posted or commented in the Experience
Cloud site.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of a person who is a member of an Experience Cloud site.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the Experience Cloud site that the member is part of.


Standard Objects NetworkMember

**Field Name** **Details**

```
PreferencesDisableAllFeedsEmail

PreferencesDisableBestAnswerEmail

PreferencesDisableBookmarkEmail

PreferencesDisableChangeCommentEmail

PreferencesDisableDirectMessageEmail

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false`, the member can automatically receive email for
updates in the Experience Cloud site, based on the types of feed emails
and digests the member has enabled.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false`, the member automatically receives email when
someone selects their answer to a post as best. Available in API 46.0
and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false`, the member automatically receives email every time
someone comments on a feed item after the member has bookmarked
it.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false`, the member automatically receives email every time
someone comments on a change the member has made, such as an
update to their profile.

**Type**
boolean

**Properties**
Filter, Update


Standard Objects NetworkMember

**Field Name** **Details**

**Description**
When `false`, the member automatically receives email every time
someone sends them a direct message in the Experience Cloud site.

```
PreferencesDisableEndorsementEmail

PreferencesDisableFollowersEmail

PreferencesDisableItemFlaggedEmail

PreferencesDisableLaterCommentEmail

PreferencesDisableLikeEmail

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false`, the member automatically receives email every time
someone endorses them for a topic.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false`, the member automatically receives email every time
someone in the Experience Cloud site starts following the member.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false`, the user automatically receives email every time a
member flags a post or comment. This setting only applies for
community moderators (with the Moderate Experiences Feeds
permission) and group owners or managers.

This field is available in API version 29.0 and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false`, the member automatically receives email every time
someone comments on a feed item after the member has commented
on the feed item.

**Type**
boolean


Standard Objects NetworkMember

**Field Name** **Details**

**Properties**
Filter, Update

**Description**
When `false`, the member automatically receives email every time
someone comments on a feed item after the member has liked the
feed item.

```
PreferencesDisableMarketingCloudEmail

PreferencesDisableMentionsPostEmail

PreferencesDisableMessageEmail

PreferencesDisableProfilePostEmail

PreferencesDisableSharePostEmail

```

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false`, the member automatically receives marketing emails
sent by Journey Builder. Available in API version 41.0 and later.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false`, the member automatically receives email every time
the member is mentioned in posts.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false`, the member automatically receives email every time
the member is sent a Chatter message.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false`, the member automatically receives email every time
someone posts to the member’s profile.

**Type**
boolean


Standard Objects NetworkMember

**Field Name** **Details**

**Properties**
Filter, Update

**Description**
When `false`, the member automatically receives email every time
the member’s post is shared.

```
PreferencesDisCommentAfterLikeEmail

PreferencesDisMentionsCommentEmail

PreferencesDisProfPostCommentEmail

ReputationPoints

```

Usage

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false`, the member automatically receives email every time
someone comments on a post the member has liked.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false`, the member automatically receives email every time
the member is mentioned in comments.

**Type**
boolean

**Properties**
Filter, Update

**Description**
When `false`, the member automatically receives email every time
someone comments on posts on the member’s profile.

**Type**
double

**Properties**
Filter, Sort, Update

**Description**
The number of reputation points the user has accumulated by
performing actions in the Experience Cloud site.

Use this object to query members of a certain Experience Cloud site and to update their email notification settings. If you have Modify
All Data, View All Data, or Create and Set Up Experiences, you can view all members of any Experience Cloud site, regardless of your own


### Standard Objects NetworkMemberGroup

membership. If you have Modify All Data or Create and Set Up Experiences, you can also update any member’s email settings. Users
without these permissions can update their own email settings and can see members of the Experience Cloud sites that they’re also
members of.

You can directly update reputation points for a member via the Salesforce API. You can also use Apex triggers to send custom notifications
based on changes to reputation points.

### NetworkMemberGroup

Represents a group of members in an Experience Cloud site. Members can be either users in your internal org or external users assigned
portal profiles. An administrator adds members to an Experience Cloud site by adding a profile or a permission set, and any user with
the profile or permission set becomes a member of the site. This object is available in API version 26.0 and later.

Note: If a Chatter customer (from a customer group) is assigned a permission set that is also associated with an Experience Cloud
site, the Chatter customer won’t be added to the site.

Prior to API version 27.0, this object was called NetworkProfile.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`

Note: The `upsert()` call is not supported for this object.

Special Access Rules

This object is available only when your org has digital experiences enabled.

Fields

**Field Name** **Details**

```
AssignmentStatus

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of a profile or permission set within an Experience Cloud site. Values
are:

**•** `Add Calculated` —The number of users that need to be added are
calculated and the add operation is in progress.

**•** `Added` —Users with this profile or permission set are members.

**•** `Failed Add` —Users with this profile or permission set were not
successfully made members.

**•** `Failed Remove` —Users with this profile or permission set were not
successfully removed from membership.


Standard Objects NetworkMemberGroup

**Field Name** **Details**

**•** `Remove Calculated` —The number of users that need to be removed
are calculated and the remove operation is in progress.

**•** `Waiting for Add` —The profile or permission set was added to the
Experience Cloud site, but the async process hasn’t completed yet. After the
process is complete, the status is updated to `Added` .

**•** `Waiting for Remove` —Use this status to remove all the members
belonging to a profile or permission set and remove a profile or permission
set from an Experience Cloud site.

```
NetworkId

ParentId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Experience Cloud site that this group of members is associated with.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the profile or permission set associated with the Experience Cloud site.

Use this object to view the profiles or permission sets associated with a particular Experience Cloud site. Profiles and permission sets are
added and removed asynchronously, so you can also check the status of a profile or permission set that was updated in a site.

If you have Modify All Data, View All Data, or Create and Set Up Experiences, you can view all profiles or permission sets for any Experience
Cloud site in the org, regardless of your membership. If you have Modify All Data or Create and Set Up Experiences, you can also add
profiles or permission sets. Users without these permissions can only find profiles and permission sets for Experience Cloud sites that
they’re members of.

Sample Code

```
// Create a new NetworkMemberGroup with a profile as the ParentId

NetworkMemberGroup nmgInsert = new NetworkMemberGroup();

nmgInsert.setNetworkId('{enter your network ID : ODB...}');

nmgInsert.setParentId('enter the profile or permission set ID : 00e... or 0PS...');

SaveResult[] results = connection.create(new SObject[] { nmgInsert });

// Update an existing NetworkMemberGroup to be removed from the Network

NetworkMemberGroup nmgUpdate = new NetworkMemberGroup();

nmgUpdate.setId('enter your NetworkMemberGroup ID : 0DL...');

```


### Standard Objects NetworkModeration

```
   nmgUpdate.setAssignmentStatus('WaitingForRemove');

   SaveResult[] results = connection.update(new SObject[] { nmgUpdate });

### NetworkModeration

```

Represents a flag on an item in a community. This object is available in API version 30.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

This object is available only when your org has digital experiences enabled.

Fields

**Field Name** **Details**

```
EntityId

ModerationType

NetworkId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the post, comment, or file that was flagged.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Determines the type of flag applied to an item. Values are:

**•** FlagAsInappropriate

**•** FlagAsSpam

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the community in which the item was flagged.


### Standard Objects NetworkPageOverride

**Field Name** **Details**

```
Visibility

```

Usage

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Nillable, Sort

**Description**
Determines visibility of a flagged item. Values are:

**•** SelfAndModerators—The user who flagged the item and any moderators
can see the flagged item. This is the default value.

**•** ModeratorsOnly—Only moderators can see the flagged item. If
ModeratorsOnly is selected, only moderators can set flags using the API.

Use this object to view the items flagged for moderation within a community. Additionally, users with “Moderate Feeds” and “Modify
All Data” can remove flags.

Flags on items are created either when a member manually flags an item in a community (if flagging is enabled for that community),
or when a trigger automatically flags an item because the item met the trigger criteria.

### NetworkPageOverride

Represents information about custom pages used to override the default pages in Experience Cloud sites. You can create Experience
Builder or Visualforce pages and override the default pages in a site. Using custom pages allows you to create a more personalized
experience for your users. This object is available in API version 34.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

**•** Only users with the Create and Setup Experiences permission can update this object.

**•** You can’t override the Change Password Page with a page created using Experience Builder. You can only override it with a Visualforce
page.

Fields

**Field Name** **Details**

```
NetworkId

```

**Type**
reference


### Standard Objects NetworkSelfRegistration

**Field Name** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Experience Cloud site where a custom page is used to override a
default page.

```
OverrideSetting

OverrideType

### NetworkSelfRegistration

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of the page used to override a default page in the Experience Cloud
site. `OverrideSetting` can take the following values:

**•** `Standard` —The standard page that comes by default with the site.

**•** `Configurable` —The page created when the Configurable Self-Reg
registration page type or the Login Discovery login page type is selected.

**•** `Designer` —A custom page created using Experience Builder.

**•** `Visualforce` —A custom page created using Visualforce.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The name of the default page in the Experience Cloud site that you want to
override with a custom page. `OverrideType` can take the following values:

**•** `LoginRequired`

**•** `ChangePassword`

**•** `ForgotPassword`

**•** `SelfReg`

**•** `Home`

Represents the account that self-registering Experience Cloud users are associated with by default. Self-registering users in an Experience
Cloud site are required to be associated with an account, which the admin must specify while setting up self-registration for the site. If
an account isn’t specified, Salesforce creates person accounts (when enabled) for self-registering users. This object is available in API
version 34.0 and later.


Standard Objects NetworkSelfRegistration

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
AccountId

ApexHandlerId

CurrencyIsoCode

ExecuteApexHandlerAsId

NetworkId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The ID of the account that self-registering users in the Experience Cloud site are
associated with.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The ID of the Apex handler created by Configurable Self-Reg registration page
type.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the org.

The default value is `USD` .

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The ID of the user who is executing the configurable self-registration handler.

**Type**
reference


Standard Objects NetworkSelfRegistration

**Field Name** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The ID of `NetworkId` is unique within your org.

You can use only one account per Experience Cloud site to assign self-registering
users.

```
OptionsDisableStandardRgstrComponent

OptionsIncludePassword

OptionsShowEmail

OptionsShowFirstName

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Determines whether you can use standard Aura and Lightning Web Runtime
(LWR) components for self-registration. If this field is `true`, self-registration flows
that use these components don’t work.

For more control over self-registration, set this field to `true` if you’re not using
the standard self-registration component.

**Type**
Boolean

**Properties**
Create, Filter, Update

**Description**

Option on Configurable Self-Reg registration page. If true, the Include Password
field is selected.

**Type**
Boolean

**Properties**
Create, Filter, Update

**Description**

Option on Configurable Self-Reg registration page. If true, the Email field appears
on the self-registration form.

**Type**
Boolean

**Properties**
Create, Filter, Update

**Description**

Option on the Configurable Self-Reg registration page. If true, the First Name
field appears on the self-registration form.


Standard Objects NetworkSelfRegistration

**Field Name** **Details**

```
OptionsShowLastName

OptionsShowMobilePhone

OptionsShowNickname

OptionsShowUsername

PermissionSetGroupId

```

**Type**
Boolean

**Properties**
Create, Filter, Update

**Description**

Option on the Configurable Self-Reg registration page. If true, the Last Name field
appears on the self-registration form.

**Type**
Boolean

**Properties**
Create, Filter, Update

**Description**

Option on the Configurable Self-Reg registration page. If true, the Mobile field
appears on the self-registration form.

**Type**
Boolean

**Properties**
Create, Filter, Update

**Description**

Option on the Configurable Self-Reg registration page. If true, the Nickname field
appears on the self-registration form.

**Type**
Boolean

**Properties**
Create, Filter, Update

**Description**

Option on the Configurable Self-Reg registration page. If true, the Username field
appears on the self-registration form.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the permission set group used for the self registration. This field is a
relationship field.

**Relationship Name**
PermissionSetGroup


### Standard Objects NetworkUserHistoryRecent

**Field Name** **Details**

**Refers To**
PermissionSetGroup

```
VerificationMethod

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of verification method that a user must supply when registering, which
can be:

**•** `SyncEmail` —User must supply an email address to verify identity.

**•** `SMS` —User must supply a phone number to verify identity.

### NetworkUserHistoryRecent

Represents an Experience Cloud site user’s history of accessed records. This object is available in API version 42.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `undelete()`

Special Access Rules

Only users with the Modify All Data permission can view and delete these data.

Fields

**Field** **Details**

```
AccessTimestamp

ActionType

```

**Type**
datetime

**Properties**
Create, Filter, Sort

**Description**
The time at which the record was accessed.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


Standard Objects NetworkUserHistoryRecent

**Field** **Details**

**Description**
Indicates the action type taken by the user. The possible values are:

**•** Read

**•** Write

```
DomainName

FeedCommentId

FeedItemId

NetworkId

NetworkUserId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The domain used to access the record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Feed comment accessed by the user.

**Type**
reference

**Properties**
Create, Filter, Group,Sort, Update

**Description**
Feed item accessed by the user.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the Experience Cloud site used to access the record or comment.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
User’s Experience Cloud site user ID to access the record or comment.


Standard Objects NetworkUserHistoryRecent

**Field** **Details**

```
RecordId

RecordKeyPrefix

Url

UserType

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The record that was accessed.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Record’s ID key prefix.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The URL from which the user accessed the record.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of user who accessed this record. The possible values include:

**•** Standard

**•** Partner

**•** Customer Portal Manager

**•** Customer Portal User

**•** Guest

**•** High Volume Portal

**•** CSN Only

**•** Self Service

Use the NetworkUserHistoryRecent object to delete comments, posts, or record access by Experience Cloud site users who would like
all such activity to be removed.


### Standard Objects Note Note

Represents a note, which is text associated with a custom object or a standard object, such as a Contact, Contract, or Opportunity.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Body

IsDeleted

IsPrivate

OwnerId

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Body of the note. Limited to 32 KB.

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
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true`, only the note owner or a user with the “Modify All Data” permission can view the
note or query it via the API. Note that if a user who does not have the “Modify All Data”
permission sets this field to `true` on a note that they do not own, then they can no longer
query, delete, or update the note. Label is **Private** .

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who owns the note.


Standard Objects Note

**Field** **Details**

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

```
ParentId

Title

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the object associated with the note.

This is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, AssessmentIndicatorDefinition, AssessmentTask,
AssessmentTaskContentDocument, AssessmentTaskDefinition, AssessmentTaskOrder, Asset,
Award, BoardCertification, BusinessLicense, BusinessMilestone, BusinessProfile, CareBarrier,
CareBarrierDeterminant, CareBarrierType, CareDeterminant, CareDeterminantType,
CareDiagnosis, CareMetricTarget, CareObservationComponent,
CarePgmProvHealthcareProvider, CareProgram, CareProgramCampaign,
CareProgramEligibilityRule, CareProgramEnrollee, CareProgramEnrolleeProduct,
CareProgramEnrollmentCard, CareProgramGoal, CareProgramProduct, CareProgramProvider,
CareProgramTeamMember, CareProviderAdverseAction, CareProviderFacilitySpecialty,
CareRegisteredDevice, CareRequest, CareRequestDrug, CareRequestExtension,
CareRequestItem, CareSpecialty, CareTaxonomy, CommSubscription,
CommSubscriptionChannelType, CommSubscriptionConsent, CommSubscriptionTiming,
Contact, Contract, CreditMemo, DelegatedAccount, EngagementChannelType,
EnrollmentEligibilityCriteria, HealthcareFacility, HealthcareFacilityNetwork,
HealthcarePayerNetwork, HealthcarePractitionerFacility, HealthcareProvider,
HealthcareProviderNpi, HealthcareProviderSpecialty, HealthcareProviderTaxonomy,
IdentityDocument, Image, IndividualApplication, Invoice, Lead, Location, MemberPlan,
Opportunity, Order, OtherComponentTask, PersonEducation, PersonLifeEvent, Product2,
ProductRequest, ProductRequestLineItem, PurchaserPlan, ReceivedDocument,
ServiceAppointment, ServiceResource, Shift, SocialPost, Visit, VisitedParty, Visitor,
VolunteerProject, WorkOrder, WorkOrderLineItem

**Type**
string


### Standard Objects NoteAndAttachment

**Field** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Title of the note.

Usage

Use this object to manage notes for an object.

SEE ALSO:

Overview of Salesforce Objects and Fields

### NoteAndAttachment

This read-only object contains all notes and attachments associated with an object.

Supported Calls

```
   describeSObjects()

```

Fields

**Field** **Details**

```
IsDeleted

IsNote

IsPrivate

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
Indicates whether the object contains a note ( `true` ) or an attachment ( `false` ).

**Type**
boolean


Standard Objects NoteAndAttachment

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true`, only the note owner or a user with the “Modify All Data” permission can view the
note or query it via the API. Note that if a regular user who does not have “Modify All Data”
permission sets this field to `true` on a note that they do not own, then they can no longer
query, delete, or update that note. Label is **Private** .

```
OwnerId

ParentId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who owns the note and attachment.

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
Filter, Group, Sort

**Description**
ID of the parent object.

This is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, AssessmentIndicatorDefinition, AssessmentTask,
AssessmentTaskContentDocument, AssessmentTaskDefinition, AssessmentTaskOrder, Asset,
Award, BoardCertification, BusinessLicense, BusinessMilestone, BusinessProfile, CareBarrier,
CareBarrierDeterminant, CareBarrierType, CareDeterminant, CareDeterminantType,
CareDiagnosis, CareMetricTarget, CareObservationComponent,
CarePgmProvHealthcareProvider, CareProgram, CareProgramCampaign,
CareProgramEligibilityRule, CareProgramEnrollee, CareProgramEnrolleeProduct,
CareProgramEnrollmentCard, CareProgramGoal, CareProgramProduct, CareProgramProvider,


### Standard Objects NoteTag

**Field** **Details**

CareProgramTeamMember, CareProviderAdverseAction, CareProviderFacilitySpecialty,
CareRegisteredDevice, CareRequest, CareRequestDrug, CareRequestExtension,
CareRequestItem, CareSpecialty, CareTaxonomy, CommSubscription,
CommSubscriptionChannelType, CommSubscriptionConsent, CommSubscriptionTiming,
Contact, Contract, CreditMemo, DelegatedAccount, EngagementChannelType,
EnrollmentEligibilityCriteria, HealthcareFacility, HealthcareFacilityNetwork,
HealthcarePayerNetwork, HealthcarePractitionerFacility, HealthcareProvider,
HealthcareProviderNpi, HealthcareProviderSpecialty, HealthcareProviderTaxonomy,
IdentityDocument, Image, IndividualApplication, Invoice, Lead, Location, MemberPlan,
Opportunity, Order, OtherComponentTask, PersonEducation, PersonLifeEvent, Product2,
ProductRequest, ProductRequestLineItem, PurchaserPlan, ReceivedDocument,
ServiceAppointment, ServiceResource, Shift, SocialPost, Visit, VisitedParty, Visitor,
VolunteerProject, WorkOrder, WorkOrderLineItem

```
 Title

```

Usage

**Type**
string

**Properties**
Filter, Nillable, Group, Sort

**Description**
Title of the note.

Use this object to list all notes and attachments for an object.

To retrieve notes and attachments, issue a describe call on an object, which returns a query result for each activity since the record was
created. You can’t directly query this object.

SEE ALSO:

### Note

Attachment

### NoteTag

Associates a word or short phrase with a Note.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`


Standard Objects NoteTag

Fields

**Field Name** **Details**

```
ItemId

Name

TagDefinitionId

Type

```

Usage

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

NoteTag stores the relationship between its parent TagDefinition and the Note being tagged. Tag objects act as metadata, allowing
users to describe and organize their data.


### Standard Objects OauthCustomScope

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.

### OauthCustomScope

Represents a permission defining the protected data that a connected app can access from an external entity when Salesforce is the
OAuth authorization provider.

An OAuth custom scope tells an external entity about a connected app’s permissions to access protected data. The OAuth custom scope
that you create in your Salesforce org corresponds to the same custom scope defined in your external entity, and assigned to the resource.

For example, you define an Order Status custom scope in your external entity that allows access to customer order status data in your
order system’s API. In Salesforce, you create an OAuth custom scope that you also name Order Status. You assign this custom scope to
the connected app requesting access to the order status API. When the external entity receives the connected app’s request to access
a customer’s order status, it validates the connected app’s access token and Order Status scope. With a successful validation, the app
can access the customer order status information in the order system’s API.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

You must have the “Manage Connected Apps” permission to access this object.

Fields

**Field Name** **Details**

```
Description

DeveloperName

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The description of the permission provided to the connected app by the scope.
The custom scope’s description must be unique, can only include alphanumeric
characters, and can be up to 60 characters long.

You can enter a custom label in place of a description. An advantage of using a
custom label is that you can maintain reusable text in a single location and
[translate the text into multiple languages. See Custom Labels.](https://help.salesforce.com/articleView?id=cl_about.htm&language=en_US)

Note: The description formatting requirements that apply to custom
scopes also apply to custom labels.

**Type**
string


Standard Objects OauthCustomScope

**Field Name** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Use when referring to the OAuth custom scope from a program. This label must
be unique, and can include only alphanumeric characters and underscores.

```
IsPublic

Language

MasterLabel

NamespacePrefix

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the object is included in the connected app’s OpenID Connect
[discovery endpoint. For more information, see OpenID Connect Discovery](https://help.salesforce.com/articleView?id=remoteaccess_using_openid_discovery_endpoint.htm&language=en_US)
[Endpoint.](https://help.salesforce.com/articleView?id=remoteaccess_using_openid_discovery_endpoint.htm&language=en_US)

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the default language defined for the developing org.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The master label for the custom scope record. This label must be unique, and
can include only alphanumeric characters and underscores.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix for an OAuth custom scope that's been installed as part
of a second-generation managed package. If the custom scope isn't packaged,
this value is empty. This field is available in API version 61.0 and later.


### Standard Objects OauthCustomScopeApp OauthCustomScopeApp

Represents the name of the connected app to which the custom scope is assigned. This object is available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
OauthCustomScopeId

### OauthToken

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the connected app to which the custom scope is assigned. If the connected
app is part of a package, include the package’s namespace prefix with the connected app’s
name. Use the following format: _**`<namespace_prefix>`**_ `__` _**`<connected_app>`**_ .
Use two underscores (_) between the namespace prefix and connected app’s name.

This is a relationship field.

**Relationship Name**
### OauthCustomScope

**Relationship Type**
Lookup

**Refers To**
### OauthCustomScope

Represents an OAuth access token for connected app authentication. Use this object to create a user interface for token management.
This object is available in API version 32.0 and later.

A connected app integrates an application with Salesforce using APIs. Connected apps use standard SAML and OAuth protocols to
authenticate, provide single sign-on, and provide tokens for use with Salesforce APIs. In addition to standard OAuth capabilities, connected
apps allow Salesforce admins to set various security policies and have explicit control over who can use the corresponding apps. Each
time that a user grants access to an application, the application obtains a new access token.

Supported Calls

`describeSObjects()`, `query()`


Standard Objects OauthToken

Special Access Rules

Users with the Customize Application permission see all tokens for all users in the org. Otherwise, you see only your own tokens.

[If you try to use Apex DML operations and then query this object in the same call, you get an](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexref.meta/apexref/apex_dml_section.htm) `UncommittedWork` error with this
description.

```
   A callout was unsuccessful because of pending uncommitted work related to a process, flow,

    or Apex operation.

   Commit or roll back the work, and then try again.

```

To avoid this error, execute DML operations and queries in separate, asynchronous calls.

Fields

**Field Name** **Details**

```
AccessToken

AppMenuItemId

AppName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The refresh token for authorization.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The unique ID for the App Picker menu item that’s associated with this OAuth
token.

This is a relationship field.

**Relationship Name**
AppMenuItem

**Relationship Type**
Lookup

**Refers To**
AppMenuItem

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The label for the connected app that’s associated with this OAuth token.


Standard Objects OauthToken

**Field Name** **Details**

```
DeleteToken

Id

LastUsedDate

RequestToken

UseCount

UserId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

A token that can be used at the revoke OAuth token endpoint to remove this
token.

**Type**
ID

**Properties**
Defaulted on create, Filter, Group, idLookup, Sort

**Description**

Reserved for future use. Currently, the value is always `null` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The most recent date when the OAuth token was used.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The authorization code that was used to request the corresponding AccessToken.
With this authorization code, you can revoke the corresponding AccessToken by
passing the DeleteToken.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

How often the token has been used.

**Type**
reference


### Standard Objects OauthTokenExchangeHandler

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**

The owner of the token.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

Usage

To delete an AccessToken, send a request to the revoke OAuth token endpoint with the DeleteToken as the parameter. For example,
the URL `https://` _`MyDomainName`_ `.my.salesforce.com/services/oauth2/revoke?token=(the Delete`
`Token)` causes the deletion of the token.

In API version 34.0 and later, this object was enhanced to help manage high instance counts. A `query()` call returns up to 500 rows.
A `queryMore()` call returns 500 more, up to 2,500 total. No more records are returned after 2,500. To make sure that you don’t miss
any records, issue a `COUNT()` query in a SELECT clause for OauthToken. This query gives you the total number of records. If there are
more than 2,500 records, use these options to manage your results.

**•** Divide queries by filtering on fields like `UserId` to return subsets of less than 2,500 records.

**•** Use `[OFFSET](https://developer.salesforce.com/docs/atlas.en-us.262.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_offset.htm)` to get batches of 2,000 records. Start with an `OFFSET` of 0 and then increment by 2,000. If you use this option, we
recommend that you also use `[LIMIT](https://developer.salesforce.com/docs/atlas.en-us.262.0.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_limit.htm)` to limit each query to 2,000.

Note: The `OFFSET` clause is limited to 2,000 rows. Requesting an offset greater than 2,000 results in a
NUMBER_OUTSIDE_VALID_RANGE error.

For example, use an initial query with this structure.

```
     SELECT <desired fields> FROM OauthToken LIMIT 2000 OFFSET 0

```

Then, run another query with an offset of 2,000.

```
     SELECT <desired fields> FROM OauthToken LIMIT 2000 OFFSET 2000

```

Continue to increase the offset by 2,000 until you have results for all records.

### OauthTokenExchangeHandler

Represents a token exchange handler. The token exchange handler also consists of an Apex class. During the OAuth 2.0 token exchange
flow, the token exchange handler is used to validate tokens from an external identity provider and to map users to Salesforce. This object
is available in API version 60.0 and later.


Standard Objects OauthTokenExchangeHandler

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Fields

**Field** **Details**

```
Description

DeveloperName

IsContactCreationAllowed

IsEnabled

IsUserCreationAllowed

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A description for your token exchange handler.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The API name for the handler.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
For internal use only.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the handler is enabled for the token exchange flow.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects OauthTokenExchangeHandler

**Field** **Details**

**Description**
Indicates whether the handler can set up new users. During the token exchange flow, the
Apex handler maps users from the identity provider to Salesforce. If the
`IsUserCreationAllowed` field is `true`, the `canCreateUser` boolean in the
`getUserForTokenSubject` method is `true`, and the user doesn’t exist in Salesforce,
the handler sets up a new User object, which Salesforce automatically inserts to finish creating
the user.

The default value is `false` .

```
Language

MasterLabel

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the language used in the org where the token exchange handler was created.

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

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects OauthTokenExchangeHandler

**Field** **Details**

**Description**
The label of the token exchange handler record.

```
NamespacePrefix

SupportedTokenTypesAccessToken

SupportedTokenTypesIdToken

SupportedTokenTypesJwt

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
`namespacePrefix__componentName` notation. The namespace prefix can have
one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the handler supports opaque access tokens from the identity provider.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the handler supports OpenID Connect ID tokens from the identity provider.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the handler supports tokens from the identity provider that are in JWT
format, such as JWT-based access tokens.


### Standard Objects OauthTokenExchHandlerApp

**Field** **Details**

```
SupportedTokenTypesRefreshToken

SupportedTokenTypesSaml2

TokenHandlerApexId

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the handler supports OAuth 2.0 refresh tokens from the identity provider.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the handler supports SAML 2.0 assertions from the identity provider.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Apex class associated with the token exchange handler. The class contains methods to
validate the token and map users to Salesforce. It must extend the
`Oauth2TokenExchangeHandler` Apex class.

This field is a relationship field.

**Relationship Name**
TokenHandlerApex

**Relationship Type**
Lookup

**Refers To**
ApexClass

### OauthTokenExchHandlerApp

Represents the enablement settings for a specific Salesforce connected app or external client app that’s enabled for the token exchange
handler. A handler can be enabled for multiple apps. This object is available in API version 60.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects OauthTokenExchHandlerApp

Special Access Rules

Fields

**Field** **Details**

```
ApexExecutionUserId

ConnectedApplicationId

IsDefault

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the user who runs the Apex token exchange handler. We recommend that you use
an integration user.

This field is a relationship field.

**Relationship Name**
ApexExecutionUser

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The connected app that’s being used to integrate with Salesforce.

This field is a relationship field.

**Relationship Name**
ConnectedApplication

**Relationship Type**
Lookup

**Refers To**
ConnectedApplication

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the token exchange handler is the default handler for this app. During the
token exchange flow, in the token request, you can optionally include a `token_handler`


### Standard Objects ObjectDataImport

**Field** **Details**

parameter with the name of a specific handler’s Apex class. If you don’t include this parameter,
Salesforce defaults to the default handler.

The default value is `false` .

```
OauthTokenExchangeHandlerId

### ObjectDataImport

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The `OauthTokenExchangeHandler` with which these enablement settings are
associated.

This field is a relationship field.

**Relationship Name**
OauthTokenExchangeHandler

**Relationship Type**
Lookup

**Refers To**
OauthTokenExchangeHandler

Represents the data import status of one or more object records. This object is available in API version 57.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
EndDate

FileName

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time (in UTC) when the data import finished.

**Type**
string


Standard Objects ObjectDataImport

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Optional. If the data import was from a comma-delimited file (CSV), the name of the file. The
maximum length is 120 characters.

```
ObjectDataImportNumber

OwnerId

PrimaryObject

Result

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number identifying the data import.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user who owns the data import status record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The name of the primary object being imported. For example, Lead. This value is usually
provided programmatically. The maximum length is 120 characters.

**Type**
textarea

**Properties**
Nillable

**Description**
The JSON response of the data object import result, including error messages.


### Standard Objects ObjectDataImportReference

**Field** **Details**

```
Status

Type

```

Associated Objects

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The processing status of the data object import.

Possible values are:

**•** `Completed`

**•** `In Progress`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of data import, such as from a comma-delimited file or through a connector.

Possible values are:

**•** `CSV Async`

**•** `CSV Sync`

**•** `External Record Import` —A record imported or updated by Partner Connect
[between a partner and vendor system. To see this field, enable Partner Connect. See Set](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_partner_parent.htm&type=5&language=en_US)
[Up Partner Connect as a Partner in](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_partner_parent.htm&type=5&language=en_US) _Salesforce Help_ . Available in API version 62.0 and later.

**•** `One time Connector`

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**[ObjectDataImportChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Sharing rules are available for the object.

**ObjectDataImportOwnerSharingRule on page 65**
Sharing rules are available for the object.

**ObjectDataImportShare on page 67**
Sharing is available for the object.

### ObjectDataImportReference

Represents the relationships to the associated reference objects showing the source from which the data is imported. This object is
available in API version 57.0 and later.


### Standard Objects ObjectMetadataTag

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

ObjectDataImportReference is read only and can only be queried.

Fields

**Field** **Details**

```
ObjectDataImportId

ObjectDataImportReferenceNumber

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Foreign key to the ObjectDataImport object.

This field is a relationship field.

**Relationship Name**
ObjectDataImport

**Relationship Type**
Lookup

**Refers To**
ObjectDataImport

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Foreign key to the reference object. For example, AsyncApiJob or DatasetImportRequest.

### ObjectMetadataTag

Represents a meta tag for a store page. Meta tags in HTML documents provide structured data used by search engines for ranking and
to show content in search results. This object is available in API version 60.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `undelete()`,
`update()`, `upsert()`


Standard Objects ObjectMetadataTag

Special Access Rules

This object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
CurrencyIsoCode

Language

Name

RecordId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Possible values are:

**•** `USD` —U.S. Dollar

The default value is `USD` .

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The language of the page meta tag.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the page meta tag.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the product or product category with which this record is associated.

This is a polymorphic relationship field.

**Relationship Name**
Record

**Relationship Type**
Lookup


### Standard Objects ObjectPermissions

**Field** **Details**

**Refers To**
Product2, ProductCategory

Availability in API versions:

**•** Product2 is available in API versions 60.0 and later

**•** ProductCategory is available in API versions 63.0 and later

```
TagType

Value

### ObjectPermissions

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of the page meta tag.

Possible values are:

**•** `Description` —Meta Description

**•** `Title` —Title Tag

**Type**
textarea

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The value of the page meta tag. This value populates the HTML tag. For example, a meta tag
with a `Type` of `Title` and a `Value` of `GoBrew Espresso` renders the HTML
`<title>GoBrew Espresso</title>` for the page.

Represents the enabled object permissions for the parent PermissionSet. This object is available in API version 24.0 and later.

To grant a user access to an object, associate an ObjectPermissions record with a PermissionSet that’s assigned to a user. ObjectPermissions
records are only supported in PermissionSet, not in Profile.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Summer ’20 and later, only users with the View Setup and Configuration permission can access this object.


Standard Objects ObjectPermissions

Fields

**Field Name** **Details**

```
ParentId

PermissionsCreate

PermissionsDelete

PermissionsEdit

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The `Id` of this object’s parent PermissionSet.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
PermissionSet

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
If `true`, users assigned to the parent PermissionSet can create records for this
object. Requires `PermissionsRead` for the same object to be `true` .

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
If `true`, users assigned to the parent PermissionSet can delete records for this
object. Requires `PermissionsRead` and `PermissionsEdit` for the
same object to be `true` .

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
If `true`, users assigned to the parent PermissionSet can edit records for this
object. Requires `PermissionsRead` for the same object to be `true` .


Standard Objects ObjectPermissions

**Field Name** **Details**

```
PermissionsModifyAllRecords

PermissionsRead

PermissionsViewAllFields

PermissionsViewAllRecords

SobjectType

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
If `true`, users assigned to the parent PermissionSet can edit all records for this
object, regardless of sharing settings. Requires `PermissionsRead`,
`PermissionsDelete`, `PermissionsEdit`, and
`PermissionsViewAllRecords` for the same object to be `true` .

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
If `true`, users assigned to the parent PermissionSet can view records for this
object.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
If `true`, users assigned to the parent PermissionSet can view all fields and field
data for this object. Available in API version 63.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
If `true`, users assigned to the parent PermissionSet can view all records for this
object, regardless of sharing settings. Requires `PermissionsRead` for the
same object to be `true` .

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The object’s API name. For example, `Merchandise__c` .


Standard Objects ObjectPermissions

Permission Dependencies

Some user permissions have dependencies on object permissions. For example, if a permission set has the “Transfer Leads” permission,
it also has “Read” and “Create” on the leads object.

You can query from ObjectPermissions up to the parent PermissionSet object. For example:

```
   SELECT Parent.Name, Parent.PermissionsTransferAnyLead, PermissionsRead, PermissionsCreate

   FROM ObjectPermissions

   WHERE SobjectType = 'Lead'

```

Determining Object Access with “Modify All Data”

When using SOQL to query object permissions, be aware that some object permissions are enabled because a user permission requires
them.

The exception to this rule is when “Modify All Data” is enabled. While it enables all object permissions, it doesn’t physically store any
object permission records in the database. As a result, unlike object permissions that are required by a user permission—such as “View
All Data” or “Import Leads”—the query still returns permission sets with “Modify All Data,” but the object permission record will contain
an invalid ID that begins with “000”. This ID indicates that the object has full access due to “Modify All Data” and the object permission
record can’t be updated or deleted. To remove full access from these objects, disable “Modify All Data” and then delete the resulting
object permission record. This ensures that when using SOQL to find all the objects that have full access, it returns all objects that have
this access regardless of whether it’s due to “Modify All Data” or because an administrator set full access.

For example, the following will return all permission sets that have “Read” on the Merchandise__c object, regardless of whether it’s
explicitly defined on the object or implicitly defined through “Modify All Data.”

```
   SELECT Id, Parent.label, SobjectType, PermissionsRead,

     Parent.PermissionsModifyAllData, ParentId

   FROM ObjectPermissions

   WHERE PermissionsRead = true and SobjectType = 'Merchandise__c'

```

Nesting Object Permissions

You can nest ObjectPermissions in a PermissionSet query. For example, the following returns any permission sets where “Transfer Leads”
is true. Additionally, the result set will include the “Read” object permission on leads. This is done by nesting the SOQL with an object
permission query using the relationship name for object permissions: `ObjectPerms` .

```
   SELECT Id,Name,PermissionsTransferAnyLead,

   (SELECT Id, PermissionsRead from ObjectPerms where SobjectType='Lead')

   FROM PermissionSet

   WHERE PermissionsTransferAnyLead = true

```

As a result, it’s possible to traverse the relationship between the PermissionSet and any child-related objects (in this case, ObjectPermissions).
You can do this from the PermissionSet object by using the child relationship ( `ObjectPerms`, `FieldPerms`, and so on) or from
the child object by referencing the PermissionSet with `Parent.` _**`permission_set_attribute`**_ .

It’s important to consider when to use a conditional `WHERE` statement to restrict the result set. To query based on an attribute on the
permission set object, nest the SOQL with the child relationship. However, to query based on an attribute on the child object, you must
reference the permission set parent attribute in your query.


### Standard Objects ObjectRelatedUrl

The following two queries return the same columns with different results, based on whether you use the child relationship or parent
notation.

```
   SELECT Id, Name, PermissionsModifyAllData,

   (SELECT Id, SobjectType, PermissionsRead from Objectperms)

   FROM PermissionSet

   WHERE PermissionsModifyAllData=true

```

versus:

```
   SELECT Id, SObjectType, PermissionsRead, Parent.Id, Parent.Name,

   Parent.PermissionsModifyAllData

   FROM ObjectPermissions

   WHERE SObjectType='Merchandise__c'

```

SEE ALSO:

PermissionSet

FieldPermissions

### ObjectRelatedUrl

Represents a URL slug for a Product or Category page on a B2B Commerce or D2C Commerce LWR site, or a custom object, account, or
contact page on an enhanced LWR Experience Cloud site. This object is available in API version 57.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `undelete()`,
`update()`, `upsert()`

Special Access Rules

Your org must have B2B Commerce or D2C Commerce license enabled for commerce use cases. ObjectRelatedUrl is available for Product2
and ProductCategory records in Commerce, and on custom object, account and contact record pages in enhanced LWR sites.

Fields

**Field** **Details**

```
LanguageCode

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The combined language and locale ISO code, which controls the language of the
object-related URL. The maximum length is 8 characters.


Standard Objects ObjectRelatedUrl

**Field** **Details**

```
Name

ParentId

Scope

UniqueIndex

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the object-related URL. This field isn’t editable.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The ID of the parent record that the `UrlName` refers to. `ParentId` can point
only to Product2, ProductCategory, and custom object, account, and contact record pages.

This field is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Product2, ProductCategory, account, contact, and custom objects

Availability in API versions:

**•** Product2 and ProductCategory in LWR Commerce stores (available in API version 58.0 and
later)

**•** Custom object pages on enhanced LWR sites (available in API version 60.0 and later)

**•** Account and contact pages on enhanced LWR sites (available in API version 61.0 and later)

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Helps ensure uniqueness of the UrlName field across all records with the same
Scope and LanguageCode values. The maximum length is 18 characters.

**Type**
string

**Properties**
Filter, idLookup, Nillable, Sort


### Standard Objects ObjectTerritory2AssignmentRule

**Field** **Details**

**Description**
Ensures uniqueness for each record within your org and creates an index for lookup. This
field isn’t editable.

This field is a calculated field.

```
UrlName

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The URL slug for the record.

Note: When creating a query, for example, `SELECT UrlName From ObjectRelatedUrl WHERE Scope='01t'`,
the `WHERE` condition must use `Id`, `UniqueIndex`, `Scope`, or `ParentId` .

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ObjectRelatedUrlChangeEvent on page 68 (API version 62.0)**
Change events are available for the object.

### ObjectTerritory2AssignmentRule

Represents a territory assignment rule that’s associated with an object, such as Account. ObjectTerritory2AssignmentRuleItem can be
created or deleted if the BooleanFilter field on its corresponding ObjectTerritory2AssignmentRule is `null` . Available if Sales Territories
has been enabled.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Standard users can access this object. If a territory model is in `Active` state, any standard user can view that model, including its
territories, assignment rules, assigned records, and assigned users. Users cannot view territory models in other states (such as `Planning`
or `Archived` ).


Standard Objects ObjectTerritory2AssignmentRule

Fields

**Field Name** **Details**

```
BooleanFilter

DeveloperName

IsActive

Language

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents advanced filter conditions that were specified for the rule in the online
application. For example, “(1 AND 2) OR 3.”

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The unique name of the object in the API. This name can contain only
underscores and alphanumeric characters and must be unique in your
organization. It must begin with a letter, not include spaces, not end with an
underscore, and not contain two consecutive underscores. The field label in the
user interface is `Unique Name` .

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance slows down while Salesforce generates one for
each record.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the rule is active (true) or inactive (false). Via the API, active
rules run automatically when object records are created and edited. The exception
is when the value of the IsExcludedFromRealign field on an object record is `true`,
which prevents record assignment rules from evaluating that record.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


### Standard Objects ObjectTerritory2AssignmentRuleItem

**Field Name** **Details**

**Description**
The language of the label in the user interface.

```
MasterLabel

ObjectType

Territory2ModelId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The user interface label for the territory type.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The object that the rule is defined for. For API version 31, Account only.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the territory model.

### ObjectTerritory2AssignmentRuleItem

A single row of selection criteria for an ObjectTerritory2AssignmentRule object. ObjectTerritory2AssignmentRuleItem can only be created
or deleted if the `BooleanFilter` field on its corresponding ObjectTerritory2AssignmentRule object is a `null` value. Available if
Sales Territories has been enabled.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Standard users can access this object. If a territory model is in `Active` state, any standard user can view that model, including its
territories and assignment rules. For territories in an active model, any standard user can view assigned records and assigned users subject
to your Salesforce sharing settings. Users cannot view territory models in other states (such as `Planning` or `Archived` ).


Standard Objects ObjectTerritory2AssignmentRuleItem

Fields

**Field Name** **Details**

```
Field

Operation

RuleId

SortOrder

Value

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The standard or custom object field that the rule item will operate on.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The criterion to apply for the rule item. For example: _`equals`_, _`notContain`_,
or _`startsWith`_ .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the associated ObjectTerritory2AssignmentRule.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The order in which this row is evaluated in relation to other
ObjectTerritoryAssignmentRuleItem objects for the given
ObjectTerritoryAssignmentRule. This field is required for assignment rule items,
which are used in the Boolean conditions in assignment rule formulas.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The field value or values to evaluate. For example: if the field is `Billing`
`ZIP/Postal Code`, a value might be `94105` .


### Standard Objects ObjectTerritory2Association ObjectTerritory2Association

Represents an association (by assignment) between a territory and an object record such as an account or a lead.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Available after enabling Sales Territories.

Standard and partner users can access this object. If a territory model is in `Active` state, any standard or partner user can view that
model, including its territories and assignment rules. For territories in an active model, any standard or partner user can view assigned
records and assigned users subject to your sharing settings.

If you delete associations, you can query them for up to 12 hours. Keep in mind that deleted associations bypass the recycle bin.

Fields

**Field Name** **Details**

```
AssociationCause

ObjectId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The means by which the record was associated with the territory. User interface
field label is `Method` .

Possible values are:

**•** `Territory2AssignmentRule` —Territory assignment rule association

**•** `Territory2Manual` —Manual association

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the object assigned to the territory.


### Standard Objects ObjectUserTerritory2View

**Field Name** **Details**

This is a polymorphic relationship field.

**Relationship Name**
### Object

**Relationship Type**
Lookup

**Refers To**
Account

Lead

```
SobjectType

Territory2Id

### ObjectUserTerritory2View

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of the object.

Possible values are:

**•** `Account`

**•** `Lead`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the territory that the record is assigned to.

This is a relationship field.

**Relationship Name**
Territory2

**Relationship Type**
Lookup

**Refers To**
Territory2

Represents a user and object, such as an account or lead, assigned to a territory. This object is available in API version 58.0 and later.


Standard Objects ObjectUserTerritory2View

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

To see this object, enable Sales Territories.

Fields

**Field** **Details**

```
ObjectId

RoleInTerritory2

Territory2Id

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Required field for querying ObjectUserTerritory2View.

ID of the object that the territory user is assigned to.

This field is a polymorphic relationship field.

**Relationship Name**
Object

**Refers To**
Account, Lead

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
Role of the user assigned to the territory.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the territory to which the object and user are assigned.

This field is a relationship field.

**Relationship Name**
Territory2

**Refers To**
Territory2


### Standard Objects OmniSupervisorConfig

**Field** **Details**

```
UserId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the user assigned to the territory.

This field is a relationship field.

**Relationship Name**
User

**Refers To**
User

### OmniSupervisorConfig

Represents the Command Center for Service configuration for an assigned group of supervisors. This object is available in API version
41.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve() update()`, `upsert()`

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

As of Spring ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field** **Details**

```
DeveloperName

```

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.


Standard Objects OmniSupervisorConfig

**Field** **Details**

In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance slows down while
Salesforce generates one for each record.

```
IsTimelineHidden

Language

MasterLabel

SkillVisibility

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If set to `true`, hides the agent timeline from the supervisors assigned to this Command
Center for Service configuration. The default value is `false` .

This field is available in API version 53.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The language of this Command Center for Service configuration.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
A unique label name for this Command Center for Service configuration. The name must
begin with a letter. The name can contain alphanumeric characters and underscores. The
name can’t contain spaces, two consecutive underscores, or end with an underscore. The
name appears as Command Center for Service Configuration Name in the UI.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

Determines which work items based on skills are visible to the supervisors assigned to this
Command Center for Service configuration. Possible values are:

**•** `AllSkills`  - Show work items with all skill requirements selected in this Command
Center for Service configuration.


### Standard Objects OmniSupervisorConfigAction

**Field** **Details**

**•** `AnySkill`                   - Show work items with at least one skill requirement selected in this
Command Center for Service configuration.

This field is available in API version 53.0 and later.

### OmniSupervisorConfigAction

Represents the actions available to the supervisors of a Command Center for Service configuration. This object is available in API version
56.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

Only authenticated internal and external users can access this object.

Fields

**Field** **Details**

```
DisplayOrder

OmniSupervisorActionType

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The order in which the action is displayed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
An action that a supervisor can perform.

Possible values are:

**•** `AgentDetails.CustomAction`

**•** `AllAgents.AWSDashboard` —All Agents - View Amazon Real-Time Metrics

**•** `AllAgents.AssignLearning`

**•** `AllAgents.ChangeQueues`


### Standard Objects OmniSupervisorConfigGroup

**Field** **Details**

**•** `AllAgents.ChangeSkills`

**•** `AllAgents.CustomAction`

**•** `AssignedWork.AWSDashboard` —Assigned Work - View Amazon Real-Time
Metrics

**•** `AssignedWork.CustomAction`

**•** `AssignedWorkDetails.CustomAction`

**•** `QueueDetails.CustomAction`

**•** `QueuesBacklog.AWSDashboard` —Queues Backlog - View Amazon Real-Time
Metrics

**•** `QueuesBacklog.CustomAction`

**•** `QueuesBacklog.ManageQueues` —Queues Backlog - Assign Agents to Queues

**•** `SkillDetails.CustomAction`

**•** `SkillsBacklog.AWSDashboard` —Skills Backlog - View Amazon Real-Time
Metrics

**•** `SkillsBacklog.CustomAction`

```
OmniSupervisorConfigId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
A unique identifier for the Command Center for Service configuration.

This field is a relationship field.

**Relationship Name**
### OmniSupervisorConfig

**Relationship Type**
Lookup

**Refers To**
### OmniSupervisorConfig

### OmniSupervisorConfigGroup

Represents the group of reps who are visible to the supervisors of a Command Center for Service configuration. The group, if visible,
appears in the Agents tab of Command Center for Service. This object is available in API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `query()`, `update()`, `retrieve()`


### Standard Objects OmniSupervisorConfigProfile

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

As of Spring ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field** **Details**

```
GroupId

OmniSupervisorConfigId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A unique identifier for the group of reps that’s made visible to the supervisors who are
assigned to the Command Center for Service configuration.

This is a relationship field.

**Relationship Name**
Group

**Relationship Type**
Lookup

**Refers To**
Group

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
A unique identifier for the Command Center for Service configuration.

This is a relationship field.

**Relationship Name**
### OmniSupervisorConfig

**Relationship Type**
Lookup

**Refers To**
### OmniSupervisorConfig

### OmniSupervisorConfigProfile

Represents the supervisor profiles to which a Command Center for Service configuration applies. User-level configurations override
profile-level configurations. This object is available in API version 41.0 and later.


Standard Objects OmniSupervisorConfigProfile

Supported Calls

`create()`, `delete()`, `query()`, `update()`, `retrieve()`

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

As of Spring ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field** **Details**

```
OmniSupervisorConfigId

ProfileId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
A unique identifier for the Command Center for Service configuration.

This is a relationship field.

**Relationship Name**
OmniSupervisorConfig

**Relationship Type**
Lookup

**Refers To**
OmniSupervisorConfig

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A unique identifier for the profile that’s associated with this Command Center for Service
configuration. A profile can be associated with only one Command Center for Service
configuration. This field is unique within your org.

This is a relationship field.

**Relationship Name**
Profile

**Relationship Type**
Lookup

**Refers To**
Profile


### Standard Objects OmniSupervisorConfigQueue OmniSupervisorConfigQueue

Represents the queues that are visible to the supervisors of a Command Center for Service configuration. The queue, if visible, appears
in the Queues Backlog and Assigned Work tabs of Command Center for Service. This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

Only authenticated internal and external users can access this object.

Fields

**Field** **Details**

```
OmniSupervisorConfigId

QueueId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
om

A unique identifier for the Command Center for Service configuration.

This is a relationship field.

**Relationship Name**
### OmniSupervisorConfig

**Relationship Type**
Lookup

**Refers To**
### OmniSupervisorConfig

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A unique identifier for the queue that’s made visible to the supervisors who are assigned to
the Command Center for Service configuration.

This is a relationship field.


### Standard Objects OmniSupervisorConfigSkill

**Field** **Details**

**Relationship Name**
Queue

**Relationship Type**
Lookup

**Refers To**
Group

### OmniSupervisorConfigSkill

Represents the skills that are visible to the supervisors of a Command Center for Service configuration. These skills, if visible, appear in
the Skills Backlog tab of Command Center for Service. This object is available in API version 53.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

Only authenticated internal and external users can access this object.

Fields

**Field** **Details**

```
OmniSupervisorConfigId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
A unique identifier for the Command Center for Service configuration.

This is a relationship field.

**Relationship Name**
### OmniSupervisorConfig

**Relationship Type**
Lookup

**Refers To**
### OmniSupervisorConfig


### Standard Objects OmniSupervisorConfigTab

**Field** **Details**

```
SkillId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A unique identifier for the skill that’s made visible to the supervisors who are assigned to the
Command Center for Service configuration.

This is a relationship field.

**Relationship Name**
Skill

**Relationship Type**
Lookup

**Refers To**
Skill

### OmniSupervisorConfigTab

Represents the visible tabs specified in a Command Center for Service configuration. This object is available in API version 60.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

Only authenticated internal and external users can access this object.

Fields

**Field** **Details**

```
DisplayOrder

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The order in which tabs are displayed in Command Center for Service.


### Standard Objects OmniSupervisorConfigUser

**Field** **Details**

```
OmniSupervisorConfigId

OmniSupervisorTabType

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
A unique identifier for the Command Center for Service configuration.

This is a relationship field.

**Relationship Name**
### OmniSupervisorConfig

**Relationship Type**
Lookup

**Refers To**
### OmniSupervisorConfig

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Tabs shown on the Command Center for Service page. Possible values are:

**•** `Agents`  - the Agents tab

**•** `AssignedWork`  - the Assigned Work tab

**•** `FlexiPageType`  - A custom tab created using Lightning App Builder, with the
`OmniSupervisorPageType` value of the `FlexiPage Type` field

**•** `QueuesBacklog`  - the Queues Backlog tab

**•** `SkillsBacklog`  - the Skills Backlog tab

**•** `Wallboard`  - the Wallboard tab

### OmniSupervisorConfigUser

Represents the users to whom a Command Center for Service configuration applies. User-level configurations override profile-level
configurations. This object is available in API version 41.0 and later.

Supported Calls

`create()`, `delete()`, `query()`, `update()`, `retrieve()`

Special Access Rules

[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)


### Standard Objects OpenActivity

As of Spring ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field** **Details**

```
OmniSupervisorConfigId

UserId

### OpenActivity

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
A unique identifier for the Command Center for Service configuration.

This is a relationship field.

**Relationship Name**
OmniSupervisorConfig

**Relationship Type**
Lookup

**Refers To**
OmniSupervisorConfig

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A unique identifier for the user associated with this Command Center for Service configuration.
A user can be associated with only one Command Center for Service configuration. This field
is unique within your org.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

This read-only object is displayed in a related list of open activities—future events and open tasks—related to an object. It includes
activities for all contacts related to the object. OpenActivity fields for phone calls are only available if your organization uses Salesforce
CRM Call Center.


Standard Objects OpenActivity

Supported Calls

```
   describeSObjects()

```

Fields

**Field** **Details**

```
AccountId

ActivityDate

ActivityDateTime

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the related account, which is determined as follows:

**•** The account associated with the `WhatId`, if it exists; or

**•** The account associated with the `WhoId`, if it exists; otherwise

**•** `null`

This is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates one of the following:

**•** The due date of a task

**•** The date of an event if `IsAllDayEvent` is set to `true`

This field has a time stamp that is always set to midnight in the Universal Time Coordinated
(UTC) time zone. The time stamp doesn’t represent the time of the activity; don’t attempt
to alter it to accommodate time zone differences. Label is `Date` .

**Type**
dateTime

**Properties**
Aggregate, Filter, Nillable, Sort


Standard Objects OpenActivity

**Field** **Details**

**Description**
Contains the event’s due date if the `IsAllDayEvent` flag is set to `false` . The time
portion of this field is always transferred in the Coordinated Universal Time (UTC) time zone.
Translate the time portion to or from a local time zone for the user or the application, as
appropriate. Label is **Due Date Time** .

The value for this field and `StartDateTime` must match, or one of them must be `null` .

```
ActivitySubtype

ActivityType

AlternateDetailId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Provides standard subtypes to facilitate creating and searching for specific activity subtypes.
This field isn’t updateable.

Possible values are:

**•** Task

**•** Email

**•** Call

**•** Event

**•** LinkedIn —Available in API version 56.0 and later.

**•** List Email

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents one of the following values: `Call`, `Email`, `Meeting`, or `Other` . Label is
`Type` . These are default values, and can be changed.

`ActivityType` is the union of `TaskType` and `EventType` . If the same activity appears
in both dynamic picklists, duplicate activities appear.

`TaskType` and `EventType` can each have a `Call` type. Internally, they are distinct from
each other.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of a record the activity is related to which contains more details about the activity.
For example, an activity can be related to an EmailMessage record.


Standard Objects OpenActivity

**Field** **Details**

This is a relationship field.

**Relationship Name**
AlternateDetail

**Relationship Type**
Lookup

**Refers To**
EmailMessage

```
CallDisposition

CallDurationInSeconds

CallObject

CallType

CompletedDateTime

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Represents the result of a given call, for example, “we'll call back,” or “call unsuccessful.” Limit
is 255 characters.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

Duration of the call in seconds.

**Type**
string

**Properties**
Filter, Group,Nillable, Sort

**Description**

Name of a call center. Limit is 255 characters.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The type of call being answered: Inbound, Internal, or Outbound.

**Type**
dateTime


Standard Objects OpenActivity

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the task was saved with a Closed status. This value is always null.

```
ConnectionReceivedId

ConnectionSentId

Description

DurationInMinutes

EndDateTime

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the PartnerNetworkConnection that shared this record with your
organization. This field is available only if your organization has enabled Salesforce to
Salesforce and only in API versions 28.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the PartnerNetworkConnection that your organization shared this record
with. This field is available only if your organization has enabled Salesforce to Salesforce, and
only in API versions 28.0 and later. The value is always `null` . You can use the
PartnerNetworkRecordConnection object to forward records to connections.

**Type**
textarea

**Properties**
Nillable

**Description**
Contains a description of the event or task. Limit is 32 KB.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the duration of the event or task.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects OpenActivity

**Field** **Details**

**Description**
Indicates the end date and time of the event or task. Available in versions 27.0 and later. This
field is optional, depending on the following:

**•** If `IsAllDayEvent` is true, you can supply a value for either `DurationInMinutes`
or `EndDateTime` . Supplying values in both fields is allowed if the values add up to
the same amount of time. If both fields are `null`, the duration defaults to one day.

**•** If `IsAllDayEvent` is false, a value must be supplied for either
`DurationInMinutes` or `EndDateTime` . Supplying values in both fields is allowed
if the values add up to the same amount of time.

```
IsAllDayEvent

IsClosed

IsDeleted

IsHighPriority

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If the value of this field is set to `true`, then the activity is an event spanning a full day, and
the `ActivityDate` defines the date of the event. If the value of this field is set to `false`,
then the activity may be an event spanning less than a full day, or it may be a task. The default
value of this field is `false` . Label is `All-Day Event` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a task is closed ( `true` ) or not closed ( `false` ). The default value of this
field is `false` . This field is set indirectly by setting `Status` on the task—each picklist
value has a corresponding `IsClosed` value. Label is `Closed` .

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the activity has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is `Deleted` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects OpenActivity

**Field** **Details**

**Description**
Indicates a high-priority task. The default value of this field is `false` . This field is derived
from the `Priority` field.

```
IsReminderSet

IsTask

IsVisibleInSelfService

Location

OwnerId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a reminder is set for an activity ( `true` ) or not ( `false` ). The default value
of this field is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If the value of this field is set to `true`, then the activity is a task; if the value is set to `false`,
then the activity is an event. The default value of this field is `false` . Label is `Task` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If the value of this field is set to `true`, then the activity can be viewed in the self-service
portal. The default value of this field is `false` . Label is `Visible in Self-Service` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If the activity is an event, then this field represents the location of the event. If the activity is
a task, then the value is `null` .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the user or group who owns the activity.


Standard Objects OpenActivity

**Field** **Details**

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Calendar, Group, User

```
PrimaryAccountId

PrimaryWhoId

Priority

ReminderDateTime

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Contains the `AccountId` value from the activity record. Available in API versions 30.0 and
later to organizations that use Shared Activities.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Contains the `WhoId` value from the activity record. Available in API versions 30.0 and later
to organizations that have enabled Shared Activities.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Indicates the priority of a task, such as high, normal, or low. The default value of this field is
`Normal` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Represents the time at which a reminder is scheduled to fire if `IsReminderSet` is set to
`true` . If `IsReminderSet` is set to `false`, then either the user has deselected the
reminder checkbox in the user interface or the reminder has already fired at the time indicated
by the value.


Standard Objects OpenActivity

**Field** **Details**

```
Status

Subject

WhatId

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Indicates the current status of a task. The default value of this field is `Not Started` . Each
predefined status field sets a value for `IsClosed` . To obtain picklist values, query the
TaskStatus object.

Possible values are:

**•** Completed

**•** Deferred

**•** In Progress

**•** Not Started

**•** Waiting on someone else

**Type**
combobox

**Properties**
Filter, Nillable, Sort

**Description**
Contains the subject of the task or event.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The `WhatId` represents nonhuman objects such as accounts, opportunities, campaigns,
cases, or custom objects. `WhatId` s are polymorphic. Polymorphic means a `WhatId` is
equivalent to the ID of a related object. The label is `Related To ID` .

This is a polymorphic relationship field.

**Relationship Name**
What

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, AssessmentIndicatorDefinition, AssessmentTask,
AssessmentTaskContentDocument, AssessmentTaskDefinition, AssessmentTaskOrder, Asset,
AssetRelationship, AssignedResource, Award, BoardCertification, BusinessLicense,
BusinessMilestone, BusinessProfile, Campaign, CareBarrier, CareBarrierDeterminant,
CareBarrierType, CareDeterminant, CareDeterminantType, CareDiagnosis,


Standard Objects OpenActivity

**Field** **Details**

CareInterventionType, CareMetricTarget, CareObservation, CareObservationComponent,
CarePgmProvHealthcareProvider, CarePreauth, CarePreauthItem, CareProgram,
CareProgramCampaign, CareProgramEligibilityRule, CareProgramEnrollee,
CareProgramEnrolleeProduct, CareProgramEnrollmentCard, CareProgramGoal,
CareProgramProduct, CareProgramProvider, CareProgramTeamMember,
CareProviderAdverseAction, CareProviderFacilitySpecialty, CareProviderSearchableField,
CareRegisteredDevice, CareRequest, CareRequestDrug, CareRequestExtension,
CareRequestItem, CareSpecialty, CareSpecialtyTaxonomy, CareTaxonomy, Case,
CommSubscriptionConsent, ContactEncounter, ContactEncounterParticipant, ContactRequest,
Contract, CoverageBenefit, CoverageBenefitItem, CreditMemo, DelegatedAccount,
DocumentChecklistItem, EnrollmentEligibilityCriteria, HealthcareFacility,
HealthcareFacilityNetwork, HealthcarePayerNetwork, HealthcarePractitionerFacility,
HealthcareProvider, HealthcareProviderNpi, HealthcareProviderSpecialty,
HealthcareProviderTaxonomy, IdentityDocument, Image, IndividualApplication, Invoice,
ListEmail, Location, MemberPlan, Opportunity, Order, OtherComponentTask, PartyConsent,
PersonLifeEvent, PlanBenefit, PlanBenefitItem, ProcessException, Product2, ProductItem,
ProductRequest, ProductRequestLineItem, ProductTransfer, PurchaserPlan,
ReceivedDocument, ResourceAbsence, ReturnOrder, ReturnOrderLineItem,
ServiceAppointment, ServiceResource, Shift, Shipment, ShipmentItem, Solution, Visit,
VisitedParty, VolunteerProject, WorkOrder, WorkOrderLineItem

```
WhoId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The WhoId represents a human such as a lead or a contact. WhoIds are polymorphic.
Polymorphic means a WhoId is equivalent to a contact’s ID or a lead’s ID. The label is `Name`
`ID` .

If Shared Activities is enabled, the value of this field is the ID of the related lead or primary
contact. If you add, update, or remove the WhoId field, you might encounter problems with
triggers, workflows, and data validation rules that are associated with the record. The label
is `Name ID` .

This is a polymorphic relationship field.

**Relationship Name**
Who

**Relationship Type**
Lookup

**Refers To**
Contact, Lead


### Standard Objects OperatingHours

Usage

**Query activities that are related to an object**

**1.** Optionally, issue a describe call against the object whose activities you want to query, to get a suggestion of the correct SOQL
query to use.

**2.** Issue a SOQL relationship query with a main clause that references the object and an inner clause that references the activity
history. For example:

```
       SELECT

        (SELECT ActivityDate, Description

         FROM OpenActivities)

       FROM Account

       WHERE Name Like 'XYZ%'

```

The user interface enforces sharing rules, filtering out related-list items that a user doesn’t have permission to see.

The following constraints on users who don’t have the “View All Data” permission help prevent performance issues.

**•** In the main clause of the relationship query, you can reference only one record. For example, you can’t filter on all records where
the account name starts with “A.” Instead, you must reference a single account record.

```
       SELECT

        (SELECT ActivityDate, Description

         FROM OpenActivities

         ORDER BY ActivityDate ASC NULLS LAST, LastModifiedDate DESC

         LIMIT 500)

       FROM Account

       WHERE Name = 'Acme'

       LIMIT 1

```

**•** In the inner clause of the query, you can’t use `WHERE` .

**•** In the inner clause of the query, you must specify a limit of 500 or fewer on the number of rows that are returned in the list.

**•** In the inner clause of the query, you must sort on `ActivityDate` in ascending order and `LastModifiedDate` in
descending order. You can optionally display nulls last. For example: `ORDER BY ActivityDate ASC NULLS LAST,`
`LastModifiedDate DESC` .

SEE ALSO:

Task

### OperatingHours

Represents the hours in which a service territory, service resource, or account is available for work. OperatingHours is used by Field
Service, Salesforce Scheduler, Salesforce Meetings, Sales Engagement, and Workforce Engagement. This object is available in API version
38.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects OperatingHours

Fields

**Field Name** **Details**

```
Description

LastReferencedDate

LastViewedDate

Name

OwnerId

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the operating hours. Add any details that aren’t included in
the name.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the operating hours record was last modified. Its label in the user
interface is `Last Modified Date` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the operating hours record was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the operating hours. For example, _`Summer Hours`_, _`Winter`_
_`Hours`_, or _`Peak Season Hours`_ .

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the operating hours record.

This field is available in API version 59.0.

This field is a polymorphic relationship field.


### Standard Objects OperatingHoursHistory

**Field Name** **Details**

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
TimeZone

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The time zone that the operating hours fall within.

By default, only System Administrators can view, create, and assign operating hours.

Service territory members—which are service resources who can work in the territory—automatically use their service territory’s operating
hours. If a resource needs different operating hours than their territory, create separate operating hours for them from the Operating
Hours tab. Then, select the desired hours in the `Operating Hours` lookup field on the service territory member detail page.

To view a service resource’s operating hours for a particular territory, navigate to their Service Territories related list and click the Member
Number for the territory. You reach the service territory member detail page, which lists the member’s operating hours and dates during
which they belong to the territory.

Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**[OperatingHoursChangeEvent (API version 54.0)](https://developer.salesforce.com/docs/atlas.en-us.262.0.api.meta/api/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.

### **OperatingHoursHistory (API version 62.0)**

History is available for tracked fields of the object.

### OperatingHoursHistory

Represents the history of changes made to tracked fields on an operating hours record. This object is available in API version 38.0 and
later.

Supported Calls

`getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)


Standard Objects OperatingHoursHistory

Special Access Rules

Field Service must be enabled in your organization, and field tracking for operating hours fields must be configured.

Fields

**Field Name** **Details**

```
DataType

Field

NewValue

OldValue

TimeSlotId

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
The name of the field that was changed.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The new value of the field that was changed.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The value of the field before it was changed.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the operating hours record being tracked. The history is displayed on the
detail page for this record.


### Standard Objects OperatingHoursHoliday OperatingHoursHoliday

Represents the day or hours for which a service territory and service resources exclusive to the service territory are unavailable in Salesforce
Scheduler. This object is available in API version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Special Access Rules

Salesforce Scheduler must be enabled.

Fields

**Field** **Details**

```
DateAndTime

HolidayId

LastReferencedDate

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
(Read-Only) The date or time for the holiday.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the holiday that’s related to the operating hours indicated in the OperatingHoursId
field.

This is a relationship field.

**Relationship Name**
Holiday

**Relationship Type**
Lookup

**Refers To**
Holiday

**Type**
dateTime


### Standard Objects Opportunity

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the current user last viewed a record related to this object.

```
LastViewedDate

OperatingHoursHolidayNumber

OperatingHoursId

### Opportunity

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this object.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
(Read-Only) An auto-generated number identifying the operating hours holiday.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the operating hours that’s related to the holiday indicated in the HolidayId field.

This is a relationship field.

**Relationship Name**
OperatingHours

**Relationship Type**
Lookup

**Refers To**
OperatingHours

Represents an opportunity, which is a sale or pending deal.


Standard Objects Opportunity

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Field Type**

```
AccountId

ActivityMetricId

ActivityMetricRollupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the account associated with this opportunity.

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
When Einstein Activity Capture with Activity Metrics is enabled, the ID of the related activity
metric.

This field is a relationship field.

**Relationship Name**
ActivityMetric

**Refers To**
ActivityMetric

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
When Einstein Activity Capture with Activity Metrics is enabled, the ID of the related activity
metric rollup.


Standard Objects Opportunity

**Field** **Field Type**

This field is a relationship field.

**Relationship Name**
ActivityMetricRollup

**Refers To**
ActivityMetricRollup

```
AgeInDays

Amount

CampaignId

```

**Type**
int

**Properties**
Aggregate, Filter, Group, Nillable, Sort

**Description**
The number of days since the opportunity was created, calculated by the current date minus
the `created_date` field. This field is available in API version 52.0 and later if you enabled
Pipeline Inspection.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Estimated total sale amount. For opportunities with products, the amount is the sum of the
related products. Any attempt to update this field, if the record has products, will be ignored.
The update call will not be rejected, and other fields will be updated as specified, but the
Amount will be unchanged.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of a related Campaign. This field is defined only for those organizations that have the
campaign feature Campaigns enabled. The User must have read access rights to the
cross-referenced Campaign object in order to create or update that campaign into this field
on the opportunity.

This is a relationship field.

**Relationship Name**
Campaign

**Relationship Type**
Lookup

**Refers To**
Campaign


Standard Objects Opportunity

**Field** **Field Type**

```
CloseDate

ConnectionReceivedId

ConnectionSentId

ContactId

ContractId

```

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Date when the opportunity is expected to close.

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
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the contact associated with this opportunity, set as the primary contact. Read-only field
that is derived from the opportunity contact role, which is created at the same time the
opportunity is created. This field can only be populated when it’s created, and can’t be
updated. To update the value in this field, change the `IsPrimary` flag on the
OpportunityContactRole associated with this opportunity. Available in API version 46.0 and
later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Opportunity

**Field** **Field Type**

**Description**
ID of the contract that’s associated with this opportunity.

This is a relationship field.

**Relationship Name**
Contract

**Relationship Type**
Lookup

**Refers To**
Contract

```
CurrencyIsoCode

Description

ExpectedRevenue

ExportStatus

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for organizations with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

If the organization has multicurrency and a Pricebook2 is specified on the opportunity (that
is, the `Pricebook2Id` field is not blank), then the currency value of this field must match
the currency of the PricebookEntry records that are associated with any opportunity line
items it has.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Text description of the opportunity. Limit: 32,000 characters.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Read-only field that is equal to the product of the opportunity `Amount` field and the
`Probability` . You can’t directly set this field, but you can indirectly set it by setting the
`Amount` or `Probability` fields.

**Type**
picklist

**Properties**
Filter, Restricted picklist, Sort


Standard Objects Opportunity

**Field** **Field Type**

**Description**
Derived field for the record map for Partner Connect. The export status of this opportunity
to the partner’s connected org. To see this field, enable Partner Connect and add the Export
Vendor Records to an Authorized Partner Org user permission to the cosell export user. See
[Set Up Partner Connect as a Vendor in](https://help.salesforce.com/s/articleView?id=slack.prm_pc_setup_vendor_parent.htm&type=5&language=en_US) _Salesforce Help_ . Available in API version 62.0 and later.

```
Fiscal

FiscalQuarter

FiscalYear

ForecastCategory

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If fiscal years are not enabled, the name of the fiscal quarter or period in which the opportunity
`CloseDate` falls. Use YYYY Q format, for example, '2006 1' for first quarter of 2006.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the fiscal quarter. Valid values are 1, 2, 3, or 4.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the fiscal year, for example, 2006.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Restricted picklist field. It is implied, but not directly controlled, by the `StageName` field.
You can override this field to a different value than is implied by the `StageName` value.
The values of this field are fixed enumerated values. The field labels are localized to the
language of the user performing the operation, if localized versions of those labels are
available for that language in the user interface.

In API version 12.0 and later, the value of this field is automatically set based on the value of
the `ForecastCategoryName` and can’t be updated any other way. The field properties
Create, Defaulted on create, Nillable, and Update are not available in version 12.0.

Possible values are:


Standard Objects Opportunity

**Field** **Field Type**

**•** `BestCase`

**•** `Closed`

**•** `Forecast`

**•** `MostLikely`

**•** `Omitted`

**•** `Pipeline`

```
ForecastCategoryName

HasOpenActivity

HasOpportunityLineItem

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The name of the forecast category. It is implied, but not directly controlled, by the
`StageName` field. You can override this field to a different value than is implied by the
`StageName` value. Available in API version 12.0 and later.

Possible values are:

**•** `Best Case`

**•** `Closed`

**•** `Commit`

**•** `Most Likely`

**•** `Omitted`

**•** `Pipeline`

**Type**
boolean

**Properties**
Defaulted on create, Group,

**Description**
Indicates whether an opportunity has an open event or task ( `true` ) or not ( `false` ). Available
in API version 35.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only field that indicates whether the opportunity has associated line items. A value of
`true` means that Opportunity line items have been created for the opportunity. An
opportunity can have opportunity line items only if the opportunity has a price book. The
opportunity line items must correspond to PricebookEntry objects that are listed in the
opportunity Pricebook2. However, you can insert opportunity line items on an opportunity


Standard Objects Opportunity

**Field** **Field Type**

that does not have an associated Pricebook2. For the first opportunity line item that you
insert on an opportunity without a Pricebook2, the API automatically sets the
`Pricebook2Id` field, if the opportunity line item corresponds to a PricebookEntry in an
active Pricebook2 that has a `CurrencyIsoCode` field that matches the
`CurrencyIsoCode` field of the opportunity. If the Pricebook2 is not active or the
`CurrencyIsoCode` fields do not match, then the API returns an error. You can’t update
the `Pricebook2Id` or `PricebookId` fields if opportunity line items exist on the
Opportunity. You must delete the line items before attempting to update the
`PricebookId` field.

```
HasOverdueTask

IqScore

IsClosed

IsDeleted

```

**Type**
boolean

**Properties**
Defaulted on create, Group,

**Description**
Indicates whether an opportunity has an overdue task ( `true` ) or not ( `false` ). Available in
API version 35.0 and later.

**Type**
int

**Properties**
Aggregate, Filter, Group, Nillable, Sort

**Description**
The likelihood, measured on a scale of 1 to 99, that an opportunity will be won. Einstein
Opportunity Scoring must be enabled. Available in API version 41.0 and later. Label is
**Opportunity Score** .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Directly controlled by `StageName` . You can query and filter on this field, but you can’t
directly set it in a create, upsert, or update request. It can only be set via `StageName` . Label
is **Closed** .

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .


Standard Objects Opportunity

**Field** **Field Type**

```
IsExcludedFromTerritory2Filter

IsPriorityRecord

IsPrivate

IsSplit

IsWon

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Used for Filter-Based Opportunity Territory Assignment (Pilot in Spring ’15 / API version 33).
Indicates whether the opportunity is excluded ( _`True`_ ) or included ( _`False`_ ) each time the
APEX filter is executed.

**Type**
boolean

**Properties**
Defaulted on create, Group

**Description**
Shows whether the user has marked the opportunity as important ( _`True`_ ) or not ( _`False`_ ).
The default value is `false` . Available in API version 53.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If _`true`_, only the opportunity owner, users above that role in the hierarchy, and admins can
view the opportunity or query it via the API. When you mark opportunities as private,
opportunity teams, opportunity splits, and sharing are removed. Label is **Private** . The default
value is _`False`_ .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only field that indicates whether credit for the opportunity is split between opportunity
team members. Label is `IsSplit` . This field is available in versions 14.0 and later for
organizations that enabled Opportunity Splits during the pilot period.

This field should not be used. However, it’s documented for the benefit of pilot customers
who find references to `IsSplit` in code.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects Opportunity

**Field** **Field Type**

**Description**
Directly controlled by `StageName` . You can query and filter on this field, but you can’t
directly set the value. It can only be set via `StageName` . Label is **Won** .

```
LastActivityDate

LastActivityInDays

LastAmountChangedHistoryId

LastCloseDateChangedHistoryId

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Value is one of the following, whichever is the most recent:

**•** Due date of the most recent event logged against the record.

**•** Due date of the most recently closed task associated with the record.

**Type**
int

**Properties**
Aggregate, Filter, Group, Nillable, Sort

**Description**
The number of days since the last completed event or task for the record, calculated by the
current date minus the `last_activity` field. If the `last_activity` field is null,
this field is null. This field is available in API version 52.0 and later if you enabled Pipeline
Inspection.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the OpportunityHistory record that contains information about when the opportunity
Amount field was last updated in Winter ’21 or later. Information includes the date and time
of the change and the user who made the change. Available in API version 50.0 and later.

This is a relationship field.

**Relationship Name**
LastAmountChangedHistory

**Relationship Type**
Lookup

**Refers To**
OpportunityHistory

**Type**
reference


Standard Objects Opportunity

**Field** **Field Type**

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the OpportunityHistory record that contains information about when the opportunity
Close Date field was last updated in Winter ’21 or later. Information includes the date and
time of the change and the user who made the change. Available in API version 50.0 and
later.

This is a relationship field.

**Relationship Name**
LastCloseDateChangedHistory

**Relationship Type**
Lookup

**Refers To**
OpportunityHistory

```
LastReferencedDate

LastStageChangeDate

LastStageChangeInDays

```

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
Aggregate, Filter, Nillable, Sort

**Description**
The date of the last change made to the `Stage` field on this opportunity record. This field
is available in API version 52.0 and later.

**Type**
int

**Properties**
Aggregate, Filter, Group, Nillable, Sort

**Description**
The number of days since the last change was made to the `Stage` field on the opportunity
record, calculated by the current date minus the `last_stage_change_date` field. If
the `last_stage_change_date` is null, then this field contains the value for
`AgeInDays` . This field is available in API version 52.0 and later if you enabled Pipeline
Inspection.


Standard Objects Opportunity

**Field** **Field Type**

```
LastViewedDate

LeadSource

Name

NextStep

OwnerId

```

**Type**
datetime

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
Source of this opportunity, such as Advertisement or Trade Show.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. A name for this opportunity. Limit: 120 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of next task in closing opportunity. Limit: 255 characters.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the User who has been assigned to work this opportunity.

If you update this field, the previous owner's access becomes Read Only or the access specified
in your organization-wide default for opportunities, whichever is greater.

If you have set up opportunity teams in your organization, updating this field has different
consequences depending on your version of the API:


Standard Objects Opportunity

**Field** **Field Type**

**•** For API version 12.0 and later, sharing records are kept, as they are for all objects. (All
previous opportunity team members are kept on the opportunity team.)

**•** For API version before 12.0, sharing records are deleted. (All previous opportunity team
members are removed from the opportunity team.)

**•** For API version 16.0 and later, users must have the Transfer Record permission in order
to update (transfer) account ownership using this field.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

```
PartnerAccountId

Pricebook2Id

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the partner account for the partner user that owns this opportunity. Available if Partner
Relationship Management is enabled or if digital experiences is enabled and you have partner
portal licenses.

If you are uploading opportunities using API version 15.0 or earlier, and one of the
opportunities in the batch has a partner user as the owner, the `Partner Account` field
on all opportunities in the batch is set to that partner user’s account regardless of whether
the partner user is the owner. In version 16.0, the `Partner Account` field is set to the
appropriate account for the partner user that owns the opportunity. If the owner of the
opportunity is not a partner user, this field remains empty.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
ID of a related Pricebook2 object. The `Pricebook2Id` field indicates which Pricebook2
applies to this opportunity. The `Pricebook2Id` field is defined only for those organizations
that have products enabled as a feature. You can specify values for only one field
( `Pricebook2Id` or `PricebookId` )—not both fields. For this reason, both fields are
declared nillable.

This is a relationship field.

**Relationship Name**
Pricebook2


Standard Objects Opportunity

**Field** **Field Type**

**Relationship Type**
Lookup

**Refers To**
Pricebook2

```
PricebookId

Probability

PushCount

RecordTypeId

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Nillable, Update

**Description**
Unavailable as of version 3.0. As of version 8.0, the Pricebook object is no longer available.
Use the `Pricebook2Id` field instead, specifying the ID of the Pricebook2 record.

**Type**
percent

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Percentage of estimated confidence in closing the opportunity. It is implied, but not directly
controlled, by the `StageName` field. You can override this field to a different value than
what is implied by the `StageName` .

If you're changing the `Probability` field through the API using a partner WSDL call, or
an Apex `before` trigger, and the value may have several decimal places, we recommend
rounding the value to a whole number. For example, the following Apex in a `before`
trigger uses the `round` method to change the field value: `o.probability =`

```
  o.probability.round();

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times an opportunity’s close date has been pushed out by one calendar
month. For example, moving a close date from April to May counts as one push, but moving
from April 1 to April 30 doesn't count. The total is not decreased when the close date is
moved in. Available in API version 53.0 and later.

**Type**
reference

**Properties**
Create, Filter, Nillable, Update


Standard Objects Opportunity

**Field** **Field Type**

**Description**
ID of the record type assigned to this object.

```
StageName

SyncedQuoteID

Territory2Id

TotalOpportunityQuantity

```

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Current stage of this record. The `StageName` field controls several other fields
on an opportunity. Each of the fields can be directly set or implied by changing the
`StageName` field. In addition, the `StageName` field is a picklist, so it has additional
members in the returned describeSObjectResult to indicate how it affects the other fields.
To obtain the stage name values in the picklist, query the OpportunityStage object. If the
`StageName` is updated, then the `ForecastCategoryName`, `IsClosed`, `IsWon`,
and `Probability` are automatically updated based on the stage-category mapping.

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
Read only in an Apex trigger. The ID of the Quote that syncs with the opportunity. Setting
this field lets you start and stop syncing between the opportunity and a quote. The ID has
to be for a quote that is a child of the opportunity.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the territory that is assigned to the opportunity. Available only if Enterprise Territory
Management has been enabled for your organization. Users who have full access to an
opportunity’s account can assign any territory from the active model to the opportunity.
Users who do _not_ can assign only a territory that is also assigned to the opportunity’s account.
The same restriction applies to territory assignments made via Apex in system mode.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Number of items included in this opportunity. Used in quantity-based forecasting.


Standard Objects Opportunity

**Field** **Field Type**

```
Type

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Type of opportunity. For example, Existing Business or New Business. Label is **Opportunity**
**Type** .

Note: When importing opportunity data, users need the Set Audit Fields upon Record Creation permission to assign values to
audit fields such as `CreatedDate` . Audit fields are automatically updated during API operations unless you set these fields
yourself.

Usage

Use the Opportunity object to manage information about a sale or pending deal. You can also sync this object with a child Quote. To
update an Opportunity, your client application needs Edit permission on opportunities. You can create, update, delete, and query
Attachment records associated with an opportunity via the API. To split credit for an opportunity among multiple opportunity team
members, use the OpportunitySplit object.

Client applications can also create or update opportunity objects by converting a Lead with `convertLead()` .

Note: On opportunities and opportunity products, the workflow rules, validation rules, and Apex triggers fire when an update to
a child opportunity product or schedule causes an update to the parent record. This means your custom application logic is
enforced when there are updates to the parent record, ensuring higher data quality and compliance with your organization’s
business policies.

Sample Code—Java

This code starts the sync between an object and a child quote.

```
public void startQuoteSync() {

      Opportunity opp = new Opportunity();

      opp.setId(new ID("006D000000CpOSy"));

      opp.setSyncedQuoteId(new ID("0Q0D000000002OZ"));

  // Invoke the update call and save the results

  try {

    SaveResult[] saveResults = binding.update(new SObject[] {opp});

    // check results and do more processing after the update call ...

  }

  catch (Exception ex) {

    System.out.println("An unexpected error has occurred." + ex.getMessage());

    return;

 }

}

```


Standard Objects Opportunity

This code stops the sync between an object and a child quote.

```
   public void stopQuoteSync() {

         Opportunity opp = new Opportunity();

         opp.setId(new ID("006D000000CpOSy"));

         opp.setFieldsToNull(new String[] {"SyncedQuoteId"} );

     // Invoke the update call and save the results

     try {

       SaveResult[] saveResults = binding.update(new SObject[] {opp});

       // check results and do more processing after the update call ...

     }

     catch (Exception ex) {

       System.out.println("An unexpected error has occurred." + ex.getMessage());

       return;

    }

   }

```

Associated Objects

This object has these associated objects. Unless noted, they are available in the same API version as this object.

**[OpportunityChangeEvent (API version 44.0)](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.

**[OpportunityFeed (API version 18.0)](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**
Feed tracking is available for the object.

**OpportunityHistory**

History is available for tracked fields of the object.

**OpportunityOwnerSharingRule**

Sharing rules are available for the object.

**OpportunityShare**

Sharing is available for the object.

Additional Considerations

If you are using `before` triggers to set `Stage` and `Forecast Category` for an opportunity record, the behavior is as follows:

**•** If you set `Stage` and `Forecast Category`, the opportunity record contains those exact values.

**•** If you set `Stage` but not `Forecast Category`, the `Forecast Category` value on the opportunity record defaults to
the one associated with trigger `Stage` .

**•** If you reset `Stage` to a value specified in an API call or incoming from the user interface, the `Forecast Category` value
should also come from the API call or user interface. If no value for `Forecast Category` is specified and the incoming `Stage`
is different than the trigger `Stage`, the `Forecast Category` defaults to the one associated with trigger `Stage` . If the trigger
`Stage` and incoming `Stage` are the same, the `Forecast Category` is not defaulted.

If you are cloning an opportunity with products, the following events occur in order:

Note: If errors occur on an opportunity product, you must return to the opportunity and fix the errors before cloning.

If any opportunity products contain unique custom fields, you must null them out before cloning the opportunity.

**•** [The parent opportunity is saved according to the order of execution.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_triggers_order_of_execution.htm)


### Standard Objects OpportunityCompetitor

**•** [The opportunity products are saved according to the order of execution.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_triggers_order_of_execution.htm)

SEE ALSO:

### OpportunityCompetitor

OpportunityHistory

OpportunityLineItem

OpportunityLineItemSchedule

OpportunityFieldHistory

Quote

QuoteLineItem

PartnerNetworkConnection

### OpportunityCompetitor

Represents a competitor on an Opportunity.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Fields

**Field** **Details**

```
CompetitorName

IsDeleted

OpportunityId

```

**Type**
combobox

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Name of the competitor.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

**Type**
reference


### Standard Objects OpportunityContactRole

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the associated Opportunity.

This is a relationship field.

**Relationship Name**
### Opportunity

**Relationship Type**
Lookup

**Refers To**
### Opportunity

```
 Strengths

 Weaknesses

```

Usage

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the competitor’s strengths. Limit: 1,000 characters.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the competitor’s weaknesses. Limit: 1,000 characters.

Use this object to manage competitors on an Opportunity, associating multiple competitors on a opportunity and specifying the strengths
and weaknesses of each competitor.

SEE ALSO:

### Opportunity OpportunityContactRole

Represents the role that a Contact plays on an Opportunity.


Standard Objects OpportunityContactRole

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ContactId

CurrencyIsoCode

Division

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of an associated Contact. The API applies user access rights to the associated Opportunity
for this object, but not to the associated Contact. The API may return rows from a query on
this object that include this field’s values for contacts to which the user does not have
sufficient access rights. It may also return values for this field for contacts that have been
deleted. In either case, the client must perform a query on the contact table for this field’s
value to determine whether the Contact is accessible to the user and has not been deleted.

This is a relationship field.

**Relationship Name**
Contact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
any currency allowed by the org. This field is available in API version 47.0.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
A logical segment of your organization's data. For example, if your company is organized
into different business units, you could create a division for each business unit, such as “North


Standard Objects OpportunityContactRole

**Field** **Details**

America,” “Healthcare,” or “Consulting.” Available only if the organization has the Division
permission enabled.

```
IsDeleted

IsPrimary

OpportunityId

Role

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the record has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
The `IsDeleted` flag is usable only when the parent record is deleted to the recycle bin,
and not when the `OpportunityContactRole` record is deleted directly. Label is
**Deleted** .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the associated Contact plays the primary role on the Opportunity ( `true` )
or not ( `false` ). Each Opportunity has only one primary contact. Label is **Primary** .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of an associated Opportunity. This field is non-nullable, and it cannot be updated.
You must provide a value for this field when creating new records. You can’t change it after
it has been created.

This is a relationship field.

**Relationship Name**
Opportunity

**Relationship Type**
Lookup

**Refers To**
Opportunity

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects OpportunityContactRoleSuggestionInsight

**Field** **Details**

**Description**
Name of the role played by the associated Contact on the Opportunity, such as Business
User or Decision Maker.

Usage

Use the Opportunity Contact Role object to manage information about contacts and roles related to opportunities. Records of this type
appear in the user interface in the Opportunity Contact Role related list and on the Opportunity detail page.

Although allowed, we do not recommend that you create multiple relationships between the same Opportunity and a Contact.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**OpportunityContactRoleChangeEvent (API version 45.0)**
Change events are available for the object.

SEE ALSO:

Overview of Salesforce Objects and Fields

### OpportunityContactRoleSuggestionInsight

Represents a suggestion for a new opportunity contact role. Available in API versions 45.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getDeleted()`, `query()`, `retrieve()`

Special Access Rules

To add or decline opportunity contact role suggestions, users need a Sales Cloud Einstein license, edit access on opportunities, and read
or edit access on contacts. As of the Spring ’20 release, Pardot and Sales Engagement users no longer have access to this object.

Fields

**Field Name** **Details**

```
ContactId

```

**Type**
reference

**Properties**
Filter, Group, Sort


Standard Objects OpportunityContactRoleSuggestionInsight

**Field Name** **Details**

**Description**
The ID of the related contact record.

```
CreatedRecordId

CurrencyIsoCode

Division

LastOperationUserId

LastReferencedDate

LastViewedDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the created opportunity contact role record.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The division of the suggested opportunity contact role.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who last performed a related operation.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last interacted with this record, directly or
indirectly.

**Type**
dateTime


Standard Objects OpportunityContactRoleSuggestionInsight

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, it's possible that the user only accessed this record or list view
( `LastReferencedDate` ), but not viewed it.

```
OpportunityId

RationaleLabel

Role

Status

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related opportunity.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The reason why this is a suggested opportunity contact role.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The role of the suggested opportunity contact role.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the suggested contact. Possible values include:

**•** New

**•** Pending

**•** Added

**•** Declined


### Standard Objects OpportunityFieldHistory

Usage

This object is read-only and isn’t supported in workflows, triggers, or process builder.

### OpportunityFieldHistory

Represents the history of changes to the values in the fields of an opportunity. This object is available in versions 13.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Fields

**Field** **Details**

```
DataType

Field

IsDeleted

OpportunityId

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
The name of the field that was changed.

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
Filter, Group, Sort


### Standard Objects OpportunityHistory

**Field** **Details**

**Description**
ID of the Opportunity. Label is **Opportunity ID** .

This is a relationship field.

**Relationship Name**
### Opportunity

**Relationship Type**
Lookup

**Refers To**
### Opportunity

```
 NewValue

 OldValue

```

Usage

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The new value of the field that was changed.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The latest value of the field before it was changed.

Use this object to identify changes to any fields on an Opportunity. The OpportunityHistory object represents the history of a change to
the `Amount`, `Probability`, `Stage`, or `Close Date` fields of an Opportunity.

This object respects field level security on the parent object.

SEE ALSO:

### Opportunity OpportunityHistory

Represents the stage history of an opportunity.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects OpportunityHistory

Fields

**Field** **Details**

```
Amount

CloseDate

ExpectedRevenue

ForecastCategory

IsDeleted

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Estimated total sale amount.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Date when the opportunity is expected to close.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Calculated revenue based on the `Amount` and `Probability` fields.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Category that determines the column in which an opportunity is totaled in a forecast. Label
is **To ForecastCategory** .

**•** `BestCase`

**•** `Closed`

**•** `Forecast`

**•** `MostLikely`

**•** `Omitted`

**•** `Pipeline`

**Type**
boolean

**Properties**
Defaulted on create, Filter


Standard Objects OpportunityHistory

**Field** **Details**

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

```
OpportunityId

PrevAmount

PrevCloseDate

Probability

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the associated Opportunity.

This is a relationship field.

**Relationship Name**
Opportunity

**Relationship Type**
Lookup

**Refers To**
Opportunity

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The value in the opportunity’s Amount field before the update of the opportunity. In
OpportunityHistory records created before Winter ’21, the value is null.Available in API version
50.0 and later.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The value in the opportunity’s Close Date field before the update of the opportunity. In
OpportunityHistory records created before Winter ’21, the value is null.Available in API version
50.0 and later.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
Percentage of estimated confidence in closing the opportunity.


### Standard Objects OpportunityInsight

**Field** **Details**

```
StageName

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Sort

**Description**
Name of the current stage of the opportunity (for example, Prospect or Proposal).

This object represents the history of a change to the `Amount`, `Probability`, `Stage`, or `Close Date` fields of an Opportunity.
The OpportunityFieldHistory object represents the history of a change to any of the fields of an Opportunity. To obtain information about
how a particular opportunity is progressing, query the OpportunityHistory records associated with a given Opportunity. Please note that
if an opportunity's `Amount`, `Probability`, `Stage`, or `Close Date` fields have not changed, nothing will be returned in the
OpportunityHistory objects. In this case, query the OpportunityFieldHistory records associated with a given Opportunity to get more
information about changes to the opportunity.

This object is read-only. The system generates a new record whenever a user or client application changes the value of any of the above
fields; the then-current values of all of these major fields are saved in the newly-generated object.

This object respects field-level security on the parent object.

Note: The record is automatically deleted if its parent Opportunity is deleted.

SEE ALSO:

### Opportunity OpportunityInsight

Represents an individual insight (deal prediction, follow-up reminder, or key moment) related to an opportunity record.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `query()`, `retrieve()`

Special Access Rules

To see an insight related to a specific opportunity, users need a Sales Cloud Einstein license and access to the opportunity record. As of
the Spring ’20 release, Pardot and Sales Engagement users no longer have access to this object.


Standard Objects OpportunityInsight

Fields

**Field Name** **Details**

```
ActualHeardWithinDays

CloseDate

CompetitorName

ContactName

ContactTitle

CurrencyIsoCode

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of days it has been since a prospect has responded for insights of
type `Prospect has not responded` and `No communication` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The close date of the related opportunity for insights of type `Opportunity`
`is overdue` and `Opportunity is unlikely to close in`
`time` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field has been deprecated as of API version 45.0.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is not in use as of API version 46.0.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is not in use as of API version 46.0.

**Type**
picklist


Standard Objects OpportunityInsight

**Field Name** **Details**

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

```
Division

ExpectedHeardWithinDays

LastHeard

LastReferencedDate

LastViewedDate

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The division of the related record.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The expected number of days it takes to hear back from a prospect for insights
of type `Prospect has not responded` and `No communication` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the related prospect was last heard from for insights of type
`Prospect has not responded` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last interacted with this record, directly or
indirectly.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects OpportunityInsight

**Field Name** **Details**

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, it's possible that the user only accessed this record or list view
( `LastReferencedDate` ), but not viewed it.

```
OpportunityId

Rationale

Reason

TaskDue

Title

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related opportunity record.

**Type**
string

**Properties**
Filter, Group, Nillable

**Description**
The explanation for an insight, providing more background information and
details that are specific to the org.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The reason why a specific insight type is appearing. Relevant to the following
insights:

**•** Opportunity is unlikely to close in time

**•** Opportunity slowing

**•** Opportunity boosting

**•** Time-consuming opportunity

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that a task associated with the related opportunity record is due.

**Type**
string


Standard Objects OpportunityInsight

**Field Name** **Details**

**Properties**
Filter, Group, Nillable

**Description**
The title of the insight.

```
TrendType

Type

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The trend type of the insight. Possible values include:

**•** Negative

**•** Positive

**•** Informational

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of insight. Possible values include:

**•** Opportunity is unlikely to close in time

**•** Prospect has not responded

**•** Opportunity slowing

**•** Opportunity boosting

**•** Time-consuming opportunity

**•** No communication

**•** Re-engaged opportunity

**•** Opportunity has an overdue task

**•** Opportunity is overdue

**•** Opportunity has no open activity

**•** Unusual opportunity amount

This object is read-only and isn’t supported in workflows, triggers, or process builder.


### Standard Objects OpportunityLineItem OpportunityLineItem

Represents an opportunity line item, which is a member of the list of Product2 products associated with an Opportunity.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

The user must have the “Edit” permission on Opportunity records to create or update opportunity line items on an opportunity.

Fields

**Field** **Details**

```
CanUseQuantitySchedule

CanUseRevenueSchedule

ConnectionReceivedId

ConnectionSentId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the opportunity product can have a quantity schedule ( `true` ) or not
( `false` ). This field is read-only.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the opportunity product can have a revenue schedule ( `true` ) or not
( `false` ). This field is read-only.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the PartnerNetworkConnection that shared this record with your organization. This
field is available if you enabled Salesforce to Salesforce.

**Type**
reference


Standard Objects OpportunityLineItem

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the PartnerNetworkConnection that you shared this record with. This field is available
if you enabled Salesforce to Salesforce. This field is supported using API versions earlier than
15.0. In all other API versions, this field’s value is null. You can use the new
PartnerNetworkRecordConnection object to forward records to connections.

```
CurrencyIsoCode

Description

Discount

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only for organizations with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

If the organization has multicurrency enabled, and a Pricebook2 isn’tspecified on the parent
opportunity (that is, the `Pricebook2Id` field is blank on the opportunity referenced by
this object’s `OpportunityId` ), then the value of this field must match the currency of
the `CurrencyIsoCode` field on the PricebookEntry records that are associated with this
object.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Text description of the opportunity line item. Limit: 255 characters.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Discount for the product as a percentage.

When updating these records:

**•** If you specify `Discount` without specifying `TotalPrice`, the `TotalPrice` is
adjusted to accommodate the new `Discount` value, and the `UnitPrice` is held
constant.

**•** If you specify both `Discount` and `Quantity`, you must also specify either
`TotalPrice` or `UnitPrice` so the system knows which one to automatically
adjust.


Standard Objects OpportunityLineItem

**Field** **Details**

```
HasQuantitySchedule

HasRevenueSchedule

HasSchedule

LastReferencedDate

LastViewedDate

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only. Indicates whether a quantity schedule has been created for this object ( `true` )
or not ( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a revenue schedule has been created for this object ( `true` ) or not
( `false` ).

If this object has a revenue schedule, the `Quantity` and `TotalPrice` fields can’t be
updated. In addition, the `Quantity` field can’t be updated if this object has a quantity
schedule. Update requests aren’t rejected but the updated values are ignored.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If either `HasQuantitySchedule` or `HasRevenueSchedule` is `true`, this field is
also `true` .

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record. Available
in API version 50.0 and later.

**Type**
datetime

**Properties**
Filter, Nillable, Sort


Standard Objects OpportunityLineItem

**Field** **Details**

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed. Available in
API version 50.0 and later.

```
ListPrice

Name

OpportunityId

PricebookEntryId

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Corresponds to the `UnitPrice` on the PricebookEntry that is associated with this line
item, which can be in the standard price book or a custom price book. A client application
can use this information to show whether the unit price (or sales price) of the line item differs
from the price book entry list price.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The opportunity line item name (known as “Opportunity Product” in the user interface). This
read-only field is available in API version 30.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the associated Opportunity.

This is a relationship field.

**Relationship Name**
Opportunity

**Relationship Type**
Lookup

**Refers To**
Opportunity

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort


Standard Objects OpportunityLineItem

**Field** **Details**

**Description**
Required. ID of the associated PricebookEntry. Exists only for those organizations that have
Products enabled as a feature. In API versions 1.0 and 2.0, you can specify values for either
this field or `ProductId`, but not both. For this reason, both fields are declared nillable. In
API version 3.0 and later, you must specify values for this field instead of `ProductId` .

This is a relationship field.

**Relationship Name**
PricebookEntry

**Relationship Type**
Lookup

**Refers To**
PricebookEntry

```
ProductId

Product2Id

ProductCode

```

**Type**
reference

**Properties**
Create, Filter, Nillable

**Description**
ID of the related Product record. This field is unavailable as of version 3.0 and is only provided
for backward compatibility. The Product object is unavailable beginning with version 8.0.
Use the `PricebookEntryId` field instead, specifying the ID of the PricebookEntry record.

This is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the related Product2 record. This is a read-only field available in API version 30.0
and later.

Use the `PricebookEntryId` field instead, specifying the ID of the PricebookEntry record.

**Type**
string


Standard Objects OpportunityLineItem

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
This read-only field is available in API version 30.0 and later. It references the value in the
ProductCode field of the related Product2 record.

```
Quantity

RecalculateTotalPrice

ServiceDate

```

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
Read-only if this record has a quantity schedule, a revenue schedule, or both a quantity and
a revenue schedule.

When updating these records:

**•** If you specify `Quantity` without specifying the `UnitPrice`, the `UnitPrice`
value is adjusted to accommodate the new `Quantity` value, and the `TotalPrice`
is held constant.

**•** If you specify both `Discount` and Quantity, you must also specify either `TotalPrice`
or `UnitPrice` so the system can determine which one to automatically adjust.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Changes behavior of OpportunityLineItem calculations when a line item has child schedule
rows for the `Quantity` value. When enabled, if the rollup quantity changes, then the
quantity rollup value is multiplied against the sales price to change the total price. Product2
flag must be set to true.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date when the product revenue will be recognized and the product quantity will be shipped.

**•** Opportunity Close Date— `ServiceDate` is ignored.

**•** Product Date— `ServiceDate` is used if not `null` .

**•** Schedule Date— `ServiceDate` is used if not `null` and there are no revenue
schedules present for this line item, that is, there are no OpportunityLineItemSchedule
records with a field `Type` value of Revenue that are children of this record.


Standard Objects OpportunityLineItem

**Field** **Details**

```
SortOrder

Subtotal

TotalPrice

UnitPrice

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number indicating the sort order selected by the user. Client applications can use this to
match the sort order in Salesforce.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Difference between standard and discounted pricing. Converted currency amounts when
the opportunity's currency is different from the user's currency.

**Type**
currency

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
This field is available only for backward compatibility. It represents the total price of the
OpportunityLineItem.

If you don’t specify `UnitPrice`, this field is required. If you specify `Discount` and
`Quantity`, this field or `UnitPrice` is required. When updating these records, you can
change either this value or the `UnitPrice`, but not both at the same time.

This field is nillable, but you can’t set both `TotalPrice` and `UnitPrice` to null in the
same update request. To insert the `TotalPrice` via the API (given only a unit price and
the quantity), calculate this field as the unit price multiplied by the quantity. This field is
read-only if the opportunity line item has a revenue schedule. If the opportunity line item
doesn’t have a schedule or only has a quantity schedule, this field can be updated.

**Type**
currency

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
The unit price for the opportunity line item. In the Salesforce user interface, this field’s value
is calculated by dividing the total price of the opportunity line item by the quantity listed for
that line item. Label is **Sales Price** .

This field or `TotalPrice` is required. You can’t specify both.

If you specify `Discount` and `Quantity`, this field or `TotalPrice` is required.


Standard Objects OpportunityLineItem

Usage

An Opportunity can have associated OpportunityLineItem records only if the Opportunity has a Pricebook2. An OpportunityLineItem
must correspond to a Product2 that is listed in the opportunity's Pricebook2. For information about inserting OpportunityLineItem for
an opportunity that doesn’t have an associated Pricebook2 or any existing line items, see Effects on Opportunities.

This object is defined only for orgs with products enabled as a feature. If the products feature isn’t enabled, this object doesn’t appear
in the `describeGlobal()` call, and you can’t use `describeSObjects()` or query the OpportunityLineItem object.

[For a visual diagram of the relationships between OpportunityLineItem and other objects, see the Product & Price Book diagram.](https://developer.salesforce.com/docs/platform/data-models/guide/product-price-book.html)

Note:

**•** If the multicurrency option is enabled, the `CurrencyIsoCode` field is present. It can’t be modified, and is always set to
the value of the `CurrencyIsoCode` of the parent Opportunity.

**•** If customizable product schedules are enabled, you can use custom fields in default schedules and customize their layout. But
if you’ve applied validation rules or Apex triggers, they’re bypassed when they’re first inserted.

Effects on Opportunities

Opportunities with associated OpportunityLineItem records are affected in the following ways:

**•** Creating an OpportunityLineItem increments the Opportunity `Amount` value by the `TotalPrice` of the OpportunityLineItem.
Additionally, inserting an OpportunityLineItem increments the `ExpectedRevenue` on the opportunity by the `TotalPrice`
times the opportunity `Probability` .

**•** The Opportunity `Amount` becomes a read-only field when the opportunity has line items. The API ignores any attempt to update
this field on an opportunity with line items. Update requests aren’t rejected, but the updated value is ignored.

**•** You can’t update the `PricebookId` field or the `CurrencyIsoCode` field on the opportunity if line items exist. The API rejects
any attempt to update these fields on an opportunity with line items.

**•** When you create or update an OpportunityLineItem, the API verifies that the line item corresponds to a PricebookEntry in the
Pricebook2 associated with the opportunity.

**–** If the opportunity has an associated active or inactive Pricebook2, the OpportunityLineItem is created or updated.

**–** If the opportunity doesn’t have an associated Pricebook2, but the OpportunityLineItem corresponds to a PricebookEntry in an
active Pricebook2 where the PricebookEntry has a `CurrencyIsoCode` value that matches the `CurrencyIsoCode`
value of the opportunity, the API automatically sets this PriceBook2 on the opportunity.

**–** If the opportunity doesn’t have an associated Pricebook2, but the line item corresponds to a PricebookEntry in a Pricebook2 that
isn’t active or that has a `CurrencyIsoCode` value that does not match the `CurrencyIsoCode` value of the opportunity,
an error is returned.

**•** The Opportunity `HasOpportunityLineItem` field is set to `true` when an OpportunityLineItem is inserted for that Opportunity.

**•** When OpportunityLineItem records are directly deleted, they aren’t sent to the recycle bin and can’t be undeleted. The
`getDeleted()` call shows deleted OpportunityLineItem records until they’re purged, which is usually within the same day or
the next day.

**•** In Lightning, the `ListPrice`, `Name`, and `ProductCode` fields aren’t populated before insert because their values are computed
after the OpportunityLineItem.Product2Id value is saved. To access a value from these fields, use an After Insert trigger.


### Standard Objects OpportunityLineItemSchedule

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[OpportunityLineItemChangeEvent (API version 60.0)](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.

SEE ALSO:

### OpportunityLineItemSchedule OpportunityLineItemSchedule Represents information about the quantity, revenue distribution, and delivery dates for a particular OpportunityLineItem .

In API version 38.0 and later, when an OpportunityLineItem record is created for a product with a previously established schedule, an
### OpportunityLineItemSchedule record is also created.

In API version 46.0 and later, this object supports custom fields, validation rules, and Apex triggers. Deleting a schedule now also invokes
delete triggers. If customizable product schedules are enabled, you can use custom fields in default schedules and customize their layout.
But if you’ve applied validation rules or Apex triggers, they’re bypassed when they’re first inserted.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Fields

**Field** **Details**

```
CurrencyIsoCode

Description

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Nillable, Restricted picklist, Update

**Description**
Available only for organizations with the multicurrency feature enabled.
Contains the ISO code for any currency allowed by the organization. This field
is available in version 10.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Text description of the opportunity line item schedule. Limit: 80 characters.
Label is **Comments** .


Standard Objects OpportunityLineItemSchedule

**Field** **Details**

```
OpportunityLineItemId

Quantity

Revenue

ScheduleDate

Type

```

**Type**
reference

**Properties**
Create, Filter

**Description**
Required. ID of the associated `OpportunityLineItem` .

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Required. The total number of units to be scheduled in a quantity schedule.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The revenue that should be recognized, or the quantity that should be
shipped, or both - depending upon the value of `Type` .

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The date the associated `OpportunityLineItem` is to be
scheduled for an event: delivery, shipping, or any other date you wish to track.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of the schedule. Required when inserting an
OpportunityLineItemSchedule. Valid values include `Quantity`, `Revenue`,
or `Both` .


Standard Objects OpportunityLineItemSchedule

Allowed Type Field Values

The allowed `Type` values for an `OpportunityLineItemSchedule` depend on the product-level schedule preferences and
whether the line item has any existing schedules. The following criteria must be met:

**•** The Product2 on which the `OpportunityLineItem` is based must have the appropriate `CanUseRevenueSchedule` or
`CanUseQuantitySchedule` fields (or both) set to `true` .

**•** When you create a schedule for a line item that does not have any existing schedules, you can specify any valid value.

**•** If you create a schedule for a line item that already has existing schedules, the new schedule must be consistent with the existing
schedules. The following matrix outlines the allowable values:

**Value of HasRevenueSchedule** **Value of HasQuantitySchedule** **Allowable Type Values**
**on line item** **on line item**

false false `Revenue`, `Quantity`, both

false true `Quantity`

true false `Revenue`

true true both

Allowed Quantity and Revenue Field Values

The allowable `Quantity` and `Revenue` field values depend on the value of the `Type` field:

**Type Value** **Allowable Quantity Value** **Allowable Revenue Value**

`Revenue` Null Non-null

`Quantity` Non-null Null

both Non-null Non-null

The `Quantity` and `Revenue` fields have the following restrictions when this object is updated:

**•** For a schedule of `Type Quantity`, you can’t update a null `Revenue` value to non-null. Likewise for a schedule of `Type`
`Revenue`, you can’t update a null `Quantity` value to non-null.

**•** You can’t null out the `Quantity` field for a schedule of `Type Quantity` . Likewise you can’t null out the `Revenue` field for
a schedule of `Type Revenue` .

**•** You can’t null out either the `Revenue` or `Quantity` fields for a schedule of type `Both` .

Usage

`OpportunityLineItemSchedule` supports two types of schedules:

**•** `Quantity` schedules

**•** `Revenue` schedules

The user must have edit access rights on the Opportunity in order to create or update line item schedules on that opportunity.


### Standard Objects OpportunityLineItemSplit

Products and Schedules Must Be Enabled

The `OpportunityLineItemSchedule` object is defined only for those organizations that have the products and schedules
features enabled. If the organization does not have the products and schedules features, the `OpportunityLineItemSchedule`
object is not returned in a describe, and you can't describe or query `OpportunityLineItemSchedule` records.

Effects on Opportunities and Opportunity Line Items

`OpportunityLineItemSchedule` records affect opportunities and opportunity line items in the following ways:

**•** Inserting an `OpportunityLineItemSchedule` of `Type` “Revenue” or “Quantity” increments the `TotalPrice` field on
### the OpportunityLineItem by the OpportunityLineItemSchedule Revenue amount. Inserting an

`OpportunityLineItemSchedule` of `Type Quantity` or `Both` increments the `Quantity` field on the
### OpportunityLineItem by the OpportunityLineItemSchedule Quantity amount.

**•** Creating an OpportunityLineItemSchedule record affects the original opportunity:

**1.** The Opportunity `Amount` is incremented the by `OpportunityLineItemSchedule` revenue amount

**2.** The Opportunity `ExpectedRevenue` is incremented by the line item schedule amount multiplied by the Opportunity

```
      Probability

### • Deleting an OpportunityLineItemSchedule has a similar effect on the related OpportunityLineItem and
```

Opportunity. Deleting an `OpportunityLineItemSchedule` decrements the `OpportunityLineItemTotalPrice`
by the deleted `OpportunityLineItemSchedule Quantity` or `Revenue` amount. The Opportunity `Amount` is also
decremented by the `OpportunityLineItemSchedule Quantity` or `Revenue` amount, and the Opportunity
`ExpectedRevenue` is reduced by `OpportunityLineItemSchedule Quantity` or `Revenue` amount multiplied
by the Opportunity `Probability` .

Deleting an Opportunity Line Item Schedule

Deleting the last remaining schedule will set the corresponding `HasQuantitySchedule` or `HasRevenueSchedule` flags (or
both) to `false` on the parent line item.

SEE ALSO:

### OpportunityLineItem

Product2

### OpportunityLineItemSplit

Represents information about an opportunity product split, including percentages, amounts, and owner. This object is available in API
version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`


Standard Objects OpportunityLineItemSplit

Special Access Rules

Before creating OpportunityLineItemSplit records, enable Team Selling, set up opportunity splits, and enable product splits on at least
one opportunity split type in Setup.

Fields

**Field** **Details**

```
ArchivedTerritoryName

CurrencyIsoCode

OpportunityLineItemId

```

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the associated territory that’s on an archived territory model. If the
OpportunityLineItemSplit isn’t associated with a territory on an archived territory model, the
field value is null. This field is available in API version 62.0 and later.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only for organizations with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

If the organization has multicurrency enabled, and a Pricebook2 is specified on the opportunity
(that is, the Pricebook2Id field isn’t blank on the opportunity referenced by this object’s
OpportunityId), then the value of this field must match the currency of the CurrencyIsoCode
field on the PricebookEntry records that are associated with this object.

Possible values are:

**•** `BRL` —Brazilian Real

**•** `CAD` —Canadian Dollar

**•** `EUR` —Euro

**•** `USD` —U.S. Dollar

The default value is `USD` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the associated parent OpportunityLineItem. This field is a relationship field.


Standard Objects OpportunityLineItemSplit

**Field** **Details**

**Relationship Name**
OpportunityLineItem

**Relationship Type**
Lookup

**Refers To**
OpportunityLineItem

```
Split

SplitAmount

SplitNote

SplitOwnerId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Read-only. Automatically generated number identifying the split within the opportunity.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount or value of the split.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Optional text about the split.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the user who is the owner of the split. This field is a relationship field.

**Relationship Name**
SplitOwner

**Relationship Type**
Lookup

**Refers To**
User


Standard Objects OpportunityLineItemSplit

**Field** **Details**

```
SplitPercentage

SplitTypeId

Territory2Id

```

Usage

**Type**
percent

**Properties**
Create, Filter, Sort, Update

**Description**
The percentage of the OpportunityLineItem's value that the split represents.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the associated OpptyLineItemSplitType. This field is a relationship field.

**Relationship Name**
SplitType

**Relationship Type**
Lookup

**Refers To**
OpptyLineItemSplitType

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the associated territory. This field is a relationship field, and is available in API version
62.0 and later.

**Relationship Name**
Territory2

**Relationship Type**
Lookup

**Refers To**
Territory2

Use the OpportunityLineItemSplit object to manage opportunity product splits for an opportunity.


### Standard Objects OpportunityOwnerSharingRule

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**OpportunityLineItemSplitHistory on page 63 (API version 59.0)**
History is available for tracked fields of the object.

### OpportunityOwnerSharingRule

Represents a rule for sharing an opportunity with users other than the owner.

Note: To enable access to this object for your org, contact Salesforce customer support. However, we recommend that you
instead use Metadata API to programmatically update owner sharing rules because it triggers automatic sharing rule recalculation.
[The SharingRules Metadata API type is enabled for all orgs.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_sharingrules.htm)

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Fields

**Field** **Details**

```
Description

DeveloperName

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A description of the sharing rule. Maximum size is 1000 characters. This field is available
in API version 29.0 and later.

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


Standard Objects OpportunityOwnerSharingRule

**Field** **Details**

When creating large sets of data, always specify a unique `DeveloperName` for
each record. If no `DeveloperName` is specified, performance slows down while
Salesforce generates one for each record.

```
GroupId

Name

OpportunityAccessLevel

UserOrGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the source group. Opportunities owned by users in the source
group trigger the rule to give access.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label of the sharing rule as it appears in the user interface. Limited to 80 characters.
Corresponds to **Label** on the user interface.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the type of sharing being allowed. The possible values are:

**•** `Read`

**•** `Edit`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the target user or group. The target user or group is being given
access.


### Standard Objects OpportunityPartner

Usage

Use this object to manage the sharing rules for opportunities. General sharing and Territory-related sharing use this object.

SEE ALSO:

Case

_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_sharingrules.htm)_ : SharingRules

### OpportunityPartner

This object represents a partner relationship between an Account and an Opportunity. An OpportunityPartner record is created
automatically when a Partner record is created for a partner relationship between an account and an opportunity.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Customer Portal users can't access this object.

Fields

**Field** **Details**

```
AccountToId

IsPrimary

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the partner Account in the partner relationship.

This is a relationship field.

**Relationship Name**
AccountTo

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort


Standard Objects OpportunityPartner

**Field** **Details**

**Description**
Indicates whether the account is the opportunity’s primary partner ( `true` ) or not ( `false` ).
Label is **Primary** .

```
OpportunityId

ReversePartnerId

Role

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the Opportunity that is in the partner relationship.

This is a relationship field.

**Relationship Name**
Opportunity

**Relationship Type**
Lookup

**Refers To**
Opportunity

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the reciprocal OpportunityPartner record in a partner relationship.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The UserRole that the Account has on the Opportunity. For example, `Reseller` or
`Manufacturer` .

Creating an Account-Opportunity Partner Relationship

When you create a partner relationship between an account and an opportunity (when you create a Partner record and specify the
`OpportunityId` field), the API automatically creates two OpportunityPartner records, one for the forward relationship and one for
the reverse.

**•** The value of the Partner field `AccountToId` maps to the value of the OpportunityPartner field `AccountToId` .

**•** The values of the `OpportunityId`, `Role`, and `IsPrimary` fields in both the Partner and OpportunityParnter records are the
same.


### Standard Objects OpportunityRelatedDeleteLog

**•** If you set the `IsPrimary` value to 1 ( `true` ) upon insert of a new OpportunityPartner, the `IsPrimary` value is automatically
set to 0 ( `false` ) for any existing primary partners for that opportunity.

This mapping allows the API to manage the records and their relationships efficiently.

SEE ALSO:

Partner

AccountPartner

### OpportunityRelatedDeleteLog

Represents an audit log of the deletion of opportunity-related child records, such as opportunity team members, product splits, or
opportunity splits. This object is available in API version 59.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
CurrencyIsoCode

DataType

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only when the multicurrency feature is enabled. Contains the ISO code for any
currency allowed by the organization.

When multicurrency is enabled, and a Pricebook2 is specified on the parent opportunity
(that is, the `Pricebook2Id` field isn’t blank on the opportunity record referenced by this
object’s `OpportunityId` ), then the value must match the currency of the
`CurrencyIsoCode` field on the PricebookEntry records that are associated with this
object.

Possible values are:

**•** `AED` —UAE Dirham

**•** `CAD` —Canadian Dollar

**•** `INR` —Indian Rupee

**•** `USD` —U.S. Dollar

The default value is `USD` .

**Type**
picklist


Standard Objects OpportunityRelatedDeleteLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Data type of the field that was deleted.

Possible values are:

**•** `Double`

**•** `DynamicEnum`

**•** `EntityId`

**•** `StaticEnum`

**•** `Text`

```
DeleteLog

FieldName

OpportunityId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The name of the field that was deleted.

Possible values are:

**•** `OpportunityLineItemSplit.SplitOwnerId`

**•** `OpportunityLineItemSplit.SplitPercentage`

**•** `OpportunityLineItemSplit.SplitTypeId`

**•** `OpportunitySplit.SplitOwnerId`

**•** `OpportunitySplit.SplitPercentage`

**•** `OpportunitySplit.SplitTypeId`

**•** `OpportunityTeamMember.TeamMemberRole`

**•** `OpportunityTeamMember.UserId`

**•** `Product2.Name`

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Required. ID of the associated opportunity.


### Standard Objects OpportunityShare

**Field** **Details**

This field is a relationship field.

**Relationship Name**
### Opportunity

**Relationship Type**
Lookup

**Refers To**
### Opportunity

```
Parent

SobjectType

Value

### OpportunityShare

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the record that was deleted. Records with the same Parent text indicate that the value
shown in the Value field came from the same record that was previously deleted. Refer to
the FieldName field to see which field is being tracked.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The object that’s being recorded for this row of data. Possible values are:

**•** `OpportunityLineItemSplit`

**•** `OpportunitySplit`

**•** `OpportunityTeamMember`

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The value of the field that was deleted.

Represents a sharing entry on an Opportunity.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.


Standard Objects OpportunityShare

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`describeSObjects()`, `create()`, `delete()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Summer ’20 and later, only users with access to the Opportunity object can access this object.

Fields

The properties available for some fields depend on the default organization-wide sharing settings. The properties listed are true for the
default settings of such fields.

**Field** **Details**

```
IsDeleted

OpportunityAccessLevel

OpportunityId

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
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Level of access that the user or group has to the opportunity. The possible values are:

**•** `Read`

**•** `Edit`

**•** `All` —This value is not valid when creating, updating, or deleting records.

This field must be set to an access level that’s higher than the org’s default access level for
opportunities.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


Standard Objects OpportunityShare

**Field** **Details**

**Description**
ID of the opportunity associated with this sharing entry. This field can’t be updated.

This is a relationship field.

**Relationship Name**
Opportunity

**Relationship Type**
Lookup

**Refers To**
Opportunity

```
RowCause

UserOrGroupId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only permitted
value is `Manual` . If no value is specified, the field defaults to `Manual` . All other `RowCause`
values are read-only. After the sharing entry is created, this field can’t be edited.

Valid values include:

**•** `Owner` —The User is the owner of the opportunity.

**•** `Manual` —The User or Group has access because a user with “All” access manually
shared the opportunity with the user or group.

**•** `Rule` —The User or Group has access via an opportunity sharing rule.

**•** `GuestRule` —The User or Group has access via an opportunity guest user sharing
rule.

**•** `ImplicitChild` —The User or Group has access to the opportunity on the account
associated with this opportunity. After faster account sharing recalculation is enabled,
sharing entries with this value aren’t returned in queries. Instead of storing implicit child
shares, record access is determined dynamically.

**•** `LpuImplicit` —The User has access to records owned by high-volume Experience
Cloud site users via a share group.

**•** `ARImplicit` —The User, who belongs to a partner or customer account, has access
to the opportunity via an account relationship data sharing rule.

**•** `Sales Team` —The User has access to the opportunity because the user is on the
opportunity sales team for the opportunity. The OpportunityTeamMember object sets
the access level. See OpportunityTeamMember for more information.

**•** `Territory` —The forecast manager has access because they are assigned to a territory
above the territory that is assigned the opportunity.

**Type**
reference


### Standard Objects OpportunitySplit

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the user or group that has been given access to the opportunity. This field can’t be
updated.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User

Usage

This object allows you to determine which users and groups can view or edit opportunities owned by other users.

Note: After faster account sharing recalculation is enabled for your org, we no longer store implicit share records between accounts
and their child opportunity records. Sharing entries that have a value of `ImplicitChild` in the `RowCause` field aren’t
returned when you query this object. Instead, the system dynamically determines whether users can access child opportunity
records when they try to access them. This change speeds up ownership and sharing recalculation for accounts.

[For more information, see the Faster Account Sharing Recalculation knowledge article.](https://help.salesforce.com/s/articleView?id=000394638&type=1&language=en_US)

If you attempt to create a record that matches an existing record, any modified fields are updated, the system returns the existing record.

If an opportunity is shared in multiple ways with a user, you don’t always see multiple sharing records. If a user has access to an opportunity
for one or more of the following RowCause values, the records in the OpportunityShare object are compressed into one record with the
highest level of access.

**•** `Manual`

**•** `Owner`

SEE ALSO:

Overview of Salesforce Objects and Fields

### OpportunitySplit OpportunitySplit credits one or more opportunity team members with a portion of the opportunity amount. This object is available in

API version 16.0 and later for pilot customers, and version 28.0 and later for others.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`


Standard Objects OpportunitySplit

Fields

**Field** **Details**

```
ArchivedTerritoryName

HasOpportunityLineItemSplit

OpportunityId

Split

```

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the associated territory that’s on an archived territory model. If the
OpportunityLineItemSplit isn’t associated with a territory on an archived territory
model, the field value is null. This field is available in API version 62.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only. Indicates whether the opportunity split has a split on the opportunity
line item level ( `true` ) or not ( `false` ).

The default value is `false` . This field is available in API version 58.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the opportunity for which the split is being created.

This field is a relationship field.

**Relationship Name**
Opportunity

**Relationship Type**
Lookup

**Refers To**
Opportunity

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Read-only. Automatically generated number identifying the split within the
opportunity.


Standard Objects OpportunitySplit

**Field** **Details**

```
SplitAmount

SplitNote

SplitOwnerId

SplitPercentage

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Monetary amount of the split.

Label is `Split Amount` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Enter any notes or comments about the split. The character limit is 255.

Label is `Split Note` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The opportunity owner.

This field is a relationship field.

**Relationship Name**
SplitOwner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
percent

**Properties**
Create, Filter, Sort, Update

**Description**
Split percentage that this team member receives. If the split type is validated to
a 100% total, this number can range from 0 to 100. If the total isn’t validated, this
number can range from 0 to 1,000.

Label is `Split (%)` .


Standard Objects OpportunitySplit

**Field** **Details**

```
SplitTypeId

Territory2Id

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Auto-generated, numeric ID for the split type defined by the OpportunitySplitType
object. This field is available in API version 28 and later.

If this field is blank, the system automatically specifies the default split type for
the opportunity amount, which is validated to 100%.

This field is a relationship field.

**Relationship Name**
SplitType

**Relationship Type**
Lookup

**Refers To**
OpportunitySplitType

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the associated territory. This field is a relationship field, and is available in
API version 62.0 and later.

**Relationship Name**
Territory2

**Relationship Type**
Lookup

**Refers To**
Territory2

Use the OpportunitySplit object to manage splits for an opportunity.

If you change the opportunity owner using the API, the old owner remains on the opportunity team with either Read-only access, or
the level of access specified in your organization-wide defaults.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


### Standard Objects OpportunitySplitType

**OpportunitySplitChangeEvent (API version 48.0)**
Change events are available for the object.

**OpportunitySplitHistory on page 63 (API version 59.0)**
History is available for tracked fields of the object.

### OpportunitySplitType OpportunitySplitType provides unique labels and behavior for each split type. This object is available in API version 28.0 and later.

There are two default split types: revenue splits, which must total 100%, and overlay splits, which can total any percentage.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`, `update()`

Fields

**Field Name** **Details**

```
Description

DeveloperName

IsActive

```

**Type**
textarea

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Describes the purpose of the split type, providing context to future developers.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The unique name of the object in the API. In managed packages, this
field prevents naming conflicts on package installations. With this field, a
developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance slows down while Salesforce generates one for
each record.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects OpportunitySplitType

**Field Name** **Details**

**Description**
Enables or disables the split type.

```
IsTotalValidated

Language

ManageableState

MasterLabel

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
If `true`, the split must total 100%. If `false`, the split can total any percentage.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates language of split labels in the user interface.

**Type**
ManageableState enumerated list

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the manageable state of the specified component that is contained in
a package:

**•** `beta`

**•** `deleted`

**•** `deprecated`

**•** `deprecatedEditable`

**•** `installed`

**•** `installedEditable`

**•** `released`

**•** `unmanaged`

This field is available in API version 38.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The user-interface label for the split type.


Standard Objects OpportunitySplitType

**Field Name** **Details**

```
NamespacePrefix

SplitEntity

SplitField

SplitDataStatus

```

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

This field can’t be accessed unless the logged-in user has the Customize
Application permission.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The containing record type, such as an opportunity. Available in API version 30
and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Indicates which currency field of the opportunity object is split. Available in API
version 30 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable,Restricted picklist, Sort,Update


### Standard Objects OpportunityStage

**Field Name** **Details**

**Description**
Indicates the status of the split type. Available in API version 30 and later.

### OpportunityStage

Represents the stage of an Opportunity in the sales pipeline, such as New Lead, Negotiating, Pending, Closed, and so on.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ApiName

DefaultProbability

Description

ForecastCategory

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Uniquely identifies a picklist value so it can be retrieved without using an id or master label.

**Type**
percent

**Properties**
Filter, Nillable, Sort,

**Description**
The default percentage estimate of the confidence in closing a specific opportunity for this
opportunity stage value. Label is **Probability (%)** .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Description of this opportunity stage value. Limit: 255 characters.

**Type**
picklist


Standard Objects OpportunityStage

**Field** **Details**

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The default forecast category for this opportunity stage value. The forecast category
automatically determines how opportunities are tracked and totaled in a forecast.

Possible values are:

**•** `BestCase`

**•** `Closed`

**•** `Forecast`

**•** `MostLikely`

**•** `Omitted`

**•** `Pipeline`

```
ForecastCategoryName

IsActive

IsClosed

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Available in API version 12.0 and later. The default forecast category value for this opportunity
stage value.

Possible values are:

**•** `Best Case`

**•** `Closed`

**•** `Commit`

**•** `Most Likely`

**•** `Omitted`

**•** `Pipeline`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this opportunity stage value is active ( `true` ) or not ( `false` ). Inactive
opportunity stage values are not available in the picklist and are retained for historical
purposes only.

**Type**
boolean


Standard Objects OpportunityStage

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this opportunity stage value represents a closed opportunity ( `true` ) or
not ( `false` ). Multiple opportunity stage values can represent a closed opportunity. Label
is **Closed** .

```
 IsWon

 MasterLabel

 SortOrder

```

Usage

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this opportunity stage value represents a won opportunity ( `true` ) or not
( `false` ). Multiple opportunity stage values can represent a won opportunity. Label is **Won** .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Master label for this opportunity stage value. This display value is the internal label that does
not get translated. Limit: 255 characters.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number used to sort this value in the opportunity stage picklist. These numbers are not
guaranteed to be sequential, as some previous opportunity stage values might have been
deleted.

This object represents a value in the opportunity stage picklist, which provides additional information about the stage of an Opportunity,
such as its probability or forecast category. Query this object to retrieve the set of values in the opportunity stage picklist, and then use
that information while processing Opportunity records to determine more information about a given opportunity. For example, the
application could test whether a given opportunity is won or not based on its `StageName` value and the value of the `IsWon` property
in the associated OpportunityStage object.


### Standard Objects OpportunityTag

This object is read-only via the API.

SEE ALSO:

Overview of Salesforce Objects and Fields

### OpportunityTag

Associates a word or short phrase with an Opportunity.

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


### Standard Objects OpportunityTeamMember

**Field Name** **Details**

**Properties**
Create, Filter, Restricted picklist

**Description**
Defines the visibility of a tag.

Valid values:

**•** `Public` —The tag can be viewed and manipulated by all users in an organization.

**•** `Personal` —The tag can be viewed or manipulated only by a user with a matching
`OwnerId` .

Usage

OpportunityTag stores the relationship between its parent TagDefinition and the Opportunity being tagged. Tag objects act as metadata,
allowing users to describe and organize their data.

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.

### OpportunityTeamMember

Represents a User on the opportunity team of an Opportunity.

See also UserTeamMember, which represents a User who is on the default Opportunity team of another user.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
IsDeleted

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not
( `false` ). Label is **Deleted** .

Note: An OpportunityTeamMember that is deleted isn’t moved to the Recycle
Bin and can’t be undeleted, unless the record was cascade-deleted when deleting
a related Opportunity. For directly deleted OpportunityTeamMember records,


Standard Objects OpportunityTeamMember

**Field** **Details**

don't use the `isDeleted` field to detect deleted records in SOQL queries.
Instead, use `getDeleted()` .

```
Name

OpportunityAccessLevel

OpportunityId

PhotoURL

TeamMemberRole

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The team member name. This read-only field is available in API version 30.0 and later.

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**
Opportunity access level for this team member. Valid values:

**•** `Read`

**•** `Edit`

**•** `All`

This field is supported in triggers, but not in workflows or validation rules. It’s editable
in API version 36.0 and later.

**Type**
reference

**Properties**
Create, Filter

**Description**
Required. ID of the Opportunity associated with this opportunity team. This field can’t
be updated.

**Type**
URL

**Properties**
Filter, Nillable, Sort, Group

**Description**
Read only. Retrieves the users Chatter photo URL. This field is available in API version
32.0 and later.

**Type**
picklist


Standard Objects OpportunityTeamMember

**Field** **Details**

**Properties**
Create, Filter, Nillable, Update

**Description**
Role that the team member has on the opportunity. The org’s admin sets the valid
values in the Opportunity Team Roles picklist. Label is **Team Role** .

```
Title

UserId

```

Usage

**Type**
string

**Properties**
Filter, Nillable, Sort, Group

**Description**
Read only. Retrieves the user’s title. This field is available in API version 36.0 and later.

**Type**
reference

**Properties**
Create, Filter

**Description**
Required. ID of the User who is a member of the opportunity team. This field can’t
be updated.

If you create a record for this object and the `OpportunityId` and `UserId` combination matches an existing record, the system
updates any modified fields and returns the existing record.

In the user interface, users can set up an opportunity team for the opportunities they own. The opportunity team includes other users
that are working on the opportunity with them. This object is available only in organizations that have enabled team selling.

Note: The behavior for changing ownership of opportunities is different using the user interface when the previous owner is on
an opportunity team. For example, when you change the owner of an opportunity using the API, the previous owner's access
becomes Read Only or the access specified in your organization-wide default for opportunities, whichever is greater. However,
performing this same action in the user interface allows you to select the access level for the previous owner when the previous
owner is on an opportunity team.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


### Standard Objects OpptyLineItemSplitType

**OpportunityTeamMemberHistory on page 63 (API version 59.0)**
History is available for tracked fields of the object.

SEE ALSO:

UserTeamMember

### OpptyLineItemSplitType

Represents an opportunity product split type. This object is available in API version 58.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
Description

DeveloperName

IsActive

```

**Type**
textarea

**Properties**
Filter, Group, Sort

**Description**
Text description of the opportunity line item split type. Limit: 80 characters.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The developer (API) name of the opportunity line item split type.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the opportunity line item split type is active ( `true` ) or not ( `false` ). The
value of this field is inherited from the `IsActive` field of the parent OpportunitySplitType
record.


Standard Objects OpptyLineItemSplitType

**Field** **Details**

```
IsTotalValidated

Language

MasterLabel

NamespacePrefix

OpportunitySplitTypeId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the OpportunityLineItemSplit records associated with the
OpportunityLineItem must have SplitPercent values that aggregate to 100% ( `true` ) or not
( `false` ). The value of this field is inherited from the `IsTotalValidated` field of the
parent OpportunitySplitType record.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the opportunity line item split type.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The opportunity line item split type label.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the parent OpportunitySplitType. Every OpptyLineItemSplitType must have a parent
OpportunitySplitType. This field is a relationship field.

**Relationship Name**
OpportunitySplitType

**Relationship Type**
Lookup


### Standard Objects Order

**Field** **Details**

**Refers To**
OpportunitySplitType

```
SplitDataStatus

SplitEntity

SplitField

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The state of the asynchronous job to delete OpportunityLineItemSplit records when the
associated OpptyLineItemSplitType record is deleted. Possible values are:

**•** `DeletionFailed–` The job failed the last time it ran.

**•** `Ready` –The job hasn't run or isn't running. OpportunityLineItemSplit records associated
with the OpptyLineItemSplitType can be interacted with.

**•** `ToBeDeleted` –The job is running.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Name or ID of the entity that contains the field being split. In API version 58.0, this value is
always OpportunityLineItem.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Name or ID of the field on OpportunityLineItem that is being split. If it's a standard field, then
the value is the API name of the field. If it’s a custom field, the value is the custom field
definition ID.

When an OpportunitySplitType has product splits enabled in Setup, then an OpptyLineItemSplitType record is created. For example, if
there is an OpportunitySplitType record with a SplitField of `Amount` and product splits is enabled in Setup, then there is an
OpptyLineItemSplitType record with a SplitField of `TotalPrice` (since the TotalPrice field rolls up to Amount).

### Order

Represents an order associated with a contract or an account.


Standard Objects Order

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
AccountId

ActivatedById

ActivatedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. ID of the Account associated with this order. Only updated when the
order’s `StatusCode` value is _`Draft`_ .

This field is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
ID of the user who activated this order.

This field is a relationship field.

**Relationship Name**
ActivatedBy

**Relationship Type**
Lookup

**Refers To**
User

**Type**
dateTime

**Properties**
Filter, Nillable, Sort, Update


Standard Objects Order

**Field Name** **Details**

**Description**
Date and time when the order was activated.

```
BillingAddress

BillingCity

BillingCountry

BillingCountryCode

BillingEmailAddress

```

**Type**
address

**Properties**
Filter, Nillable

**Description**

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
City for the billing address for this order. The maximum size is 40 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Country for the billing address for this order. The maximum size is 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ISO country code for the billing address for this order.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Email address for this order’s billing address.

This field is available with Salesforce Order Management, Revenue Cloud, or B2B
Commerce license.

This field is available in API v48.0 and later.


Standard Objects Order

**Field Name** **Details**

```
BillingGeocodeAccuracy

BillingLatitude

BillingLongitude

BillingPhoneNumber

BillingPostalCode

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode of the address.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `BillingLongitude` to specify the precise geolocation of a billing
address. Acceptable values are numbers between –90 and 90 with up to 15
decimal places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `BillingLatitude` to specify the precise geolocation of a billing
address. Acceptable values are numbers between –180 and 180 with up to 15
decimal places.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number for this order’s billing address.

This field is available with Salesforce Order Management, Revenue Cloud, or B2B
Commerce license.

This field is available in API v48.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Postal code for the billing address for this order. The maximum size is 20
characters.


Standard Objects Order

**Field Name** **Details**

```
BillingState

BillingStateCode

BillingStreet

BillToContactId

CompanyAuthorizedById

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
State for the billing address for this order. The maximum size is 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ISO state code for the order’s billing address.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Street address for the billing address.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the contact that the order is billed to.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the user who authorized the account associated with the order.

This field is a relationship field.

**Relationship Name**
CompanyAuthorizedBy

**Relationship Type**
Lookup

**Refers To**
User


Standard Objects Order

**Field Name** **Details**

```
CompanyAuthorizedDate

ContractId

CurrencyIsoCode

CustomerAuthorizedById

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date on which your organization authorized the order.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the contract associated with this order. Only updated when the order’s
`StatusCode` value is _`Draft`_ .

This field is a relationship field.

**Relationship Name**
Contract

**Relationship Type**
Lookup

**Refers To**
Contract

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Three-letter ISO 4217 currency code.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the contact who authorized the order.

This field is a relationship field.

**Relationship Name**
CustomerAuthorizedBy

**Relationship Type**
Lookup


Standard Objects Order

**Field Name** **Details**

**Refers To**
Contact

```
CustomerAuthorizedDate

Description

EffectiveDate

EndDate

ExternalCustomerReference

GrandTotalAmount

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date on which the contact authorized the order.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the order.

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Date at which the order becomes effective. Label is **Order Start Date** .

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date at which the order ends. Label is **Order End Date** .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The external customer ID from an ecommerce channel or any other external
channel. Label is **External Customer ID Reference** .

This field is available in API version 66.0 and later.

**Type**
currency


Standard Objects Order

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
Sum of `TotalAmount` and `TotalTaxAmount` .

This field is available with Salesforce Order Management, Revenue Cloud, or B2B
Commerce license.

This field is available in API v48.0 and later.

```
IsReductionOrder

```

LastReferencedDate

```
LastViewedDate

Name

OpportunityId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Read only. Determines whether an order is a reduction order. Label is **Reduction**
**Order** .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last interacted with this record, directly or
indirectly.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, it’s possible that the user only accessed this record or list view
( `LastReferencedDate` ), but not viewed it.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name for this order.

**Type**
reference


Standard Objects Order

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID for the opportunity that’s associated with this order.

```
OrderedDate

OrderManagementReferenceIdentifier

OrderNumber

OrderReferenceNumber

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time that the order was placed.

This field is available with Salesforce Order Management, Revenue Cloud, or B2B
Commerce license.

This field is available in API v48.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The field used by Order Management to store the external reference identifier
for B2C Commerce orders. On creation, the B2C Integration sets this value to _`B2C`_
_`realm ID`_ + "_" + _`B2C instance ID`_ + "@" + _`B2C Commerce`_
_`catalog/domain ID`_ + "@" + _`B2C Commerce order number`_ .
Otherwise, it isn’t set.

When you create an OrderSummary, if you don’t specify an
ExternalReferenceIdentifier value, it’s set to this value. If this value is null, then
the system generates a value for ExternalReferenceIdentifier. This value isn’t
required to be unique in an organization, but the OrderSummary
ExternalReferenceIdentifier is.

This field is available in API version 56.0 and later.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Order number assigned to this order (not the unique, system-generated ID
assigned during creation). The maximum size is 30 characters.

**Type**
string


Standard Objects Order

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Order reference number assigned to this order. The maximum size is 80 characters.

```
OriginalOrderId

OwnerId

PaymentTermId

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Optional. ID of the original order that a reduction order is reducing, if the reduction
order is reducing a single order. Label is **Original Order** .

Editable only if `isReductionOrder` is _`true`_ . If the reduction order is
reducing more than one order, leave blank.

This field is a relationship field.

**Relationship Name**
OriginalOrder

**Relationship Type**
Lookup

**Refers To**
Order

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. ID of the user or queue that owns this order.

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
Create, Defaulted on create, Filter, Group, Nillable, Sort


Standard Objects Order

**Field Name** **Details**

**Description**
The ID of the related payment term. This field is available in API version 55.0 and
later. This field is available if Subscription Management is enabled in your org.

This field is a relationship field.

**Relationship Name**
PaymentTerm

**Relationship Type**
Lookup

**Refers To**
PaymentTerm

```
PoDate

PoNumber

Pricebook2Id

QuoteId

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date of the purchase order.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number identifying the purchase order. The maximum is 80.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Required. ID of the price book associated with this order.

This field is a relationship field.

**Relationship Name**
Pricebook2

**Relationship Type**
Lookup

**Refers To**
Pricebook2

**Type**
reference


Standard Objects Order

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the quote that’s associated with this order.

If you set `QuoteId` to null, `QuoteLineItemId` on all of the order’s child
order products is set to null.

```
RecordTypeId

RelatedOrderId

RelatedOrderType

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the record type assigned to this order.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The original order that a change order was created from.

This field is available with Salesforce Order Management, Revenue Cloud, or B2B
Commerce license.

This field is available in API v48.0 and later.

This field is a relationship field.

**Relationship Name**
RelatedOrder

**Relationship Type**
Lookup

**Refers To**
Order

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies the related order type.

Possible values are:

**•** ChangeOrder

**•** SupplementalOrder


Standard Objects Order

**Field Name** **Details**

**•** TransferOrder

```
SalesChannelId

SalesStoreId

ShippingAddress

ShippingCity

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Reference to a sales channel entity.

This field is available with Salesforce Order Management, Revenue Cloud, or B2B
Commerce license.

This field is available in API v48.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the RetailStore or WebStore associated with this Order.

This field is a polymorphic relationship field.

This field is available with Salesforce Order Management, Revenue Cloud, or B2B
Commerce license.

This field is available in API v46.0 and later.

**Relationship Name**
SalesStore

**Relationship Type**
Lookup

**Refers To**
WebStore

**Type**
address

**Properties**
Filter, Nillable

**Description**
Shipping address for the order.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Order

**Field Name** **Details**

**Description**
City of the shipping address. The maximum size is 40 characters.

```
ShippingCountry

ShippingCountryCode

ShippingGeocodeAccuracy

ShippingLatitude

ShippingLongitude

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Country of the shipping address. The maximum size is 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ISO country code for the order’s shipping address.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode of the shipping address.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `ShippingLongitude` to specify the precise geolocation of a
shipping address. Acceptable values are numbers between –90 and 90 with up
to 15 decimal places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `ShippingLatitude` to specify the precise geolocation of an
address. Acceptable values are numbers between –180 and 180 with up to 15
decimal places.


Standard Objects Order

**Field Name** **Details**

```
ShippingPostalCode

ShippingState

ShippingStateCode

ShippingStreet

ShipToContactId

Status

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Postal code of the shipping address. The maximum size is 20 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
State of the shipping address. The maximum size is 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ISO state code for the order’s shipping address.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Street address of the shipping address. Maximum of 255 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the contact that the order is shipped to.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


Standard Objects Order

**Field Name** **Details**

**Description**
Picklist of values that indicate order status. Each value is associated with one of
the status categories defined in StatusCode. For example, the status picklist might
contain _`Draft`_, _`Ready for Review`_, and _`Ready for Activation`_
values with a `StatusCode` of _`Draft`_ .

```
StatusCode

TaxLocaleType

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
The status category for the order. Label is **Status Category** .

Valid values are:

**•** `Draft`

**•** `Activated`

**•** `Superseded` —This value is applicable only to Revenue Cloud Advanced
users and is available in API version 64.0 and later.

To use supplemental orders, also known as in-flight amendments, create a status
that’s associated with the Superseded status code.

.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of tax calculation that Salesforce uses for the order’s order items. VAT
regions use gross tax, which includes tax in all sale amounts. US regions use net
tax, which calculates tax separately from the initial sale amount and then adds
the sale and tax amounts together in a total.

Use `TaxLocaleType` to determine which types of tax fields to show on your
order. If `TaxLocaleType` is null, the order shows all tax fields.

**Gross Tax Fields**

```
   TotalAdjDeliveryAmtWithTax

   TotalAdjProductAmtWithTax

   TotalProductAdjDistAmtWithTax

   TotalDeliveryAdjDistAmtWithTax

```

This field is available with Salesforce Order Management, Revenue Cloud, or B2B
Commerce license.

This field is available in API v49.0 and later.


Standard Objects Order

**Field Name** **Details**

```
TotalAdjDeliveryAmtWithTax

TotalAdjProductAmtWithTax

TotalAdjustedDeliveryAmount

TotalAdjustedDeliveryTaxAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of delivery line amounts, delivery line adjustments, and tax. Order products
with null Type fields aren’t included.

This field is a gross tax field.

This field is available with Salesforce Order Management, Revenue Cloud, or B2B
Commerce license.

This field is available in API v49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of product line amounts, line adjustments, and tax. Order products with
null Type fields aren’t included.

This field is a gross tax field.

This field is available with Salesforce Order Management, Revenue Cloud, or B2B
Commerce license.

This field is available in API v49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of delivery line amounts and delivery line adjustments. Order products with
null Type fields aren’t included.

This field is available with Salesforce Order Management, Revenue Cloud, or B2B
Commerce license.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of delivery line tax amounts and delivery line tax adjustments.


Standard Objects Order

**Field Name** **Details**

This field is available with Salesforce Order Management, Revenue Cloud, or B2B
Commerce license.

This field is available in API v48.0 and later.

```
TotalAdjustedProductAmount

TotalAdjustedProductTaxAmount

TotalAmount

TotalDeliveryAdjDistAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of product line amounts and line adjustments. Order products with null
Type fields aren’t included.

This field is available with Salesforce Order Management, Revenue Cloud, or B2B
Commerce license.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of line tax amounts and line tax adjustments. Order products with null Type
fields aren’t included.

This field is available with Salesforce Order Management, Revenue Cloud, or B2B
Commerce license.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Filter, Sort

**Description**
The net total amount for the order products associated with this order.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Roll-up of the order’s delivery adjustment distributed amounts. Used only when
the Order Adjustment Group has a Type value of Header.


Standard Objects Order

**Field Name** **Details**

This field is available with Salesforce Order Management, Revenue Cloud, or B2B
Commerce license.

This field is available in API v48.0 and later.

```
TotalDeliveryAdjDistAmtWithTax

TotalDeliveryAdjDistTaxAmount

TotalProductAdjDistAmount

TotalProductAdjDistAmtWithTax

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Roll-up of the order’s delivery adjustment distributed amounts and tax. Used
only when the Order Adjustment Group has a Type value of Header.

This field is a gross tax field.

This field is available with Salesforce Order Management, Revenue Cloud, or B2B
Commerce license.

This field is available in API v49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Roll-up of the order’s delivery adjustment distributed tax amounts. Used only
when the Order Adjustment Group has a Type value of Header.

This field is available with Salesforce Order Management, Revenue Cloud, or B2B
Commerce license.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Roll-up of the order’s product adjustment distributed amounts. Order products
with null Type fields aren’t included. Used only when the Order Adjustment
Group has a Type value of Header.

This field is available with Salesforce Order Management, Revenue Cloud, or B2B
Commerce license.

This field is available in API v48.0 and later.

**Type**
currency


Standard Objects Order

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
Roll-up of the order’s product adjustment distributed amounts. Order products
with null Type fields aren’t included. Used only when the Order Adjustment
Group has a Type value of Header.

This field is a gross tax field.

This field is available with Salesforce Order Management, Revenue Cloud, or B2B
Commerce license.

This field is available in API v49.0 and later.

```
TotalProductAdjDistTaxAmount

TotalTaxAmount

Type

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Roll-up of the order’s product adjustment distributed tax amounts. Order products
with null Type fields aren’t included. Used only when the Order Adjustment
Group has a Type value of Header.

This field is available with Salesforce Order Management, Revenue Cloud, or B2B
Commerce license.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Roll-up of all taxes on the order, including delivery taxes, price adjustment taxes,
and product taxes.

This field is available with Salesforce Order Management, Revenue Cloud, or B2B
Commerce license.

This field is available in API v48.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Order

**Field Name** **Details**

**Description**
To show more information about your order, you can add custom values to the
`Type` picklist. By default, the `Type` field doesn't perform any actions or show
any values.

Usage

The `Status` field specifies the current state of an order. Status strings represent its current state ( _`Draft`_ or _`Activated`_ ).

When a client application creates an order, the `Status Code` must be _`Draft`_ and the `Status` must be any value that corresponds
to a `Status Code` of _`Draft`_ . The application can then activate an order by updating it and setting the value in its `Status` field
to an _`Activated`_ state. However, the `Status` field is the only field you can update when activating the order.

After an order is activated, your client application can change the `Status` back to the _`Draft`_ state—but only if the order doesn’t
have any child reduction order products. Your client application can delete orders when the `Status` is _`Draft`_ but not when its
`Status` is _`Activated`_ .

Client applications can use the API to create, update, delete, and query any Attachment associated with an order.

Orders Without Price Books

If your organization manages products and price books in an external platform, you can use Salesforce API to create orders and order
items without values for their price book and price book entry fields. This feature is available only for Salesforce orgs with the B2B
Commerce, B2B Commerce Starter, B2B Commerce Growth, or B2B Commerce Plus packages. Admins enable orders without price books
by going to Salesforce Order Settings and selecting the Optional Price Book setting.

In a standard order, Salesforce prompts the sales rep to select a price book when they add the first order product to the order. The sales
rep can then add order products that have price book entries in the selected price book. In an order without a price book, Salesforce
hides the order’s Add Products button and Edit Products button so that sales reps must manage their products and price books by using
their external system.

You can create orders without price books only by creating an order with the Salesforce API and leaving the `Pricebook2Id` field
null. Orders without price books follow several different guidelines compared to standard orders.

**•** Orders without price books don’t support reduction orders or change orders.

**•** Order products without price book entries require list prices.

**•** Orders without price books support only order items without price book entries. Orders with price books support only order items
with price book entries.

**•** Important: Orders without price books are supported with B2B licenses only. Salesforce Order Management requires price
books for orders and price book entries for order products.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[OrderChangeEvent (API version 44.0)](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.


### Standard Objects OrderAction

**[OrderFeed (API version 29.0)](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**
Feed tracking is available for the object.

**[OrderHistory](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[OrderOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

SEE ALSO:

OrderHistory

OrderItem

OrderSummary

SalesChannel

### OrderAction

Indicates the type of order, such as a new sale or a cancellation. This object is available in API version 55.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

This object is available if Subscription Management is enabled in your org.

Fields

**Field** **Details**

```
Name

OffsetOrderItemId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name given to the order action.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects OrderAction

**Field** **Details**

**Description**
The ID of the previous order item that is being modified by the business action. For example,
the order that is being canceled.

This is a relationship field.

**Relationship Name**
OffsetOrderItem

**Relationship Type**
Lookup

**Refers To**
OrderItem

```
OrderId

SourceAssetId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The order containing the order item that implements the business action.

This is a relationship field.

**Relationship Name**
Order

**Relationship Type**
Lookup

**Refers To**
Order

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The asset that is changed as a result of the business action. For example, the asset that is
being canceled.

This is a relationship field.

**Relationship Name**
SourceAsset

**Relationship Type**
Lookup

**Refers To**
Asset


### Standard Objects OrderAdjustmentGroup

**Field** **Details**

```
Subtype

Type

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The subtype of the action on the order line item.

Valid values are:

**•** `FieldAmendment`

**•** `Rollback`

**•** `StartDateAdjustment`

**•** `TransferFrom`

**•** `TransferTo`

This field is available with Revenue Cloud in API version 64.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The business action that created the order product.

Valid values are:

**•** `Add`

**•** `Amend`

**•** `Cancel`

**•** `No Change`

**•** `Renew`

**•** `Transfer` —Available with Revenue Cloud in API version 65.0 and later.

### OrderAdjustmentGroup

Group containing a set of adjustments applied to an order. This object is available in API version 48.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`


Standard Objects OrderAdjustmentGroup

Special Access Rules

To access Commerce Orders entities, your org must have a Salesforce Order Management license. Commerce Orders entities are available
only in Lightning Experience.

Fields

**Field** **Details**

```
AdjustmentBasisReferenceId

AdjustmentCauseId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
References the specific coupon applied.

This is a polymorphic relationship field.

**Relationship Name**
AdjustmentBasisReference

**Relationship Type**
Lookup

**Refers To**
Coupon

This field is available in API version 54.0 and later.

This field can only refer to Coupon when B2B Commerce is enabled.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
References the specific promotions applied.

This field is a polymorphic relationship field.

**Relationship Name**
AdjustmentCause

**Relationship Type**
Lookup

**Refers To**
PriceAdjustmentTier, Promotion

This field is available in API version 52.0 and later.

This field can only refer to Promotion when B2B Commerce is enabled.


Standard Objects OrderAdjustmentGroup

**Field** **Details**

```
AdjustmentSource

AdjustmentType

AdjustmentValue

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the origin of the adjustment.

Possible values are:

**•** `Discretionary` —The adjustment originates from a decision made by an individual,
for example, a manager’s discount granted to a client.

**•** `Promotion` —The adjustment originates from a promotion, for example, a holiday
sale discount.

**•** `Rule` —Reserved for future use.

**•** `System` —The adjustment originates from the system, for example, a volume discount
after the amount of items reaches a specific number.

This field is available in API version 57.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the type of mathematical adjustment to be applied to the order.

Possible values are:

**•** `AdjustmentAmount` —The adjustment is a numerical amount, for example, a cash
discount of 20.

**•** `AdjustmentPercentage` —The adjustment is a percentage amount, for example,
a 10% discount.

**•** `OverrideAmount` —The adjustment is a manual price override.

This field is available in API version 57.0 and later.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The specified `AdjustmentType` ’s amount to be applied to the order.

For example, when the `AdjustmentType` value is `AdjustmentAmount`, the
`AdjustmentValue` is expected to equal the value of the `TotalAmount` field.


Standard Objects OrderAdjustmentGroup

**Field** **Details**

When the `AdjustmentType` value is `AdjustmentPercentage`, the
`AdjustmentValue` represents the percentage number, and the `TotalAmount` field’s
value will show the calculated adjustment amount.

This field is available in API version 57.0 and later.

```
CurrencyIsoCode

Description

GrandTotalAmount

Name

OrderId

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The currency used for the checkout session. Default value is `USD` .

Possible values are:

**•** `USD` —U.S. Dollar

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
User-entered information about the order adjustment group.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all total amounts of all adjustments in this group, including tax.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The user-defined name of the order adjustment group.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique identifier of the order related to the adjustments in this order adjustment group.


Standard Objects OrderAdjustmentGroup

**Field** **Details**

This field is a relationship field.

**Relationship Name**
Order

**Relationship Type**
Lookup

**Refers To**
Order

```
Priority

RelatedAdjustmentGroupId

TotalAmount

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A numeric value that represents the order of precedence of the order adjustment group.

It can also represent the order of precedence when applying the `AdjustmentType`
values. For example, an order can have two adjustments: a $100 discount and a 10% discount.
This field will tell the pricing engine which adjustment needs to be applied first.

This field is available in API version 57.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the original order’s adjustment group. This field is a useful reference
in change order scenarios.

This field is a relationship field.

**Relationship Name**
RelatedAdjustmentGroup

**Relationship Type**
Lookup

**Refers To**
OrderAdjustmentGroup

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total of all order adjustments in this order adjustment group, excluding tax.


### Standard Objects OrderAdjustmentGroupSummary

**Field** **Details**

```
TotalTaxAmount

Type

```

Associated Objects

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total tax for all order adjustments in this order adjustment group.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates how the adjustment was applied to the order.

Possible values are:

**•** `Header` : — The adjustment was applied to the order’s balance, and then distributed
among the order products in the adjustment group.

**•** `SplitLine`  - The adjustment was applied to order product balances for the order
products in the adjustment group.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**OrderAdjustmentGroupChangeEvent on page 68**
Change events are available for the object.

**OrderAdjustmentGroupFeed on page 55**
Feed tracking is available for the object.

**OrderAdjustmentGroupHistory on page 63**
History is available for tracked fields of the object.

**OrderAdjustmentGroupOwnerSharingRule on page 65**
Sharing rules are available for the object.

**OrderAdjustmentGroupShare on page 67**
Sharing is available for the object.

### OrderAdjustmentGroupSummary

Represents the current properties and state of a group of related price adjustments. Associated with a set of
OrderItemAdjustmentLineSummaries that apply to OrderItemSummaries belonging to one OrderSummary. Corresponds to one or more
order adjustment group objects, consisting of an original object and any change objects applicable to it. This object is available in API
version 48.0 and later.


Standard Objects OrderAdjustmentGroupSummary

An OrderAdjustmentGroupSummary can represent an adjustment to an entire order as a group of adjustments to each of its products.
For example, representing “10% off the order” as a set of 10% off adjustments to each product on the order. It can also represent an
adjustment that applies to a subset of the products on an order. For example, representing “buy one, get one 50% off” as a 25% off
adjustment to each of two products.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is only available in Salesforce Order Management orgs or if the B2B Commerce license is enabled.

Fields

**Field** **Details**

```
AdjustmentBasisReferenceId

AdjustmentCauseId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
References the specific coupon applied.

This is a polymorphic relationship field.

**Relationship Name**
AdjustmentBasisReference

**Relationship Type**
Lookup

**Refers To**
Coupon

This field is available in API version 54.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
References the specific promotions applied.

This is a polymorphic relationship field.

**Relationship Name**
AdjustmentCause


Standard Objects OrderAdjustmentGroupSummary

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Promotion

This field is available in API version 52.0 and later.

```
CurrencyIsoCode

Description

GrandTotalAmount

Name

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
ISO code for the currency of the OrderSummary associated with the adjustments in the
group. The default value is USD.

Possible values are:

**•** `DKK` —Danish Krone

**•** `EUR` —Euro

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

This field is available in API version 49.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the OrderAdjustmentGroupSummary.

This field can be edited.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total, including tax, of the associated OrderItemAdjustmentLineSummaries.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


Standard Objects OrderAdjustmentGroupSummary

**Field** **Details**

**Description**
Name of the OrderAdjustmentGroupSummary.

```
OrderSummaryId

OriginalOrderAdjGroupId

TotalAmount

TotalTaxAmount

Type

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the OrderSummary associated with the OrderAdjustmentGroupSummary.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the original OrderAdjustmentGroup associated with this summary object. Nillable=true
only if the associated order summary is unmanaged. For managed order summaries,
nillable=false.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total, not including tax, of the associated OrderItemAdjustmentIineSummaries.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalAmount.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Type of the OrderAdjustmentGroupSummary. Header represents an order-level adjustment
with an OrderItemAdjustmentLineSummary for each OrderItemSummary on the
OrderSummary. SplitLine represents any other related set of
OrderItemAdjustmentLineSummaries.


### Standard Objects OrderChangeLog

**Field** **Details**

Possible values are:

**•** `Header`

**•** `SplitLine`

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**OrderAdjustmentGroupSummaryChangeEvent (API version 62.0)**
Change events are available for the object.

SEE ALSO:

OrderAdjustmentGroup

OrderItemAdjustmentLineSummary

### OrderChangeLog

Represents a log record of all change requests made to an order post activation. A log record is always one-to-one to change an order
request. This object is available in API version 48.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Commerce Cloud standard objects in the inventory data model require at least one of the following licenses: B2B Commerce, D2C
Commerce.

Fields

**Field** **Details**

```
ChangeLineId

```

**Type**
reference

**Properties**
Filter, Group, Sort


Standard Objects OrderChangeLog

**Field** **Details**

**Description**
The ID of the main change line created as a result of the change request. For example, if you
change an order item, the `ChangeLineId` would be the change OrderItem ID, or if you
change a shipping address, the `ChangeLineId` would be the change OrderDeliveryGroup
ID.

This field is a polymorphic relationship field.

**Relationship Name**
ChangeLine

**Relationship Type**
Lookup

**Refers To**
OrderAdjustmentGroup, OrderDeliveryGroup, OrderItem, OrderItemAdjustmentLineItem,
OrderItemTaxLineItem

```
ChangeLineType

ChangeOrderId

ChangeRequest

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The method used to implement the change.

Possible values are:

**•** `Delta`

**•** `New`

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the change order.

This field is a relationship field.

**Relationship Name**
ChangeOrder

**Relationship Type**
Lookup

**Refers To**
Order

**Type**
string


Standard Objects OrderChangeLog

**Field** **Details**

**Properties**
Filter, Group, idLookup, Sort

**Description**
The unique ID of the request of which this change is a part.

```
ChangeSummary

ChangeType

CurrencyIsoCode

```

**Type**
textarea

**Properties**

**Description**
A human-readable summary of the change details.

Here’s an example of a change summary:

```
  Reduced quantity by -3.

  Change adjustment by $15.

  Added an adjustment of $20.

  Changed tax by $-0.11, effective 1/1/2020.

  Added a tax of $1.5, effective 1/1/2020.

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of the change request.

Possible values are:

**•** `NewAdjustmentGroups` —Add a new header level adjustment.

**•** `NewLineAdjustments` —Add a new line level adjustment.

**•** `NewOrderItems` —Add a new order item.

**•** `QuantityChange` —Add or remove quantity from an original order item.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The ISO code for any currency allowed by the organization.

Possible value is:

**•** `USD` —U.S. Dollar

The default value is `USD` .


Standard Objects OrderChangeLog

**Field** **Details**

```
Name

RelatedLineId

RelatedOrderId

Status

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name for the order change log.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the main line that is changed as a result of this change.

This field is a polymorphic relationship field.

**Relationship Name**
RelatedLine

**Relationship Type**
Lookup

**Refers To**
OrderAdjustmentGroup, OrderDeliveryGroup, OrderItem, OrderItemAdjustmentLineItem,
OrderItemTaxLineItem

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the order that is changed.

This field is a relationship field.

**Relationship Name**
RelatedOrder

**Relationship Type**
Master-detail

**Refers To**
Order (the master object)

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


### Standard Objects OrderChgReasonCategMap

**Field** **Details**

**Description**
The order status of the change order.

Possible values are:

**•** `Activated`

**•** `Draft`

Usage

Order change log entries are automatically created each time an order is modified.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**OrderChangeLogFeed on page 55**
Feed tracking is available for the object.

**OrderChangeLogHistory on page 63**
History is available for tracked fields of the object.

### OrderChgReasonCategMap

The mapping between an order change reason and a service flow category. This object is available in API version 65.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Category

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The service flow that reasons are being categorized by.

Possible values are:

**•** `Cancel`


Standard Objects OrderChgReasonCategMap

**Field** **Details**

**•** `CancelAll`

**•** `CancelFee`

**•** `Discount`

**•** `Exchange`

**•** `RMA`

**•** `Return`

**•** `ReturnFee`

```
CurrencyIsoCode

Description

IsActive

IsAvailableForExternalUser

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The currency code of the order.

Possible values are:

**•** `EUR` —Euro

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

The default value is `USD` .

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the mapping.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Whether the category mapping is active.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects OrderChgReasonCategMap

**Field** **Details**

**Description**
Whether the mapping can be accessed and used by external users.

The default value is `false` .

```
LastReferencedDate

LastViewedDate

Name

OwnerId

Reason

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the mapping.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the mapping.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The order change reason that’s being categorized.


### Standard Objects OrderDeliveryGroup

**Field** **Details**

Possible values are:

**•** `Damaged`

**•** `DoorLocked`

**•** `IncorrectPrice`

**•** `Rejected`

**•** `WrongItem`

The default value is `Damaged` .

### OrderDeliveryGroup

A group of order items that share a delivery method and address. The delivery method and address are used during the fulfillment
process, such as shipping as a gift, downloading, picking up in store, or shipping to a standard address This object is available in API
version 48.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

To access Commerce Orders entities, your org must have a Salesforce Order Management license. Commerce Orders entities are available
only in Lightning Experience.

Fields

**Field** **Details**

```
DeliverToAddress

DeliverToCity

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
The delivery group’s order items are delivered to this address. Created based on the values
of the other `DeliverTo` fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects OrderDeliveryGroup

**Field** **Details**

**Description**
City address value. Sent to `DeliverToAddress` .

```
DeliverToCompanyName

DeliverToCountry

DeliverToFullFirstName

DeliverToFullLastName

DeliverToFullName

DeliverToFullSalutation

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Country address value. Sent to `DeliverToAddress`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Possible values are:


Standard Objects OrderDeliveryGroup

**Field** **Details**

**•** `Dr.`

**•** `Mr.`

**•** `Mrs.`

**•** `Ms.`

**•** `Prof.`

```
DeliverToGeocodeAccuracy

DeliverToLatitude

DeliverToLongitude

DeliverToName

DeliverToPostalCode

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Geocode accuracy address value. Sent to `DeliverToAddress` .

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Latitude address value. Sent to `DeliverToAddress` .

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Longitude address value. Sent to `DeliverToAddress` .

**Type**
string

**Properties**
Create, Filter, Nillable, Group, Sort, Update

**Description**
Name of the delivery recipient. Sent to `DeliverToAddress` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Postal Code address value. Sent to `DeliverToAddress` .


Standard Objects OrderDeliveryGroup

**Field** **Details**

```
DeliverToState

DeliverToStreet

DeliveryInstructions

Description

DesiredDeliveryDate

EmailAddress

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
State address value. Sent to `DeliverToAddress` .

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Street address value. Sent to `DeliverToAddress` .

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Text field for users to add other delivery instructions.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
User-defined description for this delivery group.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The buyer’s target delivery date for the order items included in the delivery group.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The buyer’s email address.


Standard Objects OrderDeliveryGroup

**Field** **Details**

```
GiftMessage

GrandTotalAmount

IsGift

OrderDeliveryGroupNumber

OrderDeliveryMethodId

OrderId

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
An optional gift message that the buyer can define if they’re sending the order items as a
gift to another recipient. Applies to all order items in the delivery group.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of the group’s total delivery amount and total tax amount.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
All items in the delivery group are gifts.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Unique number used for referencing this order delivery group.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the order delivery method related to this order delivery group.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


Standard Objects OrderDeliveryGroup

**Field** **Details**

**Description**
ID of the parent order for this order delivery group. An order can have multiple order delivery
groups.

```
PhoneNumber

PromisedDeliveryDate

RelatedDeliveryGroupId

TotalAdjustmentAmount

TotalAdjustmentAmtWithTax

```

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number of the buyer.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Merchant-defined date that the items in this group will be delivered to the customer. Usually
defined based on an estimated date from the shipping provider.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The original delivery group. Used for reference in change order scenarios.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all adjustments (of type Delivery Charge) made to order items in the order delivery
group.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all adjustments (of type Delivery Charge) made to order items in the order delivery
group, including tax.

This is a gross tax field.


Standard Objects OrderDeliveryGroup

**Field** **Details**

To access Commerce Orders fields, your org must have a Salesforce Order Management
license. Commerce Orders fields are available only in Lightning Experience.

This field is available in API v49.0 and later.

```
TotalAdjustmentTaxAmount

TotalAmount

TotalLineAmount

TotalLineAmtWithTax

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all adjustments (of type Delivery Charge) made to tax lines for order items in the
order delivery group.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all Total Amount fields (of type Delivery Charge) on order items within this delivery
group. On an order item, the total amount equals the quantity multiplied by the unit price,
including adjustments and tax.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of order items (of the type Delivery Charge). On an order item, the total line amount
equals the quantity multiplied by the unit price, before adjustments or tax.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all `TotalLineAmtWithTax` fields (of type Delivery Charge) on order items
within this delivery group. On an order item, the total line amount with tax equals the quantity
multiplied by the unit price, plus tax, before adjustments.

This is a gross tax field.

To access Commerce Orders fields, your org must have a Salesforce Order Management
license. Commerce Orders fields are available only in Lightning Experience.

This field is available in API v49.0 and later.


### Standard Objects OrderDeliveryGroupSummary

**Field** **Details**

```
TotalLineTaxAmount

TotalTaxAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all Total Line Tax Amount fields (of type Delivery Charge) on order items within
this delivery group. On an order item, the total line tax amount equals the total tax for that
line.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of all Total Tax Amount fields (of type Delivery Charge) on order items within this
order delivery group.

### OrderDeliveryGroupSummary

Represents the current properties and state of a group of OrderItemSummaries, belonging to one OrderSummary, to be fulfilled using
the same delivery method and delivered to the same address. A single shipment can include them all, but that isn’t guaranteed.
Corresponds to one or more order delivery group objects, consisting of an original object and any change objects applicable to it. This
object is available in API version 48.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is only available in Salesforce Order Management orgs or if the B2B Commerce license is enabled.

Fields

**Field** **Details**

```
CurrencyIsoCode

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort


Standard Objects OrderDeliveryGroupSummary

**Field** **Details**

**Description**
ISO code for the currency of the OrderSummary associated with the
OrderDeliveryGroupSummary. The default value is USD.

Possible values are:

**•** `DKK` —Danish Krone

**•** `EUR` —Euro

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

This field is available in API version 49.0 and later.

```
DeliverToAddress

DeliverToCity

DeliverToCompanyName

DeliverToCountry

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
Address of the recipient. Users with the Edit Delivery Information user permission can modify
this field.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Recipient address city.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Recipient address country.


Standard Objects OrderDeliveryGroupSummary

**Field** **Details**

```
DeliverToFullFirstName

DeliverToFullLastName

DeliverToFullName

DeliverToFullSalutation

DeliverTo

GeocodeAccuracy

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Possible values are:

**•** `Dr.`

**•** `Mr.`

**•** `Mrs.`

**•** `Ms.`

**•** `Prof.`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy of the geocode for the recipient address.

Possible values are:

**•** `Address`

**•** `Block`

**•** `City`


Standard Objects OrderDeliveryGroupSummary

**Field** **Details**

**•** `County`

**•** `ExtendedZip`

**•** `NearAddress`

**•** `Neighborhood`

**•** `State`

**•** `Street`

**•** `Unknown`

**•** `Zip`

```
DeliverToLatitude

DeliverToLongitude

DeliverToName

DeliverToPostalCode

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with FulfilledToLongitude to specify the precise geolocation of the recipient address.
Acceptable values are numbers between –90 and 90 with up to 15 decimal places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with FulfilledToLatitude to specify the precise geolocation of the recipient address.
Acceptable values are numbers between –90 and 90 with up to 15 decimal places.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name on the recipient address. Users with the Edit Delivery Information user permission can
modify this field.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects OrderDeliveryGroupSummary

**Field** **Details**

**Description**
Recipient address postal code.

```
DeliverToState

DeliverToStreet

DeliveryInstructions

Description

DesiredDeliveryDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Recipient address state.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Recipient address street.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Special instructions for the delivery. Users with the Edit Delivery Information user permission
can modify this field.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the OrderDeliveryGroupSummary.

This field can be edited.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects OrderDeliveryGroupSummary

**Field** **Details**

**Description**
Desired date for delivery. This field is informational, available for customizations. Users with
the Edit Delivery Information user permission can modify this field.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

```
EmailAddress

GiftMessage

GrandTotalAmount

IsGift

```

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Email address of the recipient. Users with the Edit Delivery Information user permission can
modify this field.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Gift message to include. Users with the Edit Delivery Information user permission can modify
this field.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total, including adjustments and tax, of the delivery charges associated with the
OrderDeliveryGroupSummary. This value only includes OrderItemSummaries of type code
Charge.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects OrderDeliveryGroupSummary

**Field** **Details**

**Description**
Indicates whether the OrderDeliveryGroupSummary represents a gift. Users with the Edit
Delivery Information user permission can modify this field.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

```
OrderDeliveryGroup

SummaryNumber

OrderDeliveryMethodId

OrderSummaryId

OriginalOrderDelivery

GroupId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
ID of the OrderDeliveryGroupSummary.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the order delivery method specified for the OrderDeliveryGroupSummary. Users with
the Edit Delivery Information user permission can modify this field.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the OrderSummary associated with the OrderDeliveryGroupSummary.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the original order delivery group associated with this summary object. Nillable=true
only if the associated order summary is unmanaged. For managed order summaries,
nillable=false.


Standard Objects OrderDeliveryGroupSummary

**Field** **Details**

```
PhoneNumber

PromisedDeliveryDate

TotalAdjustmentAmount

TotalAdjustment

AmtWithTax

```

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number of the recipient. Users with the Edit Delivery Information user permission can
modify this field.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Promised date for delivery. This field is informational, available for customizations. Users with
the Edit Delivery Information user permission can modify this field.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total price adjustments applied to delivery charges associated with the
OrderDeliveryGroupSummary. This value only includes adjustments to OrderItemSummaries
of type code Charge.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the price adjustments applied to the delivery charges associated with the
OrderDeliveryGroupSummary, inclusive of tax. This amount is equal to
TotalAdjustmentAmount + TotalAdjustmentTaxAmount.

This field is available in API version 49.0 and later.


Standard Objects OrderDeliveryGroupSummary

**Field** **Details**

```
TotalAdjustment

TaxAmount

TotalAmount

TotalLineAmount

TotalLineAmtWithTax

TotalLineTaxAmount

TotalTaxAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalAdjustmentAmount.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total, including adjustments but not tax, of the delivery charges associated with the
OrderDeliveryGroupSummary. This value only includes adjustments to OrderItemSummaries
of type code Charge.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total, not including adjustments or tax, of the delivery charges associated with the
OrderDeliveryGroupSummary.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total of the delivery charges associated with the OrderDeliveryGroupSummary, inclusive of
tax. This amount is equal to TotalLineAmount + TotalLineTaxAmount.

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalLineAmount.

**Type**
currency


### Standard Objects OrderDeliveryMethod

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the TotalAmount.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**OrderDeliveryGroupSummaryChangeEvent (API version 62.0)**
Change events are available for the object.

SEE ALSO:

OrderDeliveryGroup

OrderItemSummary

### OrderDeliveryMethod

Shows the customizations and options that a buyer selected for their delivery method. This object is available in API version 48.0 and
later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access Commerce Orders entities, your org must have a Salesforce Order Management license. Commerce Orders entities are available
only in Lightning Experience.

Fields

**Field** **Details**

```
Carrier

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects OrderDeliveryMethod

**Field** **Details**

**Description**
The carrier that the buyer chose for their delivery method. Developers must add values to
this field.

```
ClassOfService

Description

IsActive

LastReferencedDate

LastViewedDate

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The carrier class of service that the buyer chose for their delivery method. Developers must
add values to this field.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the delivery method.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Assign new delivery groups to active delivery methods.

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
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.


Standard Objects OrderDeliveryMethod

**Field** **Details**

```
Name

OwnerId

ProductId

ReferenceNumber

ShippingCarrierMethod

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Default name of this record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The user who owns an order delivery method record.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Optional. This product represents a delivery charge order product for a delivery using this
delivery method. For example, you could create a product that represents an overnight
express charge and assign it to an overnight express delivery method.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Reference number for an external delivery method.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Optional. A specific shipping service provided by a shipping carrier, such as Ground, 2Day,
and NextDay. Depends on the range of transit times available for each carrier.


### Standard Objects OrderHistory

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[OrderDeliveryMethodChangeEvent (API version 62.0)](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.

### OrderHistory

Represents historical information about changes that have been made to the standard fields of the associated order, or to any custom
fields with history tracking enabled.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Fields

**Field Name** **Details**

```
DataType

Field

NewValue

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
Name of the order field that was modified, or a special value to indicate some
other modification to the order.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
New value of the modified order field. Maximum of 255 characters.


### Standard Objects OrderItem

**Field Name** **Details**

```
OldValue

OrderId

```

Usage

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
Previous value of the modified order field. Maximum of 255 characters.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the order associated with this record.

This is a relationship field.

**Relationship Name**
### Order

**Relationship Type**
Lookup

**Refers To**
### Order

Order history entries are automatically created each time an order is modified.

Two rows are added to this record when foreign key fields change. One row contains the foreign key object names that display in the
online application. For example, `Jane Doe` is recorded as the name of a Contact. The other row contains the actual foreign key ID
that is only returned to and visible from the API.

This object respects field-level security on the parent object.

SEE ALSO:

### Order OrderItem

Represents an order product that your organization sells.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`


Standard Objects OrderItem

Special Access Rules

The user must have Edit permission on Order records to create or update order products on an order. The user must have Edit permission
on Order records to delete an order product.

Fields

**Field Name** **Details**

```
AdjustedLineAmount

AdjustedLineAmtWithTax

AggregatedQuantity

AvailableQuantity

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Line amount following line adjustments, excluding tax.

This field is available with Salesforce Order Management or Revenue Cloud.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Line amount following line adjustments, including tax.

This field is a gross tax field.

This field is available with Salesforce Order Management or Revenue Cloud.

This field is available in API v49.0 and later.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The quantity of a order item's grouped transaction lines or the products that have
been sold and converted to assets.

This field is available in API version 64.0 and later.

**Type**
double

**Properties**
Filter, Nillable, Sort


Standard Objects OrderItem

**Field Name** **Details**

**Description**
The amount of an order product that is available to be reduced. Value must be
greater than or equal to 0. An order product is reducible only if
`AvailableQuantity` is greater than 0.

Value is always 0 if the order product’s parent order is a reduction order.

```
BatchIdentifier

BillingFrequency2

CurrencyIsoCode

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Identifies a product bundle in a transaction processing batch to ensure that order
items from the same bundles are processed together.

This field is available in API version 64.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The time period that indicates how often the order item is billed.

This field is available in API version 55.0 and later. This field is available with
Subscription Management.

Possible values are:

**•** `Annual`

**•** `Monthly`

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO
code for the currency of the original Order associated with the OrderItem.

Possible values are:

**•** `DKK` —Danish Krone

**•** `EUR` —Euro

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

The default value is `USD` .


Standard Objects OrderItem

**Field Name** **Details**

This field is available in API version 49.0 and later.

```
DeliveryEstimationReference

DeliveryEstimationTimeZone

Description

DoesAutomaticallyRenew

EarliestEstimatedDeliveryDate

EarliestEstimatedDeliveryTime

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Unique reference ID for the delivery estimation.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Time zone in which the estimated delivery times are based.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Text description of this object. For Commerce stores, during checkout, this field
is populated with the value of a product name. The product name is copied from
the `CartItem.Name` field of a cart item that corresponds to the `OrderItem` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates that the order item is set to automatically renew (true) or not (false).

This field is available in API version 64.0 and later.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Earliest estimated date for the item to be delivered.

**Type**
timeOnly


Standard Objects OrderItem

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Earliest estimated time of the day for the item to be delivered.

```
EndDate

EndDateTime

EndTime

GrossUnitPrice

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Optional. Last day the order product is available.

**Type**
datetime

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The end date and time of the order item, derived from the End Date and End
Time fields in the time zone specified in the Start and End Time Zone field. If the
time zone isn't specified, the default is Coordinated Universal Time (UTC).

Label is **End Date Time** .

This field is available in Revenue Cloud in API version 65.0 and later.

**Type**
timeOnly

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The end time of the order item.

Label is **End Time** .

This field is available in Revenue Cloud in API version 65.0 and later.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Unit price including tax.

This field is a VAT field that includes tax. Salesforce populates it on order creation
only when `Order.TaxLocaleType` has a value of Gross.


Standard Objects OrderItem

**Field Name** **Details**

```
IsOrderItemLocked

LastEstimatedDeliveryDate

```

LastEstimatedDeliveryTime

```
LineNumber

ListPrice

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the order item and its children are locked (true) or not (false).
Locked order items and their children cannot be modified, added, or deleted.

This field is available in API version 63.0 and later.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Latest estimated date for the item to be delivered.

**Type**
timeOnly

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Latest estimated time of the day for the item to be delivered.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The number used to organize lines on the order.

This field is available with Salesforce Order Management or Revenue Cloud.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
List price for the order product. Inherited value from the associated
`PriceBookEntry` upon order product creation.


Standard Objects OrderItem

**Field Name** **Details**

```
ListPriceTotal

NetUnitPrice

OrderActionId

OrderDeliveryGroupId

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The `ListPrice` times the `Quantity` . This field is a calculated field.

This field is available in API version 55.0 and later. This field is available with
Subscription Management.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The unit price after all price adjustments are applied.

This field is available in API version 55.0 and later. This field is available with
Subscription Management.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the related order action. The order action indicates the type of order;
for example, a new sale or a cancellation.

This field is available in API version 55.0 and later. This field is available with
Subscription Management.

This field is a relationship field.

**Relationship Name**
OrderAction

**Relationship Type**
Lookup

**Refers To**
OrderAction

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The delivery group for the order product.


Standard Objects OrderItem

**Field Name** **Details**

This field is available with Salesforce Order Management or Revenue Cloud.

This field is available in API v48.0 and later.

This field is a relationship field.

**Relationship Name**
OrderDeliveryGroup

**Relationship Type**
Lookup

**Refers To**
OrderDeliveryGroup

```
OrderId

OrderItemNumber

OriginalOrderItemId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the order that this order product is a child of.

This field is a relationship field.

**Relationship Name**
Order

**Relationship Type**
Lookup

**Refers To**
Order

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Automatically generated number that identifies the order product.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Required if `isReductionOrder` on the parent order is _`true`_ .

ID of the original order product being reduced.

This field is a relationship field.


Standard Objects OrderItem

**Field Name** **Details**

**Relationship Name**
OriginalOrderItem

**Relationship Type**
Lookup

**Refers To**
OrderItem

```
PeriodBoundary

PeriodBoundaryDay

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The period boundary helps determine the start and end date of the billing periods.

This field is available in API version 55.0 and later. This field is available with
Subscription Management and Revenue Cloud.

Possible values are:

**•** `AlignToCalendar` —the period starts on the first day of the term unit;
for example, the first day of the month.

**•** `Anniversary` —The start date determines the boundary. For example, if
a monthly subscription starts on September 13, the subscription starts on
the 13th day of each month.

**•** `DayOfPeriod` —the period starts on the day indicated by
`PeriodBoundaryDay` .

**•** `LastDayOfPeriod` —the period starts on the last day of the pricing term
unit; for example, the last day of the month.

Keep these considerations in mind for amendment, renewal, and cancellations
of assets in Revenue Cloud.

**•** The value of the `PeriodBoundary` field is copied from the
AssetActionSource (initial sale), by default.

**•** For termed selling models where the `PeriodBoundary` value is
`Anniversary`, the value of the `PeriodBoundary` field is automatically
converted to `DayOfPeriod` .

**•** Start date adjustment operation on an asset preserves the original value
without conversion.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects OrderItem

**Field Name** **Details**

**Description**
Required when `PeriodBoundary` is `DayOfPeriod` . Indicates the day of
the week or month that marks the period boundary. Must be an integer from 1
through 31.

This field is available in API version 55.0 and later. This field is available with
Subscription Management and Revenue Cloud.

Keep these considerations in mind for amendment, renewal, and cancellations
of assets in Revenue Cloud.

**•** The value of the `PeriodBoundary` field is copied from the
AssetActionSource (initial sale), by default.

**•** When `PeriodBoundary` field value is converted from `Anniversary`
to `DayOfPeriod` for termed selling models, the value of the
`PeriodBoundaryDay` field is automatically populated with the day
value from AssetActionSource.StartDate.

**•** Start date adjustment operation on an asset preserves the original value
without conversion.

```
PeriodBoundaryStartMonth

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Nillable, Sort, Update

**Description**
The field is populated based on input in the StartDate, PeriodBoundary, and
PeriodBoundaryDay when BillingFrequency2 is Annual or by manual user entry.
Possible values are:

**•** `1-January`

**•** `2-February`

**•** `3-March`

**•** `4-April`

**•** `5-May`

**•** `6-June`

**•** `7-July`

**•** `8-August`

**•** `9-September`

**•** `10-October`

**•** `11-November`

**•** `12-December`

Keep these considerations in mind for amendment, renewal, and cancellations
of assets in Revenue Cloud.

**•** The value of the `PeriodBoundary` field is copied from the
AssetActionSource (initial sale), by default.


Standard Objects OrderItem

**Field Name** **Details**

**•** For termed selling models where `PeriodBoundary` field value is
`Anniversary` and `PricingTermUnit` field value is `ANNUAL`,
`SEMI_ANNUAL`, or `QUARTERLY`, the value of the
`PeriodBoundaryStartMonth` field is automatically recalculated by
using AssetActionSource.StartDate.month.

**•** Start date adjustment operation on an asset preserves the original value
without conversion.

```
PricebookEntryId

PriceRevisionPolicyId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Required. ID of the associated PricebookEntry. Specify this field when creating
OrderItem records. It can’t be changed in an update.

If you have a B2B Commerce, B2B Commerce Starter, B2B Commerce Growth, or
B2B Commerce Plus license, Salesforce users can create orders without price
books and order items without price book entries.

This field is a relationship field.

**Relationship Name**
PricebookEntry

**Relationship Type**
Lookup

**Refers To**
PricebookEntry

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The price uplift policy associated with this order item.

This field is a relationship field.

**Relationship Name**
PriceRevisionPolicy

**Refers To**
PriceRevisionPolicy

Label is **Price Revision Policy** .

This field is available in Revenue Cloud in API version 65.0 and later.


Standard Objects OrderItem

**Field Name** **Details**

```
PricingTermCount

PricingTransactionType

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A calculated field indicating the number of pricing terms in the subscription.

This field is available in API version 55.0 and later. This field is available with
Subscription Management.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the type of pricing transaction. For example, a new sale, a cancellation,
an amendment, or a renewal.

Possible values:

**•** `AmendmentAtLastNegotiatedPrice` —Calculate the price of the
amended order item by using the same price book and price adjustments
as the new sale item. For example, an order item that is amended by using
a pricing transaction type of AmendmentAtLastNegotiatedPrice is priced by
using the same price book information and price adjustments as the new
sale item. The amended order item has the same price as the new sale order
item.

**•** `AmendmentStartingFromListPrice` —Calculate the price of the
amended order item by using current price book information, disregarding
any pricing information or adjustments that were applied to the new sale
item. Typically, an amended order item has a different price than the new
sale transaction item.

**•** `Cancellation` —Calculate the price of the canceled transaction. For
example, a 1-year subscription purchased on January 1, is canceled on July
31. The price of the canceled products and services from August 1 through
Dec 31 is calculated.

**•** `NewSale` —The price of a new transaction is calculated.

**•** `RenewalAtLastNegotiatedPrice` —Calculate the price of the order
item by using the same price book and price adjustments as the new sale
item. For example, an order item that is renewed by using a pricing transaction
type of `RenewalAtLastNegotiatedPrice` is priced by using the
same price book information and price adjustments as the new sale item.
The renewal order item has the same price as the new sale order item.

**•** `RenewalAtListPrice` —Calculate the price of the order item by using
current price book information, disregarding any pricing information or


Standard Objects OrderItem

**Field Name** **Details**

adjustments that were applied to the new sale item. Typically, a renewal
order item has a different price than the new sale order item.

This field is available in API version 55.0 and later. This field is available with
Subscription Management.

```
ProFormaBillingPeriodAmount

Product2Id

ProductSellingModelId

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The initial amount for the billing period. The final amount for the billing period
can include subsequent amendments, discounts, or charges.

This field is available in API version 55.0 and later. This field is available with
Subscription Management.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the Product2 associated with this OrderItem.

This field is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the related product selling model. The product selling model defines
one method by which a product is sold; for example, as a one-time sale, an
evergreen subscription, or a termed subscription.

This field is available in API version 55.0 and later. This field is available with
Subscription Management.

This field is a relationship field.


Standard Objects OrderItem

**Field Name** **Details**

**Relationship Name**
ProductSellingModel

**Relationship Type**
Lookup

**Refers To**
ProductSellingModel

```
ProrationPolicyId

Quantity

QuoteLineItemId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the related proration policy. The proration policy defines how the price
is calculated for each subscription period. For example, whether partial periods
are allowed, and how the remainder amounts are handled.

This field is available in API version 55.0 and later. This field is available with
Subscription Management.

This field is a relationship field.

**Relationship Name**
ProrationPolicy

**Relationship Type**
Lookup

**Refers To**
ProrationPolicy

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
Required. Number of units of this order product.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. ID of the associated quote line item.

If this field is specified, the quote line item’s QuoteId must match the QuoteId
for the order product’s parent order.


Standard Objects OrderItem

**Field Name** **Details**

```
ReferencePrice

RelatedChangeIdentifier

RelatedOrderItemID

RoundedLineAmount

RoundedLineAmtWithTax

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort

**Description**
The original or reference price of the order product.

This field is available in API version 63.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The identifier used to group all related order items in the same change order.

This field is available in API version 63.0 and later.

**Type**
reference

**Properties**
Create, Filter, Sort, Group

**Description**
Required for change orders, shows the original order product.

This field is available with Salesforce Order Management or Revenue Cloud.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Filter, Sort

**Description**
The rounded line amount, before tax and adjustments. Currency with decimal
values of 0.5 and higher round to the next-highest whole unit of currency.

The formula to calculate the rounded line amount is: IF(TotalLineAmount !=
NULL, TotalLineAmount, Quantity * UnitPrice)

This field is available with Salesforce Order Management or Revenue Cloud.

This field is available in API v48.0 and later.

**Type**
currency


Standard Objects OrderItem

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The rounded line amount, including tax. Currency with decimal values of 0.5 and
higher round to the next-highest whole unit of currency.

This field is available with Salesforce Order Management or Revenue Cloud.

This field is available in API v49.0 and later.

```
SegmentType

ServiceDate

ServiceDateTime

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The duration type of the segment. You can use this field from Revenue Cloud
only when the **Ramp Deals for Groups in Quotes and Orders** setting is turned
on.

Valid values are:

**•** `Custom` —Available in API version 65.0 and later.

**•** `Prorated` —Available in API version 67.0 and later.

**•** `Trial` —Available in API version 67.0 and later.

**•** `Yearly` —Available in API version 65.0 and later.

The default value is `Yearly` .

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Start date for the order product.

Label is **Start Date** .

**Type**
datetime

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The service date and time of the order item, which is derived from the Service
Date and Service Time fields in the time zone specified in the Service and End
Time Zone field. If the time zone isn't specified, the default is Coordinated
Universal Time (UTC).

Label is **Service Time** .


Standard Objects OrderItem

**Field Name** **Details**

This field is available in Revenue Cloud in API version 65.0 and later.

```
ServiceEndTimeZone

ServiceTime

StartingPriceTotal

StartingUnitPriceSource

```

**Type**
timeOnly

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the time zone for the order item's service and end dates, times, and
datetimes.

Label is **Service and End Time Zone** .

This field is available in Revenue Cloud in API version 65.0 and later.

**Type**
timeOnly

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The service time of the order item.

Label is **Service Time** .

This field is available in Revenue Cloud in API version 65.0 and later.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The starting unit price times the quantity.

This field is available in API version 55.0 and later. This field is available with
Subscription Management.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether the starting unit price was entered manually or calculated.

This field is available in API version 55.0 and later. This field is available with
Subscription Management.

Possible values are:

**•** `Manual`


Standard Objects OrderItem

**Field Name** **Details**

**•** `System`

```
SupplementalChangeType

TaxTreatmentId

TotalAdjustedLineTaxAmount

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the order item change type in the supplemental order.

Possible values are:

**•** `Add`

**•** `Amend`

**•** `Cancel`

**•** `No Change`

This field is available in API version 64.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the related tax treatment.

This field is available in API version 55.0 and later. This field is available with
Subscription Management.

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
Filter, Sort

**Description**
Sum of line tax amount and line adjustment tax amounts.

This field is available with Salesforce Order Management or Revenue Cloud.

This field is available in API v48.0 and later.


Standard Objects OrderItem

**Field Name** **Details**

```
TotalAdjustmentAmount

TotalAdjustmentAmtWithTax

TotalAdjustmentDistAmount

TotalAdjustmentDistTaxAmount

```

**Type**
currency

**Properties**
Filter, Sort

**Description**
Roll up of the order product’s price adjustments.

This field is available with Salesforce Order Management or Revenue Cloud.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Filter, Sort

**Description**
Roll up of the order product’s price adjustments, including tax.

This field is a gross tax field.

This field is available with Salesforce Order Management or Revenue Cloud.

This field is available in API v49.0 and later.

**Type**
currency

**Properties**
Filter, Sort

**Description**
Roll up of all adjustments on the order. Used only if the OrderAdjustmentGroup
has a Type value of Header.

This field is available with Salesforce Order Management or Revenue Cloud.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Filter, Sort

**Description**
Roll up of all adjustment tax amounts on the order. Used only if the
OrderAdjustmentGroup has a Type value of Header.

This field is available with Salesforce Order Management or Revenue Cloud.

This field is available in API v48.0 and later.


Standard Objects OrderItem

**Field Name** **Details**

```
TotalAdjustmentDistAmtWithTax

TotalAdjustmentTaxAmount

TotalAmtWithTax

TotalLineAdjustmentAmount

```

**Type**
currency

**Properties**
Filter, Sort

**Description**
Roll up of all adjustment tax amounts on the order, including tax. Used only if
the OrderAdjustmentGroup has a Type value of Header.

This field is a gross tax field.

This field is available with Salesforce Order Management or Revenue Cloud.

This field is available in API v49.0 and later.

**Type**
currency

**Properties**
Filter, Sort

**Description**
Sum of the order product’s tax adjustments.

This field is available with Salesforce Order Management or Revenue Cloud.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Equals `TotalPrice` + `TotalTaxAmount` for the order item.

This field is a gross tax field.

This field is available with Salesforce Order Management or Revenue Cloud.

This field is available in API v49.0 and later.

**Type**
currency

**Properties**
Filter, Sort

**Description**
The sum of line-level adjustments for the order product.

This field is available with Salesforce Order Management or Revenue Cloud.

This field is available in API v48.0 and later.


Standard Objects OrderItem

**Field Name** **Details**

```
TotalLineAdjustmentAmtWithTax

TotalLineAdjustmentTaxAmount

TotalLineAmount

TotalLineTaxAmount

```

**Type**
currency

**Properties**
Filter, Sort

**Description**
The sum of line-level adjustments for the order product, including tax.

This field is a gross tax field.

This field is available with Salesforce Order Management or Revenue Cloud.

This field is available in API v49.0 and later.

**Type**
currency

**Properties**
Filter, Sort

**Description**
Total tax amount for adjustments made to the order product.

This field is available with Salesforce Order Management or Revenue Cloud.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The line amount of the order product, before price adjustments, inclusive of
quantity, and pricing term count for subscription.

The decimal places for this value must match the decimal places for the currency
being used. For example, if the currency is the US dollar, the decimal place for
TotalLineAmount must be 2. If the currency is the Japanese yen, the decimal
place for TotalLineAmount must be 0.

This field is available with Salesforce Order Management or Revenue Cloud.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Filter, Sort

**Description**
Total tax amount for this order product, excluding tax on adjustments.

This field is available with Salesforce Order Management or Revenue Cloud.


Standard Objects OrderItem

**Field Name** **Details**

This field is available in API v48.0 and later.

```
TotalPrice

TotalTaxAmount

Type

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total price for this order product. The calculations for this field’s value are different
if Commerce Orders are enabled.

**Default Value**
`TotalPrice` = ( `UnitPrice`  - `Quantity)`

**Commerce or Revenue Cloud Orders**
If `TotalLineAmount` is null, then `TotalPrice` = ( `ROUND(UnitPrice`

   - `Quantity)` + `TotalAdjustmentAmount` . The `ROUND(UnitPrice`

   - `Quantity)` is stored in the `RoundedLineAmount` field. Otherwise,
`TotalPrice` = `ROUND(TotalLineAmount)` +
`TotalAdjustmentAmount` . The `ROUND(TotalLineAmount)` is also
stored in the `RoundedLineAmount` field.

This field is available with Salesforce Order Management or Revenue Cloud.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Filter, Sort

**Description**
Sum of the order product’s tax and any adjustments.

This field is available with Salesforce Order Management or Revenue Cloud.

This field is available in API v48.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Describes what the order item represents. Each value is associated with one type
code, shown here in parentheses.

Possible values are:

**•** `Delivery Charge (Charge)`  - A charge, such as a delivery fee.

**•** `Fee (Charge)`  - A charge, such as a return fee. This value is available
in API v56.0 and later.


Standard Objects OrderItem

**Field Name** **Details**

**•** `Order Product (Product)`                       - An item that can be ordered.

This field is available with Salesforce Order Management or Revenue Cloud.

This field is available in API v48.0 and later.

```
TypeCode

UnitPrice

UnitPriceUplift

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The category associated with the type. A type code can be associated with one
or more types.

Possible values are:

**•** `Charge`

**•** `Product`

This field is available with Salesforce Order Management or Revenue Cloud.

This field is available in API v48.0 and later.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Unit price for the order product.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage increase of the order item's unit price.

An order can have associated order product records only if the order has a price book associated with it. An order product must correspond
to a product that is listed in the order’s price book.

Orders with associated OrderItem records are affected. When OrderItem records are directly deleted, they aren’t sent to the recycle bin
and can’t be undeleted. The `getDeleted()` call shows deleted OrderItem records until they’re purged, which is usually within the
same day or the next day.


### Standard Objects OrderItemAdjustmentLineItem

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**OrderItemChangeEvent (API version 44.0)**
Change events are available for the object.

**OrderItemFeed (API version 29.0)**
Feed tracking is available for the object.

**OrderItemHistory**

History is available for tracked fields of the object.

SEE ALSO:

### Order

OrderItemSummary

### OrderItemAdjustmentLineItem

An adjustment that has been made to an order item. This object is available in API version 48.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

To access Commerce Orders entities, your org must have a Salesforce Order Management license. Commerce Orders entities are available
only in Lightning Experience.

Fields

**Field** **Details**

```
AdjustmentAmountScope

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Used with `AdjustmentValue` to determine the amount of the adjustment.

Possible values are:

**•** `Total` —The adjustment scope is the total price.

**•** `Unit` —The adjustment scope is the unit price.

**•** `UnproratedTotal` —The adjustment scope is the unprorated total price.


Standard Objects OrderItemAdjustmentLineItem

**Field** **Details**

```
AdjustmentBasisReferenceId

AdjustmentCauseId

AdjustmentSource

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
References the specific coupon applied.

This is a polymorphic relationship field.

**Relationship Name**
AdjustmentBasisReference

**Relationship Type**
Lookup

**Refers To**
Coupon

This field is available in API version 54.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
References the specific promotions applied.

This is a polymorphic relationship field.

**Relationship Name**
AdjustmentCause

**Relationship Type**
Lookup

**Refers To**
Promotion

This field is available in API version 52.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the origin of the adjustment.

Possible values are:

**•** `Discretionary` —The adjustment originates from a decision made by an individual,
for example, a manager’s discount granted to a client.


Standard Objects OrderItemAdjustmentLineItem

**Field** **Details**

**•** `Promotion` —The adjustment originates from a promotion, for example, a holiday
sale discount.

**•** `Rule` —Reserved for future use.

**•** `System` —The adjustment originates from the system, for example, a volume discount
after the amount of items reaches a specific number.

This field is available in API version 57.0 and later.

```
AdjustmentType

AdjustmentValue

Amount

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the type of mathematical adjustment to be applied to the order.

Possible values are:

**•** `AdjustmentAmount` —The adjustment is a numerical amount, for example, a cash
discount of 20.

**•** `AdjustmentPercentage` —The adjustment is a percentage amount, for example,
a 10% discount.

**•** `OverrideAmount` —The adjustment is a manual price override.

This field is available in API version 57.0 and later.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The specified `AdjustmentType` ’s amount to be applied to the order item.

For example, when the `AdjustmentType` value is `AdjustmentAmount`, the
`AdjustmentValue` is expected to equal the value of the `Amount` field.

When the `AdjustmentType` value is `AdjustmentPercentage`, the
`AdjustmentValue` represents the percentage number, and the `Amount` field’s value
will show the calculated adjustment amount.

This field is available in API version 57.0 and later.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The net total value of the adjustment line. The value is rounded to the nearest possible
amount associated with the currency of the order item.


Standard Objects OrderItemAdjustmentLineItem

**Field** **Details**

```
AppliedPromotionDate

CouponCode

CurrencyIsoCode

Description

Name

OrderAdjustmentGroupId

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time on which the promotion was applied to the asset.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the coupon code that was applied.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
any currency allowed by the organization. Default value is `USD` .

Possible values are:

**•** `USD` —U.S. Dollar

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Users can add a custom description to the record to provide additional detail.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the adjustment line.

**Type**
reference


Standard Objects OrderItemAdjustmentLineItem

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order adjustment group that contains the order item adjustment line item.

```
OrderId

OrderItemId

Priority

RelatedAdjustmentLineItemId

TotalAmtWithTax

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The parent order of the order item related to the adjustment line.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The order item that the adjustment line applies to.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A numeric value that represents the order of precedence of the order adjustment group.

It can also represent the order of precedence when applying the `AdjustmentType`
values. For example, an order can have two adjustments: a $100 discount and a 10% discount.
This field will tell the pricing engine which adjustment needs to be applied first.

This field is available in API version 57.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The original order item adjustment line. Useful for reference in change order scenarios.

**Type**
currency

**Properties**
Filter, Nillable, Sort


### Standard Objects OrderItemAdjustmentLineSummary

**Field** **Details**

**Description**
Equals the order item’s price plus `TotalTaxAmount` for the order item adjustment line
item.

This is a gross tax field.

To access Commerce Orders fields, your org must have a Salesforce Order Management
license. Commerce Orders fields are available only in Lightning Experience.

This field is available in API v49.0 and later.

```
TotalTaxAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The total amount of tax applied to the adjustment line.

### OrderItemAdjustmentLineSummary

Represents the current properties and state of price adjustments on an OrderItemSummary. Corresponds to one or more order item
adjustment line item objects, consisting of an original object and any change objects applicable to it. This object is available in API version
48.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is only available in Salesforce Order Management orgs or if the B2B Commerce license is enabled.

Fields

**Field** **Details**

```
AdjustmentBasisReferenceId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
References the specific coupon applied.


Standard Objects OrderItemAdjustmentLineSummary

**Field** **Details**

This is a polymorphic relationship field.

**Relationship Name**
AdjustmentBasisReference

**Relationship Type**
Lookup

**Refers To**
Coupon

This field is available in API version 54.0 and later.

```
AdjustmentCauseId

Amount

CurrencyIsoCode

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
References the specific promotions applied.

This is a polymorphic relationship field.

**Relationship Name**
AdjustmentCause

**Relationship Type**
Lookup

**Refers To**
Promotion

This field is available in API version 52.0 and later.

**Type**
currency

**Properties**
Filter, Sort

**Description**
Amount, not including tax, of the OrderItemAdjustmentLineSummary.

If the `OrderLifeCycleType` field on the associated OrderSummary is set to
UNMANAGED, then users with the Edit Unmanaged Order Summaries or B2B Commerce
Integrator user permission can modify this field.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
ISO code for the currency of the OrderItemSummary to which the adjustment applies. The
default value is USD.


Standard Objects OrderItemAdjustmentLineSummary

**Field** **Details**

Possible values are:

**•** `DKK` —Danish Krone

**•** `EUR` —Euro

**•** `GBP` —British Pound

**•** `USD` —U.S. Dollar

This field is available in API version 49.0 and later.

```
Description

Name

OrderAdjustmentGroup

SummaryId

OrderItemSummaryId

OrderSummaryId

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the OrderItemAdjustmentLineSummary.

This field can be edited.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the OrderItemAdjustmentLineSummary.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
If this object belongs to an OrderAdjustmentGroupSummary, this value is the ID of that
OrderAdjustmentGroupSummary.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the OrderItemSummary to which the OrderItemAdjustmentLineSummary applies.

**Type**
reference

**Properties**
Filter, Group, Sort


Standard Objects OrderItemAdjustmentLineSummary

**Field** **Details**

**Description**
ID of the OrderSummary associated with the OrderItemSummary to which this
OrderItemAdjustmentLineSummary applies.

```
 OriginalOrderItem

 AdjustmentLineItemId

Priority

 TotalAmtWithTax

 TotalTaxAmount

```

SEE ALSO:

OrderItemAdjustmentLineItem

OrderItemSummary

OrderItemTaxLineItemSummary

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the original OrderItemAdjustmentLine associated with this summary object. Nillable=true
only if the associated order summary is unmanaged. For managed order summaries,
nillable=false.

**Type**
integer

**Properties**
Create, Nillable

**Description**
Numerical rank used to apply promotions in the correct order.

This field is available in API version 52.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the adjustment, inclusive of tax. This amount is equal to Amount +
TotalTaxAmount.

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the Amount.


### Standard Objects OrderItemGroup OrderItemGroup

Stores the group information for line items in an order. It also stores the aggregated line field information (subtotal). It contains a
parent-child relationship to order. This object is available in API version 62.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

Fields

**Field** **Details**

```
Description

EndDate

Name

OrderId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the group.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Reserved for future use.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the group.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the order that this order product is a child of.


Standard Objects OrderItemGroup

**Field** **Details**

This field is a relationship field.

**Relationship Name**
Order

**Relationship Type**
Master-detail

**Refers To**
Order (the master object)

```
SegmentType

SortOrder

StartDate

SummarySubtotal

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The duration type of the segment. You can use this field from Revenue Cloud only when the
**Ramp Deals for Groups in Quotes and Orders** setting is turned on.

Valid values are:

**•** `Custom` —Available in API version 65.0 and later.

**•** `Prorated` —Available in API version 67.0 and later.

**•** `Trial` —Available in API version 67.0 and later.

**•** `Yearly` —Available in API version 65.0 and later.

The default value is `Yearly` .

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number indicating the sort order selected by the user.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Reserved for future use.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update


### Standard Objects OrderItemRecipient

**Field** **Details**

**Description**
The total amount of all the line items in the group.

```
Type

UnitPriceUplift

### OrderItemRecipient

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of the group.

Possible values are:

**•** `CPQOrderGroup` —CPQ Line Grouping

The default value is `CPQOrderGroup` .

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The percentage increase of the order item group's unit price.

Represents a site, employee, or other entity for which services are being ordered. This includes essential details such as the recipient's
name, contact information, and the specific site or location where the services will be provided. This object is available in API version
62.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
BroadbandConnectionType

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects OrderItemRecipient

**Field** **Details**

**Description**
The name of the broadband connection that's available at the address.

```
LastReferencedDate

LastViewedDate

MaxDownloadSpeed

MaxUploadSpeed

Name

OrderId

```

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
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum download speed available at the address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum upload speed available at the address.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the customer's site or location.

**Type**
reference


Standard Objects OrderItemRecipient

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The order associated with the recipient.

This field is a relationship field.

**Relationship Name**
Order

**Relationship Type**
Master-detail

**Refers To**
Order (the master object)

```
RecipientType

ServiceAddrValidationDate

Service Account

ServiceAddrValidationMsg

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the type of recipient of the order.

Possible values are:

**•** `Location`

**•** `Subscriber`

The default value is `Location` .

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when the address was validated.

**Type**
entityid

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Reference to the Account Entity where the product is used, serviced, or installed.

**Type**
string


Standard Objects OrderItemRecipient

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The message sent after the validation of the address.

```
ServiceAddrValidationResult

ServiceAddress

ServiceCity

ServiceCountry

ServiceGeocodeAccuracy

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the status of the address validation.

Possible values are:

**•** `Fail`

**•** `Partial Success`

**•** `Success`

The default value is `Success` .

**Type**
address

**Properties**
Filter

**Description**
The address where the recipient receives the order.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city where the recipient receives the order.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country where the recipient receives the order.

**Type**
picklist


Standard Objects OrderItemRecipient

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the accuracy level of the geocoded address coordinates.

Possible values are:

**•** `Address`

**•** `Block`

**•** `City`

**•** `County`

**•** `ExtendedZip` —Extended Zip

**•** `NearAddress` —Near Address

**•** `Neighborhood`

**•** `State`

**•** `Street`

**•** `Unknown`

**•** `Zip`

```
ServiceLatitude

ServiceLongitude

ServicePostalCode

ServiceState

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The latitude of the location where the recipient receives the order.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The longitude of the location where the recipient receives the order.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code of the address.

**Type**
string


Standard Objects OrderItemRecipient

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state where the recipient receives the order.

```
ServiceStreet

ServiceabilityCheckDate

ServiceabilityData

```

Associated Objects

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street where the recipient receives the order

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when the serviceability check was done.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The information about serviciability, such as broadband connection, download, and upload
speeds available at the address.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[OrderItemRecipientChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[OrderItemRecipientFeed](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[OrderItemRecipientHistory](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[OrderItemRecipientOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[OrderItemRecipientShare](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.


### Standard Objects OrderItemRelationship OrderItemRelationship

Describes a relationship between order products. This object is available in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Special Access Rules

This object is available when Subscription Management or Revenue Cloud is enabled.

Fields

**Field** **Details**

```
AssociatedOrderItemId

AssociatedOrderItemInventory

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The unique identifier of the associated order product.

This field is a relationship field. In a bundle relationship, this order product is the bundle
component.

**Relationship Name**
AssociatedOrderItem

**Relationship Type**
Lookup

**Refers To**
### OrderItem

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A static enum that describes the associated order item inventory in the
OrderItemSummaryRelationship.

Possible values are:

**•** IncludedInMainInventory—The child product’s inventory is included in the main
inventory.


Standard Objects OrderItemRelationship

**Field** **Details**

**•** NotIncludedInMainInventory—The child product’s inventory isn’t included in the main
inventory.

**Relationship Name**
AssociatedOrderItemInventory

```
AssociatedOrderItemPricing

AssociatedOrderItemRole

AssociatedQuantScaleMethod

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates how the associated order product is priced relative to the main order product. The
value is informative; the system doesn’t check whether the associated order product is
included in the bundle price.

Possible values are:

**•** `IncludedInBundlePrice` —The associated order product’s cost is $0 because
it’s included in the bundle’s price.

**•** `NotIncludedInBundlePrice` —The associated order product has a cost because
it’s not included in the bundle’s price.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Describes the position of the associated order product in the relationship.

Possible values are:

**•** `BundleComponent` —The associated order product is part of a bundle.

**•** `SetComponent` —The associated order product is part of a set.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
How the quantity of the associated order product scales, relative to the main order product.
The value is informative; the system doesn’t check whether the scaled quantities are correct.

Possible values are:

**•** `Constant`  - The associated order’s product quantity remains the same in relation to
the main order product’s quantity. For example, the main order product has a quantity
of one and the associated order product has a quantity of one.


Standard Objects OrderItemRelationship

**Field** **Details**

**•** `Proportional`                   - The associated order’s product quantity increases or decreases
based on the main order product’s quantity. For example, the main order product has
a quantity of one and the associated order product has a quantity of two. In other words,
there are two associated order products for every one main order product.

The default value is `Proportional` .

```
IsPriceInclusive

MainOrderItemId

MainOrderItemRole

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether child products are included in the root bundle price. If set to `true`, the
price of each child product is zero.

The default value is `false` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The main order product’s unique identifier.

This field is a relationship field. In a bundle relationship, this order product is the bundle
parent.

**Relationship Name**
MainOrderItem

**Relationship Type**
Lookup

**Refers To**
OrderItem

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the role of the main order product in the relationship.

Possible values are:

**•** `Bundle`  - The main order product is the bundle parent.

**•** `Set`  - The main order product is the set parent.

Subscription Management doesn’t support the `Set` value.


Standard Objects OrderItemRelationship

**Field** **Details**

```
Name

OrderId

ProductRelationshipTypeId

RootOrderItemId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the order product relationship.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the related order.

This field is a relationship field.

**Relationship Name**
Order

**Relationship Type**
Lookup

**Refers To**
Order

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique identifier of the record that describes the relationship between the main and
associated order products.

This field is a relationship field.

**Relationship Name**
ProductRelationshipType

**Relationship Type**
Lookup

**Refers To**
ProductRelationshipType

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort


