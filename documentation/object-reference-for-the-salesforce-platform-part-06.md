Longitude

Name

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The contact’s last name.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of who or what last changed the record’s `Clean Status` field value:
a Salesforce user or a Clean job.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date on which the record’s `Clean Status` field value was last changed.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Used with `Longitude` to specify the precise geolocation of a billing address.
Data not currently provided.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Used with `Latitude` to specify the precise geolocation of a billing address.
Data not currently provided.

**Type**
string

**Properties**
Filter, Group, Sort, Update


Standard Objects ContactCleanInfo

**Field Name** **Details**

**Description**
Field label is **Contact Clean Info Name** . The name of the contact. Maximum
size is 255 characters.

```
Phone

PostalCode

State

Street

Title

```

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
The phone number for the contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Details for the billing address of the contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Details for the billing address of the contact.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**

Details for the billing address of the contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The contact’s title.


### Standard Objects ContactDailyMetric

Usage

Developers can create triggers that read the Contact Clean Info fields to help automate the cleaning or related processing of contact
records.

Create a customized set of `Title` field values. Use triggers to map values from fields on imported or cleaned records onto a standard
set of values.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ContactCleanInfoChangeEvent (API version 62.0)**
Change events are available for the object.

### ContactDailyMetric

Represents the daily engagement metrics for a contact. This object is available in API version 52.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Inbox must be enabled.

Fields

**Field** **Details**

```
AllCallsCallBackLater

AllCallsLeftVoicemail

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this contact with the call result Call Back Later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this contact with the call result Left Voicemail.


Standard Objects ContactDailyMetric

**Field** **Details**

```
AllCallsMeaningfulConnect

AllCallsNotInterested

AllCallsUncategorized

AllCallsUnqualified

AllEmailsBouncedCount

AllEmailsDeliveredCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this contact with the call result Meaningful Connect.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this contact with the call result Not Interested.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this contact with no call result specified.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this contact with the call result Unqualified.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total of hard and soft bounced emails for this contact in the day.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ContactDailyMetric

**Field** **Details**

**Description**
The number of successfully delivered emails for this contact in the day.

This is a calculated field.

```
AllEmailsDeliveredRate

AllEmailsHardBouncedCount

AllEmailsOutOfOfficeCount

AllEmailsSentCount

AllEmailsSoftBouncedCount

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of tracked emails sent that were successfully delivered to this contact. This
field is a calculated field.

Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of hard bounced emails for this contact in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that triggered an out of office reply for this contact in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact in the day.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails soft bounced for this contact in the day.


Standard Objects ContactDailyMetric

**Field** **Details**

```
AllEmailsTrackedSentCount

AllEmailsUntrackedSentCount

AllTotalCallsCount

ContactId

DailyCutOffTimeStamp

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with engagement tracking enabled in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact without engagement tracking enabled in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of calls to this contact with all call results in the day.

This is a calculated field.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related contact.

This is a relationship field.

**Relationship Name**
Contact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
dateTime

**Properties**
Filter, Sort


Standard Objects ContactDailyMetric

**Field** **Details**

**Description**
The time of day when each 24-hour metrics period starts and ends.

```
Date

DateInt

HardBounceTrackableSends

InboundEngagementsCount

LinkClickTrackableSends

```

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
The date on which the engagement occurred.

**Type**
int

**Properties**
Filter, Group, idLookup, Sort

**Description**
The date on which the engagement occurred, in yyyymmdd format.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with hard bounce tracking.

Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of inbound engagements for this contact in the day. This field is a calculated
field. The value is the sum of `UniqueEmailsOpenedCount`,
`UniqueEmailsRepliedCount`, and `UniqueEmailsLinkClickedCount` .

Available in API version 58.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with link click tracking.


Standard Objects ContactDailyMetric

**Field** **Details**

Available in API version 54.0 and later.

```
OpenTrackableSends

OutOfOfficeTrackableSends

OutboundEngagementsCount

ReplyTrackableSends

SoftBounceTrackableSends

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with open tracking.

Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with out-of-office tracking.

Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of outbound engagements for this contact in the day. This field is a calculated
field. The value is the sum of `AllTotalCallsCount` and
`AllEmailsDeliveredCount` .

Available in API version 58.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with reply tracking.

Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ContactDailyMetric

**Field** **Details**

**Description**
The number of emails sent to this contact with soft bounce tracking.

Available in API version 54.0 and later.

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
The percentage of emails sent to this contact with hard bounce tracking that hard bounced.
This field is a calculated field.

Available in API version 54.0 and later.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this contact with link tracking that had link clicks. This field
is a calculated field.

Available in API version 54.0 and later.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this contact with open tracking that were opened by the
recipient. This field is a calculated field.

Available in API version 54.0 and later.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this contact with out-of-office tracking that received
out-of-office replies. This field is a calculated field.

Available in API version 54.0 and later.


Standard Objects ContactDailyMetric

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
The percentage of emails sent to this contact with reply tracking that received replies. This
field is a calculated field.

Available in API version 54.0 and later.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this contact with soft bounce tracking that soft bounced.
This field is a calculated field.

Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of individual emails in which the contact clicked a link in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of individual emails opened by the contact in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of individual emails replied to by the contact in the day.


### Standard Objects ContactMonthlyMetric ContactMonthlyMetric

Represents the monthly engagement metrics for a contact. This object is available in API version 52.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Inbox must be enabled.

Fields

**Field** **Details**

```
AllCallsCallBackLater

AllCallsLeftVoicemail

AllCallsMeaningfulConnect

AllCallsNotInterested

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this contact with the call result Call Back Later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this contact with the call result Left Voicemail.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this contact with the call result Meaningful Connect.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this contact with the call result Not Interested.


Standard Objects ContactMonthlyMetric

**Field** **Details**

```
AllCallsUncategorized

AllCallsUnqualified

AllEmailsBouncedCount

AllEmailsDeliveredCount

AllEmailsDeliveredRate

AllEmailsHardBouncedCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this contact with no call result specified.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this contact with the call result Unqualified.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total of hard and soft bounced emails for this contact in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of successfully delivered emails for this contact in the month.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of tracked emails sent that were successfully delivered to this contact.
Available in API version 54.0 and later.

This field is a calculated field.

**Type**
int


Standard Objects ContactMonthlyMetric

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of hard bounced emails for this contact in the month.

```
AllEmailsOutOfOfficeCount

AllEmailsSentCount

AllEmailsSoftBouncedCount

AllEmailsTrackedSentCount

AllEmailsUntrackedSentCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that triggered an out of office reply for this contact in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails soft bounced for this contact in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with engagement tracking enabled in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact without engagement tracking enabled in the
month.


Standard Objects ContactMonthlyMetric

**Field** **Details**

```
AllTotalCallsCount

ContactId

HardBounceTrackableSends

LinkClickTrackableSends

Month

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of calls to this contact with all call results in the month.

This is a calculated field.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related contact.

This is a relationship field.

**Relationship Name**
Contact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with hard bounce tracking. Available in API version
54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with link click tracking. Available in API version
54.0 and later.

**Type**
date


Standard Objects ContactMonthlyMetric

**Field** **Details**

**Properties**
Filter, Group, Sort

**Description**
The month in which the engagement occurred.

```
MonthInt

OpenTrackableSends

OutOfOfficeTrackableSends

ReplyTrackableSends

SoftBounceTrackableSends

```

**Type**
int

**Properties**
Filter, Group, idLookup, Sort

**Description**
The month in which the engagement occurred, in yyyymm format.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with open tracking. Available in API version 54.0
and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with out-of-office tracking. Available in API version
54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with reply tracking. Available in API version 54.0
and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ContactMonthlyMetric

**Field** **Details**

**Description**
The number of emails sent to this contact with soft bounce tracking. Available in API version
54.0 and later.

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
The percentage of emails sent to this contact with hard bounce tracking that hard bounced.
Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this contact with link tracking that had link clicks. Available
in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this contact with open tracking that were opened by the
recipient. Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this contact with out-of-office tracking that received
out-of-office replies. Available in API version 54.0 and later.

This field is a calculated field.


Standard Objects ContactMonthlyMetric

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
The percentage of emails sent to this contact with reply tracking that received replies.
Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this contact with soft bounce tracking that soft bounced.
Available in API version 54.0 and later.

This field is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of individual emails in which the contact clicked a link in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of individual emails opened by the contact in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of individual emails replied to by the contact in the month.


### Standard Objects ContactPointAddress ContactPointAddress

Represents a contact’s billing or shipping address, which is associated with an individual or person account. This object is available in
API version 49.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ActiveFromDate

ActiveToDate

Address

AddressFirstName

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the contact’s address became active.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the contact’s address is no longer active.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The full address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
First name associated with the address.

The field is available only if the B2B Commerce license is enabled.

This field is available in API version 57.0 and later.


Standard Objects ContactPointAddress

**Field** **Details**

```
AddressLastName

AddressMiddleName

AddressType

BestTimeToContactEndTime

BestTimeToContactStartTime

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Last name associated with the address.

The field is available only if the B2B Commerce license is enabled.

This field is available in API version 57.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Middle name associated with the address.

The field is available only if the B2B Commerce license is enabled.

This field is available in API version 57.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the type of address.

Possible values are:

**•** `Billing`

**•** `Shipping`

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The latest time to contact the individual.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects ContactPointAddress

**Field** **Details**

**Description**
The earliest time to contact the individual.

```
BestTimeToContactTimezone

City

CompanyName

ContactPointPhoneId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The time zone applied to the best time to contact the individual.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The address city.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Company name associated with the address.

The field is available only if the B2B Commerce license is enabled.

This field is available in API version 57.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the primary phone number associated with this address.

This is a relationship field.

**Relationship Name**
ContactPointPhone

**Relationship Type**
Lookup

**Refers To**
ContactPointPhone


Standard Objects ContactPointAddress

**Field** **Details**

```
Country

GeocodeAccuracy

IsDefault

IsPrimary

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The address country.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The level of accuracy of a location’s geographical coordinates compared with its physical
address. A geocoding service typically provides this value based on the address’s latitude
and longitude coordinates.

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
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a contact’s address is the preferred method of communication ( `true` )
or not ( `false` ). The default value is `false` .

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects ContactPointAddress

**Field** **Details**

**Description**
Indicates whether a contact’s address is their primary address ( `true` ) or not ( `false` ). The
default value is `false` .

```
IsThirdPartyAddress

LastReferencedDate

LastViewedDate

Latitude

Longitude

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the address is associated with a third party ( `true` ) or not ( `false` ). The
default value is `false` .

This field is available in API version 57.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last referenced a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced ( `LastReferencedDate` ) and not viewed.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Longitude` to specify the precise geolocation of the address. Acceptable values
are numbers between –90 and 90 with up to 15 decimal places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


Standard Objects ContactPointAddress

**Field** **Details**

**Description**
Used with `Latitude` to specify the precise geolocation of the address. Acceptable values
are numbers between –180 and 180 with up to 15 decimal places.

```
Name

OwnerId

ParentId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. The name of the contact point address record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the account’s owner associated with this contact.

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
The ID of the contact’s parent record. Only an individual or account can be a contact’s parent.
Because this is a master-detail relationship, users must have Edit access to the parent record
to create or modify a Contact Point Address.

This is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Master-detail

**Refers To**
Account, Individual


Standard Objects ContactPointAddress

**Field** **Details**

```
PhoneNumber

PostalCode

PreferenceRank

State

Street

UsageType

```

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number associated with the address.

The field is available only if the B2B Commerce license is enabled.

This field is available in API version 57.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The address postal code.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Preference rank when there are multiple contact point addresses.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The address state.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The address street.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


### Standard Objects ContactPointConsent

**Field** **Details**

**Description**
Specify the usage type of this address. For instance, whether it’s a work address or a home
address.

Possible values are:

**•** `Home`

**•** `Inactive`

**•** `Temporary`

**•** `Work`

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ContactPointAddressChangeEvent**

Change events are available for the object.

**ContactPointAddressHistory**

History is available for tracked fields of the object.

**ContactPointAddressShare**

Sharing is available for the object.

### ContactPointConsent

Represents a customer's consent to be contacted via a specific contact point, such as an email address or phone number. This object is
available in API version 48.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

With certain page layout and field-level security settings, some fields aren't visible or editable.

**Field** **Details**

```
BusinessBrandId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects ContactPointConsent

**Field** **Details**

**Description**
The ID of the Business Brand that the individual has given consent to for a contact point. This
is a relationship field. This field is available in API version 53.0 and later.

**Relationship Name**
BusinessBrand

**Relationship Type**
Lookup

**Refers To**
BusinessBrand

```
CaptureContactPointType

CaptureDate

CaptureSource

ContactPointId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Required. Indicates how you captured consent.

Possible values are:

**•** `Email`

**•** `MailingAddress`

**•** `Phone`

**•** `Social`

**•** `Web`

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Required. Date when consent was captured.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. Indicates how you captured consent. For example, a website or online form.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


Standard Objects ContactPointConsent

**Field** **Details**

**Description**
ID of the contact point record through which the customer is consenting to be contacted.

This is a polymorphic relationship field.

**Relationship Name**
ContactPoint

**Relationship Type**
Lookup

**Refers To**
ContactPointAddress, ContactPointEmail, ContactPointPhone

```
DataUsePurposeId

DoubleConsentCaptureDate

EffectiveFrom

EffectiveTo

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the data use purpose record that you want to associate this consent with.

This is a relationship field.

**Relationship Name**
DataUsePurpose

**Relationship Type**
Lookup

**Refers To**
DataUsePurpose

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date when double opt-in was captured.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date when consents starts.

**Type**
dateTime


Standard Objects ContactPointConsent

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

Date when consent ends.

```
EngagementChannelTypeId

LastReferencedDate

LastViewedDate

Name

OwnerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

ID of the engagement channel record through which the customer is consenting to be
contacted.

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
Name of the contact point type consent record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the account owner associated with this customer.


Standard Objects ContactPointConsent

**Field** **Details**

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
 PartyRoleId

 PrivacyConsentStatus

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Party Role for the individual you want to associate consent with. This is a
polymorphic relationship field. This field is available in API version 53.0 and later.

**Relationship Name**
PartyRole

**Relationship Type**
Lookup

**Refers To**
Customer, Seller

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. Identifies whether the individual or person account associated with this record
agrees to this form of contact.

Possible values are:

**•** `NotSeen`

**•** `OptIn`

**•** `OptInPending` —Available in API version 58.0 and later.

**•** `OptOut`

**•** `Seen`

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


### Standard Objects ContactPointEmail

**ContactPointConsentChangeEvent**

Change events are available for the object.

**ContactPointConsentHistory**

History is available for tracked fields of the object.

**ContactPointConsentOwnerSharingRule**

Sharing rules are available for the object.

**ContactPointConsentShare**

Sharing is available for the object.

### ContactPointEmail

Represents a contact’s email, which is associated with an individual or person account. This object is available in API version 48.0 and
later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ActiveFromDate

ActiveToDate

BestTimeToContactEndTime

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the contact’s email became active.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the contact’s email is no longer active.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The latest time to contact the individual.


Standard Objects ContactPointEmail

**Field** **Details**

```
BestTimeToContactStartTime

BestTimeToContactTimezone

EmailAddress

EmailDomain

EmailLatestBounceDateTime

EmailLatestBounceReasonText

```

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The earliest time to contact the individual.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The timezone applied to the best time to contact the individual.

**Type**
email

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The email address of the contact.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The domain of the contact’s email, which is everything after the @ sign.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when an email failed to reach its recipient.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The reason why the email didn’t reach its recipient.


Standard Objects ContactPointEmail

**Field** **Details**

```
EmailMailBox

IsPrimary

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
A subset of the contact’s email, which is everything before the @ sign.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a contact’s email is their primary email ( `true` ) or not ( `false` ).

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
Filter, Group, idLookup, Nillable, Sort

**Description**
Required. The name of the contact point email record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects ContactPointEmail

**Field** **Details**

**Description**
The ID of the account’s owner associated with this contact.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
 ParentId

UsageType

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the contact’s parent. Only an individual or account can be a contact’s parent.

This is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Account, Individual

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specify the usage type of this email. For instance, whether it’s a work email or a temporary
email.

Possible values are:

**•** `Home`

**•** `Temp`

**•** `Work`

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


### Standard Objects ContactPointPhone

**ContactPointConsentChangeEvent**

Change events are available for the object.

**ContactPointEmailHistory**

History is available for tracked fields of the object.

**ContactPointEmailOwnerSharingRule**

Sharing rules are available for the object.

**ContactPointEmailShare**

Sharing is available for the object.

### ContactPointPhone

Represents a contact’s phone number, which is associated with an individual or person account. This object is available in API version
48.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ActiveFromDate

ActiveToDate

AreaCode

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the contact’s phone number became active.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the contact’s phone number is no longer active.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The area code of the phone number’s location for the contact.


Standard Objects ContactPointPhone

**Field** **Details**

```
BestTimeToContactEndTime

BestTimeToContactStartTime

BestTimeToContactTimezone

ExtensionNumber

FormattedInternationalPhoneNumber

FormattedNationalPhoneNumber

```

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The latest time to contact the individual.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The earliest time to contact the individual.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The timezone applied to the best time to contact the individual.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The phone number extension for the contact.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The internationally recognized format for the contact’s phone number.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The nationally recognized format for the contact’s phone number.


Standard Objects ContactPointPhone

**Field** **Details**

```
IsBusinessPhone

IsFaxCapable

IsPersonalPhone

IsPrimary

IsSmsCapable

LastReferencedDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a contact’s phone number is a business number ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a contact’s phone number is a fax number ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a contact’s phone number is a personal number ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a contact’s phone number is their primary number ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a contact’s phone number can receive text messages ( `true` ) or not
( `false` ).

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


Standard Objects ContactPointPhone

**Field** **Details**

**Description**
The timestamp for when the current user last viewed a record related to this record.

```
LastViewedDate

Name

OwnerId

ParentId

```

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
Filter, Group, idLookup, Nillable, Sort

**Description**
Required. The name of the contact point phone record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the account’s owner associated with this contact.

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
The ID of the contact’s parent. Only an individual or account can be a contact’s parent.

This is a polymorphic relationship field.

**Relationship Name**
Parent


Standard Objects ContactPointPhone

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Account, Individual

```
PhoneType

PreferenceRank

TelephoneNumber

UsageType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of phone number for the contact.

Possible values are:

**•** `Home`

**•** `Mobile`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specify how this phone numbers ranks in terms of preference among the contact’s other
phone numbers.

**Type**
phone

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The phone number for the contact.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specify the usage type of this number. For instance, whether it’s a work phone or a home
phone.

Possible values are:

**•** `Home`

**•** `Temp`

**•** `Work`


### Standard Objects ContactPointTypeConsent

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ContactPointConsentChangeEvent**

Change events are available for the object.

**ContactPointPhoneHistory**

History is available for tracked fields of the object.

**ContactPointPhoneOwnerSharingRule**

Sharing rules are available for the object.

**ContactPointPhoneShare**

Sharing is available for the object.

### ContactPointTypeConsent

Represents consent for a contact point type, such as email or phone. This object is available in API version 45.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available if Data Protection and Privacy is enabled.

Fields

With certain page layout and field-level security settings, some fields aren't visible or editable.

**Field Name** **Details**

```
BusinessBrandId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Business Brand that the individual has given consent to for a contact
point type. this is a relationship field. This field is available in API version 53.0 and
later.

**Relationship Name**
BusinessBrand

**Relationship Type**
Lookup


Standard Objects ContactPointTypeConsent

**Field Name** **Details**

**Refers To**
BusinessBrand

```
CaptureContactPointType

CaptureDate

CaptureSource

ContactPointType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Required. Indicates how you captured consent. Possible values are:

**•** `Email`

**•** `MailingAddress`

**•** `Phone`

**•** `Social`

**•** `Web`

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Required. Date when consent was captured.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. Indicates how you captured consent. For example, a website or online
form.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Required. Represents the contact method you want to apply consent to. Possible
values are:

**•** `Email`

**•** `MailingAddress`

**•** `Phone`

**•** `Social`


Standard Objects ContactPointTypeConsent

**Field Name** **Details**

**•** `Web`

```
DataUsePurposeId

DoubleConsentCaptureDate

EffectiveFrom

EffectiveTo

EngagementChannelType

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the record for data use purpose that you want to associate this consent
with.

This is a relationship field.

**Relationship Name**
DataUsePurpose

**Relationship Type**
Lookup

**Refers To**
DataUsePurpose

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date when double opt-in was captured.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date when consents starts.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

Date when consent ends.

**Type**
picklist


Standard Objects ContactPointTypeConsent

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Required if a `ContactPointType` isn’t selected. Represents the contact
method you want to apply consent to. Possible values are:

**•** `Billboard`

**•** `Email`

**•** `MailingAddress`

**•** `Phone`

**•** `SMS`

**•** `Social`

**•** `Web`

This is a relationship field.

**Relationship Name**
EngagementChannelType

**Relationship Type**
Lookup

**Refers To**
EngagementChannelType

```
LastReferencedDate

LastViewedDate

Name

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


Standard Objects ContactPointTypeConsent

**Field Name** **Details**

**Description**
Name of the contact point type consent record.

```
OwnerId

PartyId

PartyRoleId

```

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
Create, Filter, Group, Sort, Update

**Description**
Required. Represents the record based on the Individual object you want to
associate consent with.

This is a relationship field.

**Relationship Name**
Party

**Relationship Type**
Lookup

**Refers To**
Individual

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Party Role for the individual you want to associate consent with.
This is a polymorphic relationship field. This field is available in API version 53.0
and later.


### Standard Objects ContactOwnerSharingRule

**Field Name** **Details**

**Relationship Name**
PartyRole

**Relationship Type**
Lookup

**Refers To**
Customer, Seller

```
PrivacyConsentStatus

```

Associated Objects

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. Identify whether the individual associated with this record agrees to
this form of contact. Possible values are:

**•** `NotSeen`

**•** `Seen`

**•** `OptIn`

**•** `OptInPending` —Available in API version 58.0 and later.

**•** `OptOut`

**•** `OptOutPending` —Available in API version 58.0 and later.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ContactPointConsentChangeEvent (API version 47.0)**
Change events are available for the object.

**ContactPointTypeConsentHistory**

History is available for tracked fields of the object.

**ContactPointTypeConsentOwnerSharingRule**

Sharing rules are available for the object.

**ContactPointTypeConsentShare**

Sharing is available for the object.

### ContactOwnerSharingRule

Represents the rules for sharing a contact with a User other than the owner.

Note: To enable access to this object for your org, contact Salesforce customer support. However, we recommend that you
instead use Metadata API to programmatically update owner sharing rules because it triggers automatic sharing rule recalculation.
[The SharingRules Metadata API type is enabled for all orgs.](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_sharingrules.htm)


Standard Objects ContactOwnerSharingRule

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `update()`,

```
   upsert()

```

Fields

**Field** **Details**

```
ContactAccessLevel

Description

DeveloperName

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the type of access granted to the target Group, UserRole, or
User for Contacts. The possible values are:

**•** `Read`

**•** `Edit`

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

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is specified,
performance may slow while Salesforce generates one for each record.


### Standard Objects ContactRequest

**Field** **Details**

```
GroupId

Name

UserOrGroupId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the source group. A Contact owned by a User in the source Group
triggers the rule to give access.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label of the sharing rule as it appears in the user interface. Limited to 80 characters.
Corresponds to **Label** on the user interface.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the User or Group being granted access.

Use this object to manage the sharing rules for contacts.

SEE ALSO:

### Contact

ContactShare

_[Metadata API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.api_meta.meta/api_meta/meta_sharingrules.htm)_ : SharingRules

### ContactRequest

Represents a customer’s request for support to get back to them about an issue. This object is available in API version 45.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`


Standard Objects ContactRequest

Fields

**Field Name** **Details**

```
AvailableCallbackAttempts

DelayBetweenCallbackAttempts

IsCallback

```

**Type**
integer

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the number of retries that are possible for a voice callback. Applies to
calls routed through Omni-Channel Unified Routing. Valid values are `0` through
`5` . The default is `0` .

Available in API version 66.0 and later.

**Type**
integer

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the delay between voice callback attempts in minutes. Applies to calls
routed through Omni-Channel Unified Routing. Valid values are `0` through
`10,080`, and the default is `0` .

Available in API version 66.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines how a voice call callback is handled after an agent accepts the callback
work item.

If set to `true`, when an agent accepts the work item, the Omni-Channel utility
doesn’t immediately dial the callback phone number. Instead, the agent can
determine how to handle the call. For example, after the agent accepts the work
item, they can view the callback details, transfer the call, or contact the end user
at another phone number. If the agent makes a call by using click-to-dial, the
call appears as a Callback call in the Omni-Channel utility.

If set to `false`, when the agent accepts the work item in the Omni-Channel
utility, the contact request is opened. The agent can review callback details. If
they call with click-to-dial, the call appears as an Outbound call in the
Omni-Channel utility.

The default value is `false` . Available in API version 60.0 and later.


Standard Objects ContactRequest

**Field Name** **Details**

```
LastReferencedDate

LastViewedDate

Name

OwnerId

PreferredChannel

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
null, this record might only have been referenced ( `LastReferencedDate` )
and not viewed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The contact request number.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the Salesforce record that owns the request.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist


Standard Objects ContactRequest

**Field Name** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The channel the customer selected as their preferred method of communication
in the contact request flow. For example:

**•** Phone

```
PreferredPhone

RequestDescription

RequestReason

Status

```

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The phone number the customer provided when requesting help in the contact
request flow.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the customer’s issue that they provided when requesting help
in the contact request flow.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The reason the customer provided when requesting help in the contact request
flow. These values are customizable in Object Manager. The default values are:

**•** Account

**•** Billing

**•** Case

**•** General

**•** Order

**•** Other

**•** Product

**Type**
picklist


Standard Objects ContactRequest

**Field Name** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The status of the contact request. For example:

**•** Abandoned

**•** Attempted

**•** Contacted

**•** New

```
WhatId

WhoId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Salesforce record the contact request is related to, such as an account,
case, opportunity, voice call, or work order.

This is a polymorphic relationship field.

**Relationship Name**
What

**Relationship Type**
Lookup

**Refers To**
Account, Case, Contact Request, Opportunity, WorkOrder

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Salesforce contact record the contact request is related to, such as a
contact, lead, or user.

This is a polymorphic relationship field.

**Relationship Name**
Who

**Relationship Type**
Lookup

**Refers To**
Contact, Lead, User


### Standard Objects ContactRequestShare

Usage

Contact request records are created when a customer fills out an online form. This form is created using a flow that uses the type
`ContactRequestFlow` . There’s a guided setup experience to create this flow on the Customer Contact Requests page in Setup.
You then add the flow to an Experience Cloud site using either the Flows component or the Contact Request Button & Flow component.

Contact Request works in Experience Cloud sites, whether they require authentication or not. Make sure that your users have the Run
Flows permission, including your Guest User profile. Without this permission, members won’t see the button or the form to submit
contact requests.

By default, all Standard User and System Administrator profiles have access to the object. Make sure that your users profiles, like service
agents, have at least read access on the contact request object.

You can create queues for contact requests and route them with Omni-Channel.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ContactRequestOwnerSharingRule**

Sharing rules are available for the object.

### **ContactRequestShare**

Sharing is available for the object.

SEE ALSO:

_Salesforce Help_ [: Set Up and Manage Contact Requests](https://help.salesforce.com/articleView?id=contact_request.htm&language=en_US)

### ContactRequestShare

Represents a list of access levels to a ContactRequest with an explanation of the access level. This object is available in API version 45.0
and later.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects ContactRequestShare

Fields

**Field Name** **Details**

```
AccessLevel

ParentId

RowCause

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Level of access that the User or Group has to contact requests. The possible values
are:

**•** `Read`

**•** `Edit`

**•** `All` (This value is not valid for `create()` or `update()` calls.)

This value must be set to an access level that is higher than the organization’s
default access level for contact requests.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the parent object, if any.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
ContactRequest

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only
permitted value is `Manual` . If no value is specified, the field defaults to `Manual` .
All other `RowCause` values are read-only. After the sharing entry is created,
this field can’t be edited.

Possible values are:

**•** `Manual` —The User or Group has access because a user with “All” access
manually shared the ContactRequest with them.


### Standard Objects ContactShare

**Field Name** **Details**

**•** `Owner` —The User is the owner of the ContactRequest.

**•** `Rule` —The User or Group has access via a ContactRequest sharing rule.

**•** `GuestRule` —The User or Group has access via a ContactRequest guest
user sharing rule.

```
UserOrGroupId

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the User or Group that has been given access to the ContactRequest.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User

This object lets you determine which users and groups can view and edit ContactRequest records owned by other users.

If you attempt to create a new record that matches an existing record, the `create()` call updates any modified fields and returns the
existing record.

SEE ALSO:

_Salesforce Help_ [: Set Up and Manage Contact Requests](https://help.salesforce.com/articleView?id=contact_request.htm&language=en_US)

### ContactShare

Represents a list of access levels to a Contact along with an explanation of the access level. For example, if you have access to a record
because you own it, the `ContactAccessLevel` is `All` and `RowCause` is Owner.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual` . Sharing entries
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.


Standard Objects ContactShare

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

As of Summer ’20 and later, only users with access to the Contact object can access this object.

Fields

**Field** **Details**

```
ContactId

ContactAccessLevel

IsDeleted

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the Contact associated with this sharing entry. This field can't be updated.

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
Filter, Group, Restricted picklist, Sort

**Description**
Level of access that the User or Group has to cases associated with the account Contact. The
possible values are:

**•** `Read`

**•** `Edit`

**•** `All` This value is not valid for create or update.

This field must be set to an access level that is higher than the organization’s default access
level for contacts.

**Type**
boolean

**Properties**
Defaulted on create, Filter


Standard Objects ContactShare

**Field** **Details**

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

```
RowCause

UserOrGroupId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only permitted
value is `Manual` . If no value is specified, the field defaults to `Manual` . All other `RowCause`
values are read-only. After the sharing entry is created, this field can’t be edited. Valid values
include:

