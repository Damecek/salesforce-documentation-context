**•** You need the “Customize Application” permission to edit this object.

**•** Your client application can't delete this object.

Fields

**Field** **Details**

```
ConversionRate

DecimalPlaces

IsActive

IsCorporate

```

**Type**
double

**Properties**
Filter

**Description**
Required. Conversion rate of this currency type against the corporate currency.

**Type**
int

**Properties**
Filter

**Description**
Required. For this currency, specifies the number of digits to the right of the decimal
point, such as zero ( `0` ) for JPY or `2` for USD.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether this currency type is active ( `true` ) or not ( `false` ). Inactive
currency types do not appear in picklists in the user interface. Label is **Active** . This
field defaults to `false` if no value is provided when updating or inserting a record.

**Type**
boolean


### Standard Objects CustExpIntlTransfSetup

**Field** **Details**

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether this currency type is the corporate currency ( `true` ) or not ( `false` ).
Label is **Corporate Currency** . All other currency conversion rates are applied against
this corporate currency. If a currency is already defined as the corporate currency in
the user interface, it can't be unset. When a non-corporate currency is set to a
corporate currency, the system reconfigures all conversion rates based on the new
corporate currency.

```
 IsoCode

```

Usage

**Type**
picklist

**Properties**
Filter, Restricted picklist

**Description**
Required. ISO code of the currency. Must be one of the valid alphabetic, three-letter
currency ISO codes defined by the ISO 4217 standard, such as `USD`, `GBP`, or `JPY` .
Must be unique within your organization. Label is **Currency ISO Code** .

This object is for multicurrency organizations only. Use this object to define the currencies your organization uses.

When updating an existing record, make sure to provide values for all fields to avoid undesired changes to the CurrencyType. For example,
if a value for `IsActive` is not provided, the default ( `false` ) is used, which could result in a currently active CurrencyType becoming
inactive.

SEE ALSO:

DatedConversionRate

Overview of Salesforce Objects and Fields

### CustExpIntlTransfSetup

Stores information for different data sources that are processed for customer insights. This object is available in API version 65.0 and
later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`


Standard Objects CustExpIntlTransfSetup

Fields

**Field** **Details**

```
DataSourceChannelName

DataSourceChannelType

IsDataProcessingPaused

IsEnabled

LastReferencedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the associated communication channel, such as Web, Email, Chat, or Voice.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Specifies the channel type as standard or custom.

Possible values are:

**•** `Custom`

**•** `Standard`

The default value is `Standard` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether data processing for the channel is temporarily paused ( `true` ). Use this
field to control channel operations without deactivating the channel.

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the channel is active for processing data ( `true` ).

The default value is `false` .

**Type**
dateTime


### Standard Objects CustomBrand

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when the current user last viewed or modified this record, a record related
to this record, or a list view. If this value is null, the current user has never viewed or modified
a record related to this object.

```
LastViewedDate

Name

ProcessingStartDate

### CustomBrand

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when the current user last viewed or modified this record. If this value is null,
the current user has never viewed or modified this record.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the Customer Experience Intelligence Transformer Setup record.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date to start processing data in the specified communication channel.

Represents a custom branding and color scheme. This object is available in API version 28.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

This object is available only when your org has digital experiences enabled.


### Standard Objects CustomBrandAsset

Fields

**Field Name** **Details**

```
ParentId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the parent entity that this branding applies to. The parent entity can
be an Experience Cloud site, organization, topic, or reputation level.

The branding applies to the entity that the `ParentId` references. For example,
if the `ParentId` references a network ID, the branding applies to that
Experience Cloud site only, and if the `ParentId` references an organization
ID, the branding applies to the organization that it is accessed through, and so
on. Label is `Branded Entity ID` .

Use this object along with CustomBrandAsset to apply a custom branding scheme to your Experience Cloud site. The branding scheme
for the site shows in both the user interface and in the Salesforce mobile app. You must have Create and Manage Experiences to customize
site branding.

You can also use this object to apply a custom branding scheme to your org when it is accessed through the Salesforce mobile app.

SEE ALSO:

Network

### CustomBrandAsset

Represents a branding element in a custom branding scheme. For example, a color, logo image, header image, or footer text. A
### CustomBrandAsset can apply to an Experience Cloud site or to an org using the Salesforce mobile app. This object is available in API

version 28.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

This object is available only when your org has digital experiences enabled.


Standard Objects CustomBrandAsset

Fields

**Field Name** **Details**

```
AssetCategory

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

Values include:

**•** `MotifZeronaryColor` —The background color for the header. Label
is `Zeronary motif color` .

If this CustomBrandAsset is for a network, this is the header color for the
network. If it is for an org, this is the header color when users access the
Salesforce mobile app.

**•** `MotifPrimaryColor` —The color used for the active tab. Label is
`Primary motif color` .

Not used for the Salesforce mobile app branding.

**•** `MotifSecondaryColor` —The color used for the top borders of lists
and tables. Label is `Secondary motif color` .

Not used for the Salesforce mobile app branding.

**•** `MotifTertiaryColor` —The background color for section headers on
edit and detail pages. Label is `Tertiary motif color` .

Not used for the Salesforce mobile app branding.

**•** `MotifQuaternaryColor` —If this CustomBrandAsset is for a network,
this is the background color for network pages. If it is for an org, this is the
background color on a splash page. Label is `Quaternary motif`
`color` .

**•** `MotifZeronaryComplementColor` —Font color used with
`zeronaryColor` . Label is `Zeronary motif colors`
`complement color` .

**•** `MotifPrimaryComplementColor` —Font color used with
`primaryColor` . Label is `Primary motif colors complement`
`color` .

Not used for the Salesforce mobile app branding.

**•** `MotifTertiaryComplementColor` —Font color used with
`tertiaryColor` . Label is `Tertiary motif colors`
`complement color` .

Not used for the Salesforce mobile app branding.


Standard Objects CustomBrandAsset

**Field Name** **Details**

**•** `MotifQuaternaryComplementColor` —Font color used with
`quaternaryColor` . Label is `Quaternary motif colors`
`complement color` .

Not used for the Salesforce mobile app branding.

**•** `PageHeader` —An image that appears on the header of the pages. Can
be an .html, .gif, .jpg, or .png file. Label is `Page Header` .

Not used for the Salesforce mobile app branding.

**•** `PageFooter` —An image that appears on the footer of the pages. Must
be an .html file. Label is `Page Footer` .

Not used for the Salesforce mobile app branding.

**•** `LoginFooterText` —The text that appears in the footer of the login
page. Label is `Footer text displayed on the login page` .

Not used for the Salesforce mobile app branding.

**•** `LoginLogoImageId` —The logo that appears on the login page for
external users. In the Salesforce mobile app, this logo also appears on the
Experience Cloud site splash page. Label is `Logo image displayed`
`on the login page` .

**•** `LargeLogoImageId` —Only used for the Salesforce mobile app. The
logo that appears on the splash page when you start the Salesforce mobile
app. Label is `Large logo image` .

**•** `SmallLogoImageId` —Only used for the Salesforce mobile app. The
logo that appears on the publisher in the Salesforce mobile app. Label is
`Small logo image` .

**•** `StaticLogoImageURL` —The logo that appears on the login page for
external users. Label is `Static logo image url` .

**•** `LoginQuaternaryColor` —The background color that appears on the
Experience Cloud site login page for external users. Label is `Login`
`background color` .

**•** `LoginRightFrameUrl` —The URL to the contents that appears on right
side of the Experience Cloud site login page for external users. Label is `Login`
`right frame url` .

**•** `LogoAssetId` —Navigation tile menu item images. Label is `Logo`
`asset image` .

**•** `LoginPrimaryColor` —The background color of the login button. Label
is `Login primary color` .

**•** `LoginBackgroundImageUrl` —The path to the image URL that
appears as the background on the Experience Cloud site’s login page. Label
is `Background image url` .

**•** `LargeLogoAssetId` —Navigational topic images. Label is `Large`
`logo asset image` .


Standard Objects CustomBrandAsset

**Field Name** **Details**

**•** `MediumLogoAssetId` —Featured topic images. Label is `Medium`
`logo asset image` .

```
AssetSourceId

CustomBrandId

ForeignKeyAssetId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

ID of the document uploaded to the Documents folder if the value of
`AssetCategory` is:

**•** `PageHeader`

**•** `PageFooter`

**•** `LoginLogoImageId`

**•** `LargeLogoImageId`

**•** `SmallLogoImageId`

ID of the content asset if the value of the `AssetCategory` is:

**•** `LogoAssetId`

**•** `LargeLogoAssetId`

**•** `MediumLogoAssetId`

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the associated CustomBrand .

This is a relationship field.

**Relationship Name**
CustomBrand

**Relationship Type**
Lookup

**Refers To**
CustomBrand

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects CustomFieldDisplayValue

**Field Name** **Details**

**Description**

This field was removed in API version 41.0, and is available in earlier versions for
backward compatibility only. Use `AssetSourceId` instead.

ID of the document used if the value of `AssetCategory` is `PageHeader`,
`PageFooter`, or `LoginLogoImageId` .

```
TextAsset

```

Usage

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Text used if the `AssetCategory` is `LoginFooterText` .

Use this object to add basic branding elements—color scheme, header or footer images, login page logo, or footer text—to the branding
scheme ( CustomBrand ) for your Experience Cloud site. You must have Create and Manage Experiences to customize site branding.

If you’re using digital experiences in the Salesforce mobile app, the loading page shows the logo.

SEE ALSO:

Network

### CustomFieldDisplayValue

Stores variation details for the product attribute item view. This object is available in API version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

### CustomFieldDisplayValue is available only if the B2B or D2C Commerce license is enabled.


Standard Objects CustomFieldDisplayValue

Fields

**Field** **Details**

```
Color

CurrencyIsoCode

CustomFieldDisplayId

Name

PickListApiValue

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The color variation in hexadecimal value format, for example `#FF0000` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The currency ISO code allowed by the organization. Possible value is:

**•** `USD` —U.S. Dollar

The default value is `USD` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the custom field display that this variation is associated with.

This field is a relationship field.

**Relationship Name**
CustomFieldDisplay

**Refers To**
CustomFieldDisplay

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the custom field display value.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


### Standard Objects CustomHelpMenuItem

**Field** **Details**

**Description**
The API name of the color variation picklist value, for example, `red_c` .

Usage

This object only gets populated when display type in the CustomFieldDisplay object is ColorSwatch.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as
CustomFieldDisplayValue.

**CustomFieldDisplayValueChangeEvent on page 68**
Change events are available for the object.

**CustomFieldDisplayValueFeed on page 55**
Feed tracking is available for the object.

**CustomFieldDisplayValueHistory on page 63**
History is available for tracked fields of the object.

### CustomHelpMenuItem

Represents the items within a section of the Lightning Experience help menu that the admin added to display custom, org-specific help
resources. This object is available in API version 44.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Packaging Considerations

Although you can package custom Help Menu section information, the section won't appear in the Help Menu Setup page or the Help
Menu user interface of orgs where the package is installed. Instead, customers must view the data in the CustomHelpMenuItem and
CustomHelpMenuSection objects and then manually add resources on the Help Menu Setup page.

Fields

**Field** **Details**

```
LinkUrl

```

**Type**
url

**Properties**
Create, Filter, Sort, Update


### Standard Objects CustomHelpMenuSection

**Field** **Details**

**Description**
Required. The URL for the resource. Specify up to 1,000 characters.

```
MasterLabel

ParentId

SortOrder

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The name of the resource. Specify up to 100 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the custom help section the item belongs to.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
### CustomHelpMenuSection

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The order of the item within the custom section. Valid values are 1 through 15.

### CustomHelpMenuSection

Represents a section of the Lightning Experience help menu that the admin added to display custom, org-specific help resources. This
object is available in API version 44.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects CustomHelpMenuSection

Packaging Considerations

Although you can package custom Help Menu section information, the section won't appear in the Help Menu Setup page or the Help
Menu user interface of orgs where the package is installed. Instead, customers must view the data in the CustomHelpMenuItem and
CustomHelpMenuSection objects and then manually add resources on the Help Menu Setup page.

Fields

**Field** **Details**

```
DeveloperName

Language

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the custom help section in the API. This name can contain only
underscores and alphanumeric characters and must be unique in your organization. It must
begin with a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. The label corresponds to section title in the user interface. Limit:
80 characters.

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance slows down while
Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Required. Language of the label. Possible values are:

**•** da (Danish)

**•** de (German)

**•** en_US (English)

**•** es (Spanish)

**•** es_MX (Spanish (Mexico))

**•** fi (Finnish)

**•** fr (French)

**•** it (Italian)

**•** ja (Japanese)

**•** ko (Korean)

**•** nl_NL (Dutch)


### Standard Objects CustomHttpHeader

**Field** **Details**

**•** no (Norwegian)

**•** pt_BR (Portuguese (Brazil))

**•** ru (Russian)

**•** sv (Swedish)

**•** th (Thai)

**•** zh_CN (Chinese (Simplified))

**•** zh_TW (Chinese (Traditional))

```
MasterLabel

NamespacePrefix

### CustomHttpHeader

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The name of the resource. Specify up to 100 characters.

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

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

Represents a custom HTTP header that provides context information from Salesforce such as region, org details, or the role of the person
viewing the external object. This object is available in API version 43.0 and later.


Standard Objects CustomHttpHeader

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

As of Spring ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field Name** **Details**

```
Description

HeaderFieldName

HeaderFieldValue

IsActive

ParentId

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
A text description of the header field’s purpose.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Name of the header field. The name must contain at least one alphanumeric character or
underscore. It can also include: ! # $ % & ' * + - . ^ _ ` | ~

**Type**
string

**Properties**
Filter, Sort

**Description**
A formula that resolves to the value for the header. The values in the formula must evaluate
to a string. If the formula resolves to null and an empty string, the header isn’t sent.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the custom HTTP header is available to use.

**Type**
reference


### Standard Objects CustomMsgChannel

**Field Name** **Details**

**Properties**
Filter, Group, Sort

**Description**
ID of the entity that the custom HTTP header is related to.

This is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
ExternalDataSource, NamedCredential

Usage

For each OData external data source, define up 10 HTTP headers to request data.

Note: HTTP headers aren’t supported on named credentials.

### CustomMsgChannel

Represents a custom conversation channel and stores event-driven Messaging settings. Custom conversation channels are implemented
for Bring Your Own Channel for Messaging and Bring Your Own Channel for CCaaS Messaging channels. This object is available in API
version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

Access to standard objects requires Salesforce admin privileges or the Customize Application permission.

Fields

**Field** **Details**

```
ChannelDefinitionId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects CustomMsgChannel

**Field** **Details**

**Description**
Specifies the ConversationChannelDefinition for the custom channel.

This field is a relationship field.

**Relationship Name**
ChannelDefinition

**Refers To**
ConversationChannelDefinition

```
EventCapabilitiesIsInboundAcknowledgementEnabled

EventCapabilitiesIsProgressIndicatorEnabled

EventCapabilitiesIsTypingIndicatorDisabled

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the Salesforce admin has enabled read receipts and delivery receipts for
inbound messages in the Messaging settings ( `true` ) or whether the admin hasn’t enabled
these inbound acknowledgments ( `false` ). The default value is `false`, meaning inbound
acknowledgments are disabled by default even if supported by the partner.

This field is available in API version 65.0 and later. Use this field instead of
`HasInboundReceipts` .

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the Salesforce admin has enabled AI agent progress indicators in the
Messaging settings ( `true` ) or whether the admin hasn’t enabled progress indicators
( `false` ). The default value is `false`, meaning progress indicators for AI agents are disabled
by default even if supported by the partner.

This field is available in API version 65.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the Salesforce admin has enabled typing indicators for outbound messages
in the Messaging settings ( `false` ) or whether the admin hasn’t enabled outbound typing
indicators ( `true` ). The default value is `false`, meaning the outbound typing indicators
are enabled by default.

This field is available in API version 65.0 and later. Use this field instead of
`HasTypingIndicator` .


### Standard Objects CustomNotificationType

**Field** **Details**

```
HasInboundReceipts

HasTypingIndicator

MessagingChannelId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Salesforce admin has enabled read receipts and delivery receipts for
inbound messages in the Messaging settings ( `true` ) or whether the admin hasn’t enabled
these inbound acknowledgments ( `false` ). The default value is `false`, meaning inbound
acknowledgments are disabled by default even if supported by the partner.

Available in API versions 63.0 to 65.0. In API version 66.0 and later, this field is removed. Use
`EventCapabilitiesIsInboundAcknowledgementEnabled` instead.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Salesforce admin has enabled typing indicators for outbound messages
in the Messaging settings ( `true` ) or whether the admin hasn’t enabled outbound typing
indicators ( `false` ). The default value is `true`, meaning the outbound typing indicator
feature is enabled by default if supported by the partner. To disable the outbound typing
indicator feature, set this value to `false` .

Available in API versions 63.0 to 65.0. In API version 66.0 and later, this field is removed. Use
`EventCapabilitiesIsTypingIndicatorDisabled` instead.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Specifies the Messaging Channel ID for the custom channel. This field is unique within your
organization.

This field is a relationship field.

**Relationship Name**
MessagingChannel

**Refers To**
MessagingChannel

### CustomNotificationType

Stores information about custom notification types. This object is available in API version 47.0 and later.


Standard Objects CustomNotificationType

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CustomNotifTypeName

Description

Desktop

DeveloperName

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Unique, Update

**Description**
Specifies a notification type name. The notification type name is unique within your
organization. The notification type name isn’t namespaced, so it can’t be duplicated across
installed packages. Maximum number of characters: 80.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies a general description of the notification type, which is displayed with the notification
type name. Maximum number of characters: 255.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the desktop delivery channel is enabled ( `true` ) or not ( `false` ). The
default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Specifies the API name of the notification type.


### Standard Objects CustomPermission

**Field** **Details**

```
IsSlack

Language

MasterLabel

Mobile

NamespacePrefix

### CustomPermission

```

**Type**
boolean

**Properties**
Reserved for future use.

**Description**
Reserved for future use.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the language of the custom notification type. The value for this field is the language
value of the org.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Specifies the notification type label.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the mobile delivery channel is enabled ( `true` ) or not ( `false` ). The
default value is `false` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Specifies the namespace of the notification type, if installed with a managed package.

Represents a permission created to control access to a custom process or app, such as sending email. This object is available in API
version 31.0 and later.


Standard Objects CustomPermission

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

As of Summer ’20 and later, only users who have one of these permissions can access this object:

**•** View Setup and Configuration

**•** Manage Session Permission Set Activations

**•** Assign Permission Sets

Fields

**Field Name** **Details**

```
Description

DeveloperName

IsLicensed

```

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
A description of the custom permission. Limit: 255 characters.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name of the custom permission in the API. This name can contain
only underscores and alphanumeric characters and must be unique in your
organization. It must begin with a letter, not include spaces, not end with an
underscore, and not contain two consecutive underscores. The label corresponds
to **Name** in the user interface. Limit: 80 characters.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is specified,
performance may slow while Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects CustomPermission

**Field Name** **Details**

**Description**
When enabled (true) indicates that the appropriate Salesforce license is required
before accessing the permission. This field is available in API version 50.0 and
later.

```
IsProtected

Language

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the custom permission is protected ( `true` ) or not ( `false` ).
Protected components that have been installed in other organizations can’t be
linked to or referenced by components created in the subscriber organization.
A developer can delete a protected component contained in a managed package
in a future release of the package without worrying about failing installations.
However, after a component is marked as unprotected and is released globally,
the developer can’t delete it. The default value is `false` . This field is available
in API version 50.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the custom permission. Valid values are:

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


Standard Objects CustomPermission

**Field Name** **Details**

**•** Spanish (Mexico): `es_MX` Spanish (Mexico) defaults to Spanish for
customer-defined translations.

**•** Swedish: `sv`

**•** Thai: `th` The Salesforce user interface is fully translated to Thai, but Help is
in English.

```
MasterLabel

NamespacePrefix

```

Usage

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The custom permission label, which corresponds to **Label** in the user interface.
Limit: 80 characters.

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

Use the CustomPermission object to determine users’ access to custom permissions.

For example, to query all permission sets where the Button1 permission is enabled:

```
SELECT Id, DeveloperName,

(select Id, Parent.Name, Parent.Profile.Name from SetupEntityAccessItems)

FROM CustomPermission

WHERE DeveloperName = 'Button1'

```


### Standard Objects CustomPermissionDependency

To query all permission sets and profiles with custom permissions:

```
   SELECT Assignee.Name, PermissionSet.Id,

   PermissionSet.Profile.Name,

   PermissionSet.isOwnedByProfile,

   PermissionSet.Label

   FROM PermissionSetAssignment

   WHERE PermissionSetId

   IN (SELECT ParentId

     FROM SetupEntityAccess

     WHERE SetupEntityType =

   'CustomPermission')

```

To query for all SetupEntityAccess rows with custom permissions:

```
   SELECT Id,ParentId,Parent.Name, SetupEntityId

   FROM SetupEntityAccess

   WHERE SetupEntityType='CustomPermission'

   AND ParentId

   IN (SELECT Id

     FROM PermissionSet

     WHERE isOwnedByProfile = false)

```

SEE ALSO:

### CustomPermissionDependency

PermissionSet

Profile

SetupEntityAccess

### CustomPermissionDependency

Represents the dependency between two custom permissions when one custom permission requires that you enable another custom
permission. This object is available in API version 32.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

As of Spring ’20 and later, only users with View Setup and Configuration permission can access this object.

Fields

**Field Name** **Details**

```
CustomPermissionId

```

**Type**
reference


Standard Objects CustomPermissionDependency

**Field Name** **Details**

**Properties**
Filter, Group, Sort

**Description**
The ID of the custom permission that requires the permission that’s specified in
`RequiredCustomPermissionId` .

This is a relationship field.

**Relationship Name**
CustomPermission

**Relationship Type**
Lookup

**Refers To**
CustomPermission

```
RequiredCustomPermissionId

```

Usage

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the custom permission that must be enabled when
`CustomPermissionId` is enabled.

This is a relationship field.

**Relationship Name**
RequiredCustomPermission

**Relationship Type**
Lookup

**Refers To**
CustomPermission

The following Apex class contains a method that returns the IDs of all custom permissions that are required for the given custom
permission ID. To use this class, save it in your organization.

```
public class CustomPermissionUtil {

  public String[] getAllRequiredCustomPermissions(String customPermId) {

    return getAllRequiredHelper(new String[]{customPermId});

  }

  private String[] getAllRequiredHelper(String[] customPermIds) {

    CustomPermissionDependency[] requiredPerms = [SELECT RequiredCustomPermissionId

                                FROM CustomPermissionDependency

                                WHERE CustomPermissionId

                                IN :customPermIds];

```


### Standard Objects Customer

```
       String[] requiredPermIds = new String[]{};

       for (CustomPermissionDependency cpd : requiredPerms) {

         requiredPermIds.add(cpd.RequiredCustomPermissionId);

       }

       if (requiredPermIds.size() > 0) {

         customPermIds.addall(getAllRequiredHelper(requiredPermIds));

         return customPermIds;

       } else {

         return customPermIds;

       }

     }

   }

```

[For more information about using Apex classes, see the Apex Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_dev_guide.htm)

SEE ALSO:

CustomPermission

### Customer

Represents the customer role of an individual with respect to a particular company or organization. This object is available in API version
53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

### `CustomerStatusType`

```
LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the customer account.

Possible values are:

**•** `Active`

**•** `Inactive`

**Type**
dateTime


Standard Objects Customer

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

```
LastViewedDate

Name

OwnerId

PartyId

```

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
Required. Name of this customer.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who owns the record.

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
Required. Represents the individual object related to this customer record.

This is a relationship field.


### Standard Objects DandBCompany

**Field** **Details**

**Relationship Name**
Party

**Relationship Type**
Lookup

**Refers To**
Individual

```
TotalLifeTimeValue

### DandBCompany

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total revenue amount gained from this customer.

Represents a Dun & Bradstreet [®] company record, which is associated with an account added from Data.com. This object is available in
API version 25.0 and later.

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields will be removed
from your org.

To support customers’ needs around compliance and to remain a leader in trust and privacy, Salesforce removed all contact data
from the Data.com service on February 1, 2021.

[For more information, see Data.com Prospector and Clean Retirement.](https://help.salesforce.com/articleView?id=000270376&language=en_US&type=1)

Warning: You can update fields in the DandBCompany object; however, field changes may be overwritten by Data.com Clean
jobs or by using the Data.com Clean button.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Only organizations with Data.com Premium Prospector or Data.com Premium Clean can access this object.


Standard Objects DandBCompany

Fields

**Field Name** **Details**

```
Address

City

CompanyCurrencyIsoCode

Country

CountryAccessCode

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
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city where a company is physically located. Maximum size is 40 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The code used to represent a company’s local currency. This data is provided by
the International Organization for Standardization (ISO) and is based on their
three-letter currency codes. For example, USD is the ISO code for United States
Dollar. Maximum size is 3 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country where a company is physically located. Maximum size is 40 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The required code for international calls. Maximum size is 4 characters.


Standard Objects DandBCompany

**Field Name** **Details**

```
CurrencyCode

Description

DomesticUltimateBusinessName

DomesticUltimateDunsNumber

DunsNumber

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The currency in which the company’s sales volume is expressed. The full list of
values can be found at the Optimizer Resources page maintained by Dun &
Bradstreet. Maximum size is 4 characters.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A brief description of the company, which may include information about its
history, its products and services, and its influence on a particular industry.
Maximum size is 32000 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The primary name of the Domestic Ultimate, which is the highest ranking
subsidiary, specified by country, within an organization’s corporate structure.
Maximum size is 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The D-U-N-S Number for the Domestic Ultimate, which is the highest ranking
subsidiary, specified by country, within an organization’s corporate structure.
Maximum size is 9 characters.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects DandBCompany

**Field Name** **Details**

**Description**
The Data Universal Numbering System (D-U-N-S) number is a unique, nine-digit
number assigned to every business location in the Dun & Bradstreet database
that has a unique, separate, and distinct operation. D-U-N-S numbers are used
by industries and organizations around the world as a global standard for business
identification and tracking. Maximum size is 9 characters.

```
EmployeeQuantityGrowthRate

EmployeesHere

EmployeesHereReliability

EmployeesTotal

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The yearly growth rate of the number of employees in a company expressed as
a decimal percentage. The data includes the total employee growth rate for the
past two years.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The number of employees at a specified location, such as a branch location.
Maximum size is 15 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The reliability of the `EmployeesHere` figure. Available values include:

**•** 0—Actual number

**•** 1—Low

**•** 2—Estimated (for all records)

**•** 3—Modeled (for non-US records)

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The total number of employees in the company, including all subsidiary and
branch locations. This data is only available on records that have a value of


Standard Objects DandBCompany

**Field Name** **Details**

_`Headquarters/Parent`_ in the `LocationStatus` field. Maximum size
is 15 characters.

```
EmployeesTotalReliability

FamilyMembers

Fax

FifthNaics

FifthNaicsDesc

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The reliability of the `EmployeesTotal` figure. Available values include:

**•** 0—Actual number

**•** 1—Low

**•** 2—Estimated (for all records)

**•** 3—Modeled (for non-US records)

A blank value indicates this data is unavailable.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of family members, worldwide, within an organization, including
the Global Ultimate, its subsidiaries (if any), and its branches (if any). Maximum
size is 5 characters.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The company’s facsimile number.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional NAICS code used to further classify an organization by industry.
Maximum size is 6 characters.

**Type**
string


Standard Objects DandBCompany

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding NAICS code. Maximum size is 120 characters.

```
FifthSic

FifthSic8

FifthSic8Desc

FifthSicDesc

FipsMsaCode

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects DandBCompany

**Field Name** **Details**

**Description**
The Federal Information Processing Standards (FIPS) and the Metropolitan
Statistical Area (MSA) codes identify the organization’s location. The MSA codes
are defined by the US Office of Management and Budget. Maximum size is 5
characters.

```
FipsMsaDesc

FortuneRank

FourthNaics

FourthNaicsDesc

FourthSic

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s FIPS MSA code. Maximum size is 255
characters.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The numeric value of the company’s Fortune 1000 ranking. A null or blank value
means that the company isn’t ranked as a Fortune 1000 company.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional NAICS code used to further classify an organization by industry.
Maximum size is 6 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding NAICS code. Maximum size is 120 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects DandBCompany

**Field Name** **Details**

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

```
FourthSic8

FourthSic8Desc

FourthSicDesc

GeoCodeAccuracy

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The level of accuracy of a location’s geographical coordinates compared with its
physical address. Available values include:

**•** A – _`Non-US rooftop accuracy`_

**•** B – _`Block level`_

**•** C – _`Places the address in the correct city`_

**•** D – _`Rooftop level`_

**•** I – _`Street intersection`_

**•** M – _`Mailing address level`_


Standard Objects DandBCompany

**Field Name** **Details**

**•** N – _`Not matched`_

**•** P – _`PO BOX location`_

**•** S – _`Street level`_

**•** T – _`Census tract level`_

**•** Z – _`ZIP code level`_

**•** 0 (zero)– _`Geocode could not be assigned`_

```
GlobalUltimateBusinessName

GlobalUltimateDunsNumber

GlobalUltimateTotalEmployees

ImportExportAgent

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The primary name of the Global Ultimate, which is the highest entity within an
organization’s corporate structure and may oversee branches and subsidiaries.
Maximum size is 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The D-U-N-S Number of the Global Ultimate, which is the highest entity within
an organization’s corporate structure and may oversee branches and subsidiaries.
Maximum size is 9 characters.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The total number of employees at the Global Ultimate, which is the highest entity
within an organization’s corporate structure and may oversee branches and
subsidiaries. Maximum size is 15 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Identifies whether a business imports goods or services, exports goods or services,
and/or is an agent for goods. Available values include:

**•** A—Importer/exporter/agent


Standard Objects DandBCompany

**Field Name** **Details**

**•** B—Importer/exporter

**•** C—Importer

**•** D—Importer/agent

**•** E—Exporter/agent

**•** F—Agent (keeps no inventory and does not take title goods)

**•** G—None or data not available

**•** H—Exporter

```
IncludedInSnP500

Latitude

LegalStatus

LocationStatus

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A true or false value. If `true`, the company is listed in the S&P 500 Index. If
`false`, the company isn’t listed in the S&P 500 Index.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Used with longitude to specify a precise location, which is then used to assess
the Geocode Accuracy. Maximum size is 11 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Identifies the legal structure of an organization.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Identifies the organizational status of a company. Available values are _`Single`_
_`location`_, _`Headquarters/Parent`_, and _`Branch`_ . Available values
include:

**•** 0—Single location (no other entities report to the business)

**•** 1—Headquarters/parent (branches and/or subsidiaries report to the business)


Standard Objects DandBCompany

**Field Name** **Details**

**•** 2—Branch (secondary location to a headquarters location)

```
Longitude

MailingAddress

MailingCity

MailingCountry

MailingPostalCode

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Used with latitude to specify a precise location, which is then used to assess the
Geocode Accuracy. Maximum size is 11 characters.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the mailing address. Read-only. See Address Compound
Fields for details on compound address fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city where a company has its mail delivered. Maximum size is 40 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country where a company has its mail delivered. Maximum size is 40
characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code that a company uses on its mailing address. Maximum size is 20
characters.


Standard Objects DandBCompany

**Field Name** **Details**

```
MailingState

MailingStreet

MarketingPreScreen

MarketingSegmentationCluster

MinorityOwned

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state where a company has its mail delivered. Maximum size is 20 characters.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street address where a company has its mail delivered. Maximum size is 255
characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The probability that a company will pay with a significant delay compared to the
agreed terms. The risk level is based on the standard Commercial Credit Score,
and ranges from low risk to high risk. Available values include:

**•** L— _`Low risk of delinquency`_

**•** M— _`Moderate risk of delinquency`_

**•** H— _`High risk of delinquency`_

Important: Use this information for marketing pre-screening purposes
only.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Twenty-two distinct, mutually exclusive profiles, created as a result of cluster
analysis of Dun & Bradstreet data for US organizations.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects DandBCompany

**Field Name** **Details**

**Description**
Indicates whether an organization is owned or controlled by a member of a
minority group. Available values include:

**•** Y—Minority owned

**•** N—Not minority owned

```
Name

NationalId

NationalIdType

OutOfBusiness

OwnOrRent

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The primary or registered name of a company. Maximum size is 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The identification number used in some countries for business registration and
tax collection. Maximum size is 255 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
A code value that identifies the type of national identification number used. The
full list of resources can be found at the Optimizer Resources page maintained
by Dun & Bradstreet. Maximum size is 5 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether the company at the specified address has discontinued
operations. Available values include:

**•** Y—Out of business

**•** N—Not out of business

**Type**
picklist


Standard Objects DandBCompany

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether a company owns or rents the building it occupies. Available
values include:

**•** 0—Unknown or not applicable

**•** 1—Owns

**•** 2—Rents

```
ParentOrHqBusinessName

ParentOrHqDunsNumber

Phone

PostalCode

PremisesMeasure

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The primary name of the parent or headquarters company. Maximum size is 255
characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The D-U-N-S Number for the parent or headquarters. Maximum size is 9 characters.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A company’s primary telephone number.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code that corresponds to a company’s physical location. Maximum
size is 20 characters.

**Type**
int


Standard Objects DandBCompany

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A numeric value for the measurement of the premises.

```
PremisesMeasureReliability

PremisesMeasureUnit

PrimaryNaics

PrimaryNaicsDesc

PrimarySic

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A descriptive accuracy of the measurement such as actual, estimated, or modeled.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A descriptive measurement unit such as acres, square meters, or square feet.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The six-digit North American Industry Classification System (NAICS) code is the
standard used by business and government to classify business establishments
according to their economic activity for the purpose of collecting, analyzing, and
publishing statistical data related to the US business economy. The full list of
values can be found at the Optimizer Resources page maintained by Dun &
Bradstreet. Maximum size is 6 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on its NAICS code.
Maximum size is 120 characters.

**Type**
string


Standard Objects DandBCompany

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The four-digit Standard Industrial Classification (SIC) code is used to categorize
business establishments by industry. The full list of values can be found at the
Optimizer Resources page maintained by Dun & Bradstreet. Maximum size is 4
characters.

```
PrimarySic8

PrimarySic8Desc

PrimarySicDesc

PriorYearEmployees

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The eight-digit Standard Industrial Classification (SIC) code is used to categorize
business establishments by industry. The full list of values can be found at the
Optimizer Resources page maintained by Dun & Bradstreet. Maximum size is 8
characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on its SIC code.
The full list of values can be found at the Optimizer Resources page maintained
by Dun & Bradstreet. Maximum size is 80 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on its SIC code.
Maximum size is 80 characters.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of employees for the prior year.


Standard Objects DandBCompany

**Field Name** **Details**

```
PriorYearRevenue

PublicIndicator

SalesTurnoverGrowthRate

SalesVolume

SalesVolumeReliability

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The annual revenue for the prior year.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether ownership of the company is public or private. Available values
include:

**•** Y—Public

**•** N—Private

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The increase in annual revenue from the previous value for an equivalent period
expressed as a decimal percentage.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The total annual sales revenue in the headquarters’ local currency. Dun &
Bradstreet tracks revenue data for publicly traded companies, Global Ultimates,
Domestic Ultimates, and some headquarters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The reliability of the `SalesVolume` figure. Available values include:

**•** 0—Actual number


Standard Objects DandBCompany

**Field Name** **Details**

**•** 1—Low

**•** 2—Estimated (for all records)

**•** 3—Modeled (for non-US records)

```
SecondNaics

SecondNaicsDesc

SecondSic

SecondSic8

SecondSic8Desc

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional NAICS code used to further classify an organization by industry.
Maximum size is 6 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding NAICS code. Maximum size is 120 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects DandBCompany

**Field Name** **Details**

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

```
SecondSicDesc

SixthNaics

SixthNaicsDesc

SixthSic

SixthSic8

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional NAICS code used to further classify an organization by industry.
Maximum size is 6 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding NAICS code. Maximum size is 120 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects DandBCompany

**Field Name** **Details**

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

```
SixthSic8Desc

SixthSicDesc

SmallBusiness

State

StockExchange

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether the company is designated a small business as defined by the
Small Business Administration of the US government. Available values include:

**•** Y—Small business site

**•** N—Not small business site

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state where a company is physically located. Maximum size is 20 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects DandBCompany

**Field Name** **Details**

**Description**
The corresponding exchange for a company’s stock symbol. For example: NASDAQ
or NYSE. Maximum size is 16 characters.

```
StockSymbol

Street

Subsidiary

ThirdNaics

ThirdNaicsDesc

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The abbreviation used to identify publicly traded shares of a particular stock.
Maximum size is 6 characters.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street address where a company is physically located. Maximum size is 255
characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether a company is more than 50 percent owned by another
organization. Available values include:

**•** 0—Not subsidiary of another organization

**•** 3—Subsidiary of another organization

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional NAICS code used to further classify an organization by industry.
Maximum size is 6 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects DandBCompany

**Field Name** **Details**

**Description**
A brief description of an organization’s line of business, based on the
corresponding NAICS code. Maximum size is 120 characters.

```
ThirdSic

ThirdSic8

ThirdSic8Desc

ThirdSicDesc

TradeStyle1

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects DandBCompany

**Field Name** **Details**

**Description**
A name, different from its legal name, that an organization may use for conducting
business. Similar to “Doing business as” or “DBA”. Maximum size is 255 characters.

```
TradeStyle2

TradeStyle3

TradeStyle4

TradeStyle5

URL

UsTaxId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional tradestyle used by the organization. Maximum size is 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional tradestyle used by the organization. Maximum size is 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional tradestyle used by the organization. Maximum size is 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional tradestyle used by the organization. Maximum size is 255 characters.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An organization’s primary website address. Maximum size is 104 characters.

**Type**
string


### Standard Objects Dashboard

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The identification number for the company used by the Internal Revenue Service
(IRS) in the administration of tax laws. Also referred to as Federal Taxpayer
Identification Number. Maximum size is 9 characters.

```
WomenOwned

YearStarted

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether a company is more than 50 percent owned or controlled by
a woman. Available values include:

**•** Y—Owned by a woman

**•** N—Not owned by a woman, or unknown

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The year the company was established or the year when current ownership or
management assumed control of the company. Maximum size is 4 characters.

Use this object to manage D&B Company records in your organization.

### Dashboard

Represents a dashboard, which shows data from custom reports as visual components. Access is read-only. This object is available in
API version 20.0 and later.

Supported Calls

`describeSObjects()`, `describeLayout()`, `query()`, `retrieve()`, `search()`


Standard Objects Dashboard

Fields

**Field** **Details**

```
BackgroundDirection

BackgroundEnd

BackgroundStart

ChartTheme

ColorPalette

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Returns the direction of the background fade. Available values are:

**•** `Top to Bottom`

**•** `Left to Right`

**•** `Diagonal` (default value)

Label is `Background Fade Direction` .

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Returns the ending fade color in hexadecimal. Label is `Ending Color` .

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Returns the starting fade color in hexadecimal. Label is `Starting Color` .

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Returns the background theme used for charts.

Possible values are:

**•** `dark` —Dark Background

**•** `light` —Light Background

**Type**
picklist


Standard Objects Dashboard

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Returns the color palette used for the dashboard.

Possible values are:

**•** `Default` —Default Palette

**•** `accessible` —Mineral(Accessible) Palette

**•** `bluegrass` —Bluegrass Palette

**•** `colorSafe` —Color Safe Palette

**•** `dusk` —Dusk Palette

**•** `earth` —Lake Palette

**•** `fire` —Fire Palette

**•** `gray` —Gray Palette

**•** `heat` —Heat Palette

**•** `justice` —Wildflowers Palette

**•** `nightfall` —Nightfall Palette

**•** `pond` —Pond Palette

**•** `sunrise` —Sunrise Palette

**•** `tropic` —Ocean Palette

**•** `unity` —Aurora Palette

**•** `water` —Water Palette

**•** `watermelon` —Watermelon Palette

```
DashboardResultRefreshedDate

DashboardResultRunningUser

Description

```

**Type**
string

**Properties**
Nillable

**Description**
Returns the date on which the dashboard results were last refreshed.

**Type**
string

**Properties**
Nillable

**Description**
The user whose security settings were used to generate the dashboard results.

**Type**
string


Standard Objects Dashboard

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Returns the description of the dashboard. Limit: 255 characters.

```
DeveloperName

FolderId

FolderName

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Required. The unique name of the object in the API. This name can contain only
underscores and alphanumeric characters, and must be unique in your org. It
must begin with a letter, not include spaces, not end with an underscore, and
not contain two consecutive underscores. In managed packages, this field
prevents naming conflicts on package installations. With this field, a developer
can change the object’s name in a managed package and the changes are
reflected in a subscriber’s organization. Label is `Dashboard Unique Name` .

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance may slow while Salesforce generates one for each
record.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Required. Returns the ID of the Folder that contains the dashboard. See Folder.

This is a relationship field.

**Relationship Name**
Folder

**Relationship Type**
Lookup

**Refers To**
Folder, User

**Type**
string

**Properties**
Filter, Nillable, Sort


Standard Objects Dashboard

**Field** **Details**

**Description**
Name of the folder that contains the dashboard. Available in API version 35.0
and later.

```
IsDeleted

LastReferencedDate

LastViewedDate

LeftSize

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not
( `false` ). Label is `Deleted` .

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related
to this record, or a list view.

**Type**
datetime

**Properties**
Filter, Nillable, Sort,

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, the user might have only accessed this record or list view
( `LastReferencedDate` ) but not viewed it.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

Returns the size of the left column of the dashboard.

Available values are:

**•** `Narrow`

**•** `Medium`

**•** `Wide`


Standard Objects Dashboard

**Field** **Details**

```
MiddleSize

NamespacePrefix

RightSize

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

Returns the size of the middle column of the dashboard.

Available values are:

**•** `Narrow`

**•** `Medium`

**•** `Wide`

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
Filter, Group, Restricted picklist, Sort

**Description**

Returns the size of the right column in the dashboard.

Available values are:

**•** `Narrow`

**•** `Medium`

**•** `Wide`


Standard Objects Dashboard

**Field** **Details**

```
RunningUserId

TextColor

Title

TitleColor

TitleSize

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Returns the ID of the running user specified for the dashboard.

If the dashboard was created in Lightning Experience and is configured to run
as the viewing user, it returns the user ID of the dashboard creator.

If the dashboard was created in Salesforce Classic and is configured to run as the
logged-in user, returns the user ID of the last specified running user.

This is a relationship field.

**Relationship Name**
RunningUser

**Relationship Type**
Lookup

**Refers To**
User

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Returns the body text color in hexadecimal. Label is `Text Color` .

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Returns the title of the dashboard. Limit: 80 characters.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Returns the title text color in hexadecimal. Label is `Title Color` .

**Type**
int


Standard Objects Dashboard

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
Returns the title font size in points. Label is `Title Size` .

```
Type

```

Supported Query Scopes

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Returns the dashboard type. Available values are:

**•** `SpecifiedUser` —The dashboard displays data according to the access
level of one specific running user.

**•** `LoggedInUser` —The dashboard displays data according to the access
level of the logged-in user.

**•** `MyTeamUser` —The dashboard displays data according to the access level
of the logged-in user, and managers can view dashboards from the point of
view of users beneath them in the role hierarchy.

Use these scopes to help specify the data that your SOQL query returns.

**allPrivate**
Records saved in all users’ private folders.

[Requires the user permission "Manage All Private Reports and Dashboards" and Enhanced Analytics Folder Sharing. If your organization](https://help.salesforce.com/HTViewHelpDoc?id=analytics_sharing_enable.htm&language=en_US)
was created after the Summer ’13 release, you already have Enhanced Analytics Folder Sharing. Available in API version 36.0 and
later.

**created**
Records created by the user running the query.

**everything**
All records except records saved in other users’ private folders.

**mine**
Records saved in the private folder of the user running the query.

Usage

Provides read-only access to the current values in the dashboard fields.


### Standard Objects DashboardComponent

Example: Dashboards in an Inactive User’s Private Folder

This SOQL query returns dashboards saved in a specific user’s private folder.

```
   SELECT Id FROM Dashboard USING SCOPE allPrivate WHERE CreatedByID = ‘005A0000000Bc2deFG’

```

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**DashboardFeed**

Feed tracking is available for the object.

SEE ALSO:

DashboardTag

Report

### DashboardComponent

Represents a dashboard component, which can be a chart, metric, table, or gauge on a dashboard. Access is read-only. This object is
available in API version 21.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
CustomReportId

DashboardId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Requires the user permission "Manage All Private Reports and Dashboards." The ID of the
report that provides data for the dashboard component. See Report.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the dashboard that contains the dashboard component. See Dashboard.

This is a relationship field.


### Standard Objects DashboardTag

**Field** **Details**

**Relationship Name**
### Dashboard

**Relationship Type**
Lookup

**Refers To**
### Dashboard

```
Name

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the dashboard component.

Provides read only access to the current values in dashboard component fields.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**DashboardComponentFeed**

Feed tracking is available for the object.

### DashboardTag

Associates a word or short phrase with a Dashboard. This object is available in API version 20.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
ItemId

```

**Type**
reference

**Properties**
Create, Filter


Standard Objects DashboardTag

**Field Name** **Details**

**Description**
ID of the tagged item.

```
Name

TagDefinitionId

Type

```

Usage

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

DashboardTag stores the relationship between its parent TagDefinition and the Dashboard being tagged. Tag objects act as metadata,
allowing users to describe and organize their data.

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.

SEE ALSO:

Dashboard


### Standard Objects DataAssessmentFieldMetric DataAssessmentFieldMetric

Represents summary statistics for matched, blank, and differing fields in account records of an org compared to records in Data.com.
This object is available in API version 37.0 and later.

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields will be removed
from your org.

To support customers’ needs around compliance and to remain a leader in trust and privacy, Salesforce removed all contact data
from the Data.com service on February 1, 2021.

[For more information, see Data.com Prospector and Clean Retirement.](https://help.salesforce.com/articleView?id=000270376&language=en_US&type=1)

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

**Child Relationships**
### DataAssessmentFieldMetric is a child object of DataAssessmentMetric object.

Fields

**Field Name** **Details**

```
DataAssessmentMetricId

FieldName

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
A unique number that identifies the parent DataAssessmentMetric record.

This is a relationship field.

**Relationship Name**
DataAssessmentMetric

**Relationship Type**
Lookup

**Refers To**
DataAssessmentMetric

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the assessed field.


### Standard Objects DataAssessmentMetric

**Field Name** **Details**

```
Name

NumMatchedBlanks

NumMatchedDifferent

NumMatchedInSync

NumUnmatchedBlanks

### DataAssessmentMetric

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An optional field used to name your record.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of matched records that contain blank fields.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of matched records that have a different value for this field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of matched records that have the same value for this field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unmatched records that contain blank fields.

Represents a summary of statistics for fields matched and unmatched in your account records with Data.com account records. This
object is available in API version 37.0 and later.


Standard Objects DataAssessmentMetric

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields will be removed
from your org.

To support customers’ needs around compliance and to remain a leader in trust and privacy, Salesforce removed all contact data
from the Data.com service on February 1, 2021.

[For more information, see Data.com Prospector and Clean Retirement.](https://help.salesforce.com/articleView?id=000270376&language=en_US&type=1)

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
Name

NumDuplicates

NumMatched

NumMatchedDifferent

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An optional field used to name your record.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of duplicate records.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of matched records.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of records in your org matched with a Data.com record that have
different fields.


### Standard Objects DataAssessmentValueMetric

**Field Name** **Details**

```
NumProcessed

NumTotal

NumUnmatched

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of records processed in the data assessment.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of records available for data assessment processing.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of records not matched.

### DataAssessmentValueMetric

Summarizes the number of fields matched for your account records with Data.com account records.This object is available in API version
37.0 and later.

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields will be removed
from your org.

To support customers’ needs around compliance and to remain a leader in trust and privacy, Salesforce removed all contact data
from the Data.com service on February 1, 2021.

[For more information, see Data.com Prospector and Clean Retirement.](https://help.salesforce.com/articleView?id=000270376&language=en_US&type=1)

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

**Child Relationships**
### DataAssessmentValueMetric is a child of DataAssessementFieldMetric.


### Standard Objects DatabaseSaveEventLog

Fields

**Field Name** **Details**

```
DataAssessmentFieldMetricId

FieldValue

Name

ValueCount

### DatabaseSaveEventLog

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
A unique number that identifies the parent DataAssessementFieldMetric record.

This is a relationship field.

**Relationship Name**
DataAssessmentFieldMetric

**Relationship Type**
Lookup

**Refers To**
DataAssessmentFieldMetric

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The value in the matched field.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An optional field used to name your record.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times this value appears in this field.

Database Save events track when records are created,updated, or deleted This object is available in API version 64.0 and later.


Standard Objects DatabaseSaveEventLog

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
BotIdentifier

BotSessionIdentifier

DmlType

FirstObjectIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the bot.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The bot session ID.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of DML operation.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Only the first object ID is logged upon an update. During record updates, the ID of that
specific row is logged. When multiple rows are updated, only a single ID is logged.


Standard Objects DatabaseSaveEventLog

**Field** **Details**

```
KeyPrefix

LoginKey

```

PlannerIdentifier

```
RequestIdentifier

RowCount

SampleFactor

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The key prefix of the entity type that was saved

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The string that ties together all events in a given user’s login session. The session starts with
a login event and ends with either a logout event or the user session expiring. For example,
`lUqjLPQTWRdvRG4` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the agent planner.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same RequestIdentifier.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Total number of records in the result set.

**Type**
double

**Properties**
Filter, Nillable, Sort


### Standard Objects DatacloudCompany

**Field** **Details**

**Description**
Rate at which entities are logged. If the sample factor is 1 that means every entity saved was
logged. If it is 100 that means that 1/100 logs.

```
SessionKey

Timestamp

UserIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example, 2020-01-20T19:12:26.965Z.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.

### DatacloudCompany

Represents the fields for Data.com company records. This object is available in API version 30.0 or later.

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields are removed
from your org.

To support customers’ needs around compliance and to remain a leader in trust and privacy, Salesforce removed all contact data
from the Data.com service on February 1, 2021.

[For more information, see Data.com Prospector and Clean Retirement.](https://help.salesforce.com/articleView?id=000270376&language=en_US&type=1)

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`


Standard Objects DatacloudCompany

Fields

**Field Name** **Details**

```
ActiveContacts

AnnualRevenue

City

CompanyId

Country

```

**Type**
int

**Properties**
Nillable

**Description**

The number of active contacts that are associated with a company.

**Type**
currency

**Properties**
Filter, Nillable

**Description**

The amount of money that the company makes in 1 year. Annual revenue is
measured in US dollars.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

The name of the city where the company is located.

**Type**
string

**Properties**
Filter, Nillable

**Description**

A unique numerical identifier for the company and theData.com identifier for a
company.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

A string that represents the standard abbreviation for the country where the
company is located.


Standard Objects DatacloudCompany

**Field Name** **Details**

```
CountryCode

Description

DunsNumber

EmployeeQuantityGrowthRate

ExternalId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist

**Description**

A standardized name for countries of the world.

**Type**
string

**Properties**
Nillable

**Description**

A brief synopsis of the company that provides a general overview of the company
and what it does.

**Type**
string

**Properties**
Filter, Nillable

**Description**

A randomly generated nine-digit number that’s assigned by Dun & Bradstreet
(D&B) to identify unique business establishments.

**Type**
double

**Properties**
Nillable

**Description**
The yearly growth rate of the number of employees in a company expressed as
a decimal percentage. The data includes the total employee growth rate for the
past two years.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

A unique numerical identifier for the company. The `ExternalId` is a
system-generated number.


Standard Objects DatacloudCompany

**Field Name** **Details**

```
Fax

FortuneRank

FullAddress

IncludedInSnP500

Industry

IsInCrm

```

**Type**
phone

**Properties**
Nillable

**Description**

The telephone number that’s used to send and receive faxes.

**Type**
int

**Properties**
Defaulted on create, Group, Nillable

**Description**
The numeric value of the company’s Fortune 1000 ranking. A null or blank value
means that the company isn’t ranked as a Fortune 1000 company.

**Type**
string

**Properties**
Group, Nillable

**Description**
The complete address of a company, including Street, City, State, and Zip.

**Type**
string

**Properties**
Group, Nillable

**Description**
A true or false value. If `true`, the company is listed in the S&P 500 Index. If
`false`, the company isn’t listed in the S&P 500 Index.

**Type**
string

**Properties**
Nillable

**Description**
A description of the type of industry such as Telecommunications, Agriculture,
or Electronics.

**Type**
boolean


Standard Objects DatacloudCompany

**Field Name** **Details**

**Properties**
Defaulted on create, Group

**Description**

Whether the record is in Salesforce (true) or not (false).

```
IsInactive

IsOwned

NaicsCode

NaicsDesc

Name

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**

A true or false response. True, the company record is not active. False, the
company record is active.

**Type**
boolean

**Properties**
Defaulted on create

**Description**

A true or false value. True, your organization owns the record. False, your
organization doesn’t own the record.

**Type**
string

**Properties**
Filter, Nillable

**Description**

A value that represents the North American Industry Classification System (NAICS)
code. NAICS was created to provide details about a business’s service orientation.
The code descriptions are focused on what a business does.

**Type**
string

**Properties**
Nillable

**Description**

A description of the NAICS classification.

**Type**
string


Standard Objects DatacloudCompany

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**

The company’s name.

```
NumberOfEmployees

Ownership

Phone

PremisesMeasure

PremisesMeasureReliability

```

**Type**
int

**Properties**
Filter, Nillable

**Description**

The number of employees working for the company.

**Type**
string

**Properties**
Filter, Nillable

**Description**

The type of ownership of the company:

**•** `Public`

**•** `Private`

**•** `Government`

**•** `Other`

**Type**
phone

**Properties**
Nillable

**Description**

A numeric string containing the primary telephone number for the company.

**Type**
int

**Properties**
Group, Nillable

**Description**
A numeric value for the measurement of the premises.

**Type**
string


Standard Objects DatacloudCompany

**Field Name** **Details**

**Properties**
Group, Nillable

**Description**
A descriptive accuracy of the measurement such as actual, estimated, or modeled.

```
PremisesMeasureUnit

PriorYearEmployees

PriorYearRevenue

SalesTurnoverGrowthRate

Sic

```

**Type**
string

**Properties**
Group, Nillable

**Description**
A descriptive measurement unit such as acres, square meters, or square feet.

**Type**
int

**Properties**
Group, Nillable

**Description**

The total number of employees for the prior year.

**Type**
double

**Properties**
Nillable

**Description**

The annual revenue for the prior year.

**Type**
double

**Properties**
Nillable

**Description**
The increase in annual revenue from the previous value for an equivalent period
expressed as a decimal percentage.

**Type**
string

**Properties**
Filter, Nillable


Standard Objects DatacloudCompany

**Field Name** **Details**

**Description**

A numeric value that represents the Standard Industrial Codes (SIC). SIC is a
numbering convention that indicates what type of service a business provides.
It is a four-digit value.

```
SicCodeDesc

SicDesc

Site

State

StateCode

```

**Type**
string

**Properties**
Group, Nillable

**Description**
The SIC numeric code and descsciption for a company.

**Type**
string

**Properties**
Nillable

**Description**

A description of the SIC classification.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist

**Description**

An organizational status of the company.

**•** Branch: a secondary location to a headquarter location

**•** Headquarter: a parent company with branches or subsidiaries

**•** Single Location: a single business with no subsidiaries or branches

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

The two-letter standard abbreviation for a state.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist


Standard Objects DatacloudCompany

**Field Name** **Details**

**Description**

A standard two-letter abbreviation for states and territories of the United States.
The state where the company is located. The abbreviation can also be a province
or other equivalent to a state, depending on the country where the company is
located.

```
Street

TickerSymbol

TradeStyle

UpdatedDate

Website

```

**Type**
string

**Properties**
Nillable

**Description**

A postal address for the company.

**Type**
string

**Properties**
Nillable

**Description**

The symbol that uniquely identifies companies that are traded on public stock
exchanges.

**Type**
string

**Properties**
Nillable

**Description**

A legal name under which a company conducts business.

**Type**
dateTime

**Properties**
Nillable, Sort

**Description**

The last date and time when the information for this company was updated.

**Type**
url

**Properties**
Nillable


### Standard Objects DatacloudContact

**Field Name** **Details**

**Description**

The standard URL for the company’s home page.

```
YearStarted

Zip

```

Usage

**Type**
string

**Properties**
Nillable

**Description**

The year when the company was founded.

**Type**
string

**Properties**
Filter, Nillable

**Description**

A numeric postal code that’s designated for the address.

Use the DatacloudCompany object to search the Data.com database for companies with the specific criteria that you enter. Use this
object to find company records that you are interested in purchasing for your organization. Data.com APIs use the term “company,”
which is similar to Salesforce term “accounts.”

Important: DatacloudCompany can’t be used in Apex test methods, because an external web service call is required to access
it. These calls are not allowed in Apex test methods.

### DatacloudContact

The fields and properties for Data.com contact records. This object is available in API version 30.0 or later.

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields are removed
from your org.

To support customers’ needs around compliance and to remain a leader in trust and privacy, Salesforce removed all contact data
from the Data.com service on February 1, 2021.

[For more information, see Data.com Prospector and Clean Retirement.](https://help.salesforce.com/articleView?id=000270376&language=en_US&type=1)

Supported Calls

`describeSObjects()`, `query()`


Standard Objects DatacloudContact

Fields

**Field Name** **Details**

```
City

CompanyId

CompanyName

ContactId

Country

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

The city where the company is located.

**Type**
string

**Properties**
Filter, Nillable

**Description**

The unique numerical identifier for the company and the Data.com company
identification number or Data.com Key.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**

The name of the company.

**Type**
string

**Properties**
Filter, Nillable

**Description**

The unique numeric identifier for this contact.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

The standard abbreviation or name for the country where the company is located.

Note: You can enter a comma-separated list of countries; however, for
a country that uses a comma in its name, leave out the comma. For
example, enter “Taiwan, ROC” as `Taiwan ROC` .


Standard Objects DatacloudContact

**Field Name** **Details**

```
Department

Email

ExternalId

FirstName

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist

**Description**

The department in the company that the contact is affiliated with. The values of
this field are fixed enumerated values.

**•** `Engineering`

**•** `Finance`

**•** `Human Resources`

**•** `IT`

**•** `Marketing`

**•** `Operations`

**•** `Other`

**•** `Sales`

**•** `Support`

**Type**
email

**Properties**
Filter, Nillable

**Description**

A business email address for the contact.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

A unique system-generated numerical identifier for the contact.

**Type**
string

**Properties**
Filter, Nillable

**Description**

The first name of the contact.


Standard Objects DatacloudContact

**Field Name** **Details**

```
IsInCrm

IsInactive

IsOwned

LastName

Level

```

**Type**
boolean

**Properties**
Defaulted on create, Group

**Description**
Whether the record is in Salesforce (true) or not (false).

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Whether the record is active (false) or not (true).

**Type**
boolean

**Properties**
Defaulted on create

**Description**

**•** `True` : You own this record.

**•** `False` : You do not own this record.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

The last name of the contact.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist

**Description**

A human resource label that designates a person’s level in the company. The
values of this field are fixed enumerated values.

**•** `C-Level`

**•** `VP`

**•** `Director`

**•** `Manager`


Standard Objects DatacloudContact

**Field Name** **Details**

**•** `Staff`

**•** `Other`

```
Phone

SocialHandles

State

Street

Title

```

**Type**
phone

**Properties**
Nillable

**Description**
The direct-dial telephone number for the contact.

**Type**
string

**Description**
The social handles for this contact. Social handles are a normalized URL and user
name for social media accounts such as, LinkedIn, Facebook, and Twitter. This
field is response-only.

The DatacloudSocialHandles object is a child of the DatacloudContact object.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

The state where the company is located, which can also be a province or other
equivalent to a state, depending on the country where the company is located.

**Type**
string

**Properties**
Nillable

**Description**

The street address for the company where the contact works.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Title of the contact such as CEO or Vice President.


### Standard Objects DatacloudDandBCompany

**Field Name** **Details**

```
UpdatedDate

Zip

```

Usage

**Type**
dateTime

**Properties**
Nillable, Sort

**Description**

The last date and time when the information for a contact was updated.

**Type**
string

**Properties**
Filter, Nillable

**Description**

The postal or zip code for the address.

This object searches the Data.com database for contacts with the specific criteria that you enter. Use this object to find contact records
that you are interested in purchasing for your organization.

Important: DatacloudContact can’t be used in Apex test methods, because an external web service call is required to access it.
These calls are not allowed in Apex test methods.

### DatacloudDandBCompany

Represents a set of read-only fields that are used to return D&B company data from Data.com API calls. This object is available in API
version 30.0 or later.

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields will be removed
from your org.

To support customers’ needs around compliance and to remain a leader in trust and privacy, Salesforce removed all contact data
from the Data.com service on February 1, 2021.

[For more information, see Data.com Prospector and Clean Retirement.](https://help.salesforce.com/articleView?id=000270376&language=en_US&type=1)

Supported Calls

`describeSObjects()`, `query()`


Standard Objects DatacloudDandBCompany

Fields

**Field Name** **Details**

```
City

CompanyCurrencyIsoCode

CompanyId

Country

CountryAccessCode

```

**Type**
string

**Properties**
Nillable

**Description**

The name of the city where the company is physically located.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

The code used to represent a company’s local currency. This data is provided by
the International Organization for Standardization (ISO) and is based on their
three-letter currency codes. For example, USD is the ISO code for United States
Dollar.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

A unique numeric identifier for a company.

**Type**
string

**Properties**
Nillable

**Description**

The country where a company is physically located.

**Type**
string

**Properties**
Nillable

**Description**

The required code for international calls.


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

```
CurrencyCode

Description

DomesticUltimateBusinessName

DomesticUltimateDunsNumber

DunsNumber

```

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

The currency in which the company’s sales volume is expressed.

**Type**
string

**Properties**
Nillable

**Description**

A brief description of the company, which may include information about its
history, its products and services, and its influence on a particular industry.

**Type**
string

**Properties**
Nillable

**Description**

The primary name of the Domestic Ultimate, which is the highest ranking
subsidiary, specified by country, within an organization’s corporate structure.

**Type**
string

**Properties**
Nillable

**Description**

The D-U-N-S number for the Domestic Ultimate, which is the highest-ranking
subsidiary, specified by country, within an organization’s corporate structure.

**Type**
string

**Properties**
Filter, Nillable

**Description**

The Data Universal Numbering System (D-U-N-S) number is a unique, nine-digit
number assigned to every business location in the Dun & Bradstreet database
that has a unique, separate, and distinct operation. D-U-N-S numbers are used
by industries and organizations around the world as a global standard for business
identification and tracking.


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

```
EmployeeQuantityGrowthRate

EmployeesHere

EmployeesHereReliability

EmployeesTotal

EmployeesTotalReliability

```

**Type**
double

**Properties**
Nillable

**Description**
The yearly growth rate of the number of employees in a company expressed as
a decimal percentage. The data includes the total employee growth rate for the
past two years.

**Type**
double

**Properties**
Nillable

**Description**

The number of employees at a specified location, such as a branch location.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

The reliability of the `EmployeesHere` figure. Available values are _`Actual`_
_`number`_, _`Low`_, _`Estimated (for all records)`_, _`Modeled (for`_
_`non-US records)`_ . A blank value indicates this data is unavailable.

**Type**
double

**Properties**
Nillable

**Description**

The total number of employees in the company, including all subsidiary and
branch locations. This data is available only on records that have a value of
_`Headquarters/Parent`_ in the `LocationStatus` field.

**Type**
picklist

**Properties**
Nillable, Restricted picklist


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

**Description**

The reliability of the `EmployeesTotal` figure. Available values are _`Actual`_
_`number`_, _`Low`_, _`Estimated (for all records)`_, _`Modeled (for`_
_`non-US records)`_ . A blank value indicates this data is unavailable.

```
ExternalId

FamilyMembers

Fax

FifthNaics

FifthNaicsDesc

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**

A system generated numeric identification.

**Type**
int

**Properties**
Nillable

**Description**

The total number of family members, worldwide, within an organization, including
the Global Ultimate, its subsidiaries (if any), and its branches (if any).

**Type**
phone

**Properties**
Nillable

**Description**

The company’s facsimile number.

**Type**
string

**Properties**
Nillable

**Description**

A NAICS code that’s used to further classify an organization by industry.

**Type**
string

**Properties**
Nillable


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

**Description**

A brief description of an organization’s line of business, based on the
corresponding NAICS code.

```
FifthSic

FifthSic8

FifthSic8Desc

FifthSicDesc

FipsMsaCode

```

**Type**
string

**Properties**
Nillable

**Description**

A Standard Industrial Classification (SIC) code that’s used to further classify an
organization by industry.

**Type**
string

**Properties**
Group, Nillable

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Group, Nillable

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Nillable

**Description**

A brief description of an organization’s line of business, based on the
corresponding SIC code.

**Type**
string

**Properties**
Nillable


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

**Description**

The Federal Information Processing Standards (FIPS) and the Metropolitan
Statistical Area (MSA) codes identify the organization’s location. The MSA codes
are defined by the US Office of Management and Budget.

```
FipsMsaDesc

FortuneRank

FourthNaics

FourthNaicsDesc

FourthSic

```

**Type**
string

**Properties**
Nillable

**Description**

A brief description of an organization’s FIPS MSA code.

**Type**
int

**Properties**
Defaulted on create, Group, Nillable

**Description**
The numeric value of the company’s Fortune 1000 ranking. A null or blank value
means that the company isn’t ranked as a Fortune 1000 company.

**Type**
string

**Properties**
Nillable

**Description**

A NAICS code used to further classify an organization by industry.

**Type**
string

**Properties**
Nillable

**Description**

A brief description of an organization’s line of business, based on the
corresponding NAICS code.

**Type**
string

**Properties**
Group, Nillable


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

**Description**

A SIC code used to further classify an organization by industry.

```
FourthSic8

FourthSic8Desc

FourthSicDesc

GeoCodeAccuracy

```

**Type**
string

**Properties**
Group, Nillable

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Group, Nillable

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Nillable

**Description**

A brief description of an organization’s line of business, based on the
corresponding SIC code.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

The level of accuracy of a location’s geographical coordinates compared with its
physical address. Available values include _`Rooftop level`_, _`Street`_
_`level`_, _`Block level`_, _`Census tract level`_, _`Mailing address`_
_`level`_, _`ZIP code level`_, _`Geocode could not be assigned`_,
_`Places the address in the correct city`_, _`Not matched`_,
_`State or Province Centroid`_, _`Street intersection`_, _`PO`_
_`BOX location`_, _`Non-US rooftop accuracy`_, _`County Centroid`_,
_`Sub Locality-Street Level`_, and _`Locality Centroid`_


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

```
GlobalUltimateBusinessName

GlobalUltimateDunsNumber

GlobalUltimateTotalEmployees

ImportExportAgent

IncludedInSnP500

```

**Type**
string

**Properties**
Nillable

**Description**

The primary name of the Global Ultimate, which is the highest entity within an
organization’s corporate structure and may oversee branches and subsidiaries.

**Type**
string

**Properties**
Filter, Nillable

**Description**

The D-U-N-S number of the Global Ultimate, which is the highest-ranking entity
within an organization’s corporate structure and can oversee branches and
subsidiaries.

**Type**
double

**Properties**
Nillable

**Description**

The total number of employees at the Global Ultimate, which is the highest entity
within an organization’s corporate structure and may oversee branches and
subsidiaries.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

Identifies whether a business imports goods or services, exports goods or services,
and/or is an agent for goods.

**Type**
string

**Properties**
Group, Nillable

**Description**
A true or false value. If `true`, the company is listed in the S&P 500 Index. If
`false`, the company isn’t listed in the S&P 500 Index.


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

```
Industry

IsOwned

IsParent

Latitude

LegalStatus

```

**Type**
string

**Properties**
Group, Nillable

**Description**
A description of the type of industry such as Telecommunications, Agriculture,
or Electronics.

**Type**
boolean

**Properties**
Defaulted on create

**Description**

A true or false value. True, your organization owns the record. False, your
organization doesn’t own the record.

**Type**
boolean

**Properties**
Defaulted on create,

**Description**
A true or false value. True, the company is a parent company. False, the company
isn’t a parent company. A parent company owns other companies.

**Type**
string

**Properties**
Nillable

**Description**

Used with longitude to specify a precise location, which is used to assess the
Geocode Accuracy.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

Identifies the legal structure of an organization. Available values include
_`Cooperative`_, _`Nonprofit organization`_, _`Local government`_
_`body`_, _`Partnership of unknown type`_, and _`Foreign company`_ .


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

```
LocationStatus

Longitude

MailingCity

MailingCountry

```

**Type**
picklist

**Properties**
Filter, Nillable, Restricted picklist

**Description**

Identifies the organizational status of a company. A numeric value represents
each value.

Note: Only the numeric value is accepted in an API request.

**Type**
string

**Properties**
Nillable

**Description**

Used with latitude to specify a precise location, which is used to assess the
Geocode Accuracy.

**Type**
string

**Properties**
Nillable

**Description**

The city where a company has its mail delivered.

**Type**
string


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

**Properties**
Nillable

**Description**

The country where a company has its mail delivered.

```
MailingState

MailingStreet

MailingZip

MarketingPreScreen

```

**Type**
string

**Properties**
Nillable

**Description**

The state where a company has its mail delivered.

**Type**
string

**Properties**
Nillable

**Description**

The street address where a company has its mail delivered.

**Type**
string

**Properties**
Nillable

**Description**

The postal zip code for the company.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

The probability that a company pays with a significant delay compared to the
agreed terms. The risk level is based on the standard Commercial Credit Score,
and ranges from low risk to high risk. Available values are _`High risk of`_
_`delinquency`_, _`Low risk of delinquency`_, and _`Moderate risk`_
_`of delinquency`_ .

Important: Use this information for marketing pre-screening purposes
only.


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

```
MarketingSegmentationCluster

MinorityOwned

Name

NationalId

NationalIdType

```

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**
Twenty-two distinct, mutually exclusive profiles, created as a result of cluster
analysis of Dun & Bradstreet data for US organizations. Available values include

```
  High-Tension Branches of Insurance/Utility
```

_`Industries`_, _`Rapid-Growth Large Businesses`_,
_`Labor-Intensive Giants`_, _`Spartans`_, _`Main Street USA`_ .

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

Indicates whether an organization is owned or controlled by a member of a
minority group.

**Type**
string

**Properties**
Filter, Nillable

**Description**

The primary or registered name of a company.

**Type**
string

**Properties**
Nillable

**Description**

The identification number used in some countries for business registration and
tax collection.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

A code value that identifies the type of national identification number that’s used.


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

```
OutOfBusiness

OwnOrRent

ParentOrHqBusinessName

ParentOrHqDunsNumber

Phone

PremisesMeasure

```

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

Indicates whether the company at the specified address has discontinued
operations.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

Indicates whether a company owns or rents the building it occupies.

**Type**
string

**Properties**
Nillable

**Description**

The primary name of the parent or headquarters company.

**Type**
string

**Properties**
Filter, Nillable

**Description**

The D-U-N-S number for the parent or headquarters.

**Type**
phone

**Properties**
Nillable

**Description**
A company’s primary telephone number.

**Type**
int

**Properties**
Group, Nillable


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

**Description**
A numeric value for the measurement of the premises.

```
PremisesMeasureReliability

PremisesMeasureUnit

PrimaryNaics

PrimaryNaicsDesc

PrimarySic

```

**Type**
string

**Properties**
Group, Nillable

**Description**
A descriptive accuracy of the measurement such as actual, estimated, or modeled.

**Type**
string

**Properties**
Group, Nillable

**Description**
A descriptive measurement unit such as acres, square meters, or square feet.

**Type**
string

**Properties**
Nillable

**Description**

The six-digit North American Industry Classification System (NAICS) code is the
standard used by business and government to classify business establishments
according to their economic activity for the purpose of collecting, analyzing, and
publishing statistical data related to the US business economy.

**Type**
string

**Properties**
Nillable

**Description**

A brief description of an organization’s line of business, based on its NAICS code.

**Type**
string

**Properties**
Nillable

**Description**

The four-digit SIC code that’s used to categorize business establishments by
industry.


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

```
PrimarySic8

PrimarySic8Desc

PrimarySicDesc

PriorYearEmployees

PriorYearRevenue

PublicIndicator

```

**Type**
string

**Properties**
Group, Nillable

**Description**
The eight-digit Standard Industrial Classification (SIC) code is used to categorize
business establishments by industry. The full list of values can be found at the
[Optimizer Resources page maintained by Dun & Bradstreet. Maximum size is 8](http://www.dnboptimizer.com/knowledge-center/optimizer-resources.html)
characters.

**Type**
string

**Properties**
Group, Nillable

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Nillable

**Description**

A brief description of an organization’s line of business, based on its SIC code.

**Type**
int

**Properties**
Group, Nillable

**Description**

The total number of employees for the prior year.

**Type**
double

**Properties**
Nillable

**Description**

The annual revenue for the prior year.

**Type**
picklist


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

**Properties**
Nillable, Restricted picklist

**Description**

Indicates whether ownership of the company is public or private.

```
Revenue

SalesTurnoverGrowthRate

SalesVolume

SalesVolumeReliability

SecondNaics

```

**Type**
double

**Properties**
Nillable

**Description**

The annual revenue of a company in US dollars.

**Type**
double

**Properties**
Nillable

**Description**
The increase in annual revenue from the previous value for an equivalent period
expressed as a decimal percentage.

**Type**
double

**Properties**
Nillable

**Description**

The total annual sales revenue in the headquarters’ local currency. Dun &
Bradstreet tracks revenue data for publicly traded companies, Global Ultimates,
Domestic Ultimates, and some headquarters.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

The reliability of the `SalesVolume` figure.

**Type**
string

**Properties**
Nillable


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

**Description**

A NAICS code used to further classify an organization by industry.

```
SecondNaicsDesc

SecondSic

SecondSic8

SecondSic8Desc

SecondSicDesc

```

**Type**
string

**Properties**
Nillable

**Description**

A brief description of an organization’s line of business, based on the
corresponding NAICS code.

**Type**
string

**Properties**
Nillable

**Description**

A SIC code used to further classify an organization by industry.

**Type**
string

**Properties**
Group, Nillable

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Group, Nillable

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Nillable

**Description**

A brief description of an organization’s line of business, based on the
corresponding SIC code.


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

```
SixthNaics

SixthNaicsDesc

SixthSic

SixthSic8

SixthSic8Desc

SixthSicDesc

```

**Type**
string

**Properties**
Nillable

**Description**

A NAICS code used to further classify an organization by industry.

**Type**
string

**Properties**
Nillable

**Description**

A brief description of an organization’s line of business, based on the
corresponding SIC code.

**Type**
string

**Properties**
Nillable

**Description**

A SIC code used to further classify an organization by industry.

**Type**
string

**Properties**
Group, Nillable

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

**Type**
string

**Properties**
Group, Nillable

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

**Properties**
Nillable

**Description**

A brief description of an organization’s line of business, based on the
corresponding SIC code.

```
SmallBusiness

State

StockExchange

StockSymbol

Street

```

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

Indicates whether the company is designated a small business as defined by the
Small Business Administration of the US government.

**Type**
string

**Properties**
Nillable

**Description**

The state where a company is physically located.

**Type**
string

**Properties**
Nillable

**Description**

The corresponding exchange for a company’s stock symbol, for example, NASDAQ
or NYSE.

**Type**
string

**Properties**
Nillable

**Description**

The abbreviation that’s used to identify publicly traded shares of a particular
stock.

**Type**
string


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

**Properties**
Nillable

**Description**

The street address where a company is physically located.

```
Subsidiary

ThirdNaics

ThirdNaicsDesc

ThirdSic

ThirdSic8

```

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

Indicates whether a company is more than 50 percent owned by another
organization.

**Type**
string

**Properties**
Nillable

**Description**

A NAICS code used to further classify an organization by industry.

**Type**
string

**Properties**
Nillable

**Description**

A brief description of an organization’s line of business, based on the
corresponding NAICS code.

**Type**
string

**Properties**
Nillable

**Description**

A SIC code used to further classify an organization by industry.

**Type**
string

**Properties**
Group, Nillable


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

```
ThirdSic8Desc

ThirdSicDesc

TradeStyle1

TradeStyle2

TradeStyle3

```

**Type**
string

**Properties**
Group, Nillable

**Description**
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

**Type**
string

**Properties**
Nillable

**Description**

A brief description of an organization’s line of business, based on the
corresponding SIC code.

**Type**
string

**Properties**
Nillable

**Description**

A name, different from its legal name, that an organization may use for conducting
business. Similar to “Doing business as” or “DBA”.

**Type**
string

**Properties**
Nillable

**Description**

A tradestyle used by the organization.

**Type**
string

**Properties**
Nillable

**Description**

A tradestyle used by the organization.


Standard Objects DatacloudDandBCompany

**Field Name** **Details**

```
TradeStyle4

TradeStyle5

UsTaxId

Website

WomenOwned

YearStarted

```

**Type**
string

**Properties**
Nillable

**Description**

A tradestyle used by the organization.

**Type**
string

**Properties**
Nillable

**Description**

A tradestyle used by the organization.

**Type**
string

**Properties**
Nillable

**Description**

The identification number for the company used by the Internal Revenue Service
(IRS) in the administration of tax laws. Also referred to as Federal Taxpayer
Identification Number.

**Type**
url

**Properties**
Filter, Group, Nillable

**Description**

An organization’s primary website address.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**

Indicates whether a company is more than 50 percent owned or controlled by
a woman.

**Type**
string


### Standard Objects DatacloudOwnedEntity

**Field Name** **Details**

**Properties**
Nillable

**Description**

The year when the company was established or the year when current ownership
or management assumed control of the company.

```
Zip

```

Usage

**Type**
string

**Properties**
Nillable

**Description**

A five or nine-digit code that’s used to help sort mail.

Use this object to return D&B Company information. These fields are read-only.

Important: DatacloudDandBCompany can’t be used in Apex test methods, because an external web service call is required to
access it. These calls are not allowed in Apex test methods.

### DatacloudOwnedEntity

Represents fields in the DatacloudOwnedEntity object. The DatacloudOwnedEntity object tracks user-purchased records. This object is
available in API version 30.0 or later.

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields are removed
from your org.

To support customers’ needs around compliance and to remain a leader in trust and privacy, Salesforce removed all contact data
from the Data.com service on February 1, 2021.

[For more information, see Data.com Prospector and Clean Retirement.](https://help.salesforce.com/articleView?id=000270376&language=en_US&type=1)

Supported Calls

`create()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
DataDotComKey

```

**Type**
string


Standard Objects DatacloudOwnedEntity

**Field Name** **Details**

**Properties**
Create, Filter, Sort

**Description**

The Data.com contact or company record identification number used by the
DatacloudPurchaseUsage object to keep track of purchased records. This is
equivalent to the Data.com record ID for a contact or company.

```
DatacloudEntityType

Name

PurchaseType

PurchaseUsageId

```

**Type**
picklist

**Properties**
Create, Filter, Restricted picklist, Sort

**Description**

The type of Data.com record you want to purchase.

**•** 0—contact

**•** 1—company

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**

An optional field used to name your record.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

A read only field set by the API to identify the purchase type.

**•** Added

**•** Export

**•** API

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The unique identification number for the DatacloudPurchaseUsage object created
by making a REST POST request.


### Standard Objects DatacloudPurchaseUsage

**Field Name** **Details**

**•** 0—contact

**•** 1—company

```
UserId

```

Usage

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

A unique identifier for the user making the purchase.

The Datacloud object that tracks records that are purchased and owned by a specific user.

### DatacloudPurchaseUsage

Represents an object used to identify and track Data.com record purchases. This object is available in API version 30.0 or later.

Note: When your Data.com Prospector or Data.com Clean contract expires, Data.com features, objects, and fields are removed
from your org.

To support customers’ needs around compliance and to remain a leader in trust and privacy, Salesforce removed all contact data
from the Data.com service on February 1, 2021.

[For more information, see Data.com Prospector and Clean Retirement.](https://help.salesforce.com/articleView?id=000270376&language=en_US&type=1)

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field Name** **Details**

```
DatacloudEntityType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The type of Data.com record you want to purchase.

**•** 0—indicates contact entity type.


Standard Objects DatacloudPurchaseUsage

**Field Name** **Details**

**•** 1—indicates company entity type.

```
Description

Name

PurchaseType

Usage

UserId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

An optional field. You can add a description for your purchase.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**

An optional field used to name your record.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

A read only field set by the API to identify the purchase type.

**•** Added

**•** Export

**•** API

**Type**
double

**Properties**
Filter, Sort

**Description**

A read only field set by the API. It is used to track the points used to purchase
records.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

A read only field set by the API that identifies the user purchasing the records.


### Standard Objects DataDetectJobObjectSession

**Field Name** **Details**

```
UserType

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

A read only field set by the API with 2 user types.

**•** Monthly Usage

**•** List Pool User

The DatacloudPurchaseUsage object allows you to track Data.com record purchases for CRM users.

### DataDetectJobObjectSession

Represents an object-specific job session that's created whenever a DataDetect scan policy job session runs on a scan policy object. This
object is available in API version 63.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`

Fields

**Field** **Details**

```
CurrentObject

DataDetectJobSessionId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the scan policy object associated with the job object session.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the job session associated with a scan policy data scan.

This field is a relationship field.


Standard Objects DataDetectJobObjectSession

**Field** **Details**

**Relationship Name**
DataDetectJobSession

**Relationship Type**
Master-Detail

**Refers To**
DataDetectJobSession

```
SessionEndTime

ScannedRecordsCount

LastScannedRecord

JobStatus

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Time and date when the scan policy object scan completes.

**Type**
Long

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of records already scanned while the overall job is in progress.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Last scanned record identifier of the object.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Status of the scan policy object scan. Possible values are:

**•** `Cancelled`

**•** `Cancelled and CsvNoPiiData - Scan cancelled. No sensitive`

```
   data detected.

```

**•** `Cancelled and CsvUploadFailed - Scan cancelled. Results`

```
   upload failed.

```

**•** `Cancelled and CsvUploadInProgress - Scan cancelled.`

```
   Results upload in progress.

```


Standard Objects DataDetectJobObjectSession

**Field** **Details**

**•** `Cancelled and CsvUploadSuccess - Scan cancelled. Results`

```
                     upload completed successfully.

```

**•** `Completed`

**•** `Completed and CsvNoPiiData - Scan completed. No sensitive`

```
                     data detected.

```

**•** `Completed and CsvUploadFailed - Scan completed. Results`

```
                     upload failed.

```

**•** `Completed and CsvUploadInProgress - Scan completed.`

```
                     Results upload in progress.

```

**•** `Completed and CsvUploadSuccess - Scan completed. Results`

```
                     upload completed successfully.

```

**•** `Failed`

**•** `Failed and CsvNoPiiData - Scan failed. No sensitive data`

```
                     detected.

```

**•** `Failed and CsvUploadFailed - Scan failed. Results upload`

```
                     failed.

```

**•** `Failed and CsvUploadInProgress - Scan failed. Results`

```
                     upload in progress.

```

**•** `Failed and CsvUploadSuccess - Scan failed. Results upload`

```
                     completed successfully.

```

**•** `PartialSuccess`

**•** `PartialSuccess and CsvNoPiiData - Scan partially`

```
                     successful. No sensitive data detected.

```

**•** `PartialSuccess and CsvUploadFailed - Scan partially`

```
                     successful. Results upload failed.

```

**•** `PartialSuccess and CsvUploadInProgress - Scan partially`

```
                     successful. Results upload in progress.

```

**•** `PartialSuccess and CsvUploadSuccess - Scan partially`

```
                     successful. Results upload completed successfully.

```

**•** `Running`

**•** `Scheduled`

**•** `TimedOut`

The default value is `Scheduled` .

```
Name

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Auto-generated name of the job object session.


### Standard Objects DataDetectJobSession

**Field** **Details**

```
SessionStartTime

```

SEE ALSO:

_[Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.einstein_data_detect.htm&type=5&language=en_US)_ : Data Detect

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Time and date when the scan policy object scan begins. Scan policy object scan can start
anytime within a 30-day window from the current date.

### DataDetectJobSession

Represents a run of a DataDetect scan policy that's triggered manually. This object is available in API version 63.0 and later.

To opt in for beta, contact your Salesforce account executive. After the org permission is enabled, users can access the Data Detect app
from the App launcher.

Supported Calls

`delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `undelete()`

Fields

**Field** **Details**

```
DataDetectPolicyId

DataDetectPolicySnapshotId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the scan policy associated with this job session.

This field is a relationship field.

**Relationship Name**
DataDetectPolicy

**Refers To**
DataDetectPolicy

**Type**
reference


Standard Objects DataDetectJobSession

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
ID of the snapshot of the scan policy associated with this job session.

This field is a relationship field.

**Relationship Name**
DataDetectPolicySnapshot

**Relationship Type**
Master-Detail

**Refers To**
DataDetectPolicySnapshot

```
SessionEndTime

Name

NamedEntityCount

PolicyJobStatus

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Time and date when the data scan completes.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Auto-generated name of the job session.

**Type**
int

**Properties**
Create, Filter, Nillable, Update

**Description**
Aggregate count of PII found during the data scan.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Status of the data scan. Valid values are:

**•** `Cancelled`


Standard Objects DataDetectJobSession

**Field** **Details**

**•** `Cancelled and CsvNoPiiData - Scan cancelled. No sensitive`

```
                     data detected.

```

**•** `Cancelled and CsvUploadFailed - Scan cancelled. Results`

```
                     upload failed.

```

**•** `Cancelled and CsvUploadInProgress - Scan cancelled.`

```
                     Results upload in progress.

```

**•** `Cancelled and CsvUploadSuccess - Scan cancelled. Results`

```
                     upload completed successfully.

```

**•** `Completed`

**•** `Completed and CsvNoPiiData - Scan completed. No sensitive`

```
                     data detected.

```

**•** `Completed and CsvUploadFailed - Scan completed. Results`

```
                     upload failed.

```

**•** `Completed and CsvUploadInProgress - Scan completed.`

```
                     Results upload in progress.

```

**•** `Completed and CsvUploadSuccess - Scan completed. Results`

```
                     upload completed successfully.

```

**•** `Failed`

**•** `Failed and CsvNoPiiData - Scan failed. No sensitive data`

```
                     detected.

```

**•** `Failed and CsvUploadFailed - Scan failed. Results upload`

```
                     failed.

```

**•** `Failed and CsvUploadInProgress - Scan failed. Results`

```
                     upload in progress.

```

**•** `Failed and CsvUploadSuccess - Scan failed. Results upload`

```
                     completed successfully.

```

**•** `PartialSuccess`

**•** `PartialSuccess and CsvNoPiiData - Scan partially`

```
                     successful. No sensitive data detected.

```

**•** `PartialSuccess and CsvUploadFailed - Scan partially`

```
                     successful. Results upload failed.

```

**•** `PartialSuccess and CsvUploadInProgress - Scan partially`

```
                     successful. Results upload in progress.

```

**•** `PartialSuccess and CsvUploadSuccess - Scan partially`

```
                     successful. Results upload completed successfully.

```

**•** `Running`

**•** `Scheduled`

**•** `TimedOut`

The default value is `Scheduled` .


### Standard Objects DataDetectPolicy

**Field** **Details**

```
RunByUser

SessionStartTime

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
User who started the job session or data scan.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Time and date when the data scan begins.

This object has this associated object. If the API version isn’t specified, it's available in the same API version as this object. Otherwise, it's
available in the specified API version and later.

**[DataDetectJobSessionFeed](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

SEE ALSO:

_[Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.einstein_data_detect.htm&type=5&language=en_US)_ : Data Detect

### DataDetectPolicy

Represents a set of parameters that specifies the types of sensitive data to be searched for in a data scan. DataDetect scan policies can
also apply filters to a data scan, and select what specific objects and fields are to be scanned. This object is available in API version 60.0
and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Description

```

**Type**
string


Standard Objects DataDetectPolicy

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the scan policy.

```
EndTime

Name

OwnerId

ScanType

StartTime

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Time and date when the data scan completes.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the scan policy.

**Type**
reference

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The UserID of the person who owns the record. This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Designates whether the data scan type is `AIInference` or `PatternMatching` .

The default value is `PatternMatching` .

**Type**
dateTime


### Standard Objects DataDetectPolicyObject

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Time and date when the data scan begins. Data scans can start anytime within a 30-day
window from the current date.

Associated Objects

This object has this associated object. If the API version isn't specified, it's available in the same API version as this object. Otherwise, it's
available in the specified API version and later.

**[DataDetectPolicyShare](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.

SEE ALSO:

_[Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.einstein_data_detect.htm&type=5&language=en_US)_ : Data Detect

### DataDetectPolicyObject

Represents an object of the DataDetect scan policy to be scanned. This object is available in API version 62.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
DataDetectPolicyId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the scan policy associated with this scan policy object.

This field is a relationship field.

**Relationship Name**
### DataDetectPolicy

**Relationship Type**
Master-Detail


### Standard Objects DataDetectScanResult

**Field** **Details**

**Refers To**
DataDetectPolicy

```
Name

ObjectReference

```

SEE ALSO:

_[Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.einstein_data_detect.htm&type=5&language=en_US)_ : Data Detect

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the scan policy object.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Name of the scan policy object to be scanned.

### DataDetectScanResult

Represents the results of a DataDetect scan policy data scan. This object is available in API version 63.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
CreatedDate

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Time and date when an instance of PII is added to the scan result.


Standard Objects DataDetectScanResult

**Field** **Details**

```
DataDetectJobSessionId

FieldName

NamedEntityCount

NamedEntityType

ObjectName

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the job session associated with the scan policy.

This field is a relationship field.

**Relationship Name**
DataDetectJobSession

**Relationship Type**
Lookup

**Refers To**
DataDetectJobSession

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
UDD name from standard fields, or custom field ID from custom fields.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Number of times PII is found.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Type of PII found in the record of the scan policy object.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
KeyPrefix of the scan policy object that contains PII.


### Standard Objects DataDetectPolicyObjField

**Field** **Details**

```
RecordIdentifier

```

SEE ALSO:

_[Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.einstein_data_detect.htm&type=5&language=en_US)_ : Data Detect

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Unique identifier for the record.

### DataDetectPolicyObjField

Represents an object field of the DataDetect scan policy object to be scanned. This object is available in API version 64.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
DataDetectPolicyObjectId

FieldName

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the scan policy object associated with the scan policy object's field.

This field is a relationship field.

**Relationship Name**
DataDetectPolicyObject

**Relationship Type**
Master-Detail

**Refers To**
DataDetectPolicyObject

**Type**
string


### Standard Objects DataDetectPolicySnapshot

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Name of the scan policy object field.

SEE ALSO:

_[Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.einstein_data_detect.htm&type=5&language=en_US)_ : Data Detect

### DataDetectPolicySnapshot

Represents the snapshot of a DataDetect scan policy and its components retrieved during a job session. This object is available in API
version 64.0 and later.

Supported Calls

`delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `undelete()`,

Fields

**Field** **Details**

```
DataDetectPolicyId

Name

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the scan policy associated with the scan policy snapshot.

This field is a relationship field.

**Relationship Name**
### DataDetectPolicy

**Relationship Type**
Lookup

**Refers To**
### DataDetectPolicy

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


### Standard Objects DataDetPlcyDataSrchExps

**Field** **Details**

**Description**
Name of the scan policy snapshot.

```
OwnerId

RevisionNumber

SerializedPolicy

```

SEE ALSO:

_[Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.einstein_data_detect.htm&type=5&language=en_US)_ : Data Detect

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the record owner. This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Revision number of the scan policy snapshot associated with the scan policy.

**Type**
textarea

**Properties**
Nillable

**Description**
Sensitive data category item associated with the scan policy.

### DataDetPlcyDataSrchExps

Represents data search expressions for scanning DataDetect scan policies based on Java regex. This object is available in API version 64.0
and later.

Note: When working with regex, Salesforce recommends Java 17 or later.


Standard Objects DataDetPlcyDataSrchExps

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
DataDetectPolicyId

Expression

IsCaseSensitive

IsKeywordSearch

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the scan policy associated with the data search expression.

This field is a relationship field.

**Relationship Name**
DataDetectPolicy

**Relationship Type**
Master-Detail

**Refers To**
DataDetectPolicy

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Regular expression that represents sensitive data to be scanned.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Designates whether the expression is case-sensitive `(true)` or not `(false)` .

The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


### Standard Objects DataDetPlcyMdatScanCrit

**Field** **Details**

**Description**
Designates whether the expression can be used as a search keyword `(true)` or not
`(false)` .

The default value is `false` .

```
Name

```

SEE ALSO:

_[Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.einstein_data_detect.htm&type=5&language=en_US)_ : Data Detect

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the expression.

### DataDetPlcyMdatScanCrit

Represents inclusion and exclusion criteria that filter what DataDetect scan policy object fields are to be scanned based on metadata
tags. This object is available in API version 64.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Criteria

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines category of inclusion or exclusion criteria applied to fields during scan policy creation.
Valid values are:

**•** `ComplianceCategory` —Compliance acts, definitions, or regulations related to the
field's data.

**•** `DataSensitivity` —Level of data sensitivity related to the field's data.


Standard Objects DataDetPlcyMdatScanCrit

**Field** **Details**

**•** `FieldUsage` —Data planned for deprecation, or intended to be hidden, related to
the active and visible field's data.

```
DataDetectPolicyId

Name

Type

Value

```

SEE ALSO:

_[Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.einstein_data_detect.htm&type=5&language=en_US)_ : Data Detect

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the policy associated with the data search expression.

This field is a relationship field.

**Relationship Name**
DataDetectPolicy

**Relationship Type**
Master-Detail

**Refers To**
DataDetectPolicy

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the criteria.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines what criteria, `inclusion` or `exclusion`, is applied to a field in the policy scan
object.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Value of the criteria applied to filters.


### Standard Objects DataDetPlcySstvDataCatg DataDetPlcySstvDataCatg

Represents the sensitive data categories that the DataDetect scan policy is required to scan. This object is available in API version 64.0
and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
DataCategory

DataDetectPolicyId

Name

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Sensitive data category associated with the scan policy.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the scan policy associated with the sensitive data category.

This field is a relationship field.

**Relationship Name**
DataDetectPolicy

**Relationship Type**
Master-Detail

**Refers To**
DataDetectPolicy

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


### Standard Objects DataEncryptionKey

**Field** **Details**

**Description**
Name of the sensitive data category.

SEE ALSO:

_[Salesforce Help](https://help.salesforce.com/s/articleView?id=xcloud.einstein_data_detect.htm&type=5&language=en_US)_ : Data Detect

### DataEncryptionKey

The DataEncryptionKey object is part of the Bring Your Own Key (BYOK) feature, which allows users to upload a data encryption key
(DEK) using a public key generated by the Salesforce Shield Key Management Service (KMS). Customers create their own DEKs and
upload them to Salesforce. Users access this entity via the API to list DEK keys for auditing purposes. They can also programmatically use
this object to create the certificate and to upload key material. This object is available in API version 63.0 and later.

DEKs are used to encrypt and decrypt data. They reside in either the Salesforce database or in an external KMS. They’re created by root
keys, and when persisted, wrapped by root keys as well.

Supported Calls

`create()`, `describeSObjects()`, `query(), queryAll()`

Special Access Rules

This object is available as part of the Shield and Salesforce Platform Encryption add-on subscriptions.

Fields

**Field** **Details**

```
CreatedBy

### `DataEncryptionKeyCertName`

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The email address of the user who created the DEK. For example, `user@example.com` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the certificate whose public key is used to encrypt the `DEK` during a remote
key callout. When you want to create a BYOK-compatible certificate, use this property in a


Standard Objects DataEncryptionKey

**Field** **Details**

call to create() to name the certificate. You need to know the name to retrieve the certificate
later. Specify only the file name. Salesforce will add the .crt extension when it creates the
file.

```
Description

DoesUseKeyDerivation

LastModifiedBy

RootKeyIdentifier

RootKeyKmsIdentifier

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user-defined description of the root key.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the DEK is intended to be used as part of a derived key ( `true` ) or not
( `false` [). See Components Involved in Deriving Keys for information on derived keys.](https://developer.salesforce.com/docs/atlas.en-us.260.0.securityImplGuide.meta/securityImplGuide/security_pe_components.htm)

The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The email address of the user who most recently modified the key. For example,
`user@example.com` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique key identifier assigned by Salesforce to the root key used to create the DEK.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects DataEncryptionKey

**Field** **Details**

**Description**
The unique key identifier from the external KMS, such as an AWS Amazon Resource Name
(ARN). For example,

```
                   arn:aws:kms:us-west-2:123456789000:key/123ab456-7cd8-9012-3e4f-5gh678i901j2

```

```
SecretValue

SessionToken

Source

Status

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

The encrypted 256-bit secret value encoded in base64.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Contains the token for the session that was active when the DEK was last wrapped. If the
session is inactive, a new certificate is required in order to transmit the DEK.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The source of the encryption key material. Values are:

**•** `AWS` —A tenant secret or DEK fetched from the Amazon Key Management Service DEKs
with a `Source` value of `AWS` are listed as Fetched on the Key Management page in
Setup.

**•** `Salesforce` —A Salesforce-generated DEK.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The status of the key.

Possible values are:

**•** `Activation Pending` —Salesforce is waiting for confirmation of a valid key policy
in the external key store.

**•** `Active` —Can be used to encrypt new DEKs and decrypt existing DEKs.


Standard Objects DataEncryptionKey

**Field** **Details**

**•** `Archived` —Can’t encrypt new DEKs. Can be used to decrypt previously created DEKs.

**•** `Canceled` —Root key activation canceled by a user.

**•** `Inactive` —The root key, and the DEKs that it encrypts, are inaccessible. Inaccessible
DEKs can’t be used to decrypt data, which renders that data also inaccessible.

```
Type

Version

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of DEK. This value appears in the `Type` picklist:

**•** `Search Index` —search index files.

For Hyperforce orgs on API version 63.0 and later, create secrets of type `SearchIndex`
using the DataEncryptionKey object. For Hyperforce orgs on API versions 62.0 and earlier,
and for all non-Hyperforce orgs, create secrets of type `SearchIndex` using the
TenantSecret object.

You also specify a type of `SearchIndex` when you are creating a BYOK-compatible
certificate using the DataEncryptionKey object.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The version number of this secret. The version number is unique within your org.

Four functions are available: `describe()`, `create()`, `query()` and `queryAll()` .

**•** Use `create()` to create BYOK-compatible certificates and DEKs.

**•** Use `query()` or `queryAll()` to list one or all of your DEKs.

**•** Use `describe()` to get information abut the DataEncryptionKey object.

You use `create()` and `queryAll()` together to upload a Search Index Encryption DEK. Check the Examples section for how to
do each of these steps.

**•** Create a BYOK-compatible certificate with `create()` . This will create a temporary DEK to contain the certificate reference. Specify
a Type of `Search Index` and a name for the certificate file.

**•** Use `queryAll()` to list your DEKs. The temporary DEK will include the name of your certificate file in the
`DataEncryptionKeyCertName` attribute. It will also include a session token in the `sessionToken` attribute. Save this
value for later.


Standard Objects DataEncryptionKey

**•** Downlad the certificate using the metadata object API. Specify _`Certificate`_ for the object name node, and the
_`DataEncryptionKeyCertName`_ for the members node. The certificate file will be in the zip file returned by the metadata
object API.

**•** [Run the BYOK Search Index Encryption script to generate the](https://help.salesforce.com/s/articleView?id=xcloud.security_pe_byok_script_seas_tle.htm&type=5&language=en_US) **payload.bin** file which contains the plaintext of your new DEK. Use
the certificate file you created when you run the script. Alternatively, generate a key using a method of your choice. It must meet
[the specifications outlined in Bring Your Own Key Overview.](https://help.salesforce.com/s/articleView?id=xcloud.security_pe_byok.htm&type=5&language=en_US)

**•** Generate a b64 string from the contents of the **payload.bin** file.

**•** Run the `DataEncryptionKey.create()` method again, this time with the the b64 string and the session token. Specify:

```
     "SecretValue":"<b64 string>"

     "SessionToken":"<session token string>"

     "Type":"SearchIndex"

```

With success, the temporary DEK is replaced by the uploaded secret. The certificate is deleted, and the session token eventually
expires. A call to `queryAll()` will show the new DEK. The DEK will also appear on the Search Index Encryption Key Management
page.

Examples

[Use your preferred developer environment to run the examples. Use the Salesforce developer Introduction to REST API for basic information](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_rest.meta/api_rest/intro_rest.htm)
[on making REST calls into Salesforce. Also, Introducing the Salesforce Shield Platform Encryption REST API gives you starter information](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_encryption_rest_api_guide.meta/platform_encryption_rest_api_guide/api_rest_encryption.htm)
on using REST to work with Shield Platform Encryption.

**Create a BYOK-compatible certificate with** **`create()`**

To create a BYOK-compatible certificate, use a POST method to create an sObject of type `DataEncryptionKey` . Specify a Type
of `search index` (case insensitive), and an appropriate string value for DataEncryptionKeyCertName. You need to name the
certificate to retrieve it later. Specify just the name. Salesforce will add the .crt extension to the file.

```
     curl --location 'https://DOMAIN.my.salesforce.com/services/data/v62.0/sobjects/'\

                  DataEncryptionKey/create'

        --header 'Content-Type: application/json' \

        --header 'Authorization: Bearer TOKEN' \

        --data '{

             "Type": "search index",

             "DataEncryptionKeyCertName": "my-byok-compatible-cert"

            }'

```

**List all DEKs with** **`queryAll()`**

To retrieve DEKs, use `query` or `queryAll` on the `DataEncryptionKey` sObject. You must specify a limit for the query. All
DEKs are retrieved, including archived DEKs. You use `queryAll` to get the session token.

```
     curl --location

     'https://DOMAIN.my.salesforce.com/services/data/v63.0/queryAll/?q=SELECT+FIELDS(ALL)+FROM+DataEncryptionKey+LIMIT+10'

      \

                  --header 'Authorization: Bearer TOKEN'

```

**Download your Certificate**

[Retrieve the certificate using Metadata API. object to download your new certificate.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_meta.meta/api_meta/file_based_zip_file.htm)

```
     <?xml version="1.0" encoding="UTF-8"?>

     <Package xmlns="http://soap.sforce.com/2006/04/metadata">

       <types>

```


Standard Objects DataEncryptionKey

```
         <members>DataEncryptionKeyCertName</members>

         <name>Certificate</name>

       </types>

       <version>65.0</version>

     </Package>

```

Your certificate will be contained in the cert folder.

**Create a DEK with** **`create()`**

To create the final DEK, use a POST method to create an sObject of type `DataEncryptionKey` . Specify a Type of `search`
`index` (case insensitive).

```
     curl --location

     'https://DOMAIN.my.salesforce.com/services/data/v63.0/sobjects/DataEncryptionKey/create'

      \

     --header 'Content-Type: application/json' \

     --header 'Authorization: Bearer TOKEN' \

     --data '{

       "SecretValue":"b64-secret"

       "SessionToken":"session-token value"

       "Type": "search index"

     }'

```

**Describe a DataEncryptionKey with** **`describe()`**

To get information about the DataEncryptionKey sObject, use `describe` .

```
     curl --location 'https://DOMAIN.my.salesforce.com/services/data/v62.0/sobjects/'\

                  DataEncryptionKey/describe'

                  --header 'Content-Type: application/json' \

                  --header 'Authorization: Bearer TOKEN'

```

On success, the response is the full JSON description of the DataEncryptionKey sObject.

**Return Values for Create()**

The response for creating a certificate or DEK are the same. On success, the response is be similar to

```
     {

       "totalSize": (COUNT),

       "done": true,

       "records": [

         {

          "attributes": {

          "type": "DataEncryptionKey",

          "url": "/services/data/v63.0/sobjects/DataEncryptionKey/(ID)"

          },

          ATTRIBUTE LIST

         },

       ]

```

On error, the response is similar to

```
     [

       {

         "message": "ERROR MESSAGE",

         "errorCode": "ERROR CODE"

```


### Standard Objects DataIntegrationRecordPurchasePermission

```
       }

     ]

### DataIntegrationRecordPurchasePermission

```

Indicates Lightning Data purchase credits that a Salesforce admin has granted to users.

This object is available in API versions 42.0 and later.

Supported Calls

`describeSObjects()`, `create()`, `delete()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Spring ’20 and later, only your Salesforce org's internal users can access this object.

Fields

**Field Name** **Details**

```
ExternalObject

UserId

UserRecordPurchaseLimit

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the name of the data service record matched to the Salesforce record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Indicates the ID of a user to whom purchase credits are assigned.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

**Type**
int


### Standard Objects DataKitDeployEvent

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the number of purchase credits assigned to a user.

### DataKitDeployEvent

Represents a data kit deployment event that notifies subscribers of the status of the data kit component deployment. This object is
available in API version 61.0 or later.

Supported Calls

`create()`, `describeSObjects()`

Special Access Rules

Users that have access to Data Cloud.

Fields

**Field** **Details**

```
DataKitDeployStatus

DataKitName

```

**Type**
picklist

**Properties**
Create, Nillable, Restricted picklist

**Description**
The deployment status of the components deployed from a data kit. This field is available in
API version 63.0 and later. Possible values are:

**•** `Active`

**•** `Deleting`

**•** `Error`

**•** `Inactive`

**•** `Processing`

**Type**
string

**Properties**
Create, Nillable


Standard Objects DataKitDeployEvent

**Field** **Details**

**Description**
Name of the data kit from which a component is deployed.

```
DataspaceName

DeployStartTime

ErrorDetails

EventCreationDate

EventPublishDate

EventType

```

**Type**
string

**Properties**
Create, Nillable

**Description**
Name of the data space into which a component is deployed.

**Type**
dateTime

**Properties**
Create, Nillable

**Description**
The date and time the deployment starts.

**Type**
textarea

**Properties**
Create, Nillable

**Description**
Explanation of the error.

**Type**
dateTime

**Properties**
Create, Nillable

**Description**
The date and time the data kit deploy creation event was created.

**Type**
dateTime

**Properties**
Create, Nillable

**Description**
The date and time of the data kit deploy publish event.

**Type**
picklist

**Properties**
Create, Nillable, Restricted picklist


Standard Objects DataKitDeployEvent

**Field** **Details**

**Description**
The event type action of the data kit components. Available in API version 66.0 and later.
Possible values are:

**•** `Deploy`

**•** `Undeploy`

```
EventUuid

IsDataKitDeployStatusSuccess

JobIdentifier

ReplayId

TemplateName

```

**Type**
string

**Properties**
Nillable

**Description**
The unique ID of the event.

**Type**
string

**Properties**
Create, Nillable

**Description**
Status of the data kit component deployment. Possible values are:

**•** `Active`

**•** `Failure`

**Type**
string

**Properties**
Create, Nillable

**Description**
Data kit component deployment job identifier.

**Type**
string

**Properties**
Nillable

**Description**
The ID of the data kit deploy event replay.

**Type**
string

**Properties**
Create, Nillable


### Standard Objects DataKitDeploymentLog

**Field** **Details**

**Description**
The template name from which the data kit deploy event is created.

### DataKitDeploymentLog

Represents the log details of a data kit component deployment. This object is available in API version 61.0 or later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

Users that have access to Data Cloud.

Fields

**Field** **Details**

```
BundleName

ComponentName

ComponentTemplateId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the data stream bundle if a data stream is deployed from a data kit.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the component that’s deployed from a data kit.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the data kit template from which the component is deployed. This field is a polymorphic
relationship field.


Standard Objects DataKitDeploymentLog

**Field** **Details**

**Relationship Name**
ComponentTemplate

**Refers To**
DataSourceBundle

```
ComponentType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of the component for which the deployment is tracked in the log details.

Possible values are:

**•** `MktCalculatedInsight`

**•** `MktDataLakeObject`

**•** `MktDataModelObject`

**•** `MktDataStream`

**•** `MktDataTransform`

Possible values available in API version 63.0 and later are:

**•** `ActivationTarget`

**•** `DataAction`

**•** `DataActionTarget`

**•** `DataGraph`

**•** `DataSemanticSearch`

**•** `EngagementSignal`

**•** `ExtDataShare`

**•** `IdentityResolution`

**•** `MarketSegment`

**•** `MarketSegmentActivation`

**•** `MktDataConnection`

**•** `MktMLModel`

**•** `PersonalizationObjective`

**•** `PersonalizationRecommender`

Possible values available in API version 64.0 and later are:

**•** `IrRelatedListEnrichment`

**•** `MktCalculatedInsight`

**•** `MktDataLakeObject`

**•** `MktDataStream`

**•** `MktDataTransform`


Standard Objects DataKitDeploymentLog

**Field** **Details**

**•** `PersonalizationPoint`

**•** `PersonalizationSchema`

Possible values available in API version 66.0 and later are:

**•** `CopyFieldEnrichment`

**•** `SemanticModel`

```
DataKitName

DataPackageKitDefinition

DataSpaceName

DeployJob

DeploymentAction

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the data kit being deployed.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
ID of the data kit being deployed. Available in API version 63.0 and later.

Possible values are:

**•** `1dk.Collections`

**•** `1dk.SalesNextGenForecastingDatakit`

**•** `1dk.Test_Fbdk`

**•** `1dk.sf_mktg_ae__Marketing_Account_Engagement_CRM_Data`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the data space the components are deployed to.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The deployment job ID.

**Type**
picklist


Standard Objects DataKitDeploymentLog

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Deployment action of the data kit components.

Possible values are:

**•** `Deploy`

**•** `Undeploy`

```
DeploymentError

DeploymentStatus

FileBasedComponentTemplate

FlowInterviewIdentifier

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Contains the error details if the data kit deployment fails.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Deployment status of the data kit components.

Possible values are:

**•** `Failed`

**•** `Started`

**•** `Successful`

**Type**
string

**Properties**
Create, Filter, Sort, Update

**Description**
ID of the file-based component template that corresponds to the deployment log entry.
Available in API version 63.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Identifier of the flow interview if the deployment was triggered using a flow.


Standard Objects DataKitDeploymentLog

**Field** **Details**

```
JobIdentifier

LastReferencedDate

LastViewedDate

Name

OwnerId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Identifier of the data kit component deployment job. Available in API version 66.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed the deployment log file.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this deployment log.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The name of the deployment log.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user that owns the deployment.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User


Standard Objects DataKitDeploymentLog

**Field** **Details**

```
PublisherOrgComponentId

SubscriberOrgComponentId

TemplateVersion

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the component in the publisher org.

This field is a polymorphic relationship field.

**Relationship Name**
PublisherOrgComponent

**Refers To**
MktCalculatedInsight, MktDataTransform

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the component in the subscriber org in which the components of a data kit are
deployed.

This field is a polymorphic relationship field.

**Relationship Name**
SubscriberOrgComponent

**Refers To**
ActivationTarget, DataGraph, DataStream, ExtDataShare, IdentityResolution, MarketSegment,
MarketSegmentActivation, MktCalculatedInsight, MktDataTransform

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The version of the template from which the deployment was done.

Use the DataKitDeploymentLog object to track the deployment of a data kit component.


### Standard Objects DatasetExport DatasetExport

Represents a dataset exported from CRM Analytics. When a dataset is exported, the data is converted into a .csv file and the schema is
stored in a separate JSON file. These files are stored in two objects: DatasetExport and DatasetExportPart. DatasetExport acts as the header
and includes the JSON schema.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
CompressedMetadataLength

Metadata

MetadataLength

Owner

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is required when a record in an object contains a BLOB (binary large object) field.
In the DataExport object, Metadata is the BLOB field.

**Type**
base64

**Properties**
Nillable

**Description**
Contains the JSON schema that describes the data in the CSV. This schema includes column
metadata such as type, format, and defaultValue.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is required when a record in an object contains a BLOB (binary large object) field.
In the DataExport object, Metadata is the BLOB field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects DatasetExport

**Field** **Details**

**Description**
User ID of the owner, as specified in the `userId` parameter in the export node of the
dataflow that created the record. Only the specified owner can read the content of the record.

```
PublisherInfo

PublisherType

Status

```

**Type**
string

**Properties**
Filter, idLookup, Sort

**Description**
Identifies the export record to facilitate searching when a user has multiple export records.
By default, this column is set to the ID of the dataflow that generated the export record,
concatenated with the name of the specific export node. PublisherInfo is unique within your
organization.

Note: A dataflow can have multiple export nodes.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Target of the export, as specified in the `target` parameter in the export node of the
dataflow that created the record. The value must be _`EinsteinDiscovery`_ .

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Status of the export. The possible values are:

**•** New

**•** InProgress

**•** Completed

**•** Canceled

**•** Failed

Note: The content of the Metadata field can be downloaded when the status is
Completed.


### Standard Objects DatasetExportPart

Usage

This object is used with the DatasetExportPart object for exporting data from a dataset in CRM Analytics for use in Einstein Discovery.
An export is initiated using the export node in an Analytics dataflow.

SEE ALSO:

### DatasetExportPart DatasetExportPart

Represents a dataset exported from CRM Analytics. When a dataset is exported, the data is converted into a .csv file and the schema is
stored in a separate JSON file. These files are stored in two objects: DatasetExport and DatasetExportPart. DatasetExportPart contains
parts of the .csv file.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
CompressedDataFileLength

DataFile

DataFileLength

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
This field is required when a record in an object contains a BLOB (binary large object) field.
In the DataExportPart object, DataFile is the BLOB field.

**Type**
base64

**Description**
Contains a part of the dataset data from the generated .csv file. Maximum size is 32 MB.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
This field is required when a record in an object contains a BLOB (binary large object) field.
In the DataExportPart object, DataFile is the BLOB field.


### Standard Objects DataMaskCustomValueLibrary

**Field** **Details**

```
 DatasetExportId

 Owner

 PartNumber

```

Usage

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the parent record that the part record is associated with.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
User ID of the owner, as specified in the `userId` parameter in the export node of the
dataflow that created the record. Only the specified owner can read the content of the record.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Used with the DatasetExportId to uniquely identify the data part. Parts are assembled
sequentially based on their numbers.

This object is used with the DatasetExport object for exporting data from a dataset in CRM Analytics for use in Einstein Discovery. An
export is initiated using the export node in an Analytics dataflow.

SEE ALSO:

DatasetExport

### DataMaskCustomValueLibrary

Represents a set of user-inputted values in a custom library in Data Mask. This object is available in API version 64.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects DataMaskCustomValueLibrary

Special Access Rules

This object is available with the Sandbox Data Mask managed package.

Fields

**Field** **Details**

```
ContentType

Description

IsActive

LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of value used in a field of the custom library.

Possible values are:

**•** `email`

**•** `number`

**•** `phone_number`

**•** `string`

**•** `url`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the value in the custom library.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Represents whether the library is active or inactive for use.

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.


Standard Objects DataMaskCustomValueLibrary

**Field** **Details**

```
LastViewedDate

Name

OwnerId

Type

Values

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the custom library.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the custom library.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Represents how the values were added to the library.

Possible values are:

**•** `default`

**•** `user_defined`

**Type**
textarea

**Properties**
Create, Nillable, Update


### Standard Objects DataStatistics

**Field** **Details**

**Description**
The content of the value field for masking data.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**DataMaskCustomValueLibraryOwnerSharingRule on page 65**
Sharing rules are available for the object.

**DataMaskCustomValueLibraryShare on page 67**
Sharing is available for the object.

### DataStatistics

For internal use only.

### DataUseLegalBasis

Represents the legal basis for contacting a customer, such as billing or contract. This object is available in API version 45.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available if Data Protection and Privacy is enabled.

Fields

**Field Name** **Details**

```
Description

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the data use legal basis.


Standard Objects DataUseLegalBasis

**Field Name** **Details**

```
LastReferencedDate

LastViewedDate

Name

OwnerId

Source

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this
record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is
null, it’s possible that this record was referenced ( `LastReferencedDate` )
and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Specifies a name for the legal basis. For example, “billing” or “contract”.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the account associated with this customer.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
string


### Standard Objects DataUsePurpose

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the source of the legal basis. For example, the URL of a contract.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**DataUseLegalBasisChangeEvent (API version 62.0)**
Change events are available for the object.

**DataUseLegalBasisHistory**

History is available for tracked fields of the object.

**DataUseLegalBasisOwnerSharingRule**

Sharing rules are available for the object.

**DataUseLegalBasisShare**

Sharing is available for the object.

### DataUsePurpose

Represents the reason for contacting a prospect or customer, such as for billing, marketing, or surveys. This object is available in API
version 45.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available if Data Protection and Privacy is enabled.

Fields

**Field Name** **Details**

```
CanDataSubjectOptOut

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects DataUsePurpose

**Field Name** **Details**

**Description**
Required. Indicates whether the customer can decline contact for the described
purpose.

```
Description

LastReferencedDate

LastViewedDate

LegalBasisId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the purpose for contacting a customer.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this
record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is
null, it’s possible that this record was referenced ( `LastReferencedDate` )
and not viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Identifies the legal basis record associated with the data use purpose.

This is a relationship field.

**Relationship Name**
LegalBasis

**Relationship Type**
Lookup

**Refers To**
DataUseLegalBasis


Standard Objects DataUsePurpose

**Field Name** **Details**

```
Name

OwnerId

PurposeId

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Identifies the reason for contacting a customer. For example, billing or
marketing.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the account associated with this customer.

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
The ID of an object containing data specific to the data use purpose.

This is a polymorphic relationship field.

**Relationship Name**
Purpose

**Relationship Type**
Lookup

**Refers To**
Asset, CareProgram, CareRegisteredDevice, or Product2

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.


### Standard Objects DataWeaveResource

**DataUsePurposeChangeEvent (API version 62.0)**
Change events are available for the object.

**DataUsePurposeHistory**

History is available for tracked fields of the object.

**DataUsePurposeOwnerSharingRule**

Sharing rules are available for the object.

**DataUsePurposeShare**

Sharing is available for the object.

### DataWeaveResource

Represents the DataWeaveScriptResource class that is generated for all DataWeave scripts. This object is available in API version 58.0
and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`

Fields

**Field** **Details**

```
ApiVersion

BodyLength

ContentType

```

**Type**
double

**Properties**
Filter, Sort

**Description**
The API version of this component.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Size of the DataWeave script (in bytes).

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


Standard Objects DataWeaveResource

**Field** **Details**

**Description**
Possible value:

**•** `dwl` : The metadata file for the DataWeave scripts that are deployed to an org.

```
DeveloperName

IsGlobal

IsProtected

Language

MasterLabel

NamespacePrefix

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name of the object in the API.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
When set to true, the generated `DataWeaveScriptResource` class is global. The
default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Not used

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the MasterLabel.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Required. The name of the resource.

**Type**
string


### Standard Objects DatedConversionRate

**Field** **Details**

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

**•** In orgs that aren’t Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

Usage

Although the `DataWeaveResource` object supports the create and update field properties, a runtime exception occurs if you try
to create, update, or delete using the API. Instead, use the Salesforce Extensions for Visual Studio Code.

### DatedConversionRate

Represents the dated exchange rates used by an organization for which the multicurrency and the effective dated currency features are
enabled.

Supported Calls

`delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

Special Access Rules

Customer Portal users can't access this object.

Fields

**Field** **Details**

```
ConversionRate

```

**Type**
double


### Standard Objects DealIndirectPartner

**Field** **Details**

**Properties**
Filter, Update

**Description**
Required. Conversion rate of this currency type against the corporate currency.

```
IsoCode

NextStartDate

StartDate

```

Usage

**Type**
picklist

**Properties**
Filter, Restricted picklist

**Description**
Required. ISO code of the currency. Must be one of the valid alphabetic, three-letter currency
ISO codes defined by the ISO 4217 standard, such as `USD`, `GBP`, or `JPY` . Must be unique
within your organization. Label is **Currency ISO Code** .

**Type**
date

**Properties**
Filter, Nillable

**Description**
Read only. The date on which the next effective dated exchange rate will start. Effectively
the day after the end date for this exchange rate.

**Type**
date

**Properties**
Filter

**Description**
The date on which the effective dated exchange rate starts. The timestamp is determined
by the base calendar of the API.

This object is for multicurrency organizations with advanced currency management enabled. Use this object to define the exchange
rates your organization uses for a date range. This object is not available in single-currency organizations, nor is it available if the
organization does not have advanced currency management enabled.

### DealIndirectPartner

Represents an indirect partner’s involvement in a deal. This object is available in API version 63.0 and later.

A DealIndirectPartner record can be created manually or through automation when a partner is associated with an opportunity, lead,
or account, capturing role and contact information.


Standard Objects DealIndirectPartner

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AccountId

LastReferencedDate

LastViewedDate

LeadId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The account associated with the indirect partner on the deal.

This field is a relationship field.

**Relationship Name**
Account

**Refers To**
Account

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the record was last referenced by the user or system.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and the timestamp when the record was last viewed in the Salesforce UI. Helps monitor
user access and engagement.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Reference to a lead associated with this indirect partner record.

This field is a relationship field.


Standard Objects DealIndirectPartner

**Field** **Details**

**Relationship Name**
Lead

**Refers To**
Lead

```
Name

OpportunityId

OwnerId

PartnerName

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-generated unique identifier for the record, used for lookup and reference purposes.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Opportunity associated with the indirect partner.

This field is a relationship field.

**Relationship Name**
Opportunity

**Refers To**
Opportunity

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
User or group that owns this record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects DealIndirectPartner

**Field** **Details**

**Description**
Name of the indirect partner participating in the deal. This field captures the business or
entity name.

```
PartnerRoleType

PrimaryContactFirstName

PrimaryContactLastName

PrimaryContactName

PrimaryContactSalutation

```

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The role played by the indirect partner in the deal. Common values might include Reseller,
Distributor, and so on.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
First name of the primary contact at the partner organization.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Last name of the primary contact at the partner organization.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Full name of the primary contact. This field may be auto-generated by combining first and
last names or used for reporting purposes.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Salutation for the primary contact.

Possible values are:


### Standard Objects DeclinedEventRelation

**Field** **Details**

**•** `Dr.`

**•** `Mr.`

**•** `Mrs.`

**•** `Ms.`

**•** `Mx.`

**•** `Prof.`

### DeclinedEventRelation Represents event participants (invitees or attendees) with the status Declined for a given event.This object is available in API versions

29.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
EventId

RelationId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the event.

This is a relationship field.

**Relationship Name**
Event

**Relationship Type**
Lookup

**Refers To**
Event

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the invitee.


Standard Objects DeclinedEventRelation

**Field Name** **Details**

This is a polymorphic relationship field.

**Relationship Name**
Relation

**Relationship Type**
Lookup

**Refers To**
Calendar, Contact, Lead, User

```
RespondedDate

Response

Type

```

Usage

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates the most recent date and time when the invitee declined an invitation
to the event.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the content of the response field. Label is `Comment` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates whether the invitee is a user, lead or contact, or resource.

**Query invitees who have declined an invitation to an event**

```
  SELECT eventId, type, response FROM DeclinedEventRelation WHERE eventid='00UTD000000ZH5LA'

```

SEE ALSO:

AcceptedEventRelation

UndecidedEventRelation


### Standard Objects DelegatedAccount DelegatedAccount

Represents the external managed account. This object is available in API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Special Access Rules

You must have a Partner or Customer Community Plus license. You can't edit the visibility of DelegatedAccount metadata on user profiles.

Fields

**Field** **Details**

```
AccessBuyFor

AccessManageUsers

LastReferencedDate

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
The access that an admin authorizes for an external user to buy for other accounts. This field
is available in API version 50.0 and later. A B2B Commerce license is required to use
AccessBuyFor.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
The access that an admin authorizes for an external user to manage external users on other
accounts. This includes managing permission sets, membership, passwords, and activation.
This field is available in API version 50.0 and later. Delegated External User Administrator
permission is required to use AccessManageUsers.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.


Standard Objects DelegatedAccount

**Field** **Details**

```
LastViewedDate

ManagedById

Name

OwnerId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced ( `LastReferencedDate` ) and not viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the managing user.

This is a relationship field.

**Relationship Name**
ManagedBy

**Relationship Type**
Lookup

**Refers To**
User

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the external managed account.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the record owner.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup


### Standard Objects DeleteEvent

**Field** **Details**

**Refers To**
Group, User

```
ParentId

TargetId

### DeleteEvent

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the managing users account. This field is available in API version 50.0 and later.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the account being managed.

This is a relationship field.

**Relationship Name**
Target

**Relationship Type**
Lookup

**Refers To**
Account

Represents a record that has been soft deleted. Search on this object was available in API version 48.0, then removed in API version 50.0.

### DeleteEvent is a read-only object. You can't create, update, or delete it directly. To create a DeleteEvent record, soft delete a record of

[another type, like an Account. To remove a DeleteEvent record, use the emptyRecycleBin() API or hard delete the corresponding](https://developer.salesforce.com/docs/atlas.en-us.260.0.api.meta/api/sforce_api_calls_emptyrecyclebin.htm) `Record` .

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`


Standard Objects DeleteEvent

Fields

**Field** **Details**

```
DeletedById

DeletedDate

Record

RecordName

SobjectName

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user who deleted the record.

This is a relationship field.

**Relationship Name**
DeletedBy

**Relationship Type**
Lookup

**Refers To**
User

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the record was deleted.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the record that was deleted.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the record that was deleted.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects DeliveryEstimationSetup

**Field** **Details**

**Description**
The type of record that was deleted, for example, Account.

### DeliveryEstimationSetup

Shows the configuration options for the commerce delivery service offered through a web store or sales channel. Includes settings such
as delivery location group, channel, fulfillment types, and default fulfillment time. This object is available in API version 61.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The DeliveryEstimationSetup object is available only if the B2B Commerce or D2C Commerce license is enabled.

Fields

**Field** **Details**

`Channel` Id

`DefaultBusinessHours` Id

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID for the web store or sales channel associated with the delivery estimation configuration.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID for the default business hours.

This is a relationship field.

**Relationship Name**
DefaultBusinessHours

**Refers To**
BusinessHours


Standard Objects DeliveryEstimationSetup

**Field** **Details**

```
DefaultPickupTime

DefaultProcessingTime

DefaultProcessingTimeUnit

ExternalReference

isEnabled

```

**Type**
time

**Properties**
Create, Filter, Sort, Update

**Description**
Default pickup time.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Default processing time.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Default processing time unit. Possible values are:

**•** `Hours`

**•** `Days`

**•** `Weeks`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Unique code, reference, or identifier for the delivery estimation configuration record used
by external systems. Can be the name of the web store or sales channel associated with the
configuration to ensure a unique ID within the organization.

For example, `DefaultWebstore123` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the given delivery estimation configuration is active.

The default value is `false` .


Standard Objects DeliveryEstimationSetup

**Field** **Details**

```
LastReferencedDate

LastSyncedById

LastSyncedDate

LastSyncedMessage

LastViewedDate

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the record was last modified. Its label in the user interface is `Last`
`Modified Date` .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
User ID of who performed the last sync for this delivery estimation configuration. This field
is available in API version 62.0 and later.

This is a relationship field.

**Relationship Name**
LastSyncedBy

**Refers To**
User

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date the delivery estimation configuration was last synced. This field is available in API version
62.0 and later.

**Type**
textarea

**Properties**
Nillable

**Description**
Message that occurred during the last sync. This field is available in API version 62.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects DeliveryEstimationSetup

**Field** **Details**

**Description**
Last time the delivery estimation configuration was viewed.

```
LocationGroupId

Name

OwnerId

RoutingType

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Represents a group of Omnichannel Inventory locations.

This is a relationship field.

**Relationship Name**
LocationGroup

**Refers To**
LocationGroup

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the delivery estimation setup configuration.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who currently owns this DeliveryEstimationSetup object. Default value is the
user logged in to the API to perform the create.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


### Standard Objects DigitalSignature

**Field** **Details**

**Description**
Determines an order's route and calculates delivery estimations. This field is available in API
version 65.0 and later.

Possible values are:

**•** `DRE`

**•** `None`

**•** `Standard`

The default value is `None` .

```
ServiceRegion

SyncStatus

### DigitalSignature

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
An org's commerce delivery service provisioning region (North America, Europe, or Asia)
that's set when Delivery Estimation is enabled in the Order Management app. It can't be
changed. If the field is empty, provisioning hasn't occurred yet. Available in API version 63.0
and later.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Sync status of the delivery estimation setup configuration.

Possible values are:

**•** `Deleting`

**•** `Deprovisioned`

**•** `Error`

**•** `None`

**•** `Synced`

**•** `Syncing`

The default value is `NONE` . This field is available in API version 62.0 and later.

Represents a signature captured on a service report in field service.


Standard Objects DigitalSignature

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,

```
   undelete()

```

Special Access Rules

Field Service must be enabled.

Fields

**Field Name** **Details**

```
DigitalSignatureNumber

DocumentBody

DocumentContentType

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number identifying the signature.

**Type**
base64

**Properties**
Create

**Description**
The captured signature image.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The data type of the captured signature. Possible values are:

**•** `audio/acc`

**•** `audio/amr`

**•** `audio/ogg`

**•** `video/3gpp2`

**•** `video/3gpp`

**•** `image/avif`

**•** `text/calendar`

**•** `audio/x-caf`

**•** `image/webp`


Standard Objects DigitalSignature

**Field Name** **Details**

```
DocumentLength

DocumentName

ParentId

Place

SignatureType

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The length of the captured signature.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The name of the captured signature image.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the service appointment, work order, or work order line item that the service
report is generated for.

This is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
AuthorizationFormConsent, Order, ServiceAppointment, WorkOrder,
WorkOrderLineItem

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The place where the report was signed.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort


Standard Objects DigitalSignature

**Field Name** **Details**

**Description**
The role of the person signing the service report. Your org comes with one
signature type, `Default` . A service report template can only contain one
signature per type. If you plan to collect multiple signatures on service reports,
create additional values for the Signature Type field.

Create at least one value for every role that might need to sign a service report.
For example, `Technician`, `Customer`, `Supervisor`, or `Supplier` . If
some service reports will be signed by multiple people in one role—for example,
all technicians present at an appointment—create numbered types:
`Technician 1`, `Technician 2`, and so forth.

Note: You can create up to 1,000 signature types. You can’t delete
signature types, but you can deactivate them so they can’t be used in
service report templates. When you deactivate a type, it still appears on
service report templates that used it, but you can’t use it on new service
report templates.

```
SignedBy

SignedDate

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The name of the person signing.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The date and time of the signing.

Add signature blocks to service report templates to determine which signatures need to be gathered on reports that use the template.
Service report templates can contain up to 20 signatures, and each signature must use a different Signature Type. For example, create
a standard service report template that contains a customer signature and a technician signature.

[To learn more about digital signatures, see Guidelines for Using Signatures on Service Reports.](https://help.salesforce.com/articleView?id=fs_signature_guidelines.htm&language=en_US)

Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**DigitalSignatureChangeEvent (Available in API version 57.0)**
Change events are available for the object.


### Standard Objects DigitalWallet DigitalWallet

Represents a customer’s digital wallet service. Salesforce Payments can use a digital wallet as a payment source when processing
payments through a payment gateway. This object is available in API version 48.0 and later.

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
The account of the customer owns the digital wallet.

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

**Description**
Email address of the digital wallet owner where audit information about payments gets sent.

This field is available in API v49.0 and later. It doesn’t appear in the UI by default for Salesforce
orgs that upgraded from v48.0. Users must add it to the DigitalWallet page layout on their
own.


Standard Objects DigitalWallet

**Field** **Details**

```
BillingName

Comments

CompanyName

Customer

DigitalWalletNumber

Email

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Billing name linked to customer's digital wallet. Available in API version 64.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Users can provide additional details about the digital wallet. Supports a maximum of 1000
characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Company of the digital wallet owner.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Customer name of the digital wallet owner.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-generated reference number for the digital wallet.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects DigitalWallet

**Field** **Details**

**Description**
Email of the digital wallet owner.

```
ExtendedPaymentMethodType

GatewayToken

GatewayTokenDetails

GatewayTokenEncrypted

IpAddress

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Other digital payment methods used for the transaction. This field value is required when
the value of the `PaymentMethodType` field is
`extd_altrn_payment_method_type` or `extd_wallet` . This field is available
in API version 66.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Unencrypted unique token ID generated by the payment gateway to represent the digital
wallet during transactions. This field is available for backward compatibility. To secure the
token, use the `GatewayTokenEncrypted` field.

If you try to record a GatewayToken for a digital wallet that already has a GatewayToken or
GatewayTokenEncrypted value, Salesforce throws an error.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Unique ID generated by the payment gateway for the card for future transactions.

**Type**
encryptedstring

**Properties**
Create, Nillable, Update

**Description**
Encrypted unique token ID generated by the payment gateway to represent the digital wallet
during transactions. Encrypted using Salesforce Classic Encryption for custom fields.

Available in API v52.0 and later.

**Type**
string


Standard Objects DigitalWallet

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The IP address of the digital wallet owner.

This field is available in API v49.0 and later. It doesn’t appear in the UI by default for Salesforce
orgs that upgraded from v48.0. Users must add it to the DigitalWallet page layout on their
own.

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

Indicates whether the payment method can be used for recurring payments (True) or not
(False). The default value is False.

This field is available in API v55.0 and later. For orgs that upgraded from v54.0, you must add
this field to the Digital Wallet page layout in the UI. It isn't automatically added.

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
The timestamp for when the current user last viewed this record. If this value is null, it's
possible the user only referenced this record (LastReferencedDate) but not viewed it.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The MAC address of the digital wallet owner.

This field is available in API v49.0 and later. It doesn’t appear in the UI by default for Salesforce
orgs that upgraded from v48.0. Users must add it to the DigitalWallet page layout on their
own.


Standard Objects DigitalWallet

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
User-defined nickname for the digital wallet.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Gateway used with transactions for the digital wallet.

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
Full address associated with the digital wallet payment method. For more information about
address fields, see Address Compound Fields

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Part of the address for the payment method.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects DigitalWallet

**Field** **Details**

**Description**
Part of the address for the payment method.

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


Standard Objects DigitalWallet

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
Part of the address for the payment method.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Part of the address for the payment method.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Part of the address for the payment method.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
More information about the payment method. For example, if the PaymentMethodType is
Visa, this field can be digital wallet. This field is available in API version 57.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects DigitalWallet

**Field** **Details**

**Description**
Payment method used for the transaction. Possible values include credit cards such as Visa
and American Express, digital wallets like Apple Pay and PayPal, direct debits such as ACH,
BECS, Bacs, non-card payments methods such as EPS, SEPA, and iDEAL, extended alternate
payments methods, and extended wallets. This field is available in API version 57.0 and later.

```
Phone

ProcessingMode

SavedPaymentMethodId

```

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number of the digital wallet owner.

This field is available in API v49.0 and later. It doesn’t appear in the UI by default for Salesforce
orgs that upgraded from v48.0. Users must add it to the DigitalWallet page layout on their
own.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Defines whether the digital wallet is used for transactions made inside or outside the payment
platform.

Possible values are:

**•** `External` —Transactions happened outside of the Salesforce payments platform.

**•** `Salesforce` —Salesforce made and recorded an external call to the payment platform.

This field is available in API v49.0 and later. It doesn’t appear in the UI by default for Salesforce
orgs that upgraded from v48.0. Users must add it to the DigitalWallet page layout on their
own.

Important: `ProcessingMode` is required to create a DigitalWallet entity.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the saved payment method record.

**Relationship Name**
SavedPaymentMethod

**Relationship Type**
Lookup


### Standard Objects DirectMessage

**Field** **Details**

**Refers To**
SavedPaymentMethod

```
Status

### DirectMessage

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines the state of the digital wallet as a payment source.

Possible values are:

**•** `Active` —Customers can make payments with the digital wallet.

**•** `Canceled` —The digital wallet can no longer be used for payments. This status can’t
be changed.

**•** `InActive` —The digital wallet can’t be used for payments until a user changes its
status to Active.

Represents a direct message conversation between multiple users in Chatter. This object is available in API version 38.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`, `update()`

Special Access Rules

You must have the Manage Chatter Messages and Direct Messages permission enabled to access the DirectMessage object.

Fields

**Field** **Details**

```
Name

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort, Update

**Description**
A default value that isn’t visible to users.


### Standard Objects Division

**Field** **Details**

```
 Subject

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Subject of the overall direct message conversation.

DirectMessage is an object used by Salesforce to control DirectMessage conversations. It represents a record of a direct message
conversation, but doesn’t include conversation data, such as posts or comments. It is most frequently used to moderate direct message
data in order to meet data compliance regulations.

### Division

A logical segment of your organization's data. For example, if your company is organized into different business units, you could create
a division for each business unit, such as “North America,” “Healthcare,” or “Consulting.” Available only if the organization has the Division
permission enabled.

Supported Calls

`create()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

### • Divisions must be enabled for your organization to access this object. To discover whether divisions have been enabled for an

organization, inspect the User or Group object for the `DefaultDivision` field—if it is present, then divisions have been enabled,
and this field (the field is named Division in objects other than User and Group) will be available in all relevant objects.

**•** Customer Portal users can’t access this object.

Fields

**Field** **Details**

```
IsActive

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Update

**Description**
Indicates whether the division is active ( `true` ) or not ( `false` ). Label is **Active** .


Standard Objects Division

**Field** **Details**

```
IsGlobalDivision

Name

SortOrder

```

Usage

**Type**
boolean

**Properties**
Defaulted on createFilter

**Description**
Indicates whether the division is your organization’s global default division ( `true` )
or not ( `false` ). Label is **Global Division** .

**Type**
string

**Properties**
Create, Filter, Update

**Description**
A descriptive name for the division. Limit: 80 characters.

**Type**
int

**Properties**
Create, Filter, Nillable, Update

**Description**
The order in which this division name appears in the Division picklist field when
creating or editing users in the Salesforce user interface.

The values available for that field are the global division ID for the organization, created when divisions are first enabled, and any other
division IDs that have been created. The division ID associated with a user is populated in the objects owned or created by the user.

You can use the division ID to make searches, reports, and list views run more quickly and return more relevant results if an organization
has very large data sets. For more information, see the Salesforce online help, in the Fields description for the object.

You can use WITH in SOSL to pre-filter results based on division. This is faster than specifying the division in a WHERE clause.

Note: The User object has a `Division` field that is unrelated to this object. The `Division` field is a standard text field similar
to Company or Department that has no special properties. Do not confuse it with the `DefaultDivision` field, which does
relate to this object.

SEE ALSO:

Overview of Salesforce Objects and Fields


### Standard Objects DivisionLocalization DivisionLocalization

When the Translation Workbench is enabled for your organization, the DivisionLocalization object provides the translation of the label
for a division.

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
Language

NamespacePrefix

```

**Type**
string

**Properties**
Create, Filter, Nillable, Restricted picklist

**Description**
The language for this translated label.

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

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix
of the org for all objects that support it, unless an object is in an installed managed
package. In that case, the object has the namespace prefix of the installed
managed package. This field’s value is the namespace prefix of the Developer
Edition org of the package developer.


### Standard Objects DocAtchDownloadEventLog

**Field** **Details**

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only
for objects that are part of an installed managed package. All other objects have
no namespace prefix.

```
 ParentId

 Value

```

Usage

**Type**
reference

**Properties**
Create, Filter, Nillable

**Description**
The ID of the Division associated with the label that is being translated.

**Type**
string

**Properties**
Create, Filter, Nillable, Update

**Description**
The actual translated label for the division. Label is **Translation** .

Use this object to translate the labels of your divisions into the different languages supported by Salesforce.

### DocAtchDownloadEventLog

Document Attachment Downloads events contain details of document and attachment downloads. This object is available in API version
65.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
FileType

```

**Type**
string


### Standard Objects Document

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of the file or attachment.

```
ObjectIdentifier

RequestIdentifier

Timestamp

UserIdentifier

### Document

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the object that’s associated with the document or attachment.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same REQUEST_ID..

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.

For example: `00530000009M943`

Represents a file that a user has uploaded. Unlike Attachment records, documents are not attached to a parent object.


Standard Objects Document

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

You must have the “Edit” permission on documents and the appropriate access to the Folder that contains a document in order to create
or update a document in that Folder.

Fields

**Field** **Details**

```
AuthorId

Body

BodyLength

ContentType

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the User who is responsible for the Document.

This is a relationship field.

**Relationship Name**
Author

**Relationship Type**
Lookup

**Refers To**
User

**Type**
base64

**Properties**
Create, Nillable, Update

**Description**
Required. Encoded file data. If specified, then do not specify a URL.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Size of the file (in bytes).

**Type**
string


Standard Objects Document

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Type of content. Label is **Mime Type** . Limit: 120 characters.

If the `Don't allow HTML uploads as attachments or document`
`records` security setting is enabled for your organization, you cannot upload files with
the following file extensions: `.htm`, `.html`, `.htt`, `.htx`, `.mhtm`, `.mhtml`, `.shtm`,
`.shtml`, `.acgi`, `.svg` .

```
Description

DeveloperName

FolderId

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Text description of the Document. Limit: 255 characters.

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
are reflected in a subscriber’s organization. Label is **Document Unique Name** .

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance may slow while
Salesforce generates one for each record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. ID of the Folder that contains the document.

This is a relationship field.

**Relationship Name**
Folder

**Relationship Type**
Lookup


Standard Objects Document

**Field** **Details**

**Refers To**
Folder, User

```
IsBodySearchable

IsDeleted

IsInternalUseOnly

IsPublic

Keywords

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the contents of the object can be searched using a SOSL `FIND` call. The
`ALL FIELDS` search group includes the content as a searchable field.

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
Indicates whether the object is only available for internal use ( `true` ) or not ( `false` ). Label
is **Internal Use Only** .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the object is available for external use ( `true` ) or not ( `false` ). Label is
**Externally Available** .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Keywords. Limit: 255 characters.


Standard Objects Document

**Field** **Details**

```
LastReferencedDate

LastViewedDate

Name

NamespacePrefix

```

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced ( `LastReferencedDate` ) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of the document. Label is **Document Name** .

**Type**
string

**Properties**
Filter, Group, Sort, Nillable

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

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.


### Standard Objects DocumentAttachmentMap

**Field** **Details**

```
 Type

 Url

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
File type of the Document. In general, the values match the file extension for the type of
Document (such as pdf or jpg). Label is **File Extension** .

**Type**
string

**Properties**
Create, Filter, Nillable, Group, Sort, Update

**Description**
URL reference to the file (instead of storing it in the database). If specified, do not specify the
`Body` or `BodyLength` .

When creating or updating a document, you can specify a value in either the `Body` or `Url` fields, but not both.

Encoded Data

The API sends and receives the binary file data encoded as a base64 data type. Prior to creating a record, clients must encode the binary
file data as base64. Upon receiving an API response, clients must decode the base64 data to binary (this conversion is usually handled
for you by the SOAP client).

Maximum Document Size

You can only create or update documents to a maximum size of 5 MB.

SEE ALSO:

Overview of Salesforce Objects and Fields

### DocumentAttachmentMap

Maps the relationship between an EmailTemplate and its attachment, which is stored as a Document.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


### Standard Objects DocumentRecipient

Special Access Rules

Customer Portal users can’t access this object.

Fields

**Field** **Details**

```
 DocumentId

 DocumentSequence

 ParentId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the document that this object tracks.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Represents the order that the attachments will be included in the email defined by the
EmailTemplate specified by the `DocumentId` . Label is **Attachment Sequence** . The first
attachment is given a value of 0, and each subsequent attachment is given a value
incremented by 1.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the EmailTemplate parent. The attachment identified by `DocumentId` is attached
to the EmailTemplate specified in this field.

Use this object to map the relationship of an EmailTemplate to its attachments, and to specify the order of the attachments.

SEE ALSO:

EmailTemplate

### DocumentRecipient

Connects a Service Report to a Digital Signature. This object is available in API version 55.0 and later.


Standard Objects DocumentRecipient

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
DigitalSignatureId

DigitalSignatureUrl

DocumentId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Digital Signature to be used on the Service Report.

This field is a relationship field.

**Relationship Name**
DigitalSignature

**Relationship Type**
Lookup

**Refers To**
DigitalSignature

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Link to request signature from Experience Cloud site.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The document sent to the recipient.

This field is a polymorphic relationship field.

**Relationship Name**
Document

**Relationship Type**
Lookup

**Refers To**
ServiceReport


Standard Objects DocumentRecipient

**Field** **Details**

```
DocumentRecipient

LastReferencedDate

LastViewedDate

OwnerId

```

QuoteDocumentId

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Number automatically assigned to a new record.

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
ID of the owner of this object. ID of the creator of this object.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference


Standard Objects DocumentRecipient

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The quote document sent to the recipient.

This field is a relationship field.

**Relationship Name**
QuoteDocument

**Refers To**
QuoteDocument

```
RecipientId

SignatureIdentifier

SignatureStatus

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The recipient to sign the document.

This field is a polymorphic relationship field.

**Relationship Name**
Recipient

**Relationship Type**
Lookup

**Refers To**
Contact, User

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A unique identifier that associates `DocumentRecipient` with a signature Lightning
web component (LWC) on the report page layout, telling you where on the report the
signature goes.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the signature. The default value is `Completed` . Possible values are:

**•** `Completed`

**•** `Skipped`


Standard Objects DocumentRecipient

**Field** **Details**

```
SignatureStatusReason

Status

StatusReason

```

Associated Objects

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
An explanation for the signature status. For example, a reason why the signature was skipped.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the document recipient record.

Possible values are:

**•** `Completed`

**•** `Declined`

**•** `Delivered`

**•** `None`

**•** `Sent`

The default value is `None` .

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The final status reason.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**DocumentRecipientFeed on page 55**
Feed tracking is available for the object.

**DocumentRecipientOwnerSharingRule on page 65**
Sharing rules are available for the object.

**DocumentRecipientShare on page 67**
Sharing is available for the object.


### Standard Objects DocumentTag DocumentTag

Associates a word or short phrase with a Document.

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


### Standard Objects Domain

**Field Name** **Details**

**•** `Personal` —The tag can be viewed or manipulated only by a user with a matching
`OwnerId` .

Usage

DocumentTag stores the relationship between its parent TagDefinition and the Document being tagged. Tag objects act as metadata,
allowing users to describe and organize their data.

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.

### Domain

Read-only object that represents a custom Web address assigned to a site in your organization. This object is available in API version
26.0 and later.

### To access this object, Salesforce Sites, Digital Experiences, or Site.com must be enabled for your organization. DomainSite contains

records for domains that serve your Experience Cloud sites only when enhanced domains are deployed. The system-managed site
hostnames for those Experience Cloud sites end in `.my.site.com` . This object doesn’t contain records for legacy domains that serve
Experience Cloud sites with hostnames that end in `.force.com` .

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

**•** Customer Portal users can’t access this object.

**•** To view this object, you must have either the View Setup and Configuration or Manage Custom Domains permission.

**•** Site.com Publisher users have read-only API access to the Domain and DomainSite objects.

Fields

**Field** **Description**

```
CnameTarget

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The canonical name (CNAME) of the external host or server. If you use a custom
domain with a non-Salesforce provider, such as your own external server or CDN
provider, to serve your domain, this field points to the CNAME of the external
provider. This field is available in API version 43.0 and later.


Standard Objects Domain

**Field** **Description**

```
Domain

DomainType

HttpsOption

```

**Type**
string

**Properties**
Filter, idLookup, Sort

**Description**
The branded custom Web address within the global namespace identified by
this domain's type. In the Domain Name System (DNS) global namespace, this
field is the custom Web address that you registered with a third-party domain
name registrar. The custom Web address can be used to access the site of this
domain.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The global namespace that this custom Web address belongs to. This value is
set to DNS for custom Web addresses in the global DNS.

DomainType can have the following value:

**•** `DNS` —Domain Name System (DNS)

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Current HTTPS option. Values include:

**•** `CdnPartner` —Salesforce serves the custom domain, such as
`https://www.example.com`, with the Salesforce Content Delivery
Network (CDN) partner.

**•** `Community` —The system-managed Experience Cloud sites domain that
ends in `.force.com` . This option applies only to orgs without enhanced
domains.

**•** `CommunityAlt` —The system-managed Experience Cloud sites domain
that ends in `.my.site.com` . This option applies only to orgs with
enhanced domains.

**•** `ExternalHttps` —An external service or CDN serves the custom domain,
such as `https://www.example.com` .

**•** `LegacyDomain` —A previous system-managed domain for this org. This
option is rarely used.


### Standard Objects DomainSite

**Field** **Description**

**•** `NoHttps` —Salesforce serves the custom domain, such as
`http://www.example.com`, via HTTP. Used to configure your custom
domain before selecting a permanent HTTPS option.

**•** `OrgDomain` —The system-managed My Domain login URL for this org.

**•** `Sites` —The system-managed Salesforce Sites domain that ends in
`.force.com` . This option applies only to orgs without enhanced domains.

**•** `SitesAlt` —The system-managed Salesforce Sites domain that ends in
`.my.salesforce-sites.com` . This option applies only to orgs with
enhanced domains.

**•** `SitesRuntime` —Salesforce serves the custom domain, such as
`https://www.example.com`, using your HTTPS certificate on Salesforce
servers.

This field is available in API version 47.0 and higher.

[To get the current system-managed domains for your org, use the Domain Apex](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_class_System_Domain.htm)
class.

```
OptionsHstsPreload

```

Usage

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the `preload` directive is added to the HSTS header so that
the domain is eligible for HSTS preloading registration ( `true` ) or not ( `false` ).
This field is available in API version 52.0 and later.

After this field is set to `true`, to ensure that HTTPS connections are always used
in browsers that support HSTS, you must also register the domain at
[https://hstspreload.org.](https://hstspreload.org)

We only modify the HSTS headers of domains that are eligible for registration.
Domain names can consist of a public suffix plus one additional label. For more
[information, see Add a Domain in Salesforce Help.](https://help.salesforce.com/articleView?id=platform.domain_mgmt.htm&type=5&language=en_US)

Use this read-only object to query the domains that are associated with each site in your organization.

### DomainSite

Read-only junction object that joins the Site and Domain objects. This object is available in API version 26.0 and later.

### To access this object, Salesforce Sites, Digital Experiences, or Site.com must be enabled. DomainSite contains records for domains

that serve your Experience Cloud sites only when enhanced domains are deployed. The system-managed site hostnames for those


Standard Objects DomainSite

Experience Cloud sites end in `.my.site.com` . This object doesn’t contain records for legacy domains that serve Experience Cloud
sites with hostnames that end in `.force.com` .

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

**•** Customer Portal users can’t access this object.

**•** To view this object, you must have either the View Setup and Configuration or Manage Custom Domains permission.

**•** Site.com Publisher users have read-only API access to the Domain and DomainSite objects.

Fields

**Field** **Description**

```
DomainId

PathPrefix

SiteId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

The ID of the associated Domain.

This is a relationship field.

**Relationship Name**
Domain

**Relationship Type**
Lookup

**Refers To**
Domain

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Shows where a site’s root exists on a domain. Can only be set for custom Web
addresses. Always begins with a `/` .

**Type**
reference

**Properties**
Filter, Group, Sort


### Standard Objects DsarPolicy

**Field** **Description**

**Description**

The ID of the associated Site.

This is a relationship field.

**Relationship Name**
Site

**Relationship Type**
Lookup

**Refers To**
Site

Usage

Use this read-only object to query or retrieve information about your sites.

### DsarPolicy

Represents a Data Subject Access Request (DSAR) policy created in the Privacy Center managed package. DSAR policies anonymize or
transfer personal data from your org at your customer’s request. This object is available in API version 50.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

This object is for Privacy Center customers with the ReadAllData or PrivacyDataAccess permissions.

Fields

**Field** **Details**

```
Description

DeveloperName

```

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
Description of the policy. The description is limited to 255 characters.

**Type**
string


Standard Objects DsarPolicy

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
Developer name of the policy.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

```
IsActive

Language

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this policy can be used ( `true` ) or not ( `false` ) for data subject (customer)
requests. The default value is `false` .

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the MasterLabel.

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


### Standard Objects DsarPolicyLog

**Field** **Details**

**•** `zh_TW` —Chinese (Traditional)

```
MasterLabel

```

Associated Objects

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Label of the policy.

This object has the following associated objects. Unless noted, they are available in the same API version as the object.

### **DsarPolicyLog**

Sharing is available for the object.

### DsarPolicyLog

Represents the history of Data Subject Access Request (DSAR) policy execution requests. This log records the status and results of executed
DSAR policies for a customer. This object is available in API version 50.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

This object is for Privacy Center customers with the ReadAllData or PrivacyDataAccess permissions.

Fields

**Field** **Details**

```
CompletionDateTime

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the data subject access request was completed. Available in API
version 51.0 and later.


Standard Objects DsarPolicyLog

**Field** **Details**

```
DataSubjectId

DeletedDateTime

DeveloperName

DownloadedDateTime

DsarError

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15–18 character ID of the data subject making the request. Available in API version 51.0
and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the file generated for the data subject’s request is deleted. Available
in API version 51.0 and later.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Developer name of the policy.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The most recent date and time when the data subject downloaded the file generated at
their request. Available in API version 51.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Represents an error in generating the file for the data subject access request. Available in
API version 51.0 and later.


Standard Objects DsarPolicyLog

**Field** **Details**

```
DsarPolicyId

FileURL

Language

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the DSAR policy.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The result of the DSAR policy execution. The URL links to a downloadable file that contains
the customer data.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language of the MasterLabel.

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


Standard Objects DsarPolicyLog

**Field** **Details**

**•** `zh_TW` —Chinese (Traditional)

```
MasterLabel

RequestDateTime

RequestStatus

RequestUserId

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Label of the policy.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when a data subject requested access to their data in the org. Available
in API version 51.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the policy execution.

Possible values are:

**•** `Complete`

**•** `Deleted`

**•** `Downloaded`

**•** `Expired`

**•** `Failed`

**•** `In Progress`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the org employee or admin making the request on behalf of the data subject.
Available in API version 51.0 and later.


### Standard Objects DuplicateJob

Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as the object.

**DsarPolicy**

Sharing is available for the object.

### DuplicateJob

Represents an instance of a job that identifies duplicates among existing records in the system.

This object is available in API versions 42.0 and later.

A duplicate job is the parent of the DuplicateRecordSet instances that it generates. The duplicate record items in a set generated by a
duplicate job are of one object type.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`

Special Access Rules

As of Summer ’20 and later, only users with the View Setup and Configuration permission can access this object.

Fields

**Field Name** **Details**

### `DuplicateJobDefinitionId` `DuplicateJobStatus`

```
EndDateTime

```

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
The ID of the corresponding duplicate job definition.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The current status of a duplicate job. Valid values are `Not Started`, `In`
`Progress`, `Completed`, `Canceled`, `Failed`, `Results Deleted` .

**Type**
dateTime


Standard Objects DuplicateJob

**Field Name** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when a duplicate job was completed.

```
LastReferencedDate

LastViewedDate

Name

NumDuplicateRecordItems

NumDuplicateRecordSets

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when a duplicate job was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when a duplicate job was last viewed.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort, Update

**Description**
The name of a duplicate job.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The total number of duplicate records identified as a result of invoking a duplicate
job.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of duplicate record sets identified as a result of invoking a duplicate
job.


### Standard Objects DuplicateJobDefinition

**Field Name** **Details**

```
NumRecordsScanned

ResultListViewId

StartDateTime

### DuplicateJobDefinition

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of records scanned as a result of invoking a duplicate job.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
List view metadata for displaying the duplicate record sets identified as result of
invoking a duplicate job.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date and time when a duplicate job was invoked.

Setup object defining a job that identifies duplicate record items globally.

This object is available in API versions 42.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

As of Summer ’20 and later, only users with the View Setup and Configuration permission can access this object.


Standard Objects DuplicateJobDefinition

Fields

**Field Name** **Details**

```
DeveloperName

Language

MasterLabel

SobjectSubtype

SobjectType

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The name of the user who created a duplicate job.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language in the user’s personal settings.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label of the duplicate job.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The object subtype. Valid values are `Person Account` or `None` .

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The object type: account, contact, or lead.


### Standard Objects DuplicateJobMatchingRule DuplicateJobMatchingRule

Represents a MatchingRule to be used with a DuplicateJob sharing the corresponding DuplicateJobMatchingRuleDefinition.

This object is available in API versions 42.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

As of Summer ’20 and later, only users with the View Setup and Configuration permission can access this object.

Fields

**Field Name** **Details**

```
DuplicateJobId

DuplicateJobMatchRuleDefId

MatchingRuleBooleanFilter

MatchingRuleDescription

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the corresponding DuplicateJob.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the matching rule defined for the corresponding
### DuplicateJobMatchingRuleDefinition.

**Type**
textarea

**Properties**
Filter, Sort

**Description**
Boolean logic of the MatchingRule for this DuplicateJobMatchingRule.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects DuplicateJobMatchingRuleDefinition

**Field Name** **Details**

**Description**
Description of the matching rule for this DuplicateJobMatchingRule.

```
MatchingRuleName

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The name of the matching rule defined for this particular DuplicateJob invocation.

### DuplicateJobMatchingRuleDefinition

Setup object specifying a MatchingRule to use with DuplicateJob instances that share a DuplicateJobDefinition.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

This object is available in API versions 42.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `search()`

Special Access Rules

As of Summer ’20 and later, only users with the View Setup and Configuration permission can access this object.

Fields

**Field Name** **Details**

```
DuplicateJobDefinitionId

MatchingRuleId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of DuplicateJobDefinition (master) for this DuplicateJobMatchingRuleDefinition
(detail).

**Type**
reference


### Standard Objects DuplicateRecordItem

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the MatchingRule to be used with this DuplicateJobMatchingRuleDefinition.

### DuplicateRecordItem

Represents a record that’s been identified as a duplicate. DuplicateRecordItems are included in a DuplicateRecordSet, which are processed
in duplicate jobs. Use this object to create custom report types for duplicates.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access this object, enable Duplicate Management. A Salesforce admin can grant access to any user with a Sales Cloud or CRM user
license.

Fields

**Field Name** **Details**

```
DuplicateRecordSetId

Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The duplicate record set that the duplicate record item is assigned to.

This is a relationship field.

**Relationship Name**
DuplicateRecordSet

**Relationship Type**
Lookup

**Refers To**
DuplicateRecordSet

**Type**
string


### Standard Objects DuplicateRecordSet

**Field Name** **Details**

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**

### The autogenerated name that’s given to the Duplicate Record Item. Label is Duplicate

`Record Item Name` .

```
RecordId

### DuplicateRecordSet

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The name of the record as it appears on the record’s detail page.

This is a polymorphic relationship field.

**Relationship Name**
Record

**Relationship Type**
Lookup

**Refers To**
Account, Contact, Individual, Lead

Represents a group of records that have been identified as duplicates. Each duplicate record set contains one or more duplicate record
items. Use this object to create custom report types and view the results of duplicate jobs.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access this object, activate duplicate rules. A Salesforce admin must give users read and write access.

Fields

**Field Name** **Details**

```
DuplicateRuleId

```

**Type**
reference


Standard Objects DuplicateRecordSet

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The duplicate rule used to identify this list of duplicate records.

**Label**

Duplicate Rule ID

This is a relationship field.

**Relationship Name**
DuplicateRule

**Relationship Type**
Lookup

**Refers To**
DuplicateRule

```
LastReferencedDate

LastViewedDate

Name

RecordCount

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The timestamp when the current user last accessed this record, a record related to this record, or a list
view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The timestamp when the current user last viewed this record or list view. If this value is null, the user
might have only accessed this record or list view ( `LastReferencedDate` ) but not viewed it.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**

The autogenerated name that’s given to the duplicate record set. Label is `Duplicate Record`
`Set Name` .

**Type**
int


### Standard Objects DuplicateRule

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**

The number of record items in the set.

```
ParentId

### DuplicateRule

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The `ParentId` represents the parent of a duplicate rule or duplicate job. A `ParentId` is polymorphic.
The label is Parent. This field is available in API versions 42.0 and later.

Represents a duplicate rule for detecting duplicate records.

Supported Calls

`describeSObjects()`, `describeLayout()`, `query()`, `retrieve()`, `search()`

Special Access Rules

As of Summer ’20 and later, only users with the View Setup and Configuration permission can access this object.

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
The developer name for the duplicate rule.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
boolean


Standard Objects DuplicateRule

**Field Name** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a duplicate rule is active ( `true` ) or not ( `false` ). This field is
read only.

```
Language

LastViewedDate

MasterLabel

NamespacePrefix

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language for the duplicate rule.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. This
field is available in API version 41.0 or later.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label for the duplicate rule.

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


### Standard Objects DynamicDataCapture

**Field Name** **Details**

installed managed package. This field’s value is the namespace prefix of the
Developer Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set
only for objects that are part of an installed managed package. All other
objects have no namespace prefix.

```
SobjectSubtype

sObjectType

```

Usage

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The subtype of object the duplicate rule is defined for. This field is available in
API version 39.0 or later.

Possible values are:

**•** `None`

**•** `PersonAccount`

The default value is `None` .

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of object the duplicate rule is defined for.

Possible values are:

**•** `Account`

**•** `Contact`

**•** `Individual`

**•** `Lead`

You can use the API to view a duplicate rule’s details. To create, edit, or delete duplicate rules, use the UI.

Use DuplicateRule to get the sObject type.

DuplicateRule is unavailable in some orgs.

### DynamicDataCapture DynamicDataCapture is a junction object that adds a Form tab to Work Order Overview, and to the related list of a work order, work

order line item, or service appointment in the Field Service mobile app. This object is available in API version 62.0 and later.


Standard Objects DynamicDataCapture

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ActionDefinition

ActionType

Description

ExecutionOrder

IsRequired

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The associated Data Capture Flow to execute.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of platform action that the form is associated with. Possible values are:

Possible values are:

**•** `Flow`

The default value is `Flow` .

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the form.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order in which the Data Capture flow is executed. Positive integer values or null are
supported.

**Type**
boolean


Standard Objects DynamicDataCapture

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Boolean value that specifies if this form needs to be completed before moving on to the
next form.

```
LastReferencedDate

Name

OwnerId

ParentRecordId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The order in which the Data Capture flow is executed. Positive integer values or null are
supported.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the form.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID that refers to user who owns the Dynamic Data Capture object.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
ServiceAppointment, WorkOrder, WorkOrderLineItem (the parent object), Timesheet

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID that refers to a work order, work order line item, or service appointment that serves
as the parent record for junction object.

This field is a polymorphic relationship field.


Standard Objects DynamicDataCapture

**Field** **Details**

**Relationship Name**
ParentRecord

**Relationship Type**
Parent-child

**Refers To**
ServiceAppointment, WorkOrder, WorkOrderLineItem (the parent object)

```
ParentRecordType

PausedFlowInterviewId

ProcessType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of parent object associated with the junction object.

Possible values are:

**•** `Work Order`

**•** `Work Order Line Item`

**•** `Service Appointment`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the flow interview that has been paused by a user.

This field is a relationship field.

**Relationship Name**
PausedFlowInterview

**Refers To**
FlowInterview

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The flow process type for the form.

Possible values are:

**•** `DataCaptureFlow` —Data Capture Flow

The default value is `DataCaptureFlow` .


Standard Objects DynamicDataCapture

**Field** **Details**

```
ServiceDocumentTemplate

ServiceReportLanguage

StatusCategory

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The category that each status value belongs to.

Possible values are:

**•** `Completed`

**•** `InProgress` —In Progress

**•** `New`

**•** `NotApplicable` —Not Applicable

**•** `Paused`

The default value is `New` .

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**DynamicDataCaptureChangeEvent on page 68(API Version 64.0)**
Change events are available for the object.

**DynamicDataCaptureOwnerSharingRule on page 65(API Version 64.0)**
Sharing rules are available for the object.

**DynamicDataCaptureShare on page 67(API Version 64.0)**
Sharing is available for the object.


### Standard Objects ElectronicMediaGroup ElectronicMediaGroup

Represents the type of media that you can associate with a product or category.This object is available in API version 49.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

You must have the B2B Commerce license and a CMS workspace to access a web store.

Fields

**Field** **Details**

```
CurrencyIsoCode

Description

DeveloperName

LastReferencedDate

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**

The default value is `USD` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Description of the store.

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

**Type**
dateTime


Standard Objects ElectronicMediaGroup

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

```
LastViewedDate

Name

OwnerId

UsageType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced ( `LastReferencedDate` ) and not viewed.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Name of the media group.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the owner of the ElectronicMediaGroup object. For external routing, allows the
object to be used in the Streaming API to listen to events whenever a ElectronicMediaGroup
record is created, modified, or deleted.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Possible values are:

**•** `Attachment`

**•** `Banner`

**•** `Listing`

**•** `Standard`

**•** `Tile`


### Standard Objects ElectronicMediaUse ElectronicMediaUse

Represents the usage of media. This object is available in API version 49.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

You must have the B2B Commerce license and a CMS workspace to access a web store.

Fields

**Field** **Details**

```
CurrencyIsoCode

ElectronicMediaGroupId

ElectronicMediaId

ImplementorType

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**

The default value is `USD` . Possible values are:

**•** `USD` —U.S. Dollar

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the electronic media group.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the electronic media.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects EmailContent

**Field** **Details**

**Description**
The type of implementor. Available implementors of ElectronicMediaUse include:

**•** ProductMedia

**•** ProductCategoryMedia

```
SortOrder

### EmailContent

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The order that electronic media is displayed in.

Represents a marketing email asset for use with Account Engagement. This object is available in API version 50.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Special Access Rules

### EmailContent is only available for orgs that use Account Engagement. The Manage Email Content user permission is required. Users also

need the CRM User, Sales, or Service User permission set. EmailContent isn’t available for custom portal or guest users.

Fields

**Field** **Details**

```
ClickThroughRate

ClickToOpenRatio

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of visitors who click links contained in emails delivered (sent minus bounces)
to them. Multiple clicks for a same link are counted.

**Type**
percent


Standard Objects EmailContent

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The number of unique clicks divided by unique HTML opens.

```
DeliveryRate

Description

HtmlBody

LastReferencedDate

LastViewedDate

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of the emails that were delivered compared to the number that bounced
(soft and hard). Note: this data includes emails that were delivered to the recipient's spam
folder.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the email content, for example, Promotion Mass Mailing.

**Type**
textarea

**Properties**
Nillable

**Description**
The body of the email in HTML format. The field is read-only.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp that indicates when the current user last viewed the record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, the
record could have been referenced (LastReferencedDate) and not viewed.


Standard Objects EmailContent

**Field** **Details**

```
Name

OpenRate

OptOutRate

SpamComplaintRate

Subject

TemplateId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the email asset.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of unique HTML opens compared to the total number of emails delivered
(sent minus bounces).

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of users that have opted out compared to the total number of emails sent.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of spam complaints compared to the total number emails sent.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Update

**Description**
Content of the subject line.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort


Standard Objects EmailContent

**Field** **Details**

**Description**
The Email Template field is mostly read-only. You can populate the Email Template field only
during record create to prevent overwriting data on the email content record.

```
TextBody

TotalDelivered

TotalHardBounced

TotalOpens

TotalSent

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The body of the email in plain text format. The character limit is 384, 000.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of emails minus hard and soft bounces. Note: this data includes emails
that were delivered to the recipient's spam folder.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The total number of emails that permanently returned to the sender because the address is
invalid. A hard bounce can occur because the domain name doesn't exist or because the
recipient is unknown.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The total number of times a prospect’s email client loaded the images in the HTML version
of the email. We also record an open if the prospect clicks a link within the HTML or text
email without downloading images. A click indicates that they viewed the message. Some
email clients (Outlook, Apple Mail, Thunderbird) do not display images by default. Account
Engagement counts an open each time the images load.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort


Standard Objects EmailContent

**Field** **Details**

**Description**
Read-only field. The total number of list emails sent, including bounced, opted-out, and
invalid To: addresses.

```
TotalSoftBounced

TotalSpamComplaints

TotalTrackedLinkClicks

UniqueClickThroughRate

UniqueOpens

```

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Read-only field. The total number of times a recipient’s mail server acknowledged the email,
but returned it to the sender. Sometimes it is because the recipient's mailbox is full or the
mail server is temporarily unavailable. After 5 soft bounces, Account Engagement opts the
prospect out of emails.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Read-only field. The total number of prospects that reported the email as spam.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Read-only field. The number of times prospects clicked a link in the email.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
Read-only field. The percentage of visitors who clicked a link contained in an email

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort


### Standard Objects EmailDomainFilter

**Field** **Details**

**Description**
Read-only field. The number of prospects who loaded the images in the HTML version of
the email. The Unique Opens category counts each recipient only one time, even if the
prospect loaded images more than once.

```
UniqueOptOuts

UniqueTrackedLinkClicks

### EmailDomainFilter

```

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Read-only field. The total number of prospects that have clicked the link to unsubscribe or
opted out of all emails in the Email Preference Center. They are removed from future email
sends.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Read-only field. The number of times a prospect clicked a link in the email. This metric doesn’t
include multiple clicks of the same link.

Represents a filter that determines whether an email relay is restricted to a specific list of domains. This object is available in API version
43.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

You must have the “Email Administration,” “Customize Application,” and “View Setup” user permissions to use this object.

### You must create an email relay in Setup or through the EmailRelay object before you can use the EmailDomainFilter object.


Standard Objects EmailDomainFilter

Fields

**Field Name** **Details**

```
EmailRelayId

FromDomain

IsActive

PriorityNumber

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The ID of the EmailRelay record.

This is a relationship field.

**Relationship Name**
EmailRelay

**Relationship Type**
Lookup

**Refers To**
EmailRelay

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

Restricts the email relay to send emails based on the sender domains
( `FromDomain` ) listed in this field. This field is optional, accepts a list of
comma-separated values, and supports the wildcard character.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether the email domain filter is active ( `true` ) or not ( `false` ). Use
this field to enable or disable the email domain filter.

**Type**
int

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**

Indicates the order in which the email domain filter is processed. Filters are
evaluated in ascending order. The priority number must be unique. If this field


### Standard Objects EmailDomainKey

**Field Name** **Details**

is left blank, it is assigned the next available number and is processed last.
Processing stops after the first matching filter is applied.

```
ToDomain

```

Usage

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

Restricts the email relay to send emails based on the recipient domains
( `ToDomain` ) listed in this field. This field is optional, accepts a list of
comma-separated values, and supports the wildcard character.

Tip: If you also plan to activate Bounce Management and Email Compliance Management, confirm with your email admin that
[your company allows relaying email sent from Salesforce. For more information on bounce management, see Configure Deliverability](https://help.salesforce.com/articleView?id=emailadmin_send_through_salesforce_configure_deliverability.htm&language=en_US)
[Settings for Emails Sent from Salesforce.](https://help.salesforce.com/articleView?id=emailadmin_send_through_salesforce_configure_deliverability.htm&language=en_US)

### EmailDomainKey

Represents a domain key for an organization’s domain, used to authenticate outbound email that Salesforce sends on the organization’s
behalf. This object is available in API version 28.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Summer ’20 and later, only authenticated internal and external users can access this object.

We’ve upgraded and replaced the original DKIM (DomainKeys Identified Mail) key feature, so that you can create a DKIM key with
[increased email security. For more information, see Setting Up More Secure DKIM Keys.](https://help.salesforce.com/articleView?id=emailadmin_setup_dkim_key.htm&type=0&language=en_US)

Fields

**Field Name** **Details**

```
AlternatePublicKey

```

**Type**
textarea

**Properties**
Nillable


Standard Objects EmailDomainKey

**Field Name** **Details**

**Description**

Read-only. Alternate public keys are used by Salesforce to auto-rotate domain
keys. This field is available in API version 44.0 and later after activating the Critical
Update.

```
AlternateSelector

AlternateTxtRecordName

Domain

DomainMatch

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The text used to distinguish the DKIM key from any other DKIM keys your
organization uses for the specified domain. This field is available in API version
44.0 and later after activating the Critical Update.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The alternate TXT record name is used to create the CNAME record. Refer to the
Usage section for more information. This field is available in API version 44.0 and
later after activating the Critical Update.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The organization’s domain name that the DKIM key is generated for.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The specificity of match required on the sending domain name before signing
with this DKIM key. Valid values are:

**•** `DomainOnly` —Sign if sending domain matches at the domain level only
(example.com but not mail.example.com)

**•** `SubdomainsOnly` —Sign if sending domain matches at the subdomain
level only (mail.example.com but not example.com)


Standard Objects EmailDomainKey

**Field Name** **Details**

**•** `DomainAndSubdomains` —Sign if sending domain matches at the
domain and subdomain levels (example.com and mail.example.com)

```
IsActive

KeySize

PrivateKey

PublicKey

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether this DKIM key is active ( `true` ) or not ( `false` ).

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort

**Description**

Indicates the RSA key size, in bits. The possible values are:

**•** 1024

**•** 2048

This field is available in API version 45.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

Once you activate the Critical Update, this field is no longer visible.

The private portion of the DKIM key pair used to encrypt mail headers from your
domain. Salesforce generates an encrypted `PrivateKey` if you don’t specify
a value when creating the DKIM key. If you do specify a value, it must be an
existing valid `PrivateKey` from another EmailDomainKey object.

This field doesn’t contain the actual private key, but a value that represents the
key in our system. Therefore:

**•** The actual private key can’t be leaked.

**•** You can’t use the value to do your own email signing.

**Type**
textarea

**Properties**
Create, Nillable, Update


Standard Objects EmailDomainKey

**Field Name** **Details**

**Description**

Part of the domain key pair that mail recipients retrieve to decrypt the DKIM
header and verify your domain. Add the `PublicKey` value to your domain’s
DNS records before you start signing with this domain key.

```
Selector

TxtRecordName

TxtRecordsPublishState

```

Usage

**Create DKIM Keys with Increased Security**

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

Text used to distinguish the DKIM key from any other DKIM keys your organization
uses for the specified domain.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Read-only. The TXT record name is used to create the CNAME record. Refer to
the Usage section for more information. This field is available in API version 44.0
and later after activating the Critical Update.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The possible values are:

**•** Published

**•** Publishing in progress

**•** Publishing failed

This field is available in API version 44.0 and later after activating the Critical
Update.

**1.** If your Salesforce org was created before Winter ’19, enable the Critical Update. From Setup, enter _`Critical Updates`_ in the
Quick Find box, and then select **Critical Updates** . For Enable Redesigned DomainKeys Identified Mail (DKIM) Key Feature with
Increased Email Security, click **Activate** .


### Standard Objects EmailInsight

**2.** Insert `Domain`, `DomainMatch`, `Selector`, and `AlternateSelector` . Salesforce publishes your TXT record to DNS.

**3.** Retrieve the `TxtRecordName` and `AlternateTxtRecordName` and use them to create and publish the CNAME and
Alternate CNAME record to your domain’s DNS.

**a.** Create CNAME record using: _**`<selector>`**_ `._domainkey.` _**`<domain>`**_ `IN CNAME` _**`txtRecordName`**_ .

**b.** Create Alternate CNAME record using: _**`<alternateSelector>`**_ `._domainkey.` _**`<domain>`**_ `IN CNAME`
_**`alternateTxtRecordName`**_ .

**4.** Set the `IsActive` field to true.

**Create DKIM Keys (pre-Winter ‘19 Version)**

Note: The critical update activates for everyone on October 15, 2019. After that date, this approach to creating DKIM keys will no
longer be available.

When you create a DKIM key, Salesforce generates a public and private key pair. Publish the public key in the DNS.

For each domain key you create, we recommend this sequence:

**1.** Insert the `Domain`, `DomainMatch`, and `Selector` .

**2.** Update your domain’s DNS records.

**a.** Locate the DNS record at _**`selector`**_ `._domainkey.` _**`domain`**_ . For example, `mail._domainkey.mail.example.com` .

**b.** Add the `PublicKey` value, like this: `V=DKIM1; p=` _**`public_key`**_ .

DKIM Signing Outbound Email

**a.** In addition, you can optionally put the record in testing mode, which instructs recipients to not make decisions based on the
email signature. Add parameter `t=y` to the DNS entry: `V=DKIM1; t=y; p=` _**`public_key`**_ .

**3.** Update the key via the API or UI to be active.

SEE ALSO:

_Salesforce Help_ [: Considerations for Creating DKIM Keys](https://help.salesforce.com/articleView?id=emailadmin_considerations_dkim.htm&type=0&language=en_US)

_Salesforce Help_ [: Setting Up More Secure DKIM Keys](https://help.salesforce.com/articleView?id=emailadmin_setup_dkim_key.htm&type=0&language=en_US)

### EmailInsight

Represents an insight generated from an email interaction. EmailInsights acts as a central place to store various types of insights related
to email messages. The insights stored include status, type, and time of generation. Only certain types of insights can be created based
on a pre-configured list of insight types. This object is available in API version 63.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

EmailStream and SiqC2CProvisioned permissions must be enabled.

EmailStreamPref, SiqOrgProvisioned, and SyncEmailToCoreActivity Org prefs must be enabled.


Standard Objects EmailInsight

To be able to see SyncEmailToCoreActivity pref, EACLegacyEmailSyncAWS Org perm, AnalyticsActivity, UnifiedActivities, and ActivityMetrics
must be disabled. In addition, license to Standard Einstein Activity Capture and turning on Einstein Activity Capture and EmailInsights
provisions the required permissions and prefs.

Fields

**Field** **Details**

```
EmailMessageId

GeneratedDate

InsightTypeDescription

InsightTypeIdentifier

InsightTypeLabel

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Required. The ID of the email message the insight is generated for.

This field is a relationship field.

**Relationship Name**
EmailMessage

**Refers To**
EmailMessage

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
Required. The date and time when the insight was generated in the legacy system.

**Type**
textarea

**Properties**
None

**Description**
Required. Description of the insight type.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Required. The ID of the insight type based on which the insight is generated.

**Type**
string


Standard Objects EmailInsight

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
Required. The display name of the insight type.

```
IsLocked

LegacyInsightIdentifier

MayEdit

RowVersion

Status

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the email insight record is locked or not.

The default value is false.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Required. The unique ID of the insight that was generated and stored in the legacy system.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the email insight record can be edited or not.

The default value is false.

**Type**
string

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
A system-generated, read-only field that tracks the version of a record. Each time a record
is created or updated, the RowVersion value increments, providing a mechanism to detect
changes and manage concurrency.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort


### Standard Objects EmailInsightAction

**Field** **Details**

**Description**
Required. The status of the insight record.

Possible values are:

**•** `Active`

**•** `Completed`

**•** `Deprecated`

**•** `Dismissed`

The default value is `Active` .

### EmailInsightAction

Represents the actions that have been taken, or could be taken, in relation to email insights. It logs different types of actions and associated
metadata, helping to track and manage the activities and decisions made based on email insights. This object is available in API version
63.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

EmailStream and SiqC2CProvisioned permissions must be enabled.

EmailStreamPref, SiqOrgProvisioned, and SyncEmailToCoreActivity Org prefs must be enabled.

To be able to see SyncEmailToCoreActivity pref, EACLegacyEmailSyncAWS Org perm, AnalyticsActivity, UnifiedActivities, and ActivityMetrics
must be disabled. In addition, license to Standard Einstein Activity Capture and turning on Einstein Activity Capture and EmailInsights
provisions the required permissions and prefs.

Fields

**Field** **Details**

```
ActionMetadata

EmailInsightId

```

**Type**
textarea

**Properties**
Nillable

**Description**
The metadata for the action.

**Type**
reference


Standard Objects EmailInsightAction

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
Required. The ID of the email insight where the action is applied.

This field is a relationship field.

**Relationship Name**
EmailInsight

**Refers To**
EmailInsight

```
InsightAction

IsLocked

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Required. The action that's taken on the email insight.

Possible values are:

**•** `CreateCalendarEvent`

**•** `CreateTaskWithDate`

**•** `EciCreateEmail`

**•** `EciScheduleMeetings`

**•** `EciSendEmail`

**•** `EmailReply`

**•** `EmailReplyLater`

**•** `EmailReplyWithTemplate`

**•** `InsertFreeTime`

**•** `PostOnChatter`

**•** `ViewCalendar`

**•** `ViewContactProfile`

The default value is `EmailReply` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the email insight action record is locked or not.

The default value is false.


### Standard Objects EmailMessage

**Field** **Details**

```
MayEdit

RowVersion

### EmailMessage

```

Represents an email in Salesforce.

Supported Calls

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the email insight action record can be edited or not.

The default value is false.

**Type**
string

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
A system-generated, read-only field that tracks the version of a record. Each time a record
is created or updated, the RowVersion value increments, providing a mechanism to detect
changes and manage concurrency.

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

### EmailMessage is only available for orgs that use Email-to-Case or Enhanced Email, which is automatically enabled for most customers.

To use reply and forward functionality, `FromAddress` must specify an email address that exists in EmailMessageRelation, with a
`RelationType` of `FromAddress` .

The `Status` field is mostly read-only. You can change the status only from _`New`_ to _`Read`_ .

The `HtmlBody` and `RelatedToId` fields are supported in Classic list views but not in Lightning list views. In related lists and search
results in Lightning Experience, these fields either don’t appear, show blank values, or result in an error.

`update()` is supported when an email record is in `Draft` status, and `IsPrivateDraft` is `false` . It’s also supported if the
email status is `Draft`, `IsPrivateDraft` is `true,` and `CreatedBy` is associated with the current user. When the email record
isn’t in `Draft` status, the `IsExternallyVisible` field and custom fields only can be updated.

Set the Update Email Messages user permission for users, such as an Automated Case User, who run automated processes that modify
email message-related records. With the Update Email Message permission set, users’ processes can modify EmailMessageRelation and
ContentDocumentLink records that are related to an email message that isn’t in Draft status. Don’t set this user permission for other
users.


Standard Objects EmailMessage

Access to an email message depends on the associated object. The user who created the email is specified in `CreatedById` and
always has access, unless that user is a guest user. Guest users have read access if the message is marked as `IsExternallyVisible` .

The object that’s used to determine access differs for Email-to-Case and Enhanced Email.

**•** Email-to-Case—When Email-to-Case is enabled and the email is Case-based (the `ParentId` field is Case), access depends on the
user’s access to the related Case record. If the email message is a draft, only the user in the `CreatedById` field or users with the
Modify All Data permission can access it.

**•** Enhanced Email—Access is activity-based. The `ActivityId` field specifies an associated Task record. You can control access to
[activity-based objects with the Access Activities permission. Users with the Modify All Data permission can also access the message.](https://help.salesforce.com/s/articleView?id=sales.activity_access_user_perm.htm&type=5&language=en_US)

When you use the API to insert EmailMessage records in bulk, the same access rules apply: access is based on cases in `ParentId`
fields or by tasks in `ActivityId` fields. When inserting a single record, set the `CreatedById` field to the user performing the
operation or leave it blank.

Fields

**Field** **Details**

```
ActivityId

AttachmentIds

AutomationType

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the activity that is associated with the email. Usually represents an open task
that is created for the case owner when a new unread email message is received.
`ActivityId` can only be specified for emails on cases. It’s auto-created for other
entities.

If an EmailMessage has a related task, and fields on the email record are updated, we
may delete the related task and create a new related task.

**Type**
string

**Properties**
Create, Nillable, Update

**Description**
A comma-separated list of email attachments. This is used by the Send Email quick
action when you use Salesforce Classic email templates. Maximum length is 32, 768
characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
A picklist value that determines if an outgoing email was manually created or
AI-generated.


Standard Objects EmailMessage

**Field** **Details**

Possible values are:

**•** `AiAssisted` –Email is AI-generated, but sent by human.

**•** `AiAutomated` –Email is generated and sent by AI.

**•** `Null` –Email is created and sent by human.

```
BccAddress

BccIds

CcAddress

```

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A string array of email addresses for recipients who were sent a visually impaired
carbon copy of the email message. Include only email addresses that aren’t associated
with Contact, Lead, or User records in Salesforce. If the recipient is a contact, lead, or
user, add their ID to the `BccIds` field instead of adding their email address to the
`BccAddress` field. When adding their ID, the email message is automatically
associated with the contact, lead, or user. For an Experience Cloud site user who isn’t
the sender of the email, this field returns null.

You can’t send emails unless there’s at least one recipient.

**Type**
JunctionIdList

**Properties**
Create, Update

**Description**
A string array of IDs for contacts, leads, and users who were sent a visually impaired
carbon copy of the email message. Each ID is linked to an
`EmailMessageRelation` record, which represents the relationship between
an email message and a Contact, Lead, or User record. For an Experience Cloud site
user who isn’t the sender of the email, this list is empty.

Adding a `JunctionIdList` field name to the `fieldsToNull` property deletes
all related junction records. This action can’t be undone.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A string array of email addresses for recipients who were sent a carbon copy of the
email message. Include only email addresses that aren’t associated with Contact,
Lead, or User records in Salesforce. If the recipient is a contact, lead, or user, add their
ID to the `CcIds` field instead of adding their email address to the `CcAddress`
field. Then the email message is automatically associated with the contact, lead, or
user.


Standard Objects EmailMessage

**Field** **Details**

You can’t send emails unless there’s at least one recipient.

```
CcIds

ClientThreadIdentifier

ContentDocumentIds

Division

```

**Type**
JunctionIdList

**Properties**
Create, Update

**Description**
A string array of IDs for contacts, leads, and users who were sent a carbon copy of the
email message. Each ID is linked to an `EmailMessageRelation` record, which
represents the relationship between an email message and a Contact, Lead, or User
record.

Adding a `JunctionIdList` field name to the `fieldsToNull` property deletes
all related junction records. This action can’t be undone.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A value used by third-party email clients to identify which thread an email belongs
[to. See Email-to-Case Threading for more information.](https://help.salesforce.com/s/articleView?id=service.support_email_to_case_threading.htm&type=5&language=en_US)

Available in API versions 56.0 and later.

**Type**
JunctionIdList

**Properties**
Create, Update

**Description**
A string array of IDs for content documents such as files and attachments that are
associated with an email. Each ID is linked to a `ContentDocumentLink` record,
which represents the relationship between an email message and a content document
record.

Adding a `JunctionIdList` field name to the `fieldsToNull` property deletes
all related junction records. This action can’t be undone.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
A logical segment of your organization's data. For example, if your company is
organized into different business units, you could create a division for each business


Standard Objects EmailMessage

**Field** **Details**

unit, such as “North America,” “Healthcare,” or “Consulting.” Available only if the
organization has the Division permission enabled.

```
EmailRoutingAddressId

EmailTemplateId

FirstOpenedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Stores the ID of the email routing address used to create the email. This value is set
when the email is processed by Email-to-Case service. When this field is set,
EmailMessage.Incoming cannot be `false` .

**Relationship Name**
EmailRoutingAddress

**Relationship Type**
Lookup

**Refers To**
EmailRoutingAddress

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The email template, if any, that was chosen for the email. This field is populated in
Lightning Experience only.

This is a relationship field.

**Relationship Name**
EmailTemplate

**Relationship Type**
Lookup

**Refers To**
EmailTemplate

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date the email was first opened.

To see this field, enable email tracking in your org.


Standard Objects EmailMessage

**Field** **Details**

```
FromAddress

FromId

FromName

HasAttachment

Headers

```

**Type**
email

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The address that originated the email. When using this field, specify an email address
that exists in EmailMessageRelation, with a `RelationType` of `FromAddress` .

EmailMessages in Draft status with `IsPrivateDraft` set to `true` must use
the user's address, a verified org-wide email address, or a verified Email-to-Case routing
address in the `FromAddress` field.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The contact, lead, or user who sent the email. Maximum length is 18 characters.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The sender’s name. When using this field, specify an email address that exists in
EmailMessageRelation, with a `RelationType` of `FromAddress` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the email was sent with an attachment ( `true` ) or not ( `false` ).

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The Internet message headers of the incoming email. Used for debugging and tracing
purposes. Doesn’t apply to outgoing emails.


Standard Objects EmailMessage

**Field** **Details**

```
HtmlBody

Incoming

IsBounced

IsClientManaged

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The body of the email in HTML format.

You can’t send emails unless at least one of these fields has content.

**•** Subject field

**•** HTML Body or Text Body field

As the sender, you can provide the content, or it can be automatically inserted using
predefined values. An email template can also include the content for these fields.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the email was received ( `true` ) or sent ( `false` ).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the email bounced.

This field is set to True for bounced emails in orgs using Lightning Threading. It’s not
set to True for orgs using Ref ID threading.

To see this field, enable bounce management in your org.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
If EmailMessage is created with `IsClientManaged` set to `true`, users can modify
`EmailMessage.ContentDocumentIds` to link file attachments even when
the `Status` of the EmailMessage isn’t set to `Draft` . When this field is set to `true`
and Enhanced Email is enabled, a Task record is created for the EmailMessage
regardless of Email-to-Case settings.


Standard Objects EmailMessage

**Field** **Details**

```
IsDeleted

IsExternallyVisible

IsOpened

IsPrivateDraft

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not
( `false` ). Label is **Deleted** .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If the Experience Cloud site case feed is enabled, `IsExternallyVisible`
controls the external visibility of emails in sites. When `IsExternallyVisible`
is set to `true` —its default value—external users see the email message in the case
feed.

**•** Emails remain visible in the Emails related list whether or not this field is set to
true. For security reasons, we recommend that you remove this related list from
your case page layout for external community users.

**•** Only emails with a value in the `ParentId` field can be made externally visible
in sites.

**•** This field can’t be updated if the email’s `Status` is set to `Draft` .

**•** The `Enable Case Feeds in Experience Cloud Sites`
organization preference in Setup makes case-related emails, comments, and
updates visible to site members.

When this preference is off, `IsExternallyVisible` is True by default for
the EmailMessage. When this preference is on, `IsExternallyVisible`
defaults to True only if the case contact email is the sender or the recipient of the
`EmailMessage.` Otherwise, `IsExternallyVisible` defaults to False.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the email has been opened.

To see this field, enable email tracking in your org.

**Type**
boolean


Standard Objects EmailMessage

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
If `IsPrivateDraft` is set to `true`, then only the `CreatedById` user can
view, update, and send this email draft. If `IsPrivateDraft` is set to `false`,
then any user with permissions to work on the case can see these drafts. After the
email is sent, then this field is updated to be `false` . Public drafts are loaded and
visible in Salesforce Classic while Private Drafts are only used in Lightning Experience.

```
IsTracked

LastOpenedDate

MessageDate

MessageIdentifier

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the email is being tracked.

To see this field, enable email tracking in your org.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date the email was last opened.

To see this field, enable email tracking in your org.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date the email was created.

For inbound emails, Email-to-Case sets this field using the Date header. The Date
header is set by the email client and is subject to the sender's time preferences.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The ID of the email message.


Standard Objects EmailMessage

**Field** **Details**

```
Name

ParentId

RelatedToId

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
A name for the email message that's derived from the first 255 characters of the
Subject field. If the Subject field is empty, a localized string of `[No Subject]` is
used. This field is read-only and can’t be created or updated. Available in API versions
56.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the case that’s associated with the email.

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
Create, Filter, Group, Nillable, Sort, Update

**Description**

The `RelatedToId` represents nonhuman objects such as accounts, opportunities,
campaigns, cases, or custom objects. RelatedToIds are polymorphic. Polymorphic
means a RelatedToId is equivalent to the ID of a related object.

You must have access to at least one entity listed under Refers To to access RelatedToId.

You can update `RelatedToId` when `IsClientManaged` is set to `true` .

`RelatedtoId` and `ParentId` should have the same value when `ParentId`
is set. You might see unexpected results otherwise.

This is a polymorphic relationship field.

**Relationship Name**
RelatedTo


Standard Objects EmailMessage

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, AssessmentIndicatorDefinition, AssessmentTask,
AssessmentTaskContentDocument, AssessmentTaskDefinition, AssessmentTaskOrder,
Asset, AssetRelationship, AssignedResource, Award, BoardCertification, BusinessLicense,
BusinessMilestone, BusinessProfile, Campaign, CareBarrier, CareBarrierDeterminant,
CareBarrierType, CareDeterminant, CareDeterminantType, CareDiagnosis,
CareInterventionType, CareMetricTarget, CareObservation,
CareObservationComponent, CarePgmProvHealthcareProvider, CarePreauth,
CarePreauthItem, CareProgram, CareProgramCampaign, CareProgramEligibilityRule,
CareProgramEnrollee, CareProgramEnrolleeProduct, CareProgramEnrollmentCard,
CareProgramGoal, CareProgramProduct, CareProgramProvider,
CareProgramTeamMember, CareProviderAdverseAction, CareProviderFacilitySpecialty,
CareProviderSearchableField, CareRegisteredDevice, CareRequest, CareRequestDrug,
CareRequestExtension, CareRequestItem, CareSpecialty, CareSpecialtyTaxonomy,
CareTaxonomy, Case, CommSubscriptionConsent, ContactEncounter,
ContactEncounterParticipant, ContactRequest, Contract, CoverageBenefit,
CoverageBenefitItem, CreditMemo, DelegatedAccount, DocumentChecklistItem,
EnrollmentEligibilityCriteria, HealthcareFacility, HealthcareFacilityNetwork,
HealthcarePayerNetwork, HealthcarePractitionerFacility, HealthcareProvider,
HealthcareProviderNpi, HealthcareProviderSpecialty, HealthcareProviderTaxonomy,
IdentityDocument, Image, IndividualApplication, Invoice, ListEmail, Location,
MemberPlan, Opportunity, Order, OtherComponentTask, PartyConsent,
PersonLifeEvent, PlanBenefit, PlanBenefitItem, ProcessException, Product2,
ProductItem, ProductRequest, ProductRequestLineItem, ProductTransfer,
PurchaserPlan, ReceivedDocument, ResourceAbsence, ReturnOrder,
ReturnOrderLineItem, ServiceAppointment, ServiceResource, Shift, Shipment,
ShipmentItem, Solution, Visit, VisitedParty, VolunteerProject, WorkOrder,
WorkOrderLineItem

```
ReplyToEmailMessageId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the inbound or outbound email message the current email message is a reply
to. It’s not possible to reply to a message whose `Status` is `Draft` .

This is a relationship field.

This is only set for Case related Email replies at setup.

**Relationship Name**
ReplyToEmailMessage

**Relationship Type**
Lookup


Standard Objects EmailMessage

**Field** **Details**

**Refers To**
EmailMessage

```
Source

Status

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
When Sync Email as Salesforce Activity is enabled, this value reflects from where the
email was captured automatically. Available in API version 64.0 and later.

Possible values are:

**•** `Einstein Activity Capture` –Captured as an entire email message by
Einstein Activity Capture.

**•** `Einstein Activity Capture Limited` –Captured as a header-only
email by Einstein Activity Capture. The sender, recipients, date, and time of the
message were captured, not the subject or body.

**•** `Email Integration App Manual` -Captured to track the email message
records created or edited from the mailapp.

**•** `Migrated Captured Email` -An email that was captured in Einstein
Activity Capture and migrated to an updated version of Einstein Activity Capture
in which Sync Email as Activity is turned on. Available in API version 65.0 and later.

**•** `Migrated Captured Email Header Only` -An email that was captured
in Einstein Activity Capture and migrated as header-only data to an updated
version of Einstein Activity Capture in which Sync Email as Activity is turned on.
Available in API version 65.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the email.

The `Status` field is mostly read-only. You can change the status only from _`New`_ to
_`Read`_ .

Possible values are:

**•** `0` (New)

**•** `1` (Read)

**•** `2` (Replied)

**•** `3` (Sent)

**•** `4` (Forwarded)

**•** `5` (Draft)


Standard Objects EmailMessage

**Field** **Details**

For emails not sent as part of a case, only the status `3` (Sent) is valid.

```
Subject

TextBody

ThreadIdentifier

ToAddress

```

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The subject line of the email.

You can’t send emails unless at least one of these fields has content.

**•** Subject field

**•** HTML Body or Text Body field

As the sender, you can provide the content, or it can be automatically inserted using
predefined values. An email template can also include the content for these fields.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The body of the email, in plain text format. If `TextBody` isn’t set, then it’s extracted
from `HtmlBody` .

You can’t send emails unless at least one of these fields has content.

**•** Subject field

**•** HTML Body or Text Body field

As the sender, you can provide the content, or it can be automatically inserted using
predefined values. An email template can also include the content for these fields

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The ID of the email thread the email message belongs to. This field is used by features
that sync emails directly from an inbox into Salesforce. This field is not used by
On-Demand Email-to-Case.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects EmailMessage

**Field** **Details**

**Description**
A string array of email addresses for recipients who were sent the email message.
Include only email addresses that aren’t associated with Contact, Lead, or User records
in Salesforce. If the recipient is a contact, lead, or user, add their ID to the `ToIds`
field instead of adding their email address to the `ToAddress` field. Then the email
message is automatically associated with the contact, lead, or user.

You can’t send emails unless there’s at least one recipient.

```
ToIds

ValidatedFromAddress

```

Usage

EmailMessage is limited to 50 custom fields.

**Type**
JunctionIdList

**Properties**
Create, Update

**Description**
A string array of IDs for contacts, leads, and users who were sent a carbon copy of the
email message. Each ID is linked to an `EmailMessageRelation` record, which
represents the relationship between an email message and a Contact, Lead, or User
record.

Adding a `JunctionIdList` field name to the `fieldsToNull` property deletes
all related junction records. This action can’t be undone.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

A picklist value with either the sender's address, org-wide email addresses, or
Email-to-Case routing address. The email address must be verified. If the sender’s
email address is used, the sender must be the current user.

`ValidatedFromAddress` isn’t suitable for use in Group By or Sort By statements.
Use `FromAddress` instead.

If your org uses Email-to-Case, a case is created when an email is sent to one of your company’s addresses. The email, which is related
to the case by the `ParentID` field, is stored as an EmailMessage record. When users view the email, they see the EmailMessage record.

If your org uses Enhanced Email, each email is stored as an EmailMessage record and a Task record. When users view an email, they see
the EmailMessage record.

Note: In an org with Email-to-Case enabled, an inbound (Incoming = true) email with case as the parent record won’t create a
task automatically. This functionality respects the Create Task from Email setting for each Email-to-Case routing address.


### Standard Objects EmailMessageMigration

If you would like to change the recipients or contents of an outbound email, don’t use automation tools, like Flows or Apex triggers, to
update EmailMessage records. Unless they are for a draft, updates to EmailMessage records will not be reflected in the actual sent email.
[To update an email’s data before it’s sent, use Quick Action predefined values or a QuickActionDefaultsHandler.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_interface_QuickAction_QuickActionDefaultsHandler.htm)

When a Flow creates an EmailMessage with set values in the audit fields (like CreatedBy and CreatedDate), any FeedItem automatically
created for that EmailMessage will not share the same audit field values.

Sample Code—Apex

This sample logs email activity in Salesforce.

```
   // if EnhancedEmail Perm is not enabled, continue logging the email as a task

   // if EnhancedEmail Perm is enabled, create an EmailMessage object

   EmailMessage emailMessage = new EmailMessage();

   emailMessage.status = '3'; // email was sent

   emailMessage.relatedToId = '006B0000003weZGIAY'; // related to record e.g. an opportunity

   emailMessage.fromAddress = 'sender@example.com'; // from address

   emailMessage.fromName = 'Dan Perkins'; // from name

   emailMessage.subject = 'This is the Subject!'; // email subject

   emailMessage.htmlBody = '<html><body><b>Hello</b></body></html>'; // email body

   // Contact, Lead or User Ids of recipients

   String[] toIds = new String[]{'003B000000AxcEjIAJ'};

   emailMessage.toIds = toIds;

   // additional recipients who don’t have a corresponding contact, lead or user id in the

   Salesforce org (optional)

   emailMessage.toAddress = 'emailnotinsalesforce@toexample.com, anotherone@toexample.com';

   insert emailMessage; // insert

   // Add Email Message Relation for id of the sender

   EmailMessageRelation emr = new EmailMessageRelation();

   emr.emailMessageId = emailMessage.id;

   emr.relationId = '005B0000003qHvOIAU'; // user id of the sender

   emr.relationType = 'FromAddress';

   insert emr;

```

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**EmailMessageChangeEvent (API version 48.0)**
Change events are available for the object.

SEE ALSO:

Case

Overview of Salesforce Objects and Fields

### EmailMessageMigration

For internal use only.


### Standard Objects EmailMessageRelation EmailMessageRelation

Represents the relationship between an email and contacts, leads, and users. This object is available in API version 37.0 and later.

Special Access Rules

### EmailMessageRelation is only available for organizations that use Email-to-Case or Enhanced Email, which is automatically enabled for

most customers.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Fields

**Field Name** **Details**

```
EmailMessageId

RelationAddress

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
### The ID of the EmailMessage record.

This is a relationship field.

**Relationship Name**
### EmailMessage

**Relationship Type**
Lookup

**Refers To**
### EmailMessage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The email address of the sender or recipient.

Note: If a record relates an email to an existing contact, lead, or user record
in Salesforce, the value of `RelationAddress` is the current value of
the email address. If the value is not set, it is auto-populated from
`RelationId` .


Standard Objects EmailMessageRelation

**Field Name** **Details**

```
RelationId

RelationObjectType

RelationType

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The `RecordId` of the sender or recipient.

Note: If a record relates an email to an email address that’s not associated
with an existing contact, lead, or user record in Salesforce, the value of
`RelationId` is null.

This is a polymorphic relationship field.

**Relationship Name**
Relation

**Relationship Type**
Lookup

**Refers To**
Contact, Lead, User

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The API name of the object type of the `RecordId` in the `RelationId` field.
It can be a contact, lead, or user.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of relationship the contact, lead, or user has with the email message.
Possible values include:

**•** `ToAddress`

**•** `CcAddress`

**•** `BccAddress`

**•** `FromAddress`

**•** `OtherAddress`

For an Experience Cloud site user who is not the sender of the email, no
`BccAddress` relations are returned.


### Standard Objects EmailRelay

Usage

EmailMessageRelation allows an email to be related to contacts, leads, and users.

### EmailRelay

Represents the configuration for sending an email relay. An email relay routes email sent from Salesforce through your company’s email
servers. This object is available in API version 43.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

You must have the Email Administration, Customize Application, and View Setup user permissions to use this object.

Fields

**Field Name** **Details**

```
AuthType

Host

IsRequireAuth

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted Picklist, Sort, Update

**Description**

Specifies which SASL mechanism Salesforce uses for SMTP authentication. This
field is available when Enable SMTP Auth is selected. Select an option:

**•** PLAIN- Salesforce uses PLAIN SASL mechanism for SMTP authentication.
Default.

**•** LOGIN- Salesforce uses LOGIN SASL mechanism for SMTP authentication

This field is available in API version 52.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

Indicates the host name or IP address of your company's SMTP server.

**Type**
boolean


Standard Objects EmailRelay

**Field Name** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether (true) or not (false) authentication is required. When setting
this field to true, the `TlsSetting` must be set to **`RequiredVerify`** . This
field is available in API version 44.0 and later.

```
Password

Port

TlsSetting

```

**Type**
encryptedstring

**Properties**
Create, Nillable, Update

**Description**

Specifies the password for relay host STMP authentication. When
`IsRequireAuth` is set to true, this field is required. This field is available in
API version 44.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

Indicates the port number of your company's SMTP server.

**•** 25

**•** 587

**•** 10025

**•** 11025

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

Specifies whether Salesforce uses TLS for SMTP sessions.

**•** `Off` : TLS is turned off. SMTP session continues through an insecure
connection.

**•** `Preferred` : If the remote server supports TLS, Salesforce upgrades the
current SMTP session to use TLS. If TLS is unavailable, Salesforce continues
the session without TLS.


### Standard Objects EmailRoutingAddress

**Field Name** **Details**

**•** `Required` : Salesforce continues the session only if the remote server
supports TLS. If TLS is unavailable, Salesforce terminates the session without
delivering the email.

**•** `PreferredVerify` : If the remote server supports TLS, Salesforce upgrades
the current SMTP session to use TLS. Before the session begins, Salesforce
verifies that the certificate is signed by a valid certificate authority, and that
the common name presented in the certificate matches the domain or mail
exchange of the current connection. If TLS is available but the certificate is
not signed or the common name does not match, Salesforce disconnects
the session and does not deliver the email. If TLS is unavailable, Salesforce
continues the session without TLS.

**•** `RequiredVerify` : Salesforce continues the session only if the remote
server supports TLS, the certificate is signed by a valid certificate authority,
and the common name presented in the certificate matches the domain or
mail exchange to which Salesforce is connected. If any of these criteria are
not met, Salesforce terminates the session without delivering the email.

```
Username

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Specifies the username for relay host STMP authentication. When
`IsRequireAuth` is set to true, this field is required. This field is available in
API version 44.0 and later.

An email relay must be associated with an active email domain filter to take effect. If you set up multiple email relays in one org, they
are processed in the priority order of their email domain filters.

Tip: If you also plan to activate Bounce Management and Email Compliance Management, confirm with your email admin that
[your company allows relaying email sent from Salesforce. For more information on bounce management, see Configure Deliverability](https://help.salesforce.com/articleView?id=emailadmin_send_through_salesforce_configure_deliverability.htm&language=en_US)
[Settings for Emails Sent from Salesforce.](https://help.salesforce.com/articleView?id=emailadmin_send_through_salesforce_configure_deliverability.htm&language=en_US)

SEE ALSO:

EmailServicesFunction

EmailDomainFilter

### EmailRoutingAddress

An email address used for Email-to-Case. Email routing addresses store a unique email services address provided by Salesforce and
configuration options for emails received by this address.


### Standard Objects EmailServicesAddress

Supported Calls

`create()`, `describeSObjects()`, `delete()`, `update()`, `query()`, `retrieve()`, `upsert()`

Special Access Rules

To access this object, Email-to-Case must be enabled. Only admin users can access this object.

Fields

**Field** **Details**

```
PersonalName

Address

### `EmailServicesAddress`

```

SEE ALSO:

### EmailServicesAddress

**Type**
string

**Properties**
Create, Filter, Sort, Update

**Description**
The display name of the EmailRoutingAddress. Maximum size is 300 characters.

**Type**
email

**Properties**
Create, Filter, Sort, Update

**Description**
The email address to which your customers direct their questions. Emails are forwarded from
this address.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A unique, Salesforce-generated email address. This field value is read-only and can't be
modified. Emails are forwarded to this address.

### EmailServicesAddress

An email service address.

Each email service has one or more email addresses to which users can send messages for processing. An email service only processes
messages it receives at one of its addresses.


Standard Objects EmailServicesAddress

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Special Access Rules

As of Summer ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field** **Details**

```
AuthorizedSenders

DeveloperName

EmailDomainName

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Configures the email service address to only accept messages from the email addresses or
domains listed in this field. If the email service address receives a message from an unlisted
email address or domain, the email service performs the action specified in the
`AuthorizationFailureAction` field of its associated email service. Leave this field
blank if you want the email service address to receive email from any email address.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The name of the object in the API. This name can contain only underscores and alphanumeric
characters and must be unique in your org. It must begin with a letter, not include spaces,
not end with an underscore, and not contain two consecutive underscores. This 25-character
field must be unique among other EmailServicesAddress records under the same
EmailServiceFunction parent.

In managed packages, this field prevents naming conflicts on package installations. This field
is automatically generated, but you can supply your own value if you create the record using
the API. With this field, a developer can change the object’s name in a managed package
and the changes are reflected in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance might be slow
while Salesforce generates one for each record.

**Type**
string


Standard Objects EmailServicesAddress

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
A read only field you can query that contains the system-generated domain part of this email
service address. The system generates a unique domain-part for each email service address
to ensure that no two email service addresses are identical.

```
FunctionId

IsActive

LocalPart

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the email service for which the email service address receives messages.

This is a relationship field.

**Relationship Name**
Function

**Relationship Type**
Lookup

**Refers To**
EmailServicesFunction

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this object is active (true) or not (false).

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The local-part of the email service address. The local-part of the address is the string that
comes before the @ symbol.

For the local-part of a Salesforce email address, all alphanumeric characters are valid, plus
the following special characters:

```
  ! # $ % & amp; ' * / = ? ^ _ + - ` { | } ~,

```

The dot character (.) is also valid as long as it's not the first or last character.

Email addresses aren’t case-sensitive.


### Standard Objects EmailServicesFunction

**Field** **Details**

```
RunAsUserId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The username of the user whose permissions the email service assumes when processing
messages sent to this address.

This object supports the email services feature, which allows you to create automated processes that use Apex classes to process the
contents, headers, and attachments of inbound email. For example, you can create an email service that automatically creates contact
records based on contact information in messages.

SEE ALSO:

### EmailServicesFunction EmailServicesFunction

An email service.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
upsert()

```

Special Access Rules

As of Summer ’20 and later, only authenticated internal and external users can access this object.

Fields

**Field** **Details**

```
AddressInactiveAction

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates what the email service does with messages received at an email address that is
inactive.


Standard Objects EmailServicesFunction

**Field** **Details**

One of the following values:

**•** `UseSystemDefault` —The system default is used. (In API version 41.0 and earlier,
the value specified for this choice is `0` .)

**•** `Bounce` —The email service returns the message to the sender with a notification that
explains why the message was rejected. (In API version 41.0 and earlier, the value specified
for this choice is `1` .)

**•** `Discard` —The email service deletes the message without notifying the sender. (In
API version 41.0 and earlier, the value specified for this choice is `2` .)

**•** `Requeue` —The email service queues the message for processing in the next 24 hours.
If the message is not processed within 24 hours, the email service returns the message
to the sender with a notification that explains why the message was rejected. (In API
version 41.0 and earlier, the value specified for this choice is `3` .)

```
ApexClassId

AttachmentOption

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. The ID of the Apex class that the email service uses to process inbound messages.

This field is required for API version 12.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates the types of attachments the email service accepts. One of the following values:

**•** `None` —The email service accepts the message but discards any attachment. (In API
version 41.0 and earlier, the value specified for this choice is `0` .)

**•** `NoContent` —The attachment metadata (filename, MIME type, and so on) is provided
to the Apex class, but the body is set to `null` . There was no previous numeric value for
this choice.

**•** `TextOnly` —The email service only accepts the following types of attachments:

**–** Attachments with a Multipurpose Internet Mail Extension (MIME) type of text.

**–** Attachments with a MIME type of application/octet-stream and a file name that ends
with either a .vcf or .vcs extension. These are saved as text/x-vcard and text/calendar
MIME types, respectively.

(In API version 41.0 and earlier, the value specified for this choice is `1` .)

**•** `BinaryOnly` —The email service only accepts binary attachments, such as image,
audio, application, and video files. (In API version 41.0 and earlier, the value specified for
this choice is `2` .)


Standard Objects EmailServicesFunction

**Field** **Details**

**•** `All` —The email service accepts any type of attachment. (In API version 41.0 and earlier,
the value specified for this choice is `3` .)

```
AuthenticationFailureAction

AuthorizationFailureAction

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates what the email service does with messages that fail or do not support any of the
authentication protocols if the `IsAuthenticationRequired` field is true.

One of the following values:

**•** `UseSystemDefault` —The system default is used. (In API version 41.0 and earlier,
the value specified for this choice is `0` .)

**•** `Bounce` —The email service returns the message to the sender with a notification that
explains why the message was rejected. (In API version 41.0 and earlier, the value specified
for this choice is `1` .)

**•** `Discard` —The email service deletes the message without notifying the sender. (In
API version 41.0 and earlier, the value specified for this choice is `2` .)

**•** `Requeue` —The email service queues the message for processing in the next 24 hours.
If the message is not processed within 24 hours, the email service returns the message
to the sender with a notification that explains why the message was rejected. (In API
version 41.0 and earlier, the value specified for this choice is `3` .)

**Type**
picklist

**Properties**
Defaulted on create, Group, Sort, Create, Filter, Nillable, Restricted picklist, Update

**Description**
Indicates what the email service does with messages received from senders who are not
listed in the `AuthorizedSenders` field on either the email service or email service
address.

One of the following values:

**•** `UseSystemDefault` —The system default is used. (In API version 41.0 and earlier,
the value specified for this choice is `0` .)

**•** `Bounce` —The email service returns the message to the sender with a notification that
explains why the message was rejected. (In API version 41.0 and earlier, the value specified
for this choice is `1` .)

**•** `Discard` —The email service deletes the message without notifying the sender. (In
API version 41.0 and earlier, the value specified for this choice is `2` .)

**•** `Requeue` —The email service queues the message for processing in the next 24 hours.
If the message is not processed within 24 hours, the email service returns the message


Standard Objects EmailServicesFunction

**Field** **Details**

to the sender with a notification that explains why the message was rejected. (In API
version 41.0 and earlier, the value specified for this choice is `3` .)

```
AuthorizedSenders

ErrorRoutingAddress

FunctionInactiveAction

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Configures the email service to only accept messages from the email addresses or domains
listed in this field. If the email service receives a message from an unlisted email address or
domain, the email service performs the action specified in the
`AuthorizationFailureAction` field. Leave this field blank if you want the email
service to receive email from any email address.

**Type**
email

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The destination email address for error notification email messages when
`IsErrorRoutingEnabled` is `true` .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates what the email service does with messages it receives when the email service itself
is inactive.

One of the following values:

**•** `UseSystemDefault` —The system default is used. (In API version 41.0 and earlier,
the value specified for this choice is `0` .)

**•** `Bounce` —The email service returns the message to the sender with a notification that
explains why the message was rejected. (In API version 41.0 and earlier, the value specified
for this choice is `1` .)

**•** `Discard` —The email service deletes the message without notifying the sender. (In
API version 41.0 and earlier, the value specified for this choice is `2` .)

**•** `Requeue` —The email service queues the message for processing in the next 24 hours.
If the message is not processed within 24 hours, the email service returns the message
to the sender with a notification that explains why the message was rejected. (In API
version 41.0 and earlier, the value specified for this choice is `3` .)


Standard Objects EmailServicesFunction

**Field** **Details**

```
FunctionName

IsActive

IsAuthenticationRequired

IsErrorRoutingEnabled

IsTextAttachmentsAsBinary

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the email service.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this object is active ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Configures the email service to verify the legitimacy of the sending server before processing
a message. The email service uses the SPF, SenderId, and DomainKeys protocols to verify the
sender's legitimacy: If the sending server passes at least one of these protocols and does not
fail any, the email service accepts the email. If the server fails a protocol or does not support
any of the protocols, the email service performs the action specified in the
`AuthenticationFailureAction` field.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
When incoming email messages can’t be processed, indicates whether error notification
email messages are routed to a chosen address or to the senders.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true`, text attachments are supplied to the Apex code as a
`Messaging.BinaryAttachment` instead of as a


Standard Objects EmailServicesFunction

**Field** **Details**

`Messaging.TextAttachment` . This means that the body is supplied as an Apex Blob
instead of as an Apex String.

```
IsTextTruncated

IsTlsRequired

OverLimitAction

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
This field is deprecated. It is not available as of API version 23.0 and is deprecated and hidden
in versions 17.0 through 22.0. In all API versions, the email service now accepts inbound
email messages up to the 10 MB size limit, without truncating the text. Previously, it indicated
whether the email service truncated and accepted email messages with HTML body text,
plain body text, and text attachments over approximately 100,000 characters ( `true` ) or
rejected these email messages and notified the sender ( `false` ).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Not currently in use.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates what the email service does with messages if the total number of messages
processed by all email services combined has reached the daily limit for your organization.

One of the following values:

**•** `UseSystemDefault` —The system default is used. (In API version 41.0 and earlier,
the value specified for this choice is `0` .)

**•** `Bounce` —The email service returns the message to the sender with a notification that
explains why the message was rejected. (In API version 41.0 and earlier, the value specified
for this choice is `1` .)

**•** `Discard` —The email service deletes the message without notifying the sender. (In
API version 41.0 and earlier, the value specified for this choice is `2` .)

**•** `Requeue` —The email service queues the message for processing in the next 24 hours.
If the message is not processed within 24 hours, the email service returns the message
to the sender with a notification that explains why the message was rejected. (In API
version 41.0 and earlier, the value specified for this choice is `3` .)

The system calculates the limit by multiplying the number of user licenses by 1,000.


### Standard Objects EmailStatus

Usage

This object supports the email services feature, which allows you to create automated processes that use Apex classes to process the
contents, headers, and attachments of inbound email. For example, you can create an email service that automatically creates contact
records based on contact information in messages.

SEE ALSO:

EmailServicesAddress

### EmailStatus

Represents the status of email sent.

Supported Calls

```
   describeSObjects()

```

Special Access Rules

Customer Portal users can’t access this object.

Fields

**Field** **Details**

```
EmailTemplateName

FirstOpenDate

LastOpenDate

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the EmailTemplate.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date when the email was first opened by recipient. Label is **Date Opened** .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects EmailStatus

**Field** **Details**

**Description**
Date when the email was last opened by recipient.

```
TaskId

TimesOpened

WhoId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The activity (task or event) associated with the email. Label is **Activity ID** .

This is a relationship field.

**Relationship Name**
Task

**Relationship Type**
Lookup

**Refers To**
Task

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Number of times the recipient opened the email.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The WhoId represents a human such as a lead or a contact. WhoIds are polymorphic.
Polymorphic means a WhoId is equivalent to a contact’s ID or a lead’s ID. The label is `Name`
`ID` .

This is a polymorphic relationship field.

**Relationship Name**
Who

**Relationship Type**
Lookup


### Standard Objects EmailTemplate

**Field** **Details**

**Refers To**
Contact, Lead

SEE ALSO:

### EmailTemplate EmailTemplate

Represents a template for an email, mass email, list email, or Sales Engagement email. Supported in first-generation managed packages
only.

Note: You can’t send a mass email using a Visualforce email template.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `update()`, `upsert()`

Special Access Rules

Customer Portal users can’t access this object.

Fields

**Field** **Details**

```
ApiVersion

Body

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The API version for this class. Every class has an API version specified at creation.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Content of the email. Limit: 384 KB.


Standard Objects EmailTemplate

**Field** **Details**

```
BrandTemplateId

DeliveryRate

Description

DeveloperName

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. ID of the BrandTemplate associated with this email template. The brand template
supplies letterhead information for the email template.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**

Read-only. The percentage of the emails that were delivered compared to the number that
bounced (soft and hard). Note: this data includes emails that were delivered to the recipient's
spam folder.

This field is available in API version 46.0 and later. To access this field, your org must use Sales
Engagement and users need the Sales Engagement User or Sales Engagement Cadence
Creator permission set. This field value includes emails sent via the ListEmail object or Sales
Engagement cadences.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the template, for example, Promotion Mass Mailing.

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
are reflected in a subscriber’s organization. Label is **Template Unique Name** .

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance may slow while
Salesforce generates one for each record.


Standard Objects EmailTemplate

**Field** **Details**

```
Encoding

EnhancedLetterheadId

EntityType

FolderId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Character set encoding for the template.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the enhanced letterhead associated with the email template.

Note: To use an enhanced letterhead, associate it with a Lightning email template
that uses the HML merge language.

This is a relationship field.

**Relationship Name**
EnhancedLetterhead

**Relationship Type**
Lookup

**Refers To**
EnhancedLetterhead

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort,

**Description**
When `UIType` is `2` (Lightning Experience) or `3` (Lightning ExperienceSample),
`EntityType` indicates which entities this template can be used with (for example, account
or lead). Valid values are standard object ID prefixes: 001 for account, 003 for contact, 006
for opportunity, and 00Q for lead, 500 for case, and 701 for campaign.

This field has been removed in API version 39.0. Use `RelatedEntityType` instead.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the folder that contains the template.

This is a relationship field.


Standard Objects EmailTemplate

**Field** **Details**

**Relationship Name**
Folder

**Relationship Type**
Lookup

**Refers To**
Folder, Organization, User

```
FolderName

HasSalesforceFiles

HtmlValue

IsActive

IsBuilderContent

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The name of the folder that contains the template.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If the email template has attachments from Salesforce Files. The default value is false.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
This field contains the content of the email message, including HTML coding to render the
email message. Limit: 384 KB.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates that this template is active if `true`, or inactive if `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects EmailTemplate

**Field** **Details**

**Description**
If the email template was made in Email Template Builder. The default value is false.

```
LastUsedDate

Markup

Name

NamespacePrefix

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when this email template was last used.

Used with Salesforce Classic templates.

Not typically used with Lightning Experience templates.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The Visualforce markup, HTML, JavaScript, or any other Web-enabled code that defines the
content of the template.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the template. Label is **Email Template Name** .

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


Standard Objects EmailTemplate

**Field** **Details**

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

This field can’t be accessed unless the logged-in user has the Customize Application
permission.

```
OwnerId

RelatedEntityType

Subject

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the template.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
When `UIType` is `2` (Lightning Experience) or `3` (Lightning ExperienceSample),
`RelatedEntityType` indicates which entities this template can be used with. Valid
values are the entity API name: "Account" for account, "Contact" for contact, "Opportunity"
for opportunity, "Lead" for lead, and so on. The value can be any entity the user has read
access to (including custom entities) but not virtual entities, setup entities, or platform entities.

No restrictions exist at the schema level.

**Type**
string

**Properties**
Create, Nillable, Sort, Update

**Description**
Content of the subject line.

The limit is 1,000 characters for Lightning email templates and 230 characters for Classic
email templates.


Standard Objects EmailTemplate

**Field** **Details**

```
TemplateStyle

TemplateType

TimesUsed

TotalDelivered

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Style of the template.

Possible values are:

**•** `formalLetter` —Formal Letter

**•** `freeForm` —Free Form Letter

**•** `newsletter` —Newsletter

**•** `none` —No Email Layout

**•** `products` —Products

**•** `promotionLeft` —Promotion (Left)

**•** `promotionRight` —Promotion (Right)

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Type of template.

Possible values are:

**•** `custom` —Custom

**•** `html` —HTML

**•** `text` —Text

**•** `visualforce` —Visualforce

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of times this email template has been used.

Used with Salesforce Classic templates.

Not typically used with Lightning Experience templates.

**Type**
int


Standard Objects EmailTemplate

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**

Read-only. The total number of emails sent minus hard and soft bounces. Note: this data
includes emails that were delivered to the recipient's spam folder.

This field is available in API version 46.0 and later. To access this field, your org must use Sales
Engagement and users need the Sales Engagement User or Sales Engagement Cadence
Creator permission set. This field value includes emails sent via the ListEmail object or Sales
Engagement cadences.

```
TotalHardBounced

TotalOpens

TotalSent

```

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

Read-only. The total number of emails that permanently bounced back to the sender because
the address is invalid. A hard bounce can occur because the domain name doesn't exist or
because the recipient is unknown.

This field is available in API version 46.0 and later. To access this field, your org must use Sales
Engagement and users need the Sales Engagement User or Sales Engagement Cadence
Creator permission set. This field value includes emails sent via the ListEmail object or Sales
Engagement cadences.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

Read-only. The total number of times a prospect’s email client loaded the images in the
HTML version of the email. We also record an open if the prospect clicks a link within the
HTML or text email without downloading images. A click indicates that they viewed the
message. Some email clients (Outlook, Apple Mail, Thunderbird) don’t display images by
default. Pardot counts an open each time the images load.

This field is available in API version 46.0 and later. To access this field, your org must use Sales
Engagement and users need the Sales Engagement User or Sales Engagement Cadence
Creator permission set. This field value includes emails sent via the ListEmail object or Sales
Engagement cadences.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects EmailTemplate

**Field** **Details**

**Description**
Read-only. The total number of emails sent, including bounced, opted-out, and invalid To:
addresses.

This field is available in API version 46.0 and later. To access this field, your org must use Sales
Engagement and users need the Sales Engagement User or Sales Engagement Cadence
Creator permission set. This field value includes emails sent via the ListEmail object or Sales
Engagement cadences.

```
TotalSoftBounced

UIType

```

Usage

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

Read-only. The total number of times a recipient’s mail server acknowledged the email, but
returned it to the sender. Sometimes it is because the recipient's mailbox is full or the mail
server is temporarily unavailable. A soft bounce message can sometimes be delivered at
another time. After 5 soft bounces, Pardot opts the prospect out of emails.

This field is available in API version 46.0 and later. To access this field, your org must use Sales
Engagement and users need the Sales Engagement User or Sales Engagement Cadence
Creator permission set. This field value includes emails sent via the ListEmail object or Sales
Engagement cadences.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the user interface where this template is usable.

Possible values are:

**•** `Aloha`

**•** `SFX`

**•** `SFX_Sample` —SFXSample

To retrieve this object, issue a describe call on an object, which returns a query result for each activity since the object was created. You
can't query these records.


### Standard Objects EmailTemplateMonthlyMetric

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**EmailTemplateChangeEvent (API version 48.0)**
Change events are available for the object.

SEE ALSO:

Attachment

EmailStatus

DocumentAttachmentMap

### EmailTemplateMonthlyMetric

Represents the monthly engagement metrics for an email template. This object is available in API version 53.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Sales Engagement must be enabled.

Fields

**Field** **Details**

```
AllEmailsBouncedCount

AllEmailsDeliveredCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total of hard and soft bounced emails for this email template in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of successfully delivered emails for this email template in the month.

This is a calculated field.


Standard Objects EmailTemplateMonthlyMetric

**Field** **Details**

```
AllEmailsHardBouncedCount

AllEmailsLinkClickedCount

AllEmailsNotDeliveredCount

AllEmailsOpenedCount

AllEmailsOutOfOfficeCount

AllEmailsRepliedCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of hard bounced emails for this email template in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails containing a link clicked by the recipient for this email template in
the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails not delivered for this email template in the month. This field is available
in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails opened by the recipient for this email template in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that triggered an out-of-office reply for this email template in the
month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects EmailTemplateMonthlyMetric

**Field** **Details**

**Description**
The number of emails replied to for this email template in the month.

```
AllEmailsSentCount

AllEmailsSoftBouncedCount

AllEmailsTrackedSentCount

AllEmailsUntrackedSentCount

DeliveredRecipientCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent for this email template in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails soft bounced for this email template in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with engagement tracking enabled for this email template in the
month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent without engagement tracking for this email template in the
month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were successfully delivered an email for this email template
in the month. This field is available in API version 54.0 and later.


Standard Objects EmailTemplateMonthlyMetric

**Field** **Details**

This is a calculated field.

```
DeliveredRecipientRate

EmailTemplateId

HardBounceTrackableSends

HrdBncTrackableRecipientSends

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of unique recipients that received an email you sent. This field is available
in API version 54.0 and later.

This is a calculated field.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related email template.

This is a relationship field.

**Relationship Name**
EmailTemplate

**Relationship Type**
Lookup

**Refers To**
EmailTemplate

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with hard bounce tracking. This field is available in API version
54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who received an email with hard bounce tracking. This field is
available in API version 54.0 and later.


Standard Objects EmailTemplateMonthlyMetric

**Field** **Details**

```
IsLocked

LinkClickTrackableSends

LinkClkTrackableRecipientSends

MayEdit

Month

MonthInt

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the monthly metric record is locked or not.

The default value is 'false'.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with link click tracking for the email template in the month. This
field is available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who received an email with link tracking for the email template in
the month. This field is available in API version 54.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the monthly metric record can be edited or not.

The default value is 'false'.

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
The month in which the engagement occurred.

**Type**
int


Standard Objects EmailTemplateMonthlyMetric

**Field** **Details**

**Properties**
Filter, Group, idLookup, Sort

**Description**
The month in which the engagement occurred, in yyyymm format.

```
OooTrackableRecipientSends

OpenTrackableRecipientSends

OpenTrackableSends

OutOfOfficeTrackableSends

RecipientReplies

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who received an email with out-of-office tracking for the email
template in the month. Out-of-office tracking requires Inbox. This field is available in API
version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who received an email with open tracking for the email template
in the month. This field is available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with open tracking for the email template in the month. This field
is available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with out-of-office tracking for the email template in the month.
This field is available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects EmailTemplateMonthlyMetric

**Field** **Details**

**Description**
The number of unique recipients who replied to an email for this email template in the
month. This field is available in API version 54.0 and later.

```
RecipientSends

RecipientsHardBounced

RecipientsOutOfOffice

RecipientsSoftBounced

ReplyTrackableRecipientSends

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique email recipients for this email template in the month. This field is
available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients that hard-bounced an email for this email template in the month.
Hard bounces can mean that the recipient's email address doesn't exist or is misspelled. This
field is available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients that responded with an out-of-office reply for the email template
in the month. This field is available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients that soft-bounced an email for the email template in the month.
A soft bounce often indicates a temporary issue with the recipient's email server, such as a
full inbox. This field is available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects EmailTemplateMonthlyMetric

**Field** **Details**

**Description**
The number of recipients who received an email with reply tracking for this email template
in the month. This field is available in API version 54.0 and later.

```
ReplyTrackableSends

SftBncTrackableRecipientSends

SoftBounceTrackableSends

SomeEmailsDeliveredCount

SomeEmailsDeliveredRate

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with reply tracking for the email template in the month. This field
is available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who received an email with soft bounce tracking for the email
template in the month. This field is available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with soft bounce tracking for the email template in the month.
This field is available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of sent emails that were successfully delivered to at least one of its recipients
for the email template in the month. This field is available in API version 54.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort


Standard Objects EmailTemplateMonthlyMetric

**Field** **Details**

**Description**
The percentage of sent and tracked emails that were successfully delivered to at least one
of their recipients for the email template in the month. This field is available in API version
54.0 and later.

This is a calculated field.

```
TrackableRecipientSendHrdBncRt

TrackableRecipientSendOooRate

TrackableRecipientSendReplyRt

TrackableRecipientSendSftBncRt

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to unique recipients with hard bounce tracking that hard
bounced for the email template in the month. This field is available in API version 54.0 and
later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with out-of-office tracking that received out-of-office replies
from unique recipients for the email template in the month. This field is available in API
version 54.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with reply tracking that received replies from unique recipients
for the email template in the month. This field is available in API version 54.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort


Standard Objects EmailTemplateMonthlyMetric

**Field** **Details**

**Description**
The percentage of emails sent to unique recipients with soft bounce tracking that
soft-bounced for the email template in the month. This field is available in API version 54.0
and later.

This is a calculated field.

```
TrackableSendHardBounceRate

TrackableSendLinkClickRate

TrackableSendOpenRate

TrackableSendOutOfOfficeRate

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with hard bounce tracking that hard bounced for the email
template in the month. This field is available in API version 54.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with link tracking that had link clicks for the email template
in the month. This field is available in API version 54.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with open tracking that were opened by the recipient for the
email template in the month. This field is available in API version 54.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with out-of-office tracking that received out-of-office replies
for the email template in the month. This field is available in API version 54.0 and later.

This is a calculated field.


Standard Objects EmailTemplateMonthlyMetric

**Field** **Details**

```
TrackableSendReplyRate

TrackableSendSoftBounceRate

UniqueEmailsLinkClickedCount

UniqueEmailsOpenedCount

UniqueEmailsRepliedCount

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with reply tracking that received replies for the email template
in the month. This field is available in API version 54.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with soft bounce tracking that soft bounced for the email
template in the month. This field is available in API version 54.0 and later.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of link clicks by unique recipients for the email template in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times an email you sent was opened by a unique recipient for the email
template in the month. When you send a list email, this field increments each time a recipient
opens the received email.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of replies from unique recipients for the email template in the month.


### Standard Objects EmbeddedServiceDetail EmbeddedServiceDetail

Represents a metadata catalog object that exposes fields from the underlying Embedded Service setup objects defined in each
EmbeddedServiceConfig deployment for guest users. Guest users don’t have direct access to the Embedded Service setup objects.
Available in API version 39.0 and later.

Supported SOAP Calls

`describeSObjects()`, `query()`

Supported REST HTTP Methods

```
   GET

```

Fields

**Field** **Details**

```
AvatarImg

ContrastInvertedColor

ContrastPrimaryColor

CustomMinimizedComponent

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL of the image used as the agent avatar image.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Accent branding color used in the embedded component, displayed as a hexadecimal value.
Changes made to this field in the API aren’t reflected in the embedded component.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Value of the `ContrastPrimaryColor` field in the EmbeddedServiceBranding setup
object.

**Type**
string


Standard Objects EmbeddedServiceDetail

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The custom Aura component that’s used for the minimized state for this Embedded Chat
deployment.

```
CustomPrechatComponent

DurableId

FieldServiceConfirmCardImg

FieldServiceHomeImg

FieldServiceLogoImg

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The custom Aura component that’s used for the pre-chat page for this Embedded Chat
deployment.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Developer name for the EmbeddedServiceConfig.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL of the image used for the confirmation card in embedded Appointment Management
(beta).

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL of the image used for the home screen in embedded Appointment Management (beta).

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL of the logo used for the home screen in embedded Appointment Management (beta).


Standard Objects EmbeddedServiceDetail

**Field** **Details**

```
Font

FontSize

HeaderBackgroundImg

Height

IsFieldServiceEnabled

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Font used in the chat text of the Embedded Chat window.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Font size for the embedded component.

Possible values are:

**•** Small

**•** Medium

**•** Large

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL of the image used for the header background in Embedded Chat. This field is removed
in API version 49.0 and later. The header background image is no longer supported.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Height of the embedded component.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether Field Service is enabled for this Embedded Service deployment ( `true` )
or not ( `false` ). Embedded Appointment Management is currently beta.


Standard Objects EmbeddedServiceDetail

**Field** **Details**

```
IsLiveAgentEnabled

IsOfflineCaseEnabled

IsPrechatEnabled

IsQueuePositionEnabled

NavBarColor

NavBarTextColor

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether Chat is enabled for this Embedded Service deployment ( `true` ) or not
( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether offline support is enabled for this Embedded Chat deployment ( `true` )
or not ( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Value of the `PrechatEnabled` field in the EmbeddedServiceLiveAgent setup object.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether queue position (displaying the customer’s place in line while they wait
for an agent) is enabled for this Embedded Chat deployment ( `true` ) or not ( `false` ).

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Value of the `NavBarColor` field in the EmbeddedServiceBranding setup object.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects EmbeddedServiceDetail

**Field** **Details**

**Description**
This field is used to set the text color for the header.

```
OfflineCaseBackgroundImg

PrechatBackgroundImg

PrimaryColor

SecondaryColor

SecondaryNavBarColor

ShouldHideAuthDialog

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL of the image used for the background for the offline support case form in Embedded
Chat.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL of the image used for the background for the pre-chat form in Embedded Chat.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Value of the `PrimaryColor` field in the EmbeddedServiceBranding setup object.

**Type**
string

**Properties**
Filter, Group, Nillable Sort

**Description**
Value of the `SecondaryColor` field in the EmbeddedServiceBranding setup object.

**Type**
string

**Properties**
Filter, Group, Nillable Sort

**Description**
This field is used to set the color of a secondary header.

**Type**
boolean


Standard Objects EmbeddedServiceDetail

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether the prompt that the customer log in again during a flow should be hidden
( `true` ) or not ( `false` ). When it’s hidden, the customer is taken directly to your login page.

```
ShouldShowExistingAppointment

ShouldShowNewAppointment

Site

SmallCompanyLogoImg

WaitingStateBackgroundImg

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether to display a button on the home screen for customers to access their
existing appointments ( `true` ) or not ( `false` ) for embedded Appointment Management
(beta).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether to display a button on the home screen for customers to create a new
appointment ( `true` ) or not ( `false` ) for embedded Appointment Management (beta).

**Type**
string

**Properties**
Filter, Group, Nillable Sort

**Description**
Value of the `Site` field in the EmbeddedServiceConfig setup object.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL of the logo image used with Embedded Chat.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects EmbeddedServiceLabel

**Field** **Details**

**Description**
URL of the image used for the background image in Embedded Chat while the customer
waits to be connected with a support agent.

```
Width

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Width of the embedded component.

Note: Any changes you make to the image fields override what you’ve entered in Setup. We recommend setting your image
URLs in Setup.

### EmbeddedServiceLabel

Represents a customized label in Embedded Chat or embedded Appointment Management.This object is available in API version 44.0
and later.

Supported SOAP Calls

`describeSObjects()`, `query()`

Supported REST HTTP Methods

```
GET

```

Fields

**Field** **Details**

```
CustomLabelName

DurableId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The developer name for the custom label.

**Type**
string


### Standard Objects Employee

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique name containing `EmbeddedServiceConfig.labelKey` .

```
EmbeddedServiceConfigDeveloperName

LabelKey

### Employee

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Developer name for the EmbeddedServiceConfig.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of label for this embedded component. The value corresponds to the label within
a label group (substate of chat state or page type).

Represents an employee within a company or organization. This object is available in API version 48.0 and later. In API version 49.0 and
later, this object supports reports, criteria-based sharing rules, and history tracking, plus you can exclude individual fields from custom
page layouts.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search() undelete()`, `update()`, `upsert()`

Special Access Rules

To access this object, you must have a Workplace Command Center permission set license and the Provides access to Workplace
Command Center features system permission or have the Employee Management and Employee User add-on licenses.


Standard Objects Employee

Fields

**Field** **Details**

```
AboutMe

AlternateEmail

Availability

AvailabilityEndDate

AvailabilityStartDate

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Information about the employee, such as areas of interest or skills. Values can be provided
on Employee’s profile page. This field is available even if Chatter is disabled.

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee’s alternate email address.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee’s availability status.

Possible values are:

**•** `In The Office`

**•** `Out Of Office`

**•** `Out Sick`

**•** `PTO`

**•** `Volunteering Time Off`

**•** `Working Remotely`

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The end date of the Employee’s availability, inclusive of the date.

**Type**
dateTime


Standard Objects Employee

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The start date of the Employee’s availability, inclusive of the date.

```
BannerPhotoUrl

CurrentWellnessStatus

DateOfBirth

Email

EmployeeNumber

```

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
Read only. The URL for the employee's banner photo. Available in API v51.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee’s current wellness status.

Possible values are:

**•** `Available To Work`

**•** `Remote Work Only`

**•** `Unavailable`

**•** `Unknown`

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee’s date of birth.

**Type**
email

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The employee’s email address. This field is unique within your organization.

**Type**
string


Standard Objects Employee

**Field** **Details**

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. The employee's employment ID for the organization they were hired into. This
field is unique within your organization.

```
EmployeeStatus

EmploymentType

FirstName

FullPhotoUrl

```

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The employee's current work status.

Possible values are:

**•** `Active`

**•** `Inactive`

**•** `Leave`

**•** `Terminated`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee's full-time or part-time status.

Possible values are:

**•** `Full-Time`

**•** `Part-Time`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The employee’s first name.

**Type**
url

**Properties**
Filter, Nillable, Sort


Standard Objects Employee

**Field** **Details**

**Description**
Read only. The URL for the employee's profile photo. The URL is updated every time a photo
is uploaded and reflects the most recent photo. If a newer photo has been uploaded, the
URL returned for an older photo isn’t guaranteed to return a photo. Query this field for the
URL of the most recent photo. Available in API v51.0 and later.

```
Gender

HomeAddress

HomeCity

HomeCountry

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee’s gender.

Possible values are:

**•** `Female`

**•** `Male`

**•** `Non-Binary / Non-Conforming`

**•** `Other`

**•** `Prefer Not to State`

**•** `Transgender Female`

**•** `Transgender Male`

**Type**
address

**Properties**
Filter, Nillable

**Description**
The employee’s home address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city for the employee’s home address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The county for the employee’s home address.


Standard Objects Employee

**Field** **Details**

```
HomeGeocodeAccuracy

HomeLatitude

HomeLongitude

HomePhone

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The level of accuracy of an employee’s home address geographical coordinates compared
with its physical address. A geocoding service typically provides this value based on the
address’s latitude and longitude coordinates.

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
Used with HomeLongitude to specify the precise geolocation of the employee’s home
address. Acceptable values are numbers between –90 and 90 with up to 15 decimal places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with HomeLatitude to specify the precise geolocation of the employee’s home address.
Acceptable values are numbers between –180 and 180 with up to 15 decimal places.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Employee

**Field** **Details**

**Description**
The employee’s home phone number.

```
HomePostalCode

HomeState

HomeStreet

IndividualId

InternalOrganizationUnitId

JobProfile

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code for the employee’s home address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state for the employee’s home address.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street for the employee’s home address.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A reference to the Individual record that this employee is assigned to.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A reference to the InternalOrganizationUnit this employee is assigned to.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Employee

**Field** **Details**

**Description**
The employee’s job profile at the company.

```
LastName

LastReferencedDate

LastViewedDate

LocationId

ManagerId

MediumPhotoUrl

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The employee’s last name.

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
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A reference to the Location that this employee is assigned to.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A reference to the Employee record of the employee's manager.

**Type**
url


Standard Objects Employee

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
Read only. The URL for the medium-sized employee's profile photo. The URL is updated
every time a photo is uploaded and reflects the most recent photo. If a newer photo has
been uploaded, the URL returned for an older photo isn’t guaranteed to return a photo.
Query this field for the URL of the most recent photo. Available in API v51.0 and later.

```
MiddleName

Name

NameSuffix

OutOfOfficeMessage

OwnerId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee’s middle name.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
A compound field of `Employee.FirstName`, `Employee.MiddleName`, and
`Employee.LastName` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee’s suffix.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The message portion of the employee availability. This message can provide reasons or
details about the change in availability. The maximum length of this string is 40 characters.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects Employee

**Field** **Details**

**Description**
The ID of the user who currently owns this record. Default value is the user logged in to the
API to perform the create operation.

```
PreferredFirstName

PreferredPronoun

RelatedPersonId

SmallPhotoUrl

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name the employee prefers to be called.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee's preferred pronoun.

Possible values are:

**•** `He/Him/His`

**•** `Other/Ask Me`

**•** `She/Her/Hers`

**•** `They/Them/Theirs`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Links an employee to a person account with a unique value. Reserved for future use. Don’t
edit it.

**Type**
url

**Properties**
Filter, Nillable, Sort

**Description**
Read only. The URL for the small-sized employee's profile photo. The URL is updated every
time a photo is uploaded and reflects the most recent photo. If a newer photo has been
uploaded, the URL returned for an older photo isn’t guaranteed to return a photo. Query this
field for the URL of the most recent photo. Available in API v51.0 and later.


Standard Objects Employee

**Field** **Details**

```
StatusAsOf

StatusEndDate

TimeZone

UserId

WorkPhone

WorkerType

```

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
Required. Start date of the employee’s current status.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Planned end date for the employee’s status.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The time zone which the employee’s work hours fall within.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Lookup field to associate an Employee record with a user in the org. The field is optional and
unique.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee's formatted work phone number including country code and extension.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


### Standard Objects Employee2

**Field** **Details**

**Description**
Required. The type of worker for the employee.

Possible values are:

**•** `Alumnus`

**•** `Contractor`

### • Employee

**•** `Intern`

**•** `Temporary`

```
WorkingHoursEnd

WorkingHoursStart

```

Associated Objects

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The end time of the employee’s working hours.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The start time of the employee’s working hours.

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**EmployeeHistory (API version 49.0)**
History is available for tracked fields of the object.

**EmployeeOwnerSharingRule**

Sharing rules are available for the object.

**EmployeesShare (API version 49.0)**
Sharing is available for the object.

SEE ALSO:

_[Workplace Command Center for Work.com Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.workdotcom_dev_guide.meta/workdotcom_dev_guide/wdc_cc_dev_workplace_cc_solution.htm)_ : Extend Work.com with Custom Solutions

### Employee2

Represents an employee within a company or an organization. This object is available in API version 62.0 and later.


Standard Objects Employee2

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available if Talent Recruitment Management is enabled in your org. It’s also available to customers who purchase the
Unified Employee license.To access the object, you need one of these permission sets.

**User Type** **Permission Set**

Internal Users HR Service Workspace Personnel

Salesforce Platform Users
Employee Hub Community User

OR

Unified Employee Permission Set

OR

Work.com License

Unified Employee Users Unified Employee Permission Set

Fields

**Field** **Details**

```
AlternateEmail

ContactId

```

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee’s alternate email address.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The contact associated with the employee.

**Relationship Name**
Contact


Standard Objects Employee2

**Field** **Details**

**Relationship Type**
Master-detail

**Refers To**
Contact (the master object)

```
CurrencyIsoCode

EmployeeNumber

EmployeeStatus

EmployeeType

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ISO currency code for the post-authorization request.

Valid value is:

**•** `USD` —U.S. Dollar

The default value is `USD` .

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The employee's unique ID for their organization.

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The employee's current work status.

Valid values are:

**•** `Active`

**•** `Inactive`

**•** `Leave`

**•** `Terminated`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The employee's full-time or part-time status.


Standard Objects Employee2

**Field** **Details**

Valid values are:

**•** `Alumnus`

**•** `Contractor`

**•** `Permanent`

**•** `Intern`

**•** `Temporary`

```
EmploymentType

InternalOrganizationUnitId

LastReferencedDate

LastViewedDate

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee's full-time or part-time status.

Valid values are:

**•** `Full-Time`

**•** `Part-Time`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The internal organization unit associated with the employee.

**Relationship Name**
InternalOrganizationUnit

**Refers To**
InternalOrganizationUnit

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


Standard Objects Employee2

**Field** **Details**

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that the user only accessed the record or a related list view
( `LastReferencedDate` ), but not viewed the record itself.

```
Name

StatusEndDate

StatusStartDate

User

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the employee record.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The planned end date for the employee’s status.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The start date of the employee’s current status.

**Type**
reference

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The user associated with the employee. After this field is set to a non-null value, you can’t
update it.

**Relationship Name**
User

**Description**
User


### Standard Objects EmployeeCrisisAssessment EmployeeCrisisAssessment

Represents a crisis assessment of an Employee. This object is available in API version 48.0 and later. In API version 49.0 and later, this
object supports reports, criteria-based sharing rules, and history tracking, plus you can exclude individual fields from custom page layouts.

For Work.com, when an employee responds to a wellness survey, an EmployeeCrisisAssessment record is created based on an employee's
answers.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To access this object, you must be assigned a Workplace Command Center permission set license and the Provides access to Workplace
Command Center features system permission.

Fields

**Field** **Details**

```
Assessment

AssessmentDate

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The employee’s COVID-19 status at the time of the assessment.

Possible values are:

**•** `COVID-19 Immune or Recovered`

**•** `COVID-19 No Symptoms`

**•** `COVID-19 Symptoms or Exposed`

**•** `COVID-19 Test Negative`

**•** `COVID-19 Test Positive`

**•** `Declined`

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date of the assessment. Required


Standard Objects EmployeeCrisisAssessment

**Field** **Details**

```
AssessmentNumber

CrisisId

EmployeeId

LastReferencedDate

LastViewedDate

OwnerId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The assessment record number.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Crisis that this assessment is associated with.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The Employee that this assessment is associated with.

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
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


### Standard Objects EmpUserProvisioningProcess

**Field** **Details**

**Description**
The ID of the user who currently owns this record. Default value is the user logged in to the
API to perform the create operation.

```
SourceAssessment

SourceSystem

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The record in the source system that drove this assessment.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The source system that drove this assessment.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**EmployeeCrisisAssessmentHistory (API version 49.0)**
History is available for tracked fields of the object.

**EmployeeCrisisAssessmentOwnerSharingRule**

Sharing rules are available for the object.

**EmployeeCrisisAssessmentShare (API version 49.0)**
Sharing is available for the object.

SEE ALSO:

_[Workplace Command Center for Work.com Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.ajax.meta/workdotcom_dev_guide/wdc_cc_overview.htm)_ : Extend Work.com with Custom Solutions

### EmpUserProvisioningProcess

Represents an employee-user provisioning process. This object is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`


Standard Objects EmpUserProvisioningProcess

Special Access Rules

This object requires a Workplace Command Center add-on license, or an Employee Experience add-on license.

Fields

**Field** **Details**

```
EndTime

ErrorRecordCount

LastReferencedDate

LastViewedDate

Name

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time that the user provisioning process ended.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of records that encountered an error during the user provisioning process.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the user provisioning process was last referenced, with a precision
of one second.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the user provisioning process was last viewed, with a precision of
one second.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the user provisioning process.


Standard Objects EmpUserProvisioningProcess

**Field** **Details**

```
ProcessStatus

StartTime

SuccessRecordCount

TotalRecordCount

```

Usage

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the user provisioning process.

Possible values are:

**•** `Aborted`

**•** `Cancelled`

**•** `Failed`

**•** `Finished`

**•** `Initializing`

**•** `Processing`

**•** `Queued`

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time that the user provisioning process started.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of records that were successfully provisioned during the user provisioning
process.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of records in the user provisioning process.

Use the EmpUserProvisioningProcess to view the status of an employee-user provisioning process.


### Standard Objects EmpUserProvisionProcessErr EmpUserProvisionProcessErr

Represents an employee-user provisioning process error. This object is available in API version 52.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object requires a Workplace Command Center add-on license, or an Employee Experience add-on license.

Fields

**Field** **Details**

```
AccountId

EmployeeId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Person Account linked to the employee record associated with the error.

This is a relationship field.

**Relationship Name**
Account

**Refers To**
Account

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the employee record associated with the error.

This is a relationship field.

**Relationship Name**
Employee

**Relationship Type**
Lookup

**Refers To**
Employee


Standard Objects EmpUserProvisionProcessErr

**Field** **Details**

```
ErrorCode

ErrorMessage

LastReferencedDate

LastViewedDate

Name

ProvisioningProcessId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The error code if the provisioning isn’t successful.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If an error occurred, this field contains the error message.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the error was last referenced, with a precision of one second.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the error was last viewed, with a precision of one second.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the error.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the associated user provisioning process.


### Standard Objects EnablementMeasureDefinition

**Field** **Details**

This is a relationship field.

**Relationship Name**
ProvisioningProcess

**Relationship Type**
Lookup

**Refers To**
EmpUserProvisioningProcess

Usage

Use the EmpUserProvisionProcessErr to view the errors for an employee-user provisioning process.

### EnablementMeasureDefinition

Represents an Enablement measure, which specifies the job-related activity that a user performs to complete a milestone or outcome
in an Enablement program. A measure identifies a source object and optional related objects, with optional field filters and filter logic,
for tracking the activity. This object also represents Enablement measure information in Metadata API. This object is available in API
version 56.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To access this object, the Design and Deliver Enablement Programs permission is required. This permission is enabled by default as part
of the Manage Enablement Essentials permission set, which comes with the Enablement add-on license.

Fields

**Field** **Details**

```
AggregateFieldApiName

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The unique name in the API for the field that the `AggregateFunction` uses for
calculating.


Standard Objects EnablementMeasureDefinition

**Field** **Details**

For example, if you’re measuring how much revenue a sales rep has won, the value of
`aggregateFunction` is `Sum` and the value of `aggregateFieldApiName` is
`Amount`, which is the API name of the Amount field on the Opportunity object.

```
AggregateFunction

Description

DeveloperName

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The method for calculating progress towards the milestone or outcome from records that
qualify for the measure’s criteria.

Possible values are:

**•** `Average`

**•** `Count`

**•** `Sum`

For example, if you’re measuring the number of deals won, the function is `Count` .

If the function is `Average` or `Sum`, then `AggregateFieldApiName` specifies the
API name of the field to use for calculating progress.

**Type**
string

**Properties**
Create, Filter, Sort, Update

**Description**
An internal description for the measure to help Enablement admins understand the activity
that’s tracked.

**Type**
string

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


Standard Objects EnablementMeasureDefinition

**Field** **Details**

In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

```
DisplayFieldApiName

IsValid

Language

MasterLabel

```

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The unique name in the API for the field that primarily identifies records that qualify for the
activity you’re measuring. For example, if you’re measuring the number of deals won, you’re
tracking the Opportunity object, and maybe you want to identify opportunities by their
name. In this case, this field can be `Name`, the API name of the Opportunity Name field on
the Opportunity object.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether the measure is valid. A measure becomes invalid and stops tracking
progress under these circumstances:

**•** An object or field is removed.

**•** An object label or API name is renamed.

**•** A field’s API name is renamed.

Default is `false` . A measure only becomes invalid after a breaking change is saved the
[corresponding outcome or milestone progress is calculated. See Considerations for Creating](https://help.salesforce.com/s/articleView?id=sales.enablement_measures_considerations.htm&type=5&language=en_US)
[and Editing Measures.](https://help.salesforce.com/s/articleView?id=sales.enablement_measures_considerations.htm&type=5&language=en_US)

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Reserved for future use. Don’t edit this field.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


Standard Objects EnablementMeasureDefinition

**Field** **Details**

**Description**
Label for this EnablementMeasureDefinition value. This display value is the internal label that
doesn't get translated.

```
NamespacePrefix

PublishedDateTime

SourceMeasureObjectId

```

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

**•** In orgs that aren’t Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

Available in API version 62.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the measure was activated for use in Enablement programs.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the EnblMeasureObjectDefinition that specifies the criteria for the source object
that tracks the activity you're measuring. This field is a relationship field.

**Relationship Name**
SourceMeasureObject

**Relationship Type**
Lookup


### Standard Objects EnablementProgram

**Field** **Details**

**Refers To**
EnblMeasureObjectDefinition

```
SourceObjectApiName

Status

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The unique name in the API for the source object that tracks the activity you're measuring.
This value is a derived value. For example, if you're measuring the number of deals won, this
value is `Opportunity`, the API name for the Opportunity object.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The availability of the measure for use in Enablement programs.

Possible values are:

**•** `Archived` —Available in API versions 56.0 to 60.0.

**•** `Draft` —The measure is saved, but not activated for use in programs.

**•** `Published` —The measure is activated for use in programs. In Lightning Experience,
this value is Active.

An EnablementMeasureDefinition can have multiple EnblMeasureObjectDefinition references, depending on the number of related
objects in the measure. Consider an example measure that tracks activity on the Opportunity source object and the Account related
object.

**•** The EnablementMeasureDefinition identifies the Opportunity source object.

**•** An EnblMeasureObjectDefinition specifies the criteria on the Opportunity source object.

**•** An EnblMeasureObjectDefinition specifies the criteria on the Account related object.

### EnablementProgram

Represents an Enablement program, which includes exercises and measurable milestones to help users such as sales reps achieve specific
outcomes related to your company’s revenue goals. This object is available in API version 56.0 and later.


Standard Objects EnablementProgram

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

**•** For Enablement admins to create, update, and delete Enablement programs, the Design and Deliver Enablement Programs permission
is required. This permission is enabled by default as part of the Manage Enablement Essentials permission set, which comes with
the Enablement add-on license.

**•** For users who take Enablement programs, the Take Enablement Programs permission is required. This permission is enabled by
default as part of the Use Enablement Programs permission set, which comes with the Enablement add-on license.

**•** For partner users who take Partner Enablement programs, the Take Partner Enablement Programs permission is required. This
permission is enabled by default as part of the Use Partner Enablement Programs permission set, which comes with the Enablement
[add-on license. Partner Enablement also requires a supported Partner Relationship Management (PRM) add-on license.](https://help.salesforce.com/s/articleView?id=slack.prm_support_license_template.htm&type=5&language=en_US)

Fields

**Field** **Details**

```
Description

DoesAllowSelfEnrollment

EnablementProgramDefinitionId

```

**Type**
textarea

**Properties**
Create, Update

**Description**

A summary of the program’s goals and content that’s visible to users.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether users can self-enroll in programs that are shared with them ( `true` ) or
take only assigned programs ( `false` ). The default value is `false` .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The representation for the program in Metadata API. This field is a relationship field.

Available in API version 61.0 and later.

**Relationship Name**
EnablementProgramDefinition


Standard Objects EnablementProgram

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
EnablementProgramDefinition

```
IsOutcomeBased

LastReferencedDate

LastViewedDate

Name

NetworkId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the program includes a final, measurable outcome ( `true` ) or not ( `false` ).
The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a list view or related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record. If this value is null, maybe the
user accessed this record ( `LastReferencedDate` ) but not viewed it yet.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the program that’s visible to users. For example, `AE Onboarding`, `Event`
`Prep`, or `New Product Launch` .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects EnablementProgram

**Field** **Details**

**Description**
The ID of the supported Experience Cloud site where a partner program is available. For site
[requirements, see Considerations for Partner Enablement Programs.](https://help.salesforce.com/s/articleView?id=sales.enablement_partner_considerations.htm&type=5&language=en_US)

Available in API version 60.0 and later.

**Relationship Name**
Network

**Relationship Type**
Lookup

**Refers To**
Network

```
OwnerId

PublishedDateTime

Status

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the program. This field is a polymorphic relationship field.

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
The date that the program is published.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The status of the program. Only a published program is available for an Enablement admin
to assign to users or share with users so they can self-enroll.

Possible values are:

**•** `Archived`

**•** `Draft`


Standard Objects EnablementProgram

**Field** **Details**

**•** `Published`

```
TotalAssigned

TotalBehind

TotalCompleted

TotalDays

Type

```

**Type**
int

**Properties**
Nillable

**Description**
The number of assignments in this program. For example, if the program is assigned to 3
users, then `TotalAssigned=3` .

**Type**
int

**Properties**
Nillable

**Description**
The number of assignments that are behind in this program. For example, if the program is
assigned to 3 users, and 2 users are behind on their assignments, then `TotalBehind=2`

**Type**
int

**Properties**
Nillable

**Description**
The number of completed assignments in this program. For example, if the program is
assigned to 3 users, and 1 user has completed the program, then `TotalCompleted=1` .

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Total days of the program. This value is derived from the latest day of all items in the program,
including exercises, milestones, and the outcome. This field is a calculated field. For example,
a program has Task A on day 1 and Task B on day 2. Since Task B has the latest days of all
tasks, then `TotalDays=2` .

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of the program. Possible values are:


### Standard Objects EnablementProgramDefinition

**Field** **Details**

### • Enablement —A sales program in Lightning Experience.

**•** `PtnrEnablement` —A partner program in a supported Experience Cloud site. Available
in API version 60.0 and later.

**•** `EmployeeServiceEnablement` —An employee enablement program in Employee
Portal. Available in API version 63.0 and later.

Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**EnablementProgramOwnerSharingRule (API version 60.0)**
Sharing rules are available for the object.

**EnablementProgramShare (API version 60.0)**
Sharing is available for the object.

### EnablementProgramDefinition

Represents Enablement program information in Metadata API. This object is available in API version 61.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

To access this object, the Design and Deliver Enablement Programs permission is required. This permission is enabled by default as part
of the Manage Enablement Essentials permission set, which comes with the Enablement add-on license.

Fields

**Field** **Details**

```
DeveloperName

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name of the object in the API. The name:

**•** must be 40 characters or fewer


Standard Objects EnablementProgramDefinition

**Field** **Details**

**•** must begin with a letter

**•** can contain only underscores and alphanumeric characters

**•** can’t include spaces

**•** can’t end with an underscore

**•** can’t contain 2 consecutive underscores

In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

```
EnablementProgramId

Language

MasterLabel

NamespacePrefix

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Enablement program to reference in Metadata API.

This field is a relationship field.

**Relationship Name**
EnablementProgram

**Relationship Type**
Lookup

**Refers To**
EnablementProgram

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Reserved for future use. Don’t edit this field.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Label for this EnablementProgramDefinition value. This display value is the internal label
that doesn't get translated.

**Type**
string


### Standard Objects EnblMeasureObjectDefinition

**Field** **Details**

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

**•** In orgs that aren’t Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

Available in API version 62.0 and later.

### EnblMeasureObjectDefinition

Represents the criteria for an object that tracks the job-related activity for an Enablement measure in an Enablement program. A separate
### EnblMeasureObjectDefinition is used for a measure's source object and each optional related object. This object is available in API version

56.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To access this object, the Design and Deliver Enablement Programs permission is required. This permission is enabled by default as part
of the Manage Enablement Essentials permission set, which comes with the Enablement add-on license.

Fields

**Field** **Details**

```
DeveloperName

```

**Type**
string


Standard Objects EnblMeasureObjectDefinition

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
EnablementMeasureDefinitionId

FilterLogic

Language

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The measure that the EnblMeasureObjectDefinition applies to. This field is a relationship
field.

**Relationship Name**
EnablementMeasureDefinition

**Relationship Type**
Lookup

**Refers To**
EnablementMeasureDefinition

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An expression that determines how to evaluate the optional field filters for the object.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Reserved for future use. Don’t edit this field.


Standard Objects EnblMeasureObjectDefinition

**Field** **Details**

```
MasterLabel

NamespacePrefix

ObjectApiName

SequenceNumber

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for the EnblMeasureObjectDefinition value. This display value is the internal label that
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

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that aren’t Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

Available in API version 62.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The unique name in the API for the measure's source object or optional related object that
the EnblMeasureObjectDefinition describes.

For example, if you're measuring the number of deals won for a specific product, this field
on one EnblMeasureObjectDefinition references the API name of the Opportunity source
object and this field on another EnblMeasureObjectDefinition references the API name of
the Opportunity Product related object.

**Type**
int


### Standard Objects EnblPgmTaskMeasureProgress

**Field** **Details**

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A number that specifies the order of the EnblMeasureObjectDefinition, relative to other
EnblMeasureObjectDefinition records under the same EnablementMeasureDefinition, starting
at 1.

Usage

An EnablementMeasureDefinition can have multiple EnblMeasureObjectDefinition references, depending on the number of related
objects in the measure. Consider an example measure that tracks activity on the Opportunity source object and the Account related
object.

**•** The EnablementMeasureDefinition identifies the Opportunity source object.

**•** An EnblMeasureObjectDefinition specifies the criteria on the Opportunity source object.

**•** An EnblMeasureObjectDefinition specifies the criteria on the Account related object.

### EnblPgmTaskMeasureProgress

Represents a user’s progress through the object and field requirements that an Enablement measure defines for an outcome or milestone
in an Enablement program. This object is available in API version 61.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

**•** For Enablement admins to create, update, and delete Enablement programs, the Design and Deliver Enablement Programs permission
is required. This permission is enabled by default as part of the Manage Enablement Essentials permission set, which comes with
the Enablement add-on license.

**•** For users who take Enablement programs, the Take Enablement Programs permission is required. This permission is enabled by
default as part of the Use Enablement Programs permission set, which comes with the Enablement add-on license.

**•** For partner users who take Partner Enablement programs, the Take Partner Enablement Programs permission is required. This
permission is enabled by default as part of the Use Partner Enablement Programs permission set, which comes with the Enablement
[add-on license. Partner Enablement also requires a supported Partner Relationship Management (PRM) add-on license.](https://help.salesforce.com/s/articleView?id=slack.prm_support_license_template.htm&type=5&language=en_US)


Standard Objects EnblPgmTaskMeasureProgress

Fields

**Field** **Details**

```
ContributingRecordCount

EnblProgramTaskMeasureId

EnblProgramTaskProgressId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of records that qualify for a user’s progress towards completing an outcome or
milestone. To qualify, the activity must meet the criteria that the corresponding Enablement
measure defines for specific objects, fields, and field values.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the record that represents the connection between a specific Enablement measure
and a specific milestone or outcome in an Enablement program.

This field is a relationship field.

**Relationship Name**
EnblProgramTaskMeasure

**Relationship Type**
Lookup

**Refers To**
EnblProgramTaskMeasure

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the record that represents the progress through the milestone or outcome.

This field is a relationship field.

**Relationship Name**
EnblProgramTaskProgress

**Relationship Type**
Master-detail

**Refers To**
EnblProgramTaskProgress (the master object)


### Standard Objects EnblProgramSection

**Field** **Details**

```
MeasureComputationResult

```

**Type**
double

**Properties**
Filter, Sort

**Description**
The calculated progress through the measure’s requirements for a milestone or outcome.
For example, if the measure is the dollar amount of all closed opportunities, then the field
value is measured in dollars.

For a composite milestone or a composite outcome, this value represents the progress
through only one measure associated with the milestone or outcome.

### EnblProgramSection

Represents an optional section in an Enablement program. A section can include other program items, such as milestones and exercises.
This object is available in API version 60.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

**•** For Enablement admins to create, update, and delete Enablement programs, the Design and Deliver Enablement Programs permission
is required. This permission is enabled by default as part of the Manage Enablement Essentials permission set, which comes with
the Enablement add-on license.

**•** For users who take Enablement programs, the Take Enablement Programs permission is required. This permission is enabled by
default as part of the Use Enablement Programs permission set, which comes with the Enablement add-on license.

**•** For partner users who take Partner Enablement programs, the Take Partner Enablement Programs permission is required. This
permission is enabled by default as part of the Use Partner Enablement Programs permission set, which comes with the Enablement
[add-on license. Partner Enablement also requires a supported Partner Relationship Management (PRM) add-on license.](https://help.salesforce.com/s/articleView?id=slack.prm_support_license_template.htm&type=5&language=en_US)

Fields

**Field** **Details**

```
DeveloperName

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name of the object in the API. The name:


Standard Objects EnblProgramSection

**Field** **Details**

**•** must be 40 characters or fewer

**•** must begin with a letter

**•** can contain only underscores and alphanumeric characters

**•** can’t include spaces

**•** can’t end with an underscore

**•** can’t contain 2 consecutive underscores

In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

Available in API version 61.0 and later.

```
EnablementProgramId

Name

SequenceNumber

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The Enablement program that contains the section. This field is a relationship field.

**Relationship Name**
EnablementProgram

**Relationship Type**
Lookup

**Refers To**
EnablementProgram

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The title of the section that’s visible to users when they take the program.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
A number that specifies the order of the section, relative to other sections, starting at 0.


### Standard Objects EnblProgramTaskDefinition EnblProgramTaskDefinition

Represents an outcome, a milestone, or an exercise in an Enablement program. A program task is also known as a program item. This
object is available in API version 60.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

**•** For Enablement admins to create, update, and delete Enablement programs, the Design and Deliver Enablement Programs permission
is required. This permission is enabled by default as part of the Manage Enablement Essentials permission set, which comes with
the Enablement add-on license.

**•** For users who take Enablement programs, the Take Enablement Programs permission is required. This permission is enabled by
default as part of the Use Enablement Programs permission set, which comes with the Enablement add-on license.

**•** For partner users who take Partner Enablement programs, the Take Partner Enablement Programs permission is required. This
permission is enabled by default as part of the Use Partner Enablement Programs permission set, which comes with the Enablement
[add-on license. Partner Enablement also requires a supported Partner Relationship Management (PRM) add-on license.](https://help.salesforce.com/s/articleView?id=slack.prm_support_license_template.htm&type=5&language=en_US)

Fields

**Field** **Details**

```
CompositeMilestoneType

CustomEnblPgmTaskSubCategoryId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of logic to use for evaluating the activity from two Enablement measures in a
composite milestone.

Possible values are:

**•** `Addition`

**•** `Division`

**•** `Percentage`

Available in API version 61.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects EnblProgramTaskDefinition

**Field** **Details**

**Description**
The ID of the EnblProgramTaskSubCategory record associated with a custom exercise type.
This field is required when the `TaskSubCategory` field’s value is `CustomExercise` .

This field is a relationship field.

Available in API version 62.0 and later.

**Relationship Name**
CustomEnblPgmTaskSubCategory

**Relationship Type**
Lookup

**Refers To**
EnblProgramTaskSubCategory

```
Day

Description

EnablementProgramId

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The day of the program when the item is due, relative to the program's start date. For example,
if a user is expected to complete an exercise where they watch a product demo by day 2,
this field’s value is 2. For an outcome, this field specifies the number of days the full program
takes. For example, if your program lasts 60 days, the value of this field is 60 for the outcome.
This field’s value contributes to the program’s due date that users see when they take the
program.

**Type**
textarea

**Properties**
Create

**Description**
A summary of the outcome, milestone, or exercise that’s visible to users when they take the
program.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the Enablement program that contains the outcome, milestone, or exercise. This
field is a relationship field.

**Relationship Name**
EnablementProgram


Standard Objects EnblProgramTaskDefinition

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
EnablementProgram

```
EnblProgramSectionId

IsMilestoneAnOutcome

LearningItemId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of an optional program section that contains the milestone or exercise. This field is a
relationship field.

**Relationship Name**
EnblProgramSection

**Relationship Type**
Lookup

**Refers To**
EnblProgramSection

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the program item is the program’s final outcome ( `true` ) or an incremental
milestone ( `false` ). The default value is `false` .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the learning item record for the outcome, milestone, or exercise. This field is a
relationship field.

**Relationship Name**
LearningItem

**Relationship Type**
Lookup

**Refers To**
LearningItem


Standard Objects EnblProgramTaskDefinition

**Field** **Details**

```
MilestoneTarget

MinimumSampleSize

Name

SequenceNumber

StandardCustomExerciseType

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The target value for a user to achieve to get credit for completing the outcome or milestone.
The unit depends on the specific measure used with the outcome or milestone. For example,
if the measure is the dollar amount of all closed opportunities, then the field value is measured
in dollars.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of records to evaluate when calculating progress for an outcome or milestone
that uses an average-based measure. Use this field with `MilestoneTarget` . For example,
if you want users to achieve an average deal size of $50,000 after closing 4 deals, then this
field’s value is `4` and `MilestoneTarget` is `50000` .

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The title of the outcome, milestone, or exercise that’s visible to users when they take the
program.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
A number that specifies the order of the milestone or exercise, relative to other milestones
or exercises that have the same due date in the program or in the same section, starting at
0. This number determines the order of items that users see for that day in the program.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


### Standard Objects EnblProgramTaskMeasure

**Field** **Details**

**Description**
Reserved for future use.

```
TaskCategory

TaskSubCategory

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of program item. Possible values are:

**•** `Exercise`

**•** `Milestone`

`Milestone` is used for both the program’s final outcome and incremental milestones.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of exercise. This value determines the content associated with the exercise. For
example, if the field value is `Video`, the exercise must reference video content from the
Enablement workspace in the Digital Experiences app. The `LearningItemId` field
specifies the reference to that video content. Possible values are:

**•** `ActionItem`

**•** `AudioRecording`

**•** `CustomExercise` —Available in API version 62.0 and later.

**•** `Document`

**•** `FeedbackRequest`

**•** `Other`

**•** `OtherExercise`

**•** `ScheduledEvent`

**•** `StandardCustomExercise` —Reserved for future use.

**•** `TextLesson`

**•** `Trailhead`

**•** `Video`

### EnblProgramTaskMeasure

Represents the connection between an Enablement measure and a specific milestone or outcome in an Enablement program. This
object is available in API version 61.0 and later.


Standard Objects EnblProgramTaskMeasure

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

To access this object, the Design and Deliver Enablement Programs permission is required. This permission is enabled by default as part
of the Manage Enablement Essentials permission set, which comes with the Enablement add-on license.

Fields

**Field** **Details**

```
EnablementMeasureDefinitionId

EnblProgramTaskDefinitionId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the Enablement measure to use with a milestone or outcome.

This field is a relationship field.

**Relationship Name**
EnablementMeasureDefinition

**Relationship Type**
Lookup

**Refers To**
EnablementMeasureDefinition

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the outcome or milestone that uses the Enablement measure.

This field is a relationship field.

**Relationship Name**
EnblProgramTaskDefinition

**Relationship Type**
Master-detail

**Refers To**
EnblProgramTaskDefinition (the master object)


### Standard Objects EnblProgramTaskProgress

**Field** **Details**

```
SequenceNumber

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
A number that specifies the order of the Enablement measure when multiple measures are
used with one outcome or milestone, starting at 0. For example, in a composite milestone
that uses the Percentage function, the measure that provides the numerator value is sequence
0 and the measure that provides the denominator value is sequence 1.

### EnblProgramTaskProgress

Represents a user’s progress towards completing an outcome, a milestone, or an exercise in an Enablement program. This object is
available in API version 60.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

**•** For Enablement admins to create, update, and delete Enablement programs, the Design and Deliver Enablement Programs permission
is required. This permission is enabled by default as part of the Manage Enablement Essentials permission set, which comes with
the Enablement add-on license.

**•** For users who take Enablement programs, the Take Enablement Programs permission is required. This permission is enabled by
default as part of the Use Enablement Programs permission set, which comes with the Enablement add-on license.

**•** For partner users who take Partner Enablement programs, the Take Partner Enablement Programs permission is required. This
permission is enabled by default as part of the Use Partner Enablement Programs permission set, which comes with the Enablement
[add-on license. Partner Enablement also requires a supported Partner Relationship Management (PRM) add-on license.](https://help.salesforce.com/s/articleView?id=slack.prm_support_license_template.htm&type=5&language=en_US)

Fields

**Field** **Details**

```
CompletedDateTime

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the user completed the outcome, milestone, or exercise.


Standard Objects EnblProgramTaskProgress

**Field** **Details**

```
CompletedOnDay

CompletedPercent

ContributingRecordCount

DueDate

EnblProgramTaskDefinitionId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of days that the user took to complete the outcome, milestone, or exercise.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
Percentage of the outcome, milestone, or exercise that’s complete.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of records that qualify for a user’s progress towards completing an outcome or
milestone. To qualify, the activity must meet the criteria that the corresponding Enablement
measure defines for specific objects, fields, and field values.

Available in API version 61.0 and later.

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
The date the outcome, milestone, or exercise is due.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the outcome, milestone, or exercise definition. This field is a relationship field.

**Relationship Name**
EnblProgramTaskDefinition

**Relationship Type**
Lookup


Standard Objects EnblProgramTaskProgress

**Field** **Details**

**Refers To**
EnblProgramTaskDefinition

```
IsCompleted

IsNoLongerTracking

LearningItemProgressId

MilestoneComputationResult

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Whether the outcome, milestone, or exercise is complete ( `true` ) or not ( `false` ). The
default value is `false` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If the user hasn’t completed the outcome or milestone and 30 days have elapsed since the
program’s due date, the value is `true` . Otherwise, the value is `false` . The default value
is `false` [. For details, see Completion Statuses in Enablement Analytics.](https://help.salesforce.com/s/articleView?id=sales.enablement_analytics_completion_statuses.htm&type=5&language=en_US)

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the record that tracks the user's progress through the program that includes this
outcome, milestone, or exercise. This field is a relationship field.

**Relationship Name**
LearningItemProgress

**Relationship Type**
Lookup

**Refers To**
LearningItemProgress

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Derived from the associated EnblProgramTaskDefinition record. For example, if a milestone
has a single measure A with a result of 5, this field’s value is 5.


### Standard Objects EnblProgramTaskSubCategory

**Field** **Details**

```
ProgressStatus

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Status of the outcome, milestone, or exercise progress. Possible values are:

**•** `Behind`

**•** `Completed Late`

**•** `Completed On Time`

**•** `No Longer Tracking`

**•** `Not Completed`

**•** `Overdue`

[For details, see Completion Statuses in Enablement Analytics.](https://help.salesforce.com/s/articleView?id=sales.enablement_analytics_completion_statuses.htm&type=5&language=en_US)

### EnblProgramTaskSubCategory

Represents a custom exercise type that an Enablement admin adds to an Enablement program in Program Builder. A custom exercise
type also requires a corresponding EnblProgramTaskDefinition record for Program Builder and corresponding LearningItem and
LearningItemType records for when users take the exercise in the Guidance Center. This object is available in API version 62.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

**•** For Enablement admins to create, update, and delete Enablement programs, the Design and Deliver Enablement Programs permission
is required. This permission is enabled by default as part of the Manage Enablement Essentials permission set, which comes with
the Enablement add-on license.

**•** For users who take Enablement programs, the Take Enablement Programs permission is required. This permission is enabled by
default as part of the Use Enablement Programs permission set, which comes with the Enablement add-on license.

Important: Custom exercises aren’t compatible with Partner Enablement programs.

Fields

**Field** **Details**

```
DeveloperName

```

**Type**
string


Standard Objects EnblProgramTaskSubCategory

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
Icon

Language

LearningItemTypeId

```

**Type**
textarea

**Properties**
Create, Update

**Description**
The icon to use for the custom exercise type in Program Builder.

Use the format _**`iconType`**_ `:` _**`iconName`**_, where the values correspond to icon categories
[and names from the Salesforce Lightning Design System.](https://www.lightningdesignsystem.com/icons/)

**•** _**`iconType`**_ is the type of icon, such as `standard` or `doctype` .

**•** _**`iconName`**_ is the icon name, such as `flow` or `slide` .

For example, to use the Standard type Flow icon, this value is `standard:flow` . For details,
[see Implement Custom Exercise Types for Enablement Programs in the](https://developer.salesforce.com/docs/sales/enablement/guide/enablement-custom-exercises-intro.html) _Sales Programs and_
_Partner Tracks with Enablement Developer Guide_ .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Reserved for future use. Don’t edit this field.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


### Standard Objects EngagementChannelType

**Field** **Details**

**Description**
The ID of the learning item type record that represents this custom exercise type in the
Guidance Center when users take a program.

This field is a relationship field.

**Relationship Name**
LearningItemType

**Refers To**
LearningItemType

```
MasterLabel

NamespacePrefix

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for this EnblProgramTaskSubCategory value. This display value is the internal label that
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

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that aren’t Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

### EngagementChannelType

Represents a channel through which a customer can be reached for communication. This object is available in API version 48.0 and later.


Standard Objects EngagementChannelType

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ContactPointType

LastReferencedDate

LastViewedDate

Name

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The contact point type of the channel.

Possible values are:

**•** `Email`

**•** `MailingAddress`

**•** `Phone`

**•** `Social`

**•** `Web`

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


### Standard Objects EngagementSignal

**Field** **Details**

```
 OwnerId

```

Associated Objects

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the account owner associated with this customer.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**EngagementChannelTypeChangeEvent (API version 61.0)**
Change events are available for the object.

**EngagementChannelTypeFeed**

Feed tracking is available for the object.

**EngagementChannelTypeHistory**

History is available for tracked fields of the object.

**EngagementChannelTypeOwnerSharingRule**

Sharing rules are available for the object.

**EngagementChannelTypeShare**

Sharing is available for the object.

### EngagementSignal

Represents data about an individual’s engagement action, such as a web click, an email response, or a PDF download. This object is
available in API version 62.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects EngagementSignal

Fields

**Field** **Details**

```
DataSpaceId

Description

DeveloperName

IsRemote

LastReferencedDate

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Required. Unique identifier that refers to the data space where the engagement signal
originates.

This field is a relationship field.

**Relationship Name**
DataSpace

**Refers To**
DataSpace

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
An optional text description of the engagement signal.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Required. API name for the engagement signal that's system-or user-generated.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates if the engagement signal object is owned by a different org in Data 360.

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects EngagementSignal

**Field** **Details**

**Description**
Timestamp that indicates the last time the engagement signal was referenced by the current
user.

```
LastViewedDate

Name

Status

```

Usage

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp that indicates the last time the current user viewed the engagement signal record.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Required. Text label that identifies the engagement signal.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Picklist value that indicates the current status of the engagement signal.

Possible values are:

**•** `Active`

**•** `CreateError` —Error

**•** `DeleteError` —Error

**•** `Deleting`

**•** `EditError` —Error

**•** `Preparing`

**•** `Processing`

The default value is `Processing` .

Use this object to define foundational data for your business objectives and recommendations in Salesforce Personalization. Use mapped
data model object (DMO) fields to identify and track an individual’s engagement actions. For example, use data about a web click, an
email response, or a PDF download to help achieve your personalization goals.


### Standard Objects EngagementSignalCmpndMetric EngagementSignalCmpndMetric

Represents a rate metric that measures the ratio between two engagement signal metrics, such as product orders and product views
to calculate a conversion rate, or email clicks and email opens to determine a click-through rate. Use this object to create complex
measurements for A/B testing and web experimentation. This object is available in API version 62.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CompoundMetricFormula

DenomEngmtSignalMetricId

IsRemote

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
A read-only formula field that concatenates the three core components of a Compound
Metric—the primary metric, the operator, and the secondary metric—into a single string.
This field is unique within your Salesforce org.

This field is a calculated field.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Points to the `EngagementSignalMetric` record that serves as the denominator of
the compound metric.

This field is a relationship field.

**Relationship Name**
DenomEngmtSignalMetric

**Refers To**
EngagementSignalMetric

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


Standard Objects EngagementSignalCmpndMetric

**Field** **Details**

**Description**
Indicates if the engagement signal compound metric object is owned by a different org in
Data 360.

The default value is `false` .

```
LastReferencedDate

LastViewedDate

Name

NumerEngmtSignalMetricId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp that indicates the last time the engagement signal compound metric was
referenced by the current user.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp that indicates the last time the current user viewed the engagement signal
compound metric record.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Required. Text label that identifies the engagement signal compound metric.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Points to the `EngagementSignalMetric` record that serves as the numerator of the
compound metric.

This field is a relationship field.

**Relationship Name**
NumerEngmtSignalMetric

**Refers To**
EngagementSignalMetric


Standard Objects EngagementSignalCmpndMetric

**Field** **Details**

```
Operator

OwnerId

```

Usage

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Represents the mathematical operation that combines the numerator and denominator
metrics in the compound metric formula.

Possible values are:

**•** `Ratio`

The default value is `Ratio` .

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Represents the ID of the user or group that owns the engagement signal compound metric.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

Use this object to create rate metrics for A/B testing and web experimentation. To measure the effectiveness of personalization experiences,
divide the numerator metric by the denominator metric. These metrics help you make data-driven decisions to compare content
performance. This object is used for measurement and isn’t used for machine learning model training.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**EngagementSignalCmpndMetricShare on page 67**
Sharing is available for the object.


### Standard Objects EngagementSignalMetric EngagementSignalMetric

Represents a measurable quantity that’s derived from an engagement signal, such as the sum of revenue or a count of clicks. Use this
object to track user engagement for A/B tests, machine learning model training, and attribution configurations. This object is available
in API version 62.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AggregateFunction

EngagementSignalId

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Defines the type of calculation used on the metric field.

Possible values are:

**•** `Avg`

**•** `Count`

**•** `Distinct`

**•** `Select`

**•** `Sum`

The default value is `Count` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. Represents the ID of the engagement signal that’s associated with the metric.

This field is a relationship field.

**Relationship Name**
### EngagementSignal

**Relationship Type**
Master-detail

**Refers To**
EngagementSignal (the master object)


### Standard Objects EnhancedLetterhead

**Field** **Details**

```
IsRemote

LastReferencedDate

LastViewedDate

Name

```

Usage

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates if the engagement signal metric object is owned by a different org in Data 360.

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp that indicates the last time the engagement signal metric was referenced by the
current user.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp that indicates the last time the current user viewed the engagement signal metric
record.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Required. Text label that identifies the engagement signal metric.

These derived metrics serve as the core unit of measurement across the personalization platform. Use them to train machine learning
models, measure performance in A/B tests, track outcomes in attribution models, and define custom objectives or compound metrics.

### EnhancedLetterhead

Represents an enhanced letterhead that can be associated with a Lightning email template that doesn’t use the Salesforce Merge
Language (SML). This object is available in API version 46.0 and later.


Standard Objects EnhancedLetterhead

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `describeLayout()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Description

LastReferencedDate

LastViewedDate

LetterheadFooter

LetterheadHeader

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the contents of the header and footer.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when this enhanced letterhead was last used.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when this enhanced letterhead was last viewed.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The contents of the enhanced letterhead’s footer.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The contents of the enhanced letterhead’s header.


### Standard Objects Entitlement

**Field** **Details**

```
Name

```

Associated Objects

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the enhanced letterhead, such as Standard Company Letterhead.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**EnhancedLetterheadFeed**

Feed tracking is available for the object.

### Entitlement

Represents the customer support an account or contact is eligible to receive. This object is available in API version 18.0 and later.
### Entitlements may be based on an asset, product, or service contract.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AccountId

AssetId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the Account associated with the entitlement.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Required. ID of the Asset associated with the entitlement. Must be a valid asset ID.


Standard Objects Entitlement

**Field** **Details**

```
AssetWarrantyID

BusinessHoursId

CasesPerEntitlement

ContractLineItemId

EndDate

IsPerIncident

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The identifier of the asset warranty record. Must be a valid asset warranty ID.
AssetWarranty is available only with Field Service.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Required. ID of the BusinessHours associated with the entitlement. Must be a valid
business hours ID.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of cases the entitlement supports.

This field is only available if `IsPerIncident` is `true` .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Required. ID of the ContractLineItem associated with the entitlement. Must be a valid
ID.

**Type**
date

**Properties**
Create, Filter, Nillable, Update

**Description**
The last day the entitlement is in effect.

**Type**
boolean


Standard Objects Entitlement

**Field** **Details**

**Properties**
Defaulted on create, Filter, Update

**Description**
Indicates whether the entitlement is limited to supporting a specific number of cases
( `true` ) or not ( `false` ).

```
LastReferencedDate

LastViewedDate

LocationID

Name

SvcApptBookingWindowsId

```

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp when the current user last accessed this record, a record related to
this record, or a list view.

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp when the current user last viewed this record or list view. If this value
is null, the user might have only accessed this record or list view
( `LastReferencedDate` ) but not viewed it.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Location associated with the entitlement. Must be a valid location ID.

**Type**
string

**Properties**
Create, Filter, Update

**Description**
Required. Name of the entitlement.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Nillable, Update


Standard Objects Entitlement

**Field** **Details**

**Description**
The operating hours that the entitlement’s work orders should respect. The label in
the user interface is `Operating Hours` . Available only if Field Service is enabled.

```
RemainingCases

RemainingWorkOrders

ServiceContractId

SlaProcessId

StartDate

```

**Type**
int

**Properties**
Create, Filter, Nillable, Update

**Description**
The number of cases the entitlement can support. This field decreases in value by
one each time a case is created with the entitlement.

This field is only available if `IsPerIncident` is selected.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of agreed work orders remaining to be created.

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
Required. ID of the ServiceContract associated with the entitlement. Must be a valid
ID.

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the SlaProcess associated with the entitlement. This field is available in version
19.0 and later.

**Type**
date

**Properties**
Create, Filter, Nillable, Update

**Description**
The first date the entitlement is in effect.


Standard Objects Entitlement

**Field** **Details**

```
Status

SvcApptBookingWindows

Type

WorkOrdersPerEntitlement

```

Associated Objects

**Type**
picklist

**Properties**
Filter, Nillable

**Description**
Status of the entitlement, such as `Expired` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Nillable, Update

**Description**
The operating hours of the entitlement. This field is visible only if Field Service is
enabled.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Nillable, Update

**Description**
The type of entitlement, such as Web or phone support.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Total number of work orders available for this entitlement.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**EntitlementChangeEvent (API version 44.0)**
Change events are available for the object.

**EntitlementFeed (API version 23.0)**
Feed tracking is available for the object.


### Standard Objects EntitlementContact

**EntitlementHistory**

History is available for tracked fields of the object.

SEE ALSO:

### EntitlementContact

SlaProcess

### EntitlementContact

Represents a Contact eligible to receive customer support via an Entitlement. This object is available in API version 18.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,

```
   undelete()

```

Fields

**Field** **Details**

```
ContactId

EntitlementId

IsDeleted

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the Contact associated with the entitlement. Must be a valid ID.

**Type**
reference

**Properties**
Create, Filter

**Description**
Required. ID of the Entitlement associated with the entitlement contact. Must be a
valid ID.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not
( `false` ). Label is **Deleted** .


### Standard Objects EntitlementTemplate

**Field** **Details**

```
Name

```

Usage

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Nillable

**Description**
Required. Name of the entitlement contact.

Use to query and manage entitlement contacts.

SEE ALSO:

### Entitlement EntitlementTemplate

Represents predefined terms of customer support for a product (Product2). This object is available in API version 18.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

As of Summer ’20 and later, only Salesforce admins, users with access to the Case, Entitlement, or Work Order objects, and users with
the View Setup and Configuration permission can access this object.

Fields

**Field** **Details**

```
BusinessHoursId

CasesPerEntitlement

```

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the BusinessHours associated with the entitlement template. Must be a valid
business hours ID.

**Type**
int


Standard Objects EntitlementTemplate

**Field** **Details**

**Properties**
Create, Filter, Nillable, Update

**Description**
The total number of cases the entitlement template supports.

This field is only available if `IsPerIncident` is `true` .

```
IsPerIncident

Name

NamespacePrefix

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Update

**Description**
Indicates whether the entitlement template is limited to supporting a specific number
of cases ( `true` ) or not ( `false` ).

**Type**
string

**Properties**
Create, Filter, idLookup, Update

**Description**
Required. Name of the entitlement template.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org
that creates a managed package has a unique namespace prefix. Limit: 15 characters.
You can refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix
of the org for all objects that support it, unless an object is in an installed managed
package. In that case, the object has the namespace prefix of the installed
managed package. This field’s value is the namespace prefix of the Developer
Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only
for objects that are part of an installed managed package. All other objects have
no namespace prefix.

Available in version 34.0 and later.


### Standard Objects EntityHistory

**Field** **Details**

```
SlaProcessId

Term

Type

```

Usage

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the SlaProcess associated with the entitlement template. This field is available
in API version 19.0 and later.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Nillable, Update

**Description**
Number of days that the entitlement template is valid.

**Type**
picklist

**Properties**
Create, Filter, Nillable, Update

**Description**
The type of entitlement template, such as Web or phone support.

Use this object to manage entitlement templates.

### EntityHistory

Represents historical information about an object’s changed field values. This object is only available to users with the “View All Data”
[permission. This object is unavailable beginning with API version 8.0. Use the object-specific Historyobjects instead.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.xml)

Supported Calls

`describeSObjects()`, `getUpdated()`, `getDeleted()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)


Standard Objects EntityHistory

Fields

**Field** **Details**

```
FieldName

IsDeleted

NewValue

OldValue

ParentId

ParentSobjectType

```

**Type**
picklist

**Properties**
Filter, Restricted picklist

**Description**
ID of the standard or custom field.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not
( `false` ). Label is **Deleted** .

**Type**
anyType

**Properties**
Nillable

**Description**
New value of the modified field.

**Type**
anyType

**Properties**
Nillable

**Description**
Previous value of the modified field.

**Type**
reference

**Properties**
Filter

**Description**
ID of the object that contains the field.

**Type**
picklist

**Properties**
Filter, Restricted picklist


### Standard Objects EntityMilestone

**Field** **Details**

**Description**
The kind of object that contains the field.

Usage

In API version 7.0 and later, this object works with Case, Contract, and Solution objects:

**•** This object is always read-only in the online application.

**•** When a field is modified, this object records both the old and new field values. There are exceptions to this behavior for certain fields
such as long text areas and multi-select picklists. These fields appear in this object to indicate that the field was changed, but the
old and new values are not recorded.

**•** Two rows are added to this object when foreign key fields change. One row contains the foreign key object names that display in
the online application. For example, “Jane Doe” is recorded as the name of a contact. The other row contains the actual foreign key
ID that is only returned to and visible from the API.

**•** Up to a total of twenty fields (standard or custom) can be tracked for a given object.

**•** In the online application, you can specify which fields are tracked or not tracked at any time.

**•** As soon as tracking is turned on for a field, all changes to its value are recorded in the database.

**•** Turning off tracking for a field stops further changes from being recorded, but the history data is not deleted.

**•** Be advised that deleting a custom field also permanently deletes the history data for that custom field.

### EntityMilestone

Represents a required step in a customer support process on a work order. The Salesforce user interface uses the term “object milestone.
This object is available in API version 37.0 and later.

Note: Milestones on cases use the CaseMilestone object type.

Supported Calls

`delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`,

```
   update()

```

Special Access Rules

**•** As of Summer ’20 and later, only Salesforce admins, users with access to the Case, Entitlement, or Work Order objects, and users with
the View Setup and Configuration permission can access this object.

**•** Entitlement management must be enabled.

**•** Work orders or Field Service must be enabled.


Standard Objects EntityMilestone

Fields

**Field Name** **Details**

```
ActualElapsedTimeInDays

ActualElapsedTimeInHrs

ActualElapsedTimeInMins

BusinessHoursId

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of days that it took to complete a milestone. (Elapsed Time) –
(Stopped Time) = (Actual Elapsed Time)

Note: To display this field, select **Enable stopped time and actual**
**elapsed time** on the Entitlement Settings page and add the field to the
object milestone page layout.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of hours that it took to complete a milestone. (Elapsed Time) –
(Stopped Time) = (Actual Elapsed Time)

Note: To display this field, select **Enable stopped time and actual**
**elapsed time** on the Entitlement Settings page and add the field to the
object milestone page layout.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of minutes that it took to complete a milestone. (Elapsed Time) –
(Stopped Time) = (Actual Elapsed Time)

Note: To display this field, select **Enable stopped time and actual**
**elapsed time** on the Entitlement Settings page and add the field to the
object milestone page layout.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects EntityMilestone

**Field Name** **Details**

**Description**
The business hours on the milestone. If business hours aren’t specified, the
entitlement process business hours are used. If business hours are also not
specified on the entitlement process, the business hours on the record are used.

```
CompletionDate

CurrencyIsoCode

ElapsedTimeInDays

ElapsedTimeInHrs

ElapsedTimeInMins

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort, Update

**Description**
The date and time the milestone was completed.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of days it took to complete a milestone, including time during which
the milestone was stopped. Automatically calculated to include the business
hours on the record. Elapsed time is calculated only after the Completion Date
field is populated. (Elapsed Time) – (Stopped Time) = (Actual Elapsed Time).

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of hours it took to complete a milestone, including time during
which the milestone was stopped. Automatically calculated to include the
business hours on the record. Elapsed time is calculated only after the Completion
Date field is populated. (Elapsed Time) – (Stopped Time) = (Actual Elapsed Time).

**Type**
int


Standard Objects EntityMilestone

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of minutes it took to complete a milestone, including time during
which the milestone was stopped. Automatically calculated to include the
business hours on the record. Elapsed time is calculated only after the Completion
Date field is populated. (Elapsed Time) – (Stopped Time) = (Actual Elapsed Time).

```
IsCompleted

IsViolated

MilestoneTypeId

Name

ParentEntityId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Green checkmark icon that indicates a milestone completion.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Red exclamation point icon that indicates a milestone violation.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The ID of the milestone (for instance, First Response).

**Type**
string

**Properties**
Filter, Group, Sort, Update

**Description**
The name of the milestone.

**Type**
reference

**Properties**
Filter, Group, Sort


Standard Objects EntityMilestone

**Field Name** **Details**

**Description**
The ID of the record—for example, a work order—that contains the milestone.

```
SlaProcessId

StartDate

StoppedTimeInDays

StoppedTimeInHrs

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The entitlement process associated with the milestone.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort, Update

**Description**
The date and time that milestone tracking started.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of days that an agent has been blocked from completing a milestone.
For example, an agent may be waiting for a customer to reply with more
information.

Note: To display this field, select **Enable stopped time and actual**
**elapsed time** on the Entitlement Settings page and add the field to the
object milestone page layout.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of hours that an agent has been blocked from completing a
milestone. For example, an agent may be waiting for a customer to reply with
more information.

Note: To display this field, select **Enable stopped time and actual**
**elapsed time** on the Entitlement Settings page and add the field to the
object milestone page layout.


Standard Objects EntityMilestone

**Field Name** **Details**

```
StoppedTimeInMins

TargetDate

TargetResponseInDays

TargetResponseInHrs

TargetResponseInMins

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of minutes that an agent has been blocked from completing a
milestone. For example, an agent may be waiting for a customer to reply with
more information.

Note: To display this field, select **Enable stopped time and actual**
**elapsed time** on the Entitlement Settings page and add the field to the
object milestone page layout.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time to complete the milestone.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of days to complete the milestone. Automatically calculated to
include the business hours on the record.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of hours to complete the milestone. Automatically calculated to
include the business hours on the record.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of minutes to complete the milestone. Automatically calculated to
include the business hours on the record.


Standard Objects EntityMilestone

**Field Name** **Details**

```
TimeRemainingInDays

TimeRemainingInHrs

TimeRemainingInMins

TimeSinceTargetInDays

TimeSinceTargetInHrs

TimeSinceTargetInMins

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The days that remain before a milestone violation. Automatically calculated to
include the business hours on the record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The hours that remain before a milestone violation. Automatically calculated to
include the business hours on the record.

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
The minutes that remain before a milestone violation. Automatically calculated
to include the business hours on the record.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The days that have elapsed since a milestone violation. Automatically calculated
to include the business hours on the record.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The hours that have elapsed since a milestone violation. Automatically calculated
to include the business hours on the record.

**Type**
string


### Standard Objects EntitySubscription

**Field Name** **Details**

**Properties**
Group, Nillable, Sort

**Description**
The minutes that have elapsed since a milestone violation. Automatically
calculated to include the business hours on the record.

Usage

When you create an entitlement process, you select its type based on the type of record that you want the process to run on: Case or
Work Order. Processes created before Summer ’16 use the Case type. When a Work Order entitlement process runs on a work order, the
resulting milestones on the work order are object milestones. Conversely, when a Case entitlement process runs on a case, the resulting
milestones are case milestones, a separate standard object.

Tip: If an entitlement has an entitlement process associated with it, don’t use the entitlement for multiple types of support records.
An entitlement process works only on records that match the process’s type. For example, when a Case entitlement process is
applied to an entitlement, the process runs only on cases associated with that entitlement. If a work order is also associated with
the entitlement, the process doesn’t run on the work order. To ensure that the milestones you set up work as expected, associate
a customer’s work orders and cases with different entitlements.

Customize page layouts, validation rules, and more for object milestones from the Object Milestones node in Setup under Entitlement
Management.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**EntityMilestoneFeed**

Feed tracking is available for the object.

**EntityMilestoneHistory**

History is available for tracked fields of the object.

### EntitySubscription

Represents a subscription for a user following a record or another user. This object is available in API version 34.0 and later.

A user can subscribe to a record or to another user. Changes to the record and updates from the users are displayed in the Chatter feed
on the user's home page, which is a useful way to stay up-to-date with other users and with changes made to records in Salesforce.
Feeds are available in API version 18.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`


Standard Objects EntitySubscription

Fields

**Field** **Details**

```
NetworkId

ParentId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the Experience Cloud site where the user is following the record or user. This field is
available in API version 26.0 and later, if digital experiences is enabled for your org.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the record or user which the user is following.

This is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Account, Accreditation, ActivationTarget, ActivationTrgtIntOrgAccess, ApiAnomalyEventStore,
AssessmentIndicatorDefinition, AssessmentTask, AssessmentTaskContentDocument,
AssessmentTaskDefinition, AssessmentTaskIndDefinition, AssessmentTaskOrder, Asset,
AssetRelationship, AssignedResource, Award, BoardCertification, BusinessLicense,
BusinessMilestone, BusinessProfile, Campaign, CareBarrier, CareBarrierDeterminant,
CareBarrierType, CareDeterminant, CareDeterminantType, CareDiagnosis,
CareInterventionType, CareMetricTarget, CareObservation, CareObservationComponent,
CarePgmProvHealthcareProvider, CarePreauth, CarePreauthItem, CareProgram,
CareProgramCampaign, CareProgramEligibilityRule, CareProgramEnrollee,
CareProgramEnrolleeProduct, CareProgramEnrollmentCard, CareProgramGoal,
CareProgramProduct, CareProgramProvider, CareProgramTeamMember,
CareProviderAdverseAction, CareProviderFacilitySpecialty, CareProviderSearchableField,
CareRegisteredDevice, CareRequest, CareRequestDrug, CareRequestExtension,
CareRequestItem, CareSpecialty, CareSpecialtyTaxonomy, CareTaxonomy, Case, CodeSet,
CollaborationGroup, CommSubscription, CommSubscriptionChannelType,
CommSubscriptionConsent, CommSubscriptionTiming, ConsumptionSchedule, Contact,
ContactEncounter, ContactEncounterParticipant, ContentDocument, Contract,
CoverageBenefit, CoverageBenefitItem, CredentialStuffingEventStore, CreditMemo,
CreditMemoLine, Dashboard, DashboardComponent, DataStream, DelegatedAccount,
DocumentChecklistItem, EngagementChannelType, EnhancedLetterhead,
EnrollmentEligibilityCriteria, Event, HealthcareFacility, HealthcareFacilityNetwork,
HealthcarePayerNetwork, HealthcarePractitionerFacility, HealthcareProvider,


Standard Objects EntitySubscription

**Field** **Details**

HealthcareProviderNpi, HealthcareProviderSpecialty, HealthcareProviderTaxonomy, Identifier,
Image, IndividualApplication, Invoice, InvoiceLine, Lead, Location, MarketSegment,
MarketSegmentActivation, MemberPlan, MessagingSession, MktCalculatedInsight,
OperatingHours, Opportunity, Order, OrderItem, OtherComponentTask, PartyConsent,
PersonEducation, PersonLanguage, PersonLifeEvent, PersonName, PlanBenefit,
PlanBenefitItem, Product2, ProductFulfillmentLocation, ProductItem, ProductItemTransaction,
ProductRequest, ProductRequestLineItem, ProductRequired, ProductTransfer, ProfileSkill,
ProfileSkillEndorsement, ProfileSkillUser, ProviderSearchSyncLog, PurchaserPlan,
PurchaserPlanAssn, ReceivedDocument, Report, ReportAnomalyEventStore, ResourceAbsence,
ResourcePreference, ReturnOrder, ReturnOrderLineItem, ServiceAppointment, ServiceResource,
ServiceResourceSkill, ServiceTerritory, ServiceTerritoryMember, ServiceTerritoryWorkType,
SessionHijackingEventStore, Shift, Shipment, ShipmentItem, Site, SkillRequirement, SocialPost,
Solution, Task, ThreatDetectionFeedback, Topic, User, Visit, VisitedParty, Visitor, VoiceCall,
VolunteerProject, WorkBadgeDefinition, WorkOrder, WorkOrderLineItem, WorkType,
WorkTypeGroup, WorkTypeGroupMember

```
SubscriberId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the user who is following the record or user.

This is a relationship field.

**Relationship Name**
Subscriber

**Relationship Type**
Lookup

**Refers To**
User

Consider this when following records and users:

**•** Users can only follow records that they can see.

**•** Users can see which records other users are following, unless they don’t have access to the records.

**•** Administrators and users with the “Modify All Data” permission can configure a user to follow records that the user has read access
to.

**•** Administrators and users with the “Modify All Data” permission can configure users to stop following records.

**•** Following topics is available in API version 29.0 and later. For this reason, a topic ID is now a supported value for the `ParentId`
field.

**•** If you deactivate a user, any EntitySubscription where the user is associated with the ParentId or SubscriberId field, meaning all
subscriptions both to and from the user, are soft deleted. If the user is reactivated, the subscriptions are restored. However, if you


### Standard Objects EnvironmentHubMember

deactivate multiple users at once and these users follow each other, their subscriptions are hard deleted. In this case, the user-to-user
EntitySubscription is deleted twice (double deleted). Such subscriptions can’t be restored upon user reactivation.

When using `query()` with EntitySubscription,

**•** Note the following SOQL restriction. No SOQL limit if logged-in user has “View All Data” permission. If not, specify a LIMIT clause of
1,000 records or fewer.

**•** A query using a `WHERE` clause can only filter by fields on the EntitySubscription object.

**•** If user sharing is enabled and the querying user is not an administrator, a SOQL query must be constrained either by the `ParentId`
or `SubscriberId` . Otherwise, the query behavior at run time is undefined, meaning the result set can be incomplete or inconsistent
from invocation to invocation. For an unconstrained query, the sharing check limits imposed on a non-adminstrative user are likely
to be exceeded before the query completes, because access checks are run against both parent and subject, for each row of the
result set. We recommend using the Connect REST API to query EntitySubscription data instead of running a SOQL query.

**•** Users without the “View All Data” permission

**–** Need read access on the object associated with the `ParentId` field to see which users are following records for the object.

**–** Can use an `ORDER BY` clause in a query only to order by fields on the EntitySubscription object. For example, if the subscription
relates to an Account record, the query can `ORDER BY ParentId`, but it can’t `ORDER BY Account.Name` .

**–** Don’t always get all matching subscriptions when running a query. For these users, a query evaluates visibility criteria on a
maximum of 500 records to reduce the prospect of long-running queries. If a user runs a query to see the CEO's subscriptions,
it might scan a large number of records. The query only returns matches within the first 500 records scanned. It is possible that
there are more subscriptions that are visible to the user, but they are not returned. To mitigate this, we recommend using a
`WHERE` clause, if possible, to reduce the scope of the query.

Sample—SOQL

The following SOQL query returns subscriptions for all the accounts that a subscriber is following that have more than 10 employees:

```
   SELECT Id

   FROM EntitySubscription

   WHERE SubscriberId = '005U0000000Rg2CIAS'

   AND ParentId IN (

     SELECT Id FROM Account

     WHERE NumberOfEmployees > 10

   )

   LIMIT 200

```

SEE ALSO:

Custom Object __Feed __Feed

### EnvironmentHubMember

Represents a member organization in the Environment Hub. This object is available in API version 29.0 and later.

[Note: You can create only 20 member orgs per day. If you need to create additional orgs, log a support case in the Salesforce](https://partners.salesforce.com)
[Partner Community. For product, specify](https://partners.salesforce.com) **Platform** . For topic, specify **AppExchange & Managed Packages** .


Standard Objects EnvironmentHubMember

Supported Calls

`delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`

Fields

**Field Name** **Details**

```
Description

DisplayName

EnvironmentHubId

Instance

IsFedIdSsoMatchAllowed

```

**Type**
textarea

**Properties**
Nillable, Update

**Description**
A brief description of this org.

**Type**
string

**Properties**
Filter, Group, Nillable,Sort, Update

**Description**
The name that the user has specified for this member org.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The Org ID of this member’s Environment Hub org.

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the instance where the Environment Hub member org resides.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if single sign-on (SSO) has been enabled based on matching the Federation
ID. The default is `false` .


Standard Objects EnvironmentHubMember

**Field Name** **Details**

```
IsSandbox

MemberEntity

MemberType

Name

OrgEdition

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the member org is a sandbox ( `true` ) or not ( `false` ). This field is available
in API version 36.0 and later.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The unique Org ID of the member org for this record.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of member org for this record. Possible values include `Branch Org`, `Patch`
`Org`, `Release Org`, `Sandbox Org`, `Trialforce Management Org`,
and `Trialforce Source Org` .

Note: Only one member type at a time is stored. Member type is determined
according to this hierarchy: (1) Sandbox, (2) Release, (3) Trialforce Source Org
(TSO), (4) Patch, (5) Branch, and (6) Trialforce Management Org (TMO). For
example, if an org is both a sandbox and a TMO, the value of `MemberType` is
`Sandbox Org` .

**Type**
string

**Properties**
Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the member org for this record.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The org’s edition, for example, Enterprise Edition or Unlimited Edition.


Standard Objects EnvironmentHubMember

**Field Name** **Details**

```
OrgStatus

Origin

SSOMappedUsers

ServiceProviderId

ShouldAddRelatedOrgs

ShouldEnableSSO

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The licensing or creation status of this org. Possible values include `Active`, `Demo`,
`Deleted`, `Free`, `Inactive`, and `Trial` .

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The method by which this org was added to the Environment Hub. Possible values are
`autoDiscovered`, `userAdded`, and `provisioned` .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of mapped users in this member org. This field is available in API
version 36.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The ID of the service provider for this member org. This field is available in API version
36.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Status of the connection of related orgs to the hub. Possible values are `done`,
`notRequested`, `pending`, and `requested` .

**Type**
boolean


### Standard Objects Event

**Field Name** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
If SSO should be enabled when this member org is added. The default is `false` .

```
SsoStatus

SsoUsernameFormula

```

Usage

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
If SSO has been enabled for this org. Possible values are:

**•** `Enabled` —Single sign-on is enabled.

**•** `Disabled` —Single sign-on is disabled.

**•** `Pending` —Single sign-on is in the process of being enabled.

**•** `Failed` —Single sign-on enablement failed. Contact Salesforce support for
assistance.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The custom formula for matching users in the hub and member orgs.

Use this object to access and modify settings of member orgs in the Environment Hub.

### Event

Represents an event in the calendar. In the user interface, event and task records are collectively referred to as activities.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Note:

**•** An EventRelation object can’t be related to a child event, and child events don’t include the invitee related list.

**•** `query()`, `delete()`, and `update()` aren’t allowed with events related to more than one contact in API versions 25.0
and earlier.

**•** `create()` and `update()` aren’t available for read-only fields on Lightning Experience event series.


Standard Objects Event

**•** `upsert()` and `undelete()` aren’t supported for syncing changes made to events through the API using the feature
Lightning Sync.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AcceptedEventInviteeIds

AccountId

```

**Type**
JunctionIdList

**Properties**
Create, Update

**Description**
A string array of contact or lead IDs who accepted this event. This `JunctionIdList` is
linked to the `AcceptedEventRelation` child relationship.

Warning: Adding a `JunctionIdList` field name to the `fieldsToNull`
property deletes all related junction records. This action can’t be undone.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the ID of the related account. The `AccountId` is determined as follows.

If the value of `WhatId` is any of the following objects, then Salesforce uses that object’s
`AccountId` .

**•** Account

**•** Opportunity

**•** Contract

**•** Custom object that’s a child of Account

If the value of the `WhatId` field is any other object, and the value of the `WhoId` field is a
contact object, then Salesforce uses that contact’s `AccountId` . If your org uses Shared
Activities, Salesforce uses the `AccountId` of the primary contact.

Otherwise, Salesforce sets the value of the `AccountId` field to `null` .

For information on IDs, see ID Field Type.

This is a relationship field.

**Relationship Name**
Account


Standard Objects Event

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Account

```
ActivityDate

ActivityDateTime

ClientGuid

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Contains the event’s due date if the `IsAllDayEvent` flag is set to `true` . Doesn’t contain
the event’s latest due date if the `IsAllDayEvent` flag is set to `false` . When
`IsAllDayEvent` flag is set to `true`, use `ActivityDateTime` or `StartDateTime` .
This field is a date field with a timestamp that’s always set to midnight in the Coordinated
Universal Time (UTC) time zone. Don’t attempt to alter the timestamp to account for time
zone differences. Label is **Due Date Only** .

This field is required in API versions 12.0 and earlier if the `IsAllDayEvent` flag is set to
`true` .

The value for this field and `StartDateTime` must match, or one of them must be `null` .

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Contains the event’s due date if the `IsAllDayEvent` flag is set to `false` . The time
portion of this field is always transferred in the Coordinated Universal Time (UTC) time zone.
Translate the time portion to or from a local time zone for the user or the application, as
appropriate. Label is **Due Date Time** .

This field is required in API versions 12.0 and earlier if the `IsAllDayEvent` flag is set to
`false` .

The value for this field and `StartDateTime` must match, or one of them must be `null` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The client globally unique identifier identifies the external API client used to create the event.
Label is **Client GUID** .


Standard Objects Event

**Field** **Details**

```
CurrencyIsoCode

DeclinedEventInviteeIds

Description

Division

DurationInMinutes

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
any currency allowed by the organization.

**Type**
JunctionIdLIst

**Properties**
Create, Update

**Description**
A string array of contact, lead, or user IDs who declined this event. This `JunctionIdList`
is linked to the `DeclinedEventRelation` child relationship.

Warning: Adding a `JunctionIdList` field name to the `fieldsToNull`
property deletes all related junction records. This action can’t be undone.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Contains a text description of the event. Limit: 32,000 characters.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
A logical segment of your organization's data. For example, if your company is organized
into different business units, you could create a division for each business unit, such as “North
America,” “Healthcare,” or “Consulting.” Available only if the organization has the Division
permission enabled.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Contains the event length, in minutes. Even though this field represents a temporal value,
it’s an integer type—not a Date/Time type.


Standard Objects Event

**Field** **Details**

Required in API versions 12.0 and earlier if `IsAllDayEvent` is false.

In API versions 13.0 and later, this field is optional, depending on the following:

**•** If `IsAllDayEvent` is true, you can supply a value for either `DurationInMinutes`
or `EndDateTime` . Supplying values in both fields is allowed if the values add up to
the same amount of time. If both fields are `null`, the duration defaults to one day.

**•** If `IsAllDayEvent` is false, a value must be supplied for either
`DurationInMinutes` or `EndDateTime` . Supplying values in both fields is allowed
if the values add up to the same amount of time.

If the multiday event feature is enabled, then API versions 13.0 and later support values
greater than 1440 for the `DurationInMinutes` field. API versions 12.0 and earlier can’t
access event objects whose `DurationInMinutes` is greater than 1440. For more
information, see **Multiday Events** .

Depending on your API version, errors with the `DurationInMinutes` and
`EndDateTime` fields may appear in different places.

**•** Versions 38.0 and before—Errors always appear in the `DurationInMinutes` field.

**•** Versions 39.0 and later—If there’s no value for the `DurationInMinutes` field, errors
appear in the `EndDateTime` field. Otherwise, they appear in the
`DurationInMinutes` field.

```
EndDate

EndDateTime

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Read-only. Available in API versions 46.0 and later. This field supplies the date value that
appears in the EndDateTime field. This field is a date field with a timestamp that is always
set to midnight in the Coordinated Universal Time (UTC) time zone.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Available in API versions 13.0 and later. The time portion of this field is always transferred in
the Coordinated Universal Time (UTC) time zone. Translate the time portion to or from a
local time zone for the user or the application, as appropriate.

This field is optional, depending on the following:

**•** If `IsAllDayEvent` is true, you can supply a value for either `DurationInMinutes`
or `EndDateTime` . Supplying values in both fields is allowed if the values add up to
the same amount of time. If both fields are `null`, the duration defaults to one day.


Standard Objects Event

**Field** **Details**

**•** If `IsAllDayEvent` is false, a value must be supplied for either
`DurationInMinutes` or `EndDateTime` . Supplying values in both fields is allowed
if the values add up to the same amount of time.

Depending on your API version, errors with the `DurationInMinutes` and
`EndDateTime` fields may appear in different places.

**•** Versions 38.0 and before—Errors always appear in the `DurationInMinutes` field.

**•** Versions 39.0 and later—If there’s no value for the `DurationInMinutes` field, errors
appear in the `EndDateTime` field. Otherwise, they appear in the
`DurationInMinutes` field.

```
EventSubtype

EventWhoIds

GroupEventType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Provides standard subtypes to facilitate creating and searching for events. This field isn’t
updateable.

**Type**
JunctionIdList

**Properties**
Create, Update

**Description**
A string array of contact or lead IDs used to create many-to-many relationships with a shared
event. `EventWhoIds` is available when the shared activities setting is enabled. The first
contact or lead ID in the list becomes the primary `WhoId` if you don’t specify a primary
`WhoId` . If you set the `EventWhoIds` field to null, all entries in the list are deleted and
the value of `WhoId` is added as the first entry.

Warning: Adding a `JunctionIdList` field name to the `fieldsToNull`
property deletes all related junction records. This action can’t be undone.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Read-only. Available in API versions 19.0 and later.

The possible values are:

**•** `0` (Non–group event)—An event with no invitees.

**•** `1` (Group event)—An event with invitees.

**•** `2` (Proposed event)—An event created when a user requests a meeting with a contact,
lead, or person account using the Salesforce user interface. When the user confirms the


Standard Objects Event

**Field** **Details**

meeting, the proposed event becomes a group event. You can’t create, edit, or delete
proposed events in the API. This value is no longer used in API version 41.0 and later.

**•** `3` (IsRecurrence2 Series Pattern)—An event representing a template for a series
recurrence pattern in Lightning Experience. You can't view, create, edit, or delete these
events in the API.

```
IsAllDayEvent

IsArchived

IsChild

IsClientManaged

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the `ActivityDate` field ( `true` ) or the `ActivityDateTime` field
( `false` ) is used to define the date or time of the event. Label is **All-Day Event** . See also
`DurationInMinutes` and `EndDateTime` .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the event has been archived.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the event is a child of another event ( `true` ) or not ( `false` ).

For a child event, you can update `IsReminderSet` and `ReminderDateTime` only.
You can query and delete a child event. If the objects related to the child event are different
from those objects related to the parent event (this difference is possible if you use API
version 25.0 or earlier) and one of the objects related to the child event is deleted, the objects
related to the parent event are updated to ensure data integrity.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the event is managed by an external client. If the value of this field is false,
the event isn’t owned or managed by an external client, and Salesforce can be used to update
it. If the value is true, Salesforce can be used to change only noncritical fields on the event.
Label is **Is Client Managed** .


Standard Objects Event

**Field** **Details**

```
IsGroupEvent

IsPrivate

IsRecurrence

IsRecurrence2

IsRecurrence2Exception

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the event is a group event—that is, whether it has invitees ( `true` ) or not
( `false` ).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether users other than the creator of the event can ( `false` ) or can’t ( `true` )
see the event details when viewing the event user’s calendar. However, users with the View
All Data or Modify All Data permission can see private events in reports and searches, or
when viewing other users’ calendars. Private events can’t be associated with opportunities,
accounts, cases, campaigns, contracts, leads, or contacts. Label is **Private** .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a Salesforce Classic event is scheduled to repeat itself ( `true` ) or only
occurs one time ( `false` ). This field is read-only when updating records, but not when
creating them. If this field value is `true`, then `RecurrenceEndDateOnly`,
`RecurrenceStartDateTime`, `RecurrenceType`, and any recurrence fields
associated with the given recurrence type must be populated. Label is **Create recurring**
**series of events** .

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only. This field is available in API version 44.0 and later. Indicates whether a Lightning
Experience event is scheduled to repeat ( `true` ) or only occurs one time ( `false)` . If this
field value is true, then `Recurrence2PatternText` and
`Recurrence2PatternVersion` must be populated. Label is **Repeat** .

**Type**
boolean


Standard Objects Event

**Field** **Details**

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only. This field is available in API version 44.0 and later. Indicates whether an individual
event in a Lightning Experience event series is different from the rest of the series, making
it an exception. Changes made to the series aren’t made to an event that is an exception.

```
IsRecurrence2Exclusion

IsReminderSet

IsVisibleInSelfService

Location

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only. This field is available in API version 44.0 and later. Indicates when updates to a
Lightning Experience event series recurrence pattern have been made, but affect future
event occurrences only. For past event occurrences, `IsRecurrence2Exclusion` is
set to `true`, excluding past occurrences from the series recurrence pattern.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the activity is a reminder ( `true` ) or not ( `false` ).

To set `IsReminderSet` to `true`, the `ReminderDateTime` field must contain a valid
date and time to trigger the reminder.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether an event associated with an object can be viewed in the Customer Portal
( `true` ) or not ( `false` ). If your org has enabled digital experiences, events marked
`IsVisibleInSelfService` are visible to any external user in the Experience Cloud
site, as long as the user has access to the record the event was created on. This field is available
when

**•** Customer Portal or partner portal is enabled

OR

**•** Digital experiences is enabled and you have Customer Portal or partner portal licenses

**Type**
string


Standard Objects Event

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Contains the location of the event.

```
OwnerId

Recurrence2PatternStartDate

Recurrence2PatternText

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Contains the ID of the user or public calendar who owns the event. Label is **Assigned to ID** .

This is a polymorphic relationship field.

Important: By default, the event is assigned to the user who created it. If the event
is created by the Automated Process user, add a different value for OwnerId. The
Automated Process user isn’t a valid value for the OwnerId field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Calendar, User

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Read-only. This field is available in API version 44.0 and later. Indicates the date and time
when the Lightning Experience event series begins. The time portion of this field is always
transferred in the Coordinated Universal Time (UTC) time zone. Translate the time portion
to or from a local time zone for the user or the application, as appropriate.

**Type**
textarea

**Properties**
Create, Nillable

**Description**
The RRULE that describes the recurrence pattern for Lightning Experience event series.
Supports a subset of the RFC 5545 standard for internet calendaring and scheduling. See the
Event Series section in this topic for usage examples. This field has a maximum length of 512
characters.


Standard Objects Event

**Field** **Details**

This field is available in API version 44.0 and later, and has the `Create` property in API
version 52.0 and later.

```
Recurrence2PatternTimeZone

Recurrence2PatternVersion

RecurrenceActivityId

RecurrenceDayOfMonth

RecurrenceDayOfWeekMask

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is available in API version 44.0 and later. Indicates the time zone in which the
Lightning Experience event series was created or updated. This field uses standard Java
TimeZone IDs. For example, America/Los_Angeles.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort,

**Description**
For internal use only. This field is available in API version 44.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Read-only. Not required on create. Contains the ID of the main record of the Salesforce Classic
recurring event. Subsequent occurrences have the same value in this field.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the day of the month on which the event repeats.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the day or days of the week on which the Salesforce Classic recurring event repeats.
This field contains a bitmask. The values are as follows:

**•** Sunday = `1`


Standard Objects Event

**Field** **Details**

**•** Monday = `2`

**•** Tuesday = `4`

**•** Wednesday = `8`

**•** Thursday = `16`

**•** Friday = `32`

**•** Saturday = `64`

Multiple days are represented as the sum of their numerical values. For example, Tuesday
and Thursday = 4 + 16 = 20.

```
RecurrenceEndDateOnly

RecurrenceInstance

RecurrenceInterval

RecurrenceMonthOfYear

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the last date on which the event repeats. For multiday Salesforce Classic recurring
events, this date is the day on which the last occurrence starts. This field is a date field with
a timestamp that is always set to midnight in the Coordinated Universal Time (UTC) time
zone. Don’t attempt to alter the timestamp to account for time zone differences.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the frequency of the Salesforce Classic event’s recurrence. For example, `2nd` or
`3rd` .

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the interval between Salesforce Classic recurring events.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the month in which the Salesforce Classic recurring event repeats.


Standard Objects Event

**Field** **Details**

```
RecurrenceStartDateTime

RecurrenceTimeZoneSidKey

RecurrenceType

ReminderDateTime

ShowAs

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date and time when the Salesforce Classic recurring event begins. The value
must precede the `RecurrenceEndDateOnly` . The time portion of this field is always
transferred in the Coordinated Universal Time (UTC) time zone. Translate the time portion
to or from a local time zone for the user or the application, as appropriate.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the time zone associated with a Salesforce Classic recurring event. For example,
“UTC-8:00” for Pacific Standard Time.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates how often the Salesforce Classic event repeats. For example, daily, weekly, or every
nth month (where “nth” is defined in `RecurrenceInstance` ).

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Represents the time when the reminder is scheduled to fire, if `IsReminderSet` is set to
`true` . If `IsReminderSet` is set to `false`, then the user may have deselected the
reminder checkbox in the Salesforce user interface, or the reminder has already fired at the
time indicated by the value.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects Event

**Field** **Details**

**Description**
Indicates how this event appears when another user views the calendar: Busy, Out of Office,
or Free. Label is **Show Time As** .

```
StartDateTime

Subject

Type

UndecidedEventInviteeIds

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the start date and time of the event. Available in versions 13.0 and later.

If the Event `IsAllDayEvent` flag is set to true (indicating that it’s an all-day Event), then
the event start date information is contained in the `StartDateTime` field. The time
portion of this field is always transferred in the Coordinated Universal Time (UTC) time zone.
Translate the time portion to or from a local time zone for the user or the application, as
appropriate.

If the Event `IsAllDayEvent` flag is set to false (indicating that it isn’t an all-day event),
then the event start date information is contained in the `StartDateTime` field. The time
portion is always transferred in the Coordinated Universal Time (UTC) time zone. You need
to translate the time portion to or from a local time zone for the user or the application, as
appropriate.

If this field has a value, then `ActivityDate` and `ActivityDateTime` must either
be `null` or match the value of this field.

**Type**
combobox

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The subject line of the event, such as Call, Email, or Meeting. Limit: 255 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the event type, such as Call, Email, or Meeting.

**Type**
JunctionIdList

**Properties**
Create, Update


Standard Objects Event

**Field** **Details**

**Description**
A string array of contact, lead, or user IDs who are undecided about this event. This
`JunctionIdList` is linked to the `UndecidedEventRelation` child relationship.

Warning: Adding a `JunctionIdList` field name to the `fieldsToNull`
property deletes all related junction records. This action can’t be undone.

```
WhatCount

WhatId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Available if your organization has enabled Shared Activities. Represents the count of related
EventRelations pertaining to the `WhatId` . The count of the `WhatId` must be _`1`_ or less.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

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


Standard Objects Event

**Field** **Details**

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
WhoCount

WhoId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Available to organizations that have Shared Activities enabled. Represents the count of
related EventRelations pertaining to the `WhoId` .

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The WhoId represents a human such as a lead or a contact. WhoIds are polymorphic.
Polymorphic means a WhoId is equivalent to a contact’s ID or a lead’s ID. The label is `Name`
`ID` .

If Shared Activities is enabled, the value of this field is the ID of the related lead or primary
contact. If you add, update, or remove the WhoId field, you might encounter problems with
triggers, workflows, and data validation rules that are associated with the record. The label
is `Name ID` .

If the `JunctionIdList` field is used, all `WhoId` s are included in the relationship list.

Beginning in API version 37.0, if the contact or lead ID in the `WhoId` field isn't in the
`EventWhoIds` list, no error occurs and the ID is added to the `EventWhoIds` as the
primary `WhoId` . If `WhoId` is set to null, an arbitrary ID from the existing `EventWhoIds`
list is promoted to the primary position.

This is a polymorphic relationship field.

**Relationship Name**
Who

**Relationship Type**
Lookup

**Refers To**
Contact, Lead


Standard Objects Event

Usage

Use Event to manage calendar appointments.

**Querying and Filtering Events**

Queries on events are denied before they time out if they involve amounts of data that are deemed too large. In such cases, the exception
code `OPERATION_TOO_LARGE` is returned. If you receive `OPERATION_TOO_LARGE`, refactor your query to return or scan a
smaller amount of data.

When querying for events with a specific due date, you must filter on both the `ActivityDateTimeand` and `ActivityDate`
fields. For example to find all events with a due date of February 14, 2003, you need two filters:

**•** One filter with the `ActivityDate` field equal to the Coordinated Universal Time (UTC) time zone on February 14, 2003.

**•** One filter with the `ActivityDate` field greater than or equal to midnight on February 14, 2003 in the user’s local time zone AND
less than or equal to midnight on February 15, 2003 in the user’s local time zone.

Alternatively, in API version 13.0 and later, you can find events with a specific due date by filtering on `StartDateTime` . For example,
to find all events with a due date of February 14, 2003, filter with the `StartDateTime` greater than or equal to midnight on February
14, 2003 in the user's local time zone AND less than or equal to midnight on February 15, 2003 in the user's local time zone.

The `EventId` field of an EventRelation object always points to the master record. An invitee on a group event can query the EventRelation
object to view the master record.

**Multiday Events**

**•** Multiday events are available in API version 13.0 and later. Also, in earlier versions SOQL queries don’t return multiday events.

**•** Multiday events are enabled through the user interface from Setup by entering _`Activity Settings`_ in the `Quick Find`
box, then selecting **Activity Settings** .

**•** If the multiday event feature is enabled, then API versions 13.0 and later support values greater than 1440 for the
`DurationInMinutes` field. API versions 12.0 and earlier can’t access event objects whose `DurationInMinutes` is greater
than 1440.

**•** Multiday events can’t exceed 14 days.

**Event Series and Recurring Events**

In Lightning Experience, events with multiple occurrences are called event series, and are indicated when the `IsRecurrence2` field
is set to `true` . In Salesforce Classic, events with multiple occurrences are called recurring events, and are indicated when the
`IsRecurrence` field is set to `true` . Both fields can’t be set to true for the same event.

**•** Lightning Experience event series are available in API version 44.0 and later as read-only fields. Recurrence patterns, specified by the
Recurrence2PatternText field, are creatable in API version 52.0 and later. Salesforce Classic recurring events are available in API version
7.0 and later. In earlier versions, SOQL queries don’t return any Lightning Experience event series.

**•** After an event is created, you can’t change the values of `IsRecurrence2` or `IsRecurrence` from `true` to `false` or vice
versa.

**•** You can’t set fields associated with `IsRecurrence2` for events where `IsRecurrence` is set to `true`, or vice versa.

**•** For Lightning Experience event series where `IsRecurrence2` is `true`, if you’d like to delete a single or all remaining events,
use the REST API call. For Salesforce Classic recurring events where `IsRecurrence` is `true`, all past and future events in the
series are removed when you delete the recurring event series through the API. However, when you delete the recurring event series
through the user interface, only future occurrences are removed.

**•** For Lightning Experience event series in API version 58.0 and later, when you change a future event, events in the entire series also
change. When you change a past event, `IsRecurrence2Exception` is set to `true` and only that past event changes.


Standard Objects Event

**•** When creating a Salesforce Classic recurring event series, the duration of the event must be 24 hours or less. When the Salesforce
Classic recurring event series is created, you can extend the length of individual occurrences beyond 24 hours if Multiday events are
enabled; see **Multiday Events** .

**•** For Salesforce Classic recurring events, `RecurrenceStartDateTime`, `RecurrenceEndDateOnly`, `RecurrenceType`,
and any properties associated with the given recurrence type (see the Recurrence Field Usage for Salesforce Classic Recurring Events
table) must be populated.

**•** When updating a Salesforce Classic recurring event series, it’s not possible to update the `EventRelation` for the event series
object and the EventRelation for the series object occurrences at the same time.

**•** Lightning Experience event series have no series ID, so it’s not possible to locate other occurrences in the series. In Salesforce Classic
recurring events, you can use `RecurrenceActivityId` to locate other occurrences.

**•** For both Lightning Experience event series and Salesforce Classic recurring events, when a series repeats every day, month, or year,
you can only schedule occurrences one time per day, month, or year. The week option lets you schedule occurrences multiple days
per week.

[Limits for Lightning Experience event series and limits for Salesforce Classic recurring events also apply.](https://help.salesforce.com/s/articleView?id=sales.creating_events_lex.htm&type=5&language=en_US)

**Lightning Experience Event Series and Recurring Events**

Use the `Recurrence2PatternText` field to specify the recurrence pattern for Lightning Experience event series. These recurrence
patterns, called reference rules or RRULES, support a subset of the RFC 5545 standards. This table includes common RRULE examples.

The RRULE defined by `Recurrence2PatternText` supports a subset of the RFC 5545 standard for internet calendaring and
scheduling. Supported RRULE parts include FREQ, BYMONTH, BYMONTHDAY, BYDAY, WKST, BYSETPOS, INTERVAL, UNTIL, and COUNT.

When the event record is saved, the RRULE might be modified to follow the required format:

**•** The RRULE parts are placed in the following order: FREQ, BYMONTH, BYMONTHDAY, BYDAY, WKST, BYSETPOS, INTERVAL, UNTIL, and
COUNT.

**•** Any missing default values are inserted. For example, if the RRULE doesn't include INTERVAL, then `INTERVAL=1` is added.

**•** The RRULE is prefaced with `RRULE:` if that preface is missing.


Standard Objects Event


Standard Objects Event


Standard Objects Event

**Salesforce Classic Event Series and Recurring Events**

This table describes the usage of recurrence fields for Salesforce Classic recurring events. Each recurrence type must have all of its
properties set. All unused properties must be set to null.

**RecurrenceType Value** **Properties** **Example Pattern**

RecursDaily RecurrenceInterval Every second day

RecursEveryWeekday RecurrenceDayOfWeekMask Every weekday - can’t be Saturday or Sunday

RecursMonthly RecurrenceDayOfMonth Every second month, on the third day of the month
RecurrenceInterval

RecursMonthlyNth RecurrenceInterval RecurrenceInstance Every second month, on the last Friday of the month
RecurrenceDayOfWeekMask

RecursWeekly RecurrenceInterval Every three weeks on Wednesday and Friday
RecurrenceDayOfWeekMask

RecursYearly RecurrenceDayOfMonth Every March on the 26th day of the month
RecurrenceMonthOfYear

RecursYearlyNth RecurrenceDayOfWeekMask The first Saturday in every October
RecurrenceInstanceRecurrenceMonthOfYear

**Attendees, Invitees, and Resources**

The field `GroupEventType` indicates that event participants are included on an event. You can add a resource to an event only
when the resource is available. The only attendance status that can be assigned to resources is Accepted. Events can’t be saved when
resources you’ve added aren’t available.

**JunctionIdList**

To create an event using `JunctionIdList`, IDs are pulled from the related contacts and both the event and the `EventRelation`
records are created in one API call. If the `EventRelation` fails, the event is rolled back because it’s all done in a single API call.

```
   public void createEventNew(Contact[] contacts) {

    String[] contactIds = new String[contacts.size()];

    for (int i = 0; i < contacts.size(); i++) {

     contactIds[i] = contacts[i].getID();

    }

    Event event = new Event();

    event.setSubject("New Event");

    event.setEventWhoIds(contactIds);

    SaveResult[] results = null;

    try {

     results = connection.create(new Event[] {

     task

     });

    } catch (ConnectionException ce) {

     ce.printStackTrace();

    }

   }

```

**Syncing Events with Lightning Sync**


### Standard Objects EventLogFile

Attendee statuses (Accepted or Maybe, Declined, or No Response) sync from Microsoft [®] Exchange or Google to Salesforce, but not from
Salesforce to Exchange or Google. Be wary of creating API flows that update attendee status in Salesforce for users set up to sync both
ways. Eventually the original Exchange or Google status overrides the update made in Salesforce.

**Shared Field-Level Security for Event and Task Objects**

Metadata deployments for the Event object must include the field-level security for the Task object. Shared field-level security prevents
each object from changing the field-level security of the associated object.

Metadata deployments that include field-level security for only one of either the Event or Task objects can cause field-level security
changes to the other object that aren't reflected in the metadata.

**•** If field-level security is enabled for one object, then field-level security is enabled for both objects.

**•** If field-level security is disabled for one object, then it's disabled for both objects.

Note: A missing entry in the metadata is treated as field-level security being disabled.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**EventChangeEvent (API version 44.0)**
Change events are available for the object.

**EventFeed (API version 20.0)**
Feed tracking is available for the object.

SEE ALSO:

Overview of Salesforce Objects and Fields

### EventLogFile

Represents event log files for event monitoring. The event monitoring product gathers information about your Salesforce org’s operational
events, which you can use to analyze usage trends and user behavior. This object is available in API version 32.0 and later. The `Interval`
and `Sequence` fields are available only in API version 37.0 and later.

You can interact with event monitoring data by querying fields on the EventLogFile object (like `EventType` and `LogDate` ).
`CreatedDate` tracks when the log file was generated. To view the underlying event data, query the `LogFile` field. The `EventType`
determines the schema of this field. Log files don’t count towards your org’s data or file storage allocations. For more information, see
### EventLogFile Supported Event Types.

Composite requests that include multiple API requests in a single call aren’t supported. In the event of a composite request, EventLogFile
captures only the parent request.

Note: Log data schema for each `EventType` can change. With each new release, use the `LogFileFieldNames` and
`LogFileFieldTypes` fields to validate the schema changes. In the unlikely case in which no log files are generated for 24
hours, contact Salesforce Customer Support.

Tip: Debug and troubleshoot performance issues by correlating logs using the customizable Request Identifier field, available in
all Event Monitoring logs. To correlate logs pertaining to an API request call, set the `X-SFDC-REQUEST-ID` header with a 32
character OTEL compatible TraceId or a 22 -character alphanumeric Id. Using SOQL, search for the Event Monitoring logs with this
RequestId to correlate the logs and see the unit of work performed as a part of the API transaction.


Standard Objects EventLogFile

[For details about event monitoring, see the Trailhead Event Monitoring module.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Special Access Rules

Accessing this object requires View Event Log Files and API Enabled user permissions. Users with View All Data permission can view
event log files.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Note: You can only delete event log file data if you enable the **Delete event monitoring data** setting in Setup.

Fields

**Field** **Details**

```
ApiVersion

EventType

Interval

```

**Type**
double

**Properties**
Filter, Sort

**Description**
The specific API version for this log file. This field is available in API version 30.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The event type—API, Login, Report, URI, and so forth. Use to determine which files were
generated for your org. For the corresponding `LogFile` schema, see EventLogFile
Supported Event Types.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The generation schedule for the event log file. Possible values are:

**•** `Daily`

**•** `Hourly`

This field is available in API version 37.0 and later. This field is available in API version 37.0
and later to customers with hourly Event Log Files.


Standard Objects EventLogFile

**Field** **Details**

```
LogDate

LogFile

LogFileContentType

LogFileFieldNames

LogFileFieldTypes

```

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date and time of the log file’s creation. For daily event log files, tracks usage activity for
a 24-hour period, from 12:00 a.m. to 11:59 p.m. UTC time. For hourly event log files, indicates
the hour in which the log file was generated. For example, for events that occur between
11:00 AM and 12:00 PM on 3/7/2016, this field’s value is 2016-03-07T11:00:00.000Z.

Note: For hourly event log files, we recommend using `CreatedDate` to query
the date and time that an EventLogFile object was created.

**Type**
base64

**Description**
Encoded file data in `.csv` format. The `EventType` field defines the schema for this data.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The content type of the log file; always `.csv` .

**Type**
string

**Properties**
Nillable

**Description**
The ordered list of fields in the log file data.

Note: `LogFileFieldNames` and `LogFileFieldTypes` are specific to
each `EventType` . For example, `LogFileFieldNames` has a different value
for an API `EventType` and a Login `EventType` .

**Type**
string

**Properties**
Nillable

**Description**
The ordered list of field types in the log file data ( `String`, `Id`, and so forth).


#### Standard Objects EventLogFile Supported Event Types

**Field** **Details**

Note: `LogFileFieldNames` and `LogFileFieldTypes` are specific to
each `EventType` . For example, `LogFileFieldTypes` has a different value
for an API `EventType` and a Login `EventType` .

```
LogFileLength

Sequence

```

**Type**
double

**Properties**
Filter, Sort

**Description**
The log file length in bytes. You can use this field to plan storage needs for your log files.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number for the portion of the event log file data captured in an hour. For 24-hour event
log file generation, the value of this field is 0. For hourly event log files, the initial value is 1.
This value increases by 1 when events are added in the same hour after the latest event log
file is created. The value resets to 1 in the subsequent hour. For example, you have activity
between 2:00 and 3:00 PM. Two-log files are generated that contain the event log data for
that hour, with `Sequence` values of 1 and 2. For event log data that occurs at 3:01 PM,
the `Sequence` value resets to 1. This field is available in API version 37.0 and later.

#### EventLogFile Supported Event Types

The `EventType` field in the EventLogFile object supports these events. Some common fields, such as `CPU_TIME` and `RUN_TIME`,
can have null or zero values depending on how the events are generated for a given feature. Sometimes, three quotation marks
appear around event data containing special characters in the CSV file. The third quotation mark is necessary for tools and applications
to parse the field data at the correct field value boundary.

#### EventLogFile Supported Event Types

The `EventType` field in the EventLogFile object supports these events. Some common fields, such as `CPU_TIME` and `RUN_TIME`,
can have null or zero values depending on how the events are generated for a given feature. Sometimes, three quotation marks appear
around event data containing special characters in the CSV file. The third quotation mark is necessary for tools and applications to parse
the field data at the correct field value boundary.

We generate some text messages in quotes, as in "example message". To preserve the original value, we add two more quotes and the
final value looks like """example message""" in the CSV file.

Note: The Apex Unexpected Exception, API Total Usage, CORS Violation Record, CSP Violation, Hostname Redirects, Insecure
External Assets, Login, and Logout events are available in supported Salesforce editions at no additional cost. To purchase the
remaining event types, contact Salesforce.


Standard Objects EventLogFile Supported Event Types

Apex Callout Event Type
Apex Callout events contain details about callouts (external requests) during Apex code execution.

Apex Execution Event Type
Apex Execution events contain details about Apex classes that are used.

Apex Inline Event Type
This event type is reserved for future use. This object is available in API version 66.0 and later.

Apex REST API Event Type
Apex REST API events capture information about every Apex REST API request.

Apex SOAP Event Type
Apex SOAP events contain details about custom SOAP web service calls.

Apex Trigger Event Type
Apex Trigger events contain details about triggers that fire in an organization.

Apex Unexpected Exception Event Type
The Apex Unexpected Exception event type captures information about unexpected exceptions in Apex code execution. This event
type is available in the EventLogFile object in API version 45.0 and later. Unexpected exception information is not captured in the
EventLogFile object with `@IsTest` and anonymous Apex.

API Total Usage
API Total usage events contain details about Platform SOAP API, Platform REST API, and Bulk API requests.

Asynchronous Report Run Event Type
Asynchronous Report Run events are created for reporting requests that are scheduled. This category includes dashboard refreshes,
asynchronous reports, schedule reports, and analytics snapshots.

Aura Request Event Type
Aura Request events contain details of requests to Apex methods from Aura and Lightning web components. For example, you can
benchmark request time or identify the URI of an unsuccessful request.

Blocked Redirect Event Type
Blocked redirect events capture information about blocked redirections from Salesforce to untrusted and malformed URLs. The
Blocked Redirect event type is available in the EventLogFile object in API version 63.0 and later.

Bulk API Event Type
Bulk API events contain details about Bulk API requests.

Bulk API Request Event Type
The Bulk API request event captures when Bulk API requests are received to create a job, update a job, create a batch, update a batch,
and when a job completes.

Bulk API 2.0 Event Type
BulkApi2 events contain details about Bulk API 2.0 requests.

Change Set Operation Event Type
Change Set Operation events contain information from change set migrations.

Composite API Event Type
Composite API events contain details about composite API requests. One composite API event is generated for each composite API
and composite graph API call. This event type is available in API version 64.0 and later.


Standard Objects EventLogFile Supported Event Types

Composite API Subrequest Event Type
Composite API subrequest events contain details about composite API subrequests. One composite API subrequest event is generated
for each subrequest or collated set of subrequests. For example, if a composite API request contains five subrequests and four of the
subrequests are collated, then two composite API subrequest events are generated. This example also applies to composite graph
API. This event type is available in API version 64.0 and later.

Concurrent Long-Running Apex Limit Event Type
Concurrent Long-Running Apex Limit events contain information about long-running concurrent Apex requests in your org that
Salesforce terminated after reaching your org’s concurrency limit. Requests with an established Apex context that execute for 5
seconds are counted towards your org’s limit of concurrent long-running requests. (Asynchronous requests don’t count towards
the limit.) When the long-running requests exceed the org default limit, all new Apex invocation requests are denied. This event
type is available in the EventLogFile object in API version 45.0 and later.

Console Event Type
Console events contain information about the performance and use of Salesforce Consoles. The Console events are logged whenever
a Console tab is opened with a sidebar component. Outside of that, when Console tabs are opened, a regular view record detail
event is served just like in Salesforce Classic.

Content Distribution Event Type
Content Distribution events contain information about content distributions and deliveries to users.

Content Document Link Event Type
Content Document Link events contain sharing information for content documents.

Content Transfer Event Type
Content Transfer events contain information about content transfer events, such as downloads, uploads, and previews. This information
includes events performed on files and attachments to records.

Continuation Callout Summary Event Type
Continuation Callout Summary events contain information about all of the asynchronous callouts performed during a transaction,
their response status codes, execution times, and URL endpoint destinations. This event type is available in the EventLogFile object
in API version 43.0 and later.

CORS Violation Record Event Type
CORS Violation Record events capture information about Cross-Origin Resource Sharing (CORS) violations. Cross-origin requests to
Lightning apps are blocked unless the request comes from a URL listed in your CORS allowlist.

CSP Violation Event Type
CSP violation events capture details about blocked resource requests from Lightning Experience pages based on your content
security policy (CSP). The CSP Violation event type is available in the EventLogFile object in API version 63.0 and later.

Dashboard Event Type
Dashboard events contain details about report requests from dashboards. These requests are triggered by dashboard refreshes,
subscriptions, and filter changes.

Database Save Event Type
Database Save events track when records are created, updated, or deleted. This object is available in API version 63.0 and later.

Document Attachment Downloads Event Type
Document Attachment Downloads events contain details of document and attachment downloads.

External Cross-Org Callout Event Type
External Cross-Org Callout events represent external data callouts via the cross-org adapter for Salesforce Connect. This event type
is available in the EventLogFile object in API version 40.0 and later.


Standard Objects EventLogFile Supported Event Types

External Custom Apex Callout Event Type
External Custom Apex Callout events represent external data callouts via custom adapters for Salesforce Connect. This event type is
available in the EventLogFile object in API version 40.0 and later.

External Data Source Callout Event Type
External Data Source Callout events represent external data callouts via the Salesforce Connect adapters for Amazon DynamoDB
and Amazon Athena. This event type is available in the EventLogFile object in API version 56.0 and later.

External OData Callout Event Type
External OData Callout events represent external data callouts via the OData 2.0 and OData 4.0 adapters for Salesforce Connect. This
event type is available in the EventLogFile object in API version 40.0 and later.

Flow Execution Event Type
Flow Execution events contain information about flows that were executed including details such as total execution time, number
of interviews, and number of errors.

Group Membership Event Type
Group Membership events capture details about changes to public group and queue membership, such as when members are
added to or removed from the public group or queue.

Hostname Redirects Event Type
Hostname Redirect events contain details about blocked and successful redirections for your previous My Domain hostnames. The
Hostname Redirects event type is available in the EventLogFile object in API version 56.0 and later.

Insecure External Assets Event Type
Insecure External Assets events contain information about external assets. External assets include images or videos accessed by users
over an insecure HTTP protocol. The event lists all your Salesforce pages that contain assets hosted insecurely on third-party sites
that users loaded with a Chrome, Firefox, Microsoft Edge, or Safari browser. The `INSECURE_URI` field contains the URI being
used to load the asset insecurely. The Insecure External Assets event type is available in the EventLogFile object in API version 42.0
and later.

Insufficient Access Event Type
Insufficient Access events contain details about errors relating to insufficient account, case, contact, and opportunity record access,
so that you can troubleshoot and resolve access issues for your users.

Invocable Action Event Type
Invocable Action events capture the calls to Salesforce Invocable Actions. This is particularly useful to monitor actions invoked during
Agentforce flows. This event type is available in API versions 64.0 and later.

Knowledge Article View Event Type
Knowledge Article View events contain user activity with your knowledge base.

Lightning Error Event Type
Lightning Error events represent errors that occurred during user interactions with Lightning Experience and the Salesforce mobile
app. This event type is available in the EventLogFile object in API version 39.0 and later.

Lightning Interaction Event Type
Lightning Interaction events track user actions in Lightning Experience and the Salesforce mobile app, such as the user clicking,
tapping, or scrolling on a page. This event type is available in the EventLogFile object in API version 39.0 and later.

Lightning Logger Event Type
Lightning Logger events contain information from observed Lightning component logs. This event type is available in the EventLogFile
object in API version 58.0 and later.


Standard Objects EventLogFile Supported Event Types

Lightning Page View Event Type
Lightning Page View events represent information about the page on which the event occurred in Lightning Experience and the
Salesforce mobile app, such as the page's load time. This event type is available in the EventLogFile object in API version 39.0 and
later.

Lightning Performance Event Type
Lightning Performance events track trends in Lightning Experience and Salesforce mobile app performance. This event type is
available in the EventLogFile object in API version 39.0 and later.

Login Event Type
Login events contain details about your org’s user login history.

Login As Event Type
Login As events contain details about what a Salesforce admin did while logged in as another user.

Logout Event Type
Contains details of user sessions ending or being revoked.

Metadata API Operation Event Type
Metadata API Operation events contain details of Metadata API retrieval and deployment requests.

Multiblock Report Event Type
Multiblock Report events contain details about Joined Report reports.

Named Credential Event Type
The Named Credential event type captures information about Apex callouts that use named credentials as their endpoints. Use this
event type to audit the installed managed packages that use named credentials. If you don’t recognize the package namespace in
the named credential event log file, then you can investigate whether a security breach has occurred. This event type is available in
the EventLogFile object in API version 53.0 and later.

One Commerce Usage Event Type
One Commerce Usage events capture information about your Commerce instance. This event type is available in the EventLogFile
object in API version 51.0 and later.

Package Install Event Type
Package Install events contain details about package installation in the organization.

Permission Update Event Type
Permission update events represent changes to object, field, and user permissions and setup entity access that occur in profiles and
permission sets. The event type also tracks if you clone profiles or change whether session activation is required in permission sets
or permission set groups.

Platform Encryption Event Type
Platform Encryption event contains information about tenant secret and derived encryption key usage. This event type is available
in API versions 41.0 and later.

Pricing Event Type
Pricing events contain information about pricing procedures that were executed, including details such as pricing procedures used,
the pricing APIs, and pricing details and status.

Queued Execution Event Type
Queued Execution events contain details about queued executions—for example, batch Apex.

Report Event Type
Report events contain information about what happened when a user ran a report. This event type includes all activity that's in the
Report Export event type, plus more. For example, it has user activity for reports exported as both Formatted Report and Details Only
output.


Standard Objects EventLogFile Supported Event Types

Report Export Event Type
Report Export events contain details about reports that a user exported. For example, this event type captures when a user exports
a report as Details Only output. But it doesn’t capture reports that users export as Formatted Report or XLSX Detail output. For that
data, see the Report event type.

REST API Event Type
REST API events contain details about REST-specific requests.

Sandbox Event Type
Sandbox events contain details about sandbox copies.

Search Event Type
Search events contain details about the user’s search query. All searches within the app, including Experience Cloud sites, are included.
However, unauthenticated users won’t have a unique Salesforce user ID.

Search Click Event Type
Search Click events contain details about the user’s interaction with the search results in the search results page. Interactions with
search results in the instant result dialog are not recorded by this event. All searches within the app, including Experience Cloud
sites, are included. However, unauthenticated users won’t have a unique Salesforce user ID.

Sites Event Type
Sites events contain details of Site.com requests. Requests can originate from the browser (UI).

SOAP API Event Type
SOAP API events contain details about your org's SOAP API request activity.

Time-Based Workflow Event Type
Time-Based Workflow events contain details about queue activity monitoring.

Transaction Security Event Type
Transaction Security events contain details about policy execution. This event type is supported in API version 55.0 and later.

UI Telemetry Navigation Timing Event Type
UI Telemetry Navigation Timing events capture network performance metrics related to page navigation. The event extends from
[the UI Telemetry Resource Timing Event on page 2413 and includes requests initiated with either the Fetch API or the XMLHttpRequest](https://fetch.spec.whatwg.org/)
[API. This object is available in API version 61.0 and later.](https://xhr.spec.whatwg.org/)

UI Telemetry Resource Timing Event
UI Telemetry Resource Timing events capture network performance metrics related to loading an application’s resources. The event
[includes requests initiated with either the Fetch API or the XMLHttpRequest API. This object is available in API version 61.0 and later.](https://fetch.spec.whatwg.org/)

Unique Query Event Type
Unique Query events capture specific search queries (SOQL), filter IDs, and report IDs that are processed, along with the underlying
database queries (SQL). This event type is available in API versions 64.0 and later.

URI Event Type
URI events contain details about user interaction with the web browser UI.

Visualforce Request Event Type
Visualforce Request events contain details of Visualforce requests. Requests can originate from the browser (UI).

Wave Change Event Type
Wave Change events represent route or page changes made in the CRM Analytics user interface. A Wave Change event type is
captured every time the user opens a new CRM Analytics asset or tab, switches between tabs, or changes dashboard pages. Wave
Change events are logged when opening new tabs and switching back to previously opened tabs.


Standard Objects EventLogFile Supported Event Types

Wave Download Event Type
Wave Download events represent downloads made from lens explorations and dashboard widgets in the CRM Analytics user interface.
A Wave Download event type is captured when a user downloads images ( .png ), Microsoft [®] Excel [®] data ( .xls ), or comma-separated
values ( .csv ) files.

Wave Interaction Event Type
Wave Interaction events represent route or page changes made in the CRM Analytics user interface. A Wave Interaction event type
is captured when a tab is closed. It also collates the interaction statistics over the life of the tab, including total open time, read time,
and so on. These statistics are aggregated as you go to other tabs and return, and logged only once when the tab is closed.

Wave Performance Event Type
Wave Performance events help you track trends in your Analytics performance.

SEE ALSO:

EventLogFile

##### Apex Callout Event Type

Apex Callout events contain details about callouts (external requests) during Apex code execution.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
BOT_IDENTIFIER

BOT_SESSION_IDENTIFIER

CLIENT_IP

CPU_TIME

```

**Type**
string

**Description**
The ID of the bot.

**Type**
string

**Description**
The bot session ID.

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number


Standard Objects EventLogFile Supported Event Types

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

```
EVENT_TYPE

LOGIN_KEY

METHOD

ORGANIZATION_ID

PLANNER_IDENTIFIER

REQUEST_ID

```

**Type**
String

**Description**
The type of event. The value is always `ApexCallout` .

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
String

**Description**
The HTTP method of the callout.

**Example**
For example: `GET`, `POST`, `PUT`, and so on.

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
string

**Description**
The ID of the agent planner.

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .


Standard Objects EventLogFile Supported Event Types

```
REQUEST_SIZE

RESPONSE_SIZE

RUN_TIME

SESSION_KEY

STATUS_CODE

SUCCESS

TIME

TIMESTAMP

```

**Type**
Number

**Description**
The size of the callout request body, in bytes.

**Type**
Number

**Description**
The size of the callout response, in bytes.

**Type**
Number

**Description**
Not used for this event type. Use the `TIME` field instead.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
Number

**Description**
The HTTP status code for the response.

**Type**
Boolean

**Description**
Indicates if the HTTP callout was sent and a response was
returned (1) or not (0).

**Type**
Number

**Description**
The amount of time that the request took in milliseconds (ms).

**Type**
String

**Description**
The access time of Salesforce services in GMT.


Standard Objects EventLogFile Supported Event Types

For example: `20130715233322.670` .

```
TIMESTAMP_DERIVED

TYPE

URI

URI_ID_DERIVED

URL

USER_ID

```

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String

**Description**
The type of Apex callout.

For example: `REST` or `AJAX` .

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
String

**Description**
The callout endpoint URL.

**Example**

```
   www.salesforce.com

```

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`


Standard Objects EventLogFile Supported Event Types

```
USER_ID_DERIVED

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Apex Execution Event Type

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

Apex Execution events contain details about Apex classes that are used.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
BOT_IDENTIFIER

BOT_SESSION_IDENTIFIER

CALLOUT_TIME

CLIENT_IP

```

**Type**
string

**Description**
The ID of the bot.

**Type**
string

**Description**
The bot session ID.

**Type**
Number

**Description**
Time spent waiting on webservice callouts, in milliseconds.

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”. If the user’s session context isn't
available, this field returns a blank value.


Standard Objects EventLogFile Supported Event Types

```
CPU_TIME

DB_TOTAL_TIME

ENTRY_POINT

EVENT_TYPE

EXEC_TIME

IS_LONG_RUNNING_REQUEST

```

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
Number

**Description**
Time (in milliseconds) spent waiting for database processing
in aggregate for all operations in the request. Compare this
field to `CPU_TIME` to determine whether performance issues
are occurring in the database layer or in your own code.

**Type**
String

**Description**
The entry point for this Apex execution.

**Example**

**•** `GeneralCloner.cloneAndInsertRecords`

**•** `VF- /apex/CloneUser`

**Type**
String

**Description**
The type of event. The value is always `ApexExecution` .

**Type**
Number

**Description**
The end-to-end Apex execution time (in milliseconds).

**Type**
Boolean

**Description**
Indicates whether the request is counted against your org’s
concurrent long-running Apex request limit ( `true` ) or not
( `false` ).

Note: Asynchronous Apex jobs (batch, queueable,
scheduled, and future), background processes, and bulk
API requests aren’t counted against the concurrent
long-running limit.


Standard Objects EventLogFile Supported Event Types

```
LOGIN_KEY

NUMBER_SOQL_QUERIES

ORGANIZATION_ID

PLANNER_IDENTIFIER

QUIDDITY

```

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
Number

**Description**
The number of SOQL queries that were executed during the
event.

This value is the aggregate across all namespaces, and can
exceed the per-namespace limits. For test executions, the
aggregate total value across all test methods executed in the
request is used. If you’re using this value to track limit
consumption, consider filtering out test execution quiddities
(indicated by the QUIDDITY field).

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
string

**Description**
The ID of the agent planner.

**Type**
String

**Description**
The type of outer execution associated with this event.

**Example**

**•** `A` –ACS Batch Apex

**•** `B` –Bulk API and Bulk API 2.0

**•** `BA` –Start method of a Batch Apex job

**•** `C` –Scheduled Apex

**•** `CI` –Commerce Integration

**•** `DL`   - Discoverable Login page


Standard Objects EventLogFile Supported Event Types

**•** `E` –Inbound Email Service

**•** `F` –Future

**•** `FC` –Function Callback

**•** `H` –Apex REST

**•** `I` –Invocable Action

**•** `K` –Quick Action

**•** `L` –Lightning

**•** `M` –Remote Action

**•** `P` –Not used in API version 63.0 and later.

**•** `PEPC` –Platform Event Publish Callback

**•** `PI` –Post install script for a managed package

**•** `Q` –Queueable

**•** `QTXF` –Transaction Finalizer for Queueable

**•** `R` –Synchronous uncategorized (which is where all
transactions not specified elsewhere end up)

**•** `S` –QueryLocator Batch Apex (Batch Apex jobs run faster
when the start method returns a QueryLocator object that
doesn't include related records via a subquery. See Batch
[Apex Best Practices in Using Batch Apex.)](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_batch_interface.htm#apex_batch_best_practices)

**•** `TA` –Tests Async

**•** `TD` –Tests Deployment

**•** `TS` –Tests Synchronous

**•** `UD` –Undefined is the default when an event hasn’t been
assigned a more descriptive quiddity.

**•** `V` –Visualforce

**•** `W` –SOAP Webservices

**•** `X` –Execute Anonymous

Note: Implementations of the Process.Plugin interface
use the quiddity value **R** .

```
REQUEST_ID

RUN_TIME

```

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Number


Standard Objects EventLogFile Supported Event Types

**Description**
The amount of time that the request took in milliseconds.

Requests with a value over five seconds are considered
long-running requests for the purposes of the Concurrent
Long-Running Apex Limit.

Note: HTTP callout processing time isn't included when
calculating the 5-second limit. We pause the timer for
the callout and resume it when the callout completes.

```
SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

URI

URI_ID_DERIVED

```

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.


Standard Objects EventLogFile Supported Event Types

```
USER_ID

USER_ID_DERIVED

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Apex Inline Event Type

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

This event type is reserved for future use. This object is available in API version 66.0 and later.

Note: Because this event type is reserved for future use, it captures no data.

##### Apex REST API Event Type

Apex REST API events capture information about every Apex REST API request.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide. For information about](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)
[Apex REST, see Introduction to Apex REST.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_rest_intro.htm)

Fields

**Field** **Details**

```
CLIENT_IP

```

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .


Standard Objects EventLogFile Supported Event Types

```
CONNECTED_APP_ID

CLIENT_NAME

CPU_TIME

DB_BLOCKS

DB_CPU_TIME

DB_TOTAL_TIME

ENTITY_NAME

```

**Type**
String

**Description**
The 15-character ID of the connected app associated with the
API call. For example, `0H4RM00000000Kr0AI` .

**Type**
String

**Description**
The name of the client that’s using Salesforce services.

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
Number

**Description**
Indicates how much activity is occurring in the database. A
high value for this field suggests that adding indexes or filters
on your queries would benefit performance.

**Type**
Number

**Description**
The CPU time in milliseconds to complete the request. Indicates
the amount of activity taking place in the database layer during
the request.

**Type**
Number

**Description**
The time in nanoseconds for a database round trip. Includes
time spent in the JDBC driver, network to the database, and
`DB_CPU_TIME` . Compare this field to `CPU_TIME` to
determine whether performance issues are occurring in the
database layer or in your own code.

**Type**
Set


Standard Objects EventLogFile Supported Event Types

**Description**
API objects that are accessed.

For example: `Account`, `Opportunity`, `Contact`, and
so on.

```
EVENT_TYPE

EXCEPTION_MESSAGE

LOGIN_KEY

MEDIA_TYPE

METHOD

NUMBER_FIELDS

ORGANIZATION_ID

```

**Type**
String

**Description**
The type of event. The value is always `ApexRestApi` .

**Type**
String

**Description**
The returned exception message, used to debug issues. Provide
this message when seeking support.

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
String

**Description**
The media type of the response.

**Type**
String

**Description**
The HTTP method of the request.

For example: `GET`, `POST`, `PUT`, and so on.

**Type**
Number

**Description**
The number of fields or columns, where applicable.

**Type**
Id


Standard Objects EventLogFile Supported Event Types

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

```
QUERY

REQUEST_SIZE

REQUEST_STATUS

REQUEST_ID

RESPONSE_SIZE

```

**Type**
String

**Description**
The data that was queried.

**Type**
Number

**Description**
The size of the callout request body, in bytes.

**Type**
String

**Description**
The status of the request for a page view or user interface
action.

For example:

**•** `S` —Success. Salesforce handled the request successfully.
If an Apex controller throws an exception, this status is also
returned.

**•** `F` —Failure. Typically 4xx or 5xx HTTP codes, such as no
permission to view page, page took too long to render,
page is read-only.

**•** `U` —Undefined

**•** `A` —Authorization Error

**•** `R` —Redirect. Typically a 3xx HTTP code, possibly initiated
by an Apex controller in a Visualforce page.

**•** `N` —Not Found. 404 error.

This field can have a blank value.

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Number


Standard Objects EventLogFile Supported Event Types

**Description**
The size of the callout response, in bytes.

```
ROWS_PROCESSED

RUN_TIME

SESSION_KEY

STATUS_CODE

TIMESTAMP

TIMESTAMP_DERIVED

URI

```

**Type**
Number

**Description**
The number of rows that were processed in the request.

For example: `150` .

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
Number

**Description**
The HTTP status code for the response.

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

```
URI_ID_DERIVED

USER_AGENT

USER_ID

USER_ID_DERIVED

USER_TYPE

```

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
Number

**Description**
The numeric code for the type of client used to make the
request (for example, the browser, application, or API).

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

**Type**
String

**Description**
The category of user license.

Possible values are:

**•** `CsnOnly` —Users whose access to the application is
limited to Chatter. This user type includes Chatter Free and
Chatter moderator users.

**•** `CspLitePortal` —CSP Lite Portal license. Users whose
access is limited because they’re organization customers
and access the application through a customer portal or
an Experience Cloud site.


Standard Objects EventLogFile Supported Event Types

**•** `CustomerSuccess` —Customer Success license. Users
whose access is limited because they’re organization
customers and access the application through a customer
portal.

**•** `Guest` —Users whose access is limited so that your
customers can view and interact with your site without
logging in.

**•** `PowerCustomerSuccess` —Power Customer Success
license. Users whose access is limited because they’re
organization customers and access the application through
a customer portal. Users with this license type can view
and edit data they directly own or data owned by or shared
with users below them in the customer portal role
hierarchy.

**•** `PowerPartner` —Power Partner license. Users whose
access is limited because they’re partners and typically
access the application through a partner portal or site.

**•** `SelfService` —Users whose access is limited because
they’re organization customers and access the application
through a self-service portal.

**•** `Standard` —Standard user license. This user type also
includes Salesforce Platform and Salesforce Platform One
user licenses, and admins for this org.

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Apex SOAP Event Type

Apex SOAP events contain details about custom SOAP web service calls.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
CLASS_NAME

```

**Type**
String

**Description**
The Apex class name. If the class is part of a managed package,
this string includes the package namespace.


Standard Objects EventLogFile Supported Event Types

```
CLIENT_IP

CLIENT_NAME

CPU_TIME

DB_TOTAL_TIME

EVENT_TYPE

LIMIT_USAGE_PERCENT

LOGIN_KEY

```

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
String

**Description**
The name of the client that’s using Salesforce services. This
field is an optional parameter that can be passed in API calls.
If blank, the caller didn't specify a client in the CallOptions
header.

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
Number

**Description**
Time (in milliseconds) spent waiting for database processing
in aggregate for all operations in the request. Compare this
field to `CPU_TIME` to determine whether performance issues
are occurring in the database layer or in your own code.

**Type**
String

**Description**
The type of event. The value is always `ApexSoap` .

**Type**
Number

**Description**
The percentage of Apex SOAP calls that were made against
the organization’s limit.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

```
METHOD_NAME

ORGANIZATION_ID

QUERY

REQUEST_ID

REQUEST_STATUS

```

**Type**
String

**Description**
The name of the calling Apex method.

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The SOQL query, if one was performed.

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
String

**Description**
The status of the request for a page view or user interface
action.

For example:

**•** `S` —Success. Salesforce handled the request successfully.
If an Apex controller throws an exception, this status is also
returned.

**•** `F` —Failure. Typically 4xx or 5xx HTTP codes, such as no
permission to view page, page took too long to render,
page is read-only.

**•** `U` —Undefined


Standard Objects EventLogFile Supported Event Types

**•** `A` —Authorization Error

**•** `R` —Redirect. Typically a 3xx HTTP code, possibly initiated
by an Apex controller in a Visualforce page.

**•** `N` —Not Found. 404 error.

This field can have a blank value.

```
RUN_TIME

SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

URI

```

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

Requests with a value over five seconds are considered
long-running requests for the purposes of the Concurrent
Long-Running Apex Limit.

Note: HTTP callout processing time isn't included when
calculating the 5-second limit. We pause the timer for
the callout and resume it when the callout completes.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String

**Description**
The URI of the page that’s receiving the request.


Standard Objects EventLogFile Supported Event Types

For example: `/home/home.jsp` .

```
URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

USER_TYPE

```

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

**Type**
String

**Description**
The category of user license.

Possible values are:

**•** `CsnOnly` —Users whose access to the application is
limited to Chatter. This user type includes Chatter Free and
Chatter moderator users.

**•** `CspLitePortal` —CSP Lite Portal license. Users whose
access is limited because they’re organization customers
and access the application through a customer portal or
an Experience Cloud site.

**•** `CustomerSuccess` —Customer Success license. Users
whose access is limited because they’re organization
customers and access the application through a customer
portal.

**•** `Guest` —Users whose access is limited so that your
customers can view and interact with your site without
logging in.

**•** `PowerCustomerSuccess` —Power Customer Success
license. Users whose access is limited because they’re
organization customers and access the application through


Standard Objects EventLogFile Supported Event Types

a customer portal. Users with this license type can view
and edit data they directly own or data owned by or shared
with users below them in the customer portal role
hierarchy.

**•** `PowerPartner` —Power Partner license. Users whose
access is limited because they’re partners and typically
access the application through a partner portal or site.

**•** `SelfService` —Users whose access is limited because
they’re organization customers and access the application
through a self-service portal.

**•** `Standard` —Standard user license. This user type also
includes Salesforce Platform and Salesforce Platform One
user licenses, and admins for this org.

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Apex Trigger Event Type

Apex Trigger events contain details about triggers that fire in an organization.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
BOT_IDENTIFIER

BOT_SESSION_IDENTIFIER

CLIENT_IP

```

**Type**
String

**Description**
The ID of the bot.

**Type**
String

**Description**
The bot session ID.

**Type**
String

**Description**
The IP address of the client that is using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.


Standard Objects EventLogFile Supported Event Types

For example: `96.43.144.26` .

```
CPU_TIME

DB_TOTAL_TIME

ENTITY_NAME

EVENT_TYPE

EXEC_TIME

LOGIN_KEY

ORGANIZATION_ID

```

**Type**
Number

**Description**
The CPU time in milliseconds is used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
Number

**Description**
Time (in milliseconds) spent waiting for database processing
in aggregate for all operations in the request. Compare this
field to `CPU_TIME` to determine whether performance issues
are occurring in the database layer or in your own code.

**Type**
String

**Description**
The name of the object affected by the trigger.

**Type**
String

**Description**
The type of event. The value is always `ApexTrigger` .

**Type**
Number

**Description**
The end-to-end Apex execution time (in milliseconds).

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
ID

**Description**
The 15-character ID of the organization.


Standard Objects EventLogFile Supported Event Types

For example: `00D000000000123` .

```
PLANNER_IDENTIFIER

REQUEST_ID

REQUEST_STATUS

RUN_TIME

SESSION_KEY

```

**Type**
String

**Description**
The ID of the agent planner.

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
String

**Description**
The status of the request for a page view or user interface
action.

For example:

**•** `S` —Success. Salesforce handled the request successfully.
If an Apex controller throws an exception, this status is also
returned.

**•** `F` —Failure. Typically 4xx or 5xx HTTP codes, such as no
permission to view page, page took too long to render,
page is read-only.

**•** `U` —Undefined

**•** `A` —Authorization Error

**•** `R` —Redirect. Typically a 3xx HTTP code, possibly initiated
by an Apex controller in a Visualforce page.

**•** `N` —Not Found. 404 error.

This field can have a blank value.

**Type**
Number

**Description**
This field is always null. To view the end-to-end Apex execution
time (in milliseconds), refer to the `EXEC_TIME` field.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

```
TIMESTAMP

TIMESTAMP_DERIVED

TRIGGER_ID

TRIGGER_NAME

TRIGGER_TYPE

```

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . The
timezone is GMT.

**Type**
String

**Description**
The 15-character ID of the trigger that was fired.

**Type**
String

**Description**
For triggers coming from managed packages,
`TRIGGER_NAME` includes a namespace prefix separated
with a `.` character. If no namespace prefix is present, the
trigger is from an unmanaged trigger.

Examples:

**•** `examplePackage.managedExampleTrigger`   Managed trigger from the examplePackage namespace

**•** `unmanagedExampleTrigger`   - Unmanaged trigger

**Type**
String

**Description**
The type of this trigger.


Standard Objects EventLogFile Supported Event Types

**Possible Values**

**•** AfterInsert

**•** AfterUpdate

**•** BeforeInsert

**•** BeforeUpdate

```
URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

USER_TYPE

```

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
ID

**Description**
The 15-character ID of the user who is using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
ID

**Description**
The 18-character case insensitive ID of the user who is using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

**Type**
String

**Description**
The category of user license.

Possible values are:

**•** `CsnOnly` —Users whose access to the application is
limited to Chatter. This user type includes Chatter Free and
Chatter moderator users.

**•** `CspLitePortal` —CSP Lite Portal license. Users whose
access is limited because they’re organization customers


Standard Objects EventLogFile Supported Event Types

and access the application through a customer portal or
an Experience Cloud site.

**•** `CustomerSuccess` —Customer Success license. Users
whose access is limited because they’re organization
customers and access the application through a customer
portal.

**•** `Guest` —Users whose access is limited so that your
customers can view and interact with your site without
logging in.

**•** `PowerCustomerSuccess` —Power Customer Success
license. Users whose access is limited because they’re
organization customers and access the application through
a customer portal. Users with this license type can view
and edit data they directly own or data owned by or shared
with users below them in the customer portal role
hierarchy.

**•** `PowerPartner` —Power Partner license. Users whose
access is limited because they’re partners and typically
access the application through a partner portal or site.

**•** `SelfService` —Users whose access is limited because
they’re organization customers and access the application
through a self-service portal.

**•** `Standard` —Standard user license. This user type also
includes Salesforce Platform and Salesforce Platform One
user licenses, and admins for this org.

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Apex Unexpected Exception Event Type

The Apex Unexpected Exception event type captures information about unexpected exceptions in Apex code execution. This event type
is available in the EventLogFile object in API version 45.0 and later. Unexpected exception information is not captured in the EventLogFile
object with `@IsTest` and anonymous Apex.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
EVENT_TYPE

```

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The type of event. The value is always `ApexUnexpectedException` .

```
EXCEPTION_CATEGORY

EXCEPTION_MESSAGE

EXCEPTION_TYPE

```

**Type**
String

**Description**
The category of the unexpected Apex exception. Provides a breakdown of unhandled
exceptions based on the type. For example, the `LimitException` exception type is
split into subcategories that indicate if you exceeded a limit, such as the total heap size or
CPU time.

Possible values:

**•** Subcategories of `LimitException` that indicate the Apex limit you’ve exceeded.
Examples:

**–** `LimitException: CpuTime` : Maximum CPU time on the Salesforce servers.

**–** `LimitException: HeapSize` : Total heap size.

**–** `LimitException: Queries` : Total number of SOQL queries issued.

**–** `LimitException: QueryRows` : Total number of records retrieved by SOQL
queries.

**–** `LimitException: DmlStatements` : Total number of DML statements
issued.

**–** `LimitException: Callouts` : Total number of callouts (HTTP requests or
web services calls) in a transaction.

[See Execution Governors and Limits for other limits.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_gov_limits.htm)

**•** `CustomException` [: Unhandled custom exception.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_exception_custom.htm)

**•** [An Apex exception that isn’t limit-related; see Exception Class and Built-In Exceptions](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexref.meta/apexref/apex_classes_exception_methods.htm)

This field is available in API version 57.0 and later.

**Example**

```
  LimitException: CpuTime

```

**Type**
Text

**Description**
The exception’s message.

**Example**
Divide by 0

**Type**
String

**Description**
The class type of the unexpected exception.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Example**

```
                   System.MathException

```

```
ORGANIZATION_ID

REQUEST_ID

STACK_TRACE

TIMESTAMP

TIMESTAMP_DERIVED

USER_ID

```

**Type**
Id

**Description**
The 15-character ID of the org.

For example: `00D000000000123` .

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Text

**Description**
The stack trace for the exception.

Note: If the exception is thrown from a managed package, `STACK_TRACE` is
omitted.

**Example**

```
  Class.OpportunityUtility.insert: line 22, column 1

  AnonymousBlock: line 1, column 1

```

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `2024-08-08T06:08:02.755+0000` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone is GMT.

**Type**
Id


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.
For example: `00530000009M943` .

```
USER_ID_DERIVED

```

SEE ALSO:

**Type**
Id

**Description**
The 18-character case-insensitive ID of the user who’s using Salesforce services through the
UI or the API.

For example: `00590000000I1SNIA0` .

EventLogFile Supported Event Types

EventLogFile

##### API Total Usage

API Total usage events contain details about Platform SOAP API, Platform REST API, and Bulk API requests.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

API_CLIENT_CATEGORY

```
API_FAMILY

```

**Type**
String

**Description**
The category of the client making the API request.

Possible values are:

**•** `AGENTFORCE_AGENT` —API request is from an
Agentforce agent.

**•** `EXTERNAL_APPLICATION` —API request is from an
external app defined in the org.

**•** `LIGHTNING_UI` —API request is from the Lightning UI.

**•** `SALESFORCE` —API request is from an internal Salesforce
app or service.

**•** `UNKNOWN` —API request is from an unrecognized category.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The API family. Possible values are `REST`, `SOAP`, `Bulk`, or
`ApexREST` . `ApexREST` indicates Apex REST, Agentforce
Apex REST, or Agentforce AuraEnabled calls.

```
API_RESOURCE

API_VERSION

BOT_IDENTIFIER

BOT_SESSION_IDENTIFIER

CLIENT_IP

CLIENT_NAME

CONNECTED_APP_ID

```

**Type**
String

**Description**
The API method or resource. For example,
`describeSObjects` for SOAP, or

```
   /v21.0/sobjects/Account/001xx000003DGQW
```

for REST.

**Type**
Number

**Description**
The API version. For example, `21.0` .

**Type**
string

**Description**
The ID of the bot.

**Type**
string

**Description**
The bot session ID.

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
String

**Description**
The name of the client making the API request. Includes values
passed via the Sforce-Call-Options header.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The ID of the connected app making the API request.

If the connected app ID includes the prefix _`0H4`_, append it to
the connected app ID in the My Domain URL to access app
details
( `https://` _**`MyDomainName`**_ `.my.salesforce.com/` _**`0H4`**_ `xxxxxxxxxxxx` ).
If, however, the connected app ID uses the prefix _`888`_, contact
Salesforce Customer Support for app details.

```
CONNECTED_APP_NAME

COUNTS_AGAINST_API_LIMIT

ENTITY_NAME

EVENT_TYPE

HTTP_METHOD

ORGANIZATION_ID

```

**Type**
String

**Description**
The name of the connected app making the API request.

**Type**
Boolean

**Description**
Whether the request counted against the API limit ( `true` ) or
not ( `false` ).

**Type**
Set

**Description**
The name of the object accessed by the API request.

For example: `Account`, `Opportunity`, `Contact`, and
so on.

**Type**
String

**Description**
The type of event. The value is always `ApiTotalUsage` .

**Type**
String

**Description**
The HTTP method. For example, `GET` .

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .


Standard Objects EventLogFile Supported Event Types

```
PLANNER_IDENTIFIER

REQUEST_ID

STATUS_CODE

TIMESTAMP

TIMESTAMP_DERIVED

USER_ID

USER_NAME

```

**Type**
string

**Description**
The ID of the agent planner.

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Number

**Description**
The HTTP response status code for the request.

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the API.

For example: `00530000009M943`

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The username of the user who's using Salesforce services
through the API.

##### Asynchronous Report Run Event Type

Asynchronous Report Run events are created for reporting requests that are scheduled. This category includes dashboard refreshes,
asynchronous reports, schedule reports, and analytics snapshots.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
AVERAGE_ROW_SIZE

CLIENT_IP

CPU_TIME

DASHBOARD_ID

```

**Type**
Number

**Description**
The average row size of all rows in the Asynchronous Report
Run event, in bytes. A large average size, coupled with a high
`ROW_COUNT`, can indicate that a user is downloading
information for fraudulent purposes. For example, a salesperson
who downloads all sales leads before departing for a
competitor.

**Example**

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The 15-character ID of the dashboard that was run.

```
DB_TOTAL_TIME

DB_BLOCKS

DB_CPU_TIME

DISPLAY_TYPE

ENTITY_NAME

EVENT_TYPE

```

**Type**
Number

**Description**
The time in nanoseconds for a database round trip. Includes
time spent in the JDBC driver, network to the database, and
`DB_CPU_TIME` . Compare this field to `CPU_TIME` to
determine whether performance issues are occurring in the
database layer or in your own code.

**Type**
Number

**Description**
Indicates how much activity is occurring in the database. A
high value for this field suggests that adding indexes or filters
on your queries would benefit performance.

**Type**
Number

**Description**
The CPU time in milliseconds to complete the request. Indicates
the amount of activity taking place in the database layer during
the request.

**Type**
String

**Description**
The report display type, indicating the run mode of the report.

Possible values are:

**•** `D` —Dashboard

**•** `S` —Show Details

**•** `H` —Hide Details

**Type**
String

**Description**
The name of the object affected by the trigger.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The type of event. The value is always
`AsynchronousReportRun` .

```
LOGIN_KEY

NUMBER_BUCKETS

NUMBER_COLUMNS

NUMBER_EXCEPTION_FILTERS

ORGANIZATION_ID

ORIGIN

```

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
Number

**Description**
The number of buckets that were used in the report.

**Type**
Number

**Description**
The number of columns in the report.

**Type**
Number

**Description**
The number of exception filters that are used in the report.

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The context in which the report executed, such as from a UI
(Classic, Lightning, Mobile), through an API (synchronous,
asynchronous, Apex), or through a dashboard.

**Possible Values**

**•** `ReportOpenedFromMobileDashboard` : Report
executed when a user clicked a dashboard component on
a mobile device and drilled down to a report.


Standard Objects EventLogFile Supported Event Types

**•** `DashboardComponentUpdated` : Report executed
when a user refreshed a dashboard component.

**•** `DashboardComponentPreviewed` : Report
executed from a Lightning dashboard component preview.

**•** `ReportRunUsingSynchronousApi` : Report
executed from a synchronous API.

**•** `ReportRunUsingAsynchronousApi` : Report
executed from an asynchronous API.

**•** `ReportRunUsingApexSynchronousApi` : Report
executed from the synchronous Apex API.

**•** `ReportRunUsingApexAsynchronousApi` : Report
executed from the asynchronous Apex API.

**•** `ReportExported` : Report executed from a printable
view or report export that was not asynchronous nor an
API export.

**•** `ReportRunFromClassic` : Report executed from the
Run Report option of Salesforce Classic.

**•** `ReportRunFromMobile` : Report executed from the
Run Report option of the mobile Salesforce app.

**•** `ReportRunFromLightning` : Report executed from
the Run option in Lightning Experience from a non-mobile
browser.

**•** `ReportRunFromRestApi` : Report executed from the
REST API.

**•** `ReportPreviewed` : Report executed when a user got
preview results while using the report builder.

**•** `ReportScheduled` : Report was scheduled.

**•** `ProbeQuery` : Report executed from a probe query.

**•** `ReportRunFromReportingSnapshot` : Report
executed through Snapshot Analytics.

**•** `ReportExportedAsynchronously` : Report was
exported asynchronously.

**•** `ReportExportedUsingExcelConnector` : Report
was exported using the Excel connector.

**•** `ChartRenderedOnVisualforcePage` : Report
executed from a rendered chart on a VisualForce Page.

**•** `ChartRenderedInEmbeddedAnalyticsApp` :
Report executed from a rendered chart in an embedded
Analytics app.

**•** `ReportRunAndNotificationSent` : Report
executed through the notifications API.

**•** `ChartRenderedOnHomePage` : Report executed from
a rendered chart on the home page.


Standard Objects EventLogFile Supported Event Types

**•** `ReportResultsAddedToWaveTrending` : Report
executed when a user trended a report in CRM Analytics.

**•** `ReportAddedToCampaign` : Report was added from
an Add to Campaign action.

**•** `ReportResultsAddedToEinsteinDiscovery` :
Report executed synchronously from Einstein Discovery.

**•** `Unknown` : Report execution origin is unknown.

**•** `Test` : Report execution resulted from a test.

```
RENDERING_TYPE

REPORT_ID

REPORT_ID_DERIVED

REQUEST_ID

```

**Type**
String

**Description**
Describes the format of the report output in Salesforce Classic.
If the report was exported in Lightning Experience, this field is
blank.

**Possible Values**

**•** `W` : Web (HTML)

**•** `E` : Email

**•** `P` : Printable

**•** `X` : Excel

**•** `C` : Comma-separated values (CSV)

**•** `J` : JavaScript Object Notation (JSON)

**•** `D` : Dummy data

**Type**
Id

**Description**
The 15-character ID of the report that was run.

**Type**
Id

**Description**
The 18-character case insensitive ID of the report that was run.

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .


Standard Objects EventLogFile Supported Event Types

```
REQUEST_STATUS

ROW_COUNT

RUN_TIME

SESSION_KEY

```

**Type**
String

**Description**
The status of the request for a page view or user interface
action.

For example:

**•** `S` —Success. Salesforce handled the request successfully.
If an Apex controller throws an exception, this status is also
returned.

**•** `F` —Failure. Typically 4xx or 5xx HTTP codes, such as no
permission to view page, page took too long to render,
page is read-only.

**•** `U` —Undefined

**•** `A` —Authorization Error

**•** `R` —Redirect. Typically a 3xx HTTP code, possibly initiated
by an Apex controller in a Visualforce page.

**•** `N` —Not Found. 404 error.

This field can have a blank value.

**Type**
Number

**Description**
The number of rows that were processed in the Asynchronous
Report Run event. High row counts, coupled with a high
`AVERAGE_ROW_SIZE`, can indicate that a user is
downloading information for fraudulent purposes. For example,
a salesperson who downloads all sales leads before departing
for a competitor.

**Example**

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .


Standard Objects EventLogFile Supported Event Types

```
SORT

TIMESTAMP

TIMESTAMP_DERIVED

URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

```

**Type**
String

**Description**
The sort column and order that was used in the report.

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.


Standard Objects EventLogFile Supported Event Types

For example: `00590000000I1SNIA0` .

```
USER_TYPE

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

**Type**
String

**Description**
The category of user license.

Possible values are:

**•** `CsnOnly` —Users whose access to the application is
limited to Chatter. This user type includes Chatter Free and
Chatter moderator users.

**•** `CspLitePortal` —CSP Lite Portal license. Users whose
access is limited because they’re organization customers
and access the application through a customer portal or
an Experience Cloud site.

**•** `CustomerSuccess` —Customer Success license. Users
whose access is limited because they’re organization
customers and access the application through a customer
portal.

**•** `Guest` —Users whose access is limited so that your
customers can view and interact with your site without
logging in.

**•** `PowerCustomerSuccess` —Power Customer Success
license. Users whose access is limited because they’re
organization customers and access the application through
a customer portal. Users with this license type can view
and edit data they directly own or data owned by or shared
with users below them in the customer portal role
hierarchy.

**•** `PowerPartner` —Power Partner license. Users whose
access is limited because they’re partners and typically
access the application through a partner portal or site.

**•** `SelfService` —Users whose access is limited because
they’re organization customers and access the application
through a self-service portal.

**•** `Standard` —Standard user license. This user type also
includes Salesforce Platform and Salesforce Platform One
user licenses, and admins for this org.


Standard Objects EventLogFile Supported Event Types

##### Aura Request Event Type

Aura Request events contain details of requests to Apex methods from Aura and Lightning web components. For example, you can
benchmark request time or identify the URI of an unsuccessful request.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
ACTION_MESSAGE

CLIENT_IP

CPU_TIME

DB_TOTAL_TIME

EASY_SUITE_VALUE

```

**Type**
String

**Description**
The action (Apex method) names and times for all the actions
in the request in the format:

```
   action1Name=action1Time;action2Name=action2Time...

```

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
Number

**Description**
The time in nanoseconds for a database round trip. Includes
time spent in the JDBC driver, network to the database, and
`DB_CPU_TIME` . Compare this field to `CPU_TIME` to
determine whether performance issues are occurring in the
database layer or in your own code.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The org’s Small Business Suite Edition, if applicable. This field
populates only for Small Business Suite editions and Salesforce
Foundations. Otherwise, it will be empty. Available in API
version 66.0 and later.

For example:

**•** `Freemium` —Salesforce Free Suite

**•** `Starter` —Salesforce Starter Suite

**•** `Pro` —Salesforce Pro Suite

**•** `C360SuiteEE` —Salesforce Foundations

```
EVENT_TYPE

LOGIN_KEY

ORGANIZATION_ID

REQUEST_ID

REQUEST_METHOD

```

**Type**
String

**Description**
The type of event. The value is always `AuraRequest` .

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Example**

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
String

**Description**
The HTTP method of the request, such as GET or POST.


Standard Objects EventLogFile Supported Event Types

```
REQUEST_STATUS

RUN_TIME

SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

```

**Type**
String

**Description**
The status of the request for a page view or user interface
action.

For example:

**•** `S` —Success. Salesforce handled the request successfully.
If an Apex controller throws an exception, this status is also
returned.

**•** `F` —Failure. Typically 4xx or 5xx HTTP codes, such as no
permission to view page, page took too long to render,
page is read-only.

**•** `U` —Undefined

**•** `A` —Authorization Error

**•** `R` —Redirect. Typically a 3xx HTTP code, possibly initiated
by an Apex controller in a Visualforce page.

**•** `N` —Not Found. 404 error.

This field can have a blank value.

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime


Standard Objects EventLogFile Supported Event Types

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

```
URI

URI_ID_DERIVED

USER_AGENT

USER_ID

USER_ID_DERIVED

USER_TYPE

```

**Type**
String

**Description**
The URI of the resource that’s receiving the request.

For example: `/aura` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
String

**Description**
The numeric code for the type of client used to make the
request (for example, the browser, application, or API).

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

**Type**
String

**Description**
The category of user license.

Possible values are:


Standard Objects EventLogFile Supported Event Types

**•** `CsnOnly` —Users whose access to the application is
limited to Chatter. This user type includes Chatter Free and
Chatter moderator users.

**•** `CspLitePortal` —CSP Lite Portal license. Users whose
access is limited because they’re organization customers
and access the application through a customer portal or
an Experience Cloud site.

**•** `CustomerSuccess` —Customer Success license. Users
whose access is limited because they’re organization
customers and access the application through a customer
portal.

**•** `Guest` —Users whose access is limited so that your
customers can view and interact with your site without
logging in.

**•** `PowerCustomerSuccess` —Power Customer Success
license. Users whose access is limited because they’re
organization customers and access the application through
a customer portal. Users with this license type can view
and edit data they directly own or data owned by or shared
with users below them in the customer portal role
hierarchy.

**•** `PowerPartner` —Power Partner license. Users whose
access is limited because they’re partners and typically
access the application through a partner portal or site.

**•** `SelfService` —Users whose access is limited because
they’re organization customers and access the application
through a self-service portal.

**•** `Standard` —Standard user license. This user type also
includes Salesforce Platform and Salesforce Platform One
user licenses, and admins for this org.

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Blocked Redirect Event Type

Blocked redirect events capture information about blocked redirections from Salesforce to untrusted and malformed URLs. The Blocked
Redirect event type is available in the EventLogFile object in API version 63.0 and later.

This event is free for all customers with a 24-hour data retention period. The blocked redirects event is available in the API but not in the
Event Monitoring Analytics app.

[For details about event monitoring, see the Trailhead Event Monitoring module or the REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Blocked redirect events capture these redirections when the target URL isn’t a RedirectWhitelistUrl or when the target URL fails a syntax
check.


Standard Objects EventLogFile Supported Event Types

**•** An anchor link within a page or component that includes a redirection. For example, `<a`

`href="/?startURL=targetUrl">linkText</a>` includes a redirection via the startURL parameter.

**•** A parameter within a page that redirects the user. For example, this form action redirects the user through the saveURL parameter:
`<form action="/xyz?saveURL=targetURL">` .

Within pages and components, a direct anchor link to an external URL is always allowed, even if the target URL isn’t a RedirectWhitelistUrl.
For those direct anchor links, if the target URL fails a syntax check, the user receives an error but the redirection isn’t captured as a blocked
redirect event. An example of a direct anchor link is `<a` `href="targetUrl">linkText</a>` .

For hyperlinks within URL and Long Text Area fields, blocked redirections to untrusted URLs are captured as blocked redirect events only
when the user who clicked the hyperlink accessed Salesforce via Salesforce Classic. If those users see a warning message and can proceed
to the untrusted URL, that event isn’t captured as a blocked redirect event.

Note: To help preserve performance, Salesforce uses throttling, a technique that limits the number of generated blocked redirect
events when the volume is exceptionally high. Therefore, if your org generates a high volume of blocked redirections over a short
period of time, some of those redirections can fail to generate a blocked redirect event.

Fields

**Field** **Details**

```
BLOCKED_URI

BLOCKED_URI_DOMAIN

EVENT_TYPE

MALFORMED_URL

```

**Type**
String

**Description**
The full string of the target for the redirection.

**Example**
https://www.example.com/shop.htm

**Type**
String

**Description**
If `BLOCKED_URI` is a URL, the domain for that URL. To allow future redirections to the
`BLOCKED_URI`, `BLOCKED_URI_DOMAIN` [is the value to add to RedirectWhitelistUrl.](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_redirectwhitelisturl.htm?q=%22Trusted%20URL%22)

**Example**
www.example.com

**Type**
String

**Description**
The type of event. The value is always `BlockedRedirect` .

**Type**
Boolean

**Description**
Indicates whether this redirection was blocked because the target URL failed a syntax check
( `1` ) or not ( `0` ).

Here are examples of malformed URLs.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**•** https://www.example.com/$t61'3

**•** https://malformed^url.example.com

```
ORIGIN

REFERRER

REMOTE_ADDRESS

REQUEST_ID

TIMESTAMP

TIMESTAMP_DERIVED

```

**Type**
String

**Description**
The origin that caused the request to the `BLOCKED_URI` . For example, if a form on an
Experience Cloud Visualforce site page redirects a user to an untrusted URL via the `saveURL`
parameter, `ORIGIN` contains the base URL of that site.

**Type**
String

**Description**
The absolute or partial address from which the request to the `BLOCKED_URI` came. The
`Referrer-Policy` HTTP Header of the request determines how much of the URL is
shared.

**Type**
String

**Description**
Remote IP address of the client making the request.

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

**Example**

```
  0000000062_0000x8Lz
```

**Type**
DateTime

**Description**
The access time of Salesforce services in GMT.

**Example**

```
  20220715233322.670

```

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ). The time zone is always GMT.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Example**

```
                   2022-07-27T11:32:59.555Z.

```

Usage

Only one blocked redirect log file is available at a time. When the daily incremental event log file is generated during the daily background
process, the new file replaces the existing file.

If the log file doesn’t exist, either the log generation process hasn’t run yet or there’s no redirection data to report for that 24-hour
window. The log file is generated only when at least one redirection occurred for the day.

To collect blocked redirect logs for multiple days, schedule a daily query of the Blocked Redirect event type via REST API. For example,
you can configure a cron job in Unix or a scheduled task in Windows to run the query.

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Bulk API Event Type

Bulk API events contain details about Bulk API requests.

Note: This event type does not include Bulk API 2.0 requests. For information about the BulkApi2 event type, see Bulk API 2.0
Event Type on page 2163.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
BATCH_ID

CLIENT_IP

```

**Type**
String

**Description**
The 15-character ID of the Bulk API batch.

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .


Standard Objects EventLogFile Supported Event Types

```
CPU_TIME

ENTITY_TYPE

EVENT_TYPE

JOB_ID

LOGIN_KEY

MESSAGE

NUMBER_FAILURES

OPERATION_TYPE

```

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
String

**Description**
The type of entity that the Bulk API used.

**Type**
String

**Description**
The type of event. The value is always `BulkApi` .

**Type**
String

**Description**
The 15-character ID of the Bulk API job.

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
EscapedString

**Description**
Any success or error message that’s associated with the request.

**Type**
Number

**Description**
The number of failures that were returned with the request.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The type of Bulk API operation that was performed.

```
ORGANIZATION_ID

REQUEST_ID

ROWS_PROCESSED

RUN_TIME

SESSION_KEY

SUCCESS

TIMESTAMP

```

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Number

**Description**
The number of rows that were processed in the request.

For example: `150` .

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
Boolean

**Description**
Whether the batch was successful.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

```
TIMESTAMP_DERIVED

URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .


Standard Objects EventLogFile Supported Event Types

##### Bulk API Request Event Type

The Bulk API request event captures when Bulk API requests are received to create a job, update a job, create a batch, update a batch,
and when a job completes.

Note: This event type doesn’t include Bulk API 2.0 requests. For information about the BulkApi2 event types, see Bulk API 2.0
Event Type on page 2163.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
API_VERSION

BATCH_ID

CLIENT_IP

CLIENT_NAME

CONCURRENCY_MODE

CONNECTED_APP_ID

```

**Type**
Number

**Description**
The API version.

**Type**
String

**Description**
The 15-character ID of the Bulk API batch.

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
EscapedString

**Description**
The name of the client making the request.

**Type**
String

**Description**
The concurrency mode selected by the user.

**Type**
String

**Description**
The ID of the connected app making a request.


Standard Objects EventLogFile Supported Event Types

```
CPU_TIME

ERROR_MESSAGE

EVENT_TYPE

JOB_ID

LOGIN_KEY

OPERATION_TYPE

ORGANIZATION_ID

REQUEST_ID

```

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
EscapedString

**Description**
The type of entity that the Bulk API used.

**Type**
String

**Description**
The type of event. The value is always BulkApiRequest.

**Type**
String

**Description**
The 15-character ID of the Bulk API job.

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
String

**Description**
The type of Bulk API operation.

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

```
REQUEST_PATH

RUN_TIME

SESSION_KEY

STATUS_CODE

SUCCESS

TIMESTAMP

TIMESTAMP_DERIVED

```

**Type**
String

**Description**
The path of the request.

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
Number

**Description**
The HTTP Status code indicating whether the batch was
successful.

**Type**
Boolean

**Description**
Whether the batch was successful.

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime


Standard Objects EventLogFile Supported Event Types

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . The
timezone is GMT.

```
URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

##### Bulk API 2.0 Event Type

```

BulkApi2 events contain details about Bulk API 2.0 requests.

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
Id

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
Id

**Description**
The ID of the user making the request.

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

Note: This event type does not include Bulk API requests. For information about the BulkApi event type, see Bulk API Event Type
on page 2156.

You can monitor the following Bulk API 2.0 parameters:

**•** The type of data processed via Bulk API 2.0 operations, and how much of that data was processed.

**•** Bulk API 2.0 limits.

**•** For jobs, track how long it takes to complete, database, and CPU usage.

**•** Understand users and the operations they performed.

**•** Detailed errors and failures.


Standard Objects EventLogFile Supported Event Types

BulkApi2 events represent the steps in the Bulk API 2.0 workflow and changes in job state.

For a Bulk API 2.0 **Ingest** job, an event is emitted when a job is marked:

**•** created

**–** Note: For multi-part requests, there is no “created” event emitted, only an uploadComplete event.

**•** uploadComplete

**•** inProgress

**•** with a processing update

**•** complete

**•** aborted

**•** deleted

For a Bulk API 2.0 **Query** job, an event is emitted when a job is marked:

**•** created

**•** uploadComplete

**•** inProgress

**•** with a processing update

**•** complete

**•** aborted

**•** deleted

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
CLIENT_IP

CPU_TIME

ENTITY_TYPE

```

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal
IP (such as a login from AppExchange) is shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request. This field indicates
the amount of activity taking place in the app server layer.

**Type**
String

**Description**
The type of entity that Bulk API 2.0 used.


Standard Objects EventLogFile Supported Event Types

For example, `Account` or `Contact` .

```
EVENT_TYPE

JOB_ID

JOB_STATUS

LOGIN_KEY

OPERATION_TYPE

ORGANIZATION_ID

RECORDS_FAILED

RECORDS_PROCESSED

```

**Type**
String

**Description**
The type of event. The value is always `BulkApi2` .

**Type**
String

**Description**
The 15-character ID of the Bulk API 2.0 job.

**Type**
String

**Description**
The job’s current status.

**Type**
String

**Description**
The string that ties together all events in a given user’s login session. It starts with
a login event and ends with either a logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
String

**Description**
The type of Bulk API 2.0 operation that was performed.

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
Number

**Description**
The total number of records that failed.

For example: `150` .

**Type**
Number


Standard Objects EventLogFile Supported Event Types

**Description**
Number of records processed for this event.

For example: `980` .

Note: The number of records processed is reported differently for ingest
and query jobs.

For _ingest_ jobs:

**•** Events with a status of `InProgress` report (if applicable) the number
of records processed.

For _query_ jobs:

**•** Events with a status of `JobComplete` or `InProgress` report (if
applicable) the number of records processed.

```
RESULT_SIZE_MB

REQUEST_ID

RUN_TIME

SESSION_KEY

TIMESTAMP

```

**Type**
Number

**Description**
Number of megabytes returned in query. Empty for ingest jobs.

For example: `670` .

Note: RESULT_SIZE_MB currently does not emit events, but is shown here
as a placeholder for future enhancement.

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain one or more events.
Each event in a given transaction has the same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify all user events
within a session. When a user logs out and logs in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

```
TIMESTAMP_DERIVED

URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

```

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone is GMT.

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case-safe ID of the URI of the page that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or
the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case-safe ID of the user who’s using Salesforce services through
the UI or the API.

For example: `00590000000I1SNIA0` .

##### Change Set Operation Event Type

Change Set Operation events contain information from change set migrations.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)


Standard Objects EventLogFile Supported Event Types

Fields

**Field** **Details**

```
CHANGE_SET_NAME

CLIENT_IP

CPU_TIME

EVENT_TYPE

LOGIN_KEY

OPERATION

```

**Type**
String

**Description**
The name of the change set.

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
String

**Description**
The type of event. The value is always
`ChangeSetOperation` .

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
String

**Description**
The operation that’s being performed.

**Possible Values**

**•** DELETE


Standard Objects EventLogFile Supported Event Types

**•** DEPLOY

**•** UPLOAD

**•** VALIDATE

```
ORGANIZATION_ID

REQUEST_ID

RUN_TIME

SESSION_KEY

TARGET_ORG_ID

TIMESTAMP

```

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
Id

**Description**
The 15-character ID of the organization that’s receiving the
change set.

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .


Standard Objects EventLogFile Supported Event Types

```
TIMESTAMP_DERIVED

URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Composite API Event Type

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

Composite API events contain details about composite API requests. One composite API event is generated for each composite API and
composite graph API call. This event type is available in API version 64.0 and later.


Standard Objects EventLogFile Supported Event Types

Fields

**Field** **Details**

ALL_OR_NONE

CLIENT_IP

CPU_TIME

EVENT_TYPE

FAILURE_REASON

IS_REQUEST_COLLATION_ON

LOGIN_KEY

NUM_GRAPH_DEPTH

**Type**
boolean

**Description**
Indicates whether the entire request is rolled back when the update of any object fails (true),
or if the call should continue with the independent update of other objects in the request
(false). The default is false. If true, it overrides the ALL_OR_NONE setting in subrequests.

**Type**
String

**Description**
The IP address of the client that’s using the API.

**Type**
Number

**Description**
The CPU time in milliseconds to complete the request.

**Type**
String

**Description**
The type of the event. The value is always CompositeApi.

**Type**
String

**Description**
An error code giving the reason for a failed request.

**Type**
boolean

**Description**
The setting for subrequest collation.

**Type**
String

**Description**
Identifies all related events in a given user’s login session. It starts with a login event and
ends with either a logout event or the user session expiring. For example:

```
  GeJCsym5eyvtEK2I

```

**Type**
Number


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The depth of the graph. When multiple graphs are present, this number is the depth of the
deepest graph.

NUM_RETRIES

ORGANIZATION_ID

REQUEST_ID

RUN_TIME

SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

**Type**
Number

**Description**
Number of attempted retries while processing the graph.

**Type**
Id

**Description**
The 15-character ID of the organization that made the request. For example:

```
  00D000000000123

```

**Type**
String

**Description**
A unique ID identifying the composite API request.

**Type**
Number

**Description**
The amount of time in milliseconds to complete the request.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
For example: `20130715233322.670`

**Type**
String

**Description**
The date and time that the event was generated.

**Type**
DateTime

**Description**
The date and time, in ISO8601-compatible format (YYYY-MM-DDTHH:MM:SS.sssZ), that the
event was generated. The timezone is GMT. For example:

```
  2015-07-27T11:32:59.555Z

```


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

SEE ALSO:

**Type**
String

**Description**
The resource URI.

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user that’s using the API. For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user that’s using the API. For example:

```
  00590000000I1SNIA0

```

_[REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_rest.meta/api_rest/resources_composite_composite.htm)_ : Composite

_[REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_rest.meta/api_rest/resources_composite_graph.htm)_ : Composite Graph

_REST API Developer Guide_ [: Using Composite Resources](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_rest.meta/api_rest/using_composite_resources.htm)

##### Composite API Subrequest Event Type

Composite API subrequest events contain details about composite API subrequests. One composite API subrequest event is generated
for each subrequest or collated set of subrequests. For example, if a composite API request contains five subrequests and four of the
subrequests are collated, then two composite API subrequest events are generated. This example also applies to composite graph API.
This event type is available in API version 64.0 and later.

Fields

**Field** **Details**

CANCELLED_REASON

**Type**
String

**Description**
If the subrequest was canceled, shows the reason.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

CLIENT_IP

CPU_TIME

DB_TOTAL_TIME

EVENT_TYPE

INITIAL_REFERENCE_IDS

IS_CANCELLED

LOGIN_KEY

METHOD

**Type**
String

**Description**
The IP address of the client that’s using the API.

**Type**
Number

**Description**
The CPU time in milliseconds to complete the request.

**Type**
Number

**Description**
Time (in nanoseconds) spent waiting for database processing in aggregate for all operations
in the subrequest or set of collated subrequests. Compare this field to CPU_TIME to determine
whether performance issues are occurring in the database layer or in your own code.

**Type**
String

**Description**
The type of the event. The value is always CompositeApiSubrequest.

**Type**
String

**Description**
The original reference IDs of subrequests that were collated into the current subrequest.

**Type**
boolean

**Description**
True if the subrequest call was canceled.

**Type**
String

**Description**
Identifies all related events in a given user’s login session. It starts with a login event and
ends with either a logout event or the user session expiring. For example:

```
  GeJCsym5eyvtEK2I

```

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The HTTP method of the request.

ORGANIZATION_ID

REQUEST_ID

REQUEST_STATUS

RUN_TIME

SESSION_KEY

STATUS_CODE

**Type**
Id

**Description**
The 15-character ID of the organization that made the request. For example:

```
  00D000000000123

```

**Type**
String

**Description**
A unique ID identifying the composite API request.

**Type**
String

**Description**
The status of the subrequest or collated set of subrequests. For example:

**•** S—Success. Salesforce handled the request successfully. If an Apex controller throws an
exception, this status is also returned.

**•** F—Failure. Typically 4xx or 5xx HTTP codes, such as no permission to view page, page
took too long to render, page is read-only.

**•** U—Undefined

**•** A—Authorization Error

**•** R—Redirect. Typically a 3xx HTTP code, possibly initiated by an Apex controller in a
Visualforce page.

**•** N—Not Found. 404 error.

This field can have a blank value.

**Type**
Number

**Description**
The amount of time in milliseconds to complete the request.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
For example: `20130715233322.670`

**Type**
Number


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The HTTP status code for the response.

SUCCESS

TIMESTAMP

TIMESTAMP_DERIVED

URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

**Type**
boolean

**Description**
True if the subrequest call succeeded.

**Type**
String

**Description**
The date and time that the event was generated.

**Type**
DateTime

**Description**
The date and time, in ISO8601-compatible format (YYYY-MM-DDTHH:MM:SS.sssZ), that the
event was generated. The timezone is GMT. For example:

```
  2015-07-27T11:32:59.555Z

```

**Type**
String

**Description**
The resource URI.

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user that’s using the API. For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user that’s using the API. For example:

```
  00590000000I1SNIA0

```


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

USER_TYPE

SEE ALSO:

**Type**
String

**Description**
The category of user license. Possible values are:

**•** CsnOnly—Users whose access to the application is limited to Chatter. This user type
includes Chatter Free and Chatter moderator users.

**•** CspLitePortal—CSP Lite Portal license. Users whose access is limited because they’re
organization customers and they access the application through a customer portal or
an Experience Cloud site.

**•** CustomerSuccess—Customer Success license. Users whose access is limited because
they’re organization customers and they access the application through a customer
portal.

**•** Guest—Users whose access is limited so that your customers can view and interact with
your site without logging in.

**•** PowerCustomerSuccess—Power Customer Success license. Users whose access is limited
because they’re organization customers and they access the application through a
customer portal. Users with this license type can view and edit data that they directly
own or data owned by or shared with users below them in the customer portal role
hierarchy.

**•** PowerPartner—Power Partner license. Users whose access is limited because they’re
partners and they typically access the application through a partner portal or site.

**•** SelfService—Users whose access is limited because they’re organization customers and
they access the application through a self-service portal.

**•** Standard—Standard user license. This user type also includes Salesforce Platform and
Salesforce Platform One user licenses and admins for this org.

_[REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_rest.meta/api_rest/resources_composite_composite.htm)_ : Composite

_[REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_rest.meta/api_rest/resources_composite_graph.htm)_ : Composite Graph

_REST API Developer Guide_ [: Using Composite Resources](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_rest.meta/api_rest/using_composite_resources.htm)

##### Concurrent Long-Running Apex Limit Event Type

Concurrent Long-Running Apex Limit events contain information about long-running concurrent Apex requests in your org that Salesforce
terminated after reaching your org’s concurrency limit. Requests with an established Apex context that execute for 5 seconds are counted
towards your org’s limit of concurrent long-running requests. (Asynchronous requests don’t count towards the limit.) When the
long-running requests exceed the org default limit, all new Apex invocation requests are denied. This event type is available in the
EventLogFile object in API version 45.0 and later.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)


Standard Objects EventLogFile Supported Event Types

Fields

**Field** **Details**

```
EVENT_TYPE

NUMBER_REQUESTS

ORGANIZATION_ID

REQUEST_ID

REQUEST_URI

REQUESTS_LIMIT

```

**Type**
String

**Description**
The type of event. The value is always `ConcurrentLongRunningApexLimit` .

**Type**
Number

**Description**
Count of requests with an established Apex context executing for longer than 5 seconds in
your org.

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
String

**Description**
URI of the long-running Apex request that Salesforce terminated.

**Example**
/apex/ApexClassName

**Type**
Number

**Description**
Maximum count of requests with an established Apex context that can execute for longer
than 5 seconds. When `NUMBER_REQUESTS` reaches this limit, then additional long-running
Apex requests are terminated. (Asynchronous requests don’t count towards the limit.)

See _Apex Developer Guide_ [: Lightning Platform Apex Limits.](https://developer.salesforce.com/docs/atlas.en-us.260.0.apexcode.meta/apexcode/apex_gov_limits.htm#in_topic_non_transactional_gov_limits_section)

**Example**


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
TIMESTAMP

TIMESTAMP_DERIVED

USER_ID

```

Usage

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone is GMT.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.

For example: `00530000009M943`

For example, you can monitor Concurrent Long-Running Apex Limit log counts to get a benchmark or plot a count by hour. To identify
where the limit was exceeded, see the REQUEST_URI field. Then, cross-reference this data with Apex Execution event data where the
average RUN_TIME exceeds 5 seconds. To identify synchronous requests only, cross-reference event data with the QUIDDITY field in
Apex Execution event data. For example, QUIDDITY NOT IN (A,BA,F,Q,S) and CALLOUT_TIME (>5000).

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

_Salesforce Developers Blog_ [: Designing Force.com Applications That Avoid Hitting Concurrent Request Limits](https://developer.salesforce.com/blogs/engineering/2013/05/force-com-concurrent-request-limits.html)

##### Console Event Type

Console events contain information about the performance and use of Salesforce Consoles. The Console events are logged whenever
a Console tab is opened with a sidebar component. Outside of that, when Console tabs are opened, a regular view record detail event
is served just like in Salesforce Classic.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**


Standard Objects EventLogFile Supported Event Types

```
CLIENT_IP

COMPONENT_ID

COMPONENT_ID_DERIVED

CONSOLE_ID

CONSOLE_ID_DERIVED

CPU_TIME

DB_TOTAL_TIME

```

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Id

**Description**
The 15-character ID of the component.

**Type**
Id

**Description**
The 18-character, case-insensitive ID of the component.

**Type**
Id

**Description**
The 15-character ID of the console.

**Type**
Id

**Description**
The 18-character, case-insensitive ID of the console.

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
Number

**Description**
The time in nanoseconds for a database round trip. Includes
time spent in the JDBC driver, network to the database, and
`DB_CPU_TIME` . Compare this field to `CPU_TIME` to
determine whether performance issues are occurring in the
database layer or in your own code.


Standard Objects EventLogFile Supported Event Types

```
EVENT_TYPE

LICENSE_CONTEXT

LOGIN_KEY

ORGANIZATION_ID

RECORD_ID

RECORD_ID_DERIVED

REQUEST_ID

```

**Type**
String

**Description**
The type of event. The value is always `Console` .

**Type**
String

**Description**
The license context in which a user is using a console.

**Example**
service, salesandservice, sales

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
Id

**Description**
The 15-character ID of the record that’s associated with the
console.

**Type**
Id

**Description**
The 18-character, case-insensitive ID of the record that’s
associated with the console.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

```
REQUEST_STATUS

RUN_TIME

SESSION_KEY

TIMESTAMP

```

**Type**
String

**Description**
The status of the request for a page view or user interface
action.

For example:

**•** `S` —Success. Salesforce handled the request successfully.
If an Apex controller throws an exception, this status is also
returned.

**•** `F` —Failure. Typically 4xx or 5xx HTTP codes, such as no
permission to view page, page took too long to render,
page is read-only.

**•** `U` —Undefined

**•** `A` —Authorization Error

**•** `R` —Redirect. Typically a 3xx HTTP code, possibly initiated
by an Apex controller in a Visualforce page.

**•** `N` —Not Found. 404 error.

This field can have a blank value.

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .


Standard Objects EventLogFile Supported Event Types

```
TIMESTAMP_DERIVED

URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

USER_TYPE

```

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

**Type**
String

**Description**
The category of user license.

Possible values are:

**•** `CsnOnly` —Users whose access to the application is
limited to Chatter. This user type includes Chatter Free and
Chatter moderator users.


Standard Objects EventLogFile Supported Event Types

**•** `CspLitePortal` —CSP Lite Portal license. Users whose
access is limited because they’re organization customers
and access the application through a customer portal or
an Experience Cloud site.

**•** `CustomerSuccess` —Customer Success license. Users
whose access is limited because they’re organization
customers and access the application through a customer
portal.

**•** `Guest` —Users whose access is limited so that your
customers can view and interact with your site without
logging in.

**•** `PowerCustomerSuccess` —Power Customer Success
license. Users whose access is limited because they’re
organization customers and access the application through
a customer portal. Users with this license type can view
and edit data they directly own or data owned by or shared
with users below them in the customer portal role
hierarchy.

**•** `PowerPartner` —Power Partner license. Users whose
access is limited because they’re partners and typically
access the application through a partner portal or site.

**•** `SelfService` —Users whose access is limited because
they’re organization customers and access the application
through a self-service portal.

**•** `Standard` —Standard user license. This user type also
includes Salesforce Platform and Salesforce Platform One
user licenses, and admins for this org.

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Content Distribution Event Type

Content Distribution events contain information about content distributions and deliveries to users.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
ACTION

```

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The action that’s used when a delivery is viewed.

**Possible Values**

**•** `VIEW`

**•** `INSERT`

**•** `UPDATE`

```
DELIVERY_ID

DELIVERY_LOCATION

EVENT_TYPE

ORGANIZATION_ID

RELATED_ENTITY_ID

REQUEST_ID

```

**Type**
Id

**Description**
The 15-character ID of the content delivery.

**Type**
String

**Description**
The location of the delivery.

**Type**
String

**Description**
The type of event. The value is always
`ContentDistribution` .

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
Id

**Description**
The 15-character ID of the record that’s associated with the
delivery distribution.

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .


Standard Objects EventLogFile Supported Event Types

```
TIMESTAMP

TIMESTAMP_DERIVED

USER_ID

USER_ID_DERIVED

VERSION_ID

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Content Document Link Event Type

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

**Type**
Id

**Description**
The 15-character ID of the content version.

Content Document Link events contain sharing information for content documents.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)


Standard Objects EventLogFile Supported Event Types

Fields

**Field** **Details**

```
DOCUMENT_ID

EVENT_TYPE

ORGANIZATION_ID

REQUEST_ID

SHARED_WITH_ENTITY_ID

SHARING_OPERATION

```

**Type**
Id

**Description**
The 15-character ID of the document that’s being shared.

**Type**
String

**Description**
The type of event. The value is always
`ContentDocumentLink` .

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Id

**Description**
Who the document was shared with.

**Type**
String

**Description**
The type of sharing operation on the document.

**Possible Values**

**•** `INSERT`

**•** `UPDATE`

**•** `DELETE`


Standard Objects EventLogFile Supported Event Types

```
SHARING_PERMISSION

TIMESTAMP

TIMESTAMP_DERIVED

USER_ID

USER_ID_DERIVED

```

**Type**
String

**Description**
What permissions the document was shared with.

**Possible Values**

**•** `V` : Viewer

**•** `C` : Collaborator

**•** `I` : Inferred—that is, the sharing permissions were inferred
from a relationship between the viewer and document.
For example, a document’s owner has a sharing permission
to the document itself. Or, a document can be a part of a
content collection, and the viewer has sharing permissions
to the collection rather than explicit permissions to the
document directly.

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.


Standard Objects EventLogFile Supported Event Types

For example: `00590000000I1SNIA0` .

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Content Transfer Event Type

Content Transfer events contain information about content transfer events, such as downloads, uploads, and previews. This information
includes events performed on files and attachments to records.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
DOCUMENT_ID

DOCUMENT_ID_DERIVED

EVENT_TYPE

FILE_PREVIEW_TYPE

FILE_TYPE

```

**Type**
Id

**Description**
The 15-character ID of the document that’s being shared.

**Type**
Id

**Description**
The 18-character case insensitive ID of the document that’s
being shared.

**Type**
String

**Description**
The type of event. The value is always `ContentTransfer` .

**Type**
String

**Description**
The content type of the file preview.

**Type**
String

**Description**
The content type of the file version.


Standard Objects EventLogFile Supported Event Types

```
ORGANIZATION_ID

REQUEST_ID

SIZE_BYTES

TIMESTAMP

TIMESTAMP_DERIVED

TRANSACTION_TYPE

```

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Number

**Description**
The size of the file transfer, in bytes.

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String

**Description**
The operation that was performed, including operations on
files and attachments to records. For example, you can track
operations in the Attachments related list on a case.

**Possible Values**

**•** `VersionDownloadAction` and
`VersionDownloadApi` represent downloads via the
user interface and API respectively.


Standard Objects EventLogFile Supported Event Types

**•** `VersionRenditionDownload` represents a file
preview action.

**•** `saveVersion` represents a file that’s being uploaded.

```
USER_ID

USER_ID_DERIVED

VERSION_ID

VERSION_ID_DERIVED

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Continuation Callout Summary Event Type

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

**Type**
Id

**Description**
The 15-character ID of the content version.

**Type**
Id

**Description**
The 18-character case insensitive ID of the content version.

Continuation Callout Summary events contain information about all of the asynchronous callouts performed during a transaction, their
response status codes, execution times, and URL endpoint destinations. This event type is available in the EventLogFile object in API
version 43.0 and later.

[For details about event monitoring, see the Trailhead Event Monitoring module or the REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)


Standard Objects EventLogFile Supported Event Types

Fields

**Field** **Details**

```
CONTINUATION_ID

DURATION

EVENT_TYPE

ORGANIZATION_ID

ORIGIN_REQUEST_ID

REQUEST_FORM_SIZE

REQUEST_ID

```

**Type**
String

**Description**
A unique ID identifying a sequence of events within a request.

**Example**
SFDC-Continuation-14e3cg85-961d-389e-7bz1-3d171543162a

**Type**
Number

**Description**
Total duration of continuation, in milliseconds.

**Type**
String

**Description**
The type of event. The value is always `ContinuationCalloutSummary` .

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
Id

**Description**
The ID of the request that initiated a callout.

**Example**
TID:5ILoVKlztX_rDDJcp7

**Type**
String

**Description**
Continuation request form size, in bytes. Depending on how many HTTP requests were used
in a continuation, this field can contain up to three space-separated values.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

```
RESPONSE_SIZE

STATUS_CODE

SUCCESS

TIMESTAMP

TIMESTAMP_DERIVED

```

**Type**
String

**Description**
The size of the callout response, in bytes. Depending on how many HTTP requests were used
in a continuation, this field can contain up to three space-separated values.

**Type**
String

**Description**
The HTTP status or internal code returned by the remote endpoint. A status code of 200
indicates that the request was successful. Other status code values indicate the type of
problem that was encountered. Depending on how many HTTP requests were used in a
continuation, this field can contain up to three space-separated values.

**Examples**

**•** 2000—The timeout was reached, and the server didn’t get a chance to respond.

**•** 2001—There was a connection failure.

**•** 2002—Exceptions occurred.

**•** 2003—The response hasn’t arrived (which also means that the Apex asynchronous
callout framework hasn’t resumed).

**•** 2004—The response size is too large (greater than 1 MB).

**Type**
Boolean

**Description**
Indicates whether the continuation was successful ( `1` ) or not ( `0` ).

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

For example: `2015-07-27T11:32:59.555Z` . Timezone is GMT.

```
URL

USER_ID

USER_ID_DERIVED

VF_CONTROLLER_SIZE

```

SEE ALSO:

**Type**
String

**Description**
The callout endpoint URL. Depending on how many HTTP requests were used in a
continuation, this field can contain up to three space-separated values.

**Example**
http://prod.location.amazonaws.com:1000/orders/order/_search

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using Salesforce services through the
UI or the API.

For example: `00590000000I1SNIA0` .

**Type**
String

**Description**
Continuation Visualforce controller size, in bytes. Depending on how many HTTP requests
were used in a continuation, this field can contain up to three space-separated values.

EventLogFile Supported Event Types

EventLogFile

##### CORS Violation Record Event Type

CORS Violation Record events capture information about Cross-Origin Resource Sharing (CORS) violations. Cross-origin requests to
Lightning apps are blocked unless the request comes from a URL listed in your CORS allowlist.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)


Standard Objects EventLogFile Supported Event Types

Fields

**Field** **Details**

```
EVENT_TYPE

HOST

ORGANIZATION_ID

ORIGIN

REQUEST_ID

```

**Type**
String

**Description**
The type of event. The value is always `CorsViolation` .

**Type**
String

**Description**
The URL of the requested Salesforce resource.

If JavaScript code at `https://www.example.com`
requests a resource from
`https://www.salesforce.com`, the origin is
`https://www.example.com` and the host is
`https://www.salesforce.com` .

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The URL of the site making the cross-origin request to
Salesforce.

If JavaScript code at `https://www.example.com`
requests a resource from
`https://www.salesforce.com`, the origin is
`https://www.example.com` and the host is
`https://www.salesforce.com` .

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .


Standard Objects EventLogFile Supported Event Types

```
TIMESTAMP

TIMESTAMP_DERIVED

##### CSP Violation Event Type

```

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

CSP violation events capture details about blocked resource requests from Lightning Experience pages based on your content security
policy (CSP). The CSP Violation event type is available in the EventLogFile object in API version 63.0 and later.

This event is free for all customers with a 24-hour data retention period. The CSP violation event is available in the API but not in the
Event Monitoring Analytics app.

[For details about event monitoring, see the Trailhead Event Monitoring module or the REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Note: To help preserve performance, Salesforce uses throttling, a technique that limits the number of generated CSP violation
events when the volume is exceptionally high. Therefore, if your org generates a high volume of CSP violations over a short period
of time, some of those violations can fail to generate a CSP violation event.

Fields

**Field** **Details**

```
BLOCKED_URI

BLOCKED_URI_DOMAIN

```

**Type**
String

**Description**
The full string of the blocked resource. If the call to the blocked resource used a URL,
`BLOCKED_URI` is the full URL. Or, for violations with a `DIRECTIVE` of `script-src`
directives, `inline` or `eval` .

**Examples**

**•** https://www.example.com/images/picture.png

**•** file://host1:0002/media/video.mp4

**•** inline

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
If `BLOCKED_URI` is a URL, the domain for that URL. To allow resources to be loaded from
the `BLOCKED_URI`, `BLOCKED_URI_DOMAIN` is the `endpointUrl` value to add or
update in the CspTrustedSite Metadata API.

**Example**
www.example.com

```
COLUMN_NUMBER

CONTEXT

DIRECTIVE

DISPOSITION

```

**Type**
Number

**Description**
The column number in the document or worker script at which the violation occurred. This
value is relevant only when `DIRECTIVE` is `script-src` .

For those violations, use this value with `LINE_NUMBER` to identify the location of the
violation.

**Example**

**Type**
String

**Description**
The content security policy (CSP) context for the request. The CSP context controls which
pages can load content from a CspTrustedSite.

CSP violation events capture details about blocked resource requests from only Lightning
Experience pages, this value is always `Lightning` .

**Type**
String

**Description**
The CSP directive that blocked the resource request.

**Possible Values**

**•** `font-src`

**•** `frame-src`

**•** `img-src`

**•** `media-src`

**•** `style-src`

**•** `script-src`

[For information on these directives and a full list of all CSP directives, see MDN Web Docs:](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy)
[Content-Security-Policy.](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy)

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The CSP violation handling instruction for the user agent at the time of the violation.

**Possible Values**

**•** `enforce` —Enforce the policy violation. For violations with this `DISPOSITION`, the
resource request was blocked.

**•** `report` —Report the policy violation. For violations with this `DISPOSITION`, the
resource request wasn’t blocked, but the violation was reported.

```
EVENT_TYPE

LINE_NUMBER

REQUEST_ID

RESOURCE_SAMPLE

```

**Type**
String

**Description**
The type of event. The value is always `CspViolation`

**Type**
Number

**Description**
The line number in the document or worker script at which the violation occurred. This value
is relevant only when `DIRECTIVE` is `script-src` . For those violations, use this value
with `COLUMN_NUMBER` to identify the location of the violation.

**Example**

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

**Example**

```
  0000000062_0000x8Lz
```

**Type**
String

**Description**
A sample of the resource that caused the violation, usually the first 40 characters, or the
empty string.

**Example**


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
                    LoginHint.saveHintEdit();

                    function handleLogin(){document.login.un…

```

```
SOURCE

SOURCE_FILE

TIMESTAMP

TIMESTAMP_DERIVED

```

Usage

**Type**
String

**Description**
The page where this CSP violation originated. For example, if your CSP policy prevented an
image from loading on a Visualforce page, `SOURCE` contains the URL of that page.

**Example**

```
  https:// MyDomainName .my.salesforce.com/apex/HelloWorld

```

**Type**
String

**Description**
The URL of the script in which the violation occurred. If the violation didn’t occur in a script,
`SOURCE_FILE` is null.

**Example**
https://www.example.com/script_xyz.js

**Type**
DateTime

**Description**
The access time of Salesforce services in GMT.

**Example**

```
  20220715233322.670

```

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ). The time zone is always GMT.

**Example**

```
  2022-07-27T11:32:59.555Z.

```

Only one CSP violation event log file is available at a time. When the daily incremental event log file is generated during the daily
background process, the new file replaces the existing file.

If the event log file doesn’t exist, either the log generation process hasn’t run yet or there’s no violation data to report for that 24-hour
window. The event log file is generated only when at least one violation occurred for the day.


Standard Objects EventLogFile Supported Event Types

To collect CSP violation logs for multiple days, schedule a daily query of the CSP Violation event type via REST API. For example, you can
configure a cron job in Unix or a scheduled task in Windows to run the query.

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Dashboard Event Type

Dashboard events contain details about report requests from dashboards. These requests are triggered by dashboard refreshes,
subscriptions, and filter changes.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
CLIENT_IP

CPU_TIME

DASHBOARD_COMPONENT_ID

DASHBOARD_ID

DASHBOARD_ID_DERIVED

```

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
Id

**Description**
The 15-character ID of the dashboard component.

**Type**
String

**Description**
The 15-character ID of the dashboard that was run.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The 18-character case insensitive ID of the dashboard that was
run.

```
DASHBOARD_TYPE

EVENT_TYPE

IS_SCHEDULED

IS_SUCCESS

LOGIN_KEY

ORGANIZATION_ID

```

**Type**
String

**Description**
The type of dashboard.

**Possible Values**

**•** `R` : Run as running user

**•** `C` : Run as context user

**•** `S` : Run as specific user

**Type**
String

**Description**
The type of event. The value is always `Dashboard` .

**Type**
Boolean

**Description**
1 if the dashboard component ran successfully, 0 if it didn’t.

**Type**
Boolean

**Description**
1 if the dashboard component ran successfully, 0 if it didn’t.

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .


Standard Objects EventLogFile Supported Event Types

```
REPORT_ID

REPORT_ID_DERIVED

REQUEST_ID

RUN_TIME

SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

```

**Type**
Id

**Description**
The 15-character ID of the report that was run.

**Type**
Id

**Description**
The 18-character case insensitive ID of the report that was run.

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).


Standard Objects EventLogFile Supported Event Types

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

```
URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

VIEWING_USER_ID

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Database Save Event Type

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user the dashboard is running as.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user the dashboard
is running as.

For example: `00590000000I1SNIA0` .

**Type**
Id

**Description**
The ID of the user who’s viewing the dashboard.

Database Save events track when records are created, updated, or deleted. This object is available in API version 63.0 and later.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)


Standard Objects EventLogFile Supported Event Types

Fields

**Field** **Details**

```
DML_TYPE

EVENT_TYPE

FIRST_ENTITY_ID

KEY_PREFIX

LOGIN_KEY

NUM_ROWS

ORGANIZATION_ID

REQUEST_ID

```

**Type**
String

**Description**
The type of DML statement.

**Type**
Id

**Description**
The type of event.

**Type**
String

**Description**
The first ID that is logged when an update occurs. If a single record is updated, the ID of that
row is logged. If multiple records are updated, only one ID is logged.

**Type**
String

**Description**
The key prefix of the entity type that was saved.

**Type**
String

**Description**
The string that ties together all events in a given user’s login session.

**Type**
String

**Description**
The number of entities that were saved.

**Type**
Id

**Description**
The 15-character ID of the organization.

**Type**
String

**Description**
Globally unique id for a given request.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
SAMPLE_FACTOR

SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

USER_ID

```

**Type**
Number

**Description**
The ratio of saved entities that were logged. A value of 1 means every entity saved was logged.
A value of 100 means that 1 out of 100 entities saved was logged.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started.

**Example**

```
  d7DEq/ANa7nNZZVD

```

**Type**
String

**Description**
The Timestamp at which the log event was generated.

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

**Example**

```
  2015-07-27T11:32:59.555Z

```

**Type**
Id

**Description**
The ID of the user who’s using Salesforce services through the UI or the API.

**Example**

```
  005XXXXXXXXXXXX

```

##### Document Attachment Downloads Event Type

Document Attachment Downloads events contain details of document and attachment downloads.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)


Standard Objects EventLogFile Supported Event Types

Fields

**Field** **Details**

```
ENTITY_ID

EVENT_TYPE

FILE_TYPE

ORGANIZATION_ID

REQUEST_ID

TIMESTAMP

TIMESTAMP_DERIVED

```

**Type**
Id

**Description**
The 15-character ID of the entity that’s associated with the
document or attachment.

**Type**
String

**Description**
The type of event. The value is always
`DocumentAttachmentDownoads` .

**Type**
String

**Description**
The type of the file or attachment.

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime


Standard Objects EventLogFile Supported Event Types

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

```
USER_ID

USER_ID_DERIVED

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### External Cross-Org Callout Event Type

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

External Cross-Org Callout events represent external data callouts via the cross-org adapter for Salesforce Connect. This event type is
available in the EventLogFile object in API version 40.0 and later.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Note: For the cross-org adapter for Salesforce Connect, event monitoring currently doesn’t track search callouts.

Fields

**Field** **Details**

```
ACTION

```

**Type**
String

**Description**
Action performed by the callout.

**Possible Values**

**•** query


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**•** upsert

**•** delete

```
ENTITY

EVENT_TYPE

EXECUTE_MS

FETCH_MS

FILTER

HAVING

```

**Type**
String

**Description**
Name of the external object being accessed.

**Example**
Order

**Type**
String

**Description**
Type of event. Value is always `ExternalCrossOrgCallout` .

**Type**
Number

**Description**
How long it took (in milliseconds) for Salesforce to prepare and execute the query. Available
in API version 42.0 and later.

**Example**

**Type**
Number

**Description**
How long it took (in milliseconds) to retrieve the query results from the external system.
Available in API version 42.0 and later.

**Example**

**Type**
Text

**Description**
Field expressions to filter which rows to return. Corresponds to `WHERE` in SOQL queries.

**Example**
WHERE CustomerId='123456'

**Type**
Text

**Description**
Reserved for future use.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
LIMIT

MESSAGE

OFFSET

ORDERBY

ORGANIZATION_ID

```

**Type**
Number

**Description**
Maximum number of rows to return for a query. Corresponds to `LIMIT` in SOQL queries.

**Example**

**Type**
String

**Description**
Error or warning message associated with the failed query callout. Value is always empty for
upsert and delete callouts.

**Example**
System.UnexpectedException: Query is either selecting too many fields or the filter conditions
are too complicated

**Type**
Number

**Description**
Number of rows to skip when paging through a result set.

Corresponds to `OFFSET` in SOQL queries. If a SOQL query doesn’t define an `OFFSET`, the
value is -1.

**Example**
0 (default)

**Type**
String

**Description**
Field or column to use for sorting query results, and whether to sort the results in ascending
(default) or descending order. Corresponds to `ORDER BY` in SOQL queries.

**Examples**

**•** ORDER BY ShipName

**•** ORDER BY ShipName DESC

**Type**
Id

**Description**
15-character ID of the organization.

**Example**
00D000000000123


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
REQUEST_ID

ROWS

ROWS_FETCHED

SELECT

STATUS

SUBQUERIES

```

**Type**
String

**Description**
Unique ID of a transaction. A transaction can contain one or more events. All events in a
transaction have the same REQUEST_ID.

**Example**
4A13-HSKv3CKs-0FKfceaV

**Type**
Number

**Description**
Total number of records in the result set. Value is always 0 for upsert and delete callouts.

**Example**

**Type**
Number

**Description**
Reserved for future use.

**Type**
String

**Description**
Comma-separated list of fields being queried. Corresponds to `SELECT` in SOQL queries.

**Example**
SELECT Id,Name,CustomerID,OrderDate

**Type**
Boolean

**Description**
Whether the query was successful. Value is always empty for upsert and delete callouts.

**Possible Values**

**•** 1—Success

**•** 0—Failed

**Type**
Number

**Description**
The number of subqueries that the query is split into.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
THROUGHPUT

TIMESTAMP

TIMESTAMP_DERIVED

TOTAL_MS

USER_ID

USING_MRU

```

**Type**
Number

**Description**
Reserved for future use.

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone is GMT.

**Type**
Number

**Description**
How long it took (in milliseconds) to prepare and execute the query and to retrieve the query
results.

**Example**

**Type**
Id

**Description**
15-character ID of the user accessing the external system.

**Example**
00530000009M943

**Type**
Boolean


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
Reserved for future use.

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### External Custom Apex Callout Event Type

External Custom Apex Callout events represent external data callouts via custom adapters for Salesforce Connect. This event type is
available in the EventLogFile object in API version 40.0 and later.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
ACTION

ENTITY

EVENT_TYPE

EXECUTE_MS

```

**Type**
String

**Description**
Action performed by the callout.

**Possible Values**

**•** query

**•** upsert

**•** delete

**Type**
String

**Description**
Name of the external object being accessed.

**Example**
Order

**Type**
String

**Description**
Type of event. Value is always `ExternalCustomApexCallout` .

**Type**
Number


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
How long it took (in milliseconds) for Salesforce to prepare and execute the query. Available
in API version 42.0 and later.

**Example**

```
FETCH_MS

FILTER

LIMIT

MESSAGE

OFFSET

```

**Type**
Number

**Description**
How long it took (in milliseconds) to retrieve the query results from the external system.
Available in API version 42.0 and later.

**Example**

**Type**
Text

**Description**
Field expressions to filter which rows to return. Corresponds to `WHERE` in SOQL queries.

**Example**
Filter:[columnName=CustomerID, columnValue=537, subfilters=null, tableName=Order,
type=EQUALS]

**Type**
Number

**Description**
Maximum number of rows to return for a query. Corresponds to `LIMIT` in SOQL queries.

**Example**

**Type**
String

**Description**
Error or warning message associated with the failed call.

**Example**
System.UnexpectedException: Query is either selecting too many fields or the filter conditions
are too complicated

**Type**
Number

**Description**
Number of rows to skip when paging through a result set. Corresponds to `OFFSET` in SOQL
queries.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Example**
0 (default)

```
ORDERBY

ORGANIZATION_ID

REQUEST_ID

ROWS

ROWS_FETCHED

```

**Type**
String

**Description**
Field or column to use for sorting query results, and whether to sort the results in ascending
(default) or descending order. Corresponds to `ORDER BY` in SOQL queries.

**Examples**
(Order:[columnName=OrderDate, direction=ASCENDING, tableName=Order])

**Type**
Id

**Description**
15-character ID of the organization.

**Example**
00D000000000123

**Type**
String

**Description**
Unique ID of a transaction. A transaction can contain one or more events. All events in a
transaction have the same REQUEST_ID.

**Example**
4A13-HSKv3CKs-0FKfceaV

**Type**
Number

**Description**
Total number of records in the result set.

The value is always -1 if the custom adapter’s `DataSource.Provider` class doesn’t
declare the `QUERY_TOTAL_SIZE` capability.

**Example**

**Type**
Number

**Description**
Number of rows fetched by the callout. Available in API version 42.0 and later.

**Example**


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
SELECT

STATUS

THROUGHPUT

TIMESTAMP

SUBQUERIES

TIMESTAMP_DERIVED

```

**Type**
String

**Description**
Comma-separated list of fields being queried. Corresponds to `SELECT` in SOQL queries.

**Example**
(ColumnSelection:[aggregation=NONE, columnName=Name, tableName=Order],
ColumnSelection:[aggregation=NONE, columnName=CustomerID, tableName=Order],
ColumnSelection:[aggregation=NONE, columnName=OrderDate, tableName=Order])

**Type**
Boolean

**Description**
Whether the query was successful.

**Possible Values**

**•** 1—Success

**•** 0—Failed

**•** Empty—Failed with no logged status or message

**Type**
Number

**Description**
Number of records retrieved in one second.

**Example**
302.57

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
Number

**Description**
Reserved for future use.

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

For example: `2015-07-27T11:32:59.555Z` . Timezone is GMT.

```
TOTAL_MS

USER_ID

```

SEE ALSO:

**Type**
Number

**Description**
How long it took (in milliseconds) to prepare and execute the query and to retrieve the query
results.

**Example**

**Type**
Id

**Description**
15-character ID of the user accessing the external system.

**Example**
00530000009M943

EventLogFile Supported Event Types

EventLogFile

##### External Data Source Callout Event Type

External Data Source Callout events represent external data callouts via the Salesforce Connect adapters for Amazon DynamoDB and
Amazon Athena. This event type is available in the EventLogFile object in API version 56.0 and later.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
ACTION

```

**Type**
String

**Description**
Action performed by the callout.

**Possible Values**
For Amazon DynamoDB data source:

**•** query

**•** insert

**•** delete

**•** update


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**•** upsert

For Amazon Athena data source:

**•** query

```
DATA_SOURCE_NAME

EVENT_TYPE

EXTERNAL_OBJECT

FETCH_MS

FILTER

LIMIT

MESSAGE

```

**Type**
String

**Description**
Name of the external data source being accessed.

**Type**
String

**Description**
Type of event. Value is always `ExternalDataSourceCallout` .

**Type**
String

**Description**
Name of the external object being accessed.

**Type**
Number

**Description**
How long it took (in milliseconds) to retrieve the query results from the external data source.

**Example**

**Type**
Text

**Description**
Field expressions to filter which rows to return. Corresponds to `WHERE` in queries.

**Type**
Number

**Description**
[Maximum number of rows to return for a query. Corresponds to Limit parameter in](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ExecuteStatement.html)
[ExecuteStatement operation for an Amazon DynamoDB data source.](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ExecuteStatement.html)

**Type**
String

**Description**
Error or warning message associated with the failed call.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
NEXT_LINK

OFFSET

OPERATION

ORDERBY

ORGANIZATION_ID

PARENT_CALLOUT

```

**Type**
String

**Description**
Next link that the callout used to request a subsequent page of rows. A next link is provided
in a previous response when the response includes only part of the result set.

For requests to AWS data sources, this field stores the `nextToken` parameter that contains
a unique hash string.

**Type**
Number

**Description**
Number of rows to skip when paging through a result set. Corresponds to `OFFSET` in
queries to Amazon Athena. This field is not supported by queries to Amazon DynamoDB.

**Type**
String

**Description**
The operation that’s being performed.

**Type**
String

**Description**
Field or column to use for sorting query results, and whether to sort the results in ascending
(default) or descending order. Corresponds to `ORDER BY` in queries.

**Example**

**•** Country ASC

**•** CustomerName DESC

**Type**
Id

**Description**
15-character ID of the organization.

**Example**
00D000000000123

**Type**
String

**Description**
If the callout requested a subsequent page of rows, this field identifies the initial callout
whose request resulted in the multi-page result set.

**Example**
4EoZtuBzzRIXSk-ysRdf1F-1


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
PROVIDER_TYPE

REQUEST_ID

RESPONSE_SIZE

ROWS_FETCHED

SEARCH

SELECT

```

**Type**
String

**Description**
Whether the callout was made by Salesforce Connect adapter for Amazon DynamoDB or
Amazon Athena.

**Possible Values**

**•** `amazonDynamodb`

**•** `amazonAthena`

**Type**
String

**Description**
Unique ID of a transaction. A transaction can contain one or more events. All events in a
transaction have the same REQUEST_ID.

**Example**
4A13-HSKv3CKs-0FKfceaV

**Type**
Number

**Description**
The size of the callout response, in bytes.

**Type**
Number

**Description**
Number of records fetched by the callout. The records fetched by a callout can be a subset
of a large result set.

**Example**

**Type**
String

**Description**
Search query string.

**Type**
String

**Description**
Comma-separated list of fields being queried. Corresponds to `SELECT` in queries.

To query, Salesforce Connect adapter uses PartiQL with Amazon DynamoDB and SQL with
Amazon Athena.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Example**
CustomerID,OrderDate,OrderID,ShipCity,ShipCountry

```
STATUS

STATUS_CODE

TABLE_NAME

THROUGHPUT

TIMESTAMP

TIMESTAMP_DERIVED

```

**Type**
Boolean

**Description**
Whether the query was successful.

**Possible Values**

**•** 1—Success

**•** 0—Failed

**Type**
Number

**Description**
The HTTP response status code for the request.

**Type**
String

**Description**
Name of the table being queried in the AWS data source.

**Type**
Number

**Description**
Number of records retrieved in one second.

**Example**
3025.67

**Type**
DateTime

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone is GMT.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
TOTAL_MS

USER_ID

```

**Type**
Number

**Description**
How long it took (in milliseconds) to prepare and execute the query and to retrieve the query
results.

**Type**
Id

**Description**
15-character ID of the user accessing the external data source.

**Example**
00530000009M943

##### External OData Callout Event Type

External OData Callout events represent external data callouts via the OData 2.0 and OData 4.0 adapters for Salesforce Connect. This
event type is available in the EventLogFile object in API version 40.0 and later.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
ACTION

BYTES

ENTITY

```

**Type**
String

**Description**
Action performed by the callout.

**Possible Values**

**•** query

**•** upsert

**•** delete

**Type**
Number

**Description**
Size of the result set in bytes.

**Type**
String

**Description**
Name of the external object being accessed.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Example**
Order

```
EVENT_TYPE

EXECUTE_MS

EXPAND

FETCH_MS

FILTER

LIBRARY

```

**Type**
String

**Description**
Type of event. Value is always `ExternalODataCallout` .

**Type**
Number

**Description**
How long it took (in milliseconds) for Salesforce to prepare and execute the query. Available
in API version 42.0 and later.

**Example**

**Type**
String

**Description**
Reserved for future use.

**Type**
Number

**Description**
How long it took (in milliseconds) to retrieve the query results from the external system.
Available in API version 42.0 and later.

**Example**

**Type**
Text

**Description**
Field expressions to filter which rows to return. Corresponds to `WHERE` in SOQL queries and
`$filter` in OData queries.

**Example**
CustomerID eq 12345

**Type**
String

**Description**
Reserved for future use.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
LIMIT

MESSAGE

NEXT_LINK

OFFSET

ORDERBY

```

**Type**
Number

**Description**
Maximum number of rows to return for a query. Corresponds to `LIMIT` in SOQL queries
and `$top` in OData queries.

**Example**

**Type**
String

**Description**
Error or warning message associated with the failed call.

**Example**
The OData query result was too large, so the external data didn’t load.

**Type**
String

**Description**
OData next link that the callout used to request a subsequent page of rows. A next link is
provided in a previous response from the OData producer when the response includes only
part of the result set.

Available in API version 42.0 and later. However, this field isn’t supported for the OData 2.0
adapter on orgs created before Spring ’18.

**Example**
http://services.example.org/Warehouse.svc/Orders?$count=true&
$select=CustomerID,OrderID,RequiredDate,ShippedDate&$top=301&$skiptoken=10447

**Type**
Number

**Description**
Number of rows to skip when paging through a result set.

Corresponds to `OFFSET` in SOQL queries and `$skip` in OData queries.

**Example**

**Type**
String

**Description**
Field or column to use for sorting query results, and whether to sort the results in ascending
(default) or descending order. Corresponds to `ORDER BY` in SOQL queries and `$orderby`
in OData queries.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Examples**

**•** ShipName

**•** ShipName desc

```
ORGANIZATION_ID

PARENT_CALLOUT

PROVIDER_TYPE

RATE_LIMIT_USAGE_PERCENT

REQUEST_ID

```

**Type**
Id

**Description**
15-character ID of the organization.

**Example**
00D000000000123

**Type**
String

**Description**
If the callout requested a subsequent page of rows, this field identifies the initial callout
whose request resulted in the multi-page result set.

Available in API version 42.0 and later. However, this field isn’t supported for the OData 2.0
adapter on orgs created before Spring ’18.

**Example**
4EoZtuBzzRIXSk-ysRdf1F-1

**Type**
String

**Description**
Whether the OData 2.0 or OData 4.0 adapter made the callout.

**Possible Values**

**•** OData—OData 2.0 adapter

**•** OData4—OData 4.0 adapter

**Type**
Number

**Description**
Consumed percentage of the org’s limit of OData callouts per hour.

**Example**
2.5—2.5% of the hourly callout limit has been consumed

**Type**
String

**Description**
Unique ID of a transaction. A transaction can contain one or more events. All events in a
transaction have the same REQUEST_ID.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Example**
4A13-HSKv3CKs-0FKfceaV

```
REQUESTS

ROWS

ROWS_FETCHED

SEARCH

SELECT

STATUS

```

**Type**
Number

**Description**
Reserved for future use.

**Type**
Number

**Description**
Total number of records in the result set. Available in API version 42.0 and later.

**Example**

**Type**
Number

**Description**
Number of records fetched by the callout. The records fetched by a callout can be a subset
of a large result set.

Available in API version 42.0 and later. However, this field isn’t supported for the OData 2.0
adapter on orgs created before Spring ’18.

**Example**

**Type**
String

**Description**
Search query string. Corresponds to condition expressions in SOSL.

**Example**
contains(CustomerID,'10248') eq true or contains(ShipName,'10248') eq true

**Type**
String

**Description**
Comma-separated list of fields being queried. Corresponds to `SELECT` in SOQL queries
and `$select` in OData queries.

**Example**
CustomerID,OrderDate,OrderID,ShipCity,ShipCountry

**Type**
Boolean


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
Whether the query was successful.

**Possible Values**

**•** 1—Success

**•** 0—Failed

```
THROUGHPUT

TIMESTAMP

TIMESTAMP_DERIVED

TOTAL_MS

USER_ID

```

**Type**
Number

**Description**
Number of records retrieved in one second.

Available in API version 42.0 and later. However, this field isn’t supported for the OData 2.0
adapter on orgs created before Spring ’18.

**Example**
3025.67

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone is GMT.

**Type**
Number

**Description**
How long it took (in milliseconds) to prepare and execute the query and to retrieve the query
results.

**Type**
Id

**Description**
15-character ID of the user accessing the external system.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Example**
00530000009M943

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Flow Execution Event Type

Flow Execution events contain information about flows that were executed including details such as total execution time, number of
interviews, and number of errors.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
BOT_IDENTIFIER

BOT_SESSION_IDENTIFIER

EVENT_TYPE

TIMESTAMP

REQUEST_ID

```

**Type**
string

**Description**
The ID of the bot.

**Type**
string

**Description**
The bot session ID.

**Type**
String

**Description**
The type of event. The value is always `FlowExecution` .

**Type**
String

**Description**
The time that the flow was executed in GMT.

For example: `20210606032436.520` .

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

For example: `TID:000000000000c00fff` .

```
ORGANIZATION_ID

USER_ID

PLANNER_IDENTIFIER

PROCESS_TYPE

```

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
Id

**Description**
The 15-character ID of the user who executed the flow through the UI or the API.

For example: `00530000009M943`

**Type**
string

**Description**
The ID of the agent planner.

**Type**
String

**Description**
The type of the flow. Valid values are:

**•** `ActionableEventManagementFlow` —A flow that triggers an actionable event
orchestration process in the background and automatically executes different types of
actions based on the event type. This value is available in API version 62.0 and later.

**•** `ActionCadenceAutolaunchedFlow` —A flow that’s executed when a user
completes a cadence step. This value is available in API version 56.0 and later.

**•** `ActionCadenceStepFlow` —A screen flow used as a cadence step. This value is
available in API version 56.0 and later.

**•** `ActivityObjectMatchingFlow` —A flow that launches when Einstein Activity
Capture detects and captures a new activity, such as an email. This type of flow runs in
the background without user interaction. This value is available with Sync Email as
Salesforce Activity in API version 64.0 and later.

**•** `Appointments` —A flow for Lightning Scheduler. This value is available in API version
44.0 and later.

**•** `ApprovalWorkflow` —An orchestration that’s used for an approval process. This
value is available in API version 63.0 and later.

**•** `AutoLaunchedFlow` —A flow that doesn’t require user interaction.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**•** `CheckoutFlow` —A flow used in Lightning B2B Commerce to create a checkout in a
store. This value is available in API version 48.0 and later.

**•** `ContactRequestFlow` —A flow that lets customers request to be contacted by
customer support. This flow is used to create contact request records. This value is
available in API version 45.0 and later.

**•** `CustomerLifecycle` —A Salesforce Surveys flow that lets you associate survey
questions with different stages in customer lifecycles. This value is available in API version
49.0 and later and only when the Customer Lifecycle Designer license is enabled.

**•** `CustomEvent` —A process that is invoked when it receives a platform event message.
In the UI, it’s an event process. This value is available in API version 41.0 and later.

**•** `DataCaptureFlow`                   - In the UI, Data Capture flows configure the Form tab in the
Field Service mobile app. When the Data Capture flow is launched, its Flow metadata is
publicly available in JavaScript format. This value is available in API version 62.0 and later.

**•** `DcvrFrameworkDataCaptureFlow` —A screen flow that presents assessment
questions from Discovery Framework. Launches when invoked by a user on a mobile
device. This type of flow collects or displays information, requires user interaction, and
works offline or online. This value is available in API version 62.0 and later.

**•** `EvaluationFlow` —A flow for evaluating custom entry and exit conditions in an
orchestration. Uses the `isOrchestrationConditionMet` output variable and
discards values from any other output variables. This value is available in API version 54.0
and later.

**•** `FieldServiceMobile` —A flow for the Field Service mobile app. This value is
available in API version 39.0 and later.

**•** `FieldServiceWeb` —A flow for embedded Appointment Booking. Its UI label is
Field Service Embedded Flow. This value is available in API version 41.0 and later.

**•** `Flow` —A flow that requires user interaction because it contains one or more screens
or local actions, choices, or dynamic choices. In the UI and Salesforce Help, it’s a screen
flow. Screen flows can be launched from the UI, such as with a flow action, Lightning
page, or web tab.

**•** `FSCLending` —A flow for Financial Services Cloud Mortgage. This value is available
in API version 46.0 and later.

**•** `IdentityUserRegistrationFlow` —A flow to handle user registration and
updates for single sign-on with the authentication provider framework. Available in API
version 64.0 and later.

**•** `IndicatorResultFlow` —A flow for Outcome Management that calculates and
creates indicator results for a selected indicator performance period. This value is available
with the Outcome Management license in API version 60.0 and later.

**•** `IndividualObjectLinkingFlow` —A flow that associates individuals with
interactions such as voice calls, messaging sessions, or case-related emails. This value is
available in API version 58.0 and later.

**•** `InvocableProcess` —A process that another process or the Invocable Actions
resource in REST API invokes. This value is available in API version 38.0 and later.

**•** `Journey` —An audience-driven flow for Marketing Cloud. This value is available in API
version 57.0 and later.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**•** `LoginFlow` —A flow for login. This value is available in API version 51.0 and later.

**•** `LoyaltyManagementFlow` —A flow for the Loyalty Management app that’s
invokable by loyalty program processes. This value is available in API version 54.0 and
later.

**•** `Orchestrator` —An orchestration that organizes flows into groups of steps contained
in a series of stages. This value is available in API version 53.0 and later.

**•** `PromptFlow` —A flow for Prompt Builder. Pass data between Prompt Builder and the
flow. This value is available in API version 60.0 and later.

**•** `RecommendationStrategy` —Build recommendations for your users. A
recommendation launches its assigned flow. This value is available in API version 54.0
[and later. See Flow Builder Strategies.](https://help.salesforce.com/s/articleView?id=platform.nba_building_flow_builder_strategy.htm&type=5&language=en_US)

**•** `RoutingFlow` —A flow for Salesforce Omni-Channel routing and other business logic.
This value is available in API version 52.0 and later.

**•** `Survey` —A flow for Salesforce Surveys. From the UI, this type of flow is created in
Survey Builder. This value is available in API version 42.0 and later.

**•** `SurveyEnrich` —A Salesforce Surveys flow that uses the Survey Data Mapper. From
the UI, this type of flow is created in the Survey Builder and requires an associated survey
flow type. This value is available in API version 49.0 or later and only when the Customer
Lifecycle Designer license is enabled.

**•** `Workflow` —A process that is invoked when a record is created or edited. In the UI
and Salesforce Help, it’s a record change process.

These values are reserved for future use.

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

```
FLOW_VERSION_ID

```

**Type**
Id

**Description**
The ID of the flow version that was executed.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
FLOW_LOAD_TIME

TOTAL_EXECUTION_TIME

NUMBER_OF_INTERVIEWS

NUMBER_OF_ERRORS

TIMESTAMP_DERIVED

```

**Type**
Number

**Description**
The time in milliseconds to load the flow’s metadata.

**Type**
Number

**Description**
The total time in milliseconds to start and finish all flow interviews.

**Type**
Number

**Description**
The number of flow interviews that started after the flow version was executed.

**Type**
Number

**Description**
The number of errors for all flow interviews after the flow version was executed.

**Type**
DateTime

**Description**
The time that the flow was executed in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone is GMT.

##### Group Membership Event Type

Group Membership events capture details about changes to public group and queue membership, such as when members are added
to or removed from the public group or queue.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
CLIENT_IP

```

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Example**

```
                   96.43.144.26

```

```
CPU_TIME

EVENT_TYPE

GROUP_ID

GROUP_TYPE

LOGIN_KEY

MEMBER_ID

```

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity that took place in the app server layer.

**Type**
String

**Description**
The type of event. The value is always `GroupMembership` .

**Type**
Id

**Description**
ID of the group whose membership changed.

**Example**

```
  00GXXXXXXXXXXXX

```

**Type**
String

**Description**
The type of group. Valid values are:

**•** `R` —Public group

**•** `Q` —Queue

**Example**

```
  R

```

**Type**
String

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring.

**Example**

```
  GeJCsym5eyvtEK2I

```

**Type**
Id


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The ID of the member added to or removed from the group. Public groups can contain
individual users, other groups, or users in a specified role or territory. Queues can contain
individual users, roles, public groups, territories, connections, or partner users.

**Example**
`005XXXXXXXXXXXX` or `00GXXXXXXXXXXXX`

```
OPERATION

ORGANIZATION_ID

REQUEST_ID

RUN_TIME

SESSION_KEY

```

**Type**
String

**Description**
The operation that occurred, such as a member being added to or removed from a group.
Valid values are:

**•** `AddedGroupMember`

**•** `DeletedGroupMember`

**Example**

```
  DeletedGroupMember

```

**Type**
Id

**Description**
The 15-character ID of the organization.

**Example**

```
  00DXXXXXXXXXXXX

```

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

**Example**

```
  3nWgxWbDKWWDIk0FKfF5DV

```

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Example**

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started.

**Example**

```
                   d7DEq/ANa7nNZZVD

```

```
TIMESTAMP

TIMESTAMP_DERIVED

URI

URI_ID_DERIVED

USER_ID

```

**Type**
String

**Description**
The access time of Salesforce services in GMT.

**Example**

```
  20130715233322.670

```

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

**Example**

```
  2015-07-27T11:32:59.555Z

```

**Type**
String

**Description**
The URI of the page that’s receiving the request.

**Example**

```
  /home/home.jsp

```

**Type**
Id

**Description**
The 18-character case insensitive ID of the URI of the page that’s receiving the request.

**Example**

```
  005XXXXXXXXXYAY

```

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.

**Example**

```
  005XXXXXXXXXXXX

```


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
USER_ID_DERIVED

```

SEE ALSO:

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using Salesforce services through the
UI or the API.

**Example**

```
  005XXXXXXXXXXXXIA0

```

EventLogFile Supported Event Types

EventLogFile

##### Hostname Redirects Event Type

Hostname Redirect events contain details about blocked and successful redirections for your previous My Domain hostnames. The
Hostname Redirects event type is available in the EventLogFile object in API version 56.0 and later.

Note: The HostnameRedirects event type is disabled by default. To enable this event type, use the `logRedirections` field
on the MyDomainSettings Metadata API type or enable the **Log Redirections** setting in the Routing section of the My Domain
Setup page.

This event is free for all customers with a 24-hour data retention period. The hostname redirections event is available in the API but not
in the Event Monitoring Analytics app. You can also download the latest hostname redirections event log file through a button on the
My Domain page.

[For details about event monitoring, see the Trailhead Event Monitoring module or the REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
EVENT_TYPE

TIMESTAMP

```

**Type**
String

**Description**
The type of event. The value is always `HostnameRedirects` .

**Type**
String

**Description**
The access time of Salesforce services in GMT.

**Example**

```
  20220715233322.670

```


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
REQUEST_ID

ORGANIZATION_ID

USER_ID

RUN_TIME

CPU_TIME

URI

SESSION_KEY

LOGIN_KEY

```

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same REQUEST_ID.

**Example**

```
  0000000062_0000x8Lz
```

**Type**
ID

**Description**
The 15-character ID of the org.

**Example**

```
  00D000000000345

```

**Type**
ID

**Description**
This field is unused in the HostnameRedirects event type. The value is always null.

**Type**
Number

**Description**
This field is unused in the HostnameRedirects event type. The value is always `0` .

**Type**
Number

**Description**
This field is unused in the HostnameRedirects event type. The value is always null.

**Type**
String

**Description**
This field is unused in the HostnameRedirects event type. The value is always null.

**Type**
String

**Description**
This field is unused in the HostnameRedirects event type. The value is always null.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
This field is unused in the HostnameRedirects event type. The value is always null.

```
MESSAGE

DOMAIN

SOURCE_HOSTNAME

TARGET_HOSTNAME

PATH

```

**Type**
String

**Description**
This field is unused in the HostnameRedirects event type. The value is always null.

**Type**
Url

**Properties**
Filter, Sort

**Description**
This field is unused in the HostnameRedirects event type. The value is always null.

**Type**
String

**Description**
The hostname of the URL from which the redirection originated.

**Example**
If `https://` _**`oldMyDomainName`**_ `.my.salesforce.com` is redirected to
`https://` _**`newMyDomainName`**_ `.my.salesforce.com`, the value of this field is

```
  oldMyDomainName .my.salesforce.com

```

**Type**
String

**Description**
The hostname of the URL to which the user or API was redirected.

**Example**
If `https://` _**`oldMyDomainName`**_ `.my.salesforce.com` is redirected to
`https://` _**`newMyDomainName`**_ `.my.salesforce.com`, the value of this field is

```
  newMyDomainName .my.salesforce.com

```

**Type**
String

**Description**
The path of the originating URL request, up to the first question mark (?). The path is also
used in the redirection target URL. However, this field doesn’t include the query string, if
present.

**Example**
If the user is redirected from
`https://MyOldCompany.my.site.com/shop?q=sneakers` to


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

`https://MyNewCompany.my.site.com/shop?q=sneakers`, the value of
this field is `/shop` .

```
REDIRECT_REASON

IS_BLOCKED_REDIRECTION

```

**Type**
String

**Description**
The reason for the hostname redirect event.

**Possible Values**

**•** `Redirected due to a hostname mismatch.` —The referring hostname
was redirected to the current My Domain equivalent.

**•** `Redirection suppressed to prevent Lightning Out`
`integration failure.` —The `*.force.com` site URL can’t be redirected for
[use with Lightning Out. To prevent issues, the original URL was processed as-is. To avoid](https://developer.salesforce.com/docs/component-library/documentation/en/lwc/lwc.lightning_out)
issues after `*.force.com` site hostname redirections are stopped, update hard-coded
references to the hostname in your Lightning Out integrations. For a Lightning Out code
[example that uses a site hostname, see Share Lightning Out Apps with Unauthenticated](https://developer.salesforce.com/docs/component-library/documentation/en/lwc/lwc.lightning_out_public_apps)
[Users in the Salesforce Lightning Component Library.](https://developer.salesforce.com/docs/component-library/documentation/en/lwc/lwc.lightning_out_public_apps)

**•** `Redirection was blocked because redirections for this`
`hostname are disabled.—` Only your last set of My Domain login hostnames
is redirected. Those redirections are blocked when the My Domain Routing option
**Redirect previous My Domain URLs to your current My Domain** is deselected or
because you removed your previous My Domain. That option applies to legacy
(non-enhanced) hostnames in production orgs until Spring ’25. In non-production orgs,
that option has no impact on redirections for legacy hostnames in Winter ’25 and later.
Non-production orgs include sandboxes, Developer Edition orgs, demo orgs, patch orgs,
scratch orgs, and Trailhead Playgrounds. For information

If the `SOURCE_HOSTNAME` is a legacy `*.force.com` site hostname, the redirection
was blocked because the **Redirect** _`previousSiteHostnames`_ **URLs to your**
**current My Domain site URLs** Routing option was deselected on the My Domain Setup
page. That option is available in production orgs until Spring ’25. In non-production orgs,
that option was removed in Winter ’25. Non-production orgs include sandboxes,
Developer Edition orgs, demo orgs, patch orgs, scratch orgs, and Trailhead Playgrounds.

**•** `Redirection was blocked because redirections for the`
`legacy SOURCE_HOSTNAME are no longer supported.` —If your org
was created before June 2022, Salesforce served the org on a different set of hostnames
until enhanced domains were deployed. The `SOURCE_HOSTNAME` is one of those
hostnames. For non-production orgs, redirections for those hostnames stopped in Winter
’25.

**Type**
Boolean

**Description**
Indicates whether the redirection was blocked.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Possible Values**

**•** `1` —The redirection was blocked and returned an HTTP 404 response.

**•** `0` —The redirection proceeded and returned an HTTP 301 or 307 response.

```
REFERRER

ORIGIN

TIMESTAMP_DERIVED

```

**Type**
String

**Description**
The absolute or partial address from which the request to the `SOURCE_HOSTNAME` came.
The `Referrer-Policy` HTTP Header of the request determines how much of the URL
is shared.

For example, if a user clicked a link to the `SOURCE_HOSTNAME` from a web page, and
that web page is on a different domain:

**•** if the `Referrer-Policy` HTTP Header is `no-referrer-when-downgrade`,
`REFERRER` includes the origin, path, and query-string parameters up to the first hash
( `#` ), if present.

**•** if the `Referrer-Policy` HTTP Header is
`strict-origin-when-cross-origin`, `REFERRER` includes the origin only.

**•** if the `Referrer-Policy` HTTP Header is `same-origin`, `REFERRER` is null.

**Examples**

**•** https://www.example.com

**•** https://www.example.com/page/page/index.htm

**•** https://www.example.com/page/index.htm?q="Salesforce"

**Type**
String

**Description**
The origin (protocol, hostname, and port) that caused the request to the
`SOURCE_HOSTNAME` . For example, if a website on a different domain makes an
XMLHttpRequest (XHR) to `SOURCE_HOSTNAME`, `ORIGIN` contains the base URL of that
website.

The port isn’t included in the origin information with all requests. `ORIGIN` can be null in
a number of situations, including but not limited to cross-origin requests and origins with a
restrictive `Referrer-Policy` header. For example, if the request to the
`SOURCE_HOSTNAME` is sent from a site external to Salesforce with a `RequestMode`
of `no-cors`, `ORIGIN` is null.

**Examples**

**•** https://www.example.com

**•** https://www.example.com:443

**Type**
DateTime


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ). The time zone is always GMT.

**Example**

```
                   2022-07-27T11:32:59.555Z.

```

```
USER_ID_DERIVED

CLIENT_IP

URI_ID_DERIVED

```

Usage

**Type**
String

**Description**
This field is unused in the HostnameRedirects event type. The value is always null.

**Type**
String

**Description**
The IP address of the client that made this request.

**Possible Values/Example**

```
  111.43.144.26

```

**Type**
String

**Description**
This field is unused in the HostnameRedirects event type. The value is always null.

Use the information in the Hostname Redirects event log to determine the hostnames to update in your org after you deploy a change
to your My Domain name. You can also use the log to develop communications to your customers and users about the changed
hostnames. For example, you can encourage users to use the new hostnames and update their bookmarks. For more information on
[the steps to take after a My Domain change, see Update Your Org and Test My Domain Changes in Salesforce Help.](https://help.salesforce.com/s/articleView?id=products.domain_name_deploy_update_test.htm&type=5&language=en_US)

To access the log, use the HostnameRedirects event type from the EventLogFile object. Alternatively, you can download the current
hostname redirections event log by clicking **Download Redirections Log** on the My Domain Setup page.

Each event, or each row in the redirection log, represents a redirection for a specific requested URL. Subsequent requests to the same
URL within the hour following that request, however, aren’t logged. If your last My Domain change included enhanced domains
[deployment, the log includes redirections for the old hostnames listed on My Domain URL Format Changes with Enhanced Domains](https://help.salesforce.com/s/articleView?id=products.domain_name_url_format_changes_enable_enhanced.htm&type=5&language=en_US)
[Deployment in Salesforce Help.](https://help.salesforce.com/s/articleView?id=products.domain_name_url_format_changes_enable_enhanced.htm&type=5&language=en_US)

Note: To keep the size of the log file manageable, the log includes one entry for each redirected hostname and path combination
within an hour. As a result, the log includes all redirected hostname and path combinations, but only includes the first redirection
within each hour.

For example, if `https://MyCompany.my.site.com/shop` is redirected at 02:01 PM and
`https://MyCompany.my.site.com/shop?q=sneakers` is redirected for another user at 02:02 PM, only the
redirection that occurred at 02:01 PM is captured for `MyCompany.my.site.com/shop` for that hour. But if


Standard Objects EventLogFile Supported Event Types

`https://MyCompany.my.site.com/help` is redirected at 2:05 PM, that redirection is captured on a new line because
the `MyCompany.my.site.com/help` hostname and path combination differs from `MyCompany.my.site.com/shop` .

Similarly, if the redirection of `https://MyCompany.my.site.com/contactUs` is blocked at 07:02 AM and
`https://MyCompany.my.site.com/contactUs` is redirected at 07:11 AM, only the blocked redirection for
`MyCompany.my.site.com/contactUs` is captured in the log for that hour.

Only one hostname redirection log file is available at a time. When the daily incremental event log file is generated during the daily
background process, the new file replaces the existing file. When you download the redirections log from the My Domain Setup page,
you get the latest daily log file in CSV format.

If the log file doesn’t exist, either the log generation process hasn’t run yet or there’s no redirection data to report for that 24-hour
window. The log file is generated only when at least one redirection occurred for the day.

To collect hostname redirection logs for multiple days, schedule a daily query of the Hostname Redirects event type via REST API. For
example, you can configure a cron job in Unix or a scheduled task in Windows to run the query.

Salesforce CLI Example

To use Salesforce CLI to query the Hostname redirects log, use the `sf data query` command to query the HostnameRedirects
EventType.

[First, download and install Salesforce CLI.](https://developer.salesforce.com/tools/salesforcecli)

**Example**
This Unix example authorizes Salesforce CLI to access your org and sets `orgAlias` to your org login URL. This method prompts
you to log in to your org via a browser to grant Salesforce CLI access. To query event log files, log in as a user with the View Event
Log Files and API Enabled permissions.

```
     sf org web login --alias orgAlias --instance-url https:// MyDomainName .my.salesforce.com

```

**Example response**

After you authenticate with a user via a browser, this response confirms that Salesforce CLI is authorized for use in your org.

```
     Successfully authorized admin@mycompany.com with org ID 00D00000000000aIW

```

Then export the HostnameRedirects log to a CSV file.

**Example**
This example exports the HostnameRedirects EventType to a CSV file in your org, where `orgAlias` is your org's alias within
Salesforce CLI.

```
     ORGALIAS= orgAlias ; QUERYRESULT=$(sf data query --target-org "$ORGALIAS" --query "SELECT

      LogDate, LogFile FROM EventLogFile WHERE EventType='HostnameRedirects' ORDER BY

     CreatedDate DESC LIMIT 1" --json); QUERYSTATUS=$(echo "$QUERYRESULT"|grep \"status\"|cut

      -d : -f 2|cut -d, -f 1); if [[ "$QUERYSTATUS" -eq 0 ]]; then LOGDATE=$(echo

     "$QUERYRESULT"|grep LogDate|cut -d \" -f 4|cut -d T -f 1); if [[ "$LOGDATE" == "" ]];

     then echo "No daily event log file exists for hostname redirects."; else

     DOWNLOADPATH=$(echo "$QUERYRESULT"|grep \"url\"|cut -d \" -f 4); ORGDISPLAY=$(sf org

     display --target-org "$ORGALIAS" --json 2> /dev/null); SESSION=$(echo "$ORGDISPLAY"|grep

     accessToken|cut -d \" -f 4); ORGURL=$(echo "$ORGDISPLAY"|grep instanceUrl|cut -d \" -f

     4); curl -H "Authorization: Bearer ${SESSION}" --silent ${ORGURL}${DOWNLOADPATH}/LogFile

      > HostnameRedirectEvent-${LOGDATE}.csv; fi; else echo "$QUERYRESULT"; fi

```


Standard Objects EventLogFile Supported Event Types

**Example CSV formatted response**

```
     "EVENT_TYPE","TIMESTAMP","REQUEST_ID","ORGANIZATION_ID","USER_ID","RUN_TIME",

     "CPU_TIME","URI","SESSION_KEY","LOGIN_KEY","MESSAGE","DOMAIN","SOURCE_HOSTNAME",

     "TARGET_HOSTNAME","PATH","REDIRECT_REASON","IS_BLOCKED_REDIRECTION","REFERRER",

     "ORIGIN","TIMESTAMP_DERIVED","USER_ID_DERIVED","CLIENT_IP","URI_ID_DERIVED"

     "HostnameRedirects","20220803011210","4kTkZZ1PzwSSHDkCagbl7-","00D000000000aIW",

     "","0","","","","","Redirection was blocked because redirections for the legacy

     SOURCE_HOSTNAME are no longer supported.","","ExperienceCloudSubdomain.force.com",

     "","","","0","https://partner.example.com/pagename.html","",

     "2022-08-03T01:12:10.015Z","","198.51.100.0"," "

     "HostnameRedirects","20220803022225","4kTkSZ1PzwSTHDkCagbl9-","00D000000000aIW",

     "","0","","","","","Redirection was blocked because redirections for the legacy

     SOURCE_HOSTNAME are no longer supported.","",

     "SalesforceSitesSubdomain.secure.force.com","","","","0","",

     "https://partner2.example.com","2022-08-03T02:22:25.015Z","","2001:DB8::",""

     "HostnameRedirects","20220803025230","4kNP4KyC_ddbI0GxqZ8Lz-","00D000000000aIW",

     "","0","","","","","Redirection prevented due to a hostname mismatch.","",

     "oldMyDomainName.my.salesforce.com","currentMyDomainName.my.salesforce.com","",

     "","0","https://www.example.com/login_hub.htm","https://www.example.com",

     "2022-08-03T02:52:30.015Z","","203.0.113.0",""

     "HostnameRedirects","20220803081241","4kTkSZ1PzwSTHDkCagbl9-","00D000000000aIW",

     "","0","","","","","Redirection was blocked because redirections for the legacy

     SOURCE_HOSTNAME are no longer supported.","",

     "SalesforceSitesSubdomain.secure.force.com","","","","0",

     "https://myDomainName.my.site.com/store/Page1","","2022-08-03T08:12:41.015Z","",

     "Salesforce.com IP",""

     "HostnameRedirects","20220803113801","4kNQs7BYKbSbIWGxqZ8Lz-","00D000000000aIW",

     "","0","","","","","Redirection prevented due to a hostname mismatch.","",

     "oldMyDomainName.lightning.force.com","currentMyDomainName.lightning.force.com",

     "","","0",

     "https://sandboxMyDomainName--SandboxName.sandbox.lightning.force.com/r/

     product__c/a00000000000000IAI/view",

     "https://sandboxMyDomainName--SandboxName.sandbox.lightning.force.com",

     "2022-08-03T11:38:01.015Z","","Salesforce.com IP",""

```

For more information on Salesforce CLI, see the Salesforce CLI Setup Guide, Salesforce CLI Command Reference, and the Salesforce DX
Developer Guide.

REST API Example

[To use REST API to query the Hostname Redirects event log, use the Query resource to retrieve field values from a record. Specify the](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_rest.meta/api_rest/resources_query.htm#topic-title)
fields you want to retrieve in the fields parameter and use the GET method of the resource.

**Example**
This example retrieves the HostnameRedirects event log based on `Field` and `EventType` via a GET request. Replace `token`
with your access token. In a production org, replace `MyDomainName` with your My Domain name. In a sandbox, replace
`MyDomainName.my.salesforce.com` with your org’s My Domain login hostname.

```
     curl https:// MyDomainName .my.salesforce.com/services/data/v66.0/query?q=SELECT+

     LogDate%2C+LogFile+FROM+EventLogFile+WHERE+EventType%3D%27HostnameRedirects%27

     +ORDER+BY+CreatedDate+DESC+LIMIT+1 -H "Authorization: Bearer token"

```


Standard Objects EventLogFile Supported Event Types

**Example raw response**

```
     {"totalSize":1,"done":true,"records":[{"attributes":

     {"type":"EventLogFile","url":"/services/data/v56.0/sobjects/EventLogFile/

     0AT00000003KxUSWA0"},"LogDate":"2022-08-03T00:00:00.000+0000","LogFile":"

     /services/data/v56.0/sobjects/EventLogFile/0AT00000003KxUSWA0/LogFile"}]}

```

The log file can be downloaded by using curl with the same Authorization header while setting the URL path to the `LogFile` value
from the output.

[For more information on accessing event log files via REST API, see Using Event Monitoring in the REST API Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.260.0.api_rest.meta/api_rest/using_resources_event_log_files.htm)

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Insecure External Assets Event Type

Insecure External Assets events contain information about external assets. External assets include images or videos accessed by users
over an insecure HTTP protocol. The event lists all your Salesforce pages that contain assets hosted insecurely on third-party sites that
users loaded with a Chrome, Firefox, Microsoft Edge, or Safari browser. The `INSECURE_URI` field contains the URI being used to load
the asset insecurely. The Insecure External Assets event type is available in the EventLogFile object in API version 42.0 and later.

Assets over HTTP can be manipulated through man-in-the-middle and other types of attacks. These attacks can trick users into sending
their Salesforce credentials to malicious sites. Always use HTTPS in your custom code and templates for any asset you’re loading from
external sites.

Important: Because HTTPS connections are required to load external assets, Insecure External Assets events no longer apply. In
Spring ’25 and later, this event type captures no data.

To view blocked redirections and content security policy (CSP) violations for your org, use the BrowserPolicyViolation object.

[For details about event monitoring, see the Trailhead Event Monitoring module or the REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
ASSET_TYPE

```

**Type**
String

**Description**
Type of insecure asset.

**Possible Values**

**•** `Base URI`

**•** `Connect`

**•** `Font`

**•** `Frame Ancestor` : External page that embeds the Salesforce page in an iframe

**•** `Frame`

**•** `Image`


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**•** `Media`

**•** `Object`

**•** `Other`

**•** `Plugin Types`

**•** `Script`

**•** `Style`

```
CLIENT_IP

CPU_TIME

DISPOSITION

DOCUMENT_URI

EVENT_TYPE

```

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

**Type**
String

**Description**
If the insecure external asset is related to your content security policy (CSP), the HTTP header
that identified the insecure asset.

Available in API version 61.0 and later.

**Possible Values**

**•** `enforce` —The `Content-Security-Policy` header identified the insecure
external asset.

**•** `report` —The `Content-Security-Policy-Report-Only` header identified
the insecure external asset.

**Type**
String

**Description**
URL of the page that contains the insecure asset, excluding the query parameter.

**Example**
https://company.my.salesforce.com/00XXXXXXXXX

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The type of event. The value is always `InsecureExternalAssets` .

```
INSECURE_URI

LOGIN_KEY

NETWORK_ID

ORGANIZATION_ID

REQUEST_ID

```

**Type**
String

**Description**
Insecure external asset URL being used to load an asset insecurely. For example, loading
Javascript libraries using **`http:`** `//ajax.googleapis.com/` in your custom code
logs an Insecure External Asset Event with the `INSECURE_URI` field set to this URL. Find
this reference in your code and update it to use **`https:`** `//ajax.googleapis.com/`
instead.

**Example**
http://pbs.twimg.com/profile_images/5699091412070816/Z4Stwts_normal.jpeg

**Type**
String

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
String

**Description**
The ID of the Experience Cloud site related to the request, if applicable.

Available in API version 61.0 and later.

**Type**
String

**Description**
The 15-character ID of the org.

**Example**
00D000000000123

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
RUN_TIME

SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

TYPE

```

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone is GMT.

**Type**
String

**Description**
Type of Salesforce page.

**Possible Values**

**•** `Appserver` —Page without My Domain subdomain (for example,
https://na44.salesforce.com)

**•** `Communities` —Customer Experience Cloud site

**•** `Email` —Email preview

**•** `Login` —Login page (for example, https://login.salesforce.com)

**•** `Mydomain` —Page on My Domain subdomain (for example,
https://mycompany.my.salesforce.com)

**•** `Sites` —Customer site

**•** `Static` —Static content (for example, https://sfdcstatic.com)

**•** `Unknown` —other type of page


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
UNIQUE_ID

URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

```

Usage

**Type**
String

**Description**
The 32-character ID of the event log file in which the insecure external asset event data is
found.

**Example**
44e128a5-ac7a-4c9a-be4c-224b6bf81b20

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using Salesforce services through the
UI or the API.

For example: `00590000000I1SNIA0` .

`UNIQUE_ID` is used by Salesforce Customer Support to troubleshoot any issues that occur.

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile


Standard Objects EventLogFile Supported Event Types

##### Insufficient Access Event Type

Insufficient Access events contain details about errors relating to insufficient account, case, contact, and opportunity record access, so
that you can troubleshoot and resolve access issues for your users.

Note: The Insufficient Access event type is disabled by default. You can enable this event type for a period of 24 hours by contacting
Salesforce Customer Support.

These insufficient access error scenarios are logged:

**•** The user can’t share a case, contact, or opportunity because the user doesn’t have permission to share the parent account or the
recipient of the share doesn’t currently have read access to the parent account.

**•** The user can’t change ownership of a case, contact, or opportunity because the user doesn’t have permission to share the parent
account or the new owner doesn’t currently have read access to the parent account.

**•** The user can’t change the parent account of a case, contact, or opportunity because the user doesn’t have permission to share the
new parent account or the owner of the case, contact, or opportunity doesn’t have read access to the new parent account.

Insufficient access errors resulting from bulk operations involving two or more records aren’t logged.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

[For more information on interpreting Insufficient Access events, see this knowledge article.](https://help.salesforce.com/s/articleView?id=000396437&type=1&language=en_US)

Fields

**Field** **Details**

```
ACCESS_ERROR

ACTUAL_LOGGED_IN_USER_ID

```

**Type**
String

**Description**
The type of insufficient access error that the user received. Valid values are:

**•** `DATA_NOT_AVAILABLE` —The record is no longer accessible. For example, a record
was deleted and moved to the Recycle Bin.

**•** `INVALID_TYPE` —The record type doesn’t exist.

**•** `NO_ACCESS` —The user doesn’t have the required access level to complete the
attempted action on the record.

**Example**

```
  NO_ACCESS

```

**Type**
Id

**Description**
The 15-character ID of the user who initiated the action that caused the insufficient access
error. For example, a user attempts to transfer ownership of a record to a teammate, but the
operation fails because the teammate doesn’t have the required access. In this scenario, the
`ACTUAL_LOGGED_IN_USER_ID` is the user who attempted to transfer access, and the
`USER_ID` is their teammate.

**Example**

```
  005XXXXXXXXXXXX

```


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
ENTITY_TYPE

ERROR_DESCRIPTION

ERROR_TIMESTAMP

EVENT_TYPE

ORGANIZATION_ID

RECORD_ID

```

**Type**
String

**Description**
The object for which the user received the insufficient access error. Access errors for the
account, case, contact, and opportunity objects are supported.

**Example**
Account

**Type**
String

**Description**
Description of the insufficient access error that the user received.

**Example**
User 005XXXXXXXXXXXX doesn't have full access for the record 001XXXXXXXXXXXX.

**Type**
String

**Description**
The time in GMT that the insufficient access error occurred.

**Example**

```
  20130715233322.670

```

**Type**
String

**Description**
The type of event. The value is always `InsufficientAccess` .

**Type**
Id

**Description**
The 15-character ID of the organization.

**Example**

```
  00DXXXXXXXXXXXX

```

**Type**
String

**Description**
The ID of the record that the user doesn’t have access to.

**Example**

```
  001XXXXXXXXXXXX

```


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
REQUEST_ID

REQUESTED_ACCESS_LEVEL

TIMESTAMP

TIMESTAMP_DERIVED

USER_ID

```

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

**Example**

```
  3nWgxWbDKWWDIk0FKfF5DV

```

**Type**
String

**Description**
The access level required by the user’s attempted action on the record. Valid values are:

**•** `DELETE`

**•** `FULL`

**•** `READ`

**•** `TRANSFER`

**•** `WRITE`

**Example**

```
  FULL

```

**Type**
String

**Description**
The access time of Salesforce services in GMT.

**Example**

```
  20130715233322.670

```

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

**Example**

```
  2015-07-27T11:32:59.555Z

```

**Type**
Id

**Description**
The 15-character ID of the user for whom the insufficient access error occurred, either when
the user couldn’t access a record, the user couldn’t complete an operation, or the user was


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

the intended recipient of a record transfer that failed because the user didn’t have the required
access.

**Example**

```
                   005XXXXXXXXXXXX

```

```
USER_ID_DERIVED

```

SEE ALSO:

**Type**
Id

**Description**
The 18-character case-insensitive ID of the user for whom the insufficient access error
occurred, either when the user couldn’t access a record or the user was the intended recipient
of a record transfer that wasn’t completed.

**Example**

```
  005XXXXXXXXXXXXIA0

```

EventLogFile Supported Event Types

EventLogFile

_Knowledge Article_ [: Interpret Insufficient Access Event Logs](https://help.salesforce.com/s/articleView?id=000396437&type=1&language=en_US)

##### Invocable Action Event Type

Invocable Action events capture the calls to Salesforce Invocable Actions. This is particularly useful to monitor actions invoked during
Agentforce flows. This event type is available in API versions 64.0 and later.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
ACTION_NAME

ACTION_TYPE

ACTION_VERSION

```

**Type**
String

**Description**
Name of the action.

**Type**
String

**Description**
InvocableActionType being referenced.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The invocable action version.

```
API_CALLER

BOT_IDENTIFIER

BOT_SESSION_IDENTIFIER

DURATION

EVENT_TYPE

FLOW_PROCESS_TYPE

FLOW_VERSION_ID

ORGANIZATION_ID

```

**Type**
String

**Description**
Identifier of the API caller. This is only populated when the
action is invoked from a REST API call

**Type**
string

**Description**
The ID of the bot.

**Type**
string

**Description**
The bot session ID.

**Type**
String

**Description**
Time (in nanos) taken to process this set of requests.

**Type**
String

**Description**
The type of event. The value is always `InvocableAction` .

**Type**
String

**Description**
The process type of the calling flow.

**Type**
String

**Description**
The ID of the version of the calling flow.

**Type**
Id

**Description**
The number of invoked requests.


Standard Objects EventLogFile Supported Event Types

```
PLANNER_IDENTIFIER

REQUEST_COUNT

REQUEST_ID

TIMESTAMP

TIMESTAMP_DERIVED

USER_ID

##### Knowledge Article View Event Type

```

**Type**
string

**Description**
The ID of the agent planner.

**Type**
Number

**Description**
The number of invoked requests.

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same REQUEST_ID.

**Type**
String

**Description**
The access time of Salesforce services in GMT.

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format (YYYY-MM-DDTHH:MM:SS.sssZ). For example:
2015-07-27T11:32:59.555Z. Timezone is GMT.

**Type**
String

**Description**
ID of the user employing salesforce.com services, whether
through the user interface or API

Knowledge Article View events contain user activity with your knowledge base.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**


Standard Objects EventLogFile Supported Event Types

```
ARTICLE_ID

ARTICLE_STATUS

ARTICLE_VERSION

ARTICLE_VERSION_ID

CONTEXT

ENTITY

```

**Type**
Id

**Description**
The 15-character ID of the article.

For example: `00Dxx0000001gEb` .

**Type**
Character

**Description**
Possible values are:

**•** `D` —Draft

**•** `O` —Online

**•** `A` —Archived

**Type**
Number

**Description**
Article version number.

For example: `2` .

**Type**
Id

**Description**
The 15-character ID of the article version.

For example: `ka0R00000005rt6` .

**Type**
String

**Description**
Context of the request.

**Description**
Possible values are:

**•** `Apex`

**•** `API`

**•** empty string

**Type**
String

**Description**
Entity requested.

For example: `Knowledge__kav` .


Standard Objects EventLogFile Supported Event Types

```
EVENT_TYPE

LANGUAGE

LARGE_LANGUAGE_MODEL

LAST_VERSION

ORGANIZATION_ID

REQUEST_ID

```

**Type**
String

**Description**
The type of event. The value is always
`KnowledgeArticleView` .

**Type**
String

**Description**
iso-code of the language.

For example: `en_US` /

**Example**

**Type**
String

**Description**
The name of the large language model (LLM) that generated
the knowledge article version.

**Type**
Boolean

**Description**
`True` if it is the last version.

Possible values are:

**•** `True`

**•** `False`

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .


Standard Objects EventLogFile Supported Event Types

```
SESSION_ID

TIMESTAMP

TIMESTAMP_DERIVED

USER_ID

USER_ID_DERIVED

USER_TYPE

```

**Type**
String

**Description**
Session ID of the request.

For example:
`gV7pCSW2vGaaJNFi3GSpuPIjNbKVbSxRvx34LJsIvuc=` .

**Example**

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . The
timezone is GMT.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

**Type**
Character

**Description**
User type of the request.

Possible values are:

**•** `A` —App


Standard Objects EventLogFile Supported Event Types

**•** `C` —Customer Portal

**•** `P` —Partner Portal

**•** `G` —guest

**•**

##### Lightning Error Event Type

Lightning Error events represent errors that occurred during user interactions with Lightning Experience and the Salesforce mobile app.
This event type is available in the EventLogFile object in API version 39.0 and later.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
APP_NAME

BROWSER_NAME

BROWSER_VERSION

CLIENT_GEO

CLIENT_ID

```

**Type**
String

**Description**
The name of the application that the user accessed.

**Type**
String

**Description**
The name of the browser that the user accessed.

**Example**
`Chrome`, `Safari`

**Type**
String

**Description**
The version of the browser that the user accessed in `major.minor version` format.
Some browsers don’t provide a minor version.

**Type**
String

**Description**
The geolocation of the client in the form of `<Country>/<State|Province>` .

**Example**

```
  United States/California

```

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The API client ID.

```
CLIENT_IP

COMPONENT_NAME

CONNECTION_TYPE

DEVICE_ID

```

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”.

**Example**

```
  96.43.144.26

```

**Type**
String

**Description**
The internal name of the standard component that generated the error. The Salesforce
developer assigned the name when the standard component was created.

**Example**
`SaveEdit`, `Lead.CCPM_sendSMS`, `ChangeOwnerOne`

**Type**
String

**Description**
The type of connection.

**Possible Values**

**•** `CDMA1x`

**•** `CDMA`

**•** `EDGE`

**•** `EVDO0`

**•** `EVDOA`

**•** `EVDOB`

**•** `GPRS`

**•** `HRPD`

**•** `HSDPA`

**•** `HSUPA`

**•** `LTE`

**•** `WIFI`

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The unique identifier used to identify a device when tracking events. `DEVICE_ID` is a
generated value that’s created when the mobile app is initially run after installation.

```
DEVICE_MODEL

DEVICE_PLATFORM

DEVICE_SESSION_ID

EVENT_TYPE

LOGIN_KEY

```

**Type**
String

**Description**
The name of the device model.

**Example**
`iPad`, `iPhone`

**Type**
String

**Description**
The type of application experience in `name:experience:form` format.

**Possible Values**

**•** `name` : `APP_BUILDER`, `CUSTOM`, `S1`, `SFX`

**•** `experience` : `BROWSER`, `HYBRID`

**•** `form` : `DESKTOP`, `PHONE`, `TABLET`

**Type**
Id

**Description**
The unique identifier of the user’s session based on page load time. If the user reloads a page,
it starts a new session.

**Example**

```
  321a1ddfaf924803a075f1e69fc87bc06f53ccd0

```

**Type**
String

**Description**
The type of event. The value is always `LightningError` .

**Type**
String

**Description**
The string that ties together all events in a user’s login session. It starts with a login event
and ends with either a logout event or the user session expiring.

**Example**

```
  GeJCsym5eyvtEK2I

```


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
MESSAGE

ORGANIZATION_ID

OS_NAME

OS_VERSION

PAGE_APP_NAME

PAGE_CONTEXT

PAGE_ENTITY_ID

```

**Type**
String

**Description**
The error message generated.

**Type**
String

**Description**
The 15-character ID of the org.

**Example**

```
  00D000000000123

```

**Type**
String

**Description**
The operating system name, derived from `USER_AGENT` .

**Example**
`Android`, `iOS`, `OSX`, `Windows`

**Type**
String

**Description**
The operating system version, derived from `USER_AGENT` .

**Type**
String

**Description**
The internal name of the application that the user accessed from the App Launcher.

**Example**

```
  LightningSales

```

**Type**
String

**Description**
Context of the page where the event occurred.

**Example**

```
  clients:cardsContainer

```

**Type**
Id


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The unique entity identifier of the event.

**Example**

```
                   0013000000I3zJAAAZ

```

```
PAGE_ENTITY_TYPE

PAGE_START_TIME

PAGE_URL

REQUEST_ID

SDK_APP_TYPE

```

**Type**
String

**Description**
The entity type of the event.

**Example**
`Task`, `Account`

**Type**
Number

**Description**
The time when the page was initially loaded, measured in milliseconds.

**Example**

```
  1471564788642

```

**Type**
String

**Description**
Relative URL of the top-level Lightning Experience or Salesforce mobile app page that the
user opened. The page can contain one or more Lightning components. Multiple record IDs
can be associated with `PAGE_URL` .

**Example**

```
  /sObject/0064100000JXITSAA5/view

```

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

**Example**

```
  3nWgxWbDKWWDIk0FKfF5DV

```

**Type**
String

**Description**
The mobile SDK application type.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Possible Values**

**•** `HYBRID`

**•** `HYBRIDLOCAL`

**•** `HYBRIDREMOTE`

**•** `NATIVE`

**•** `REACTNATIVE`

```
SDK_APP_VERSION

SDK_VERSION

SESSION_KEY

STACK_TRACE

TIMESTAMP

```

**Type**
String

**Description**
The mobile SDK application version number.

**Example**

```
  5.0

```

**Type**
String

**Description**
The mobile SDK version number.

**Example**

```
  2.1.0

```

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify all events in Lightning
Experience within a session. When a user logs out and logs in again, a new session is started.

**Example**

```
  cdd09305cb6babf34059e27f70e47f1b11dec868

```

**Type**
String

**Description**
The stack trace contains the location in the code where the error occurred along with the
calling frames that led to the error.

**Type**
String

**Description**
The access time of Salesforce services in GMT.

**Example**

```
  20130715233322.670

```


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
TIMESTAMP_DERIVED

UI_EVENT_ID

UI_EVENT_SEQUENCE_NUM

UI_EVENT_SOURCE

```

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

**Example**
`2015-07-27T11:32:59.555Z` . The timezone is GMT.

**Type**
String

**Description**
ID of the Lightning event type.

**Possible Values**

**•** `ltng:error`

**•** `ltng:interaction`

**•** `ltng:pageView`

**•** `ltng:performance`

**Type**
Number

**Description**
An auto-incremented sequence number of the current event since the session started.

**Type**
String

**Description**
The source of the error event.

**Examples**
Here are some examples of error flags returned in this field.

**•** `AuraError`

**•** `Error`

**•** `InvalidStateError`

**•** `RangeError`

**•** `ReferenceError`

**•** `SecurityError`

**•** `SyntaxError`

**•** `TypeError`

**•** `unknown`


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
UI_EVENT_TIMESTAMP

UI_EVENT_TYPE

USER_AGENT

USER_ID

USER_ID_DERIVED

USER_TYPE

```

**Type**
Number

**Description**
The time at which this event occurred, measured in milliseconds.

**Example**

```
  1479769912796

```

**Type**
String

**Description**
The type of error event.

**Example**
`error`, `info`, `warn`

**Type**
String

**Description**
The numeric code for the type of client used to make the request (for example, browser,
application, or API) as a string.

**Type**
String

**Description**
The 15-character ID of the user accessing Salesforce services through the UI or API.

**Example**

```
  00530000009M943

```

**Type**
Id

**Description**
The 18-character case-insensitive ID of the user who’s using Salesforce services through the
UI or the API.

**Example**

```
  00590000000I1SNIA0

```

**Type**
String

**Description**
The category of user license of the user accessing Salesforce services through the UI or API.

**Possible Values**

**•** `A` : Automated Process


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**•** `b` : High Volume Portal

**•** `C` : Customer Portal User

**•** `D` : External Who

**•** `F` : Self Service

**•** `G` : Guest

##### • L : Package License Manager

**•** `N` : Salesforce to Salesforce

**•** `n` : CSN Only

**•** `O` : Power Custom

**•** `o` : Custom

**•** `P` : Partner

**•** `p` : Customer Portal Manager

**•** `S` : Standard

**•** `X` : Salesforce Administrator

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Lightning Interaction Event Type

Lightning Interaction events track user actions in Lightning Experience and the Salesforce mobile app, such as the user clicking, tapping,
or scrolling on a page. This event type is available in the EventLogFile object in API version 39.0 and later.

Warning: The Lightning Interaction Event type is a best effort logging of user interactions but is not intended to meet privacy
and security audit requirements. Not all interactions or CRUD operations are tracked and data loss may occur.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
APP_NAME

BROWSER_NAME

```

**Type**
String

**Description**
The name of the application that the user accessed.

**Type**
String

**Description**
The name of the browser that the user accessed.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Example**
`Chrome`, `Safari`

```
BROWSER_VERSION

CLIENT_GEO

CLIENT_ID

CLIENT_IP

COMPONENT_NAME

CONNECTION_TYPE

```

**Type**
String

**Description**
The version of the browser that the user accessed in `major.minor version` format.
Some browsers don’t provide a minor version.

**Type**
String

**Description**
The geolocation of the client in the form of `<Country>/<State|Province>` .

**Example**

```
  United States/California

```

**Type**
String

**Description**
The API client ID.

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such
as a login from AppExchange) is shown as “Salesforce.com IP”.

**Example**

```
  96.43.144.26

```

**Type**
String

**Description**
The internal name of the standard component that the user interacted with. The Salesforce
developer assigned the name when the standard component was created.

**Example**
`SaveEdit`, `Lead.CCPM_sendSMS`, `ChangeOwnerOne`

**Type**
String

**Description**
The type of connection.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Possible Values**

**•** `CDMA1x`

**•** `CDMA`

**•** `EDGE`

**•** `EVDO0`

**•** `EVDOA`

**•** `EVDOB`

**•** `GPRS`

**•** `HRPD`

**•** `HSDPA`

**•** `HSUPA`

**•** `LTE`

**•** `WIFI`

```
DEVICE_ID

DEVICE_MODEL

DEVICE_PLATFORM

DEVICE_SESSION_ID

```

**Type**
String

**Description**
The unique identifier used to identify a device when tracking events. `DEVICE_ID` is a
generated value that’s created when the mobile app is initially run after installation.

**Type**
String

**Description**
The name of the device model.

**Example**
`iPad`, `iPhone`

**Type**
String

**Description**
The type of application experience in `name:experience:form` format.

**Possible Values**

**•** `name` : `APP_BUILDER`, `CUSTOM`, `S1`, `SFX`

**•** `experience` : `BROWSER`, `HYBRID`

**•** `form` : `DESKTOP`, `PHONE`, `TABLET`

**Type**
Id


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The unique identifier of the user’s session based on page load time. When the user reloads
a page, a new session is started.

**Example**

```
                   321a1ddfaf924803a075f1e69fc87bc06f53ccd0

```

```
DURATION

EVENT_TYPE

GRANDPARENT_UI_ELEMENT

LOGIN_KEY

ORGANIZATION_ID

OS_NAME

```

**Type**
Number

**Description**
The duration in milliseconds since the page start time.

**Type**
String

**Description**
The type of event. The value is always `LightningInteraction` .

**Type**
String

**Description**
Grandparent scope of the page element where the event occurred.

**Type**
String

**Description**
The string that ties together all events in a user’s login session. It starts with a login event
and ends with either a logout event or the user session expiring.

**Example**

```
  GeJCsym5eyvtEK2I

```

**Type**
String

**Description**
The 15-character ID of the org.

**Example**

```
  00D000000000123

```

**Type**
String

**Description**
The operating system name, derived from `USER_AGENT` .

**Example**
`Android`, `iOS`, `OSX`, `Windows`


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
OS_VERSION

PAGE_APP_NAME

PAGE_CONTEXT

PAGE_ENTITY_ID

PAGE_ENTITY_TYPE

PAGE_START_TIME

```

**Type**
String

**Description**
The operating system version, derived from `USER_AGENT` .

**Type**
String

**Description**
The internal name of the application that the user accessed from the App Launcher.

**Example**

```
  LightningSales

```

**Type**
String

**Description**
Context of the page where the event occurred.

**Example**

```
  clients:cardsContainer

```

Note: A value of `UNKNOWN` means that the page hasn't finished loading, so the
context can't be identified.

**Type**
Id

**Description**
The unique entity identifier of the event.

**Example**

```
  0013000000I3zJAAAZ

```

**Type**
String

**Description**
The entity type of the event.

**Example**
`task`, `contacts`

Note: A value of `UNKNOWN` means that the page hasn't finished loading or the
page isn't displaying a record, so the entity type can't be identified.

**Type**
Number

**Description**
The time when the page was initially loaded, measured in milliseconds.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Example**

```
                   1471564788642

```

```
PAGE_URL

PARENT_UI_ELEMENT

RECORD_ID

RECORD_TYPE

RELATED_LIST

```

**Type**
String

**Description**
Relative URL of the top-level Lightning Experience or Salesforce mobile app page that the
user opened. The page can contain one or more Lightning components. Multiple record
IDs can be associated with `PAGE_URL` .

**Example**

```
  /sObject/0064100000JXITSAA5/view

```

Note: A value of `UNKNOWN` means that the page hasn't finished loading, so the
URL can't be identified.

**Type**
String

**Description**
Parent scope of the page element where the event occurred.

**Type**
String array

**Description**
The IDs of one or more records that the user interacted with. For more information on the
user interaction, see `UI_EVENT_TYPE` and `UI_EVENT_SOURCE` fields.

**Example**

```
  ["5004100000JaGGLAA3", "5004100000Dn79CAAR",

  "50041000007KeugAAC"]

```

**Type**
String

**Description**
The type of record object that the user interacted with.

**Example**
`Account`, `Opportunity`

**Type**
String

**Description**
The type of related list that the user clicked.

**Example**

```
  Opportunity

```


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
REQUEST_ID

SDK_APP_TYPE

SDK_APP_VERSION

SDK_VERSION

SESSION_KEY

```

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

**Example**

```
  3nWgxWbDKWWDIk0FKfF5DV

```

**Type**
String

**Description**
The mobile SDK application type.

**Possible Values**

**•** `HYBRID`

**•** `HYBRIDLOCAL`

**•** `HYBRIDREMOTE`

**•** `NATIVE`

**•** `REACTNATIVE`

**Type**
String

**Description**
The mobile SDK application version number.

**Example**

```
  5.0

```

**Type**
String

**Description**
The mobile SDK version number.

**Example**

```
  2.1.0

```

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify all events in Lightning
Experience within a session. When the user logs out and logs in again, a new session is
started.

**Example**

```
  cdd09305cb6babf34059e27f70e47f1b11dec868

```


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
TARGET_UI_ELEMENT

TIMESTAMP

TIMESTAMP_DERIVED

UI_EVENT_ID

UI_EVENT_SEQUENCE_NUM

UI_EVENT_SOURCE

```

**Type**
String

**Description**
The target page element where the event occurred.

**Example**

```
  tabitem-link

```

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

**Example**
`2015-07-27T11:32:59.555Z` . The timezone is GMT.

**Type**
String

**Description**
Id of the Lightning event type.

**Possible Values**

**•** `ltng:error`

**•** `ltng:interaction`

**•** `ltng:pageView`

**•** `ltng:performance`

**Type**
Number

**Description**
An auto-incremented sequence number of the current event since the session started.

**Type**
String

**Description**
The user action on the record or records in `RECORD_ID` . This field’s value indicates whether
the user’s action was on a single record or multiple records. For example, `read` indicates


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

that one record was read (such as on a record detail page); `reads` indicates that multiple
records were read (such as in a list view).

**Examples**

**•** `click`

**•** `create`

**•** `delete`

**•** `hover`

**•** `read`

**•** `update`

```
UI_EVENT_TIMESTAMP

UI_EVENT_TYPE

USER_AGENT

USER_ID

USER_ID_DERIVED

```

**Type**
Number

**Description**
The time at which this event occurred, measured in milliseconds.

**Example**

```
  1479769912796

```

**Type**
String

**Description**
The type of interaction with the records in `RECORD_ID` .

**Example**
`crud`, `system`, `user`, `userInteraction`

**Type**
String

**Description**
The numeric code for the type of client used to make the request (for example, the browser,
application, or API) as a string.

**Type**
String

**Description**
The 15-character ID of the user accessing Salesforce services through the UI or API.

**Example**

```
  00530000009M943

```

**Type**
Id


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The 18-character case-insensitive ID of the user who’s using Salesforce services through
the UI or the API.

**Example**

```
                   00590000000I1SNIA0

```

```
USER_TYPE

```

SEE ALSO:

**Type**
String

**Description**
The category of user license of the user accessing Salesforce services through the UI or API.

**Possible Values**

**•** `A` : Automated Process

**•** `b` : High Volume Portal

**•** `C` : Customer Portal User

**•** `D` : External Who

**•** `F` : Self Service

**•** `G` : Guest

##### • L : Package License Manager

**•** `N` : Salesforce to Salesforce

**•** `n` : CSN Only

**•** `O` : Power Custom

**•** `o` : Custom

**•** `P` : Partner

**•** `p` : Customer Portal Manager

**•** `S` : Standard

**•** `X` : Salesforce Administrator

EventLogFile Supported Event Types

EventLogFile

##### Lightning Logger Event Type

Lightning Logger events contain information from observed Lightning component logs. This event type is available in the EventLogFile
object in API version 58.0 and later.

To enable Lightning Logger events, from Setup, in the Quick Find box, enter _`event`_, and then select **Event Monitoring Settings** . Turn
on Lightning Logger Events.

Note: The browser sends Lightning Logger event logs to the server in batches. Batches are sent when the user interacts with the
page and when the page closes or refreshes. If the user experiences connectivity issues or if their login session expires due to


Standard Objects EventLogFile Supported Event Types

browser inactivity, any pending Lightning Logger event logs on the browser are erased. There isn’t a way to retrieve these lost
logs.

The limit for Lightning Logger events is 30,000 events per minute per organization. Burst capacity may support up to 45,000-50,000
events per minute, but this is not guaranteed. The `MESSAGE` field shows details about what's logged when the limit is hit.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
APP_NAME

BROWSER_NAME

BROWSER_VERSION

CLIENT_GEO

CLIENT_ID

CLIENT_IP

```

**Type**
String

**Description**
The name of the application the user accessed.

**Type**
String

**Description**
The name of the browser that the user accessed.

**Example**
Chrome, IE, Safari, Gecko

**Type**
String

**Description**
The user’s browser version in `major.minor` format. Some
browsers don’t provide a minor version.

**Type**
String

**Description**
The geolocation of the client in the form of
<Country>/<State|Province>.

**Example**
United States/California

**Type**
String

**Description**
The API client ID.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP, such as a login from AppExchange, is
shown as “Salesforce.com IP”.

**Example**

```
                              96.43.144.26

```

```
CONNECTION_TYPE

DEVICE_MODEL

DEVICE_PLATFORM

```

**Type**
String

**Description**
The type of connection.

**Possible Values**

**•** `CDMA1x`

**•** `CDMA`

**•** `EDGE`

**•** `EVDO0`

**•** `EVDOA`

**•** `EVDOB`

**•** `GPRS`

**•** `HRPD`

**•** `HSDPA`

**•** `HSUPA`

**•** `LTE`

**•** `WIFI`

**Type**
String

**Description**
The name of the device model.

**Example**
iPad, iPhone

**Type**
String

**Description**
The type of application experience in
`name:experience:form` format.

**Possible Values**
Name

**•** `APP_BUILDER`

**•** `CUSTOM`


Standard Objects EventLogFile Supported Event Types

**•** `S1`

**•** `SFX`

Experience

**•** `BROWSER`

**•** `HYBRID`

Form

**•** `DESKTOP`

**•** `PHONE`

**•** `TABLET`

```
DEVICE_SESSION_ID

EVENT_TYPE

LOGIN_KEY

MESSAGE

```

**Type**
Id

**Description**
The unique identifier of the user’s session based on page load
time. When the user reloads a page, a new session is started.

**Example**
321a1ddfaf924803a075f1e69fc87bc06f53ccd0

**Type**
String

**Description**
The type of event. The value is always `LightningLogger` .

**Type**
String

**Description**
The string that ties together all events in a user’s login session.
It starts with a login event and ends with either a logout event
or the user session expiring.

**Example**
GeJCsym5eyvtEK2I

**Type**
String

**Description**
The message passed to the `lightning/logger log()`
method. The message can be a JSON object or a string. String
length is limited to 4 KB (4096 characters).

If you hit the logger limit, subsequent events are muted for a
minute. During this time, the message field is replaced with
this text: `Rate limiting hit for this`
`organization.` Lightning Logger events resume when
the limit resets in the next minute.


Standard Objects EventLogFile Supported Event Types

```
ORGANIZATION_ID

OS_NAME

OS_VERSION

PAGE_CONTEXT

PAGE_ENTITY_ID

PAGE_ENTITY_TYPE

PAGE_URL

```

**Type**
String

**Description**
The 15-character ID of the org.

**Example**
00D000000000123

**Type**
String

**Description**
The operating system name, derived from the User Agent.

**Example**
Android, iOS, OSX, Windows

**Type**
String

**Description**
The operating system version, derived from the User Agent.

**Type**
String

**Description**
The name of the component hosting the main page content.

**Example**
clients:cardsContainer

**Type**
Id

**Description**
The entity ID (if any) of the record being displayed.

**Example**
0013000000I3zJAAAZ

**Type**
String

**Description**
The entity type of the page being displayed.

**Example**
Task, contacts

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
Relative URL of the top-level Lightning Experience or Salesforce
mobile app page that the user opened. The page can contain
one or more Lightning components. Multiple record IDs can
be associated with `PAGE_URL` .

**Example**
/sObject/0064100000JXITSAA5/view

```
REQUEST_ID

SDK_APP_TYPE

SDK_APP_VERSION

SDK_VERSION

```

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

**Example**
3nWgxWbDKWWDIk0FKfF5DV

**Type**
String

**Description**
The mobile SDK application type.

**Possible Values**

**•** `HYBRID`

**•** `HYBRIDLOCAL`

**•** `HYBRIDREMOTE`

**•** `NATIVE`

**•** `REACTNATIVE`

**Type**
String

**Description**
The mobile SDK application version number.

**Example**
5.0

**Type**
String

**Description**
The mobile SDK version number.

**Example**
2.1.0


Standard Objects EventLogFile Supported Event Types

```
SEQUENCE

SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

UI_EVENT_RELATIVE_TIMESTAMP

UI_EVENT_TIMESTAMP

```

**Type**
Number

**Description**
An auto-incremented sequence number of the current event
since the session started.

**Type**
String

**Description**
The user’s unique session ID. Use this value to identify all events
in Lightning Experience within a session. When the user logs
out and logs in again, a new session is started.

**Example**
cdd09305cb6babf34059e27f70e47f1b11dec868

**Type**
String

**Description**
The access time of Salesforce services in GMT.

**Example**
20130715233322.670

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format (YYYY-MM-DDTHH:MM:SS.sssZ).

**Example**
2015-07-27T11:32:59.555Z. The timezone is GMT.

**Type**
Number

**Description**
Difference in milliseconds between when the message was
logged and when the browser tab was opened.

**Example**
29322.23

**Type**
Number

**Description**
The time at which this event occurred, measured in
milliseconds.


Standard Objects EventLogFile Supported Event Types

**Example**

```
USER_ID

USER_ID_DERIVED

USER_TYPE

```

**Type**
String

**Description**
The 15-character ID of the user accessing Salesforce services
through the UI or API.

**Example**
00530000009M943

**Type**
Id

**Description**
The 18-character case-insensitive ID of the user who’s using
Salesforce services through the UI or the API.

**Example**
00590000000I1SNIA0

**Type**
String

**Description**
The category of user license of the user accessing Salesforce
services through the UI or API.

**Possible Values**

**•** `A` : Automated Process

**•** `b` : High Volume Portal

**•** `C` : Customer Portal User

**•** `D` : External Who

**•** `F` : Self-Service

**•** `G` : Guest

**•** `L` : Package License Manager

**•** `N` : Salesforce to Salesforce

**•** `n` : CSN Only

**•** `O` : Power Custom

**•** `o` : Custom

**•** `P` : Partner

**•** `p` : Customer Portal Manager

**•** `S` : Standard

**•** `X` : Salesforce Administrator


Standard Objects EventLogFile Supported Event Types

##### Lightning Page View Event Type

Lightning Page View events represent information about the page on which the event occurred in Lightning Experience and the Salesforce
mobile app, such as the page's load time. This event type is available in the EventLogFile object in API version 39.0 and later.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
APP_NAME

BROWSER_NAME

BROWSER_VERSION

CLIENT_GEO

CLIENT_ID

CLIENT_IP

```

**Type**
String

**Description**
The name of the application that the user accessed.

**Type**
String

**Description**
The name of the browser that the user accessed.

**Example**
`Chrome`, `Safari`

**Type**
String

**Description**
The version of the browser that the user accessed in `major.minor version` format.
Some browsers don’t provide a minor version.

**Type**
String

**Description**
The geolocation of the client in the form of `<Country>/<State|Province>` .

**Example**

```
  United States/California

```

**Type**
String

**Description**
The API client ID.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as `Salesforce.com IP` .

**Example**

```
                   96.43.144.26

```

```
CONNECTION_TYPE

DEVICE_ID

DEVICE_MODEL

DEVICE_PLATFORM

```

**Type**
String

**Description**
The type of connection.

**Possible Values**

**•** `CDMA1x`

**•** `CDMA`

**•** `EDGE`

**•** `EVDO0`

**•** `EVDOA`

**•** `EVDOB`

**•** `GPRS`

**•** `HRPD`

**•** `HSDPA`

**•** `HSUPA`

**•** `LTE`

**•** `WIFI`

**Type**
String

**Description**
The unique identifier used to identify a device when tracking events. `DEVICE_ID` is a
generated value that’s created when the mobile app is initially run after installation.

**Type**
String

**Description**
The name of the device model.

**Example**
`iPad`, `iPhone`

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The type of application experience in `name:experience:form` format.

**Possible Values**

**•** `name` : `APP_BUILDER`, `CUSTOM`, `S1`, `SFX`

**•** `experience` : `BROWSER`, `HYBRID`

**•** `form` : `DESKTOP`, `PHONE`, `TABLET`

```
DEVICE_SESSION_ID

DURATION

EFFECTIVE_PAGE_TIME

EFFECTIVE_PAGE_TIME_DEVIATION

EFFECTIVE_PAGE_TIME_DEVIATION_ERROR_TYPE

```

**Type**
Id

**Description**
The unique identifier of the user’s session based on page load time. When the user reloads
a page, a new session is started.

**Example**

```
  321a1ddfaf924803a075f1e69fc87bc06f53ccd0

```

**Type**
Number

**Description**

If the page completes loading, then `DURATION` indicates the duration of time in milliseconds
between `PAGE_START_TIME` and when the loading completes. In this case, `DURATION`
corresponds to `EFFECTIVE_PAGE_TIME` .

If the page doesn't complete loading, then `DURATION` indicates the duration of time in
milliseconds between `PAGE_START_TIME` and when the user navigates to another page.

**Type**
Double

**Description**
Indicates how many milliseconds it takes for the page to load before a user can interact with
the page. Multiple factors can affect effective page time (EPT), such as network speed,
hardware performance, or page complexity.

**Type**
Boolean

**Description**
When a deviation is detected, `EFFECTIVE_PAGE_TIME_DEVIATION` records `true` .
The default value is `false` .

**Type**
String

**Description**
Indicates the origin of an error. This field is populated when
EFFECTIVE_PAGE_TIME_DEVIATION_REASON contains the PAGE_HAS_ERROR value.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Possible Values**

**•** `CUSTOM` —An error originating from the customer's system or network.

**•** `SYSTEM` —An error originating in Salesforce.

```
EFFECTIVE_PAGE_TIME_DEVIATION_REASON

EVENT_TYPE

GRANDPARENT_UI_ELEMENT

LOGIN_KEY

```

**Type**
String

**Description**
The reason for deviation in page loading time.

**Possible Values**

**•** `PageHasError` —An undefined page loading error occurred.

**•** `PageNotLoaded` —If a customer navigates away from a page while loading processes
are in progress, the page doesn't finish loading.

**•** `PreviousPageNotLoaded` —When navigating to a new page, and the previous
page hasn't completed loading, the next page is considered to have a deviation.
Incomplete loading processes on a previous page can affect how the next page loads.

**•** `InteractionsBeforePageLoaded` —A user interacts with a page element
before the page is fully loaded.

**•** `PageInBackgroundBeforeLoaded` —A background loading process runs on a
page. Background processes run when a user navigates away from a page to another
browser tab. The browser de-prioritizes the page in the background until the user activates
the page’s tab. Because a user can leave a page in the background for a long time, the
page is expected to have a high Effective Page Time (EPT).

**Type**
String

**Description**
The type of event. The value is always `LightningPageView` .

**Type**
String

**Description**
The grandparent scope of the page element where the event occurred.

**Type**
String

**Description**
The string that ties together all events in a user’s login session. It starts with a login event
and ends with either a logout event or the user session expiring.

**Example**

```
  GeJCsym5eyvtEK2I

```


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
ORGANIZATION_ID

OS_NAME

OS_VERSION

PAGE_APP_NAME

PAGE_CONTEXT

PAGE_ENTITY_ID

```

**Type**
String

**Description**
The 15-character ID of the org.

**Example**

```
  00D000000000123

```

**Type**
String

**Description**
The operating system name, derived from `USER_AGENT` .

**Example**
`Android`, `iOS`, `OSX`, `Windows`

**Type**
String

**Description**
The operating system version, derived from `USER_AGENT` .

**Type**
String

**Description**
The internal name of the application that the user accessed from the App Launcher.

**Example**

```
  LightningSales

```

**Type**
String

**Description**
The name of the component hosting the main content of the page.

**Example**

```
  clients:cardsContainer

```

**Type**
Id

**Description**
The ID of the record that the user accessed which triggered the event on the page.

**Example**

```
  0013000000I3zJAAAZ

```


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
PAGE_ENTITY_TYPE

PAGE_FLEXI_PAGE_NAME_OR_ID

PAGE_FLEXI_PAGE_TYPE

PAGE_START_TIME

PAGE_URL

PARENT_UI_ELEMENT

```

**Type**
String

**Description**
The entity type of the event.

**Example**
`Task`, `contacts`

**Type**
String

**Description**
The page name or identifier.

**Example**

```
  runtime_sales_seller_home__SellerHome_L

```

**Type**
String

**Description**
The page type.

**Example**

```
  HomePage

```

**Type**
Number

**Description**
The time when the page starts loading, measured in milliseconds.

**Example**

```
  1471564788642

```

**Type**
String

**Description**
Relative URL of the top-level Lightning Experience or Salesforce mobile app page that the
user opened. The page can contain one or more Lightning components. Multiple record IDs
can be associated with `PAGE_URL` .

**Example**

```
  /sObject/0064100000JXITSAA5/view

```

**Type**
String

**Description**
The parent scope of the page element where the event occurred.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
PREVPAGE_APP_NAME

PREVPAGE_CONTEXT

PREVPAGE_ENTITY_ID

PREVPAGE_ENTITY_TYPE

PREVPAGE_URL

REQUEST_ID

```

**Type**
String

**Description**
The internal name of the previous application that the user accessed from the App Launcher.

**Example**

```
  LightningSales

```

**Type**
String

**Description**
The context of the previous page where the event occurred.

**Example**

```
  clients:cardsContainer

```

**Type**
Id

**Description**
The unique previous page entity identifier of the event.

**Type**
String

**Description**
The previous page entity type of the event.

**Example**
`Task`, `contacts`

**Type**
String

**Description**
The relative URL of the previous Lightning Experience or Salesforce mobile app page that
the user opened.

**Example**

```
  /sObject/006410000

```

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

**Example**

```
  3nWgxWbDKWWDIk0FKfF5DV

```


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
SDK_APP_TYPE

SDK_APP_VERSION

SDK_VERSION

SESSION_KEY

TARGET_UI_ELEMENT

```

**Type**
String

**Description**
The mobile SDK application type.

**Possible Values**

**•** `HYBRID`

**•** `HYBRIDLOCAL`

**•** `HYBRIDREMOTE`

**•** `NATIVE`

**•** `REACTNATIVE`

**Type**
String

**Description**
The mobile SDK application version number.

**Example**

```
  5.0

```

**Type**
String

**Description**
The mobile SDK version number.

**Example**

```
  2.1.0

```

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify all events in Lightning
Experience within a session. When the user logs out and logs in again, a new session is
started.

**Example**

```
  cdd09305cb6babf34059e27f70e47f1b11dec868

```

**Type**
String

**Description**
The target page element where the event occurred.

**Example**

```
  tabitem-link

```


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
TIMESTAMP

TIMESTAMP_DERIVED

UI_EVENT_ID

UI_EVENT_SEQUENCE_NUM

UI_EVENT_SOURCE

UI_EVENT_TIMESTAMP

```

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . The timezone is GMT.

**Type**
String

**Description**
Id of the Lightning event type.

**Possible Values**

**•** `ltng:error`

**•** `ltng:interaction`

**•** `ltng:pageView`

**•** `ltng:performance`

**Type**
Number

**Description**
An auto-incremented sequence number of the current event since the session started.

**Type**
String

**Description**
This field is being deprecated and is mostly null, except in mobile app views where it indicates
the page type of views where the context is “native.”

**Type**
Number

**Description**
The time at which this event occurred, measured in milliseconds.

**Example**

```
  1479769912796

```


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
USER_AGENT

USER_ID

USER_ID_DERIVED

USER_TYPE

```

**Type**
String

**Description**
The type of client used to make the request (for example, the browser, application, or API)
as a string.

**Type**
String

**Description**
The 15-character ID of the user accessing Salesforce services through the UI or API.

**Example**

```
  00530000009M943

```

**Type**
Id

**Description**
The 18-character case-insensitive ID of the user who’s using Salesforce services through the
UI or the API.

**Example**

```
  00590000000I1SNIA0

```

**Type**
String

**Description**
The category of user license of the user accessing Salesforce services through the UI or API.

**Possible Values**

**•** `A` : Automated Process

**•** `b` : High Volume Portal

**•** `C` : Customer Portal User

**•** `D` : External Who

**•** `F` : Self-Service

**•** `G` : Guest

**•** `L` : Package License Manager

**•** `N` : Salesforce to Salesforce

**•** `n` : CSN Only

**•** `O` : Power Custom

**•** `o` : Custom

**•** `P` : Partner

**•** `p` : Customer Portal Manager

**•** `S` : Standard


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**•** `X` : Salesforce Administrator

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Lightning Performance Event Type

Lightning Performance events track trends in Lightning Experience and Salesforce mobile app performance. This event type is available
in the EventLogFile object in API version 39.0 and later.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
APP_NAME

BROWSER_NAME

BROWSER_VERSION

CLIENT_GEO

```

**Type**
String

**Description**
The name of the application that the user accessed.

**Type**
String

**Description**
The name of the browser that the user accessed.

**Example**
`Chrome`, `Safari`

**Type**
String

**Description**
The version of the browser that the user accessed in `major.minor version` format.
Some browsers don’t provide a minor version.

**Type**
String

**Description**
The geolocation of the client in the form of `<Country>/<State|Province>` .

**Example**

```
  United States/California

```


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
CLIENT_ID

CLIENT_IP

CONNECTION_TYPE

DEVICE_ID

DEVICE_MODEL

```

**Type**
String

**Description**
The API client ID.

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
String

**Description**
The type of connection.

**Possible Values**

**•** `CDMA1x`

**•** `CDMA`

**•** `EDGE`

**•** `EVDO0`

**•** `EVDOA`

**•** `EVDOB`

**•** `GPRS`

**•** `HRPD`

**•** `HSDPA`

**•** `HSUPA`

**•** `LTE`

**•** `WIFI`

**Type**
String

**Description**
The unique identifier used to identify a device when tracking events. `DEVICE_ID` is a
generated value that’s created when the mobile app is initially run after installation.

**Type**
String

**Description**
The name of the device model.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Example**
`iPad`, `iPhone`

```
DEVICE_PLATFORM

DEVICE_SESSION_ID

DURATION

EVENT_TYPE

LOGIN_KEY

ORGANIZATION_ID

```

**Type**
String

**Description**
The type of application experience in `name:experience:form` format.

**Possible Values**

**•** `name` : `APP_BUILDER`, `CUSTOM`, `S1`, `SFX`

**•** `experience` : `BROWSER`, `HYBRID`

**•** `form` : `DESKTOP`, `PHONE`, `TABLET`

**Type**
Id

**Description**
The unique identifier of the user’s session based on page load time. When the user reloads
a page, a new session is started.

**Example**

```
  321a1ddfaf924803a075f1e69fc87bc06f53ccd0

```

**Type**
Number

**Description**
The duration in milliseconds since the page start time.

**Type**
String

**Description**
The type of event. The value is always `LightningPerformance` .

**Type**
String

**Description**
The string that ties together all events in a user’s login session. It starts with a login event
and ends with either a logout event or the user session expiring.

**Example**

```
  GeJCsym5eyvtEK2I

```

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The 15-character ID of the org.

**Example**

```
                   00D000000000123

```

```
OS_NAME

OS_VERSION

PAGE_START_TIME

REQUEST_ID

SDK_APP_TYPE

```

**Type**
String

**Description**
The operating system name, derived from `USER_AGENT` .

**Example**
`Android`, `iOS`, `OSX`, `Windows`

**Type**
String

**Description**
The operating system version, derived from `USER_AGENT` .

**Type**
Number

**Description**
The time when the page was initially loaded, measured in milliseconds.

**Example**

```
  1471564788642

```

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

**Example**

```
  3nWgxWbDKWWDIk0FKfF5DV

```

**Type**
String

**Description**
The mobile SDK application type.

**Possible Values**

**•** `HYBRID`

**•** `HYBRIDLOCAL`

**•** `HYBRIDREMOTE`

**•** `NATIVE`


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**•** `REACTNATIVE`

```
SDK_APP_VERSION

SDK_VERSION

SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

UI_EVENT_ID

```

**Type**
String

**Description**
The mobile SDK application version number.

**Example**

```
  5.0

```

**Type**
String

**Description**
The mobile SDK version number.

**Example**

```
  2.1.0

```

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify all events in Lightning
Experience within a session. When the user logs out and logs in again, a new session is
started.

**Example**

```
  cdd09305cb6babf34059e27f70e47f1b11dec868

```

**Type**
String

**Description**
The access time of Salesforce services in GMT.

**Example**

```
  20130715233322.670

```

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

**Example**
`2015-07-27T11:32:59.555Z` . The timezone is GMT.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
Id of the Lightning event type.

**Possible Values**

**•** `ltng:error`

**•** `ltng:interaction`

**•** `ltng:pageView`

**•** `ltng:performance`

Note: Any other value, such as `ltng:bootstrap`, is for internal usage only.

```
UI_EVENT_SOURCE

UI_EVENT_TIMESTAMP

UI_EVENT_TYPE

USER_AGENT

```

**Type**
String

**Description**
The user action on the record or records. This field’s value indicates whether the user’s action
was on a single record or multiple records. For example, `read` indicates that one record
was read (such as on a record detail page); `reads` indicates that multiple records were read
(such as in a list view).

**Example**

**•** `click`

**•** `create`

**•** `delete`

**•** `hover`

**•** `read`

**•** `update`

**Type**
Number

**Description**
The time at which this event occurred, measured in milliseconds.

**Example**

```
  1479769912796

```

**Type**
String

**Description**
The type of performance event.

**Example**
`bootstrap`, `defs`, `performance`

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The numeric code for the type of client used to make the request (for example, browser,
application, or API) as a string.

```
USER_ID

USER_ID_DERIVED

USER_TYPE

```

**Type**
String

**Description**
The 15-character ID of the user accessing Salesforce services through the UI or API.

**Example**

```
  00530000009M943

```

**Type**
Id

**Description**
The 18-character case-insensitive ID of the user who’s using Salesforce services through the
UI or the API.

**Example**

```
  00590000000I1SNIA0

```

**Type**
String

**Description**
The category of user license of the user accessing Salesforce services through the UI or API.

**Possible Values**

**•** `A` : Automated Process

**•** `b` : High Volume Portal

**•** `C` : Customer Portal User

**•** `D` : External Who

**•** `F` : Self Service

**•** `G` : Guest

**•** `L` : Package License Manager

**•** `N` : Salesforce to Salesforce

**•** `n` : CSN Only

**•** `O` : Power Custom

**•** `o` : Custom

**•** `P` : Partner

**•** `p` : Customer Portal Manager

**•** `S` : Standard


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**•** `X` : Salesforce Administrator

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Login Event Type

Login events contain details about your org’s user login history.

Note: The Login event type is used by EventLogFile (ELF). It isn’t a real-time event. For the LoginEvent real-time event, which is
[part of Real-Time Event Monitoring (RTEM), see LoginEvent in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/sforce_api_objects_loginevent.htm) _Platform Events Developer Guide_ .

[For details about event monitoring, see the Trailhead Event Monitoring module or the REST API Developer Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
API_TYPE

API_VERSION

AUTHENTICATION_METHOD_REFERENCE

```

**Type**
String

**Description**
The type of API request.

Possible values are:

**•** `D` —Apex Class

**•** `E` —SOAP Enterprise

**•** `M` —SOAP Metadata

**•** `P` —SOAP Partner

**•** `S` —SOAP Apex

**•** `T` —SOAP Tooling

**•** `f` —Feed

**•** `l` —Live Agent

**•** `p` —SOAP ClientSync

**Type**
String

**Description**
The version of the API that’s being used.

For example: `36.0` .

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The authentication method used by a third-party identification
provider for an OpenID Connect single sign-on protocol. This
field is available in API version 51.0 and later.

```
AUTHENTICATION_SERVICE_ID

BROWSER_TYPE

CIPHER_SUITE

CLIENT_IP

```

**Type**
Id

**Description**
The 15-character ID for the authentication service used to log
in. This field stores IDs for these authentication services.

**•** SAML single sign-on providers

**•** Token exchange handlers

Available in API version 60.0 and later.

**Type**
String

**Description**
The identifier string returned by the browser used at login.

Example values are:

**•** `Go-http-client/1.1`

**•** `Mozilla/5.0 (Macintosh; Intel Mac OS`

```
    X 10.12; rv%3A50.0) Gecko/20100101

    Firefox/50.0

```

**•** `Mozilla/5.0 (Macintosh; Intel Mac OS`

```
    X 10_11_6) AppleWebKit/537.36 (KHTML,

    like Gecko) Chrome/51.0.2704.84

    Safari/537.36

```

**Type**
String

**Description**
The TLS cipher suite used for the login. Values are
OpenSSL-style cipher suite names, with hyphen delimiters. For
[more information, see OpenSSL Cryptography and SSL/TLS](https://www.openssl.org/source/)
[Toolkit.](https://www.openssl.org/source/)

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .


Standard Objects EventLogFile Supported Event Types

```
COUNTRY_CODE

CPU_TIME

DB_TOTAL_TIME

EVENT_TYPE

FORWARDED_FOR_IP

HTTP_REFERER

```

**Type**
String

**Description**
The country code associated with the IP address of the user
logging in.

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
Number

**Description**
The time in nanoseconds for a database round trip. Includes
time spent in the JDBC driver, network to the database, and
`DB_CPU_TIME` . Compare this field to `CPU_TIME` to
determine whether performance issues are occurring in the
database layer or in your own code.

**Type**
String

**Description**
The type of event. The value is always `Login` .

**Type**
String

**Description**
The value in the `X-Forwarded-For` header of HTTP
requests sent by the client. For logins that use one or more
HTTP proxies, the `X-Forwarded-For` header is sometimes
used to store the origin IP and all proxy IPs.

The `FORWARDED_FOR_IP` field stores whatever value the
client sends, which might not be an IP address. The maximum
length is 256 characters. Longer values are truncated. The
`FORWARDED_FOR_IP` field isn’t populated for logins
completed via OAuth flows or single sign-on (SSO).

Available in API version 61.0 and later.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The referring URI of the page that’s receiving the request.

```
LOGIN_KEY

LOGIN_STATUS

LOGIN_SUB_TYPE

LOGIN_TYPE

```

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
String

**Description**
The status of the login attempt. For successful logins, the value
is LOGIN_NO_ERROR. All other values indicate errors or
authentication issues. For details, see Login Event Type —
LOGIN_STATUS Values on page 2307.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**
The type of login flow used. See the `LoginSubType` field
[of LoginHistory in the Object Reference guide for the list of](https://developer.salesforce.com/docs/atlas.en-us.260.0.object_reference.meta/object_reference/sforce_api_objects_loginhistory.htm)
possible values.

Label is **Login Subtype** .

**Type**
String

**Description**
The type of login used to access the session.

Possible values are:

**•** `7` —AppExchange

**•** `A` —Application

**•** `s` —Certificate-based login

**•** `k` —Chatter Communities External User

**•** `n` —Chatter Communities External User Third Party SSO

**•** `x` —Cross Tenant Login (for internal use only)

**•** `r` —Employee Login to Community

**•** `z` —Lightning Login


Standard Objects EventLogFile Supported Event Types

**•** `l` —Networks Portal API Only

**•** `6` —Remote Access Client

**•** `i` —Remote Access 2.0

**•** `I` —Other Apex API

**•** `R` —Partner Product

**•** `w` —Passwordless Login

**•** `3` —Customer Service Portal

**•** `q` —Partner Portal Third-Party SSO

**•** `9` —Partner Portal

**•** `5` —SAML Idp Initiated SSO

**•** `m` —SAML Chatter Communities External User SSO

**•** `b` —SAML Customer Service Portal SSO

**•** `c` —SAML Partner Portal SSO

**•** `h` —SAML Site SSO

**•** `8` —SAML Sfdc Initiated SSO

**•** `E` —SelfService

**•** `j` —Third Party SSO

```
LOGIN_URL

ORGANIZATION_ID

REQUEST_ID

REQUEST_STATUS

```

**Type**
String

**Description**
The URL of the login page.

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
String

**Description**
The status of the request for a page view or user interface
action.


Standard Objects EventLogFile Supported Event Types

For example:

**•** `S` —Success. Salesforce handled the request successfully.
If an Apex controller throws an exception, this status is also
returned.

**•** `F` —Failure. Typically 4xx or 5xx HTTP codes, such as no
permission to view page, page took too long to render,
page is read-only.

**•** `U` —Undefined

**•** `A` —Authorization Error

**•** `R` —Redirect. Typically a 3xx HTTP code, possibly initiated
by an Apex controller in a Visualforce page.

**•** `N` —Not Found. 404 error.

This field can have a blank value.

```
RUN_TIME

SESSION_KEY

SOURCE_IP

TIMESTAMP

```

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started. For Login Event Type, this
field is usually null because the event is captured before a
session is created.

**Example**
d7DEq/ANa7nNZZVD

**Type**
IP

**Description**
The IP address of the incoming client request that first reaches
Salesforce during a login. For example, `126.7.4.2` . For
clients that redirect through one or more HTTP proxies, this
field stores the IP address of the first proxy to reach Salesforce.
To better identify the origin IP for these cases, check the
`FORWARDED_FOR_IP` field instead.

**Type**
String

**Description**
The access time of Salesforce services in GMT.


Standard Objects EventLogFile Supported Event Types

For example: `20130715233322.670` .

```
TIMESTAMP_DERIVED

TLS_PROTOCOL

URI

URI_ID_DERIVED

USE_API_TOKEN

USER_ID

```

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Time zone
is GMT.

**Type**
String

**Description**
The TLS protocol used for the login.

**Example**
There are 3 possible values.

**•** 1.0

**•** 1.1

**•** 1.2

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
String

**Description**
Login with API Token - T token, or P password.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`


Standard Objects EventLogFile Supported Event Types

```
USER_ID_DERIVED

USER_NAME

USER_TYPE

```

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

**Type**
String

**Description**
The username that’s used for login.

**Type**
String

**Description**
The category of user license.

Possible values are:

**•** `CsnOnly` —Users whose access to the application is
limited to Chatter. This user type includes Chatter Free and
Chatter moderator users.

**•** `CspLitePortal` —CSP Lite Portal license. Users whose
access is limited because they’re organization customers
and access the application through a customer portal or
an Experience Cloud site.

**•** `CustomerSuccess` —Customer Success license. Users
whose access is limited because they’re organization
customers and access the application through a customer
portal.

**•** `Guest` —Users whose access is limited so that your
customers can view and interact with your site without
logging in.

**•** `PowerCustomerSuccess` —Power Customer Success
license. Users whose access is limited because they’re
organization customers and access the application through
a customer portal. Users with this license type can view
and edit data they directly own or data owned by or shared
with users below them in the customer portal role
hierarchy.

**•** `PowerPartner` —Power Partner license. Users whose
access is limited because they’re partners and typically
access the application through a partner portal or site.

**•** `SelfService` —Users whose access is limited because
they’re organization customers and access the application
through a self-service portal.


Standard Objects EventLogFile Supported Event Types

**•** `Standard` —Standard user license. This user type also
includes Salesforce Platform and Salesforce Platform One
user licenses, and admins for this org.

Login Event Type — LOGIN_STATUS Values
When users attempt to log in to your org, the success or failure of their login attempts is tracked in event log file data. Specifically,
the LOGIN_STATUS field in the Login event type contains the result of these login attempts. The data in LOGIN_STATUS can help
you determine whether your users’ login attempts were successful. This field is available in the Login event type in the EventLogFile
object in API version 39.0 and later.

SEE ALSO:

Login Event Type — LOGIN_STATUS Values

EventLogFile Supported Event Types

EventLogFile

Login Event Type — LOGIN_STATUS Values

When users attempt to log in to your org, the success or failure of their login attempts is tracked in event log file data. Specifically, the
LOGIN_STATUS field in the Login event type contains the result of these login attempts. The data in LOGIN_STATUS can help you
determine whether your users’ login attempts were successful. This field is available in the Login event type in the EventLogFile object
in API version 39.0 and later.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

**API Error Code** **Details (If Available)**

LOGIN_CHALLENGE_ISSUED Failed: Computer activation required

LOGIN_CHALLENGE_PENDING Failed: Computer activation pending

LOGIN_DATA_DOWNLOAD_ONLY

LOGIN_END_SESSION_TXN_SECURITY_POLICY

LOGIN_ERROR_API_TOO_OLD

Failed: API Version Removed. The API version specified for login is
below the minimum supported value, and has been removed. Update
to a newer, supported API version.

LOGIN_ERROR_APPEXCHANGE_DOWN Unable to process your login request

LOGIN_ERROR_ASYNC_USER_CREATE

LOGIN_ERROR_AVANTGO_DISABLED

LOGIN_ERROR_AVANTGO_TRIAL_EXP

LOGIN_ERROR_CLIENT_NO_ACCESS

LOGIN_ERROR_CLIENT_REQ_UPDATE Failed: Client update required

LOGIN_ERROR_CSS_FROZEN


Standard Objects EventLogFile Supported Event Types

**API Error Code** **Details (If Available)**

LOGIN_ERROR_CSS_PW_LOCKOUT

LOGIN_ERROR_DUPLICATE_USERNAME

LOGIN_ERROR_EXPORT_RESTRICTED Restricted country

LOGIN_ERROR_GLOBAL_BLOCK_DOMAIN Restricted domain

LOGIN_ERROR_HT_DOWN

LOGIN_ERROR_HTP_METHD_INVALID Failed: Invalid HTTP method

LOGIN_ERROR_INSECURE_LOGIN Failed: Login over insecure channel

LOGIN_ERROR_INVALID_GATEWAY Invalid gateway

LOGIN_ERROR_INVALID_ID_FIELD

LOGIN_ERROR_INVALID_PASSWORD Invalid password

LOGIN_ERROR_LOGINS_EXCEEDED Maximum logins exceeded

LOGIN_ERROR_MUST_USE_API_TOKEN Failed: API security token required

LOGIN_ERROR_MUTUAL_AUTHENTICATION Mutual authentication failed

LOGIN_ERROR_NETWORK_INACTIVE Invalid - Experience Cloud site offline

LOGIN_ERROR_NO_HT_ACCESS

LOGIN_ERROR_NO_NETWORK_ACCESS No Experience Cloud site access

LOGIN_ERROR_NO_NETWORK_INFO

LOGIN_ERROR_NO_PORTAL_ACCESS Invalid profile association

LOGIN_ERROR_NO_SET_COOKIES

LOGIN_ERROR_OFFLINE_DISABLED Offline disabled

LOGIN_ERROR_OFFLINE_TRIAL_EXP Offline trial expired

LOGIN_ERROR_ORG_CLOSED Organization closed

LOGIN_ERROR_ORG_DOMAIN_ONLY Restricted domain

LOGIN_ERROR_ORG_IN_MAINTENANCE Organization is in maintenance

LOGIN_ERROR_ORG_INACTIVE Organization is inactive

LOGIN_ERROR_ORG_IS_DOT_ORG Organization is a DOT

LOGIN_ERROR_ORG_LOCKOUT Organization locked

LOGIN_ERROR_ORG_SIGNING_UP

LOGIN_ERROR_ORG_SUSPENDED Organization suspended

LOGIN_ERROR_OUTLOOK_DISABLED Outlook integration disabled


Standard Objects EventLogFile Supported Event Types

**API Error Code** **Details (If Available)**

LOGIN_ERROR_PAGE_REQUIRES_LOGIN

LOGIN_ERROR_PASSWORD_EMPTY

LOGIN_ERROR_PASSWORD_LOCKOUT Password lockout

LOGIN_ERROR_PORTAL_INACTIVE Invalid - Portal disabled

LOGIN_ERROR_RATE_EXCEEDED Login rate exceeded

LOGIN_ERROR_RESTRICTED_DOMAIN Restricted IP

LOGIN_ERROR_RESTRICTED_TIME Restricted time

LOGIN_ERROR_SESSION_TIMEOUT

LOGIN_ERROR_SSO_PWD_INVALID Invalid password

LOGIN_ERROR_SSO_SVC_DOWN Your company's authentication service is down

LOGIN_ERROR_SSO_URL_INVALID The Single Sign-On Gateway URL is invalid

LOGIN_ERROR_STORE

LOGIN_ERROR_STORE_DOWN

LOGIN_ERROR_SWITCH_SFDC_INSTANCE

LOGIN_ERROR_SWITCH_SFDC_LOGIN

LOGIN_ERROR_SYNCOFFLINE_DISBLD Failed: Mobile disabled

LOGIN_ERROR_SYSTEM_DOWN

LOGIN_ERROR_UNKNOWN_ERROR Login invalid

LOGIN_ERROR_USER_API_ONLY Failed: API-only user

LOGIN_ERROR_USER_FROZEN User is frozen

LOGIN_ERROR_USER_INACTIVE User is inactive

LOGIN_ERROR_USER_NON_MOBILE Failed: Mobile license required

LOGIN_ERROR_USER_STORE_ACCESS

LOGIN_ERROR_USERNAME_EMPTY

LOGIN_ERROR_WIRELESS_DISABLED Wireless disabled

LOGIN_ERROR_WIRELESS_TRIAL_EXP Wireless trial expired

LOGIN_LIGHTNING_LOGIN Lightning Login required

LOGIN_NO_ERROR

LOGIN_OAUTH_API_DISABLED Failed: OAuth API access disabled

LOGIN_OAUTH_CONSUMER_DELETED Failed: Consumer Deleted


Standard Objects EventLogFile Supported Event Types

**API Error Code** **Details (If Available)**

LOGIN_OAUTH_DS_NOT_EXPECTED Failed: Activation secret not expected

LOGIN_OAUTH_EXCEED_GET_AT_LMT Failed: Get Access Token Limit Exceeded

LOGIN_OAUTH_INVALID_CODE_CHALLENGE Failed: Invalid Code Challenge

LOGIN_OAUTH_INVALID_CODE_VERIFIER Failed: Invalid Code Verifier

LOGIN_OAUTH_INVALID_DEVICE Failed: Device Id missing or not registered

LOGIN_OAUTH_INVALID_DS Failed: Activation secret invalid

LOGIN_OAUTH_INVALID_DSIG Failed: Signature Invalid

LOGIN_OAUTH_INVALID_IP Failed: IP Address Not Allowed

LOGIN_OAUTH_INVALID_NONCE Failed: Invalid Nonce

LOGIN_OAUTH_INVALID_SIG_METHOD Failed: Invalid Signature Method

LOGIN_OAUTH_INVALID_TIMESTAMP Failed: Invalid Timestamp

LOGIN_OAUTH_INVALID_TOKEN Failed: Invalid Token

LOGIN_OAUTH_INVALID_VERIFIER Failed: Invalid Verifier

LOGIN_OAUTH_INVALID_VERSION Failed: Version Not Supported

LOGIN_OAUTH_MISSING_DS Activation secret missing

LOGIN_OAUTH_NO_CALLBACK_URL Failed: Invalid Callback URL

LOGIN_OAUTH_NO_CONSUMER Missing Consumer Key Parameter

LOGIN_OAUTH_NO_TOKEN Missing OAuth Token Parameter

LOGIN_OAUTH_NONCE_REPLAY Failed: Nonce Replay Detected

LOGIN_OAUTH_PACKAGE_MISSING Package for this consumer is not installed in your organization

LOGIN_OAUTH_PACKAGE_OLD Installed package for this consumer is out of date

LOGIN_OAUTH_UNEXPECTED_PARAM Failed: Unexpected parameter

LOGIN_ORG_TRIAL_EXP Trial Expired

LOGIN_READONLY_CANNOT_VALIDATE

LOGIN_SAML_INVALID_AUDIENCE Failed: Audience Invalid

LOGIN_SAML_INVALID_CONFIG Failed: Configuration Error/Perm Disabled

LOGIN_SAML_INVALID_FORMAT Failed: Assertion Invalid

LOGIN_SAML_INVALID_IN_RES_TO Failed: InResponseTo Invalid

LOGIN_SAML_INVALID_ISSUER Failed: Issuer Mismatched

LOGIN_SAML_INVALID_ORG_ID Failed: Invalid Organization Id


Standard Objects EventLogFile Supported Event Types

**API Error Code** **Details (If Available)**

LOGIN_SAML_INVALID_PORTAL_ID Failed: Invalid Portal Id

LOGIN_SAML_INVALID_RECIPIENT Failed: Recipient Mismatched

LOGIN_SAML_INVALID_SESSION_LEVEL

LOGIN_SAML_INVALID_SIGNATURE Failed: Signature Invalid

LOGIN_SAML_INVALID_SITE_URL Failed: Invalid Site URL

LOGIN_SAML_INVALID_STATUS Failed: Status Invalid

LOGIN_SAML_INVALID_SUB_CONFIRM Failed: Subject Confirmation Error

LOGIN_SAML_INVALID_TIMESTAMP Failed: Assertion Expired

LOGIN_SAML_INVALID_USERNAME Failed: Username Or SSO Id Invalid

LOGIN_SAML_INVALID_VERSION

LOGIN_SAML_MISMATCH_CERT Failed: Signature Invalid/Configured Certificate Mismatch

LOGIN_SAML_MISSING_ORG_ID Failed: Missing Organization Id for Portal login

LOGIN_SAML_MISSING_PORTAL_ID Failed: Missing Portal Id

LOGIN_SAML_PROVISION_ERROR Failed: SAML Provision Error

LOGIN_SAML_REPLAY_ATTEMPTED Failed: Replay Detected

LOGIN_SAML_SITE_INACTIVE Failed: Specified Site is Inactive

LOGIN_TWOFACTOR_REQ Multi-factor (formerly called two-factor) is required

Usage

Use LOGIN_STATUS to determine whether your users’ login attempts were successful. For example, you can determine whether a
departed employee attempted to log in successfully or unsuccessfully.

SEE ALSO:

Login Event Type

EventLogFile Supported Event Types

EventLogFile

##### Login As Event Type

Login As events contain details about what a Salesforce admin did while logged in as another user.

Note: Login As Event Type is used by EventLogFile (ELF). It isn’t a real-time event. For the LoginAsEvent real-time event, which
[is part of Real-Time Event Monitoring (RTEM), see LoginAsEvent in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/sforce_api_objects_loginasevent.htm) _Platform Events Developer Guide_ .


Standard Objects EventLogFile Supported Event Types

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Note: Bolster your security posture by receiving alerts and blocking potentially malicious LoginAsEvent activities with a Transaction
Security policy.

Fields

**Field** **Details**

```
CLIENT_IP

CPU_TIME

DELEGATED_USER_ID

DELEGATED_USER_ID_DERIVED

DELEGATED_USER_NAME

```

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or API. In this case, the user who’s doing the
impersonation.

**Type**
Id

**Description**
The 18-character case-insensitive ID of the user who’s using
Salesforce services through the UI or API. In this case, the user
who’s doing the impersonation.

**Type**
String

**Description**
The username of the user who’s using Salesforce services
through the UI or API. In this case, the user who’s doing the
impersonation.


Standard Objects EventLogFile Supported Event Types

```
EVENT_TYPE

LOGIN_KEY

ORGANIZATION_ID

REQUEST_ID

RUN_TIME

SESSION_KEY

TIMESTAMP

```

**Type**
String

**Description**
The type of event. The value is always `LoginAs` .

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

```
TIMESTAMP_DERIVED

URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .


Standard Objects EventLogFile Supported Event Types

##### Logout Event Type

Contains details of user sessions ending or being revoked.

Note: Logout Event Type is used by EventLogFile (ELF). It isn’t a real-time event. For the LogoutEvent real-time event, which is
[part of Real-Time Event Monitoring (RTEM), see LogoutEvent in the](https://developer.salesforce.com/docs/atlas.en-us.260.0.platform_events.meta/platform_events/sforce_api_objects_logoutevent.htm) _Platform Events Developer Guide_ .

These scenarios count as logout events.

**•** Logging out via the UI

**•** Session expiration

**•** Revoking access for a connected app

**•** Calling the Salesforce revocation endpoint

**•** Salesforce disabling a connected app

**•** Note: For batch operations where multiple sessions are revoked at once, Salesforce records only one logout event. You can
tell that it’s a batch operation because there’s no user ID.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
API_TYPE

API_VERSION

```

**Type**
String

**Description**
The type of API request.

Possible values are:

**•** `D` —Apex Class

**•** `E` —SOAP Enterprise

**•** `M` —SOAP Metadata

**•** `P` —SOAP Partner

**•** `S` —SOAP Apex

**•** `T` —SOAP Tooling

**•** `f` —Feed

**•** `l` —Live Agent

**•** `p` —SOAP ClientSync

**Type**
String

**Description**
The version of the API that’s being used.

For example: `36.0` .


Standard Objects EventLogFile Supported Event Types

```
APP_TYPE

BROWSER_TYPE

CLIENT_IP

CLIENT_VERSION

EVENT_TYPE

```

**Type**
Number

**Description**
The application type that was in use upon logging out.

**Example Values**

**•** `1000` : Application

**•** `1007` : SFDC Application

**•** `1014` : Chat

**•** `2501` : CTI

**•** `2514` : OAuth

**•** `3475` : SFDC Partner Portal

**Type**
String

**Description**
The identifier string returned by the browser used at login.

Example values are:

**•** `Go-http-client/1.1`

**•** `Mozilla/5.0 (Macintosh; Intel Mac OS`

```
    X 10.12; rv%3A50.0) Gecko/20100101

    Firefox/50.0

```

**•** `Mozilla/5.0 (Macintosh; Intel Mac OS`

```
    X 10_11_6) AppleWebKit/537.36 (KHTML,

    like Gecko) Chrome/51.0.2704.84

    Safari/537.36

```

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number

**Description**
The version of the client that was in use upon logging out.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The type of event. The value is always `Logout` .

```
LOGIN_KEY

ORGANIZATION_ID

PLATFORM_TYPE

REQUEST_ID

```

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
Number

**Description**
The code for the client platform. If a timeout caused the logout,
this field is null.

**Example Values**

**•** `1000` : Windows

**•** `1008` : Windows 2003

**•** `1013` : Windows 8.1

**•** `1015` : Windows 10

**•** `2003` : Macintosh/Apple OSX

**•** `4000` : Linux

**•** `5005` : Android

**•** `5006` : iPhone

**•** `5007` : iPad

**•** `5200` : Android 10.0

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .


Standard Objects EventLogFile Supported Event Types

```
RESOLUTION_TYPE

SESSION_KEY

SESSION_LEVEL

SESSION_TYPE

```

**Type**
Number

**Description**
The screen resolution of the client. If a timeout caused the
logout, this field is null.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String

**Description**
The security level of the session that was used when logging
out.

**Possible Values**

**•** `1` : Standard Session

**•** `10` : High-Assurance Session

**Type**
String

**Description**
The session type that was used when logging out.

**Possible Values**

**•** `A` : API

**•** `I` : APIOnlyUser

**•** `N` : ChatterNetworks

**•** `Z` : ChatterNetworksAPIOnly

**•** `C` : Content

**•** `P` : OauthApprovalUI

**•** `O` : Oauth2

**•** `T` : SiteStudio

**•** `R` : SitePreview

**•** `S` : SubstituteUser

**•** `B` : TempContentExchange

**•** `G` : TempOauthAccessTokenFrontdoor

**•** `Y` : TempVisualforceExchange


Standard Objects EventLogFile Supported Event Types

**•** `F` : TempUIFrontdoor

**•** `U` : UI

**•** `E` : UserSite

**•** `V` : Visualforce

**•** `W` : WDC_API

```
TIMESTAMP

TIMESTAMP_DERIVED

USER_ID

USER_ID_DERIVED

USER_INITIATED_LOGOUT

```

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

When a customer logs out by using the **Logout** button, the
`TIMESTAMP` field records the actual logout time. However,
when a customer is logged out automatically, Salesforce
detects the event by using a process that runs every 15
minutes. `TIMESTAMP` values can reflect a logout time up to
15 minutes later than the actual automatic logout time.

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

**Type**
Boolean


Standard Objects EventLogFile Supported Event Types

**Description**
The value is 1 if the user intentionally logged out of the
organization by clicking the **Logout** button. If the user’s session
timed out due to inactivity or another implicit logout action,
the value is 0.

```
USER_TYPE

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Metadata API Operation Event Type

**Type**
String

**Description**
The category of user license of the user that logged out.

**Possible Values**

**•** `A` : Automated Process

**•** `b` : High Volume Portal

**•** `C` : Customer Portal User

**•** `D` : External Who

**•** `F` : Self-Service

**•** `G` : Guest

**•** `L` : Package License Manager

**•** `N` : Salesforce to Salesforce

**•** `n` : CSN Only

**•** `O` : Power Custom

**•** `o` : Custom

**•** `P` : Partner

**•** `p` : Customer Portal Manager

**•** `S` : Standard

**•** `X` : Salesforce Administrator

Metadata API Operation events contain details of Metadata API retrieval and deployment requests.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**


Standard Objects EventLogFile Supported Event Types

```
API_VERSION

CLIENT_ID

CLIENT_IP

CPU_TIME

EVENT_TYPE

LOGIN_KEY

OPERATION

```

**Type**
String

**Description**
The version of the API that’s being used.

For example: `36.0` .

**Type**
String

**Description**
The API client ID.

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
String

**Description**
The type of event. The value is always
`MetadataApiOperation` .

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The operation that’s being performed.

**Possible Values**

**•** `meta_deploy`

**•** `meta_list`

**•** `meta_retrieve`

**•** `meta_synchronous_create`

**•** `meta_synchronous_read`

**•** `meta_synchronous_upsert`

```
ORGANIZATION_ID

REQUEST_ID

RUN_TIME

SESSION_KEY

TIMESTAMP

```

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .


Standard Objects EventLogFile Supported Event Types

```
TIMESTAMP_DERIVED

URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Multiblock Report Event Type

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

Multiblock Report events contain details about Joined Report reports.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)


Standard Objects EventLogFile Supported Event Types

Fields

**Field** **Details**

```
CLIENT_IP

CPU_TIME

DB_TOTAL_TIME

EVENT_TYPE

HAS_CHART

LOGIN_KEY

```

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
Number

**Description**
The time in nanoseconds for a database round trip. Includes
time spent in the JDBC driver, network to the database, and
`DB_CPU_TIME` . Compare this field to `CPU_TIME` to
determine whether performance issues are occurring in the
database layer or in your own code.

**Type**
String

**Description**
The type of event. The value is always `MultiblockReport` .

**Type**
Boolean

**Description**
True if the report has a chart.

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .


Standard Objects EventLogFile Supported Event Types

```
MASTER_REPORT_ID

ORGANIZATION_ID

REQUEST_ID

REQUEST_STATUS

RUN_TIME

```

**Type**
String

**Description**
The 15-character ID of the master report.

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
String

**Description**
The status of the request for a page view or user interface
action.

For example:

**•** `S` —Success. Salesforce handled the request successfully.
If an Apex controller throws an exception, this status is also
returned.

**•** `F` —Failure. Typically 4xx or 5xx HTTP codes, such as no
permission to view page, page took too long to render,
page is read-only.

**•** `U` —Undefined

**•** `A` —Authorization Error

**•** `R` —Redirect. Typically a 3xx HTTP code, possibly initiated
by an Apex controller in a Visualforce page.

**•** `N` —Not Found. 404 error.

This field can have a blank value.

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.


Standard Objects EventLogFile Supported Event Types

```
SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

URI

URI_ID_DERIVED

USER_ID

USER_ID_DERIVED

```

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`

**Type**
Id


Standard Objects EventLogFile Supported Event Types

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

```
USER_TYPE

```

**Type**
String

**Description**
The category of user license.

Possible values are:

**•** `CsnOnly` —Users whose access to the application is
limited to Chatter. This user type includes Chatter Free and
Chatter moderator users.

**•** `CspLitePortal` —CSP Lite Portal license. Users whose
access is limited because they’re organization customers
and access the application through a customer portal or
an Experience Cloud site.

**•** `CustomerSuccess` —Customer Success license. Users
whose access is limited because they’re organization
customers and access the application through a customer
portal.

**•** `Guest` —Users whose access is limited so that your
customers can view and interact with your site without
logging in.

**•** `PowerCustomerSuccess` —Power Customer Success
license. Users whose access is limited because they’re
organization customers and access the application through
a customer portal. Users with this license type can view
and edit data they directly own or data owned by or shared
with users below them in the customer portal role
hierarchy.

**•** `PowerPartner` —Power Partner license. Users whose
access is limited because they’re partners and typically
access the application through a partner portal or site.

**•** `SelfService` —Users whose access is limited because
they’re organization customers and access the application
through a self-service portal.


Standard Objects EventLogFile Supported Event Types

**•** `Standard` —Standard user license. This user type also
includes Salesforce Platform and Salesforce Platform One
user licenses, and admins for this org.

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Named Credential Event Type

The Named Credential event type captures information about Apex callouts that use named credentials as their endpoints. Use this
event type to audit the installed managed packages that use named credentials. If you don’t recognize the package namespace in the
named credential event log file, then you can investigate whether a security breach has occurred. This event type is available in the
EventLogFile object in API version 53.0 and later.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
BOT_IDENTIFIER

BOT_SESSION_IDENTIFIER

CALLER_PACKAGE_NAMESPACE

CLIENT_IP

```

**Type**
String

**Description**
The ID of the bot.

**Type**
String

**Description**
The bot session ID.

**Type**
String

**Description**
If an Apex callout using a Named Credential endpoint is initiated from a package, then this
field contains the package’s namespace. If the callout isn’t initiated from a package, then
this field is empty.

**Example**
Acme

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The IP address of the client that’s using Salesforce services. A Salesforce internal IP (such as
a login from AppExchange) is shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

```
CPU_TIME

EVENT_TYPE

LOGIN_KEY

NAMED_CREDENTIAL_NAME

ORGANIZATION_ID

PLANNER_IDENTIFIER

```

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request. This field indicates the amount
of activity taking place in the app server layer.

**Type**
String

**Description**
The type of event. The value is always `NamedCredential` .

**Type**
String

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
String

**Description**
The name of the named credential that’s the endpoint of the Apex callout.

**Example**
My_Named_Credential

**Type**
ID

**Description**
The 15-character ID of the org.

**Example**

```
  00D000000000123

```

**Type**
String

**Description**
The ID of the agent planner.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
REQUEST_ID

RUN_TIME

SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

URI

URI_ID_DERIVED

```

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone is GMT.

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Description**
The 18-character case-safe ID of the URI of the page that’s receiving the request.

```
USER_ID

USER_ID_DERIVED

```

SEE ALSO:

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.

For example: `00530000009M943`

**Type**
Id

**Description**
The 18-character case-safe ID of the user who’s using Salesforce services through the UI or
the API.

For example: `00590000000I1SNIA0` .

_Salesforce Help_ [: Named Credentials](https://help.salesforce.com/articleView?id=xcloud.named_credentials_about.htm&type=5&language=en_US)

EventLogFile Supported Event Types

EventLogFile

##### One Commerce Usage Event Type

One Commerce Usage events capture information about your Commerce instance. This event type is available in the EventLogFile object
in API version 51.0 and later.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields


Standard Objects EventLogFile Supported Event Types


Standard Objects EventLogFile Supported Event Types


Standard Objects EventLogFile Supported Event Types


Standard Objects EventLogFile Supported Event Types


Standard Objects EventLogFile Supported Event Types


Standard Objects EventLogFile Supported Event Types


Standard Objects EventLogFile Supported Event Types


Standard Objects EventLogFile Supported Event Types

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Package Install Event Type

Package Install events contain details about package installation in the organization.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
CLIENT_IP

```

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

```
CPU_TIME

EVENT_TYPE

FAILURE_TYPE

IS_MANAGED

IS_PUSH

IS_RELEASED

IS_SUCCESSFUL

```

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
String

**Description**
The type of event. The value is always `PackageInstall` .

**Type**
String

**Description**
A general categorization of any error that’s encountered.

**Type**
Boolean

**Description**
True if the operation is performed on a managed package.

**Type**
Boolean

**Description**
True if the package was installed as a result of a push upgrade.

**Type**
Boolean

**Description**
True if the operation is performed on a released package.

**Type**
Boolean

**Description**
True if the package was successfully installed.


Standard Objects EventLogFile Supported Event Types

```
LOGIN_KEY

OPERATION_TYPE

ORGANIZATION_ID

PACKAGE_NAME

REQUEST_ID

RUN_TIME

```

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
String

**Description**
The type of package operation.

**Possible Values**

**•** INSTALL

**•** UPGRADE

**•** EXPORT

**•** UNINSTALL

**•** VALIDATE_PACKAGE

**•** INIT_EXPORT_PKG_CONTROLLER

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The name of the package that’s being installed.

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

**Type**
Number


Standard Objects EventLogFile Supported Event Types

**Description**
The amount of time that the request took in milliseconds.

```
SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

URI

URI_ID_DERIVED

USER_ID

```

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

**Type**
Id

**Description**
The 15-character ID of the user who’s using Salesforce services
through the UI or the API.

For example: `00530000009M943`


Standard Objects EventLogFile Supported Event Types

```
USER_ID_DERIVED

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Permission Update Event Type

**Type**
Id

**Description**
The 18-character case insensitive ID of the user who’s using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

Permission update events represent changes to object, field, and user permissions and setup entity access that occur in profiles and
permission sets. The event type also tracks if you clone profiles or change whether session activation is required in permission sets or
permission set groups.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Note: This event type tracks if Salesforce updates object or field permissions in standard profiles, in addition to changes you make
to your custom profiles, permission sets, and permission set groups.

Fields

**Field** **Details**

```
CONTEXT

DESCRIPTION

EVENT_TYPE

```

**Type**
String

**Description**
Reserved for future use.

**Type**
String

**Description**
A description of the update that occurred in the profile, permission set, or permission set
group.

**Example**

```
  UserPerm: ConvertLeads disabled

```

**Type**
String

**Description**
The type of event. The value is always `PermissionUpdate` .


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

```
FEATURE_ID

LOGIN_KEY

ORGANIZATION_ID

PERMISSION_TYPE

REQUEST_ID

SESSION_KEY

```

**Type**
Id

**Description**
The ID of the feature, such as a profile, permission set, or permission set group, that was
updated.

**Type**
String

**Description**
The string that ties together all events in a given user’s login session. It starts with a login
event and ends with either a logout event or the user session expiring.

**Example**

```
  GeJCsym5eyvtEK2I

```

**Type**
Id

**Description**
The 15-character ID of the organization.

**Example**

```
  00DXXXXXXXXXXXX

```

**Type**
String

**Description**
The type of permission, such as user, object, or field, or setup entity access, such as tab
settings or Apex class access, that was updated.

**Example**

```
  EntityObject

```

**Type**
String

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .

**Example**

```
  3nWgxWbDKWWDIk0FKfF5DV

```

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify all user events within a session.
When a user logs out and logs in again, a new session is started.


Standard Objects EventLogFile Supported Event Types

**Field** **Details**

**Example**

```
                   d7DEq/ANa7nNZZVD

```

```
TIMESTAMP

TIMESTAMP_DERIVED

UPDATE_TYPE

USER_ID

```

**Type**
String

**Description**
The access time of Salesforce services in GMT.

**Example**

```
  20130715233322.670

```

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible format
( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

**Example**

```
  2015-07-27T11:32:59.555Z

```

**Type**
String

**Description**
For object permissions, user permissions, and setup entity access, the type of update that
occurred. For example, a permission was updated or deleted.

For other changes in profiles, permission sets, or permission set groups, this information is
tracked in the `DESCRIPTION` field.

**Example**

```
  delete

```

**Type**
Id

**Description**
The 15-character ID of the user who made the permission update.

**Example**

```
  005XXXXXXXXXXXX

```

##### Platform Encryption Event Type

Platform Encryption event contains information about tenant secret and derived encryption key usage. This event type is available in
API versions 41.0 and later.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)


Standard Objects EventLogFile Supported Event Types

Fields

**Field** **Details**

```
ACTION

BOT_IDENTIFIER

BOT_SESSION_IDENTIFIER

```

**Type**
String

**Description**
The name and type of the event.

**Possible Values**

**•** TS Imported: A tenant secret generated by the Shield Key
Management Service (KMS), or customer-supplied key
material, imported by a customer.

**•** TS Generated: A tenant secret generated by the Shield Key
Management Service (KMS).

**•** Key Derived: An encryption key derived from a tenant
secret for encryption or decryption.

**•** TS Wrapped: A tenant secret generated by the Shield Key
Management Service (KMS), or customer-supplied key
material, encrypted for storage.

**•** Key Delivered: A data encryption key delivered for
encryption or decryption.

**•** TS Stored: A tenant secret generated by the Shield Key
Management Service (KMS), or customer-supplied key
material, stored encrypted in the database.

**•** TS Read: An encrypted tenant secret generated by the
Shield Key Management Service (KMS), or encrypted
customer-supplied key material, that is loaded for
encryption or decryption.

**•** TS Unwrapped: An encrypted tenant secret generated by
the Shield Key Management Service (KMS), or encrypted
customer-supplied key material, unwrapped for use by the
KMS.

**•** TS Exported: An encrypted tenant secret exported by a
customer.

**•** TS Destroyed: A tenant secret and related data encryption
key destroyed by a customer.

**Type**
String

**Description**
The ID of the bot.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The bot session ID.

```
CLIENT_IP

CPU_TIME

EVENT_TYPE

KEY_ID

KEY_ID_DERIVED

KEY_TYPE

```

**Type**
String

**Description**
The IP address of the client that is using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”.

For example: `96.43.144.26` .

**Type**
Number

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

**Type**
String

**Description**
The type of event. The value is always
`PlatformEncryption` .

**Type**
String

**Description**
The 15-character ID of the tenant secret.

**Example**
02GD000000096Cb

**Type**
String

**Description**
The 18-character ID of the derived encryption key.

**Example**
02GD000000096CbMAI

**Type**
String

**Description**
The type of tenant secret.


Standard Objects EventLogFile Supported Event Types

**Possible Values**

**•** Data

**•** DeterministicData

**•** Analytics

**•** OauthSecret (internal use only)

**•** SearchIndex

```
LOGIN_KEY

METHOD

ORGANIZATION_ID

PLANNER_IDENTIFIER

REQUEST_ID

```

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

For example: `GeJCsym5eyvtEK2I` .

**Type**
String

**Description**
The string that identifies a change in tenant secret Active state.
For example, tenant secrets become active when they’re
created, and are made inactive when they’re exported.

**Examples**

**•** TS Exported: User ID

**•** TS Generated: HSM or BYOK

**•** TS Unwrapped: Tenant Secret or BYOK

**Type**
ID

**Description**
The 15-character ID of the organization.

For example: `00D000000000123` .

**Type**
String

**Description**
The ID of the agent planner.

**Type**
String


Standard Objects EventLogFile Supported Event Types

**Description**
The unique ID of a single transaction. A transaction can contain
one or more events. Each event in a given transaction has the
same `REQUEST_ID` .

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

```
RUN_TIME

SESSION_KEY

TIMESTAMP

TIMESTAMP_DERIVED

URI

URI_ID_DERIVED

```

**Type**
Number

**Description**
The amount of time that the request took in milliseconds.

**Type**
String

**Description**
The user’s unique session ID. You can use this value to identify
all user events within a session. When a user logs out and logs
in again, a new session is started.

For example: `d7DEq/ANa7nNZZVD` .

**Type**
String

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
DateTime

**Description**
The access time of Salesforce services in ISO8601-compatible
format ( `YYYY-MM-DDTHH:MM:SS.sssZ` ).

For example: `2015-07-27T11:32:59.555Z` . Timezone
is GMT.

**Type**
String

**Description**
The URI of the page that’s receiving the request.

For example: `/home/home.jsp` .

**Type**
ID


Standard Objects EventLogFile Supported Event Types

**Description**
The 18-character case insensitive ID of the URI of the page
that’s receiving the request.

```
USER_ID

USER_ID_DERIVED

```

SEE ALSO:

EventLogFile Supported Event Types

EventLogFile

##### Pricing Event Type

**Type**
ID

**Description**
The 18-character case insensitive ID of the user who is using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

**Type**
ID

**Description**
The 18-character case insensitive ID of the user who is using
Salesforce services through the UI or the API.

For example: `00590000000I1SNIA0` .

Pricing events contain information about pricing procedures that were executed, including details such as pricing procedures used, the
pricing APIs, and pricing details and status.

[For details about event monitoring, see the Trailhead Event Monitoring module or REST API Developer’s Guide.](https://trailhead.salesforce.com/en/modules/event_monitoring/units/event_monitoring_intro)

Fields

**Field** **Details**

```
CLIENT_IP

CPU_TIME

```

**Type**
String

**Description**
The IP address of the client that’s using Salesforce services. A
Salesforce internal IP (such as a login from AppExchange) is
shown as “Salesforce.com IP”. If the user’s session context isn't
available, this field returns a blank value.

**Type**
Number


Standard Objects EventLogFile Supported Event Types

**Description**
The CPU time in milliseconds used to complete the request.
This field indicates the amount of activity taking place in the
app server layer.

```
EVENT_TYPE

LOGIN_KEY

ORGANIZATION_ID

PRICING_API_ENDPOINT

PRICING_DETAILS

PRICING_ERROR_CODE

```

**Type**
String

**Description**
The type of event. The value is always `Pricing` .

**Type**
String

**Description**
The string that ties together all events in a given user’s login
session. It starts with a login event and ends with either a
logout event or the user session expiring.

**Type**
Id

**Description**
The 15-character ID of the organization.

For example: `00D000000000062` .

**Type**
String

**Description**
The starting point of the Pricing API or Headless Pricing API.

For example: `Pricing API` .

**Type**
String

**Description**
The details of the pricing event that describes if the pricing API
was executed or failed.

For example: `Pricing element was processed.` .

**Type**
String

**Description**
The API error code that appears when pricing execution fails.
If there is no error, the value is null.

For example: `INTERNAL_ERROR` .


Standard Objects EventLogFile Supported Event Types

```
PRICING_LOG_NAME

PRICING_PROCEDURE

PRICING_STATUS

REQUEST_ID

RUN_TIME

SESSION_KEY

TIMESTAMP

```

**Type**
String

**Description**
The detailed pricing log message generated.

For example: `The Headless Pricing API was`
`run in:{0}` .

**Type**
String

**Description**
The name of the pricing procedure used to perform pricing
calculations.

For example: `Default Pricing Procedure` .

**Type**
String

**Description**
The status of the request for pricing execution.

For example: `Completed or Failed` .

**Type**
String

**Description**