**•** `Rule` —The User or Group has access via a Contact sharing rule.

**•** `GuestRule` —The User or Group has access via a Contact guest user sharing rule.

**•** `ImplicitChild` —The User or Group has access to the Contact via sharing access on
the associated Account. After faster account sharing recalculation is enabled for your org,
sharing entries with this value aren’t returned in queries. Instead of storing implicit child
shares, record access is determined dynamically.

**•** `ImplicitPerson` —The User or Group has access to the business contact of a person
account via access to the person account itself.

**•** `GuestPersonImplicit` —The guest user has access to the business contact of a
person account via a Contact sharing rule.

**•** `PortalImplicit` —The Contact is associated with the portal user.

**•** `LpuImplicit` —The User has access to records owned by high-volume Experience
Cloud site users via a share group.

**•** `ARImplicit` —The User, who belongs to a partner or customer account, has access
to the Contact via an account relationship data sharing rule.

**•** `Manual` —The User or Group has access because a User with “All” access manually shared
the Contact with them.

**•** `Owner` —The User is the owner of the Contact.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the User or Group that has been given access to the Contact. This field can't be updated.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup


### Standard Objects ContactSuggestionInsight

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Group, User

Usage

This object allows you to determine which users and groups can view or edit Contact records owned by other users.

Note: After faster account sharing recalculation is enabled for your org, we no longer store implicit share records between accounts
and their child contact records. Sharing entries that have a value of `ImplicitChild` in the `RowCause` field aren’t returned
when you query this object. Instead, the system dynamically determines whether users can access child contact records when
they try to access them. This change speeds up ownership and sharing recalculation for accounts.

[For more information, see the Faster Account Sharing Recalculation knowledge article.](https://help.salesforce.com/s/articleView?id=000394638&type=1&language=en_US)

SEE ALSO:

AccountShare

### ContactSuggestionInsight

Represents a suggestion for a new contact record. Available in API versions 45.0 and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

To add or decline contact suggestions, users need a Sales Cloud Einstein license and edit access on accounts. As of the Spring ’20 release,
Pardot and Sales Engagement users no longer have access to this object.

Fields

**Field Name** **Details**

```
AccountId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related account.


Standard Objects ContactSuggestionInsight

**Field Name** **Details**

```
Address

City

ContactTitle

Country

CreatedRecordId

CurrencyIsoCode

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
The address of the suggested contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The city of the suggested contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The title of the suggested contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The country of the suggested contact.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the created contact record.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort


Standard Objects ContactSuggestionInsight

**Field Name** **Details**

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

```
Division

Email

FirstName

GeocodeAccuracy

LastName

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The division of the suggested contact.

**Type**
email

**Properties**
Filter, Group, Nillable, Sort

**Description**

The email address of the suggested contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The first name of the suggested contact.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Accuracy level of the geocode for the address. See Compound Field
Considerations and Limitations for details on geolocation compound fields.

Note: This field is available in the API only.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The last name of the suggested contact.


Standard Objects ContactSuggestionInsight

**Field Name** **Details**

```
LastOperationUserId

LastReferencedDate

LastViewedDate

Latitude

Longitude

Phone

```

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
The timestamp when the current user last accessed this record, a record related
to this record, or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, the user might have only accessed this record or list view
( `LastReferencedDate` ) but not viewed it.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Used in conjunction with `Longitude` to specify the precise geolocation of an
address.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Used in conjunction with `Latitude` to specify the precise geolocation of an
address.

**Type**
phone


Standard Objects ContactSuggestionInsight

**Field Name** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The phone number of the suggested contact.

```
PostalCode

RationaleLabel

State

Status

Street

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The postal code of the suggested contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The reason why this entry is a suggested contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The state of the suggested contact.

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

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects ContactTag

**Field Name** **Details**

**Description**
The street of the suggested contact.

Usage

This object is read-only and isn’t supported in workflows, triggers, process builder, or Visualforce pages.

### ContactTag

Associates a word or short phrase with a Contact.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
ItemId

Name

TagDefinitionId

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


### Standard Objects ContentAsset

**Field Name** **Details**

```
Type

```

Usage

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

ContactTag stores the relationship between its parent TagDefinition and the Contact being tagged. Tag objects act as metadata, allowing
users to describe and organize their data.

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.

### ContentAsset

Represents a Salesforce file that has been converted to an asset file in a custom app in Lightning Experience. Use asset files for org setup
and configuration. Asset files can be packaged and referenced by other components. This object is available in API version 38.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

**•** Only admin users can edit or delete ContentAssets.

**•** Users with file access can create and query ContentAssets.

**•** It isn’t necessary to create asset files for regular, collaborative use of Salesforce Files. “Assetize” files only when they’re used in setup
and configuration situations.

**•** Neither the file (ContentDocument) nor the asset settings record (ContentAssets) can be deleted if the asset file is referenced by
another component.

### • ContentAsset doesn’t support search or most recently used (MRU) lists. • ContentAsset doesn’t support Apex triggers.


Standard Objects ContentAsset

Fields

**Field** **Details**

```
ContentDocumentId

DeveloperName

IsVisibleByExternalUsers

Language

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the document.

This is a relationship field.

**Relationship Name**
ContentDocument

**Relationship Type**
Lookup

**Refers To**
ContentDocument

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the asset file in the API. ContentAsset.DeveloperName:

**•** must be 40 characters or fewer

**•** must begin with a letter

**•** can contain only underscores and alphanumeric characters

**•** can’t include spaces

**•** can’t end with an underscore

**•** can’t contain 2 consecutive underscores

In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether unauthenticated users can see the asset file.

**Type**
picklist


### Standard Objects ContentBody

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language for this document. This field defaults to the user's language unless the org is
multi-language enabled. Specifies the language of the labels returned. The value must be a
valid user locale (language and country), such as `de_DE` or `en_GB` . For more information
on locales, see the `Language` field on the CategoryNodeLocalization object.

```
MasterLabel

NamespacePrefix

### ContentBody

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label for the asset file. This internal label doesn’t get translated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix associated with this object. Each Developer Edition organization that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
_**`namespacePrefix`**_ `__` _**`componentName`**_ notation.

Represents the body of a file in Salesforce CRM Content or Salesforce Files. This object is available in API version 40.0 and later.

Supported Calls

```
describeSObjects()

```

Special Access Rules

Cannot be queried, inserted, updated, or deleted directly.


### Standard Objects ContentDistribution

Fields

**Field** **Details**

```
Id

```

Usage

**Type**
ID

**Properties**
, Filter, Group, idLookup, Sort

**Description**
ID of the file body.

ContentBody is intended for internal Salesforce use. If you need to access the file content body, please use ContentVersion on page 1526.

### ContentDistribution

Represents information about sharing a document externally. This object is available in API version 32.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

**•** Content deliveries must be enabled to query content deliveries.

**•** Users (including users with the “View All Data” permission) can query only the files that they have access to. If the file is managed
by a Content Library, the user must have “Deliver Content” enabled in the library permission definition and be a member of the
library. If the file isn’t managed by a Content Library, the user must have the “Enable Creation of Content Deliveries for Salesforce
Files” permission.

**•** Users can query the `DistributionPublicUrl` and `Password` fields only if they are the file owner, if the file is shared with
them, or if the `RelatedRecordId` specifies a record that the users can access.

**•** If the shared document is deleted, the delete cascades to any associated ContentDistribution. The ContentDistribution is still queryable
by using the `QueryAll` verb.

**•** If the shared document is archived, the only fields that users can edit are `ExpiryDate` and `PreferencesExpires` .

**•** Customer Portal users can’t access this object.

**•** Guest users of Experience Cloud sites can't access or create this object.

**•** Chatter Free users can’t access this object.


Standard Objects ContentDistribution

Fields

**Field Name** **Details**

```
ContentDocumentId

ContentDownloadUrl

ContentVersionId

DistributionPublicUrl

ExpiryDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the shared document.

**Type**
string

**Properties**
Sort, Nillable

**Description**
The link for downloading the file. This field is available in API version 40.0 and
later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the shared document version.

This is a relationship field.

**Relationship Name**
ContentVersion

**Relationship Type**
Lookup

**Refers To**
ContentVersion

**Type**
string

**Properties**
Nillable, Sort

**Description**
URL of the link to the shared document.

**Type**
dateTime


Standard Objects ContentDistribution

**Field Name** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date when the shared document becomes inaccessible.

```
FirstViewDate

LastViewDate

Name

OwnerId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date when the shared document is first viewed.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date when the shared document was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the content delivery.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the user who owns the shared document.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User


Standard Objects ContentDistribution

**Field Name** **Details**

```
PdfDownloadUrl

Password

PreferencesAllowOriginalDownload

PreferencesAllowPDFDownload

PreferencesAllowViewInBrowser

```

**Type**
string

**Properties**
Sort, Nillable

**Description**
The link for downloading the file as a PDF. This field is available in API version
40.0 and later.

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
A password that allows access to a shared document.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, the shared document can be downloaded as the file type that it
was uploaded as.

When `false`, download availability depends on whether a preview of the file
exists. If a preview exists, the file can’t be downloaded. If a preview doesn’t exist,
the file can still be downloaded.

If the shared document is a link, it can’t be downloaded.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, the shared document can be downloaded as a PDF if the original
file type is PDF or if a PDF preview has been generated.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, a preview of the shared document can be viewed in a Web browser.


Standard Objects ContentDistribution

**Field Name** **Details**

```
PreferencesExpires

PreferencesLinkLatestVersion

PreferencesNotifyOnVisit

PreferencesNotifyRndtnComplete

PreferencesPasswordRequired

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, access to the shared document expires on the date that’s specified
by `ExpiryDate` .

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, users see the most recent version of a shared document. When
`false`, users see the version of the document that’s shared, even if it isn’t the
most recent version.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, the owner of the shared document is emailed the first time that
someone views or downloads the shared document.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, the owner of the shared document is emailed when renditions of
the shared document that can be previewed in a Web browser are generated.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
When `true`, a password, specified by `Password`, is required to access the
shared document.


Standard Objects ContentDistribution

**Field Name** **Details**

```
RelatedRecordId

ViewCount

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the record, such as an Account, Campaign, or Case, that the shared document
is related to.

This is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
Account, Campaign, Case, Contact, EmailMessage, Lead, ListEmail, Opportunity

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times that the shared document has been viewed.

Use this object to create, update, delete, or query information about a document shared externally via a link or via Salesforce CRM Content
delivery.

The ContentDistribution object supports triggers before and after these operations: insert, update, delete. It supports triggers after
undelete.

Example: The VP of Marketing wants file authors to specify whether their files can be shared with external people using content
delivery. He also wants some files to have a password. You can add a custom field `DeliveryPolicy` on the ContentVersion
object. Make the custom field a picklist with the values, `Allowed`, `Blocked`, and `Password required` . Add the field to
the ContentVersion layout so that the user can set the delivery policy per file. Then, add an insert trigger for the ContentDistribution
object to enforce the rules based on the delivery policy set in the file.

Note: The `ContentVersionId` for `ContentDistribution` must be unique.

This trigger for the ContentDistribution object enforces the delivery policy rules for each file:

```
   trigger deliveryPolicy on ContentDistribution (before insert) {

     for (ContentDistribution cd : trigger.new) {

        String versionId = DeliveryPolicyHelper.getContentVersionId(cd);

        ContentVersion version = [select DeliveryPolicy__c from ContentVersion where

   Id = :versionId];

```


### Standard Objects ContentDistributionEventLog

```
           String policy = version.DeliveryPolicy__c;

           if (policy.equals('Blocked')) {

             cd.addError('This file is not allowed to be delivered.');

           } else if (policy.equals('Password required')){

             if (!DeliveryPolicyHelper.requirePassword(cd)) {

               cd.addError('To deliver this file, set a password.');

             }

           }

        }

      }

```

The trigger calls this helper class:

```
      public class DeliveryPolicyHelper {

        public static String getContentVersionId(ContentDistribution cd) {

           if (cd.ContentVersionId != null) {

             return cd.ContentVersionId;

           } else {

             String versionId = [select LatestPublishedVersionId from ContentDocument

      where Id = :cd.ContentDocumentId].get(0).LatestPublishedVersionId;

             return versionId;

           }

        }

        public static boolean requirePassword(ContentDistribution cd) {

           return cd.PreferencesPasswordRequired;

        }

      }

```

Important: Apex has a per organization limit of 10 concurrent requests that last longer than 5 seconds. A trigger that uploads
files can easily hit this limit.

### ContentDistributionEventLog

Content Distribution events contain information about content distributions and deliveries to users. This object is available in API version
65.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.


Standard Objects ContentDistributionEventLog

Fields

**Field** **Details**

```
Action

DeliveryIdentifier

DeliveryLocation

RelatedObjectIdentifier

RequestIdentifier

Timestamp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The action that’s used when a delivery is viewed.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the content delivery.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The location of the delivery.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the record that’s associated with the delivery distribution.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same REQUEST_ID.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


### Standard Objects ContentDistributionView

**Field** **Details**

**Description**
The access time of Salesforce services in GMT. For example, `20130715233322.670` .

```
UserIdentifier

VersionIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.
For example: `00530000009M943` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the content version.

### ContentDistributionView

Represents information about views of a shared document. This read-only object is available in API version 32.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`

Special Access Rules

**•** Content deliveries must be enabled to query content deliveries.

**•** Users (including users with the “View All Data” permission) can query only the files that they have access to. If the file is managed
by a Content Library, the user must have “Deliver Content” enabled in the library permission definition and be a member of the
library. If the file isn’t managed by a Content Library, the user must have the “Enable Creation of Content Deliveries for Salesforce
Files” permission.

### • ContentDistributionView can be deleted by an admin.

**•** If the shared document is deleted, the delete cascades to any associated ContentDistributionView. The ContentDistributionView is
still queryable by using the `QueryAll` verb.

**•** Customer Portal users can’t access this object.

**•** Chatter Free users can’t access this object.


Standard Objects ContentDistributionView

Fields

**Field Name** **Details**

```
DistributionId

IsDownload

IsInternal

ParentViewId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the content delivery that the document is part of.

This is a relationship field.

**Relationship Name**
Distribution

**Relationship Type**
Lookup

**Refers To**
ContentDistribution

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
`true` if the shared document is downloaded; `false` if the shared document
is viewed.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
`true` if the shared document is viewed by a user in the same organization;
`false` if viewed by an external user.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of this instance of accessing the shared document.


### Standard Objects ContentDocument

Usage

Use this read-only object to query information about users who are accessing shared documents.

### ContentDocument

Represents a document that was uploaded to a library in Salesforce Files or Salesforce CRM content. This object is available in versions
17.0 and later for Salesforce CRM.This object is available in API version 21.0 and later for Salesforce Files.

The maximum number of documents that can be published is 30,000,000. Archived files count toward this limit and toward storage
usage limits.

**•** Contact Manager, Group, Professional, Enterprise, Unlimited, and Performance Edition customers can publish a maximum of 200,000
new versions per 24-hour period.

**•** Developer Edition and trial users can publish a maximum of 2,500 new versions per 24-hour period.

Supported Calls

`delete()`, `describeLayout()describeSObjects()`, `query()`, `retrieve()`, `search()`, `undelete()`,

```
   update()

```

Special Access Rules

**•** By default, users (including users with the View All Data permission) can only query files they have access to, including:

**–** Salesforce files in their personal library and in libraries they're a member of, regardless of library permissions (API version 17.0
and later).

**–** Salesforce files they own, shared directly with them, posted on their profile, or posted on groups they can see (API version 21.0
and later).

Turn on the Query All Files permission to let your View All Data users bypass the restrictions on querying files.

**–** Query All Files returns all files, including files in non-member libraries and files in unlisted groups.

**–** Users can’t edit, upload new versions, or delete files they don’t have access to.

**–** View All Data permission is required to enable Query All Files.

**•** For API version 62.0 and later, enable the Query Non Vetoed Files permission in Data Cloud orgs to let your integration or API users
view and SOQL query only public and non-vetoed files in the org.

**•** Customer and partner portal users must have the View Content in Portal permission to query content in libraries where they have
access.

**•** A Salesforce CRM content document can be deleted if any of these statements is true.

**–** The document is published into a personal library or is in the user's upload queue.

**–** The document is published into a public library, the user trying to delete the document is the file owner, and is a member of
that library.

**–** The document is published into a public library and the user trying to delete the document isn’t the owner but has the Manage
Library or Delete Content library permission enabled.

For API version 25.0 and later, you can change ownership of Salesforce Files and Salesforce CRM content documents.

**•** A user can change ownership of a Salesforce CRM content document or Salesforce file if any of these statements is true.


Standard Objects ContentDocument

**–** The user is the current owner.

**–** The user has the Modify All Data permission enabled.

**–** For a file in a Content Library, the user either has the Manage Salesforce CRM content permission enabled, or has the Manage
Library permission enabled for the library containing the document.

Note: When the owner of a ContentDocument is changed, ContentDocumentLink may be triggered. This action deletes the
ContentDocumentLink to the old owner and inserts one to the new owner. When you change document ownership, keep
these considerations in mind.

**–** The user who’s becoming the document owner must be a visible, active user. The original owner can be inactive.

**–** If the new document owner doesn’t have access to the library that contains the document, library administrators must
give the new owner membership to the library.

Fields

**Field** **Details**

```
ArchivedById

ArchivedDate

ContentAssetId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who archived the document.

This field is available in API version 24.0 and later.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date when the document was archived.

This field is available in API version 24.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
If the ContentDocument is an asset file, this field points to the asset. For most entities, the
value of this field is `null` .

This field is available in API version 38.0 and later.

This is a relationship field.

**Relationship Name**
ContentAsset


Standard Objects ContentDocument

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
ContentAsset

```
ContentModifiedDate

ContentSize

ContentSizeLong

Description

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the document was modified.

`ContentModifiedDate` updates when, for example, the document is renamed or a
new document version is uploaded. When you’re uploading the first version of a document,
`ContentModifiedDate` can be set to the current time or anytime in the past.

This field is available in API version 32.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

The size of the document in bytes for documents smaller than 2 GB.

This field is available in API version 31.0 and later. In API version 65.0 and later, we recommend
that you use the `ContentSizeLong` field even for files smaller than 2 GB.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**

The size of the document in bytes up to 10 GB.

This field is available in API version 65.0 and later.

**Type**
textarea

**Properties**
Filter, Nillable, Sort, Update

**Description**

A description of the document.

This field is available in API version 31.0 and later.


Standard Objects ContentDocument

**Field** **Details**

```
Division

FileExtension

FileType

IsArchived

IsInternalOnly

```

**Type**
picklist

**Properties**
Defaulted on Create, Filter, Group, Restricted picklist, Sort

**Description**
A logical segment of your organization's data. For example, if your company is organized
into different business units, you could create a division for each business unit, such as “North
America,” “Healthcare,” or “Consulting.” Available only if the organization has the Division
permission enabled.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

File extension of the document.

This field is available in API version 31.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Type of document, determined by the file extension.

This field is available in API version 31.0 and later.

**Type**
boolean

**Properties**
Defaulted on Create, Filter, Group, Sort, Update

**Description**
Indicates whether the document was archived ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Defaulted on Create, Filter, Group, Sort, Update

**Description**
Indicates that a file is for internal use only. When `true`, prevents users with the Query Non
Vetoed Files permission from viewing and performing SOQL query on public and non vetoed
files in a Data Cloud org. Default value is `false` .


Standard Objects ContentDocument

**Field** **Details**

This field is available in API version 62.0 and later.

```
LastReferencedDate

LastViewedDate

LatestPublishedVersionId

```

`MalwareScanDate` (Beta)

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
record might only have been referenced ( `LastReferencedDate` ) and not viewed.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the latest document version (ContentVersion).

This is a relationship field.

**Relationship Name**
LatestPublishedVersion

**Relationship Type**
Lookup

**Refers To**
ContentVersion

**Type**
dateTime

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date the document was scanned for malware. This field is available as a beta feature in
API version 66.0 and later.

Note: The `MalwareScanDate` field is a pilot or beta service that is subject to
[the Beta Services Terms at Agreements - Salesforce.com or a written Unified Pilot](https://www.salesforce.com/company/legal/agreements/)


Standard Objects ContentDocument

**Field** **Details**

[Agreement if executed by Customer, and applicable terms in the Product Terms](https://ptd.salesforce.com/)
[Directory. Use of this pilot or beta service is at the Customer's sole discretion.](https://ptd.salesforce.com/)

`MalwareScanStatus` (Beta)

```
OwnerId

ParentId

```

**Type**
picklist

**Properties**
Filter, Group, Sort

**Description**
Indicates whether the document was scanned for malware and whether it’s safe or malicious.
This field is available in API version 66.0 and later.

**•** `NotScanned` —The file hasn’t yet been scanned for malware. This is the default value.

**•** `Scheduled` —The file scan is in progress.

**•** `Clean` —The file was scanned and doesn’t contain malware.

**•** `Malicious` —The file was scanned and contains malware.

**•** `Skipped` —The file can’t be scanned because it’s either larger than 100 MB or it’s a
Salesforce-generated file, such as a Content Note.

**•** `Failed` —The file wasn’t scanned because of an error.

Note: The `MalwareScanStatus` field is a pilot or beta service that is subject
[to the Beta Services Terms at Agreements - Salesforce.com or a written Unified Pilot](https://www.salesforce.com/company/legal/agreements/)
[Agreement if executed by Customer, and applicable terms in the Product Terms](https://ptd.salesforce.com/)
[Directory. Use of this pilot or beta service is at the Customer's sole discretion.](https://ptd.salesforce.com/)

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
ID of the owner of this document.

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
Filter, Group, Nillable, Sort, Update


Standard Objects ContentDocument

**Field** **Details**

**Description**
ID of the library that owns the document. Created automatically when inserting a
ContentVersion via the API for the first time.

This field is available in API version 24.0 and later when Salesforce CRM content is enabled.

```
PublishStatus

SharingOption

SharingPrivacy

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**

Indicates if and how the document is published. Valid values are:

**•** `P` —The document is published to a public library and is visible to other users. Label is
**Public** .

**•** `R` —The document is published to a personal library and is not visible to other users.
Label is **Personal Library** .

**•** `U` —The document is not published because publishing was interrupted. Label is **Upload**
**Interrupted** .

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Controls whether sharing is frozen for a file. Only administrators and file owners with
Collaborator access to the file can modify this field. Default is `Allowed`, which means that
new shares are allowed. When set to `Restricted`, new shares are prevented without
affecting existing shares.

This field is available in API versions 35.0 and later.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Controls sharing privacy for a file. Only administrators and file owners with Collaborator
access to the file can modify this field.

Valid values are:

**•** `N` —Default. Label is **Visible to Anyone With Record Access**

**•** `P` —The file is private on records but can be shared selectively with others. Label is
**Private on Records** .

This field is available in API versions 41.0 and later.


Standard Objects ContentDocument

**Field** **Details**

```
Title

```

Usage

**Type**
string

**Properties**
Filter, Group, idLookup, Sort, Update

**Description**

The title of a document.

**•** Use this object to retrieve, query, update, and delete the latest version of a document in a library or a Salesforce file. Use the
ContentVersion object to create, query, retrieve, search, edit, and update a specific version of a Salesforce CRM content document
or Salesforce file.

**•** A document record is a container for multiple version records. You create a version to add a document to the system. The new
version contains the actual file data which allows the document to have multiple versions. The version stores the body of the uploaded
document.

**•** To create a document, create version via the ContentVersion object without setting the `ContentDocumentId` . This process
automatically creates a parent document record. When adding a new version of the document, you must specify an existing
`ContentDocumentId` which initiates the revision process for the document. When the latest version is published, the title,
owner, and publish status fields are updated in the document.

**•** You can’t add new versions of archived documents.

**•** When you delete a document, all versions of that document are deleted, including ratings, comments, and tags.

**•** A ContentDocument insert trigger executes when a file (ContentDocument) is added to the file library.

**•** A ContentDocument delete trigger executes when a file is deleted, but the cascaded ContentDocumentLink delete does not trigger
ContentDocumentLink triggers.

**•** The `query()` call doesn’t return archived documents. The `queryAll()` call returns archived documents.

**•** To query a file that is accessible only through a record share, you must specify the content ID of the file. When SOQL querying the
ContentDocument object, the `ContentDocumentId` must be compounded by an AND operator.

For example,

```
  SELECT Id, Title FROM ContentDocument

  WHERE (Id = '<ContentDocumentId>' and Title LIKE '%<title>%'

  SELECT Id, Title, MyCustomField_c FROM ContentDocument

  WHERE (Id IN ('<Id1>', '<Id2>')) AND (Title LIKE '%<title1>%' OR (Title LIKE '%<title2>%')

```

**•** If you query versions in the API, versions with a `PublishStatus` of `Upload Interrupted` are not returned.

**•** Assign topics to ContentDocument using `TopicAssignment` in API version 37.0 or later.

Associated Objects

This object has the following associated objects. Unless noted, associated objects are available in the same API version as this object.

**ContentDocumentChangeEvent on page 68 (API version 55.0)**
Change events are available for the object.


### Standard Objects ContentDocumentHistory

**ContentDocumentFeed (API version 20.0)**
Feed tracking is available for the object.

### **ContentDocumentHistory**

History is available for tracked fields of the object.

SEE ALSO:

### ContentDocumentHistory

ContentVersion

### ContentDocumentHistory

Represents the history of a document. This object is available in versions 17.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Special Access Rules

**•** Customer and Partner Portal users must have the “View Content in Portal” permission to query content in libraries where they have
access.

**•** A user can query all versions of a document from their personal library and any version that is part of or shared with a library where
they are a member, regardless of library permissions.

Fields

**Field** **Details**

```
ContentDocumentId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the document.

This is a relationship field.

**Relationship Name**
### ContentDocument

**Relationship Type**
Lookup

**Refers To**
### ContentDocument


Standard Objects ContentDocumentHistory

**Field** **Details**

```
DataType

Division

Field

NewValue

OldValue

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
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
A logical segment of your organization's data. For example, if your company is organized
into different business units, you could create a division for each business unit, such as “North
America,” “Healthcare,” or “Consulting.” Available only if the organization has the Division
permission enabled.

**Type**
picklist

**Properties**
Filter, Group, Sort, Restricted picklist

**Description**
The name of the field that was changed. Possible values include:

**•** `contentDocPublished` —The document is published into a library.

**•** `contentDocUnpublished` —The document is archived or removed from a library,
either directly or when the owning library is changed.

**•** `contentDocRepublished` —The document is removed from the archive.

**•** `contentDocFeatured` —The document is featured.

**•** `contentDocSubscribed` —The document is subscribed to.

**•** `contentDocUnsubscribed` —The document is no longer subscribed to.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The new value of the field that was changed.

**Type**
anyType


### Standard Objects ContentDocumentLink

**Field** **Details**

**Properties**
Nillable, Sort

**Description**
The latest value of the field before it was changed.

Usage

Use this read-only object to query the history of a document.

SEE ALSO:

### ContentDocument ContentDocumentLink

Represents the link between a Salesforce CRM Content document, Salesforce file, or ContentNote and where it's shared. A file can be
shared with other users, groups, records, and Salesforce CRM Content libraries. This object is available in versions 21.0 and later for
Salesforce CRM Content documents and Salesforce Files.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

**•** In API versions 59.0 and later, turn on the Query All Files permission to query without a filter on `id`, `LinkedEntityId`, and
`documentID` fields. The View All Data permission is required to turn on Query All Files.

**•** In API versions 33.0 and later, you can create and delete ContentDocumentLink objects with a `LinkedEntityId` of any record
type that can be tracked in the feed, even if feed tracking is disabled for that record type.

**•** In API versions 25.0 and later, you can create ContentDocumentLink objects with a `LinkEntityId` of type User, CollaborationGroup,
or Organization.

**•** In API versions 21.0 and later, users with explicit Viewer access (the file has been directly shared with the user) to a file can delete
### ContentDocumentLink objects between the file and other users who have Viewer access. In the same API versions, any user with

Viewer access to a file can delete ContentDocumentLink objects between the file and organizations or groups of which they’re a
member.

**•** For orgs with Digital Experiences enabled, a document can be shared with only users and groups that are a part of the Experience
Cloud site the file was created in.


Standard Objects ContentDocumentLink

Fields

**Field** **Details**

```
ContentDocumentId

LinkedEntityId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the document.

This is a relationship field.

**Relationship Name**
ContentDocument

**Relationship Type**
Lookup

**Refers To**
ContentDocument

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the linked object. Can include Chatter users, groups, records (any that support Chatter
feed tracking including custom objects), and Salesforce CRM Content libraries.

Using the API only, you can relate notes to custom settings.

This is a polymorphic relationship field.

**Relationship Name**
LinkedEntity

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


Standard Objects ContentDocumentLink

**Field** **Details**

CareRegisteredDevice, CareRequest, CareRequestDrug, CareRequestExtension,
CareRequestItem, CareSpecialty, CareSpecialtyTaxonomy, CareTaxonomy, Case, CodeSet,
CollaborationGroup, CommSubscription, CommSubscriptionChannelType,
CommSubscriptionConsent, CommSubscriptionTiming, ConsumptionSchedule, Contact,
ContactEncounter, ContactEncounterParticipant, ContentWorkspace, Contract,
ConversationEntry, CoverageBenefit, CoverageBenefitItem, CredentialStuffingEventStore,
CreditMemo, CreditMemoLine, Dashboard, DashboardComponent, DataStream,
DelegatedAccount, DocumentChecklistItem, EmailMessage, EmailTemplate,
EngagementChannelType, EnhancedLetterhead, EnrollmentEligibilityCriteria, Event,
HealthcareFacility, HealthcareFacilityNetwork, HealthcarePayerNetwork,
HealthcarePractitionerFacility, HealthcareProvider, HealthcareProviderNpi,
HealthcareProviderSpecialty, HealthcareProviderTaxonomy, Identifier, Image,
IndividualApplication, Invoice, InvoiceLine, Lead, ListEmail, Location, MarketSegment,
MarketSegmentActivation, MemberPlan, MessagingSession, MktCalculatedInsight,
OperatingHours, Opportunity, Order, OrderItem, Organization, OtherComponentTask,
OutgoingEmail, PartyConsent, PersonEducation, PersonLanguage, PersonLifeEvent,
PersonName, PlanBenefit, PlanBenefitItem, Product2, ProductFulfillmentLocation, ProductItem,
ProductItemTransaction, ProductRequest, ProductRequestLineItem, ProductRequired,
ProductTransfer, ProfileSkill, ProfileSkillEndorsement, ProfileSkillUser, ProviderSearchSyncLog,
PurchaserPlan, PurchaserPlanAssn, ReceivedDocument, Report, ReportAnomalyEventStore,
ResourceAbsence, ResourcePreference, ReturnOrder, ReturnOrderLineItem,
ServiceAppointment, ServiceResource, ServiceResourceSkill, ServiceTerritory,
ServiceTerritoryMember, ServiceTerritoryWorkType, SessionHijackingEventStore, Shift,
Shipment, ShipmentItem, Site, SkillRequirement, SocialPost, Solution, Task,
ThreatDetectionFeedback, Topic, User, Visit, VisitedParty, Visitor, VoiceCall, VolunteerProject,
WorkBadgeDefinition, WorkOrder, WorkOrderLineItem, WorkType, WorkTypeGroup,
WorkTypeGroupMember

```
ShareType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Required. The permission granted to the user of the shared file in a library. This is determined
by the permission the user already has in the library. This field is available in API version 25.0
and later.

```
  V
```

Viewer permission. The user can explicitly view but not edit the shared file.

```
  C
```

Collaborator permission. The user can explicitly view and edit the shared file. You can
retrieve the ShareType for ContentDocumentLink, but you can't create a
ContentDocumentLink with a `ShareType` of `C` from an Apex trigger.

```
  I
```

Inferred permission. The user’s permission is determined by the related record. For shares
with a library, this is defined by the permissions the user has in that library.


Standard Objects ContentDocumentLink

**Field** **Details**

Inferred permission on shares with libraries and file owners is available in API versions
21.0 and later. Inferred permission on shares with standard objects is available in API
versions 36.0 and later. Inferred permission can’t be used on shares with the Organization
object.

```
Visibility

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies whether this file is available to all users, internal users, or shared users. This field is
available in API version 26.0 and later.

Valid values are:

**•** `AllUsers` —The file is available to all users who have permission to see the file.

**•** `InternalUsers` —The file is available only to internal users who have permission
to see the file.

**•** `SharedUsers` —The file is available to all users who can see the feed to which the
file is posted. SharedUsers is used only for files shared with users, and is available only
when an org has private org-wide sharing on by default. The `SharedUsers` value is
available in API version 32.0 and later.

Note the following exceptions for `Visibility` .

**•** `AllUsers` & `InternalUsers` values apply to files posted on standard and custom
object records, but not to users, groups, or content libraries.

**•** For posts to a record feed, `Visibility` is set to `InternalUsers` for all internal
users by default.

**•** External users can set `Visibility` only to `AllUsers` .

**•** On user and group posts, only internal users can set `Visibility` to
`InternalUsers` .

**•** For posts to a user feed, if the organization-wide default for user sharing is set to private,
`Visibility` is set to `SharedUsers` .

**•** Only internal users can update Visibility.

**•** Visibility can be updated on links to files posted on standard and custom object records,
but not to users, groups, or content libraries.

**•** Visibility is updatable in API version 43.0 and later.

The visibility setting on ContentDocumentLink determines a file’s visibility on a record post.
When a file has multiple references posted in a feed, the file’s visibility is determined by the most
visible setting.


Standard Objects ContentDocumentLink

Usage

Use this object to query the locations where a file is shared or query which files are linked to a particular location. For example, the
following query returns a particular document shared with a Chatter group:

```
   SELECT ContentDocument.title FROM ContentDocumentLink WHERE ContentDocumentId =

   '069D00000000so2' AND LinkedEntityId = '0D5000000089123'

```

**•** You can't run a query without filters against ContentDocumentLink.

**•** You can't filter on ContentDocument fields if you're filtering by `ContentDocumentId` . You can only filter on ContentDocument
fields if you're filtering by `LinkedEntityId` .

**•** You can't filter on the related object fields. For example, you can't filter on the properties of the account to which a file is linked. You
can filter on the properties of the file, such as the title field.

A SOQL query must filter on one of `Id`, `ContentDocumentId`, or `LinkedEntityId` .

The ContentDocumentLink object supports triggers before and after these operations: insert, update, delete. A ContentDocumentLink
trigger executes whenever there is an addition or deletion of the ContentDocumentLink. When a file is deleted, a ContentDocument
delete trigger executes, but the cascaded ContentDocumentLink delete does not trigger ContentDocumentLink triggers.

Example: This trigger for the ContentDocumentLink object prevents public XLSX files from being shared.

```
      trigger NoShareXLSX on ContentDocumentLink (after insert) {

        for (ContentDocumentLink cdl : trigger.new) {

           if (!CDLHelper.isSharingAllowed(cdl)) {

             cdl.addError('Sorry, you cannot share this file.');

           }

        }

      }

```

The trigger calls this helper class.

```
      public class CDLHelper {

        /**

         * Gets FileExtension of the inserted content.

         */

        public static String getFileExtension(ContentDocumentLink cdl) {

           String fileExtension;

           String docId = cdl.ContentDocumentId;

          FileExtension = [select FileExtension from ContentVersion where ContentDocumentId

      = :docId].get(0).FileExtension;

           return FileExtension;

        }

        /**

         * Checks the file's PublishStatus and FileExtension to decide whether user can

      share the file with others.

         * PublishStatus 'P' means the document is in a public library.

         */

        public static boolean isSharingAllowed(ContentDocumentLink cdl) {

           String docId = cdl.ContentDocumentId;

          ContentVersion version = [select PublishStatus,FileExtension from ContentVersion

      where ContentDocumentId = :docId].get(0);

           if (version.PublishStatus.equals('P') && (version.FileExtension != null &&

      version.FileExtension.equals('xlsx'))) {

```


### Standard Objects ContentDocumentListViewMapping

```
             return false;

           }

           return true;

        }

        /**

         * Gets the parent account name if the file is linked to an account.

         */

        public static String getAccountName(ContentDocumentLink cdl) {

           String name;

           String id = cdl.LinkedEntityId;

           if (id.substring(0,3) == '001') {

             name = [select Name from Account where Id = :id].get(0).Name;

           }

           return name;

        }

      }

```

Important: Apex has a per organization limit of 10 concurrent requests that last longer than 5 seconds. A trigger that uploads
files, like bulk `ContentVersion` creation, can easily hit the SOQL queries limit.

Associated Objects

This object has the following associated objects. Unless noted, associated objects are available in the same API version as this object.

**ContentDocumentLinkChangeEvent on page 68 (API version 55.0)**
Change events are available for the object.

SEE ALSO:

### ContentDocument ContentDocumentListViewMapping

Represents an association between a ListView and a Quip ContentDocument. Applies to Quip file types only. Maintains the mapping
between a list view and Quip document when the list view is exported to a newly created Quip document. This object is available in API
version 44.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To use this object, the Files Connect and Quip permissions must be enabled in the org.

To insert and update this object through the API, the QuipMassAction gater permission must also be enabled.


Standard Objects ContentDocumentListViewMapping

Fields

**Field** **Details**

```
ContentDocumentId

LastReferencedDate

LastViewedDate

ListViewId

Name

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the document.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this document.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the list view associated with the document.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the document.

ContentDocumentListViewMapping is used primarily by the Quip list view integration feature. Only Quip file types (Quip sheets and
docs) are supported. The ContentDocumentId field must point to a Quip file.


### Standard Objects ContentDocumentSubscription ContentDocumentSubscription

Represents a subscription for a user following or commenting on a file in a library. This object is available in API version 42.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Only users with Modify All Data permission have access to this object.

Fields

**Field** **Details**

```
ContentDocumentId

IsCommentSub

IsDocumentSub

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the file.

This is a relationship field.

**Relationship Name**
### ContentDocument

**Relationship Type**
Lookup

**Refers To**
### ContentDocument

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether the user made comments on the file.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether the user follows the file.


### Standard Objects ContentDocLinkEventLog

**Field** **Details**

```
UserId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user following or commenting on the file.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

### ContentDocLinkEventLog

Content Document Link events contain sharing information for content documents. This object is available in API version 65.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
DocumentIdentifier

RequestIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the document that’s being shared.

**Type**
string


Standard Objects ContentDocLinkEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same REQUEST_ID.

```
SharedWithObjectIdentifier

SharingOperation

SharingPermission

Timestamp

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Who the document was shared with.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of sharing operation on the document.

**Possible Values**

**•** `INSERT`

**•** `UPDATE`

**•** `DELETE`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
What permissions the document was shared with.

**Possible Values**

**•** `V` : Viewer

**•** `C` : Collaborator

**•** `I` : Inferred—that is, the sharing permissions were inferred from a relationship between
the viewer and document. For example, a document’s owner has a sharing permission
to the document itself. Or, a document can be a part of a content collection, and the
viewer has sharing permissions to the collection rather than explicit permissions to the
document directly.

**Type**
dateTime


### Standard Objects ContentFolder

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

```
UserIdentifier

### ContentFolder

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.

For example: `00530000009M943`

Represents a folder in a content library for adding files. This object is available in API version 34.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

**•** Salesforce CRM Content or Chatter must be enabled to access ContentFolder.

**•** All users with a content feature license can modify folders in their personal library.

**•** To modify a folder, the user must be a member of the library and have permission to modify folders.

Fields

**Field Name** **Details**

```
Name

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the folder.


### Standard Objects ContentFolderItem

**Field Name** **Details**

```
ParentContentFolderId

```

Associated Objects

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the ParentFolder.

This is a relationship field.

**Relationship Name**
ParentContentFolder

**Relationship Type**
Lookup

**Refers To**
### ContentFolder

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ContentFolderChangeEvent (API version 62.0)**
Change events are available for the object.

### ContentFolderItem

Represents a file (ContentDocument) or folder (ContentFolder) that resides in a ContentFolder in a ContentWorkspace. This object is
available in API version 35.0 and later.

Supported Calls

`describeSObjects()`, `describeLayout()`, `query()`, `retrieve()`

Special Access Rules

Fields

**Field Name** **Details**

```
ContentSize

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ContentFolderItem

**Field Name** **Details**

**Description**

The size of the file or folder in bytes, when the size is smaller than 2 GB.

In API version 66.0 and later, we recommend that you use the
`ContentSizeLong` field even for files smaller than 2 GB.

```
ContentSizeLong

FileExtension

FileType

IsFolder

ParentContentFolderId

```

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**

The size of the file or folder in bytes up to 10 GB.

This field is available in API version 66.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Specifies the file extension if the ContentFolderItem is a file.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

Specifies the type of file if the ContentFolderItem is a file.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates that the ContentFolderItem is a folder, and not a file.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects ContentFolderLink

**Field Name** **Details**

**Description**

The ID of the ContentFolder that the ContentFolderItem resides in.

This is a relationship field.

**Relationship Name**
ParentContentFolder

**Relationship Type**
Lookup

**Refers To**
### ContentFolder

```
Title

### ContentFolderLink

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**

The name of the file or folder.

Defines the association between a library and its root folder. This object is available in API version 34.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

**•** Salesforce CRM Content must be enabled to access ContentFolderLink.

### • ContentFolderLink is read-only in the context of a library.

Fields

**Field Name** **Details**

```
ContentFolderId

```

**Type**
reference

**Properties**
Filter, Group, Sort


### Standard Objects ContentFolderMember

**Field Name** **Details**

**Description**
ID of the folder.

This is a relationship field.

**Relationship Name**
### ContentFolder

**Relationship Type**
Lookup

**Refers To**
### ContentFolder

```
EnableFolderStatus

ParentEntityId

### ContentFolderMember

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the status of enabling folders for the library. Valid values are:

### • C — Completed folder enablement

**•** `S`  - Started folder enablement

**•** `F`  - Failed folder enablement

This field is available in API version 39.0 and later.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Name of the entity the folder hierarchy is linked to.

Defines the association between a file and a folder. This object is available in API version 34.0 and later.

Supported Calls

`describeSObjects()`, `delete()`, `query()`, `retrieve()`, `update()`

Special Access Rules

**•** Salesforce CRM Content or Chatter must be enabled to access ContentFolderMember.

**•** All users with a content feature license can modify folders in their personal library.


### Standard Objects ContentHubItem

**•** To modify ContentFolderMember, the user must be a member of the library and have permission to modify folders.

Fields

**Field Name** **Details**

```
ChildRecordId

ParentContentFolderId

### ContentHubItem

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the file.

This is a relationship field.

**Relationship Name**
ChildRecord

**Relationship Type**
Lookup

**Refers To**
ContentDocument

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
ID of the folder the file is in.

This is a relationship field.

**Relationship Name**
ParentContentFolder

**Relationship Type**
Lookup

**Refers To**
ContentFolder

Represents a file or folder in a Files Connect external data source, such as Microsoft SharePoint or OneDrive for Business. This object is
available in API version 33.0 and later.

Special Access Rules

Chatter and Files Connect must be enabled for the organization.


Standard Objects ContentHubItem

Supported Calls

`describeSObjects()`, `query()`, `search()`

Fields

**Field Name** **Details**

```
ContentHubRepositoryId

ContentItemSize

ContentModifiedDate

ContentSize

Description

```

**Type**
reference

**Properties**
Filter, Group, Nillable

**Description**
The ID for the related external data source described by the ContentHubRepository
object.

**Type**
long

**Properties**
Group, Nillable

**Description**
The size of the file or folder. Available in API version 65.0 and later.

**Type**
dateTime

**Properties**
Nillable

**Description**
Date the file or folder content last changed.

**Type**
int

**Properties**
Group, Nillable

**Description**
The size of the file or folder that's less than 2 GB.

**Type**
string

**Properties**
Filter, Group, Nillable

**Description**
Explanation of item in external data source.


Standard Objects ContentHubItem

**Field Name** **Details**

```
ExternalContentUrl

ExternalDocumentUrl

ExternalId

FileExtension

FileType

IsFolder

```

**Type**
url

**Properties**
Group, Nillable

**Description**
The URL of the document content in the external data source.

**Type**
url

**Properties**
Group, Nillable

**Description**
The URL of the detail page in the external data source.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID for the file or folder in the external data source.

**Type**
string

**Properties**
Group, Nillable

**Description**
File format extension, such as .doc or .pdf

**Type**
string

**Properties**
Group, Nillable

**Description**
Complete file type, such as “Microsoft Word Document.”

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether item is a folder or file.


Standard Objects ContentHubItem

**Field Name** **Details**

```
MimeType

Name

Owner

ParentId

Title

```

**Type**
string

**Properties**
Filter, Group, Nillable

**Description**
MIME type of the content.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Name of the file or folder in the external data source.

**Type**
string

**Properties**
Filter, Group, Nillable

**Description**
Username of the content owner in the external data source.

**Type**
string

**Properties**
Filter, Group, Nillable

**Description**
The ID of the parent folder for the record.

This field isn’t returned in queries or searches of the ContentHubItem object. It
supports only WHERE clauses, such as the following:

```
  WHERE ContentHubRepositoryId = <ID of external

  source> and ParentId = <ID of parent folder or
```

`record>` .

Or specify `WHERE ParentId = <name of root folder>` to return
the children of the root folder.

Tip: The ParentId field supports both Salesforce IDs (in the format
“0CHxxx”) and external IDs.

**Type**
string

**Properties**
Group, Nillable


Standard Objects ContentHubItem

**Field Name** **Details**

**Description**
The title that appears in the content, which often differs from the `Name` of the
containing file or folder.

```
UpdatedBy

```

Usage

**Type**
string

**Properties**
Group, Nillable

**Description**
Username for the person who last updated the file.

The following SOQL query examples show how to retrieve files and folders from a Files Connect external data source. These examples
use placeholders for ID values for the repository ID and folder IDs. Before running these queries, replace the placeholders with valid ID
values for your external data source and folders.

Important: You must filter queries and searches on ContentHubItem with the `ContentHubRepositoryId` field; for
example, `SELECT Id FROM ContentHubItem WHERE ContentHubRepositoryId = <ID of external`
`data source>` .

**Example 1:** Get the ID and name of the root folder in an external file source.

```
SELECT Id, Name

FROM ContentHubItem

WHERE ContentHubRepositoryId = ' <repository ID> ' AND ParentId = NULL

```

**Example 2:** List all folders and files under the specified root folder.

```
SELECT Id, Name

FROM ContentHubItem

WHERE ContentHubRepositoryId = ' <repository ID> ' AND ParentId = ' <root folder ID> '

```

**Example 3:** List all external file data sources by querying ContentHubRepository.

```
SELECT DeveloperName

FROM ContentHubRepository

```

**Example 4:** List all files and folders in a given folder and external file source.

```
SELECT Id, Name

FROM ContentHubItem

WHERE ContentHubRepositoryId = ' <repository ID> ' AND ParentId = ' <parent folder ID> '

```

**Example 5:** To return only folders in the result set, add `IsFolder = true` in the `WHERE` clause to a query that returns files and
folders. For example, the following query lists all folders under the root folder.

```
SELECT Id, Name

FROM ContentHubItem

```


### Standard Objects ContentHubRepository

```
   WHERE ContentHubRepositoryId = ' <repository ID> ' AND ParentId = ' <root folder ID> '

       AND IsFolder = true

```

**Example 6:** Retrieve a link that is used to open the specified document in an external source.

```
   SELECT ExternalDocumentUrl

   FROM ContentHubItem

   WHERE ContentHubRepositoryId = ' <repository ID> ' AND Id = ' <document ID> '

```

**SOSL Example:** Retrieve the ID and name of all documents that contain the search string. The result set is limited to the first 10 documents.

```
   FIND {<search string>}

   RETURNING ContentHubItem(Id, Name

                  WHERE ContentHubRepositoryId = ' <repository ID> ')

   LIMIT 10

### ContentHubRepository

```

Represents a Files Connect external data source such as Microsoft SharePoint or OneDrive for Business. This object is available in API
version 33.0 and later.

Special Access Rules

Chatter and Files Connect must be enabled for the organization.

Supported Calls

`describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`

Fields

**Field Name** **Details**

```
DeveloperName

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name of the record in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. This field is automatically generated but you can supply
your own value if you create the record using the API.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is specified,
performance may slow while Salesforce generates one for each record.


### Standard Objects ContentNote

**Field Name** **Details**

```
MasterLabel

Type

### ContentNote

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Master label for the external data source. This display value is the internal label
and does not get translated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The data source type. Possible values are:

**•** `contenthubGoogleDrive`

**•** `contenthubOffice365`

**•** `contenthubOneDrive`

**•** `contenthubSharepoint`

**•** `contenthubBox`

**•** `contenthubQuip`

Represents a note created with the enhanced note-taking tool, released in Winter ’16. This object is available in API version 32.0 and
later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `search()`, `update()`

Special Access Rules

**•** Notes must be enabled.

Fields

**Field** **Details**

### `Content`

**Type**
base64


Standard Objects ContentNote

**Field** **Details**

**Properties**
Create, Nillable, Update

**Description**
The content or body of the note, which can include properly formatted HTML or plain text.
When a document is uploaded or downloaded via the API, it must be base64 encoded (for
upload) or decoded (for download). Any special characters within plain text in the `Content`
field must be escaped. You can escape special characters by calling
`content.escapeHtml4()` . If the input contains unsafe HTML characters or new lines,
we automatically strip them out before saving the content.

```
ContentModifiedDate

ContentSize

ContentSizeLong

FileExtension

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the document was modified. ContentModifiedDate updates when, for example,
the document is renamed or a new document version is uploaded.

This field is available in API version 48.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The size of the note in bytes for notes smaller than 2 GB. In API version 66.0 and later, use
the `ContentSizeLong` field.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**

The size of the note in bytes, up to 10 GB.

This field is available in API version 66.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
File extension of the note.


Standard Objects ContentNote

**Field** **Details**

```
FileType

IsReadOnly

LastViewedDate

LatestContentId

LatestPublishedVersionId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Type of file for the note. All notes have a file type of `SNOTE` .

**Type**
boolean

**Properties**
Defaulted on create, Group, Sort

**Description**
Indicates whether the note is read only.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the note was last viewed. This field is available in API version 35.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Lookup to the note's ContentBody. This field is available in API version 52.0 and later.

This is a relationship field.

**Relationship Name**
LatestContent

**Relationship Type**
Lookup

**Refers To**
ContentBody

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the ContentVersion for the latest published version of the note.


Standard Objects ContentNote

**Field** **Details**

```
OwnerId

SharingPrivacy

TextPreview

Title

```

Usage

**Type**
reference

**Properties**
Create (for users assigned the Set Audit Fields Upon Creation permission), Defaulted on
create, Filter, Group, Sort, Update (for users assigned the Set Audit Fields Upon Creation
permission)

**Description**
ID of the owner of the note.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Controls sharing privacy for a file. Only Salesforce admins and file owners with Collaborator
access to the file can modify this field. Default is `Visible to Anyone With Record`
`Access` . When set to `Private on Records`, the file is private on records but can
be shared selectively with others.

This field is available in API versions 41.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A preview of the note’s content. This field is available in API version 35.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Namefield, Sort, Update

**Description**
Title of the note.

**•** Use ContentNote to create, query, retrieve, search, edit, and update notes.

**•** ContentNote is built on ContentVersion, and so it has many of the same usages.

**•** Not all fields can be set for notes. Only the `Content` and `Title` fields can be updated.


### Standard Objects ContentNotification

**•** The maximum file size that you can upload via the SOAP API is 50 MB. When a document is uploaded or downloaded via the API,
it’s converted to base64. This conversion increases the document size by approximately 37%. Account for the base64 conversion
increase so that the file you plan to upload is less than 50 MB after conversion.

**•** You can convert old Note records to Lightning Experience, so users can view and edit notes from the Notes & Attachments related
list in Lightning Experience. Users can edit their converted notes, which are accessible from the Notes related list and Notes tab.
Copy old Note records to newly created ContentNote records. Users assigned the Set Audit Fields Upon Creation permission can set
the owner, created date, and last modified date on ContentNote records.

**•** SOQL and SOSL queries on the ContentNote return only the most recent version of the note.

**•** To relate a note to a record, use `ContentDocumentLink` . Review the `LinkedEntityID` field in `ContentDocumentLink`
for a list of objects that notes can relate to.

For example, the following Apex code creates a note and escapes any special characters so they’re converted to their HTML equivalents.

Note: Apex code doesn’t need to be encoded to base64 before it’s uploaded and downloaded.

```
   ContentNote cn = new ContentNote();

   cn.Title = 'test1';

   String body = 'Hello World. Before insert/update, escape special characters such as ", ',

    &, and other standard escape characters.';

   cn.Content = Blob.valueOf(body.escapeHTML4());

   insert(cn);

```

In this example, the following code creates a note using text that is already formatted as HTML, so it doesn’t need to be escaped.

```
   ContentNote cn = new ContentNote();

   cn.Title = 'test2';

   String body = '<b>Hello World. Because this text is already formatted as HTML, it does not

    need to be escaped.

   Special characters such as &quot;, etc. must already use their HTML equivalents.</b>';

   cn.Content = body;

   insert(cn);

### ContentNotification

```

Represents a notification for a file. This object is available in API version 42.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Only users with Modify All Data permission have access to this object.


Standard Objects ContentNotification

Fields

**Field** **Details**

```
EntityIdentifierId

EntityType

Nature

Subject

Text

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the object with the notification.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Type of object with the notification. One of the following.

**•** `ContentDocument`

**•** `ContentTagName`

**•** `ContentVersion`

**•** `ContentWorkspace`

**•** `ContentWorkspacePermission`

**•** `User`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Type of notification.

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
Subject of the notification.

**Type**
textarea

**Properties**
Filter, Nillable, Sort


### Standard Objects ContentTagSubscription

**Field** **Details**

**Description**
Text of the notification.

```
UsersId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who received the notification.

This is a relationship field.

**Relationship Name**
Users

**Relationship Type**
Lookup

**Refers To**
User

### ContentTagSubscription

Represents a subscription for a user following a tag on a file. This object is available in API version 42.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Only users with Modify All Data permission have access to this object.

Fields

**Field** **Details**

```
UserId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the user following the tag on the file.

This is a relationship field.


### Standard Objects ContentTaxonomy

**Field** **Details**

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

### ContentTaxonomy

Represents a content taxonomy, which is used to classify and organize Salesforce CMS content. To create a hierarchy of terms in a content
taxonomy, use this object in addition to the ContentTaxonomyTerm, ContentTaxonomyRelatedTerm, and
### ContentTaxonomyTermRelatedTerm objects. This object is available in API version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

To view this object, users need the permission View Content Taxonomy enabled. To edit this object, users need View Content Taxonomy
and Manage Content Taxonomy enabled.

Fields

**Field** **Details**

```
Description

Language

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the content taxonomy. This description appears in the API and in the Content
Taxonomy tab in the Digital Experiences App. The maximum length is 255 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The combined language and locale ISO code.


### Standard Objects ContentTaxonomyRelatedTerm

**Field** **Details**

```
Name

```

SEE ALSO:

### ContentTaxonomyRelatedTerm

ContentTaxonomyTerm

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the content taxonomy.

ContentTaxonomyTermRelatedTerm

ContentTaxonomyTermRelationshipType

### ContentTaxonomyRelatedTerm

Represents the relationship between a term and the content taxonomy to which the term belongs. This object is available in API version
63.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `undelete()`

Special Access Rules

To view this object, users need the permission View Content Taxonomy enabled. To edit this object, users need View Content Taxonomy
and Manage Content Taxonomy enabled.

Fields

**Field** **Details**

```
ContentTaxonomyId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the content taxonomy to which the term belongs.

This field is a relationship field.

**Relationship Name**
### ContentTaxonomy


### Standard Objects ContentTaxonomyTerm

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
ContentTaxonomy object

### `ContentTaxonomyTermId`

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the term that belongs to the content taxonomy.

This field is a relationship field.

**Relationship Name**
### ContentTaxonomyTerm

**Relationship Type**
Lookup

**Refers To**
### ContentTaxonomyTerm object

To include a term in a taxonomy, you must use this object in addition to the ContentTaxonomyTerm and ContentTaxonomy objects.

SEE ALSO:

### ContentTaxonomy ContentTaxonomyTerm ContentTaxonomyTerm

Represents a term in a content taxonomy. Terms describe what content is or how it's used, and they’re organized in parent-child
relationships in the taxonomy hierarchy. This object is available in API version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

To view this object, users need the permission View Content Taxonomy enabled. To edit this object, users need View Content Taxonomy
and Manage Content Taxonomy enabled.


Standard Objects ContentTaxonomyTerm

Fields

**Field** **Details**

```
Description

DeveloperName

ExternalId

Name

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the content taxonomy term. This description appears in the API and in the
Content Taxonomy tab in the Digital Experiences App. The maximum length is 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The unique name of the content taxonomy term in the API. This field is unique within your
organization. The name:

**•** must be 80 characters or fewer

**•** must begin with a letter

**•** can contain only underscores and alphanumeric characters

**•** can't include spaces

**•** can't end with an underscore

**•** can't contain 2 consecutive underscores

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The external ID of the content taxonomy term.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the content taxonomy term. The name must be between 2 and 255 characters
long.


### Standard Objects ContentTaxonomyTermRelatedTerm

Usage

To include a term in a taxonomy, you must also use the objects ContentTaxonomyRelatedTerm and ContentTaxonomy. If you create
only a ContentTaxonomyTerm, then the term isn’t considered part of the taxonomy, and isn't visible. To relate this term to another term
in your taxonomy, use the object ContentTaxonomyTermRelatedTerm.

SEE ALSO:

### ContentTaxonomy

ContentTaxonomyRelatedTerm

### ContentTaxonomyTermRelatedTerm ContentTaxonomyTermRelatedTerm

Represents the relationship between two terms in a content taxonomy. This object is available in API version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,

```
   undelete()

```

Special Access Rules

To view this object, users need the permission View Content Taxonomy enabled. To edit this object, users need View Content Taxonomy
and Manage Content Taxonomy enabled.

Fields

**Field** **Details**

```
ContentTaxonomyId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the content taxonomy to which the term belongs.

This field is a relationship field.

**Relationship Name**
### ContentTaxonomy

**Relationship Type**
Lookup

**Refers To**
ContentTaxonomy object


Standard Objects ContentTaxonomyTermRelatedTerm

**Field** **Details**

```
ContentTaxonomyTermId

ContentTaxonomyTrmRelaTypeId

RelatedContentTaxonomyTermId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the primary term that has a relationship with another term.

This field is a relationship field.

**Relationship Name**
ContentTaxonomyTerm

**Relationship Type**
Lookup

**Refers To**
ContentTaxonomyTerm object

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the type of relationship between the two taxonomy terms.

This field is a relationship field.

**Relationship Name**
ContentTaxonomyTrmRelaType

**Relationship Type**
Lookup

**Refers To**
ContentTaxonomyTermRelationshipType object

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the term that is related to the primary term.

This field is a relationship field.

**Relationship Name**
RelatedContentTaxonomyTerm

**Relationship Type**
Lookup


### Standard Objects ContentTaxonomyTermRelationshipType

**Field** **Details**

**Refers To**
ContentTaxonomyTerm object

Usage

To relate a term to another term in a content taxonomy, use this object in addition to the ContentTaxonomyTerm object. This object
can’t be updated. You can only create and delete it.

SEE ALSO:

### ContentTaxonomyTerm ContentTaxonomyTermRelationshipType

Represents the type of relationship between two terms in a content taxonomy. This object is available in API version 63.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

To view this object, users need the permission View Content Taxonomy enabled.

Fields

**Field** **Details**

```
ContentTaxonomyTrmRelaCatg

Description

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Category of the relationship type.

Possible values are:

**•** `HasBroader`

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects ContentTransferEventLog

**Field** **Details**

**Description**
Description of the relationship type.

```
Name

```

Usage

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Name of the relationship type.

ContentTaxonomyRelationshipType can’t be created, updated, or deleted. In API version 63.0, the default category for the relationship
type is HasBroader.

### ContentTransferEventLog ContentTransferEventLog stores information about content transfer events, such as downloads, uploads, and previews. This information

includes events performed on files and attachments to records. This object is available in API version 62.0 and later.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
DocumentIdentifier

FilePreviewType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the document that’s being shared.

**Type**
string


Standard Objects ContentTransferEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The content type of the file preview.

```
FileSize

FileType

OperationType

RequestIdentifier

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The size of rendition being added (bytes).

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The content type of the file version.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The operation that’s being performed.

**Possible Values**

**•** `meta_deploy`

**•** `meta_list`

**•** `meta_retrieve`

**•** `meta_synchronous_create`

**•** `meta_synchronous_read`

**•** `meta_synchronous_upsert`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same `REQUEST_ID` .


### Standard Objects ContentUserSubscription

**Field** **Details**

For example: `3nWgxWbDKWWDIk0FKfF5DV` .

```
Timestamp

UserIdentifier

VersionIdentifier

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT.

For example: `20130715233322.670` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 18-character ID of the user who’s using Salesforce services through the UI or the API.

For example: `00530000009M943YAS`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the content version.

### ContentUserSubscription

Represents a subscription for a user following another user. This object is available in API version 42.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Only users with Modify All Data permission have access to this object.


### Standard Objects ContentVersion

Fields

**Field** **Details**

```
SubscribedToUserId

SubscriberUserId

### ContentVersion

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who is followed by another user.

This is a relationship field.

**Relationship Name**
SubscribedToUser

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who follows another user.

This is a relationship field.

**Relationship Name**
SubscriberUser

**Relationship Type**
Lookup

**Refers To**
User

Represents a specific version of a document in Salesforce CRM content or Salesforce Files. This object is available in versions 17.0 and
later for Salesforce CRM content documents. This object is available in versions 20.0 and later for Salesforce Files.

The maximum number of versions that can be published in a 24-hour period is 200,000.

Note: Depending on how files are shared, queries on ContentDocument and ContentVersion without specifying an ID don’t
return all files a user has access to. For example, if a user only has access to a file because they have access to a record that the file
is shared with, the file won't be returned in a query such as "SELECT Id FROM ContentDocument."


Standard Objects ContentVersion

Supported Calls

`create()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `search()`, `update()`, `upsert()`

Special Access Rules

**•** All users with a content feature license can create versions in their personal library. Customer and Partner Portal users must also
supply the `NetworkId` of the Experience Cloud site in the request.

**•** By default, users (including users with the “View All Data” permission) can only query files they have access to, including:

**–** Salesforce Files in their personal library and in libraries they're a member of, regardless of library permissions (API version 17.0
and later).

**–** Salesforce Files they own, shared directly with them, posted on their profile, or posted on groups they can see (API version 21.0
and later).

Enable the Query All Files permission to let your View All Data users bypass the restrictions on querying files.

**–** Query All Files returns all files, including files in non-member libraries and files in unlisted groups.

**–** Users can’t edit, upload new versions, or delete files they don’t have access to.

**–** View All Data permission is required to enable Query All Files.

**•** All users can update versions in their personal library.

**•** The owner of a version or document can update the document if they’re a member of the library, regardless of library permissions.

**•** To update a Salesforce CRM Content document, the user must be a member of the library with one of these library privileges enabled:

**–** Add Content

**–** Add Content On Behalf of Others

**–** Manage Library

**•** Customer and Partner Portal users must have the View Content in Portal permission to query content in libraries where they have
access.

**•** Customer and Partner Portal users can only publish, version, or edit documents if they have a Salesforce CRM Content feature license.

**•** `FileType` is defined by either `ContentUrl` for links or `PathOnClient` for documents, but not both.

**•** In API version 34.0 and later, any file can be shared with libraries, whether the file originated in Chatter or in Salesforce CRM Content.

**•** [In API version 39.0 and later, custom Apex download handlers can be created that can control access to documents. See the Apex](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dev_guide.htm)
[Developer Guide for more information.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dev_guide.htm)

Fields

**Field** **Details**

```
Checksum

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
MD5 checksum for the file.


Standard Objects ContentVersion

**Field** **Details**

```
ContentBodyId

ContentDocumentId

ContentLocation

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Allows inserting a file version independently of the file blob being uploaded. This field is
available for query and insert only. It can only point to a ContentBody record. This field is
available in API version 40.0 and later.

This is a relationship field.

**Relationship Name**
ContentBody

**Relationship Type**
Lookup

**Refers To**
ContentBody

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the document.

This is a relationship field.

**Relationship Name**
ContentDocument

**Relationship Type**
Lookup

**Refers To**
ContentDocument

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Origin of the document. Valid values are:

**•** **S** —Document is located within Salesforce. Label is **Salesforce** .

**•** **E** —Document is located outside of Salesforce. Label is **External** .

**•** **L** —Document is located on a social network and accessed via Social Customer Service.
Label is **Social Customer Service** .

**•** **SfDrive** —For internal use only.


Standard Objects ContentVersion

**Field** **Details**

**•** **SCS** —For internal use only.

```
ContentModifiedById

ContentModifiedDate

ContentSize

ContentSizeLong

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the user who modified the document.

This is a relationship field.

**Relationship Name**
ContentModifiedBy

**Relationship Type**
Lookup

**Refers To**
User

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**

Date the document was modified.

`ContentModifiedDate` updates when, for example, the document is renamed or a
new document version is uploaded. When uploading the first version of a document,
`ContentModifiedDate` can be set to the current time or any time in the past.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The size of the document in bytes for documents smaller than 2 GB. The value is zero for links.

In API version 66.0 and later, we recommend that you use the `ContentSizeLong` field
even for documents smaller than 2 GB.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**

The size of the document in bytes up to 10 GB. The value is zero for links.


Standard Objects ContentVersion

**Field** **Details**

This field is available in API version 66.0 and later.

```
ContentUrl

Description

Division

ExternalDataSourceId

```

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
URL for links. This is only set for links. One of the fields that determines the `FileType` . The
character limit in API versions 33.0 and later is 1,300. The character limit in API versions 32.0
and earlier was 255.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the content version.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A logical segment of your organization's data. For example, if your company is organized
into different business units, you could create a division for each business unit, such as “North
America,” “Healthcare,” or “Consulting.” Available only if the org has the Division permission
enabled.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the external document referenced in the `ExternalDataSource` object.

This is a relationship field.

**Relationship Name**
ExternalDataSource

**Relationship Type**
Lookup

**Refers To**
ExternalDataSource


Standard Objects ContentVersion

**Field** **Details**

```
ExternalDocumentInfo1

ExternalDocumentInfo2

FeaturedContentBoost

FeaturedContentDate

FileExtension

```

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Stores the URL of the file in the external content repository. The integration from the external
source determines the content for this string. After the reference or copy is created, the URL
of the external file is updated when you:

**•** Republish a file reference in Lightning Experience

**•** Open the document

**•** Create a file reference in the Connect REST API with `reuseReference` set to true.

When the file is updated, the shared link is updated to the most current version.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Contains the external file ID. Salesforce determines the content for this string, which is private.
The content can change without notice, depending on the external system. After the file
reference is created, this field isn’t updated, even if the file path changes.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Read only. Designates a document as featured.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Date the document was featured.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ContentVersion

**Field** **Details**

**Description**

File extension of the document.

This field is available in API version 31.0 and later.

```
FileType

FirstPublishLocationId

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Type of content determined by `ContentUrl` for links or `PathOnClient` for documents.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

ID of the location where the version was first published. If the version is first published into
a user's personal library or My Files, the field will contain the ID of the user who owns the
personal library or My Files. In Lightning Experience, if the first version is published into a
public library, the field will contain the ID of that library.

Accepts all record IDs supported by ContentDocumentLink (anything a file can be attached
to, like records and groups).

Setting `FirstPublishLocationId` allows you to create a file and share it with an
initial record/group in a single transaction, and have the option to create more links to share
the file with other records or groups later. When a file is created, it’s automatically linked to
the record, and PublishStatus will change to Public from Pending/Personal.

This field is only set the first time a version is published via the API.
`FirstPublishLocationId` can’t be set to another ID when a new content version
is inserted.

Note: Salesforce updates the `FirstPublishLocationId` updates automatically
when a new `OwnerId` is added to the `ContentVersion` . For example, when
you publish a new version with a different `OwnerId` than the current `OwnerId`,
the `FirstPublishLocationId` of all previous versions updates to the previous
`OwnerId` . The new published version sets the `FirstPublishLocationId`
to the new `OwnerId` .

This is a polymorphic relationship field.

**Relationship Name**
FirstPublishLocation

**Relationship Type**
Lookup


Standard Objects ContentVersion

**Field** **Details**

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
ContactEncounter, ContactEncounterParticipant, ContentWorkspace, Contract,
ConversationEntry, CoverageBenefit, CoverageBenefitItem, CredentialStuffingEventStore,
CreditMemo, CreditMemoLine, Dashboard, DashboardComponent, DataStream,
DelegatedAccount, DocumentChecklistItem, EmailMessage, EmailTemplate,
EngagementChannelType, EnhancedLetterhead, EnrollmentEligibilityCriteria, Event,
HealthcareFacility, HealthcareFacilityNetwork, HealthcarePayerNetwork,
HealthcarePractitionerFacility, HealthcareProvider, HealthcareProviderNpi,
HealthcareProviderSpecialty, HealthcareProviderTaxonomy, Identifier, Image,
IndividualApplication, Invoice, InvoiceLine, Lead, ListEmail, Location, MarketSegment,
MarketSegmentActivation, MemberPlan, MessagingSession, MktCalculatedInsight,
OperatingHours, Opportunity, Order, OrderItem, Organization, OtherComponentTask,
OutgoingEmail, PartyConsent, PersonEducation, PersonLanguage, PersonLifeEvent,
PersonName, PlanBenefit, PlanBenefitItem, Product2, ProductFulfillmentLocation, ProductItem,
ProductItemTransaction, ProductRequest, ProductRequestLineItem, ProductRequired,
ProductTransfer, ProfileSkill, ProfileSkillEndorsement, ProfileSkillUser, ProviderSearchSyncLog,
PurchaserPlan, PurchaserPlanAssn, ReceivedDocument, Report, ReportAnomalyEventStore,
ResourceAbsence, ResourcePreference, ReturnOrder, ReturnOrderLineItem,
ServiceAppointment, ServiceResource, ServiceResourceSkill, ServiceTerritory,
ServiceTerritoryMember, ServiceTerritoryWorkType, SessionHijackingEventStore, Shift,
Shipment, ShipmentItem, Site, SkillRequirement, SocialPost, Solution, Task,
ThreatDetectionFeedback, Topic, User, Visit, VisitedParty, Visitor, VoiceCall, VolunteerProject,
WorkBadgeDefinition, WorkOrder, WorkOrderLineItem, WorkType, WorkTypeGroup,
WorkTypeGroupMember

```
IsAssetEnabled

```

**Type**
boolean

**Properties**
Create, Group, Defaulted on create


Standard Objects ContentVersion

**Field** **Details**

**Description**
Can be specified on insert of ContentVersion to automatically convert a ContentDocument
file into a ContentAsset. This field can be SOQL queried, but it can’t be edited. This field is
available in API version 38.0 and later.

```
IsLatest

IsMajorVersion

Language

```

`MalwareScanDate` (Beta)

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this is the latest version of the document ( `true` ) or not ( `false` ).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
`true` if the document is a major version; `false` if the document is a minor version. Major
versions can’t be replaced.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language for this document. This field defaults to the org’s default language unless the
multi language setting is enabled.

Specifies the language of the labels returned. The value must be a valid user locale (language
and country), such as `de_DE` or `en_GB` . For more information on locales, see the
`Language` field on the CategoryNodeLocalization object.

**Type**
dateTime

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date the document was scanned for malware. This field is available as a beta feature in
API version 66.0 and later.

Note: The `MalwareScanDate` field is a pilot or beta service that is subject to the
[Beta Services Terms at Agreements - Salesforce.com or a written Unified Pilot](https://www.salesforce.com/company/legal/agreements/)
[Agreement if executed by Customer, and applicable terms in the Product Terms](https://ptd.salesforce.com/)
[Directory. Use of this pilot or beta service is at the Customer's sole discretion.](https://ptd.salesforce.com/)


Standard Objects ContentVersion

**Field** **Details**

`MalwareScanStatus` (Beta)

```
NegativeRatingCount

NetworkId

```

**Type**
picklist

**Properties**
Filter, Group, Sort

**Description**
Indicates whether the document was scanned for malware and whether it’s safe or malicious.
This field is available in API version 66.0 and later.

Valid values are:

**•** `NotScanned` —The file hasn’t yet been scanned for malware. This is the default value.

**•** `Scheduled` —The file scan is in progress.

**•** `Clean` —The file was scanned and doesn’t contain malware.

**•** `Malicious` —The file was scanned and it contains malware.

**•** `Skipped` —The file can’t be scanned because it’s either larger than 100 MB or it’s a
Salesforce-generated file, such as a Content Note.

**•** `Failed` —The file wasn’t scanned because of an error.

Note: The `MalwareScanStatus` field is a pilot or beta service that is subject to
[the Beta Services Terms at Agreements - Salesforce.com or a written Unified Pilot](https://www.salesforce.com/company/legal/agreements/)
[Agreement if executed by Customer, and applicable terms in the Product Terms](https://ptd.salesforce.com/)
[Directory. Use of this pilot or beta service is at the Customer's sole discretion.](https://ptd.salesforce.com/)

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Read only. The number of times different users have given the document a thumbs down.

Rating counts for the latest version are not version-specific. If Version 1 receives 10
thumbs-down votes, and Version 2 receives 2 thumbs-down votes, the
`NegativeRatingCount` on Version 2 is 12. However, rating counts are not retroactive
for prior versions. The `NegativeRatingCount` on Version 1 is 10.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the Experience Cloud site that this file originated from. This field is available in API version
26.0 and later, if digital experiences is enabled for your org.

You can add a `NetworkId` only when creating a file. You can’t change or add a
`NetworkId` for an existing file.


Standard Objects ContentVersion

**Field** **Details**

```
Origin

OwnerId

PathOnClient

PositiveRatingCount

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The source of the content version. Valid values are:

**•** **C** —Content document from the user's personal library. Label is **Content** . The
`FirstPublishLocationId` must be the user's ID. If
`FirstPublishLocationId` is left blank, it defaults to the user's ID.

**•** **H** —Salesforce file from the user's My Files. Label is **Chatter** . The
`FirstPublishLocationId` must be the user's ID. If
`FirstPublishLocationId` is left blank, it defaults to the user's ID. Origin can
only be set to **H** if Chatter is enabled for your organization.

This field defaults to C. Label is **Content Origin** .

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of this document.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
string

**Properties**
Create, Filter, Nillable, Sort

**Description**
The complete path of the document. One of the fields that determines the `FileType` .

Note: Specify a complete path including the file extension in order for the document
to be visible in the Preview tab.

**Type**
int


Standard Objects ContentVersion

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
Read only. The number of times different users have given the document a thumbs up.

Rating counts for the latest version are not version-specific. If Version 1 receives 10 thumbs-up
votes, and Version 2 receives 2 thumbs-up votes, the `PositiveRatingCount` on Version
2 is 12. However, rating counts are not retroactive for prior versions. The
`PositiveRatingCount` on Version 1 is 10.

```
PublishStatus

RatingCount

ReasonForChange

RecordTypeId

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Indicates if and how the document is published. Valid values are:

**•** `P` —The document is published to a public library and is visible to other users. Label is
**Public** .

**•** `R` —The document is published to a personal library and is not visible to other users.
Label is **Personal Library** .

**•** `U` —The document is not published because publishing was interrupted. Label is **Upload**
**Interrupted** .

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Read only. Total number of positive and negative ratings.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The reason why the document was changed. This field can only be set when inserting a new
version (revising) a document.

**Type**
reference

**Properties**
Create, Filter, Nillable, Update


Standard Objects ContentVersion

**Field** **Details**

**Description**
ID of the record type of the version.

Custom fields are restricted in `RecordTypeId` . When an administrator creates a custom
field via the API it must be added to at least one page layout:

**•** If the custom field is added to the page layout associated with the General record type,
the `RecordTypeId` that corresponds to that record type does not have to be set on
the version record.

**•** If the custom field is added to the page layout associated with a custom record type, the
`RecordTypeId` that corresponds to that record type must be set on the version
record.

```
SharingOption

SharingPrivacy

TagCsv

TextPreview

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Controls whether sharing is frozen for a file. Only administrators and file owners with
Collaborator access to the file can modify this field. Default is `Allowed`, which means that
new shares are allowed. When set to `Restricted`, new shares are prevented without
affecting existing shares.

This field is available in API versions 35.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Controls sharing privacy for a file. Only administrators and file owners with Collaborator access
to the file can modify this field. Default is `Visible to Anyone With Record`
`Access` . When set to `Private on Records`, the file is private on records but can be
shared selectively with others.

This field is available in API versions 41.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Sort, Update

**Description**
Text used to apply tags to a content version via the API.

**Type**
string


Standard Objects ContentVersion

**Field** **Details**

**Properties**
Nillable, Filter,Group, Sort

**Description**
A preview of a document. Available in API version 35.0 and later.

```
Title

VersionData

VersionDataURL

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

The title of a document.

**Type**
base64

**Properties**
Create, Nillable, Update

**Description**
The content or body of the note, which can include properly formatted HTML or plain text.
When a document is uploaded or downloaded via the API, it should be base64 encoded (for
upload) or decoded (for download). Any special characters within plain text in the `Content`
field must be escaped. You can escape special characters by calling
`content.escapeHtml4()` .

This field can't be set for links.

The maximum file size you can upload via the SOAP API is 50 MB. When a document is
uploaded or downloaded via the API, it is converted to base64 and stored in `VersionData` .
This conversion increases the document size by approximately 37%. Account for the base64
conversion increase so that the file you plan to upload is less than 50 MB after conversion.

If a custom Apex download handler is active, this field is accessed from the API, and the
download is not allowed, Salesforce will return a
`CONTENT_CUSTOMIZED_DOWNLOAD_EXCEPTION` error.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URL used to fetch a file from the binary data endpoint. This field is only populated on
direct queries to ContentVersion, and not when queried through a related entity’s foreign
key to ContentVersion.


Standard Objects ContentVersion

**Field** **Details**

If available, access preview images of a file by appending a `thumb` query parameter to this
URL. For example:

```
                    myContentVersion.VersionDataUrl + '?thumb=THUMB240BY180'

```

Available `thumb` parameter values are:

**•** `THUMB720BY480`                   - corresponds to the `big-thumbnail` preview format

**•** `THUMB240BY180`                   - corresponds to the `thumbnail` preview format

**•** `THUMB120BY90`                   - corresponds to the `tiny-thumbnail` preview format

[See File Preview in the](https://developer.salesforce.com/docs/atlas.en-us.262.0.chatterapi.meta/chatterapi/connect_resources_files_preview_format.htm) _Connect REST API Developer Guide_ for additional details about file
previews.

This field can't be set for links.

This field is available in API versions 55.0 and later.

```
VersionNumber

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version number. The number increments with each version of the document, for example,
1, 2, 3.

**•** Use this object to create, query, retrieve, search, edit, and update a specific version of a Salesforce CRM Content document or Salesforce
file. Use the ContentDocument object to retrieve, query, update, and delete the latest version of a document, but not a content pack,
in a library or a Salesforce file.

**•** Use this object to create, query, retrieve, search, edit, and update a specific version of a Salesforce file. Use the ContentDocument
object to retrieve, query, update, and delete the latest version of a Salesforce file.

**•** To query a file that is shared only with a record, you must specify the content ID of the file.

**•** Not all fields can be set for Salesforce Files.

**•** You can only update a version if it is the latest version and if it is published.

**•** You can't archive versions.

**•** Using API version 32.0 and later, you can update record types on versions.

**•** You can't delete a version via the API.

**•** The maximum file size you can upload via the SOAP API is 50 MB. When a document is uploaded or downloaded via the API, it is
converted to base64 and stored in `VersionData` . This conversion increases the document size by approximately 37%. Account
for the base64 conversion increase so that the file you plan to upload is less than 50 MB after conversion.

**•** To download a document via the API, you must export the `VersionData` of the document. This does not increase the download
count.


Standard Objects ContentVersion

**•** When you upload a document from your local drive using the Data Loader, you must specify the actual path in both `VersionData`
and `PathOnClient` . `VersionData` identifies the location and extracts the format and `PathOnClient` identifies the type
of document being uploaded.

**•** SOQL queries on the ContentVersion object return all versions of the document. SOSL searches on the ContentVersion object return
only the most recent version of the document.

**•** To query a file that is accessible only through a record share, you must specify the content ID of the file. When SOQL querying the
ContentVersion object, either the `ContentVersionId` or the `ContentDocumentId` must be compounded by an AND
operator.

For example,

```
     SELECT FileExtension, Title FROM ContentVersion

     WHERE (ContentDocumentId = '<ContentDocumentId>' or Id='<ContentVersionId>') and

     IsLatest=true

     SELECT Id, VersionData, FileExtension, Title FROM ContentVersion

     WHERE ContentDocumentId='<ContentDocumentId>' AND FirstPublishLocationId =

     '<FirstPublishLocationId>'

```

**•** If you query versions in the API, versions with a `PublishStatus` of `Upload Interrupted` are not returned.

**•** Documents published into a personal library assume the default record type that is set for the user profile of the person publishing
the document (General, if no default is set for the user profile).

Note: An administrator can rename the default ( _Content Version Layout_ ) page layout.

**•** Contact Manager, Group, Professional, Enterprise, Unlimited, and Performance Edition customers can publish a maximum of 200,000
new versions per 24–hour period. Developer Edition and trial users can publish a maximum of 2,500 new versions per 24–hour
period.

**•** Custom validation rules can prevent an update of documents published into a personal library via the API.

Applying Tags to ContentVersion Records

Tags can be applied to ContentVersion records using either Enterprise or Partner API.

To apply tags to a ContentVersion record, set a value in the `TagCsv` field. For example, setting this field to `one,two,three` creates
and associates three tags to that version.

**•** The maximum length of the `TagCsv` field is 2,000 characters.

**•** The maximum length of an individual tag is 100 characters.

**•** When tags are applied to a version, the content is indexed automatically and the tags are searchable.

**•** You can't apply tags to a `TagCsv` that is published into a personal library. You can apply tags to a `TagCsv` that's in a shared
library or folder.

**•** You can't apply tags using the ContentDocument object.

**•** You can't change or delete tag names. You can remove tags from a document, but that doesn't delete the tag.

**•** Tags are case insensitive. You can't have two tags with the same name even if they use different uppercase and lowercase letters.
The case of the original tag is always used.

To delete tags from a ContentVersion record, perform a standard API update, and remove any values from the `TagCsv` field that you
want to delete. For example, if the original `TagCsv` is `one,two,three`, perform an API update specifying `one,three` in the
`TagCsv` field to delete `two` . To delete all tags from a ContentVersion you perform a standard API update by setting the field to `null` .


### Standard Objects ContentVersionComment

If you create a ContentVersion record and want to revise it via the API, you insert another ContentVersion record but associate it to the
same ContentDocument record as the original. This has an impact on tagging:

**•** If you insert the revision and do not set any value in the `TagCsv` field, any tags applied to the previous version are automatically
applied to the new version.

**•** If you insert the revision and specify a new `TagCsv` field, no tags transfer over and the tags you specify are applied instead.

When you perform a SOQL query for a ContentVersion record and select the `TagCsv` field, all the tags associated with that record are
returned. The tags in the string are always ordered alphabetically even if they were inserted in a different order. You can't use the
`TagCsv` field as part of a filter in a SOQL query. You can't query all tags in your organization.

Library tagging rules:

**•** API tagging respects the tagging restrictions that exist on any library that the document is published into. For example, if the library
is in restricted tagging mode and only allows tags `one,three`, you can't save a version with a `TagCsv` of `one,two,three` .

**•** If the library is in guided tagging mode, you can apply tags to the ContentVersion. You can't query the value of guided tags on a
library, but you can query the tagging model of a library.

Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ContentVersionChangeEvent on page 68 (API version 55.0)**
Change events are available for the object.

**ContentVersionHistory**

History is available for tracked fields of the object.

SEE ALSO:

ContentDocument

ContentVersionHistory

### ContentVersionComment

Represents a comment on a version of a file. This object is available in API version 42.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Only users with Modify All Data permission have access to this object.


Standard Objects ContentVersionComment

Fields

**Field** **Details**

```
ContentDocumentId

ContentVersionId

UserComment

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the file.

This is a relationship field.

**Relationship Name**
ContentDocument

**Relationship Type**
Lookup

**Refers To**
ContentDocument

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the version of the file.

This is a relationship field.

**Relationship Name**
ContentVersion

**Relationship Type**
Lookup

**Refers To**
ContentVersion

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
ID of the user who commented on the file.


### Standard Objects ContentVersionHistory ContentVersionHistory

Represents the history of a specific version of a document. This object is available in version 17.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

Special Access Rules

**•** Customer and Partner Portal users must have the “View Content in Portal” permission to query content in libraries where they have
access.

**•** A user can query all versions of a document from their personal library and any version that is part of or shared with a library where
they are a member, regardless of library permissions.

Note: To record an event in `contentVersionViewed`, make sure:

**•** All files are published to a Content Library.

**•** The details page is viewed in Salesforce Classic.

Fields

**Field** **Details**

```
ContentVersionId

DataType

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the version.

This is a relationship field.

**Relationship Name**
### ContentVersion

**Relationship Type**
Lookup

**Refers To**
### ContentVersion

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects ContentVersionHistory

**Field** **Details**

**Description**
Data type of the field that was changed.

```
Division

Field

NewValue

OldValue

```

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
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The name of the field that was changed. Possible values include:

**•** `contentVersionCreated` —A new version is created.

**•** `contentVersionUpdated` —The title, description, or any custom field on the
version is changed.

**•** `contentVersionDownloaded` —A version is downloaded.

**•** `contentVersionViewed` —The version details are viewed.

**•** `contentVersionRated` —The version is rated.

**•** `contentVersionCommented` —The version receives a comment.

**•** `contentVersionDataReplaced` —The new version replaces the previous version,
which can happen only when the new version is uploaded immediately after the previous
version.

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


### Standard Objects ContentVersionRating

**Field** **Details**

**Description**
The latest value of the field before it was changed.

Usage

Use this read-only object to query the history of a document version.

SEE ALSO:

### ContentVersion ContentVersionRating

Represents a rating on a version of a file. This object is available in API version 42.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Only users with Modify All Data permission have access to this object.

Fields

**Field** **Details**

```
ContentVersionId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the version of the file.

This is a relationship field.

**Relationship Name**
### ContentVersion

**Relationship Type**
Lookup

**Refers To**
### ContentVersion


### Standard Objects ContentWorkspace

**Field** **Details**

```
Rating

UserComment

UserId

### ContentWorkspace

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Rating of the file.

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
Comment made by the user who rated the file.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who rated the file.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

Represents a content library. This object is available in versions 17.0 and later.

Note: This object doesn’t apply to personal libraries.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Note: create( ), update( ) and delete( ) on ContentWorkspace are supported in API version 40.0 and later only.


Standard Objects ContentWorkspace

Special Access Rules

**•** The Access Libraries user permission allows orgs to make libraries available to users without requiring that they have the legacy
Salesforce CRM Content license. This permission is available for profiles and permission sets on most standard user licenses, and isn’t
available for High Volume Customer Portal, Customer Community, or Chatter Free licenses. Available in API versions 40.0 and later.

**•** Users with the Create Libraries user perm or the Manage Salesforce CRM Content administrator permission can create libraries
(ContentWorkspaces) from the Libraries tab in Salesforce Classic and from the API.

**•** Customer and Partner Portal users can only edit the library document object if they have a Salesforce CRM Content feature license.

**•** Customer and Partner Portal users can query this object if they have the “View Content in Portal” permission. A user can query all
public libraries where they’re members, regardless of library permissions.

**•** Automated process users can’t publish documents to libraries (ContentWorkspaces).

Fields

**Field** **Details**

```
DefaultRecordTypeId

Description

DeveloperName

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the default content type for the library. Content types are the containers
for custom fields in Salesforce CRM Content.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Text description of the content library.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique name of the library in the API. Allows a link to the library to be
packaged when an asset file is added to a package. Although libraries aren’t a
packageable entity, references to libraries with a developer name will be
included in the package when asset files are packaged. These links can then
be restored in the target org.

This name can contain only underscores and alphanumeric characters, and
must be unique in your org. It must begin with a letter, not include spaces, not


Standard Objects ContentWorkspace

**Field** **Details**

end with an underscore, and not contain two consecutive underscores. Label
is Unique Name.

This field is available in API version 39.0 and later.

```
IsRestrictContentTypes

IsRestrictLinkedContentTypes

Name

NamespacePrefix

RootContentFolderId

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read only. Indicates whether content types have been restricted ( `true` ) or
not ( `false` ).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read only. Indicates whether linked content types have been restricted ( `true` )
or not ( `false` ).

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the library.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique name of the library in the API. Allows a link to the library to be
packaged when an asset file is added to a package. Limit: 15 characters. This
field is available in API version 39.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of root folder of the library. This field is available in API version 39.0 and later.


Standard Objects ContentWorkspace

**Field** **Details**

```
ShouldAddCreatorMembership

TagModel

WorkspaceImageId

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Group

**Description**
Automatically create a library membership for the user creating the library. Note
this field isn’t meant for query and always returns false in query. This field is
available in API version 40.0 and later.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of tagging assigned to a library. Valid values are:

**•** `U`  - Unrestricted. No restrictions on tagging. Users can enter any tag when
publishing or editing content.

**•** `G`  - Guided. Users can enter any tag when publishing or editing content,
but they’re also offered a list of suggested tags.

**•** `R`  - Restricted. Users must choose from a list of suggested tags.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of a library image. Image files can be assigned to libraries for branding and
easy identification. Library image is visible to all users, even if they aren’t library
members. This field is available in API version 43.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of a library image. Image files can be assigned to libraries for branding and
easy identification. Library image is visible to all users, even if they are not library
members. This field is available in API version 43.0 and later.

This is a relationship field.

**Relationship Name**
WorkspaceImage


### Standard Objects ContentWorkspaceDoc

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
ContentAsset

```
WorkspaceType

```

Usage

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Differentiates between different types of libraries. Valid values are:

**•** `R`  - Regular library

**•** `B`  - Org asset library

This field is available in API version 39.0 and later.

Use this object to query libraries to find out where documents can be published.

If the content type isn’t specified when publishing a new version into a library, it is determined by the `DefaultRecordTypeId` of
the primary library.

As of 40.0, you can create, update, or delete a library via the API.

SEE ALSO:

### ContentWorkspaceDoc ContentWorkspaceDoc

Represents a link between a document and a public library in Salesforce CRM Content. This object is available in versions 17.0 and later.

Note: This object does not apply to documents and versions in a personal library.

Supported Calls

`create()`, `delete()`, `describeSObjects()query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

**•** Customer and Partner Portal users must have the “View Content in Portal” permission in order to query and obtain content in libraries
where they have access.

**•** Customer and Partner Portal users can only edit documents if they have a Salesforce CRM Content feature license.


Standard Objects ContentWorkspaceDoc

**•** To create a ContentWorkspaceDoc, you must be a member of the library with one of these library privileges enabled:

**–** “Add Content”

**–** “Add Content On Behalf of Others”

**–** “Manage Library”

**•** To query all library documents in a library, a user must be a member of that library, regardless of library permissions.

Fields

**Field** **Details**

```
ContentDocumentId

ContentWorkspaceId

IsOwner

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Read only. ID of the library document.

This is a relationship field.

**Relationship Name**
ContentDocument

**Relationship Type**
Lookup

**Refers To**
ContentDocument

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Read only. ID of the library.

This is a relationship field.

**Relationship Name**
ContentWorkspace

**Relationship Type**
Lookup

**Refers To**
ContentWorkspace

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


### Standard Objects ContentWorkspaceMember

**Field** **Details**

**Description**
Read only. Indicates whether the library owns the document and determines
permissions for that document ( `true` ) or not ( `false` ). Documents can belong to
more than one library, but only one library owns the document and determines its
permissions.

Usage

**•** Use this object to link a document to one or more libraries.

**•** To share a document with additional libraries, create additional ContentWorkspaceDoc records which join the document to the
additional libraries.

**•** Inserting a ContentWorkspaceDoc triggers the publish process for public libraries.

**•** A document can be published into many public libraries, but it will always be owned by one library which controls the security of
the document.

**•** A document can only be published into the document owner's personal library. You can't publish into another user's personal library.
Personal libraries are not visible via the API.

**•** To publish a document into a personal library, you must specify your user ID as the first publish location ID. If you leave the first
publish location ID blank, it defaults to the current user's ID.

**•** A document can be published from a personal library into a public library, but once it has been published into the public library, it
can't be published into the personal library again.

**•** You can't publish a document from a personal library into a public library that has restricted content types.

**•** You can't update or delete a library document via the API.

SEE ALSO:

### ContentWorkspace ContentWorkspaceMember

Represents a member of a content library. This object is available in API version 40.0 and later.

Manage library membership from the API.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

A user can create/update/delete memberships if they have the Manage Salesforce CRM Content admin perm or the Manage Library
permission for the library concerned.


Standard Objects ContentWorkspaceMember

Fields

**Field** **Details**

```
ContentWorkspaceId

ContentWorkspacePermissionId

MemberId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the library.

This is a relationship field.

**Relationship Name**
ContentWorkspace

**Relationship Type**
Lookup

**Refers To**
ContentWorkspace

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The id of the library permission or role.

This is a relationship field.

**Relationship Name**
ContentWorkspacePermission

**Relationship Type**
Lookup

**Refers To**
ContentWorkspacePermission

**Type**
reference

**Properties**
Create, Filter, Group,Namepointing, Sort

**Description**
ID of the library member (the member is either a user or a group).

This is a polymorphic relationship field.

**Relationship Name**
Member


### Standard Objects ContentWorkspacePermission

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
Group, User

```
MemberType

```

Usage

**Type**
picklist

**Properties**
Filter, Group, Nillable,Restricted picklist, Sort

**Description**
The type of library member. Valid values are:

**•** G - Group

**•** U - User

Use this object to create, update, or delete members from a library.

### ContentWorkspacePermission

Represents a library permission. This object is available in API version 40.0 and later.

A library permission is a group of privileges assigned to each content library member. It determines which tasks a member can perform
in a particular library. The same user can have a different library permission in each of his or her libraries.

Note: Library permissions do not apply to personal libraries. All library users can save files in their personal libraries.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

The ability to create permissions requires either the Manage Salesforce CRM Content admin perm or the Manage Content Permissions
user perm.

Fields

**Field** **Details**

```
Description

```

**Type**
textarea


Standard Objects ContentWorkspacePermission

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

```
Name

PermissionsAddComment

PermissionsAddContent

PermissionsAddContentOBO

PermissionsArchiveContent

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Namefield, Sort, Update

**Description**
Name of the library.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to post comments to any content in the library and view all comments
in the library. Users can edit or delete their own comments.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to publish new content to the library, upload new content versions, or
restore archived (deleted) content. Content authors can also change any tags associated
with their content and archive or delete their own content.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to choose an author when publishing content in the library.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to archive and restore any content in the library.


Standard Objects ContentWorkspacePermission

**Field** **Details**

```
PermissionsChatterSharing

PermissionsDeleteContent

PermissionsDeliverContent

PermissionsFeatureContent

PermissionsManageWorkspace

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to make content from this library accessible outside of the library, sharing
with a record or in Chatter. From a record or from Chatter, select a file from the library and
attach it to a record or a post.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to delete any content in the library. Authors can undelete their own
content from the Recycle Bin.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to share content outside the org via a content delivery or public link.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to identify any content in the library as “featured.”

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to perform any action in the library. This privilege is required to edit a
library’s name and description, add or remove library members, or delete a library. Manage
Library is a super permission which provides all other permission options listed except Deliver
Content. Creating a library requires the Manage Salesforce CRM Content app permission or
Create Libraries system permission.


Standard Objects ContentWorkspacePermission

**Field** **Details**

```
PermissionsModifyComments

PermissionsOrganizeFileAndFolder

PermissionsTagContent

PermissionsViewComments

Type

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to edit or delete comments made to any content in the library.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to create, rename, and delete folders in libraries.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to add tags when publishing content or editing content details in the
library.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Permission for user to view comments.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Provides the type of access a user has to a library. Valid values are:

**•** Library Administrator

**•** Author

**•** Viewer

**•** Custom


### Standard Objects ContentWorkspaceSubscription ContentWorkspaceSubscription

Represents a subscription for a user following a library. This object is available in API version 42.0 and later.

Supported Calls

`delete()`, `describeSObjects()`, `query()`, `retrieve()`

Special Access Rules

Only users with Modify All Data permission have access to this object.

Fields

**Field** **Details**

```
ContentWorkspaceId

UserId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the library.

This is a relationship field.

**Relationship Name**
### ContentWorkspace

**Relationship Type**
Lookup

**Refers To**
### ContentWorkspace

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user following the library.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup


### Standard Objects ContextParamMap

**Field** **Details**

**Refers To**
User

### ContextParamMap

Represents optional context data for a Conversation or a ConversationParticipant. This object is available in API version 57.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ContextEntityId

MapKey

MapValue

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Conversation or ConversationParticipant record.

This field is a polymorphic relationship field.

**Relationship Type**
Lookup

**Refers To**
Conversation, ConversationParticipant

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The key for the context data.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The value for the context data.


### Standard Objects Contract Contract

Represents a contract (a business agreement) associated with an Account.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AccountId

ActivatedById

ActivatedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort,Update

**Description**
Required. ID of the Account associated with this contract.

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
Filter, Group, Nillable, Sort,Update

**Description**
ID of the User who activated this contract.

This field is a relationship field.

**Relationship Name**
ActivatedBy

**Relationship Type**
Lookup

**Refers To**
User

**Type**
dateTime


Standard Objects Contract

**Field** **Details**

**Properties**
Filter, Nillable, Sort, Update

**Description**
Date and time when this contract was activated.

```
ActivityMetricId

ActivityMetricRollupId

AggregationStrategy

```

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

This field is a relationship field.

**Relationship Name**
ActivityMetricRollup

**Refers To**
ActivityMetricRollup

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The aggregation strategy when creating a pricing contract.

Valid value is `Cumulative` . This field is available with Revenue Cloud in API version 64.0
and later.


Standard Objects Contract

**Field** **Details**

```
BillingAddress

BillingCity

BillingCountry

BillingCountryCode

BillingGeocodeAccuracy

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the billing address. Read-only. See Address Compound Fields for
details on compound address fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the billing address. The maximum size is 40 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the billing address of this account. The maximum size is 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO country code for the contract's billing address.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The accuracy of the geocode for the billing address.

Possible values are:

**•** `Address`

**•** `Block`

**•** `City`

**•** `County`

**•** `ExtendedZip`


Standard Objects Contract

**Field** **Details**

**•** `NearAddress`

**•** `Neighborhood`

**•** `State`

**•** `Street`

**•** `Unknown`

**•** `Zip`

```
BillingLatitude

BillingLongitude

BillingPostalCode

BillingState

BillingStateCode

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `BillingLongitude` to specify the precise geolocation of a billing address.
Acceptable values are numbers between –90 and 90 with up to 15 decimal places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `BillingLatitude` to specify the precise geolocation of a billing address.
Acceptable values are numbers between –180 and 180 with up to 15 decimal places.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the billing address of this account. The maximum size is 20 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the billing address. The maximum size is 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Contract

**Field** **Details**

**Description**
The ISO state code for the contract's billing address.

```
BillingStreet

CompanySignedDate

CompanySignedId

ContractNumber

ContractTerm

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Street address for the billing address.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date your organization signed the contract.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the user who signed the contract.

This field is a relationship field.

**Relationship Name**
CompanySigned

**Relationship Type**
Lookup

**Refers To**
User

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Number of the contract.

**Type**
int


Standard Objects Contract

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of months that the contract is valid.

```
CustomerSignedDate

CustomerSignedId

CustomerSignedTitle

Description

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the customer signed the contract.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Contact who signed this contract.

This field is a relationship field.

**Relationship Name**
CustomerSigned

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Title of the customer who signed the contract.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the contract.


Standard Objects Contract

**Field** **Details**

```
EndDate

HasContractCotermination

IsPricingContract

IsDeleted

LastActivityDate

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort,

**Description**
Read-only. Calculated end date of the contract. This value is calculated by adding the
`ContractTerm` to the `StartDate` . If the **Auto-calculate Contract End Date** setting
is disabled, the contract end date is editable.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the contract can be coterminated ( `true` ) or not ( `false` ).

The default value is `false` . This field is available with Revenue Cloud in API version 65.0
and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the contract has related contract item prices ( `true` ) or if there are no
contract item prices for the contract ( `false` ). This field is available with Revenue Cloud in
API version 63.0 and later.

**Type**
boolean

**Properties**
Defaulted on create or filter

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
The label is **Deleted** .

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Value is the most recent:

**•** The due date of the most recent event is logged against the record.


Standard Objects Contract

**Field** **Details**

**•** The due date of the most recently closed task associated with the record.

```
LastApprovedDate

LastReferencedDate

LastViewedDate

OwnerExpirationNotice

OwnerId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Last date the contract was approved.

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
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it’s possible that the user only accessed this record or list view ( `LastReferencedDate` )
but didn’t view it.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Number of days ahead of the contract end date (15, 30, 45, 60, 90, and 120). Used to notify
the owner in advance that the contract is ending.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who owns the contract.

This field is a relationship field.


Standard Objects Contract

**Field** **Details**

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

```
Pricebook2Id

PricingSource

RecordTypeId

RenewalTerm2

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the pricebook, if any, associated with this contract.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Source of the pricing for the contract.

Valid values are:

**•** `LastTransaction`

**•** `PriceBookListPrice` —Price Book or List Price

Available in API version 60.0 and later.

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the record type assigned to this object.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The default subscription term for renewals. For example, if the Renewal Term Unit is months
and you want a 6-month term, set the Renewal Term to 6. Available in API version 60.0 and
later.


Standard Objects Contract

**Field** **Details**

```
RenewalTermUnit

ShippingAddress

ShippingCity

ShippingCountry

ShippingCountryCode

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The unit of time for a subscription term.

Valid values are:

**•** `Annual` —UI label is **Years**

**•** `Months`

**•** `Quarterly` —Available in API version 61.0 and later.

**•** `Semi-Annual` —Available in API version 61.0 and later.

Available in API version 60.0 and later.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the shipping address. Read-only. See Address Compound Fields for
details on compound address fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the shipping address. City maximum size is 40 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the shipping address. Country maximum size is 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO country code for the contract's shipping address.


Standard Objects Contract

**Field** **Details**

```
ShippingGeocodeAccuracy

ShippingLatitude

ShippingLongitude

ShippingPostalCode

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The accuracy of the geocode for the shipping address.

Valid values are:

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

Available in API version 60.0 and later.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `ShippingLongitude` to specify the precise geolocation of a shipping address.
Acceptable values are numbers between –90 and 90 with up to 15 decimal places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `ShippingLatitude` to specify the precise geolocation of an address.
Acceptable values are numbers between –180 and 180 with up to 15 decimal places.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects Contract

**Field** **Details**

**Description**
Details of the shipping address. The postal code maximum size is 20 characters.

```
ShippingState

ShippingStateCode

ShippingStreet

SourceQuoteId

SpecialTerms

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details of the shipping address. The maximum size for the state is 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO state code for the contract's shipping address.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street address of the shipping address. The maximum size is 255 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Sort,Update

**Description**
ID of the source quote associated with this contract. This field is available with Revenue Cloud
in API version 64.0 and later.

This field is a relationship field.

**Relationship Name**
Contract

**Relationship Type**
Lookup

**Refers To**
Quote

**Type**
textarea


Standard Objects Contract

**Field** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Special terms that apply to the contract.

```
StartDate

Status

StatusCode

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort,Update

**Description**
Start date for this contract. The label is **Contract Start Date** .

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The picklist of values that indicate order status. Each value is within one of two status
categories defined in `StatusCode` . For example, the status picklist may contain: Ready
to Ship, Shipped, Received as values within the Activated `StatusCode` .

Valid values are:

**•** `Activated`

**•** `Draft`

**•** `In Approval Process`

Available in API version 60.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status category for the contract. A contract can be Draft, InApproval, or Activated. Label
is **Status Category** .

Valid values are:

**•** `Activated`

**•** `Draft`

**•** `InApproval`

Available in API version 60.0 and later.


### Standard Objects ContractContactRole

**Field** **Details**

```
UnitPriceUplift

```

Usage

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the percentage increase of a line item’s unit price. This field is available with Revenue
Cloud in API version 64.0 and later.

The Contract object represents a business agreement.

The `Status` field specifies the current state of a contract. Status strings (defined in the ContractStatus object) represent its current
state ( `Draft`, `InApproval`, or `Activated` ).

Client applications must initially create a Contract in a non-Activated state. Client applications can subsequently activate a Contract by
updating it and setting the value in its `Status` field to `Activated` ; however, the `Status` field is the only field you can update
when activating the Contract.

After a Contract has been activated, your client application can't change its status; however, before activation, your client application
can change the status value from `Draft` to `InApproval` via the API. Also, your client application can delete contracts whose status
is `Draft` or `InApproval` but not when a contract status is `Activated` .

Client applications can use the API to create, update, delete, and query any Attachment associated with a contract.

Associated Objects

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**AccountChangeEvent (API version 46.0)**
Change events are available for the object.

**ContractFeed (API version 18.0)**
Feed tracking is available for the object.

**ContractHistory**

History is available for tracked fields of the object.

SEE ALSO:

### ContractContactRole

ContractStatus

### ContractContactRole

Represents the role that a Contact plays on a Contract.


Standard Objects ContractContactRole

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
ContactId

ContractId

IsDeleted

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the Contact associated with this Contract.

This is a relationship field.

**Relationship Name**
Contact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the Contract.

This is a relationship field.

**Relationship Name**
Contract

**Relationship Type**
Lookup

**Refers To**
Contract

**Type**
boolean

**Properties**
Defaulted on create, Filter


### Standard Objects ContractLineItem

**Field** **Details**

**Description**
Indicates whether the object has been moved to the Recycle Bin ( `true` ) or not ( `false` ).
Label is **Deleted** .

```
 IsPrimary

 Role

```

SEE ALSO:

ContractStatus

### ContractLineItem

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort,Update

**Description**
Specifies whether this Contact plays the primary role on this Contract ( `true` ) or not ( `false` ).
Each contract has one primary contact role. Default is `false` . Labels is **Primary** .

**Type**
picklist

**Properties**
Create, Filter, Nillable, Group, Sort, Update

**Description**
Name of the role played by the Contact on this Contract, such as Decision Maker, Approver,
Buyer, and so on. Must be unique—there can't be multiple records in which the
`ContractId`, `ContactId`, and `Role` values are identical. Different contacts can play
the same role on the same contract. A contact can play different roles on the same contract.

Represents a product covered by a service contract (customer support agreement). This object is available in API version 18.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
AssetId

```

**Type**
reference


Standard Objects ContractLineItem

**Field** **Details**

**Properties**
Create, Filter, Nillable, Update

**Description**
Required. ID of the Asset associated with the contract line item. Must be a valid asset ID.

```
Description

Discount

EndDate

LastReferencedDate

LastViewedDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the contract line item.

**Type**
percent

**Properties**
Create, Filter, Nillable, Update

**Description**
The discount for the product as a percentage.

When updating, if you specify `Discount` without specifying `TotalPrice`, the
`TotalPrice` will be adjusted to accommodate the new `Discount` value, and the
`UnitPrice` will be held constant.

If you specify both `Discount` and `Quantity`, you must also specify either
`TotalPrice` or `UnitPrice` so the system can determine which one to automatically
adjust.

**Type**
date

**Properties**
Create, Filter, Nillable, Update

**Description**
The last day the contract line item is in effect.

**Type**
date

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
date


Standard Objects ContractLineItem

**Field** **Details**

**Properties**
Filter, Nillable, Sort, Update

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view ( `LastReferencedDate` ) but
not viewed it.

```
LineItemNumber

ListPrice

LocationId

ParentContractLineItemId

PricebookEntryId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Update

**Description**
Automatically-generated number that identifies the contract line item.

**Type**
currency

**Properties**
Filter, Nillable

**Description**
Corresponds to the `UnitPrice` on the PricebookEntry that is associated with this line
item, which can be in the standard pricebook or a custom pricebook. A client application
can use this information to show whether the unit price (or sales price) of the line item differs
from the pricebook entry list price.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The location associated with the contract line item.

If you have access to the location entity, it doesn’t necessarily mean you can access the
location id field. To access the location, you must have `userHasLocation` user access.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The line item’s parent line item, if it has one.

**Type**
reference


Standard Objects ContractLineItem

**Field** **Details**

**Properties**
Create, Filter, Update

**Description**
Required. ID of the associated PricebookEntry.

Only exists if Product2 is enabled.

```
Product2Id

Quantity

RootContractLineItemId

ServiceContractId

StartDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The product related to the contract line item.

**Type**
double

**Properties**
Create, Filter, Update

**Description**
Number of units of the contract line item (product) included in the associated service contract.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
(Read only) The top-level line item in a contract line item hierarchy. Depending on where a
line item lies in the hierarchy, its root could be the same as its parent.

**Type**
reference

**Properties**
Create, Filter

**Description**
Required. ID of the ServiceContract associated with the contract line item. Must be a valid
service contract ID.

**Type**
date

**Properties**
Create, Filter, Nillable, Update


Standard Objects ContractLineItem

**Field** **Details**

**Description**
The first day the contract line item is in effect.

```
Status

Subtotal

TotalPrice

UnitPrice

```

**Type**
picklist

**Properties**
Filter, Nillable

**Description**
Status of the contract line item.

**Type**
currency

**Properties**
Filter, Nillable

**Description**
Contract line item's sales price multiplied by the `Quantity` .

**Type**
currency

**Properties**
Filter, Nillable

**Description**
This field is available only for backward compatibility. It represents the total price of the
ContractLineItem

If you specify `Discount` and `Quantity`, this field or `UnitPrice` is required.

This field is nillable, but you can't set both `TotalPrice` and `UnitPrice` to null in the
same update request. To insert the `TotalPrice` for a contract line item via the API (given
only a unit price and the quantity), calculate this field as the unit price multiplied by the
quantity.

**Type**
currency

**Properties**
Create, Filter, Update

**Description**
The unit price for the contract line item. In the user interface, this field’s value is calculated
by dividing the total price of the contract line item by the quantity listed for that line item.
Label is **Sales Price** .

This field or `TotalPrice` is required. You can’t specify both.

If you specify `Discount` and `Quantity`, this field or `TotalPrice` is required.


### Standard Objects ContractLineOutcome

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ContractLineItemChangeEvent (API version 44.0)**
Change events are available for the object.

**ContractLineItemFeed**

Feed tracking is available for the object.

**ContractLineItemHistory**

History is available for tracked fields of the object.

### ContractLineOutcome

Represents information on a contract line outcome’s captured data and other related parameters that are used when capturing data.
This object is available in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

**•** Field Service must be enabled.

**•** Entitlements must be enabled.

Fields

**Field** **Details**

```
CalculationMethod

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The method used for calculating the contract line outcome’s captured data to determine
the outcome value. Select `Average` or `As Captured` to calculate the contract line
outcome. `Average` calculates the outcome value based on the average of all data captured
to date. `As Captured` calculates the outcome value based on the asset’s current data at
the time of the compliance check.

Possible values are:

**•** `AsCaptured`

**•** `Average`


Standard Objects ContractLineOutcome

**Field** **Details**

```
CaptureFrequency

ComplianceStatus

ContractLineItemId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The frequency at which data capturing and contract compliance check for the contract line
outcome occurs.

Possible values are:

**•** `Daily`

**•** `Monthly`

**•** `Weekly`

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates if the criteria were met. Compliant–The outcome is compliant with the contract.
Not Compliant–The outcome isn’t compliant with the contract. Not Available–The outcome’s
compliance information isn’t available yet. Invalid–The outcome isn’t valid because the
option selected for the Criteria Field of the recordset filter criteria was deleted. To restart the
calculation, create a new contract line outcome.

Possible values are:

**•** `Compliant`

**•** `Invalid`

**•** `NotAvailable`

**•** `NotCompliant`

The default value is `NotAvailable` .

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The contract line item associated with the contract line outcome.

This field is a relationship field.

**Relationship Name**
ContractLineItem

**Relationship Type**
Lookup


Standard Objects ContractLineOutcome

**Field** **Details**

**Refers To**
ContractLineItem

```
Description

EndDate

LastReferencedDate

LastViewedDate

Name

NextDataCaptureDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the contract line outcome.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The contract line outcome's data capture end date.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the contract line outcome was last modified. Its UI label is Last
Modified Date.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the contract line outcome was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the contract line outcome.

**Type**
dateTime


Standard Objects ContractLineOutcome

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The date of the next data capture and compliance check based on the capture frequency.
The date is auto-populated and updated after each capture

```
OwnerId

RecordsetFilterCriteriaId

ServiceContractId

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The contract line outcome’s owner. By default, the owner is the user who created the contract
line outcome record. Its UI label is Contract Line Outcome Owner.

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
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the recordset filter criteria in which the contract line outcome’s conditions are
defined.

This field is a relationship field.

**Relationship Name**
RecordsetFilterCriteria

**Relationship Type**
Lookup

**Refers To**
RecordsetFilterCriteria

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ContractLineOutcome

**Field** **Details**

**Description**
The service contract associated with the contract line item and the contract line outcome.

This field is a relationship field.

**Relationship Name**
ServiceContract

**Relationship Type**
Lookup

**Refers To**
ServiceContract

```
StartDate

```

Usage

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The contract line outcome's data capture start date.

Use this object to define the data capture frequency and other related parameters that are used when capturing data in order to evaluate
a service contract’s compliance.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ContractLineOutcomeChangeEvent on page 68**
Change events are available for the object.

**ContractLineOutcomeFeed on page 55**
Feed tracking is available for the object.

**ContractLineOutcomeHistory on page 63**
History is available for tracked fields of the object.

**ContractLineOutcomeOwnerSharingRule on page 65**
Sharing rules are available for the object.

**ContractLineOutcomeShare on page 67**
Sharing is available for the object.

SEE ALSO:

ContractLineOutcomeData


### Standard Objects ContractLineOutcomeData ContractLineOutcomeData

Represents the contract line outcome’s captured data. It stores the data that was captured between the contract line outcome’s start
date and end date. This object is available in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

**•** Field Service must be enabled.

**•** Entitlements must be enabled.

Fields

**Field** **Details**

```
CalculatedValue

CaptureDate

ContractLineOutcomeId

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The value calculated based on the contract line outcome’s calculation method and the
captured data.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date and time when the data was captured.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The contract line outcome associated with the contract line outcome data record.

This field is a relationship field.

**Relationship Name**
### ContractLineOutcome


Standard Objects ContractLineOutcomeData

**Field** **Details**

**Relationship Type**
Lookup

**Refers To**
ContractLineOutcome

```
KeyPerformanceIndicator

LastReferencedDate

LastViewedDate

Name

Value

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The key performance indicators (fields or asset attributes) that define the contract line
outcome’s compliance status.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the contract line outcome data record was last modified. Its UI label
is Last Modified Date.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the contract line outcome data record was last viewed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the contract line outcome data record.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The actual value of the key performance indicator.


### Standard Objects ContractStatus

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ContractLineOutcomeDataChangeEvent on page 68**
Change events are available for the object.

**ContractLineOutcomeDataFeed on page 55**
Feed tracking is available for the object.

**ContractLineOutcomeDataHistory on page 63**
History is available for tracked fields of the object.

**ContractLineOutcomeDataOwnerSharingRule on page 65**
Sharing rules are available for the object.

**ContractLineOutcomeDataShare on page 67**
Sharing is available for the object.

### ContractStatus

Represents the status of a Contract, such as Draft, InApproval, Activated, Terminated, or Expired.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ApiName

IsDefault

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Uniquely identifies a picklist value so it can be retrieved without using an id or primary label.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this is the default contract status value ( `true` ) or not ( `false` ) in the
picklist.


Standard Objects ContractStatus

**Field** **Details**

```
 MasterLabel

 SortOrder

 StatusCode

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Label for this contract status value. This display value is the internal label that does not get
translated.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number used to sort this value in the contract status picklist. These numbers are not
guaranteed to be sequential, as some previous contract status values might have been
deleted.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Code indicating the status of a contract. One of the following values:

**•** `Draft`

**•** `InApproval`

**•** `Activated`

Two other values ( `Terminated` and `Expired` ) are defined but are not available for use
via the API.

This object represents a value in the contract status picklist. The contract status picklist provides additional information about the status
of a Contract, such as its current state ( `Draft`, `InApproval`, or `Activated` ). You can query these records to retrieve the set of
values in the contract status picklist, and then use that information while processing Contract objects to determine more information
about a given contract. For example, the application could test whether a given contract is activated based on its `Status` value and
the value of the `StatusCode` property in the associated ContractStatus object.

SEE ALSO:

ContractContactRole


### Standard Objects ContractTag ContractTag

Associates a word or short phrase with a Contract.

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


### Standard Objects ConvAnalysisSummary

**Field Name** **Details**

**•** `Personal` —The tag can be viewed or manipulated only by a user with a matching
`OwnerId` .

Usage

ContractTag stores the relationship between its parent TagDefinition and the Contract being tagged. Tag objects act as metadata,
allowing users to describe and organize their data.

When a tag is deleted, its parent TagDefinition will also be deleted if the name is not being used; otherwise, the parent remains. Deleting
a TagDefinition sends it to the Recycle Bin, along with any associated tag entries.

### ConvAnalysisSummary

Represents the information stored for each run or refresh of Sales Signals. This object is available in API version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Users need the Sales Signals permission set and the Sales Signals feature must be enabled.

Fields

**Field** **Details**

```
AnalysisDate

DataModelVersion

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date when the actual data analysis was done, accounting for the delay between the
refresh start time and the data analysis.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The data model version generated by Hawking.


Standard Objects ConvAnalysisSummary

**Field** **Details**

```
Error

FlowIdentifier

RefreshDate

Status

TotalCalls

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The error message sent by Hawking when a refresh fails.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The UUID used to track the Hawking flow ID.

**Type**
dateTime

**Properties**
Create, Filter, Sort

**Description**
Required. The date when the admin started the refresh of their ECI data for processing.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. The status of the refresh or run.

Possible values are:

**•** `FAILED`

**•** `PARTIALLY_FAILED`

**•** `PROCESSING`

**•** `SUCCESS`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of calls that were analyzed for Sales Signals.


### Standard Objects ConvAnalysisTopic

**Field** **Details**

```
TotalMentions

### ConvAnalysisTopic

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of mentions or keywords that were analyzed.

Represents a topic generated from the Sales Signals refresh or run. For example, a product experiencing issues due to high pricing could
be a topic identified through the analysis of multiple calls. This object is available in API version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Users need the Sales Signals permission set and the Sales Signals feature must be enabled.

Fields

**Field** **Details**

```
CallPercentage

Category

```

**Type**
double

**Properties**
Create, Filter, Sort

**Description**
Required. The percentage of calls that apply to a topic, out of the total number of calls that
were analyzed.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Required. A classification or grouping used to filter topics. This field is used in conjunction
with `Keyword` .


Standard Objects ConvAnalysisTopic

**Field** **Details**

```
ConvAnalysisSummaryId

GenerationsIdentifier

Keyword

MentionCount

Order

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The conversation analysis summary associated with the topic.

This field is a relationship field.

**Relationship Name**
ConvAnalysisSummary

**Relationship Type**
Master-detail

**Refers To**
ConvAnalysisSummary (the parent object)

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The ID used to track the LLM-generated response for feedback purposes.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Required. A specific word used in conjunction with `Category` to filter topics. For example,
`Product:Salesforce`, where the keyword is Salesforce.

**Type**
int

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The number of call insights associated with the topic.

**Type**
int

**Properties**
Create, Filter, Group, Sort


Standard Objects ConvAnalysisTopic

**Field** **Details**

**Description**
Required. A numerical value used to sort topics in a sequence.

```
Summary

Title

TopicSentiment

TotalCalls

TotalCallsForCategoryKeyword

TotalMentionsForCategoryKeyword

```

**Type**
textarea

**Properties**
Create, Update

**Description**
Required. A detailed explanation of the topic.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The title of the topic that describes it.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The sentiment of the topic, whether it’s negative, neutral, or positive.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The total number of calls analyzed for the topic.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**

The total number of calls analyzed for `category:keyword` . Multiple topics can be under
a single `category:keyword` .

**Type**
int


### Standard Objects ConvAnalysisTopicEntry

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The total number of mentions analyzed for `category:keyword` .

```
TurnIdentifier

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
UUID that is generated and used to track a group of LLM-generated content.

### ConvAnalysisTopicEntry

Represents a single entry under the ConvAnalysisTopic object. An entry represents a segment of a video or voice call that is associated
with a conversation analysis topic. This object is available in API version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Users need the Sales Signals permission set and the Sales Signals feature must be enabled.

Fields

**Field** **Details**

```
BulletGenerationsIdentifier

CallId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The generation ID used to track the LLM-generated response for feedback purposes.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort


### Standard Objects Conversation

**Field** **Details**

**Description**
The unique identifier of the voice or video call that corresponds to the entry.

This field is a polymorphic relationship field.

**Relationship Name**
Call

**Refers To**
VideoCall, VoiceCall

```
ConvAnalysisTopicId

SnippetStartTime

Summary

### Conversation

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The conversation analysis topic associated with the entry.

This field is a relationship field.

**Relationship Name**
ConvAnalysisTopic

**Relationship Type**
Master-detail

**Refers To**
ConvAnalysisTopic (the parent object)

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The timestamp when the call is associated with the current topic entry.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The LLM-generated call summary that corresponds to the parent topic.

Represents a conversation between an end user and an agent. Available in API version 49.0 and later.


Standard Objects Conversation

Note: This object is available for Einstein Conversation Insights customers whose data is stored natively on the Salesforce Platform.
If you turned on Einstein Conversation Insights for the first time starting in Spring ’26, this object is available to query and access
using Salesforce tools. For existing ECI customers, data migration and access to related Salesforce Platform objects is scheduled
to begin in Summer ’26.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
ConversationChannelId

ConversationIdentifier

EndTime

Name

```

**Type**
reference

**Properties**
Filter, Group, idLookup, Sort

**Description**
The record ID of the channel used to initialize the conversation. This can either be a messaging
channel for the Messaging product or a call center for the Service Cloud Voice product.
Available in API version 50.0 and later.

Service Cloud Voice is now Salesforce Voice. You may see references to Service Cloud Voice
in Salesforce applications and documentation.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
A unique identifier generated for the conversation.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that a conversation ends.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The autogenerated name of the conversation.


### Standard Objects ConversationApiLog

**Field** **Details**

```
StartTime

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that a conversation starts.

### ConversationApiLog

Logs of an API operation on a specific conversation object done using the Conversation Service API. This object is available in API version
63.0 and later.

[This object stores the logs of operations done on the Conversation Service API. The Conversation Service API enables you to interact](https://developer.salesforce.com/docs/service/conversation-service-api/overview)
with conversational data on the Conversation Platform, offering tools to manage, access, and maintain your data effectively.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
Action

Name

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The specific action performed using the Conversation Service API.

Possible values are:

**•** `Delete`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Autogenerated name of the logs.


Standard Objects ConversationApiLog

**Field** **Details**

```
Operation

OwnerId

RequestedById

RequestedDate

RequestedEntityIdentifier

```

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Name of the operation that triggered the Conversation Srevice API log.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Owner ID that triggered the Conversation API log.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The User ID that triggered the Conversation API log.

This field is a relationship field.

**Relationship Name**
RequestedBy

**Refers To**
User

**Type**
dateTime

**Properties**
Create, Filter, Sort

**Description**
The date of the operation that triggered the Conversation API log.

**Type**
string


### Standard Objects ConversationContextEntry

**Field** **Details**

**Properties**
Create, Filter, Group, Sort

**Description**
The entity ID being created, updated, or deleted.

```
RequestedEntityType

Status

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of entity being created, updated, or deleted.

Possible values are:

**•** `MessagingEndUser` —Messaging End User

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the Conversation API operation.

Possible values are:

**•** `Completed`

**•** `Enqueued`

**•** `Failed`

**•** `InProgress` —In Progress

**•** `Requested`

### ConversationContextEntry

Represents the context of a message or an event in the chat history between an agent and a messaging user. This object is available in
API version 47.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

As of Summer ’20 and later, only authenticated internal and external users can access this object.


Standard Objects ConversationContextEntry

Fields

**Field** **Details**

```
 ConversationContextEntryName

 CustomDetailContextKey

 CustomDetailContextValue

 ParentId

```

Associated Objects

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The autogenerated number of the entry.

**Type**
textarea

**Properties**
Create, Nillable

**Description**
The key or name of the pre-chat field specified by the admin in the pre-chat implementation,
for example, `customer_email` .

**Type**
textarea

**Properties**
Create, Nillable

**Description**
The value entered in the pre-chat field by a user before starting the chat.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The Conversation ID this entry is associated with.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ConversationContextChangeEvent (API version 62.0)**
Change events are available for the object.


### Standard Objects ConversationChannelDefinition ConversationChannelDefinition

Represents a configurable definition of a conversation channel that’s implemented for Interaction Service for Bring Your Own Channel
for Messaging and Bring Your Own Channel for CCaaS messaging channels. This object is available in API version 60.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To access this object, interaction service must be configured. Access to standard objects requires Salesforce admin privileges or the
Customize Application permission.

Fields

**Field** **Details**

```
CapabilitiesSupportsCustomChannelParameters

CapabilitiesSupportsDoubleOptInConsent

CapabilitiesSupportsExplicitConsent

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether admins can configure custom parameters and parameter mappings for
messaging channels. Custom parameters and parameter mappings are used to pass additional
information at runtime to Omni-Channel flows. The default value is _`false`_ . Available in API
version 61.0.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the channel supports ( _`true`_ ) the Double Opt-In consent level. The default
value is _`false`_ . If set to true, then `capabilitiesSupportsExplicitConsent`
must also be set to true. This field is optional and isn’t supported for Bring Your Own Channel
for Messaging. It's only supported for Bring Your Own Channel for CCaaS.

**Type**
boolean

**Properties**
Filter


Standard Objects ConversationChannelDefinition

**Field** **Details**

**Description**
Indicates whether the channel supports ( _`true`_ ) the Explicit Opt-In consent level. This field
is optional.

```
CapabilitiesSupportsImplicitConsent

CapabilitiesSupportsIsoCountryCode

CapabilitiesSupportsKeywords

ConnectedAppOauthLink

ConnectedAppType

```

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the channel supports ( _`true`_ ) the Implicit Opt-In consent level. This value
is required and must always be set to true. The default value is false.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the channel supports ( _`true`_ ) ISO country codes. The default value is false.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the channel supports ( _`true`_ ) keywords. The default value is false.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
DO NOT SET OR CHANGE THIS VALUE. This value is automatically generated. This field
represents the OAuth link for the external client app (ECA) or connected app if the
ConnectedAppType is `Partner` . This is a string identifier to the ECA or connected app
containing the partner Org ID and the consumer ID minus the key prefixes.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects ConversationChannelDefinition

**Field** **Details**

**Description**
The owner of the external client app (ECA) or connected app used to manage authentication
between Salesforce Interaction Service and the Messaging or CCaaS partner’s system.

Possible values are:

**•** `Partner`

**•** `Customer`

The default value is `Partner` .

If set to _`Partner`_, the partner creates the ECA or connected app and includes it in their
managed package. If set to _`Customer`_, the admin creates the ECA or connected app.

Available in API version 62.0.

```
ConsentOwner

ConversationVendorInfoId

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The system the customer uses to manage consent levels.

Possible values are:

**•** `Partner`

**•** `Salesforce`

The default value is `Salesforce` .

For example, if set to _`Salesforce`_, consent levels are managed by the Salesforce system.
If set to _`Partner`_, consent levels are managed by the partner’s telephony system.

For Bring Your Own Channel for Messaging, this value must be set to _`Salesforce`_ .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The _`ConversationChannelDefinition.ConversationVendorInfoId`_
value used to link this record to the ConversationVendorInfo record. For example,
0m8000000000000123.

This field is a relationship field.

**Relationship Name**
ConversationVendorInfo

**Relationship Type**
Lookup

**Refers To**
ConversationVendorInfo


Standard Objects ConversationChannelDefinition

**Field** **Details**

```
customEventChnlAddrIdField

CustomEventPayloadField

customEventRecipientField

CustomEventTypeField

CustomIconId

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The mapping field that points to the custom field used to point to the
`ChannelAddressIdentifier` field.

This field is deprecated in API version 60.0 and will be removed in API version 61.0. Use a
combination of `customEventTypeField` and `customEventPayloadField`
instead.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The mapping field that points to the custom field used to point to the `Payload` field in
the format _`<orgNamespace>`_ __ _`<CustomFieldName>`_ __c. This is the API name of
the custom Payload field in the custom platform event. For example, devorg__Payload__c.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The mapping field that points to the custom field used to point to the Recipient field.

This field is deprecated in API version 60.0 and will be removed in API version 61.0. Use a
combination of `customEventTypeField` and `customEventPayloadField`
instead.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The mapping field that points to the custom field used to point to the Platform event type
(EventType) field, in the format _`<orgNamespace>`_ __ _`<CustomFieldName>`_ __c. This
is the API name of the custom EventType field in the custom platform event. For example,
devorg__EventType__c.

**Type**
reference


Standard Objects ConversationChannelDefinition

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
For Bring Your Own Channel for Messaging and Bring Your Own Channel for CCaaS, this field
represents the name of the status resource image used to identify the channel integration,
such as a channel logo. For the best results, set the image size to 50px x 50px and save the
image in SVG file format. This field is optional. Available in API version 61.0 and later.

This field is a relationship field.

**Relationship Name**
CustomIcon

**Relationship Type**
Lookup

**Refers To**
StaticResource

```
CustomPlatformEvent

CustomerConnectedAppOauthLink

DeveloperName

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The API name of the custom platform event created for the Interaction Service API in the
format _`<orgNamespace>`_ __ _`<CustomPlatformEventName>`_ __e. For example,
devorg__TestEvent__e.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
DO NOT SET OR CHANGE THIS VALUE. This value is automatically generated. This field
represents the OAuth link for the external client app or connected app created by an admin
if the ConnectedAppType is `Customer` . Available in API version 62.0.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name of the custom metadata type object in the API in the format
_`<Prefix>`_ _ _`<ConversationChannelDefinition>`_, where _`Prefix`_ matches
the prefix you gave to the name of the Interaction Service external client app or connected


Standard Objects ConversationChannelDefinition

**Field** **Details**

app. For example, Partner1_ChannelDefinition1, where Partner1 is the prefix and
ChannelDefinition1 is the given name.

```
EventCapabilitiesIsInboundAcknwOptionExposed

EventCapabilitiesIsProgressIndicatorOptExposed

EventCapabilitiesIsRoutingWorkResultSupported

EventCapabilitiesIsTypingIndicatorOptionHidden

```

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the partner supports read receipts and delivery receipts for inbound
messages ( `true` ) or whether the partner doesn’t support these inbound acknowledgments
and the functionality is hidden from the Salesforce admin in the Messaging settings ( `false` ).
The default value is `false` .

This field is available in API version 65.0 and later. Use this field instead of
`IsInboundReceiptsEnabled` .

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the partner supports progress indicators for AI agents ( `true` ) or whether
the partner doesn’t support them and the functionality is hidden from the Salesforce admin
in the Messaging settings ( `false` ). The default value is `false` .

This field is available in API version 65.0 and later.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the Routing Work Result event is sent as a Custom Platform event ( `true` )
or not ( `false` ). The default value is `false` .

This field is available in API version 65.0 and later. Use this field instead of
`IsRoutingWorkResultEnabled` .

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Indicates whether the partner doesn’t support typing indicators for outbound messages and
the functionality is hidden from the Salesforce admin in the Messaging settings ( `true` ) or


Standard Objects ConversationChannelDefinition

**Field** **Details**

whether outbound typing indicators are supported by the partner ( `false` ). The default
value is `false`, meaning the outbound typing indicator feature is supported by default.
To disable the outbound typing indicator feature, set this value to `true` .

This field is available in API version 65.0 and later. Use this field instead of
`IsTypingIndicatorDisabled` .

```
IsConferenceSupported

IsInboundReceiptsEnabled

IsRoutingWorkResultEnabled

IsTypingIndicatorDisabled

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the partner supports conferencing for Bring Your Own Channel ( `true` ),
or not ( `false` ). With conferencing, more than two participants are allowed in a Messaging
session. The default is `false` .

This field is available in API version 64.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the partner supports read receipts and delivery receipts for inbound
messages ( `true` ) or whether the partner doesn’t support these inbound acknowledgements
and the functionality is hidden from the Salesforce admin in the Messaging settings ( `false` ).
The default value is `false` .

Available in API versions 63.0 to 65.0. In API version 66.0 and later, this field is removed. Use
`EventCapabilitiesIsInboundAcknwOptionExposed` instead.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the Routing Work Result event is sent as a Custom Platform event or not.

The default value is `false` .

Available in API versions 64.0 and 65.0. In API version 66.0 and later, this field is removed.
Use `EventCapabilitiesIsRoutingWorkResultSupported` instead.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects ConversationChannelDefinition

**Field** **Details**

**Description**
Indicates whether the partner doesn’t support typing indicators for outbound messages and
the functionality is hidden from the Salesforce admin in the Messaging settings ( `true` ) or
whether outbound typing indicators are supported by the partner ( `false` ). The default
value is `false`, meaning the outbound typing indicator feature is supported by default.
To disable the outbound typing indicator feature, set this value to `true` .

Available in API versions 63.0 to 65.0. In API version 66.0 and later, this field is removed. Use
`EventCapabilitiesIsTypingIndicatorOptionHidden` instead.

```
MasterLabel

MaxParticipantsForCnfrOverride

NamespacePrefix

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The UI label name for the custom metadata type object in the API. This name appears in
several places in the UI, so include the partner channel name for easy identification. For
example, Channel Definition 1.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the limit for how many participants can be in a messaging conference. If set, this
field overrides the platform limit for the number of participants in a conference. If not set or
if set to a value higher than the messaging platform limit, the limit defaults to the messaging
platform limit of how many participants can be in a messaging conference at one time.

This field is available in API version 64.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
_`namespacePrefix`_ __ _`componentName`_ notation. The namespace prefix can have
one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This


### Standard Objects ConversationEntry

**Field** **Details**

field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

`NamespacePrefix` is null if the publisher is Salesforce.

```
RoutingOwner

### ConversationEntry

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The system the customer uses to manage routing for Bring Your Own Channel for Messaging
or Bring Your Own Channel for CCaaS.

Possible values are:

**•** `Partner`

**•** `Salesforce`

The default value is `Salesforce` .

For example, if set to _`Salesforce`_, routing is managed by the Salesforce system. If set to
_`Partner`_, routing is managed by the partner’s system.

For Bring Your Own Channel for Messaging, this value must be set to _`Salesforce`_ .

Represents a message or event in a voice call or messaging session. The schema on this page only applies to conversation entries for
[legacy chat. Refer to the ConversationEntry (Off-Core) schema in the Messaging Object Model guide to see the ConversationEntry schema](https://developer.salesforce.com/docs/service/messaging-object-model/guide/overview.html)
for Enhanced Channels. This object is available in API version 43.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

To use the ConversationEntry object, enable the Access Conversation Entries user permission, which is available in API version 50.0 and
later. Earlier versions do not require permissions.


Standard Objects ConversationEntry

Fields

**Field** **Details**

```
ActorId

ActorName

ActorType

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the author. The possible values can be `null` or any ID in the following domain
set:

**•** `BotDefinition`

**•** `LiveChatVisitor`

**•** `MessagingEndUser`

**•** `User`

This is a polymorphic relationship field.

**Relationship Name**
Actor

**Relationship Type**
Lookup

**Refers To**
MessagingEndUser, User

**Type**
string

**Properties**
Create, Filter, Nillable, Sort

**Description**
The name of the author sending the message or event.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The author of this entry in the chat history. The valid values include:

**•** `Agent`

**•** `Bot`

**•** `EndUser`

**•** `Supervisor`

**•** `System`


Standard Objects ConversationEntry

**Field** **Details**

```
ClientDuration

ClientTimestamp

ConversationId

EntryEndTime

EntryTime

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The length in milliseconds for the entry. This field is used with voice messages and other
applicable use cases. This value may be 0 if not set by the client. This field is available in API
version 51.0 and later.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The timestamp sent by the client when it generated the entry. This field is available in API
version 51.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The MessagingSession ID this entry belongs to.

This is a polymorphic relationship field.

**Relationship Name**
Conversation

**Relationship Type**
Lookup

**Refers To**
MessagingSession, VoiceCall

**Type**
datetime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The timestamp that this entry ended in the chat history. This field is available in API version
48.0 and later.

**Type**
datetime


Standard Objects ConversationEntry

**Field** **Details**

**Properties**
Create, Filter, Sort

**Description**
The timestamp of this entry in the chat history.

```
EntryTimeMilliSecs

EntryType

HasAttachments

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The milliseconds value for the time when an entry was received by the server. Note that the
related `EntryTime` field does not provide millisecond accuracy. This field is available in
API version 51.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of entry in the chat history. Can be a message ( `text` ) or an event. The possible
values include:

**•** `Text`

**•** `AdminOptedIn`

**•** `AdminOptedOut`

**•** `BotEscalated`

**•** `ChatbotClosedIdleSession`

**•** `ChatbotEndedChatByAction` —Conversation ended by automated action

**•** `ChatbotEndedTransferNotConfigured` —Conversation ended because
transfer fail is not configured

**•** `ChatbotEstablished`

**•** `ChatbotNotEstablished`

**•** `EndUserOptedIn`

**•** `EndUserOptedOut`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a message has attachments associated with it ( `true` ) or not ( `false` ).


Standard Objects ConversationEntry

**Field** **Details**

```
Message

MessageDeliverTime

MessageIdentifier

MessageReadTime

MessageSendTime

MessageStatus

```

**Type**
textarea

**Properties**
Create, Nillable

**Description**
The message or event sent by the author. In ConversationEntry records for enhanced
Messaging channels or Messaging for In-App and Web, the Message field is blank due to
data storage differences from standard channels.

**Type**
datetime

**Properties**
Create, Filter, Nillable, Sort

**Description**
Unused field reserved for future use.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The unique ID for the message. Maximum size is 36 characters.

**Type**
datetime

**Properties**
Create, Filter, Nillable, Sort

**Description**
Unused field reserved for future use.

**Type**
datetime

**Properties**
Create, Filter, Nillable, Sort

**Description**
Unused field reserved for future use.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort


Standard Objects ConversationEntry

**Field** **Details**

**Description**
The status of the message sent by the author. The valid values include:

**•** `Delivered`

**•** `Error`

**•** `Pending`

**•** `Read`

**•** `Sent`

```
MessageStatusCode

Seq

ServerReceivedTimestamp

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The code associated with a message status. `MessageStatusCode` is only populated
when a message is undeliverable

**Type**
int

**Properties**
Create, Filter, Group, Sort

**Description**
The sequence position of this entry in the chat history.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The timestamp recorded when the server received the entry. This is a unique value and is
used for ordering. This value can also be referred to as the “transcripted timestamp.” This
field is available in API version 51.0 and later.

Important: The schema on this page only applies to conversation entries for legacy chat. The legacy chat product is in
maintenance-only mode, and we won't continue to build new features. Refer to the ConversationEntry (Off-Core) schema in the
[Messaging Object Model guide to see the ConversationEntry schema for Enhanced Channels.](https://developer.salesforce.com/docs/service/messaging-object-model/guide/overview.html)

In standard SMS, WhatsApp, and Facebook Messenger channels, a ConversationEntry record is created for each message sent by a
messaging end user or an agent, bot, or automation. Each ConversationEntry record is associated with a MessagingSession record, which
represents the interaction between the messaging end user and the business. Access and work with ConversationEntry records like any


### Standard Objects ConversationParticipant

standard object. You can report on messaging activity and track the conversation workflow end to end. You can also download or delete
transcripts, redact sensitive text, and customize your workflows with solutions built on the ConversationEntry object.

In enhanced Messaging channels, Messaging for In-App and Web, and Service Cloud Voice ("enhanced channels"), inbound and outbound
messages are processed in one of two ways depending on your location.

**•** A ConversationEntry record is created but the `Message` field is blank, or

**•** No ConversationEntry record is created.

To get the fullest picture of conversations in enhanced channels, use Data Cloud, the Connect REST API, or the Conversation Transcript
[Export tool to access transcripts. See Accessing Messaging and Voice Conversation Data.](https://help.salesforce.com/s/articleView?id=service.conversation_transcript_access.htm&type=5&language=en_US)

Note: ConversationEntry records aren’t created until the messaging session ends and the agent closes the session tab. One
exception is for the first message in any standard messaging session, whose ConversationEntry record is created immediately.

### ConversationParticipant

Represents an active participant in a conversation. A new ConversationParticipant record is created each time a participant joins a
conversation. This object is available in API version 49.0 and later.

Note: This object is available for Einstein Conversation Insights customers whose data is stored natively on the Salesforce Platform.
If you turned on Einstein Conversation Insights for the first time starting in Spring ’26, this object is available to query and access
using Salesforce tools. For existing ECI customers, data migration and access to related Salesforce Platform objects is scheduled
to begin in Summer ’26.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
AppType

ConversationId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of app used by the participant, such as messaging, chatbot, live_message, agent.
The nillable property is available in API version 51.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The record ID of the conversation that this participant is part of.


Standard Objects ConversationParticipant

**Field** **Details**

```
JoinedTime

LastActiveTime

LeftTime

Name

ParticipantContext

ParticipantEntityId

```

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date and time that a participant joined a conversation.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date and time that a participant was last active during a conversation.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that a participant left a conversation.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The autogenerated name of the conversation participants.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
An identifier, such as a Facebook page, to add context about this participant.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects ConvIntelligenceSignalRule

**Field** **Details**

**Description**
The ID of the record connected to this participant record, such as a Contact, Messaging End
User, or User record.

```
ParticipantKey

ParticipantRole

```

**Type**
string

**Properties**
Filter, idLookup, Group, Nillable, Sort

**Description**
A value that uniquely identifies this participant.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The role of this participant in the conversation, such as Agent, End User, or Supervisor.

### ConvIntelligenceSignalRule

Represents a conversation intelligence signal rule. The rule triggers actions based on real-time intelligence signals from your telephony
system or keywords mentioned by support reps or customers. The rule contains a set of conditions (subrules) and the filter logic used
to evaluate those conditions to determine whether to trigger actions. This object is available in API version 62.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

This type requires an add-on license for Salesforce Voice for Amazon Connect, Salesforce Voice for Partner Telephony with Amazon
Connect, Salesforce Voice for Partner Telephony, or Digital Engagement.

Fields

**Field** **Details**

```
ActionType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


Standard Objects ConvIntelligenceSignalRule

**Field** **Details**

**Description**

Required. Action to take based on the conversation intelligence signal detected during a
conversation. Possible values are:

Possible values are:

**•** `AlertSupervisor` –Sends an alert to the supervisor.

**•** `AlertSupervisorAndAgent` –Sends an alert to the rep and supervisor.

**•** `LaunchFlow` –Triggers an auto-launched flow. If set, also set `ActionValue` .

**•** `LaunchNBA` –Recommends the next best action to the rep.

```
ActionValue

ConversationChannelId

Criteria

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Action to perform based on the `ActionType` specified.

If `ActionType` is set to `LaunchFlow`, this value is the `DeveloperName` of the flow
to be launched. For example, EmailAlert.

For all other `ActionType` values, don’t set this parameter.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**

Required. ID ( `ChannelAddressIdentifier` ) of the Messaging channel or name
( `InternalName` ) of the Voice channel.

This field is a polymorphic relationship field.

**Relationship Name**
ConversationChannel

**Refers To**
CallCenter, MessagingChannel

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. Filter logic applied to the rule conditions (subrules). For example, ((1 AND 2) OR
3). The numbers in the formula are derived from the
`ConvIntelligenceSignalSubrule.Order` value plus 1. For example, filter logic


Standard Objects ConvIntelligenceSignalRule

**Field** **Details**

(1 AND 2) is calculated by adding the first condition ( `Order` =0) with the second condition
( `Order` =1).

```
DeveloperName

IsActive

Label

ParticipantRole

Service

```

**Type**
string

**Properties**
Required. Create, Filter, Group, Sort, Update

**Description**
API name of the conversation intelligence signal rule.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. Indicates whether the conversation intelligence signal rule is active ( `true` ) or
inactive ( `false` ). The default value is `false` .

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the conversation intelligence signal rule.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If `Service` is set to KeywordMatch, this value determines whether the rule applies to
utterances made by reps, customers, or both roles. Possible values are:

Possible values are:

**•** `Agent`

**•** `AgentOrCustomer`

**•** `Customer`

If `Service` is not set to KeywordMatch, don’t set this parameter.

**Type**
picklist


### Standard Objects ConvIntelligenceSignalSubRule

**Field** **Details**

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

Required. Salesforce- or partner-provided intelligence source.

For Salesforce-provided intelligence sources, set this parameter to `KeywordMatch` .

For partner-provided intelligence sources, possible values are:

**•** `AmazonConnectContactLens`

If none of the options apply to you, contact your Salesforce representative for the service
name.

### ConvIntelligenceSignalSubRule

Represents a condition (subrule) within a conversation intelligence signal rule. This object is available in API version 62.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

This type requires an add-on license for Salesforce Voice for Amazon Connect, Salesforce Voice for Partner Telephony with Amazon
Connect, Salesforce Voice for Partner Telephony, or Digital Engagement.

Fields

**Field** **Details**

```
ConvIntelligenceSignalRuleId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Unique ID of the conversation intelligence signal rule. This field is a relationship field.

**Relationship Name**
ConvIntelligenceSignalRule

**Relationship Type**
Master-detail

**Refers To**
ConvIntelligenceSignalRule (the master object)


Standard Objects ConvIntelligenceSignalSubRule

**Field** **Details**

```
OperandValue

Operator

Order

Type

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Value of the signal type used to determine if the rule condition is met. For example,
escalate_level_1.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Filter logic operator used to determine if the rule condition is met. Possible values are:

**•** `Equals`

**•** `GreaterThan`

**•** `LessThan`

**•** `NotEquals`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Order the condition appears in relation to the other conditions in the list, with zero (0) being
the first condition listed. If `Type` is set to Keyword, the maximum value is 24. For all other
`Type` values, the maximum value is 4. This value is used when applying filter logic to the
rule.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

Type of conversation intelligence signal used by the rule to determine whether to trigger
an action. This value depends on the ConvIntelligenceSignalRule.ConversationChannelId
and ConvIntelligenceSignalRule.Service values.

If `Service` is set to KeywordMatch, possible values are:

**•** `Keyword` –A word or group of words spoken or typed.

If `Service` is set to AmazonConnectContactLens, possible values are:


### Standard Objects ConvMessageSendRequest

**Field** **Details**

**•** `Category` –Category name defined in your telephony system.

If `Service` is set to another value, contact your Salesforce representative for the
conversation intelligence signal types available for your intelligence source.

### ConvMessageSendRequest

Represents a request to send a template-based messaging component to a series of messaging users in an enhanced messaging channel
or Messaging for In-App. This object is available in API version 60.0 and later.

Supported Calls

`describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`

Special Access Rules

Messaging and its associated objects are available only in Enterprise, Unlimited, and Developer Editions for Service Cloud or Sales Cloud
with the Digital Engagement add-on license.

Fields

**Field** **Details**

```
AllowExistingSessionStatus

CommSubscriptionId

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Indicates whether the message can be sent only at certain times.

Possible values are:

**•** `Any` —Send the message regardless of whether the messaging user is engaged in an
active messaging session with the business.

**•** `Closed` —Send the message unless the messaging user is engaged in a messaging
session with a status other than Error or Ended, in which case it’s never sent.

**•** `NonActive` —Send the message unless the messaging user is engaged in a messaging
session with a status of Active, in which case it’s never sent.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ConvMessageSendRequest

**Field** **Details**

**Description**
The ID of the related communication subscription, if applicable. This field is a relationship
field that refers to CommSubscription.

```
CompletedDate

FailedMessageCount

FailedMessageErrorReasons

FailedMessageIdentifiers

FailedMeuPlatformKeys

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when the request completes and all messages associated with the request
are sent or failed to be sent.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The number of messages that failed to be delivered to a messaging user. For example, if a
flow sends the message to 50 messaging users and 4 don’t receive the message, this value
is 4.

**Type**
textarea

**Properties**
Nillable

**Description**
The error reason for each of the failed messages. For example, if 4 messages fail to send, this
field shows the error reason for each failed message.

**Type**
textarea

**Properties**
Nillable

**Description**
The IDs of the messages that failed to send. For example, if 4 messages fail to send, this field
shows 4 message IDs.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort


Standard Objects ConvMessageSendRequest

**Field** **Details**

**Description**
A list of platform keys for messaging end users with messages that failed to send. Available
in API version 65.0 and later.

```
InProgressMessageCount

InProgressMessageIdentifiers

InProgressMessagingEndUserIds

InProgressMessagingSessionIds

InProgressMeuPlatformKeys

```

**Type**
int

**Properties**
Defaulted on Create, Filter, Group, Sort

**Description**
The number of messages in the process of being sent.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
A list of IDs of the messages being sent.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
A list of IDs of messaging end users with messages that are being sent. Available in API
version 65.0 and later.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
A list of IDs of messaging sessions with messages that are being sent. Available in API version
65.0 and later.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
A list of platform keys for messaging end users with messages that are being sent. Available
in API version 65.0 and later.


Standard Objects ConvMessageSendRequest

**Field** **Details**

```
MessageDefinition

MessageDefinitionParameters

Name

PendingMessageCount

PendingMessageEndUserIds

PendingMeuPlatformKeys

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The name of the messaging component being sent. Only active messaging components
can be sent.

**Type**
textarea

**Properties**
Nillable

**Description**
A list of parameters used to dynamically construct the message that is being sent. Available
in API version 65.0 and later.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated ID for the request that uses the format MSJ-{00000000}.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of messages that haven’t yet been sent.

**Type**
textarea

**Properties**
Nillable

**Description**
A list of IDs of the messaging end users with pending messages. Available in API version 65.0
and later.

**Type**
textarea

**Properties**
Nillable


Standard Objects ConvMessageSendRequest

**Field** **Details**

**Description**
A list of platform keys of the messaging end users with pending messages. Available in API
version 65.0 and later.

```
PendingMessageIdentifiers

RequestConsentType

RequestStatus

RequestType

```

**Type**
textarea

**Properties**
Nillable

**Description**
A list of IDs of the pending messages.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates whether the flow applies the consent settings of the messaging end user or the
communication subscription.

Possible values are:

**•** `CommunicationSubscription`

**•** `MessagingEndUser`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the request.

Possible values are:

**•** `Completed`

**•** `Pending`

**•** `In Progress` —The system is actively trying to send the message. If a message can’t
be sent, the RequestStatus returns to Pending and sending is tried again later.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of request.

Possible values are:


Standard Objects ConvMessageSendRequest

**Field** **Details**

**•** `SendNotificationMessages`

```
SessionLongevityPreference

ShouldEnforceChannelConsent

SuccessMessageCount

SuccessMessageIdentifiers

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates whether to end the session after the message is sent.

Possible values are:

**•** `KeepSessionOpen` —After the flow sends the message, keep the messaging session
in a New state. If the end user doesn’t respond within 48 hours, the session ends. Use
this option if you expect customers to respond to automated messages and want service
reps to see their response in context.

**•** `EndSession` —After the flow sends the message, end the messaging session. If the
customer responds, a new messaging session is created and routed to your support
team.

**•** `KeepSessionOpenOrAppend` —If there’s an existing session with the messaging
end user in the New state, use that session to send the message. Otherwise, follow the
behavior documented for the `KeepSessionOpen` option. Available in API version
65.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the existing Messaging channel consent preferences are applied when
determining who receives the message. Setting this value to `true` is the most common
approach. The default value, `false`, allows you to add custom consent logic—for example,
to customize a flow to send the message to both implicitly opted-in users and explicitly
opted-in users.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The number of messages that were successfully sent to messaging users. Delivery can occur
much later than sending, depending on factors such as the connectivity status of the recipient.
Delivery is reflected in the messaging session transcript.

**Type**
textarea


### Standard Objects ConversationVendorInfo

**Field** **Details**

**Properties**
Nillable

**Description**
A list of IDs of the messages that were sent.

```
SuccessMeuPlatformKeys

TotalMessageCount

```

Usage

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
A list of platform keys for messaging end users with messages that were sent. Available in
API version 65.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of messages that the related flow attempted to send.

This field is a calculated field.

A ConvMessageSendRequest can be generated by a flow, Apex code, or REST API call that invokes the sendConversationMessages
invocable action. Use the ConvMessageSendRequest object to query messages sent by the sendConversationMessages invocable action.

### ConversationVendorInfo

This setup object connects the partner vendor system to the Service Cloud feature. For example, for Salesforce Voice with Telephony
Providers, this object contains information about the partner telephony or Contact Center as a Service (CCaaS) partner system. For Bring
Your Own Channel for Messaging this object contains information about the partner messaging system, and for Bring Your Own Channel
for CCaaS, this object contains information about the CCaaS partner system. This object is available in API version 52.0 and later.

Note: Service Cloud Voice is now Salesforce Voice. You may see references to Service Cloud Voice in Salesforce applications and
documentation.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects ConversationVendorInfo

Special Access Rules

This object requires an add-on license for Salesforce Voice for Partner Telephony or Digital Engagement.

Fields

The fields in the ConversationVendorInfo object apply to all Service Cloud features unless otherwise stated in the field description. For
example, if a field applies to just one Salesforce Voice telephony model setup or is applied differently by different partner systems, this
is stated in the field description.


Standard Objects ConversationVendorInfo


Standard Objects ConversationVendorInfo


Standard Objects ConversationVendorInfo


Standard Objects ConversationVendorInfo


Standard Objects ConversationVendorInfo


Standard Objects ConversationVendorInfo


Standard Objects ConversationVendorInfo


Standard Objects ConversationVendorInfo


Standard Objects ConversationVendorInfo


### Standard Objects CorsWhitelistEntry

### CorsWhitelistEntry

Represents an entry in the cross-origin resource sharing (CORS) allowlist. Origins included in the allowlist can request REST resources
from that Salesforce org.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

Supported Calls

`create()`, `delete()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects CorsWhitelistEntry

Fields

**Field Name** **Details**

```
DeveloperName

Language

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the record in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
This field is automatically generated but you can supply your own value if you create the
record using the API.

Note: When creating large sets of data, always specify a unique `DeveloperName`
for each record. If no `DeveloperName` is specified, performance may slow while
Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

This picklist contains the following fully-supported languages:

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


Standard Objects CorsWhitelistEntry

**Field Name** **Details**

**•** Spanish (Mexico): `es_MX` Spanish (Mexico) defaults to Spanish for customer-defined
translations.

**•** Swedish: `sv`

**•** Thai: `th` The Salesforce user interface is fully translated to Thai, but Help is in English.

```
MasterLabel

NamespacePrefix

UrlPattern

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Primary label for the CORS allowlist entry.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
For managed packages, this field is the namespace prefix assigned to the package. For
unmanaged packages, this field is blank.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The origin URL pattern must include the HTTPS protocol (unless you’re using your localhost)
and a domain name, and can include a port. The wildcard character (*) is supported and
must be in front of a second-level domain name. For example,
`https://*.example.com` adds all subdomains of `example.com` to the allowlist.

The origin URL pattern can be an IP address. But an IP address and a domain that resolve to
the same address aren’t the same origin, and you must add them to the CORS allowlist as
separate entries.

Google Chrome [™] and Mozilla [®] Firefox [®] browser extensions are also allowed as resources in
API version 53 and later. Chrome extensions must use the prefix `chrome-extension://`
and 32 characters without digits or capital letters, for example
`chrome-extension://abdkkegmcbiomijcbdaodaflgehfffed` . Firefox
extensions must use the prefix `moz-extension://` and an 8-4-4-4-12 format of small
alphanumeric characters, for example
`moz-extension://1234ab56-78c9-1df2-3efg-4567891hi1j2` .


### Standard Objects Coupon

Usage

Cross-Origin Resource Sharing (CORS) allows web browsers to request resources from other origins. For example, using CORS, the
JavaScript for a web application at `https://www.example.com` can request a resource from
`https://www.salesforce.com` . To allow access to supported Salesforce APIs, Apex REST resources, and Lightning Out from
JavaScript code in a web browser, add the requesting origin to your Salesforce CORS allowlist.

If a browser that supports CORS makes a request to an origin in the Salesforce CORS allowlist, Salesforce returns the origin in the
`Access-Control-Allow-Origin` HTTP header, along with any additional CORS HTTP headers. If the origin isn’t included in
the allowlist, Salesforce returns HTTP status code 403.

Important: CORS doesn’t support requests for unauthenticated resources, including OAuth endpoints. You must pass an OAuth
token with requests that require it.

[CORS is a W3C recommendation to enable browsers to request resources from origins other than their own.](http://www.w3.org/TR/cors/)

### Coupon

A coupon associated with a promotion. This object is available in API version 54.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

The Coupon object is available only if the B2B Commerce license is enabled.

Fields

**Field** **Details**

### `CouponCode`

```
CurrencyIsoCode

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
### Coupon code for the coupon. A buyer can use the coupon code to qualify for a promotion.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
any currency allowed by the organization.


Standard Objects Coupon

**Field** **Details**

```
Description

EndDateTime

LastReferencedDate

LastViewedDate

Name

OwnerId

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the coupon.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The end date and time when the coupon is no longer active.

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
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view ( `LastReferencedDate` ) but
not viewed it.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the coupon.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects Coupon

**Field** **Details**

**Description**
The ID of the owner of this coupon.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
PromotionId

RedemptionLimitAllBuyers

RedemptionLimitPerBuyer

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the promotion associated with the coupon.

This is a relationship field.

**Relationship Name**
Promotion

**Relationship Type**
Lookup

**Refers To**
Promotion

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of times this coupon can be used in total. This field is available in API version 61.0
and later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of times this coupon can be used per customer. This field is available in API version
61.0 and later.


### Standard Objects CouponCodeRedemption

**Field** **Details**

```
StartDateTime

Status

```

Associated Objects

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The start date and time when the coupon is active.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Status of the coupon.

Possible values are:

**•** `Active`

**•** `Inactive`

The default value is `Inactive`

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CouponChangeEvent on page 68 (API version 62.0)**
Change events are available for the object.

### CouponCodeRedemption

Tracks each coupon code redemption. This object is available in API version 58.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object is available through the B2B Commerce license. To access this object, the Promotions Coupon Redemption Limit user
permission must be assigned.


Standard Objects CouponCodeRedemption

Fields

**Field** **Details**

```
Buyer

CouponId

Name

OwnerId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Information about the buyer. Can be any buyer-specific information.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the redeemed coupon.

This field is a relationship field.

**Relationship Name**
Coupon

**Relationship Type**
Lookup

**Refers To**
Coupon

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Salesforce generated coupon code, such as CCR-000000002. Can’t be edited.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who created the coupon code redemption.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup


### Standard Objects CreditMemo

**Field** **Details**

**Refers To**
Group, User

```
Transaction

### CreditMemo

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort

**Description**
ID of the transaction where the coupon code was redeemed. Must be a valid cart ID.

Represents a document that is used to reduce the amount that a buyer owes a seller under the terms of an earlier invoice. This object
is available in API version 48.0 and later.

A credit memo always decreases the balance of an invoice. Users can apply positive credit memos to positive invoices, for example, a
$10 credit memo reduces the balance of a $100 invoice line to $90.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,

```
update()

```

Special Access Rules

This object is available with Order Management, Subscription Management, and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_creditmemo.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_creditmemo.htm)

Fields

**Field** **Details**

```
AppType

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Read-only field that indicates which Salesforce application generated the credit memo.

Possible values are:

**•** `Commerce Cloud`


Standard Objects CreditMemo

**Field** **Details**

**•** `Revenue Cloud`

This field is available in API versions 54.0 to 55.0

```
Balance

BillToContactId

BillingAccountId

CreationMode

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of the credit memo that's available for allocation.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Inherited from the account’s Bill to Account field.

This field is a relationship field.

**Relationship Name**
BillToContact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
The customer account associated with this credit memo.

This field is a relationship field.

**Relationship Name**
BillingAccount

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
picklist


Standard Objects CreditMemo

**Field** **Details**

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates whether the credit memo originated in Salesforce or an external system.

Possible values are:

**•** `External`

**•** `Salesforce`

This field is available in API version 55.0 and later.

```
CreditDate

CreditMemoNumber

CurrencyIsoCode

Description

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date when the credit memo was posted.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
A credit memo numbering alternative to DocumentNumber, containing a number in a format
of your choice. Credit memo numbering is optional.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Three-letter ISO 4217 currency code associated with the credit memo.

The default value is USD.

This field is available in API version 55.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Description of the credit memo.


Standard Objects CreditMemo

**Field** **Details**

```
DocumentNumber

EffectiveDate

ExternalReference

ExternalReferenceDataSource

LastReferencedDate

LastViewedDate

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-generated number for organizing financial documents, for example DOC-0000123.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the effective date of the credit memo. If this field is empty, the credit date is used.
For reporting purposes only; this field drives no other logic.

This field is available in API version 55.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Contains an external system’s ID for the credit memo.

This field is available in API version 55.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Contains the name of the external system that also contains the credit memo.

This field is available in API version 55.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime


Standard Objects CreditMemo

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it's
possible that this record was only referenced ( `LastReferencedDate` ) and not viewed.

```
NetCreditsApplied

OwnerId

ReferenceEntityId

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Represents the total difference between the credit applied to and credit unapplied from the
invoice.

This field is a calculated field. This field is available in API version 55.0 and later.

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
The user who owns a credit memo record.

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
Filter, Group, Nillable, Sort, Update

**Description**
The ID of the record that this credit memo was generated from. For example, the order, order
summary, or invoice.

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceEntity

**Relationship Type**
Lookup


Standard Objects CreditMemo

**Field** **Details**

**Refers To**
Invoice, Order

This field is available in API version 53.0 and later.

```
SourceAction

Status

TotalAdjustmentAmount

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates which Salesforce API created the credit memo.

Possible values are:

**•** `Invoice` —Indicates that Credit Invoice API created the credit memo and applied it
to the invoice.

**•** `NegativeInvoiceLineConversion` —Indicates that Subscription Management
created the credit memo when a negative invoice line was converted.

**•** `Standalone` —Indicates that the Credit Memo API created the credit memo.

**•** `VoidPostedInvoice` —Indicates that the Void a Posted Invoice API created the
credit memo to offset the amount that was voided on the invoice.

This field is available in API version 55.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort, Update

**Description**
Status of the credit memo.

Possible values are:

**•** `Canceled` —Indicates that the credit memo isn't being used and doesn't have a
financial impact.

**•** `Error` —Indicates that the credit memo has an error and doesn’t have a financial impact.

**•** `Pending` —Indicates that the credit memo is being processed but hasn't yet been
posted as a financial transaction.

**•** `Posted` —The credit memo has been recorded as a financial transaction. Most fields
can’t be edited.

**Type**
currency

**Properties**
Filter, Nillable, Sort


Standard Objects CreditMemo

**Field** **Details**

**Description**
Sum of `TotalAmount` values for the credit memo’s adjustment lines.

This field is a calculated field.

```
TotalAdjustmentAmountWithTax

TotalAdjustmentTaxAmount

TotalAmount

TotalAmountWithTax

TotalChargeAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of the credit memo’s adjustment line amounts, including tax.

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of the credit memo’s adjustment line tax. Adjustment line balances are excluded.

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of the credit memo’s `TotalLineAmount` and `TotalAdjustmentAmount` .

This field is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total credit memo amount, with tax included.

This field is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort


Standard Objects CreditMemo

**Field** **Details**

**Description**
Sum of `TotalAmount` values for the credit memo’s charge lines.

This field is a calculated field.

```
TotalChargeAmountWithTax

TotalChargeTaxAmount

TotalCreditAmountApplied

TotalCreditAmountUnapplied

TotalTaxAmount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The sum of the credit memo’s charge line amounts, including tax.

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Credit memo amount that's been applied to invoices.

This field is available in API version 53.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Credit memo amount that's been unapplied from invoices.

This field is available in API version 55.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of `TotalAmount` values for the credit memo’s tax lines.


### Standard Objects CreditMemoAddressGroup

**Field** **Details**

This field is a calculated field.

Associated Objects

This object has the following associated objects. If the API version isn’t specified, the associated objects are available in the same API
versions as this object. Otherwise, they’re available in the specified API version and later.

**CreditMemoFeed on page 55**
Feed tracking is available for the object.

**CreditMemoHistory on page 63**
History is available for tracked fields of the object.

**CreditMemoOwnerSharingRule on page 65**
Sharing rules are available for the object.

**CreditMemoShare on page 67**
Sharing is available for the object.

### CreditMemoAddressGroup

Stores the buyer's address information, which is used to determine the amount of tax to credit to a buyer when a credit memo is issued.
This object is available in API version 55.0 and later.

Supported Calls

`delete(), describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_creditmemoaddressgroup.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_creditmemoaddressgroup.htm)

Fields

**Field** **Details**

```
Address

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
Buyer’s address.


Standard Objects CreditMemoAddressGroup

**Field** **Details**

```
City

Country

CreditMemoAddressGroupNumber

CreditMemoId

CurrencyIsoCode

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Buyer's city.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Buyer's country.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number, such as 0000123, that represents the address group.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the credit memo associated with the address group.

This field is a relationship field.

**Relationship Name**
CreditMemo

**Relationship Type**
Lookup

**Refers To**
CreditMemo

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Three-letter ISO 4217 currency code associated with the credit memo.


Standard Objects CreditMemoAddressGroup

**Field** **Details**

The default value is USD.

```
GeocodeAccuracy

LastReferencedDate

LastViewedDate

Latitude

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The accuracy rating for the geocode of the address group. An accuracy rating contains
information about the location of a latitude and longitude.

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
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this address group.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this address group.

**Type**
double

**Properties**
Filter, Nillable, Sort


### Standard Objects CreditMemoInvApplication

**Field** **Details**

**Description**
Latitude of the buyer’s address.

```
Longitude

PostalCode

State

Street

```

Associated Objects

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Longitude of the buyer’s address.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The buyer’s postal code or ZIP code.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The buyer’s state.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
The buyer’s street number and name.

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CreditMemoAddressGroupHistory on page 63**
History is available for tracked fields of the object.

### CreditMemoInvApplication

Represents an amount applied from a credit memo to an invoice. This object is available in API version 48.0 and later.


Standard Objects CreditMemoInvApplication

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,

```
   update()

```

Special Access Rules

This object is available with Subscription Management and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_creditmemoinvapplication.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_creditmemoinvapplication.htm)

Fields

**Field** **Details**

```
Amount

AppliedDate

AssociatedLineId

```

**Type**
currency

**Properties**
Filter, Sort

**Description**
The amount of the credit memo that was applied to or unapplied from the invoice.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the credit memo was applied. If the credit memo invoice application's type
is `Unapplied`, this value is inherited from the Applied date of the credit memo referenced
in the AssociatedLineId.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
For a credit memo invoice application that represents an unapplied credit memo, this field
shows the original credit memo invoice application.

This field is a relationship field.

**Relationship Name**
AssociatedLine

**Relationship Type**
Lookup


Standard Objects CreditMemoInvApplication

**Field** **Details**

**Refers To**
CreditMemoInvApplication

```
CreditMemoBalance

CreditMemoId

CreditMemoInvoiceNumber

Date

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The balance of a credit memo after a credit memo is applied or unapplied. This field is a
snapshot of the credit memo's balance after the action. It isn't updated after further changes
to the credit memo balance.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The credit memo that was applied or unapplied.

This field is a relationship field.

**Relationship Name**
CreditMemo

**Relationship Type**
Lookup

**Refers To**
CreditMemo

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Number of the invoice to which a credit memo is applied.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date when the credit memo amount was applied to the invoice.


Standard Objects CreditMemoInvApplication

**Field** **Details**

```
Description

EffectiveDate

HasBeenUnapplied

ImpactAmount

InvoiceBalance

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Description of the credit applied to an invoice.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The effective date of the application or unapplication of credit. Users can provide this value
when applying or unapplying the credit memo. This field is optional and provided only for
reporting purposes. It doesn't affect the credit memo invoice application's other fields.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Shows whether this credit memo application has been unapplied from the target invoice.

Possible values are:

**•** `NA`

**•** `No`

**•** `Yes`

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The net adjustment to the invoice's balance after a credit memo is applied or unapplied. If
a credit memo was applied, this value is the negative version of the credit memo invoice
application's `Amount` . If a credit memo was unapplied, this value is the positive version of
the credit memo invoice application's `Amount` .

This field is a calculated field.

**Type**
currency


Standard Objects CreditMemoInvApplication

**Field** **Details**

**Properties**
Filter, Nillable, Sort

**Description**
The balance of the credit memo after a credit memo is applied or unapplied. This field is a
snapshot of the credit memo's balance after the action. It isn't updated after further changes
to the credit memo balance.

```
InvoiceId

Type

UnappliedDate

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the invoice to which credit is applied.

This field is a relationship field.

**Relationship Name**
Invoice

**Relationship Type**
Lookup

**Refers To**
Invoice

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Indicates whether the credit memo line application was generated because of an apply
action (application) or an unapply action (unapplication).

Possible values are:

**•** `Applied`

**•** `Unapplied`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when this application was unapplied from the target invoice.


### Standard Objects CreditMemoLine

Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CreditMemoInvApplicationFeed on page 55**
Feed tracking is available for the object.

**CreditMemoInvApplicationHistory on page 63**
History is available for tracked fields of the object.

### CreditMemoLine

Represents product, service, adjustment, or tax line items that were included in a credit memo. This object is available in API version 48.0
and later.

Supported Calls

`describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`, `search()`,

```
   update()

```

Special Access Rules

This object is available with Order Management, Subscription Management, and Billing (Revenue Cloud).

[For information about this object that's available with Billing (Revenue Cloud), including its special access rules, see the Revenue Cloud](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_creditmemoline.htm)
[Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.revenue_lifecycle_management_dev_guide.meta/revenue_lifecycle_management_dev_guide/sforce_api_objects_creditmemoline.htm)

Fields

**Field** **Details**

```
AdjustmentAmount

AdjustmentAmountWithTax

```

**Type**
currency

**Properties**
Filter, Nillable, Sort, Update

**Description**
Amount of this credit memo line item if its type is Adjustment.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of the adjustment amount and the adjustment tax amount.

This field is available in API version 49.0 and later. This field is available when Subscription
Management is enabled.


Standard Objects CreditMemoLine

**Field** **Details**

```
AdjustmentTaxAmount

BillingAddressId

ChargeAmount

ChargeAmountWithTax

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of the tax related to the adjustment amount.

This field is available in API version 55.0 and later. This field is available when Subscription
Management is enabled.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the billing address related to this credit memo line.

This field is a relationship field. This field is available in API version 55.0 and later. This field is
available when Subscription Management is enabled.

**Relationship Name**
BillingAddress

**Relationship Type**
Lookup

**Refers To**
CreditMemoAddressGroup

**Type**
currency

**Properties**
Filter, Nillable, Sort, Update

**Description**
Amount of this credit memo line item if its type is Charge.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Sum of the adjustment amount and the adjustment tax amount.

This field is available in API version 55.0 and later. This field is available when Subscription
Management is enabled.


Standard Objects CreditMemoLine

**Field** **Details**

```
ChargeTaxAmount

CreditMemoId

CurrencyIsoCode

Description

EndDate

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of the tax related to the charge amount.

This field is available in API version 55.0 and later. This field is available when Subscription
Management is enabled.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the parent credit memo.

This field is a relationship field.

**Relationship Name**
CreditMemo

**Relationship Type**
Lookup

**Refers To**
CreditMemo

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Three-letter ISO 4217 currency code associated with the credit memo line.

The default value is USD.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Description of the credit memo line.

**Type**
date


Standard Objects CreditMemoLine

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
For credit memos made from a time-based service, the end date of the line item being
credited.

```
LineAmount

Name

Product2Id

ReferenceEntityItemId

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of the credit memo line.

This field is a calculated field. This field is available in API version 49.0 and later.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort, Update

**Description**
Name of the credit memo line.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The product or service being credited in the credit memo line.

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
Filter, Group, Nillable, Sort, Update

**Description**
The order product or invoice line corresponding to this credit memo line.


Standard Objects CreditMemoLine

**Field** **Details**

This field is a polymorphic relationship field. This field is available in API version 53.0 and
later.

**Relationship Name**
ReferenceEntityItem

**Relationship Type**
Lookup

**Refers To**
OrderItemSummary, OrderProduct, InvoiceLine

```
ReferenceEntityItemType

ReferenceEntityItemTypeCode

RelatedLineId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of transaction that generated the credit memo line.

Possible values are:

**•** `DeliveryCharge`

**•** `OrderProduct`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of object that generated the credit memo line.

Possible values are:

**•** `Charge`

**•** `Product`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The credit memo line related to this line item.

This field is a relationship field.

**Relationship Name**
RelatedLine

**Relationship Type**
Lookup


Standard Objects CreditMemoLine

**Field** **Details**

**Refers To**
CreditMemoLine

```
ShippingAddressId

StartDate

Status

TaxAmount

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the shipping address.

This field is a relationship field. This field is available in API version 55.0 and later. This field is
available when Subscription Management is enabled.

**Relationship Name**
ShippingAddress

**Relationship Type**
Lookup

**Refers To**
CreditMemoAddressGroup

**Type**
date

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
For credit memo lines generated from a time-based service, the first date of the billing for
the service.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
State of the credit memo line. Inherited from the credit memo.

**Type**
currency

**Properties**
Filter, Nillable, Sort, Update

**Description**
Total tax for the credit memo.


Standard Objects CreditMemoLine

**Field** **Details**

```
TaxCode

TaxDocumentNumber

TaxEffectiveDate

TaxName

TaxRate

TotalAmount

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The code used to calculate the tax rate for the invoice line.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The document number that tracks taxes calculated for this credit memo line.

This field is available in API version 55.0 and later. This field is available when Subscription
Management is enabled.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The date used to calculate the credit memo line’s `TaxAmount` .

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
User-defined name for applied tax.

**Type**
percent

**Properties**
Filter, Nillable, Sort, Update

**Description**
Percentage value used for calculating tax.

**Type**
currency

**Properties**
Filter, Nillable, Sort


Standard Objects CreditMemoLine

**Field** **Details**

**Description**
The total amount of the credit memo line before any applicable tax.

```
TotalAmountWithTax

TaxStatus

TaxTransactionNumber

TaxTreatmentId

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of tax for this credit memo line, with tax included. Sum of TotalAmount and
TaxAmount.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Tracks whether the taxes were calculated for this credit memo line.

Possible values are:

**•** `Complete`

**•** `Error`

**•** `None`

The default value is None. This field is available in API version 55.0 and later. This field is
available when Subscription Management is enabled.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Tracks the transaction number of the tax calculated for this credit memo line. This field is
available in API version 55.0 and later. This field is available when Subscription Management
is enabled.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the tax treatment for the credit memo line.

This field is a relationship field. This field is available in API version 55.0 and later. This field is
available when Subscription Management is enabled.


### Standard Objects Crisis

**Field** **Details**

**Relationship Name**
TaxTreatment

**Relationship Type**
Lookup

**Refers To**
TaxTreatment

```
 Type

```

Associated Objects

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of transaction for the invoice line.

Possible values are:

**•** `Adjustment`

**•** `Charge`

**•** `Tax`

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CreditMemoLineFeed on page 55**
Feed tracking is available for the object.

**CreditMemoLineHistory on page 63**
History is available for tracked fields of the object.

### Crisis

Represents a major crisis event that affects an Employee in an InternalOrganizationUnit. This object is available in API version 48.0 and
later. In API version 49.0 and later, this object supports reports, criteria-based sharing rules, and history tracking, plus you can exclude
individual fields from custom page layouts.

Work.com uses this object to track and describe crisis situations.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`


Standard Objects Crisis

Special Access Rules

To access this object, you must be assigned a Workplace Command Center permission set license and the Provides access to Workplace
Command Center features system permission.

Fields

**Field** **Details**

```
CrisisType

Description

EndDate

LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The type or category of crisis.

Possible values are:

**•** `Economic Crisis`

**•** `Natural Disaster`

**•** `Pandemic`

**•** `War`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The crisis description.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date the crisis ended.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.


Standard Objects Crisis

**Field** **Details**

```
LastViewedDate

Name

OwnerId

StartDate

```

Associated Objects

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
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. The crisis record name.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who currently owns this record. Default value is the user logged in to the
API to perform the create operation.

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The date the crisis started.

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**CrisisHistory (API version 49.0)**
History is available for tracked fields of the object.

**CrisisOwnerSharingRule**

Sharing rules are available for the object.


### Standard Objects CronJobDetail

**CrisisShare (API version 49.0)**
Sharing is available for the object.

SEE ALSO:

_[Workplace Command Center for Work.com Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.262.0.ajax.meta/workdotcom_dev_guide/wdc_cc_overview.htm)_ : Extend Work.com with Custom Solutions

### CronJobDetail

Contains details about the associated scheduled job, such as the job’s name and type. This object is available in API version 29.0 and
later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
JobType

Name

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of the associated scheduled job. The following are the available job types. Use the
job type value when querying for a specific job type.

**•** `1` —Data Export

**•** `3` —Dashboard Refresh

**•** `4` —Reporting Snapshot

**•** `6` —Scheduled Flow

**•** `7` —Scheduled Apex

**•** `8` —Report Run

**•** `9` —Batch Job

**•** `A` —Reporting Notification

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the associated scheduled job.


### Standard Objects CronTrigger

Usage

Use this object to query additional information about a scheduled job, such as the job’s name and type.

### CronTrigger

Contains schedule information for a scheduled job. CronTrigger is similar to a cron job on UNIX systems. This object is available in API
version 17.0 and later.

Supported Calls

`describeSObjects()`, `query()`, `retrieve()`

Fields

**Field** **Details**

```
CronExpression

CronJobDetailId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The cron expression used to initiate the schedule.

Syntax:

```
  Seconds Minutes Hours Day_of_month Month Day_of_week

  Optional_year

```

See `[schedule(jobName, cronExpression, schedulableClass)](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexref/apex_methods_system_system.htm)` in the
_Apex Reference Guide_ .

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the CronJobDetail record containing more details about this scheduled job.

This is a relationship field.

**Relationship Name**
CronJobDetail

**Relationship Type**
Lookup

**Refers To**
CronJobDetail


Standard Objects CronTrigger

**Field** **Details**

```
EndTime

NextFireTime

OwnerId

PreviousFireTime

StartTime

State

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the job either finished or will finish.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The next date and time the job is scheduled to run. `null` if the job is not scheduled to run
again.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Owner of the job.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The most recent date and time the job ran. `null` if the job has not run before current local
time.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the most recent iteration of the scheduled job started.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


### Standard Objects CryptoProdCatgWalletGroup

**Field** **Details**

**Description**
The current state of the job. The job state is managed by the system. Possible values are:

**•** `WAITING` —The job is waiting for execution.

**•** `ACQUIRED` —The job has been picked up by the system and is about to execute.

**•** `EXECUTING` —The job is executing.

**•** `COMPLETE` —The trigger has fired and is not scheduled to fire again.

**•** `ERROR` —The trigger definition has an error.

**•** `DELETED` —The job has been deleted.

**•** `PAUSED` —A job can have this state during patch and major releases. After the release
has finished, the job state is automatically set to `WAITING` or another state.

**•** `BLOCKED` —Execution of a second instance of the job is attempted while one instance
is running. This state lasts until the first job instance is completed.

**•** `PAUSED_BLOCKED` —A job has this state due to a release occurring. When the release
has finished and no other instance of the job is running, the job’s status is set to another
state.

```
TimesTriggered

TimeZoneSidKey

```

Usage

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times this job has been triggered.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Returns the timezone ID. For example, `America/Los_Angeles` .

Use this object to query scheduled jobs in your organization.

### CryptoProdCatgWalletGroup

Specifies if CryptoWalletGroup is in the allowlist or airdrop for the ProductCategory. A custom object between ProductCategory and
CryptoWalletGroup adding the CryptoWalletGroup to allowlist or airdrop. This object is available in API version 58.0 and later.


Standard Objects CryptoProdCatgWalletGroup

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

This object has read, create, update, delete, modify all, and view all access.

Fields

**Field** **Details**

```
CryptoWalletGroupId

LastReferencedDate

LastViewedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The CryptoWalletGroup ID.

This field is a relationship field.

**Relationship Name**
CryptoWalletGroup

**Relationship Type**
Lookup

**Refers To**
CryptoWalletGroup

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example,
through a list view or related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
and `LastReferenceDate` is not null, the user accessed this record or list view indirectly.


Standard Objects CryptoProdCatgWalletGroup

**Field** **Details**

```
Name

ProductCategoryId

Status

Type

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the record.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the category.

This field is a relationship field.

**Relationship Name**
ProductCategory

**Relationship Type**
Lookup

**Refers To**
ProductCategory

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies if CryptoProdCatgWalletGroup is active and functional, or inactive and disabled.

Possible values are:

**•** `Active`

**•** `Inactive`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Determines whether the list of wallets is for minting allowlist or for executing an airdrop.

Possible values are:

**•** `Airdrop`

**•** `Allowlist`


### Standard Objects CspTrustedSite CspTrustedSite

Represents a trusted URL. For each CspTrustedSite, you can specify Content Security Policy (CSP) directives and permissions policy
directives. Each CSP directive allows Lightning components, third-party APIs, and WebSocket connections to access a resource type
from the trusted URL. If the Permissions-Policy HTTP header is enabled, each permissions policy directive grants the trusted URL access
to a browser feature. In API version 58.0 and earlier, CspTrustedSite included only CSP directives and was referred to as CSP Trusted Sites
in Salesforce Setup. Available in API version 39.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CanAccessCamera

CanAccessMicrophone

Context

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this CspTrustedSite can access the user’s camera. The default value is
`false` .

This field takes effect only when the `enablePermissionsPolicy` field equals `true`
and the `grantCameraAccess` field equals `TrustedUrls` in the SecuritySettings
metadata API type.

This field is available in API version 59.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this CspTrustedSite can access the user’s microphone. The default value
is `false` .

This field takes effect only when the `enablePermissionsPolicy` field equals `true`
and the `grantMicrophoneAccess` field is `TrustedUrls` in the SecuritySettings
metadata API type.

This field is available in API version 59.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


Standard Objects CspTrustedSite

**Field** **Details**

**Description**
Declares the scope of the CSP directives for this trusted URL.

Possible values are:

**•** `All` —Apply the CSP directives to all supported context types.

**•** `Communities` —Apply the CSP directives to Experience Builder sites only.

**•** `FieldServiceMobileExtension` —Apply the CSP directives to the Field Service
Mobile Extensions only.

**•** `LEX` —Apply the CSP directives to Lightning Experience only.

**•** `LightningOut` —Reserved for future use. Available in API version 64.0 and later

**•** `VisualForce` —Apply the CSP directives to custom Visualforce pages only. This value
is available in API version 55.0 and later.

For custom Visualforce pages, content is restricted to trusted URLs only if the page’s
`cspHeader` attribute is set to `true` .

This field is available in API version 44.0 and later.

```
Description

DeveloperName

EndpointUrl

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the trusted URL. Limit: 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The developer name of the trusted URL.

Only users with View DeveloperName OR View Setup and Configuration permission can
view, group, sort, and filter this field.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The URL for this CspTrustedSite.

This field must include a domain name and can include a port. For example,
`https://example.com` or `https://example.com:8080` .


Standard Objects CspTrustedSite

**Field** **Details**

To reduce repetition, you can use the wildcard character `*` (asterisk). For example,
`*.example.com` . For a third-party API, the URL must begin with https://. For example,
`https://example.com` . For a WebSocket connection, the URL must begin with wss://.
For example, `wss://example.com` .

Otherwise, the URL cannot be malformed. Examples of malformed URLs that fail a syntax
check are `malformed^url.example.com`, and
`https://{subdomain}.example.com` .

Before February 2025, it was possible to save a malformed URL. Malformed URLs are excluded
from generated CSP HTTP headers. To keep your Trusted URLs list accurate, remove any
malformed entries. You can use an Apex class to find all malformed URLs. See the knowledge
[article, Identify Malformed Trusted URLs.](https://help.salesforce.com/s/articleView?id=005317938&type=1&language=en_US)

To add a URL based on parameters, build the URL before you update the `EndpointUrl`
field.

```
IsActive

IsApplicableToConnectSrc

IsApplicableToFontSrc

IsApplicableToFrameSrc

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this CspTrustedSite is active.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether Lightning components, third-party APIs, and WebSocket connections can
load URLs using script interfaces from this trusted URL.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether Lightning components, third-party APIs, and WebSocket connections can
load fonts from this trusted URL.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


Standard Objects CspTrustedSite

**Field** **Details**

**Description**
Indicates whether Lightning components, third-party APIs, and WebSocket connections can
load resources contained in `<iframe>` elements from this trusted URL.

```
IsApplicableToImgSrc

IsApplicableToMediaSrc

IsApplicableToStyleSrc

Language

MasterLabel

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether Lightning components, third-party APIs, and WebSocket connections can
load images from this trusted URL.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether Lightning components, third-party APIs, and WebSocket connections can
load audio and video from this trusted URL.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether Lightning components can load style sheets from this trusted URL.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language for the trusted URL.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Master label for this trusted URL.


### Standard Objects CspViolationEventLog

**Field** **Details**

```
NamespacePrefix

```

Usage

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Namespace prefix for this trusted URL.

For each CSPTrustedSite, at least one field starting with `grantAccess` or `isApplicableTo` must be set to `true` .

In API versions 50.0 to 58.0, if all `isApplicable` fields are `false`, the `isApplicableToImgSrc` field is set to `true` . In API
version 49.0 and earlier, if all `isApplicable` fields are `false`, those fields all default to `true` .

To ensure smooth integration across Salesforce products, Salesforce includes URLs in each of the CSP directives that correspond to the
`isApplicable` fields, even though those URLs aren’t defined as CspTrustedSite components. Salesforce regularly updates those
URLs based on the latest requirements.

### CspViolationEventLog

CSP violation events capture details about blocked resource requests from Lightning Experience pages based on your content security
policy (CSP). This object is available in API version 63.0 and later.

This event is free for all customers with a 24-hour data retention period. The CSP violation event is available in the API but not in the
Event Monitoring Analytics app.

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
BlockedUri

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


Standard Objects CspViolationEventLog

**Field** **Details**

**Description**
The full string of the blocked resource. If the call to the blocked resource used a URL,
`BLOCKED_URI` is the full URL. Or,for violations with a `DIRECTIVE` of `script-src`
directives, `inline` or `eval` .

**Examples**

**•** https://www.example.com/images/picture.png

**•** file://host1:0002/media/video.mp4

**•** inline

```
BlockedUriDomain

ColumnNumber

Context

Directive

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If `BLOCKED_URI` is a URL, the domain for that URL. To allow resources to be loaded from
the `BLOCKED_URI`, `BLOCKED_URI_DOMAIN` is the `endpointUrl` value to add or
[update in the CspTrustedSite Metadata API.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_csptrustedsite.htm)

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The column number in the document or worker script at which the violation occurred. This
value is relevant only when `DIRECTIVE` is `script-src` .

For those violations, use this value with `LINE_NUMBER` to identify the location of the
violation.

**Example**

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The content security policy (CSP) context for the request. The CSP context controls which
[pages can load content from a CspTrustedSite.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_csptrustedsite.htm)

CSP violation events capture details about blocked resource requests from only Lightning
Experience pages, this value is always `Lightning` .

**Type**
string


Standard Objects CspViolationEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

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

```
Disposition

LineNumber

RequestIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The CSP violation handling instruction for the user agent at the time of the violation.

**Possible Values**

**•** `enforce` —Enforce the policy violation. For violations with this `DISPOSITION`, the
resource request was blocked.

**•** `report` —Report the policy violation. For violations with this `DISPOSITION`, the
resource request wasn’t blocked, but the violation was reported.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The line number in the document or worker script at which the violation occurred. This value
is relevant only when `DIRECTIVE` is `script-src` . For those violations, use this value
with `COLUMN_NUMBER` to identify the location of the violation.

**Example**

**Type**
string


Standard Objects CspViolationEventLog

**Field** **Details**

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a single transaction. A transaction can contain one or more events. Each
event in a given transaction has the same REQUEST_ID.

```
ResourceSample

Source

SourceFile

Timestamp

UniqueIdentifier

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A sample of the resource that caused the violation, usually the first 40 characters, or the
empty string.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The page where this CSP violation originated. For example, if your CSP policy prevented an
image from loading on a Visualforce page, `SOURCE` contains the URL of that page.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URL of the script in which the violation occurred. If the violation didn’t occur in a script,
`SOURCE_FILE` is null.

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


### Standard Objects CurrencyType

**Field** **Details**

**Description**
A string identifier for the CSP violation.

Usage

Only one CSP violation event log file is available at a time. When the daily incremental event log file is generated during the daily
background process, the new file replaces the existing file.

If the event log file doesn’t exist, either the log generation process hasn’t run yet or there’s no violation data to report for that 24-hour
window. The event log file is generated only when at least one violation occurred for the day.

To collect CSP violation logs for multiple days, schedule a daily query of the CSP Violation event type via REST API. For example, you can
configure a cron job in Unix or a scheduled task in Windows to run the query.

### CurrencyType

Represents the currencies used by an organization for which the multicurrency feature is enabled.

Supported Calls

`create()`, `describeSObjects()`, `getUpdated()`, `query()`, `retrieve()`, `search()`, `update()`

Special Access Rules

**•** This object is not available in single-currency organizations.

**•** You need the “Customize Application” permission to edit this object.

**•** Your client application can't delete this object.

Fields

**Field** **Details**

```
ConversionRate

DecimalPlaces

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


Standard Objects CurrencyType

**Field** **Details**

**Description**
Required. For this currency, specifies the number of digits to the right of the decimal
point, such as zero ( `0` ) for JPY or `2` for USD.

```
IsActive

 IsCorporate

 IsoCode

```

Usage

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

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether this currency type is the corporate currency ( `true` ) or not ( `false` ).
Label is **Corporate Currency** . All other currency conversion rates are applied against
this corporate currency. If a currency is already defined as the corporate currency in
the user interface, it can't be unset. When a non-corporate currency is set to a
corporate currency, the system reconfigures all conversion rates based on the new
corporate currency.

**Type**
picklist

**Properties**
Filter, Restricted picklist

**Description**
Required. ISO code of the currency. Must be one of the valid alphabetic, three-letter
currency ISO codes defined by the ISO 4217 standard, such as `USD`, `GBP`, or `JPY` .
Must be unique within your organization. Label is **Currency ISO Code** . The `CUC`
(Cuban Convertible Peso) picklist value is not available in API version 65.0 and later.

This object is for multicurrency organizations only. Use this object to define the currencies your organization uses.


### Standard Objects CustExpIntlTransfSetup

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

Fields

**Field** **Details**

```
DataSourceChannelName

DataSourceChannelType

IsDataProcessingPaused

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


Standard Objects CustExpIntlTransfSetup

**Field** **Details**

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether data processing for the channel is temporarily paused ( `true` ). Use this
field to control channel operations without deactivating the channel.

The default value is `false` .

```
IsEnabled

LastReferencedDate

LastViewedDate

Name

ProcessingStartDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the channel is active for processing data ( `true` ).

The default value is `false` .

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when the current user last viewed or modified this record, a record related
to this record, or a list view. If this value is null, the current user has never viewed or modified
a record related to this object.

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


### Standard Objects CustomBrand

**Field** **Details**

**Properties**
Create, Filter, Sort, Update

**Description**
The date to start processing data in the specified communication channel.

### CustomBrand

Represents a custom branding and color scheme. This object is available in API version 28.0 and later.

Supported Calls

`create()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Special Access Rules

This object is available only when your org has digital experiences enabled.

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


### Standard Objects CustomBrandAsset

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


Standard Objects CustomBrandAsset

**Field Name** **Details**

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


Standard Objects CustomBrandAsset

**Field Name** **Details**

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

**•** `MediumLogoAssetId` —Featured topic images. Label is `Medium`
`logo asset image` .

```
AssetSourceId

CustomBrandId

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


### Standard Objects CustomFieldDisplayValue

**Field Name** **Details**

**Description**
ID of the associated CustomBrand .

This is a relationship field.

**Relationship Name**
CustomBrand

**Relationship Type**
Lookup

**Refers To**
CustomBrand

```
ForeignKeyAssetId

TextAsset

```

Usage

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

This field was removed in API version 41.0, and is available in earlier versions for
backward compatibility only. Use `AssetSourceId` instead.

ID of the document used if the value of `AssetCategory` is `PageHeader`,
`PageFooter`, or `LoginLogoImageId` .

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


Standard Objects CustomFieldDisplayValue

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`, `retrieve()`,
`undelete()`, `update()`, `upsert()`

Special Access Rules

CustomFieldDisplayValue is available only if the B2B or D2C Commerce license is enabled.

Fields

**Field** **Details**

```
Color

CurrencyIsoCode

CustomFieldDisplayId

Name

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


### Standard Objects CustomHelpMenuItem

**Field** **Details**

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the custom field display value.

```
PickListApiValue

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The API name of the color variation picklist value, for example, `red_c` .

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


Standard Objects CustomHelpMenuItem

Fields

**Field** **Details**

```
LinkUrl

MasterLabel

ParentId

SortOrder

```

**Type**
url

**Properties**
Create, Filter, Sort, Update

**Description**
Required. The URL for the resource. Specify up to 1,000 characters.

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
CustomHelpMenuSection

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The order of the item within the custom section. Valid values are 1 through 15.


### Standard Objects CustomHelpMenuSection CustomHelpMenuSection

Represents a section of the Lightning Experience help menu that the admin added to display custom, org-specific help resources. This
object is available in API version 44.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Packaging Considerations

Although you can package custom Help Menu section information, the section won't appear in the Help Menu Setup page or the Help
Menu user interface of orgs where the package is installed. Instead, customers must view the data in the CustomHelpMenuItem and
### CustomHelpMenuSection objects and then manually add resources on the Help Menu Setup page.

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


Standard Objects CustomHelpMenuSection

**Field** **Details**

**•** en_US (English)

**•** es (Spanish)

**•** es_MX (Spanish (Mexico))

**•** fi (Finnish)

**•** fr (French)

**•** it (Italian)

**•** ja (Japanese)

**•** ko (Korean)

**•** nl_NL (Dutch)

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


### Standard Objects CustomHttpHeader

**Field** **Details**

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

### CustomHttpHeader

Represents a custom HTTP header that provides context information from Salesforce such as region, org details, or the role of the person
viewing the external object. This object is available in API version 43.0 and later.

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


### Standard Objects CustomMsgChannel

**Field Name** **Details**

**Description**
A formula that resolves to the value for the header. The values in the formula must evaluate
to a string. If the formula resolves to null and an empty string, the header isn’t sent.

```
IsActive

ParentId

```

Usage

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the custom HTTP header is available to use.

**Type**
reference

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

For each OData external data source, define up 10 HTTP headers to request data.

Note: HTTP headers aren’t supported on named credentials.

### CustomMsgChannel

Represents a custom conversation channel and stores event-driven Messaging settings. Custom conversation channels are implemented
for Bring Your Own Channel for Messaging and Bring Your Own Channel for CCaaS Messaging channels. This object is available in API
version 63.0 and later.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`


Standard Objects CustomMsgChannel

Special Access Rules

Access to standard objects requires Salesforce admin privileges or the Customize Application permission.

Fields

**Field** **Details**

```
ChannelDefinitionId

EventCapabilitiesIsInboundAcknowledgementEnabled

EventCapabilitiesIsProgressIndicatorEnabled

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Specifies the ConversationChannelDefinition for the custom channel.

This field is a relationship field.

**Relationship Name**
ChannelDefinition

**Refers To**
ConversationChannelDefinition

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


Standard Objects CustomMsgChannel

**Field** **Details**

```
EventCapabilitiesIsTypingIndicatorDisabled

HasInboundReceipts

HasTypingIndicator

MessagingChannelId

```

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


### Standard Objects CustomNotificationType

**Field** **Details**

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

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

Supported Calls

`create()`, `delete()`, `describeSObjects()`, `query()`, `retrieve()`, `update()`, `upsert()`

Fields

**Field** **Details**

```
CustomNotifTypeName

Description

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


Standard Objects CustomNotificationType

**Field** **Details**

```
Desktop

DeveloperName

IsSlack

Language

MasterLabel

Mobile

```

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


### Standard Objects CustomPermission

**Field** **Details**

**Description**
Indicates whether the mobile delivery channel is enabled ( `true` ) or not ( `false` ). The
default value is `false` .

```
NamespacePrefix

### CustomPermission

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Specifies the namespace of the notification type, if installed with a managed package.

Represents a permission created to control access to a custom process or app, such as sending email. This object is available in API
version 31.0 and later.

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

```

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
A description of the custom permission. Limit: 255 characters.

**Type**
string


Standard Objects CustomPermission

**Field Name** **Details**

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

```
IsLicensed

IsProtected

Language

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
When enabled (true) indicates that the appropriate Salesforce license is required
before accessing the permission. This field is available in API version 50.0 and
later.

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


Standard Objects CustomPermission

**Field Name** **Details**

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

```
MasterLabel

NamespacePrefix

```

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


Standard Objects CustomPermission

**Field Name** **Details**

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace
prefix of the org for all objects that support it, unless an object is in an installed
managed package. In that case, the object has the namespace prefix of the
installed managed package. This field’s value is the namespace prefix of the
Developer Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set
only for objects that are part of an installed managed package. All other
objects have no namespace prefix.

Usage

Use the CustomPermission object to determine users’ access to custom permissions.

For example, to query all permission sets where the Button1 permission is enabled:

```
   SELECT Id, DeveloperName,

   (select Id, Parent.Name, Parent.Profile.Name from SetupEntityAccessItems)

   FROM CustomPermission

   WHERE DeveloperName = 'Button1'

```

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

CustomPermissionDependency

PermissionSet

Profile

SetupEntityAccess


### Standard Objects CustomPermissionDependency CustomPermissionDependency

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

RequiredCustomPermissionId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the custom permission that requires the permission that’s specified in
`RequiredCustomPermissionId` .

This is a relationship field.

**Relationship Name**
### CustomPermission

**Relationship Type**
Lookup

**Refers To**
### CustomPermission

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


### Standard Objects Customer

**Field Name** **Details**

**Relationship Type**
Lookup

**Refers To**
CustomPermission

Usage

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

[For more information about using Apex classes, see the Apex Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.262.0.apexcode.meta/apexcode/apex_dev_guide.htm)

SEE ALSO:

CustomPermission

### Customer

Represents the customer role of an individual with respect to a particular company or organization. This object is available in API version
53.0 and later.

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`


Standard Objects Customer

Fields

**Field** **Details**

```
CustomerStatusType

LastReferencedDate

LastViewedDate

Name

OwnerId

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


### Standard Objects DandBCompany

**Field** **Details**

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

```
PartyId

TotalLifeTimeValue

### DandBCompany

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. Represents the individual object related to this customer record.

This is a relationship field.

**Relationship Name**
Party

**Relationship Type**
Lookup

**Refers To**
Individual

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


Standard Objects DandBCompany

Supported Calls

`create()`, `delete()`, `describeLayout()`, `describeSObjects()`, `getDeleted()`, `getUpdated()`, `query()`,
`retrieve()`, `search()`, `undelete()`, `update()`, `upsert()`

Special Access Rules

Only organizations with Data.com Premium Prospector or Data.com Premium Clean can access this object.

Fields

**Field Name** **Details**

```
Address

City

CompanyCurrencyIsoCode

Country

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


Standard Objects DandBCompany

**Field Name** **Details**

```
CountryAccessCode

CurrencyCode

Description

DomesticUltimateBusinessName

DomesticUltimateDunsNumber

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The required code for international calls. Maximum size is 4 characters.

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


Standard Objects DandBCompany

**Field Name** **Details**

```
DunsNumber

EmployeeQuantityGrowthRate

EmployeesHere

EmployeesHereReliability

EmployeesTotal

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Data Universal Numbering System (D-U-N-S) number is a unique, nine-digit
number assigned to every business location in the Dun & Bradstreet database
that has a unique, separate, and distinct operation. D-U-N-S numbers are used
by industries and organizations around the world as a global standard for business
identification and tracking. Maximum size is 9 characters.

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


Standard Objects DandBCompany

**Field Name** **Details**

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The total number of employees in the company, including all subsidiary and
branch locations. This data is only available on records that have a value of
_`Headquarters/Parent`_ in the `LocationStatus` field. Maximum size
is 15 characters.

```
EmployeesTotalReliability

FamilyMembers

Fax

FifthNaics

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


Standard Objects DandBCompany

**Field Name** **Details**

**Description**
An additional NAICS code used to further classify an organization by industry.
Maximum size is 6 characters.

```
FifthNaicsDesc

FifthSic

FifthSic8

FifthSic8Desc

FifthSicDesc

```

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
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

```
FipsMsaCode

FipsMsaDesc

FortuneRank

FourthNaics

FourthNaicsDesc

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Federal Information Processing Standards (FIPS) and the Metropolitan
Statistical Area (MSA) codes identify the organization’s location. The MSA codes
are defined by the US Office of Management and Budget. Maximum size is 5
characters.

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


Standard Objects DandBCompany

**Field Name** **Details**

**Description**
A brief description of an organization’s line of business, based on the
corresponding NAICS code. Maximum size is 120 characters.

```
FourthSic

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


Standard Objects DandBCompany

**Field Name** **Details**

**Description**
The level of accuracy of a location’s geographical coordinates compared with its
physical address. Available values include:

**•** A – _`Non-US rooftop accuracy`_

**•** B – _`Block level`_

**•** C – _`Places the address in the correct city`_

**•** D – _`Rooftop level`_

**•** I – _`Street intersection`_

**•** M – _`Mailing address level`_

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


Standard Objects DandBCompany

**Field Name** **Details**

**Description**
The total number of employees at the Global Ultimate, which is the highest entity
within an organization’s corporate structure and may oversee branches and
subsidiaries. Maximum size is 15 characters.

```
ImportExportAgent

IncludedInSnP500

Latitude

LegalStatus

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Identifies whether a business imports goods or services, exports goods or services,
and/or is an agent for goods. Available values include:

**•** A—Importer/exporter/agent

**•** B—Importer/exporter

**•** C—Importer

**•** D—Importer/agent

**•** E—Exporter/agent

**•** F—Agent (keeps no inventory and does not take title goods)

**•** G—None or data not available

**•** H—Exporter

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


Standard Objects DandBCompany

**Field Name** **Details**

**Description**
Identifies the legal structure of an organization.

```
LocationStatus

Longitude

MailingAddress

MailingCity

MailingCountry

```

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

**•** 2—Branch (secondary location to a headquarters location)

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


Standard Objects DandBCompany

**Field Name** **Details**

**Description**
The country where a company has its mail delivered. Maximum size is 40
characters.

```
MailingPostalCode

MailingState

MailingStreet

MarketingPreScreen

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code that a company uses on its mailing address. Maximum size is 20
characters.

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


Standard Objects DandBCompany

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
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Twenty-two distinct, mutually exclusive profiles, created as a result of cluster
analysis of Dun & Bradstreet data for US organizations.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether an organization is owned or controlled by a member of a
minority group. Available values include:

**•** Y—Minority owned

**•** N—Not minority owned

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


Standard Objects DandBCompany

**Field Name** **Details**

```
OutOfBusiness

OwnOrRent

ParentOrHqBusinessName

ParentOrHqDunsNumber

Phone

```

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

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates whether a company owns or rents the building it occupies. Available
values include:

**•** 0—Unknown or not applicable

**•** 1—Owns

**•** 2—Rents

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


Standard Objects DandBCompany

**Field Name** **Details**

**Description**
A company’s primary telephone number.

```
PostalCode

PremisesMeasure

PremisesMeasureReliability

PremisesMeasureUnit

PrimaryNaics

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code that corresponds to a company’s physical location. Maximum
size is 20 characters.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A numeric value for the measurement of the premises.

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


Standard Objects DandBCompany

**Field Name** **Details**

values can be found at the Optimizer Resources page maintained by Dun &
Bradstreet. Maximum size is 6 characters.

```
PrimaryNaicsDesc

PrimarySic

PrimarySic8

PrimarySic8Desc

PrimarySicDesc

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on its NAICS code.
Maximum size is 120 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The four-digit Standard Industrial Classification (SIC) code is used to categorize
business establishments by industry. The full list of values can be found at the
Optimizer Resources page maintained by Dun & Bradstreet. Maximum size is 4
characters.

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


Standard Objects DandBCompany

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of an organization’s line of business, based on its SIC code.
Maximum size is 80 characters.

```
PriorYearEmployees

PriorYearRevenue

PublicIndicator

SalesTurnoverGrowthRate

SalesVolume

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of employees for the prior year.

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


Standard Objects DandBCompany

**Field Name** **Details**

**Description**
The total annual sales revenue in the headquarters’ local currency. Dun &
Bradstreet tracks revenue data for publicly traded companies, Global Ultimates,
Domestic Ultimates, and some headquarters.

```
SalesVolumeReliability

SecondNaics

SecondNaicsDesc

SecondSic

SecondSic8

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The reliability of the `SalesVolume` figure. Available values include:

**•** 0—Actual number

**•** 1—Low

**•** 2—Estimated (for all records)

**•** 3—Modeled (for non-US records)

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


Standard Objects DandBCompany

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An additional SIC code used to further classify an organization by industry.
Maximum size is 8 characters.

```
SecondSic8Desc

SecondSicDesc

SixthNaics

SixthNaicsDesc

SixthSic

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
SixthSic8

SixthSic8Desc

SixthSicDesc

SmallBusiness

State

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
Indicates whether the company is designated a small business as defined by the
Small Business Administration of the US government. Available values include:

**•** Y—Small business site

**•** N—Not small business site

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


Standard Objects DandBCompany

**Field Name** **Details**

**Description**
The state where a company is physically located. Maximum size is 20 characters.

```
StockExchange

StockSymbol

Street

Subsidiary

ThirdNaics

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The corresponding exchange for a company’s stock symbol. For example: NASDAQ
or NYSE. Maximum size is 16 characters.

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


Standard Objects DandBCompany

**Field Name** **Details**

**Description**
An additional NAICS code used to further classify an organization by industry.
Maximum size is 6 characters.

```
ThirdNaicsDesc

ThirdSic

ThirdSic8

ThirdSic8Desc

ThirdSicDesc

```

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
A brief description of an organization’s line of business, based on the
corresponding SIC code. Maximum size is 80 characters.

```
TradeStyle1

TradeStyle2

TradeStyle3

TradeStyle4

TradeStyle5

URL

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A name, different from its legal name, that an organization may use for conducting
business. Similar to “Doing business as” or “DBA”. Maximum size is 255 characters.

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


### Standard Objects Dashboard

**Field Name** **Details**

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
An organization’s primary website address. Maximum size is 104 characters.

```
UsTaxId

WomenOwned

YearStarted

```

Usage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The identification number for the company used by the Internal Revenue Service
(IRS) in the administration of tax laws. Also referred to as Federal Taxpayer
Identification Number. Maximum size is 9 characters.

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


Standard Objects Dashboard

Supported Calls

`describeSObjects()`, `describeLayout()`, `query()`, `retrieve()`, `search()`

Fields

**Field** **Details**

```
BackgroundDirection

BackgroundEnd

BackgroundStart

ChartTheme

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


Standard Objects Dashboard

**Field** **Details**

```
ColorPalette

DashboardResultRefreshedDate

DashboardResultRunningUser

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Returns the color palette used for the dashboard.

Possible values are:

**•** `Default` —Default Palette

**•** `accessible` —Mineral(Accessible) Palette

**•** `bluegrass` —Branding Palette

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


Standard Objects Dashboard

**Field** **Details**

```
Description

DeveloperName

FolderId

FolderName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Returns the description of the dashboard. Limit: 255 characters.

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

[Note: This object stores event data that's queryable from platform APIs. For event data stored in event log files, see EventLogFile.](https://developer.salesforce.com/docs/atlas.en-us.262.0.object_reference.meta/object_reference/sforce_api_objects_eventlogfile.htm)

Supported Calls

`describeSObjects()`, `query()`

Special Access Rules

To access this object, you must have the View Event Log Object Data user permission.

Fields

**Field** **Details**

```
DmlType

FirstObjectIdentifier

KeyPrefix

LoginKey

```

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
